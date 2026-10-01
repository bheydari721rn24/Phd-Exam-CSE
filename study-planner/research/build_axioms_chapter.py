"""Render the reviewed probability-axioms manuscript and original problem bank."""
from __future__ import annotations

import re
from pathlib import Path

from markdown_it import MarkdownIt
from math_typography import normalize_math, normalize_scripts

ROOT = Path(__file__).resolve().parents[1]
source = "\n\n".join((ROOT / "research" / name).read_text(encoding="utf-8") for name in ("s_axioms.en.md", "s_axioms-supplement.en.md"))
assert not re.search(r"[\u0600-\u06ff]", source)
assert source.count("### Problem ") == 24
assert "## 9. High-yield review" in source
body = MarkdownIt("commonmark", {"html": True}).enable("table").render(source)
anchors = ["sources", "modeling", "measurability", "axioms", "laws", "limits", "laboratory", "worked-problems", "quick-reference", "references"]
labels = ["Scope and sources", "Modeling", "Event domains", "Axioms and proofs", "Probability laws", "Event limits", "Laboratory", "Worked problems", "Key points", "References"]
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
  <meta name="description" content="Probability axioms, modeling, event algebra, and limiting events: five reviewed university sources, rigorous proofs, 24 fully worked problems, and a detailed review.">
  <title>Sample Spaces, Events, and Probability Axioms · Doctoral CSE 1406</title>
  <link rel="stylesheet" href="chapter.en.css">
  <link rel="stylesheet" href="s_axioms.css">
  <script src="s_axioms-lab.js" defer></script>
</head>
<body>
<main class="chapter">
  <div class="top-link"><a href="../index.html#week-1">← Back to the weekly plan</a></div>
  <header class="hero">
    <p class="eyebrow">Probability and Statistics · Chapter 1</p>
    <h1>Sample Spaces, Events, and Probability Axioms</h1>
    <p>Approved chapter · four core university sources and one supplement · 24 fully worked problems</p>
  </header>
  <nav class="toc" aria-label="Chapter contents">{nav}</nav>
  <article class="lesson">{body}</article>
  <p class="top-link"><a href="../index.html#week-1">← Back to the weekly plan</a></p>
</main>
</body>
</html>
'''
(ROOT / "dist" / "chapters" / "s_axioms.html").write_text(html, encoding="utf-8")
print(f"Rendered {len(source.split())} manuscript words into s_axioms.html")
