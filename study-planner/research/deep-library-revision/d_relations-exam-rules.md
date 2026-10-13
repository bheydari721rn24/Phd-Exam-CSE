## Twenty additional final decisions with mathematical witnesses

These detailed decisions supplement the seventeen retained examination notes and the complete seventy-two-rule review. They are intended for choosing and applying a method after the full lesson, not as a replacement for that instruction.

### 18. Decide what the number is counting

For five classes of size five, the carrier has twenty-five elements, the quotient has five classes and the relation has $5\cdot5^2=125$ ordered pairs. The number of possible partitions is a different task. Name the counted object before substituting a formula; an exponent alone does not identify its meaning.

### 19. Separate diagonal and off-diagonal choices

On n labelled elements, symmetry leaves one bit per unordered distinct pair and one per diagonal. Reflexivity fixes diagonal bits to one; irreflexivity fixes them to zero. Both constrained symmetric families have $2^{\binom n2}$ relations, although their diagonals differ. Equal counts do not mean equal families.

### 20. Price antisymmetry with three legal pair states

For distinct a,b, the states 00,10,01 are legal and 11 is not. Every diagonal remains optional, so the count is $2^n3^{\binom n2}$. At n=4 this is $16\cdot729=11664$. Dropping the binary factor silently imposes a fixed diagonal; allowing four pair states silently removes antisymmetry.

### 21. A two-cycle tests transitivity with repeated vertices

If aRb and bRa, the transitivity triple (a,b,a) requires aRa. Symmetric irreflexive relations can therefore be transitive only when empty. Restricting a checker to three distinct vertices misses this failure and does not implement the definition. The complete candidate set has $n^3$ triples, not $\binom n3$.

### 22. Unique output does not mean distinct outputs across rows

Rows 03 and 09 can each have singleton target 02. Each row is right-unique, but their equal targets show the relation is not injective on those rows. The authentic girl/boy question asks existence and uniqueness per girl. Replacing that quantifier by a global distinct-target requirement changes the statement.

### 23. Convert a difference condition into closure obligations

For the full real carrier, $x\sim y\iff x-y\in H$ needs $0\in H$, $-H=H$ and closure under addition. Allowed differences two and three with missing sum five produce the witness triple (5,3,0). For a restricted carrier, first confirm that the selected witness values belong to it; subgroup necessity is not automatic after restricting available differences.

### 24. Dividing equal-block order is conditional

For blocks of sizes three and four on seven labelled elements, selecting the three-element block gives $\binom73=35$ with no division. For two four-element blocks on eight labelled elements, either selected block describes the same partition, so the count is $\binom84/2=35$. The denominator comes from actual interchangeability, not a rule that every two-block count divides by two.

### 25. An equivalence pair count has a parity check

For block sizes $b_i$, the relation size is $N+2\sum_i\binom{b_i}{2}$, where N is the carrier size. Thus relation size and carrier size have the same parity. On six elements, a proposed equivalence with thirteen pairs is impossible. This quick rejection supplements the block-size proof; correct parity alone does not establish a realizable profile.

### 26. Inclusion of equivalences reverses quotient-count direction

If $R\subseteq S$, each R-block is contained in one S-block, and $[a]_R\mapsto[a]_S$ is onto. On finite carriers this gives $|A/R|\ge|A/S|$. Identity versus a universal equivalence on two elements gives two classes versus one. Pair inclusion enlarges blocks, rather than producing more blocks.

### 27. Intersection properties differ from intersection-preserving closures

The intersection of transitive relations is transitive. It does not follow that $(R\cap S)^+=R^+\cap S^+$. Separate a-to-c paths through b and d give the same endpoint in both closures while their input edge sets are disjoint. Expand the witnesses to distinguish these two assertions.

### 28. The isolated vertex decides a closure convention

A positive transitive closure gives no loop to an isolated vertex. Reflexive transitive closure adds one. In a three-cycle plus isolated d, the positive closure contains nine pairs in the cycle square, while reflexive transitive closure contains ten. Cycles can supply other diagonal entries, so “has some loops” does not identify the convention.

### 29. Powers specify exact lengths

In a three-cycle, the first power moves forward, the second backward and the third gives identity. They are not nested. On an n-cycle, the shortest positive return requires n edges, explaining the term $R^n$ in a uniform positive-closure bound. For zero-length closure, identity already supplies loops and powers through n−1 suffice for distinct endpoints.

### 30. Boolean products collapse duplicate witnesses

If two middle vertices connect the same source to the same target, a numerical matrix product entry is two while the Boolean product entry is one. The relation still contains one ordered pair. Source rows require $M_R$ followed by $M_S$ for $S\circ R$; the reversed symbolic composition convention does not transpose or reorder the typed matrix factors.

### 31. A closure answer must also be least

To prove the computed reachability is the transitive closure, show it is transitive and that every transitive superset contains every positive path endpoint. The latter is an induction on path length. A universal relation always contains the input and is transitive, but usually adds unnecessary pairs and is not the least extension.

### 32. Hasse edges omit loops and shortcuts

For divisors of seventy-two, exponent coordinates produce twelve vertices and seventeen cover edges. The full nonstrict order has sixty ordered pairs, and its strict part has forty-eight. A Hasse diagram draws neither twelve identity loops nor the thirty-one non-cover strict comparisons; upward paths encode those consequences. Count the requested object explicitly.

### 33. Height uses vertices when the question says so

The divisor-grid rank increases from zero to five, giving five possible strict increments and six vertices in a longest chain. The witness $1,2,4,8,24,72$ attains the bound. Answering five substitutes an edge count for height. A proof of longestness needs both the upper bound and the witness, not just a visually long path.

### 34. A total listing is not one maximal path

The twelve-divisor poset has ten saturated least-to-greatest paths but 462 linear extensions. A path uses six vertices; a linear extension lists all twelve while preserving comparisons. Count legal prefixes as order ideals and derive the final-element recurrence to count listings. Choosing an increment ordering counts a different structure.

### 35. Minimal and least must be checked in the selected carrier

In the induced divisor carrier $\{2,3,4,6\}$, two and three are both minimal and neither is least. The omitted divisor one cannot serve as its least element. For finite nonempty posets, a unique minimal element is least because descending from every element reaches it; infinite disjoint chains provide counterexamples when termination of descent fails.

### 36. Recheck the ambient carrier before using gcd or lcm

After deleting six from divisors of twelve, the join of two and three is twelve. Their lcm six is absent and is not an admissible bound. First list common ambient upper bounds, then prove the leastness condition. Having joins and meets for every pair gives a lattice; it does not automatically give distributive identities, as the resulting five-element pentagon demonstrates.

### 37. Prove guarded recursion by well-founded induction

A call from (m,n) to (m−1,n-squared-plus-one) decreases lexicographically despite possibly increasing every fixed positive linear sum am+bn. A call to (m,n−2) also decreases when n≥2. The guards preserve natural coordinates. Inductively terminating every smaller call, together with finitely many calls and subsequent operations, proves completion of each invocation. Failure of one proposed numerical rank does not refute a valid well-founded proof.
