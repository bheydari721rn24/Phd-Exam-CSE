"""Finite countermodel and structural checks for the sets chapter (not a proof)."""

from __future__ import annotations

from html.parser import HTMLParser
from itertools import combinations
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "research" / "d_sets.en.md").read_text(encoding="utf-8")
html = (ROOT / "dist" / "chapters" / "d_sets.html").read_text(encoding="utf-8")
assert source.count("### Problem ") == 20
assert all(f"### Problem {i} " in source for i in range(1, 21))
assert "## 6. High-yield review" in source
assert all(f"**{i}." in source for i in range(1, 17))
assert all(name in source for name in ["MIT", "Stanford", "Cornell", "Carnegie Mellon", "Berkeley"])
assert not re.search(r"[\u0600-\u06ff]", source + html)


class TableParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_table = False
        self.in_row = False
        self.cols = 0
        self.tables: list[list[int]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "table":
            self.in_table = True
            self.tables.append([])
        elif tag == "tr" and self.in_table:
            self.in_row = True
            self.cols = 0
        elif tag in {"td", "th"} and self.in_row:
            self.cols += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "tr" and self.in_row:
            self.tables[-1].append(self.cols)
            self.in_row = False
        elif tag == "table":
            self.in_table = False


parsed = TableParser()
parsed.feed(html)
for table in parsed.tables:
    assert table and len(set(table)) == 1, f"Unequal column counts in table: {table}"

universe = frozenset(range(3))
all_sets = [frozenset(s) for length in range(4) for s in combinations(universe, length)]
power = lambda s: frozenset(frozenset(t) for k in range(len(s) + 1) for t in combinations(s, k))
sym = lambda a, b: a ^ b
product = lambda a, b: frozenset((x, y) for x in a for y in b)
for a in all_sets:
    assert len(power(a)) == 2 ** len(a)
    assert power(frozenset()) == frozenset({frozenset()})
    for b in all_sets:
        assert a == (a & b) | (a - b)
        assert (a <= b) == (a & b == a) == (a | b == b) == (a - b == frozenset())
        assert sym(a, b) == (a | b) - (a & b)
        assert (sym(a, b) == frozenset()) == (a == b)
        assert power(a & b) == power(a) & power(b)
        assert (power(a | b) == power(a) | power(b)) == (a <= b or b <= a)
        assert (power(a) <= power(b)) == (a <= b)
        assert (universe - (a | b)) == (universe - a) & (universe - b)
        assert len(a | b) == len(a) + len(b) - len(a & b)
        assert len(sym(a, b)) == len(a) + len(b) - 2 * len(a & b)
        assert len(power(a) & power(b)) == 2 ** len(a & b)
        assert power(a - b) != power(a) - power(b)
        for c in all_sets:
            assert a - (b | c) == (a - b) & (a - c)
            assert a - (b & c) == (a - b) | (a - c)
            assert a | (b & c) == (a | b) & (a | c)
            assert sym(sym(a, b), c) == sym(a, sym(b, c))
            assert ((a - b) <= c) == (a <= b | c)
            assert ((a & b) <= c) == (a <= (universe - b) | c)
            assert a - (b - c) == (a - b) | (a & c)
            assert (sym(a, b) <= c) == (a - c == b - c)
            assert (sym(a, b) == sym(a, c)) == (b == c)
            assert product(a, b - c) == product(a, b) - product(a, c)
            assert len(a | b | c) == (len(a) + len(b) + len(c)
                - len(a & b) - len(a & c) - len(b & c) + len(a & b & c))

for a in all_sets:
    for b in all_sets:
        for c in all_sets:
            for d in all_sets:
                lhs = product(a, b)
                rhs = product(c, d)
                assert lhs - rhs == product(a - c, b) | product(a, b - d)
                if lhs == rhs and lhs:
                    assert a == c and b == d

# Verify the one-element counterexample in Problem 20 and the false cancellation examples.
x = frozenset({0})
empty = frozenset()
assert sym(x, x & empty) != sym(x, x) & sym(x, empty)
assert x | x == empty | x and x != empty
assert x - x == empty - x and x != empty

print(f"Sets checks passed: {len(parsed.tables)} HTML tables; 20 problems; exhaustive 3-element finite models.")
