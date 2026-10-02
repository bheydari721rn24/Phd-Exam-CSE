## 1. Chapter boundary and source synthesis

This chapter teaches binary relations, their logical properties, relational algebra, closures, equivalence classes, preorders, partial orders, Hasse diagrams, extremal elements, bounds, lattices, finite scheduling, and well-founded reasoning. The goal is to make each definition usable in a proof, a computation, and a difficult question. Read the teaching sections before using the worked-problem bank and final review sheet.

Prerequisites are sets, quantified statements, direct proof, counterexamples, and induction. Matrices are introduced here as tables of truth values; prior numerical matrix multiplication is helpful but unnecessary. A path means a finite sequence of directed edges, with repeated vertices permitted unless explicitly excluded. A strict comparison never includes equality. Natural numbers include zero; positive integers are denoted $ℕ_{>0}$.

Four principal written university courses were selected after comparing the accessible candidate pool. Cornell's independently authored lecture notes provide a fifth, focused supplement. The selection is specific to this chapter's needs; it is not a claim that every course worldwide was discovered or that university reputation guarantees correctness.

| Course and instructor | Material actually read for this chapter | Contribution to the synthesis |
|---|---|---|
| MIT, 6.042J / 18.062J, Fall 2010; Tom Leighton and Marten van Dijk | Chapter 7, printed pp. 213–236, §§7.1–7.9 | Typed relations, representations, order structure, linear extensions, parallel scheduling, chain–antichain bounds. |
| Stanford, CS103, Spring 2017; Keith Schwarz | Selected substantive pages of Binary Relations I and II; Problem Set 3, pp. 2–4 | Definition-driven proofs, independence of properties, alternative characterizations of equivalence, strict orders, and covers. |
| Cambridge, Discrete Mathematics, 2003–2004; Peter Robinson | Lent notes, printed pp. 35–43 | Composition, quotient sets, closure existence, Warshall's invariant, orders, and well-founded induction. |
| Oxford, Discrete Mathematics, Michaelmas 2010; Andrew D. Ker | Chapters 4 and 8, printed pp. 45–56 and 97–110 | Counting constrained relations, complete partition arguments, product orders, bounds, and order isomorphisms. |
| Cornell, CS2800, Spring 2017; Michael George | Lecture 6's relation section and Lecture 7 | Quotient sets and the requirement that constructions not depend on representatives. |

The four principal courses cover different gaps. MIT provides applications that Oxford develops less extensively; Cambridge provides an algorithmic account that Stanford does not; Stanford emphasizes proof failures that a formula table can conceal. Some source statements require correction or additional hypotheses. The source audit records these explicitly. In particular, finite irreflexivity alone does not imply well-foundedness, and the real numbers are not a complete lattice under their usual order.

Problems marked **course-derived** are independently written exercises using identified mathematical patterns from the source courses. Their solutions are authored for this chapter. They are not a reproduction of every published assignment, and no archived Iranian entrance-exam questions are included at this stage. The final section lists exact text links and review ranges.

## 2. Relations as typed mathematical objects

### 2.1 What a relation specifies

A binary relation from a set $A$ to a set $B$ is a subset $R⊆A×B$. Membership $(a,b)∈R$, also written $aRb$, states that the first object is related to the second. Nonmembership states that this particular association does not hold. The word binary refers to the two argument positions, not to a numerical base.

The surrounding sets matter. For $R={(1,u),(2,u)}$, the source carrier might be ${1,2}$ or ${1,2,3}$. The listed pairs are the same, but the claim that every source element has a related target changes when the carrier changes. We use **source carrier** and **target carrier** for the declared sets; **active domain** means the elements that occur as first coordinates, and **range** means those that occur as second coordinates. Some texts call the source carrier the domain. Keeping both notions explicit prevents a terminological disagreement from changing a proof.

<div class="formula-block">dom(R) = {a ∈ A : ∃b ∈ B, aRb}<br>ran(R) = {b ∈ B : ∃a ∈ A, aRb}</div>

A relation can give an input no outputs, one output, or several outputs. A **right-unique** relation satisfies: if $aRb$ and $aRc$, then $b=c$. A **left-total** relation satisfies: for every $a∈A$, some $b∈B$ satisfies $aRb$. A total function is both right-unique and left-total. Right-uniqueness alone describes a partial function, not a total function. A relation is right-total, or surjective as a relation, when its range is the entire target carrier. These statements inspect different rows or columns, so one must not substitute one for another.

On a finite $m$-element source and $n$-element target there are $mn$ possible ordered pairs. Each is independently included or excluded, giving $2^{mn}$ relations. There are $(2^n−1)^m$ left-total relations: each row chooses a nonempty subset of the target. There are $(n+1)^m$ partial functions and $n^m$ total functions: a row chooses no target or one target in the first count, and exactly one in the second. If both carriers are empty, the empty relation is the unique total function. If the source is nonempty and the target empty, no total function exists. Combinatorial powers with exponent zero represent one empty assignment, including the counting convention $0^0=1$ in this context.

### 2.2 Graphs, matrices, images, and restrictions

For distinct source and target roles, draw a two-column bipartite diagram, even when the underlying sets happen to overlap. An edge from the source copy of $a$ to the target copy of $b$ means $aRb$. A relation on one carrier $A$ can instead be drawn as a directed graph with one vertex per element and one arrow per pair. A loop represents a pair $(a,a)$.

Choose explicit enumerations $A=(a₁,…,a_m)$ and $B=(b₁,…,b_n)$. The Boolean matrix $M_R$ has entry 1 precisely when $a_iRb_j$. Rows represent sources; columns represent targets. Reordering a carrier permutes the corresponding rows or columns without changing the abstract relation. A Boolean matrix records existence. It does not record weights or the number of different paths.

For a subset $X⊆A$, the relational image $R[X]$ is the set of targets related to at least one member of $X$. Existential quantification gives

<div class="formula-block">R[X] = {b ∈ B : ∃a ∈ X, aRb}<br>R[X ∪ Y] = R[X] ∪ R[Y]<br>R[X ∩ Y] ⊆ R[X] ∩ R[Y].</div>

To prove the union identity, a witness from the union belongs to at least one operand, and either operand's witness belongs to the union. Intersection equality can fail: the same target may have different witnesses in the two source sets, with neither witness in their intersection. This witness distinction is a recurring theme in relational algebra.

The converse, also called the inverse relation, reverses every pair: $R^{−1}={(b,a):(a,b)∈R}$. It always exists, including for a many-to-many relation; it need not be a function. Its matrix is the transpose of $M_R$, and reversing twice returns $R$. The inverse image of $Y⊆B$ is $R^{−1}[Y]$. It is an existential inverse image, so it need not preserve intersections or complements as a function's inverse image does.

Restricting $R$ to source set $X$ and target set $Y$ produces $R∩(X×Y)$. For a relation on $A$, its induced restriction to $X⊆A$ is $R∩(X×X)$. Reflexivity on the restricted carrier, symmetry, antisymmetry, irreflexivity, and transitivity survive induced restriction. For example, a transitivity witness in $X$ is also a witness in $A$, and its required endpoint pair remains in $X×X$. Seriality can fail when its only witnesses were deleted.

### 2.3 Composition, with the direction fixed

Let $R⊆A×B$ and $S⊆B×C$. Throughout this chapter, $S∘R$ means **first follow $R$, then follow $S$**:

<div class="formula-block">a(S ∘ R)c ⇔ ∃b ∈ B, (aRb ∧ bSc).</div>

Cambridge's selected notes sometimes write the same first-then operation as $R∘S$. This chapter uses the function-compatible convention above. In an unfamiliar examination, inspect the supplied definition rather than guessing from the symbol alone.

<!-- FIGURE:composition -->

Associativity follows by expanding both sides. Membership of $(a,d)$ in $T∘(S∘R)$ means there are $b,c$ with $aRb$, $bSc$, and $cTd$. The same witnesses establish membership in $(T∘S)∘R$. Conversely, witnesses for the second expression establish the first. This proves equality by mutual inclusion. Associativity permits a multi-step composition without parentheses; it does not permit changing the sequence of relations.

The identity relation on $A$ is $I_A={(a,a):a∈A}$. Its only possible intermediate witness is the same element, so $R∘I_A=R$ and $I_B∘R=R$. Converse reverses the sequence:

<div class="formula-block">(S ∘ R)<sup>−1</sup> = R<sup>−1</sup> ∘ S<sup>−1</sup>.</div>

Indeed, $c(S∘R)^{−1}a$ says $aRbSc$ for some $b$, which is the reversed chain $cS^{−1}bR^{−1}a$. Composition distributes over unions on either side because an existential witness using a union edge uses one of the alternatives. Composition is monotone: adding pairs to either input cannot remove an existing witness. It generally does not distribute over intersections. The two separate compositions can be witnessed by different intermediate objects, whereas composing an intersection requires a shared witness.

With our source-row convention, the matrix for $S∘R$ is the **Boolean product of $M_R$ followed by $M_S$**, despite the reversed order of the relation symbols:

<div class="formula-block"><math display="block"><mrow><msub><mi>M</mi><mrow><mi>S</mi><mo>∘</mo><mi>R</mi></mrow></msub><mo>[</mo><mi>i</mi><mo>,</mo><mi>j</mi><mo>]</mo><mo>=</mo><munderover><mo>⋁</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mrow><mo>|</mo><mi>B</mi><mo>|</mo></mrow></munderover><mrow><mo>(</mo><msub><mi>M</mi><mi>R</mi></msub><mo>[</mo><mi>i</mi><mo>,</mo><mi>k</mi><mo>]</mo><mo>∧</mo><msub><mi>M</mi><mi>S</mi></msub><mo>[</mo><mi>k</mi><mo>,</mo><mi>j</mi><mo>]</mo><mo>)</mo></mrow></mrow></math></div>

Every middle index asks whether the corresponding two edges both exist. The outer disjunction asks whether any index works. Numerical multiplication and addition instead count such middle witnesses; converting a positive numerical result to true recovers the Boolean answer, but the numerical entries themselves are not relation entries.

## 3. Logical properties and their boundary cases

### 3.1 Definitions that can be proved or falsified

For a relation on a single carrier $A$, the following table gives exact conditions. Quantifiers range over the declared carrier, including isolated vertices. A failure witness must belong to that carrier.

| Property | Required condition | A witness that disproves it |
|---|---|---|
| Reflexive | Every $a$ satisfies $aRa$. | One element lacking its loop. |
| Irreflexive | No $a$ satisfies $aRa$. | One element possessing a loop. |
| Symmetric | $aRb$ implies $bRa$. | An edge whose reverse is missing. |
| Antisymmetric | $aRb$ and $bRa$ imply $a=b$. | Two distinct elements with both directional edges. |
| Asymmetric | $aRb$ implies that $bRa$ is false. | Any two-way pair, including a loop. |
| Transitive | $aRb$ and $bRc$ imply $aRc$. | Two consecutive edges with a missing shortcut. |
| Serial, or left-total on $A$ | Every $a$ has at least one outgoing edge. | One vertex with an empty outgoing row. |

Reflexivity and irreflexivity are not logical negations. Not being reflexive means at least one missing loop. Irreflexivity means all loops are missing. A relation with some but not all loops satisfies neither property. Likewise, not being symmetric does not mean being antisymmetric: a relation can contain one two-way pair and another unpaired edge, so it has neither property.

The variables in transitivity are not required to be distinct. A two-cycle $aRbRa$ forces the loop $aRa$ in a transitive relation. Ignoring this repeated-vertex case gives an incorrect transitivity verdict. Conversely, when no two edges can be chained, transitivity holds vacuously. The empty relation on a nonempty set is symmetric, antisymmetric, asymmetric, irreflexive, and transitive, but neither reflexive nor serial. On the empty carrier it satisfies every listed condition, since all universal quantifications are vacuous. There is exactly one relation on that carrier.

To prove a property of an infinite relation, choose arbitrary elements under the property's hypotheses and derive its conclusion. A list of successful examples cannot replace this proof. To disprove a property, supply one complete witness and show both the hypotheses and failed conclusion. For a finite matrix, check the diagonal for reflexivity, compare transpose entries for symmetry and antisymmetry, and test every two-edge combination for transitivity.

### 3.2 Implications, independence, and partial equivalence

Asymmetry is equivalent to antisymmetry together with irreflexivity. In one direction, asymmetry prohibits all loops and all reverse pairs. In the other, a reverse pair would force equality by antisymmetry, producing a loop prohibited by irreflexivity. This proof uses no transitivity assumption.

An irreflexive, transitive relation is automatically asymmetric. If both $aRb$ and $bRa$ held, transitivity would force $aRa$. Thus a strict partial order needs only irreflexivity and transitivity. Antisymmetry alone does not prohibit a directed three-cycle; adding transitivity prohibits all cycles of distinct vertices.

A relation that is both symmetric and antisymmetric has only diagonal pairs. It need not contain all diagonal pairs. If it is also reflexive, it is exactly $I_A$. A symmetric, transitive relation is sometimes called a **partial equivalence relation**. Its active domain $D$ contains precisely the elements with loops. To see this, if $aRb$, symmetry supplies $bRa$, and transitivity supplies $aRa$. Conversely, a loop itself witnesses active membership. On $D$, the relation is an equivalence relation; isolated elements outside $D$ are excluded. The defective argument “symmetry and transitivity imply reflexivity” silently assumes that every element has an outgoing edge. Adding seriality repairs it.

Useful alternative characterizations sharpen proof skills. A relation is **cyclic** when $aRb$ and $bRc$ imply $cRa$. Reflexivity plus cyclicity is equivalent to equivalence: use $aRaRb$ to obtain $bRa$, then cyclicity plus the newly proved symmetry to obtain transitivity. A relation is **right-Euclidean** when $aRb$ and $aRc$ imply $bRc$. Reflexivity plus right-Euclideanity is also equivalent to equivalence. From $aRb$ and $aRa$ obtain $bRa$; from $aRb$, the reverse $bRa$, and $bRc$, obtain $aRc$. The converse follows by reversing the first edge and composing with the second. Without reflexivity, either alternative may omit isolated elements or allow different structures.

### 3.3 Counting local constraints

For $n$ labelled elements there are $n$ diagonal positions and $q=n(n−1)/2$ unordered pairs of distinct elements. Reflexivity fixes all diagonals and leaves $n²−n$ entries free. Symmetry gives one binary choice for each diagonal and one for each unordered pair. Antisymmetry gives each unordered pair three choices: neither direction, forward only, or reverse only. Asymmetry additionally fixes every diagonal to absent.

| Condition | Number of relations |
|---|---|
| No constraints | $2^{n²}$ |
| Reflexive, or irreflexive | $2^{n²−n}$ |
| Symmetric | $2^{n+q}$ |
| Reflexive and symmetric | $2^q$ |
| Antisymmetric | $2^n3^q$ |
| Reflexive and antisymmetric | $3^q$ |
| Asymmetric | $3^q$ |
| Symmetric and antisymmetric | $2^n$ |
| Reflexive, symmetric, and antisymmetric | $1$ |

These are counts of local entry restrictions, not counts of transitive relations. Transitivity couples different unordered pairs, so one cannot multiply independent pair choices after adding it. On a fixed labelled set there are $n!$ total orders, since each permutation gives exactly one increasing listing. Equivalence relations correspond to partitions, leading to Bell numbers rather than a simple independent-entry power.

## 4. Powers, closures, and reachability

### 4.1 Exact lengths versus arbitrary lengths

For $R$ on $A$, define $R⁰=I_A$ and $R^{k+1}=R∘R^k$. Induction shows that $aR^kb$ holds exactly when a sequence of $k$ edges leads from $a$ to $b$. The base case is a length-zero path at the same element; the step appends an edge to an existing path. Exact powers are not necessarily nested: a chain may have a length-two path without a length-one edge, and a directed cycle may alternate which destinations are reached at even and odd lengths.

The transitive closure $R⁺$ includes positive-length reachability. The reflexive transitive closure $R⁎$ additionally includes zero-length paths:

<div class="formula-block"><math display="block"><mrow><msup><mi>R</mi><mo>+</mo></msup><mo>=</mo><munderover><mo>⋃</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>∞</mi></munderover><msup><mi>R</mi><mi>k</mi></msup></mrow></math><br>R⁎ = I<sub>A</sub> ∪ R⁺.</div>

To prove transitivity, concatenate two positive paths; their combined length is positive. To prove leastness, let $T$ be any transitive relation containing $R$. Induction on path length shows every $R$-path's endpoint pair belongs to $T$. Consequently $R⁺⊆T$. Adding all diagonal pairs gives the least reflexive transitive superset. This leastness proof is stronger than merely checking the output's properties: it shows that no unnecessary pair was added.

For a finite nonempty carrier with $n$ elements, a shortest path between distinct endpoints has no repeated vertex, so its length is at most $n−1$. A shortest positive closed path at a vertex may be a simple cycle of length $n$. Therefore

<div class="formula-block">R⁺ = R ∪ R² ∪ ··· ∪ Rⁿ<br>R⁎ = I<sub>A</sub> ∪ R ∪ ··· ∪ R<sup>n−1</sup>.</div>

The second bound does not lose cycle-induced loops, because the identity already supplies them. For $n=1$, the reflexive transitive closure is the identity regardless of whether the one loop originally existed. For the empty carrier all closures are empty and the finite unions are interpreted as empty unions. A claim about $R⁺$ that truncates at $n−1$ fails on a directed cycle of length $n$.

### 4.2 Closure existence and the order of operations

The reflexive closure is $r(R)=R∪I_A$; the symmetric closure is $s(R)=R∪R^{−1}$; the transitive closure is $t(R)=R⁺$. Each is extensive, monotone, and idempotent: it contains its input, respects input inclusion, and changes nothing when applied again. Extensiveness follows from the constructions; monotonicity follows by preserving edges or path witnesses; idempotence follows because the first output already has the required property.

These familiar closures do not justify a closure for every conceivable property. If all admissible supersets have a property preserved under intersection, and at least one admissible superset exists, their intersection is the least admissible superset. Reflexivity, symmetry, and transitivity satisfy this criterion on a fixed carrier. Antisymmetry is intersection-preserving, but an input containing both $(a,b)$ and $(b,a)$ for distinct elements has no antisymmetric superset at all. One cannot repair it by adding pairs.

Reflexive and symmetric closure commute because both simply add independent sets of pairs. Reflexive and transitive closure also commute: inserting loops into a path never creates a new pair of distinct endpoints, so $t(r(R))=r(t(R))$. Symmetric and transitive closure generally do not commute. If $R={(a,b),(a,c)}$, positive reachability adds no new pairs. Symmetrizing afterwards still lacks $(b,c)$, whereas symmetrizing first creates the path $b→a→c$. Thus $t(s(R))$ includes pairs missing from $s(t(R))$.

The least equivalence relation containing $R$ is

<div class="formula-block">e(R) = (R ∪ R<sup>−1</sup>)⁎.</div>

An undirected path can be traversed backwards, so this relation is symmetric; length-zero paths give reflexivity; concatenation gives transitivity. Every equivalence relation containing $R$ contains its reversed edges and all their finite paths, proving leastness. Its classes are the connected components after ignoring arrow orientation, including isolated vertices. Positive-length closure alone would omit the isolated vertices' loops.

Two existing equivalence relations $E,F$ on the same carrier have an equivalence intersection: each required implication holds in both operands. Their union need not be transitive; its equivalence closure is $(E∪F)⁺$, which is already reflexive because both inputs contain every loop. In partition language, intersection refines blocks, while equivalence closure of the union merges blocks connected through either relation. This is the mathematical reason behind repeated union operations in disjoint-set structures.

### 4.3 Warshall's algorithm and its invariant

Let vertices be numbered $0,…,n−1$. At stage $k$, allow the first $k$ vertices as internal vertices of a path. The initial matrix records direct edges only. When allowing vertex $k$, either an old path avoids it, or a path can be split into an old path to $k$ and an old path from $k$. Repeated visits to $k$ can be removed from a shortest witness without changing the endpoints; a positive closed witness is treated as a cycle rather than being replaced by a zero-length path.

<div class="formula-block">D<sup>(k+1)</sup>[i,j] = D<sup>(k)</sup>[i,j] ∨ (D<sup>(k)</sup>[i,k] ∧ D<sup>(k)</sup>[k,j]).</div>

The invariant is: after $k$ stages, the entry is true exactly when a positive-length path exists whose internal vertices belong to ${0,…,k−1}$. Induction on stages proves the recurrence correct. After $n$ stages, every internal vertex is allowed, so the matrix is $R⁺$. Set the initial diagonal to true when the desired result is $R⁎$.

```python
def transitive_closure(matrix, *, include_zero_length=False):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("A relation on one carrier needs a square matrix.")
    reach = [[bool(value) for value in row] for row in matrix]
    if include_zero_length:
        for i in range(n):
            reach[i][i] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (
                    reach[i][k] and reach[k][j]
                )
    return reach
```

In-place updates are valid for this loop order. During stage $k$, row $k$ and column $k$ do not change: their proposed updates have forms $x∨(x∧d)$ or $x∨(d∧x)$, both equal to $x$. Thus every new entry uses the same two pivotal values as the stage-start matrix. The outer pivot loop is essential for this invariant; arbitrarily exchanging the loops and making a single pass is not justified. The algorithm performs $n³$ constant-time Boolean updates and stores $n²$ entries. In an adjacency-list representation, a graph search from each vertex may be preferable for sparse graphs; it computes reachability by a different invariant, not by silently reordering Warshall.

## 5. Equivalence, partitions, and quotient constructions

### 5.1 Complete proof of the correspondence

An equivalence relation is reflexive, symmetric, and transitive. Fix one, denoted $∼$, on $A$. Define $[a]={x∈A:a∼x}$. Reflexivity puts $a$ in its own class, so every class is nonempty and the union of all classes is $A$. Suppose $z∈[a]∩[b]$. Then $a∼z$ and $b∼z$, so symmetry and transitivity give $a∼b$. For any $x∈[a]$, reverse $a∼b$ and compose $b∼a∼x$ to obtain $x∈[b]$. Swapping the roles proves the opposite inclusion. Hence intersecting classes are equal; distinct classes are disjoint.

Conversely, let a partition be a family of nonempty, pairwise disjoint blocks whose union is $A$. Relate two elements exactly when they occur in the same block. Each element belongs to a block, proving reflexivity. Being in the same block is symmetric. If $a,b$ share one block and $b,c$ another, the shared element $b$ forces those blocks to be equal, proving transitivity. The classes of the resulting relation are exactly the original blocks. Starting with a relation and returning through its partition also recovers exactly the original pairs. Therefore the two constructions are inverse bijections, including the empty partition of the empty set.

<div class="formula-block">a ∼ b ⇔ [a] = [b] ⇔ [a] ∩ [b] ≠ ∅.</div>

<!-- FIGURE:partition -->

The quotient set $A/∼$ is the set of distinct classes, not the set of chosen representative elements. It can have fewer elements than $A$, and its elements are subsets of $A$. A representative provides a name for a class, but several names may denote the same object. For finite blocks of sizes $b₁,…,b_k$, the relation consists of the union of the disjoint squares $B_i×B_i$, so it has $b₁²+···+b_k²$ pairs.

### 5.2 Examples and representative independence

For a positive integer $m$, integer congruence is defined by $a∼b$ when $m$ divides $a−b$. The difference is zero for equal arguments; negating a multiple of $m$ is a multiple of $m$; adding two such differences gives the third difference. These are the three required proofs. The classes are all integers with a fixed remainder, and there are exactly $m$ classes. A modulus must be specified; “same remainder” with no fixed divisor does not define a unique relation.

For any function $f:A→B$, the relation $a∼b$ defined by $f(a)=f(b)$ is an equivalence relation because equality is reflexive, symmetric, and transitive. Its classes are the nonempty fibers of $f$. Conversely, every equivalence relation is the equality-of-images relation for the projection $π:A→A/∼$ defined by $π(a)=[a]$.

Suppose we try to define a quotient function by $\bar g([a])=g(a)$. This construction is well-defined exactly when equivalent inputs have equal outputs. Necessity follows because $[a]=[b]$ must not produce two different answers. Sufficiency follows because replacing a representative by any equivalent representative leaves the result unchanged. This is a condition on $g$, not a consequence of merely writing brackets.

For example, parity of an integer descends to congruence classes modulo 8, since equivalent integers differ by an even multiple of 4. The integer itself does not descend: 1 and 9 name the same class but are different integers. Binary operations require checking both arguments: a proposed operation $[a]⊙[b]=[h(a,b)]$ must produce equivalent outputs whenever either input is replaced by an equivalent representative. Equality of outputs is not required if the output itself is a quotient class; equivalence of outputs is the correct criterion.

Rational numbers illustrate why domain restrictions matter. On pairs $(p,q)$ with $p∈ℤ$ and $q∈ℕ_{>0}$, define $(p,q)∼(r,s)$ when $ps=rq$. Reflexivity and symmetry follow immediately. For transitivity, $ps=rq$ and $rt=us$ imply $pst=rqt=qus$; cancellation of the nonzero $s$ gives $pt=qu$. Allowing a zero denominator would invalidate this cancellation and can destroy transitivity. Fractions are classes of valid pairs, not arbitrary pairs with zero denominators.

### 5.3 Counting classes and counting partitions

When all blocks of a finite equivalence relation have the same size $b$, the number of blocks is $|A|/b$. Without that equal-size condition, dividing by one chosen class size is invalid. For partitions of an $n$-element labelled set into exactly $k$ nonempty unlabelled blocks, write $S(n,k)$, a Stirling number of the second kind. Follow the final labelled element: either it forms a singleton block, leaving $S(n−1,k−1)$ possibilities, or it joins one of $k$ existing blocks, giving $kS(n−1,k)$.

<div class="formula-block">S(n,k) = S(n−1,k−1) + kS(n−1,k)<br>S(0,0) = 1; S(n,0) = 0 for n &gt; 0; S(n,k) = 0 for k &gt; n.</div>

The total number of partitions is $B_n=S(n,0)+···+S(n,n)$, the Bell number. The first values are $1,1,2,5,15,52$ for sizes zero through five. These also count equivalence relations on fixed labelled carriers. Do not multiply by $k!$: the blocks are unlabelled. If a question labels the blocks or asks for an onto function to a labelled $k$-element set, that extra factor is appropriate.

## 6. Preorders and partial orders

### 6.1 Equality versus indistinguishability

A preorder is reflexive and transitive. A partial order additionally satisfies antisymmetry. We write a partial order as $≼$ and call $(A,≼)$ a poset. Two elements are comparable when $a≼b$ or $b≼a$. A total, or linear, order makes every pair comparable. The failure of $a≼b$ in a partial order does not imply $b≼a$: the elements may be incomparable.

Subset inclusion is a partial order: every set includes itself; two mutual inclusions give equality; inclusions compose. Positive-integer divisibility is another. If $a$ divides $b$ and $b$ divides $a$, positive integer factors force both factors to be 1. On all integers the corresponding argument fails: 3 and −3 divide each other but are unequal. Divisibility on all integers is a preorder, and quotienting mutual divisibility identifies integers that differ only by sign, with zero forming its own class.

For a preorder $P$, define $a∼b$ when both $aPb$ and $bPa$. Reflexivity and symmetry are immediate. If $a∼b$ and $b∼c$, transitivity gives both directions between $a,c$, so this is an equivalence relation. Define a quotient comparison by $[a]≼[b]$ when $aPb$. It is well-defined: replacing $a$ by $a′∼a$ and $b$ by $b′∼b$ gives $a′PaPbPb′$, hence $a′Pb′$. The reverse replacement proves independence in both directions. Reflexivity and transitivity descend, and two mutual comparisons imply $a∼b$, hence equality of the classes. The quotient is therefore a partial order.

Directed reachability $R⁎$ is a preorder. Its mutual-reachability classes are the strongly connected components. Reachability between those components is a partial order: a cycle between distinct components would merge them. One-way reachability between original vertices is generally not an equivalence relation. Undirected connectivity and directed mutual reachability must not be confused.

### 6.2 Strict and nonstrict orders

Given a partial order $≼$, define $a≺b$ when $a≼b$ and $a≠b$. It is irreflexive. If $a≺b≺c$, transitivity gives $a≼c$; equality $a=c$ would create comparisons in both directions with $b$, forcing $a=b$ by antisymmetry. Hence $a≠c$, so $a≺c$. Conversely, starting with an irreflexive transitive relation $≺$, add the identity pairs. The result is reflexive, and its transitivity follows by considering whether either input comparison is equality. Two opposite strict comparisons would imply a prohibited loop, so the result is antisymmetric. These conversions undo one another.

A strict order is acyclic, but an acyclic graph need not already be transitive. An edge graph $a→b→c$ omitting $a→c$ is the smallest instructive example. Its positive reachability is a strict order. Adding the identity gives a partial order. Acyclicity alone describes immediate constraints; transitivity describes all consequences of those constraints.

### 6.3 Product, lexicographic, and dual orders

For posets $(A,≼_A)$ and $(B,≼_B)$, the product order compares both coordinates:

<div class="formula-block">(a,b) ≼<sub>P</sub> (a′,b′) ⇔ a ≼<sub>A</sub> a′ and b ≼<sub>B</sub> b′.</div>

Reflexivity and transitivity follow in each coordinate. Two mutual comparisons force equality in each coordinate by antisymmetry, proving equality of the pairs. Even if both factors are total, opposite coordinate movements can make two pairs incomparable: $(1,4)$ and $(2,3)$ demonstrate this under ordinary numerical order.

Lexicographic order gives priority to the first coordinate:

<div class="formula-block">(a,b) ≼<sub>L</sub> (a′,b′) ⇔ a ≺<sub>A</sub> a′ or (a = a′ and b ≼<sub>B</sub> b′).</div>

If both factors are total, the first unequal coordinate determines the direction, and equal first coordinates delegate to the second. To prove transitivity, examine two consecutive comparisons. If a strict first-coordinate increase occurs in either one, first-coordinate transitivity and equality cases give a strict increase overall. If both first coordinates remain equal, second-coordinate transitivity completes the proof. Antisymmetry forbids a first-coordinate increase in both directions and otherwise reduces to the second factor. These arguments use posets. Applying the formula with $a≠a′$ as the strict part of an arbitrary preorder can break transitivity; quotient the preorder first or use a properly defined asymmetric strict part.

The product order is contained in the lexicographic order on these posets: a first-coordinate product comparison is either strict or equality. The reverse containment fails. The dual order reverses every comparison. Reflexivity, antisymmetry, and transitivity are preserved; minimal and maximal, least and greatest, and upper and lower bounds exchange roles. Reversing a diagram's vertical orientation without changing the stated comparison would instead change its meaning.

### 6.4 Order embeddings and isomorphisms

A map is an order embedding when $a≼b$ holds exactly when $f(a)≼f(b)$ holds. In posets this condition implies injectivity: equal images give both comparisons and hence equal inputs. An order isomorphism is a bijective order embedding. A merely order-preserving bijection is insufficient because it might make originally incomparable elements comparable. Isomorphisms preserve covers, chains, antichains, bounds that exist, and extremal elements, since their inverse also preserves order.

For a squarefree number with distinct prime factors, send each divisor to the set of primes it contains. Divisibility is equivalent to subset inclusion, giving an isomorphism with a power-set poset. For a number with repeated prime factors, use exponent vectors; coordinatewise comparison gives the product of finite chains. This representation explains divisor Hasse diagrams and gcd/lcm bounds without relying on numerical size as the order.

## 7. Hasse diagrams, extrema, bounds, and lattices

### 7.1 Covers and diagram reconstruction

An element $b$ covers $a$, written $a⋖b$, when $a≺b$ and there is no $c$ with $a≺c≺b$. A Hasse diagram draws only cover edges, omits loops, and places greater elements above lesser ones. All upward paths imply comparisons by transitivity. Horizontal proximity, edge crossings, and equal drawing height do not by themselves assert comparability. This chapter uses upward-greater diagrams explicitly.

In a finite poset, every strict comparison can be expanded into a sequence of covers. If a comparison is not a cover, insert an intermediate element. Repeating cannot continue indefinitely because the inserted elements are distinct and the carrier is finite. Consequently the reflexive transitive closure of the cover graph recovers the entire partial order. In a dense infinite order such as the rationals, every strict comparison has an intermediate rational. Its cover relation is empty even though its order is not. Finiteness is essential to that reconstruction claim.

<!-- FIGURE:hasse -->

### 7.2 Minimal, maximal, least, and greatest

For $S⊆A$, an element $m∈S$ is minimal in $S$ if no different element of $S$ lies below it. It is a least element of $S$ if $m≼s$ for every $s∈S$. Maximal and greatest are the dual definitions. Least implies minimal. Minimal need not imply least because incomparable elements may remain. Minimality is relative to $S$, not necessarily to the whole carrier.

A least element is unique: if $m,m′$ are both least, then $m≼m′$ and $m′≼m$, so antisymmetry gives equality. The same proof gives uniqueness of a greatest element. A nonempty finite poset always has a minimal element: repeatedly moving strictly downward cannot repeat a vertex or continue past the number of vertices. Applying this argument within the elements below an arbitrary $s$ finds a minimal element below $s$. Therefore a **unique** minimal element of a finite nonempty poset is least. The dual assertion also holds. For infinite posets it can fail: a disjoint union of a singleton and the integers under their usual order has a unique minimal element, the singleton, but it is incomparable with every integer.

### 7.3 Bounds and the additional leastness test

An upper bound for $S$ is an element $u$ of the ambient carrier with $s≼u$ for every $s∈S$. It need not belong to $S$. A lower bound lies below every member of $S$. The supremum, or least upper bound, is an upper bound that lies below **every** upper bound. The infimum, or greatest lower bound, is defined dually. Antisymmetry ensures uniqueness whenever either exists.

To establish a supremum, perform two separate checks: prove the proposed element bounds every member of $S$, then choose an arbitrary upper bound and prove that the proposal lies below it. Being a minimal upper bound is weaker: other incomparable minimal upper bounds can exist. If $S$ has a greatest member, that member is its supremum, since every upper bound must bound that member. A supremum need not be a maximum: the open interval $(0,1)$ in the real numbers has supremum 1, which is absent from the interval.

For $S⊆T$, if both suprema exist in the same ambient poset, $sup(S)≼sup(T)$. Every upper bound of $T$ bounds $S$, so the leastness property for $S$ applies to $sup(T)$. Infima satisfy the reversed inequality. Changing the ambient carrier can change existence: the positive rational numbers with square less than 2 have supremum $√2$ in the real numbers, but no supremum in the rational numbers.

The empty subset is bounded above and below by every ambient element, by vacuity. Its supremum, if it exists, is the least element of the entire poset; its infimum is the greatest element. In the empty poset these objects do not exist, since a bound must be an element. In a finite nonempty poset, find the upper-bound set and test for its least member. A unique minimal upper bound suffices there, by the finite argument above; this shortcut is not valid for an arbitrary infinite poset.

### 7.4 Lattices and the scope of completeness

A nonempty poset is a lattice when every pair has a supremum and an infimum. Write $a∨b$ for the join and $a∧b$ for the meet; these symbols denote order operations here, not Boolean operations on arbitrary truth values. In a power-set lattice, join is union and meet is intersection. For all positive integers ordered by divisibility, join is lcm and meet is gcd. For the divisors of a fixed positive integer, these operations stay inside the carrier, so they also define a lattice.

Uniqueness of bounds proves commutativity. Joining an element with itself returns that element, proving idempotence. Both $(a∨b)∨c$ and $a∨(b∨c)$ are the least upper bound of the same three-element set: each bounds all three elements, and any common upper bound bounds each intermediate join. Thus join is associative; the dual proof applies to meet. Since $a≼a∨b$, their meet is $a$, proving absorption $a∧(a∨b)=a$. The dual absorption law follows similarly. These identities hold in every lattice. Distributivity does not: in the five-element diamond lattice, three incomparable middle elements have pairwise meet bottom and pairwise join top. For middle elements $a,b,c$, $a∧(b∨c)=a$ while $(a∧b)∨(a∧c)$ is bottom.

A complete lattice requires suprema and infima for **every subset**, including empty and unbounded subsets. A finite nonempty lattice is complete. Repeated finite joins and meets give the greatest and least elements by taking the whole carrier, and hence handle empty subsets as well. A nonempty complete lattice has both endpoints. The ordinary real-number order has neither, so it is not a complete lattice; it has the weaker least-upper-bound property for nonempty subsets bounded above. Adding both extended endpoints produces a complete lattice. Chain completeness, sometimes called completeness in programming-semantics notes, is another condition and must not be silently substituted for complete-lattice completeness.

## 8. Finite scheduling and well-founded reasoning

### 8.1 Linear extensions and unit-time layers

A linear extension is a total order on the same finite carrier that preserves every partial-order comparison. A nonempty finite poset has a minimal element; put any such element first, remove it, and apply induction to the induced order on the remainder. No remaining element was required to precede the removed one, and the inductive listing preserves all other constraints. The empty listing handles the zero-element base case. Thus every finite poset has a linear extension, often nonunique.

```text
remaining := all vertices
output := empty list
while remaining is not empty:
    choose a vertex with no strict predecessor in remaining
    append the vertex to output
    remove the vertex and its outgoing cover edges
return output
```

If an arbitrary input graph has no available vertex while some remain, it contains a directed cycle and cannot be a dependency DAG. A cover graph or any graph whose reachability gives the poset can be used; one need not explicitly materialize every transitive edge. With adjacency lists and maintained incoming-edge counts, the usual finite topological procedure takes time proportional to vertices plus edges. The choice among available vertices changes the total listing without invalidating it.

A chain is a subset whose distinct elements are all comparable. An antichain is a subset whose distinct elements are pairwise incomparable. The empty set and every singleton satisfy both definitions. The height of a finite nonempty poset is the maximum number of vertices in a chain; the width is the maximum number in an antichain. We count vertices, not edges, and give the empty poset height and width zero.

For unit-duration tasks and unlimited processors, define the level of $v$ as the length of a longest chain ending at $v$. A minimal element has level 1. If $u≺v$, append $v$ to a longest chain ending at $u$, so the level of $v$ is strictly larger. Hence equal-level vertices form antichains and can execute simultaneously after all predecessors finish. There are exactly height-many occupied levels, and a longest chain requires that many sequential slots. Thus the optimal time equals height under these assumptions. With unequal durations, the weighted critical path replaces the vertex count; with limited processors the height bound need not be achievable.

<!-- FIGURE:scheduling -->

The level argument also proves that the minimum number of antichains partitioning a finite poset equals its height: a longest chain needs one part per vertex, and the levels achieve that lower bound. If height is $h$ and width $w$, the level partition contains at most $w$ vertices per level, giving $n≤hw$. Thus a poset cannot simultaneously have both a short longest chain and a small largest antichain.

### 8.2 The dual chain-partition theorem, with proof

Dilworth's theorem states that the minimum number of chains partitioning a finite poset equals its width. The lower bound is immediate: a chain contains at most one member of an antichain. The matching construction supplies the less obvious upper bound without assuming that the level antichains can simply be turned sideways.

Create left and right copies of every vertex. Connect $x_L$ to $y_R$ exactly when $x≺y$. A matching is a set of edges sharing no endpoint. Matching edges link each vertex to at most one successor and at most one predecessor. Since strict comparisons have no cycles, these links form disjoint chains; a matching with $m$ edges gives $n−m$ chains. Conversely, a partition into $c$ chains gives a matching of $n−c$ edges by linking consecutive vertices within each chain. Therefore the minimum chain count is $n−m$ for a maximum matching.

To connect this count to width, we need the finite bipartite matching–cover fact. Start with a maximum matching. From unmatched left vertices, follow alternating paths: unmatched edges from left to right and matched edges from right to left. Let reached left and right vertices be $Z_L,Z_R$. No unmatched right vertex is reached, since the alternating path to it could be flipped to increase the matching. The set consisting of unreached left vertices and reached right vertices is a vertex cover. An uncovered edge would run from a reached left vertex to an unreached right vertex. If unmatched, it would be traversed; if matched, its left endpoint could not be reached without its partner, unless it were unmatched, which it is not. Both possibilities contradict being unreached. Each matched edge has exactly one endpoint in the cover: its endpoints are either both reached or both unreached. Every cover member lies on a matching edge, because unmatched left vertices are reached and unmatched right vertices are unreached. Thus the cover has exactly $m$ vertices. Any cover has at least $m$ vertices because the matching edges are endpoint-disjoint. This proves the needed equality.

Now collect the original vertices neither of whose copies belongs to this cover. Call the collection $U$. At most $m$ original vertices have a covered copy, so $|U|≥n−m$. Two distinct comparable members $x≺y$ would produce an uncovered edge $x_Ly_R$, impossible. Thus $U$ is an antichain. Its size is at least the minimum chain count, while every antichain's size is at most that count by the lower-bound argument. Equality follows. This proof is finite and constructive; no assertion about arbitrary infinite posets is being used.

### 8.3 Well-foundedness and induction

A strict relation is well-founded when every nonempty subset has an element with no predecessor inside that subset. A finite strict partial order is well-founded: any indefinitely descending sequence would repeat a vertex and create a cycle. A finite irreflexive relation alone need not be well-founded, because a directed two-cycle has no minimal vertex in its two-element subset. More generally, for a finite relation, well-foundedness is equivalent to having no directed cycle, including loops; transitivity is unnecessary for that equivalence.

The usual strict order on natural numbers is well-founded, while the usual order on all integers is not: the integers themselves have no least element. A well-order is a total order whose strict part is well-founded. For a partial order, well-foundedness gives minimal elements, possibly several incomparable ones; it does not give a least element of every subset.

If two posets are well-founded in their strict parts, their lexicographic product is well-founded. For any nonempty set of pairs, choose a minimal first coordinate among those appearing. Among pairs with that coordinate, choose a minimal second coordinate. No lexicographically smaller pair in the subset can have a smaller first coordinate or an equal first coordinate and smaller second coordinate. This proves minimality directly without needing a global decreasing numerical rank. The product order's strict part is contained in this lexicographic strict part, so it is well-founded too. On all finite words over an alphabet containing $a<b$, dictionary order need not be well-founded: $b,ab,aab,…$ is strictly decreasing.

Well-founded induction says: if for every $x$, truth of $P(y)$ for all $y≺x$ implies truth of $P(x)$, then $P$ holds throughout the carrier. Suppose otherwise. The set of counterexamples has a minimal member $x$. Every strict predecessor satisfies $P$, so the induction step proves $P(x)$, a contradiction. Minimal elements require no separate hidden predecessor: their induction hypothesis is vacuously true. For recursive definitions, one must additionally verify that each recursive argument decreases and that all nonrecursive operations are defined. An order proof by itself does not validate an undefined arithmetic operation.

## 9. Fully worked instructional problems

<!-- INCLUDE:problems -->

## 10. High-yield summary and complete exam rules

<!-- INCLUDE:review -->

## 11. Relation and reachability laboratory

The laboratory models one finite relation on the fixed carrier ${a,b,c,d}$. Toggle matrix entries to add or remove directed edges. Inspect failure witnesses for each property, compare positive and zero-length reachability, and advance Warshall one pivot at a time. The equivalence closure groups vertices by undirected connectivity; the directed reachability output preserves arrow directions. These are different constructions.

The demonstration is an explanation aid, not a pre-study examination. A computed verdict on four vertices is not a proof about every infinite relation. The displayed matrix is always Boolean. Resetting or changing an edge restarts the staged computation so that stages cannot silently refer to a different input.

<div class="lab" id="relation-lab">
<h3>Inspect a relation, then follow its closure</h3>
<p>Rows are sources and columns are targets. A pressed cell means the directed pair is present.</p>
<div class="lab-actions"><button type="button" id="lab-chain">Load chain</button><button type="button" id="lab-cycle">Load cycle and isolated vertex</button><button type="button" id="lab-empty">Clear edges</button></div>
<div id="lab-input"></div>
<div id="lab-properties" aria-live="polite"></div>
<h4>Warshall stages for positive-length paths</h4>
<p id="lab-stage" aria-live="polite"></p>
<button type="button" id="lab-next">Allow the next internal vertex</button>
<div id="lab-stage-matrix"></div>
<h4>Closures of the original input</h4>
<div id="lab-closures"></div>
<p id="lab-components"></p>
</div>

## 12. Exact references and coverage limits

1. **MIT.** Tom Leighton and Marten van Dijk, *6.042J / 18.062J Mathematics for Computer Science*, Fall 2010. [Chapter 7: Relations and Partial Orders](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/efac321fdc8d0b27586ca35b04aab808_MIT6_042JF10_chap07.pdf), printed pp. 213–236, PDF pp. 1–24. §§7.1–7.9 were read. The PDF's final page is an attribution notice. [Course page](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/). The teaching here uses total function to require exactly one target, whereas that text also uses function for a right-unique relation with a separate totality condition.
2. **Stanford.** Keith Schwarz, *CS103: Mathematical Foundations of Computing*, Spring 2017. [Binary Relations I](https://web.stanford.edu/class/archive/cs/cs103/cs103.1176/lectures/06/Small06.pdf): PDF pp. 7–8, 17–21, 24–25, 28–36, 42–49, and 56–57. [Binary Relations II](https://web.stanford.edu/class/archive/cs/cs103/cs103.1176/lectures/07/Small07.pdf): pp. 4–20, 27–28, 40–42, and 64–78. These are selected substantive pages; announcement and repeated animation slides are not claimed as separate content. [Problem Set 3](https://web.stanford.edu/class/archive/cs/cs103/cs103.1176/handouts/150%20Problem%20Set%203.pdf), pp. 2–4, supplies strict-order, Euclidean, partial-equivalence, rational-coset, and cover exercise patterns. Function-only exercises on pp. 5–6 belong to the next chapter. Negated relation symbols were checked against the original slide rendering because PDF text extraction can omit their slashes.
3. **Cambridge.** Peter Robinson, *Discrete Mathematics*, Computer Science Tripos Part IA, Michaelmas 2003 and Lent 2004. [Lecture notes](https://www.cl.cam.ac.uk/teaching/2003/DiscMaths/DiscMaths.pdf), Lent printed pp. 35–43, PDF pp. 37–45. Composition, equivalence, closures, Warshall, partial and total orders, products, Hasse diagrams, well-foundedness, and the relevant exercises were read. The present chapter corrects overbroad finite-irreflexivity and descending-sequence assertions; graph circuits and countability have separate chapter boundaries. The original matrix on PDF p. 40 was visually inspected.
4. **Oxford.** Andrew D. Ker, *Discrete Mathematics*, Michaelmas Term 2010. [Lecture notes](https://www.cs.ox.ac.uk/andrew.ker/docs/discretemaths-lecture-notes-mt2010.pdf), Chapter 4, printed pp. 45–56 / PDF pp. 55–66; Chapter 8, printed pp. 97–110 / PDF pp. 107–120. Both chapters and their practice answers were read. The present treatment qualifies lexicographic claims to posets, corrects the complete-lattice claim about real numbers, and uses the correct direction for the witness disproving an upper bound. The 2022–2023 Oxford catalogue is a screened offering, not the date or instructor of these 2010 notes.
5. **Cornell.** Michael George, *CS2800: Discrete Structures*, Spring 2017. [Lecture 6: Relations](https://www.cs.cornell.edu/courses/cs2800/2017sp/lectures/lec06-relations.html), relation-properties section; [Lecture 7: Equivalence Relations](https://www.cs.cornell.edu/courses/cs2800/2017sp/lectures/lec07-equivalence.html), equivalence, partitions, quotient sets, and well-defined constructions. These independently authored pages supplement the four principal courses. The linked MIT textbook is not counted as a second independent course text.

The lesson covers the declared chapter boundary, including the advanced extensions explicitly taught above. Finite matching is introduced only to prove the chain-partition theorem; general graph matching algorithms have a later graph boundary. Abstract ordinal theory, infinite order-extension theorems, full domain theory, and general lattice representation theorems are outside this chapter. The problem bank samples every identified in-scope reasoning pattern and includes original extensions, rather than claiming to reproduce every exercise on the internet. Archived Iranian examination papers remain reserved for the final month.

The accompanying [source-selection audit](../reviews/d_relations-sources.html) records the screened pool, the actual reading depth, corrected source issues, and the topic-to-source mapping. Mathematical proofs and finite checks support the documented coverage. They cannot establish a literal guarantee about every unseen future examination question. This is a complete review draft awaiting the student's approval for promotion to the approved library.
