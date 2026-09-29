"""Finite countermodels and structural checks; not a universal mathematical proof."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "research" / "d_proof.en.md").read_text(encoding="utf-8")
html = (ROOT / "dist" / "chapters" / "d_proof.html").read_text(encoding="utf-8")
assert source.count("### Problem ") == 22
assert all(f"### Problem {i} " in source for i in range(1, 23))
assert "## 10. High-yield review" in source
assert all(f"**{i}." in source for i in range(1, 25))
assert all(name in source for name in ["MIT", "Stanford", "Berkeley", "Cornell", "ETH Zürich"])
assert not re.search(r"[\u0600-\u06ff]", source + html)
assert "@font-face" in (ROOT / "dist" / "chapters" / "chapter.en.css").read_text(encoding="utf-8")
assert "<svg" in html and "formula-block" in html


class Tables(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.rows: list[list[int]] = []
        self.in_table = False
        self.in_row = False
        self.cols = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "table":
            self.in_table = True
            self.rows.append([])
        elif tag == "tr" and self.in_table:
            self.in_row = True
            self.cols = 0
        elif tag in ("th", "td") and self.in_row:
            self.cols += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "tr" and self.in_row:
            self.rows[-1].append(self.cols)
            self.in_row = False
        elif tag == "table":
            self.in_table = False


tables = Tables()
tables.feed(html)
assert tables.rows
for rows in tables.rows:
    assert rows and len(set(rows)) == 1, rows

for a in range(-7, 8):
    for b in range(-7, 8):
        for c in range(-7, 8):
            if a and b % a == 0 and c % a == 0:
                assert (2 * b - 3 * c) % a == 0
            if a and b % a == 0 and c % a == 0:
                assert (b + c) % a == 0
    assert (a * a % 2 == 0) == (a % 2 == 0)
    assert 3 * a * (a + 1) % 6 == 0
    assert (a % 2 != 0) == (a * a % 2 != 0)
    if a % 5 != 0:
        assert (a**4 - 1) % 5 == 0
    r, s = a + 1, a - 1
    assert r * r - s * s == 4 * a

assert 41**2 - 41 + 41 == 41**2
assert {1} - ({1} & set()) != ({1} - {1}) & ({1} - set())
assert {1} - ({1} & set()) == ({1} - {1}) | ({1} - set())
assert (-3) ** 2 == 3**2 and -3 != 3
print(f"Proof chapter checks passed: {len(tables.rows)} tables, 22 problems, 24 review rules, finite edge cases.")
