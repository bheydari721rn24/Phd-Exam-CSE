## Sources and learning contract

This chapter develops divide-and-conquer algorithms from their specifications, proves their combination steps, and analyzes the cost of the actual representation. Four principal written university sources are MIT 6.006, Stanford CS161, UC Berkeley's CS170-associated Algorithms reader and CMU 15-451/651. A fifth genuinely reviewed course, ETH Zurich's Data Structures and Algorithms, supplies maximum-subarray material. The [source comparison and reading audit](../reviews/a_divide-sources.html) explains the eight-university candidate pool, selected pages, rejected candidates and source qualifications.

The prerequisites are arrays, induction, asymptotic notation, recurrences, basic integer arithmetic and matrix multiplication. Complex numbers and primitive roots of unity are developed before the Fourier algorithm. You should be able to reconstruct a proof and an implementation, rather than only recall a recurrence.

| Component | Required outcome |
|---|---|
| Specification and recursive design | State the input, output, termination measure, child contract and complete combination argument. |
| Search, merge and inversions | Preserve the right interval or multiset; handle duplicates and empty inputs; distinguish stable ties from strict inversions. |
| Maximum subarrays | Explain both the crossing scan and the constant-size summary that reduces the running time to linear. |
| Closest pair | Prove the geometric candidate bound and keep both coordinate orders without sorting again at every level. |
| Karatsuba and Strassen | Derive reduced product counts algebraically and preserve digit widths and block multiplication order. |
| FFT and convolution | Derive even/odd splitting, primitive-root requirements, the inverse and sufficient zero padding. |
| Examination reasoning | Identify the computational model, repair an incomplete algorithm and explain why a tempting shortcut fails. |

This is an auditable treatment of this boundary, not a promise about every possible unseen question. Full quicksort, selection, randomized analysis and general correctness methods have later dedicated chapters. National entrance-exam archives are reserved for the final month.

## Design before recurrence

### The four obligations

A recursive algorithm is specified by an input domain, a postcondition and a decreasing measure. For an array problem, length is often the measure; for multiplication, digit length is more informative than the integer's numerical value. A legal recursive call must satisfy the child's precondition and reduce the measure whenever the base case does not apply. Balanced splitting alone does not prove either correctness or termination.

Write the proof in this order. First, solve every base case, including empty or singleton inputs according to the specification. Second, define the children precisely. Third, assume the child contracts hold and show that the combination establishes the parent contract. Finally, derive costs from the implemented division and combination operations. Deriving a recurrence before checking the algorithm can produce a correct analysis of an incorrect program.

For two array halves use the half-open interval $[lo,hi)$ and $mid=lo+⌊(hi−lo)/2⌋$. If $hi−lo≥2$, both $[lo,mid)$ and $[mid,hi)$ have positive lengths smaller than the parent. They are disjoint and their concatenation is the original interval. Odd lengths are covered automatically. The subtraction form of the midpoint also avoids overflow from adding two large fixed-width indices.

The children need not be disjoint in every problem: algebraic algorithms may derive different combinations of the same input blocks. What matters is that all child instances are well-defined and smaller. In dynamic programming, repeated subproblems are cached; ordinary divide and conquer recomputes them unless an additional mechanism is introduced.

### What information must a child return?

Returning only the child's final answer can be insufficient. Two half-arrays can have the same best internal subarray sum but different suffix sums. When the parent asks for a crossing interval, those suffix sums affect the answer. The missing information is a *boundary summary*. Strengthening the child contract may reduce the combination cost dramatically.

Other representations offer the same lesson. A sorted half-array supports merging; a point set in y-order supports a linear closest-pair combination; a polynomial's values at carefully chosen points support componentwise multiplication. Representation changes are part of algorithm design and must be charged in the cost.

For balanced children and a combination cost $g(n)$, the usual recurrence is $T(n)=T(⌊n/2⌋)+T(⌈n/2⌉)+g(n)$. However, copying slices may add a linear cost even when the conceptual combination is constant. A claimed linear summary algorithm should pass index ranges rather than repeatedly copy subarrays.

### Work, span and storage

Work counts all executed operations. Span counts the longest dependency chain when independent child calls may run in parallel. Two parallel halves do not halve the total work. A sequential linear merge still contributes a linear term to span. Storage concerns simultaneously live memory, not the sum of every temporary allocation over the run.

A sequential depth-first implementation can release a child's temporary storage before exploring unrelated branches. A parallel implementation may keep many branches live at once. Statements about space should therefore name the execution and allocation policy. Recursion depth is logarithmic for balanced splitting but linear for repeated removal of one element.

## Search and stable merging

### Binary search as a one-child design

For a sorted array, the useful general primitive is lower bound: return the first position whose value is at least the target, or the length if none exists. Its result is meaningful even if the target is absent or repeated.

Maintain a half-open candidate interval $[lo,hi)$. Every position before $lo$ is known to contain a value smaller than the target. Every position at or after $hi$ is known to contain a value at least as large. Initially both claims hold vacuously. If the middle value is smaller, sortedness justifies discarding all positions through the midpoint. Otherwise the midpoint may be the answer, so retain it by moving the upper boundary to it.

```python
def lower_bound(a, target):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

Each iteration reduces the interval length. At termination the interval is empty and the boundary invariants identify the first feasible position. To test membership, additionally check that the returned position is within the array and equals the target. Never index the returned length.

The cost is $O(log(n+1))$ comparisons with constant auxiliary space, assuming random access. On a linked list, reaching a midpoint may cost linear time; copying half-arrays similarly destroys the intended cost. Binary search is also called decrease and conquer because it recurses into only one half. The terminology does not change its proof.

### Merge: three separate postconditions

A sorting routine should preserve the input multiset and establish sortedness. Stability is an additional property: equal-key records retain their original order. A sorted list that drops an item is not a correct sort. A sorted multiset with equal records reversed is correct only if stability was not required.

Suppose two sorted runs are contiguous pieces of the original input. During merging, the output prefix must contain exactly the consumed items, in sorted order. At each step the smaller unconsumed head is a minimum of all remaining items, because everything later in its run is at least as large. If the heads tie, taking the left head preserves original run order. Exhaustion must be checked before indexing either run.

Every step consumes one item. Once one run is exhausted, the other sorted remainder can be appended. The resulting list contains every input item exactly once. Induction on the merge-sort recursion then proves sortedness and multiset preservation. Stability also follows by induction: equal-key items in the same child keep their order, and equal-key items across the split are taken from the left child first.

This argument requires the left run to precede the right run in the original sequence. Arbitrarily rotating runs through a queue can destroy global stability even if every individual merge is locally stable. A bottom-up stable merge sort combines adjacent runs of lengths one, two, four and so on, preserving their original run order.

### Counting strict inversions during the merge

An inversion is an index pair $i<j$ with $A_i>A_j$. Equal values do not form inversions. Each inversion belongs to exactly one of three classes: wholly left, wholly right or crossing the split. Child calls count the first two classes.

During a merge, if the right head is strictly smaller than the left head, it is smaller than every unconsumed left item. Each of those items preceded it in the original array. Therefore add the number of remaining left items. If the heads tie, take the left head and add nothing. Cross inversions with a right item are counted when that item is consumed, so no pair is counted twice.

```python
def sort_and_count(a):
    if len(a) <= 1:
        return list(a), 0
    mid = len(a) // 2
    left, left_count = sort_and_count(a[:mid])
    right, right_count = sort_and_count(a[mid:])
    out, i, j = [], 0, 0
    count = left_count + right_count
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
            count += len(left) - i
    out.extend(left[i:])
    out.extend(right[j:])
    return out, count
```

The code is written for totally ordered numeric values. A stable record sort compares keys with the same left-on-equality rule. Values such as floating-point NaN, which do not satisfy a total order, require an explicit ordering policy before this reasoning applies.

<!-- FIGURE:merge -->

### Cost and representation

Merging lengths $p$ and $q$ takes $Θ(p+q)$ output work and at most $p+q−1$ head comparisons when both lengths are positive. Ordinary merge sort performs linear work at each of logarithmically many levels, giving $Θ(n log n)$ for $n≥2$, including already sorted inputs in this nonadaptive implementation.

The illustrative slicing implementation has $O(n)$ peak live list storage plus $O(log n)$ stack frames under sequential depth-first execution. The sum of allocations over the run is $Θ(n log n)$; that is different from peak storage. A reusable output buffer and index ranges can reduce allocation overhead without changing the asymptotic work.

The inversion count can be as large as $n(n−1)/2$, so a fixed-width counter must be checked for overflow. Python integers grow as needed, but very large counts bring bit costs beyond a unit-cost RAM analysis. An algorithm can write its final output back into the original array and still require linear auxiliary memory; mutation is not the definition of constant-space sorting.

## Maximum subarrays and sufficient summaries

### State whether an empty interval is legal

For a nonempty array, the nonempty maximum-subarray problem asks for $0≤i<j≤n$ maximizing the sum over $[i,j)$. If all entries are negative, the answer is the largest entry, not zero. The empty-allowed version permits $i=j$ and has answer at least zero. This chapter uses the nonempty version unless explicitly stated otherwise.

The cubic baseline enumerates all intervals and sums each from scratch. There are $n(n+1)/2$ nonempty intervals. The total number of inspected elements is $n(n+1)(n+2)/6$, hence cubic work. Prefix sums reduce an interval query to $Q_j−Q_i$, giving a quadratic enumeration after linear preprocessing. These baselines are useful independent checkers and explain what recursion is improving.

### Three exhaustive locations

Split after position $m$. Any interval lies entirely left, entirely right, or crosses the boundary. A crossing interval must consist of a nonempty suffix of the left half and a nonempty prefix of the right half. Choices of the suffix start and prefix end are independent, so the maximum crossing sum is the largest left suffix plus the largest right prefix.

Scan backward from the left boundary and forward into the right half to find those maxima. Initialize each maximum from an actual item, or use negative infinity as a comparison identity. Initializing to zero silently changes the specification. Compare the two recursive answers with the crossing answer. The three-location classification proves correctness; the scans give $T(n)=2T(n/2)+Θ(n)$ and therefore $Θ(n log n)$ work.

### Return four quantities instead

For a nonempty segment $X$, define its total sum $T_X$, maximum nonempty prefix sum $P_X$, maximum nonempty suffix sum $S_X$ and maximum nonempty interval sum $B_X$. A singleton with value $v$ has summary $(v,v,v,v)$.

For a concatenation $XY$, the exact combination rules are:

<!-- MATH:summary -->

The total is additive. A prefix either stops inside $X$ or contains all of $X$ and a nonempty prefix of $Y$. A suffix either stays inside $Y$ or contains a nonempty suffix of $X$ and all of $Y$. An interval lies in $X$, lies in $Y$, or crosses using the best suffix and prefix. Those statements establish each formula by an exhaustive, nonoverlapping classification of possibilities.

The formulas do not require nonnegative totals. For example, a negative total in the left half may make its own best prefix preferable to extending into the right half. Knowing only the best interval values cannot decide this.

```python
def join_summary(left, right):
    lt, lp, ls, lb = left
    rt, rp, rs, rb = right
    return (
        lt + rt,
        max(lp, lt + rp),
        max(rs, rt + ls),
        max(lb, rb, ls + rp),
    )

def subarray_summary(a):
    if not a:
        raise ValueError("A nonempty array is required.")
    def solve(lo, hi):
        if hi - lo == 1:
            v = a[lo]
            return (v, v, v, v)
        mid = lo + (hi - lo) // 2
        return join_summary(solve(lo, mid), solve(mid, hi))
    return solve(0, len(a))
```

Every internal node uses constant summary work. A full binary tree with $n$ singleton leaves has $n−1$ internal nodes, even for odd lengths. Hence the algorithm uses $Θ(n)$ work and $O(log n)$ auxiliary stack space with fixed-size summaries and index ranges. This is not the same algorithm as rescanning prefixes and suffixes at every node.

<!-- FIGURE:subarray -->

### Associativity, witnesses and order

The summary of a concatenation is uniquely determined by the underlying sequence. Combining summaries for $(XY)Z$ and $X(YZ)$ therefore gives the same result; the operation is associative. This is a semantic proof, valid beyond a finite test. The operation is not commutative because reversing two segments changes prefixes, suffixes and crossing order.

An optional empty-segment identity is $(0,−∞,−∞,−∞)$, using the rules that a finite number plus negative infinity is negative infinity. This identity is an algebraic convenience; it does not make the best nonempty interval of an empty input a legal returned answer. Software should reject that input or return a separately documented absence value.

To return an interval witness, store endpoints with every prefix, suffix and best interval. Offset right-local indices by the left length. Choose ties consistently, for example by larger sum, then smaller start, then smaller end. The same tie order must be used in child selection and combination. A returned sum without matching endpoints is an incomplete implementation of the witness specification.

These summaries also support segment trees: build in linear work, update a single value in logarithmic work, and answer a range by combining summaries in original left-to-right order. Arbitrarily rearranging partial results is invalid despite associativity. Kadane's scan is another linear algorithm: the best interval ending at the current position either starts there or extends the previous best ending interval. For the nonempty version initialize from the first item rather than zero.

Any exact algorithm on unrestricted numeric arrays must inspect every entry in the worst case. An uninspected entry could be changed to a sufficiently large positive value, changing the answer without changing observed data. The linear algorithms match that input-reading lower bound in the stated model.

## Closest pair: geometry and representation

### Contract and preprocessing

Given distinct point records in the Euclidean plane, return two different record IDs attaining the smallest distance. Records may have equal coordinates. Fewer than two records have no pair. Two records at the same coordinates immediately give distance zero, which no distance can improve.

Use squared distance $(x_1−x_2)^2+(y_1−y_2)^2$ when coordinates are integers: comparisons remain exact and no square root is needed. Fixed-width squaring can overflow. A real-RAM cost model treats coordinate arithmetic and comparisons as constant cost; arbitrary-length coordinates need separate bit-cost analysis. Approximate floating-point coordinates require a numerical policy, especially at nearly equal distances.

Assign unique IDs. Sort once by $(x,y,id)$ and separately by $(y,x,id)$. A recursive instance receives the same records in both orders. Split the x-ordered sequence by rank into halves, with midpoint coordinate $c$ separating them weakly. Equal x-coordinates are assigned by rank and ID, not by a test such as $x<c$, which might send almost every point into one child.

Partition the y-ordered sequence by membership in the left-ID set. Filtering preserves y-order and costs linear time with constant-time membership in the stated model. A boolean membership array indexed by dense IDs provides deterministic access; a hash set's expected cost should not be silently described as deterministic worst-case constant time.

### Why the strip is sufficient

Find the closest pair in each half and let $δ$ be the smaller child distance. A better pair with endpoints in opposite halves has both horizontal coordinates within $δ$ of the dividing coordinate. Otherwise their horizontal separation alone would be at least $δ$. Keep this strip in y-order.

For a strip point $p$, a potentially improving partner above it must have y-difference smaller than $δ$. Points farther away vertically cannot improve the distance. The crucial remaining question is how many candidates can lie in this window.

### Seven successors: the half-specific packing proof

Consider the strip rectangle from height $y_p$ to $y_p+δ$, of width at most $2δ$. Its left-half portion fits into a rectangle of width $δ$ and height $δ$, partitioned into four squares of side $δ/2$. Two points from the left recursive half in one square would be at distance at most $δ/√2<δ$, contradicting the definition of the child distance. Therefore each square holds at most one left-half point. The right-half portion yields the same bound.

There are at most eight points total in the window, counting $p$. Thus at most seven later points in y-order can improve its distance. Crucially, this is a bound on each color separately. A left point and a right point may be arbitrarily close; the claim that *all* strip points are pairwise at least $δ$ apart is false.

Half-open cell ownership removes ambiguity for points on grid lines. Tied x-coordinates on the dividing line are assigned to their original recursive half and use that half's four cells. Their numerical positions can coincide with cell boundaries without violating the same-half separation argument. Duplicate coordinate records have already returned zero.

<!-- FIGURE:geometry -->

Comparing each point with its next seven strip successors is enough for finding a strictly better distance. Keeping one previously found witness on ties is valid. If a separate requirement asks for the lexicographically smallest pair among *all* equal-distance pairs, the strict-improvement proof alone is insufficient; the tie-enumeration policy needs its own argument.

### Complete implementation

The following implementation accepts integer coordinate pairs and returns squared distance and an attaining ID pair. Its preprocessing detects duplicate coordinates. At each recursion, it preserves both sorts and uses a reusable dense membership array, avoiding a hash-table complexity assumption.

```python
def closest_pair(points):
    n = len(points)
    if n < 2:
        return None
    px = sorted((x, y, i) for i, (x, y) in enumerate(points))
    for a, b in zip(px, px[1:]):
        if a[:2] == b[:2]:
            return 0, (a[2], b[2])
    py = sorted(px, key=lambda p: (p[1], p[0], p[2]))
    marks = [False] * n
    def distance(a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    def solve(xs, ys):
        if len(xs) <= 3:
            best = None
            for i in range(len(xs)):
                for j in range(i + 1, len(xs)):
                    d = distance(xs[i], xs[j])
                    if best is None or d < best[0]:
                        best = d, (xs[i][2], xs[j][2])
            return best
        m = len(xs) // 2
        lx, rx = xs[:m], xs[m:]
        c = rx[0][0]
        for p in lx:
            marks[p[2]] = True
        ly, ry = [], []
        for p in ys:
            (ly if marks[p[2]] else ry).append(p)
        for p in lx:
            marks[p[2]] = False
        left, right = solve(lx, ly), solve(rx, ry)
        best = left if left[0] <= right[0] else right
        strip = [p for p in ys if (p[0] - c) ** 2 < best[0]]
        for i, p in enumerate(strip):
            for q in strip[i + 1:i + 8]:
                if (q[1] - p[1]) ** 2 >= best[0]:
                    break
                d = distance(p, q)
                if d < best[0]:
                    best = d, (p[2], q[2])
        return best
    return solve(px, py)
```

The shared membership array is reset before recursive calls, so one call does not inherit another's marks. Every nonbase recursive call has at least four points and two children of at least two, so the child answers exist. Updating the best distance during scanning can only shrink the improvement window; the original seven-successor bound remains safe.

The two initial sorts cost $O(n log n)$. Filtering, splitting and strip scanning cost $O(n)$ per recursive instance. Therefore the overall cost is $O(n log n)$ with $O(n)$ peak live sequence storage under depth-first evaluation. Sorting the strip by y from scratch at each call instead gives a linear-logarithmic toll and $O(n log^2 n)$ work. The constant seven is specific to the two-dimensional Euclidean packing argument, not an automatically valid rule in higher dimensions or other metrics.

## Karatsuba: replace a product with algebra

### Representation and the ordinary four products

Let the radix be $B≥2$. Split a nonnegative integer after its lowest $m$ digits:

<!-- MATH:split -->

The low parts lie between zero and $B^m−1$. The high parts contain all remaining digits, including an extra digit when the total width is odd. Expanding the product gives the high-high term shifted by $2m$ digits, the two mixed terms shifted by $m$, and the low-low term without a shift. Ordinary recursion therefore uses four roughly half-size products. With linear-cost additions and shifts, its ideal bit recurrence gives quadratic work.

Do not write the high shift as the total digit count unless that count is exactly $2m$. For an odd width, the shift is still $2m$. Padding a representation with leading zero digits does not change its value, but arithmetic shifts must match the chosen low-part width.

### Three products suffice

Compute $z_2=x_Hy_H$, $z_0=x_Ly_L$ and $z_d=(x_H−x_L)(y_H−y_L)$. Distributivity gives $z_d=z_2+z_0−x_Hy_L−x_Ly_H$. Thus the mixed coefficient is $z_2+z_0−z_d$, and the final result is:

<!-- MATH:karatsuba -->

This is an identity, not an approximation. A negative difference product is allowed; subtracting it adds its magnitude. Recursive unsigned multiplication can handle the absolute differences and apply their signs afterward.

The commonly taught sum variant uses $(x_H+x_L)(y_H+y_L)$ and subtracts the two unmixed products. It is also correct, but a sum can require one more digit than its parts. A recurrence that ignores this extra digit needs a padding or rounding argument. In the difference variant, the absolute difference of two bounded nonnegative parts fits within the larger part's width. Both variants have the same standard asymptotic exponent.

<!-- FIGURE:karatsuba -->

### Original implementation and its contract

```python
def karatsuba(x, y):
    sign = -1 if (x < 0) != (y < 0) else 1
    def multiply(a, b):
        n = max(a.bit_length(), b.bit_length())
        if n <= 3:
            return a * b
        m = n // 2
        mask = (1 << m) - 1
        ah, al = a >> m, a & mask
        bh, bl = b >> m, b & mask
        z2 = multiply(ah, bh)
        z0 = multiply(al, bl)
        da, db = ah - al, bh - bl
        zd = multiply(abs(da), abs(db))
        if (da < 0) != (db < 0):
            zd = -zd
        middle = z2 + z0 - zd
        return (z2 << (2 * m)) + (middle << m) + z0
    return sign * multiply(abs(x), abs(y))
```

The base case handles zero and small magnitudes without recursion. For every larger instance, high, low and absolute-difference operands have at most $⌈n/2⌉$ bits, which is smaller than $n$. This proves termination, including unequal and odd widths. The algebraic identity and the inductive child contracts prove the returned product exactly; the outer sign then handles all signed inputs.

### Complexity: state what a primitive operation costs

In a bit model, adding, subtracting or shifting an $n$-bit integer costs at most linear work in its represented size. Three recursive products yield $M(n)≤3M(⌈n/2⌉)+O(n)$, hence $M(n)=O(n^{log_2 3})$. For a fixed-width padded three-branch recursion with linear toll, the corresponding recurrence has a tight theta bound. A value-dependent implementation can have cheaper calls on particular inputs; do not infer a per-instance lower bound merely from the worst-case recurrence.

This analysis does not treat an arbitrary-precision multiplication as constant time. It also does not assert that this illustrative Python routine is faster than a language runtime's built-in multiplication, which uses its own algorithms and thresholds. Karatsuba is a design and bit-complexity result; practical crossover points require measurement.

For a worked decimal split, take $x=123$, $y=45$ and $m=1$. Then $(x_H,x_L)=(12,3)$ and $(y_H,y_L)=(4,5)$. The three products are $48$, $15$ and $9⋅(−1)=−9$. The mixed coefficient is $48+15−(−9)=72$. Recombining gives $48⋅100+72⋅10+15=5535$. The high part has two digits here, but the shifts are determined by the one-digit low parts.

## Strassen: seven ordered block products

### Why block multiplication works

Partition square matrices of even dimension into compatible blocks:

<!-- MATH:blocks -->

Each entry of the upper-left output block is the sum of products over the first half of the shared index plus the sum over the second half. Those sums are precisely the corresponding entries of $AE$ and $BG$. The other three blocks follow by the same index split. This proves the block formula from the definition of matrix multiplication, rather than treating blocks as commuting scalar symbols.

Standard recursive multiplication computes eight half-size block products and combines them with quadratic entrywise work. The recurrence gives cubic arithmetic work. Strassen constructs seven products instead. The chosen naming convention below is fixed throughout this chapter:

<!-- MATH:strassen-products -->

Denote the output product's blocks by $R_{11},R_{12},R_{21},R_{22}$ in row order. Recombine the seven products as follows:

<!-- MATH:strassen-result -->

### Prove every block without commuting factors

Expand each product using distributivity. The upper-left expression becomes $AE+AH+DE+DH+DG−DE−AH−BH+BG+BH−DG−DH=AE+BG$. The upper-right expression is $AF−AH+AH+BH=AF+BH$. The lower-left expression is $CE+DE+DG−DE=CE+DG$. The lower-right expression is $AF−AH+AE+AH+DE+DH−CE−DE−AE−AF+CE+CF=CF+DH$.

Only like ordered products cancel. We never replace $AE$ by $EA$. Therefore the derivation works for matrix blocks, where multiplication is generally noncommutative, as long as addition, subtraction and distributivity are available. A formula proved only by swapping factors of scalar entries may fail on recursive matrix blocks.

The mathematical identities require a ring with additive inverses, not division. They remain valid over integers and finite fields, including characteristic two with subtraction interpreted appropriately. Boolean OR/AND arithmetic and min-plus arithmetic do not supply the same subtraction operations, so these identities cannot simply be transplanted to those semirings.

### Exact small example

For matrices with rows $(1,2),(3,4)$ and $(5,6),(7,8)$, the seven products are respectively $−2,24,35,8,65,−30,−22$. Their recombination gives $19,22,43,50$ in row order. For example, the upper-left value is $65+8−24−30=19$, while the lower-right is $−2+65−35−(−22)=50$. Computing the ordinary four dot products confirms the result independently.

```python
def strassen_blocks(A, B, C, D, E, F, G, H, add, sub, mul):
    p1 = mul(A, sub(F, H))
    p2 = mul(add(A, B), H)
    p3 = mul(add(C, D), E)
    p4 = mul(D, sub(G, E))
    p5 = mul(add(A, D), add(E, H))
    p6 = mul(sub(B, D), add(G, H))
    p7 = mul(sub(A, C), add(E, F))
    return (
        sub(add(add(p5, p4), p6), p2),
        add(p1, p2),
        add(p3, p4),
        sub(sub(add(p1, p5), p3), p7),
    )
```

The helper expresses the seven-product identity for any compatible blocks using supplied addition, subtraction and multiplication operations. A recursive matrix program supplies recursive multiplication and a classical base case; a proof test can supply exact small matrix blocks. Passing callbacks does not itself make this a complete high-performance matrix library.

### Padding, models and practical limitations

The recurrence is $T(n)=7T(n/2)+Θ(n^2)$, giving $Θ(n^{log_2 7})$ arithmetic operations in the regular recursion. Pad a non-power-of-two square dimension to the next power $N$: then $n≤N<2n$. Fill the additional rows and columns with zero and return the original-sized upper-left part. The constant-factor increase in dimension preserves the exponent.

Input and output storage alone are quadratic. Intermediate storage depends on scheduling and buffer reuse; storing every temporary at every depth is unnecessary. Large integer entries can grow, so arithmetic operations are not automatically constant-bit-cost operations. Floating-point additions and subtractions introduce roundoff and possible cancellation. Algebraic exactness does not prove numerical superiority.

For small sizes, sparse matrices or strongly rectangular matrices, ordinary multiplication may be preferable. An asymptotic exponent does not establish a practical crossover or a universal speedup. Padding a very skinny rectangular problem into a huge square can waste work; a rectangular strategy must account for its dimensions directly.

## Polynomial multiplication and Fourier division

### Coefficients, convolution and the change of representation

A polynomial of degree at most $d$ has $d+1$ coefficients. Store coefficients in increasing power order, including zeros for missing powers. If $A$ has length $m$ and $B$ length $k$, their product has length at most $m+k−1$. Its coefficient at index $r$ is the sum of $a_i b_j$ over $i+j=r$, with out-of-range coefficients treated as zero. Direct convolution uses quadratic work for comparable lengths.

Evaluation respects multiplication: at any point $z$, $(AB)(z)=A(z)B(z)$. Thus we can evaluate both polynomials at enough points, multiply corresponding values, and interpolate the result. We need distinct evaluation points: two polynomials of degree less than $N$ agreeing at $N$ distinct points are equal. Their difference would otherwise be a nonzero polynomial with at least $N$ roots, contradicting the root bound obtained by repeatedly factoring out a root.

An arbitrary choice of points does not make evaluation and interpolation fast. Fourier points are chosen because the even/odd split turns one evaluation problem into two half-size problems.

### Complex numbers and primitive roots

A complex number is $u+iv$ with $i^2=−1$. Multiplication follows distributivity: $(u+iv)(s+it)=(us−vt)+i(ut+vs)$. On the unit circle, $e^{iθ}=cos θ+i sin θ$ and multiplication adds angles. Its magnitude is one.

For a positive integer $N$, choose $ω=e^{2πi/N}$. Then $ω^N=1$, and no smaller positive exponent equals one. Such a root has order $N$ and is called primitive. Its powers $1,ω,…,ω^{N−1}$ are distinct. Merely satisfying $ω^N=1$ is insufficient: choosing one for every evaluation point loses all information except the sum of coefficients.

For an even power of two $N≥2$, $ω^{N/2}=−1$ and $ω^2$ is a primitive root of order $N/2$. To prove the second statement, $(ω^2)^r=1$ means $N$ divides $2r$, so the smallest positive such $r$ is $N/2$. These properties drive the recursion.

### Derive the butterfly

Split coefficients by parity, not into a low and a high contiguous half. Write $A(x)=E(x^2)+xO(x^2)$, where $E$ contains the even-indexed coefficients and $O$ the odd-indexed coefficients. Each has $N/2$ coefficients after padding.

Evaluate both at powers of $ω^2$. For $0≤j<N/2$, let $E_j=E(ω^{2j})$ and $O_j=O(ω^{2j})$. The outputs are:

<!-- MATH:butterfly -->

The second equation follows from two root identities:

<!-- MATH:parity -->

The children solve all the necessary even and odd evaluations. Each pair of parent outputs needs one twiddle-factor multiplication and two additions or subtractions. This two-output dependency is a butterfly.

<!-- FIGURE:fft -->

Two half-size transforms plus linear combination give $Θ(N log N)$ arithmetic operations. A positive power-of-two length guarantees that repeated halving reaches one. Arbitrary lengths need other factorizations or padding and should not be passed unchanged to this radix-two implementation.

```python
import cmath

def fft(a, inverse=False):
    n = len(a)
    if n == 0 or n & (n - 1):
        raise ValueError("Length must be a positive power of two.")
    direction = -1 if inverse else 1
    def transform(values):
        size = len(values)
        if size == 1:
            return [complex(values[0])]
        even = transform(values[::2])
        odd = transform(values[1::2])
        omega = cmath.exp(direction * 2j * cmath.pi / size)
        out = [0j] * size
        factor = 1 + 0j
        for j in range(size // 2):
            term = factor * odd[j]
            out[j] = even[j] + term
            out[j + size // 2] = even[j] - term
            factor *= omega
        return out
    result = transform(a)
    return [v / n for v in result] if inverse else result
```

This chapter uses the positive-exponent forward transform and negative-exponent inverse. Some libraries reverse those signs. Either convention works if the pair is consistent. The inverse normalization is applied once at the outermost result, not at every recursive level.

### Derive the inverse instead of memorizing a sign

The forward transform is the following finite weighted sum:

<!-- MATH:forward -->

Multiply $Y_j$ by $ω^{−jt}$, sum over $j$ and exchange the finite sums. The coefficient of $a_r$ becomes a geometric sum with exponent difference $q=r−t$. If that difference is zero, the sum is $N$. Otherwise it is nonzero modulo $N$, since both indices lie between zero and $N−1$. Primitivity makes the ratio different from one. The geometric identity then gives:

<!-- MATH:geometric -->

The denominator is nonzero, and the numerator is zero because $ω^N=1$. These facts recover the original coefficient after division by $N$:

<!-- MATH:inverse -->

Therefore the same transform structure with $ω^{−1}$, followed by division by $N$, recovers every coefficient. Distinct exponents modulo $N$ and the primitive-root condition are essential to this orthogonality argument.

If $F$ is the unnormalized Fourier matrix, the same calculation gives the following identities, where the star denotes conjugate transpose and the double bars denote the complex Euclidean norm:

<!-- MATH:normalization -->

Only the normalized matrix $U$ is unitary and preserves that norm. Calling the unnormalized transform a norm-preserving rotation is incorrect.

### Zero padding and circular aliasing

Choose a power of two $N≥m+k−1$ and pad both coefficient arrays to length $N$. Compute their transforms, multiply values componentwise, and invert. Because the product degree is below $N$, unique interpolation recovers the ordinary convolution without ambiguity.

If $N$ is too short, evaluation at the $N$th roots cannot distinguish $x^N$ from one. The inverse then returns coefficients modulo $x^N−1$: high-degree coefficients wrap around and add to lower indices. This is circular convolution, not the requested ordinary polynomial product.

For example, $(1+x)^2=1+2x+x^2$. A length-two transform identifies $x^2$ with one, returning coefficients $(2,2)$. Length four is sufficient and returns $(1,2,1,0)$. The extra zero is padding, not a coefficient of an additional nonzero term.

### Numerical and exact arithmetic alternatives

The complex implementation uses floating-point approximations. An inverse coefficient near an integer can be rounded only when an error bound guarantees an error below one half in the relevant norm. Small examples passing tests do not establish this for arbitrarily large coefficients or lengths. Repeated twiddle multiplication also introduces roundoff.

A number-theoretic transform uses a finite field instead. For a prime modulus $p$, choose a primitive root of order $N$ with $N$ dividing $p−1$, and require that $N$ is nonzero and invertible in the field. The same geometric-sum proof works because the nonzero denominator is invertible. In the field modulo seventeen, two has order eight: its fourth power is sixteen, its eighth power is one, and no earlier divisor of eight gives one. The inverse of eight is fifteen.

Such a transform recovers coefficients modulo the prime, not automatically as ordinary integers. To recover signed integer coefficients, choose enough moduli so their product exceeds twice an established absolute coefficient bound, then use Chinese remainder reconstruction and signed representatives. The field conditions, coefficient bound and reconstruction are additional obligations; “exact modular arithmetic” alone is not a proof of exact unrestricted integer convolution.

The butterfly network has logarithmic stages and linear work per stage. In a common iterative in-place organization, the coefficient positions are first permuted by reversing their binary index bits. For length eight the order is $0,4,2,6,1,5,3,7$. This permutation follows the recursive even/odd choices from low-order bit to high-order bit; it is not a sort by coefficient value.

## Choosing a method and proving its boundary

| Task | Useful child representation | Combination | Stated-model work |
|---|---|---|---|
| Lower-bound search | Sorted interval with excluded-prefix/suffix invariants | Keep one half | Logarithmic comparisons |
| Merge sort / inversions | Sorted sequence and optional inversion count | Linear stable merge | Linear-logarithmic |
| Maximum subarray, crossing scan | Best internal answer | Linear boundary scans | Linear-logarithmic |
| Maximum subarray, augmented summary | Total, prefix, suffix and best | Constant-size ordered combination | Linear |
| Planar closest pair | Identical record sets in x-order and y-order | Filter and seven-successor scan | Linear-logarithmic |
| Karatsuba | High/low digit parts | Three products and linear bit arithmetic | Subquadratic bit-operation upper bound |
| Strassen | Compatible matrix blocks | Seven ordered block products | Subcubic arithmetic-operation count |
| Radix-two FFT | Even and odd coefficient subsequences | Linear butterflies | Linear-logarithmic arithmetic-operation count |

The table is not interchangeable across computational models. An array access, a large integer product, a matrix-block product and a complex multiplication have different meanings. Always identify the size parameter and the cost units before comparing algorithms.

For a new problem, derive the parent answer from exhaustive answer locations or an algebraic identity. Ask what boundary information the child must retain. Find a representation that makes the combination cheap, prove it sufficient, and only then solve the recurrence. Check empty inputs, singleton inputs, odd sizes, duplicate keys, ties, degenerate geometry, arithmetic overflow and invalid algebraic operations.

There are problems for which an apparently natural summary is insufficient or no cheap combination is known. A recurrence cannot repair missing information. Conversely, discovering a stronger constant-size summary can remove a logarithmic factor, as maximum subarrays demonstrate. The examination skill is identifying the reason for the speedup, rather than associating every two-child recursion with the same complexity.

## Fully worked problem bank

All statements and explanations below are independently authored. Source exercise families are identified where relevant; no past national entrance-exam questions are used. The bank tests specification repair, counterexamples, derivations and exact computations as well as running-time analysis.

<!-- INCLUDE:problems -->

## Complete summary and examination rules

The main lesson contains the derivations. This final section gives complete sentences for revision and a reproducible decision procedure; it is not a replacement for the proofs.

<!-- INCLUDE:review -->

## Interactive summary laboratory

The laboratory works with nonempty intervals and bounded exact integers. It computes the recursive four-component summary, shows both children and the crossing candidate, and compares the result against an independent enumeration of all nonempty intervals. It returns an interval witness with ties resolved by earlier start and then earlier end. Try the presets to see why all-negative arrays, crossing answers and equal best sums require explicit policies.

<!-- LAB:subarray -->

## References, reading scope and limits

1. **MIT — 6.006 Introduction to Algorithms, Spring 2020.** Erik Demaine, Jason Ku and Justin Solomon. [Recitation 3: Sets and Sorting](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/1869dbf640ded6b31f1bd369d2001ef5_MIT6_006S20_r03.pdf). PDF pages 1–7 read; merge representation, stability and sorted-array searching used.
2. **Stanford — CS161 Design and Analysis of Algorithms.** Gregory Valiant's hosted course materials. [Lecture 2: MergeSort, Recurrences and Asymptotics](https://theory.stanford.edu/~valiant/cs161/CS161Lecture02.pdf). PDF pages 1–7 read. The note is dated September 28, 2016; it is hosted under the Winter 2017 course. Named scribes are Michael P. Kim (2015) and Ofir Geri (2016).
3. **UC Berkeley — CS170-associated Algorithms reader.** Sanjoy Dasgupta, Christos H. Papadimitriou and Umesh V. Vazirani. [Chapter 2: Divide-and-Conquer Algorithms](https://people.eecs.berkeley.edu/~vazirani/algorithms/chap2.pdf). PDF pages 1–9 and 12–36 read; printed pages 55–63 and 66–90. Integer multiplication, block products, polynomial representation, FFT, inverse derivation and the exercise list used.
4. **Carnegie Mellon — 15-451/651, Spring 2021.** Danny Sleator and David Woodruff. [Closest Pair lecture, April 27, 2021](https://www.cs.cmu.edu/~15451-s21/lectures/lec21-closest-pair.pdf). PDF pages 1–3 used for deterministic geometry and preprocessing. Page 3 was visually inspected. Later randomized material and image-only code are not claimed as source coverage.
5. **ETH Zurich — Data Structures and Algorithms, 2018.** Felix Friedrich. [Handout 2](https://lec.inf.ethz.ch/DA/2018/slides/daLecture2.en.handout.2x2.pdf). PDF pages 7–13, slides 97–121, read. Maximum-subarray baseline, crossing decomposition, linear scan and lower-bound discussion used.

The [source audit](../reviews/a_divide-sources.html) records the larger screened pool and every selected scope. Source-specific exercises are represented by independently authored variants and thematic mappings. Topics assigned to later chapters are not counted as covered here. The four-component laboratory, code, diagrams and problem solutions are original teaching material.

Finite execution checks supplement mathematical proofs; they cannot prove an unrestricted theorem. Floating-point FFT code is educational and has stated numerical limits. This chapter remains a draft until your explicit approval. Scientific care supports a strong preparation resource, but cannot guarantee literal completeness across all worldwide courses or perfect performance on all unseen questions.
