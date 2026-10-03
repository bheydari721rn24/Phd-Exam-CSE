## Teaching through formulas and conceptual decisions

### Convert a combine operation into a numerical contract

Merging sorted arrays of lengths$p,q$ needs at most$p+q-1$ key comparisons when both are nonempty. Remaining items are copied without comparing after one side is exhausted. For strict inversion counting, emitting a right item smaller than the current left item creates one inversion with every remaining left item. Equality must not trigger that count.

For maximum-subarray summaries, each child returns total$T$, best nonempty prefix$P$, suffix$S$ and interval$B$. Concatenating left$X$ and right$Y$ gives total$T_X+T_Y$, prefix$\max(P_X,T_X+P_Y)$, suffix$\max(S_Y,T_Y+S_X)$ and best$\max(B_X,B_Y,S_X+P_Y)$. The crossing term is a suffix plus a prefix, not the sum of child best intervals. A nonempty contract returns the largest negative singleton for an all-negative array; an empty-allowed contract returns zero.

### Compare arithmetic algorithms in the same model

Ordinary recursive digit multiplication uses four half-size products, giving quadratic work. Karatsuba computes three, giving exponent$\log_23$. Strassen changes eight block multiplications to seven, giving exponent$\log_27$. These exponents assume linear digit additions for Karatsuba and quadratic matrix-block additions for Strassen. Constant-cost whole-number arithmetic or an incompatible representation asks a different question.

For unequal digit lengths, align low-part widths before applying reconstruction; for odd widths, use the actual low width$m$ in the shifts$B^m,B^{2m}$. Matrix blocks need their multiplication order preserved because they do not generally commute. Padding can increase operation counts even though it does not change the asymptotic exponent for bounded-factor padding.

### Fourier size and sign conventions determine the answer

Coefficient lengths$r,s$ have linear convolution length$r+s-1$. A power-of-two transform must choose$N\ge r+s-1$ to avoid wraparound. Without enough padding, cyclic convolution aliases high-degree coefficients into lower positions. Under a forward transform using$\omega^{jk}$, the inverse uses$\omega^{-jk}/N$. Omitting the normalization multiplies recovered coefficients by$N$; using the wrong sign permutes their phase structure.

## Formula and conceptual problem bank

### Question 1. Merge comparison bound

Two sorted nonempty arrays have lengths4 and6. What is the worst-case number of key comparisons for the usual two-pointer merge?

**A.** 6

**B.** 9

**C.** 10

**D.** 24

**Answer: B.**

The worst case keeps both arrays nonempty until only one item remains, using$4+6-1=9$ comparisons. Every comparison emits one item, and the last item requires only copying. The output still has ten writes under an explicit-output contract; key comparisons and writes are different counts.

### Question 2. Strict cross inversions

Merge left$[2,4,7]$ with right$[1,4,6]$. How many strict cross inversions exist?

**A.** 4

**B.** 5

**C.** 6

**D.** 9

**Answer: B.**

Right1 is smaller than all three left items and contributes3. Right4 is smaller only than left7 and contributes1; equality with left4 is not an inversion. Right6 is also smaller only than7 and contributes1. Total5. Counting only the first equal-key comparison can incorrectly lose the later7-versus4 inversion.

### Question 3. Four-summary combine

Left summary$(T,P,S,B)=(6,6,8,8)$ and right summary$(-3,1,5,5)$ use nonempty subarrays. What is the combined summary?

**A.** (3,7,5,9)

**B.** (3,6,8,8)

**C.** (3,7,13,13)

**D.** (3,1,5,8)

**Answer: A.**

Total is3. Prefix is$\max(6,6+1)=7$. Suffix is$\max(5,-3+8)=5$. Best interval is$\max(8,5,8+1)=9$. The crossing best uses the left suffix and right prefix, not the two child best intervals. Compute each field separately; different fields can have different winning witnesses.

### Question 4. All-negative contract

For array$[-8,-3,-5]$, what is the maximum nonempty subarray sum?

**A.** -16

**B.** -8

**C.** -3

**D.** 0

**Answer: C.**

Adding any other negative entry makes a selected interval sum smaller. The best nonempty interval is the singleton$[-3]$, giving$-3$. Zero is valid only when an empty interval is allowed. The word nonempty determines initialization and invalidates the common zero-initialized maximum shortcut.

### Question 5. Sufficient child information

Why is returning only each child’s best subarray sum insufficient for a correct divide-and-conquer combine?

**A.** The arrays must be sorted.

**B.** A crossing optimum needs left suffix and right prefix information.

**C.** The recursive calls must overlap.

**D.** Every child best must be negative.

**Answer: B.**

The optimal parent interval can cross the split and then consists of a suffix of the left child followed by a prefix of the right. A child’s best internal interval may touch neither boundary. Therefore its value cannot reconstruct the required crossing candidate. This information gap motivates the four-field summary and is independent of whether inputs are positive or negative.

### Question 6. Closest-pair strip

Recursive halves each have minimum distance at least$\delta>0$. Which cross pair can improve$\delta$?

**A.** Any pair regardless of its horizontal coordinates.

**B.** Only pairs with both endpoints within$\delta$ of the divider.

**C.** Only pairs in the left half.

**D.** Only pairs already compared recursively.

**Answer: B.**

If a cross pair has distance below$\delta$, its horizontal separation is below$\delta$. Each endpoint’s horizontal distance from the divider is at most that separation, so both lie in the strip. This is a necessary filter, not proof that every strip pair improves the minimum. Same-half pairs have already been bounded by the recursive result.

### Question 7. Packing successor bound

In the standard closest-pair strip sorted by vertical coordinate, the half-specific packing argument permits comparison with at most how many later points per point?

**A.** 3

**B.** 6

**C.** 7

**D.** All remaining points.

**Answer: C.**

The relevant height-$\delta$ window has four small cells per half, each of diameter below$\delta$ under consistent boundary treatment. At most one point from each recursive half lies in each half-specific cell. There are at most eight points including the current point, hence seven successors. The same-half separation premise is essential; it does not constrain cross-half closeness.

### Question 8. Karatsuba exponent

Three half-size digit multiplications and linear combine work give which tight order?

**A.** $\Theta(n)$

**B.** $\Theta(n\log n)$

**C.** $\Theta(n^{\log_23})$

**D.** $\Theta(n^2)$

**Answer: C.**

The recurrence is$T(n)=3T(n/2)+\Theta(n)$. The leaf exponent$\log_23$ exceeds1, so recursive multiplication dominates and the total has that power. Four half-size products would give exponent2. The stated digit model charges linear addition and shifting work rather than treating arbitrarily long integers as unit words.

### Question 9. Karatsuba reconstruction

With decimal low width1, let$x=23,y=45$. The high product is8, low product15, and difference product$(2-3)(4-5)=1$. What is the mixed coefficient?

**A.** 7

**B.** 15

**C.** 22

**D.** 24

**Answer: C.**

The mixed coefficient is$z_2+z_0-z_d=8+15-1=22$. Reconstruction gives$8\cdot100+22\cdot10+15=1035$, equal to23 times45. Adding rather than subtracting the difference product gives24 and an incorrect product. The low width1 determines both decimal shifts.

### Question 10. Strassen exponent

Seven half-size block products and quadratic block-addition work give which tight order?

**A.** $\Theta(n^2)$

**B.** $\Theta(n^2\log n)$

**C.** $\Theta(n^{\log_27})$

**D.** $\Theta(n^3)$

**Answer: C.**

The recurrence$7T(n/2)+\Theta(n^2)$ has leaf exponent$\log_27>2$, so the answer is$n^{\log_27}$. The ordinary eight-product block algorithm gives cubic work. The number of added matrices affects constants and storage but not this exponent under the stated dense scalar-operation model.

### Question 11. Zero-padding length

Polynomial coefficient arrays have lengths5 and4. What is the minimum power-of-two transform length avoiding cyclic aliasing?

**A.** 4

**B.** 5

**C.** 8

**D.** 16

**Answer: C.**

The linear convolution has length$5+4-1=8$, corresponding to maximum degree7. The minimum power of two at least8 is8. Using16 is valid but not minimum; using4 or5 wraps some higher-degree contributions into earlier coefficients.

### Question 12. Linear convolution coefficients

What is the coefficient array for multiplying$(1+2x+3x^2)$ by$(4+5x)$?

**A.** [4,13,22,15]

**B.** [4,10,12,15]

**C.** [4,13,15]

**D.** [4,5,6]

**Answer: A.**

Constant is4. The$x$ coefficient is$1\cdot5+2\cdot4=13$. The$x^2$ coefficient is$2\cdot5+3\cdot4=22$, and$x^3$ is$3\cdot5=15$. Polynomial multiplication uses convolution, not entrywise multiplication. The expected length3+2-1=4 supplies a useful dimension check.

### Question 13. Cyclic aliasing

The linear product in Question 12 has coefficients[4,13,22,15]. What length-two cyclic convolution results if coefficients wrap modulo$x^2-1$?

**A.** [4,13]

**B.** [22,15]

**C.** [26,28]

**D.** [17,37]

**Answer: C.**

Degrees0 and2 share the first cyclic position, giving4+22=26. Degrees1 and3 share the second, giving13+15=28. Reducing modulo$x^2-1$ sets$x^2=1$ and$x^3=x$, explaining the wrap. Truncating high coefficients would give a different, incorrect cyclic result.

### Question 14. Fourier inverse normalization

A forward length-eight transform uses$Y_k=\sum_j a_j\omega^{jk}$. The inverse uses the negative exponent but omits division by8. What coefficients are recovered?

**A.** The originals$a_j$.

**B.** $8a_j$.

**C.** $a_j/8$.

**D.** Always zero.

**Answer: B.**

Root orthogonality gives an inner geometric sum equal to8 when indices match and0 otherwise. Without the inverse$1/8$ factor, every coefficient is multiplied by8. The negative exponent fixes orthogonality, but the normalization is a separate required factor.

### Question 15. FFT butterflies

A radix-two length-eight FFT has three stages with four butterflies per stage. How many butterflies execute?

**A.** 7

**B.** 8

**C.** 12

**D.** 24

**Answer: C.**

There are$\log_28=3$ stages and$8/2=4$ butterflies per stage, for12. Twenty-four counts two output values per butterfly rather than butterfly instances. Exact real multiplication counts depend on how special twiddle factors and complex products are implemented.

### Question 16. Presorting versus sorting every level

A closest-pair implementation sorts by vertical coordinate anew at every recursive combine, causing$T(n)=2T(n/2)+\Theta(n\log n)$. What order results?

**A.** $\Theta(n)$

**B.** $\Theta(n\log n)$

**C.** $\Theta(n\log^2n)$

**D.** $\Theta(n^2)$

**Answer: C.**

The extra sorting toll gives$n(h-i)$ at depth$i$ for$h=\log_2n$. Summing across levels yields$n\Theta(h^2)$. Maintaining and linearly merging vertical order reduces the toll to linear and restores$n\log n$. The geometric idea alone does not determine the complexity; representation maintenance is part of the algorithm.

<!-- CHALLENGE-BANK -->

### Question 17. Challenge: A finite-field Fourier evaluation

Work modulo17 with length-four root$\omega=4$. For$a=[1,2,0,0]$ and forward positive exponents, what is$Y$?

**A.** [3,9,16,10]

**B.** [3,10,16,9]

**C.** [1,2,0,0]

**D.** [3,8,15,9]

**Answer: A.**

Powers of4 modulo17 are1,4,16,13; the square is$-1$ and the fourth power is1, so its order is4. Each evaluation is$1+2\omega^k$, producing3,9,33 modulo17=16, and27 modulo17=10. Reversing the exponent sign exchanges the second and fourth values. The inverse normalization uses$4^{-1}=13$ modulo17, not real division by4.

### Question 18. Challenge: Exact modular recovery range

An integer coefficient is known only to lie in$[-10,10]$, and its residue modulo17 is7. Is its exact value uniquely determined?

**A.** Yes, it must be7.

**B.** Yes, it must be-10.

**C.** No, both7 and-10 fit.

**D.** No value in the range fits.

**Answer: C.**

Values7 and$7-17=-10$ share the residue and both lie in the allowed interval. Unique centered recovery needs a modulus greater than the full coefficient-range width20, or additional information excluding one candidate. Exact modular arithmetic prevents rounding error but does not by itself prevent integer aliasing. More CRT moduli can enlarge the combined modulus enough to distinguish the possibilities.

## Applicable formulas and examination notes

### 1. Merge comparisons and writes

For two nonempty sorted inputs of lengths$p,q$, worst-case key comparisons are$p+q-1$ and output writes are$p+q$. An exhausted side requires copying but no further key comparison. Exact operation categories must remain separate.

### 2. Strict inversion charge

When a right item is strictly smaller than the current left item, charge every remaining left item. Equal keys are not strict inversions. Left[2,4,7] and right[1,4,6] have cross count3+1+1=5.

### 3. Nonempty maximum subarray

An all-negative array returns its least-negative singleton under a nonempty contract. Empty-allowed versions can return0. Initialize and combine according to the chosen contract rather than assuming all maxima are nonnegative.

### 4. Crossing summary

Parent best is$\max(B_X,B_Y,S_X+P_Y)$. Child best sums alone cannot reconstruct a crossing interval. Prefix and suffix fields identify boundary-touching candidates; totals allow extensions across an entire child.

### 5. Order of summary composition

Four-field concatenation summaries are associative because they represent the same joined sequence, but concatenation is not commutative. Reversing children changes prefixes, suffixes and interval witnesses even if some numeric fields coincide.

### 6. Closest-pair strip

Any cross pair improving$\delta$ has both endpoints within$\delta$ of the divider and vertical separation below$\delta$. These are necessary filters. Tied divider coordinates retain their recursive-half membership in the packing proof.

### 7. Seven successors

The half-specific packing window holds at most eight points including the current one, giving seven later candidates. The proof assumes same-half separation and a consistent cell-boundary convention. Coincident points yield distance0 and need early handling.

### 8. Preserved vertical order

Presort and maintain vertical order through linear partitioning or merging to obtain$n\log n$. Sorting afresh at every combine adds a logarithmic factor. Sorting costs must appear in the recurrence rather than disappear from the algorithm description.

### 9. Karatsuba difference identity

Mixed coefficient is$z_2+z_0-z_d$ for$z_d=(x_H-x_L)(y_H-y_L)$. With23 and45 it is22. Signed intermediate differences are valid; their product sign must be retained.

### 10. Digit widths

Use the actual common low width$m$ in$B^m$ and$B^{2m}$. Odd-length splits need not have equal digit counts. Linear combine costs rely on a digit representation; unit-cost arbitrary-precision multiplication is a different model.

### 11. Strassen block order

Block products do not commute. Preserve their factor order while verifying every output block. Seven products give exponent$\log_27$ with quadratic additions; exchanging a factor may leave scalar examples correct while breaking matrix cases.

### 12. Padding overhead

Polynomial lengths$r,s$ require$N\ge r+s-1$. Square matrix power-of-two padding raises dimensions by less than a factor2 but changes exact costs. An asymptotic exponent does not justify ignoring a large constant for small instances.

### 13. Convolution check

Coefficient$k$ is$\sum_i a_i b_{k-i}$ over valid indices. For[1,2,3] and[4,5], the result is[4,13,22,15]. Verify output length and one boundary coefficient before trusting a transform calculation.

### 14. Cyclic wrap

Insufficient padding reduces degrees modulo$N$ under$x^N-1$, adding aliased coefficients. Length-two wrap of[4,13,22,15] gives[26,28]. It is cyclic reduction, not simple truncation.

### 15. Fourier signs and scale

A forward positive-exponent convention pairs with inverse negative exponent and factor$1/N$. Omitting scale recovers$Na_j$. State the root order and sign convention before evaluating butterfly or inverse formulas.

### 16. FFT work and arithmetic reliability

Radix-two FFT has$(N/2)\log_2N$ butterflies. Each shares a twiddle multiplication across two outputs. Floating recovery requires an error margin before integer rounding; exact NTT recovery requires a suitable root and sufficient modulus or CRT range.

<!-- BOUNDARY-NOTES -->

### 17. Binary-search comparisons

Specify whether each iteration uses one three-way comparison or separate less-than and equality tests. Halving interval length gives logarithmic iterations, but exact key-comparison counts depend on that interface and on inclusive versus half-open bounds.

### 18. Witnesses and ties

Equal optimum values can have different interval endpoints or closest-pair identities. Define a deterministic tie rule if a unique witness is required. Correct optimum value alone does not certify a requested lexicographically first or shortest witness.

### 19. Numerical versus exact transforms

A floating FFT plus rounding needs a justified error bound smaller than the distance to a competing integer. An NTT needs a root of the specified order and a modulus or CRT product sufficient to distinguish possible coefficients. Passing small numerical tests does not provide a general exactness guarantee.
