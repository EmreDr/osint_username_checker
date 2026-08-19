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
        "url": "https://www.instagram.com/{username}/",
        "found_codes": [200],
        "not_found_codes": [404],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [429],
        "follow_redirects": True
    } ,
    "X": {
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
    },
    "YouTube": {
        "url": "https://www.youtube.com/@{username}",
        "found_codes": [200],
        "not_found_codes": [404],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [429]
    },
    "Twitch": {
        "url": "https://www.twitch.tv/{username}",
        "found_codes": [200],
        "not_found_codes": [404],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [409]
    },
    "SoundCloud": {
        "url": "https://soundcloud.com/{username}",
        "found_codes": [200],
        "not_found_codes": [404],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [409]
    },
    "Vimeo": {
        "url": "https://vimeo.com/{username}",
        "found_codes": [200],
        "not_found_codes": [404],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [429]
    },
    "DeviantArt": {
        "url": "https://www.deviantart.com/{username}",
        "found_codes": [200],
        "not_found_codes": [404],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [409]
    },
    "Behance": {
        "url": "https://www.behance.net/{username}",
        "found_codes": [200],
        "not_found_codes": [404],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [429]
    },
    "Dribbble": {
        "url": "https://dribbble.com/{username}",
        "found_codes": [200],
        "not_found_codes": [404],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [429]
    },
    "DevTo": {
        "url": "https://dev.to/{username}",
        "found_codes": [200],
        "not_found_codes": [404],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [429]
    },
    "Linktree": {
        "url": "https://linktr.ee/{username}",
        "found_codes": [200],
        "not_found_codes": [404],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [429]
    },
    "Patreon": {
        "url": "https://www.patreon.com/{username}",
        "found_codes": [200],
        "not_found_codes": [404],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [429]
    },
    "Steam": {
        "url": "https://steamcommunity.com/id/{username}",
        "found_codes": [200],
        "not_found_codes": [404],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [429]
    },
    "Telegram": {
        "url": "https://t.me/{username}",
        "found_codes": [200],
        "not_found_codes": [404],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [429]
    },
    "GitLab": {
        "url": "https://gitlab.com/{username}",
        "found_codes": [200],
        "not_found_codes": [404],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [429]
    },
    "Replit": {
        "url": "https://replit.com/@{username}",
        "found_codes": [200],
        "not_found_codes": [404],
        "redirect_codes": [301, 302, 307, 308],
        "blocked_codes": [403, 429],
        "rate_limited_codes": [429]
    }

}