"""Render the reviewed counting/independence chapter and original worked bank."""
from __future__ import annotations

import json
import re
from html import escape
from pathlib import Path

from markdown_it import MarkdownIt
from math_typography import normalize_math, normalize_scripts

ROOT = Path(__file__).resolve().parents[1]
source = "\n\n".join((ROOT / "research" / name).read_text(encoding="utf-8") for name in
    ("s_counting.en.md", "s_counting-models.en.md", "s_counting-problems.en.md"))
source = source.replace("ᵍ", "<sup>g</sup>").replace("ᵐ", "<sup>m</sup>")
assert not re.search(r"[\u0600-\u06ff]", source)
assert source.count("### Problem ") == 34
body = MarkdownIt("commonmark", {"html": True}).enable("table").render(source)
# A summation's upper/lower bounds belong to the operator, not to two
# consecutive text offsets. MathML preserves this geometry in print and screen.
def index_math(text: str) -> str:
    tokens = re.findall(r"[A-Za-z]+|\d+|.", text)
    return "<mrow>" + "".join(
        f'<{"mn" if token.isdigit() else "mi" if token.isalpha() else "mo"}>{escape(token)}</{"mn" if token.isdigit() else "mi" if token.isalpha() else "mo"}>'
        for token in tokens
    ) + "</mrow>"

def operator_limits(match: re.Match[str]) -> str:
    operator, lower, upper = match.groups()
    tag = "munderover" if upper else "munder"
    args = index_math(lower) + (index_math(upper) if upper else "")
    return f'<math class="sum-limits"><{tag}><mo largeop="true">{operator}</mo>{args}</{tag}></math>'

body = re.sub(r"([∑∏])<sub>([^<>]+)</sub>(?:<sup>([^<>]+)</sup>)?", operator_limits, body)
anchors = ["sources", "principles", "selections", "constraints", "identities", "probabilities", "independence", "laboratory", "worked-problems", "quick-reference", "references"]
labels = ["Scope and sources", "Counting rules", "Selections", "Constraints", "Identities", "Probability models", "Independence", "Laboratory", "Worked problems", "Key points", "References"]
count = 0

def add_id(match: re.Match[str]) -> str:
    global count
    result = f'<h2 id="{anchors[count]}">{match.group(1)}</h2>'
    count += 1
    return result

body = re.sub(r"<h2>(.*?)</h2>", add_id, body)
assert count == len(anchors)
body = normalize_scripts(normalize_math(body))
nav = " ".join(f'<a href="#{key}">{label}</a>' for key, label in zip(anchors, labels))
html = f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Counting probabilities and independence: four reviewed university courses, rigorous derivations, 34 fully worked problems, exact parity laboratory, and a detailed decision-oriented review.">
<title>Counting Probabilities and Independence · Doctoral CSE 1406</title>
<link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="s_counting.css">
<script src="s_counting-lab.js" defer></script>
</head><body><main class="chapter">
<div class="top-link"><a href="../index.html#library">← Back to the chapter library</a></div>
<header class="hero"><p class="eyebrow">Probability and Statistics · Chapter 2</p>
<h1>Counting Probabilities and Independence</h1>
<p>Approved chapter · four reviewed university courses · 34 fully worked problems</p></header>
<nav class="toc" aria-label="Chapter contents">{nav}</nav>
<article class="lesson">{body}</article>
<p class="top-link"><a href="../index.html#library">← Back to the chapter library</a></p>
</main></body></html>'''
(ROOT / "dist" / "chapters" / "s_counting.html").write_text(html, encoding="utf-8")
lessons_path = ROOT / "dist" / "lessons.json"
lessons = json.loads(lessons_path.read_text(encoding="utf-8"))
chapter = next(c for w in lessons for c in w["chapters"] if c["topicId"] == "s_counting")
chapter.update(url="chapters/s_counting.html")
lessons_path.write_text(json.dumps(lessons, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
register_path = ROOT / "dist" / "course-audit-week1.en.json"
register = json.loads(register_path.read_text(encoding="utf-8"))
reviewed = json.loads((ROOT / "research" / "s_counting-reviewed-courses.json").read_text(encoding="utf-8"))
reviewed_ids = {item["id"] for item in reviewed}
register["courses"] = [item for item in register["courses"] if item["id"] not in reviewed_ids] + reviewed
register["reviewedAt"] = "2026-10-01"
register_path.write_text(json.dumps(register, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Rendered {len(source.split())} manuscript words; 34 fully worked problems; 11 sections.")
