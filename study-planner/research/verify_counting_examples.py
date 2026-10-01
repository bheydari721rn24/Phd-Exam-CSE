"""Independent small finite enumerations; these supplement the written proofs."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import comb, factorial

assert sum(p[0] != 0 for p in product(range(10), repeat=4)) == 9000
assert sum(p[0] != 0 for p in permutations(range(10), 4)) == 4536
assert sum(x < y for x, y in product(range(1, 7), repeat=2)) == 15
draws = list(permutations(range(9), 3))
assert F(sum(sum(x < 5 for x in d) == 2 for d in draws), len(draws)) == F(10, 21)
assert len(set(permutations("AAABBC"))) == 60
assert comb(10, 4) * comb(6, 3) == 4200
# Six people: encode a partition as a sorted tuple of sorted pairs.
partitions = {tuple(sorted(tuple(sorted(p[i:i+2])) for i in (0, 2, 4))) for p in permutations(range(6))}
assert len(partitions) == 15
# Six distinct labels: anchor 0; quotient reflection by a canonical reversal.
circles = list(permutations(range(1, 6)))
assert len(circles) == 120 and len({min(p, p[::-1]) for p in circles}) == 60
rows = list(permutations(range(7)))
assert sum(max(p.index(x) for x in (0, 1, 2)) - min(p.index(x) for x in (0, 1, 2)) == 2 for p in rows) == 720
assert sum(all(abs(p.index(x) - p.index(y)) > 1 for x, y in combinations((0, 1, 2), 2)) for p in rows) == 1440
strings = list(product((0, 1), repeat=9))
assert sum(sum(p) == 3 and all(not(p[i] and p[i+1]) for i in range(8)) for p in strings) == 35
assert sum(sum(p) == 12 for p in product(range(2, 13), range(1, 13), range(13), range(3, 13))) == 84
assert sum(sum(p) <= 5 for p in product(range(6), repeat=3)) == 56
assert sum(sum(p) == 10 for p in product(range(4), repeat=4)) == 10
placements = list(product(range(3), repeat=4))
occupancies = Counter(tuple(p.count(b) for b in range(3)) for p in placements)
assert occupancies[(2, 1, 1)] == 12
assert Counter(len(set(p)) for p in placements) == {1: 3, 2: 42, 3: 36}
sample = list(combinations(range(12), 4))
assert F(sum(sum(x < 5 for x in p) == 2 for p in sample), len(sample)) == F(14, 33)
def independent_law(probabilities):
    law = {}
    for bits in product((0, 1), repeat=len(probabilities)):
        mass = F(1)
        for bit, prob in zip(bits, probabilities):
            mass *= prob if bit else 1-prob
        law[bits] = mass
    assert sum(law.values()) == 1
    return law
law = independent_law([F(1, 3)] * 5)
assert sum(p for bits, p in law.items() if sum(bits) == 2) == F(80, 243)
assert sum(p for bits, p in law.items() if any(bits)) == F(211, 243)
law = independent_law([F(1, 2), F(1, 3), F(1, 4)])
assert sum(p for bits, p in law.items() if sum(bits) == 1) == F(11, 24)
assert F(sum(len(set(p)) < 4 for p in product(range(10), repeat=4)), 10**4) == F(62, 125)
fixed = Counter(sum(i == x for i, x in enumerate(p)) for p in permutations(range(5)))
assert fixed[0] == 44 and fixed[2] == 20 and fixed[4] == 0
for n in range(7):
    dn = sum(all(i != x for i, x in enumerate(p)) for p in permutations(range(n)))
    formula = sum((-1)**j * comb(n, j) * factorial(n-j) for j in range(n+1))
    assert dn == formula
    for k in range(n+1):
        actual = sum(sum(i == x for i, x in enumerate(p)) == k for p in permutations(range(n)))
        dr = sum(all(i != x for i, x in enumerate(p)) for p in permutations(range(n-k)))
        assert actual == comb(n, k) * dr
for theta in (F(-1), F(-1, 2), F(0), F(1, 2), F(1)):
    law = {b: (1+theta*((-1)**sum(b)))/8 for b in product((0, 1), repeat=3)}
    assert sum(law.values()) == 1 and min(law.values()) >= 0
    for i in range(3):
        assert sum(p for b, p in law.items() if b[i]) == F(1, 2)
    for i, j in combinations(range(3), 2):
        for x, y in product((0, 1), repeat=2):
            assert sum(p for b, p in law.items() if b[i] == x and b[j] == y) == F(1, 4)
    assert law[(1, 1, 1)] == (1-theta)/8
    assert (law[(1, 1, 1)] == F(1, 8)) == (theta == 0)
law = {(1, 1, 1): F(1, 8), (1, 1, 0): F(3, 8), (0, 0, 1): F(3, 8), (0, 0, 0): F(1, 8)}
assert all(sum(p for b, p in law.items() if b[i]) == F(1, 2) for i in range(3))
assert sum(p for b, p in law.items() if b[0] and b[1]) == F(1, 2)
law = independent_law([F(1, 2)]*5)
assert sum(p for b, p in law.items() if any(b[:2]) and sum(b[2:]) == 1) == F(9, 32)
law = independent_law([F(1, 2)]*3)
assert sum(p for b, p in law.items() if any(b[:2]) and any(b[1:])) == F(5, 8)
conditional = {b: F(1, 3) for b in ((0, 1), (1, 0), (1, 1))}
assert sum(p for b, p in conditional.items() if b[0]) == F(2, 3)
assert conditional[(1, 1)] == F(1, 3)
mix = {}
for probability in (F(3, 4), F(1, 4)):
    for b, p in independent_law([probability]*2).items():
        mix[b] = mix.get(b, F(0)) + p/2
assert mix[(1, 1)] == F(5, 16)
assert mix[(1, 1)] / sum(p for b, p in mix.items() if b[0]) == F(5, 8)
weights = [F(1, 2), F(3, 10), F(1, 5)]
weighted = {}
for p in product(range(3), repeat=3):
    weight = F(1)
    for x in p: weight *= weights[x]
    weighted[p] = weight
assert sum(p for b, p in weighted.items() if len(set(b)) == 3) == F(9, 50)
assert sum(p for b, p in weighted.items() if 0 in b) == F(7, 8)
assert sum(p for b, p in weighted.items() if 0 in b or 1 in b) == F(124, 125)
assert sum(all(not(b[i] and b[i+1]) for i in range(5)) for b in product((0, 1), repeat=6)) == 21
for n in range(7):
    for k in range(n+1):
        for r in range(k+1):
            assert comb(n, k)*comb(k, r) == comb(n, r)*comb(n-r, k-r)
print("Independent enumerations passed: codes, fibers, partitions, symmetries, restrictions, occupancy, sampling, fixed points, weighted trials, and independence counterexamples.")
