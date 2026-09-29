"""Render the reviewed English logic manuscript as a static, printable chapter."""

from __future__ import annotations

import re
from pathlib import Path

from markdown_it import MarkdownIt


ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "research" / "d_logic.en.md").read_text(encoding="utf-8")
assert not re.search(r"[\u0600-\u06ff]", source), "The English lesson contains Arabic-script text."
assert not re.search(r"Exams/|entrance-exam question [0-9]+", source, flags=re.I)
assert source.count("### Problem ") == 14

renderer = MarkdownIt("commonmark", {"html": True}).enable("table")
body = renderer.render(source)
anchors = [
    "course-selection", "foundations", "propositional", "first-order",
    "worked-problems", "quick-reference", "laboratory", "references",
]
index = 0


def add_heading_id(match: re.Match[str]) -> str:
    global index
    value = match.group(1).replace(" {#references}", "")
    slug = anchors[index]
    index += 1
    return f'<h2 id="{slug}">{value}</h2>'


body = re.sub(r"<h2>(.*?)</h2>", add_heading_id, body)
assert index == len(anchors)

nav = " ".join(
    f'<a href="#{slug}">{label}</a>'
    for slug, label in zip(
        anchors,
        ["Sources", "Foundations", "Propositional logic", "Predicates",
         "Worked problems", "Key points", "Truth-table lab", "References"],
    )
)

html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="An English, source-synthesized chapter on propositions, predicates, and logical equivalence.">
  <title>Propositions, Predicates, and Logical Equivalence · Doctoral CSE 1406</title>
  <link rel="stylesheet" href="chapter.en.css">
</head>
<body>
<main class="chapter">
  <div class="top-link"><a href="../index.html#week-1">← Back to the weekly plan</a></div>
  <header class="hero">
    <p class="eyebrow">Discrete Mathematics · Chapter 1</p>
    <h1>Propositions, Predicates, and Logical Equivalence</h1>
    <p>Student-approved chapter · four university course texts synthesized · 14 fully worked problems</p>
  </header>
  <nav class="toc" aria-label="Chapter contents">{nav}</nav>
  <article class="lesson">{body}</article>
  <p class="top-link"><a href="../index.html#week-1">← Back to the weekly plan</a></p>
</main>
<script>
const select = document.getElementById("formula-select");
const output = document.getElementById("truth-output");
function evaluate(kind,p,q,r) {{
  if (kind === "imp" || kind === "rewritten") return !p || q;
  if (kind === "converse") return !q || p;
  if (kind === "biconditional") return p === q;
  return (p || q) && !r;
}}
function draw() {{
  let table = "<table><thead><tr><th>p</th><th>q</th><th>r</th><th>Formula value</th></tr></thead><tbody>";
  for (let p=0; p<=1; p++) for (let q=0; q<=1; q++) for (let r=0; r<=1; r++)
    table += "<tr><td>"+p+"</td><td>"+q+"</td><td>"+r+"</td><td>"+(evaluate(select.value,!!p,!!q,!!r)?1:0)+"</td></tr>";
  output.innerHTML = table + "</tbody></table>";
}}
select.addEventListener("change",draw); draw();
</script>
</body>
</html>
"""
(ROOT / "dist" / "chapters" / "d_logic.html").write_text(html, encoding="utf-8")
print(f"Rendered {len(source.split())} manuscript words into d_logic.html")
