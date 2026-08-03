import asyncio
import aiohttp
from platforms import PLATFORMS

TIMEOUT_SECONDS = 8
MAX_CONCURRENT_REQUESTS = 5
RETRY_ATTEMPTS = 3
RETRY_BACKOFF_SECONDS = 1.5
SUSPICIOUS_MARKERS = [
    "client challenge",
    "just a moment",
    "cf-browser-verification",
    "attention required",
    "access denied",
    "are you a robot",
    "enable javascript",
]
def classify_state(cfg: dict, status_code: int, body: str = "") -> str:
    if status_code in cfg["found_codes"]:
        lowered = body.lower()
        if any(marker in lowered for marker in SUSPICIOUS_MARKERS):
            return "uncertain"
        return "found"

    if status_code in cfg["not_found_codes"]:
        return "not_found"

    if status_code in cfg["redirect_codes"]:
        return "redirect"

    if status_code in cfg["rate_limited_codes"]:
        return "rate_limited"

    if status_code in cfg["blocked_codes"]:
        return "blocked"

    return "uncertain"


async def check_variant_on_platform(session, semaphore, variant: str, platform: str, cfg: dict) -> dict:
    url = cfg["url"].format(username=variant)

    async with semaphore:
        last_error = None

        for attempt in range(1, RETRY_ATTEMPTS + 1):
            try:
                timeout = aiohttp.ClientTimeout(total=TIMEOUT_SECONDS)
                async with session.get(url, timeout=timeout, allow_redirects=False) as response:
                    status_code = response.status
                    body = await response.text()
                    state = classify_state(cfg, status_code, body[:3000])
                return {
                    "platform": platform,
                    "variant": variant,
                    "url": url,
                    "http_status": status_code,
                    "state": state,
                    "found": state == "found",
                    "attempts": attempt,
                    "error": None,
                }

            except (aiohttp.ClientError, asyncio.TimeoutError) as exc:
                last_error = str(exc) or type(exc).__name__
                if attempt < RETRY_ATTEMPTS:
                    await asyncio.sleep(RETRY_BACKOFF_SECONDS * attempt)
    return {
        "platform": platform,
        "variant": variant,
        "url": url,
        "http_status": None,
        "state": "uncertain",
        "found": False,
        "attempts": RETRY_ATTEMPTS,
        "error": last_error,
    }


async def check_all_platforms(variants: list) -> list:
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

    async with aiohttp.ClientSession() as session:
        tasks = [
            check_variant_on_platform(session, semaphore, variant, platform, cfg)
            for variant in variants
            for platform, cfg in PLATFORMS.items()
        ]
        results = await asyncio.gather(*tasks)

    return list(results)