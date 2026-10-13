## Deeper mathematical constructions for function questions

The complete underlying lesson and its forty-two worked tutorials remain. The constructions below connect exact definitions to the counting and conceptual mechanisms in the rewritten bank. Each method states its assumptions before using a formula.

### 1. Type checking precedes algebra and counting

A total function is a typed object $f:A\to B$ with one output in B for every input in A. Its graph has the axiom $\forall a\in A\;\exists!b\in B\;(a,b)\in\Gamma_f$. This combines existence and uniqueness; neither can replace the other. A prescription that fails this axiom is not a noninjective function waiting to be classified. It is an invalid declaration.

For finite sizes m=|A| and n=|B|, the empty cases are best treated as objects before powers. If m=0, there is one empty graph for the specified target. If m>0 and n=0, there is no function. The combinatorial count $n^m$ adopts $0^0=1$ precisely because the empty graph exists. This convention does not settle unrelated analytic limits or numerical programming conventions for zero powers.

An injection with empty domain and nonempty target has no total left inverse, because the reverse type would send an available input into an empty set. For nonempty A, a left inverse exists by taking the unique antecedent on f[A] and a fixed default input outside f[A]. A right inverse of a finite surjection selects one member of every nonempty fiber. For arbitrary sets, simultaneous selection of representatives needs an appropriate choice convention or a specified selection rule. A true bijective inverse requires no arbitrary choice: the antecedent is unique.

These statements determine whether a formula is permitted before its numerical value is considered. The expression $m^{n-m}$ for left inverses is used when m>0 and n≥m; it is not a substitute for examining the empty reverse type.

### 2. Fibers turn output constraints into disjoint cases

For each b in B, define $F_b=\{a\in A:f(a)=b\}$. Totality and single-valuedness say that the fibers are pairwise disjoint and cover A. They may be empty. Injection means every size is at most one; surjection means every size is at least one. Thus constraints on function values often become constraints on a labelled fiber-size vector.

For fixed labelled target sizes $r_1,\ldots,r_n\ge0$ summing to m, choose the input labels assigned to each target. The count is
$$\frac{m!}{r_1!\cdots r_n!}.$$
Target labels are already named; do not divide by n!. If instead a question specifies only an unordered profile, first assign that profile to the target labels. Equal profile parts require care because exchanging equal sizes does not produce another assignment of sizes.

Example: onto maps from six labelled inputs to four labelled targets have profiles (3,1,1,1) or (2,2,1,1). These contribute $4\cdot6!/3!=480$ and $\binom{4}{2}6!/(2!2!)=1080$. Their sum 1560 agrees with inclusion–exclusion. The computation shows where each label factor enters rather than treating an unexplained Stirling number as an answer.

With allowed size sets L_b, the general count is the sum of these multinomial terms over all admissible vectors. A compact bookkeeping form is the exponential generating coefficient
$$m!\,[z^m]\prod_{b\in B}\left(\sum_{r\in L_b}\frac{z^r}{r!}\right).$$
The symbol $[z^m]$ means the coefficient of the stated power in a formal series; it is not numerical division. Multiplying the series chooses one size per target. Only terms with total m survive the coefficient extraction, and m! converts inverse factorial weights into assignments of the labelled inputs. This derivation is useful for bounded fibers, prescribed parity and exact occupancy.

### 3. Counting pairs of functions with a composition identity

Let A and B be finite labelled sets of sizes m and n. For $f:A\to B$ and $g:B\to A$, the left identity $g\circ f=\operatorname{id}_A$ forces f injective: applying g to equal f-values recovers equal inputs. For m>0 and n≥m, choose f in $n!/(n-m)!$ ways. The values of g on the m attained B-points are forced; its values on the n−m unused B-points independently choose any of the m A-points. Therefore the pair count is
$$\frac{n!}{(n-m)!}\,m^{n-m}.$$

The opposite identity $f\circ g=\operatorname{id}_B$ forces g injective. For n>0 and m≥n, choose g in $m!/(m-n)!$ ways, then force f on the n selected A-points and choose its remaining m−n outputs among B. The count is
$$\frac{m!}{(m-n)!}\,n^{m-n}.$$

These count ordered pairs (f,g), not just forward maps or inverse relations. Requiring both identities makes f a bijection and g its unique inverse; it yields m! pairs when m=n and zero when the finite sizes differ. Both-empty gives one empty pair. If exactly one carrier is empty, a total map in one of the two required directions is impossible, so there are no pairs.

For A with two elements and B with four, the left-identity count is $4\cdot3\cdot2^2=48$. The reverse identity is impossible, since a four-element B cannot inject into two-element A. This distinction is visible before performing any multiplication.

### 4. Monotonicity is an encoding of multiplicities

For input chain 1,…,m and output chain 1,…,n, a weakly increasing function is determined by the nonnegative multiplicities c_1,…,c_n summing to m. Writing each value that many times reconstructs exactly one function. Thus the count is $\binom{m+n-1}{n-1}$ for n>0. If all outputs are required, all multiplicities are positive; subtracting one from each gives $\binom{m-1}{n-1}$ when m≥n.

If n≥2, m≥2 and the endpoints are fixed to 1 and n, only c_1 and c_n must be positive. Subtract their compulsory occurrences. The remaining n nonnegative counts sum to m−2, giving $\binom{m+n-3}{n-1}$. Onto-ness still requires the interior value counts positive and changes this count.

Strictly increasing maps cannot repeat outputs. Choosing any m-element target subset determines the unique strictly increasing assignment, so the count is $\binom{n}{m}$ when m≤n and zero otherwise. A finite strictly increasing self-map of a chain is therefore the identity. An infinite strictly increasing self-map need not be: shifting every integer by one preserves order without fixing any input. The finite conclusion must retain its finiteness hypothesis.

### 5. Direct-image and preimage maps have dual classification laws

View $I_f:\mathcal P(A)\to\mathcal P(B)$, $I_f(S)=f[S]$, and $P_f:\mathcal P(B)\to\mathcal P(A)$, $P_f(T)=f^{-1}[T]$, as functions between power sets. This is different from asking whether the underlying f is injective or onto.

If f is injective, equal images recover equal input subsets, so I_f is injective. Conversely colliding inputs give distinct singleton subsets with equal images. If f is onto, every target subset T equals f[f^{-1}[T]], so I_f is onto. Conversely onto-ness of I_f must supply the whole target B as an image, forcing f[A]=B.

For P_f the directions reverse. If f is onto and two target subsets differ at b, an antecedent of b distinguishes their preimages; hence P_f is injective. If b is unused, the distinct subsets empty and {b} have the same empty preimage, disproving injection. P_f is onto exactly when f is injective: injection gives $f^{-1}[f[S]]=S$ for each S, while a collision prevents either colliding singleton from being a preimage, since every preimage contains whole fibers.

Thus both power-set functions reflect the same underlying properties, with the preimage classification interchanging injection and surjection. These equivalences also handle empty carriers; they do not require an inverse function for f.

### 6. Saturation and quotient factorization expose information loss

The operator $C_f(S)=f^{-1}[f[S]]$ fills every fiber touched by S. It is extensive, monotone and idempotent. Its fixed subsets are exactly the unions of whole nonempty fibers. If f has k attained values on a finite carrier, each of those k fibers may independently be included or omitted, so there are $2^k$ saturated subsets.

For a target subset T contained in f[A], the number of input subsets with direct image exactly T is
$$\prod_{b\in T}(2^{|F_b|}-1).$$
Choose a nonempty subset inside each included fiber; choose nothing inside any excluded fiber. If T contains an unused target the count is zero, and the empty product gives the unique empty input subset for T empty. A preimage T, by contrast, always takes an entire included fiber, so unused targets are its only possible ambiguity.

Define the kernel equivalence $a\sim a'$ exactly when f(a)=f(a'). Then $f=i\circ\bar f\circ q$, where q maps inputs to their kernel classes, $\bar f:A/{\sim}\to f[A]$ maps each class to its unique common output and is bijective, and i includes the image in B. This isolates merging inputs, relabelling classes, and unused codomain points. A quotient map formed from a coarser arbitrary equivalence must be checked for representative independence; it is not automatically the kernel quotient.

### 7. Finite functional graphs determine powers and eventual projections

A finite endofunction on a nonempty carrier has exactly one outgoing edge at every vertex. Following edges must eventually repeat a vertex; the repeated segment is a directed cycle. The endpoints of every edge reach the same eventual cycle, so every weakly connected component contains exactly one such cycle, with directed trees feeding into it. A permutation has no noncycle vertices, because each target also has exactly one antecedent. The empty endofunction is the identity and every one of its powers is idempotent; its nonexistent cycle lengths require no least-common-multiple construction.

Let H be the greatest number of edges needed to reach a cycle, and let L be the least common multiple of all cycle lengths. For a positive integer k,
$$f^{2k}=f^k\quad\Longleftrightarrow\quad k\ge H\ \text{and}\ L\mid k.$$
For necessity, f^k(x) must be fixed by f^k. Any point fixed by a positive iterate lies on a cycle, so k must reach every cycle and exceed every entry distance. On a cycle of length ell, its points are fixed by f^k exactly when ell divides k. For sufficiency, k≥H moves every input onto a cycle; L dividing k makes the next k steps return that cycle point, giving the equality.

The least positive idempotent power is therefore L times the least positive integer whose product with L is at least H. The zero power is always the identity and is handled separately. For a permutation H=0 and the least positive identity power is L. For an idempotent map all cycles are loops and H≤1. A two-cycle cannot itself be idempotent, although its square is.

### 8. Infinite conclusions require actual constructions

Finite-size equalities do not classify specified infinite maps. The shift n↦n+1 on zero-based naturals is injective and not onto; floor(n/2) is onto and not injective. A proper subset can have equal cardinality to its ambient set. Use explicit antecedents, collisions or encodings rather than subtracting infinite sizes.

The pairing rule $p(x,y)=2^x(2y+1)-1$ on zero-based naturals is decoded by uniquely extracting the power of two and the odd part of z+1. The exponent is essential. Schröder–Bernstein constructs a bijection from two injections by following the specified alternating layers; it does not turn either given injection into an onto map. Cantor's diagonal set disproves every proposed surjection to a power set, including the empty case.

To well-order a countable set, transfer the natural-number index order through a bijective enumeration. This constructs an order, not a property of every order already given on that set. The usual integer order is a counterexample to the latter claim. These distinctions decide the genuine examination assertions in the chapter.
