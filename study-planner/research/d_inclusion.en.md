# Inclusion-Exclusion: Overlap, Exact Multiplicity, and Forbidden Configurations

## 1. Sources, prerequisites, and a precise counting contract

This chapter combines four primary written courses: MIT 6.042J (Lehman, Leighton and Meyer), Oxford Discrete Mathematics (Andrew Ker), Cornell CS2800 (Pass and Tseng), and CMU 21-301 (Michael Tait). UC Berkeley EECS70 Note 14 is a genuinely reviewed fifth source for weighted events. The [source audit](../reviews/d_inclusion-sources.html) gives exact reading ranges, a bounded eight-candidate comparison, source corrections and an exercise inventory. The final reference section contains the original URLs. Each application below is derived in this chapter rather than assumed from a formula list.

You need finite sets, complements, factorials, binomial coefficients, the product rule and the previous counting chapter. For probability bridges, only nonnegative weights summing to one are required. A finite universe $U$ contains every object that the problem permits before the additional restrictions. Sets $A_1,\ldots,A_m$ describe properties of those same objects. A permutation, a function, an occupancy vector and a digit string are different kinds of objects; changing the universe changes all intersection counts.

Before calculating, write four things: the universe, the target predicate, the meaning of each event, and the count of an arbitrary specified intersection. The word “specified” matters. An intersection with three fixed indices is one set; the sum over all three-index choices contains $\binom m3$ sets. That multiplier is justified only when all such intersections have the same cardinality. Most difficult questions test this distinction rather than the alternating signs themselves.

An intersection does not mean “exactly these properties.” It means “these properties hold,” allowing additional properties. By contrast, an atom specifies both which events hold and which do not. We use $[m]=\{1,\ldots,m\}$, $A_I=\bigcap_{i\in I}A_i$, and $A_{\varnothing}=U$. All cardinalities in the set-counting sections are finite nonnegative integers. For counting bounded compositions, define $H_m(t)=\binom{t+m-1}{m-1}$ for integers $t\ge0$ and $m\ge1$, and $H_m(t)=0$ for $t<0$. This explicit convention prevents inappropriate evaluation of a binomial coefficient with a negative upper argument.

## 2. Two and three sets: atoms before formulas

For two sets, separate the universe into four disjoint regions: only $A$, only $B$, both, and neither. Adding $|A|+|B|$ counts the first two regions once and the shared region twice. Therefore $|A\cup B|=|A|+|B|-|A\cap B|$. The complement count is $|U|-|A|-|B|+|A\cap B|$. These identities require neither disjointness nor independence. Disjointness merely makes the intersection term zero.

For three sets, label the pairwise *inclusive* overlaps $p_{AB},p_{AC},p_{BC}$ and the triple overlap $t$. The triple belongs to each inclusive pair. Consequently the pair-only counts are $p_{AB}-t$, $p_{AC}-t$ and $p_{BC}-t$. The only-$A$ atom is $|A|-p_{AB}-p_{AC}+t$, and the other two single-only atoms follow by changing the letter. The outside atom is

$$z=|U|-|A|-|B|-|C|+p_{AB}+p_{AC}+p_{BC}-t.$$

Every one of these eight atoms must be a nonnegative integer. This is both a necessary and sufficient feasibility test for the stated three-set data: if all atoms are valid, construct disjoint groups of those sizes and give each group its specified memberships. Pairwise comparisons such as $p_{AB}\le\min(|A|,|B|)$ alone are insufficient because they do not test the single-only atoms or the outside atom.

**Worked example 1.** In a universe of 100 objects, the set sizes are 40, 35 and 30; the inclusive pair sizes are 12, 10 and 9; the triple size is 4. The only-$A$, only-$B$, only-$C$ counts are 22, 18 and 15. Pair-only counts are 8, 6 and 5; the triple count is 4. The union is $40+35+30-12-10-9+4=78$, so 22 objects are outside. Exactly two events hold for $12+10+9-3\cdot4=19$ objects; exactly one holds for $40+35+30-2(12+10+9)+3\cdot4=55$. These results sum to 100 after including the triple and outside.

If a problem reports “only $A$ and $B$,” do not insert that number directly as $|A\cap B|$. Add the triple count first. Conversely, if it reports $|A\cap B|$, do not add the triple again. In the three-set union, a triple object initially contributes $3-3+1=1$; omitting the final positive term makes its contribution zero.

<!-- SIM:atoms -->

**Worked example 2: a minimum, not just an expression.** The authentic doctoral example has 32 offices, device-set sizes 15, 10 and 8, and two offices in all three. Let $q$ be the number in exactly two device sets. The union is $15+10+8-2\cdot2-q=29-q$, so the outside count is $3+q\ge3$. Equality is attainable by using only single-device groups of sizes 13, 8 and 6, plus two triple-device offices and three outside offices. The bound alone would not establish the minimum without this construction.

## 3. The general theorem and why it works

The union formula is

$$\left|\bigcup_{i=1}^{m}A_i\right|=\sum_{\varnothing\ne I\subseteq[m]}(-1)^{|I|+1}|A_I|.$$

The empty set is excluded because the union formula counts objects with at least one property. To prove the identity, fix an object $x$ belonging to exactly $r$ events. If $r=0$, it is absent from every term. If $r>0$, it occurs in $\binom rj$ intersections with $j$ indices. Its net coefficient is $\sum_{j=1}^r(-1)^{j+1}\binom rj=1$, because $\sum_{j=0}^r(-1)^j\binom rj=(1-1)^r=0$. Each union object therefore contributes one and every outside object contributes zero. Summing these per-object coefficients proves the formula for arbitrary finite sets, not merely those in the simulation.

The complementary form is

$$\left|U\setminus\bigcup_{i=1}^{m}A_i\right|=\sum_{I\subseteq[m]}(-1)^{|I|}|A_I|.$$

Now the empty-index term is $|U|$. An outside object contributes one through that term alone; an object belonging to $r>0$ events contributes $(1-1)^r=0$. For $m=0$ the union is empty and the complementary formula consists only of $|U|$. For repeated or nested events the theorem remains valid, although reducing redundant events can greatly shorten the calculation.

There is a second proof that explains the algebra. Let $b_i(x)$ be one if $x\in A_i$ and zero otherwise. Then $\prod_{i=1}^m(1-b_i(x))$ equals one precisely when no event holds. Distributing the product chooses either 1 or $-b_i(x)$ from each factor, giving one term for every index subset $I$. The product $\prod_{i\in I}b_i(x)$ equals the indicator of $A_I$. Sum over all $x\in U$ and interchange two finite sums. This produces the complementary formula, then subtract it from $|U|$ to obtain the union formula. The proof also works with nonnegative weights instead of unit weights.

<!-- SIM:cancellation -->

**Worked example 3: compatible adjacency.** Permute ten distinct digits, allowing zero at the beginning because the objects are permutations, not ten-digit numbers. Count arrangements containing one or more of the directed blocks 42, 04 and 60. Each single block contracts to one object, giving $9!$. Any specified pair contracts to eight objects: overlapping blocks concatenate, so 60 with 04 forms 604 rather than two disjoint blocks. All three form 6042 and leave seven objects. Hence the union count is $3\cdot9!-3\cdot8!+7!$. Direction matters: 06 is not 60. The intersection argument has checked compatibility; it has not blindly substituted $(10-j)!$ for every imaginable collection of blocks.

## 4. Exactly r properties, at least r properties, and inversion

Define the intersection sums $S_j=\sum_{|I|=j}|A_I|$, with $S_0=|U|$. Let $N_r$ count objects with exactly $r$ true properties. An object with $r$ memberships belongs to $\binom rj$ specified $j$-way intersections, so double counting yields

$$S_j=\sum_{r=j}^{m}\binom rj N_r.$$

This is a triangular system, not $S_j=N_j$. Solve it from the top: $N_m=S_m$, then $N_{m-1}=S_{m-1}-mN_m$, and so forth. The closed inversion is

$$N_r=\sum_{j=r}^{m}(-1)^{j-r}\binom jr S_j.$$

**Proof.** Substitute the double-counting equation. For an object with $t\ge r$ memberships, its coefficient becomes $\sum_{j=r}^t(-1)^{j-r}\binom jr\binom tj$. Use $\binom tj\binom jr=\binom tr\binom{t-r}{j-r}$, which chooses $r$ distinguished indices first and then the other $j-r$ indices. The resulting coefficient is $\binom tr(1-1)^{t-r}$: one if $t=r$, zero if $t>r$. Objects with $t<r$ never occur. This proves the inversion, including $r=0$.

For $r\ge1$, summing exact counts and using the alternating partial-binomial identity gives

$$N_{\ge r}=\sum_{j=r}^{m}(-1)^{j-r}\binom{j-1}{r-1}S_j.$$

To justify the coefficient rather than memorize it, sum the coefficients $(-1)^{j-t}\binom jt$ over exact counts $t=r,\ldots,j$. Their sum is $(-1)^{j-r}\binom{j-1}{r-1}$, obtained by induction from Pascal's identity. For “at least zero” use $|U|$ directly; the displayed formula is deliberately restricted to positive $r$.

**Worked example 4.** Four events have $S_1=70$, $S_2=40$, $S_3=10$, $S_4=1$, and $S_0=50$. Then $N_4=1$, $N_3=10-4=6$, $N_2=40-3\cdot10+6=16$, $N_1=70-2\cdot40+3\cdot10-4=16$, and $N_0=50-70+40-10+1=11$. At least two events hold for $40-2\cdot10+3=23$ objects. The vector is nonnegative and sums to 50, so these aggregate data are realizable: assign $N_r$ objects to any membership masks of size $r$. That construction concerns the aggregate sums; it does not assert that arbitrary specified pair sizes can also be chosen freely.

For a specified exact membership set $J$, put $G(J)$ for the number in all events of $J$, and $F(J)$ for the number in exactly the events of $J$. Then

$$G(J)=\sum_{K\supseteq J}F(K),\qquad F(J)=\sum_{K\supseteq J}(-1)^{|K|-|J|}G(K).$$

This is the same cancellation argument on the additional indices outside $J$. It is the Boolean-subset version of Möbius inversion. We need no general poset machinery here. The distinction between a specified atom $F(J)$ and a multiplicity total $N_{|J|}$ is essential: the latter sums over all masks of that size.

<!-- SIM:inversion -->

## 5. Partial information and Bonferroni bounds

Computing all $2^m-1$ nonempty intersections may be impractical. Write $T_k=S_1-S_2+\cdots+(-1)^{k+1}S_k$. For odd $k$, $T_k$ is an upper bound on the union; for even $k$, it is a lower bound. If $k\ge m$, it is exact. For $k<m$, consider an object with $r$ memberships. Its truncated coefficient is

$$\sum_{j=1}^{k}(-1)^{j+1}\binom rj=1-(-1)^k\binom{r-1}{k}$$

when $r>0$, using zero for $\binom{r-1}{k}$ if $k>r-1$. Derive the identity by writing each binomial coefficient as two neighbors from Pascal's identity: all interior terms cancel and only the endpoint remains. For odd $k$ the excess coefficient is nonnegative; for even $k$ it is nonpositive. Sum over objects to prove the bounds. An outside object contributes zero throughout.

The first two consequences are $S_1-S_2\le|\bigcup A_i|\le S_1$. Intersect these with the trivial range $[0,|U|]$. Taking complements reverses inequalities: $|U|-T_{2h-1}\le N_0\le|U|-T_{2h}$. A negative lower bound remains a valid but useless bound; clamp it to zero. These formulas do not require independent events or equal-sized intersections.

Odd upper bounds can be sharpened by taking their minimum, and even lower bounds by taking their maximum. Do not assume every consecutive truncation is closer in absolute error. For an object in ten events, $T_1=10$ and $T_2=10-45=-35$: the second truncation is farther from the true union coefficient one. It is nevertheless on the correct side. This is an important correction to an overly strong reading of “better successive approximations.”

**Worked example 5.** In a universe of 200 objects, suppose $S_1=150$, $S_2=60$, $S_3=15$ and further intersections are unknown. Then the union lies between 90 and 105, while the count with no properties lies between 95 and 110. The lower union bound uses order two and the upper bound uses order three. These are certified bounds, not a guessed exact count. Additional atom constraints may make the feasible interval smaller; without checking them, do not label every endpoint attainable.

<!-- SIM:bounds -->

## 6. Required labels, surjections, and image sizes

The universe of functions $f:[n]\to[m]$ has $m^n$ objects: each of the $n$ labeled inputs independently chooses a labeled output. To require every output, let $A_i$ be the event that output $i$ is missing. Omitting a specified set of $j$ outputs leaves $m-j$ choices per input, so $|A_I|=(m-j)^n$. All specified intersections of size $j$ agree, justifying grouping them. The onto count is

$$O(n,m)=\sum_{j=0}^{m}(-1)^j\binom mj(m-j)^n.$$

For $n>0$, the final term has base zero and equals zero. For $n=0$, define $0^0=1$ as the count of the empty function into the empty set, not as a limit of real powers. Then $O(0,0)=1$, $O(n,0)=0$ for $n>0$, and $O(0,m)=0$ for $m>0$. If $m>n$, there are no onto functions; the alternating sum cancels to zero. For $m=n$, every onto function is bijective and the count is $n!$.

**Worked example 6.** Six labeled inputs and four labeled outputs give $4^6-4\cdot3^6+6\cdot2^6-4=1560$ onto maps. Dividing by 30 gives 52, the authentic MSc interval question's required comparison. There is no extra factor $4!$: the codomain labels already appear in the $4^6$ universe and in the missing-label choices.

If only a specified set of $q$ output labels is required to appear, other labels may or may not appear. The count becomes $\sum_{j=0}^q(-1)^j\binom qj(m-j)^n$. In contrast, if exactly $q$ outputs occur, choose the image set in $\binom mq$ ways and map onto that selected set: $\binom mq O(n,q)$. If exactly $q$ outputs are *missing*, use $\binom mq O(n,m-q)$. These are three different predicates with three different formulas.

A surjection partitions the input labels into nonempty fibers. Forgetting the output labels divides by $m!$, because every unlabeled nonempty partition has exactly $m!$ labelings. Thus the Stirling number of the second kind is $\left\{\begin{matrix}n\\m\end{matrix}\right\}=O(n,m)/m!$. The recurrence follows by examining the final input: it either forms a singleton new block or joins one of the $m$ existing blocks, giving $S(n,m)=S(n-1,m-1)+mS(n-1,m)$ with $S(0,0)=1$. This recurrence gives an independent exact check on the alternating sum.

Lower occupancy constraints larger than one are not obtained by simply replacing $m$ with a smaller number. For labeled balls, allocations with specified occupancies $x_i$ have weight $n!/\prod x_i!$; for identical balls, every occupancy vector has weight one. The universe determines whether multinomial weights are needed.

<!-- SIM:onto -->

## 7. Derangements, partial restrictions, and fixed-point counts

A derangement is a permutation $\pi$ of $[n]$ with $\pi(i)\ne i$ for every position. Let $A_i$ be the event that position $i$ is fixed. Fixing a specified $j$ positions forces their values and leaves a permutation on the other $n-j$ symbols, so the intersection has $(n-j)!$ elements. The complement theorem gives

$$D_n=\sum_{j=0}^{n}(-1)^j\binom nj(n-j)!=n!\sum_{j=0}^{n}\frac{(-1)^j}{j!}.$$

The initial values are $D_0=1$ and $D_1=0$. The empty permutation is a valid derangement because there is no violated position. Exactly $r$ fixed points in an $n$-permutation are counted by $\binom nr D_{n-r}$: choose which positions are fixed, then require the remaining positions to avoid their own values. Replacing $D_{n-r}$ by $(n-r)!$ would allow additional fixed points and count the event “at least the selected positions are fixed.”

If only $q$ specified positions are forbidden to stay fixed, unrestricted behavior is allowed elsewhere. The count is $\sum_{j=0}^q(-1)^j\binom qj(n-j)!$. If a separate specified set of $r$ positions must stay fixed and is disjoint from the forbidden set, replace $n$ by $n-r$ in the factorial while retaining $q$. If the required-fixed and forbidden-fixed sets overlap, the count is zero before any calculation.

**Worked example 7.** In a permutation of seven labels, forbid fixed points only in positions 1, 2 and 3. The answer is $7!-3\cdot6!+3\cdot5!-4!=3216$. This is larger than $D_7$ because positions 4 through 7 may remain fixed. For exactly two fixed points, the answer instead is $\binom72D_5=21\cdot44=924$.

The recurrence $D_n=(n-1)(D_{n-1}+D_{n-2})$ has a direct bijective proof. Choose $\pi(1)=a\ne1$. If $\pi(a)=1$, remove the two-cycle $(1,a)$ and derange the remaining $n-2$ elements. Otherwise there is a unique $b$ with $\pi(b)=1$ and $b\ne a$. Remove 1 from its directed cycle by replacing $b\to1\to a$ with $b\to a$. The result is a derangement on $n-1$ labels: the only changed arrow cannot be fixed because $b\ne a$. Conversely, in a derangement on the remaining labels, split the unique arrow into $a$ by inserting 1. These two cases are disjoint and exhaustive for each of the $n-1$ choices of $a$.

The alternating-series error gives $|D_n-n!/e|<1/(n+1)$. For $n\ge1$ this is strictly less than one half, so $D_n$ is the nearest integer to $n!/e$. Do not apply that nearest-integer rule at $n=0$, where it would give zero instead of one. The probability of a derangement for a uniform permutation is $D_n/n!$, tending to $1/e$. This limit does not say the finite probability equals $1/e$.

<!-- SIM:derangements -->

## 8. Forbidden positions and rook numbers

General assignment restrictions are a board $B$ of forbidden cells $(i,j)$: assigning label $j$ to position $i$ is disallowed there. A permutation selects exactly one cell in every row and column. For each forbidden cell define the bad event that the permutation uses it. The intersection of two cells in the same row or column is empty; the assignments conflict. An intersection of $k$ nonconflicting forbidden cells forces $k$ distinct row/column assignments and leaves $(n-k)!$ completions.

Let $r_k(B)$ count ways to select $k$ forbidden cells with no repeated row or column; $r_0=1$. Then the permitted permutation count is

$$\sum_{k=0}^{n}(-1)^k r_k(B)(n-k)!.$$

This is inclusion-exclusion grouped by compatible cell sets. The coefficient is a rook number, not $\binom{|B|}{k}$. The latter also selects conflicting cells whose intersections have cardinality zero. A diagonal board has $r_k=\binom nk$, recovering derangements.

**Worked example 8.** On a four-by-four board forbid $(1,1),(1,2),(2,1)$. Then $r_0=1$, $r_1=3$ and $r_2=1$: the only nonconflicting pair is $(1,2),(2,1)$. No triple is possible. There are $4!-3\cdot3!+2!=8$ permitted permutations. If all three pairs were counted, the erroneous answer would be 12.

A useful recursion chooses one forbidden cell $c$. Rook sets either exclude $c$, leaving the board with just that cell deleted, or include $c$, forcing deletion of its entire row and column. Hence $R_B(x)=R_{B\setminus\{c\}}(x)+xR_{B\setminus(\text{row}(c)\cup\text{col}(c))}(x)$, where $R_B(x)=\sum r_kx^k$. The deletion in the first term removes one cell; the deletion in the second removes incompatible possibilities. If two board components have disjoint row sets *and* disjoint column sets, their rook polynomials multiply, because compatible selections in the components combine independently. Disjoint cell sets alone do not suffice.

The same compatibility discipline applies to required adjacency edges in linear permutations. Selected directed edges must give each vertex at most one predecessor and one successor, and contain no directed cycle. Compatible paths contract to blocks, producing $(n-k)!$ arrangements for $k$ selected edges. A directed cycle of two or more distinct symbols cannot fit in a linear arrangement even though every vertex has acceptable degree. For circular arrangements, a complete cycle has a different meaning; do not transfer the linear count without changing the universe.

<!-- SIM:rook -->

## 9. Bounded allocations and position-sensitive strings

For identical tokens in labeled boxes, count integer vectors satisfying $\sum x_i=N$ and $\ell_i\le x_i\le u_i$. First check that all bounds are integers with $0\le\ell_i\le u_i$, and that $\sum\ell_i\le N\le\sum u_i$. Set $y_i=x_i-\ell_i$, $T=N-\sum\ell_i$, $c_i=u_i-\ell_i$. The unrestricted shifted count is $H_m(T)$. Define violation $A_i$ by $y_i\ge c_i+1$. For a specified violating subset $I$, subtract $c_i+1$ from those coordinates. This is a bijection to unrestricted nonnegative vectors of total $T-\sum_{i\in I}(c_i+1)$. Therefore the valid count is

$$\sum_{I\subseteq[m]}(-1)^{|I|}H_m\left(T-\sum_{i\in I}(c_i+1)\right).$$

The threshold is $c_i+1$, not $c_i$: equality at the upper bound is allowed. If all caps equal $c$, intersections depend only on their size and the sum compresses to $\sum_{j=0}^m(-1)^j\binom mjH_m(T-j(c+1))$. For unequal caps, replace neither the selected cap sum nor the intersection count by an average. An unbounded coordinate contributes no upper-violation event, but still appears in the stars-and-bars dimension.

**Worked example 9.** Count $x_1+x_2+x_3=8$ with $0\le x_1\le2$, $1\le x_2\le4$ and $2\le x_3\le6$. Shifting gives total 5 and caps 2, 3 and 4. There are $H_3(5)=21$ unrestricted vectors. Violations have shifted totals 2, 1 and 0, yielding 6, 3 and 1 vectors. No two violations are feasible because their thresholds already sum above 5. Thus the answer is $21-6-3-1=11$. Listing vectors or multiplying the finite polynomials $(1+x+x^2)(1+x+x^2+x^3)(1+x+\cdots+x^4)$ provides independent checks, not a second interpretation with distinguishable tokens.

For six-digit integers containing both 7 and 9, the first digit has nine choices; other digits have ten. Excluding one of 7 or 9 leaves eight first-digit choices and nine later choices. Excluding both leaves seven first-digit choices and eight later choices. Hence the answer is $9\cdot10^5-2\cdot8\cdot9^5+7\cdot8^5=184592$. The same predicate on unrestricted length-six digit codes has $10^6-2\cdot9^6+8^6$ solutions, a different number. More generally, for allowed symbol sets $B_t$ at position $t$ and required symbols $R$, the count is $\sum_{I\subseteq R}(-1)^{|I|}\prod_t|B_t\setminus I|$. This handles unequal position alphabets directly.

<!-- SIM:caps -->

## 10. Divisibility, modular intersections, and exact endpoints

For positive integers in the closed interval $[L,H]$, multiples of a positive $d$ number $\lfloor H/d\rfloor-\lfloor(L-1)/d\rfloor$. Convert strict endpoints before counting: integers strictly below $H$ end at $H-1$. Intersections of divisibility events use the least common multiple, because $d_i\mid x$ for every selected divisor precisely when $\operatorname{lcm}(d_i:i\in I)\mid x$. Multiplying divisors is valid only when the selected divisors are pairwise coprime.

**Worked example 10.** Among integers 1 through 200, count those divisible by 4 or 6. The singles contribute 50 and 33; the intersection uses 12, contributing 16. The union is 67. Using 24 instead of 12 incorrectly produces 75. A divisor event contained in another event can be removed first: multiples of 12 are already multiples of 4 and 6.

For distinct primes dividing a positive integer $n$, an integer is coprime to $n$ precisely when it avoids every prime-divisibility event. Each specified prime product divides $n$, so the floor counts simplify to exact quotients. Expanding the subset sum factors as $\varphi(n)=n\prod_{p\mid n}(1-1/p)$. Only distinct primes appear; exponents remain incorporated in $n$. For $n=1$, the empty product gives $\varphi(1)=1$ under the domain $1\le x\le n$.

Congruence events are more general. The pair $x\equiv a\pmod d$ and $x\equiv b\pmod e$ is feasible iff $a\equiv b\pmod{\gcd(d,e)}$. If feasible, its solutions form one residue class modulo $\operatorname{lcm}(d,e)$. If not feasible, the intersection is empty. Find the merged residue first and then count it in the stated interval. A class $x\equiv a\pmod d$ has $\lfloor(H-a)/d\rfloor-\lfloor(L-1-a)/d\rfloor$ members. This formula works with negative endpoints when floor means mathematical floor rather than truncation toward zero.

<!-- SIM:sieve -->

## 11. Weighted events, independence, and conditional universes

Assign each $x\in U$ a nonnegative weight $w(x)$. Every per-object proof above remains valid after multiplying its coefficient by $w(x)$ and summing. If total weight is one, the counts become probabilities. Thus inclusion-exclusion is valid for arbitrary dependence. Independence is used only to compute an intersection probability as a product, never to justify the union theorem.

**Worked example 11.** Roll three independent fair dice. The event that at least one die shows a specified face has probability $3/6-3/36+1/216=91/216$. Complement counting gives $1-(5/6)^3$, the same result. Adding $3/6$ alone is an upper bound, not the exact answer, because two or three hits overlap. For unequal independent hit probabilities $p_i$, the none probability is $\prod_i(1-p_i)$; expanding the product reproduces inclusion-exclusion. Pairwise independence alone does not justify the triple product. Two independent fair bits $X,Y$ and $Z=X\mathbin{\mathrm{xor}}Y$ are pairwise independent but the three-way event $X=Y=Z=1$ is impossible.

If conditioning on an event $C$ with positive weight, first restrict the universe to $C$ and renormalize. The conditional union is $\sum_{\varnothing\ne I}(-1)^{|I|+1}P(A_I\cap C)/P(C)$. Dividing unconditioned intersection probabilities by $P(C)$ without intersecting with $C$ can produce nonsense. Independence before conditioning may disappear afterward. Counting distinct outcomes and counting their probabilities coincide only for a uniform distribution on the appropriate universe.

**Worked example 12: extremal data.** Suppose only $P(A)=a$ and $P(B)=b$ are given. The intersection lies between $\max(0,a+b-1)$ and $\min(a,b)$, because the four atom weights must be nonnegative. Both endpoints are attainable by constructing the four atom weights. Therefore $P(A\cup B)$ lies in $[\max(a,b),\min(1,a+b)]$. Adding a third marginal does not determine a triple intersection. Use atom constraints or explicit stated independence; do not invent the missing information.

<!-- SIM:weights -->

## 12. Exact computation, audit strategy, and a complete solution workflow

The subset sum has exponentially many terms in general. Symmetry may reduce it to $m+1$ terms; zero intersections, nested events and incompatibility prune it further. The mathematical proof remains the same. For a board of forbidden assignments, a bit-mask dynamic program can independently count legal permutations. For small maps or allocations, direct enumeration checks the model. A check on a few inputs does not prove an arbitrary-$n$ identity; it is useful for catching a wrong threshold, sign, factor or universe alongside the proof.

For exact atoms from all inclusive intersection counts, the following executable Python transform uses integer arithmetic. Array index bits describe a specified event set. Starting with $G(J)$, subtract contributions from strict supersets one bit at a time. Before processing bit $b$, each entry has already enforced the absence of previously processed outside bits. After all $m$ stages it is $F(J)$. The operation is invertible by replacing subtraction with addition in the corresponding superset sum transform. The cost is $O(m2^m)$ time and $O(2^m)$ storage, including the supplied array; obtaining the intersection counts may require additional work.

```python
def exact_atoms(intersections, m):
    if len(intersections) != 1 << m:
        raise ValueError("one inclusive count is required per mask")
    if any(type(x) is not int or x < 0 for x in intersections):
        raise ValueError("inclusive counts must be nonnegative integers")
    atoms = list(intersections)
    for bit in range(m):
        for mask in range(1 << m):
            if not (mask & (1 << bit)):
                atoms[mask] -= atoms[mask | (1 << bit)]
    if any(x < 0 for x in atoms):
        raise ValueError("the specified intersection data are infeasible")
    return atoms

def onto(n, m):
    if type(n) is not int or type(m) is not int or min(n, m) < 0:
        raise ValueError("sizes must be nonnegative integers")
    from math import comb
    return sum((-1) ** j * comb(m, j) * (m - j) ** n
               for j in range(m + 1))
```

A nonnegative atom vector is sufficient for finite-set realizability of the *complete* intersection table: create that many objects per mask. It does not mean the events have any desired geometric or probabilistic independence structure. Floating-point arithmetic is unnecessary for these integer counts and can lose many leading digits in large alternating sums. Use arbitrary-precision integers, a Stirling recurrence or an exact occupancy dynamic program; only round the final probability if a decimal is requested.

A complete examination solution follows this sequence. State the universe and interpret inclusive versus exclusive words. Choose bad events whose intersections simplify. Count a specified intersection, checking compatibility and positional restrictions. Introduce any symmetry multiplier only after proving size invariance. Apply the union, complement, exact-multiplicity or bound formula matching the requested predicate. Evaluate using exact arithmetic. Finally check range, integrality, boundary cases and an independent description. If the question asks for a minimum or maximum, construct a configuration attaining the bound. If data are incomplete, supply a range or show two distinct realizations instead of inventing a unique result.

<!-- SIM:transform -->

## 13. Solved problems: authentic revisits and original examination models

The authentic items retain original identifiers and links to the archive PDFs. The other problems include independently written reconstructions of the selected courses' relevant examples and original medium-to-hard examination models. Every solution identifies the counted object, derives the intersection or inversion, and explains the mistake a tempting alternative makes. All answers are available for study; no prerequisite test is requested from you.

<!-- INCLUDE:problems -->

## 14. Complete summary and examination rules

The decisive insight is cancellation at the level of one object. An object with $r$ true properties occurs in $\binom rj$ intersections of order $j$. The union's alternating coefficient is one for $r>0$; the complement's is one for $r=0$. Exact-count inversion changes the coefficient to select a particular $r$, and Bonferroni truncation supplies an inequality with a parity-controlled error. These are consequences of the same finite identity, with different target predicates.

Surjections use missing output labels with intersection counts $(m-j)^n$. Derangements use forced fixed positions with counts $(n-j)!$. Rook numbers replace the binomial multiplier when forbidden cells can conflict. Bounded weak compositions use coordinate shifts by the first forbidden value, and divisibility uses least common multiples. Weighted and conditional events use the same coefficients with correctly computed weights. None of these applications authorizes changing the universe or confusing a specified intersection with the sum of all intersections of the same size.

The rules below are full statements with conditions and consequences. They are a review tool after the detailed lesson, not a replacement for it. When a rule mentions an exact formula, the relevant derivation above explains why it is valid.

<!-- INCLUDE:review -->

## 15. Interactive exact-count laboratories

Use the small finite labs to compare independently enumerated objects with the general formulas. The set lab displays exact atoms, inclusive intersections and signed corrections; the map lab displays actual arrows for onto functions; the permutation lab displays forbidden-cell assignments; the allocation lab lists bounded occupancy vectors and subset shifts. Bounds are deliberately small so every displayed result can be audited. The proofs above establish general identities; enumeration verifies only the inputs actually evaluated.

<!-- LAB:inclusion -->

## 16. References and verification limits

The mathematical proofs are general under the explicit finite and nonnegative-weight assumptions. Automated enumerations, formula checks, original-PDF inspection and browser checks verify the stated cases and presentation. The [quality audit](../reviews/d_inclusion-quality.html) records observed evidence and remaining boundaries. This chapter does not promise correctness on every possible unseen question or claim to have reviewed all courses worldwide. Its intended outcome is a rigorous, inspectable foundation for difficult formula and conceptual questions in this topic.

1. Eric Lehman, F. Thomson Leighton and Albert R. Meyer. **MIT 6.042J: Mathematics for Computer Science, Spring 2015**, section 14.9, physical PDF pages 590–596. [Textbook](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf).
2. Andrew D. Ker. **Oxford Discrete Mathematics, Michaelmas 2010**, sections 3.3–3.4, physical PDF pages 47–50. [Lecture notes](https://www.cs.ox.ac.uk/andrew.ker/docs/discretemaths-lecture-notes-mt2010.pdf).
3. Rafael Pass and Wei-Lung Dustin Tseng. **A Course in Discrete Structures**, Cornell CS2800 course text, section 4.4, physical PDF pages 74–76. [Course copy](https://www.cs.cornell.edu/courses/cs2800/2016sp/handouts/pass_tseng_discmath.pdf).
4. Michael Tait. **CMU 21-301: Combinatorics, Fall 2018**, section 2.5, physical PDF pages 20–24. [Lecture notes](https://www.math.cmu.edu/users/math/mtait/301/Notes.pdf).
5. **UC Berkeley EECS70: Discrete Mathematics and Probability Theory, Spring 2020**, Note 14 section 4.3, pages 10–11. [Lecture note](https://sp20.eecs70.org/static/notes/n14.pdf). Individual authorship is not specified in the note.
6. **Iranian MSc Computer Science examination, 1405, Q124**, original booklet PDF page 27; **Iranian PhD Computer Science examination, 1405, Q21**, original booklet PDF page 8. [Pinned examination repository](https://github.com/bheydari721rn24/Phd-Exam-CSE/tree/bdadf6e2c9cadc4772ae137a96a3da753c7cfd08/Exams). Answers here are independently derived.
