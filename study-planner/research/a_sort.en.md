# Comparison and Non-comparison Sorting

## 1. Sources, scope, and study route

This chapter combines five written university courses. The four core selections are **MIT 6.006** (Erik Demaine, Jason Ku, Justin Solomon), **Princeton COS226** (Robert Sedgewick and Kevin Wayne, slide authors), **CMU 15-122** (Frank Pfenning, Lecture 7 author), and **Oxford B16** (Andrea Vedaldi). **Stanford CS161** (Mary Wootters) supplies a fifth selected treatment of randomized analysis and radix invariants. The [source comparison](../reviews/a_sort-sources.html) gives exact reading ranges, selection reasons, corrections and limitations. References at the end link directly to written documents; videos are unnecessary.

Prerequisites are arrays, loop invariants, induction, asymptotic notation, elementary recurrences, logarithms and basic expectation. Earlier chapters establish these tools; here they are applied precisely enough to answer questions that change the implementation, cost model or input restrictions. The adjacent selection and priority-queue chapters develop their complete interfaces separately. This chapter includes the heap representation and construction needed to understand heapsort.

Read Sections 2–4 first. Study a method by matching its contract, code, proof, cost and animation. Then compare methods using Sections 13–18. The solved-problem bank is part of the instruction: many questions test how an apparently familiar formula fails after a condition changes. Finally read the complete-sentence examination rules. There is no quiz before teaching.

The scope includes ordering and stability; selection, insertion, binary insertion, bubble and gap sorting; stable merging and merge-sort variants; Lomuto, classic Hoare, CMU and three-way partitions; randomized quicksort and pivot guarantees; Floyd heapsort; comparison lower bounds with restricted inputs; counting, radix, bucket and string sorting; adaptive runs, hybrids, external merging and implementation hazards. Every claim carries its model. Neither a finite course collection nor a finite verification suite can guarantee an outcome on every unseen examination question.

## 2. What a sorting algorithm must preserve

A record has a **key**, which determines ordering, and a **payload**, which belongs to that particular occurrence. Two records can have the same key without being the same record. Throughout the animations, letters identify original occurrences: for example, $2_a$ and $2_b$ are distinct records whose keys are both two. Comparisons ignore the letters unless a problem explicitly asks for an index tie-breaker.

For an array $A$ of length $n$, an ascending sort must satisfy both conditions:

$$A'_i\le A'_{i+1}\quad(0\le i<n-1).$$

$$\operatorname{multiset}(A')=\operatorname{multiset}(A).$$

The second condition includes payload identity and multiplicity. A program that replaces every value by zero satisfies nondecreasing order but is not a sorting algorithm. Equal length, equal sum and even equal minimum/maximum do not establish multiset equality. A correctness proof must explain why moves neither lose nor invent records. Swaps preserve the multiset immediately. A saved-key insertion preserves it across the union of occupied slots and the held record; a hole is not another record.

### Ordering relations

The comparison rule must be consistent. A total preorder permits ties: every pair is comparable, and the nonstrict relation is transitive. A strict weak order defines equivalence by neither record being strictly less than the other; comparisons of equivalent records must behave consistently against other records. If the comparator says $a<b$, $b<c$ and $c<a$, no linear ascending arrangement can satisfy the intended relation. A prerequisite relation in a graph is usually a partial order and belongs to topological sorting, which is a different problem.

Do not implement an integer comparator as `x - y` in a bounded integer type: overflow can reverse the sign. Use direct comparisons. Floating-point NaN requires an explicitly chosen ordering policy because ordinary numeric comparisons do not establish a total order. A key must not change during sorting. These are prerequisites for the proofs, not cosmetic details.

### Stability

A sort is **stable** when equal-key records retain their original relative order. If $i<j$ and $\operatorname{key}(A_i)=\operatorname{key}(A_j)$, then the occurrence originally at $i$ precedes the occurrence originally at $j$ in the output. Stability is not equivalent to the numerical output being sorted. Test it with labeled equal keys, not an integer-only array.

Stability enables composition. To sort by primary key $p$, then secondary key $s$, first sort stably by $s$, then stably by $p$. Different primary keys are put into their primary order; equal-primary records preserve their established secondary order. Reversing this pass order reverses the key priority. Alternatively compare tuples $(p,s)$ directly. Decorating each record with its original index and comparing $(\operatorname{key},\operatorname{index})$ can force a stable result using an otherwise unstable sorter, but decoration and storage costs must be counted.

## 3. Cost models, inversions, and storage

We use zero-based arrays and half-open ranges $[\ell,r)$. Their length is $r-\ell$, the empty range has $\ell=r$, and the last valid slot is $r-1$. Python code accesses keys through a function; illustrative scalar arrays use `key=lambda x: x`. Code examples use unbounded Python integers for arithmetic. The mathematical word-RAM analysis separately assumes that keys, indices and arithmetic operands fit machine words.

The animations distinguish **key comparisons**, **array writes** and **nontrivial swaps**. A swap of two different slots writes two array cells. A saved local variable does not count as an array write. A self-swap is suppressed and costs zero displayed swaps/writes. Loop-index tests and assignments still affect total runtime, but are not key comparisons. Three-way partition counts one ternary comparator invocation per inspected record; implementing it with two Boolean tests can make a different exact count.

An **inversion** is a pair of positions that violates ascending order:

$$I(A)=|\{(i,j):0\le i<j<n,\ A_i>A_j\}|.$$

The inequality is strict. Equal keys contribute no inversion. For distinct reverse order, $I=\binom n2$; in sorted order, $I=0$. Swapping an inverted adjacent pair removes exactly one inversion: that pair changes order, while their relationships with all outside positions are unchanged. Therefore any adjacent-swap algorithm that sorts must perform exactly $I$ inversion-removing swaps, and no adjacent-swap sorter can use fewer than $I$ swaps. A long-distance swap can remove several inversions, so this lower bound must not be transferred to arbitrary swaps.

For uniformly random permutations of distinct keys, each position pair is inverted with probability one half. Linearity of expectation gives:

$$\mathbb E[I]=\frac12\binom n2=\frac{n(n-1)}4.$$

The pair events need not be independent. With repeats, the expectation depends on the sampling model. For a random permutation of a fixed multiset, equal-value pairs never contribute; only unequal-record pairs have inversion probability one half.

<!-- SIM:inversions -->

### Memory distinctions

Report peak auxiliary storage, recursion depth, cumulative allocated storage and output storage separately. A conventional array merge sort uses a linear buffer plus logarithmic stack depth. Allocating a new buffer at every merge can have cumulative allocation $\Theta(n\log n)$ while the maximum simultaneously live storage remains $\Theta(n)$ under sequential recursion and prompt release. Cumulative allocation is not peak space.

We call a method **strictly in-place** when all auxiliary storage, including the call stack, is $O(1)$. Some course summaries allow $O(\log n)$ stack space under that name; this chapter states both quantities. Iterative selection, insertion and heapsort are strictly in-place. Ordinary recursive quicksort has a constant-size partition buffer, but its call stack can be linear in the worst case. Overwriting the input is merely destructive; it does not imply constant auxiliary storage.

## 4. Selection sort: fixed comparisons and few exchanges

At iteration $i$, find the minimum of $A[i:n]$ and move it to $i$. The invariant is stronger than a sorted prefix: the prefix consists of the $i$ smallest records by key in sorted order, and every prefix key is no greater than every suffix key. Initially the prefix is empty. The suffix scan identifies its minimum, swapping puts that minimum immediately after the prefix, and the invariant grows. At termination all slots belong to the final prefix. Every operation is a swap, so permutation preservation is immediate.

```python
def selection_sort(a, key=lambda x: x):
    for i in range(len(a) - 1):
        m = i
        for j in range(i + 1, len(a)):
            if key(a[j]) < key(a[m]):
                m = j
        if m != i:
            a[i], a[m] = a[m], a[i]
```

The suffix scan uses $n-i-1$ key comparisons, regardless of values or initial order:

$$C_{\mathrm{selection}}=\sum_{i=0}^{n-2}(n-i-1)=\frac{n(n-1)}2.$$

Our implementation makes at most $n-1$ nontrivial swaps, or at most $2(n-1)$ array writes. A textbook version that executes a self-swap every iteration reports a different swap count. Selection sort is $\Theta(n^2)$ even on sorted input, uses constant extra storage and is not stable. On $[2_a,2_b,1_c]$, the first swap gives $[1_c,2_b,2_a]$, reversing equal-key identities. Choosing the leftmost minimum does not fix this counterexample.

A stable selection variant removes the selected minimum and shifts all intervening records right by one before inserting it. Stability then follows from preserving the order of the shifted interval, but the number of writes can be quadratic. The ordinary version is useful in a cost model where record writes are exceptionally expensive and quadratic comparisons are affordable; it is not a general fast sorter.

<!-- SIM:selection -->

## 5. Insertion and binary insertion: the role of existing order

Insertion sort maintains a sorted prefix of the original first $i$ records. Hold record $x=A_i$, leave a hole at $i$, move predecessors greater than $x$ one slot to the right, then place $x$ into the hole. During the inner loop, occupied prefix slots and the held key together preserve all original prefix records. Records already shifted right are greater than $x$; records left of the scan position remain sorted. When the loop stops, the preceding key is no greater than $x$ or the hole is at zero. Inserting $x$ establishes the larger sorted prefix.

```python
def insertion_sort(a, key=lambda x: x):
    for i in range(1, len(a)):
        x = a[i]
        j = i
        while j > 0 and key(a[j - 1]) > key(x):
            a[j] = a[j - 1]
            j -= 1
        a[j] = x
```

The strict `>` test makes this version stable: an earlier equal record never crosses the new record. Replacing it with `>=` preserves numerical sortedness but destroys stability and makes an all-equal input quadratic. A short-circuit bounds check must come before the predecessor access.

Each shift removes the conceptual inversion between the held record and the predecessor it crosses. Each strict inversion is removed exactly once when its right-hand record is inserted. Thus the exact number of shifts is $I(A)$ and, for $n\ge1$, this implementation uses:

$$W_{\mathrm{insertion}}=I(A)+(n-1).$$

It writes the held record once per outer iteration, even if no shift occurred. For each insertion, successful key comparisons equal its shifts. There is one additional failed key comparison when the scan stops at a valid predecessor; there is none when the record moves all the way to zero. If $R$ is the number of inserted records that become a new strict prefix minimum, then for distinct keys:

$$C_{\mathrm{insertion}}=I(A)+(n-1)-R.$$

The general form is shifts plus the count of stops at a valid predecessor. Consequently $I\le C\le I+n-1$ and runtime is $\Theta(n+I)$, including loop overhead. On sorted input, comparisons are $n-1$, shifts zero and runtime linear. On reverse distinct input, comparisons and shifts both equal $n(n-1)/2$. On a random distinct permutation, expected shifts are $n(n-1)/4$, while failed tests add only a linear term. Empty input performs no iteration; do not insert $n=0$ into a formula stated for $n\ge1$.

<!-- SIM:insertion -->

### Binary insertion

Search the sorted prefix for the **first key greater than** the new key, using an upper-bound binary search. Place the new record after existing equals, then shift the intervening interval. For a prefix of length $i$, there are $i+1$ possible insertion gaps; binary search uses $O(\log(i+1))$ comparisons. Summing gives $O(n\log n)$ comparisons, but shifting still costs $I$ writes plus insertion writes. Worst-case movement remains quadratic, so comparison efficiency does not imply $O(n\log n)$ runtime in the ordinary array model.

```python
def upper_bound(a, lo, hi, x, key=lambda x: x):
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if key(a[mid]) <= key(x):
            lo = mid + 1
        else:
            hi = mid
    return lo
```

The returned position is the first key strictly greater than $x$, or the exclusive upper boundary if none exists. Using lower bound instead puts the new record before equal predecessors. A linked list avoids contiguous array shifts after locating the predecessor, but does not support constant-time indexed binary search. Representation changes both the search and movement costs.

## 6. Bubble, cocktail, and Shell sorting

In a left-to-right bubble pass over the active prefix, adjacent inverted pairs are exchanged. At the end, its maximum reaches the last active slot. This final suffix grows one slot per pass. Strict comparisons preserve equal-key order, so ordinary bubble sort is stable and strictly in-place. Its total nontrivial swaps equal $I(A)$. Without an early-stop flag, shrinking passes make exactly $n(n-1)/2$ comparisons on every input. With a flag, a pass containing no exchange proves the whole active prefix is sorted and permits termination.

```python
def bubble_sort(a, key=lambda x: x):
    for end in range(len(a) - 1, 0, -1):
        changed = False
        for j in range(end):
            if key(a[j]) > key(a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                changed = True
        if not changed:
            break
```

Early stopping yields linear best-case time and quadratic worst-case time. Few inversions do not guarantee this particular bubble implementation is linear: on $[2,3,\ldots,n,1]$, the smallest record can move left only one slot per pass, so $I=n-1$ but comparisons remain quadratic. The reverse pattern $[n,1,2,\ldots,n-1]$ moves the large first record right across the array in one pass. Pass direction matters. Cocktail sorting alternates directions, moving a small delayed record left during the reverse pass; it remains an adjacent-swap method with quadratic worst-case bounds.

<!-- SIM:bubble -->

### Shell sorting and gap-dependent claims

A gap-$h$ insertion pass sorts each residue-class subsequence $A_r,A_{r+h},A_{r+2h},\ldots$. After the pass the array is **$h$-sorted**: $A_i\le A_{i+h}$ whenever both slots exist. Apply decreasing positive gaps ending in one. The final gap-one pass is ordinary insertion on the entire array, proving final sortedness. All moves preserve records. A gap pass can move equal keys past each other in different residue classes, so standard Shell sort is not stable.

Complexity depends on the complete gap sequence, not just its largest gap. The halving sequence has quadratic worst cases; other sequences have different provable bounds and constants. It is incorrect to write “Shell sort is $\Theta(n\log n)$” without assumptions. A single gap-one sequence is insertion sort. Adding gap passes is extra work and can improve the final pass by removing long-distance disorder, but not by magic.

For $n=qh+r$ with $0\le r<h$, $r$ residue classes have length $q+1$ and $h-r$ have length $q$. The maximum comparisons of a straightforward reverse-distinct insertion pass are:

$$r\binom{q+1}{2}+(h-r)\binom q2.$$

This is a bound for that pass; maxima for successive passes may not be simultaneously attainable. Adding independent worst-pass maxima gives a valid upper bound, not necessarily a tight worst-case total. The laboratory identifies the exact gap sequence rather than labeling every gap sorter as one implementation.

<!-- SIM:shell -->

## 7. Stable merging and exact merge-sort counts

Merging is not sorting two arbitrary arrays. Its precondition is that both input runs are already sorted. Keep a head pointer in each run and emit the smaller head. The output invariant says that the output is a sorted prefix of the merged multiset; it contains exactly the consumed records, and its final key is no greater than either unconsumed head. Equality chooses the left run to preserve the original order across a contiguous split.

```python
def merge(left, right, key=lambda x: x):
    i = j = 0
    out = []
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out
```

When one run becomes empty, append the other tail without comparing keys. For nonempty run lengths $p,q$, the comparison count satisfies:

$$\min(p,q)\le C_{\mathrm{merge}}\le p+q-1.$$

For the lower extreme, all records of the shorter run precede all records of the longer run. For the upper extreme, both runs remain nonempty until the penultimate output record; the two globally largest records lie in different runs. Empty versus nonempty merging uses zero key comparisons and still copies the records, demonstrating why runtime and comparison count differ. If a question uses sentinels and compares on every output iteration, its exact count changes; prove that the sentinel exceeds all legal keys and is never mistaken for a payload.

### Top-down merge sort

Split $[\ell,r)$ at $m=\ell+\lfloor(r-\ell)/2\rfloor$. Recursively sort both strictly smaller ranges and merge them. Strong induction gives sorted child permutations; the merge proof then gives a sorted permutation of the original range. Stability follows because equal records retain order inside each child and ties from the left child precede equal records from the right child. A base case of length at most one includes empty input.

At each merge-tree level the total number of emitted records is at most $n$, and there are $\lceil\log_2n\rceil$ levels. The conventional implementation has $\Theta(n\log n)$ runtime and $\Theta(n)$ peak buffer storage. Its number of key comparisons can vary with the input while its linear copies per level persist.

For $n=2^k$, the worst-case front-merge comparison recurrence is:

$$M(1)=0,\qquad M(n)=2M(n/2)+n-1.$$

Expanding by levels sums $n-2^j$ for $j=0,\ldots,k-1$, giving:

$$M(n)=n\log_2n-n+1.$$

The best-case recurrence uses $n/2$ comparisons at each merge:

$$B(n)=2B(n/2)+n/2,\qquad B(1)=0.$$

Hence $B(n)=(n/2)\log_2n$. An already sorted input attains that count in the unoptimized front-merge version because every left child empties first. It does not make the conventional copying algorithm linear. For the exact archive input $[12,7,5,9,3,8,2,6]$, the four size-two merges cost four, the two size-four merges cost six, and the final merge costs six: total sixteen, not the worst-case seventeen.

For arbitrary positive $n$, floor/ceiling splits give an attainable worst-case count:

$$M(n)=n\lceil\log_2n\rceil-2^{\lceil\log_2n\rceil}+1.$$

One proof uses the balanced split tree's leaf depths. With $h=\lceil\log_2n\rceil$, there are $2^h-n$ leaves at depth $h-1$ and $2n-2^h$ at depth $h$. The sum of leaf depths is $nh-(2^h-n)$. Each internal merge contributes subtree leaf count minus one; summing leaf counts gives the sum of depths, and the $n-1$ internal nodes contribute the subtracted ones. Subtracting yields $nh-2^h+1$. Interleaving child ranks recursively constructs worst-case inputs, establishing attainability rather than only an upper bound. For $n=0$, define comparisons separately as zero.

<!-- SIM:merge -->

## 8. Merge variants, inversions, and adaptive inputs

### Boundary skip and bottom-up merging

After sorting both children, if the greatest left key is no greater than the smallest right key, the combined range is already sorted. A single boundary comparison can skip the merge. On a globally sorted array, every internal node succeeds, so there are exactly $n-1$ boundary comparisons, no merge comparisons and no copying in a shared-buffer range implementation. This is linear runtime. If each recursive call first copies/slices its children, that copying can still cause $\Theta(n\log n)$ work; optimizing comparisons is not enough.

Bottom-up merge sort first merges adjacent runs of length one, then two, four and so on. At width $w$, merge $[\ell,\min(\ell+w,n))$ with $[\min(\ell+w,n),\min(\ell+2w,n))$. The invariant says every complete run of the current width is sorted before the next pass. It needs no recursion and still uses a linear array buffer. A final short run is legal. With a linked list, merges relink nodes rather than shift array slots; iterative bottom-up list merging can sort with constant auxiliary pointers when run lengths and node ownership are tracked correctly.

### Counting strict inversions during a merge

If the right head is strictly less than the left head, it is less than every unconsumed left record, because the left run is sorted. Add the number of remaining left records to the cross-inversion total, emit the right head, and continue. On equality, emit left and add zero. Recursive inversion counts satisfy:

$$I(A)=I(L)+I(R)+I_{\mathrm{cross}}(L,R).$$

All inversion pairs fall into exactly one of those disjoint categories. This counts them in $\Theta(n\log n)$ time rather than examining all pairs. For $L=[1,3,3]$ and $R=[2,3,4]$, only the two left threes versus the right two contribute: the cross count is two. Equal threes do not contribute. To count nonstrict pairs instead, both the definition and tie treatment must change together.

### Runs and local disorder

A natural merge sorter detects already sorted contiguous runs and merges them according to a specified merge schedule. If $r$ runs have comparable lengths and are combined in a balanced schedule, the merge work is $O(n\log r)$ after $O(n)$ detection. Arbitrary unbalanced sequential merging can instead become quadratic, even when every initial run is sorted. The merge schedule is part of the algorithm.

To exploit a strictly decreasing run stably, reverse it. Reversing a weakly decreasing run that contains equals reverses equal-record identity order and is not stable. Run detection and reversal must use compatible strictness. Hybrid run algorithms also need precise stack or merge-size invariants; “uses runs” alone does not prove a runtime bound.

If each distinct record is displaced by at most $k$ positions from its final place, a min-heap containing the next $k+1$ records can emit the next minimum, giving $O(n\log(k+1))$ time and $O(k+1)$ extra storage. For $k=0$ it is already sorted. Insertion can give $O(n(k+1))$ under that displacement restriction. A statement that an array is “almost sorted” is incomplete until a quantity such as inversions, displacement or number of runs is specified.

## 9. Quicksort contracts: partition schemes are different algorithms

Quicksort performs its linear work before recursion. Choose a pivot, partition records by their relation to it, then recursively sort the remaining ranges. Partition does not sort the ranges internally. The correctness proof needs range inequalities, record preservation and strictly smaller recursive arguments. Equal keys make partition details especially important.

### Lomuto with a final pivot

This version partitions $[\ell,r)$ using $p=A_{r-1}$ and the strict `<` test. During the scan at $j$, $A[\ell:b]$ is below $p$, $A[b:j]$ is at least $p$, $A[j:r-1]$ is unexamined, and the pivot remains at $r-1$.

```python
def lomuto(a, lo, hi, key=lambda x: x):
    pivot = a[hi - 1]
    b = lo
    for j in range(lo, hi - 1):
        if key(a[j]) < key(pivot):
            a[b], a[j] = a[j], a[b]
            b += 1
    a[b], a[hi - 1] = a[hi - 1], a[b]
    return b

def quicksort_lomuto(a, lo=0, hi=None, key=lambda x: x):
    if hi is None:
        hi = len(a)
    if hi - lo <= 1:
        return
    p = lomuto(a, lo, hi, key)
    quicksort_lomuto(a, lo, p, key)
    quicksort_lomuto(a, p + 1, hi, key)
```

The returned slot contains the pivot in a valid final sorted position. The children exclude it and have lengths summing to parent length minus one. Each partition uses exactly $m-1$ key comparisons for range length $m$. An increasing input with last pivots repeatedly produces lengths $m-1$ and zero, giving $n(n-1)/2$ total comparisons. An all-equal input with strict `<` repeatedly returns the first slot and also produces quadratic work. Uniform pivot choice does not fix that equal-key degeneration in this two-way version.

<!-- SIM:quick -->

### Classic Hoare partition

Choose a saved pivot value, scan inward from both ends, stopping the left scan at a key at least the pivot and the right scan at a key at most the pivot. Swap out-of-place endpoints until the indices cross. A classic implementation returns a **split boundary**, not necessarily a pivot slot. For inclusive bounds its recursion is on $[\ell,j]$ and $[j+1,h]$. For a half-open wrapper it is on $[\ell,j+1)$ and $[j+1,r)$. Recursing as though $j$ held a finalized pivot can leave an unsorted record or fail to shrink.

```python
def hoare_split(a, lo, hi, key=lambda x: x):
    pivot = key(a[lo])          # requires hi - lo >= 2
    i, j = lo - 1, hi
    while True:
        i += 1
        while key(a[i]) < pivot:
            i += 1
        j -= 1
        while key(a[j]) > pivot:
            j -= 1
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]
```

The pivot value supplies scan stopping witnesses, and the outer iteration advances both indices after each exchange. Stopping on equals avoids a scan that runs past every equal key. On all-equal inputs this scheme divides into roughly equal parts and uses $\Theta(n\log n)$ sorting work, rather than the quadratic strict-Lomuto chain. This is still slower asymptotically than removing an entire equal block in one three-way partition. A Sedgewick scan variant additionally swaps a saved first pivot into its final slot and returns that slot; its contract differs from classic Hoare even though both scan inward.

### CMU's scan variant

The CMU note moves its pivot to the first slot, scans `left` from the next slot, and keeps an exclusive `right` boundary. Values at most the pivot advance `left`; larger values are exchanged with `right - 1`, after which only `right` decreases. Finally the pivot swaps to `left - 1`. It returns a pivot slot, but its intermediate order differs from both Lomuto and classic Hoare. The chapter includes a faithful CMU trace for the deterministic-middle-pivot counterexample. Do not predict its later pivots using Lomuto's intermediate arrays.

<!-- SIM:cmu -->

## 10. Quicksort time, randomization, and stack depth

For a pivot with $q$ smaller distinct keys, the exact ideal comparison recurrence is:

$$C(n)=C(q)+C(n-1-q)+(n-1).$$

A fixed fraction split bounded away from zero and one gives $\Theta(n\log n)$ runtime: every branch has logarithmic depth, and total work per level is at most linear. One-sided splits give quadratic work. The best balanced recurrence uses children of size about $(n-1)/2$, not $n/2$ with no pivot removed. Precise counts for small arrays require the actual integer child lengths.

### Randomized expectation: a complete derivation

Assume distinct keys, a uniformly random pivot in every recursive range, and one comparison between each nonpivot record and the pivot. Let sorted ranks be $1,\ldots,n$, and let $X_{ij}$ indicate whether ranks $i<j$ are compared. A pair is compared at most once: one member must be a pivot, and that member then leaves recursion. The pair stays together until the first pivot from the rank interval $i,\ldots,j$ is chosen. They are compared exactly when this first pivot is an endpoint. Uniform pivot priorities make every rank in that interval equally likely to be first, hence:

$$\Pr(X_{ij}=1)=\frac{2}{j-i+1}.$$

No independence between different pair indicators is needed. Their sum is the total comparison count. Grouping by interval length $d=j-i+1$ gives:

$$\mathbb E[C_n]=\sum_{i=1}^{n-1}\sum_{j=i+1}^{n}\frac{2}{j-i+1}=2\sum_{d=2}^{n}\frac{n-d+1}{d}.$$

With harmonic numbers $H_n=\sum_{d=1}^n1/d$, simplify:

$$\mathbb E[C_n]=2(n+1)H_n-4n=\Theta(n\log n).$$

For $n=3$, this is $8/3$: choosing the middle rank gives two comparisons, while either extreme gives three. For large $n$, the leading term is $2n\ln n$, approximately $1.386n\log_2n$. This exact harmonic expression does not include Hoare scan-crossing tests or extra pivot-selection comparisons. Those can preserve the asymptotic bound while changing exact constants.

The expectation is over algorithmic randomness for each fixed distinct-key input, not an assumption that the user provides randomly ordered input. A one-time uniform shuffle followed by an appropriate deterministic pivot rule can reproduce a random pivot-priority order, but arbitrary biased shuffling does not establish this guarantee. Expected $\Theta(n\log n)$ does not exclude a quadratic execution or promise a deadline.

The argument “expected left length equals $(n-1)/2$, so substitute that size into the recurrence” is invalid. An algorithm choosing either the global minimum or maximum with equal probability has the same balanced expected child lengths, but every execution has a one-sided split and quadratic work. In general $\mathbb E[T(X)]$ is not $T(\mathbb E[X])$.

### Bounding the actual call stack

Ordinary recursive quicksort can have $\Theta(n)$ stack depth in a one-sided execution. Merely calling the smaller child first does not guarantee logarithmic depth if the larger child is also invoked recursively before the current call returns. The necessary transformation is to recurse only on the smaller child and **iterate** on the larger child in the current activation.

The recursively entered child has size at most $(m-1)/2$. Along every simultaneously active recursion chain, sizes therefore halve. The stack is $O(\log n)$ in every execution, even if runtime remains quadratic. For Lomuto's half-open ranges, after partition at $p$, choose between lengths $p-\ell$ and $r-p-1$; recurse on the smaller and update the loop bounds to the larger. This separates a storage guarantee from a time guarantee.

<!-- SIM:quick-worst -->

## 11. Duplicate keys, three-way partition, and pivot sampling

Three-way partition maintains four regions: keys below the saved pivot, keys equal to it, unknown keys, and keys above it. Use half-open boundaries $\ell\le lt\le i\le gt\le r$:

$$A[\ell:lt]<p,\quad A[lt:i]=p,\quad A[i:gt]\text{ is unknown},\quad A[gt:r]>p.$$

The initial pivot record supplies the first equal record; set $lt=\ell$, $i=\ell+1$, $gt=r$. If an inspected key is below $p$, exchange it with $A_{lt}$ and advance both $lt$ and $i$. The displaced equal key goes to the end of the equal block, so both invariants persist. If it is equal, advance $i$. If it is above, decrement $gt$ and exchange with that slot, without advancing $i$: the imported record was unexamined and must be classified next. In every iteration $gt-i$ decreases by one, proving termination.

```python
def three_way(a, lo, hi, key=lambda x: x):
    pivot = key(a[lo])
    lt, i, gt = lo, lo + 1, hi
    while i < gt:
        v = key(a[i])
        cmp = (v > pivot) - (v < pivot)
        if cmp < 0:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1
        elif cmp > 0:
            gt -= 1
            a[i], a[gt] = a[gt], a[i]
        else:
            i += 1
    return lt, gt
```

This code defines the logical ternary comparison; the two primitive Boolean comparisons in `cmp` should be counted separately if that is the requested cost model. Recursion sorts only $[\ell,lt)$ and $[gt,r)$; the whole equal interval is complete. On an all-equal range, the model performs $n-1$ ternary comparator calls, no exchanges and no nontrivial recursive children. On a range with $r$ distinct values, any root-to-leaf path removes a distinct pivot value at each partition, so there are at most $r$ partition levels. Each level processes at most $n$ records, giving a deterministic upper bound $O(nr)$. For constant $r$, the work is linear. For $r=n$, this bound permits quadratic work.

Standard swapping three-way quicksort is not stable: equal records can be displaced by swaps involving other values. Removing an equal block makes it efficient on duplicates but does not preserve identity order inside that block. A stable partition using three append-only output sequences is possible, at the cost of auxiliary storage and extra movement.

<!-- SIM:three -->

### A frequent value versus few distinct values

“Ninety-nine percent of the array has one key” does not imply that a comparison sort has linear worst-case work. The remaining one percent can contain a linear number of distinct keys. Restricting the input to those positions gives an embedded arbitrary sorting problem of size $n/100$, whose comparison lower bound is still $\Omega(n\log n)$ asymptotically. In contrast, an array containing only a fixed number of distinct keys is a genuinely different restriction. State which parameter is fixed as $n$ grows.

### What a pivot sample guarantees

Taking the median of a fixed sample of three does not guarantee a balanced fraction of the whole array. It guarantees only one sample record below and one above the pivot when keys are distinct. An adversarial arrangement can put every other record on the same side. A randomized sample can improve expected balance but does not create a deterministic worst-case guarantee by itself.

For a distinct sample of $2s+1$ records, its median guarantees at least $s$ sample records on each side. Therefore the child lengths are between $s$ and $n-s-1$; the rest of the input can concentrate on one side. If $s=\Theta(\sqrt n)$ and the sample is sorted by insertion, sample work is $\Theta(n)$ in its worst case and partition work is linear. The unbalanced worst recurrence is approximately:

$$T(n)=T(n-\sqrt n)+T(\sqrt n)+\Theta(n).$$

This is not a balanced Master-Theorem recurrence. Along the large-child chain, the square root of the size decreases by a constant order per step, giving $\Theta(\sqrt n)$ large-chain levels. Summing their linear tolls gives $\Theta(n^{3/2})$. A rigorous upper induction can substitute $c n^{3/2}$: the decrease $n^{3/2}-(n-\sqrt n)^{3/2}$ is $\Theta(n)$, while the small-child term is $n^{3/4}=o(n)$. Choose a sufficiently large constant to absorb the toll; a lower bound follows by summing the first constant fraction of the large chain, where every size remains $\Theta(n)$. The archive question asks for the recurrence, so do not confuse deriving it with solving it.

Selecting the exact median in deterministic linear time gives balanced quicksort with $O(n\log n)$ worst-case work. Selection itself will be developed in the next scheduled chapter. Introsort instead monitors recursion depth and falls back to heapsort when its depth budget is exceeded, yielding a worst-case bound without computing an exact median every time.

## 12. Heapsort: shape, heap order, and Floyd construction

A binary max-heap is an array interpreted as a **complete** binary tree whose parent key is at least each child's key. With zero-based indexing, the children of $i$ are $2i+1$ and $2i+2$, when those indices are below the active heap length. The parent of $i>0$ is $\lfloor(i-1)/2\rfloor$. Heap order is not full sortedness: siblings and nodes in different subtrees can be in either order.

To restore heap order at a node whose child subtrees are already heaps, select the larger child. If the parent is no smaller, stop. Otherwise exchange them and continue down that child's subtree. Only that lower subtree can now violate heap order. The path has logarithmic length. With two children, a straightforward level uses one comparison to choose the larger child and one to compare it against the parent; a sole child needs only the latter comparison. These counts explain why “one comparison per level” is generally wrong.

```python
def sink(a, i, end, key=lambda x: x):
    while 2 * i + 1 < end:
        j = 2 * i + 1
        if j + 1 < end and key(a[j]) < key(a[j + 1]):
            j += 1
        if key(a[i]) >= key(a[j]):
            break
        a[i], a[j] = a[j], a[i]
        i = j

def heapsort(a, key=lambda x: x):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        sink(a, i, n, key)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sink(a, 0, end, key)
```

### Why bottom-up construction is linear

All leaves are already heaps. Process internal nodes in decreasing index order, so their child subtrees satisfy the heap property before each sink. This inductively establishes the whole heap. Bounding every sink by the root height gives $O(n\log n)$ but is unnecessarily loose: most nodes lie near the leaves and can move only a short distance.

For a complete heap with $n$ nodes, the number of nodes of height at least $h$ is $\lfloor n/2^h\rfloor$. Summing those counts gives the sum of all node heights:

$$\sum_{v}\operatorname{height}(v)=\sum_{h\ge1}\lfloor n/2^h\rfloor<n.$$

Each sink uses at most two comparisons per available descent level; total construction comparisons are below $2n$, and total exchanges are below $n$. Since reading/processsing the input is linear, construction time is $\Theta(n)$. Repeated individual heap insertion instead follows upward paths and can require $\Theta(n\log n)$ construction on increasing keys. The two methods build a valid heap but need not build the same array arrangement.

### Sortdown and proof

The root is a maximum of the active heap. Swap it into its last active slot, shrink the heap, and sink the replacement root. The invariant states that the active prefix is a max-heap, the suffix is sorted in ascending order, and every active key is no greater than every suffix key. Each maximum extends the final suffix leftward; when one heap record remains the whole array is sorted. Swaps preserve identities, but their long-distance movement can reverse equals, so heapsort is not stable.

The sum of logarithmic sink bounds is $O(n\log n)$; there are inputs attaining $\Omega(n\log n)$ comparisons, so worst-case time is $\Theta(n\log n)$. Do not infer that every input has this same count: this early-exit sink version on all-equal keys stops at once, making the complete execution linear in comparisons and moves. Iterative heapsort is strictly in-place. The tree animation keeps the active tree synchronized with its zero-based array and final suffix; lines end on node boundaries.

<!-- SIM:heap -->

## 13. Comparison lower bounds and their quantifiers

Consider $n$ distinct labeled keys whose relative order is initially unknown. A deterministic comparison algorithm learns about them only from binary ordering outcomes. Its execution can be represented by a decision tree. Each root-to-leaf path records the outcomes for one input order, and the leaf tells the algorithm which input-index permutation puts that order into ascending order. All $n!$ relative orders require distinguishable leaves: a single prescribed permutation cannot correctly sort two different relative orders.

A binary tree of height $h$ has at most $2^h$ leaves. Therefore:

$$2^h\ge n!,\qquad h\ge\lceil\log_2(n!)\rceil.$$

For even $n$, the largest $n/2$ factors of $n!$ are at least $n/2$, so $n!\ge(n/2)^{n/2}$. Taking logarithms establishes $\Omega(n\log n)$ without requiring Stirling's approximation. A more precise asymptotic expression is:

$$\log_2(n!)=n\log_2n-(\log_2e)n+O(\log n).$$

The claim is: **every correct comparison sorter has some size-$n$ input requiring asymptotically at least $n\log n$ comparisons.** It is not a statement that every input costs that much, that every sorter is upper-bounded by it, or that non-comparison sorting cannot be linear. The integer leaf-count lower bound is not always attainable by a legal sorting decision tree for a particular small $n$; some binary questions do not correspond to valid pair comparisons.

For a uniform distribution over distinct input permutations, average path length is also at least $\log_2(n!)$, by the prefix-code/Kraft inequality or entropy bound. Fixing random coins gives a deterministic correct tree; averaging over uniform inputs and then over the coins preserves that bound. Thus some fixed input has expected $\Omega(n\log n)$ comparisons for a randomized sorter that is always correct. This is a statement about an input distribution used in the proof, not an assumption required by randomized quicksort's per-input upper bound.

### Restricted information can reduce the bound

For known duplicate multiplicities $m_1,\ldots,m_r$, there are:

$$N=\frac{n!}{\prod_{i=1}^r m_i!}$$

distinct key arrangements. A binary-comparison leaf bound is $\lceil\log_2N\rceil$ for that restricted problem. If the comparison primitive is a three-outcome oracle, the direct branching bound uses $\log_3N$; both give the same relevant order when $N$ is large. Distinct inputs still reduce a three-way comparator to two feasible ordering outcomes. When all keys are equal, $N=1$, so this information bound is zero; input inspection, validation and output construction can still require linear work depending on the task promise.

If two internally sorted runs of lengths $p,q$ must be merged, the number of possible interleavings is $\binom{p+q}{p}$. Therefore comparison merging has an information lower bound $\lceil\log_2\binom{p+q}{p}\rceil$. Ordinary head merging uses at most $p+q-1$ comparisons, but it is not comparison-optimal for every highly unequal pair of run lengths. Inserting a one-element run into a large sorted run can locate its gap by binary search; movement/output costs remain separate.

A known sorted prefix of length $n-k$ followed by arbitrary $k$ records can be handled by sorting that tail and merging in $O(n+k\log k)$ time. Sorting all records again ignores the promise. Having only a fixed number of key values, few inversions, few runs, and a small integer universe are different promises and permit different algorithms.

<!-- SIM:lower-bound -->

## 14. Counting sort: integer reconstruction versus stable records

Assume integer keys in a known interval $[L,H]$, and let $K=H-L+1$. Shift a key $x$ to index $x-L$, which lies in $[0,K)$. Scanning the records and incrementing one counter per key gives a frequency array. Initializing all counters takes $\Theta(K)$, and scanning takes $\Theta(n)$. Reconstructing each integer value as many times as its counter says takes $\Theta(n+K)$ overall because the total of the counters is $n$.

That counts-only reconstruction is sufficient for plain integer values. For records, it would discard payloads and cannot claim identity preservation or stability. A stable record version uses cumulative counts:

$$F_j=|\{x:\operatorname{key}(x)-L=j\}|,\qquad P_j=\sum_{t=0}^jF_t.$$

The equal-key block $j$ occupies indices $[P_{j-1},P_j)$, defining $P_{-1}=0$. Each $P_j$ is the exclusive end. Scan the original records right to left, decrement their block's end pointer, and place the record at that resulting slot. The later equal record is encountered first and takes the rightmost available equal slot, so earlier equals end farther left. This proves stability and uniqueness of output positions.

```python
def stable_counting(a, low, high, key=lambda x: x):
    k = high - low + 1
    if k <= 0:
        raise ValueError("The key interval must be nonempty")
    counts = [0] * k
    for x in a:
        j = key(x) - low
        if not 0 <= j < k:
            raise ValueError("Key outside the stated interval")
        counts[j] += 1
    for j in range(1, k):
        counts[j] += counts[j - 1]
    out = [None] * len(a)
    for x in reversed(a):
        j = key(x) - low
        counts[j] -= 1
        out[counts[j]] = x
    return out
```

The reverse input traversal must read the original records; do not overwrite unprocessed input positions using the same array without a safe source copy. A left-to-right traversal is also stable if it uses **starting** positions and increments them. Combining left-to-right traversal with decrementing cumulative ends reverses every equal-key group. These are two correct directional conventions and one common incorrect mixture.

Runtime is $\Theta(n+K)$ and auxiliary storage is $\Theta(n+K)$ for this output-array version. It is linear in $n$ only if $K=O(n)$. A small number of occupied keys does not make a huge dense universe cheap: all $K$ counters must still be initialized/scanned. Sparse maps need an ordered traversal of their occupied keys, which itself has a cost. Counting sort bypasses the comparison lower bound because it reads numeric key values and uses them as indices; it does not obtain all information through pair comparisons.

<!-- SIM:counting -->

## 15. Radix sorting: an invariant across stable digit passes

For nonnegative integer keys below an exclusive universe bound $U$, choose integer base $B\ge2$. Express each key in equal-width base-$B$ digits, padding high positions with zeros. After $t$ least-significant-digit passes, the array is stably sorted by the suffix consisting of its $t$ lowest digits. The next stable digit pass puts smaller next digits first. Among records with equal next digits, stability preserves their previously ordered lower-digit suffix. Together these facts prove the suffix invariant for $t+1$. After enough digits cover the full key, numerical order follows.

An unstable digit sorter invalidates the proof. For example, after the units pass on $[12,11]$, the order is $[11,12]$; an unstable tens pass can reverse those equal tens to $[12,11]$, leaving an unsorted output. Sorting most-significant first and then globally sorting less-significant digits is also generally incorrect: a later digit pass can mix records from different high-digit blocks. MSD sorting instead recurses **within** each high-digit block.

For $U\ge2$, the required number of digits is the smallest integer $d$ with $B^d\ge U$, or $d=\lceil\log_BU\rceil$. For an inclusive maximum $M\ge1$, it is $\lfloor\log_BM\rfloor+1$. These are equivalent with $U=M+1$; confusing inclusive and exclusive bounds produces an error at exact powers. For an all-zero nonempty input one may perform one zero-digit pass by convention, or return immediately. Empty input should return before computing its maximum. When choosing $B=n$, handle $n<2$ separately.

Floating-point logarithms can round near a power boundary. An exact implementation uses repeated integer division or multiplies the place value while it is no larger than the maximum. This chapter does not use an approximate bit-length quotient as an exact base-$B$ digit count. A base-three key requiring ten digits can be undercounted by that shortcut.

```python
def radix_sort(a, base=10):
    if base < 2:
        raise ValueError("Base must be at least two")
    if not a:
        return []
    low = min(a)
    out = list(a)
    maximum = max(a) - low
    place = 1
    while True:
        buckets = [[] for _ in range(base)]
        for x in out:
            buckets[((x - low) // place) % base].append(x)
        out = [x for bucket in buckets for x in bucket]
        if maximum // place < base:
            return out
        place *= base
```

Shifting by the minimum is monotone, so it also supports negative integer values without reversing their mathematical order. Records should retain payloads while the digit is computed from a shifted key. Under bounded-width two's-complement keys, toggling the sign bit converts signed numeric order to unsigned bit-pattern order; this requires the exact word width and representation assumption. Naively treating signed bit patterns as unsigned puts nonnegative keys before negative keys, contrary to signed order.

<!-- SIM:radix -->

### Time, base and bit complexity

A dense stable counting pass uses $\Theta(n+B)$ time and $\Theta(n+B)$ peak auxiliary storage. Reusing the buffer across $d$ passes gives:

$$T_{\mathrm{radix}}=\Theta(d(n+B)).$$

For $U\le n^c$, fixed positive $c$ and $n\ge2$, choosing $B=n$ gives a constant number of passes and linear word-RAM time. Choosing constant base ten instead requires $\Theta(\log n)$ passes on a polynomial universe, so the time can be $\Theta(n\log n)$. The number of digits is a parameter, not automatically a constant. A larger base reduces digits but increases the count array; memory constraints may forbid it.

For a $w$-bit key and digit width $b$, $B=2^b$ and $d=\lceil w/b\rceil$. The cost is $\Theta(\lceil w/b\rceil(n+2^b))$. Powers of two permit extracting a digit using shifts and a mask. This is constant-time only when the relevant words and operations are constant-cost in the chosen machine model. With arbitrary-precision integers, reading, shifting or comparing all bits can require more work. “Linear in records” is not the same as “linear in encoded input bits.”

## 16. Bucket distributions and string ordering

### Distribution bucket sort

For independent uniform keys in $[0,1)$, divide the interval into $n$ equal subintervals and append each key to its bucket. Sort each bucket, often using insertion, then concatenate buckets in order. Keys in earlier buckets are less than keys in later buckets; within-bucket sorting establishes the remaining order. Distribution into a bucket is not itself a proof of internal sorting.

Let $N_i$ be a bucket's size. Insertion work inside it is $O(N_i^2)$, and total work is $O(n+\sum_iN_i^2)$. With independent uniform placement, $N_i$ is binomial with probability $1/n$:

$$\mathbb E[N_i]=1,\quad \operatorname{Var}(N_i)=1-1/n,\quad \mathbb E[N_i^2]=2-1/n.$$

Summing gives $\mathbb E[\sum_iN_i^2]=2n-1$, so expected runtime is $O(n)$. Initialization/distribution requires $\Omega(n)$, giving expected $\Theta(n)$. If all keys land in one bucket and arrive in reverse order, insertion work is quadratic; no worst-case linear claim is justified. For bucket probabilities $p_i$ and independent placements:

$$\mathbb E\left[\sum_iN_i^2\right]=n+n(n-1)\sum_i p_i^2.$$

Uniformity is sufficient, not logically necessary: near-balanced probabilities can also make this expression linear. Dependence between input placements can break the binomial argument even if individual marginal probabilities look uniform. To make the complete sort stable, append in input order and use a stable within-bucket sorter. The laboratory uses integer percentages from zero through ninety-nine and five intervals; that deterministic classroom trace illustrates mechanics, not evidence for the uniform expected-time theorem.

<!-- SIM:bucket -->

### LSD and MSD strings

For $n$ strings of equal length $L$ over an ordered alphabet of size $R$, stable LSD character sorting from right to left costs $\Theta(L(n+R))$ with dense counting passes. If $R$ is constant, this is linear in the total $nL$ characters. It is not $O(n)$ independent of string length. A whole-string comparison can itself inspect many characters; an $O(n\log n)$ count of comparisons can mean $O(Ln\log n)$ character work.

For variable-length lexicographic order, a string precedes every longer string of which it is a proper prefix. A character accessor in MSD sorting therefore uses an end-of-string sentinel ordered below every ordinary character. Do not use an ordinary alphabet character as that sentinel. After distributing by the current character, recursively sort each nonterminal bucket by the next character. Strings already ended require no recursion. Common prefixes create deep recursive paths, so character work and maximum string length remain relevant.

Naively left-padding variable-length strings and using an ordinary numeric-style LSD sorter does not produce dictionary order. Either use a rigorously defined sentinel/padding convention compatible with the target order, or use MSD/trie-like refinement. Locale-sensitive human alphabetical order is a different comparator from raw Unicode code-unit order; specify which ordering the algorithm must implement.

## 17. Hybrids, external sorting, and choosing a method

### Cutoffs and introspection

Using insertion on subproblems of at most a fixed cutoff $k$ can reduce overhead. Across all such disjoint subproblems, insertion work is at most $O(nk)$; with fixed $k$, this is linear and does not change a merge/quick algorithm's main asymptotic bound. If $k$ grows with $n$, it is no longer a constant hidden in the analysis.

An introspective sorter starts with quicksort and assigns a depth budget proportional to $\log n$. When a range exhausts that budget, sort it with heapsort. Above the cutoff depth, at most logarithmically many partition levels each process at most $n$ records, so their total work is $O(n\log n)$. Fallback ranges are disjoint; summing $m_i\log m_i$ over them is at most $n\log n$. Thus the combined worst-case work is $O(n\log n)$. Insertion cutoffs add only $O(n)$ when fixed. Stable behavior is not supplied by this ordinary swapping hybrid.

### External merging

When records do not fit in RAM, disk block transfers can dominate key-comparison cost. Let $M$ records fit in memory and a disk block hold $B$ records. Generate sorted runs of about $M$ records; their number is $r=\lceil n/M\rceil$. A multiway merge uses one input buffer per active run plus an output buffer, so a conservative fan-in is $f=\lfloor M/B\rfloor-1$, assuming sufficient space for its metadata. At each merge pass, read and write every record, about $2\lceil n/B\rceil$ block transfers. Approximately $\lceil\log_f r\rceil$ merge passes suffice when $f\ge2$. Run generation adds its own reading/writing pass.

With a heap holding each run's current head, CPU merging work is $O(n\log f)$ per pass, while buffer space and I/O costs are different quantities. A tie-break by original run order and within-run stability preserves global stability for runs formed from consecutive original ranges. A two-way merge schedule can be correct but incur more passes than a feasible multiway schedule.

### Comparison table

The entries describe the implementations taught here, under constant-cost key access. A plus sign in a storage entry separates the element buffer from the call stack.

| Method | Best or adaptive behavior | Worst time | Auxiliary storage | Stable? |
| --- | --- | --- | --- | --- |
| Selection with swaps | Fixed quadratic comparisons; at most linear exchanges | $\Theta(n^2)$ | $O(1)$ | No |
| Saved-key insertion | $\Theta(n+I)$ | $\Theta(n^2)$ | $O(1)$ | Yes, strict predecessor test |
| Binary insertion | $O(n\log n)$ comparisons; movement still depends on $I$ | $\Theta(n^2)$ movement | $O(1)$ | Yes, upper-bound insertion |
| Bubble with early exit | Linear on sorted data; few inversions alone are insufficient | $\Theta(n^2)$ | $O(1)$ | Yes, strict swaps |
| Shell with stated gaps | Depends on gaps and input | Gap-dependent; halving can be quadratic | $O(1)$ | Generally no |
| Conventional array merge | $\Theta(n\log n)$ copying, input-dependent comparisons | $\Theta(n\log n)$ | $O(n)+O(\log n)$ | Yes, left tie first |
| Merge with boundary skip | Linear on sorted ranges if copying is also skipped | $\Theta(n\log n)$ | $O(n)+O(\log n)$ | Yes |
| Random-pivot quick, distinct keys | Expected $\Theta(n\log n)$ per fixed input | $\Theta(n^2)$ | $O(1)$ buffer; stack up to $O(n)$ | No |
| Three-way quick | Linear on all-equal keys; $O(nr)$ for $r$ values | $\Theta(n^2)$ with unrestricted values | Same stack qualification | No |
| Floyd heapsort with early-stop sink | Can be linear on all-equal keys | $\Theta(n\log n)$ | $O(1)$ | No |
| Stable counting | $\Theta(n+K)$ | Same for stated universe | $O(n+K)$ | Yes |
| Stable LSD radix | $\Theta(d(n+B))$ | Same for stated digits/base | $O(n+B)$ reused | Yes |
| Distribution bucket + insertion | Expected linear under the stated independence/distribution | $\Theta(n^2)$ | $O(n+\text{buckets})$ | If both stages preserve identity order |

No row is a universal winner. Choose using the actual promise: stability, payload size, write cost, available RAM, integer universe, duplicates, inversions, adversarial input, expected versus worst-case requirements, and external storage. Explain why each competing method violates a requirement or loses the relevant bound.

## 18. Complete summary and an examination-solving method

Sorting requires an ordered permutation of records, not only a numerically ordered array. Stability is a second identity condition. Representation, comparator assumptions, range boundaries, comparison primitive, array-write definition and memory convention must be stated before a formula is applied.

Insertion's movements are governed by strict inversions; selection's comparisons are insensitive to input order. Bubble removes the same number of inversions but can discover them inefficiently because pass direction limits movement. Merge exploits already sorted children, uses a stable tie rule, and stops comparing when one child empties. Quicksort's partition contract determines both recursion boundaries and duplicate behavior. Floyd heap construction is linear because most nodes have small height; logarithmic root height alone is not a tight construction analysis.

Comparison lower bounds measure distinguishable relative orders. They constrain worst-case or distributional comparison work under a stated input family, not every input of every sorter. Counting and radix gain speed by inspecting numeric representation. Their universe, alphabet, digits, machine-word and buffer parameters cannot disappear from the analysis. Bucket sort gains expected speed from a distribution assumption that must be proved appropriate, not inferred from one attractive animation.

For a supplied-array question, first write the exact variant and count only the requested primitive. List each partition/merge or each successful and failed insertion comparison. Use formulas only after confirming that the supplied input attains their conditions. For a conceptual question, identify the hidden quantifier or missing promise. For a recurrence question, derive child sizes and verify record conservation before choosing a theorem. For a memory question, distinguish peak live buffer, stack depth and cumulative allocation. For a stability question, label at least two equal records and construct or rule out their reversal.

The animations show checkpoint mechanics; the written proofs establish their general claims. Exact counters refer to the displayed algorithm, not all algorithms sharing its name. The problem bank gives authentic checked archive items, explicitly mapped course-derived reconstructions and newly authored mathematical/conceptual questions. Complete solutions teach the derivation and explain the common wrong inference.

## 19. Mathematical and conceptual problems with complete solutions

<!-- INCLUDE:problems -->

## 20. Final examination rules and transfer notes

<!-- INCLUDE:review -->

## 21. Interactive sorting laboratory

Change the array, choose a precisely named variant, and inspect every comparison, move, held key, output buffer, pivot region or heap transition. Letters retain original identity. Playback starts paused. Previous, next, restart, seek, speed and keyboard controls are available. Reduced-motion mode preserves complete checkpoints without movement animation. Printing includes the state captions, counters and every checkpoint; answers remain complete text when animations cannot run.

<!-- LAB:sorting -->

## 22. References and verification limits

1. **MIT — 6.006 Introduction to Algorithms, Spring 2020.** Erik Demaine, Jason Ku, Justin Solomon. [Lecture 3: Sorting](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/6d1ae5278d02bbecb5c4428928b24194_MIT6_006S20_lec3.pdf), [Lecture 5: Linear Sorting](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/78a3c3444de1ff837f81e52991c24a86_MIT6_006S20_lec5.pdf), [Recitation 5](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/cda4cc0c0e626bfbd30bc15fb78c3994_MIT6_006S20_r05.pdf). Used for contracts, comparison/representation models, counting, radix and exercise reconstruction.
2. **Princeton — COS226 Algorithms and Data Structures, Spring 2026.** Robert Sedgewick and Kevin Wayne, lecture-slide authors. [Elementary Sorts](https://www.cs.princeton.edu/courses/archive/spring26/cos226/lectures/21ElementarySorts.pdf), [Mergesort](https://www.cs.princeton.edu/courses/archive/spring26/cos226/lectures/22Mergesort.pdf), [Quicksort](https://www.cs.princeton.edu/courses/archive/spring26/cos226/lectures/23Quicksort.pdf), [Priority Queues](https://www.cs.princeton.edu/courses/archive/spring26/cos226/lectures/24PriorityQueues.pdf). Used for exact variant distinctions, memory, duplicates, heap sorting and structured inputs.
3. **Carnegie Mellon — 15-122 Principles of Imperative Computation, Spring 2026.** Frank Pfenning, [Lecture 7: Quicksort](https://www.cs.cmu.edu/~15122-archive/s26/handouts/lectures/07-quicksort.pdf). Used for explicit partition invariants, recursive contracts, preservation, stability and all six exercise themes.
4. **Oxford — B16 Algorithms and Data Structures 1, 2024–25, v2.1.** Andrea Vedaldi, [written notes](https://www.robots.ox.ac.uk/~vedaldi/assets/teach/2024/b16/b16-notes.pdf), Chapter 2. Used for merging, lower-bound quantifiers, iterator/storage distinctions and the counts-only integer variant.
5. **Stanford — CS161 Design and Analysis of Algorithms, Fall 2025.** Mary Wootters, [written lecture index](https://cs161-stanford.github.io/lectures/), [insertion proof](https://cs161-stanford.github.io/assets/Lectures/Lecture2/CS161Lecture02_handout.pdf), [Lecture 5](https://cs161-stanford.github.io/assets/Lectures/Lecture5/Lecture5-compressed.pdf), [Lecture 6](https://cs161-stanford.github.io/assets/Lectures/Lecture6/Lecture6-compressed.pdf). Used for randomized pair indicators, the invalid mean-split counterexample, stable radix induction and base trade-offs.
6. **Iranian MSc/PhD examination repository.** [Phd-Exam-CSE, pinned archive commit](https://github.com/bheydari721rn24/Phd-Exam-CSE/tree/bdadf6e2c9cadc4772ae137a96a3da753c7cfd08/Exams). The two included sorting questions link individually to their original pages and retain PDF hashes. Options were visually checked. Answers are independently derived; no official-key status is claimed.

The [quality audit](../reviews/a_sort-quality.html) records mathematical oracles, model checks, layout/control checks and preserved previous material. The selected courses cover a documented pool; their entire worldwide alternatives have not been exhaustively reviewed. Advanced examples such as external merging and distribution bucket analysis are independently derived extensions with their assumptions written in full. This is a review draft awaiting the student's approval. Proofs and finite tests reduce error risk; they do not establish literal 100% certainty or promise a particular examination score.
