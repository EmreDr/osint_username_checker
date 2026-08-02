import requests
from platforms import PLATFORMS

TIMEOUT_SECONDS = 8


def classify_state(cfg: dict, status_code: int) -> str:
    if status_code in cfg["found_codes"]:
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


def check_variant_on_platform(variant: str, platform: str, cfg: dict) -> dict:
    url = cfg["url"].format(username=variant)
    try:
        response = requests.get(url, timeout=TIMEOUT_SECONDS, allow_redirects=False)
        status_code = response.status_code
        state = classify_state(cfg, status_code)
    except requests.RequestException:
        status_code = None
        state = "uncertain"

    return {
        "platform": platform,
        "variant": variant,
        "url": url,
        "http_status": status_code,
        "state": state,
        "found": state == "found",
    }


def check_all_platforms(variants: list) -> list:
    results = []
    for variant in variants:
        for platform, cfg in PLATFORMS.items():
            results.append(check_variant_on_platform(variant, platform, cfg))
    return results