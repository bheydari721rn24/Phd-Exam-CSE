"""Render the reviewed vector-geometry chapter through shared math typography."""
from __future__ import annotations

import json
import re
from html import escape
from pathlib import Path

from markdown_it import MarkdownIt
from math_typography import normalize_math, normalize_scripts

ROOT = Path(__file__).resolve().parents[1]
source = "\n\n".join((ROOT / "research" / name).read_text(encoding="utf-8") for name in
    ("l_vectors.en.md", "l_vectors-problems.en.md", "l_vectors-review.en.md"))
assert not re.search(r"[\u0600-\u06ff]", source)
assert source.count("### Problem ") == 34
source = source.replace("ⱼ", "<sub>j</sub>").replace("ᵀ", "<sup>T</sup>")
source = source.replace("ℝⁿ", "ℝ<sup>n</sup>").replace("‖₁", "‖<sub>1</sub>")
source = source.replace("²", "<sup>2</sup>").replace("³", "<sup>3</sup>")
# Resolve indices before wrapping new norm/angle delimiters into styled spans.
source = normalize_scripts(source)
body = MarkdownIt("commonmark", {"html": True}).enable("table").render(source)

def index_math(text: str) -> str:
    tokens = re.findall(r"[A-Za-z]+|\d+|.", text.replace("&lt;", "<"))
    return "<mrow>" + "".join(
        f'<{"mn" if t.isdigit() else "mi" if t.isalpha() else "mo"}>{escape(t)}</{"mn" if t.isdigit() else "mi" if t.isalpha() else "mo"}>'
        for t in tokens
    ) + "</mrow>"

def operator_limits(match: re.Match[str]) -> str:
    operator, lower, upper = match.groups()
    tag = "munderover" if upper else "munder"
    args = index_math(lower) + (index_math(upper) if upper else "")
    return f'<math class="math-limits"><{tag}><mo largeop="true">{operator}</mo>{args}</{tag}></math>'

body = re.sub(r"([∑∏∫])<sub>([^<>]+)</sub>(?:<sup>([^<>]+)</sup>)?", operator_limits, body)
body = re.sub(r"<mo>([()])</mo>", r'<mo stretchy="false">\1</mo>', body)
# Extend the shared glyph treatment only for this chapter's new notation.
# Operate on text nodes, excluding existing math, SVG, code, scripts, and links.
parts = re.split(r"(<[^>]+>)", body)
stack = []
void = {"input", "br", "hr", "img", "meta", "link", "wbr"}
for i, part in enumerate(parts):
    if i % 2:
        start = re.match(r"<([\w:-]+)\b", part)
        end = re.match(r"</([\w:-]+)\b", part)
        if start and start[1] not in void:
            stack.append((start[1], "math-inline" in part or "formula-block" in part))
        elif end:
            for j in range(len(stack)-1, -1, -1):
                if stack[j][0] == end[1]:
                    del stack[j:]
                    break
    elif not any(t in {"math", "svg", "code", "pre", "script", "style", "a"} or styled for t, styled in stack):
        parts[i] = re.sub(r"[⟨⟩‖⊥ℂᵀ∫]", lambda m: f'<span class="math-inline">{m[0]}</span>', part)
body = normalize_scripts(normalize_math("".join(parts)))
anchors = ["sources", "vectors", "span", "norms", "inner-products", "projection", "orthonormal", "affine", "cross-product", "laboratory", "worked-problems", "quick-reference", "references"]
labels = ["Scope and sources", "Vectors", "Span and bases", "Norms and angles", "Inner products", "Projection", "Gram–Schmidt", "Affine distances", "Area and volume", "Laboratory", "Worked problems", "Key points", "References"]
count = 0
def add_id(match: re.Match[str]) -> str:
    global count
    result = f'<h2 id="{anchors[count]}">{match.group(1)}</h2>'
    count += 1
    return result
body = re.sub(r"<h2>(.*?)</h2>", add_id, body)
assert count == len(anchors)
nav = " ".join(f'<a href="#{key}">{label}</a>' for key, label in zip(anchors, labels))
html = f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Vectors and inner products: four reviewed university courses, rigorous proofs, 34 fully worked problems, a projection laboratory, and a detailed examination review.">
<title>Vectors, Inner Products, and Linear Geometry · Doctoral CSE 1406</title>
<link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="l_vectors.css">
<script src="l_vectors-lab.js" defer></script>
</head><body><main class="chapter">
<div class="top-link"><a href="../index.html#library">← Back to the chapter library</a></div>
<header class="hero"><p class="eyebrow">Linear Algebra · Chapter 1</p>
<h1>Vectors, Inner Products, and Linear Geometry</h1>
<p>Review draft · four reviewed university courses · 34 fully worked problems</p></header>
<nav class="toc" aria-label="Chapter contents">{nav}</nav>
<article class="lesson">{body}</article>
<p class="top-link"><a href="../index.html#library">← Back to the chapter library</a></p>
</main></body></html>'''
(ROOT / "dist/chapters/l_vectors.html").write_text(html, encoding="utf-8")
path = ROOT / "dist/lessons.json"
lessons = json.loads(path.read_text(encoding="utf-8"))
chapter = next(c for w in lessons for c in w["chapters"] if c["topicId"] == "l_vectors")
chapter.update(url="chapters/l_vectors.html")
path.write_text(json.dumps(lessons, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
path = ROOT / "dist/course-audit-week1.en.json"
register = json.loads(path.read_text(encoding="utf-8"))
reviewed = json.loads((ROOT / "research/l_vectors-reviewed-courses.json").read_text(encoding="utf-8"))
ids = {c["id"] for c in reviewed}
register["courses"] = [c for c in register["courses"] if c["id"] not in ids]+reviewed
register["reviewedAt"] = "2026-10-01"
path.write_text(json.dumps(register, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
print(f"Rendered {len(source.split())} manuscript words; 34 fully worked problems; 13 sections.")
