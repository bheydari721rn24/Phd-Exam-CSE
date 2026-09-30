"""Use semantic, consistently styled indices in rendered English lessons."""

from __future__ import annotations

import re


SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉₊₋ₙₖᵢ", "0123456789+-nki")
SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻ⁿʲᵏᵗᴺⁱ", "0123456789+-njktNi")
SCRIPT = re.compile(r"([A-Za-z0-9)|])([₀₁₂₃₄₅₆₇₈₉₊₋ₙₖᵢ]+|[⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻ⁿʲᵏᵗᴺⁱ]+)")

# These patterns operate on rendered HTML *text nodes*, never attributes, code,
# SVG, MathML, or an already-styled mathematical span. A bounded atom grammar
# deliberately avoids treating a whole English sentence as a formula.
SCRIPT_GLYPHS = "₀₁₂₃₄₅₆₇₈₉₊₋ₙₖᵢ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻ⁿʲᵏᵗᴺⁱ"
ATOM = rf"(?:\{{[^{{}}\n]{{1,70}}\}}|[A-Za-zΓΔΩΘℕℤℚℝ∅][A-Za-z]?[0-9_{SCRIPT_GLYPHS}]*(?:\([^()\n]{{0,50}}\))?|[0-9]+[A-Za-z]{{0,2}}[_{SCRIPT_GLYPHS}]*(?:\([^()\n]{{0,50}}\))?)"
OP = r"(?:[∈∉⊆⊊⊂⊃⊄∪∩∖△→↔⇒⇔↦≡⊨⊢∧∨⊕∣∤≤≥≠≈∼=+−×÷⋅/<>]|&lt;|&gt;)"
EXPRESSION = re.compile(rf"(?<![\w])(?:{ATOM})(?:[\s\u2009]*{OP}[\s\u2009]*(?:{ATOM}))+", re.UNICODE)
FUNCTION = re.compile(r"(?<![\w])(?:[A-Za-z]|Var|Even|Odd|Dom|Pow|Pr|rank|card|gcd|ceil|floor|max|min|log|len|size|cost)\([^()\n]{1,45}\)")
NUMBER_PRODUCT = re.compile(rf"(?<![\w.])[0-9]+[A-Za-z]{{1,2}}[_{SCRIPT_GLYPHS}]*(?![A-Za-z0-9])")
RADICAL_PRODUCT = re.compile(r"(?<![\w.])[0-9]+√")
PAREN_PRODUCT = re.compile(r"\([a-z]{2}\)")
PAREN_POWER = re.compile(rf"\([^()\n]{{1,60}}\)[{SCRIPT_GLYPHS}]+")
ABS = re.compile(rf"\|[^|\n]{{1,60}}\|[{SCRIPT_GLYPHS}]*")
QUANTIFIED = re.compile(r"[∀∃][A-Za-z](?:[\s\u2009]*[∈∉][\s\u2009]*[A-Za-zℕℤℚℝ])?")
MATH_GLYPH = re.compile(r"[¬∧∨⊕→↔⇒⇔↦↑∀∃∈∉⊆⊊⊂⊃⊄∪∩⋃⋂∖△∅ℕℤℚℝ℘Α-Ωα-ω∞≡⊨⊢∑∏≤≥≠≈∼∣∤×÷⋅√∝⋯−=+|]|&lt;|&gt;")
SINGLE_VARIABLE = re.compile(rf"(?<![A-Za-z0-9'’/.-])(?:[b-zB-Z])(?![A-Za-z0-9'’/{SCRIPT_GLYPHS}])")
LIST_MARKER = re.compile(r"\(([a-d])\)(?=\s+[A-Za-z])")
FORMULA_A = re.compile(r"(?<![A-Za-z0-9'’/.-])A(?=\s+(?:is|and|or|has|be|true|false|holds|belongs|exactly|mean|means|fails|changes|are|would)\b|\s*[,;:.=+−×÷∈⊆∪∩∖△⊂⊃⊄→↔⇒⇔≡⊨⊢≤≥≠≈∣∤∧∨⊕◦)\]}])")
FORMULA_A_CONTEXT = re.compile(r"(?i:\b(?:of|to|from|with|every|each|all|let|if|satisfying|subset|member|members|belongs|meaning|take))\s+(A)\b")
FORMULA_a = re.compile(r"(?<![A-Za-z0-9'’/.-])a(?=\s*[,;:.=+−×÷∈⊆∪∩∖△⊂⊃⊄→↔⇒⇔≡⊨⊢≤≥≠≈∣∤∧∨⊕◦}\]])")
TRAILING_BASE = re.compile(r"(?<![A-Za-z0-9'’/.-])[A-Za-z](?=\s*$)")
MATH_CONTEXT_VARIABLE = re.compile(
    rf"(?i:\b(?:variable|variables|integer|integers|element|elements|predicate|function|value|values|witness|parameter|parameters|constant|constants|peg|vertex|node|region|atom|premise|family))\s+([A-Za-z])\b(?![{SCRIPT_GLYPHS}])"
    rf"|(?i:\b(?:set|sets|domain|formula|formulas|property|case))\s+([A-Z])\b(?![{SCRIPT_GLYPHS}])"
)


def _replace(match: re.Match[str], *, wrap: bool) -> str:
    base, script = match.groups()
    if script[0] in "₀₁₂₃₄₅₆₇₈₉₊₋ₙₖᵢ":
        tag, value = "sub", script.translate(SUB)
    else:
        tag, value = "sup", script.translate(SUP)
    rendered = f"{base}<{tag}>{value}</{tag}>"
    return f'<span class="math-inline">{rendered}</span>' if wrap else rendered


def normalize_scripts(body: str) -> str:
    """Replace Unicode small index glyphs in text, leaving markup/SVG/code intact."""
    parts = re.split(r"(<[^>]+>)", body)
    stack: list[tuple[str, bool]] = []
    excluded = {"svg", "math", "script", "style", "code", "pre"}
    void = {"br", "hr", "img", "input", "meta", "link", "wbr"}
    for i, part in enumerate(parts):
        if i % 2:
            opening = re.match(r"<([A-Za-z][\w:-]*)\b", part)
            closing = re.match(r"</([A-Za-z][\w:-]*)\b", part)
            if opening:
                tag = opening.group(1)
                if tag not in void and not part.endswith("/>"):
                    styled = (tag == "span" and 'class="math-inline"' in part) or (
                        tag == "div" and 'class="formula-block' in part
                    )
                    stack.append((tag, styled))
            elif closing:
                tag = closing.group(1)
                for j in range(len(stack) - 1, -1, -1):
                    if stack[j][0] == tag:
                        del stack[j:]
                        break
            continue
        if not any(tag in excluded for tag, _ in stack):
            styled = any(is_math for _, is_math in stack)
            parts[i] = SCRIPT.sub(lambda m: _replace(m, wrap=not styled), part)
    return "".join(parts)


def _math_text(text: str, *, before_script: bool = False, table_cell: bool = False) -> str:
    spans: list[tuple[int, int]] = []
    list_markers = {m.start(1) for m in LIST_MARKER.finditer(text)}
    for pattern in (EXPRESSION, FUNCTION, NUMBER_PRODUCT, RADICAL_PRODUCT, PAREN_PRODUCT, PAREN_POWER, ABS, QUANTIFIED, MATH_GLYPH, SINGLE_VARIABLE, FORMULA_A, FORMULA_a):
        spans.extend((m.start(), m.end()) for m in pattern.finditer(text))
    if before_script:
        spans.extend((m.start(), m.end()) for m in TRAILING_BASE.finditer(text))
    if table_cell and text.strip() == "A":
        start = text.index("A")
        spans.append((start, start + 1))
    spans = [(start, end) for start, end in spans if start not in list_markers]
    for match in MATH_CONTEXT_VARIABLE.finditer(text):
        spans.append(match.span(1 if match.group(1) else 2))
    spans.extend(match.span(1) for match in FORMULA_A_CONTEXT.finditer(text))
    if not spans:
        return text
    spans.sort()
    merged: list[list[int]] = []
    for start, end in spans:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    out = []
    previous = 0
    for start, end in merged:
        out.append(text[previous:start])
        out.append(f'<span class="math-inline">{text[start:end]}</span>')
        previous = end
    out.append(text[previous:])
    return "".join(out)


def normalize_math(body: str) -> str:
    """Set formulas and mathematical glyphs in the chapter's distinct math face."""
    parts = re.split(r"(<[^>]+>)", body)
    stack: list[tuple[str, bool]] = []
    void = {"br", "hr", "img", "input", "meta", "link", "wbr"}
    excluded = {"svg", "math", "script", "style", "code", "pre", "a"}
    for i, part in enumerate(parts):
        if i % 2:
            opening = re.match(r"<([A-Za-z][\w:-]*)\b", part)
            closing = re.match(r"</([A-Za-z][\w:-]*)\b", part)
            if opening:
                tag = opening.group(1)
                if tag not in void and not part.endswith("/>"):
                    styled = (tag == "span" and 'class="math-inline"' in part) or (
                        tag == "div" and 'class="formula-block' in part
                    )
                    stack.append((tag, styled))
            elif closing:
                tag = closing.group(1)
                for j in range(len(stack) - 1, -1, -1):
                    if stack[j][0] == tag:
                        del stack[j:]
                        break
            continue
        if not any(tag in excluded or styled for tag, styled in stack):
            following = parts[i + 1] if i + 1 < len(parts) else ""
            parts[i] = _math_text(
                part,
                before_script=bool(re.match(r"<(?:sub|sup)\b", following)),
                table_cell=any(tag in {"td", "th"} for tag, _ in stack),
            )
    return "".join(parts)
