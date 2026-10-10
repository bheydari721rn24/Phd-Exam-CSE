# Heaps and Priority Queues: Exact Structure, Repair Proofs, and Amortized Design

## 1. Written sources and learning contract

This chapter synthesizes four core written university courses: MIT 6.006, CMU 15-122, Princeton COS226, and Cambridge Algorithms. Stanford CS106B supplies an additional reviewed comparison. The [source-selection audit](../reviews/a_heap-sources.html) records the candidate pool, exact reading ranges, limitations and corrections. Source prestige is not a correctness proof: every claim below specifies its representation, comparison rule and cost model.

Prerequisites are logarithms, complete binary trees, array indices, loop invariants, permutations and asymptotic bounds. The teaching route goes from those foundations to indexed queues, heap counting, selection applications, binomial forests and ordinary Fibonacci heaps. Advanced structures have different invariants and different animations; a binary heap animation cannot demonstrate a Fibonacci cascade.

The default queue is a **min-priority queue**. A smaller numeric key means a higher priority. Most binary examples use zero-based storage. A max heap reverses comparisons. Every diagram declares its orientation and inputs. A review draft is a quality-checked teaching artifact, not a claim of student approval or a guarantee about every unseen examination question.

## 2. Priority is an interface, not a tree shape

A priority queue maintains a multiset of records and supports insertion, peeking at an extreme-priority record, and removing such a record. It may also support changing a known record's priority, deleting a known record, melding queues or finding both extrema. A binary heap is one implementation of some of these operations. A heap-ordered pointer tree with an arbitrary shape is not necessarily a binary heap.

Represent a record as `(priority, arrival, identifier, payload)`. Compare priority first. For FIFO ties, compare the unique arrival number next. The identifier locates the record and the payload is the information returned to the client. Duplicate priorities are valid; duplicate live identifiers are not. Comparing a payload accidentally, or mutating a priority outside the queue's repair operation, breaks the intended interface.

For a general comparator, require a consistent strict weak ordering; numerical examples use the usual total order. If neither record precedes the other, they belong to an equivalence class. A secondary arrival key makes stable tie order explicit. NaN, inconsistent comparators and time-varying comparison rules require a declared policy rather than an assumption that ordinary heap proofs still apply.

| Implementation | Insert | Extract extreme | Peek extreme | Qualification |
|---|---|---|---|---|
| Unordered fixed-capacity array | Constant | Linear | Linear | A cached extreme improves peek, but deletion may require a new scan. |
| Sorted array, extreme at the occupied end | Linear | Constant | Constant | Binary search does not eliminate shifting. |
| Sorted singly linked list, extreme at the head | Linear | Constant | Constant | Locating insertion position can scan the list. |
| Balanced search tree | Logarithmic | Logarithmic | Logarithmic without a cache | A maintained extreme pointer gives constant peek. |
| Fixed-capacity binary heap | Logarithmic worst case | Logarithmic worst case | Constant | Search for an arbitrary identifier is linear without additional indexing. |

The distinction between a cached minimum and an obsolete minimum is important. A max heap supporting only insert and delete-max can cache the minimum value: delete-max cannot eliminate the last occurrence of a smaller minimum while larger values remain. This argument fails after arbitrary deletions or priority increases. Metadata must be justified against the entire permitted operation set.

## 3. Complete shape and exact array arithmetic

A complete binary tree fills every depth before starting the next, and fills the final depth from left to right. For a nonempty tree of size $n$, its edge height is

$$h=\lfloor\log_2 n\rfloor.$$

Indeed, depth $h$ starts at size $2^h$ and ends at size $2^{h+1}-1$. A singleton has height zero. The empty heap has no root; set its height to minus one when a formula needs a convention, but never evaluate the logarithm of zero.

For zero-based storage, root index is zero. For a nonroot index $i$,

$$p(i)=\left\lfloor\frac{i-1}{2}\right\rfloor.$$

Its potential child indices are $2i+1$ and $2i+2$. A child exists only if its index is smaller than the active size. A missing left child implies a missing right child. The one-based translation uses parent $\lfloor i/2\rfloor$, children $2i$ and $2i+1$, and root one. Convert the entire representation consistently rather than changing one formula in isolation.

At depth $d$, the zero-based indices run from $2^d-1$ to $2^{d+1}-2$, clipped at $n-1$. Thus the depth of index $i$ is $\lfloor\log_2(i+1)\rfloor$. In one-based numbering, remove the leading one from the binary representation of the index: each remaining zero chooses left and each one chooses right. This encodes a **position**, not a key-order search route.

Node $i$ has a child precisely when $2i+1<n$. Therefore the internal indices are zero through $\lfloor n/2\rfloor-1$ and the leaf indices begin at $\lfloor n/2\rfloor$. The number of leaves is $\lceil n/2\rceil$. For even size there is exactly one internal node with only a left child; for odd size every internal node has two children.

An array's capacity can exceed its active size. Spare cells are not tree nodes. In the CMU one-based representation, `next = size + 1`; an empty queue has next one and a singleton has next two. A diagram must use the active prefix, not every allocated cell.

<!-- SIM: shape -->

## 4. Heap order and what it does not imply

For a min heap, every parent key is at most its child key. For a max heap, every parent is at least its child. Transitivity along a root-to-node route proves that the root is a global extreme. This proof requires neither sibling order nor sorted left and right subtrees.

For instance, $[1,7,3,9,8,4,5]$ is a min heap, although the array is unsorted and the left child exceeds the right child. Its inorder traversal is also not a sorted sequence. Binary search by key cannot decide which child contains a sought value. A min heap can prune a subtree when its root exceeds a queried upper threshold, but in the worst case arbitrary membership still inspects a linear number of entries.

With distinct keys, the second minimum lies among the root's existing children: any deeper candidate has a smaller ancestor below the root. More generally, the $k$th smallest key has depth at most $k-1$, because a route of depth $d$ contains $d$ smaller ancestors. This is an upper bound, not an assertion that every shallow node is one of the first $k$ keys.

The maximum of a min heap has a representative among its leaves. If keys are distinct, it must be a leaf. With equal keys, an internal node can also attain the maximum, but following equal-or-larger child keys reaches a maximal leaf. Scanning all leaves therefore suffices. Without extra metadata, the worst case is linear because the leaf values can be independent candidates.

## 5. Sifting upward: algorithm and strengthened proof

To insert a record, append it at the unique next complete-tree position, then compare it with its parent. If it precedes its parent, exchange the entire records and continue from the parent's index. Stop at the root or the first satisfied comparison. This preserves complete shape throughout.

```python
def sift_up(a, i):
    while i > 0:
        p = (i - 1) // 2
        if not a[i] < a[p]:
            break
        a[i], a[p] = a[p], a[i]
        i = p
    return i
```

For insertion, the active record is initially a leaf. All other edges satisfy heap order. During repair, one upward edge may fail, but a proof using only that exception is too weak for a general helper: after a swap, the displaced parent must also be no larger than the active record's children.

Consider a local min-tree with parent 10, active child 1, and the active child's children 2 and 3. Every edge except 10-to-1 is legal. Swapping 10 and 1 creates illegal edges from 10 to 2 and 3. This is a counterexample to the unstrengthened invariant, not a counterexample to insertion: that configuration is not reached by appending a leaf and moving it upward from an initially valid heap.

A sufficient strengthened invariant states that every edge except the active upward edge is ordered, and the active node's parent is no larger than every existing child of the active node. When the active record rises, the displaced parent is legal above those children. The rising smaller record is legal above the displaced parent and the untouched sibling. At the next position, the corresponding grandparent condition follows from previously ordered edges. The active index strictly decreases, so termination follows. At termination, the only permitted exception is either absent or satisfied.

Inserting 2 into $[5,9,8,12,10,14,11]$ places 2 at index seven, then exchanges indices 7–3, 3–1 and 1–0. The final array is $[2,5,8,9,10,14,11,12]$. There are three priority comparisons and three exchanges. Inserting a sufficiently large key into a nonempty min heap needs one comparison and no exchange. Worst-case route work is logarithmic, not the exact work of every insertion.

<!-- SIM: up -->

## 6. Sifting downward and extracting the root

To extract the minimum, save the root record, move the final active record to index zero, shrink the active size, then sift that replacement downward. Removing a singleton must leave an empty array without reading a nonexistent root. Save and return the removed record; moving a record to repair shape is not itself a second deletion.

Choose the smaller existing child, compare that child with the active parent, and exchange only if the child precedes it. With equal children, this chapter consistently chooses the left child. Choosing a merely smaller-than-parent child without checking its sibling can leave the promoted root above a still-smaller sibling.

```python
def sift_down(a, i, size):
    while 2 * i + 1 < size:
        c = 2 * i + 1
        r = c + 1
        if r < size and a[r] < a[c]:
            c = r
        if not a[c] < a[i]:
            break
        a[i], a[c] = a[c], a[i]
        i = c
    return i
```

The child subtrees are heaps. After promoting their smaller root, the promoted record is legal above both the displaced record and the other child. Only the displaced record's outgoing edges may now fail. If the operation begins below a parent, require that parent to be no larger than the child roots that might be promoted; extraction from the global root satisfies this condition vacuously. A generalized heapify helper can instead specify that it repairs only its subtree, leaving the enclosing parent edge outside its postcondition.

Each iteration moves to a greater-depth index and cannot pass the subtree's height. The last iteration may have one child, requiring only the parent comparison. Two children require one comparison to choose a child and one to decide whether to exchange. Loop/index tests, record movements and priority comparisons are different counters.

Extracting from $[2,5,8,9,10,14,11,12]$ moves 12 to the root. The chosen child indices are one, then three. The repaired result is $[5,9,8,12,10,14,11]$. The algorithm makes four priority comparisons and two repair exchanges; the initial root replacement is counted separately as a movement.

<!-- SIM: down -->

## 7. Linear construction: a complete proof for incomplete trees

To build a heap from an arbitrary array, sift internal nodes downward in decreasing index order. Leaves are already heaps. When node $i$ is visited, both its child subtrees have already been repaired; a sift repairs the subtree rooted at $i$. Backward induction establishes a valid heap at the final root.

```python
def build_min_heap(a):
    for i in range(len(a) // 2 - 1, -1, -1):
        sift_down(a, i, len(a))
```

Multiplying the number of internal nodes by the root height gives a valid but loose logarithmic-per-node upper bound. Most internal nodes are close to leaves. We can count the available downward steps exactly.

At zero-based index $i$, the leftmost descendant $j$ edges below has index $2^j(i+1)-1$. It exists exactly when $2^j(i+1)\le n$. Consequently the subtree height is

$$h_i=\left\lfloor\log_2\frac{n}{i+1}\right\rfloor.$$

Count the heights by horizontal layers: the number of nodes with height at least $j$ is $\lfloor n/2^j\rfloor$. Thus

$$\sum_{i=0}^{n-1}h_i=\sum_{j\ge1}\left\lfloor\frac{n}{2^j}\right\rfloor.$$

Write the binary expansion of $n$ as $n=\sum_{b\ge0}\epsilon_b2^b$. A set bit at position $b$ contributes $2^{b-1}+\cdots+1=2^b-1$ to the right-hand sum. If $s_2(n)$ is the number of set bits,

$$\sum_{j\ge1}\left\lfloor\frac{n}{2^j}\right\rfloor=n-s_2(n)<n.$$

Each sift uses at most its starting subtree height exchanges and at most twice that height priority comparisons. The build therefore uses at most $n-s_2(n)$ repair exchanges and at most $2(n-s_2(n))$ comparisons. These are safe upper bounds; a terminal failed comparison is included in the per-height bound, and the comparison count is not claimed to equal twice the realized exchanges.

For size ten, the sum is $5+2+1=8$. The binary expansion of ten has two set bits, giving the same result. For a perfect tree of edge height $h$, the sum is $n-h-1$. Arrays already satisfying heap order have zero repair exchanges but still require inspecting child comparisons under the stated builder.

The lower bound is linear in the comparison model: a construction algorithm must identify the root extreme among all entries, which requires at least $n-1$ comparisons in the worst case. Reading/writing the output representation also costs linear work. Hence bottom-up build is worst-case linear. Repeated insertion has a different worst case: a descending input into a min heap makes every new record rise to the root, with total exchanges $\sum_{j=1}^{n}\lfloor\log_2 j\rfloor$.

<!-- SIM: build -->

## 8. Exact traces, counters and alternative repair implementations

For the input $[9,4,7,1,0,3,2]$, build visits indices two, one and zero. Index two exchanges 7 with 2. Index one exchanges 4 with 0. Index zero exchanges 9 with 0, then 9 with 1. The final array is $[0,1,2,9,4,3,7]$. There are four exchanges and eight priority comparisons. The final array need not match repeated insertion's valid final array.

A hole implementation holds the active record in a temporary variable and moves parents or children into its vacated cell until it finds a destination. It reduces assignments per traversed edge, but comparisons and logical positions follow the same route when stopping/tie rules agree. A visualization of a hole must distinguish a temporarily empty position from a deleted record.

An unconditional-to-leaf sink promotes the smaller child until a leaf, then moves the held record upward to its destination. This can reduce some comparison counts but is a different algorithm; the ordinary early-stop counters cannot be copied to it. Similarly, checking both parent-child relations separately before choosing the better child can perform more comparisons than the two-comparison implementation above.

For examination counting, write down: orientation, index base, active size, chosen-child tie rule, stopping rule, whether the root-last exchange is counted, and whether comparisons refer to priorities or all program conditions. An asymptotic answer often survives these choices; an exact numerical answer usually does not.

## 9. Indexed queues, changing priorities and arbitrary deletion

Store a permutation array `pq[position] = identifier`, a key array indexed by identifier, and an inverse position array or map `pos[identifier] = position`. The invariant is

$$\operatorname{pos}(\operatorname{pq}(j))=j.$$

Every exchange updates both inverse entries. A handle is an identifier or a stable node reference; an ordinary array index is not stable when records move. A stale index can silently mutate a different record even though the numerical array still looks heap-ordered.

Decreasing a min-heap priority can violate only the upward edge, so sift upward. Increasing it can violate only outgoing child edges, so sift downward. For a max heap, reverse those directions. Equal priorities require no numerical repair, although changing a secondary comparator field can still change the full record's order.

To delete a known position, remove its record, move the final record into the vacated position, and shrink size. If the replacement precedes its new parent, sift upward; otherwise sift downward. Why is one direction sufficient? If the replacement is smaller than the parent, that parent was no larger than the old entry and the old entry was no larger than its children. Thus the replacement is also no larger than those children. If the upward relation is legal, only downward edges can be wrong. Deleting the final position requires no repair. Deleting an unknown identifier still requires a search unless an index structure is present.

If lookup uses a hash map, constant lookup is expected under its declared assumptions; it is not automatically a worst-case constant guarantee. A direct bounded identifier array gives worst-case constant lookup at a capacity cost. A balanced identifier dictionary gives logarithmic lookup, still compatible with logarithmic repair.

<!-- SIM: indexed -->

## 10. Capacity growth, aggregate work and lower bounds

A fixed-capacity heap insertion traverses at most logarithmic height. A resizable array may copy all active records in one operation. Doubling from capacities one, two, four and so forth makes total copied records across $n$ appends less than $2n$. The storage component is constant amortized, so total insertion cost is logarithmic amortized; one insertion can remain linear actual time.

Shrinking at half-full while growing at full can cause repeated large copies near the threshold. Shrink at a lower occupancy, such as one quarter, to provide hysteresis. An append/pop sequence using geometric growth and such hysteresis has linear aggregate storage cost, in addition to heap repair work. Initial nonempty states require an initial-potential term in the amortized bound.

No comparison-based priority queue can make **both** insertion and extract-min constant amortized time for arbitrary distinct keys across all operation sequences. Insert an arbitrary array and extract all records: those operations would sort it in linear comparisons, contradicting the decision-tree lower bound $\log_2(n!)=\Theta(n\log n)$. This does not prohibit constant peek, constant amortized insertion alone, or specialized bounded-integer queues operating outside the comparison model.

Building a heap does not disclose the sorted order of its leaves and siblings. Its linear lower bound is compatible with the sorting lower bound because heap construction leaves many valid arrangements and incomparable pairs.

## 11. Heapsort: two simultaneous invariants

Ascending in-place heapsort first builds a **max** heap. At active size $m$, exchange root with index $m-1$, reduce $m$, and repair the prefix. The suffix consists of the previously extracted maxima in ascending final order. Every suffix key is at least every active-prefix key. The active prefix becomes a heap again after each repair.

```python
def heapsort(a):
    def down(i, m):
        while 2*i + 1 < m:
            c = 2*i + 1
            if c + 1 < m and a[c] < a[c+1]:
                c += 1
            if not a[i] < a[c]:
                break
            a[i], a[c] = a[c], a[i]
            i = c
    for i in range(len(a)//2 - 1, -1, -1):
        down(i, len(a))
    for m in range(len(a)-1, 0, -1):
        a[0], a[m] = a[m], a[0]
        down(0, m)
```

Bottom-up construction is linear. Sortdown has at most a logarithmic repair route at each size, giving a worst-case upper bound proportional to $n\log n$. The general comparison sorting lower bound supplies a matching worst-case lower bound. This is a worst-case statement, not a proof that every input needs that many comparisons.

With equal keys and the early-stop code above, every sink stops after its first child selection/parent check. Construction and sortdown then perform only linear work. Distinct-key best-case analysis is subtler and is not derived from that equal-key example. The standard algorithm is not stable: equal records can exchange their original order during root-last moves even if equal parent-child comparisons never exchange.

The iterative in-place implementation uses constant auxiliary storage. A separate queue holding all entries uses linear extra storage, and a recursive sift adds logarithmic call-stack space. Decorating records with original arrival numbers can impose stable sorted order but changes the compared keys and may require extra metadata; it does not make the undecorated algorithm stable.

<!-- SIM: sort -->

## 12. Counting valid distinct-key heaps

The complete shape is fixed by size. For distinct keys, the minimum must occupy the root of a min heap. If the left and right subtrees have sizes $L$ and $R$, choose which $L$ of the remaining $n-1$ ranks go left, then arrange each subtree as a valid heap:

$$H(n)=\binom{n-1}{L}H(L)H(R).$$

Use $H(0)=H(1)=1$. For edge height $h\ge1$, put $t=n-(2^h-1)$, the population of the final level. The left subtree has its full earlier levels plus the left portion of the final level:

$$L=2^{h-1}-1+\min(t,2^{h-1}),\qquad R=n-1-L.$$

For seven nodes, both subtrees have size three, so $H(7)=\binom{6}{3}\cdot2\cdot2=80$. For six nodes, the subtree sizes are three and two, giving $H(6)=\binom{5}{3}\cdot2\cdot1=20$. A uniformly random permutation is therefore a min heap with probability $H(n)/n!$; for six nodes this is one thirty-sixth.

An equivalent tree-poset formula is

$$H(n)=\frac{n!}{\prod_{v}|T_v|}.$$

Induct on the root split: multiplying the child formulas and the binomial choice cancels the two subtree factorials and contributes the root subtree size $n$ in the denominator. This counts rankings respecting ancestor order. It is not a count of insertion histories or final arrays under a particular builder. With duplicate keys, neither division by the factorials of multiplicities nor the distinct-label recurrence is generally valid without a new counting argument.

## 13. Multiway heaps and workload-dependent arity

A complete $d$-ary heap fills each level from left to right with up to $d$ children per node. For zero-based storage, the parent of nonroot index $i$ is $\lfloor(i-1)/d\rfloor$ and the children of index $i$ are $di+1$ through $di+d$, clipped by active size.

The maximum nodes through depth $h$ are $(d^{h+1}-1)/(d-1)$. For $n\ge1$ and integer $d\ge2$, the exact edge height is

$$h=\left\lceil\log_d((d-1)n+1)\right\rceil-1.$$

Use integer geometric thresholds in executable checks to avoid floating-rounding errors at powers. A sift-up uses one priority comparison per traversed level. A sift-down with $c$ existing children uses $c-1$ comparisons to find the best child and one to compare with the parent. Consequently its worst-case comparison upper bound is proportional to $d\log_d n$, whereas insertion is proportional to $\log_d n$. These expressions describe a useful regime; if $d$ exceeds size, a root has only the actual existing children, not $d$ comparisons.

For $U$ upward operations and $D$ downward operations at roughly fixed large size, a simplified comparison objective is $(U+Dd)/\ln d$, ignoring common factors and incomplete final levels. If $D>0$, differentiating gives the continuous stationary equation

$$d(\ln d-1)=U/D.$$

Round only after comparing feasible integer candidates. For deletion-only comparison work, the optimum continuous arity is $e$, so binary versus ternary is the meaningful integer comparison. Frequent upward operations favor larger arity. Cache lines, branch cost and record movement can change the practical optimum. There is no universally best arity four independent of workload.

<!-- SIM: multiway -->

## 14. Selection, thresholds and sorted streams

To retain the largest $k$ entries from a stream, maintain a **min** heap of at most $k$ retained entries. Its root is the weakest retained entry. Fill it first; afterwards reject a candidate no better than the root and replace/repair the root for a better candidate. The invariant is that the retained multiset consists of the largest $k$ entries seen so far, with an explicit tie policy. Worst-case time is $O(n\log k)$ and storage is $O(k)$; taking logarithms of one can be avoided by writing $O(n\log(k+1))$.

To find the $k$th smallest entry of an existing min heap without modifying it, use a second min heap of frontier positions. Start with the source root. Remove the smallest frontier record and add its existing children. Every not-yet-returned source node has a first unreturned ancestor in the frontier, whose key is no greater. Thus the next frontier extreme is the next global rank. After $k$ removals, frontier size is at most $k+1$, so the cost is $O(k\log(k+1))$. The original heap stays unchanged. Repeatedly extracting from the original instead costs $O(k\log n)$ and destroys entries unless they are restored.

For a max heap, to decide whether at least $k$ entries are at least threshold $x$, visit a node only when its key meets the threshold; otherwise prune its entire subtree. Stop after $k$ qualifying entries. Before stopping, each qualifying node generates at most two child tests, so the decision costs $O(k+1)$ even if many entries would ultimately qualify. This threshold decision is not a general linear-time proof for finding the exact $k$th key.

To merge $r$ sorted lists containing $N$ total entries, keep one unconsumed head from each nonempty list in a min heap. After extracting a head, insert the next entry from that same list. Every remaining entry is at least its own list's head, proving the frontier invariant. Initialization costs $O(r)$ with bottom-up build; the merge costs $O(N\log(r+1))$ and $O(r)$ extra storage. Sequentially merging into a growing accumulated list is a different algorithm with a different bound, as the authentic examination bridge explains.

Two heaps maintain a running median: a max heap for a lower half and a min heap for an upper half. Keep every lower key no greater than every upper key, and maintain equal sizes or one extra lower entry. A new key enters an appropriate half, and at most one extreme transfer restores the size invariant. The lower median is the lower root; the arithmetic mean for even size is a separate definition and may overflow fixed-width integer addition.

## 15. Binomial forests: binary addition made structural

A binomial tree $B_0$ has one node. Link two heap-ordered trees of rank $j$ by attaching the worse root beneath the better root; the result is $B_{j+1}$. By induction, $B_j$ has $2^j$ nodes, edge height $j$, root degree $j$, and child trees of ranks $j-1,j-2,\ldots,0$. Its depth-$r$ population is $\binom{j}{r}$ by Pascal's recurrence.

A canonical binomial heap has at most one tree of each rank. Its ranks are exactly the set-bit positions of its size. Size thirteen gives ranks zero, two and three because thirteen is eight plus four plus one. The number of roots is $s_2(n)$, and the maximum rank is logarithmic.

Melding two canonical forests resembles binary addition. At a rank with two trees, link them and carry one tree to the next rank. If an incoming carry meets two existing trees, keep one tree at that rank and carry the link of the other two; the implementation must not discard any of the three. Heap order chooses the winning root but does not change the rank arithmetic.

Each link reduces the total root count by exactly one. Thus melding sizes $n$ and $m$ uses exactly

$$s_2(n)+s_2(m)-s_2(n+m)$$

links, regardless of priority values, under full canonical consolidation. Insertion is meld with a singleton; size $2^q-1$ causes $q$ links, while an even size causes none. Across $N$ singleton insertions from empty, total links are $N-s_2(N)$, so linking work is constant amortized. An implementation that scans every rank on every insertion would waste this benefit; carry insertion must stop when the carry stops.

Extract-min locates the least root, removes it, turns its ranked children into a forest, and melds those children with the remaining forest. Reversing a linked child list may be necessary to obtain increasing rank order. This costs logarithmic time. A cached minimum makes peek constant but must be refreshed after extraction and maintained across links and melds. Decrease-key can move the record upward in its binomial tree; a handle map must follow the **record**, not just a node whose payload may have changed.

<!-- SIM: binomial -->

## 16. Potential analysis without invalid cancellation

Let $c_i$ be the actual cost of operation $i$, and let a nonnegative state function $\Phi$ measure stored accounting credit. Define the amortized charge

$$\widehat c_i=c_i+\Phi_i-\Phi_{i-1}.$$

Summing telescopes:

$$\sum_{i=1}^{m}c_i=\sum_{i=1}^{m}\widehat c_i+\Phi_0-\Phi_m.$$

If the initial potential is zero and final potential is nonnegative, actual aggregate cost is bounded by aggregate charges. If the initial heap is already complicated, the $\Phi_0$ term remains. Amortized analysis is deterministic aggregate reasoning; it is not an expected value over random inputs.

For a binomial insertion using $q$ links, count one unit for the new singleton and one per link. The root potential changes by $1-q$. Thus the charge is $(1+q)+(1-q)=2$. Root count never becomes negative and starts at zero. This exact normalized calculation proves constant amortized linking work. Additional constant work per link can be paid by scaling the root potential by an adequate constant.

Never cancel $O(q)$ against minus $q$ without controlling its coefficient. If actual link work is at most $Cq+C_0$, use potential scaled by $C$. An equation containing big-O notation is an inequality with hidden constants, not algebra on a known numerical cost.

## 17. Fibonacci heaps: laziness, marks and exact operations

An ordinary Fibonacci heap stores a forest of heap-ordered trees, a root list, a minimum-root pointer, and for each node a degree, parent, child-list pointer and mark. Unlike binary heaps, its trees need not be complete. Unlike a canonical binomial heap, it may temporarily have many roots of the same degree.

Insertion adds a singleton root and updates the minimum pointer. Meld concatenates root lists and takes the better of the two minimum pointers. Circular doubly linked lists support these actions in constant pointer work; copying an array of roots or children would not. Handle lookup must be specified separately.

Extract-min removes the minimum root, promotes its children to unmarked roots, and consolidates equal-degree roots. A degree table stores at most one current root per degree. When a collision occurs, link the worse root under the better root, increase the winning degree, clear the occupied slot and continue carrying. Recompute the minimum among the surviving roots. Iterate over a stable root snapshot or carefully maintain traversal pointers while links mutate the list.

Decrease-key first changes the known record's key. If its parent relation is still legal, no cut is required; if it is now better than its parent, cut it and add it to the root list. Losing a first child marks a **nonroot** parent. Losing a second child cuts that marked parent too, clears its mark, and continues upward. Roots do not become marked merely for losing a child. A newly linked child starts unmarked.

For example, root 1 has child 4, and 4 has children 7 and 9. Decreasing 7 to 0 cuts that child and marks 4. Decreasing 9 to 2 then cuts that child and the already-marked 4; both become unmarked roots. The root count rises by two in that second operation while the marked-node count falls by one. These are changes in the forest's actual edges, not a binary sift through fixed array positions.

Deleting a known node can be reduced to decrease-key to a special value preceding every ordinary key, followed by extract-min. If ordinary keys can already attain a numeric negative infinity, use a separate forced-priority flag or an implementation that removes the specified node directly. Merely assigning the same minimum value does not identify which tied record is extracted.

<!-- SIM: fibonacci -->

## 18. Fibonacci degree proof and amortized costs

Let $t$ be the number of roots and $m$ the number of marked nonroot nodes. Use the potential $\Phi=t+2m$ in normalized primitive work, with constant scaling when required. It is nonnegative and zero for an empty heap.

Insertion adds one root, so actual and potential changes are constant. Meld adds the root/mark counts; relative to the sum of the two input potentials, concatenation has constant charge. A decrease-key cascade cutting $c$ nodes adds $c$ roots. At least $c-1$ of the cut nodes were marked ancestors and become unmarked; at most one final ancestor becomes marked. Therefore

$$\Delta\Phi\le c-2(c-1)+2=4-c.$$

Under cost $c+1$ for cuts plus fixed work, its charge is at most five. A single operation may make many cuts; its amortized bound remains constant because earlier marks paid for the cascade. With a larger primitive coefficient, scale the potential. This argument includes cascades that stop at the root and short cascades with no final new mark.

During extract-min, suppose $T$ roots await consolidation, $L$ links occur and $R=T-L$ roots remain. Each link reduces potential by one, offsetting its normalized work. Scanning the input roots is also paid in proportion to the lost root count plus the surviving count: $T=L+R$. A degree-table scan and child promotions cost $O(D)$ where $D$ bounds maximum degree. The surviving forest has at most one root per degree, so $R\le D+1$. With suitable constant scaling, total amortized extract-min cost is $O(D+1)$; actual work can be linear when many lazy insertions precede one extraction.

To bound $D$, inspect a node $x$ with surviving children $y_1,\ldots,y_d$ ordered by their last link time. When $y_i$ was linked, $x$ already had at least $i-1$ earlier surviving children. Equal-degree linking gave $y_i$ at least $i-1$ children at that time. While remaining attached, it could subsequently lose at most one child, so its current degree is at least $\max(0,i-2)$.

Let $S_d$ be the smallest size permitted by this child-degree lower-bound rule. Its base values are $S_0=1$ and $S_1=2$, and

$$S_d=1+S_0+\sum_{j=0}^{d-2}S_j\quad(d\ge2).$$

Subtract the analogous expression for the previous degree to get $S_d=S_{d-1}+S_{d-2}$. Hence $S_d=F_{d+2}$ with $F_0=0,F_1=1$. Since $F_{d+2}\ge\varphi^d$, any degree-$d$ subtree has at least $\varphi^d$ nodes, giving $d\le\log_{\varphi} n$. Thus maximum degree is logarithmic and extract-min is logarithmic amortized.

The bound applies to every node, not only roots. Degree is the number of children, not tree height. Cascading cuts do not enforce AVL balance; ordinary Fibonacci trees can have large height. Marks preserve enough descendants for the degree bound, which is the quantity needed for extract-min.

## 19. Related meldable structures and application choices

A leftist min heap uses null-path length: set null rank to zero and a node's rank to one plus the smaller child rank. Maintain left rank at least right rank. A rank-$r$ subtree has at least $2^r-1$ nodes by induction, so the right spine is logarithmic. Meld compares roots, recursively melds the better root's right child with the other heap, swaps child pointers if needed to restore the leftist condition, and recomputes rank. The recursive route decreases the sum of two right-spine lengths; meld is logarithmic in combined size. The entire leftist tree need not have logarithmic height. Insert is meld with a singleton and extract-min is meld of the root's two children.

A min-max heap instead has alternating level order: with root depth zero, every even-depth node is no larger than its descendants, and every odd-depth node is no smaller. The root is the minimum; the maximum is among its existing children. Repair must compare children and grandchildren and preserve alternating ancestor constraints. Ordinary binary sift code does not establish this stronger invariant. A dual-heap design with stable identifiers is often simpler: store each live record in both an indexed min heap and an indexed max heap, and remove its counterpart after an extraction. Both roots are constant-time extrema, known updates are logarithmic, and storage is linear.

For Dijkstra with nonnegative edge weights, an indexed binary queue supports at most logarithmic work for each successful relaxation/decrease and each extraction, giving $O((V+E)\log(V+1))$ with adjacency lists. An ordinary Fibonacci queue gives $O(E+V\log(V+1))$ amortized. The queue does not fix Dijkstra's correctness on negative edges. Lazy duplicate entries can avoid decrease-key, but stale entries must be discarded and queue size can depend on $E$, changing the logarithmic factor and storage claim.

For hard real-time latency, a logarithmic worst-case fixed-capacity binary queue can be more appropriate than an amortized Fibonacci bound. For frequent melds, binomial or leftist structures offer a different interface tradeoff. For mostly peek operations, a cached extreme changes the relevant comparison. State the operation mix and latency requirement before choosing a structure.

## 20. Examination reasoning from formula to invariant

First identify what the question gives: an existing heap, an arbitrary input array, a stream, a known handle, a rank query, or a meld operation. Next identify what the algorithm may change. Selecting from an existing heap is different from building one, and reading a handle is different from searching by value.

For exact counts, draw the active indices and follow the stated comparison code. For asymptotic counts, express the aggregate route heights or the permitted potential. For structure counts, distinguish rank, degree, depth and size. For conceptual alternatives, produce a valid counterexample or a proof under all stated assumptions. The final rules and worked bank apply this process to incomplete shapes, equal priorities, wrong-child repairs, lower bounds, mutable handles and advanced amortization.

The authenticated bank includes a doctoral existing-heap rank question and an MSc sequential-merge question read from the original PDF pages. Their solutions are independently derived, not official answer keys. The original and course-inspired bank adds medium-to-hard formula and proof problems, with small boundary diagnostics clearly identified. It is a selected extensive bank, not a claim that every question in every course has been reproduced.

## 21. Complete summary

Complete shape gives exact index arithmetic and logarithmic binary height; heap order makes only the root extreme. Sift-up follows a possible parent violation, while sift-down promotes the best existing child. Both proofs need enough local order information to justify displaced records. Bottom-up construction is linear because the total available downward height is $n-s_2(n)$, while repeated insertion can be logarithmic per record.

An indexed queue preserves an inverse permutation after every movement. Known priority changes and deletion repair one route; unknown-record search and opposite-extreme search need separate analysis. Resizing adds an amortized storage component and can create linear individual operations. Heapsort's active heap and final suffix have simultaneous invariants; its worst case is logarithmic per item, its iterative auxiliary space is constant, and its ordinary tie behavior is unstable.

Distinct heap counts follow a fixed-shape binomial recurrence. Multiway arity trades shorter routes against more child comparisons. A second frontier heap selects from an existing heap without modifying it; a retained min heap supports stream top-k; one head per sorted list supports multiway merging; two opposite heaps support a running median.

Binomial forests encode size in rank bits and support exact carry-link counts. Fibonacci forests postpone consolidation, use marks to control child losses, and pay for expensive individual operations with nonnegative potential. Their degree lower bound is Fibonacci growth, yielding logarithmic amortized extraction and constant amortized decrease-key. These are qualified bounds for defined operations and representations, not unconditional performance labels.

## 22. Worked mathematical and conceptual problems

<!-- INCLUDE: problems -->

## 23. Final reasoning rules and examination traps

<!-- INCLUDE: review -->

## 24. Editable exact laboratories

<!-- LAB: heap -->

## 25. References and remaining uncertainty

- MIT, 6.006 Introduction to Algorithms, Spring 2020; Erik Demaine, Jason Ku and Justin Solomon: [Lecture 8, Binary Heaps](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/40d4851e550507ca14dc778b9b2266cc_MIT6_006S20_lec8.pdf), PDF pages 1–7.
- Carnegie Mellon University, 15-122 Principles of Imperative Computation, Fall 2026; Frank Pfenning: [Lecture 25, Priority Queues](https://www.cs.cmu.edu/~15122/handouts/lectures/25-pq.pdf), pages 1–13, and [Lecture 26, Restoring Invariants](https://www.cs.cmu.edu/~15122/handouts/lectures/26-heap.pdf), pages 1–24.
- Princeton University, COS226 Algorithms and Data Structures, Spring 2025 written archive; Robert Sedgewick and Kevin Wayne: [Priority Queues slides](https://www.cs.princeton.edu/courses/archive/spring25/cos226/lectures/24PriorityQueues.pdf), all 43 PDF pages, and [Algorithms, Fourth Edition, §2.4](https://algs4.cs.princeton.edu/24pq/).
- University of Cambridge, Algorithms, 2023–2024; Damon Wischik, with Frank Stajano course materials: [Algorithms 2](https://www.cl.cam.ac.uk/teaching/2324/Algorithm1/content/algorithms2.pdf), printed pages 51–74 / PDF pages 53–76, and [Example sheet 6](https://www.cl.cam.ac.uk/teaching/2324/Algorithm1/ex/ex6.pdf), two pages.
- Stanford University, CS106B Programming Abstractions, Spring 2020; Chris Gregg and Julie Zelenski: [written heap slides](https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1206/lectures/heaps/), 16 slides; Autumn 2023 [written priority-queue notes](https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1242/lectures/17-pqheap/).
- Iranian original examination provenance, file hashes, page numbers and independently derived answers appear beside each authenticated question and in the audit.

The coverage audit distinguishes automated arithmetic checks, independently recomputed algorithm states, manually reviewed proof obligations and browser/diagram checks. Finite testing cannot prove every input property; the written invariants supply the general arguments. Optimal selection algorithms, production library details and more specialized heap families remain outside this chapter's claims. Studying it develops broad problem-solving tools; learning and examination performance still require practice and later assessment.
