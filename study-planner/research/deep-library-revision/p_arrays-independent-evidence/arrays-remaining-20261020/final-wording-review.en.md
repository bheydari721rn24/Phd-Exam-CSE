# Review of the actual rewritten Arrays solution manuscripts

I read all 81 actual replacement blocks individually: the requested PA13–PA81 plus PA01–PA12 in the existing first manuscript. This review concerns the manuscript text, not just the previous question certificates. `final-wording-review.json` records SHA-256 hashes of all three read files and the complete ID coverage.

## Required explanatory correction

**PA70:** “In a one-line cache, every access evicts the line needed for the following row access” incorrectly identifies the evicted line. Loading the current row line evicts the previous resident row line; the following row asks for a third line. The count remains 64, but the explanation should say: “Each next row access requests a line different from the sole resident line and therefore misses.” This also covers the column boundary, where the last row's line differs from the first row's requested line.

## Mathematical and semantic conclusions

- All numerical results in the new solution blocks agree with the independent oracle and the stated arithmetic models.
- PA66 now correctly separates a potentially widened evaluated product from a later narrowing conversion to `size_t`. The valid bound 8191 and maximum 65528 bytes are unchanged. Its post-conversion versus genuinely-wider-product distinction is important and correct.
- PA79 correctly identifies the largest required value as n squared, with 46340 as the largest positive n whose square fits signed 32-bit arithmetic. The n=0 logical case, positive C array-bound requirement, allocation arithmetic, and allocation success are separated appropriately.
- PA71's line-count expression is mathematically correct. For positive n it counts first through last line inclusively; n=0 is handled separately. Standard TeX accepts the single-token form `\frac B L`, but normalizing it to `\frac{B}{L}` avoids depending on custom-parser support. Apply the same brace normalization to denominators written as a bare 2 and the bare-n fractions in PA64. This is a renderer compatibility issue, not a mathematical error.
- PA67 retains the nonzero-size condition, safe temporary ownership update, old-pointer invalidation on success, and original allocation preservation on failure. Its code is valid as a C fragment in a context declaring `realloc` and `NULL`; it should not be advertised as a complete standalone translation unit without the standard header and surrounding declarations.
- The `sizeof`, array-parameter, initialization, pointer-to-row, row-subarray, C string initialization, string-literal modification, and ctype distinctions are stated correctly. I did not invoke a C compiler or run undefined behavior.
- All additional results introduced in the rewrite were checked: PA23 non-strict comparison gives five or six updates under the two initializations; PA24 zero-based weighting gives 16; PA38's three reversals use six swaps; and PA50's second output sums to six.
- The first twelve manuscripts' extended claims are consistent: PA04's matching-coordinate count is gcd(R-1,C-1)+1 for both dimensions greater than one; PA06's complete transpose permutation is correct; PA07 keeps the unspecified byte width explicit; PA10's right-biased search correctly skips empty rows; and PA12 does not infer legal subtraction from nearby numeric addresses.

## Editorial integration notes

1. PA02 and PA05 have explicit “Stem clarification required” paragraphs. Apply those source-stem repairs and retain the repair history in the audit rather than presenting unfinished editorial instructions to the student.
2. PA51 currently says an assumption “must appear in the stem.” Apply that assumption to the actual stem and phrase the solution directly as its stated environment.
3. PA52's final paragraph describes prior rendering damage. The restored code block already makes the educational concept clear; keep the damage history in the audit and remove that paragraph from the final student answer.
4. PA75's finite-arithmetic advice should explicitly say the final count must itself fit. Dividing an even factor before multiplication prevents an avoidable intermediate overflow but cannot make an unrepresentable final count representable. Its current mathematical counts are correct.

## Verification boundary

The per-question numerical/Python oracle remains `oracle.py` and `oracle-report.json`, with 14,898 counted checks. This final reading adds manuscript-specific mathematical and semantic review. It is not a claim of worldwide course exhaustion, physical hardware testing, compiler-based conformance, or literal 100% correctness.
