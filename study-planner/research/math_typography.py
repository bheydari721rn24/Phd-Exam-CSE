"""Use semantic, consistently styled indices in rendered English lessons."""

from __future__ import annotations

import re


SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉₊₋ₙₖᵢ", "0123456789+-nki")
SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻ⁿʲᵏᵗᴺⁱ", "0123456789+-njktNi")
SCRIPT = re.compile(r"([A-Za-z0-9)|])([₀₁₂₃₄₅₆₇₈₉₊₋ₙₖᵢ]+|[⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻ⁿʲᵏᵗᴺⁱ]+)")


def _replace(match: re.Match[str]) -> str:
    base, script = match.groups()
    if script[0] in "₀₁₂₃₄₅₆₇₈₉₊₋ₙₖᵢ":
        tag, value = "sub", script.translate(SUB)
    else:
        tag, value = "sup", script.translate(SUP)
    return f'<span class="math-inline">{base}<{tag}>{value}</{tag}></span>'


def normalize_scripts(body: str) -> str:
    """Replace Unicode small index glyphs in text, leaving markup/SVG/code intact."""
    parts = re.split(r"(<[^>]+>)", body)
    excluded = {"svg": 0, "math": 0, "script": 0, "style": 0, "code": 0, "pre": 0}
    for i, part in enumerate(parts):
        if i % 2:
            open_match = re.match(r"<([A-Za-z][\w:-]*)\b", part)
            close_match = re.match(r"</([A-Za-z][\w:-]*)\b", part)
            if open_match and open_match.group(1) in excluded:
                excluded[open_match.group(1)] += 1
            elif close_match and close_match.group(1) in excluded:
                excluded[close_match.group(1)] -= 1
                assert excluded[close_match.group(1)] >= 0
            continue
        if not any(excluded.values()):
            parts[i] = SCRIPT.sub(_replace, part)
    assert not any(excluded.values())
    return "".join(parts)
