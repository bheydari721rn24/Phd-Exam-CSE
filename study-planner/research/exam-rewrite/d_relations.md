## Teaching through formulas and conceptual decisions

### Count independent local relation choices

For$n$ labeled objects, a relation is an$n\times n$ Boolean matrix. There are$2^{n^2}$ arbitrary relations. Reflexivity fixes all diagonal entries to1 and leaves$n(n-1)$ free bits. Symmetry ties each off-diagonal pair and leaves$n(n+1)/2$ independent bits. Combining reflexivity with symmetry leaves only$n(n-1)/2$ free bits. Antisymmetry forbids only the both-directions state for distinct objects, so every unordered off-diagonal pair has three choices; each diagonal remains independently optional. The antisymmetric count is therefore$2^n3^{n(n-1)/2}$. Asymmetry additionally forbids every diagonal and has count$3^{n(n-1)/2}$.

Transitivity couples several pairs, so these local-choice products do not count transitive relations. Equivalence relations instead correspond to partitions; their count is the Bell number, with a fixed number of classes counted by a Stirling number of the second kind. A class of size$k$ contributes$k^2$ ordered pairs to the relation. Summing class sizes does not count relation edges.

### Use Boolean multiplication for composition

With the convention $(x,z)\in S\circ R$ when there exists$y$ with$xRy$ and$ySz$, the matrix entries use OR of AND-products. Multiple witnesses do not create multiplicity in a relation. The transitive closure includes paths of positive length; the reflexive-transitive closure additionally includes zero-length paths, hence the full diagonal. A cycle can make diagonal pairs appear even in the positive-length closure.

### Read a Hasse diagram without confusing four extrema

Minimal means no strictly smaller element; least means below every element. Multiple minimal elements can exist but a least element is unique. For a pair, an upper bound must dominate both; a least upper bound must also lie below every common upper bound. If two incomparable minimal upper bounds exist, there is no join. Hasse edges show covers, omitting loops and transitive edges; reachability reconstructs the order. In the divisor order of a positive integer, meet is gcd and join is lcm, both still divisors of the ambient integer.

## Formula and conceptual problem bank

### Question 1. Reflexive relation count

How many reflexive relations exist on three labeled objects?

**A.** 8

**B.** 32

**C.** 64

**D.** 512

**Answer: C.**

The three diagonal positions are forced1. Six off-diagonal positions remain independently free, yielding$2^6=64$.512 counts all nine bits free. Reflexivity does not restrict off-diagonal direction pairs or impose symmetry.

### Question 2. Reflexive symmetric count

How many relations on four labeled objects are both reflexive and symmetric?

**A.** 16

**B.** 64

**C.** 128

**D.** 1024

**Answer: B.**

Reflexivity fixes the four diagonal bits. There are$\binom42=6$ unordered distinct pairs, each choosing either both directions or neither. Hence$2^6=64$. Counting twelve ordered off-diagonal bits independently would violate symmetry.

### Question 3. Antisymmetric count

How many antisymmetric relations exist on three labeled objects?

**A.** 27

**B.** 64

**C.** 216

**D.** 512

**Answer: C.**

Each of the three diagonal positions is free, giving$2^3$. Each of three unordered distinct pairs has options neither direction, forward only or backward only, giving$3^3$. The product is$8\cdot27=216$. Removing all diagonal choices would count asymmetric rather than antisymmetric relations.

### Question 4. Symmetric and antisymmetric

How many relations on four labeled objects are simultaneously symmetric and antisymmetric?

**A.** 1

**B.** 4

**C.** 16

**D.** 64

**Answer: C.**

For distinct objects, symmetry would require both directions whenever one is present, but antisymmetry forbids both. Thus no off-diagonal pair can occur. Each of four diagonal pairs remains optional, yielding$2^4=16$. If reflexivity were added, all four would be forced and only the identity relation would remain.

### Question 5. Equivalence edges

An equivalence relation has three classes of sizes2,3 and4. How many ordered pairs does it contain?

**A.** 9

**B.** 18

**C.** 29

**D.** 81

**Answer: C.**

Every class relates all of its elements to every element of that same class, including itself. The total is$2^2+3^2+4^2=4+9+16=29$.81 would relate all nine objects across classes as well. Counting unordered pairs omits directions and diagonal loops.

### Question 6. Two-class partitions

How many equivalence relations on four labeled objects have exactly two classes?

**A.** 6

**B.** 7

**C.** 8

**D.** 15

**Answer: B.**

Choose a nonempty proper subset to be one class: there are$2^4-2=14$ choices. Each partition is counted twice, once by either class, so divide by2 to obtain7. The total Bell number15 counts every possible class count, not just two classes.

### Question 7. Composition direction

Let$R=\{(1,2),(2,3)\}$ and$S=\{(2,1),(3,2)\}$. Under the stated convention, what is$S\circ R$?

**A.** $\{(1,1),(2,2)\}$

**B.** $\{(2,2),(3,3)\}$

**C.** $\{(1,3)\}$

**D.** $\varnothing$

**Answer: A.**

Follow an$R$ edge first and then an$S$ edge. The path1 to2 to1 gives(1,1), and2 to3 to2 gives(2,2). No$R$ edge begins at3. The second option is the reversed composition. Writing the witness condition before following edges prevents a convention-dependent reversal.

### Question 8. Positive-length closure of a cycle

On$\{1,2,3\}$, let$R=\{(1,2),(2,3),(3,1)\}$. How many pairs lie in its transitive closure?

**A.** 3

**B.** 6

**C.** 9

**D.** 12

**Answer: C.**

From each starting vertex, one step reaches the next, two reach the remaining vertex, and three return to the start. Thus every ordered pair is reachable by a positive-length path, including every diagonal pair. There are$3^2=9$ pairs. A transitive closure need not be irreflexive when the original graph has a cycle.

### Question 9. Asymmetric versus antisymmetric

Which relation on$\{1,2\}$ is antisymmetric but not asymmetric?

**A.** $\{(1,1)\}$

**B.** $\{(1,2)\}$

**C.** $\varnothing$

**D.** $\{(1,2),(2,1)\}$

**Answer: A.**

A permits a diagonal loop, allowed by antisymmetry because its two endpoints are equal. Asymmetry forbids every diagonal pair. B andC are asymmetric; D violates antisymmetry through a distinct bidirectional pair. The two property names differ in their diagonal requirement, not just in wording.

### Question 10. Minimal versus least

In the divisor order on$\{2,3,6\}$, which statement is correct?

**A.** 2 is least.

**B.** 3 is least.

**C.** There are two minimal elements and no least element.

**D.** There are no minimal elements.

**Answer: C.**

Neither2 nor3 has a strictly smaller element in this set, so both are minimal. But2 does not divide3 and3 does not divide2; neither is below every element.6 is greatest. Removing the divisor1 from the ambient set removed the least element without removing all minimal elements.

### Question 11. Meet and join

In the divisor lattice of60, what are the meet and join of12 and20?

**A.** (4,60)

**B.** (2,60)

**C.** (4,240)

**D.** (12,20)

**Answer: A.**

The greatest common divisor is4, the largest common lower bound in divisibility. The least common multiple is60, the least common upper bound. Both belong to the divisor set of60. Ordinary numeric minimum and maximum do not define the meet and join for this order.

### Question 12. Linear extensions

A poset has four labeled elements with only the strict requirements$a<b$ and$c<d$. How many linear extensions does it have?

**A.** 4

**B.** 6

**C.** 8

**D.** 12

**Answer: B.**

Choose which two of the four positions hold the$a,b$ chain; their internal order is forced. The remaining two positions hold$c,d$ in their forced order. This gives$\binom42=6$. Counting all$4!$ orders and dividing by the two independent pair-order factors4 gives the same result.

### Question 13. Scheduling layers

A finite poset has longest chain length5 and tasks take one unit with unlimited processors. What is the minimum number of precedence-respecting time slots?

**A.** 1

**B.** 4

**C.** 5

**D.** The width.

**Answer: C.**

Every five-element chain needs five distinct successive slots, giving a lower bound. Assign each element a level equal to the longest chain ending there; comparable elements have strictly increasing levels. These five levels provide a feasible schedule, attaining the bound. Width describes simultaneous incomparability, not the required serial depth.

### Question 14. Chain partition duality

A finite poset has largest antichain size4. What does Dilworth’s theorem guarantee?

**A.** Every chain has length4.

**B.** A partition into four chains exists, and fewer cannot suffice.

**C.** Exactly four maximal elements exist.

**D.** Exactly four linear extensions exist.

**Answer: B.**

An antichain of four requires four different chains in any chain partition, because a chain cannot contain two incomparable members. Dilworth supplies a matching partition into four chains. Neither the longest chain nor the number of maximal elements or linear extensions is determined by width alone.

<!-- CHALLENGE-BANK -->

### Question 15. Challenge: Divisor-poset cover count

The divisor lattice of$72=2^3 3^2$ is represented by a Hasse diagram. How many vertices and cover edges does it have?

**A.** (12,17)

**B.** (12,24)

**C.** (6,17)

**D.** (12,29)

**Answer: A.**

Vertices correspond to exponent pairs$0\le i\le3$, $0\le j\le2$, giving4 times3=12. Covers increment exactly one exponent by1. There are3 horizontal increments in each of three rows, giving9, and2 vertical increments in each of four columns, giving8. Total17. Counting all comparable pairs would include transitive edges omitted from a Hasse diagram.

### Question 16. Challenge: Height of a product order

In the same divisor lattice, what is the longest-chain length measured in vertices?

**A.** 3

**B.** 4

**C.** 5

**D.** 6

**Answer: D.**

The exponent rank$i+j$ starts at0 and ends at5. Every strict cover raises it by1, so a chain can have at most six vertices. The chain1,2,4,8,24,72 attains that bound. Width instead concerns incomparable sets and is not this serial depth. Measuring edges would give5 rather than the requested vertex count.

## Applicable formulas and examination notes

### 1. Relation bit counts

Arbitrary$n$-object relations number$2^{n^2}$; reflexive ones number$2^{n(n-1)}$. Diagonal requirements fix$n$ bits, not an entire row. Other properties can couple the remaining bits.

### 2. Symmetry count

Symmetric relations number$2^{n(n+1)/2}$; adding reflexivity reduces this to$2^{n(n-1)/2}$. Choose one bit per unordered off-diagonal pair, and handle each diagonal independently.

### 3. Antisymmetric count

Antisymmetric relations number$2^n3^{n(n-1)/2}$. Asymmetric relations number$3^{n(n-1)/2}$. The factor$2^n$ is exactly the optional diagonal; transitivity is not included in either product.

### 4. Equivalence blocks

A class of size$k$ contributes$k^2$ ordered pairs. For class sizes2,3,4 the relation has29 pairs. Counting partitions gives equivalence relations; counting partitions with exactly$r$ blocks gives a Stirling number, not the Bell total.

### 5. Two-block formula

For$n\ge1$, two-class partitions number$(2^n-2)/2=2^{n-1}-1$. Exclude empty and full subsets, then remove the double count from selecting either class. Ordered labeled classes would omit the final division.

### 6. Composition direction

Write$(x,z)\in S\circ R$ iff some$y$ satisfies$xRy$ and$ySz$. Follow$R$ then$S$. Boolean matrix multiplication uses OR of AND, so two witnesses still produce one pair.

### 7. Closure diagonals

Transitive closure uses positive-length paths; cycles can create diagonal pairs. Reflexive-transitive closure explicitly adds zero-length paths. A three-cycle reaches all nine pairs, even without original loops.

### 8. Property counterexamples

To refute transitivity, find$xRy,yRz$ with missing$xRz$. To refute antisymmetry, find distinct objects related both ways. A loop alone refutes asymmetry, not antisymmetry.

### 9. Hasse reconstruction

Hasse edges are covers, with reflexive and transitive pairs omitted from the drawing. Use reachability to recover comparisons. A missing direct edge does not mean two elements are incomparable.

### 10. Extrema distinctions

Minimal means no smaller member; least means below every member. In divisors2,3,6, the two minimal elements are2 and3 but no least exists. Greatest and maximal have the dual distinction.

### 11. Bounds and joins

A join is below every common upper bound, not merely one minimal-looking upper bound. In a divisor lattice meet is gcd and join is lcm. Two incomparable minimal upper bounds imply no least upper bound.

### 12. Linear extensions

Two independent chains of lengths$r,s$ have$\binom{r+s}r$ interleavings when no extra comparisons exist. Additional precedence edges remove legal interleavings; do not reuse the unconstrained binomial formula blindly.

### 13. Height and scheduling

With unit tasks and unlimited processors, required slots equal longest-chain length. The level construction attains the chain lower bound. Processor limits or nonunit durations change the model.

### 14. Width and chain partitions

Dilworth equates maximum antichain size with minimum chain-partition count for finite posets. Height instead equals minimum antichain-layer count. These dual quantities answer different scheduling and decomposition questions.

<!-- BOUNDARY-NOTES -->

### 15. Preorder quotient

For a reflexive transitive relation, define $x\sim y$ by both $xRy$ and $yRx$. This is an equivalence relation, and its classes inherit a partial order. Antisymmetry fails on original distinct but mutually related points and is restored by quotienting.

### 16. Partial equivalence support

A symmetric transitive relation is reflexive on points participating in some edge, but may omit diagonal pairs for isolated points. It is a partial equivalence relation, not necessarily an equivalence on the entire declared set.

### 17. Well-founded strict orders

A finite strict partial order is well founded. On an infinite set, absence of finite directed cycles does not by itself rule out an infinite descending chain. A rank into nonnegative integers is a useful sufficient certificate.
