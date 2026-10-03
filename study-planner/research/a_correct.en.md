## Sources and chapter boundaries

This chapter develops **algorithm correctness**, from state-based specifications to complete proofs of searching, sorting, arithmetic and certificate verification. Read the earlier chapters on induction, logical implication, loop invariants and divide and conquer when a prerequisite needs reinforcement. Here, every proof connects to an executable algorithm or a precise mathematical question. Correctness, termination, safety and efficiency are separate claims, and every algorithm states which claims are established.

Four principal written university courses were compared and read in the relevant sections:

| University and course | Material actually read | Contribution to this chapter |
| --- | --- | --- |
| Carnegie Mellon, 15-122 Principles of Imperative Computation, Frank Pfenning | Lecture 2, Contracts, all 24 PDF pages | Exponentiation contracts, old input values, invariant preservation and machine arithmetic |
| Cambridge, Specification and Verification I, Mike Gordon | PDF pages 11–28, 47–59 and 63–72 | Hoare rules, backward substitution, arrays, verification conditions and total correctness |
| MIT, 6.042J Mathematics for Computer Science, Albert Meyer and Adam Chlipala; text by Eric Lehman, F. Thomson Leighton and Albert Meyer | Text §5.4, PDF pages 140–152 | State-machine invariants, reachability and well-founded termination |
| Stanford, CS161 Design and Analysis of Algorithms, Winter 2022 | Lecture 2 notes, PDF pages 1–4 | Insertion-sort and merge-sort induction, merge boundaries and recursive proof structure |

The [source comparison and reading audit](../reviews/a_correct-sources.html) records the accessible candidate pool, scope, selection and limitations. This is a comparison of accessible written materials, not a claim to have examined every course ever offered. University-derived tasks are independently worded and individually attributed. Original tasks and authentic entrance-examination translations have distinct labels.

## Contracts, states and the meaning of correctness

A **state** gives values to variables and identifies the current control location. For arrays, it also gives each indexed value; for mutable objects, it records shared references. A program command maps an initial state to an execution that may terminate normally, fail, or continue indefinitely. A mathematical pseudocode model uses exact integers unless a finite arithmetic model is explicitly declared.

A **precondition** $P$ describes the admitted initial states. A **postcondition** $Q$ describes the required final state. The notation $\{P\}\ C\ \{Q\}$ here means partial correctness: every normally terminating execution from a state satisfying $P$ ends in a state satisfying $Q$. It says nothing about a nonterminating execution. We establish safety separately, so the absence of normal termination through an error cannot count as a useful correctness certificate. **Total correctness** means partial correctness together with termination for every admitted input; our complete algorithm claims also require safe evaluation of every expression and array access.

For a sorting routine, “the result is sorted” is an incomplete contract. A routine returning an empty array satisfies that sentence for every input. Let $A_0$ be an immutable snapshot of the initial array, and let $\operatorname{bag}(A)$ denote its multiset of values, including multiplicities. A complete value-level contract is:

$$\operatorname{bag}(A)=\operatorname{bag}(A_0)$$

For every valid adjacent index, meaning $0\le i<n-1$, require:

$$A[i]\le A[i+1].$$

The quantified set is empty when the array has fewer than two elements. Stability is an additional contract: equal-key records retain their original relative order. If the procedure sorts in place, its frame condition must also specify which memory it may modify. Correctness of a sorted list of keys does not establish correctness of record identities, payloads or external aliases.

Specifications can be inconsistent or too weak. An impossible precondition makes a partial-correctness triple vacuously valid. A postcondition that merely says “the output is an integer” does not specify exponentiation. Before proving anything, identify the input domain, mathematical function, permitted mutation, empty-input convention and tie rule.

**Example: two meanings of exponentiation.** Over exact integers, the result of input $(3,6)$ is $729$. Under arithmetic modulo $256$, the corresponding residue is $217$. A proof of one result does not prove the other. Unsigned finite-width arithmetic, signed arithmetic and arbitrary-precision arithmetic must not be interchanged silently. In C, unsigned arithmetic wraps modulo its range; signed overflow is not defined as ordinary modular wrapping.

<!-- FIGURE:obligations -->

## Backward reasoning and verification conditions

Suppose a pure assignment is `x = E`, and the expression is defined in every admitted state. To establish a desired postcondition $Q$, substitute the old expression $E$ for every free occurrence of the assigned variable in $Q$. This is substitution in the logical formula, not substitution of a newly computed value into the old expression. Bound variables must be renamed if necessary to avoid capture.

$$\operatorname{wp}(x:=E,Q)=Q[E/x].$$

For example, after `x = x + 3`, the requirement $x^2=25$ becomes $(x+3)^2=25$, hence old $x=-8$ or old $x=2$. A forward guess such as $x=5$ refers to the final state and is not the required initial condition. Over fixed-width arithmetic, this algebra must be repeated in the specified arithmetic model and include any safety obligation.

For a sequence, reason backward from the final command first:

$$\operatorname{wp}(C_1;C_2,Q)=\operatorname{wp}(C_1,\operatorname{wp}(C_2,Q)).$$

For `x = x + 1; y = 2*x`, and final requirement $y=10$, the second assignment requires $2x=10$, so the first requires $2(x+1)=10$, giving initial $x=4$. Initial $y$ is irrelevant because it is overwritten. Reversing the substitution order gives the wrong state relationship.

For a total, pure Boolean guard $B$:

Write the two guarded requirements separately:

$$F_1=(B\Rightarrow\operatorname{wp}(C_1,Q)),$$
$$F_2=(\neg B\Rightarrow\operatorname{wp}(C_2,Q)).$$

The conditional's weakest precondition is their conjunction $F_1\land F_2$.

The guard is evaluated in the initial state of the conditional. For `if x < 0: x = -x`, the omitted else branch is `skip`. Thus $x\ge0$ afterward follows both when initial $x<0$ and when initial $x\ge0$. In machine signed integers, negating the minimum representable value requires separate analysis; the exact-integer proof alone does not justify the implementation.

The **consequence rule** permits a stronger precondition and a weaker postcondition. If $P'\Rightarrow P$, the known triple $\{P\}C\{Q\}$ applies to $P'$; if $Q\Rightarrow Q'$, its result implies $Q'$. The directions matter. Proving correctness for positive inputs does not prove it for all integers. Proving the exact result does imply a looser result bound, but a loose bound does not identify the exact result.

An array update must account for aliasing of indices. For `A[i] = v`, model the new array as a functional update: its value at $j$ is $v$ when $j=i$, and old $A[j]$ otherwise. In `A[i]=1; A[j]=2`, the desired postcondition $A[i]=1\land A[j]=2$ requires $i\ne j$, assuming both indices are valid. Treating the two indexed cells as automatically distinct is an invalid proof.

A **verification condition** is a mathematical implication whose validity establishes one proof obligation. For a loop with guard $B$ and invariant $I$, the partial-correctness conditions are:

$$P\Rightarrow I,$$
$$\{I\land B\}\ C\ \{I\},$$
$$I\land\neg B\Rightarrow Q.$$

Add obligations for a defined guard, safe body operations, termination of the body and a well-founded decrease. A failed verification condition may mean the program is wrong, but it may instead mean the annotation is too weak or unsuitable. For example, annotating `while False` with an invariant `False` fails initialization even though the command immediately terminates and leaves the state unchanged.

## Invariant discovery and termination

An invariant belongs to a specified checkpoint, normally just before the guard. Statements about the state halfway through the body may differ. To discover an invariant, rewrite the final goal as a relationship between **processed data**, **unprocessed data** and immutable inputs. Then add bounds sufficient to establish safety and an exit implication. Useful components include conservation laws, prefix properties, interval exclusion and snapshots of overwritten values.

Inductiveness is stronger than truth on reachable states. A predicate may hold at every reachable checkpoint but fail to be preserved at an unreachable state satisfying that predicate. Verification conditions quantify over all states allowed by the invariant; strengthening it can exclude those spurious states. Conversely, a transition-preserved predicate that is false initially tells us nothing about reachable states. The negation of an invariant is not automatically an invariant.

For total correctness, choose a **variant** in a well-founded set. A nonnegative integer $V$ that strictly decreases on each executed body permits at most initial $V$ iterations. The variant need not reach zero: the guard may become false sooner. A nonnegative real that decreases strictly can have an infinite sequence, such as $1,1/2,1/4,\ldots$. A nonnegative integer that merely never increases can also remain constant forever.

For nested progress, lexicographic pairs of nonnegative integers are useful. The pair $(a,b)$ decreases if the first coordinate decreases, or if it stays equal and the second decreases. A decrease of $a$ may reset $b$ to any finite nonnegative value. Such a measure proves termination, but initial $a+b$ need not bound the number of steps. If a program can nondeterministically reset $b$ to arbitrarily large finite values, there may be no uniform step bound determined by the initial pair alone.

**Counterexample discipline.** To disprove a universal claim, give one admitted input, trace the relevant states, identify the failed obligation and state which hypothesis would repair it. Testing many inputs is evidence about those inputs. A proof establishes a quantified claim under its assumptions. Neither should be presented as the other.

## Binary search with empty arrays and duplicate keys

The **lower bound** of a target $t$ in a sorted array is the first index whose value is at least $t$, or $n$ if no such value exists. This differs from finding an arbitrary equal element. Duplicates therefore belong to the contract, not to an optional afterthought.

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

At the checkpoint, use these three clauses:

$$0\le lo\le hi\le n,$$
$$\forall i<lo: A[i]<t,$$
$$\forall i\ge hi: A[i]\ge t,$$

where the quantified indices are valid array indices. The unclassified interval is $[lo,hi)$. Initialization holds because both classified ranges are empty. If $lo<hi$, floor midpoint selection gives $lo\le mid<hi$, so the access is safe.

If $A[mid]<t$, sortedness implies that every earlier array value is also less than $t$. Moving $lo$ to $mid+1$ therefore classifies the entire discarded left region correctly. The old right classification remains unchanged. Otherwise $A[mid]\ge t$, and sortedness makes every later value at least $t$; assigning $hi=mid$ establishes the right classification.

Let $L=hi-lo$. The first branch produces $L'=hi-mid-1$; the second produces $L'=mid-lo$. Both lie between zero and $\lfloor L/2\rfloor$. Hence $L$ is a nonnegative integer variant and the loop terminates. At exit $lo=hi$, so the two classified regions exhaust the array. This proves the first eligible index, including the all-small case $lo=n$ and the empty-array case $lo=0$.

For nonempty intervals the maximum number of body executions is $\lfloor\log_2 n\rfloor+1$, equivalently $\lceil\log_2(n+1)\rceil$; an empty array requires zero. This counts body executions in this exact implementation, not arbitrary binary-search implementations. Depending on the target, some branches end sooner.

The tempting update `lo = mid` is wrong here. With $A=[2]$ and $t=3$, it preserves the classification invariant but leaves the interval unchanged. Partial correctness cannot supply the missing termination argument. The midpoint expression also illustrates model dependence: `lo + (hi-lo)//2` avoids adding the two endpoints, but the implementation still needs a type capable of representing the endpoints, their difference and all assigned values.

<!-- FIGURE:interval -->

## Sorting proofs that preserve records

### Insertion sort: the saved-key hole

```python
def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
```

At the outer checkpoint, the prefix $A[0:i]$ is sorted and contains exactly the records initially in that prefix; the unprocessed suffix has not changed. The inner loop cannot use the assertion that the physical array remains a permutation after every assignment. A shift duplicates a value while the saved `key` temporarily lives outside the array. Instead regard position $j+1$ as a logical **hole**. The other prefix positions plus the saved key contain the original prefix multiset.

The portion left of the hole remains sorted. Every record shifted right has key strictly greater than the saved key, and its relative order with other shifted records is preserved. When the guard becomes false, either $j=-1$, or $A[j]\le key$. Filling the hole yields a sorted prefix of length $i+1$ and restores physical multiset equality. The inner variant is $j+1$ at a true guard; every shift decreases it by one. The outer loop has finitely many positions.

With tagged records $(2,a),(1,b),(2,c)$, processing the last record with a strict greater-than comparison leaves $(2,a)$ before $(2,c)$. Replacing `>` by `>=` can move the newer equal-key record ahead of an older one. Sortedness and multiplicity survive, but stability does not. Comparison equality must be evaluated on keys, while assignments carry the full record.

<!-- FIGURE:hole -->

### Merge sort: two distinct inductions

To prove merge sort, first prove a merge lemma: given two sorted input sequences, merging them returns a sorted multiset union. At a merge checkpoint, the emitted prefix is sorted, every emitted value is no greater than each next available head, and the emitted prefix plus both unconsumed suffixes preserves the total input multiset. Consume the smaller head; consume the left head on equality when stable sorting is required. When one side is exhausted, append the remaining sorted suffix.

The merge variant is the number of unconsumed records across both inputs. Appending a tail can be viewed as repeated safe emissions. Array access requires testing exhaustion before comparing heads. A proof that assumes both heads exist cannot justify the final phase of the algorithm.

Now use strong induction on input length. Length zero or one is already sorted. For larger lengths, split into children of lengths $\lfloor n/2\rfloor$ and $\lceil n/2\rceil$, both strictly smaller than $n$. The induction hypothesis proves both child contracts. The merge lemma proves the parent contract. The length measure proves recursive termination. The runtime recurrence is a separate analysis; solving a recurrence does not establish that the returned sequence has the right order.

## Partitioning without skipping unclassified elements

For three-way partitioning around a pivot $p$, maintain four regions:

$$A[0:lt]<p,\quad A[lt:i]=p,\quad A[i:gt]\text{ unknown},\quad A[gt:n]>p.$$

Here a relation on a slice means it holds for every value in that slice. The bounds are $0\le lt\le i\le gt\le n$. Start with $lt=i=0$, $gt=n$, and repeat while $i<gt$.

```python
def partition3(a, pivot):
    lt, i, gt = 0, 0, len(a)
    while i < gt:
        if a[i] < pivot:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1
        elif a[i] > pivot:
            gt -= 1
            a[i], a[gt] = a[gt], a[i]
        else:
            i += 1
    return lt, gt
```

In the less-than branch, when $lt<i$, the old element at $lt$ belongs to the equal region, so moving it to the old scan position preserves the enlarged equal region. When $lt=i$, the swap is a self-swap and both boundaries advance together. In the greater-than branch, the incoming value from the old end of the unknown region remains unclassified. Advancing the scan index would skip it; keep $i$ unchanged. The variant $gt-i$ decreases by exactly one in all branches. Swaps preserve the multiset, and at termination no unknown element remains.

This procedure partitions; it does not sort either outer region. It is not stable in general. For arrays containing unordered values such as floating-point NaN, the three comparison cases may not have the assumed trichotomy. The exact ordered-key model must be stated.

<!-- FIGURE:partition -->

## Arithmetic algorithms and their domains

### Division by repeated subtraction

For nonnegative integer $X$ and positive integer $Y$, initialize $q=0,r=X$ and repeatedly execute `r = r - Y; q = q + 1` while $r\ge Y$. The invariant is:

$$X=qY+r,\quad q\ge0,\quad r\ge0.$$

The body preserves conservation because $(q+1)Y+(r-Y)=qY+r$. The guard ensures the new remainder remains nonnegative. Since $Y\ge1$, the variant $r$ strictly decreases. At exit $0\le r<Y$, which uniquely characterizes quotient and remainder. The number of body executions is $\lfloor X/Y\rfloor$.

If $Y=0$, the conservation equality alone remains true and the guard stays true, but the remainder never decreases. If $Y<0$, the remainder grows under subtraction. Thus the positive-divisor assumption is a termination requirement and part of the mathematical division convention. Cambridge's worked partial-correctness derivation deliberately separates these obligations; it must not be read as a total-correctness proof for every divisor.

### Euclid's algorithm

For integers $a\ge0,b\ge0$, use `while b != 0: a,b = b,a % b`, with simultaneous assignment. At each checkpoint, $\gcd(a,b)=\gcd(a_0,b_0)$ and both variables remain nonnegative. Every common divisor of $a,b$ divides $a-qb$, and every common divisor of $b,a-qb$ divides $a$, so the gcd is preserved. Euclidean remainder gives $0\le a\bmod b<b$ for a positive divisor. The old $b$ is therefore a decreasing variant. At exit $b=0$, the gcd equals final $a$. Adopt the explicit convention $\gcd(0,0)=0$ if that input is admitted.

Sequentially writing `a=b; b=a%b` destroys the old dividend: the second assignment now computes $b\bmod b=0$. A temporary variable or simultaneous assignment is essential. Bounds on division cost and exact bit complexity belong to runtime analysis, not to this gcd correctness proof.

### Exponentiation by squaring

```python
def power(x, y):
    assert y >= 0
    r, b, e = 1, x, y
    while e > 0:
        if e % 2 == 1:
            r *= b
        b *= b
        e //= 2
    return r
```

For exact integers and nonnegative exponent, use $r b^e=x^y$ and $e\ge0$, with immutable original $x,y$. In this algorithm the exponent-zero value is defined as one, including $x=0$. If old $e=2k$, the new product is $r(b^2)^k=r b^{2k}$. If old $e=2k+1$, it is $(rb)(b^2)^k=r b^{2k+1}$. The update of the accumulator must use the old base. At exit $e=0$, the invariant gives $r=x^y$.

For positive $e$, floor halving strictly decreases it. For $y>0$, the number of loop iterations is $\lfloor\log_2 y\rfloor+1$; the number of accumulator multiplications is the population count of $y$ in binary. This displayed implementation squares the base once per iteration, including the final iteration. An optimized implementation may avoid that last square without changing the result.

The unnecessary final square also matters to machine safety. With a signed 32-bit type, base 50,000 and exponent one, the mathematical result 50,000 is representable, but squaring the base creates 2,500,000,000, beyond the signed positive range. Thus representability of the final answer alone does not prove safety of every intermediate operation.

For modulus $M\ge1$, reduce the initial base and each product modulo $M$, initialize $r=1\bmod M$, and replace equality by congruence. The same even/odd proof establishes the residue. When $M=1$, the result is zero even for exponent zero. In a narrow machine type, multiplying two residues may overflow before reduction; modular algebra does not justify an unsafe intermediate product. Exact arithmetic, a sufficiently wide intermediate, or a proved overflow-safe modular multiplication routine is required.

## Certificates and choosing a proof method

A **certificate** is additional information that lets a verifier check a claimed result. It need not reveal how the result was found. For sorting, check nondecreasing order and multiset preservation; checking only order accepts a constant array. A permutation of original record indices provides a direct witness that every input record appears exactly once. Its indices must be distinct, in range and consistent with the claimed output values.

For a finite weighted directed graph, a shortest-path certificate illustrates the difference between feasibility and optimality. Suppose all vertices under discussion are reachable from root $s$. Supply distances $d$, a parent chain ending at $s$ for every other vertex, and $d(s)=0$. Each parent edge must exist and satisfy $d(v)=d(parent(v))+w(parent(v),v)$. Every graph edge must satisfy:

$$d(v)\le d(u)+w(u,v).$$

Summing these inequalities along any root-to-vertex path gives $d(v)$ no greater than that path's weight. Summing the parent equalities gives an actual path of weight $d(v)$. Together, they establish optimality. The parent relation must be acyclic and reach the root; a zero-weight cycle of parents supplies equalities but no root path. Negative edge weights do not invalidate this certificate argument, but a reachable negative cycle prevents a finite certificate satisfying all edge inequalities. Unreachable vertices require separate reachability and infinity conventions and are outside this finite-distance presentation.

<!-- FIGURE:certificate -->

For a rooted tree, structural induction is often simpler than a mutable-state invariant. For a recursive function, prove each child is smaller in a well-founded measure and use its complete contract, including preservation. For a greedy optimization algorithm, a local invariant can establish feasibility while optimality still requires an exchange or dominance argument. For dynamic programming, correctness requires an induction over the dependency order and proof that the recurrence covers every admissible decision. These are proof-method boundaries; the full greedy and dynamic-programming methods receive their own later chapters.

| Claim | Appropriate evidence | Frequent invalid replacement |
| --- | --- | --- |
| Exact output of an iterative procedure | State invariant, exit implication and termination | A runtime recurrence |
| Recursive correctness | Base cases, smaller children and composition lemma | A trace of one recursion tree |
| Optimality | Feasibility plus an upper/lower bound meeting a witness | Feasibility alone |
| Implementation safety | Index, expression and arithmetic-domain checks | Mathematical identities alone |
| Worst-case runtime | Cost model, counted operations and bound | Number of source-code lines |

## Mathematical and conceptual problem bank

The bank contains four authentic examination translations and 48 original or independently worded course-derived problems. Questions require exact calculations, formulas, boundary analysis and proof obligations. Full solutions are expandable for reading convenience and open automatically for printing. Original difficulty labels are qualitative medium/hard judgments; they are not measured student-performance statistics. Cross-topic authentic items are used to develop output, index and structural certificates, not relabeled as questions explicitly asking for Hoare logic.

<!-- INCLUDE:problems -->

## Complete summary and examination notes

<!-- INCLUDE:review -->

## Binary-search proof laboratory

The laboratory shows every checkpoint, the unresolved interval, the classified regions and the termination measure. Compare the correct update with a deliberately faulty update on a one-element interval. A reported counterexample refutes that implementation; bounded examples do not replace the general proof above. The laboratory admits only sorted integer inputs within an exact, bounded arithmetic range.

<!-- LAB:search -->

## References and attribution

1. Frank Pfenning. **15-122 Principles of Imperative Computation, Lecture 2: Contracts**, Carnegie Mellon University, 13 January 2011. [Complete written lecture](https://www.cs.cmu.edu/~wlovas/15122-r11/lectures/02-contracts.pdf). Read all 24 PDF pages. Course-derived tasks address the lecture's exponentiation derivation and Exercises 1–2; they are independently worded rather than copied.
2. Mike Gordon. **Specification and Verification I**, University of Cambridge, Part II lecture notes, 2010 course archive. [Lecture notes](https://www.cl.cam.ac.uk/archive/mjcg/Lectures/SpecVer1/Notes/Notes.pdf). Read PDF pages 11–28, 47–59 and 63–72. Relevant task origins include Exercises 41, 42, 44, 45 and 53 and the array-assignment discussion. Original assignments and constants differ where indicated.
3. Eric Lehman, F. Thomson Leighton and Albert R. Meyer. **Mathematics for Computer Science**, 2015; MIT 6.042J, Spring 2015, Albert Meyer and Adam Chlipala. [Written course text](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf). Read §5.4, PDF pages 140–152. State-machine, reachability and termination problems are independently developed from the reviewed concepts.
4. **CS161 Design and Analysis of Algorithms, Winter 2022, Lecture 2 notes**, Stanford University. [Written lecture](https://stanford-cs161.github.io/winter2022/assets/files/lecture2-notes.pdf). Read PDF pages 1–4. The notes credit adaptation from Virginia Williams and contributions by Michael Kim, Ofir Geri, Mary Wootters and Aviad Rubinstein; they invite corrections to Moses Charikar and Nima Anari. Insertion and merge proof tasks are independently worded and complete the boundary cases left implicit in the lecture scaffold.
5. **Iranian MSc and PhD examination archive**, immutable repository revision `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`. Authentic items below identify booklet, year, field, PDF page and question. English translations retain option order. Solutions are independently derived and are not represented as official keys.

The proofs establish the stated claims under their explicit mathematical and implementation assumptions. The source pool and finite checks do not establish universal coverage of every course or guarantee performance on unseen questions. [Read the chapter quality audit](../reviews/a_correct-quality.html).
