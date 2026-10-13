## Mathematical constructions for difficult relation questions

The complete underlying lesson and forty-six tutorials remain. These additional constructions connect the rewritten bank to deeper formula and proof methods. They keep counts of relations, sizes of one relation, classes, paths and total listings separate.

### 1. Three counting problems with three different objects

For a fixed labelled carrier A of size n, a relation is one subset of its n-squared possible ordered pairs. A question asking how many relations exist counts possible subsets, typically producing an exponential number. A question asking how many pairs belong to one specified relation counts entries that are one, typically producing a polynomial number. A question asking how many equivalence classes exist counts distinct blocks of that particular partition.

An n-by-n equivalence-block arrangement on n-squared elements has n classes, n-squared carrier elements and n-cubed relation pairs. Each block contributes its own Cartesian square. The universal relation on the same carrier would have n-to-the-fourth pairs, because it additionally includes cross-block pairs. One must not square the quotient size when the task asks for the relation's size.

For arbitrary nonempty block sizes $b_1,\ldots,b_k$ with total N,
$$|E|=\sum_{i=1}^k b_i^2=N+2\sum_{i=1}^k\binom{b_i}{2}.$$
The second form separates loops from the two orientations of each within-block distinct pair. It proves, in particular, that $|E|-N$ is even. A proposed size with the wrong parity is impossible without inspecting every partition. For N=6, size profiles (3,2,1) and (2,2,1,1) give fourteen and ten pairs respectively, while their quotient sizes are three and four.

### 2. Local independence stops when an axiom couples entries

For symmetry, one choice determines both directions of a distinct pair; for antisymmetry, its legal states are 00,10,01. These constraints can be handled independently across unordered pairs. Reflexivity or irreflexivity independently fixes the diagonal. This yields binary or ternary product counts because no local decision constrains a different unordered pair.

Transitivity is different. On vertices one, two and three, accepting edges one-to-two and two-to-three can force one-to-three. Thus decisions are coupled. Applying a local-choice power after adding transitivity does not count transitive relations. The appropriate technique can instead enumerate partitions for equivalence, enumerate partial orders with a structural method, or check a fixed matrix's witness triples.

Seriality also couples symmetry-constrained bits. A row must contain a loop or some incident edge, and an off-diagonal symmetric edge satisfies row requirements at both endpoints. On a labelled n-element carrier, the number of symmetric serial relations with optional loops is
$$\sum_{j=0}^n(-1)^j\binom nj\,2^{(n-j)(n-j+1)/2}.$$
To derive it, begin with all symmetric matrices and apply inclusion–exclusion to empty-row events. Fixing j vertices to empty removes their loops and every incident edge, leaving an arbitrary symmetric relation on n-j remaining vertices. The remaining exponent counts its diagonals and unordered pairs. This derivation explains why independently choosing nonempty rows would overcount.

### 3. Difference-defined equivalence is a subgroup theorem

On the entire real line, a condition $x\sim y\iff x-y\in H$ is an equivalence exactly when H contains zero and is closed under negation and addition. Reflexivity forces zero; symmetry tests a difference and its negative; transitivity tests the sum of consecutive differences. Conversely these closure properties give each axiom directly. The full carrier is used in the necessity witnesses, so restricting it can change which differences are ever tested.

This method reduces an infinite family question to concrete algebra. For dyadic rationals, placing two terms over a common power-of-two denominator proves closure. For a union of multiples of two and three, the permitted differences two and three sum to the forbidden difference five. One algebraic counterexample becomes a complete three-point relation counterexample.

For allowed residues H inside $\mathbb Z/m\mathbb Z$, the same argument asks whether H is an additive subgroup. If it is, the number of integer classes is its index, $m/|H|$. After a finite induced restriction, intersect those integer classes with the carrier and discard empty intersections. The pair count then uses the resulting finite block sizes; neither subgroup size nor the original modulus automatically equals the quotient size.

### 4. Existence algebra and multiplicity algebra are distinct

With source rows, a composition $S\circ R$ has entry
$$M_{S\circ R}[i,j]=\bigvee_{k=1}^r(M_R[i,k]\land M_S[k,j]).$$
Each middle index k contributes one possible two-edge witness. Boolean OR collapses multiple witnesses to one truth value. Ordinary multiplication instead sums witness indicators and therefore counts witnesses; it gives the same membership after replacing every positive entry by one, but its numerical entries are not Boolean relation entries.

The matrix order is first the source-to-middle matrix, then the middle-to-target matrix. Its dimensions are m-by-r multiplied by r-by-n. Converse transposes the matrices and reverses the relation composition order. Expanding the common witness gives the proof; merely reversing written symbols without checking types is unreliable.

Separate witnesses also explain failed distributivity over intersection. Each of two compositions may reach the same endpoint through a different middle element, while composition of an intersection requires the relevant edge to exist in both operands. Similarly, a path in each positive closure need not be a path using intersection edges. The distinction recurs across both relational algebra and graph reachability.

### 5. Closures need a path convention and a leastness certificate

Positive closure includes positive-length paths; reflexive transitive closure additionally includes every zero-length self-path. An acyclic directed path has no positive self-return, so its positive closure has no loops. A directed cycle does have positive self-returns. Therefore the diagonal alone cannot tell which convention produced a matrix: it must be interpreted with the input graph and stated operation.

Every positive endpoint path forces its endpoint pair in any transitive superset, by induction on length. This proves leastness of positive closure. Adding all identity pairs proves leastness for reflexive transitive closure. For equivalence closure, add reverse edges first and then use zero-length reachability so that isolated vertices retain their singleton-class loops.

Intersection closure of an axiom does not by itself ensure an extension exists. An input containing a distinct two-way pair has no antisymmetric superset, because adding pairs cannot remove that violation. For a finite partial-order extension, nontrivial directed cycles are the obstruction; harmless original loops are allowed. When no such cycle exists, reflexive transitive reachability is the least partial-order superset.

### 6. The exponent grid explains divisibility formulas

For a positive integer $M=\prod_{r=1}^k p_r^{a_r}$, unique prime factorization identifies each divisor with a vector whose r-th coordinate is between zero and $a_r$. Divisibility is coordinatewise comparison. Hence the number of divisor vertices is
$$V=\prod_{r=1}^k(a_r+1).$$
A cover increases one coordinate by one and leaves the rest unchanged. In direction r, that coordinate has $a_r$ possible starting values and the other coordinates have all their allowed values. Thus
$$E_{\mathrm{cover}}=\sum_{r=1}^k a_r\prod_{s\ne r}(a_s+1).$$
The directions are disjoint, so adding their counts does not overcount an edge. Hasse diagrams omit identity loops and all strict comparisons obtainable through longer upward paths.

Rank equal to the coordinate sum strictly increases along any strict comparison. The maximum possible rank is $\sum_r a_r$. Incrementing one coordinate at a time from the all-zero vector to the all-maximal vector attains every intermediate rank, so height measured in vertices is $1+\sum_r a_r$. The number of saturated least-to-greatest chains is the number of increment orderings,
$$\frac{(\sum_r a_r)!}{\prod_r a_r!}.$$
Finally, a nonstrict comparable pair chooses its two endpoints independently in each coordinate chain. A length-$a_r+1$ chain has $\binom{a_r+2}{2}$ nonstrict ordered comparisons, giving total relation size $\prod_r\binom{a_r+2}{2}$. Vertex count, cover count, height, longest-chain count and relation size are five different quantities derived from the same grid.

### 7. Extremal proofs and dynamic programs certify different outcomes

To prove a longest chain, give an upper bound on every chain and a chain attaining it. To prove a minimum chain partition, give a valid partition and an antichain requiring at least that many parts. To prove a supremum, first prove the candidate bounds every subset member, then prove it lies below every ambient upper bound. A computation of a plausible candidate does not discharge these universal obligations.

Counting linear extensions asks for all legal total listings. At each step, a prefix must be an order ideal. A recurrence may count how many legal sequences reach each ideal; it must prove that possible final elements are disjoint and exhaustive and that removing one produces a valid predecessor state. This is different from choosing one longest Hasse path, which can omit most carrier vertices.

The twelve-divisor example has twelve vertices, seventeen covers, sixty nonstrict comparisons, height six, ten saturated longest chains and 462 linear extensions. The last number follows from the finite ideal-state recurrence in Challenge 6. These values provide a concrete check on which mathematical object an examination asks to count, while the full lesson supplies the proofs underlying each object.
