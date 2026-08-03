from typing import List

SEPARATOR = ["",".",",","-","_"]
SUFFIXIES = ["" , "0" , "real", "official",]

def _base_candidates(parts : list) -> list:
    first, last = parts[0], parts[-1]
    initials = "".join(p[0] for p in parts)

    bases = [first + last, last + first, initials + last]
    return bases

    for sep in SEPARATORS:
        bases.append(f"{first}{sep}{last}")
        bases.append(f"{last}{sep}{first}")

    return bases


def generate_variants(full_name: str) -> List[str]:
    parts = [p.lower() for p in full_name.strip().split() if p]
    if not parts:
        return []

    bases = set(_base_candidates(parts))

    variants = set()
    for base in bases:
        for prefix in SUFFIXIES:
            for suffix in SUFFIXIES:
                variants.add(prefix + base + suffix)

    return sorted(variants)