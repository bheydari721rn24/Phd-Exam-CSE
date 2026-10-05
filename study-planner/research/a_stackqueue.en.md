# Stacks, Queues, and Applications

## 1. Sources and the chapter map

This chapter builds on arrays, linked lists, elementary loop invariants, and amortized analysis. Its main question is precise: how does restricting access to the ends of a sequence change correctness, cost, and the algorithms that become possible? We study both the abstract access rule and the concrete storage that implements it. A priority queue removes an item according to a key rather than arrival order and belongs to a later chapter.

Four primary written courses were genuinely reviewed and selected from a documented seven-university candidate pool. Princeton COS226 supplies representation and cost analysis; Oxford B16 supplies explicit storage conventions; CMU 15-122 supplies interface contracts and client restoration; Stanford CS106B supplies expression processing and changing-container pitfalls. MIT's sequence-end problems and Berkeley's sentinel design provide complementary checks. See the [source-selection and reading audit](../reviews/a_stackqueue-sources.html) for the exact scopes, candidates, source inconsistencies, and limits.

| Primary course | Instructor or authors | Material used |
|---|---|---|
| Princeton COS226, Spring 2026 | Robert Sedgewick and Kevin Wayne | Stacks and Queues I, complete 45-page deck |
| Oxford B16, 2024 | Andrea Vedaldi | Chapter 3, Sections 3.3, 3.4, and linked-list representation passages |
| Carnegie Mellon 15-122, Spring 2026 | Frank Pfenning, Andre Platzer, Rob Simmons | Lecture 9, pages 1-19, including six exercise themes |
| Stanford CS106B, Spring 2017 | Chris Gregg | Lecture 5, complete deck; technical instruction in pages 8-29 and 33-45 |

The chapter develops implementations, representation proofs, two-stack amortization, restoration and aliasing, stack permutations, Catalan counting, typed brackets, postfix/prefix evaluation, infix conversion, minimum/maximum augmentation, associative aggregates, monotone structures, histogram rectangles, worklist boundaries, and round-robin elimination. The solved bank contains authentic archive questions, independent course reconstructions, and new medium-to-hard mathematical/conceptual problems. Every visual identifies its inputs and invariant; a finite animation illustrates a proof rather than replacing it.

## 2. Abstract operations, orientation, and legal histories

Write a stack as $S=(s_0,s_1,\ldots,s_{n-1})$ from **bottom to top**. `push(x)` changes it to $(s_0,\ldots,s_{n-1},x)$. `pop()` requires $n>0$, returns $s_{n-1}$, and removes that item. `top()` returns the same item without changing the sequence. Write a queue $Q=(q_0,\ldots,q_{n-1})$ from **front to rear**. `enqueue(x)` appends x; `dequeue()` requires $n>0$, returns $q_0$, and removes it. `front()` observes $q_0$. These rules specify behavior; they do not identify an array or list.

A legal operation history never removes from an empty structure. If $P_t$ insertions and $D_t$ removals have occurred through prefix t from an initially empty structure, occupancy is $P_t-D_t$. For capacity C, every prefix must satisfy

$$0\le P_t-D_t\le C.$$

Final occupancy alone is insufficient. The history pop, push has final occupancy zero but is illegal at its first operation. The minimum required capacity for a legal history is its maximum prefix occupancy. Underflow and overflow should be rejected before changing storage or counters; an unsuccessful operation must have a specified effect. This chapter's bounded laboratory rejects it and retains the state.

Cost uses a word-RAM model: one valid pointer access, one word-sized payload transfer, and one index update take constant time. When exact counts are requested, the question states which primitive is charged. Copying a variable-size object, allocating memory, evaluating arbitrary-precision arithmetic, or running a destructor can cost more. All algorithms here have exclusive access unless explicitly discussing the concurrency boundary.

<!-- SIM:order -->

**Worked contrast.** Insert 4, 7, 9, remove once, insert 2, then remove twice. Stack outputs are 9, 2, 7 and its surviving bottom is 4. Queue outputs are 4, 7, 9 and its survivor is 2. Both have identical occupancy history and minimum capacity three. Occupancy does not identify removal order.

## 3. Fixed array stacks and two stacks sharing storage

For an array stack, use `n` as the **next unused slot**, not the occupied top index. The invariant is $0\le n\le C$, with exactly the live logical sequence in $A[0..n-1]$. Empty means $n=0$; top, when present, is $A[n-1]$.

```text
push(x):
    require n < C
    A[n] = x
    n = n + 1

pop():
    require n > 0
    n = n - 1
    x = A[n]
    A[n] = empty_slot       // release retained reference if required
    return x
```

Push writes exactly the first unused slot and extends the represented sequence by x. Pop shortens it and reads the former last live slot. Induction over a legal history proves LIFO behavior. Clearing a reference slot affects object retention but is not the abstract removal itself. In languages with value objects, reducing a counter without invoking required destruction may violate the object-lifetime contract; pseudocode is not a complete C++ ownership implementation.

If another problem uses occupied top index t, its invariant is $-1\le t<C$ and $n=t+1$. Push increments t before using $A[t]$; pop uses $A[t]$ before decrementing. Mixing these two conventions creates an off-by-one fault even when the underlying concept is correct.

Two stacks can share an array of C slots. Let left top $\ell=-1$ and right top $r=C$ initially. Left push decrements the free interval by increasing $\ell$; right push decreases r. Occupancy is $(\ell+1)+(C-r)$ and available space is $r-\ell-1$. Shared overflow occurs exactly when $\ell+1=r$. Their independent empty tests are $\ell=-1$ and $r=C$. If one stack is nearly empty, the other can use the spare space. A fixed midpoint partition wastes this flexibility.

<!-- SIM:shared -->

**Worked example.** With C=12, left top 3 and right top 9, left has four items, right has three, and slots 4 through 8 are free. Five more combined pushes fit, regardless of which stack receives them. With word size eight bytes, the slot array uses 96 bytes before metadata and alignment.

## 4. Linked stacks, linked queues, and deque invariants

A singly linked stack keeps its top at the head. Each node has a payload and successor; head is null iff empty. To push, allocate and initialize a new node with `next = head`, then set head to it. To pop, save head and its payload, advance head to the saved successor, then release the detached node. Each operation rewrites a constant number of fields, provided allocation and payload handling meet the model. Keeping the top at the tail of a singly linked list makes repeated pop require finding the predecessor, normally linear time.

A singly linked FIFO queue stores head and tail. For a nonempty queue, head is the oldest node, tail is the newest, and `tail.next = null`. Empty requires **both** head and tail null. Enqueue allocates a node with null successor; if empty set both handles to it, otherwise set `tail.next` to it and advance tail. Dequeue advances head; if head becomes null also clear tail. Leaving tail pointing to a freed singleton node breaks the next enqueue.

```text
dequeue_linked():
    require head != null
    victim = head
    x = victim.value
    head = victim.next
    if head == null:
        tail = null
    release victim
    size = size - 1
    return x
```

A doubly linked deque supports insertion and removal at **both** ends. With a circular sentinel s, empty means `s.next = s` and `s.prev = s`. Insert x between a and b where `a.next=b` and `b.prev=a`: set x.prev=a, x.next=b, a.next=x, b.prev=x. Removal reconnects its two neighbors and then releases x. The forward/backward invariants are mutual: for every linked node v, `v.next.prev=v` and `v.prev.next=v`. End handles or a sentinel are required for constant-time endpoint access; a bare node somewhere in a list does not give both ends.

<!-- SIM:linked -->

The exact field-write count depends on whether node initialization, sentinel fields, size metadata, and reference clearing are counted. Complexity is constant because those counts are bounded, not because every implementation performs the same number of writes. The authentic PhD deque question in the bank tests this representation argument.

## 5. Circular queues: front/count and reserved-slot conventions

A ring buffer reuses physical slots without shifting survivors. Use capacity $C\ge1$, front index $f\in\{0,\ldots,C-1\}$, and live count $0\le n\le C$. Logical item j is in physical slot $(f+j)\bmod C$ for $0\le j<n$. The next enqueue slot is $r=(f+n)\bmod C$. Empty means n=0; full means n=C. The same equality r=f occurs in both cases, so the count carries essential information.

```text
enqueue_ring(x):
    require n < C
    A[(f + n) mod C] = x
    n = n + 1

dequeue_ring():
    require n > 0
    x = A[f]
    A[f] = empty_slot
    f = (f + 1) mod C
    n = n - 1
    return x
```

For enqueue, the old j positions remain unchanged, while the new logical position n maps to a previously free slot. For dequeue, the new item j maps to $(f+1+j)\bmod C$, exactly the old item j+1. This proves FIFO by induction even when physical addresses wrap. No geometric circle is required in memory: modular addressing supplies the circular behavior.

**Worked example.** Capacity seven, front five, count four occupies slots 5, 6, 0, 1 in that logical order. Next enqueue uses slot 2. After two dequeues, front becomes zero and count becomes two. Both the ordering and count are necessary to interpret storage.

<!-- SIM:ring -->

An alternative stores f as next removal and r as next insertion, reserving one slot. Empty is f=r; full is $(r+1)\bmod C=f$. Occupancy is $(r-f+C)\bmod C$, constrained to $0..C-1$. A C-slot buffer now holds only C−1 live items. Distinguishing full from empty using a count or separate phase bit can recover all C slots, but then it is a different representation. Capacity one in the reserved-slot convention holds zero items.

Oxford's course uses a backward-growing convention: i is the next rear insertion slot; after inserting, i decreases modulo C, and the front slot for n live items is $(i+n)\bmod C$. It remains FIFO because each new value is placed on the opposite end. The formula $(f+n)\bmod C$ from our forward convention cannot be attached to Oxford's i without translating meanings. In C-like languages, negative remainder may be negative; use `(i + C - 1) % C` for a decrement rather than assuming `(-1) % C = C-1`. Bit masking by C−1 equals nonnegative modulo C only when C is a power of two.

## 6. Circular resizing, shrinking, and worst-case latency

If a count-based buffer is full, allocate a larger buffer and copy **logical** item j from $A[(f+j)\bmod C]$ to new slot j. Set front to zero and retain live count; under a separate rear counter, set rear to n modulo new capacity. Copying raw physical slots in ascending order preserves memory order but can scramble FIFO order. After relocation, old interior pointers may be invalid.

**Worked example.** Old capacity five, front three, full logical sequence `(A,B,C,D,E)` occupies physical slots `(C,D,E,A,B)`. Copy slots 3,4,0,1,2 to new positions 0..4. The result `(A,B,C,D,E)` has front zero and enqueue slot five in a capacity-ten buffer. Copying physical slots 0..4 gives a wrong queue despite containing the correct set of values.

Geometric growth makes aggregate relocation work linear over an update sequence. Doubling from capacity one under append-only arrivals copies $1+2+4+\cdots$; after m enqueues, copy writes equal $2^{\lceil\log_2 m\rceil}-1$. Include m new-value writes only if requested. A single resize can remain linear. If removing items shrinks capacity immediately at half occupancy, alternating insertion/removal can trigger costly grow/shrink pairs. Shrinking only at quarter occupancy restores a gap between thresholds.

The potential from the arrays chapter applies to count n and capacity C independent of the front index:

$$\Phi(n,C)=\begin{cases}2n-C,&n\ge C/2,\\C/2-n,&n<C/2.\end{cases}$$

Charge one unit for the basic update and one per relocated item. Nonresizing insertion has amortized cost at most three; nonresizing removal at most two. A growth insertion from full C costs C+1 and drops potential from C to 2, giving three. A quarter-triggered shrink removal starts with length C/4+1 and ends with length C/4, capacity C/2; cost 1+C/4 and potential change −(C/4−1) give two. Minimum capacity and small integer thresholds are handled separately. The proof uses exact power-of-two capacities and equality thresholds, not unstated floating thresholds. Allocation zero-fill or payload deep copying must be incorporated if charged.

<!-- SIM:resize -->

Amortized constant time is a worst-case bound on the total legal sequence, not a probability statement and not a guarantee that every operation meets a deadline. A persistent queue can revisit earlier versions and repeat transfers; the ordinary destructive proof does not automatically apply across the branching history. A real-time queue needs an incremental scheduling invariant, which is outside this chapter's implementations.

## 7. A queue built from two stacks: order and exact amortization

Use input stack I and output stack O, each written bottom-to-top. Enqueue pushes to I. Dequeue uses the top of O. **Only if O is empty**, move every item from I to O by repeated pop/push, then pop O. Empty means both stacks empty. The logical queue is

$$Q=\operatorname{reverse}(O)\,\Vert\,I.$$

The symbol $\Vert$ means concatenation. O reversed gives its top-to-bottom removal order; I in bottom-to-top order gives subsequent arrivals. Enqueue appends to the right side. If O is nonempty, popping its top removes the first logical item. If O is empty, transfer reverses I's physical stack order, putting the oldest arrival on O's top; the queue sequence stays unchanged during the complete transfer. Half-finished transfers need an explicit intermediate-state convention and must not be presented as public completed states.

```text
dequeue_two_stacks():
    require not empty(I) or not empty(O)
    if empty(O):
        while not empty(I):
            push(O, pop(I))
    return pop(O)
```

For e enqueues, d successful dequeues, and t transferred items, primitive push/pop cost is exactly

$$T=e+2t+d,\qquad 0\le t\le e.$$

Every item enters I once, moves to O at most once, and is removed at most once, so $T\le3e+d$. If all e items are eventually removed, T=4e. A single dequeue that transfers k pending items costs 2k+1. Define $\Phi=2|I|$. Enqueue costs one and raises potential by two, for amortized cost three. A dequeue without transfer costs one and leaves potential unchanged. A transfer/dequeue costs 2k+1 and lowers potential by 2k, for amortized cost one. Since the initially empty potential is zero and remains nonnegative, telescoping proves the sequence bound.

<!-- SIM:two -->

**Failure case.** Enqueue A,B, dequeue A, enqueue C. O still has B. Moving C into nonempty O puts C above B and makes the next dequeue return C, violating FIFO. Cheap transfers in the wrong place do not implement the interface. `front()` can similarly trigger one complete transfer but must not pop its final item. Repeated front calls after the transfer cost constant each.

## 8. Implementing a stack with queues and preserving client data

A stack can use queues by making either insertion or removal expensive. In a single-queue expensive-push version, enqueue the new x, then rotate exactly the old n items from front to rear. The new item becomes front and pop is one dequeue. Push costs n+1 enqueues and n dequeues, totaling 2n+1 primitive queue operations; pop costs one. Building n items from empty costs $\sum_{j=0}^{n-1}(2j+1)=n^2$. In an expensive-pop version, keep arrival order and rotate n−1 items before removing the last; push costs one, pop costs 2n−1. Removing all n items then costs n². Two queues can transfer survivors and exchange handles with the same linear expensive operation. These tradeoffs do not inherit the two-stack queue's constant amortization.

Client algorithms must restore order as well as item count. To measure a stack's size using only push/pop/empty, move S to temporary T, count removals, then move T back. Two reversals restore S; four primitive operations per original item give 4n transfers and linear time. A recursive version pops one x, recurses on the rest, then restores x on return. It uses 2n data-stack operations and n+1 simultaneous calls including the empty base invocation, hence linear auxiliary call space.

To create an independent **container** copy of S, first reverse into T, then pop T and push each value into both S and the copy. It needs 5n primitive push/pop operations. Copying during the first reversal gives the copied stack the opposite order. Shared payload references still alias payload objects: container independence is not deep object independence. `C=S` can be a mere handle alias, depending on language and declared copy semantics.

For a queue with available size n, a fixed n iterations of dequeue, observe/copy, and reenqueue preserves its order. Without size, use a temporary queue to drain and restore rather than waiting for a nonempty queue to become empty while reenqueuing every item. If a loop tests `i < Q.size()` while removing one item each iteration, after i removals it tests i<n−i. It executes $\lceil n/2\rceil$ times, not n. Saving the original bound separates traversal from mutation.

<!-- SIM:restore -->

## 9. Legal stack permutations and the 312 obstruction

Push distinct inputs $1,2,\ldots,n$ in that order, with arbitrary legal interleaving of pops. Not every output permutation is possible. To validate a target, maintain the next unused input a and a stack. For desired x, if x is already on top, pop it. Otherwise push consecutive unused inputs until x is pushed, then pop x. If all inputs up to x have already been pushed and x is below a different top, reject.

Why is this greedy test complete? Any realization must have pushed every earlier input before x. A top equal to the next desired output must be removed before any other pop can match the target. If a larger covering item must be popped to expose x, that would output the wrong next value. The forced push/pop steps therefore either reproduce a valid realization or prove none exists. Each input is pushed/popped once; validation is linear with linear worst-case stack space. With a capacity limit h, additionally reject a forced push that would exceed h. The maximum occupancy of the successful greedy trace is the minimum capacity for this target, because those pending items were forced.

<!-- SIM:permutation -->

**Worked example.** Target `(3,2,1,5,4)` is produced by push1,push2,push3,pop3,pop2,pop1,push4,push5,pop5,pop4. Peak is three. Target `(3,1,2)` fails: after removing 3, 2 covers 1 and cannot be removed before 1 without changing the requested order.

For these fixed increasing inputs, a possible output avoids the pattern **312**: there cannot be positions i<j<k with output values $p_i>p_k>p_j$. After the largest $p_i$ was pushed and output, the intermediate $p_k$ lies above the smallest $p_j$ and must leave first. Conversely, a greedy failure on requested x has a covering y>x that has already been pushed. Because y was pushed but not output, some previously output z>y caused the input stream to advance past y while x remained pending. Thus the target contains z,x,y, a 312 pattern. This proves both directions. Pattern 231 is often quoted for the inverse sorting convention; do not import it without checking which permutation is input and which is output.

Duplicates require distinct occurrence identities or a carefully specified matching rule; the distinct-permutation theorem does not count duplicate-value outputs. Reversing all inputs needs capacity n, while outputting each input immediately needs capacity one.

## 10. Catalan counting, prefix constraints, and bounded capacity

With n pushes and n pops, encode push as an up step and pop as a down step. A legal complete history has n of each, never goes below height zero, and returns to zero. These are Dyck paths. With fixed distinct increasing inputs, each path determines a unique output permutation, and the forced greedy realization shows the converse. Therefore histories and realizable outputs have the same count.

There are $\binom{2n}{n}$ balanced words without prefix restriction. For each bad word, reflect its prefix through the first height −1. This exchanges one excess down step with an up step, mapping bijectively to words with n+1 up and n−1 down steps. Bad words count $\binom{2n}{n-1}$. Thus

$$C_n=\binom{2n}{n}-\binom{2n}{n-1}=\frac{1}{n+1}\binom{2n}{n}.$$

The first-return decomposition gives $C_0=1$ and $C_n=\sum_{j=0}^{n-1}C_jC_{n-1-j}$. A nonempty path consists of an opening push, a legal interior of j pairs, its matching pop, and a remaining legal suffix. This is a structural proof, not simply a remembered formula. For n=4, the count is 14, whereas unrestricted permutations number 24.

For bounded capacity h, define D(p,d) as the number of histories with p pushes and d pops performed, subject to $0\le d\le p\le n$ and $p-d\le h$. Start D(0,0)=1. Push adds to D(p+1,d) when p<n and p−d<h; pop adds to D(p,d+1) when d<p. Then D(n,n) is the count. This lattice recurrence handles overflow and underflow together. For n=3,h=2, it gives four; the excluded fifth path pushes all three before popping. Capacity one has one path; capacity at least n gives Cn. Exact maximum height h is the difference between bounds h and h−1.

<!-- SIM:catalan -->

The bounded recurrence can be implemented without enumerating output permutations:

```text
count_histories(n, h):
    require n >= 0 and h >= 0
    D = (n+1)-by-(n+1) array of zeros
    D[0][0] = 1
    for total = 0 to 2*n:
        for p = 0 to n:
            d = total - p
            if d < 0 or d > p or d > n or p-d > h:
                continue
            if p < n and p-d < h:
                D[p+1][d] += D[p][d]
            if d < p:
                D[p][d+1] += D[p][d]
    return D[n][n]
```

Processing by total steps ensures each transition goes to a strictly later layer, so no contribution is used before its predecessors are accumulated. Each legal history has a unique last step; its predecessor is counted exactly once, establishing the recurrence by induction. There are quadratically many possible lattice cells and constant-many outgoing transitions per cell, so the table uses quadratic arithmetic operations and quadratic storage. Counts grow beyond fixed machine words; big-integer addition cost must be included for a bit-complexity claim. A layer-based implementation can retain only the previous and current layers, reducing working count storage to linear size. At n=0 there is one empty history, even with capacity zero; at n>0,h=0 there are no complete histories. These cases should be derived from the initialization, not patched by an incorrect blanket zero rule.

With p pushes and d pops, p≥d, but an unfinished legal history, the ballot count is $\binom{p+d}{d}-\binom{p+d}{d-1}$. A stack of typed opening brackets needs identities as well as height; height alone proves single-type balance, not nesting correctness for mixed types.

## 11. Bracket matching, continuations, and explicit traversal

For bracket tokens only, push each opening delimiter. On a closing delimiter, require a nonempty stack and a top with the matching type; then pop. At end require empty. The invariant is that the stack contains exactly the unmatched openings of the processed prefix, oldest at bottom. The next closing delimiter must match the most recent unmatched opening because properly nested pairs cannot cross. A mismatch such as `([)]` has balanced counts but fails at its third token. Worst-case time is linear in token count and auxiliary space is the largest nesting depth. Lexical preprocessing must distinguish comments and quoted strings if parsing actual source code; bracket characters inside strings are not necessarily delimiters.

<!-- SIM:brackets -->

A function-call stack stores unfinished continuations, not merely argument values. In recursive depth-first traversal, a frame may contain a node, local variables, and which child or statement comes next. An explicit stack that stores only nodes may reproduce preorder but not postorder. For postorder use `(node,visited)` or a `(node,nextChild)` frame: delay the node's final processing until its children have completed. Recursion depth measures simultaneous frames, while total calls measure all invocations; they are generally different.

For a binary tree, iterative preorder that pushes right child before left visits left first because of LIFO. Reversing push order reverses sibling visitation. A FIFO worklist processes discovered vertices by distance layers, provided vertices are marked when enqueued so duplicates do not multiply pending entries. The dedicated graph-search chapters cover graph-level proofs and complexity; here the purpose is to distinguish the worklist discipline.

## 12. Postfix, prefix, and expression-stack validity

Tokens, not characters, are the unit: 12 is one operand and −3 can be a signed literal if the grammar says so. For binary postfix evaluation, scan left to right. Push an operand. For an operator, require at least two values, pop **right** operand b, then **left** operand a, and push a op b. End requires exactly one value. Division by zero and arithmetic overflow need explicit policies. The invariant is that the stack holds values of completed subexpressions waiting to be combined, in left-to-right order. An operator replaces the last two completed subexpressions with their correctly ordered result.

**Worked example.** `18 6 3 / - 4 *` creates stacks `(18)`, `(18,6)`, `(18,6,3)`, `(18,2)`, `(16)`, `(16,4)`, `(64)`. Reversing either division or subtraction operands gives a different result. The complete trace is embedded below.

<!-- SIM:postfix -->

```text
evaluate_postfix(tokens):
    S = empty value stack
    for token in tokens:
        if token is a valid operand:
            push(S, decode(token))
        else if token is a supported binary operator:
            require size(S) >= 2
            right = pop(S)
            left = pop(S)
            require apply(token, left, right) is defined
            push(S, apply(token, left, right))
        else:
            reject token
    require size(S) == 1
    return pop(S)
```

The loop invariant is stronger than a count: from bottom to top, the value stack contains the evaluated, not-yet-combined subexpressions of the scanned postfix prefix in their left-to-right order. Reading an operand appends a new completed leaf. A binary operator combines exactly the last two such subexpressions; removing them and appending their result preserves the invariant. If two are unavailable, no valid parse of that prefix exists. At termination, one value proves that all fragments combine into one expression; an empty or multi-value stack does not. Separating token decoding from operators distinguishes a signed literal such as `-3` from the binary token `-`. The laboratory normalizes rational fractions after every operation; this gives exact values while imposing an explicit digit bound on its editable input display.

If all operators are binary, n operands require n−1 operators. This total count is necessary but insufficient: before each operator at least two values must be available. Occupancy after a prefix is operands minus operators. At every operator position the post-operation occupancy must be at least one; final occupancy must be one. Thus `2 + 3` has plausible totals but underflows early, and `2 3` has an extra final value. For an operator of arity k, require k values and replace them with one; occupancy changes by 1−k. An arity-zero constant behaves as an operand.

For prefix, scan right to left. On an operator, the **first** pop is its left operand and the second pop its right. This is the opposite pop interpretation from postfix because the scanning direction is reversed. A stack of expression strings can convert postfix to fully parenthesized infix: pop b then a and push `(a op b)`. It preserves tree shape; it does not justify arbitrary algebraic reassociation. Naive immutable string concatenation can make text conversion quadratic even when token-stack actions are linear; constructing an expression tree and emitting it once avoids this cost.

## 13. Infix conversion: precedence, associativity, and unary operators

Use an output list and an operator stack. An operand goes directly to output. An opening parenthesis is pushed. A closing parenthesis pops operators until a matching opening parenthesis, which is removed but not emitted. For incoming operator o, repeatedly pop top operator t while t has greater precedence, or equal precedence and o is **left-associative**. Then push o. At end emit remaining operators and reject any unmatched delimiter.

The invariant is that output is a completed postfix prefix, while stacked operators await a not-yet-completed right operand or a parenthesis boundary. Popping a higher-precedence operation completes it before a weaker operation can combine the result. Popping on equal precedence implements left grouping; retaining an equal-precedence top for a right-associative incoming operator implements right grouping.

**Worked examples.** `a-b-c` becomes `a b - c -`, representing `(a-b)-c`. With right-associative exponentiation, `a^b^c` becomes `a b c ^ ^`, representing `a^(b^c)`. For `a+b*c-d/e`, output is `a b c * + d e / -`. Each operator is pushed and popped once, giving linear token actions. Precedence tables and associativity are grammar inputs, not universal language facts.

<!-- SIM:infix -->

Unary minus requires its own token such as NEG, arity one, and a declared precedence relative to exponentiation. If exponentiation binds more tightly, `-2^2` means `-(2^2)=-4`; `(-2)^2=4`. Treating every '-' as binary underflows at the beginning of an expression. Function calls with commas and varying arity need argument-count state. The chapter's laboratory evaluates explicit postfix tokens and avoids pretending that a small tokenizer is a full programming-language parser.

## 14. Minimum/maximum stacks and associative queue aggregates

To support maximum in constant time with pop, store with each data entry its **prefix maximum**. On push x, store `(x,max(x,oldMaximum))`; on pop remove the complete pair. The remaining top's cached maximum belongs to the surviving prefix, so no rescan is needed. Empty maximum is undefined unless a contract chooses a separate identity/sentinel. The proof is induction: the cached aggregate for a new prefix is the aggregate of its predecessor and x; removing the last prefix exposes the previously correct aggregate. Space is linear and operations constant under constant-time key comparison. A single global maximum fails when the current maximum is popped.

An auxiliary extrema stack may instead push x when x≥current max and pop its top whenever the removed data value equals it. Equality matters: if duplicate maxima are not counted, removing one equal value can discard the maximum of a still-live copy. A pair `(maximum,multiplicity)` is another correct solution. The authentic PhD max-stack item tests this exact restoration property.

<!-- SIM:extrema -->

More generally, an associative operation $\circ$ with identity e defines a monoid. A queue aggregate can use the two-stack queue. Cache in I the bottom-to-top fold, updating $A_I\leftarrow A_I\circ x$ on push. Cache in O the top-to-bottom fold, updating $A_O\leftarrow x\circ A_O$ during transfer pushes. The total queue aggregate is $A_O\circ A_I$. Associativity permits grouping but not reordering; commutativity is unnecessary. String concatenation illustrates direction: O removing order `(a,b)` and pending I `(c,d)` must aggregate `abcd`, not `bacd` or `cdab`.

Min, max, sum, and gcd are common constant-word aggregates, with appropriate empty identities and value domains. String concatenation is a conceptual noncommutative example, not a constant-time fixed-size aggregate when copying growing strings. Inverse-free operations such as minimum cannot generally be updated after arbitrary removal by subtracting the removed value; stored prefix aggregates solve this restricted endpoint case.

## 15. Monotone stacks, next greater values, and histogram widths

For the next **strictly greater** element to the right, scan indices left to right with a stack of unresolved indices. Before pushing index i, while the stack is nonempty and $A[i]>A[\operatorname{top}(S)]$, pop j and record i as j's answer. Store indices because distance and identity matter; values alone lose position information. The invariant is that stack indices increase in time while their values are nonincreasing. A popped j had no greater element between j and i; otherwise it would already have been popped. Therefore i is the first greater position. Every index is pushed once and popped at most once, so a nested while still has linear aggregate time. Unresolved indices at end have no greater element.

<!-- SIM:monostack -->

```text
next_strictly_greater(A):
    answer = array of none
    S = empty stack of indices
    for i = 0 to length(A)-1:
        while not empty(S) and A[top(S)] < A[i]:
            j = pop(S)
            answer[j] = i
        push(S, i)
    return answer
```

After each completed iteration, every stored j has no strictly greater item among the scanned positions after j. The pending values are nonincreasing, so all candidates smaller than the incoming value are a suffix of the stack; a pop loop can reach every one without disturbing a larger blocker. An index popped at i receives its earliest possible answer because the invariant excludes earlier greater values. An index left at termination has no answer. A potential equal to stack length makes each successful pop release one unit, while each new index supplies one: the entire scan performs exactly n pushes and at most n pops. For the nearest greater value to the **left**, query the incoming element against a stack of earlier candidates and discard values that cannot qualify; that is a different direction and invariant. Reversing only the output array does not transform the right-neighbor problem into the left-neighbor problem.

**Worked example.** For `[2,1,2,4,3]`, next-greater zero-based indices are `[3,2,3,none,none]`, and distances are `[3,1,1,none,none]`. The second 2 does not resolve the first 2 because greater is strict. Switching `>` to `>=` changes the question and tie invariant.

For histogram maximum rectangles with unit-width nonnegative bars, maintain indices of nondecreasing heights. On a smaller current height, pop j. Its right exclusive boundary is i; after popping, the previous stack top k is the left blocking boundary under this tie policy, or −1 if absent. Width is $i-k-1$, and area is $A[j](i-k-1)$. Equal heights can remain and be popped separately; the earliest equal bar eventually obtains the widest range. Append a zero sentinel and finally flush any residual zero bars if an explicit complete empty state is desired. The maximum area is independent of a consistent alternative tie policy that replaces equal bars and retains the earliest left boundary.

**Worked example.** `[2,1,5,6,2,3]` has maximum area 10, from height five over indices 2..3. Height six over one bar gives six. The height-one rectangle spans all six bars and has area six. Using width i−j alone misses the left expansion after shorter intervening bars were removed.

<!-- SIM:histogram -->

```text
largest_rectangle(A):
    require every height is nonnegative
    S = empty stack of indices
    best = 0
    for i = 0 to length(A):
        current = A[i] if i < length(A) else 0
        while not empty(S) and A[top(S)] > current:
            j = pop(S)
            left = top(S) if not empty(S) else -1
            best = max(best, A[j] * (i-left-1))
        if i < length(A):
            push(S, i)
    return best
```

Why does testing these popped heights suffice? Take any maximal positive rectangle and choose a bar of minimum height within it. Its height can extend until a shorter bar blocks it on each side. The stack eventually pops a representative of that minimum-height plateau when its right shorter boundary appears, including the virtual final zero. Earlier equal bars are popped after later equal bars, so one receives the whole plateau span. That candidate has at least the original rectangle's area; it cannot cross a shorter blocking height. Consequently the maximum among these candidates equals the optimum among all intervals. The remaining zero bars need no positive-area test. Empty input returns zero. For non-unit bar widths, replace index difference by a difference of prefix sums of widths; the unit-width area formula would otherwise be dimensionally incorrect. Negative heights are outside the histogram contract rather than an extra ordinary case.

## 16. Monotone deques and sliding-window extrema

To compute maxima of windows of width k in linear time, keep a deque of candidate indices in increasing index order and **strictly decreasing** value order when removing rear values ≤the new value. At index i, first remove front indices ≤i−k because they expired; next remove rear indices j with $A[j]\le A[i]$; then append i. Once i≥k−1, the front value is the current maximum.

Why can dominated rear j be discarded? New i has at least as large a value and expires later, so j cannot be the uniquely needed maximum of any future window containing j and i. Removing equals prefers the newest identity. If only strictly smaller rear values are removed, equal candidates remain and the earliest equal identity wins; the maximum values are the same. Expiration must compare indices, not just values. Each index enters once and leaves at most once, either by expiration or domination, giving linear total deque operations and O(k) space. One update can delete many candidates, so its individual worst case is O(k).

<!-- SIM:window -->

```text
window_maxima(A, k):
    require 1 <= k <= length(A)
    D = empty deque of indices
    output = empty list
    for i = 0 to length(A)-1:
        while not empty(D) and first(D) <= i-k:
            delete_first(D)
        while not empty(D) and A[last(D)] <= A[i]:
            delete_last(D)
        insert_last(D, i)
        if i >= k-1:
            append(output, A[first(D)])
    return output
```

The domination argument must include future lifetime: when j<i and its value is no larger than the incoming value, every future window that still contains j also contains i until j expires. Therefore j cannot be needed as a maximum value, and retaining the newer equal candidate gives the newest argmax policy. A later larger value might itself be dominated, but the chain ends at a retained candidate at least as large and at least as new. Expiration separately removes candidates that no longer belong to the window; it cannot be replaced by a value comparison. The deque front is thus the largest retained live value, and discarded live values have a dominating retained witness. This proves the reported maximum. Candidate storage is at most k indices after each completed iteration, and there are exactly length(A)-k+1 outputs. With strictly smaller rear deletion, equal candidates survive and the oldest argmax policy is obtained instead.

**Worked example.** For `[1,3,-1,-3,5,3,6,7]`, k=3 maxima are `[3,3,5,5,6,7]`. The first 3 is removed when expired; the 5 removes weaker rear candidates; the later 6 and 7 dominate earlier smaller values. The authentic MS rear-dominance question is a closely related amortized deletion pattern without an expiration window.

## 17. Worklist boundaries, round robin, and failures of abstraction

FIFO by discovery time implements breadth-first layers in an unweighted graph. LIFO implements depth-first exploration but requires the correct frame state for return events. Neither ordinary FIFO nor LIFO guarantees minimum weighted distance when arbitrary positive weights exist. For edge weights only zero or one, **0-1 BFS** uses a deque: an improved zero-edge neighbor goes to the front, an improved one-edge neighbor to the rear. It must perform distance relaxation; a simplistic one-time visited rule can freeze a suboptimal first discovery. The general graph proof belongs to its chapter, but the distinction prevents misidentifying a deque as an ordinary BFS queue.

A round-robin queue repeatedly serves its front and reenqueues unfinished tasks. If every job eventually finishes, this models cyclic turns. If jobs never finish, emptiness is not a termination condition. For Josephus elimination with n labels and counting step k, rotate k−1 survivors then remove the front. For `[1,2,3,4,5,6,7]`, k=3, elimination order is `[3,6,2,7,5,1,4]`. The final survivor is 4.

<!-- SIM:josephus -->

For a zero-based survivor, $J(1,k)=0$ and $J(n,k)=(J(n-1,k)+k)\bmod n$. Removing the kth person makes original index k mod n the new start; mapping the smaller problem's survivor back shifts it by k. For one-based labels return J(n,k)+1. With k=2 and $n=2^m+\ell$, $0\le\ell<2^m$, the one-based survivor is 2ℓ+1. Queue simulation costs O(nk) literal rotations when k is a variable; reduce k−1 modulo current length for each elimination. A recurrence obtains only the survivor in O(n) arithmetic operations, not the entire elimination order.

Containers and their elements have separate identity. Aliasing handles, returning a reference to a popped slot, and moving storage during growth can invalidate a client's assumptions. Failure-safe updates initialize nodes and allocate replacement arrays before publishing them. Shared concurrent queues require synchronization and ordering guarantees; sequential pointer invariants alone do not prove thread safety. A fixed ring also needs a declared overflow policy: reject, block, drop newest, or overwrite oldest are different behaviors.

## 18. Complete chapter summary

1. A stack removes the newest live item; a queue removes the oldest. Write orientation before tracing. A legal history satisfies every prefix's underflow and capacity constraints.
2. Fixed-array stack count n points to the next unused slot. A linked stack belongs at the head. A singly linked queue needs both ends and must clear its tail on singleton removal. A deque needs both predecessor and successor access.
3. A count-based ring stores logical j at `(front+j) mod C`, can use all C slots, and distinguishes full from empty by count. A reserved-slot ring uses C−1 slots. Formula meanings must remain consistent through wrap and resize.
4. Resize copies the logical queue sequence, resets front, and preserves count. Geometric growth plus a separated contraction threshold gives constant amortized work, while individual relocation can be linear.
5. The two-stack queue preserves `reverse(output) concatenated with input`. Transfer occurs only when output is empty. Exact primitive work is e+2t+d and nonnegative potential 2|input| proves amortized bounds.
6. Client restoration must preserve order and identity contracts. Two stack reversals restore order; queue rotation requires a fixed original count or a genuine draining temporary structure. Aliases do not create independent containers.
7. Distinct increasing inputs can generate precisely 312-avoiding output permutations. Their legal complete histories are Dyck paths counted by Catalan numbers. Bounded capacity requires a height-limited recurrence rather than the unrestricted formula.
8. Brackets need both height and delimiter types. Expression evaluation needs tokenization, correct operand order, arity checks, domain checks, and exactly one final result. Infix conversion must explicitly handle equal-precedence associativity and unary operators.
9. Cached prefix extrema restore in constant time after pop. Associative queue aggregates preserve fold direction; commutativity is unnecessary. Costs of aggregate computation must still fit the claimed model.
10. Monotone stacks resolve first qualifying positions, and monotone deques remove expired or dominated candidates. Each identity is inserted once and removed at most once, yielding aggregate linear time even when an individual iteration removes many items.

## 19. Formula and conceptual problem bank

Work through the complete solutions after reading the lesson. Difficulty labels describe reasoning demands and have not been calibrated by student response statistics. Source problems retain their provenance and original option numbering; original variants deliberately test formula derivation, assumptions, boundary cases, and counterexamples. Visual traces use the question's exact inputs unless explicitly labeled as a separate example.

<!-- INCLUDE:problems -->

## 20. Examination rules and important final notes

These complete statements are a retrieval guide after the full instruction. They include hypotheses and failure conditions so that a remembered formula is not applied outside its domain.

<!-- INCLUDE:review -->

## 21. Editable laboratories

Choose a ring operation history, two-stack queue history, postfix token stream, target stack permutation, or sliding-window input. Each run recomputes exact states and starts paused. Ring operations use `E:x` and `D`; queue operations use `E:x`, `D`, and `F`; values are integers in the displayed bounds. Invalid input keeps the last valid model and explains the failure. The laboratory is for inspecting instruction and is not an assessment requested from you.

<!-- LAB:stackqueue -->

## 22. References and scope limits

The following lines are entirely English. They identify actual reviewed material rather than suggesting that every website section or exercise was copied. Independent extensions and question reconstructions are identified in the source audit and bank.

1. Robert Sedgewick and Kevin Wayne. Princeton COS226, *Stacks and Queues I*, Spring 2026, pages 1-45. [Lecture slides](https://www.cs.princeton.edu/courses/archive/spring26/cos226/lectures/13StacksAndQueuesI.pdf).
2. Andrea Vedaldi. Oxford B16, *Algorithms and Data Structures 1*, Chapter 3, Sections 3.3-3.5, 2024. [Course notes](https://www.robots.ox.ac.uk/~vedaldi/assets/teach/2024/b16/notes/3-elementary-data-structures.html).
3. Frank Pfenning, Andre Platzer, Rob Simmons. Carnegie Mellon 15-122, *Lecture 9: Stacks and Queues*, Spring 2026, pages 1-19. [Lecture notes](https://www.cs.cmu.edu/~15122-archive/s26/handouts/lectures/09-stackqueue.pdf).
4. Chris Gregg. Stanford CS106B, *Lecture 5: Stacks and Queues*, April 12, 2017, pages 8-29 and 33-45. [Lecture slides](https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1176/lectures/5-Stacks_Queues/5-Stacks_Queues.pdf).
5. Erik Demaine, Jason Ku, Justin Solomon. MIT 6.006, *Problem Session 1 Solutions*, Spring 2020, Problems 1-2 and 1-3, pages 2-3. [Written solutions](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/1ecbb4149fe5f5166033bdde285dba07_MIT6_006S20_prob1sol.pdf).
6. Berkeley CS61B. *DLLists*, Chapter 5. [Written textbook](https://cs61b-2.gitbook.io/cs61b-textbook/5.-dllists.md).
7. Iranian entrance-examination archive. PhD CE 1404, Q9 and Q11; MS CE 1393, Q49. Original PDF locators, hashes and independently derived answers appear with the authentic questions.

General proofs are separated from finite verification. The chapter covers the explicit prerequisite-to-advanced map above under its stated models. It does not establish literal scientific certainty or guarantee every unseen exam answer. Priority queues, full graph algorithms, advanced grammar parsing, concurrent lock-free algorithms, and persistent real-time queue construction are separate topics. This draft awaits your explicit approval before the next chapter starts.
