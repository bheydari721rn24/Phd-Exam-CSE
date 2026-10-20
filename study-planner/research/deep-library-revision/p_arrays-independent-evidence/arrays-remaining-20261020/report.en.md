# Independent review of Arrays PA13–PA81 and 80 review rules

## Reviewed artifacts and actual scope

I read every stem and existing solution for PA13 through PA81 individually, including the certificate fields, and all 80 numbered rules in `research/p_arrays-review.en.md`. I did not modify the checkout. An independent oracle and its complete per-question ledger accompany this report. The oracle completed **14,898 counted checks**, plus its complete-ID coverage assertion. It does not certify the rewritten solutions until their actual final text has separately been read.

The question-source SHA-256 was `93168ff4dde24b0c6ae25d2ec538856b8630040b758dcd1ce3733ea4985a10c1`. The 80-rule source SHA-256 was `c4148641a147dea9096977ea95547b9b754c42e08c351785daf1dec8eabf4db5`.

## Required correction: PA66 integer promotions

The maximum fitting count **8191**, maximum fitting byte count **65528**, and mathematical next count product **65536** are correct. However, `SIZE_MAX=65535` alone does not guarantee that the expression `n * sizeof(element)` is evaluated in 16-bit unsigned arithmetic. On a conforming model with a 16-bit unsigned `size_t` and a wider `int`, integer promotions can convert both operands to `int`; their product 65536 is representable there. A later conversion to `size_t`, such as when supplying an allocation size, reduces it to zero. Therefore revise the original claim that the multiplication itself necessarily wraps to zero.

Suggested complete wording: “The mathematical byte count for 8192 elements is 65536, which cannot be represented by this `size_t`. In a 16-bit unsigned computation, or on conversion of that value to this `size_t`, it becomes zero. Integer promotions may instead calculate the product in a wider `int` first, so identify the expression's actual type before describing the point of wraparound. The precondition `n <= SIZE_MAX / sizeof *p` avoids both routes to an invalid allocation count.”

Checking only `product <= SIZE_MAX` after first storing the product into `size_t` is ineffective. Checking a genuinely wider product can be meaningful, so the explanation should distinguish these two cases.

## Text and assumption corrections

1. **PA52 and PA54** contain literal `\x27` spelling for apostrophes in the JSON source stems. Inspect rendering and replace it with genuine C character-literal notation, such as `'a'`, `'b'`, and `'c'`. This is a source-display defect, not a numerical answer error.
2. **PA41** calls the exercise a “two-pass difference transform” although the stated task is one reverse scan and the answer compares two alternative directions. Retitle it to “Direction of an in-place adjacent-difference transform,” or explicitly distinguish the forward-prefix and inverse-difference pair of transformations. Its correct output `[3,2,4,1]` and incorrect-direction output `[3,2,7,3]` agree with independent execution.
3. **PA39** uses addition by eight modulo twelve. For a left rotation by eight this naturally denotes **destination-to-source**, while original-to-destination subtracts eight. Both give the same cycle sets but opposite traversal orientations. The cycle `0 -> 8 -> 4 -> 0` is correct for the stated plus-eight map; label that map precisely before describing value movement.
4. **PA67** must retain the explicit **`new_bytes > 0`** assumption for the stated failure-preserves-old-allocation rule. This is already in the existing solution and must not disappear in a rewrite.
5. **PA72** is a mathematical modulo example. An implementation using finite `head + length` must avoid overflow separately, even though the modular formula is mathematically correct. No erroneous answer appears in this small numeric instance.

## Individual verification coverage

- **PA13–PA22:** transformed pointer-index interval, stipulated `sizeof` quotients and typed strides, row-subarray boundary qualification, initialization categories, diagnostic versus runtime distinctions, one-past subtraction, safe reverse iteration for lengths 0 through 100, and exact stride count. I did not execute illegal C accesses or declarations.
- **PA23–PA29:** both minimum initialization policies and earliest tied index; exact weighted total 24; all three boundary-prefix answers; signed boundary difference events; complete two-dimensional prefix table; and forward/reverse evolving neighbor-update traces.
- **PA30–PA41:** both overlapping-move directions, weak final-source contract counterexamples, all bounded copy intervals with length below 20, insertion/deletion counts, reversal pairs, all three rotation states, all four modular cycles, stable compaction, and both adjacent-difference loop directions. General invariant arguments were read separately from finite enumeration.
- **PA42–PA51:** executed all ten actual Python certificate programs in fresh namespaces against independently derived expectations. Additionally extracted and executed the exact multiline code printed in PA46 and PA48, checked row identity in PA47, verified both invalid single indices for PA42, and verified the failed extended-slice replacement in PA44. Python results agree with the source answers. No assumption about a C/Python implementation's physical representation was inferred from these runs.
- **PA52–PA61:** abstract initialized-byte/terminator facts; C versus C++ string-initializer distinction; modifiable array versus literal target; bounded-scan success/absence; exact naive-search total 12 and match index 2; empty/longer pattern behavior; append capacity including terminator; pointer-versus-character sentinel; ctype argument domain; and borrowed interior-pointer lifetime. C semantics were reviewed, not compiled or run.
- **PA62–PA69:** exact allocate-copy-free growth accounting; doubling inequalities for all lengths 1 through 10000; additive series for 100 multiples of three; tripling versus doubling at length ten; allocation arithmetic including the promotion caveat above; realloc lifecycle; expand-then-shift count 15 and peak 24; and shrink/grow oscillation's eight copies plus one new-value write.
- **PA70–PA81:** explicit cold one-line cache simulation giving 8 versus 64 fills; all bytes in the misaligned interval giving four lines; ring positions `[5,6,0,1]` and append position two; full rectangular transpose permutation and four-cycle; exact triangular inversion `(5,2)`; independent pair-region enumeration; stronger nonempty/sentinel interface contracts; signed-overflow partial-sum counterexample without running UB; mirrored-bound checks for lengths 0 through 100; exact square-root bound 46340; pointer offset domains for every position including one-past for lengths 1 through 30; and integer-versus-floating mean behavior.

## Review rules

All 80 existing rules were read individually. Their mathematical claims and stated semantic distinctions agree with this review. They are a concise decision checklist, so the rewritten solved problems should supply the detailed demonstrations rather than inflating these rules with duplicated derivations. Preserve rule 66's explicit value-movement direction, rule 80's arithmetic/cost assumptions, and the separation of logical length from backing storage.

## Limits

No C or C++ compiler was invoked. No undefined behavior was executed to infer an answer. No real allocation failure, allocator address stability, hardware cache, ABI, or physical Python object layout was measured. The C statements are manual semantic review, and the simulations are the explicitly stated abstract models. Finite checks supplement the mathematical proofs; they do not establish literal 100% correctness or full worldwide course coverage.
