## Complete summary and examination decisions

### Connected summary

Divide and conquer has three separate obligations: smaller valid child instances, child answers rich enough to reconstruct the parent, and a combination step whose actual cost matches the proposed recurrence. Merge maintains a smallest-head invariant; maximum subarray carries four ordered summaries; closest pair preserves recursive identities and two sorted orders. Karatsuba and Strassen reduce multiplication count by algebraic cancellation, while Fourier recursion exploits paired primitive roots. Their exponents are consequences of these mechanisms and their declared cost models.

For power-of-two input length $N=2^h$, ordinary balanced merge sort has worst comparisons $hN-N+1$ and sorted-input comparisons $hN/2$. Strict cross inversion charges equal the remaining left length only when the right head is strictly smaller. Nonempty summary combination uses $B=\max(B_L,B_R,U_L+P_R)$ together with total, prefix and suffix formulas; it is associative but ordered. Closest pair obtains linear combination cost through a bounded strip scan and maintained y-order, not repeated sorting.

Karatsuba reconstructs $z_2b^{2m}+(z_s-z_2-z_0)b^m+z_0$ using the actual low-part width. Strassen preserves operand order in seven block products and requires additive inverses. A radix-two transform of length $2^h$ has $h2^{h-1}$ butterflies, counted as two-output units. Forward and inverse root conventions, inverse normalization, convolution padding and integer-recovery bounds must be checked separately. A median-of-full-five-groups certificate and a binary-search decision tree count keys, ranks and calls under different interfaces; these quantities cannot be interchanged.

The decisions below are written as complete rules with their premises and reasons. They apply to the chapter's declared algorithms, not automatically to every program with a similar recurrence.

### Decision 1. Write the multiset contract before a sorting proof

The output must contain every input record with unchanged multiplicity and have ordered keys. Returning a sorted subset is incorrect. The authentic median concatenation outputs the right side, median and left side in descending order; omitting records equal to the median is only harmless when distinct keys are a stated premise.

### Decision 2. Prove strict shrinkage on every recursive branch

A base threshold alone cannot prevent a recursive child identical to its parent. Check integer rounding, pivot removal and endpoint updates. In half-open binary search, a right branch advances to mid+1; advancing merely to mid can leave a singleton interval unchanged.

### Decision 3. Charge only operations the question measures

A tail copy is an output write, not a head comparison. A base call is a call, not a stored-key inspection. A butterfly produces two outputs, so the butterfly count differs from the output-operation count. Declare the comparison or arithmetic interface before computing an exact total.

### Decision 4. Retain the last-comparison saving in a merge

For nonempty sorted lengths $p,q$, the worst head-comparison count is $p+q-1$, because one side becomes empty before the final output is written. This upper bound may not be attained by the particular input. The write count is exactly $p+q$ for fresh-output merging.

### Decision 5. Sum node savings across all depths

For $N=2^h$, depth j has $2^j$ merges with aggregate size N. Its maximum comparison cost is $N-2^j$, so total maximum is $hN-N+1$. Replacing every level by N loses an exact linear correction and is insufficient for a numerical question.

### Decision 6. Sorted-input counts depend on the implementation

An ordinary merge selects all left keys before right keys when every left key is smaller. Equal halves therefore use N/2 comparisons per depth. A boundary-test implementation can skip merging already ordered runs; its cost must include those tests and cannot inherit the ordinary formula unchanged.

### Decision 7. Stable equality handling is identity-sensitive

For adjacent original runs, select left on equal keys. Child stability and adjacency then prove global stability. For arbitrary interleaved runs, preserve original indices and use them as a secondary key; left-first equality alone is not enough.

### Decision 8. Strict inversion counts do not charge equality

Charge the unconsumed left count only when $R_j<L_i$. The same selected right record has an inversion with every remaining left record, so one linear-time charge represents many pairs. Replacing the strict test by less-than-or-equal overcounts duplicate keys.

### Decision 9. Separate cross and internal inversions

Sorting the halves destroys their original inversion order, so compute their internal counts recursively before adding cross charges. The parent count is left internal plus right internal plus cross. Counting only the merge step omits valid inversions inside the children.

### Decision 10. Use a sufficiently wide inversion counter

The maximum is $N(N-1)/2$, even though an index is at most N. Widen before multiplying N by N−1. A correctly derived formula can still overflow if an implementation first multiplies in a narrow integer type.

### Decision 11. Specify whether the empty interval is feasible

Under the nonempty policy, an all-negative array returns its least negative element. Zero initialization instead admits emptiness. Use a singleton summary $(x,x,x,x)$ and initialize scans from actual data or symbolic negative infinity.

### Decision 12. A best value alone is not a sufficient child answer

The parent's crossing interval needs the left suffix and right prefix. Its future prefix and suffix also need child totals. Store all four quantities; omitting one is only valid after proving it can be recovered from the remaining representation.

### Decision 13. Explain every maximum candidate as a feasible interval

The best parent lies left, right or across the split. These cases produce $B_L$, $B_R$ and $U_L+P_R$. Taking the maximum is correct because the cases are exhaustive and each candidate has a valid witness; a formula without this decomposition hides its correctness premise.

### Decision 14. Associativity permits regrouping, not reversal

Both bracketings summarize the same ordered concatenation, proving associativity. Reversing L and R changes prefixes, suffixes and possibly the best value. A segment-tree query must combine fragments in original position order even when its traversal encounters them differently.

### Decision 15. Declare witness tie rules before reconstruction

The earliest-start/earliest-end witness need not be the shortest interval. Carry endpoints with each candidate and apply the same total ordering in leaf, prefix, suffix and best comparisons. Showing only a correct sum cannot certify the required interval identity.

### Decision 16. Distinguish linear work from logarithmic span

There are N−1 internal combinations in a balanced tree with N singleton leaves. Constant-cost summaries therefore use linear total work and logarithmic span if independent children run in parallel. The span bound does not mean a sequential machine does only logarithmic work.

### Decision 17. Split tied coordinates by rank and identity

An x-value equality can span both children. Partition the maintained y-list using child membership identities, not an x-only predicate. This preserves balance, retains every point exactly once and makes the geometric separation premise unambiguous.

### Decision 18. Return immediately when the child distance is zero

Distance cannot be negative. A duplicate pair already realizes the minimum possible value, so a zero child bound is sufficient. A packing proof dividing by delta must not be applied with delta zero.

### Decision 19. Color strip cells by recursive half

Within-child separation is at least delta; cross-child separation can be smaller. The one-point-per-cell proof therefore uses four cells per child half, with consistent boundary ownership. An unrestricted cell crossing the divider can contain two close points from different children.

### Decision 20. Maintaining y-order is part of the complexity proof

Linear filtering and bounded-neighbor scanning give a linear toll. Sorting at every node introduces an N log N toll and yields N log-squared N total. A geometric correctness proof alone does not establish the faster running time.

### Decision 21. Widen coordinate arithmetic before squaring

With coordinates in $[-K,K]$, squared distance can reach $8K^2$. Compute differences and squares in a type capable of that bound. Avoiding square roots improves comparisons but does not prevent integer overflow.

### Decision 22. Radix shifts use the chosen low-part width

If the low part has m digits, reconstruction uses $b^m$ and $b^{2m}$. This holds for odd total widths and differently sized operands. Rounding a half-width in one place but not another changes the represented integer.

### Decision 23. Account for the extra sum digit

The Karatsuba sum product can require one extra bit in each operand. The real bit-cost recurrence is an inequality with rounded and expanded widths. The ideal exact-half leaf count is a teaching model, not a literal count for every carry-sensitive implementation.

### Decision 24. Signed differences require signed multiplication

The difference product may be negative. Its subtraction in $z_1=z_2+z_0-d$ must preserve that sign. Taking an absolute value without restoring it changes the mixed coefficient and the final product.

### Decision 25. Distinguish product leaves from bit operations

A complete ternary recursion of h levels has $3^h$ leaves. Linear-width additions and shifts also occur internally. The asymptotic bit-cost result follows after summing those costs; a leaf count alone is not a complete bit-complexity proof.

### Decision 26. Never commute Strassen blocks during expansion

Distributivity and additive cancellation suffice for Strassen's identities. Matrix blocks need not commute. Keep every left-input block before its right-input partner; scalar spot checks cannot detect an illegal swap that becomes wrong for matrix blocks.

### Decision 27. Subtraction restricts the arithmetic domain

Strassen's displayed formulas require additive inverses. They do not directly apply to every semiring, such as Boolean OR/AND. State the domain before transferring a multiplication identity to a graph or logical matrix problem.

### Decision 28. Recursively saving a product changes the exponent

Seven half-side products at every level yield $7^h$ scalar leaves and exponent $\log_2 7$. Saving one product only at the root changes a constant. The addition toll remains quadratic in side length at each node and must be summed too.

### Decision 29. Padding preserves asymptotics but costs storage

Padding a square side to the next power of two multiplies it by less than two and preserves the asymptotic exponent. Zero-pad both inputs and crop the output. Temporary matrices and padding can still increase practical memory and running-time constants substantially.

### Decision 30. A transform root must have exact order

The equation $\omega^N=1$ alone is insufficient. A primitive root provides N distinct evaluation points and a half-order squared root at the next level. Root 1 is the simplest counterexample to invertibility when N exceeds one.

### Decision 31. Butterfly output indices matter

The plus output belongs to k and the minus output to k+N/2. Even and odd refer to coefficient positions, not coefficient values. Misplacing the outputs or splitting by value parity changes the transform even if the number of operations looks correct.

### Decision 32. Keep the inverse root and normalization together

Under the positive-exponent forward convention, inversion uses the negative-exponent root and division by N. Omitting the normalizer returns N times the input. In a finite field, replace division by the multiplicative inverse of N and verify that it exists.

### Decision 33. Count butterflies as two-output units

Each level contains N/2 butterflies and radix-two depth is h, giving $hN/2$. A butterfly usually has a twiddle multiplication and an addition/subtraction pair, with special twiddles sometimes optimized. Do not confuse this abstract count with a particular machine-instruction count.

### Decision 34. An unnormalized DFT scales norm

For the complex Fourier matrix, $F^*F=NI$. The norm grows by square root N, whereas the normalized transform is unitary. Energy or rotation arguments must use the declared normalization; invertibility alone does not imply norm preservation.

### Decision 35. Pad according to coefficient length, not largest degree alone

Lengths r and s require at least r+s−1 positions. Their degrees are r−1 and s−1, so the product degree is at most r+s−2. A transform length equal only to that degree loses the last coefficient through wraparound.

### Decision 36. Index aliasing and residue ambiguity are independent

Insufficient length adds coefficients at congruent indices. Insufficient modulus makes distinct admissible coefficient values share a residue. Increasing the modulus repairs only the second issue; increasing transform length repairs only the first.

### Decision 37. Justify exact integer recovery

For signed coefficient bound C, modulus product above 2C is sufficient for centered CRT recovery. Each NTT prime must separately admit a primitive root of the chosen length. For floating FFT recovery, an error bound below one-half is needed before rounding can be claimed exact.

### Decision 38. Distinguish strict pivot certificates from inclusive counts

With 2t+1 full five-key groups and distinct keys, each side has at least 3t+2 strict keys. The pivot's own group supplies two strict keys, not three. Partial groups and duplicates change the argument; three-way partitioning preserves equality correctly.

### Decision 39. Count the unsuccessful base call separately

In a perfect tree with $2^h-1$ keys, an unsuccessful path has h key inspections and h+1 calls including the empty child. Equality-plus-order interfaces may use two primitive tests per inspected key. The question's operation definition selects which count is relevant.

### Decision 40. Certify both the general argument and the numerical instance

An exact trace validates a specific answer; an invariant, exhaustive case decomposition or algebraic identity establishes its general mechanism. For each option, check assumptions, equality behavior, base region and measured object. A wrong option often counts writes as comparisons, charges equal inversions, drops normalization, wraps coefficients or includes the pivot in a strict side. Explain the specific error rather than dismissing it as obviously false.

### A complete examination workflow

First rewrite the specification with length, domain, ordering, equality and output-witness policy. Next identify executed children and prove strict shrinkage. Then derive the combination invariant and the information it requires. Count the requested operation, including exact base and tail treatment. Solve or sum the resulting recurrence under its declared input family. Finally check a small boundary input, a duplicate or negative case when admissible, and each proposed option. This procedure turns a remembered formula into a defensible solution.
