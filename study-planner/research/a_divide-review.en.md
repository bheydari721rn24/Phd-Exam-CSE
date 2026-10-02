### One connected summary

Divide and conquer replaces one instance by smaller instances and a justified combination. Correctness depends on a complete child contract, exhaustive answer locations or an algebraic identity, and a decreasing measure. Running time depends on the implemented representation, not only the recursion diagram.

Binary search discards one half using a monotone predicate. Stable merge takes the left item on a key tie and emits every item exactly once. Inversion counting charges a right item only when it is strictly smaller than the remaining left items. Maximum-subarray recursion becomes linear when each child returns total, prefix, suffix and best sums.

Closest pair uses presorted coordinate orders, rank-based membership, a strip and a packing bound within each recursive half. Karatsuba reconstructs the mixed coefficient from three smaller products. Strassen uses seven ordered block products and cancellation valid without commutativity. FFT recursively evaluates even and odd coefficient sequences at primitive roots, then uses the opposite-root transform and one normalization for inversion. Sufficient zero padding distinguishes ordinary from circular convolution.

### Rules 1–11: specifications, termination and representation

1. **State the complete output contract.** A numerical optimum, an attaining witness, a tie-breaking policy and an absence result are different obligations; specify whichever the task requires before choosing the recursion.
2. **Separate preconditions from hoped-for behavior.** Sortedness, a total key order, compatible block shapes and a valid primitive root must hold before their corresponding algorithms can be justified.
3. **Use a decreasing measure.** Array length or digit width must strictly decrease outside the base case; an apparently balanced coordinate test can fail this requirement on equal coordinates.
4. **Cover every base input.** Empty sequences, singletons and two-point geometric instances may require different outputs; a singleton proof alone does not settle an empty-input contract.
5. **Partition index ranges exactly.** Half-open children ending and beginning at the same midpoint neither overlap nor omit an item, including when the parent length is odd.
6. **Prove the combination before its cost.** A cheap operation returning an incorrect or incomplete parent answer does not become an algorithm merely because its recurrence has an attractive solution.
7. **Choose sufficient child information.** A child's optimal value may omit the boundary information required by a crossing parent solution; a richer summary can remove repeated scans.
8. **Charge representation changes.** Sorting, copying slices, filtering membership and constructing evaluation values are real operations that belong in the time and space analysis.
9. **Distinguish repeated states from independent instances.** Recomputing overlapping subproblems may motivate memoization, but naming a method divide and conquer does not automatically cache them.
10. **Identify the cost unit.** A comparison, a coordinate operation, a digit addition and a matrix multiplication are not interchangeable primitives; the size parameter must match the chosen model.
11. **Separate work, span and live storage.** Parallel children can reduce a dependency chain without reducing total work, and cumulative allocation is not peak simultaneously occupied memory.

### Rules 12–22: search, merge and inversion counts

12. **Lower bound is not membership.** Its returned length is a valid insertion boundary; membership requires an additional in-range equality check before accessing that position.
13. **Retain or exclude the midpoint deliberately.** A too-small midpoint must be excluded by advancing past it, while a feasible midpoint remains a possible lower bound when moving the upper boundary.
14. **Binary search needs the right monotonicity.** Sorted distinct integers make value-minus-index nondecreasing for fixed-point search; duplicates destroy that particular inference even though the values remain sorted.
15. **Random access is a model assumption.** Searching a linked list or copied subarray cannot inherit the constant-time midpoint-access cost of an indexed array without further analysis.
16. **Sortedness alone is insufficient.** A correct sort also preserves every input multiplicity; stability is an additional promise concerning the relative order of equal-key records.
17. **Take the left item on equal keys for stable merge.** This rule preserves cross-half original order only when the supplied runs themselves occur in the correct original run order.
18. **Check exhaustion before indexing.** The heads of both merge runs exist only while both pointers are within bounds; once one run ends, append the other remainder.
19. **Count strict inversions on strict inequality.** When a right head is smaller, it contributes one inversion with each remaining left item; equal values contribute none.
20. **Count each pair in one place.** Left-internal, right-internal and crossing inversions are disjoint classes, and each crossing inversion is charged when its right endpoint is emitted.
21. **Ordinary merge sort is not automatically adaptive.** The illustrated implementation processes all levels even on already sorted inputs; a linear best-case claim requires an explicit skip or another adaptation.
22. **Check result-counter range.** The largest inversion count is quadratic in array length, so a type suitable for indexing may still be too small for the accumulated count.

### Rules 23–33: maximum subarrays and summary algebra

23. **Declare whether emptiness is permitted.** The nonempty answer on an all-negative input is its largest entry; returning zero solves a different specification unless zero is actually present.
24. **Classify all interval locations.** Relative to one split, every nonempty interval is wholly left, wholly right or crossing; these cases establish the recursive combination proof.
25. **A crossing interval is a suffix plus a prefix.** The two endpoints can be optimized independently because the chosen suffix and prefix always concatenate into a valid crossing interval.
26. **Initialize maxima according to the contract.** Zero initialization admits an empty choice; initialize from actual items or negative infinity when maximizing nonempty prefixes, suffixes or intervals.
27. **Return all four summary components.** Total, best prefix, best suffix and best internal interval are jointly sufficient for constant-size combination of adjacent nonempty segments.
28. **Do not confuse scan and summary versions.** Repeated linear crossing scans give linear-logarithmic work; constant-size combines over singleton leaves give linear work with index-range recursion.
29. **Associativity permits regrouping, not reordering.** The summary of a fixed concatenation is unique, but changing segment order can change prefix, suffix and crossing values.
30. **An empty identity is an algebraic device.** Its negative-infinity best component does not become a legal nonempty answer for an empty input without a separate absence policy.
31. **Store witness metadata consistently.** Right-child indices must be offset, and every candidate comparison must follow the same sum/start/end tie order throughout recursion.
32. **Preserve segment order in range queries.** Segment-tree pieces may be parenthesized differently but must be combined in their original left-to-right sequence because the summary operation is noncommutative.
33. **A linear bound matches the input-reading barrier.** An unrestricted uninspected item could be made large enough to change the maximum, so exact worst-case algorithms cannot skip arbitrary entries.

### Rules 34–44: closest-pair geometry

34. **Use distinct record IDs.** Two records with identical coordinates are distinct endpoints and yield distance zero; a coordinate-only output can obscure which records were selected.
35. **Handle fewer than two records explicitly.** There is no legal pair for zero or one record, so that input requires absence rather than a fabricated distance witness.
36. **Split by sorted rank when coordinates tie.** A numerical less-than-median test can leave one child empty; rank and ID membership preserve balanced child sizes.
37. **Preserve both coordinate orders.** Filter the y-sorted list by the actual x-rank membership so the two child representations contain exactly the same assigned records.
38. **State membership-access assumptions.** Dense-ID marking gives deterministic constant-time lookups in the indexed-array model; an ordinary hash set may require expected-cost qualifications.
39. **The strip follows from horizontal distance.** An improving cross-half pair cannot have either endpoint farther from the divider than the current child minimum.
40. **Apply separation within each half.** Opposite-half points can be much closer than the child minimum, so the packing proof cannot assume that all strip points are mutually separated.
41. **Count the window including the current point.** At most four points per half give eight in the rectangle, hence seven successors besides the current point.
42. **Boundary ownership must be defined.** Half-open cells and fixed recursive membership prevent points on grid lines or the divider from being counted ambiguously.
43. **Shrinking the current distance is safe.** A better discovered pair reduces the relevant vertical window and cannot create more candidates than the original packing bound allowed.
44. **Do not export the constant seven indiscriminately.** It comes from a two-dimensional Euclidean packing proof; other metrics, dimensions or universal tie-enumeration requirements need their own analysis.

### Rules 45–55: integer multiplication

45. **Digit width is the relevant size.** An integer's numeric magnitude is exponential in its representation length, so using its value as the recurrence parameter hides the intended complexity.
46. **Choose the low-part width explicitly.** The reconstruction shifts are that width and twice that width, even when the original total digit count is odd.
47. **Expand the ordinary product first.** Four high/low products expose the two mixed terms, making it clear what the three-product identity must recover.
48. **Derive the reduced product count algebraically.** The difference product contains the two unmixed terms minus the mixed sum, so subtracting it reconstructs the missing contribution exactly.
49. **Allow negative internal differences.** Their signs affect the middle coefficient and must be restored after any recursive multiplication of absolute magnitudes.
50. **Separate internal signs from input signs.** The signed outer product is the signed unsigned-magnitude result; it is not obtained by blindly reusing a difference-product sign.
51. **Difference widths are bounded.** The absolute difference of two nonnegative parts fits within their larger width, while their sum may require an extra bit.
52. **Odd-width calls still terminate.** Every nonbase operand shrinks to at most the ceiling half-width; prove this inequality instead of pretending every size is an exact power of two.
53. **Charge additions and shifts by represented size.** Large-integer arithmetic is linear-size overhead in the elementary bit model, rather than a constant-cost operation on arbitrary magnitudes.
54. **Use the right strength of bound.** A regular padded recurrence gives a tight exponent, while a value-dependent implementation may be faster on special inputs and should not inherit a universal per-input lower bound.
55. **Asymptotic improvement does not prove a software speedup.** Runtime multiplication routines and practical cutoffs differ; benchmark before asserting that an educational implementation is faster.

### Rules 56–66: matrix products

56. **Block dimensions must be compatible.** Splitting the shared dot-product index proves each block product; merely drawing four quadrants does not verify conformable multiplication.
57. **Preserve multiplication order.** Matrix blocks generally do not commute, so a scalar manipulation that swaps factors is not a valid recursive matrix identity.
58. **Fix one product-numbering convention.** Different Strassen presentations label their seven products differently; their recombination equations must be kept with the same definitions.
59. **Verify all four output blocks.** Checking one cancellation or one numerical example does not establish the full matrix identity; expand every block without reordering factors.
60. **Subtraction is a precondition.** Strassen uses additive inverses and distributivity, so it applies to suitable rings rather than automatically to every multiplication-like semiring.
61. **The count is seven recursive block products.** Entrywise additions and subtractions still contribute quadratic work; reducing the product count does not eliminate combination costs.
62. **Zero padding must preserve the desired output.** Added positions contribute zero to relevant dot products, and the required original-sized block is extracted afterward.
63. **Power-of-two padding changes dimension by a bounded factor.** The next power is less than twice the original square dimension, preserving a fixed polynomial asymptotic exponent.
64. **Rectangular and sparse inputs need separate accounting.** Square padding and dense block addition can erase advantages of the original structure, so the square recurrence is not a universal recommendation.
65. **Exact algebra does not settle floating-point quality.** Additional additions and subtractions can cause cancellation and roundoff, even though the ring identity is mathematically exact.
66. **Squaring shortcuts require block-valid identities.** A scalar five-product derivation relying on commutativity cannot be recursively applied to arbitrary matrix blocks without another proof.

### Rules 67–77: Fourier transforms and convolution

67. **Coefficient count is degree plus one.** Two arrays of lengths $m$ and $k$ need up to $m+k−1$ product coefficients, including zeros for missing intermediate powers.
68. **Interpolation needs enough distinct points.** A polynomial of degree below the transform length is determined by that many distinct evaluations; repeated points do not supply equivalent information.
69. **A primitive root has the full required order.** The equation that its transform-length power is one alone is insufficient, because a smaller-order root repeats evaluation points.
70. **Split coefficients by parity.** The identity for even and odd coefficients produces half-size polynomials in the squared argument; splitting contiguous low and high halves is a different decomposition.
71. **Squared roots must remain primitive at the child size.** For a power-of-two transform, the root-square has exactly half the original order, which justifies each recursive evaluation grid.
72. **One butterfly produces two outputs.** The second half uses the negative twiddle contribution because the root raised to half the transform length equals negative one.
73. **Keep the sign convention consistent.** Either forward exponent sign is permissible, but inversion must use the opposite sign with the correct single normalization factor.
74. **Normalize the inverse once.** Dividing by the full transform length at the end implements the orthogonality proof; applying arbitrary normalization at every recursive node changes the result.
75. **The unnormalized Fourier matrix scales norms.** Its conjugate-transpose product is the transform length times identity; only dividing the matrix by the square root of that length yields a unitary map.
76. **Pad to prevent cyclic aliasing.** A length shorter than the product coefficient count folds powers modulo the transform-length relation and returns circular rather than ordinary convolution.
77. **FFT bounds count arithmetic operations.** Floating-point precision, coefficient magnitude and exact-integer recovery are additional questions not answered by the linear-logarithmic operation count.

### Rules 78–88: exact recovery and examination method

78. **Validate the radix-two input.** The illustrated implementation requires a positive power-of-two length; neither zero nor an arbitrary odd length is a valid unchecked input.
79. **Prove numerical rounding conditions.** Recovering an integer from an approximate coefficient requires an error below one half, not merely an observed close result on a few examples.
80. **Modular transforms need a field-compatible root.** The root order, divisibility of the field's multiplicative group size and invertibility of the transform length must all be verified.
81. **A modular answer is a residue.** Ordinary signed coefficients require a magnitude bound and enough combined modulus to select their unique centered representatives.
82. **Bit reversal is an index permutation.** Its fixed-width binary digits reflect parity-recursion order; it is unrelated to sorting coefficient values.
83. **Distinguish necessary from sufficient information.** A reduced majority candidate can be spurious, so an original-array verification step is required before returning a majority witness.
84. **Use tiny counterexamples deliberately.** Equal keys, all-negative entries, tied coordinates, odd digit widths and noncommuting blocks reveal different unsupported assumptions.
85. **Compare against an independent baseline.** Direct inversion counting, interval enumeration, ordinary matrix products and direct transforms test different reasoning paths rather than merely reusing the optimized combine.
86. **Finite tests support but do not replace proofs.** Passing bounded inputs checks implementations and arithmetic examples; unrestricted correctness still depends on the stated inductive and algebraic arguments.
87. **Respect the chapter boundary.** Full quicksort, selection, randomized algorithms and further correctness techniques belong to later chapters; do not claim they have been completely taught by a brief reference.
88. **End with a reproducible answer.** State the specification, proof idea, valid representation, recurrence, model and boundary cases so a reader can reconstruct the algorithm and identify its limits.

### A six-step examination procedure

1. Translate the requested output into a precise contract, including empty input, witnesses and ties.
2. Identify the input-size measure and state the costs of data access and arithmetic.
3. Divide the instance using rules that preserve membership and decrease the measure.
4. Derive every possible parent answer location or the exact algebraic identity; strengthen the child summary when necessary.
5. Prove the base case and combination, then charge the real representation operations and solve the resulting recurrence.
6. Check a small adversarial case and verify the returned witness; use an independent simple method when practical.

For example, claiming a linear maximum-subarray recursion requires a four-component child summary, index ranges rather than copied slices, a constant-size combination proof, and a nonempty singleton base case. Merely changing the recurrence's toll to a constant does not establish any of those obligations.
