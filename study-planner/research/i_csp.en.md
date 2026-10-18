# Constraint Satisfaction, Propagation, and Structured Search

Author-review draft. Read the definitions and proofs before the question bank. A surviving domain value is a possibility under a stated local test; it is not automatically part of a complete solution. All executable examples use the actual domains and relations displayed beside them.

## 1. Written foundations and the chapter contract

This chapter reconciles Stanford CS221 Spring 2026 written CSP modules, Berkeley CS188 textbook CSP material, CMU 15-281 Fall 2025 written notes, MIT 16.410 Fall 2010 constraint lectures by Brian Williams, and the relevant CSP slides of Cornell CS4700 Fall 2013 by Bart Selman. Harvard CS50 AI written CSP and crossword explanations provide an additional implementation comparison. The [source audit](../reviews/i_csp-sources.html) records the bounded candidate pool, exact reading scopes, source errors, unavailable material and the reasons for selecting complementary contributions. A course index or successful download is not counted as actual course reading.

The mathematical core is a finite constraint satisfaction problem. Continuous optimization and arbitrary probabilistic inference are different problems. We introduce weighted factor graphs only after the feasibility problem is clear. The executable reference and laboratory cover finite binary relations; higher-arity/global constraints are taught with separate, explicitly identified models rather than silently passed to a binary solver. Prerequisites are finite sets, relations, elementary graphs, recursion, induction, products and asymptotic bounds. Each new notion is developed here before being used.

The learning target is to translate a statement into exact variables and constraints, distinguish local from global evidence, justify each pruning step, calculate a search or propagation bound under its assumptions, and explain why a completed answer follows. The chapter supplies difficult transfers and original-examination applications. Its finite sources and tests are not a guarantee about every unseen examination question.

## 2. Variables, domains, relations and solutions

A finite CSP has variables $X_1,\ldots,X_n$, finite domains $D_1,\ldots,D_n$, and constraints. A constraint has an ordered scope $(X_{i_1},\ldots,X_{i_k})$ and an allowed relation $R\subseteq D_{i_1}\times\cdots\times D_{i_k}$. Its arity is $k$. A complete assignment chooses one value for every variable. It is a solution exactly when its tuple on every scope lies in the corresponding relation. A domain is a set of allowable values; it is not a single chosen value.

For example, $A,B,C\in\{1,2,3\}$ with $A<B$ and $B=C$ has solutions $(1,2,2),(1,3,3),(2,3,3)$. The first relation is the three-pair table $\{(1,2),(1,3),(2,3)\}$; the second is equality. Listing three independent domains does not permit all $3^3$ tuples after constraints are imposed. Conversely, repeated occurrences of the same variable name do not create additional independent choices.

A partial assignment fixes only some variables. In this chapter it is **locally consistent** when every fully instantiated constraint is satisfied. This is necessary, but not sufficient, for extension to a solution. A **globally extendible** partial assignment has at least one complete solution extension. Keeping those phrases separate prevents the common error of treating a locally legal search node as a promise of eventual success.

The empty assignment is a solution of an empty constraint system with no variables: the empty Cartesian product contains one empty tuple. A variable with an empty domain instead makes a CSP impossible, even if it has no incident edges. A false zero-arity constraint also makes a system impossible; such constants must be checked separately when an implementation supports them. The binary reference accepts explicit variable domains and binary constraints, not zero-arity or general higher-arity input.

## 3. Modeling changes the search space

In $N$-queens, use one variable $Q_i$ per column, with value equal to its row. For distinct columns $i,j$, impose $Q_i\ne Q_j$ and $|Q_i-Q_j|\ne|i-j|$. Column occupancy is built into the representation. There are $N^N$ complete row tuples before testing attacks. For $N=4$, the two solutions are $(2,4,1,3)$ and $(3,1,4,2)$. This is also the coordinate convention used by the board player and the worked questions.

An alternative Boolean encoding uses $N^2$ variables $B_{ij}\in\{0,1\}$. At-most-one constraints alone admit the all-zero board. Exactly-one in each column, together with row/diagonal attack restrictions, supplies the missing occupancy requirement. The Boolean universe has $2^{N^2}$ assignments; a larger universe does not by itself prove slower solving because propagation structure also changes.

For scheduling, an event-variable encoding gives each event one allowed time-slot value and imposes all-different on the event variables. A slot-variable encoding instead assigns an event or an empty marker to each slot and requires every event to occur exactly once. These are equivalent only after the missing occupancy, uniqueness and allowed-slot conditions are all included. Count variables, domain sizes, constraint arities and propagation strength; do not compare encodings only by one of those counts.

<!-- CSP:queens -->

## 4. Constraint graphs and factor graphs

For a binary CSP, a constraint graph has one variable vertex per variable and an edge for each related pair. Unary restrictions can be absorbed into domains first. The edge means that the pair has a relation; it does not mean the relation is symmetric. The ordered table for $A<B$ and the reversed table for testing $B$ against $A$ represent the same constraint viewed from opposite ends.

Several constraints on the same variable pair should be conjoined into one effective relation if the algorithm claims joint pair consistency. Equality and inequality separately both give supports on two identical two-element domains, but their conjunction allows no pair. Testing them separately with different witnesses is a weaker procedure and cannot justify the same deductions as testing their intersection.

A factor graph is bipartite: variable nodes connect to separate factor nodes naming their scopes. A three-variable parity constraint is one arity-three factor. Replacing it by an ordinary triangle of binary projections generally loses information. For even Boolean parity, every two-variable projection is the full binary relation, yet only four of the eight complete triples satisfy parity. The higher-arity relation cannot be recovered from those projections.

## 5. Why assignment order creates redundant paths

Suppose all $n$ domains have size $d$, and temporarily ignore early constraint rejection. A search that chooses any unassigned variable and then a value has branching factors $nd,(n-1)d,\ldots,d$. Its number of complete paths is $n!d^n$. There are only $d^n$ different complete assignments: the extra factor counts all orders of writing the same choices.

Fixing which variable is selected at each node removes that permutation redundancy. The selector may depend on the current domains, as MRV does, provided it returns one unassigned variable and every value needed for completeness is eventually considered. For uniform domains and a fixed variable order, the full tree contains $1+d+\cdots+d^n$ nodes, not merely its $d^n$ leaves. For $d>1$ this sum is $(d^{n+1}-1)/(d-1)$; for $d=1$ it is $n+1$. Constraints can prune the tree but do not change this unconstrained counting argument.

The number of all distinct partial maps of arbitrary scope is instead $\sum_{k=0}^n\binom nk d^k=(1+d)^n$. That set is different from the prefix states visited by one fixed-order tree. Distinguish complete assignments, partial assignments, action-order paths, expanded nodes and primitive relation checks whenever an examination asks for a count.

## 6. Backtracking: invariant, soundness and completeness

Backtracking maintains a locally consistent partial assignment. It chooses one unassigned variable, tries its values, rejects any value inconsistent with earlier choices, recurses and then restores the earlier state before trying a sibling. A complete candidate must satisfy every constraint, including higher-arity constraints whose last variable has just been assigned. A depth-$n$ path supplies a full assignment; hitting a failed branch returns to the nearest choice point with another value available.

**Soundness.** A returned assignment uses domain values and has all variables fixed. Each constraint was checked when its scope became fully assigned, or is checked explicitly at return. Therefore every returned assignment satisfies the original CSP.

**Completeness.** Let $s$ be a solution extending a current node. Whatever unassigned variable is selected, its value in $s$ is among the values to be tried. Checking constraints against $s$ cannot reject that value. Sound filtering cannot delete it either. Induct on the number of unassigned variables to obtain a path to $s$. If every branch fails, no solution exists below that node. For a finite CSP, finitely many choices ensure termination. A failure at the empty root disproves satisfiability; a failure below an assumption disproves only that branch.

Searching for one solution may stop at the first verified complete assignment. Counting all solutions must continue. Proving an optimum for weighted factors also cannot stop at an arbitrary feasible assignment. The stopping rule is part of the problem, not a cosmetic implementation detail.

## 7. MRV, degree and deterministic ties

Minimum remaining values chooses an unassigned variable with the smallest current legal domain. An empty domain is a failure certificate; a singleton is a forced remaining choice. MRV is a fail-first policy: every variable will eventually need a value, so exposing a difficult variable early can avoid exploring irrelevant later choices. It is a heuristic, not a theorem that runtime always improves.

The residual-degree tie-breaker prefers the tied variable constraining the largest number of other unassigned variables. Count distinct remaining neighbors, not two directed arcs per neighbor, already assigned neighbors or the variable's own domain size. On a fixed complete binary graph the initial degrees are equal, but later filtering can make MRV different. A low-degree singleton still wins under MRV-first ordering over a high-degree variable with several values.

To make a trace reproducible, state a complete rule: smallest current domain, then largest residual degree, then the declared variable order. State value tie-breaking separately. “Use MRV” alone may leave several valid traces when domains tie. If domains have not been maintained, counting their raw initial sizes can fail to measure the legal values remaining under the current assignment; either compute legal counts or explain the weaker heuristic actually used.

## 8. Least-constraining value is a declared score

After selecting $X$, one usual LCV score counts the neighbor-domain values that would be deleted by assigning $X=a$:

$$L(a)=\sum_{Y\in N(X),\,Y\text{ unassigned}}|\{b\in D_Y:(a,b)\notin R_{XY}\}|.$$

Try smaller $L(a)$ first. Since the pre-choice total neighbor-domain size is the same for every candidate, this is equivalent to maximizing the remaining number of individual neighbor values under the same one-step test. It is not equivalent to minimizing the number of affected neighboring variables. Deleting three values in one neighbor can be worse than deleting one in each of two neighbors.

A propagation-based LCV policy may trial-run AC-3 for each candidate and count the eventual domain loss. That is a different, more expensive score; restore domains after each trial. Neither score generally maximizes the exact number of complete solutions. With nonnegative weighted factors, a highly flexible feasible value can still have a worse objective. The heuristic's usefulness and its cost depend on whether the task is finding one solution, counting solutions or proving an optimum.

## 9. Forward checking and its precise boundary

After assigning $X=a$, restrict $D_X$ to $\{a\}$. For each unassigned neighbor $Y$, remove $b\in D_Y$ if $(b,a)\notin R_{YX}$. Fail immediately if a neighbor loses every value. This is one layer of filtering from the new assignment; it does not normally propagate the resulting changes between two other unassigned variables.

For equality chain $A=B=C$ with all domains $\{0,1\}$, assigning $A=0$ makes forward checking reduce $B$ to $\{0\}$ but leaves $C$ unchanged. Further consistency propagation reduces $C$ to $\{0\}$ too. A singleton produced by filtering need not yet be recorded as an explicit search assignment; the algorithm can still select and assign it later. Domain state, assignment state and recursive depth are different records.

With maximum degree $\delta$, largest domain $d$, a fixed head singleton and constant-time relation lookup, one such forward-checking pass uses $O(\delta d)$ pair checks. A generic REVISE routine against an arbitrary head domain instead has $O(d^2)$ cost per arc. State which operation is being counted before quoting a coarse $O(nd^2)$ or a tighter bound.

<!-- CSP:equality-chain -->

## 10. Directed arc consistency and support witnesses

An arc $X\to Y$ is consistent when every surviving $a\in D_X$ has at least one surviving support $b\in D_Y$ with $(a,b)\in R_{XY}$. The quantifiers are **for every tail value, there exists a head support**. Different tail values may use different supports; a support need not itself extend to a global solution. Reverse consistency is a separate directed test.

For $X+Y=4$ with $D_X=\{1,2,3,4,5\}$ and $D_Y=\{1,2\}$, only $X=2$ and $X=3$ survive. Their supports are respectively $Y=2$ and $Y=1$. Values one, four and five have no head support. The operation deletes from $D_X$ only; it does not delete $Y$ values merely because it was called in the forward direction.

For asymmetric relation $X<Y$, reversing the arc uses $R_{YX}=\{(b,a):(a,b)\in R_{XY}\}$. It must not reinterpret the reverse test as a new requirement $Y<X$. A unary condition must be enforced before a claim of node-and-arc consistency. An isolated variable is not protected from an empty domain merely because there are no arcs to process.

<!-- CSP:sum-four -->

## 11. REVISE and AC-3 queue discipline

REVISE snapshots the tail domain, checks each candidate against the current head domain and removes candidates having no support. Snapshotting avoids modifying a set or list while iterating over that same live container. If any tail value is deleted, neighboring variables may have lost a support in that changed domain. Enqueue existing **incoming** arcs $Z\to X$, not outgoing arcs $X\to Z$.

With one conjoined relation per unordered pair and the reverse relation stored as its transpose, rechecking $Y\to X$ immediately after revising $X\to Y$ is unnecessary. A removed $a$ supported no current value of $Y$, so its removal cannot be the cause of a lost support in that reverse arc. If a program handles several separate constraints with different witnesses, this exclusion needs a fresh proof; the chapter's reference avoids that ambiguity by conjoining relations first.

Full preprocessing starts with all directed constraint arcs. After assigning a variable in a previously arc-consistent branch, it suffices to start with incoming arcs to that changed singleton, then propagate every resulting domain change. That incremental initialization is not sufficient for an arbitrary unprocessed CSP: some disconnected arc may already be inconsistent. Queue order changes the intermediate trace and primitive-check count; it does not license deleting a supported value.

<!-- CSP:strict-chain -->

## 12. Why propagation is sound and terminates

**Solution-preservation invariant.** Assume the current domains contain all values used by every solution compatible with the current branch assumptions. If REVISE deletes $a$ from $D_X$, no $b$ in the current $D_Y$ satisfies their relation. Any compatible complete solution using $X=a$ would have to choose such a $b$, a contradiction. Therefore deletion preserves every compatible solution. Induction over the finite deletion sequence proves the invariant for AC-3 and for its use inside backtracking.

**Termination.** Values are only removed, never created, within one propagation invocation. There are at most $\sum_i|D_i|$ possible deletions. Requeueing happens only after a strict shrink; every such event adds finitely many existing arcs. The queue therefore eventually empties or an empty domain is detected. Repeated unchanged revisions do not generate more work.

**Fixed-point meaning.** When the full queue finishes successfully, every required directed arc has current support for every tail value. An arc processed earlier could become invalid only after its head domain changed; that change would have requeued it. If execution stops early on a wipeout, the other displayed domains are merely that particular partial failure trace, not necessarily a unique fully propagated closure. Across fair complete closure runs, monotone support deletion has a greatest arc-consistent subdomain below the starting domains; arbitrary early-failure snapshots need not be identical.

## 13. Deriving the AC-3 time bound

Let $e$ be the number of directed binary arcs after parallel constraints have been conjoined, and $d\ge1$ the largest starting domain. A naive revision examines at most $d$ tail values and up to $d$ head candidates for each, so costs $O(d^2)$ relation tests with constant-time table lookup. An arc is initially queued once and can be requeued only when its head domain strictly shrinks. Before a domain becomes empty, it can strictly shrink at most $d-1$ times. On empty-domain detection this implementation returns before adding further arcs. Thus each arc can be processed at most $d$ times under this declared queue contract.

Multiplying gives $O(ed^3)$ time for binary relation checks, plus domain initialization and representation costs. For a dense graph $e=O(n^2)$, yielding $O(n^2d^3)$. A sparse graph should retain $e$ rather than silently replacing it by $n^2$. If a constraint evaluation itself costs $c$, multiply the pair-test cost by $c$. Initial empty-domain checks still require reading the variable list even when $e=0$.

The maintained state requires $O(nd+e)$ space for domains and a deduplicated arc queue, excluding the input relation tables. Explicit binary tables may themselves require $O(ed^2)$ storage. Keeping every teaching snapshot or every solution adds separate output storage; it is not part of the lean solver's auxiliary-space bound. A bound for one AC-3 invocation is not the total cost across an exponential search tree.

## 14. Arc consistency does not decide general satisfiability

Take a triangle with two colors and inequality on all three edges. Every tail color has the other color as a support across each individual edge. AC-3 deletes nothing. Yet choosing $A=0$ forces $B=1$ and $C=1$, violating $B\ne C$; choosing $A=1$ gives the symmetric contradiction. There is no complete solution. Nonempty arc-consistent domains are necessary local evidence, not a sufficient global certificate.

By contrast, an empty domain after sound propagation proves that no solution extends the current assumptions. At the root this disproves the original CSP. Under $A=0$ it disproves only that branch; another value of $A$ may succeed. A successful propagation call therefore returns an **arc-consistency status**, not a verified solution, and a failed branch does not justify declaring every sibling impossible.

<!-- CSP:odd-cycle -->

## 15. Maintaining arc consistency and restoring a branch

MAC combines complete backtracking with AC-3 after each assignment. The root is first made arc consistent. At a child, fix the selected variable to one value and start incremental propagation from incoming arcs. Continue only if no domain empties. MRV then uses the smaller current domains, which can change its next selection substantially.

Restoration is essential to the completeness proof. Copying all domains for each child is simple and safe: siblings never share a mutable filtered domain. A trail is more efficient when carefully implemented. Record each deletion with its variable and value, save a trail length at the branch entrance, and restore entries back to that marker when leaving the child. Also restore explicit assignments, cached supports or counts, and any queue state a particular implementation reuses. A cached support removed later must be revalidated before it is used again.

For $X\le Y$, $Y=Z$, $X\ne Z$ on Boolean domains, the branch $X=1$ fails: $Y$ must be one and $Z$ must be zero, contradicting equality. Restoring the original branch domains and trying $X=0$ succeeds with $(0,1,1)$. Keeping the wiped domain from the first branch would wrongly reject this valid solution. A deletion justified under an assumption cannot be applied globally without that assumption or a logically valid learned constraint.

<!-- CSP:rollback -->

## 16. Executable finite binary reference

The following reference implements explicit binary relations, conjunction of repeated pair constraints, directed support tests, an initial empty-domain guard, deterministic MRV/degree ties and exact branch copying. It uses integers as teaching values. Every AC-3 snapshot records the domains, current arc, support witness or deletion reason and remaining queue. The validator compares this actual printed algorithm with independent enumeration of small CSPs; the finite comparison supplements the general proofs above.

<!-- CSP:reference-code -->

The full snapshot list is a teaching output and can be much larger than the solver state. Setting recording off avoids that trace storage. The browser laboratory independently executes the same binary contract on bounded inputs and is checked against exact Python results; it is not presented as a general solver for arbitrary global constraints or continuous domains.

## 17. Tree and forest CSPs: backward filtering, forward assignment

Assume a finite binary constraint graph is a tree and domains have already absorbed unary restrictions. Choose a root and order variables so each parent comes before its children. In reverse order, revise the parent domain against each child domain. If a domain empties, report failure. Otherwise choose any remaining root value, then walk forward assigning each child a value supporting its chosen parent value.

**Why it works.** After processing a child's entire subtree, every surviving child value extends to a valid assignment in that subtree, by induction from leaves upward. Parent revision retains only values supported by such a child value. Distinct child subtrees have no cross edges in a tree, so their extensions can be combined independently. Consequently every surviving root value extends to the whole tree. The forward pass selects those witnesses. This argument fails on a cycle because two “subtrees” may contain an additional linking constraint.

There are $n-1$ edges, each requiring at most $d^2$ pair checks in the backward pass; the forward pass needs at most $O(nd)$ witness work. Total time is $O(nd^2)$ with constant-time binary checks. A forest is handled component by component, including isolated nonempty-domain variables. Linear time in $n$ means the domain bound and relation-check convention are fixed; it does not mean linear in every possible input representation.

## 18. Counting tree solutions with messages

Existence and counting are different tasks. Define $M_i(a)$ as the number of valid assignments in the subtree rooted at $X_i$ when $X_i=a$. For a leaf, $M_i(a)=1$ for every allowed value. For an internal node,

$$M_i(a)=\prod_{j\in\operatorname{children}(i)}\left(\sum_{b\in D_j:(a,b)\in R_{ij}}M_j(b)\right).$$

The inner sum counts the child's choices and their descendant extensions; the product combines independent child subtrees. The total is $\sum_{a\in D_r}M_r(a)$. For a forest, multiply component totals, not add them. The number of arithmetic operations has the same pairwise structure as tree solving, but integer bit complexity can grow with the solution count. This is not a claim that arbitrarily large exact integers cost constant time.

A three-variable path with three colors and inequality has $3\cdot2\cdot2=12$ solutions. The existential tree algorithm returns one; the message calculation counts all twelve. A root value with two different supported child values contributes both to the sum, rather than requiring one support shared across all root choices.

## 19. Cycle cutsets and the assumptions hidden in a bound

A cycle cutset is a set of variables whose removal leaves a forest. Given a cutset of size $c$, enumerate its at most $d^c$ assignments, reject those violating constraints internal to the cutset, restrict residual domains against the assigned boundary and solve each remaining forest. If any branch succeeds, combine its cutset assignment and forest assignment into a full solution.

The familiar $O(d^c(n-c)d^2)$ expression describes the residual forest work under additional simplifications. It must not erase internal/boundary checking or give zero work when $c=n$. A safe binary-operation accounting for a supplied cutset is $O(d^c(e+nd^2))$ when checks are constant time, with room to sharpen sparse cases. Searching for a minimum cutset is a separate combinatorial task and is not included in that supplied-cutset bound. A larger known cutset may still be useful; minimality is not needed for correctness.

For a triangle with three colors, condition on one vertex. Each of its three choices leaves two adjacent vertices with two colors; the edge permits two completions. Total solution count is six. Conditioning does not make every cutset assignment feasible; each residual branch still needs its domain and edge checks.

## 20. Higher-arity constraints, global support and Hall reasoning

Pairwise inequalities and the global all-different relation have the same complete solutions, but their propagation strength can differ. Let $D_X=D_Y=\{1,2\}$ and $D_Z=\{1,2,3\}$. Pairwise inequality is arc consistent without deleting one or two from $D_Z$. Global all-different requires $X,Y$ to use the two-value set $\{1,2\}$, leaving $Z=3$.

The underlying counting principle is Hall's condition: any subset of variables must collectively have at least as many possible values as variables if distinct values are to be assigned. Three variables all restricted to $\{1,2\}$ violate that condition, although each binary inequality still has local support. A global support test for a candidate value must find a single satisfying tuple for the entire relation containing that value. Different pairwise witnesses are insufficient.

An explicit hidden-tuple encoding can convert a finite arity-$k$ relation to binary constraints. Add an auxiliary variable whose domain is the set of allowed $k$-tuples; connect it to each original variable with a projection-equality relation. Every original solution has a corresponding tuple value and every satisfying extended assignment projects to an original solution. The encoding is exact, but the tuple domain can have up to $d^k$ entries. “Everything can be made binary” is not a promise of small memory or identical propagation behavior.

<!-- CSP:hall -->

## 21. Path consistency, k-consistency and strong consistency

A CSP is $k$-consistent when every consistent assignment to any $k-1$ distinct variables extends to any selected $k$th variable. The one-variable extension condition requires an allowed value for every selected variable. Unary filtering is often called node consistency, but merely checking that every surviving value satisfies unary restrictions can be vacuously true on an empty domain. For the construction theorem below, require a nonempty unary-consistent base explicitly. Binary arc consistency then corresponds to the two-variable extension condition in this binary model. Three-consistency requires extension of an already compatible pair, a stronger question than finding independent supports on two edges.

Strong $k$-consistency means consistency at every level from one through $k$. Strong $n$-consistency permits a backtrack-free construction in any variable order: extend a consistent prefix of length zero, one, and so on by the appropriate next-level condition. The distinction is important: merely finding at least one solution on every $k$-variable subset does not establish the universal extension quantifier in the definition.

Path consistency can remove an allowed pair $(a,b)\in R_{XY}$ when some third variable $Z$ has no value jointly supporting that pair through both relevant relations. In the Boolean triangle $X=Y$, $Y=Z$, $X\ne Z$, every binary arc has support but no allowed $X,Y$ pair extends through $Z$. Pair-relation filtering exposes the contradiction. Relation tables may need to be introduced or expanded as a stronger-consistency algorithm operates; the extra cost is part of the algorithm and its representation.

## 22. Conflicts, backjumping and legitimate learning

Chronological backtracking returns to the immediately preceding assigned variable. Conflict-directed reasoning asks which earlier assumptions actually caused failure. Suppose $X_4=X_1$ and $X_4=1$, while $X_2,X_3$ are unrelated choices. Under $X_1=0$, no value for $X_4$ works. Changing only $X_2$ or $X_3$ cannot fix that contradiction, so returning directly to $X_1$ is justified. Its explanation is the incompatible assumptions on $X_1$ and $X_4$, not merely the fact that $X_4$ happened to be assigned last.

A conflict set records earlier variables whose current assignments suffice for the rejection. When every value of a variable fails, combine the explanations needed to reject all those values; a reason for only one value does not justify eliminating every value. Jump to the most recent relevant earlier assignment and retain the necessary earlier causes when propagating the explanation upward. The implementation must define how reasons from propagation and prior failures are accumulated; a static graph neighbor list is not automatically a complete dynamic explanation.

A nogood is a partial assignment proved not to have any solution extension. Its negation can be retained as a logically implied constraint. A branch-specific deleted value without its antecedent is not a global nogood. Learning is sound only when every retained clause or relation follows from the original constraints and recorded assumptions. The MIT notes identify omitted protected pseudocode; this chapter teaches the reasoning and a checked example, without pretending the removed text was available or presenting a full conflict-directed solver as part of the binary laboratory.

## 23. Complete-assignment repair and min-conflicts

Local search begins with a complete assignment and changes values to reduce violations, rather than extending an empty assignment. One min-conflicts policy selects a currently conflicting variable, computes how many constraints would be violated under each of its values and tries a minimum-scoring value. Count violated constraints or attacking queen pairs as declared; that is different from the number of variables participating in at least one violation.

This can work extremely well on some instances, but a positive conflict score is not an unsatisfiability certificate. The method can plateau, cycle under equal-score moves or become trapped in a local minimum. A finite iteration budget and unsuccessful restarts do not establish that no solution exists. The triangle with two colors has minimum conflict count one, but that lower bound follows from the parity argument, not merely from one unsuccessful run.

If an implementation accepts only strictly improving moves in a finite state space, it terminates because the objective has finitely many values. It can still terminate at a non-solution. If equal-value moves are allowed, a tie policy or separate stopping rule is needed; finite assignments alone do not prevent cycling. A complete backtracking search and an incomplete repair procedure have different failure meanings.

## 24. Weighted factors, partial bounds and approximate search

For nonnegative factors $f_j$, define $W(x)=\prod_j f_j(x)$. Ordinary hard constraints are the special case $f_j\in\{0,1\}$. A zero factor vetoes a complete assignment; a positive weight states feasibility under the zero/nonzero interpretation but not optimality. Probabilities need additional normalization/interpretation and are not implied merely by multiplying nonnegative numbers.

When extending a partial assignment, multiply each newly fully instantiated factor exactly once. Its scope determines when it becomes evaluable. If remaining factors may exceed one, the current partial product is not an upper bound on future weight. A partial weight two can later become twenty after a factor ten. A valid crude maximization upper bound is the current product times an upper bound for every unevaluated factor, with bounds taken over all remaining permitted values. Shared variables can make the product loose, but looseness does not invalidate an upper bound.

Beam search keeps at most $K$ surviving partial assignments per depth. It can discard the unique feasible or optimal completion and is generally incomplete. With $n$ levels, at most $d$ extensions per candidate, constant incremental scoring and linear-time top-$K$ selection, the work is $O(nKd)$. Sorting instead adds a logarithmic selection factor; randomized quickselect provides expected linear selection, not an unqualified deterministic worst-case guarantee. Copying whole assignments or evaluating many factors adds its own cost. A fixed beam size does not establish a universal approximation ratio.

Coordinate-wise maximization of weighted factors is another incomplete local method. If unaffected factors are strictly positive, their common multiplicative constant can be omitted when comparing a single-coordinate move. If that constant is zero, all full products remain zero and the local comparison cannot claim a strict global improvement. Keep a current value on ties or define a full-sweep stopping policy when proving convergence; arbitrary equal-weight moves may cycle.

## 25. A complete examination decision sequence

First identify whether the question concerns feasibility, counting, optimization or one particular algorithm trace. Write the actual domains, unary restrictions, relation scopes and any branch assumptions. Draw a binary graph only for binary constraints; give higher-arity constraints their own representation. If a graph comes from a map, use the exact adjacencies, not a guessed geographic picture.

For a propagation question, write every directed queue entry in its stated order. For a popped arc, list tail values and at least one valid head witness for each survivor. Delete only unsupported tail values. Record incoming requeues after a strict shrink, stop under the specified wipeout rule and distinguish intermediate from fixed-point domains. State whether the conclusion concerns the root or an assumed branch.

For heuristic questions, recompute current legal-domain sizes, apply MRV before a declared degree tie, count only residual neighbors and calculate the actual LCV score requested. Separate a variable-selection heuristic from a value-ordering heuristic. For a counting question, distinguish paths, distinct assignments, leaves, nodes, revisions and individual relation tests.

For a tree or cutset question, prove the structural assumption, check empty domains, identify supplied versus computed cutsets and account for boundary/internal constraints. For all-different or stronger-consistency questions, ask whether the same joint tuple supports all requirements, rather than assembling incompatible pairwise witnesses. Finally verify any returned full assignment against every original constraint. A local success flag, one positive factor or a plausible-looking coloring is not that final verification.

## 26. Fully worked mathematical and conceptual questions

<!-- CSP:questions -->

## 27. Complete summary and final examination decisions

<!-- CSP:review -->

## 28. Written references and exact reading record

- **Stanford University, CS221, Spring 2026.** Moses Charikar and Zachary Robertson, course instructors. Written modules: Overview, Definitions, Examples, Dynamic Ordering, Arc Consistency, Beam Search and Local Search. [Module index](https://stanford-cs221.github.io/spring2026/modules/). The written JavaScript bodies contain slide text, explanatory prose and drawing definitions; source reading and actually viewed images are recorded separately.
- **University of California, Berkeley, CS188.** Nikhil Sharma, Josh Hug, Jacky Liang and Henry Zhu, textbook authors, with the contributors credited on the textbook home page. [Filtering](https://inst.eecs.berkeley.edu/~cs188/textbook/csp/filtering.html), [Ordering and Structure](https://inst.eecs.berkeley.edu/~cs188/textbook/csp/ordering.html), and the adjacent CSP sections identified in the audit. A textbook attribution is not silently replaced by a particular semester's lecturer.
- **Carnegie Mellon University, 15-281, Fall 2025.** Pat Virtue, course instructor; course-staff written notes, [Constraint Satisfaction Problems](https://www.cs.cmu.edu/~15281-f25/coursenotes/constraints/index.html). The chapter proves its bounds with explicit sparse-graph and relation-check assumptions.
- **Massachusetts Institute of Technology, 16.410, Fall 2010.** Brian Charles Williams, constraint-lecture instructor; course co-taught with Emilio Frazzoli. Lectures 5, 6 and 7a in the [written lecture collection](https://ocw.mit.edu/courses/16-410-principles-of-autonomy-and-decision-making-fall-2010/pages/lecture-notes/). Exact in-scope PDF pages and unavailable protected material are declared in the audit.
- **Cornell University, CS4700, Fall 2013.** Bart Selman, [Constraint Satisfaction slides](https://www.cs.cornell.edu/courses/cs4700/2013fa/slides/CS4700-CSP_v6.pdf). Relevant consistency and backtracking pages were compared; historical arithmetic, notation and complexity remarks are qualified rather than adopted unquestioningly.
- **Harvard University, CS50 AI.** Brian Yu, lecturer, and David J. Malan, course co-instructor. [Optimization notes](https://cs50.harvard.edu/ai/notes/3/), Constraint Satisfaction through the final summary; [Crossword project specification](https://cs50.harvard.edu/ai/projects/3/crossword/). Used as an additional implementation comparison, not as a claim to have solved an enrolled student's assignment.

Original Iranian examination records, PDF page numbers, pinned file fingerprints, independent answer derivations and the status of any official key are attached to the authentic question placements. The source audit states exactly what was read and which course prompts were developed. Full university publications and protected exercise material are not redistributed with this original chapter.
