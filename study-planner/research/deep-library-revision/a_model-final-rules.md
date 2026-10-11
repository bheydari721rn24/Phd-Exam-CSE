## Complete computation-model rules and examination traps

### 1. Write the input and output contract before counting

Specify admissible values, their representation, required outputs, permitted observations and charged resources. “Find a duplicate pair,” “return all duplicate pairs,” and “return whether a pair exists” allow different outputs and can impose different unavoidable work. An algorithm's deterministic choice can still solve a relation that permits several correct answers.

### 2. Binary length jumps at exact powers of two

For $U>0$, the minimal unpadded length is $\lfloor\log_2U\rfloor+1$. The pair $2^b-1,2^b$ has lengths $b,b+1$. Zero requires its separate encoding convention. Replacing the floor-plus-one by a ceiling fails exactly at powers of two.

### 3. An exactly $b$-bit positive integer has a range

Its values are $2^{b-1}\le U\le2^b-1$. A value-linear loop therefore has worst iteration count $2^b-1$, not $b$ or $2^b$ as an exact answer. Approximate asymptotic notation may ignore the final minus one; an exact interval or count may not.

### 4. Unary and binary lengths cannot be interchanged freely

Unary uses $U$ marks, whereas binary uses logarithmically many bits. The same $U$-iteration routine is linear in unary length and may be exponential in binary length. Converting a short binary description into materialized unary output has its own large writing cost.

### 5. State all input parameters and field widths

An $m$-element array of fixed $b$-bit values has $mb$ payload bits before metadata. A dense $r\times c$ matrix has $rc$ entries. Graphs require their representation: adjacency lists use vertex and edge records, whereas a matrix has $V^2$ positions. A parameter such as matrix width or vertex count is not automatically total encoded length.

### 6. Address width and length-counter width differ

Addressing $M$ cells numbered zero through $M-1$ requires $\lceil\log_2M\rceil$ bits for $M\ge2$. Holding the integer $M$ itself requires $\lceil\log_2(M+1)\rceil$. At $M=256$, these are eight and nine. Extra allocation must fit the address space too.

### 7. A word instruction has bounded-size operands

A primitive word operation acts on a constant number of $w$-bit words under a specified instruction set. A growing exact integer can span many words, turning one source operator into a subroutine. Multiplication and division must be explicitly allowed when a constant-cost argument depends on them.

### 8. Declare overflow and arithmetic semantics

Exact integers, modular words, saturating arithmetic and trapping arithmetic produce different behaviors. The exact value $2^{64}$ needs 65 bits, while reduction modulo $2^{64}$ gives zero. Word-level execution and correctness of an exact-integer specification require compatible semantics.

### 9. Initialization and preprocessing are charged phases

Returning one stored entry can be constant time, while eagerly zeroing $M$ cells requires $M$ one-cell writes. A direct-address query's constant cost comes after establishing a table and inserting keys. Analyze total work as preprocessing plus queries when the contract begins with raw input.

### 10. State whether input is resident or streamed

Random access allows an arbitrary indexed read without consuming all prior positions. A sequential stream may require traversing a prefix. A precomputed summary supplies extra information. A lower bound proved for one interface cannot be transferred without checking these access assumptions.

### 11. Read-all lower bounds need an indistinguishability pair

On a chosen input, alter an unread coordinate while keeping the entire observed transcript fixed and show that the correct answer changes. For the all-zero test, the modified coordinate can be one. Merely asserting that each coordinate matters somewhere does not prove that all must be read on one common execution.

### 12. Distinguish bits, words, references and scalar events

Writing $B$ packed bits can require about $\lceil B/w\rceil$ word writes, while $R$ one-word references require $R$ writes. A scalar multiplication is not automatically one bit operation. Specify alignment, framing and whether a primitive emits a bounded number of output units.

### 13. Explicit output count multiplies objects by description length

Full subset vectors emit $n2^n$ bits. Full permutation lists emit $n\,n!$ references. Full unordered triples emit $3\binom n3$ references. Counting objects alone omits their mandated descriptions; a compact generator or change stream has a different output interface.

### 14. A capacity-sized table is not a bit-length-sized table

For an exactly $b$-bit capacity, $cW$ cells have maximum $c(2^b-1)$. A $W+1$-state table includes capacities zero through $W$; a $W$-cell table excludes one endpoint. Keep the declared endpoint convention and cell unit in exact counts.

### 15. Pseudo-polynomial describes the specified method

A bound polynomial in item count and numeric values may be superpolynomial in their binary encoding lengths. This does not prove every algorithm for that problem is slow. Restrictions relating numeric parameters to structural ones can change the admitted family's bound.

### 16. Count only distinguishable outputs in information bounds

Distinct sorting keys admit $n!$ relative orders. Four zero positions among eight positions admit $\binom84=70$ outcomes. Permuting indistinguishable same-key records does not create another required key assignment. A stable-output rule must also be interpreted using the original positions.

### 17. Apply the branch-capacity inequality with the correct arity

At most $r$ outcomes per test and $q$ required distinctions imply $r^d\ge q$, so $d\ge\lceil\log_rq\rceil$. Distinct-key less/greater comparisons effectively branch twice; a truly ternary observation has another capacity. Rounding down can leave inputs indistinguishable.

### 18. An information lower bound is not exact attainability

Enough leaves are necessary, but legal comparisons may prevent the balanced partitions that attain that capacity. A matching upper bound needs an algorithm. Worst-case depth also does not mean every input takes that many comparisons; early terminal paths may be shorter.

### 19. Comparison restrictions do not cover integer addressing

Using an integer key as an address or inspecting its bits can obtain information outside opaque-key comparisons. Such an algorithm must charge its key range, word width, table construction and space. It changes the model rather than contradicting a comparison-only theorem.

### 20. Ordinary merge has exact endpoint bounds

For nonempty lengths $p,q$, key comparisons range from $\min(p,q)$ to $p+q-1$. An initially empty list requires zero. Every comparison emits one key while both sides are nonempty; after exhaustion, tail copying does not compare keys.

### 21. Trace a supplied array instead of substituting the worst case

Record each pair of current fronts at every merge stage. The authentic eight-key example uses 16 comparisons, whereas the corresponding general worst-case maximum is 17. An asymptotic order cannot determine that input's exact count.

### 22. Sequential and balanced merge schedules differ

Sequentially incorporating equal lists processes sizes $2m,3m,\ldots,km$, giving $m(k(k+1)/2-1)$ emitted-key work. Balanced merging instead processes all keys across logarithmically many levels. Specify $m=n/k$, divisibility and $k\ge2$ before deriving the sequential bound.

### 23. Distinguish scan comparisons from successful minimum updates

A length-$n$ running-minimum scan performs $n$ comparisons under the infinity-initialized convention. In a uniform distinct permutation, expected updates are $H_n$, while decreasing input has $n$ updates. Initializing from the first key changes the counted updates by one.

### 24. Use indicators without inventing independence

For prefix minima, symmetry gives probability $1/i$ at position $i$. Linearity yields $\mathbb E[Y]=\sum_i1/i$ without an independence premise. Ties and nonuniform permutations require a new probability argument. The harmonic mean is not exactly $\ln n$.

### 25. Exact matrix counts depend on the implementation convention

Direct $r\times s$ by $s\times c$ multiplication uses $rsc$ scalar products and $rc(s-1)$ chain additions for $s\ge1$. Accumulating from zero uses $rcs$ source additions instead. Count products, additions, fused instructions and bit work separately.

### 26. An algorithmic operation count is not a problem lower bound

The direct matrix method has $n^3$ products, but that does not forbid reorganized algebraic methods. A procedure's proved upper cost is distinct from a lower bound covering every allowed algorithm. Stating the direction of the bound prevents this common inference error.

### 27. Use the eligible index region for nested comparisons

Comparing each key with every earlier key visits $1\le j<i\le n$, totaling $\binom n2=n(n-1)/2$. Adding the diagonal gives $n(n+1)/2$; allowing both orientations gives a different set. Data-dependent exits require their own witness inputs and distributions.

### 28. Peak live stack is not the whole recursion tree

Sequential balanced recursion has one live root-to-leaf path. Constant-size frames give logarithmic stack storage even when combine work is $\Theta(n\log n)$. Copied subarrays, retained buffers, parallel sibling calls or nonconstant frame storage change that conclusion.

### 29. Search counts nodes; tree height often counts edges

A successful key at edge depth $d$ requires $d+1$ node-key comparisons under one three-way comparison per visit. A perfect tree of $2^h-1$ keys has $h$ nonempty levels. An unsuccessful null check has no additional stored key; a different Boolean-instruction metric must be stated explicitly.

### 30. Fullness, perfection and a fixed node count are different

The finite binary leaf-mass equality characterizes full branching, not equal depths. A perfect-height premise yields logarithmic search, while a one-child search-tree chain can have linear depth at the same size. State exactly which structural invariant supplies the bound.

### 31. Check exact intermediate widths before declaring unit cost

Repeated exact squaring from two gives $x_k=2^{2^k}$ with $2^k+1$ bits. The number of source statements may be tiny while operands outgrow a machine word. A sparse exponent representation and dense materialized output are different choices with different charges.

### 32. Finite measurements do not establish universal extrema

A measured maximum across selected inputs is no greater than the maximum across the whole admissible family under the same metric. It is not a universal upper bound. Best, worst and average cost use different quantifiers; average cost additionally needs a stated distribution.
