# The Pigeonhole Principle: Sharp Guarantees, Hidden Classes, and Constructive Witnesses

## 1. Sources, chapter contract, and prerequisites

This chapter teaches deterministic guarantees: conclusions that hold for **every** placement, selection, sequence or encoding allowed by the stated assumptions. A likely event and an unavoidable event are different mathematical objects. The central skill is to describe a complete assignment into genuinely countable classes, calculate the largest configuration that avoids the desired conclusion, and decide whether that configuration can actually occur.

Five selected written courses from four universities supply complementary material. [MIT 6.042J, Spring 2015, Lehman, Leighton and Meyer, §14.8](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf) supplies the finite-function formulation, equal-sum subsets and the card-information example. [MIT 18.310, Fall 2013, Michel Goemans, Pigeonhole Principle lecture](https://ocw.mit.edu/courses/18-310-principles-of-discrete-applied-mathematics-fall-2013/ce68ab24d3cac4f2d808ced2705e6375_MIT18_310F13_Ch2.pdf) develops sequence labels and decision transcripts. [Oxford Discrete Mathematics, Michaelmas 2010, Andrew D. Ker, §6.5 and Exercises 6.7–6.8](https://www.cs.ox.ac.uk/andrew.ker/docs/discretemaths-lecture-notes-mt2010.pdf) supplies odd-part classes, compression, modular images and geometric partitions. [Stanford CS103, Winter 2026, Sean Szumlanski, Lecture 11](https://web.stanford.edu/class/archive/cs/cs103/cs103.1264/lectures/11/Lecture%20Slides.pdf) supplies degree restrictions, strict-average implications, saturation and the friends-and-strangers argument. [Toronto MAT344, Summer 2019, Balazs Elek, Lecture 7 §4](https://www.math.toronto.edu/balazse/2019_Summer_MAT344/Lec_7.pdf) supplies a second, independently checked proof of the monotone-subsequence theorem. [Cornell CS2800, Rafael Pass and Wei-Lung Dustin Tseng, §4.5](https://www.cs.cornell.edu/courses/cs2800/2016sp/handouts/pass_tseng_discmath.pdf) is a sixth reviewed complementary text for the ceiling formulation and contradiction proof.

The source audit compares nine located course candidates, records the exact reading boundaries and explains the selection. It is a bounded comparison of accessible written material. Course examples below are independently worded and attributed; the chapter does not reproduce whole course exercise collections. Additional capacity, collision-pair, prefix, endpoint and witness arguments are derived here with explicit proofs.

Prerequisites are finite sets, total functions, integer division, elementary counting and proof by contradiction. A binomial coefficient counts subsets of a specified size. Congruence modulo a positive integer means equality of remainders. A simple undirected graph has no loops and at most one edge between two distinct vertices; its degree is the number of neighbors. Every advanced application below introduces its extra definitions before using them. Full graph theory, coding theory, matching algorithms and asymptotic number theory have separate chapter boundaries.

**How to read the visual models.** Each trace states its invariant and begins paused. Step through the actual placement, prefix, directed dependency or geometric assignment next to its proof. A displayed finite example is a witness or illustration; the accompanying proof explains the arbitrary-size claim. Editable labs report exact results only inside their stated input ranges.

## 2. From objects and classes to a rigorous theorem

Let $A$ be a finite set of $N$ distinguishable objects and let $B=\{1,\ldots,k\}$ be a finite set of available classes, with $k\ge1$. A total function $f:A\to B$ assigns each object to exactly one class. The fiber $f^{-1}(i)$ is the set of objects assigned to class $i$; write its size as $x_i$. Distinct fibers are disjoint and cover $A$, so

$$x_i\in\mathbb N_0,\qquad \sum_{i=1}^{k}x_i=N.$$

The ordinary pigeonhole principle follows immediately. If $N>k$ and every fiber had size at most one, their sum would be at most $k$, contradicting $N>k$. Therefore two **distinct objects** have the same class label. In function language, no injection exists from a larger finite domain to a smaller finite codomain. The contrapositive says that an injection forces $|A|\le|B|$.

Three details matter. First, a list containing repeated numerical values still has distinguishable positions; two positions can be different objects with the same value. Second, a class count is an upper bound on possible labels, not necessarily the number of labels already observed. Third, a partial function may leave objects unassigned and does not meet the partition identity. If $B$ is empty, a total function exists only when $A$ is empty; do not evaluate a division by zero as a replacement for this case.

**Worked example 1 — a collision is forced, surjectivity is not.** Assign seven distinct requests to five servers. If each server receives at most one request, only five requests can be assigned, so a repeated server is unavoidable. Nevertheless, mapping all seven requests to server 1 is allowed. Thus the theorem proves noninjectivity, while it does not prove that every server is used. To prove surjectivity one needs a separate assumption on the assignment.

An infinite domain changes the situation completely. The map $n\mapsto n+1$ injects $\mathbb N_0$ into its proper subset of positive integers. One cannot subtract a finite number of labels from an infinite set and use the finite numerical inequality as though the cardinality became smaller. All sharp occupancy calculations in this chapter concern finite assignments.

<!-- SIM:assignment -->

## 3. Generalized occupancy, averages, and strict inequalities

At least one occupancy is at least the average $N/k$; otherwise the sum of $k$ strictly smaller values would be strictly smaller than $N$. Because occupancies are integers, at least one is at least the ceiling. Similarly, at least one occupancy is at most the floor:

$$\max_i x_i\ge\left\lceil\frac Nk\right\rceil,\qquad \min_i x_i\le\left\lfloor\frac Nk\right\rfloor.$$

These statements identify potentially different classes. Neither says that all classes achieve these bounds, or that the large class has exactly the ceiling. In the distribution $(11,0,0,0,0)$ the maximum is 11, although the guaranteed lower bound for eleven objects in five classes is only 3.

Write $N=qk+s$ with $0\le s<k$. A balanced distribution has $s$ occupancies equal to $q+1$ and $k-s$ equal to $q$. It attains the smallest possible maximum $\lceil N/k\rceil$ and the largest possible minimum $\lfloor N/k\rfloor$. This construction proves the two universal bounds are sharp for unrestricted placements. If the bins have capacities or placement restrictions, the balanced vector may be illegal; sharpness must be reconsidered.

For nonnegative real loads $w_i$, the average argument remains valid, but rounding does not: some $w_i\ge W/k$ and some $w_i\le W/k$, where $W=\sum_iw_i$. Loads $(0.4,0.4)$ do not force a load of 1. Rounding is justified by integral occupancy, not by averaging alone.

There is a stronger exact statement about a fixed distribution. A value lies strictly above its mean **if and only if** another lies strictly below it. To prove one direction, suppose every other value were at least the mean while one were larger; the sum would exceed $N$. The reverse direction follows by the symmetric argument. If $k$ divides $N$, all occupancies can equal the mean and neither strict inequality occurs. If $k$ does not divide $N$, integer occupancies cannot all equal the nonintegral mean, so both strict directions occur.

**Worked example 2 — ceiling, floor, and equality.** Forty-three jobs go to eight workers. Division gives $43=5\cdot8+3$, so some worker has at least six jobs and some has at most five. The vector $(6,6,6,5,5,5,5,5)$ shows both guarantees are optimal. For forty jobs the vector with five per worker shows that “some worker has more than five” is false. The exact equality case is an examination distractor that a decimal average can hide.

**Saturation principle.** If $x_i\le c_i$ for every class and $\sum_i x_i=\sum_i c_i$, then $x_i=c_i$ for every class. Indeed, all deficits $c_i-x_i$ are nonnegative and their sum is zero, so each deficit is zero. This is stronger than a large-fiber guarantee.

**Worked example 3 — incidence counts force a structural conclusion.** Twenty people each attend at most three of four workshops. The attendance totals are 18, 16, 14 and 12, whose sum is 60. There are twenty personal capacities of three, also totaling 60. Saturation forces every person to attend exactly three workshops. Every person therefore attends at least one of any specified pair of workshops: missing both would leave at most two available workshops. Double-counting attendance incidences is essential; people themselves are not the sixty objects.

<!-- SIM:average -->

## 4. Sharp thresholds, unequal capacities, and finite inventories

To force **some** class to contain at least $r$ objects, with $r\ge1$, negate the desired conclusion: every class has at most $r-1$. The largest unrestricted total avoiding it is $k(r-1)$. Thus the exact threshold is

$$N_{\mathrm{force}}=k(r-1)+1.$$

At the preceding total, placing $r-1$ objects in each class is a legal counterexample. For $r=1$, the threshold is 1. A common incorrect answer $kr$ requires every bin to reach the target in a balanced placement; the desired conclusion concerns only one bin under any placement.

Now let bin $i$ have physical inventory or capacity $c_i\ge0$. To avoid a class-specific target $r_i\ge1$, it can hold at most

$$a_i=\min(c_i,r_i-1).$$

If there is no cross-bin restriction, the maximum avoiding total is $M=\sum_i a_i$. A violation is forced at $M+1$ **only if this many objects exist**, meaning $M+1\le\sum_i c_i$. Each target exceeding its inventory is unreachable; if all targets are unreachable then $M=\sum_i c_i$ and no legal selection forces a violation. A total exceeding the physical inventory is infeasible, not an extraordinary guarantee.

**Worked example 4 — unequal colors and an impossible target.** A drawer contains 2 red, 7 blue and 9 green tokens. To guarantee four of one color, the largest avoiding selection has $(2,3,3)$, totaling 8. The ninth token forces four blue or four green; four red is impossible. To guarantee ten of one color, the avoiding maximum is the entire inventory 18, so there is no feasible guarantee. Writing 19 as though it were a drawable number would confuse impossibility with a threshold.

A **specified** class has a different quantifier. To force at least $r$ objects from class $j$, an adversary may first select every object outside that class and then $r-1$ from it. If $r\le c_j$, the exact threshold is

$$N_{\mathrm{specified}}=\sum_{i\ne j}c_i+r.$$

In the previous drawer, four blue tokens are guaranteed only after selecting $2+9+4=15$ tokens. The “any color” threshold 9 does not guarantee four blue.

To force at least $t$ distinct nonempty colors, sort their positive inventories decreasingly. Avoiding the conclusion uses at most $t-1$ colors, so the maximum avoiding total is the sum of the largest $t-1$ inventories. Add one, provided $t$ does not exceed the number of available colors. This maximization differs from capping each color at $r-1$.

For a second refinement, assume a common capacity $C\ge r$ and $N\le kC$. Let $h$ count bins with at least $r$ objects. The other bins have at most $r-1$, so

$$N\le k(r-1)+h(C-r+1).$$

Consequently, when $N>k(r-1)$,

$$h\ge\left\lceil\frac{N-k(r-1)}{C-r+1}\right\rceil.$$

This bound is sharp without further restrictions. Start with $r-1$ in every bin and let $E=N-k(r-1)>0$. Distribute these extra objects to as few bins as possible, at most $C-r+1$ extras per bin. Exactly $\lceil E/(C-r+1)\rceil$ bins become heavy. When $N\le k(r-1)$, a placement with no heavy bins is possible and the minimum is zero. Feasibility and unrestricted assignment are part of this proof.

<!-- SIM:capacity -->

## 5. Counting collisions rather than merely finding one

If bin $i$ has $x_i$ objects, it contributes $\binom{x_i}{2}$ unordered pairs sharing a label. The total is

$$P=\sum_{i=1}^{k}\binom{x_i}{2}.$$

This counts pairs of objects, not occupied bins. A bin with four objects contributes six pairs. To minimize $P$ at a fixed total $N$, consider two occupancies $a\ge b+2$. Moving one object from the larger bin to the smaller changes the pair total by

$$\binom a2+\binom b2-\binom{a-1}2-\binom{b+1}2=a-b-1>0.$$

Thus any unbalanced vector with a difference of at least two can be improved. Repeating the exchange leads to the balanced vector from Section 3. For $N=qk+s$, the exact minimum is

$$P_{\min}=k\binom q2+s q.$$

The maximum is $\binom N2$, attained by putting everything in one unrestricted bin. If capacities restrict either extremal construction, these extrema must be recomputed; the formula above is not a capacity-constrained theorem.

**Worked example 5 — a minimum number of repeated-label pairs.** Distribute 17 objects among five classes. Here $17=3\cdot5+2$, so at least $5\binom32+2\cdot3=21$ collision pairs occur. The vector $(4,4,3,3,3)$ contributes $6+6+3+3+3=21$. Counting only the five occupied bins would miss most pairs. The existence of a class of size at least four follows from the occupancy theorem, but alone would prove only six pairs rather than the stronger 21.

The same exchange idea counts $t$-element monochromatic subsets. Use $\binom{x}{t}=0$ when $x<t$. Pascal's identity shows that balancing never increases their total. Therefore the balanced vector gives the minimum

$$\sum_i\binom{x_i}{t}\ge k\binom qt+s\binom q{t-1}.$$

For $t\ge3$, other vectors can sometimes tie the minimum because the discrete marginal cost is initially zero. Balanced occupancy still supplies an attaining construction, but uniqueness of the minimizer must not be asserted from the pair proof.

For a hash function to $2^b$ possible outputs, $2^b+1$ distinct keys guarantee a collision for every function. A smaller set can already collide, but collision is not guaranteed independently of the function. The birthday probability on random outputs belongs to probability theory; it is a different calculation. Collision resistance does not mean that collisions do not exist; the difficulty of finding them is a computational property.

<!-- SIM:collisions -->

## 6. Residues, prefix sums, and decimal constructions

For modulus $m\ge1$, assign each integer its canonical remainder in $\{0,\ldots,m-1\}$. Any $m+1$ integers yield two whose difference is divisible by $m$. They need not be different numerical values unless the original selection is distinct. Equal residues do **not** force their sum to be divisible by $m$: residues $r,r$ give sum residue $2r$.

To force a divisible **contiguous sum**, use prefix sums rather than individual values. For integers $a_1,\ldots,a_m$, define $S_0=0$ and $S_j=\sum_{i=1}^{j}a_i$. There are $m+1$ prefixes and $m$ residue classes. Two indices $i<j$ satisfy $S_i\equiv S_j\pmod m$, hence

$$a_{i+1}+\cdots+a_j=S_j-S_i\equiv0\pmod m.$$

The block is nonempty because the indices are distinct. Including $S_0$ automatically covers the case of an initial block with zero remainder. Without $S_0$, one must split the proof into “some prefix is zero” and “two nonzero prefixes share a remainder.” Negative input values are allowed; positivity is not required by the residue proof.

**Worked example 6 — construct the block, not just its existence.** For modulus 5 and sequence $(3,4,2,7,1)$, prefix residues are $(0,3,2,4,1,2)$. The repeated remainder 2 occurs at indices 2 and 5. The block is positions 3 through 5, with sum $2+7+1=10$. An alternative claim that positions 2 through 5 form the block would have sum 14 and fail. Index conversion is part of the solution.

For the decimal repunit $R_j$ consisting of $j$ ones, let $R_0=0$. The $m+1$ values $R_0,\ldots,R_m$ have two equal residues. If $i<j$, then $R_j-R_i$ is a positive decimal number containing $j-i$ ones followed by $i$ zeros and is divisible by $m$. It has at most $m$ digits. This proves every positive integer divides some nonzero number using only digits 0 and 1.

If $\gcd(m,10)=1$, a stronger all-ones conclusion follows. A collision gives $m\mid10^i R_{j-i}$, and cancellation of the invertible factor $10^i$ gives $m\mid R_{j-i}$. If $m$ has a factor 2 or 5, no all-ones number is divisible by $m$, although a 0–1 multiple still exists. This is a useful example of a hypothesis needed for cancellation rather than for the original pigeonhole step.

### Two large modular images must meet

Two subsets of a universe of size $m$ must intersect if their cardinalities sum to more than $m$. Otherwise they would be disjoint and their union would exceed the universe. This is a collision argument with the two origin sets retained as tags: a repeated label must come from different origins when each origin lists its labels only once.

For an odd prime $p$, the set of square residues has size $(p+1)/2$: zero contributes one residue, while the $p-1$ nonzero inputs pair as $x$ and $-x$. There are no other identifications because $x^2\equiv y^2$ implies $p\mid(x-y)(x+y)$, and primality forces $x\equiv y$ or $x\equiv-y$. Thus the image sets $\{x^2+1\pmod p\}$ and $\{-y^2\pmod p\}$ both have $(p+1)/2$ elements. Their total size is $p+1>p$, so they meet. At an intersection, $x^2+y^2\equiv-1\pmod p$. For $p=2$, verify directly with $x=1,y=0$; the odd-prime residue count must not be substituted as $3/2$. A composite modulus can have additional square identifications, so this proof's counting step requires primality even when a particular composite instance happens to have a solution. For $p=7$, choosing $x=2,y=3$ gives $4+9\equiv6=-1\pmod7$.

```python
def divisible_block(values, modulus):
    if modulus < 1:
        raise ValueError("The modulus must be positive.")
    first = {0: 0}
    remainder = 0
    for end, value in enumerate(values, 1):
        remainder = (remainder + value) % modulus
        if remainder in first:
            start = first[remainder]
            return start, end  # Python slice values[start:end]
        first[remainder] = end
    return None
```

If there are at least $m$ inputs, the proof guarantees a returned pair. For fewer inputs, `None` is possible. The returned slice has positive length and its sum is divisible by the modulus. The dictionary stores the earliest occurrence of each remainder; overwriting it is unnecessary. Arithmetic operation counts are linear in the number of examined inputs, while bit costs depend on the integer representation.

<!-- SIM:residues -->

## 7. Subset images, equal sums, and cancellation

For $n$ indexed positive integers $a_1,\ldots,a_n$ with total $T$, each of the $2^n$ index subsets maps to its sum in $\{0,\ldots,T\}$. If $2^n>T+1$, two distinct index subsets have equal sums. Equivalently, the $2^n-1$ nonempty subsets have positive sums in $\{1,\ldots,T\}$, so $2^n-1>T$ suffices. These conditions are the same integer inequality.

Let $U,V$ be two distinct equal-sum index subsets. Remove their common indices. Then $U\setminus V$ and $V\setminus U$ are disjoint and their sums remain equal. Positivity ensures both are nonempty: if one were empty and the other nonempty, the latter would have strictly positive sum and could not equal zero. If zero or negative values are allowed, equality can involve an empty side after cancellation; that stronger nonempty conclusion requires an extra argument.

**Worked example 7 — equal sums without a constructive search guarantee.** Thirty positive integers each less than $10^7$ have total at most $30(10^7-1)=299,999,970$. There are $2^{30}=1,073,741,824$ subsets, more than the 299,999,971 possible sum values. Distinct equal-sum subsets exist, and canceling common indices gives nonempty disjoint equal-sum subsets. The count proves existence, not a polynomial-time algorithm to find the pair. This is a reconstructed MIT 18.310 application, with exact endpoints written explicitly.

If only $t$-element subsets are used, there are $\binom nt$ objects. Sort the positive values. Let $L$ be the sum of the smallest $t$ and $U$ the sum of the largest $t$. All relevant sums lie in the integer interval $[L,U]$, containing $U-L+1$ labels. Therefore $\binom nt>U-L+1$ forces a collision among equal-size subsets. After cancellation, the two remaining index subsets have the same cardinality as well as the same sum. This sharper range can be much smaller than the crude bound $tB-t+1$ when every value lies between 1 and $B$.

Mapping subsets to sum residues needs only $m$ labels. If $2^n>m$, two distinct subset sums agree modulo $m$. Cancellation yields a difference of two disjoint subset sums divisible by $m$, **not necessarily a positive-sum nonempty subset whose sum is divisible by $m$**. For values $(2,2)$ modulo 3, subset sums 2 collide, but the possible nonempty sums are 2 and 4, neither divisible by 3. Prefix sums provide the contiguous zero-sum theorem from Section 6; arbitrary subset-image collisions provide a different conclusion.

Products also define labels modulo $m$. If $2^n>m$, two index-subset products agree modulo $m$, using empty product 1. After removing common factors, cancellation is legitimate only if the common product is invertible modulo $m$. For example, $2\cdot1\equiv2\cdot4\pmod6$ while $1≢4\pmod6$. Equal product labels alone do not permit division in a ring with nonunits.

<!-- SIM:subsets -->

## 8. Complementary pairs, distinct selection, and odd-part chains

Selecting distinct integers from $\{1,\ldots,2n\}$ can be analyzed by the $n$ disjoint pairs $\{i,2n+1-i\}$. More than one selected member in a pair produces a target sum of $2n+1$. Thus $n+1$ selections force the sum. Selecting $\{1,\ldots,n\}$ gives a counterexample of size $n$, proving exact minimality. Repeated selections of one value do not obey the argument: sharing a pair label need not supply its two different members.

More generally, fix a target sum $s$ in a finite distinct-value universe. Partition the universe into two-member complement classes where both $a$ and $s-a$ are present, and singleton classes for unpaired values or the fixed point $s/2$. A fixed point can be selected once but cannot supply two distinct values summing to $s$. If there are $p$ two-member classes and $u$ singletons, the largest target-avoiding set has $p+u$ values. The threshold $p+u+1$ is feasible exactly when $p\ge1$.

For divisibility, pair labels are insufficient. Write each positive integer uniquely as

$$a=2^{v_2(a)}b,\qquad b\ \text{odd}.$$

Here $v_2(a)$ is the largest nonnegative exponent of 2 dividing $a$, and $b$ is its odd part. The odd parts of integers in $\{1,\ldots,2n\}$ belong to the $n$ odd values $1,3,\ldots,2n-1$. Among $n+1$ distinct selected integers, two have the same odd part. Their exponents differ, so the one with the smaller exponent divides the other. The upper half $\{n+1,\ldots,2n\}$ has no such divisibility pair: a proper multiple of an element larger than $n$ exceeds $2n$. Therefore the threshold is exactly $n+1$.

**Worked example 8 — the hidden class is not the remainder.** In the set $(6,7,10,12,15,18,19)$ from $\{1,\ldots,12\}$ the stated universe is violated, so no bound for $2n=12$ may be applied. For a valid selection $(2,3,5,6,8,10,11)$, the odd-part labels are $(1,3,5,3,1,5,11)$. The equal labels of 3 and 6 exhibit divisibility. The theorem asserts some comparable pair; it does not assert consecutive values, equal remainders or a fixed ratio of exactly 2. Values 2 and 8 share odd part 1 and have ratio 4.

Distinct integers also give a consecutive-pair proof. Partition $\{1,\ldots,2n\}$ into $\{1,2\},\{3,4\},\ldots,\{2n-1,2n\}$. Selecting $n+1$ forces two members of one pair. Consecutive positive integers are coprime because any common divisor divides their difference 1. The all-even set has size $n$ and no coprime pair, proving sharpness for the coprime guarantee. These are different partitions with different witness conclusions; a shared numerical threshold does not identify their logical content.

<!-- SIM:chains -->

## 9. Geometric partitions, endpoints, and approximation

To translate geometric proximity into a pigeonhole proof, partition the region into $k$ sets of diameter at most $d$. The diameter is the largest possible distance between two points in one set. Assign boundary points to exactly one cell using a stated tie rule. Any $k+1$ points then yield two at distance at most $d$. An area bound alone does not bound diameter: a long thin rectangle can have small area and large diameter.

For a square of side $L$, an $r\times r$ grid has $r^2$ cells of side $L/r$ and cell diameter $L\sqrt2/r$. Hence $r^2+1$ points force two at distance at most this value. Use half-open cells except at the outer boundary, or assign every grid-line point to the cell immediately above/right, retaining the outermost cells for the top/right edges. This gives a total assignment even when a point lies at a four-cell intersection. The proof gives a sufficient threshold; arbitrary geometric packing constraints may make it nonminimal.

For an equilateral triangle of side 1, join side midpoints to obtain four smaller equilateral triangles of side $1/2$. Their diameters are $1/2$. Any five points force two within $1/2$. This specific threshold is sharp: take the three original vertices and the centroid. Vertex–centroid distance is $1/\sqrt3>1/2$, and vertex–vertex distance is 1, so four points can avoid the conclusion. The final inequality is non-strict: vertices of a smaller cell can be exactly $1/2$ apart.

**Worked example 9 — translating the target distance into a grid size.** In a unit square, to obtain a grid guarantee of distance at most $1/4$, choose the smallest positive integer $r$ with $\sqrt2/r\le1/4$. Since $r\ge4\sqrt2$, this is $r=6$. The grid proof therefore needs $6^2+1=37$ points. This is the smallest threshold supplied by this particular square-grid argument, not a proof that 36 points can all have pairwise distances greater than $1/4$.

An interval argument produces Diophantine approximation. For real $\alpha$ and integer $m\ge1$, take the $m+1$ fractional parts $\{j\alpha\}$ for $j=0,\ldots,m$. Partition $[0,1)$ into $m$ half-open intervals of width $1/m$. Two indices $i<j$ have fractional parts differing by strictly less than $1/m$. With $q=j-i$ and $p=\lfloor j\alpha\rfloor-\lfloor i\alpha\rfloor$,

$$1\le q\le m,\qquad |q\alpha-p|<\frac1m,\qquad \left|\alpha-\frac pq\right|<\frac1{mq}.$$

The strict inequality follows from the half-open interval width. The denominator $q$ is produced by the collision and need not equal $m$. For $\alpha=\sqrt2$ and $m=5$, indices 0 and 5 lie in the first interval, yielding $p=7,q=5$ and $|5\sqrt2-7|\approx0.0711<0.2$. The proof does not claim the displayed rational is the globally best approximation.

<!-- SIM:geometry -->

## 10. Monotone subsequences and the sharp product bound

A subsequence preserves the original index order but may skip positions. A contiguous block cannot skip positions. Consider distinct real values $a_1,\ldots,a_N$. Let $I_i$ be the length of the longest strictly increasing subsequence ending at index $i$, and $D_i$ the length of the longest strictly decreasing subsequence ending there. Each length is at least one.

For $i<j$, distinctness gives either $a_i<a_j$ or $a_i>a_j$. In the first case, append $a_j$ to a longest increasing subsequence ending at $i$, obtaining $I_j\ge I_i+1$. In the second case, append it to a longest decreasing subsequence, obtaining $D_j\ge D_i+1$. Thus the ordered labels $(I_i,D_i)$ are pairwise distinct.

If no increasing subsequence has length $r$ and no decreasing subsequence has length $s$, all labels lie in the $(r-1)\times(s-1)$ rectangle. Therefore

$$N\le(r-1)(s-1).$$

Its contrapositive is the Erdős–Szekeres monotone-subsequence theorem: $N\ge(r-1)(s-1)+1$ forces an increasing subsequence of length $r$ or a decreasing one of length $s$, for $r,s\ge2$. If either target is 1, any nonempty sequence already satisfies it.

The threshold is sharp. Construct $r-1$ descending blocks, each of length $s-1$, with every value in a later block larger than every value in an earlier block. An increasing subsequence uses at most one value per block, so its length is at most $r-1$. A decreasing subsequence stays within one block, so its length is at most $s-1$. Both bounds are attained. This is a witness of size $(r-1)(s-1)$, not merely a numerically plausible rectangle.

**Worked example 10 — a trace and a sharp construction.** For $(3,1,4,2,5)$ the ending labels are $(1,1),(1,2),(2,1),(2,2),(3,1)$. Since five exceeds a $2\times2$ rectangle, an increasing or decreasing length-three subsequence is forced. Here $(1,2,5)$ is increasing. At size four, $(2,1,4,3)$ has longest increasing and decreasing lengths both 2, showing that the threshold five is exact.

For the symmetric question, let $L$ and $D$ be the longest lengths. The distinct-label argument gives $N\le LD$, hence $\max(L,D)\ge\lceil\sqrt N\rceil$. The least $N$ forcing one length at least $t$ is $(t-1)^2+1$, not $t^2$. A sequence of 17 distinct values forces length 5 because 17 exceeds 16; it need not force an increasing length 5 specifically.

If equal values are allowed, “strictly increasing or strictly decreasing” is false even for an arbitrarily long constant sequence. One valid asymmetric repair is **nondecreasing** versus **strictly decreasing**: when $a_i\le a_j$, extend the nondecreasing subsequence, and when $a_i>a_j$, extend the decreasing one. The same label proof applies. Switching both inequalities to non-strict also gives a valid existence conclusion, but changes the exact avoidance model.

```python
def ending_lengths(values):
    inc = [1] * len(values)
    dec = [1] * len(values)
    for j in range(len(values)):
        for i in range(j):
            if values[i] < values[j]:
                inc[j] = max(inc[j], inc[i] + 1)
            if values[i] > values[j]:
                dec[j] = max(dec[j], dec[i] + 1)
    return inc, dec
```

The quadratic dynamic program computes ending labels, not a common length for every prefix. To reconstruct an actual witness, store a predecessor when a candidate improves a length, start at an index attaining the global maximum, and follow predecessors backward. Reverse the recovered indices to restore subsequence order. Toronto's alternative proof uses increasing subsequences **starting** at an index and decreasing subsequences **ending** there; it is valid, but the two coordinate conventions must not be mixed inside one recurrence.

<!-- SIM:subsequences -->

## 11. Degrees, forbidden labels, and a small Ramsey theorem

In a simple undirected graph with $n\ge2$ vertices, every degree belongs to $\{0,\ldots,n-1\}$. That initially gives $n$ labels for $n$ objects and no collision guarantee. The extra structural restriction is that degree 0 and degree $n-1$ cannot both occur: the purported universal neighbor would have to connect to the isolated vertex. Therefore the available degree values lie in either $\{0,\ldots,n-2\}$ or $\{1,\ldots,n-1\}$, only $n-1$ possibilities. Two vertices have the same degree.

The restriction is about coexistence, not exclusion of one fixed value in all graphs. An empty graph uses degree 0, and a complete graph uses degree $n-1$. For directed graphs, the outdegrees in a transitive tournament are $0,1,\ldots,n-1$, all distinct; mutual friendship and absence of loops were essential assumptions in the undirected proof.

Color every edge of the complete graph on six vertices red or blue. Choose a vertex $v$. Five incident edges have two color labels, so three share a color; call it red and their other endpoints $a,b,c$. If any edge among $a,b,c$ is red, it and the two red edges back to $v$ form a red triangle. Otherwise all three edges among $a,b,c$ are blue and form a blue triangle. Thus every coloring contains a monochromatic triangle.

The bound six is sharp. On five vertices, color the five edges of a cycle red and the other five edges blue. The red graph is a five-cycle, which has no triangle; the blue complement is also a five-cycle and has no triangle. Consequently $R(3,3)=6$, where $R(3,3)$ is the least complete-graph size forcing a red or blue triangle.

### A sharp monochromatic-rectangle guarantee

Consider a matrix with four columns whose entries use three colors. In every row, two columns share a color. A certificate consists of an unordered pair of column positions and that shared color, so there are $3\binom42=18$ certificate labels. Choose one such certificate for each row by a deterministic rule. Nineteen rows force two rows with the same certificate, giving the four same-color corners of a rectangle. A whole-row-pattern argument would instead use $3^4=81$ labels and require 82 rows, which is correct but weaker.

The bound 19 is exact. For each of the eighteen pair-and-color labels, create one row with the chosen color in the chosen pair and the other two colors once each in the remaining positions. Each row has exactly one repeated-color pair. Every label appears exactly once across the eighteen rows, so no two rows can create a monochromatic rectangle. This is an explicit construction, not just the number of available certificates. For $r$ colors and $r+1$ columns, the identical construction proves the sharp threshold $r\binom{r+1}{2}+1$. With a different column count, a row may have several certificates; the same crude label argument may cease to be sharp.

**Worked example 11 — the second branch matters.** At a vertex in a six-vertex coloring, suppose the edges to $a,b,c$ are red. It is incorrect to declare a red triangle immediately: the edges $ab,ac,bc$ might all be blue. The correct proof examines these three edges. A red internal edge gives a red triangle including the chosen vertex; three blue internal edges give a blue triangle avoiding it. A monochromatic star is not itself a monochromatic triangle.

This is an introductory Ramsey application, not a claim that every larger Ramsey number has a simple exact formula. The first pigeonhole step proves a monochromatic neighbor group; a second structural step establishes the target subgraph.

<!-- SIM:graphs -->

## 12. Information limits, compression, and necessary versus sufficient bounds

A deterministic yes/no decision strategy of worst-case depth $q$ can distinguish at most $2^q$ possibilities. Each answer transcript is a label; two objects with the same complete transcript cannot be distinguished by a strategy whose next question depends only on previous answers. A binary tree of depth $q$ has at most $2^q$ leaves, even if some branches stop earlier. To distinguish $M$ objects, therefore,

$$q\ge\lceil\log_2 M\rceil.$$

With unrestricted subset questions, this lower bound is attainable: label the objects by distinct fixed-length binary words and ask for their successive bits. With restricted comparisons or geometric queries, attainability requires a legal decision tree. An information bound alone does not supply one.

For fixed-length binary inputs of length $n$, there are $2^n$ messages. The number of binary outputs of length **strictly less than** $n$, including the empty output, is

$$\sum_{j=0}^{n-1}2^j=2^n-1.$$

An injective lossless encoder cannot send every length-$n$ input to a shorter output. This counting statement assumes the decoder has no uncounted side information. If the original length, a dictionary or a selector is transmitted separately, its description is part of the code rather than a free extra class label.

Oxford supplies a stronger universal-compressor argument. Suppose a lossless encoder on **all** finite binary strings never lengthens an input and shortens at least one. Let $n$ be the shortest input length that is shortened and let its output length be $m<n$. Every input of length $m$ must retain that length: it cannot be shortened by minimality of $n$ and cannot be lengthened by hypothesis. The $2^m$ inputs of length $m$ and the shortened length-$n$ input then map into the $2^m$ outputs of length $m$. A collision contradicts lossless decoding. Thus some input must grow if another shrinks under these universal assumptions. A compressor for a restricted source family need not satisfy the all-string hypothesis.

**Worked example 12 — allowing one false answer.** In a fixed $q$-question nonadaptive binary encoding, suppose at most one answer bit can be flipped and the object must remain uniquely recoverable. Around each truthful word are $q+1$ transcripts: the unchanged word and the $q$ single-bit flips. The transcript sets for different objects must be disjoint. Therefore

$$M(q+1)\le2^q,\qquad M\le\left\lfloor\frac{2^q}{q+1}\right\rfloor.$$

For $q=7$, this bound is 16. For $q=20$, it is 49,932. This is a **necessary upper bound**, not an automatic construction of a code of that size for every $q$. MIT's adaptive one-lie discussion uses one transcript for each possible first lie position along its deterministic branch, also giving $q+1$ distinguishable transcripts per object. For an adaptive strategy, those transcripts are not generally the Hamming ball around one fixed truthful word, because subsequent questions can change after a lie. The nonadaptive proof above has a precise Hamming-ball interpretation; the counting bound can extend beyond that interpretation without justifying a nonadaptive geometric picture for adaptive transcripts.

A finite target search poses another quantifier distinction. To guarantee finding a particular unknown password among $M$ legal passwords by testing each once, the adversary can place it last, so $M$ tests are necessary and sufficient. This is not the same as guaranteeing that **some pair** of tested objects has equal labels. The authentic MSc password question below illustrates a worst-case fixed-target guarantee.

### A constructive card channel and its impossible variant

In a standard 52-card deck, any five distinct cards contain two of the same suit because there are four suit labels. Put their ranks on a cycle of length 13. The two directed clockwise distances sum to 13, so exactly one distance is between 1 and 6. Reveal its starting card first and hide its endpoint. The hidden suit is now known, and only a distance from 1 through 6 remains to be communicated. Sort the remaining three visible cards by a fixed total ordering; their $3!=6$ permutations encode the six distances. For example, use ascending order for distance 1 and descending order for distance 6. Starting at rank 10 and advancing six positions modulo 13 reaches rank 3. A decoder needs the shared ordering and the agreed permutation table; it must not guess the distance from the numerical size of the visible cards alone.

With only four selected cards and three revealed in order, there are $\binom{52}{4}=270,725$ possible hidden hands but only $52\cdot51\cdot50=132,600$ possible visible transcripts. Every legal assistant strategy defines a total assignment of hands to transcripts. Some transcript must correspond to at least $\lceil270725/132600\rceil=3$ hands, so unique decoding is impossible. In a general deck of $d$ cards, hiding one of five requires the necessary information inequality $\binom d5\le d(d-1)(d-2)(d-3)$, which reduces to $d\le124$ for $d\ge5$. Sufficiency for arbitrary card graphs requires a separate matching argument outside this chapter; the explicit standard-deck construction above proves the 52-card case directly.

<!-- SIM:information -->

## 13. Complete summary and a method-selection table

The basic theorem converts a total finite assignment into the sum of its nonnegative integer fiber sizes. The generalized theorem rounds the mean upward for one large fiber and downward for one small fiber. Balanced placements prove sharpness only when all such placements are legal. Capacity problems negate the target, maximize the avoiding total and add one only within the physical inventory. Specified targets and arbitrary targets require different avoidance constructions.

To count collision pairs, sum the binomial contribution of each fiber and use an exchange proof to balance the occupancies. To obtain a divisible difference, use remainder labels of individual integers. To obtain a nonempty contiguous divisible sum, use all prefixes including the empty prefix. To prove equal-sum subsets, compare the number of index subsets with the number of possible image sums, then justify cancellation and nonemptiness separately.

Complementary-value pairs and odd-part chains are distinct class systems. The first supplies a target sum, and the second supplies divisibility. Geometry requires a genuine partition with a diameter bound and explicit boundary assignment. Monotone subsequences require ordered pair labels and an extension proof showing their distinctness. Degree repetition needs the structural prohibition on simultaneous degrees 0 and $n-1$. Ramsey's triangle proof needs a second branch after the monochromatic-star guarantee.

Information arguments bound the number of distinguishable transcripts. They prove impossibility when injective encoding is blocked; an upper bound does not itself establish an attainable coding strategy. The common examination procedure is therefore: identify the exact target and its quantifiers; define objects, labels and a total assignment; establish the avoidance bound; check feasibility; provide a boundary witness if exact minimality is requested; and translate the resulting witness back into the original objects.

| Question trigger | Objects and labels | Formula or decisive step | Required qualification |
|---|---|---|---|
| Largest guaranteed occupancy | Objects mapped to $k$ bins | $\lceil N/k\rceil$ | Integral occupancies and $k\ge1$ |
| First total forcing some occupancy $r$ | Negation gives $r-1$ per bin | $k(r-1)+1$ | Unrestricted placement and legal threshold |
| Unequal finite inventory | Binwise avoidance capacities | $1+\sum_i\min(c_i,r_i-1)$ | Threshold must not exceed inventory |
| A specified bin reaches $r$ | All other inventory can be drawn first | $r+\sum_{i\ne j}c_i$ | $r\le c_j$ |
| Fewest collision pairs | Balanced fibers | $k\binom q2+s q$ | $N=qk+s$ and no capacity restriction |
| Divisible contiguous sum | Prefix residues | Two equal prefixes give a nonempty block | Include index 0 and convert indices correctly |
| Equal disjoint subset sums | Index subsets mapped to sums | $2^n>T+1$ | Positivity for both remaining sides to be nonempty |
| A divisibility pair from $1$ through $2n$ | Odd parts | $n+1$ selections | Distinct positive values |
| Nearby points | Cells of bounded diameter | $k+1$ points | Endpoint assignment and actual distance metric |
| Increasing length $r$ or decreasing length $s$ | Distinct ending-length pairs | $(r-1)(s-1)+1$ | Distinct values for both strict directions |
| No-loss information or question limit | Distinct messages mapped to transcripts | $M\le2^q$ | Count side information and respect query constraints |

## 14. Fully worked question bank

The bank combines authentic archive bridge questions, independently reconstructed course exercises, and original mathematical and conceptual examination-style tasks. The original tasks deliberately include sharpness, parameter thresholds, invalid cancellation, unavailable targets and misleading quantifier changes. Their labels do not claim they appeared in a national examination. Full solutions explain the modeling and the distractors; read them as further instruction after attempting the relevant calculation during your own study.

<!-- INCLUDE:problems -->

## 15. Examination rules and specific traps

Each rule below gives the trigger, exact usable implication, conditions, a calculation or counterexample, and the plausible incorrect conclusion. Use these as a final consolidation after the full derivations above. They do not replace the lesson or the worked solutions.

<!-- INCLUDE:review -->

## 16. Editable exact laboratories

The labs allow you to inspect occupancy guarantees, prefix collisions, ending-length labels, and two-color complete graphs. Their results are exact within the displayed finite input bounds. A lab demonstrates a particular witness or enumerated case; a successful run does not substitute for the arbitrary-input proof. The graph lab draws actual edges and highlights a triangle; the sequence lab follows directed predecessor dependencies; the prefix lab identifies the actual contiguous block.

<!-- LAB:pigeonhole -->

## 17. References and verification boundaries

1. Eric Lehman, F. Thomson Leighton and Albert R. Meyer. **6.042J Mathematics for Computer Science**, MIT, Spring 2015. §14.8, physical PDF pages 581–590, respecting the §14.9 boundary; selected Problems 14.37–14.43 on physical pages 618–619 are consulted within this chapter's boundary. [Official textbook](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf).
2. Michel Goemans. **18.310 Principles of Discrete Applied Mathematics**, MIT, Fall 2013. Pigeonhole Principle lecture, September 2, 2013, all four substantive pages and the attribution page. [Official notes](https://ocw.mit.edu/courses/18-310-principles-of-discrete-applied-mathematics-fall-2013/ce68ab24d3cac4f2d808ced2705e6375_MIT18_310F13_Ch2.pdf).
3. Andrew D. Ker. **Discrete Mathematics**, Oxford, Michaelmas 2010. §6.5, printed pages 77–79 / physical pages 87–89, and Exercises 6.7–6.8 with solutions on physical pages 92 and 94. The case $p=2$ is handled separately when a proof counts $(p+1)/2$ square residues. [Official notes](https://www.cs.ox.ac.uk/andrew.ker/docs/discretemaths-lecture-notes-mt2010.pdf).
4. Sean Szumlanski. **CS103 Mathematical Foundations of Computing**, Stanford, Winter 2026. Lecture 11, physical pages 12–74 and 83–135; page 139 is consulted for the 0–1 multiple application, while its informal topology sampler is outside this chapter. [Official slides](https://web.stanford.edu/class/archive/cs/cs103/cs103.1264/lectures/11/Lecture%20Slides.pdf), [course attribution](https://web.stanford.edu/class/archive/cs/cs103/cs103.1264/).
5. Balazs Elek. **MAT344 Introduction to Combinatorics**, Toronto, Summer 2019. Lecture 7, May 28, §4, physical pages 1–2, through the Erdős–Szekeres proof and before §5. [Official notes](https://www.math.toronto.edu/balazse/2019_Summer_MAT344/Lec_7.pdf), [course attribution](https://www.math.toronto.edu/balazse/2019_Summer_MAT344/).
6. Rafael Pass and Wei-Lung Dustin Tseng. **A Course in Discrete Structures**, Cornell CS2800 official course copy. §4.5, physical page 77, Lemma 4.28 and Example 4.29. [Official textbook](https://www.cs.cornell.edu/courses/cs2800/2016sp/handouts/pass_tseng_discmath.pdf).

The source and quality audit pages record exact reading, corrected interpretations, original archive fingerprints, independent mathematical checks and observed browser tests. The archive answers are independently derived, not represented as official answer keys. Necessary information and geometric bounds are explicitly separated from proved exact thresholds. Finite checks and these source ranges do not certify every possible future examination question.
