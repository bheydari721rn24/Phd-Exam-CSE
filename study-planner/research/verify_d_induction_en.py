"""Finite regression and document-structure checks for induction; not universal proofs."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "research" / "d_induction.en.md").read_text(encoding="utf-8")
html = (ROOT / "dist" / "chapters" / "d_induction.html").read_text(encoding="utf-8")
assert len(source.split()) >= 4500
assert source.count("### Problem ") == 24
assert all(f"### Problem {i} " in source for i in range(1, 25))
assert all(f"**{i}." in source for i in range(1, 29))
assert all(name in source for name in ["MIT", "Stanford", "Berkeley", "Cornell", "ETH Zürich"])
assert not re.search(r"[\u0600-\u06ff]", source + html)
assert html.count("<svg") == 2
assert "formula-block" in html and "<sub>" in html and "<sup>" in html
assert "STIX Two Math" in (ROOT / "dist" / "chapters" / "chapter.en.css").read_text(encoding="utf-8")


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
assert tables.rows and all(rows and len(set(rows)) == 1 for rows in tables.rows)

for n in range(0, 101):
    assert sum(range(1, n + 1)) == n * (n + 1) // 2
    assert sum(2 * i + 1 for i in range(n)) == n * n
    assert (n**3 - n) % 3 == 0
    assert n * n % 2 == n % 2
    assert 2**n >= n + 1
    if n >= 12:
        assert any(4 * a + 5 * b == n for a in range(n // 4 + 1) for b in range(n // 5 + 1))
    if n >= 6:
        assert any(3 * a + 4 * b == n for a in range(n // 3 + 1) for b in range(n // 4 + 1))
assert not any(4 * a + 5 * b == 11 for a in range(4) for b in range(3))
assert not any(3 * a + 4 * b == 5 for a in range(3) for b in range(2))
fib = [0, 1]
for _ in range(2, 31):
    fib.append(fib[-1] + fib[-2])
assert all(value < 2**n for n, value in enumerate(fib))
for n in range(1, 101):
    assert abs(sum(1 / (i * (i + 1)) for i in range(1, n + 1)) - n / (n + 1)) < 1e-12
    assert sum(1 / (i * i) for i in range(1, n + 1)) <= 2 - 1 / n + 1e-12
    if n <= 12:
        from math import comb

        assert sum((-1) ** j * comb(n, j) for j in range(n + 1)) == 0
for n in range(1, 9):
    even = odd = 0
    for number in range(2**n):
        if number.bit_count() % 2:
            odd += 1
        else:
            even += 1
    assert even == odd == 2 ** (n - 1)
print(f"Induction chapter checks passed: {len(source.split())} words, 24 problems, 28 rules, {len(tables.rows)} tables.")
