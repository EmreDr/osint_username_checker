import json
from pathlib import Path
from typing import Dict, List, Optional

# Template placeholders: {first}, {last}, {f} (first initial), {l} (last initial), {initials}
PATTERNS: Dict[str, str] = {
    "first":        "{first}",
    "last":         "{last}",
    "firstlast":    "{first}{last}",
    "lastfirst":    "{last}{first}",
    "first.last":   "{first}.{last}",
    "last.first":   "{last}.{first}",
    "first_last":   "{first}_{last}",
    "first-last":   "{first}-{last}",
    "flast":        "{f}{last}",
    "lfirst":       "{l}{first}",
    "initialslast": "{initials}{last}",
    "initials":     "{initials}",
}

DEFAULT_NUMBER_SUFFIXES = ["0", "official","_"]

FORMATS_CONFIG_PATH = Path(__file__).resolve().parent / "formats.json"


def _load_patterns() -> Dict[str, str]:
    if FORMATS_CONFIG_PATH.exists():
        return json.loads(FORMATS_CONFIG_PATH.read_text(encoding="utf-8"))
    return PATTERNS


def _build_context(parts: List[str]) -> Dict[str, str]:
    return {
        "first":    parts[0],
        "last":     parts[-1],
        "f":        parts[0][:1],
        "l":        parts[-1][:1],
        "initials": "".join(p[0] for p in parts),
    }


def _needs_multiple_parts(template: str) -> bool:
    return any(key in template for key in ["{last}", "{l}", "{initials}"])


def _render_pattern(template: str, ctx: Dict[str, str]) -> Optional[str]:
    try:
        return template.format(**ctx)
    except KeyError:
        return None


def _dedupe_preserve_order(items: List[str]) -> List[str]:
    seen = set()
    out = []
    for item in items:
        if item and item not in seen:
            seen.add(item)
            out.append(item)
    return out


def _apply_number_suffixes(variants: List[str], numbers: List[str]) -> List[str]:
    if not numbers:
        return variants
    result = []
    for v in variants:
        result.append(v)
        for n in numbers:
            result.append(f"{v}{n}")
    return result


def generate_variants(
    full_name: str,
    formats: List[str] = None,
    number_suffixes: List[str] = None,
    include_numbers: bool = True,
) -> List[str]:
    parts = [p.lower() for p in full_name.strip().split() if p]
    if not parts:
        return []

    is_single_word = len(parts) == 1
    ctx = _build_context(parts)

    active_patterns = _load_patterns()
    if formats is not None:
        active_patterns = {k: v for k, v in active_patterns.items() if k in formats}

    if number_suffixes is None and include_numbers:
        number_suffixes = DEFAULT_NUMBER_SUFFIXES
    elif not include_numbers:
        number_suffixes = None

    base_variants = []
    for name, template in active_patterns.items():
        if is_single_word and _needs_multiple_parts(template):
            continue
        rendered = _render_pattern(template, ctx)
        if rendered:
            base_variants.append(rendered)

    base_variants = _dedupe_preserve_order(base_variants)
    final_variants = _apply_number_suffixes(base_variants, number_suffixes)

    return sorted(set(final_variants))