

PLATFORMS = {

    "github" : {
        "url" : "https://github.com/{username}",
        "found_codes" : [200],
        "not_found_codes" : [404],
        "redirect_codes" : [301,302,307,308],
        "blocked_codes" : [403,429],
        "rate_limited_codes" : [409]
    } ,
    "instagram": {
        "url": "https://instagram.com/{username}",
        "found_codes": [200],
        "not_found_codes": [404],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [409]
    } ,
    "X(new twitter)": {
        "url": "https://x.com/{username}",
        "found_codes": [200,201],
        "not_found_codes": [404,410],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [409]
    } , #Actually there was a TikTok here, but it kept giving an error every time.
    "Reddit": {
        "url": "https://www.reddit.com/user/{username}",
        "found_codes": [200],
        "not_found_codes": [404],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [409]
    },
    "Pinterest": {
        "url": "https://www.pinterest.com/{username}",
        "found_codes": [200],
        "not_found_codes": [404],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [409]
    },
    "Medium": {
        "url": "https://medium.com/@{username}",
        "found_codes": [200,201,204],
        "not_found_codes": [404],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [409]
    }
}