## Final review: complete decisions, formulas, and failure checks

These rules support reconstruction after the full lesson. Every formula below belongs to a specified outcome model. A count becomes a probability only after the weights of elementary outcomes are justified.

### 1. Specify the outcome before its count

Record distinct versus indistinguishable objects, named versus unnamed positions, order, replacement, and the restriction. Five draws from four labels give $4^5=1024$ words but only $\binom83=56$ multiset summaries. Changing the description changes the answer. Never infer a uniform law from the number of summaries alone.

### 2. Products need constant continuation counts

If every first-stage choice has $b$ second-stage continuations, $a$ first choices yield $ab$ outcomes. Otherwise use a sum of branch counts. In Question 1, 21 triples each allow 16 pairs, giving 336. In Question 20, different bounded-coordinate values leave different residual totals, so the continuation counts must be added individually.

### 3. Sums need disjoint cases

Partition by an exact category count or a unique first occurrence. Question 73 partitions by three or four algebra selections, contributing 100 and 50. Adding overlapping witness events counts some outcomes repeatedly. Use inclusion–exclusion or choose the exact category before summing.

### 4. A factorial divisor must name an erased symmetry

Pairing $2n$ labels removes $2^n$ internal orientations and $n!$ block orders. Ten labels therefore have $10!/(2^5 5!)=945$ pairings. Keeping either symmetry changes the outcome. Demonstrate the constant fiber size instead of dividing because the resulting number looks plausible.

### 5. Repetition can make fibers unequal

A multiplicity vector has $n!/\prod c_i!$ word preimages. Under independent uniform draws from $r$ types, its mass is $n!/(r^n\prod c_i!)$. Three binary draws give masses $1,3,3,1$ divided by eight. Uniform multisets would require a separately specified mechanism.

### 6. Named bins remain named even at equal sizes

Three named groups of size $n$ have $(3n)!/(n!)^3$ partitions. Only genuinely unnamed nonempty groups add a divisor $3!$. At $n=1$, there are six named assignments but one unnamed partition. Empty groups require a stabilizer check; the positive-size formula cannot be extended blindly to zero.

### 7. Lower bounds change the total

For $x_i\ge L_i$ and total $T$, use residual $R=T-\sum L_i$. When $R\ge0$, $r$ named coordinates have $\binom{R+r-1}{r-1}$ allocations. Total ten with lower bounds $2,1,3$ gives residual four and count 15. A negative residual means zero outcomes.

### 8. Total inequalities need one slack coordinate

For $r$ nonnegative coordinates totaling at most $T$, append $s=T-\sum x_i\ge0$. This is a bijection, so the count is $\binom{T+r}r$. Three coordinates totaling at most five give $\binom83=56$. Summing only allocations with equality omits smaller totals.

### 9. Upper bounds are violated at one beyond the limit

A cap $y_i\le U$ is first violated at $U+1$. Four nonnegative coordinates totaling eight with cap four give $\binom{11}3-4\binom63=85$, because two violations require ten units and are impossible. Shifting by four would incorrectly remove permitted boundary values.

### 10. Several caps require overlap corrections

For a set of violators $J$, subtract the sum of their first-forbidden thresholds from the residual and apply stars and bars if it remains nonnegative. Alternate signs by $|J|$. Four coordinates totaling ten with cap three give $\binom{13}3-4\binom93+6\binom53=10$. Subtracting singleton violations alone counts intersections incorrectly.

### 11. Parity changes a coefficient, not just a proportion

Writing $x=2a$ preserves the equation's factor two. For $x+y+z=2n$, even $x$ gives $(n+1)^2$, odd $x$ gives $n(n+1)$. At total ten these are 36 and 30. A one-half shortcut needs an actual constraint-preserving bijection and fails here.

### 12. Floors preserve the last admissible endpoint

For $2a+c=R-b$, the count is $\max(0,\lfloor(R-b)/2\rfloor+1)$. The plus one counts zero. Question 68 gives row sizes $9,8,8,7$, totaling 32. Rounding to the nearest integer or using the same endpoint in every row changes the event.

### 13. Weakly increasing maps are multiplicity vectors

A weakly increasing length-$m$ sequence on $r$ ordered values has $\binom{m+r-1}{r-1}$ possibilities. Its counts reconstruct it uniquely. Five positions and five values give 126. Strict increase gives $\binom rm$ instead; arbitrary order gives $r^m$.

### 14. Requiring a value shifts its multiplicity

If a sorted sequence must use a specified value, subtract one from that value's count. Four positions over three values containing 2 give $\binom52=10$. The unrestricted 15 includes five sequences avoiding 2. The shift counts occurrence, not a choice of witness position.

### 15. At least a category count means a sum

Choosing five objects from $n$ red and $n$ blue with at least three reds gives $\binom n3\binom n2+n\binom n4+\binom n5$. For $n=5$ this is 126. The exactly-three-red term alone is 100. Two simultaneous category bounds restrict the feasible sum further.

### 16. Equal-color symmetry has a tie condition

For equal population sizes and an odd selection size, color swapping pairs red-majority with blue-majority subsets, so each class is half the total. Five of ten objects give $\binom{10}5/2=126$. For an even selection size, ties form a third class and must be counted before halving the remainder.

### 17. Witnesses may count outcomes unevenly

A mixed four-subset with $r$ odds has $r(4-r)$ odd-even witness pairs: three when $r=1,3$ and four when $r=2$. A witness count has no constant divisor here. Count the complement instead: among ten labels the mixed four-subsets number $\binom{10}4-2\binom54=200$.

### 18. Surjections forbid all empty-target events

For $m\ge1$ objects and $r$ named targets, onto maps number $\sum_{j=0}^r(-1)^j\binom rj(r-j)^m$. Six to four give 1560. Stars and bars counts size profiles rather than assignments; multiply each profile by its multinomial count if using that route.

### 19. An exact fiber avoids multiple witnesses

If the first target must receive at least two objects, choose its entire fiber of size $k$, then count onto maps of the remainder. Five to three with this restriction give $\binom52(2^3-2)+\binom53(2^2-2)=80$. Choosing two witnesses overcounts a three-object fiber three times.

### 20. Parity filters use both signed and unsigned sums

For one distinguished symbol in a four-symbol alphabet, $E+O=4^n$ and $E-O=2^n$. Thus $E=(4^n+2^n)/2$. At length five this is 528, not 512. Three symbols instead give $E=(3^n+1)/2$ for positive length; handle the empty word directly.

### 21. Coefficients require an integer exponent solution

In $(x^a+x^b)^m$, solve $bm+(a-b)j=s$ with integer $0\le j\le m$ before writing $\binom mj$. In $(x^2+x^{-1})^{14}$, exponent 14 would need $j=28/3$, so its coefficient is zero. A range check without the congruence check is insufficient.

### 22. Marked-subset sums can be counted in two orders

The identity $\binom nk\binom kr=\binom nr\binom{n-r}{k-r}$ counts $R\subseteq K$. Summing over $k$ gives $\binom nr2^{n-r}$. For $n=9,r=3$, the result is 5376. Omitting the marked subset counts a different object.

### 23. Nonadjacent fixed-weight positions compress gaps

With $j$ nonadjacent ones in length $n$, $q_i=p_i-(i-1)$ gives $\binom{n-j+1}j$ words when feasible. Length eight with three ones gives $\binom63=20$. This is not the count over every weight. Circular endpoints add an extra constraint.

### 24. The all-weight recurrence needs both seeds

The no-adjacent-one count satisfies $T_n=T_{n-1}+T_{n-2}$ for $n\ge2$, with $T_0=1,T_1=2$. Thus $T_8=55$. An empty suffix has one construction, and setting its count to zero loses words such as 10 at length two.

### 25. Circular order erases an origin

For $n\ge1$ distinct labels, rotations identified and reflections retained give $(n-1)!$. Five labels give 24. Reflection identification halves this for $n\ge3$, with small cases checked separately. Repeated labels have variable orbit sizes and require a general orbit argument.

### 26. Linear adjacency creates reversible blocks

For $n$ distinct couples adjacent in a row, the count is $2^n n!$. Five couples give 3840. In a circle the factor changes to $(n-1)!$ for $n\ge2$, and the single-couple circle has one outcome. Internal orientation remains visible in a row.

### 27. Derangements exclude every fixed-position event

Use $D_n=n!\sum_{j=0}^n(-1)^j/j!$, with $D_0=1,D_1=0$. Five labels give 44. Removing only the identity leaves many permutations with fixed points. One full cycle is sufficient for derangement but not necessary.

### 28. Exactly fixed means derange the rest

Exactly $k$ fixed points gives $\binom nkD_{n-k}$. Five labels with exactly two fixed points give 20. Exactly four fixed points give zero, because the last label is forced fixed. Freely permuting the remainder counts additional fixed points.

### 29. Sampling weights decide binomial versus hypergeometric

Uniform sampling of $m$ distinct objects without replacement gives $\binom Kk\binom{N-K}{m-k}/\binom Nm$. Independent equal-probability trials give $\binom mkp^k(1-p)^{m-k}$. Twelve objects with five marked and a size-four sample give exactly two marked probability $14/33$. Marginal equality alone does not justify independent trials.

### 30. Equal independent counts need a convolution

For independent fair-toss blocks of lengths $a,b$, equality probability is $2^{-(a+b)}\sum_k\binom ak\binom bk=\binom{a+b}b/2^{a+b}$. Eight and five tosses give $1287/8192$. The denominator includes both blocks; a uniform distribution on head counts is false.

### 31. Independence has an exact logical scope

Two events require $P(A\cap B)=P(A)P(B)$. Mutual independence requires every subfamily; pairwise tests alone fail for xor-derived fair bits. Conditional ratios additionally need positive conditioning mass. Disjoint positive-mass events are dependent, while null events are independent of every event by the product definition.

### 32. Conditioning and stopping need a declared law

Conditioning two fair bits on at least one one leaves three equiprobable pairs and creates dependence. Revealing a hidden coin type can remove mixture dependence. In repeated independent trials with category probabilities $a,b$ and $a+b>0$, a neutral-trial race has probability $a/(a+b)$; its geometric sum begins at exponent zero. If $a=b=0$, no relevant event occurs and the ratio is undefined. Recheck assumptions whenever information or the sampling mechanism changes.

### Final reconstruction check

For any new problem, write its outcome contract, test feasibility, select a reversible construction or a disjoint partition, justify every quotient and probability weight, calculate exactly, and check a second route or boundary. The chapter develops those skills within its stated scope. Recorded source checks and finite enumerations support the derivations; they do not certify literal universal completeness or success on every unseen examination question.
