"""Render the source-reviewed proof chapter as a printable English draft."""

from __future__ import annotations

import re
from pathlib import Path

from markdown_it import MarkdownIt


ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "research" / "d_proof.en.md").read_text(encoding="utf-8")
assert not re.search(r"[\u0600-\u06ff]", source)
assert not re.search(r"Exams/|entrance-exam question [0-9]+", source, re.I)
assert source.count("### Problem ") == 22
body = MarkdownIt("commonmark", {"html": True}).enable("table").render(source)
anchors = [
    "course-selection", "proof-obligations", "direct-proofs", "contrapositive",
    "contradiction", "cases-and-iff", "existence", "counterexamples",
    "worked-problems", "quick-reference", "references",
]
labels = [
    "Sources", "Proof obligations", "Direct proof", "Contrapositive", "Contradiction",
    "Cases and iff", "Existence", "Counterexamples", "Worked problems",
    "Key points", "References",
]
index = 0


def add_id(match: re.Match[str]) -> str:
    global index
    result = f'<h2 id="{anchors[index]}">{match.group(1)}</h2>'
    index += 1
    return result


body = re.sub(r"<h2>(.*?)</h2>", add_id, body)
assert index == len(anchors)

# Give inline symbols a little space without altering tag attributes or SVG text.
operators = "∈∉⊆∪∩∖∣=→↔≥≤≠∨∧"
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
  <meta name="description" content="An in-depth English chapter on direct proof, contradiction, counterexamples, and 22 worked problems.">
  <title>Direct Proof, Contradiction, and Counterexamples · Doctoral CSE 1406</title>
  <link rel="stylesheet" href="chapter.en.css">
  <style>@media print {{.lesson{{font-size:.92rem;line-height:1.44}}}}</style>
</head>
<body>
<main class="chapter">
  <div class="top-link"><a href="../index.html#week-1">← Back to the weekly plan</a></div>
  <header class="hero">
    <p class="eyebrow">Discrete Mathematics · Chapter 3</p>
    <h1>Direct Proof, Contradiction, and Counterexamples</h1>
    <p>Review draft · five reviewed university course texts · 22 fully worked problems</p>
  </header>
  <nav class="toc" aria-label="Chapter contents">{nav}</nav>
  <article class="lesson">{body}</article>
  <p class="top-link"><a href="../index.html#week-1">← Back to the weekly plan</a></p>
</main>
</body>
</html>
'''
(ROOT / "dist" / "chapters" / "d_proof.html").write_text(html, encoding="utf-8")
print(f"Rendered {len(source.split())} manuscript words into d_proof.html")
