# Arrays, Linked Lists, and Operation Costs

## 1. Sources, scope, and learning targets

This chapter studies the representation of a mutable sequence. It separates the cost of locating an element from the cost of modifying a representation, proves amortized bounds, and follows actual memory links. Programming syntax and elementary array indexing were introduced in the programming chapter; here they become assumptions in quantitative data-structure arguments. Stacks, queues, heaps, hashing, and tree interfaces receive their own chapters. Sparse matrices appear only as a representation-selection bridge.

Four primary courses were selected from a documented seven-university candidate pool: MIT 6.006, Berkeley CS61B, Oxford B16, and Princeton COS226. Stanford CS106B supplies a fifth reviewed course for allocation, deletion, and recursive traversal. Cornell CS2110 contributes specifically reviewed representation-invariant examples. This is a bounded comparison of accessible written materials, not a claim that every course worldwide was accessible or reviewed. The source audit records sections actually read, inaccessible candidates, and the reason for each selection.

| Course | Reviewed material used here | Main contribution |
|---|---|---|
| MIT 6.006, Spring 2020; Erik Demaine, Jason Ku, Justin Solomon | Recitation 2, pages 1–9 | Sequence interface, indexed-list pitfall, geometric growth, cycle exercise |
| Berkeley CS61B textbook | Chapters 4 and 5, SLLists and DLLists | Cached size, sentinel design, tail-removal limitation, circular doubly linked lists |
| Oxford B16, Andrea Vedaldi, 2024 | Chapter 3, §§3.1, 3.2, 3.5 | Stable shifts, linked-list implementation, ownership and traversal |
| Princeton COS226, Robert Sedgewick and Kevin Wayne, Spring 2026 | Stacks and Queues I, primarily PDF pages 21–34 | Resizing cost, geometric sums, quarter-full shrinking, worst versus amortized cost |
| Stanford CS106B, Julie Zelenski, Handout 21, 2008 | All four pages | Iterative destruction, recursion, sorted insertion and duplicate policy |
| Cornell CS2110, Fall 2025 | Lecture 13, selected invariant and circular-list sections | Explicit empty-list representation and class invariants |

By the end, you should be able to derive a cost under stated assumptions, refute an incorrect complexity claim with a counterexample, prove a pointer algorithm, and choose a representation for a workload. Studying a chapter supports these skills; it cannot guarantee performance on every unseen examination question. The worked problems and final rules make the assumptions behind each answer visible.

## 2. The sequence interface and the cost model

A sequence is an ordered collection with logical positions $0,1,\ldots,n-1$. An abstract operation such as `insert(i,x)` specifies the new logical sequence; it does not specify an array, a linked list, or a cost. An implementation refines that interface using a representation and invariant.

Unless a problem states otherwise, use a word-RAM model. Reading or writing one word, following one valid pointer, testing two word-sized keys, and updating one counter cost one unit. An array stores fixed-size element slots. Copying a slot costs constant time; copying a variable-size object or executing a user-defined destructor need not. Allocation is treated separately when it matters. Integer addresses and indices fit in one machine word. Algorithms have exclusive access to their structures; concurrent readers require additional synchronization that this chapter does not model.

Let $n$ be live length, $C$ allocated capacity, $b$ element-slot size in bytes, and $B$ the base address. The invariant is $0\le n\le C$. Valid retrieval indices satisfy $0\le i<n$; insertion permits $0\le i\le n$. An insertion index equal to $n$ means append. An empty sequence has an insertion position but no valid retrieval position. Array capacity and list length are different quantities.

With zero-based indexing, element $i$ starts at $B+bi$. With lower bound $L$, the expression is $B+b(i-L)$. Arithmetic identifies an address directly. A singly linked list instead obtains the next node through the current node's `next` field. Its rank-$i$ element normally needs $i$ link traversals from the head. A known node handle changes the problem: it supplies a location without that traversal.

<!-- SIM:access -->

**Worked example.** An array starts at byte address 2048, has eight-byte slots, and uses lower bound −3. The slot for index 5 begins at $2048+8(5+3)=2112$. The subtraction of the lower bound is essential. The linked-list counterpart cannot infer a node address from rank and element size: nodes may be allocated far apart.

## 3. Stable array insertion and deletion

In a stable insertion, old elements retain their relative order. Assume capacity is available. Inserting at $i$ must move old positions $i$ through $n-1$ one slot to the right. The number of old-slot copies is exactly $n-i$; writing the new element adds one write. Start at the right end so a source is read before it is overwritten.

```text
insert(A, n, C, i, x):
    require 0 <= i <= n and n < C
    for j = n down to i + 1:
        A[j] = A[j - 1]
    A[i] = x
    return n + 1
```

Let `old` denote the original array. Immediately before writing position $j$, the already completed positions $j+1,\ldots,n$ contain `old[j],…,old[n−1]`, and the unprocessed source prefix remains intact. The assignment extends the completed suffix by one. When the loop terminates, positions $i+1,\ldots,n$ contain precisely the displaced old suffix. This invariant proves both content and order. An increasing loop copies the newly overwritten value repeatedly; it is not an alternative implementation of stable insertion.

Deletion at $i$ shifts old positions $i+1$ through $n-1$ left. It uses $n-i-1$ old-slot copies. The forward direction is safe because a copied source lies to the right of every position already overwritten. A reference array should clear the vacated last slot to release an otherwise retained reference; that extra write is distinct from shifting. If order is irrelevant, replacing $A[i]$ with the last live element gives constant-time deletion after the index is known. It changes the abstract contract.

<!-- SIM:shifts -->

**Worked example.** Insert 9 at position 2 in `[2,4,6,8,10]`. Copy 10 to slot 5, 8 to slot 4, and 6 to slot 3, then write 9 at slot 2. There are three shifts and four element writes. Deleting position 1 from the six-element result needs four shifts. Its final live content is `[2,9,6,8,10]`.

For a uniformly chosen insertion position among $n+1$ positions, expected shifts are $n/2$. For uniformly chosen deletion among $n$ live indices, expected shifts are $(n-1)/2$. These are probabilistic averages of linear worst-case work, not amortized bounds. Repeated insertion at the front into an initially empty array causes $0+1+\cdots+(m-1)=m(m-1)/2$ shifts even when capacity is ample.

## 4. Dynamic capacity: exact counts and geometric growth

A dynamic array separates logical length from storage capacity. When full, allocate a larger buffer, copy the $n=C$ live slots, replace the backing-buffer handle, and insert the new slot. Existing pointers into the old buffer may become invalid. Logical indices can remain unchanged even though physical addresses change.

For doubling with initial capacity one, after $m\ge1$ append operations the final capacity is $2^{\lceil\log_2 m\rceil}$. When $m=1$, there are no resize copies. In general, copies total final capacity minus one, because growth copies buffers of sizes $1,2,4,\ldots,C/2$. Including the $m$ writes for new elements gives

$$T(m)=m+2^{\lceil\log_2 m\rceil}-1<3m.$$

This counts element writes, not allocation initialization or reads. If both a copy read and write are charged, the copy term must be doubled. A resize append remains $\Theta(n)$ worst case; the average cost over every permitted append sequence is constant. No random input assumption appears.

**Worked example.** For 13 appends, capacities grow 1→2→4→8→16. Copy counts are 1, 2, 4, 8, totaling 15. Thirteen new-slot writes bring the total to 28. The thirteenth append itself writes one slot, whereas the ninth append copies eight and writes one. Equal amortized bounds do not imply equal per-operation latency.

With exact geometric capacities $C_0,gC_0,\ldots,g^kC_0$ and fixed $g>1$, the copies preceding the final capacity are

$$C_0\frac{g^k-1}{g-1}=\frac{C_{\mathrm{final}}-C_0}{g-1}.$$

Integer rounding changes exact counts, but fixed $g>1$ still gives linear total copies. A growth factor approaching one as the structure grows does not automatically preserve the same constant bound. Fixed additive growth by $h$ copies $h+2h+\cdots+qh=hq(q+1)/2$ after $q$ growth events. For $m$ appends with initial capacity $h$, $q=\lceil m/h\rceil-1$. Fixed $h$ therefore gives quadratic total copying.

<!-- SIM:growth -->

The time-space tradeoff is quantitative. Immediately after growth from full capacity $C$ to $gC$, live length is $C+1$; unused slots are $(g-1)C-1$. During copying, both buffers may coexist, occupying $(g+1)Cb$ bytes before allocator overhead. A factor of two reduces resize frequency but temporarily needs roughly three times the old buffer. A smaller factor reduces slack and increases copy frequency. Neither is universally optimal without the workload and memory constraints.

## 5. Amortization, shrinking, and hysteresis

For append-only doubling, define $\Phi(n,C)=2n-C$. After the first append from an initial capacity-one empty array, this potential is nonnegative. Before that first append, it is −1; either isolate the first operation or shift the potential by one. Do not silently assume a nonnegative initial potential.

For a nonresizing append, actual cost is one, and potential rises by two, giving amortized cost three. For an append from a full buffer of size $C$, actual cost is $C+1$. Before it, $\Phi=C$; afterward length is $C+1$, capacity is $2C$, and $\Phi=2$. The amortized cost is again three. Telescoping yields total actual cost bounded by three per append plus the initial-potential adjustment. Potential stores prepaid work; it is not an additional runtime operation.

If deletion immediately shrinks a half-full buffer by half, a full buffer can alternate between expensive growth and expensive shrinking. After growing capacity $C$ to $2C$ at length $C+1$, one deletion brings length to $C$. Shrinking now returns to capacity $C$, so the next append grows again. Only one cheap operation separates linear copies.

A standard remedy grows when full and shrinks from $C$ to $C/2$ only after deletion leaves $n=C/4$, for power-of-two capacities. Keep a fixed minimum capacity. This leaves a gap between growth and shrink thresholds. After shrinking, occupancy is one half; reaching another resize takes a number of ordinary operations proportional to capacity.

For the exact quarter-full policy, use the nonnegative piecewise potential

$$\Phi(n,C)=\begin{cases}2n-C,&n\ge C/2,\\C/2-n,&n<C/2.\end{cases}$$

An append without resizing has amortized cost at most three. A deletion without shrinking has amortized cost at most two: in the sparse branch its potential increases by one; in the dense branch it decreases by two, with a bounded transition at half occupancy. A growing append has amortized cost three as above. A shrinking deletion starts from $n=C/4+1$; afterward length is $C/4$ and capacity is $C/2$. Actual cost, charging one deletion plus copied live slots, is $1+C/4$. The old potential is $C/4-1$ and the new potential is zero, so amortized cost is two. Capacities at the minimum are handled separately, with only constant bounded work.

<!-- SIM:shrink -->

**Worked example.** With capacity 32 and length 9, a deletion reaches length 8 and shrinks to capacity 16. Eight live slots are copied. Potential falls from 7 to 0; actual cost 9 gives amortized cost 2. The next append uses existing capacity. By contrast, shrinking at half occupancy would leave no spare slot immediately after contraction.

Amortization does not turn stable middle insertion into constant time: the capacity-management overhead may be amortized constant, but $n-i$ shifts remain. A dynamic array with $m$ front insertions still has quadratic total work.

## 6. Singly linked lists: representation and safe updates

A node contains an element and a pointer to the next node. A noncircular representation stores `head`, optionally `tail`, and optionally cached `size`. With no sentinel, empty means `head = null`; if a tail is stored, it must also be null. For nonempty acyclic lists, repeatedly following `next` from head visits exactly `size` live nodes and ends at the unique tail, whose successor is null. Cached metadata belongs to the representation invariant: forgetting to decrement size is a correctness error, not a small performance defect.

A head sentinel is a permanent node whose value is outside the data sequence. Its successor is the first real node. It simplifies insertion or deletion at the front because those operations become insertion or deletion after a known predecessor. A tail pointer accelerates append but cannot normally find the predecessor of the tail. Storing only a second-to-last pointer does not solve repeated removals: after removing the tail, the predecessor of the newly cached second-to-last node is again unknown.

To insert new node $x$ after known predecessor $p$, first save or assign `x.next = p.next`, then assign `p.next = x`. Reversing these assignments makes `x.next` point to itself. Update tail if the old successor was null. Allocate and initialize the new node before publishing it through a list link, so allocation failure leaves the original list intact.

To remove the successor of $p$, require that it exists. Save victim `v = p.next`, save `v.next`, then bypass the victim. If victim was tail, set tail to $p$ (or null when $p$ is the head sentinel and the list becomes empty). Release only the detached node, and update size. Reading a victim after releasing its storage is invalid.

<!-- SIM:singly -->

**Worked example.** For head→A→B→C→null, inserting X after A performs `X.next = B; A.next = X`. Removing B afterward requires its predecessor X, so `X.next = C`. If you know only B and are forbidden to search for its predecessor, a genuine unlink is not generally constant time in a singly linked list.

The familiar node-only deletion trick copies the successor's value into the given node and bypasses the successor. It requires a non-tail node and movable payload. It destroys the successor's identity and changes the given node's payload. External handles, immutable values, or the requirement to delete exactly the given object invalidate the trick. It is not a universal solution to deletion from a singly linked list.

## 7. Doubly linked lists and circular sentinels

A doubly linked node has `prev` and `next`. For every linked node $x$, the local invariant is `x.next.prev = x` and `x.prev.next = x`. With circular sentinel $s$, an empty list has `s.next = s.prev = s`. A nonempty list places all data nodes between the sentinel's successor and predecessor. Traversal stops when it reaches $s$, not null.

Insert $x$ between adjacent nodes $p$ and $q$, with `p.next=q` and `q.prev=p`:

```text
x.prev = p
x.next = q
p.next = x
q.prev = x
```

These are four link-field writes, excluding size. The intermediate states need not satisfy the full bidirectional invariant; the completed operation must. With exclusive access, order can vary if neighbors were saved first. Concurrent publication requires an appropriate synchronization protocol.

Deleting known non-sentinel node $x$ uses saved `p=x.prev` and `q=x.next`, then `p.next=q; q.prev=p`. These two writes unlink $x$. Clearing its two fields is an optional additional two writes. Releasing storage, updating size, and preserving handles are separate concerns.

Splicing a known consecutive range from one circular doubly linked list into another needs six boundary-link writes: two to close the source gap, and four to connect the range to destination neighbors. Internal range links are unchanged. This gives constant pointer-rewiring time. If each list stores a size and the range length is unknown, determining that length costs linear time in the moved range. For a splice within the same list, the destination must not lie inside the moved range, and adjacency or no-op cases must be specified separately.

<!-- SIM:doubly -->

**Worked example.** Moving B→C from sentinel→A→B→C→D→sentinel after X in another list first links A to D in both directions. Then connect X↔B and C↔the old successor of X. Six writes are sufficient even when a source becomes empty. The sentinels eliminate null endpoints; they do not remove ownership and size obligations.

## 8. Reversal: a heap invariant, not a memorized picture

For an acyclic singly linked list, iterative reversal uses three handles:

```text
prev = null
cur = head
while cur != null:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
head = prev
```

At the loop head, `prev` reaches exactly the already processed original prefix in reverse order, while `cur` reaches the untouched suffix in original order. The two node sets are disjoint and their union is the original node set. Saving `nxt` before modifying `cur.next` preserves access to the suffix. Each iteration moves one node from the unprocessed suffix to the reversed prefix. A decreasing count of unprocessed nodes proves termination. For $n$ nodes, exactly $n$ `next` fields are written, including the original head's new null link. Auxiliary space is constant. The old head becomes the new tail.

<!-- SIM:reverse -->

A recursive reverse-print routine can leave links unchanged but uses one pending call per node. Its auxiliary call-stack space is $\Theta(n)$ even though its text is short. Recursive pointer reversal also normally consumes linear stack space unless a specific runtime optimizes the recursion. Iterative destruction similarly saves `next` before freeing each node. A recursive ownership chain can exhaust the call stack during destruction; this is distinct from the amount of heap memory being released.

**Worked example.** For A→B→C, successive pairs `(reversed prefix, untouched suffix)` are `(empty, ABC)`, `(A, BC)`, `(BA, C)`, `(CBA, empty)`. If `cur=cur.next` is executed after replacing that link, the traversal follows the reversed prefix instead of the original suffix. The saved successor is part of the proof, not an optional optimization.

## 9. Cycles: meeting, entry, and length

Floyd's algorithm uses a slow cursor advancing one link and a fast cursor advancing two. Check `fast` and `fast.next` before dereferencing twice. Compare cursor identities only after a complete iteration; the initial equal head handles do not prove a cycle.

For a reachable cycle, let $\mu$ be the number of links from head to the cycle entry and $\lambda$ the cycle length. After $t$ complete iterations, slow has moved $t$ links and fast $2t$. Once both are on the cycle, equality is equivalent to $t\equiv0\pmod\lambda$. Thus the first positive meeting iteration is the smallest positive multiple of $\lambda$ satisfying $t\ge\mu$:

$$t=\lambda\max\left(1,\left\lceil\frac{\mu}{\lambda}\right\rceil\right).$$

After a meeting, reset one cursor to head and advance both one link at a time. In $\mu$ steps, the head cursor reaches entry. The meeting cursor reaches the same node because its meeting displacement from entry is $t-\mu$ modulo $\lambda$, and $t$ is a multiple of $\lambda$. Count cycle length by keeping one cursor at the meeting node and moving another until it returns; the positive number of traversed links is $\lambda$.

<!-- SIM:cycle -->

**Worked example.** With $\mu=5$ and $\lambda=4$, the first meeting is at $t=8$. Slow is three cycle links beyond entry. After resetting one cursor, five one-link advances bring both to entry. Detection used 24 link traversals (one plus two per iteration); entry discovery uses ten more; length discovery uses four. This exact count assumes no extra defensive traversals beyond those specified.

If fast moves $r$ links per iteration, collision requires $(r-1)t\equiv0\pmod\lambda$. Detection can still work, but the standard reset proof needs $t\equiv0\pmod\lambda$, which is no longer forced. For $r=3$, $\mu=1$, $\lambda=4$, meeting occurs at $t=2$; resetting and moving both by one leaves a nonzero modular separation forever. Changing speed changes the proof obligation.

## 10. Traversal patterns and hidden quadratic work

A loop calling `get(i)` on a singly linked list from $i=0$ through $n-1$ performs $0+1+\cdots+(n-1)=n(n-1)/2$ link traversals. A cursor that retains the current node performs only $n-1$ links between successive nodes. Identical logical visits can have different physical costs.

Binary search on a sorted linked list cannot obtain midpoint nodes in constant time. If each iteration calls `get(mid)` from the global head, an unsuccessful search beyond the maximum follows ranks near $n/2,3n/4,7n/8,\ldots$; there are $\Theta(\log n)$ such ranks of order $n$, giving $\Theta(n\log n)$ link work in that implementation. A range-aware implementation that walks from the current range start spends $O(n)$ total midpoint-discovery work because subrange lengths shrink geometrically. Neither establishes the array's logarithmic pointer-work bound. Counting key comparisons alone hides traversal cost.

To find the $k$th node from the end, with $k=1$ meaning last, advance a lead cursor $k$ links, rejecting if too short. Then advance lead and lag together until lead is null. Their distance remains $k$ links, so lag identifies the answer. The lead traverses $n$ links and lag traverses $n-k$, totaling $2n-k$, under the convention that moving last→null counts one link. Cached size allows a single traversal of $n-k$ links instead.

<!-- SIM:traversal -->

For middle finding, the exact initialization and stopping condition determine which of the two central nodes is returned for even length. With slow=head, fast=head, and a loop while fast and fast.next exist, slow lands at index $\lfloor n/2\rfloor$: the second middle for positive even length. State the convention before choosing an option.

## 11. Merge, compaction, rotation, and aliasing

Merge two disjoint sorted acyclic lists by repeatedly taking the smaller head. Taking from the left list on equality preserves stability with respect to the concatenated input order. If lengths are $m,n>0$, the maximum number of head-key comparisons is $m+n-1$; when one list is exhausted, attach its remaining suffix without further key comparisons. Every selected node must be detached safely before its link is repurposed. Shared nodes invalidate the disjointness assumption and may create cycles.

Stable array compaction uses a read cursor and a write cursor. After processing old positions $0$ through $r-1$, the live prefix $A[0..w-1]$ is exactly the retained subsequence of that processed prefix. Always $w\le r$, so writing a retained value at $w$ cannot overwrite an unread future value. If the predicate is tested once per old element, there are $n$ predicate tests and $k$ retained-slot assignments for $k$ survivors. An implementation that skips self-assignments can write fewer slots.

<!-- SIM:mergecompact -->

Left-rotate an acyclic singly linked list by $k$ positions, with $n>0$, after replacing $k$ by $k\bmod n$. If it is zero, do nothing. Otherwise find old rank $k-1$ as new tail, save its successor as new head, connect old tail to old head, and break the new tail's link. With old tail and size cached, finding the cut costs $k-1$ traversals; rewiring is constant. The intermediate temporary cycle must not escape the operation.

**Worked example.** Left-rotating A→B→C→D→E by two yields C→D→E→A→B. Connecting E→A without breaking B→C leaves a cycle. Breaking B→C before saving C loses the new head handle. The operation needs a saved cut successor and a complete postcondition.

Two lists may share an immutable suffix. Pointer identity detects sharing; equal payloads do not. The two-cursor intersection method traverses one list then the other, switching at null. Each cursor walks lengths $m+n$ before termination or alignment, eliminating the unequal-prefix offset. This assumes acyclic lists and no mutation during the run. Destructive concatenation of overlapping lists can create a cycle, so ownership is part of the contract.

<!-- SIM:rotation -->

## 12. Memory, locality, and representation selection

An array needs $Cb$ bytes for backing slots, plus metadata. A linked list with node payload $d$, $p$ pointers of $w$ bytes, and alignment $a$ may need a rounded node size $a\lceil(d+pw)/a\rceil$, before allocator headers. A sentinel adds one node. A cached tail and size add metadata but do not change the number of live elements. Space expressions must state whether they count capacity, live data, peak allocation, or auxiliary storage.

Sequential array access often exploits cache locality, but a locality statement needs a model. For blocks containing $L$ slots and an initial offset $r$ slots into a block, $n>0$ consecutive slots touch $\lceil(r+n)/L\rceil$ blocks. A linked list whose nodes each occupy a distinct uncached block may need $n$ block fetches. A packed or pool-allocated list may do better. Hardware latency, prefetching, and allocator behavior are not fixed by the abstract RAM bound.

**Worked example.** A node has 12 bytes of payload, eight-byte pointers, and eight-byte alignment. A singly linked node rounds 20 bytes to 24; a doubly linked node rounds 28 to 32. For 1000 live nodes plus one sentinel, the respective node-storage totals are 24,024 and 32,032 bytes. A 1024-slot array with 12-byte payloads uses 12,288 slot bytes. Allocator overhead could widen the gap. These are model-specific figures, not universal object sizes.

| Operation and supplied information | Dynamic array | Singly linked list, head/tail/size | Circular doubly linked list |
|---|---|---|---|
| Retrieve or replace rank $i$ | $\Theta(1)$ | $\Theta(i+1)$ time | $\Theta(1+\min(i,n-1-i))$ with both directions |
| Append | Amortized $\Theta(1)$; resize worst $\Theta(n)$ | $\Theta(1)$ | $\Theta(1)$ |
| Stable insertion at rank $i$ | $\Theta(n-i+1)$ plus resizing | Search plus constant rewiring | Search plus constant rewiring |
| Remove known node identity | Rank must be available or found; stable shift | Needs predecessor, except restricted value-copy trick | $\Theta(1)$ unlink |
| Delete last element | Amortized $\Theta(1)$ with safe shrink policy | $\Theta(n)$ without predecessor links | $\Theta(1)$ |
| Full ordered scan | $\Theta(n)$ | $\Theta(n)$ with one cursor | $\Theta(n)$ |

The best representation depends on supplied information and dominant work. An array suits random indexing and compact traversal. A doubly linked list suits many insertions or deletions at valid known handles. A singly linked list can minimize per-node overhead when operations occur after known predecessors. Calling any one representation universally superior discards the workload.

## 13. Sparse-matrix bridge and structured representations

For a sparse matrix, a node can store row, column, value, a right link within its row, and a down link within its column. Row and column headers form an orthogonal linked representation. Its purpose is to expose both row and column traversals. A list of row lists naturally exposes rows but needs extra work to retrieve columns. One circular list alone does not organize two independent adjacency relations.

An outer product $C=ab^T$ has entries $C_{ij}=a_i b_j$. Over the real numbers, its support has size $\operatorname{nnz}(a)\operatorname{nnz}(b)$ because a product is nonzero precisely when both factors are nonzero. If one factor is zero, the matrix is zero. A factorized representation stores two vectors in $O(m+n)$ space and computes a requested entry in constant time, but may not satisfy a question demanding a general mutable sparse-matrix representation with row and column operations. General addition can destroy rank-one form.

<!-- SIM:sparse -->

**Worked example.** With $a=(2,0,3)$ and $b=(0,5,7,0)$, the nonzero coordinates are $(0,1),(0,2),(2,1),(2,2)$, with values 10, 14, 15, 21. There are four nodes in an explicit sparse representation; factorization stores seven scalar slots. If two arbitrary matrix objects must support independent row and column traversal and changing dimensions, orthogonal links meet a different requirement from factorization. Examine the requested operations before exploiting algebraic structure.

## 14. Complete chapter summary

The abstract sequence operation does not determine its implementation cost. Direct array indexing uses address arithmetic; linked indexing uses traversal. Stable array insertion at rank $i$ shifts $n-i$ old elements; deletion shifts $n-i-1$. Direction matters because updates overwrite storage. Unordered deletion has a different contract and can avoid shifts.

Geometric growth gives linear total copying for a fixed factor greater than one, so append is amortized constant while individual resize appends remain linear. Additive growth by a fixed amount gives quadratic total copying. Hysteresis separates growth and shrink thresholds. The quarter-full policy can be proved with a nonnegative piecewise potential. These conclusions concern capacity management and do not erase middle-insertion shifts.

Known locations and searched locations are different inputs. A singly linked insertion after a known predecessor is constant-time rewiring; tail removal still needs a predecessor. Circular doubly linked sentinels eliminate empty-end null cases and permit constant unlinking of known nodes. Splice rewiring can be constant even when maintaining unknown range lengths requires traversal. Ownership, node identity, payload copying, and allocator work must be counted under the stated contract.

Iterative reversal maintains disjoint reversed and untouched regions and writes each successor once. Floyd's one-versus-two speed proof uses modular arithmetic; its reset phase cannot be transferred blindly to other speeds. A retained traversal cursor prevents the quadratic work of repeated indexed list access. Merge and compaction require ordering and non-overwrite invariants, respectively. Matrix, cache, and memory questions require their own concrete models.

## 15. Worked examination and course-derived problems

The bank combines two archive items rechecked against their original rendered pages with original mathematical and conceptual problems and independently reconstructed course exercise families. Answers are derived here; no answer is represented as an official examination key. Difficulty labels are author assessments, not calibrated score predictions. Each worked solution identifies the relevant assumptions and explains why a tempting shortcut fails.

<!-- INCLUDE:problems -->

## 16. Examination rules and traps

Use these as a final retrieval sheet after reading the derivations. Each rule provides a trigger, a condition, a worked consequence, and a trap. They supplement the lesson rather than replacing its proofs.

<!-- INCLUDE:review -->

## 17. Editable laboratories and their limits

The laboratory recomputes actual array writes, resize counts, linked-list reversal, or Floyd pointer positions from bounded user-selected parameters. Its result is a finite instance, not a proof of an asymptotic theorem. The surrounding models preserve node identities and expose exact checkpoints. They start paused and support forward/backward steps, restart, speed selection, seeking, reduced motion, and printable complete traces.

<!-- LAB:arrays -->

## 18. References and provenance

1. Massachusetts Institute of Technology. Erik Demaine, Jason Ku, Justin Solomon. *6.006 Introduction to Algorithms*, Spring 2020. [Recitation 2: Data Structures](https://live.ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/c08a3b63dfe5f6f6b32257d35f86ae63_MIT6_006S20_r02.pdf), pages 1–9. The accessible browser PDF was reviewed; the separate local download timed out.
2. University of California, Berkeley. *CS61B Textbook*. [Chapter 4: SLLists](https://cs61b-2.gitbook.io/cs61b-textbook/4.-sllists) and [Chapter 5: DLLists](https://cs61b-2.gitbook.io/cs61b-textbook/5.-dllists). Used for list design and invariants; the course index was screened separately and is not counted as instructional reading.
3. University of Oxford. Andrea Vedaldi. *B16 Algorithms and Data Structures 1*, 2024. [Chapter 3: Elementary Data Structures](https://www.robots.ox.ac.uk/~vedaldi/assets/teach/2024/b16/notes/3-elementary-data-structures.html), §§3.1, 3.2, 3.5.
4. Princeton University. Robert Sedgewick and Kevin Wayne. *COS226 Algorithms and Data Structures*, Spring 2026. [Stacks and Queues I](https://www.cs.princeton.edu/courses/archive/spring26/cos226/lectures/13StacksAndQueuesI.pdf), primarily PDF pages 21–34. Stack and queue interfaces are deferred; backing-array resizing arguments are used here.
5. Stanford University. Julie Zelenski. *CS106B Programming Abstractions*, Handout 21, February 4, 2008. [Linked List Code](https://see.stanford.edu/materials/icspacs106b/H21-LinkedListCode.pdf), pages 1–4. Historical code is independently reconstructed; duplicate policy and ownership must be stated explicitly.
6. Cornell University. *CS2110*, Fall 2025. [Lecture 13: Linked Lists](https://www.cs.cornell.edu/courses/cs2110/2025fa/lectures/lec13/). Only the selected representation-invariant and circular-list sections recorded in the source audit are counted as reviewed.
7. *PhD Computer Science and Engineering Entrance Examination 1405*, booklet 707A, question 18, physical PDF page 5. Original archive path and immutable commit are linked beside the problem. Its selection answer is independently reasoned under the stated general-matrix requirements.
8. *MS Computer Science Entrance Examination 1393*, booklet 370E, question 167, physical PDF page 34. This is an explicitly labeled bridge revisit, with pseudocode assessed as an algorithm rather than compilable C declarations.

The lesson's prose, proofs, numerical examples, diagrams, and original problem statements were independently written. Course-family reconstructions carry provenance; they do not reproduce entire copyrighted exercise collections. The audit discloses inaccessible material and implementation-dependent assumptions. No assertion of complete worldwide source coverage or guaranteed examination performance is made.
