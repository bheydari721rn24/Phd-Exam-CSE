"""Render the source-audited asymptotic-analysis manuscript as an English draft."""

from __future__ import annotations

import re
from pathlib import Path

from markdown_it import MarkdownIt
from math_typography import normalize_math, normalize_scripts


ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "research" / "a_asym.en.md").read_text(encoding="utf-8")
assert not re.search(r"[\u0600-\u06ff]", source)
assert source.count("### Problem ") == 18
assert "## 7. High-yield review" in source
body = MarkdownIt("commonmark", {"html": True}).enable("table").render(source)
anchors = [
    "sources", "contract", "definitions", "growth", "algebra",
    "worked-problems", "quick-reference", "references",
]
labels = [
    "Sources", "Complexity contract", "Definitions and proof", "Growth classes",
    "Algebra and traps", "Worked problems", "Key points", "References",
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
  <meta name="description" content="Asymptotic notation and growth comparison, with four reviewed university courses, proofs, diagrams, 18 worked problems, and a high-yield review.">
  <title>Asymptotic Notation and Growth Comparison · Doctoral CSE 1406</title>
  <link rel="stylesheet" href="chapter.en.css">
  <style>@media print {{.lesson{{font-size:.92rem;line-height:1.44}}}}</style>
</head>
<body>
<main class="chapter">
  <div class="top-link"><a href="../index.html#week-1">← Back to the weekly plan</a></div>
  <header class="hero">
    <p class="eyebrow">Data Structures and Algorithms · Chapter 2</p>
    <h1>Asymptotic Notation and Growth Comparison</h1>
    <p>Review draft · four reviewed university course texts · 18 fully worked problems</p>
  </header>
  <nav class="toc" aria-label="Chapter contents">{nav}</nav>
  <article class="lesson">{body}</article>
  <p class="top-link"><a href="../index.html#week-1">← Back to the weekly plan</a></p>
</main>
</body>
</html>
'''
(ROOT / "dist" / "chapters" / "a_asym.html").write_text(html, encoding="utf-8")
print(f"Rendered {len(source.split())} manuscript words into a_asym.html")
