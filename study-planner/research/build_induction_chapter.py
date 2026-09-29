"""Render the source-reviewed induction manuscript as a printable English draft."""

from __future__ import annotations

import re
from pathlib import Path

from markdown_it import MarkdownIt


ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "research" / "d_induction.en.md").read_text(encoding="utf-8")
assert not re.search(r"[\u0600-\u06ff]", source)
assert source.count("### Problem ") == 24
assert "## 10. High-yield review" in source
body = MarkdownIt("commonmark", {"html": True}).enable("table").render(source)
anchors = [
    "sources", "induction-rule", "ordinary-induction", "initial-values",
    "strong-induction", "well-ordering", "strengthening", "invalid-inductions",
    "worked-problems", "quick-reference", "references",
]
labels = [
    "Sources", "The rule", "Ordinary induction", "Initial values", "Strong induction",
    "Well-ordering", "Strengthening", "Common errors", "Worked problems",
    "Key points", "References",
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
# Separate mathematical operators visually without editing tags or diagram labels.
operators = "∈∉⊆∑∧=→↔≥≤≠∨∣+−"
thin = "\u2009"
parts = re.split(r"(<[^>]+>)", body)
inside_svg = False
for i, part in enumerate(parts):
    if i % 2:
        if part.startswith("<svg"):
            inside_svg = True
        elif part.startswith("</svg"):
            inside_svg = False
        continue
    if inside_svg:
        continue
    part = re.sub(rf"(?<![\s{thin}])([{operators}])", thin + r"\1", part)
    part = re.sub(rf"([{operators}])(?![\s{thin}])", r"\1" + thin, part)
    parts[i] = part
body = "".join(parts)
nav = " ".join(f'<a href="#{key}">{label}</a>' for key, label in zip(anchors, labels))
html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Ordinary and strong mathematical induction, with full explanations, diagrams, 24 solved problems, and 28 review rules.">
  <title>Ordinary and Strong Induction · Doctoral CSE 1406</title>
  <link rel="stylesheet" href="chapter.en.css">
  <style>@media print {{.lesson{{font-size:.92rem;line-height:1.44}}}}</style>
</head>
<body>
<main class="chapter">
  <div class="top-link"><a href="../index.html#week-1">← Back to the weekly plan</a></div>
  <header class="hero">
    <p class="eyebrow">Discrete Mathematics · Chapter 4</p>
    <h1>Ordinary and Strong Induction</h1>
    <p>Review draft · five reviewed university course texts · 24 fully worked problems</p>
  </header>
  <nav class="toc" aria-label="Chapter contents">{nav}</nav>
  <article class="lesson">{body}</article>
  <p class="top-link"><a href="../index.html#week-1">← Back to the weekly plan</a></p>
</main>
</body>
</html>
'''
(ROOT / "dist" / "chapters" / "d_induction.html").write_text(html, encoding="utf-8")
print(f"Rendered {len(source.split())} manuscript words into d_induction.html")
