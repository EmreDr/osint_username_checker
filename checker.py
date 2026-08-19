import asyncio
import aiohttp
from typing import List
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

NOT_FOUND_MARKERS: List[str] = [
    "sorry, this page isn't available",
    "this page isn't available",
    "bu sayfaya ulaşılamıyor",
    "sayfa kaldırılmış olabilir",
    "the link you followed may be broken",
    "bu içerik şu anda kullanılamıyor",
    "this content isn't available right now",
    "the specified profile could not be found",
    "error: no user found",
    "no user was found with this custom url",
    "bu profil bulunamadı",
    "sorry, this user doesn't seem to exist",
    "this user doesn't seem to exist",
    "uh oh! the page you were looking for could not be found",
    "this user does not exist",
    "the page you are looking for could not be found",
    "the page you are looking for does not exist",
    "the page you were looking for doesn't exist",
    "the page you're looking for doesn't exist",
    "the page you requested could not be found",
    "the page could not be found or you don't have permission",
    "has left deviantart",
    "this channel doesn't exist",
    "channel not found",
    "sorry. unless you've got a time machine",
    "this is not the page you're looking for",
    "this is not the web page you are looking for",
    "sorry! we couldn't find that page",
    "sorry, we couldn't find that page",
    "sorry, we couldn't find that",
    "sorry, we can't find that page",
    "sorry, nobody on reddit goes by that name",
    "we couldn't find that page",
    "we can't find that page",
    "we can't find the page",
    "we can't find that user",
    "we can't find this page",
    "we can't find that repl",
    "this page doesn't exist",
    "this page is unavailable",
    "this page is not available",
    "this account doesn't exist",
    "this blog doesn't exist",
    "this linktree does not exist",
    "this creator doesn't exist",
    "this portfolio does not exist",
    "this pen doesn't exist",
    "this user could not be found",
    "there doesn't seem to be anything here",
    "there is no last.fm user with that name",
    "oops! this page doesn't exist",
    "oops! this page isn't here",
    "oh snap! you found a page that doesn't exist",
    "profile not found",
    "account not found",
    "user not found",
    "page not found",
    "that handle can't be found",
    "couldn't find that user",
    "no such user",
    "invalid username",
    "bu sayfa mevcut değil",
]
def classify_state(cfg: dict, status_code: int, body: str = "") -> str:
    if status_code in cfg["found_codes"]:
        lowered = body.lower()
        if any(marker in lowered for marker in SUSPICIOUS_MARKERS):
            return "uncertain"
        if any(marker in lowered for marker in NOT_FOUND_MARKERS):
            return "not_found"
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
                async with session.get(url, timeout=timeout, allow_redirects=cfg.get("follow_redirects", False)) as response:
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