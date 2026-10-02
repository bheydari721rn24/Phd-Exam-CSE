# Invariants and Recursive Reasoning

## Sources, prerequisites, and the chapter boundary

This chapter develops a single reasoning discipline: describe how an object or a computation is built, identify the information that each construction step must preserve, and justify the conclusion by induction over those steps. The objects may be program states, lists, trees, or recursive calls. The conclusion may concern impossibility, a returned value, termination, or an exact quantitative bound. These conclusions require different proof obligations; keeping them separate is essential.

The principal readings are four genuinely reviewed written university courses. Their complementary contributions are summarized here; the [source comparison and exercise ledger](../reviews/d_invariants-sources.html) records the larger candidate pool, exact reading boundaries, corrections, and selection limitations.

| University and course | Written material used | Contribution to the synthesis |
|---|---|---|
| MIT, 6.042J Mathematics for Computer Science | Eric Lehman, F. Thomson Leighton, and Albert R. Meyer, Spring 2015 textbook, Section 5.4 and Sections 6.1–6.4 | Transition systems, invariant proofs, derived variables, well-founded progress, recursive definitions, and expression substitution |
| Stanford, CS161 Design and Analysis of Algorithms | Mary Wootters's Spring 2017 course; Jessica Su, Section 1: Loop and Recursion Invariants | The connection between induction, merging, loop assertions, and recursive exponentiation |
| Carnegie Mellon, 15-150 Principles of Functional Programming | Michael Erdmann, Spring 2026 structural-induction and list-reversal notes, linked from the lecture archive | Constructor-by-constructor proofs, totality, accumulator generalization, and tree flattening |
| Cambridge, Foundations of Computer Science | Lawrence C. Paulson, 2013 course notes, recursion, lists, and binary-tree sections | Evaluation traces, implementation costs, tail recursion, and distinctions between empty trees and data-bearing leaves |

Cornell CS2800 supplements the comparison of induction on one argument with induction on pairs. Berkeley CS70 supplements hypothesis strengthening. Princeton COS226 supplies an independently checked merge implementation and a comparison-count question. These supplements do not replace the four principal courses.

**Prerequisites.** Read the approved [proof chapter](d_proof.html), [induction chapter](d_induction.html), [relations chapter](d_relations.html), and [functions chapter](d_functions.html). You should understand implication, universal quantifiers, relations, function domains, and ordinary and strong induction. The present chapter restates the exact principles it needs and extends them to computations and recursively constructed data. The approved [loop chapter](a_loop.html) provides additional algorithm-analysis context.

**Boundary.** We cover reachable states, inductive assertions, conserved quantities, coloring and modular arguments, loop contracts, partial and total correctness, integer and lexicographic rankings, recursion-domain obligations, structural induction, generalized accumulator specifications, mutually recursive definitions, expression-tree substitution, and finite certificate checking. Number-theory algorithms are illustrative applications; divisibility and congruence theory receive their own next chapter. General recurrence-solving methods and complete sorting-algorithm analyses belong to the upcoming algorithms chapters. Tree examples teach proof structure without introducing automata theory. Iranian examination archives remain reserved for the final month.

**How to study.** First read the definitions and proofs through the accumulator section. Then read the worked problems, including the explanations of failed arguments. Finish with the complete review rules and the laboratory. The problems are supplied with full teaching solutions; no diagnostic test is required before instruction. The source boundary is explicit: this chapter does not claim to reproduce every exercise from every course or to guarantee performance on every unseen examination question.

## States, transitions, and reachable configurations

### A state must contain enough information

A transition system consists of a state set $S$, an initial set $S_0 ⊆ S$, and a transition relation $T ⊆ S × S$. We write $s → t$ when $(s,t) ∈ T$. Several initial states allow a program to accept several inputs, and several outgoing transitions allow environmental choices or nondeterministic operations. Determinism means at most one successor per state in this simple model; it does not mean that the state set is finite.

A state must record everything that determines which steps are permitted. For a loop that scans an array, the array and the index alone may be insufficient: the current partial sum and the program location also matter. Immutable input values can be treated as fixed parameters, but a proof must still distinguish them from variables overwritten by the computation. If a program has several control locations, the same numeric variables at different locations can obey different assertions.

An execution prefix is a finite sequence $s_0,s_1,…,s_k$ with $s_0 ∈ S_0$ and $s_i → s_{i+1}$ for each consecutive pair. Its length is the number of transitions, namely $k$, rather than the number of states, which is $k+1$. An infinite execution satisfies the same transition condition indefinitely. A reachable state appears in some finite prefix. Write $R$ for the set of all reachable states.

Define successive approximations by $R_0 = S_0$ and $R_{k+1} = R_k ∪ Post(R_k)$, where $Post(X) = {t ∈ S : ∃s ∈ X, s → t}$. The approximations contain states reachable in at most the indicated number of transitions. Therefore:

<!-- MATH:reachability -->

**Proof.** The initial approximation contains exactly the zero-step states. If a state is already in $R_k$, it remains in the next approximation. A state newly added through $Post(R_k)$ has a predecessor reachable in at most $k$ steps, so it is reachable in at most $k+1$ steps. Conversely, a noninitial state on a prefix of length at most $k+1$ has a predecessor on a prefix of length at most $k$. Induction proves the claim for every approximation, and taking their union gives all finite-prefix reachability.

### The least closed set viewpoint

The reachable set contains $S_0$ and is closed under transitions: $Post(R) ⊆ R$. If another set $J$ contains $S_0$ and is closed under transitions, every approximation $R_k$ lies in $J$, by induction. Consequently $R ⊆ J$. Thus reachability is the **least** transition-closed set containing the initial states. This characterization connects state reasoning with the closure constructions in the relations chapter.

Closure is directional. A transition from a state outside $J$ into $J$ is harmless for forward preservation. A transition from inside $J$ to outside $J$ is a counterexample. Reversing an arrow reverses which proof obligation it threatens.

For a finite graph, breadth-first search constructs $R$ and records a shortest witness path to every reachable state. For an infinite state space, enumerating a few layers is only exploration: absence from those layers is not a proof of impossibility. An invariant compresses the argument for all layers into a finite proof.

## Inductive invariants, safety, and strengthening

### Three assertions that must not be confused

A predicate $P$ on states can be identified with its truth set, also denoted $P ⊆ S$. A **reachable-state property** satisfies $R ⊆ P$. A **preserved predicate** satisfies $Post(P) ⊆ P$. An **inductive invariant** satisfies both initialization $S_0 ⊆ P$ and preservation $Post(P) ⊆ P$. The vocabulary varies across courses; these explicit definitions avoid relying on a single ambiguous word.

The invariant theorem states that every inductive invariant is a reachable-state property. To prove it, consider an arbitrary execution prefix. Initialization proves $P(s_0)$. If $P(s_i)$ holds, the transition and preservation imply $P(s_{i+1})$. Induction on the prefix length proves the assertion at every reachable state. The argument applies to every permitted choice of successor; proving preservation for one favored branch is insufficient.

To establish a safety property $Q$, it is enough to find an inductive invariant $J$ with $J ⊆ Q$. The invariant can contain unreachable states, but those extra states must still pass the preservation obligation. It need not describe reachability exactly.

### A true property can fail the inductive test

Consider four states $0,1,2,3$, initial set ${0}$, and transitions $0 → 1$ and $2 → 3$. The reachable set is ${0,1}$. The candidate $P = {0,1,2}$ is true at every reachable state, but it is not preserved: $2 ∈ P$ and $2 → 3$, while $3 ∉ P$. The failure involves an unreachable predecessor, so it does not disprove the reachable-state property. It shows that this candidate is unsuitable as a direct one-step inductive certificate.

Strengthen the candidate to $J = {0,1}$. It contains the initial state, is closed, and implies the original candidate. The proof now succeeds because the troublesome unreachable predecessor has been excluded.

<!-- FIGURE:closure -->

In practice, strengthening adds an informative equality or bound. If the desired claim is that a partial sum never exceeds a target, an exact description of which input prefix has been summed can make preservation easier. A stronger statement creates a larger obligation to prove, but also provides a more useful hypothesis for the next step.

### Algebra of invariant certificates

If $J$ and $K$ are transition-closed, so are $J ∩ K$ and $J ∪ K$. For intersection, a successor of a state in both sets remains in both. For union, the predecessor is in at least one set, and its successor stays in that set. If both are initialized, their intersection and union are initialized too. Arbitrary intersections of inductive invariants are inductive invariants. The empty intersection is interpreted as $S$, which is always a valid but uninformative certificate.

The complement of a preserved set need not be preserved. For $0 → 1$, the set ${1}$ is closed, but its complement ${0}$ is not. Similarly, an implication between state predicates does not automatically transfer preservation. A weaker assertion may contain extra predecessors that leave it. You must check preservation of the actual predicate being offered.

Initialization and preservation are logically independent. The empty truth set is preserved for every transition relation, but cannot contain a nonempty initial set. The entire state set is initialized and preserved, but excludes no unsafe state. These two examples explain why a correct proof needs both an initialized certificate and a useful consequence.

## Discovering conservation laws and impossibility proofs

### Work from the change, not from a long trace

For a numerical function $F : S → D$, compute the change $F(t) − F(s)$ under each move. An exact conservation law makes this difference zero. A modular conservation law makes it divisible by a modulus $m ≥ 2$. A monotone quantity has a consistently signed change. These possibilities serve different conclusions: a conserved value can exclude a target, whereas a strictly decreasing well-founded value can establish termination.

For a vector state $x ∈ ℤ^d$ and additive moves $x → x+v_j$, a linear expression $F(x) = w ⋅ x$ is conserved if $w ⋅ v_j = 0$ for every permitted move vector. To search systematically, place the move vectors as columns of a matrix $V$ and solve $w^T V = 0$. For a modular invariant, solve the same congruences modulo $m$. Over a prime modulus this is a linear system over a field; over a composite modulus, ordinary field elimination cannot be used without checking divisibility of pivots. The linear-algebra track supplies the general elimination theory.

For example, allow changes $(x,y) → (x+2,y−1)$ and $(x,y) → (x−2,y+1)$ when the resulting coordinates are nonnegative. The expression $x+2y$ changes by $2+2(−1)=0$ in the first move and by $−2+2=0$ in the second. From $(4,3)$, every reachable state therefore satisfies $x+2y=10$. The target $(3,3)$ is excluded because its value is $9$. A target satisfying the equality is only a candidate; the allowed moves may still exclude it through parity, bounds, or directionality.

<!-- FIGURE:conservation -->

### Modular invariants and checkerboard arguments

A robot on $ℤ^2$ that changes both coordinates by either $+1$ or $−1$ preserves the parity of $x+y$. Every change to the sum is $−2$, $0$, or $2$. Starting at $(0,0)$, a state with odd coordinate sum is impossible. Here the invariant happens to characterize reachability: if $x+y$ is even, then $x$ and $y$ have equal parity. Choose a nonnegative integer $k ≥ max(|x|,|y|)$ of this common parity. There are sign sequences of length $k$ summing to each coordinate, because the required numbers of positive steps are $(k+x)/2$ and $(k+y)/2$. Pairing these sequences gives a diagonal walk to $(x,y)$. The constructive converse is an additional proof, not a consequence of conservation alone.

Coloring is a way to assign weights to positions. On an even-sided checkerboard, every domino covers one square of each color. The difference between the numbers of uncovered black and white squares is unchanged when a domino is placed. Removing two same-colored corners leaves a nonzero difference, so a tiling is impossible. Area divisibility alone misses this obstruction: a board may have an even number of available squares and still be untileable.

For more complicated tiles, use three or more colors, or assign signed weights. Compute the total weight of **every permitted placement**, including orientations. A weighting that works only for horizontal placements proves nothing about vertical placements. If each tile has weight zero, a nonzero total board weight excludes a tiling. If each tile has a fixed nonzero weight, compare the required number of tiles and the total board weight instead.

### Permutation parity must be defined before it is used

For distinct entries in a list, an inversion is a pair of positions $i<j$ with the earlier value larger than the later value. Interchanging two adjacent distinct entries changes the inversion count by exactly one. Every other entry has the same combined relationships to those two values; only their mutual ordering changes. Thus an adjacent swap flips inversion parity. A three-cycle can be executed with two swaps and preserves parity. This supplies a compact impossibility proof for puzzles whose legal operations are even permutations.

Duplicates require care. Swapping equal entries changes nothing, so the statement that every adjacent swap flips parity assumes distinct entries. Sliding puzzles also contain a blank: ignoring it changes the numerical list differently for horizontal and vertical moves. The worked bank derives the correct row-and-inversion combination rather than treating the blank as an ordinary numbered tile.

## Loop contracts and total correctness

### Locate the assertion at a definite control point

Consider `while guard: body`. Place the invariant at the loop head, immediately before each guard evaluation. Let $A$ be the precondition, $J$ the invariant, $G$ the guard, and $Q$ the postcondition. The partial-correctness obligations are:

1. Initialization: executing the setup from a state satisfying $A$ establishes $J$.
2. Preservation: every completed body execution from a loop-head state satisfying $J ∧ G$ reaches the next loop head satisfying $J$. Separately check that every enabled execution avoids undefined operations; termination of the body is an additional obligation for total correctness.
3. Exit consequence: $J ∧ ¬G$ implies $Q$.

The body-safety requirement includes valid array indices, defined arithmetic, and appropriate subroutine preconditions. If body execution can itself diverge, the ordinary preservation implication describes completed iterations but does not establish total correctness. To obtain a total-correctness proof, show that each enabled body execution terminates and that a well-founded rank decreases between consecutive loop heads.

A Hoare triple ${A} C {Q}$ states that every terminating execution of command $C$ started in $A$ finishes in $Q$, under partial-correctness semantics. The braces here delimit predicates; they do not denote the singleton set containing a proposition. An infinite loop can satisfy such a triple vacuously while failing to compute a useful answer.

### Assignment reasoning uses the old state

For an assignment `x = E`, a postcondition $Q$ holds exactly when the old state satisfies the predicate obtained by substituting the old-state expression $E$ for the free occurrences of $x$ in $Q$, provided the expression is defined. For example, after `x = x + 1`, the desired postcondition $x ≤ n$ requires old-state $x+1 ≤ n$. It is not enough to assume old-state $x ≤ n$.

Sequential assignments are not simultaneous. For `x = y; y = x`, both final values equal the old value of $y$. For `x, y = y, x`, the pair is exchanged. A proof that needs old values can name them $x_{old}$ and $y_{old}$ or use temporary variables. Deriving an invariant against an imagined simultaneous update is a common source of incorrect proofs.

### A prefix-sum proof with all boundaries

Let the immutable input array be $A$ of length $n ≥ 0$. The program below uses exact integer arithmetic.

```python
def prefix_sum(a):
    total = 0
    i = 0
    while i < len(a):
        total = total + a[i]
        i = i + 1
    return total
```

At the loop head use $0 ≤ i ≤ n$ and the exact statement that `total` is the sum of entries with indices from $0$ through $i−1$. The empty prefix sum is zero. Initialization sets $i=0$ and `total=0`, so both clauses hold. Under the guard, $i<n$; the lower bound proves that `a[i]` is a valid access. Adding that entry extends the prefix by one, and incrementing the index makes the new equality describe the new prefix. The new index is at most $n$.

At exit, $i ≥ n$ from the false guard and $i ≤ n$ from the invariant, so $i=n$ and the sum is complete. The rank $n−i$ is a nonnegative integer at every loop head and decreases by one per body execution. The body consists of terminating arithmetic and assignments, so the loop terminates after exactly $n$ iterations. For the empty array, it performs zero iterations and returns the empty sum. No claim that the running total increases is needed; negative array entries are allowed.

<!-- MATH:prefix -->

If machine arithmetic wraps, the exact integer equality may no longer hold. One can either prove that no intermediate sum overflows or state the specification modulo the machine word size. An arithmetic model is part of the theorem, not a formatting detail.

### Postconditions suggest useful invariants

Start from what the final answer must mean, replace the completed object with a processed prefix or smaller subproblem, and state the relationship between processed and remaining work. A weak assertion such as “the output is sorted” may be preserved while allowing the program to lose every input element. A sorting or merge proof also needs a multiplicity-preservation condition. A search proof needs a statement locating every possible answer in the current candidate interval, not merely a bound on the interval's endpoints.

Ghost variables are immutable snapshots or proof-only state used to describe the original input. They help write a relation between changing values and their initial counterparts. If an auxiliary variable is updated during a proof, its updates must be specified and proved; calling it a ghost does not make arbitrary assertions true.

## Monovariants, rankings, and termination

### Strict progress and the right codomain

A ranking function $ρ$ maps relevant states to a well-founded order and strictly decreases on each enabled transition. For integer ranking, $ρ : J → ℕ$ and $ρ(t)<ρ(s)$ whenever $s ∈ J$ and $s → t$. Initialization and preservation ensure that every reached state remains in the domain where the ranking obligations hold.

**Termination theorem.** If an infinite execution existed, its ranks would form an infinite strictly descending sequence in a well-founded order, contradicting well-foundedness. Therefore no infinite execution is possible. For a nonnegative integer rank, every transition reduces the rank by at least one. A prefix of length $k$ therefore satisfies $ρ(s_k) ≤ ρ(s_0)−k$, giving $k ≤ ρ(s_0)$. This is a bound on the number of ranked transitions, not automatically on the number of arithmetic operations inside a transition.

There are three distinct failure modes. A weakly decreasing rank may stay constant forever. A strictly decreasing integer rank with no lower bound may decrease through negative integers forever. A strictly decreasing positive real rank may approach zero forever, as in $1,1/2,1/4,…$. The conclusion requires strict descent **and** a well-founded range; positivity alone does not suffice.

A uniform real decrease of at least a fixed $ε>0$ repairs the third situation when the rank has a lower bound $L$. After $k$ transitions, its value is at most $ρ(s_0)−kε$ and at least $L$, so $k ≤ (ρ(s_0)−L)/ε$. The existence of some positive decrease at each step, without a fixed lower bound on that decrease, is weaker and insufficient.

### Lexicographic descent allows resets

Define $(a',b') <_{lex} (a,b)$ if $a'<a$, or if $a'=a$ and $b'<b$. On $ℕ^2$ this order is well-founded. Suppose there were an infinite descending chain. Its first coordinates could decrease only finitely often, because they are nonnegative integers. Eventually the first coordinate would be fixed, forcing the second coordinate to decrease infinitely often in $ℕ$, which is impossible.

Thus a process may reduce a primary counter and reset a secondary counter to an arbitrarily large nonnegative value, provided steps that keep the primary counter fixed strictly reduce the secondary counter. The sum of the counters need not decrease. This is the correct reasoning for nested progress, many recursive definitions, and the resetting robot below.

Consider state $(y,x) ∈ ℕ^2$. A step may decrease $x$ by one when $x>0$, or decrease $y$ by one and assign any nonnegative integer to $x$ when $y>0$. The pair $(y,x)$ strictly decreases lexicographically at every step. Every maximal execution therefore terminates at $(0,0)$, because that is the only state with no permitted move. From $(1,0)$, however, a reset can choose an arbitrarily large $x$. There is no uniform finite bound on all execution lengths from that fixed initial state.

<!-- FIGURE:lexicographic -->

This example separates **every execution is finite** from **all executions have one common finite length bound**. The separation uses unbounded branching at the reset. It also explains why no natural-valued rank decreasing by one can certify every transition from the fixed start: such a rank would impose the missing uniform bound. Lexicographic rankings prove termination without claiming that bound.

If the secondary counter has a known upper bound $B$ whenever it is reset, the scalar rank $(B+1)y+x$ does decrease. A primary decrease lowers its first term by $B+1$, whereas the reset can increase the secondary term by at most $B$. Without that reset bound, selecting a large constant weight is unjustified.

### Termination, deadlock, and fairness

A finite maximal execution ends at a state with no enabled outgoing step. This can be a successful halt or an unintended deadlock. A ranking argument alone does not prove that its terminal state has the desired answer. Add an invariant and an exit characterization, or a progress theorem showing that every non-goal state has an enabled move.

Likewise, the existence of a path to a goal does not mean all choices reach it. A system can offer both an exit edge and an endlessly repeatable self-loop. Proving eventual exit requires excluding the loop or imposing a precise fairness assumption. Fairness is an assumption on executions, not an invariant derived automatically from the state graph. Our termination certificates quantify over all permitted choices and do not silently assume fairness.

## Recursive calls: domains, measures, and specifications

### Prove that recursion is legitimate before using its answer

A recursive definition needs a declared domain, sufficient base cases, domain-preserving recursive arguments, and a well-founded dependency relation. A base case written somewhere in the program does not ensure that every input reaches it. For `f(n)=f(n+1)` with a base value at zero, positive inputs move away from the base forever.

For a recursive function with input $x$, choose a measure $μ(x)$ and show that each recursive argument $y$ satisfies $μ(y)<μ(x)$. Also show that $y$ meets the recursive call's precondition. Strong induction on the measure then permits assuming termination and the full specification for those smaller calls. The specification should describe the result for **every valid input**, not merely for the original top-level value.

For example, if a routine halves a nonnegative integer, the recursive input must be an integer quotient. Replacing it by ordinary real division changes both the domain and the termination argument. At $n=1$, repeated real halving never reaches exact zero in a mathematical real-number model. Similarly, a factorial routine that stops only at zero is not total on negative integers.

### Recursive exponentiation, including zero

For a scalar $a$ and nonnegative integer $n$, define exponentiation recursively with the convention $a^0=1$, including the computational empty-product convention when $a=0$.

```python
def power(a, n):
    # Precondition: n is a nonnegative integer.
    if n == 0:
        return 1
    q = n // 2
    half = power(a, q)
    if n % 2 == 0:
        return half * half
    return a * half * half
```

For $n>0$, the integer $q=⌊n/2⌋$ satisfies $0 ≤ q<n$, so every call is in the domain and has smaller measure. Strong induction can therefore assume that the recursive call terminates and returns $a^q$. If $n=2q$, squaring gives $a^{2q}=a^n$. If $n=2q+1$, the extra multiplication by $a$ gives $a^{2q+1}=a^n$. The zero case returns the specified identity element. These arguments prove total correctness under exact arithmetic.

The recursive result is computed **once** and reused. Writing the recursive call twice in the even case preserves the returned mathematical value but changes the recursion tree drastically. Correctness and efficiency are separate questions. Unit-cost arithmetic gives logarithmic call depth for the shared-result version. Integer bit complexity also depends on the growing operand lengths, and Python's finite stack limit can interrupt a mathematically terminating recursion on sufficiently large inputs.

### Iterative exponentiation exposes a conserved obligation

An iterative version keeps `result`, `base`, and `exponent`, initialized to $1,a,n$. Its loop invariant is $result ⋅ base^{exponent}=a^n$, with `exponent` nonnegative. In an odd step, first multiply `result` by the old `base`; then square `base` and replace `exponent` by its integer quotient by two. In an even step, leave `result` unchanged and perform the same squaring and halving.

For an old exponent $2q$, the new expression is $result ⋅ (base^2)^q$, equal to the old expression. For an old exponent $2q+1$, it is $(result ⋅ base) ⋅ (base^2)^q$, again equal to the old expression. At exponent zero, the invariant yields $result=a^n$. Halving a positive exponent strictly decreases it in $ℕ$, proving termination. A proof must use the old base in the odd multiplication; squaring it first without saving it changes the program.

## Structural induction and recursive data

### Constructors specify both data and proof cases

A recursively generated set is the **smallest** set containing its base objects and closed under its constructors. The smallest-set clause excludes arbitrary extra objects and infinite objects that cannot be produced by a finite construction. For finite lists over a set $E$, use the empty list $[]$ and the constructor $Cons(x,L)$ for $x ∈ E$ and an existing finite list $L$.

To prove $P(L)$ for every finite list, prove $P([])$, then prove $P(Cons(x,L))$ for arbitrary $x$ under the hypothesis $P(L)$. This works because every list has a finite constructor derivation. A proof by induction on the number of constructors gives a formal justification. For a constructor with two recursive arguments, both hypotheses are available and both may be needed. For several constructors, each constructor produces a separate proof obligation.

Parameters that are not reduced by the recursive definition should remain universally quantified. To prove a concatenation identity, induction on the first list can use a predicate of the form “for every second list, the identity holds.” Inducting on both lists is sometimes valid, but is not mandatory. If both can shrink, justify the product induction using a measure such as the sum of their lengths, or use a well-founded product order with explicit hypotheses.

### List operations and their defining equations

Let $L ⧺ M$ denote list concatenation. Define $[] ⧺ M=M$ and $Cons(x,L) ⧺ M=Cons(x,L ⧺ M)$. Define length by $len([])=0$ and $len(Cons(x,L))=1+len(L)$. Both functions terminate on finite lists because their recursive calls use the proper tail of the first list.

**Length theorem.** For all finite lists $L,M$, $len(L ⧺ M)=len(L)+len(M)$. Induct on $L$, keeping $M$ arbitrary. The empty case gives $len(M)=0+len(M)$. For the constructor case, the defining equation gives $1+len(L ⧺ M)$, the hypothesis gives $1+len(L)+len(M)$, and the length definition gives the required equality for $Cons(x,L)$.

**Associativity theorem.** For all finite lists $L,M,N$, $(L ⧺ M) ⧺ N=L ⧺ (M ⧺ N)$. The empty case reduces both sides to $M ⧺ N$. In the constructor case, the left side reduces to $Cons(x,(L ⧺ M) ⧺ N)$. The induction hypothesis identifies its tail with $L ⧺ (M ⧺ N)$, and the concatenation equation identifies the resulting list with the right side. This theorem is used later in accumulator proofs; a proof must not invoke it before establishing it.

Right identity $L ⧺ []=L$ also follows by induction on $L$. Left identity is a defining equation, whereas right identity is a derived theorem. Concatenation is not commutative: $[1] ⧺ [2]=[1,2]$ and $[2] ⧺ [1]=[2,1]$ differ. Associativity permits regrouping, never arbitrary reordering.

### Two binary-tree conventions

A leaf-labeled full binary tree is either $Leaf(v)$ or $Node(L,R)$. Every internal node has two children; leaves carry data. Define the number of internal nodes $I$, the number of leaves $L_f$, and total nodes $N$ by the corresponding base and constructor equations. At a leaf, $I=0$, $L_f=1$, and $N=1$. At a node, $I=1+I(L)+I(R)$, $L_f=L_f(L)+L_f(R)$, and $N=1+N(L)+N(R)$.

Structural induction proves $L_f=I+1$. For the constructor, substitute $L_f(L)=I(L)+1$ and $L_f(R)=I(R)+1$, obtaining $L_f=I(L)+I(R)+2=I+1$. Hence $N=2I+1=2L_f−1$. These identities depend on the full-binary condition; a node with only one child changes the count.

<!-- FIGURE:tree -->

Cambridge also uses a different type: an empty tree or a node with a stored label and two possibly empty children. For that type, data-node count is zero at the empty tree, and the number of **external empty child positions** is one there. The same arithmetic gives external positions equal to data nodes plus one. An external empty position is not a data-bearing leaf. For example, a single stored root has two external empty children, but only one ordinary nonempty leaf.

Height conventions must be stated. For the empty-or-node type, take $h(Empty)=0$ and $h(Node(v,L,R))=1+max(h(L),h(R))$. Induction gives $N ≤ 2^h−1$. In the constructor case, each child has height at most $h−1$, so each has at most $2^{h−1}−1$ data nodes; adding the root gives the bound. For a leaf-labeled full tree with a data leaf of height zero, the corresponding total-node bound is $N ≤ 2^{h+1}−1$. The change in the base convention explains the changed exponent.

### Ambiguity of construction is a mathematical issue

Structural induction proves properties of all finite derivations even when an object has several derivations. Defining a function by assigning a value to each derivation is more delicate: every derivation of the **same object** must yield the same value. Unique constructor decomposition makes this consistency automatic; an ambiguous representation requires a separate independence-of-representation proof.

For instance, let a generated set contain the empty string and permit concatenating two generated strings. A proposed construction-cost function with value zero on the empty string and value $1+c(s)+c(t)$ on a concatenation is inconsistent on strings: concatenating the empty string with itself produces the empty string, but assigns cost one. The equations define a cost of a derivation tree, not a well-defined cost of the resulting string. Clarifying the domain repairs the ambiguity; pretending that every representation is unique does not.

## Generalized specifications and accumulator proofs

### The reason an apparently stronger statement is easier

Define reversal by $rev([])=[]$ and $rev(Cons(x,L))=rev(L) ⧺ [x]$. Define an accumulator helper by $revAcc([],A)=A$ and $revAcc(Cons(x,L),A)=revAcc(L,Cons(x,A))$. The intended wrapper calls the helper with an empty accumulator.

Trying to prove only $revAcc(L,[])=rev(L)$ gives an induction hypothesis about an empty accumulator. In the constructor case, the recursive call has accumulator $Cons(x,[])$, so that hypothesis cannot be applied. The remedy is to prove, for **every** finite accumulator $A$:

<div class="formula-block">$revAcc(L,A)=rev(L) ⧺ A$.</div>

Induct on $L$, keeping the quantifier over all accumulators inside the predicate. The empty case gives $A=[] ⧺ A$. In the constructor case, apply the hypothesis to the changed accumulator $Cons(x,A)$, obtaining $rev(L) ⧺ Cons(x,A)$. Since $Cons(x,A)=[x] ⧺ A$, associativity rewrites this as $(rev(L) ⧺ [x]) ⧺ A$, which is $rev(Cons(x,L)) ⧺ A$. Setting $A=[]$ only after the general theorem yields correctness of the wrapper.

The proof explains how to discover the statement: describe what the helper means for an arbitrary accumulator, including its position relative to the remaining result. Swapping the order to $A ⧺ rev(L)$ is generally false. The accumulator is an output suffix here, even though new input elements are consed onto its front.

### Tree flattening needs the same generalization

For a leaf-labeled full tree, define $flatten(Leaf(v))=[v]$ and $flatten(Node(L,R))=flatten(L) ⧺ flatten(R)$. The order is left-to-right. Define $flatAcc(Leaf(v),A)=Cons(v,A)$ and $flatAcc(Node(L,R),A)=flatAcc(L,flatAcc(R,A))$.

The generalized claim is $flatAcc(T,A)=flatten(T) ⧺ A$ for every tree and accumulator. At a leaf, both sides give $Cons(v,A)$. At an internal node, first apply the hypothesis for the right subtree at $A$, yielding $flatten(R) ⧺ A$. Then apply the left-subtree hypothesis at that whole changed accumulator, yielding $flatten(L) ⧺ (flatten(R) ⧺ A)$. Associativity gives $(flatten(L) ⧺ flatten(R)) ⧺ A$, which is the specified result. Both recursive hypotheses and totality of the intermediate list computation are needed.

The right subtree is evaluated first by this helper in a strict evaluation model, but the result remains left-to-right because the left subtree is placed before the suffix already built from the right. Evaluation order and output order are different concepts.

### State invariants and generalized recursion are two views

In iterative list reversal, after processing an input prefix $P$, the accumulator equals $rev(P)$ and the remaining list is $Q$ with original input $P ⧺ Q$. Equivalently, $rev(Q) ⧺ A$ remains equal to the reversal of the original input. At exit $Q=[]$, so the accumulator is the complete answer. The generalized recursive equation describes what would be returned if execution continued from an arbitrary remaining list and accumulator; the loop invariant describes the relation of that same state to a fixed original input.

Tail recursion means that the recursive call's returned value is returned directly, with no pending operation afterward. It does not automatically mean constant space in every language. Tail-call optimization is an implementation guarantee, and newly allocated output still occupies space. On linked immutable lists, naive reversal repeatedly copies prefixes through concatenation and performs quadratic work; accumulator reversal uses one cons per element and linear work. Python list slicing and concatenation are not constant-time linked-list primitives, so a direct translation using slices has different costs.

## Advanced proof obligations and finite verification

### Mutual recursion needs a joint statement

Suppose `even(0)` is true, `odd(0)` is false, and for positive integers each function calls the other on $n−1$. Prove termination and both parity specifications simultaneously by induction on $n$. The induction hypothesis contains correctness of both functions on $n−1$, so each recursive call is justified. Proving one function while silently using the unproved correctness of the other creates a circular argument.

If one function calls the other on the same numeric input, attach a finite phase to the ranking. For example, a call from phase one to phase zero at the same $n$ decreases $(n,phase)$ lexicographically; a later call reducing $n$ may reset the phase. A cycle of same-size calls with no decreasing phase cannot be justified by saying that “the routines are mutually recursive.”

### Nested recursion and lexicographic induction

Use the standard Ackermann variant $A(0,n)=n+1$, $A(m+1,0)=A(m,1)$, and $A(m+1,n+1)=A(m,A(m+1,n))$ for nonnegative integers. This convention differs from some textbooks' Ackermann variants; compare only after fixing the defining equations.

Induct over lexicographically ordered argument pairs, with the first coordinate primary. The base row returns a natural directly. For a positive first argument and zero second argument, the recursive call has a smaller first coordinate. For both arguments positive, the inner call has the same first coordinate and a smaller second coordinate, so it terminates and returns a natural. The outer call has a smaller first coordinate, so it is smaller regardless of how large that returned natural is. It therefore terminates too. The proof establishes totality on naturals, not a practical resource bound.

For the MIT variant, $B(m,n)=2n$ when $m=0$ or $n≤1$, and $B(m,n)=B(m−1,B(m,n−1))$ otherwise. Exactly the same dependency argument proves totality, with the required natural-valued output included in the induction statement. No fixed weighted sum of the arguments has been assumed to decrease.

### Recursive expression semantics

Let arithmetic expressions be $Const(k)$, $Var$, $Add(E,F)$, $Mul(E,F)$, or $Neg(E)$, with integer constants. Define $eval(E,z)$ by replacing the variable with integer $z$ and interpreting each constructor by its corresponding arithmetic operation. Define $subst(E,H)$ by replacing every variable occurrence in $E$ with the expression $H$ and recursively preserving the other constructors.

The substitution theorem is:

<div class="formula-block">$eval(subst(E,H),z)=eval(E,eval(H,z))$.</div>

Prove it by structural induction on $E$, with $H$ and $z$ arbitrary. For a constant, both sides are that constant. For the variable, both sides are $eval(H,z)$. For addition, evaluate the substituted left and right subexpressions and apply their hypotheses; their sum is precisely evaluation of the original addition under the new variable value. For multiplication, apply the same two hypotheses and multiply the resulting values. For negation, apply the subexpression hypothesis and negate both sides. These are all constructors, so the proof is complete. Finite expression size proves termination of evaluation and substitution.

This theorem uses pure exact integer expressions. If subexpressions have side effects or variable bindings, duplicating a substitution can change behavior or capture variables; a different semantics and additional hypotheses are needed. Such language-semantics extensions are outside this chapter's boundary.

### What an exhaustive finite check can certify

For a supplied finite graph, one can compute reachability exactly, check initialization and preservation for every state and edge, and produce a concrete counterexample path or edge. One can also decide whether any reachable directed cycle exists. A reachable cycle permits an infinite execution by repeatedly traversing it; an infinite execution in a finite graph must revisit a state, yielding a reachable cycle. Thus absence of reachable cycles is equivalent to termination of all executions in this finite model.

Acyclic reachable graphs admit a natural ranking: assign each reachable state the maximum length of a path from that state to a terminal state. Every outgoing edge decreases this value by at least one. The maximum exists because there are finitely many states and no cycle. This construction proves the existence of a ranking even when a proposed user-supplied ranking fails.

For arbitrary infinite systems, finite examples remain error detectors. Testing many inputs does not establish an induction step for all inputs, and failure of one candidate rank does not establish nontermination. The independent audits accompanying this chapter exercise finite edge cases and the actual laboratory implementation; the general results are justified by the proofs above.

## Worked problems with complete teaching solutions

<!-- INCLUDE:problems -->

## Complete summary and examination rules

<!-- INCLUDE:review -->

## Interactive invariant and termination laboratory

The laboratory has four states, a fixed initial state $0$, an editable transition matrix, a proposed truth set, and proposed nonnegative integer ranks. Every result is computed from the displayed graph. It distinguishes a reachable-state property from a one-step inductive certificate, displays a violating path when safety fails, checks each proposed rank edge, and independently detects reachable cycles. Presets include a true but noninductive property, an unsafe transition, an acyclic chain, and a reachable cycle.

<!-- LAB:invariants -->

**Interpretation.** “The supplied rank fails” means that this proposed certificate has a bad edge; another rank may work. “No reachable cycle” is a separate exact termination decision for this finite model. Preservation is checked on every state in the proposed truth set, including unreachable states. Rank checking for termination is restricted to reachable edges, whose scope is displayed explicitly. An unreachable cycle does not create an infinite execution from the initial state.

## References and audit boundary

1. Eric Lehman, F. Thomson Leighton, and Albert R. Meyer. **Mathematics for Computer Science**, MIT 6.042J, Spring 2015. [Textbook](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf), Section 5.4, printed pages 130–144; selected Section 5.4 exercises on printed pages 163–171; Sections 6.1–6.4, printed pages 173–188, and selected structural exercises.
2. Jessica Su. **Section 1: Loop and Recursion Invariants**, Stanford CS161, Spring 2017; course instructor Mary Wootters. [Section notes](https://web.stanford.edu/class/archive/cs/cs161/cs161.1176/Sections/161-section-1.pdf), pages 1–5. [Course archive](https://web.stanford.edu/class/archive/cs/cs161/cs161.1176/).
3. Michael Erdmann, based in part on a draft by Frank Pfenning. **Some Notes on Structural Induction**, CMU 15-150, Spring 2026. [Notes](https://www.cs.cmu.edu/~15150/resources/lectures/04/structural.pdf), pages 1–7. Michael Erdmann, **List Reversal**, [notes](https://www.cs.cmu.edu/~15150/resources/lectures/04/rev.pdf), pages 1–2. [Lecture code](https://www.cs.cmu.edu/~15150/resources/lectures/04/code04.sml). The current archive's code identifies Fall 2026 lecturers Dilsun Kaynar and Stephanie Balzer; the PDF notes retain their own Spring 2026 attribution.
4. Lawrence C. Paulson. **Foundations of Computer Science**, Cambridge Computer Science Tripos Part IA, 2013. [Course notes](https://www.cl.cam.ac.uk/teaching/1314/FoundsCS/fcs-notes.pdf), printed pages 14–24, 26–35, and 56–65; close comparison of recursion, accumulators, list primitives, and the tree equations.
5. Michael George. **CS2800 Discrete Structures**, Cornell, Spring 2017. [Lecture 21: Structural Induction](https://www.cs.cornell.edu/courses/cs2800/2017sp/lectures/lec21-structural.html). The manuscript uses independently checked definitions rather than copying the undefined auxiliary variable in the online concatenation equation.
6. UC Berkeley, **CS70 Discrete Mathematics and Probability Theory**, Fall 2026 course notes. [Note 4: Induction](https://www.eecs70.org/assets/pdf/notes/n4.pdf), pages 1–6, especially hypothesis strengthening on pages 4–6.
7. Robert Sedgewick and Kevin Wayne. **COS226 Algorithms and Data Structures**, Princeton, Spring 2021. [Mergesort slides](https://www.cs.princeton.edu/courses/archive/spring21/cos226/lectures/22Mergesort.pdf), slides 4–9, especially exhaustion guards and the comparison-count question on slides 7–8.

This chapter has been approved by the student. The source audit explains the bounded course search and every selected exercise family. The quality audit records mathematical checks, implementation checks, typography, figure geometry, and remaining limitations. The chapter has not been calibrated against the deferred Iranian examination archive; universal coverage, literal certainty, and performance on all future questions are not asserted.
