# Recursion: Contracts, Frames, Costs, and Backtracking

## 1. Sources, scope, and a reliable way to study this chapter

The four core written courses are Berkeley CS61A (John DeNero, *Composing Programs*, Section 1.7), MIT 6.0001 (Ana Bell, Eric Grimson, and John Guttag, Fall 2016, Lecture 6), Stanford CS106B (Eric Roberts, Winter 2015, Handouts 14 and 16), and Carnegie Mellon 15-112 (Pat Virtue, Fall 2023, Week 9, Lecture 2). Harvard CS50x 2025, Notes 3, supplies a supplementary C example. Exact materials, reading scopes, candidate comparisons, and source limitations appear in the references and source audit. These courses are complementary: Berkeley explains recursive contracts and tree recursion; MIT links inductive reasoning with execution frames and caching; Stanford explains recursive decomposition and backtracking continuations; CMU emphasizes practical tracing, debugging, and undoing choices.

The main implementation language is **C17**. Python and C++ source ideas are reconstructed under explicit C contracts rather than silently importing slicing, reference parameters, arbitrary integers, or evaluation order. The chapter covers scalar, array, tree, and choice recursion; mathematical termination; exact call counts; simultaneous space; memoization; and failure modes. Full sorting implementations belong to the sorting chapter; general recurrence-solving methods belong to the algorithms chapters. Here they are used to explain recursive execution.

Read the lesson before attempting the worked bank. For each program, write its input domain, returned value or side effect, base cases, decreasing measure, and pending work. Then step through the relevant animation. The questions and final rules reinforce formula selection and conceptual distinctions. This chapter aims at rigorous coverage of the stated scope; a finite source review cannot certify every course worldwide or guarantee answers to every unseen examination.

## 2. What a recursive call actually promises

A function is directly recursive when its body can call itself, and indirectly recursive when a chain of function calls can return to the same function. A call is an ordinary invocation with its own parameters and automatic local objects. Its caller waits until the callee returns, unless the implementation transforms the execution while preserving observable behavior.

The useful design unit is a **contract**, not an execution screenshot. For factorial, define $\operatorname{fact}(n)=n!$ on integers $n\ge0$. The zero case returns one because the empty product is one. For a nonzero argument, the recursive call promises $(n-1)!$, and multiplication by $n$ establishes $n!$. This reasoning is valid only if the child argument remains in the domain and is strictly smaller in a well-founded order.

A function that calls another function once is not necessarily recursive. A call graph cycle establishes possible recursion; a particular input can still take a nonrecursive branch. Also distinguish a recursive definition from an efficient recursive implementation: writing the same subproblem twice can reproduce its entire computation twice.

## 3. Termination requires a well-founded measure

A ranking function maps each nonterminal state to a set with no infinite descending chains, commonly the nonnegative integers. If $\mu(s)\in\mathbb N$ and every executed child satisfies $\mu(s')<\mu(s)$, the call chain cannot continue forever. A base case must handle every reachable minimal state. A numerical argument need not decrease when another measure does: searching a suffix increases its starting index while decreasing its remaining length.

Consider subtraction by two. If the contract is $n\ge0$ and the only guard is `n == 0`, positive odd inputs never reach zero over mathematical integers. A guard `n <= 0` repairs that mathematical progression if negative final arguments are permitted; an unsigned C argument requires a different guard, `n <= 1`, before subtracting two. Merely displaying a base case is not a proof that it is reachable.

For a state $(i,j)$, a lexicographic measure can decrease even if the second component resets upward whenever the first decreases. This is distinct from decreasing the sum, which may increase during a reset. For graph exploration, the relevant measure can be the number of unvisited vertices on the current path. Marking before recursive exploration prevents an immediate cycle; unmarking on backtracking changes the algorithm's complexity and meaning.

## 4. Partial correctness and total correctness

Partial correctness says that a terminating execution satisfies its postcondition. Total correctness adds termination. An induction proof of a recursive program has four obligations: the base branch establishes the contract; every child call satisfies its precondition; its measure is smaller; and the parent combines the promised child results into its own postcondition.

For an array sum over the half-open interval $[l,r)$, the empty interval returns zero. For $l<r$, the child sum over $[l+1,r)$ excludes precisely the first element. Adding `a[l]` restores the required sum. The decreasing measure is $r-l$. Bounds $0\le l\le r\le N$ must remain valid; a mathematical induction does not license an out-of-bounds read or signed overflow in C.

The recursive hypothesis is not circular reasoning: it is applied only to smaller states already covered by induction. Strong induction is convenient when the child size drops by more than one or when several different smaller sizes occur. Structural induction handles a finite tree by proving the empty-tree case and combining already established results for its proper subtrees.

## 5. Factorial with an explicit C17 range contract

On implementations providing `uint64_t`, the following function computes exactly the mathematical factorial for $0\le n\le20$. The result pointer must designate a writable `uint64_t` object. Failed calls do not change that object. The initial range check prevents uncontrolled depth and overflow; a mathematical factorial outside the range still exists, but is not representable by this interface.

```c
#include <stdbool.h>
#include <stdint.h>

bool factorial64(unsigned n, uint64_t *out) {
    if (out == 0 || n > 20) return false;
    if (n == 0) { *out = 1; return true; }
    uint64_t smaller;
    if (!factorial64(n - 1, &smaller)) return false;
    *out = (uint64_t)n * smaller;
    return true;
}
```

The zero guard is evaluated before `n - 1`, so unsigned wraparound does not occur on the recursive edge. A child writes into the parent's local `smaller`, which remains alive while the parent is suspended. Returning the address of that automatic object would instead produce a pointer to an object whose lifetime ends on return. An output pointer is passed by value, but the designated object can be mutated through the copied address.

## 6. Frames, continuations, and the return phase

For `fact(4)`, the descent creates logical invocations for 4, 3, 2, 1, and 0. The frame for 4 retains the pending instruction to multiply the child result by four. Reaching zero does not finish the outer call: the return phase computes 1, 1, 2, 6, and 24 while those pending operations are completed in reverse order.

An activation record conceptually stores parameters, locals, saved results, and the location at which execution resumes. The last unfinished call returns first. A diagram of the full call tree includes completed calls that no longer occupy live frames. These are different objects and must not be counted interchangeably. C permits recursion but does not mandate a particular hardware stack layout or a uniform byte size per call.

<!-- SIM: stack -->

During the animation, the highlighted row is the active invocation. Other displayed rows are suspended continuations. A return checkpoint marks a completed value before the frame is removed at the next checkpoint; the frame-count convention is stated in the snapshot. Returned values travel to the caller's pending operation rather than being assigned to every frame at once.

## 7. Output before and after the child call

```c
#include <stdio.h>
void around(unsigned n) {
    if (n == 0) return;
    printf("%u ", n);
    around(n - 1);
    printf("%u ", n);
}
```

Calling `around(3)` prints `3 2 1 1 2 3`. The first print occurs on descent and the second occurs while unwinding. The terminal invocation prints nothing. Moving both prints before the call changes the order to `3 3 2 2 1 1`; placing both after it gives `1 1 2 2 3 3`. Returning a number and printing a number are different postconditions. A function may have the same return value as another function while producing a different output trace.

For multiple children, explicitly sequence calls when an exact trace matters. With pre-child, between-child, and post-child actions, the position of each action determines preorder, inorder, or postorder behavior. A base branch's own output must also be included in the count.

<!-- SIM: output -->

## 8. Automatic locals, shared state, and expression order

Every invocation gets a distinct automatic local object. A `static` local is one shared object for the program's lifetime, and a global object is also shared. Passing a pointer can make multiple frames refer to the same object. Therefore, the assertion that recursion makes all state independent is false. A saved local parameter is independent; the pointee is not automatically independent.

In C17, `f(n--)` passes the old value of `n`. The parent is decremented before the child body begins, but the child starts with the old value, so repeated calls can fail to make progress. `f(n - 1)` passes a smaller value without changing the parent's parameter. `f(--n)` passes the smaller value and also changes the parent's parameter, which affects subsequent parent actions.

For `f(n-1) + f(n-2)`, C17 does not specify which operand call executes first. Pure calls can still yield a fixed sum. To specify a left-first trace, write separate statements that save each result before adding. Separate called function bodies are indeterminately sequenced rather than arbitrarily interleaved; `i++ + i++` has unsequenced conflicting updates and undefined behavior. Do not equate unspecified order with undefined behavior. A non-void function that reaches its closing brace without a return has undefined behavior if the caller uses the missing result.

## 9. Linear recursion: exact calls and resource cost

For one child of size $n-1$ with a base at zero, let $C(n)$ count invocations including the root and base. Then $C(0)=1$ and $C(n)=1+C(n-1)$, so $C(n)=n+1$. There are $n$ recursive edges, $n$ nonbase invocations, and peak logical depth $n+1$. If every frame uses bounded local space, auxiliary stack space is $\Theta(n)$. These counts exclude the external caller such as `main`.

If a child reduces the argument by a fixed $k>0$ until $n\le0$, the number of nonbase invocations for $n>0$ is $\lceil n/k\rceil$. The total includes one final base invocation. If an invocation also runs a loop proportional to its current argument, total work is a sum rather than merely the call count. A one-child recursion can therefore take quadratic time while having only linear depth.

For variable local storage, sum the sizes of simultaneously live objects along a path. An array of size $n$ in a frame followed by a child with size $n-1$ gives quadratic simultaneous storage if each array remains live. If sizes halve, the geometric sum is linear even though depth is logarithmic. C17 implementations may omit VLA support; these statements concern the stated allocation model.

## 10. Digit recursion and Euclid's algorithm

For a nonnegative integer $x$, digit sum has base $x<10$ and recursive decomposition $s(x)=x\bmod10+s(\lfloor x/10\rfloor)$. The argument loses one decimal digit. For $x>0$, there are $\lfloor\log_{10}x\rfloor+1$ invocations under this one-digit base, whereas a zero-only base adds another call. Define the behavior at zero before using a logarithm, since $\log 0$ is undefined.

Euclid's algorithm on unsigned nonnegative integers is `gcd(a,b) = b == 0 ? a : gcd(b,a % b)`. The remainder operation is reached only when $b>0$. The measure is the second argument: $0\le a\bmod b<b$. The first argument may increase on the first step if initially $a<b$, which does not invalidate termination. The identity $\gcd(a,b)=\gcd(b,a\bmod b)$ follows because a divisor of $a$ and $b$ divides the remainder, and a divisor of $b$ and the remainder divides $a$. Mathematical $\gcd(0,0)$ is convention-dependent; an implementation returning zero should state that convention.

<!-- SIM: euclid -->

## 11. Array and string intervals without slicing

A half-open interval separates the empty case cleanly. Its length is $r-l$, and the endpoint `r` is never dereferenced. A palindrome test can compare `a[l]` and `a[r-1]` only after verifying $r-l\ge2$. The middle interval is $[l+1,r-1)$. Short-circuiting on a mismatch avoids all further comparisons. An empty or single-element interval is a palindrome under this contract.

```c
#include <stddef.h>
#include <stdbool.h>
/* Requires 0 <= l <= r <= the readable array extent. */
bool palindrome(const unsigned char *a, size_t l, size_t r) {
    if (r - l <= 1) return true;
    if (a[l] != a[r - 1]) return false;
    return palindrome(a, l + 1, r - 1);
}
```

The caller may supply a null pointer only for an interval whose base branch returns without dereferencing it; the interface does not perform pointer arithmetic on that pointer. An explicit extent or a prior validated C-string length is required. The terminator is excluded from the content interval. Unlike repeated Python slicing, these index updates do not allocate copies of substrings. Unicode grapheme palindromes require a different representation and are not implied by byte equality.

<!-- SIM: palindrome -->

## 12. Binary search: shrinking the interval precisely

For a sorted array over $[l,r)$, handle `l == r` first. Set `m = l + (r-l)/2`; this avoids overflow from adding the endpoints. If the target is smaller than `a[m]`, recurse on $[l,m)$. If larger, recurse on $[m+1,r)$. Both children are strictly shorter because the compared midpoint is removed.

On an unsuccessful path starting with $n\ge1$ elements, the maximum number of nonempty comparison invocations is $\lfloor\log_2 n\rfloor+1$ for this midpoint policy; the final empty invocation makes the maximum total one larger. For zero elements there is exactly one empty invocation. A successful search stops at its matching invocation and does not append a final empty one. A child interval $[m,r)$ can fail to shrink when it retains the midpoint, so changing an endpoint by one can destroy termination.

<!-- SIM: binary -->

The count above concerns comparisons against the midpoint, not every C relational test. Bound checking, equality checks, and less-than checks form a different primitive-operation count. When duplicates occur, the simple search returns some matching index; finding the first or last matching index requires an additional contract and search rule.

## 13. Exponentiation: storing a recursive result matters

For integer $e\ge0$, define $a^0=1$ as the empty product for this algorithm, including the computational convention at $a=0$. Base cases at zero and one return 1 and $a$. For larger $e$, compute $h=a^{\lfloor e/2\rfloor}$ once. If $e$ is even, return $h^2$; if odd, return $ah^2$. Exponent parity proves the combination correct.

With zero/one bases, $e\ge1$ gives $\lfloor\log_2 e\rfloor+1$ invocations and $\lfloor\log_2 e\rfloor$ squarings. Every nonleading one bit requires one further multiplication by $a$. Therefore the multiplication count is $\lfloor\log_2 e\rfloor+\operatorname{popcount}(e)-1$. The exponent-zero case uses zero multiplications and one invocation.

Writing `power(a,e/2) * power(a,e/2)` recomputes the same child rather than reusing its answer. For powers of two, this makes a full binary tree and linear work in $e$, rather than logarithmic work. Exact arithmetic, fixed-width overflow, and modular multiplication require separate contracts; taking a remainder after an overflowing product does not undo the overflow.

## 14. Tree recursion and the full binary tree identity

If every nonleaf invocation makes exactly two children, write $I$ for internal invocations and $L$ for leaves. The tree has $I+L-1$ edges, while counting edges from parents gives $2I$. Thus $L=I+1$, and the total number of invocations is $2L-1$. This identity requires a finite full binary call tree; it is not valid for arbitrary trees with one-child nodes.

Sequentially executing two children does not keep both complete call trees active at once. Peak depth follows a longest path. When the parent stores the first child's result while evaluating the second, that stored result contributes to live space, but the first child's returned frames do not. If both children are actually spawned concurrently, or entire child outputs remain stored, a different space model is needed.

## 15. Naive Fibonacci: exact formulas, not just a slogan

This chapter fixes $F_0=0$, $F_1=1$, and $F_n=F_{n-1}+F_{n-2}$ for $n\ge2$. Berkeley's illustrated sequence and MIT's rabbit-count sequence use different initial indexing or values; their numbers are translated before comparison. In a naive implementation with bases zero and one, call count satisfies $C_0=C_1=1$ and $C_n=1+C_{n-1}+C_{n-2}$.

Set $D_n=C_n+1$. Then $D_n=D_{n-1}+D_{n-2}$ with $D_0=D_1=2$, giving $C_n=2F_{n+1}-1$. Nonbase invocations perform one addition, so there are $F_{n+1}-1$ additions. The number of leaves is $F_{n+1}$. For $n\ge1$, peak depth is $n$, including the root and terminal invocation; at $n=0$ it is one. The base at one makes this depth different from factorial's zero-only base.

<!-- SIM: fibonacci -->

The characteristic equation is $x^2=x+1$, whose larger root is $\varphi=(1+\sqrt5)/2$. Consequently $C_n=\Theta(\varphi^n)$, a sharper growth description than the valid upper bound $O(2^n)$. The result $F_n$ itself has $\Theta(n)$ bits, so constant-time addition is a unit-cost abstraction rather than an arbitrary-precision guarantee.

## 16. Memoization: requests, misses, and valid cache keys

Memoization stores the result for an already computed state. Start with cache entries for $F_0$ and $F_1$. A request first checks the cache; a miss recursively requests the two children in explicitly left-first order, stores their sum, and returns it. For $n\ge2$, the newly evaluated nonbase states are exactly $2,3,\ldots,n$, so there are $n-1$ misses.

Each miss makes two child requests and there is one initial request. Hence the total number of requests is $2n-1$, including hits. The additions are $n-1$, and the final cache has $n+1$ entries. For inputs zero or one there is one hit, zero additions, and the two initially seeded entries remain. A warm cache already containing the requested answer makes just one request. Do not apply the cold-cache formula to that situation.

<!-- SIM: memo -->

A cache key must include all state affecting the result. If a function depends on both an index and a remaining target, indexing the cache only by the index is wrong. Mutation, random input, time, or observable printing can make replacing a call by a cached result change behavior. In cyclic state dependencies, a visited flag is not a completed answer: use an in-progress state to detect cycles rather than returning an unfinished cache entry.

## 17. Time, depth, and bytes are separate quantities

The table uses sequential execution, bounded local frame storage, and unit-cost arithmetic unless otherwise specified.

| Algorithm and base policy | Total invocations | Peak logical depth | Principal work |
|---|---:|---:|---:|
| Factorial, base zero | $n+1$ | $n+1$ | $n$ multiplications |
| Digit sum, one-digit base, $x>0$ | $\lfloor\log_{10}x\rfloor+1$ | Same as invocations | One digit per invocation |
| Naive Fibonacci, bases zero and one | $2F_{n+1}-1$ | $\max(1,n)$ | $F_{n+1}-1$ additions |
| Cold memo Fibonacci, $n\ge2$ | $2n-1$ requests | $n$ | $n-1$ additions |
| Hanoi, zero base | $2^{n+1}-1$ | $n+1$ | $2^n-1$ disk moves |
| Exhaustive binary choices of length $n$ | $2^{n+1}-1$ | $n+1$ | $2^n$ complete choices |

For a sequential balanced divide-and-combine algorithm, a typical recurrence is $T(n)=2T(n/2)+\Theta(n)$, while constant-local stack depth follows $D(n)=1+D(n/2)$. Time is $\Theta(n\log n)$ and depth is $\Theta(\log n)$. This does not claim constant total auxiliary memory for merge sort: a merge buffer adds its own storage requirement.

## 18. Tail position and accumulator invariants

A call is in tail position when its returned result is immediately returned without pending work in the caller. `return fact(n-1) * n;` is not tail recursive, because multiplication remains. An accumulator variant has contract `fact_acc(n,a)` returns $a\,n!$. Its recursive step passes $(n-1,an)$, maintaining the required product; its zero case returns $a$.

The invariant at a call originating from $(N,1)$ is $a\,n!=N!$. Returning the child result completes the parent with no mathematical combination remaining. This permits a loop transformation, but **C17 does not require tail-call elimination**. A source-level tail-recursive implementation can still use linear logical or physical stack space. The transformed loop uses a bounded number of scalar variables, subject to arithmetic range and result-size constraints.

Accumulator transformations can change rounding in floating-point arithmetic because reassociation changes operation order. They also need care with side effects and overflow checks. Mathematical associativity does not establish identical floating-point or C execution behavior.

## 19. Converting recursion to an explicit stack

For non-tail recursion, replacing a call with a loop requires preserving its continuation. For a binary computation, a frame can store the input, a phase indicating which child remains, and a saved first-child result. Phase 0 schedules the first child; phase 1 saves its returned result and schedules the second; phase 2 combines both and returns to the parent.

Simply pushing both children and discarding the parent loses the pending combine operation. To reproduce left-first traversal using a last-in-first-out stack, push the right task first, then the left task. For preorder printing, emit on entry; for postorder printing, push a separate completion task or record a phase. An explicit stack exposes resource limits and may avoid implementation call-depth limits, but it does not inherently remove the information needed by the computation.

## 20. Mutual recursion and finite structural recursion

Two parity functions can call each other: `even(0)` is true, `odd(0)` is false, and each nonzero argument calls the other on one less. The natural-number measure decreases on each edge across both functions. Proving the pair together avoids assuming a theorem about one function before establishing the other. Negative input must be rejected or handled by a separate safe conversion; negating the minimum signed integer can overflow.

For a binary tree, `size(NULL)` returns zero; a nonempty node returns one plus the sizes of its children. Assuming a finite acyclic tree with disjoint child subtrees, every node is counted once. With $N$ nodes, there are $N+1$ null-child calls, hence $2N+1$ invocations. A shared DAG does not satisfy the disjoint-subtree assumption and can lead to repeated counts; a cycle can prevent termination. Define whether the contract counts visits, unique nodes, or structural occurrences before selecting a method.

## 21. Towers of Hanoi: legality and optimality

Three pegs hold disks of distinct sizes, with larger disks always below smaller ones. To move $n$ disks from source to destination, first move the top $n-1$ to the spare peg; move the largest disk once; then move the $n-1$ from spare to destination. The zero case does nothing. Induction proves legality: the first move sequence respects the smaller tower's rules, the largest disk then moves to an available legal destination, and the final sequence places only smaller disks above it.

Let $M_n$ count physical moves. Then $M_0=0$ and $M_n=2M_{n-1}+1$, so $M_n=2^n-1$. For optimality, before moving the largest disk from its original peg to the target, the smaller disks must be moved away, and afterward they must be brought onto it. In a minimal solution, an unnecessary largest-disk detour cannot improve this lower bound; formally, consider the first largest-disk move and the last one onto the destination. If it moves directly, both required smaller transfers yield $2M_{n-1}+1$; if it first moves to the spare, at least three smaller-tower transfers and two largest-disk moves are required. The recursive construction attains the direct-transfer bound.

<!-- SIM: hanoi -->

The animation uses actual pegs and sized disks. Each move has a lift, horizontal transfer, and lowering checkpoint, so a disk never passes through another disk in the visualization. Only settled checkpoints represent completed legal puzzle moves; in-transit states are explicitly labelled. The simulator verifies that the moved disk was on top and that its destination is empty or topped by a larger disk.

## 22. Binary decisions and restoring shared choices

To enumerate all subsets of $n$ distinct positions, recurse on index $i$. One branch excludes position $i$; the other includes it. At $i=n$, emit the chosen set. Under a mutable-list implementation, including means append, recurse, then remove exactly the appended element. This restoration makes the parent's state available for later siblings. A by-value persistent representation may avoid mutation, but pays different copying costs.

Every level fixes one position, so the tree has $2^n$ leaves and $2^{n+1}-1$ invocations. Peak depth is $n+1$, excluding the caller. If emitting a subset copies all selected elements, total emitted element occurrences are $n2^{n-1}$ for $n\ge1$, since every position belongs to half the subsets. Thus output cost is not constant per leaf when whole subsets are materialized.

<!-- SIM: subsets -->

An empty input has one subset, the empty set. Equal element values do not merge position-labelled subsets automatically: distinct index choices can have equal displayed values. Removing duplicate value subsets requires a separately specified generation policy.

## 23. Backtracking contracts and pruning

Backtracking explores alternatives while maintaining constraints. A useful contract is: search all completions of the current valid prefix, return or emit the required answers, and restore the prefix before returning. A decision procedure that retains the first successful path has a different postcondition: restore failed branches, but preserve the successful path. Confusing these policies is a common source of correct Boolean answers paired with corrupt output paths.

For subset sum with nonnegative values, prune when the partial sum exceeds the target, because later additions cannot decrease it. If negative values are allowed, that pruning rule is unsound. A remaining-sum upper bound can prune when even choosing every remaining nonnegative value cannot reach the target. Bounds must be recomputed under the actual data contract, and pruning changes exact call counts compared with the complete binary tree.

For a maze, mark a cell before exploring neighbors. If enumerating simple paths, unmark it on return so a later branch can use it; this can enumerate exponentially many paths. For ordinary reachability, retaining a global visited set yields a different algorithm, typically linear in vertices plus edges. A source backtracking maze should not silently be assigned the complexity of global-visited graph search.

## 24. Permutations, partitions, and recursive geometry

Choosing one remaining position per level generates $n!$ leaves for permutations of $n$ distinct positions. At depth $d$, there are $n!/(n-d)!$ invocations, so the total is $n!\sum_{k=0}^{n}1/k!$. Printing each full permutation costs $\Theta(n\,n!)$ symbol writes. The state can be restored by swapping the chosen value into position, recursing, then swapping it back. Repeated values require skipping equivalent choices within a level to avoid duplicate value permutations.

The partition count $P(n,m)$ represents ways to form $n$ from positive parts at most $m$, disregarding order. The two disjoint classes are partitions containing a part $m$, counted by $P(n-m,m)$, and those with no part $m$, counted by $P(n,m-1)$. Base policies are $P(0,m)=1$, $P(n,m)=0$ for $n<0$, and $P(n,0)=0$ for $n>0$. Test the zero-target case before the zero-maximum case so $P(0,0)=1$. Both state coordinates belong in a memoization key.

A Koch segment replaces one segment by four segments each of one-third its length. At order $k$, there are $4^k$ final segments, each of length $L/3^k$, so total length is $L(4/3)^k$. A four-child recursion with a zero-order drawing base has $(4^{k+1}-1)/3$ calls and depth $k+1$. Recursive geometry deserves a geometric diagram rather than a generic counter: its visible replacement rule is the concept being taught.

<!-- SIM: koch -->

## 25. A systematic debugging and examination procedure

First classify the specification: is the question asking for a return value, printed output, array mutation, total calls, recursive edges, leaves, or maximum simultaneous frames? State the base convention before deriving a formula. Trace a small input with all local parameters and shared objects separated. Check the zero, one, negative, odd, empty, duplicate, and maximum-representable cases relevant to the contract.

Second, check each child argument and endpoint. Post-decrement can pass an unchanged argument; unsigned subtraction can wrap; a retained midpoint can stop progress; repeated evaluation can double a subtree. Then identify the pending action after each child. Exact order requires explicit sequencing in C. For complexity, form a recurrence for the requested quantity rather than borrowing a memorized result from a superficially similar program.

Finally, prove the result symbolically and use a small trace to detect off-by-one errors. Independent checks validate many concrete instances but do not replace a proof for all inputs. Mathematical correctness, C representability, and finite execution resources are three separate obligations. A formula containing $\log n$ needs its domain and an explicit zero case.

## 26. Consolidated summary with exact assumptions

A correct recursive design uses a contract, reachable bases, a well-founded decrease, and a justified combination. A call frame is a continuation containing unfinished work. Descent and return determine output order. Automatic locals are distinct per invocation, while pointees, static locals, and globals can be shared. C17 does not force left-first operand evaluation or tail-call elimination.

For a one-child decrement-to-zero recursion, total invocations and depth are both $n+1$. For a full binary call tree, total invocations are twice its leaves minus one. Naive Fibonacci has $2F_{n+1}-1$ calls; cold memo Fibonacci has $2n-1$ requests for $n\ge2$, with preseeded bases and left-first evaluation. Hanoi needs $2^n-1$ moves but $2^{n+1}-1$ invocations under its zero-base implementation. Binary choices have $2^n$ complete outputs; materializing them adds an output-size cost. None of these formulas should be transferred to a program with a different base or branch policy without rederivation.

Space follows simultaneously live state. A longest call path is different from the full execution tree. Memoization reuses completed pure state answers, while backtracking restores shared state and pruning requires a valid constraint argument. The final rules and worked solutions below develop these distinctions through concrete calculations, proofs, counterexamples, and exam-style distractors.

## 27. Fully worked mathematical and conceptual problems

<!-- INCLUDE: problems -->

## 28. Examination rules and final conceptual notes

<!-- INCLUDE: review -->

## 29. Editable recursion laboratory

<!-- LAB: recursion -->

## 30. References and source qualifications

1. **University of California, Berkeley — CS61A.** John DeNero, [Composing Programs, Section 1.7, Recursive Functions](https://composingprograms.com/pages/17-recursive-functions.html), Sections 1.7.1–1.7.5. The [CS61A course calendar](https://cs61a.org/fa26/) links its textbook's recursive-functions section. The older complete Section 1.7 edition was read for stable examples and explicit source numbering.
2. **Massachusetts Institute of Technology — 6.0001, Fall 2016.** Ana Bell, Eric Grimson, and John Guttag, [Lecture 6: Recursion and Dictionaries](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/mit6_0001f16_lec6/). The 58-page lecture was read as extracted text; recursion and memoization are concentrated on PDF pages 1–39 and 54–57. Individual slide authorship is not assigned beyond the course's listed instructors.
3. **Stanford University — CS106B, Winter 2015.** Eric Roberts, [Handout 14: Recursive Strategies](https://cs.stanford.edu/people/eroberts/courses/cs106b/handouts/14-RecursiveStrategies.pdf) and [Handout 16: Recursive Backtracking](https://cs.stanford.edu/people/eroberts/courses/cs106b/handouts/16-RecursiveBacktracking.pdf), all six pages of extracted text. Decomposition, Hanoi, fractals, maze search, and path retention inform the reconstruction. Handout 19A contains image-based answers not captured as readable solution text; it is not counted as a fully studied solution bank.
4. **Carnegie Mellon University — 15-112, Fall 2023.** Pat Virtue, [Week 9, Lecture 2: Recursion](https://www.cs.cmu.edu/~112-f23/lecture/15112_F23_Lec2_Week9_Recursion.pdf), complete extracted text of 48 slides, especially pages 18–48. Debugging, repeated recursive evaluation, and apply/recurse/undo inform the lesson. Image-only demos are not represented as read transcripts.
5. **Harvard University — CS50x 2025.** David J. Malan, [Notes 3: Algorithms, Recursion, and Merge Sort](https://cs50.harvard.edu/x/2025/notes/3/), binary-search and recursion sections. Supplementary C explanation, not one of the four required core selections. Asymptotic notation is defined independently here: big Omega is not inherently a best-case designation.
6. **ISO/IEC WG14 — primary language reference, not a university course.** [N1570](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf), Sections 5.1.2.3, 6.5, 6.5.2.2, 6.5.2.4, 6.8.6.4, and 6.2.4, for sequencing, permitted direct/indirect recursion, return behavior, and automatic-object lifetime. This publicly accessible C11 committee draft is used for these unchanged C17 language rules; it is not labelled the C17 standard.

The source audit records the finite accessible candidate pool and the choice of complementary core courses. Problems are original or independently reconstructed conceptual variants with individual provenance. They are not a wholesale copy of external copyrighted exercise banks. Authentic examination content is a checked, cited bridge revisit, with an independently derived answer rather than an asserted official key. Review status and remaining qualifications are visible in the quality audit.
