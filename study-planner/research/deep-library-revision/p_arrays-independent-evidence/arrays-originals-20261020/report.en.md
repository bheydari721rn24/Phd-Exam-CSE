# Independent source audit: the two authentic p_arrays items

Audit date: 20 October 2026. Scope: the original local PDFs, their complete relevant pages and enlarged question crops, the two editable adaptation records, and independent exact computations. No checkout files were changed. No official answer key was inspected or verified.

## Acquisition and visual evidence

Both local PDF SHA-256 digests match the corresponding Git blobs at pinned repository revision `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`.

| Item | Original PDF page | SHA-256 |
| --- | --- | --- |
| MS CS 1393 Q167 | 34; printed page 34 | `7ed89fae8eb601a964355fde5e5d297cbb30844e5240b9e3908b798fb86e349d` |
| PhD CS 1404 Q72 | 16; printed page 16 | `928e51b55059b3094583f9c190e260b405ec775da05f6c7679675e332a8a6f40` |

The companion `acquisition.json` contains exact source paths. Images personally inspected in this audit: `MS_CS_1393_Q167-full.png`, `MS_CS_1393_Q167-detail.png`, `Phd_CS_1404_Q72-full.png`, and `Phd_CS_1404_Q72-detail.png`. These are rendered original scans, not recreations of their code.

## MS CS 1393 Q167: reverse-stride copying

The current editable record agrees with the actual source. The source explicitly calls `store(N-1,0)` and says that `a` and `b` are global arrays. It asks for every other element, from the last source element toward the first, stored consecutively from the beginning of `b`.

All four options use `if (n < 0) return`. Actual option numbering and distinctions:

1. `b[i] = a[n]; store(n-2,i+1);`
2. `b[i+1] = a[n]; store(n-2,i+1);`
3. `b[i] = a[n]; store(n-2,i+2);`
4. `b[i+1] = a[n]; store(n-2,i+2);`

Every recursive source stride is minus two. The fourth alternative does not use `n-1`. The guard is strict `n<0`, not `n<=0`: a nonnegative source index zero must still be copied when reached.

### Full derivation suitable for the solution

Let `t` count completed copies. Initially `t=0`, source index `n=N-1`, and destination index `i=0`. At the beginning of each copying activation, maintain

\[
n=N-1-2t,\qquad i=t,\qquad
b[j]=a_{\mathrm{original}}[N-1-2j]\quad(0\le j<t).
\]

If `n>=0`, option 1 writes exactly the next required value into `b[t]`. Its recursive call changes `n` to `N-1-2(t+1)` and `i` to `t+1`, preserving the invariant. When `n<0`, every required source index has been processed and the guard prevents an invalid negative read. This proves option 1 independently of any answer key.

For nonnegative array length `N`, the number of copies is `m=ceil(N/2)`. If `N=2k`, the last copied index is 1, and the terminal call receives -1. If `N=2k+1`, the last copied index is 0, and the terminal call receives -2. There are `m+1` activations including the terminal guard-only activation. The source is pseudocode: treating a negative terminal index as an ordinary unsigned C array size would invalidate the stopping argument. An implementation must also provide destination capacity at least `m` and distinct source/destination storage or another preservation strategy.

For `a=[10,20,30,40,50,60]`, the actual mappings are source indices `5,3,1` to destination indices `0,1,2`, producing `b=[60,40,20]`. For five elements the mappings are `4,2,0`, so index zero must not be discarded. Option 2 skips `b[0]`; option 3 leaves destination gaps; option 4 does both. These are different bugs even though all four source strides are correct.

Independent enumeration checked the index/count/terminal formulas for every `N=0..100`; exact results are in `independent-checks.json`. The empty case is an implementation extension, not an explicit promise that the examination intended an empty input.

## PhD CS 1404 Q72: running-minimum updates

The original source says that `A` has `n` distinct numbers and each permutation of `A` is equally likely. Its code is visually unambiguous in the enlarged source crop:

```text
min <- +infinity
for (i = 1; i <= n; i++)
    if (min > A[i])
        min = A[i]  // *
```

The loop bound is **`i <= n`**, not `i < n`. The comparison is **strict `min > A[i]`**. The initialization is positive infinity. `Y` counts changes at the assignment marked with `*`, not the initial sentinel assignment and not all evaluations of the condition. The source options are exactly 1, `ln n`, `n`, and `n ln n`, in that order. The first condition is always successful for a nonempty array of ordinary finite numbers.

The current record correctly adds the large-`n` interpretation needed for the listed logarithmic approximation. The original wording asks which expression is closer to the mean; it does not explicitly contain the phrase "for large n". Therefore this wording should be identified as a clarified English adaptation rather than an exact literal translation. It is especially useful not to claim that `ln n` equals the exact expectation for every positive `n`.

### Full derivation suitable for the solution

Define `I_i=1` precisely when the assignment executes at position `i`. That happens exactly when `A[i]` is the smallest of the first `i` values. Among all orders of those `i` distinct ranks, each of their `i` positions is equally likely to contain the smallest. Hence `P(I_i=1)=1/i`. Since `Y=I_1+...+I_n`, linearity gives

\[
\mathbb E[Y]=\sum_{i=1}^{n}\mathbb E[I_i]
=\sum_{i=1}^{n}\frac1i=H_n.
\]

Linearity does not require an independence argument. This is a statement about successful record updates, not loop complexity: there are `n` condition evaluations and `n+1` loop-guard evaluations under the printed conventional for-loop execution model, while the number of writes is random. In increasing order there is one write; in decreasing order there are `n` writes.

For example, `A=[5,2,4,1,3]` executes the marked assignment at positions 1, 2 and 4; the stored values are 5, 2 and 1, so this permutation has `Y=3`. Across all six permutations when `n=3`, the total update count is 11, giving exact mean `11/6`; this is neither 1 nor 3 nor exactly `ln 3`.

For `n>=1`, integrating the decreasing function `1/x` gives `ln(n+1)<=H_n<=1+ln n`, and `H_n/ln n -> 1` as `n` grows. Thus option 2 is the intended asymptotic approximation, independently derived. It is inaccurate to present `H_n=ln n` as an identity. For very small `n`, the phrase "closest" needs care: at `n=1` the numerical values of options 1 and 3 coincide, and at `n=2` the mean is 3/2. The cleaned adaptation should preserve its explicit large-`n` qualification.

Do not replace the source by `min=A[1]` without changing the count: initializing from the first actual element and scanning only the rest would count `Y-1` successful subsequent writes and would have mean `H_n-1`. Allowing duplicate values also requires a fresh probability model; the printed distinctness assumption is what makes the rank-symmetry proof immediate. The sentinel is a pseudocode mathematical infinity, not an unchecked claim that an arbitrary finite C integer can represent a value above all possible inputs.

Independent exact enumeration tested every permutation of distinct ranks for each `n=1..8`: 46,233 permutations in total. Total update counts were 1, 3, 11, 50, 274, 1764, 13068, 109584 respectively, giving means `1, 3/2, 11/6, 25/12, 137/60, 49/20, 363/140, 761/280`, each equal to `H_n` exactly. These are finite checks supporting, not replacing, the general proof.

## Editing recommendations and limits

- Preserve the source option order and the `<=` loop glyph explicitly in any new code block, trace and diagram.
- The existing reverse-stride answer remains 1 and the record-minimum answer remains 2; both answers are independently derived, not certified official keys.
- Both are bridge revisits of previously used archive questions, not new unique archive discoveries.
- The current `difficulty` fields contain mojibake (`Mediumâ€“Hard`) when decoded as UTF-8. Normalize those metadata strings to plain `Medium to hard` during the owning agent's edit.
- The exact source code and the adapted modern presentation should be distinguished: the source uses mathematical pseudocode/global arrays; strict C interface, signedness, capacities and machine overflow require explicit additional contracts.
- No entire-examination corpus or official answer key was reviewed in this bounded task. No source PDFs were changed.
