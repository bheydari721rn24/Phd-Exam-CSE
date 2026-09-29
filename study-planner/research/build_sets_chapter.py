"""Render the reviewed sets manuscript as a static, printable English draft."""

from __future__ import annotations

import re
from pathlib import Path

from markdown_it import MarkdownIt
from math_typography import normalize_scripts


ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "research" / "d_sets.en.md").read_text(encoding="utf-8")
assert not re.search(r"[\u0600-\u06ff]", source), "The English lesson contains Arabic-script text."
assert not re.search(r"Exams/|entrance-exam question [0-9]+", source, re.I)
assert source.count("### Problem ") == 20

body = MarkdownIt("commonmark", {"html": True}).enable("table").render(source)
anchors = ["course-selection", "objects", "operations", "families", "worked-problems", "quick-reference", "laboratory", "references"]
labels = ["Sources", "Foundations", "Operations", "Families and products", "Worked problems", "Key points", "Set laboratory", "References"]
index = 0


def heading_id(match: re.Match[str]) -> str:
    global index
    result = f'<h2 id="{anchors[index]}">{match.group(1)}</h2>'
    index += 1
    return result


body = re.sub(r"<h2>(.*?)</h2>", heading_id, body)
assert index == len(anchors)

# Ordinary HTML text does not provide TeX's automatic binary-operator spacing.
# Add a stable thin space around set and logic operators in text nodes only;
# attributes, links, and the script remain untouched.
math_operators = "∈∉⊆⊊∪∩△∖×=⇔↔→"
thin = "\u2009"
parts = re.split(r"(<[^>]+>)", body)
for i in range(0, len(parts), 2):
    chunk = parts[i]
    chunk = re.sub(rf"(?<![\s{thin}])([{math_operators}])", thin + r"\1", chunk)
    chunk = re.sub(rf"([{math_operators}])(?![\s{thin}])", r"\1" + thin, chunk)
    parts[i] = chunk
body = normalize_scripts("".join(parts))
nav = " ".join(f'<a href="#{anchor}">{label}</a>' for anchor, label in zip(anchors, labels))

html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="A source-synthesized English review draft on sets and set operations, with 20 worked problems and a high-yield review sheet.">
  <title>Sets and Set Operations · Doctoral CSE 1406</title>
  <link rel="stylesheet" href="chapter.en.css">
</head>
<body>
<main class="chapter">
  <div class="top-link"><a href="../index.html#week-1">← Back to the weekly plan</a></div>
  <header class="hero">
    <p class="eyebrow">Discrete Mathematics · Chapter 2</p>
    <h1>Sets and Set Operations</h1>
    <p>Student-approved chapter · four principal university courses and one supplemental text · 20 fully worked problems</p>
  </header>
  <nav class="toc" aria-label="Chapter contents">{nav}</nav>
  <article class="lesson">{body}</article>
  <p class="top-link"><a href="../index.html#week-1">← Back to the weekly plan</a></p>
</main>
<script>
const controls = ["in-a", "in-b", "in-c"].map(id => document.getElementById(id));
const setOutput = document.getElementById("set-lab-output");
function showMembership() {{
  const [a,b,c] = controls.map(control => control.value === "1");
  const rows = [
    ["A ∩ (B ∪ C)", a && (b || c)],
    ["(A ∩ B) ∪ (A ∩ C)", (a && b) || (a && c)],
    ["A △ (B ∩ C)", a !== (b && c)],
    ["(A △ B) ∩ (A △ C)", (a !== b) && (a !== c)]
  ];
  setOutput.innerHTML = "<table><thead><tr><th>Expression</th><th>Contains x?</th></tr></thead><tbody>" +
    rows.map(([name, value]) => `<tr><td>${{name}}</td><td>${{value ? "Yes" : "No"}}</td></tr>`).join("") + "</tbody></table>";
}}
controls.forEach(control => control.addEventListener("change", showMembership));
showMembership();
</script>
</body>
</html>
'''
(ROOT / "dist" / "chapters" / "d_sets.html").write_text(html, encoding="utf-8")
print(f"Rendered {len(source.split())} manuscript words into d_sets.html")
