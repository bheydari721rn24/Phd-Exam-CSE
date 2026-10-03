## Teaching through formulas and conceptual decisions

### Recover all four atomic probabilities

Given $P(A)=a$, $P(B)=b$ and $P(A\cap B)=t$, the four disjoint masses are $t,a-t,b-t,1-a-b+t$. Nonnegativity yields $\max(0,a+b-1)\le t\le\min(a,b)$. This inequality is both necessary and sufficient: if it holds, the four numbers define a valid law on four atoms. Thus feasibility questions can be solved without guessing independence.

The union is $a+b-t$, exactly one is $a+b-2t$, neither is $1-a-b+t$, and $A$ without$B$ is$a-t$. These are distinct events. A diagram of the four regions determines the coefficient of$t$ and is safer than memorizing ambiguous phrases such as “either.” When the question says “either but not both,” it means symmetric difference.

### A count ratio requires equally likely elementary outcomes

If a fair die's outcomes are grouped into parity, the two groups are equally likely because each contains three equally likely faces. Grouping into “one” versus “not one” creates masses1/6 and5/6, not1/2 each. For a nonuniform finite law, sum the masses of favorable elementary outcomes. A probability density at a point is not its point probability.

### Infinite sums and limiting events

For a countable discrete law $p_k=c/2^k$ for$k\ge1$, normalization uses the convergent geometric series and gives$c=1$. For a uniform point on$[0,1]$, an interval's mass is its length while every singleton has probability zero. Countable unions of null singletons remain null, but the uncountable union of every singleton is the whole interval. Countable additivity deliberately does not extend to arbitrary uncountable sums.

For increasing measurable events, $P(\bigcup A_n)=\lim P(A_n)$; for decreasing ones, $P(\bigcap A_n)=\lim P(A_n)$ in a probability space. A moving interval sequence can have empty intersection even when each individual interval has positive mass. “Infinitely often” is an intersection of tail unions, while “eventually always” is a union of tail intersections.

## Formula and conceptual problem bank

### Question 1. Recover a union

$P(A)=0.6$, $P(B)=0.5$ and $P(A\cap B)=0.2$. Find $P(A\cup B)$.

**A.** 0.3

**B.** 0.7

**C.** 0.9

**D.** 1.1

**Answer: C.**

Count each singleton probability once and subtract the overlap counted twice: $0.6+0.5-0.2=0.9$. The outside mass is0.1, confirming feasibility. The sum1.1 is not a valid union probability because the events overlap. Difference0.3 instead counts $B\setminus A$, and0.7 counts exactly one event.

### Question 2. Exactly one versus at least one

With the data in Question 1, what is the probability of exactly one of$A,B$?

**A.** 0.2

**B.** 0.7

**C.** 0.9

**D.** 0.1

**Answer: B.**

The exclusive masses are $0.6-0.2=0.4$ and $0.5-0.2=0.3$. They are disjoint, so their sum is0.7. The union probability0.9 still includes the0.2 intersection. The outside probability0.1 means neither, and0.2 means both. Translate the phrase into disjoint regions before using numbers.

### Question 3. Sharp intersection range

If $P(A)=0.7$ and $P(B)=0.6$, which is the exact feasible range for$P(A\cap B)$?

**A.** [0,0.6]

**B.** [0.3,0.6]

**C.** [0.42,0.6]

**D.** [0.3,0.7]

**Answer: B.**

The union cannot exceed1, requiring $t\ge0.7+0.6-1=0.3$. The intersection cannot exceed either event, requiring $t\le0.6$. Every$t$ in this range gives nonnegative four-region masses and is realizable. The value0.42 assumes independence, which is not supplied. A allows a negative outside mass for small$t$.

### Question 4. An inconsistent table

Which triple $(P(A),P(B),P(A\cap B))$ is impossible?

**A.** (0.8,0.7,0.6)

**B.** (0.3,0.5,0.1)

**C.** (0.8,0.7,0.4)

**D.** (0.3,0.5,0.3)

**Answer: C.**

ForC, the union would be $0.8+0.7-0.4=1.1$ and the outside mass would be$-0.1$. The necessary lower intersection bound is0.5. All other triples satisfy both the lower bound and the upper minimum bound. Feasibility needs all four disjoint masses nonnegative; checking only that every given number lies in[0,1] is insufficient.

### Question 5. Nonuniform elementary outcomes

A law on outcomes1,2,3,4 assigns probability proportional to the outcome number. What is the probability of an even outcome?

**A.** 1/2

**B.** 3/5

**C.** 2/5

**D.** 1/4

**Answer: B.**

The normalization denominator is $1+2+3+4=10$. The even outcomes carry mass $(2+4)/10=3/5$. Counting two favorable labels out of four gives1/2 only for a uniform law. Neither the number of labels nor the name of the event changes the assigned masses.

### Question 6. A grouped experiment

A fair die is recorded as “one” or “not one.” What is the probability of “one”?

**A.** 1/2

**B.** 1/6

**C.** 1/3

**D.** 5/6

**Answer: B.**

The elementary outcomes are the six equally likely faces. Exactly one maps to the first recorded label, so its mass is1/6. Grouping changes the labels but does not reassign equal probability to the two groups. The complementary label has five preimages and probability5/6.

### Question 7. Normalize an infinite discrete law

For $k=1,2,\ldots$, $P(\{k\})=c/2^k$. What is$c$?

**A.** 1/2

**B.** 1

**C.** 2

**D.** No finite value.

**Answer: B.**

The geometric sum from$k=1$ is $1/2+1/4+\cdots=1$. Total mass is therefore$c$, which must equal1. Starting the sum at zero would give2 and a different normalization. Nonnegative masses and a sum of1 define the discrete probability law.

### Question 8. A tail probability

Under the law of Question 7, what is $P(\{4,5,6,\ldots\})$?

**A.** 1/16

**B.** 1/8

**C.** 1/4

**D.** 1/2

**Answer: B.**

The tail begins with1/16 and has ratio1/2. Its sum is $(1/16)/(1-1/2)=1/8$. OptionA counts only the first point. The equivalent complement computation subtracts $1/2+1/4+1/8=7/8$ from1, giving the same result.

### Question 9. Uniform continuous length

$X$ is uniform on$[0,1]$. What is $P(1/4<X\le3/4)$?

**A.** 0

**B.** 1/4

**C.** 1/2

**D.** 3/4

**Answer: C.**

The interval length is $3/4-1/4=1/2$. Each endpoint has probability zero, so open or closed endpoints do not change this value. Zero is the mass of one specified point, not of an interval containing uncountably many points. Counting endpoints as separate positive atoms would be inconsistent with the uniform continuous law.

### Question 10. A decreasing sequence

For uniform$X$ on$[0,1]$, let $A_n=\{0<X<1/n\}$. What is $P(\bigcap_{n=1}^{\infty}A_n)$?

**A.** 0

**B.** 1

**C.** 1/2

**D.** It does not exist.

**Answer: A.**

No positive real number is less than1/n for every$n$, and zero is excluded. The intersection is empty and has mass zero. Alternatively the sequence decreases and $P(A_n)=1/n\to0$, so continuity from above gives zero. Every individual event having positive probability does not force a positive intersection probability.

### Question 11. A union bound

For events $E_1,E_2,E_3$ with probabilities0.1,0.2,0.25 and no overlap data, which upper bound on their union is guaranteed?

**A.** 0.05

**B.** 0.25

**C.** 0.55

**D.** Exactly0.55.

**Answer: C.**

Finite subadditivity gives $P(E_1\cup E_2\cup E_3)\le0.1+0.2+0.25=0.55$. This is an upper bound, not an equality; nested events could have union0.25. It is sharp if the three events are disjoint, which is feasible since the total is below1. The largest individual mass is a lower bound on the union, not an upper bound.

### Question 12. Finite information partitions

A sigma-algebra on a finite sample space is generated by a partition into three nonempty atoms. How many events does it contain?

**A.** 3

**B.** 6

**C.** 8

**D.** 9

**Answer: C.**

Every measurable event is a union of partition atoms, and every choice of included atoms gives one event. Three independent yes/no choices yield $2^3=8$. The empty event and the full space are included. Counting only the three atoms omits their unions and violates closure of the event family.

<!-- CHALLENGE-BANK -->

### Question 13. Challenge: Three-event feasibility

Three events each have probability0.5 and every pair intersection has probability0.3. What is the exact feasible interval for triple-intersection probability$t$?

**A.** [0,0.3]

**B.** [0.1,0.3]

**C.** [0.2,0.5]

**D.** Only0.125.

**Answer: B.**

The triple atom has mass$t$, each pair-only atom has$0.3-t$, each single-only atom has$0.5-0.3-0.3+t=t-0.1$, and the outside atom has$1-1.5+0.9-t=0.4-t$. All eight masses must be nonnegative, yielding$t\ge0.1$ and$t\le0.3$. These masses sum to1 and construct a law for every$t$ in that interval, proving sufficiency as well as necessity. The independence guess0.125 does not reproduce the supplied pair masses.

### Question 14. Challenge: Mixed discrete and continuous mass

A law puts probability1/4 exactly at0 and distributes the remaining3/4 uniformly on$[0,1]$. What is$P(X\le1/2)$?

**A.** 1/4

**B.** 3/8

**C.** 1/2

**D.** 5/8

**Answer: D.**

The point atom at0 belongs to the event and contributes1/4. The continuous component contributes$(3/4)(1/2)=3/8$. Their sum is5/8. The singleton0 has mass1/4 under this mixed law, even though the uniform component assigns it zero. Treating the whole distribution as uniform or forgetting the atom loses the mixture contract.

## Applicable formulas and examination notes

### 1. Four-region reconstruction

Use$t,a-t,b-t,1-a-b+t$ for both, first-only, second-only and neither. With$a=0.6,b=0.5,t=0.2$, these are0.2,0.4,0.3,0.1. Their sum and nonnegativity are independent checks on every computed answer.

### 2. Sharp feasibility

$\max(0,a+b-1)\le t\le\min(a,b)$ is necessary and sufficient for two-event data. For$a=0.7,b=0.6$, the range is[0.3,0.6]. The product$ab$ is just an independence value, not the universal lower bound.

### 3. Exactly one

$P(A\oplus B)=a+b-2t$. Subtract overlap twice because both original masses counted it. The union subtracts it once. “Either” is ambiguous unless the question explicitly specifies inclusive or exclusive meaning.

### 4. Difference and complement

$P(A\setminus B)=a-t$ and $P((A\cup B)^c)=1-a-b+t$. Negating “both” gives the complement of the intersection, whereas negating “at least one” gives the complement of the union.

### 5. Nonuniform mass sums

Use $\sum_{\omega\in E}p_\omega$ for a nonuniform law. For probabilities proportional to1,2,3,4, the even event is6/10. Favorable count divided by total count is valid only when elementary outcomes are equally likely.

### 6. Coarse recording

Grouped labels inherit the total masses of their preimages. Recording one die face versus all other faces produces1/6 and5/6. Two possible labels do not imply equal probability.

### 7. Infinite normalization and tails

For $p_k=2^{-k}$ starting at1, total mass is1 and the tail from$m$ is$2^{1-m}$. Verify the starting index; starting at0 doubles the sum. A tail probability includes all its points, not only its first term.

### 8. Continuous endpoints

For uniform length on$[0,1]$, point masses are zero and interval probabilities equal length. A countable set of specified points is null. The union of uncountably many null singletons can have mass1; countable additivity does not justify an uncountable sum.

### 9. Monotone limits

Increasing events use a union and decreasing events an intersection. For$(0,1/n)$, the intersection is empty and its mass is the limit0. Positive masses at every finite stage do not imply a positive limiting mass.

### 10. Union bounds versus equality

$P(\bigcup E_i)\le\sum P(E_i)$ always for a finite or countable family. Equality requires that overlaps contribute no mass. If the sum exceeds1, replace the numerical upper bound by1; do not report a probability greater than1.

### 11. Finite sigma-algebras

A partition into$k$ nonempty atoms generates $2^k$ events, each a union of whole atoms. Distinct subsets of sample points are not all observable if they split an atom. Count atoms, not individual elementary labels, for the event-family size.

### 12. Infinitely often

$\limsup E_n=\bigcap_m\bigcup_{n\ge m}E_n$ means infinitely many occurrences; $\liminf E_n=\bigcup_m\bigcap_{n\ge m}E_n$ means eventual permanent occurrence. If$\sum P(E_n)$ converges, tail union bounds give $P(\limsup E_n)=0$, with no independence assumption.

<!-- BOUNDARY-NOTES -->

### 13. Probability zero is not emptiness

Under a uniform continuous law, the event of one specified point is nonempty but has probability zero. Its complement has probability one without being the whole sample space. Almost sure statements exclude a null set, not necessarily every conceivable outcome.

### 14. Three-event coefficients

For three events, union probability is the singleton sum minus pair-intersection sum plus triple intersection. Exactly-one probability subtracts twice the pair sum and adds three times the triple. Inclusive pair intersections already contain the triple mass; pair-only data must be handled differently.

### 15. Event-family measurability

A probability is assigned only to members of the specified sigma-algebra. A finite partition model allows unions of whole atoms, not arbitrary subsets splitting an atom. A question may be about observability rather than merely cardinality.
