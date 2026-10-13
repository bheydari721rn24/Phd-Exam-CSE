## Chapter summary and detailed examination decisions

A complete solution states its domain and transition, chooses a certificate for the requested conclusion, proves its actual obligations, and uses the correct final condition. The following decisions supplement the full lesson and forty-nine derivation tutorials. They do not replace those proofs. Exact arithmetic, finite data and stated guards remain part of every formula's scope.

### 1. Identify the claim before choosing an invariant

Reachability asks whether at least one finite legal path exists. Safety asks whether every reached state obeys the property. Universal termination excludes every infinite execution. These are different quantifiers: a goal can be reachable while another execution loops forever. State zero with both a self-loop and an edge to a goal is a concrete example. A safety coloring alone cannot force an enabled exit to be chosen.

### 2. Record the complete state and checkpoint

The same variable values at two program locations can permit different next operations. Include the control location when needed, and give original inputs fixed names. For addition followed by increment, the loop-head sum excludes the next indexed entry; after addition it includes that entry while the index is still old. Using an equality from the wrong location makes a correct arithmetic formula an incorrect program invariant.

### 3. Initialization and preservation are independent

An inductive certificate $J$ requires $I\subseteq J$ and $\operatorname{Post}(J)\subseteq J$. The empty set is always closed but fails initialization when an initial state exists. The full state set is initialized and closed but proves no useful exclusion by itself. To obtain safety $Q$, also show $J\subseteq Q$. A zero-edge violating prefix can already occur when initialization fails.

### 4. A bad closure edge need not be a reachable violation

For transitions $0\to1$ and $2\to3$ from initial zero, $P=\{0,1,2\}$ holds on the reachable set yet fails closure at two. The counterexample is an edge from an unreachable candidate state. Strengthening to $\{0,1\}$ removes it and gives an initialized closed certificate. Rejecting the original certificate does not establish that safety itself is false.

### 5. Compute closure in the correct direction

Forward iteration adds successors to the initial set and returns the least initialized closed set. Backward safe deletion removes states with any escaping successor and returns the greatest closed subset of the permitted region. Universal safety holds exactly when the initial set lies in that latter fixed point. A safe dead end remains in it; a successful computation requires a separate terminal-state specification.

### 6. Intersections and unions preserve forward closure; complements may not

For two closed sets, a successor of a state in their intersection remains in both, and a successor from their union remains in at least the operand that contained its predecessor. An incoming edge to a closed set becomes an escaping edge from its complement, so complement closure fails in general. Weakening can also admit extra bad predecessors. Logical implication between predicates does not automatically transfer the stronger predicate's closure to the weaker one.

### 7. Derive an exact or modular change for every permitted move

For an additive move vector $v$, a linear conserved weighting satisfies $w^Tv=0$; a residue weighting satisfies $w^Tv\equiv0\pmod m$. All generators and orientations must pass. In the two-generator lattice example, the exact nullspace is trivial but a nonzero modulo-five weighting exists. A modular obstruction can therefore contain information absent from all exact linear sums. Composite moduli require checking invertibility before field-style elimination.

### 8. Equal conserved values give candidates, not automatically paths

Different conserved values prove impossibility. Equal values require a constructive converse or another completeness argument. Signed lattice coefficients give paths only when reverse moves and the state domain permit them. Under nonnegative guards, intermediate states must also be legal. A drawing of two endpoints with matching colors does not prove the connecting move sequence exists.

### 9. Distinguish a conserved quantity from an affine recurrence

For $d'=2d+1$, the difference changes by $d+1$; it is not constant. The transformation $u=d+1$ makes the update $u'=2u$, which simplifies solving it but still describes growth. Under $(a,b)\mapsto(2a+1,2b)$ with $b\ne0$, $(a+1)/b$ is genuinely conserved. Keeping the affine constant is necessary for exact values such as $a_t-b_t=n2^t-1$.

### 10. Coloring arguments must check every allowed placement

A domino covers one square of each checkerboard color in either orientation. Removing two same-color corners from an eight-by-eight board leaves thirty versus thirty-two squares and makes a covering impossible despite even area. For other tiles, compute every allowed orientation's weight. If a permitted placement changes the supposed conserved difference, the proposed coloring does not certify the stated problem.

### 11. Flipping an even number preserves parity, not the count

Flipping $k$ selected coins of which $h$ show heads changes the total heads by $k-2h$. For even $k$ the change is even, but can be positive, negative or zero. With odd $k$, head parity flips at each move instead of remaining a state invariant. This distinction prevents turning a residue fact into an incorrect monotonicity or termination claim.

### 12. Permutation parity and inversion descent have different strengths

An adjacent swap of distinct values changes inversion parity. A three-cycle uses two swaps and preserves parity, but may leave the numerical inversion count unchanged. Equal values invalidate the distinct-value flip argument. In a sliding puzzle, a vertical blank move crosses width-minus-one numbered entries; even width therefore needs inversion parity combined with blank-row parity. An odd-width board preserves numbered inversion parity alone.

### 13. Partial correctness needs a real exit consequence

For a loop-head invariant $J$ and guard $G$, establish setup, valid body operations, preservation and $J\land\neg G\Rightarrow Q$. A prefix-sum equality becomes the full sum only when the bounds and false guard force the final index. Partial correctness constrains completed executions; a divergent routine may satisfy it vacuously. Termination of the body and a well-founded progress argument are additional requirements for total correctness.

### 14. Sequential assignments read the updated state

In `a=b; b=a%b`, the remainder uses the new first argument and becomes zero. This is not Euclid's simultaneous $(a,b)\leftarrow(b,a\bmod b)$ transition. For the latter, common divisors are preserved and the second argument decreases. Save old values or use a genuine parallel assignment before applying a simultaneous-update proof. Do not reject a correct old-value program based on an imagined overwrite order either.

### 15. A natural rank supplies an upper bound; extra conditions supply an exact count

Strict descent in nonnegative integers limits ranked transitions by the initial rank. If every step lowers it by exactly one, the terminal rank is zero, and every positive rank enables a terminating step, the length equals the initial rank. A deadlock at positive rank would destroy equality while preserving the upper bound. A rank counts its transitions, not uncounted operations inside the body.

### 16. Exclude all three false descent arguments

Weak descent in naturals permits a constant self-loop. Strict descent in unrestricted integers permits $0,-1,-2,\ldots$. Strict positive-real descent permits $1,1/2,1/4,\ldots$. Each can run forever. A real quantity with a lower bound and a uniform decrease at least a fixed positive amount does give a finite step bound; merely having some positive decrease at each step is insufficient.

### 17. Lexicographic priority permits secondary resets

For natural pairs, a smaller primary component makes the pair smaller regardless of the new secondary component. When the primary is unchanged, the secondary must strictly decrease. This proves termination with arbitrary finite resets even when the sum rises. All executions from one fixed start can be finite while their possible lengths are unbounded if reset branching is unbounded. The reset system does not have a finite uniform natural rank at that start.

### 18. Derive a scalar weight from an actual reset bound

If the secondary reset is at most $B$, rank $(B+1)i+j$ decreases on both ordinary decrements and primary resets. An arbitrary unbounded reset cannot be absorbed by choosing one large constant. For a process creating $B$ future decrements per primary step, the same weight prices those future decrements plus the current primary action. The weighted rank explains how one component may grow while total remaining work decreases.

### 19. Finite cycles decide termination; failed ranks do not

In a finite reachable graph, a directed cycle allows an infinite repeated execution, and any infinite execution revisits a state. Absence of reachable cycles is therefore equivalent to universal termination. An acyclic graph admits a rank equal to the longest remaining path to a sink. An unreachable self-loop does not invalidate termination from the fixed initial state. A globally failing rank must not be confused with a failing reachable-state termination theorem.

### 20. Fix powering base and final-square conventions before counting

For positive exponent $n$, positive halving iterations number $\ell=\lfloor\log_2n\rfloor+1$, and odd iterations number $p=\operatorname{popcount}(n)$. An always-square iterative routine executes $\ell+p$ multiplications. Skipping the final unused square subtracts one. A recursive routine with direct zero and one bases and a single reused half-result uses $\ell+p-2$. At zero the separate count is zero; none of the logarithmic formulas is evaluated there.

### 21. A recursive call must stay in the domain and get smaller

A natural-number exponent routine calls an integer quotient, not a real half. Repeated real halving from one never reaches exact mathematical zero and invalidates its natural-domain proof. Negative factorial inputs likewise require another domain. Multiple smaller calls can terminate while creating exponential work. A visible base clause does not show that every input reaches it or that all overlapping mathematical clauses agree.

### 22. Structural induction follows every constructor

Each base constructor gives a proof case; each recursive constructor gives hypotheses for all of its recursive components. A two-child tree may need both hypotheses. Finite-data generation excludes infinite lazy objects unless they are explicitly part of a different model. For a two-argument theorem, induction on the first argument with the second universally quantified can suffice. Product induction still requires a justified smaller-pair relation.

### 23. Generalize the helper over the accumulator it actually receives

The reversal helper calls itself with a nonempty changed accumulator. The statement only at the empty accumulator cannot justify that call. Prove $revAcc(L,A)=rev(L)\Vert A$ for every $A$, then specialize to empty. The accumulator is a suffix of the eventual result here. Swapping it to the front changes the specification and generally makes it false; associativity permits regrouping, not arbitrary list reordering.

### 24. Output order differs from evaluation order

Right-first tree-helper evaluation constructs the suffix before the left values are prepended, producing left-to-right output. A recursive sorting routine can evaluate either child first while still joining greater block, pivot and smaller block to obtain descending order. For pure calls the specified joining order controls the result. Side effects or bindings require another semantics and can invalidate simple equational rearrangement.

### 25. Count allocated linked cells separately from result length and peak space

Append copies its first linked list and can share the second. Naive reversal allocates $n(n+1)/2$ cons cells over its execution, whereas accumulator reversal allocates $n$. Those counts do not say all allocated cells are live simultaneously. Tail recursion avoids pending work only when the implementation eliminates tail calls. Python array slicing and concatenation copy data and do not inherit constant-time cons/tail assumptions.

### 26. Use the actual internal-node arities in leaf accounting

For a finite nonempty rooted tree, $L=1+\sum_{v\text{ internal}}(d(v)-1)$. A binary internal node contributes one net leaf, a ternary node two, and a unary node zero. Full $k$-ary trees give $L=(k-1)I+1$. Edges equal vertices minus one only under the tree hypotheses; a forest changes the constant, and cycles change the equation. Neither height alone nor total edges alone is the requested leaf count.

### 27. Binary leaf weights have a stronger exact deficit formula

With root depth zero and leaf weights $2^{-d}$, the sum is at most one. The deficit is the sum of $2^{-d(u)-1}$ over unary vertices. Missing-child losses are positive, so equality holds exactly for finite full binary trees. Unequal leaf depths do not by themselves imply strict inequality. An empty tree requires a separate root/mass convention; ordinary data leaves must not be replaced with external empty child positions.

### 28. Height bounds depend on the base convention

For the empty-or-node representation with empty height zero, stored-node count obeys $N\le2^h-1$. Equality requires both child bounds tight and their heights equal, recursively giving a perfect tree. For a data-leaf height-zero full binary representation, the total-node bound is $2^{h+1}-1$. The shifted exponent is explained by the different base constructor, not by contradictory mathematics.

### 29. Recursion depth, leaves and total calls are distinct counts

A complete ternary call tree of depth $n$ has $3^n$ leaves, $(3^n-1)/2$ internal calls and $(3^{n+1}-1)/2$ total calls. Sequential child evaluation has at most $n+1$ calls on its active root-to-leaf stack. These counts coincide only in exceptional trivial cases. An irregular call tree needs its actual branch and base structure; a three-branch statement alone does not justify complete levels of equal depth.

### 30. Prove residue cycles on a complete finite state

An order-two recurrence requires a pair of consecutive residues. A returned pair under a deterministic transition proves a repeated cycle. The starting indices determine its phase. For qualifying multiples of $q$ in inclusive indices $L$ through $U$, the count is $\lfloor U/q\rfloor-\lfloor(L-1)/q\rfloor$. A final partial period may contribute several terms and must be inspected. Huge-index parity can be solved without calculating the huge integers themselves.

### 31. Nested and mutual recursion need joint specifications

For mutual parity routines, include correctness and termination of both routines in the induction predicate, or use an input/phase rank. For nested Ackermann calls, first establish that the inner call terminates and returns a natural in the outer call's domain. The outer first coordinate is smaller even if its second grows. Fix the exact variant's base equations: standard $A(1,5)=7$ and the specified alternative $B(1,5)=32$ are both correct for different functions.

### 32. Well-defined object functions require representation independence

A cost attached to finite derivation trees can terminate while assigning different costs to the same generated string. Concatenating two empty strings with an extra construction cost conflicts with the zero-cost empty base. Either make the derivation the input or prove equations independent of representation. Structural induction can prove membership soundness even for ambiguous generation; completeness separately shows every claimed object has a derivation.

### 33. A simplifier's soundness is not completeness or optimality

For pure exact expression constructors, prove value preservation by structural induction, covering constants, variables, addition, multiplication and negation. A routine deleting an added zero can preserve value yet miss a product by zero or a zero on the other side. The substitution theorem also assumes pure evaluation; duplicating an effectful expression would require more than a numeric identity. A finite test of expressions does not replace the constructor proof.

### 34. Report the exact scope of mathematical and visual checks

Finite exhaustive tests certify the enumerated state space and can expose errors in proposed general arguments. They do not supply an unproved universally quantified preservation step. A model showing one guarded witness establishes that path; a model aggregating level counts must say it is an aggregate. Formula checks, actual control checks, source-page verification and inspected layouts address different failure modes. Keep unfinished drafts distinguishable from checked editions and preserve the recorded limitations.
