## Mathematical constructions for precise cost models

### 1. Derive encoding lengths before substituting them into costs

For positive $U$, ordinary binary notation has $b(U)=\lfloor\log_2U\rfloor+1$ bits. The proof is the interval equivalence $b(U)=b\iff2^{b-1}\le U<2^b$. Numerical magnitude and position count are different objects; the largest $b$-bit integer is $2^b-1$, while $2^b$ itself needs $b+1$ bits. Zero needs a separate encoding convention because its logarithm is undefined.

Suppose a procedure performs exactly $U$ charged iterations. Its worst cost among inputs of length $b$ is $2^b-1$, although its expression in the numeric parameter is linear. If it performs $mU$ iterations on an $m$-item input, write the complete serialization length before classifying the result. Fixed-width capacities and weights bounded by $U$ might contribute $\Theta(m\log(U+1))$ bits, whereas other fields and delimiters contribute additional terms. An exponential dependence on the capacity bit length does not automatically imply an identical formula in the total length of every possible instance.

The important family is obtained by holding $m$ fixed and allowing a binary capacity to grow. Then the full length grows logarithmically in $U$, while the capacity-sized table grows linearly in $U$. If another promise bounds $U$ by a fixed polynomial in $m$, the restricted family's classification changes. Thus the encoded domain, rather than one observed capacity, determines whether a worst-case polynomial claim is justified.

### 2. Separate scalar events, word instructions and bit work

In a word-RAM, each primitive works on a bounded number of $w$-bit words. A binary integer of $b$ bits spans at least $\lceil b/w\rceil$ payload words. An exact operation on such an integer may be a multiword algorithm; a source-language operator is not its instruction count. A scalar-operation model may deliberately price that same mathematical operation as one event. These are different resource conventions.

For an explicit bit example, adding four-bit operands 7 and 3 starts from `0111` and `0011`. Processing columns from the least significant bit gives the following exact ripple states.

| Column | Operand bits and carry in | Sum bit | Carry out |
| ---: | --- | ---: | ---: |
| 0 | $1+1+0=2$ | 0 | 1 |
| 1 | $1+1+1=3$ | 1 | 1 |
| 2 | $1+0+1=2$ | 0 | 1 |
| 3 | $0+0+1=1$ | 1 | 0 |

The result is `1010`, or ten. One ideal word addition and four bit-stage calculations can describe the same arithmetic under different charging conventions. This ripple demonstration is not a claim about a processor's physical carry circuitry. General exact big-integer addition or multiplication needs its own representation and operand-size bounds.

Likewise, doubling $2^{k-1}$ has operand length $k$. A model charging that length produces total $\sum_{k=1}^nk=n(n+1)/2$. A representation storing only its exponent could price this special family differently; it cannot silently replace the declared dense-integer cost model.

### 3. Prove a decision-tree bound and state exactly what it proves

If each test has at most $r\ge2$ possible outcomes, a depth-$d$ tree has at most $r^d$ leaves. This follows by induction: a depth-zero tree has one leaf, and each of at most $r$ child trees of depth at most $d-1$ contributes at most $r^{d-1}$. If $q$ answers must be distinguished, correctness requires $r^d\ge q$ and hence $d\ge\lceil\log_rq\rceil$.

Two distinctions are essential. First, count the outputs actually required by the contract: $n!$ distinct relative key orders differ from $n^n$ arbitrary self-maps, and repeated-key assignments can reduce distinguishable orders by a multiplicity-factor denominator. Second, having enough leaves is necessary but need not be sufficient: legal key comparisons might be unable to partition candidate inputs into equal-sized branches. The capacity calculation alone supplies no exact optimal algorithm.

For binary comparison sorting, $n!$ required orders yield the familiar logarithmic factorial bound. The inequalities $(n/2)^{n/2}\le n!\le n^n$ for sufficiently large integers $n$ show that its order is $n\log n$. An integer algorithm inspecting bits or using keys as addresses obtains information through operations outside that comparison tree; it therefore needs a different bound rather than violating the original one.

### 4. Derive both sides of an exact merge count

When ordinary merging compares two current front keys, one comparison emits exactly one key while both inputs are nonempty. For nonempty lengths $p,q$, earliest exhaustion needs at least $\min(p,q)$ comparisons. If all keys from the shorter list precede every key of the other, that minimum is attained. The last possible comparison happens with two total keys still unconsumed, giving maximum $p+q-1$. Distinct globally largest and second-largest keys assigned to opposite inputs attain that maximum.

An exact supplied-array trace must enumerate the compared pairs; summing the worst-case maxima can overestimate it. Copies of the tail do not compare keys. All outputs are nevertheless written, so total merge work remains linear in $p+q$ under ordinary explicit-output accounting even when the comparison count is smaller.

For sequentially incorporating $k$ equal lists with $m=n/k$ keys each, stage $j$ processes $jm$ keys. Summing gives $m(k(k+1)/2-1)$ emitted-key work and worst comparison total $m(k(k+1)/2-1)-(k-1)$. A balanced schedule instead shares work across logarithmically many levels. The distinction comes from the schedule's changing subproblem sizes, not simply the word “merge.”

### 5. Expected updates are not expected loop lengths

For a uniformly permuted distinct array, let $I_i$ indicate that position $i$ is a prefix minimum. Symmetry among the first $i$ positions gives $\operatorname{Pr}(I_i=1)=1/i$. Summing indicators gives exact expected update count $H_n$, with no independence premise. The same execution always performs $n$ comparisons against the running minimum.

The integral estimates $\ln(n+1)\le H_n\le1+\ln n$ show logarithmic expected update growth. They neither change the linear number of scanned keys nor establish a logarithmic worst-case update count: decreasing input updates at every position. If the algorithm initializes from the first element instead of infinity, its later replacement count has expectation $H_n-1$. Ties or a nonuniform permutation distribution change the symmetry argument and must be modeled before applying it.

### 6. Total work, peak live storage and output volume

For sequential balanced recursion with constant-size frames, total calls and simultaneously live calls are different sets. At size $2^h$, the complete recursion tree has $2^{h+1}-1$ calls, but only one root-to-leaf path of $h+1$ frames is live at maximum depth. If each nonleaf combine phase costs its subproblem size, each of $h$ levels contributes total work proportional to the original size. Hence work is $\Theta(n\log n)$ while stack storage is $\Theta(\log n)$ words under the stated constant-frame condition.

An output stream can also dwarf live storage. Full subset vectors emit $n2^n$ bits; full permutations emit $n\,n!$ references; all triples emit $3\binom n3$ references. An iterator may retain only one current object, but completing the explicit output still charges every required payload unit. Packing $w$ bits per output word changes a bit-write bound to a word-write bound; accepting a compressed description changes the contract itself.

The lower bound applies to explicit materialization. To claim every input entry must be read, an additional sensitivity proof is needed. On an unsummarized all-zero array, altering any unread entry to one changes the answer to “are all entries zero?” without changing the observed transcript. Thus a correct deterministic procedure must inspect every entry on that input. A trusted stored length or precomputed all-zero flag removes this indistinguishability pair and changes the task's available information.

### 7. Exact arithmetic distinguishes equality, height and representation

A finite binary leaf-mass inequality follows from halving a root's unit mass. Its equality condition is fullness, not perfect balance. A perfect tree with $N=2^h-1$ keys has $h$ nonempty levels and a deepest successful path with $h$ node comparisons, although its edge height is $h-1$. Another search tree with the same number of keys can be a linear chain. Node count, edge height and a charged key comparison are separate quantities.

Repeated squaring creates a different kind of growth: from $x_0=2$ and $x_{k+1}=x_k^2$, exact values are $2^{2^k}$ and bit lengths are $2^k+1$. A source-level sequence of $k$ squarings therefore does not imply $k$ fixed-width exact word operations. The special input family can be compactly described by exponents, but materialized integer output still needs all its bits.

### 8. Interpret the two contract demonstrations below

The insertion-sort animation uses six tagged records with keys $[4,2,3,1,3,2]$. Its sorted-output contract requires both nondecreasing keys and preservation of each original record. During insertion, a saved record and the non-hole array slots jointly preserve that multiset; comparing only the visible non-hole keys would miss the temporarily saved item. Record tags distinguish identity from the sorting key.

The shortest-path animation is a separate example of a verifiable output certificate, not a lesson claiming that insertion sort computes paths. The directed edges are $0\to1$ of weight 2, $0\to2$ of weight 5, $1\to2$ of weight 1, $2\to3$ of weight 3, and $1\to3$ of weight 7. Proposed distances are $(0,2,3,6)$ and the tight parent path is $0\to1\to2\to3$. Each edge satisfies $d(v)\le d(u)+w(u,v)$; summing these inequalities along a rooted path shows its cost is at least the label of its endpoint. The tight parent paths attain those labels. Together these two directions prove the shortest distances. Feasible inequalities alone would not: the all-zero labels satisfy them on this nonnegative graph without giving its actual positive distances.

These demonstrations explain how a computational problem specifies admissible outputs and how an independently checked witness can establish correctness. Their finite executions illustrate those contracts; full algorithm analysis is developed in the subsequent chapters.
