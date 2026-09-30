"""Render the source-audited computation-model manuscript as an English draft."""

from __future__ import annotations

import re
from pathlib import Path

from markdown_it import MarkdownIt
from math_typography import normalize_math, normalize_scripts


ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "research" / "a_model.en.md").read_text(encoding="utf-8")
assert not re.search(r"[\u0600-\u06ff]", source)
assert source.count("### Problem ") == 16
assert "## 9. High-yield review" in source
body = MarkdownIt("commonmark", {"html": True}).enable("table").render(source)
anchors = [
    "sources", "problem-contract", "input-size", "word-ram", "restricted-models",
    "numeric-parameters", "lower-bounds", "worked-problems", "quick-reference", "references",
]
labels = [
    "Sources", "Problem contract", "Input size", "Word-RAM", "Restricted models",
    "Numeric values", "Lower bounds", "Worked problems", "Key points", "References",
]
count = 0


def add_id(match: re.Match[str]) -> str:
    global count
    assert count < len(anchors)
    result = f'<h2 id="{anchors[count]}">{match.group(1)}</h2>'
    count += 1
    return result


body = re.sub(r"<h2>(.*?)</h2>", add_id, body)
assert count == len(anchors)
body = normalize_scripts(normalize_math(body))
nav = " ".join(f'<a href="#{key}">{label}</a>' for key, label in zip(anchors, labels))
html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Computation models and input size, with rigorous cost conventions, diagrams, 14 solved problems, and a precise review sheet.">
  <title>Computation Models and Input Size · Doctoral CSE 1406</title>
  <link rel="stylesheet" href="chapter.en.css">
  <style>@media print {{.lesson{{font-size:.92rem;line-height:1.44}}}}</style>
</head>
<body>
<main class="chapter">
  <div class="top-link"><a href="../index.html#week-1">← Back to the weekly plan</a></div>
  <header class="hero">
    <p class="eyebrow">Data Structures and Algorithms · Chapter 1</p>
    <h1>Computation Models and Input Size</h1>
    <p>Review draft · five reviewed university course texts · 16 fully worked problems</p>
  </header>
  <nav class="toc" aria-label="Chapter contents">{nav}</nav>
  <article class="lesson">{body}</article>
  <p class="top-link"><a href="../index.html#week-1">← Back to the weekly plan</a></p>
</main>
</body>
</html>
'''
(ROOT / "dist" / "chapters" / "a_model.html").write_text(html, encoding="utf-8")
print(f"Rendered {len(source.split())} manuscript words into a_model.html")
