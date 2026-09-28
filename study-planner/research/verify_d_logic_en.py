"""Independent finite checks for claims used in the English logic chapter."""

from __future__ import annotations

from itertools import product
from pathlib import Path
import re


chapter = (Path(__file__).resolve().parents[1] / "research" / "d_logic.en.md").read_text(encoding="utf-8")
assert len(re.findall(r"^### Problem \d+ ", chapter, re.M)) == 10
assert "Exams/" not in chapter
assert not re.search(r"[\u0600-\u06ff]", chapter)

rows = list(product((False, True), repeat=3))
imp = lambda a, b: not a or b

for p, q, r in rows:
    assert imp(p, q) == (not p or q)
    assert imp(p, q) == imp(not q, not p)
    assert (not imp(p, q)) == (p and not q)
    xor = p != q
    f = xor or r
    dnf = (p and not q) or (not p and q) or r
    cnf = (p or q or r) and (not p or not q or r)
    assert f == dnf == cnf
    assert not ((p or q) and imp(p, r) and imp(q, r) and not r)

valid_outputs = []
for assignment in product((False, True), repeat=8):
    valid = True
    for (p, q, r), output in zip(rows, assignment):
        if imp(p, q) and not output:
            valid = False
            break
    if valid:
        valid_outputs.append(assignment)
assert len(valid_outputs) == 4, valid_outputs

count_problem_7 = sum(imp(p, q) and (q or r) for p, q, r in rows)
assert count_problem_7 == 5

domain = (0, 1)
equality = lambda x, y: x == y
assert all(any(equality(x, y) for y in domain) for x in domain)
assert not any(all(equality(x, y) for x in domain) for y in domain)

edges = {(0, 1), (1, 0)}
assert all(any((x, y) in edges for y in domain) for x in domain)
assert all(((x, y) not in edges or (y, x) in edges) for x in domain for y in domain)
assert not all((x, x) in edges for x in domain)

for size in (1, 2, 3):
    objects = tuple(range(size))
    subsets = [
        {objects[index] for index, included in enumerate(bits) if included}
        for bits in product((False, True), repeat=size)
    ]
    for requested in subsets:
        for accepted in subsets:
            for retryable in subsets:
                every_accepted = all(x not in requested or x in accepted for x in objects)
                some_retryable = any(x in requested and x in retryable for x in objects)
                original = imp(every_accepted, some_retryable)
                derived_negation = every_accepted and all(
                    x not in requested or x not in retryable for x in objects
                )
                assert derived_negation == (not original)
        for solved in subsets:
            exact_one = any(
                x in requested and x in solved and
                all(y not in requested or y not in solved or y == x for y in objects)
                for x in objects
            )
            assert exact_one == (len(requested & solved) == 1)

for relation_bits in product((False, True), repeat=4):
    relation = {(x, y) for (x, y), yes in zip(product(domain, repeat=2), relation_bits) if yes}
    for q_bits in product((False, True), repeat=4):
        q_relation = {(x, y) for (x, y), yes in zip(product(domain, repeat=2), q_bits) if yes}
        original = all(
            any((x, y) not in relation or all((y, z) in q_relation for z in domain)
                for y in domain)
            for x in domain
        )
        derived_negation = any(
            all((x, y) in relation and any((y, z) not in q_relation for z in domain)
                for y in domain)
            for x in domain
        )
        assert derived_negation == (not original)
    for x in domain:
        for y in domain:
            before = all((x, z) in relation for z in domain)
            capture_free_result = all((y, z) in relation for z in domain)
            if x == y:
                assert before == capture_free_result

for a_bits in product((False, True), repeat=2):
    a = dict(zip(domain, a_bits))
    for b in (False, True):
        assert (all(a.values()) and b) == all(a[x] and b for x in domain)
        assert (any(a.values()) or b) == any(a[x] or b for x in domain)

print("English logic chapter checks passed: truth-functional claims and finite-model checks for Problems 1–9, quantifier movement, and scope examples.")
