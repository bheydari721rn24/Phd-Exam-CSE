"""Finite counterchecks for the chapter's delicate exact-count formulas.

These checks detect transcription errors; the manuscript supplies general proofs.
"""

from itertools import permutations
from math import ceil, comb, isqrt, log2


for n in range(0, 129):
    assert sum(1 for i in range(n) for j in range(i)) == comb(n, 2)
    assert sum(1 for i in range(n) for j in range(i + 1, n) for k in range(j + 1, n)) == comb(n, 3)
    assert len(range(0, n, 3)) == (n + 2) // 3
    assert len(range(0, n + 1, 3)) == n // 3 + 1
    assert sum(isqrt(i) for i in range(1, n + 1)) == sum(
        1 for i in range(1, n + 1) for j in range(1, isqrt(i) + 1)
    )
    if n:
        m = n.bit_length() - 1
        assert sum(1 << k for k in range(m + 1)) == (1 << (m + 1)) - 1
        assert n <= (1 << (m + 1)) - 1 < 2 * n
        by_start = sum(sum(1 for k in range(m + 1) if i * (1 << k) <= n) for i in range(1, n + 1))
        by_depth = sum(n // (1 << k) for k in range(m + 1))
        assert by_start == by_depth
        assert n <= by_depth < 2 * n
        multiples = sum(sum(1 for j in range(i, n + 1, i)) for i in range(1, n + 1))
        assert multiples == sum(n // i for i in range(1, n + 1))
        logarithmic = sum((i.bit_length()) for i in range(1, n + 1))
        counted = sum(sum(1 for k in range(i.bit_length()) if (1 << k) <= i) for i in range(1, n + 1))
        assert logarithmic == counted

for n in range(2, 257):
    i, visits = 2, 0
    while i < n:
        visits += 1
        i *= i
    predicted = max(0, ceil(log2(log2(n))))
    assert visits == predicted, (n, visits, predicted)

for size in range(1, 6):
    for values in permutations(range(size)):
        data = list(values)
        shifts = 0
        for i in range(1, size):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                shifts += 1
                j -= 1
            data[j + 1] = key
        inversions = sum(values[p] > values[q] for p in range(size) for q in range(p + 1, size))
        assert shifts == inversions
        assert data == sorted(values)

print("Finite loop-count checks passed; general proofs remain in the lesson.")
