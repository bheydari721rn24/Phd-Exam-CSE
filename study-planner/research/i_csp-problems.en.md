# Original and attributed written-course problems

## IC01 | Count assignments, paths and nodes separately

**Origin.** Original examination-style problem; reconciles the Stanford/CMU/Cornell assignment-order discussion.

**Question.** Five variables have domains of size three and no constraints. Count complete assignments, complete paths when each action may select any unassigned variable, all distinct partial assignments, and nodes in a full fixed-order tree. Explain the different answers.

**Solution.** A complete assignment chooses one of three values independently for each of five named variables, so there are $3^5=243$. If actions may choose the next variable too, every complete assignment can be written in $5!=120$ orders. The action tree therefore has $5!3^5=29160$ complete paths, although many paths end at the same assignment.

For a distinct partial map, each variable is either unassigned or takes one of three values: four independent possibilities. Thus there are $4^5=1024$ distinct partial maps, equivalently $\sum_{k=0}^5\binom5k3^k$. A fixed variable order visits only prefix scopes, not every possible partial scope. Its complete tree has $1+3+9+27+81+243=364$ nodes, of which 243 are leaves. None of these numbers counts primitive constraint tests because there are no constraints here. Early pruning would reduce the action tree, whereas merging equivalent states addresses a different source of redundancy. The source notation $n^d$ is not the count for $n$ variables of domain size $d$.

## IC02 | Four queens and a nonadjacent-column relation

**Origin.** Adapted from MIT 16.410 Lecture 5, PDF page 13, with an independently derived complete solution.

**Question.** Let $Q_i$ be the row of the queen in column $i$ on a four-by-four board. Give the allowed relation between $Q_1$ and $Q_3$, then find every complete solution. Contrast the initial assignment count with a sixteen-variable Boolean encoding.

**Solution.** The two columns are distance two apart. A pair $(a,b)$ is allowed exactly when $a\ne b$ and $|a-b|\ne2$. Enumerating the four possibilities for each coordinate leaves

$$R_{13}=\{(1,2),(1,4),(2,1),(2,3),(3,2),(3,4),(4,1),(4,3)\}.$$

Every complete solution must also satisfy the other five column-pair restrictions. Starting with $Q_1=1$ leaves no complete nonattacking arrangement; $Q_1=2$ forces the completion $(2,4,1,3)$. Reflecting rows gives $(3,1,4,2)$ from $Q_1=3$; $Q_1=4$ mirrors the failed first case. Independent enumeration of all $4^4=256$ column tuples confirms exactly those two. Each uses distinct rows, and its six absolute row differences avoid the corresponding column differences.

The Boolean encoding starts with $2^{16}=65536$ truth assignments before imposing occupancy and attack constraints. It must require exactly one queen per column or an equivalent total/occupancy condition. At-most-one attack constraints alone admit the empty board. The different universe sizes do not, by themselves, establish solver runtime.

## IC03 | Show a support for every surviving value

**Origin.** Adapted from Stanford CS221 Spring 2026, Arc Consistency, written numerical example.

**Question.** For $X+Y=4$, $D_X=\{1,2,3,4,5\}$ and $D_Y=\{1,2\}$, revise $X\to Y$ and then the reverse arc. List supports and the complete solutions.

**Solution.** Test tail candidates individually. For $X=1$, the required support is three, which is absent from $D_Y$; delete one. For $X=2$, support $Y=2$ exists. For $X=3$, support $Y=1$ exists. For $X=4$ and five, required supports zero and minus one are absent; delete both. Thus the first revision leaves $D_X=\{2,3\}$ and does not itself alter $D_Y$.

On the reverse arc, $Y=1$ has support $X=3$ and $Y=2$ has support $X=2$. Neither is deleted, so the pair is arc consistent in both directions. The only complete solutions are $(2,2)$ and $(3,1)$. The surviving witnesses are different; arc consistency never requires one single $Y$ value to support every $X$ value simultaneously. In this two-variable example the surviving pairs characterize solutions exactly. That conclusion does not transfer to a general cyclic graph with several constraints. The displayed player records the direction, support witnesses and deleted tail values at each checkpoint.

## IC04 | Strict inequalities propagate from both ends

**Origin.** Original problem.

**Question.** Variables $A,B,C$ initially have domain $\{1,2,3,4\}$ with $A<B<C$. Find the AC closure and every solution. Explain why just applying each inequality once may be insufficient.

**Solution.** On $A<B$, value four has no larger support, so $A$ loses four; $B$ loses one because it has no smaller support. On $B<C$, $B$ loses four and $C$ loses one and two once $B$ has minimum two. The loss of $B=4$ then removes support for $A=3$. The fixed point is $D_A=\{1,2\}$, $D_B=\{2,3\}$, $D_C=\{3,4\}$. Each survivor has a witness on each incident directed arc.

Complete solutions are the increasing triples $(1,2,3),(1,2,4),(1,3,4),(2,3,4)$, one for each choice of three distinct values from four. Thus there are $\binom43=4$, rather than the product $2\cdot2\cdot2=8$ of the final domain sizes. Those domains record individually possible values, not unconstrained combinations. The path structure permits backtrack-free construction after directional filtering, but arbitrary independent selection from all final domains can still violate an edge. Requeueing is needed because a head-domain loss can invalidate an earlier tail support.

## IC05 | An extensional relation with holes

**Origin.** Adapted from Cornell CS4700 Fall 2013, PDF page 76.

**Question.** Let $D_X=\{1,2,3\}$, $D_Y=\{3,4,5,6\}$ and $R_{XY}=\{(1,3),(1,5),(3,3),(3,6)\}$. Find the arc-consistent domains and count complete solutions. Does a domain product give that count?

**Solution.** Tail value $X=2$ appears in no allowed pair and is removed. Values one and three retain supports three/five and three/six respectively. Reversing the relation, $Y=4$ occurs in no allowed pair and is removed; $Y=3,5,6$ retain supports. The fixed-point domains are $\{1,3\}$ and $\{3,5,6\}$.

The four listed allowed tuples are exactly the four complete solutions. The domain product has six tuples, including forbidden $(1,6)$ and $(3,5)$, so multiplying final domain sizes overcounts. Both domains may be nonempty and both directions supported while not every cross-product pair is compatible. The input is an extensional table, so a constant-time hashed-pair membership lookup supports the usual REVISE complexity assumption. Scanning the entire relation afresh for each pair would be a different implementation with an additional lookup cost. Keeping holes in a domain also matters: the surviving set is not the numeric interval from its minimum to its maximum.

## IC06 | A source triangle solved entirely by propagation

**Origin.** Adapted from MIT 16.410 Lecture 5, PDF pages 20–34.

**Question.** Three variables are pairwise unequal. Their domains are $D_1=\{R,G,B\}$, $D_2=\{R,G\}$ and $D_3=\{G\}$. Derive the closure and verify the complete assignment without guessing colors.

**Solution.** Because $X_3$ can only be green, $X_2=G$ has no support on $X_2\to X_3$ and is deleted, leaving $X_2=R$. Likewise $X_1=G$ has no support against $X_3$ and is removed. Now $X_1=R$ loses its only possible unequal support in $D_2$, because that domain has become the singleton red. Hence $D_1=\{B\}$.

The remaining domains are $(\{B\},\{R\},\{G\})$. Check the three original inequalities: blue differs from red, blue differs from green and red differs from green. Thus the complete assignment $(B,R,G)$ satisfies every constraint. It is unique because every variable's domain is a singleton and sound propagation preserved every solution. A different initial arc queue can display the deletions in a different order; a fair run still reaches this successful closure. The player uses integer color codes with an explicit legend, so a colored node never hides the actual declared domain value.

## IC07 | A locally supported but impossible triangle

**Origin.** Course-derived counterexample compared across Stanford, Cornell and Harvard written CSP discussions.

**Question.** A triangle has inequality on every edge and Boolean domains. Prove it is arc consistent and unsatisfiable. Explain what MAC does after assigning its first variable.

**Solution.** For either tail value zero or one, the opposite head value supports inequality across each edge. Therefore both directions of all three edges pass REVISE, and preprocessing removes nothing. This is a direct verification of the universal-tail/existential-head condition, not an inference from equal domain sizes.

For global impossibility, choose $A=0$. Inequality forces both $B=1$ and $C=1$, violating their mutual edge. Choosing $A=1$ gives the complementary failure. These two cases exhaust the first variable's domain, so there is no solution. Under MAC, either first assignment propagates to the two other singletons and then produces a wipeout. Each wipeout is initially a branch failure; after both first-variable branches have been exhausted, root failure establishes unsatisfiability. An isolated AC call returning nonempty domains has proved only local support. The contradiction is the inability to combine the separate witnesses into one joint coloring.

## IC08 | An even cycle with the same local domains

**Origin.** Original comparison problem.

**Question.** Replace the previous triangle by a four-cycle $A-B-C-D-A$, still with two colors and inequality. Find its AC closure and its number of solutions. Why can the same local test coexist with a different satisfiability answer?

**Solution.** Every directed edge again has opposite-color support for both values, so no domain changes. The final domains therefore look exactly like the triangle's initial/final domains when viewed one vertex at a time.

Choose $A=0$. The cycle forces $B=1$, $C=0$, $D=1$, and the closing edge $D\ne A$ is satisfied. Choosing $A=1$ gives the complementary coloring. Every remaining value is then forced along the path, so there are precisely two solutions, $(0,1,0,1)$ and $(1,0,1,0)$; no others can occur. An even number of inequality flips returns to the original color, whereas the triangle's odd number creates a contradiction. Arc consistency checks each pair separately and does not record that parity around the whole cycle. It is therefore consistent for AC to give identical domain sizes in the two problems while one has zero complete solutions and the other has two.

## IC09 | One layer versus propagated equality

**Origin.** Original problem.

**Question.** In the equality chain $A=B=C$ with Boolean domains, assign $A=0$. Compare forward checking with MAC. Count extensions of that branch.

**Solution.** Forward checking tests the arcs entering the newly assigned singleton $A$. Only $B$ is its neighbor, so it deletes $B=1$ and leaves $D_B=\{0\}$. There is no direct $A,C$ constraint, so a one-layer pass leaves $D_C=\{0,1\}$. That remaining one at $C$ is not promised to extend to a solution; it has simply not been tested against the changed $B$ domain.

MAC requeues $C\to B$ after $B$ shrinks. Candidate $C=1$ now has no equal head support and is removed, leaving all three domains singleton zero. The branch has exactly one complete extension, $(0,0,0)$, verified against both equalities. Before assigning $A$, the original CSP had two solutions, the all-zero and all-one assignments. The stronger pruning did not remove a valid branch extension; it exposed a consequence earlier. It also did not automatically increase recursive assignment depth: a solver can keep $B,C$ as unassigned singleton-domain variables until it explicitly selects them.

## IC10 | Restore a failed branch before trying its sibling

**Origin.** Original hard implementation/correctness problem.

**Question.** Boolean variables satisfy $X\le Y$, $Y=Z$ and $X\ne Z$. Try $X=1$ first and then $X=0$ with MAC. Show why sharing the failed domains across siblings is incorrect.

**Solution.** In the first branch, $X=1$ and $X\le Y$ force $Y=1$. The inequality $X\ne Z$ forces $Z=0$. Equality $Y=Z$ then has no allowed pair, so propagation empties a domain and this branch fails. That failure used the assumption $X=1$.

Restore the parent domains $D_X=D_Y=D_Z=\{0,1\}$ before selecting $X=0$. Now $X\ne Z$ forces $Z=1$, equality forces $Y=1$, and $0\le1$ is valid. Thus $(0,1,1)$ is a complete solution. It is the only solution: $X=1$ was impossible, and $X=0$ forces the other two values as shown.

If a mutable domain emptied in the first branch is reused for the second without restoration, the solver rejects the valid solution and becomes incomplete. Branch copying avoids aliasing; a trail must restore every deletion back to its saved marker. The valid learned statement here is that $X=1$ has no extension, not that the emptied variable has no values under every possible assumption.

## IC11 | MRV first, residual degree second

**Origin.** Original examination-style heuristic problem.

**Question.** Six variables remain unassigned. Their graph edges are AB, AC, BC, BE, CE and CF; D is isolated. Current domain sizes are $|D_A|=2$, $|D_B|=2$, $|D_C|=3$, $|D_D|=1$, $|D_E|=|D_F|=4$. Verify the residual degrees of A,B,C,D are two, three, four and zero. Use MRV, then maximum residual degree, then alphabetical order. Choose the next variable; after D is assigned without altering other domains, choose the next one.

**Solution.** The smallest domain size is one, achieved only by $D$. It is selected despite having degree zero. The degree rule is a tie-breaker after MRV, not a license to override a strictly smaller domain. Selecting $C$ because its degree is four would apply a different heuristic.

After assigning the isolated $D$, it is excluded from the candidate list. By the question's premise no other domain or residual degree changes. The new minimum domain size is two, tied between $A$ and $B$. Of those, $B$ has larger residual degree, three versus two, so it is selected. Alphabetical order is never reached in either decision. If a trace did not specify how MRV ties are broken, both $A$ and $B$ could be valid next choices under MRV alone. Current domain sizes, residual degrees and the sequence of priorities are all necessary to reproduce a deterministic trace.

## IC12 | Deleted values and affected neighbors rank differently

**Origin.** Original hard LCV counterexample.

**Question.** Let $X\in\{a,b\}$ and $Y,Z\in\{1,2,3,4\}$. Choosing $a$ permits only $Y=1$ and permits every Z. Choosing $b$ permits $Y,Z\in\{2,3,4\}$. No other constraints exist. Compare deleted-value LCV, affected-neighbor count and exact completion counts.

**Solution.** Under $a$, Y loses three values and Z loses none, so the deleted-value score is three. Under $b$, each neighbor loses one value, so the score is two. Standard one-step deleted-value LCV therefore prefers $b$. Equivalently the surviving individual value totals are $1+4=5$ versus $3+3=6$.

An affected-neighbor score instead counts one changed neighbor for $a$ and two for $b$, so it prefers the opposite candidate. This demonstrates that the two definitions cannot be silently substituted. Exact completion counts are $1\cdot4=4$ for $a$ and $3\cdot3=9$ for $b$, because the two neighbors have no linking constraint. In this instance LCV agrees with the larger solution count, but that agreement is not a general theorem once neighbors interact. Both candidates remain feasible, and the full CSP has thirteen solutions. The laboratory represents a,b by declared integer codes, preserving the actual allowed-pair tables.

## IC13 | Separate supports can contradict one another

**Origin.** Original consistency-definition problem.

**Question.** On Boolean domains, impose both $X=Y$ and $X\ne Y$. Compare testing each relation separately with testing their conjunction. What must a solver do before using a one-relation-per-pair AC-3 proof?

**Solution.** Equality supplies support $Y=x$ for each value $x$ of X; inequality supplies support $Y=1-x$. The same observations hold in reverse. Thus each separate binary relation is arc consistent on the unchanged full domains. However no pair can satisfy both relations, because equality and inequality are mutually exclusive.

Their effective joint relation is the intersection of the equality table $\{(0,0),(1,1)\}$ and the inequality table $\{(0,1),(1,0)\}$, which is empty. Revising against that joint relation deletes both tail values and detects impossibility. Different witnesses for different predicates do not form one witness satisfying the conjunction. Before applying the chapter's exclusion of the just-revised reverse arc or its joint-support interpretation, conjoin all constraints on that pair, or otherwise explicitly enforce a consistency definition that uses a common witness. The complete solution set is empty in either representation, but the propagation strengths differ until the representation/algorithm is made precise.

## IC14 | Reverse the table, not the mathematical inequality

**Origin.** Original problem.

**Question.** With $X,Y\in\{1,2,3\}$ and $X<Y$, compute both directed revisions. Explain the error in checking Y<X on the reverse arc.

**Solution.** The allowed forward pairs are $(1,2),(1,3),(2,3)$. The forward arc deletes $X=3$, because no larger Y is available, and retains X values one and two. For the reverse test, use the transposed pairs $(2,1),(3,1),(3,2)$ in Y,X order. It deletes $Y=1$, since no smaller X exists; Y values two and three survive. The final domains are $D_X=\{1,2\}$ and $D_Y=\{2,3\}$, with the same three complete solutions as the original relation table.

Checking the new condition $Y<X$ would impose a different constraint rather than view the original from the other endpoint. Conjoining both strict inequalities would make the problem impossible. A directed arc describes which domain is being filtered and which supplies supports; it does not change the underlying admissible assignments. This distinction matters especially for inequalities, sums with asymmetric coefficients and scheduling precedences, even though it is easy to overlook on symmetric inequality/coloring examples.

## IC15 | A complete queue trace has a declared order

**Origin.** Original exact-trace problem.

**Question.** For $A<B<C$ on $\{1,2,3\}$, use initial FIFO queue $(A,B),(B,A),(B,C),(C,B)$, append incoming affected arcs not already queued and omit the just-processed reverse. List domain changes and the fixed point.

**Solution.** First $(A,B)$ removes three from A, leaving A={1,2}. Next $(B,A)$ removes one from B, leaving B={2,3}; its affected incoming arc $(C,B)$ is already queued. Processing $(B,C)$ removes B=3, leaving B={2}. This requeues $(A,B)$ because A may have lost its support B=3. The original queued $(C,B)$ now sees B={2} and removes C=1 and C=2, leaving C={3}. No additional incoming neighbor other than the just-processed B is present. Finally the requeued $(A,B)$ deletes A=2, leaving A={1}.

The resulting singleton assignment is $(1,2,3)$, and all edges are satisfied. The declared deduplicated queue processes five arcs; it performs more individual pair-membership checks than revisions. Reversing the initial queue would change intermediate deletions and possibly primitive-test counts. A correct final-domain answer cannot justify an invented intermediate queue trace; both the initialization and reinsertion convention are part of the question.

## IC16 | Empty domains and the empty variable set

**Origin.** Original algorithm-boundary problem.

**Question.** Explain what a robust solver should return for (a) one isolated variable with empty domain, (b) one isolated variable with three values, and (c) no variables and no constraints. Why is an empty AC-3 queue alone insufficient to decide among them?

**Solution.** In case (a), no value can be assigned to the variable, so the system has zero solutions. There are no arcs, but an explicit initial-domain guard must still reject it. An algorithm that returns success immediately from an empty queue would give a false satisfiability impression here.

In case (b), each of the three values independently supplies a complete solution, so there are three. The empty arc queue correctly means no binary support tests are required; it does not select a value or count solutions by itself. In case (c), the empty assignment satisfies every constraint vacuously, so there is exactly one solution, the empty tuple. That is the empty-product convention underlying recursive base cases, not zero solutions.

If a system permits a false zero-arity constraint, case (c) changes to impossible and that constant must be checked. The printed binary reference does not accept such a constraint as an edge. These endpoint cases test whether the implementation has confused “no pending pair test” with “a verified complete assignment exists.”

## IC17 | Charge reprocessing to the head domain

**Origin.** Original calculation based on the written AC-3 analyses.

**Question.** A binary CSP has 120 directed arcs and maximum initial domain size ten. Use the chapter's one-copy initial queue, immediate wipeout return and constant-time pair lookup. Give a safe bound on revisions and pair tests in one invocation. Does this bound cover all backtracking nodes together?

**Solution.** A particular directed arc is present initially once. It is requeued only after its head domain strictly shrinks; before becoming empty a ten-value domain can shrink at most nine times. A shrink to empty terminates before adding another queue batch. Thus at most ten revisions of that directed arc are possible. Across 120 arcs, at most $120\cdot10=1200$ revisions occur.

Each naive revision inspects at most ten tail candidates and ten head candidates for each, giving at most one hundred pair checks. Consequently $1200\cdot100=120000$ is a safe coarse pair-test bound. Early supporting witnesses, smaller later domains, deduplication and skipped reverse arcs often reduce it. If “120 edges” meant undirected edges, there would be 240 directed arcs and the numerical bound would double.

This is one propagation invocation. Backtracking can restore domains and invoke propagation at many different search nodes, so summing work across the whole tree can still be exponential. The bound also excludes input construction and the cost of a nonconstant constraint oracle. Those costs cannot be hidden inside a claimed exact revision count.

## IC18 | Why MAC keeps every solution despite stronger pruning

**Origin.** Original proof problem.

**Question.** Prove completeness of MAC with deterministic dynamic ordering and branch copies. Identify the step that fails if a heuristic discards a nonempty candidate value without a sound reason.

**Solution.** Fix a solution s and a search node whose explicit assignments agree with it. Initially s's unassigned values lie in the node's domains. The selector chooses one unassigned variable X, possibly based on the current domains; it need not follow a fixed global order. When its candidate s(X) is tried, the partial assignment remains locally legal because it agrees with a solution.

Sound AC-3 cannot delete any remaining value used by s: a deleted value would lack a head support, while s itself supplies the compatible head value. Therefore the corresponding child survives. Inducting on the number of unassigned variables constructs a path to s. Exact branch copies ensure that a failed sibling cannot contaminate that child's domains. Finiteness and eventually trying every candidate ensure the path is eventually visited.

If a heuristic deletes a candidate merely because its LCV score is poor or a beam is full, the step “s(X) is eventually tried” may fail. Such a procedure can be useful but is not the complete MAC algorithm proved here. Ordering changes when a solution is sought; unsound pruning changes which solutions are still reachable.

## IC19 | Tree existence and exact counting are different

**Origin.** Original tree-CSP problem.

**Question.** A path A-B-C has three colors at each vertex and inequality on each edge. Give a backtrack-free construction and count all solutions using subtree messages.

**Solution.** Root the tree at A. Backward parent-to-child revision deletes nothing because every color has two unequal child supports. Choose any A color, then one of its two supporting B colors, then one of the two C colors unequal to that chosen B. This verifies all edges and requires no backtracking after the backward sweep.

For counting, each fixed C color has leaf message one. For a fixed B color, summing over its two permitted C colors gives message two. For a fixed A color, the two permitted B colors each contribute two, so its subtree count is four. Summing over A's three colors gives twelve complete solutions. The product $3^3=27$ ignores constraints, while returning one forward assignment solves only existence.

The message sum uses alternative choices within a child subtree; products would be used across several independent children. The arithmetic-operation count is $O(nd^2)$ under naive pair tables, but an arbitrarily large exact count can have growing bit length. The tree premise is essential to both the independent-subtree combination and the backtrack-free guarantee.

## IC20 | A tree can be rejected in the backward pass

**Origin.** Original problem.

**Question.** A star has center H with domain {1,2,3} and leaves U={1}, V={2}, W={3}. Every leaf must differ from H. Perform the backward tree sweep and explain why no forward assignment should be attempted.

**Solution.** Each leaf has only its displayed value. Revising H against U removes H=1, because equality to that singleton would violate the edge. Revising H against V removes H=2. Revising H against W removes H=3. The center domain is now empty, establishing that no value can satisfy all three required inequalities simultaneously.

Every deletion has its own direct witness failure; the contradiction is not based on counting four vertices or assuming a star is automatically satisfiable. Trees admit a polynomial decision/construction algorithm, not a guarantee that every domain specification has a solution. The backward sweep is the existence test. Only if all required domains, including the root domain, remain nonempty does the forward witness construction become valid. Here a forward pass cannot choose a root value, so it must return failure. Processing the leaves in another order changes which color disappears first but not the conclusion that all three are excluded.

## IC21 | Independent components multiply solution counts

**Origin.** Original problem.

**Question.** A forest consists of edges A-B and C-D, with Boolean domains and inequality, plus an isolated variable E having three values. Count complete solutions and explain what happens if E's domain is empty instead.

**Solution.** The first edge has two solutions, (0,1) and (1,0). Independently, the second has the same two possibilities. A complete solution chooses one assignment from each component and one of E's three values. There are therefore $2\cdot2\cdot3=12$ solutions. Adding component counts would wrongly count alternatives among components rather than simultaneous choices for all variables.

The Cartesian-product decomposition is exact because no constraint connects different components. Conversely any full solution restricts to a valid solution in each component, so the product count neither misses nor duplicates assignments. If E has an empty domain, its component has zero solutions and the product is zero even though both edge components remain arc consistent and satisfiable. A solver must inspect isolated variables; they do not appear in an arc queue. For finding one solution, solve each component and combine the assignments; for counting, multiply the component totals and respect exact-integer costs.

## IC22 | Condition one triangle variable and solve a forest

**Origin.** Original cutset-conditioning problem.

**Question.** A triangle has three colors at every vertex and pairwise inequality. Use cutset {A}, count all solutions and describe the work that is performed in each cutset branch.

**Solution.** Removing A leaves the edge B-C, a tree. There are three cutset assignments, one for each A color. For a fixed choice, boundary constraints remove that color from both residual domains. The two remaining colors must be different on B-C, yielding two ordered completions. Thus the total is $3\cdot2=6$ solutions.

For each branch, first verify the chosen cutset values against constraints whose scopes lie inside the cutset; here there is no such edge. Then propagate the boundary restrictions to B and C, revise the residual tree and choose or count its supported assignments. The original triangle was cyclic, so the tree proof applies only after conditioning and boundary pruning.

The calculation uses a supplied valid cutset; it does not include finding a minimum one. Assigning a cutset does not imply that the residual CSP will succeed, although all three branches happen to do so here. Each returned coloring must include A and satisfy its two incident original edges as well as the residual B-C edge.

## IC23 | A cutset does not make every branch feasible

**Origin.** Original hard graph/propagation problem.

**Question.** The complete graph K4 has three-color domains and inequality on every edge. Explain why one removed vertex is not a cycle cutset, why two are, and why conditioning on any two still yields no solution.

**Solution.** Removing one vertex leaves K3, which contains a triangle and is not a forest. Removing two leaves one edge, a tree, so any pair of vertices is a valid cycle cutset. Enumerate its $3^2=9$ assignments. The three equal-color assignments violate the edge internal to the cutset and must be rejected before residual solving.

For each of the six distinct-color cutset assignments, every residual vertex is adjacent to both assigned vertices and loses those two colors. Both residual domains become the same singleton third color. Their mutual edge then has no unequal pair, so the residual tree fails. Thus all nine branches are rejected and the original graph has no three-coloring.

Root AC-3 alone would delete nothing because every individual unequal edge has supports in the full three-color domains. Conditioning exposes stronger joint consequences under its assumptions. This example separates “the remainder is a tree” from “the remainder is satisfiable,” and shows why internal cutset edges and boundary edges must both be included in a complexity/correctness description.

## IC24 | The all-variable cutset exposes a missing cost

**Origin.** Original asymptotic-boundary problem.

**Question.** A formula for supplied-cutset solving is quoted as $O(d^c(n-c)d^2)$. Set c=n and explain why literal zero work is wrong. Give a bound that includes the missing tasks.

**Solution.** If every variable belongs to the cutset, the residual graph is empty, so its tree-solving term is indeed zero. But the algorithm still has to examine up to $d^n$ cutset assignments and verify constraints among them. The zero residual term is not the total algorithm cost. The empty remaining graph contributes one empty completion to each already valid full cutset assignment, rather than removing the need to check that assignment.

A safe operation accounting for a supplied cutset is $O(d^c(e+nd^2))$ with constant-time binary checks. It includes per-branch constraint checking and a conservative residual/boundary allowance. For c=n, a sharper direct enumeration description is $O(d^n(n+e))$ if constructing each candidate costs O(n) and checking all edges costs O(e). Representation and enumeration choices can sharpen this further, but not to zero.

Finding the cutset itself is a separate task and is absent from both supplied-cutset formulas. The lesson is to distinguish the cost of a subroutine on the residual problem from the cost of the surrounding enumeration and verification.

## IC25 | Global all-different removes a locally supported value

**Origin.** Original Hall-set problem, motivated by the written global-constraint discussions.

**Question.** Let X,Y have domains {1,2} and Z have {1,2,3}. Compare pairwise inequality AC with global all-different support. Find all solutions.

**Solution.** Pairwise AC deletes nothing: for any value of one variable, each other neighbor separately has a different value available. In particular Z=1 has X=2 as a support and Y=2 as another separate support. Those two witnesses cannot be used simultaneously because X and Y must also differ.

Under the global relation, the two variables X,Y must occupy the two available values {1,2}. Their set is a Hall set with exactly two variables and two possible values. Z cannot use either of those values, so its only globally supported value is three. Then X,Y must be (1,2) or (2,1), giving exactly $(1,2,3)$ and $(2,1,3)$.

The complete solution set of the pairwise-inequality encoding is the same as the global relation's; the difference is propagation strength. Pairwise AC's surviving Z values one and two are locally supported but globally impossible. A single matching/tuple-support test can explain those removals, while the ordinary binary trace must not claim to perform that stronger global algorithm.

## IC26 | Detect a Hall violation that every pair misses

**Origin.** Original problem.

**Question.** Three variables each have domain {1,2} and must all be different. Prove unsatisfiability, verify pairwise arc consistency and explain why a global support check can fail before any explicit assignment.

**Solution.** The union of the three domains contains only two values. Assigning three pairwise distinct values would require an injection from a three-element variable set into a two-element value set, which is impossible by the pigeonhole principle. In Hall form, the three-variable subset has a value union of size two, violating the necessary inequality three ≤ two.

Nevertheless every pairwise inequality has support for both values: one is supported by two and two by one. Thus binary AC-3 leaves all domains unchanged. It has not made an arithmetic mistake; it enforced a weaker consistency notion. A global all-different propagator can ask whether a matching covers every variable in the variable–value bipartite graph. No such matching exists here, so it can reject the entire current branch without selecting one variable first.

The global conclusion comes from one jointly feasible distinct-value allocation, not separate matches for each edge. In a fixed diagram, distinguish a currently chosen partial matching from the existence of any full matching. Failure of one greedy matching attempt alone would not prove the Hall violation; the two-value counting argument does.

## IC27 | A binary encoding must retain the entire allowed tuple

**Origin.** Original higher-arity modeling problem.

**Question.** Boolean variables X,Y,Z have even parity: $X+Y+Z$ is even. Find the allowed tuples, show why pairwise projections lose the constraint and construct an exact hidden-variable binary encoding.

**Solution.** The allowed triples are 000, 011, 101 and 110. Projecting onto any pair gives all four Boolean pairs: for every selected pair there is exactly one value of the third variable completing even parity. Hence the triangle of pairwise projected constraints permits all eight triples, including invalid 001. It is not an equivalent representation.

Introduce auxiliary variable H with four domain values, one for each allowed triple. Connect H to X, Y and Z by projection constraints requiring each original value to equal the corresponding coordinate of H's chosen tuple. Any even-parity assignment extends by its own tuple H. Conversely, satisfying those three binary constraints forces X,Y,Z to be exactly an allowed H tuple. This proves equivalence in both directions.

The extra variable has tuple-valued states, not four independent choices for each coordinate. For a general arity-k table, its domain can have up to $d^k$ tuples. The encoding is finite and exact, but its size and propagation behavior must be accounted for; reducing arity is not a universal compression theorem.

## IC28 | Bare n-consistency can be vacuously true

**Origin.** Original consistency-hierarchy counterexample.

**Question.** Three singleton-domain variables A,B,C each have domain {0} and pairwise inequality. Is the system 3-consistent under the extension definition? Is it strongly 3-consistent or satisfiable?

**Solution.** There is no consistent assignment to any pair: the only pair (0,0) violates its inequality. The statement “every consistent assignment to two variables extends to the third” is therefore vacuously true, because there are no consistent two-variable assignments to test. Thus bare 3-consistency holds under that quantified definition.

The system is not 2-consistent. The consistent singleton assignment A=0 cannot be extended to B, since B's only value is equal to A. Consequently it is not strongly 3-consistent, which requires all lower consistency levels too. It is also unsatisfiable, directly from any one inequality edge.

This example explains why a backtrack-free theorem must include strong consistency and a usable nonempty unary-consistent base. Bare high-order extension statements may become true for the unhelpful reason that lower-order assignments already do not exist. Do not read a universal statement over an empty set as an existence assertion. The failure is logical, not a detail of which queue order AC-3 uses.

## IC29 | Remove an allowed pair with no third-variable extension

**Origin.** Original path-consistency problem.

**Question.** Let X,Y,Z be Boolean, with X=Y, Y=Z and X≠Z. Show that binary arcs are consistent but path consistency can remove every allowed X,Y pair.

**Solution.** Equality supports each value by itself, and inequality supports it by its complement, so every directed binary arc has a witness. For path consistency, consider an allowed pair on X=Y. Pair (0,0) requires Z=0 under Y=Z but Z=1 under X≠Z. No single Z supports both requirements, so the pair is removed. Pair (1,1) similarly requires both Z=1 and Z=0 and is removed.

The effective X,Y relation becomes empty. That is a joint-pair failure, which a relation-filtering algorithm can then propagate to domains or use directly to report inconsistency. It does not follow from merely intersecting X's and Y's domains, both of which originally contain two values. The stronger algorithm changes a relation table as well as, potentially, unary domains.

All three constraints are needed for the contradiction. Testing X=Y and Y=Z alone allows the all-zero and all-one solutions; testing the third separately supplies supports that are incompatible with those joint extensions. The pair-support table shows precisely the two contradictory requirements on Z, rather than treating three unrelated successful edge tests as a joint solution.

## IC30 | Count attacking pairs, not conflicting queens

**Origin.** Original min-conflicts calculation.

**Question.** On a four-column board, queen rows are (1,1,3,4). Count attacking pairs. If only Q1 may change, compute the conflict count for each row choice and state every best one-variable move.

**Solution.** Initially the attacking pairs are (Q1,Q2) in the same row, (Q1,Q3) and (Q1,Q4) on diagonals, and (Q3,Q4) on a diagonal. The other two pairs do not attack, so the score is four. This counts constraints, not four queens or a double count of both directed pair orders.

The Q3,Q4 conflict is unaffected by moving Q1 and always contributes one. With Q1=1, its own three attacking pairs remain, totaling four. With Q1=2, it attacks Q2 diagonally but neither Q3 nor Q4, totaling two with the unaffected pair. With Q1=3, only its same-row attack on Q3 remains, again totaling two. With Q1=4, it shares a row with Q4, also totaling two. Thus rows two, three and four tie as best local moves.

None gives a zero-conflict solution because Q3,Q4 still attack. A complete tie rule must decide which move the implementation chooses. One locally best move is not a certificate of global optimality or unsatisfiability.

## IC31 | Finite assignments do not rule out a plateau cycle

**Origin.** Original termination problem.

**Question.** Two Boolean variables have an objective that is identically one for all four assignments. A coordinate-update method changes a selected variable to another maximizing value whenever possible. Does finiteness prove termination? Give a repair and its limitation.

**Solution.** Every value of every variable is maximizing because the score never changes. An implementation can alternate X=0 and X=1 forever while leaving Y fixed. It visits only two of the four states, so having finitely many assignments does not prevent an infinite revisit cycle. Nondecreasing objective values are not strictly increasing objective values.

One repair is to retain the current value on equal scores and stop after a full sweep with no strict improvement. In a finite state space, strict improvements cannot continue indefinitely because only finitely many objective values exist. This establishes termination under that policy. It does not establish global optimality for a nonconstant objective: a state can have no improving one-variable neighbor while a distant assignment scores better. Another policy may allow a bounded number of sideways moves or random restarts, but its stopping and completeness properties require separate analysis. A lecture statement about convergence must identify the actual tie/stopping convention rather than infer it merely from a finite number of states.

## IC32 | A partial product need not upper-bound a completion

**Origin.** Original weighted-factor branch-and-bound problem.

**Question.** A partial assignment has evaluated-factor product two. The best complete assignment seen so far has weight five. One unevaluated factor can reach ten. Is pruning on 2<5 sound? Derive a valid crude bound and state when the partial product itself is an upper bound.

**Solution.** Pruning is unsound: a completion attaining the remaining factor ten would have weight $2\cdot10=20$, exceeding the current best five. The partial product omits factors whose scope is not yet fully instantiated; it is not automatically a bound in the maximization direction.

If each unevaluated nonnegative factor has a valid upper bound $u_j$ over all completions still permitted by the branch, then $U=2\prod_j u_j$ upper-bounds every completed product. Shared variables can prevent all individual maxima from being simultaneously attainable, making U loose, but not too small. Prune only when that valid upper bound cannot improve the incumbent, with tie handling matched to whether all optima are requested.

If every remaining factor is at most one, multiplying them cannot increase a nonnegative product, so the partial product is itself an upper bound. A factor greater than one invalidates that shortcut. Taking logs also needs care: zero factors have logarithm minus infinity and cannot be silently treated as ordinary finite costs.

## IC33 | The written voting factor graph

**Origin.** Adapted from Stanford CS221 Spring 2026, Definitions, voting example.

**Question.** Three variables choose B or R. Factors are $[X_1=B]$, $[X_1=X_2]$, $[X_2=X_3]+2$ and $[X_3=R]+1$. Compute every positive-weight complete assignment and identify the optimum.

**Solution.** The first factor forces X1=B for any positive weight. The second then forces X2=B. Every assignment violating either condition has product zero regardless of the remaining factors. Only X3 remains free.

For (B,B,B), the factors are 1,1,3,1 and their product is three. For (B,B,R), they are 1,1,2,2 and the product is four. Thus the only positive-weight assignments are these two, with unique optimum (B,B,R). The third factor's preference for agreeing with X2 is outweighed by the fourth factor's preference for red: local preferences must be combined rather than optimized independently.

The factors are nonnegative scores and were not specified as probabilities. No normalization is needed to compare their products, but calling four a probability would be invalid. If the task were plain feasibility, either positive assignment would suffice. For maximum weight, returning the first feasible (B,B,B) without a bound or exhaustive continuation would give the wrong answer.

## IC34 | A narrow beam can discard the only solution

**Origin.** Original counterexample to completeness of approximate search.

**Question.** Boolean X,Y have unary weight f(X)=3 for X=0 and 2 for X=1. Their only allowed binary tuple is (1,0). Use variable order X then Y and beam width one, ranking partial products without lookahead. Compare with beam width two.

**Solution.** At depth one, the binary factor is not fully instantiated, so partial weights are three for X=0 and two for X=1. Width-one selection keeps X=0 and discards X=1. At the next depth, both Y values violate the binary relation, so the retained branch has no feasible completion. The algorithm reports failure even though (1,0) is a valid solution of weight two.

With width two, both depth-one assignments survive. At depth two, the only positive candidate is (1,0), which is retained and returned. This example specifies that no AC preprocessing or lookahead was used; full AC would have removed X=0 earlier and would change the trace. Approximate algorithms must be compared under their declared filtering assumptions.

The counterexample establishes that beam failure is not an unsatisfiability certificate and that a small beam lacks the complete backtracking guarantee. Increasing the width can help, but a finite width smaller than an entire frontier still does not supply a universal correctness theorem or approximation ratio.

## IC35 | A zero unaffected factor breaks a strict-improvement claim

**Origin.** Original coordinate-ascent boundary problem.

**Question.** A weighted factor product contains f(Y)=0 at the current fixed Y and g(X), with g(0)=1 and g(1)=9. Does changing X from zero to one strictly improve the complete objective? Explain the usual locality shortcut's missing hypothesis.

**Solution.** Both full products are zero: $0\cdot1=0$ and $0\cdot9=0$. The local factor involving X increases, but the complete objective does not. Hence a statement that maximizing just the changed factors strictly improves the full product is false when the omitted common factor is zero.

If the product C of all unaffected factors is strictly positive, comparing $Cg(a)$ is equivalent to comparing g(a), and strict local improvements remain strict globally. If C=0, all these coordinate choices tie in full objective. A solver may still deliberately choose the locally larger factor to seek later escape, but it must not claim a strict global ascent certificate or use that claim as its termination proof.

With nonnegative factors, omitting a nonnegative common constant cannot reverse an ordering; the issue at zero is loss of strictness and inability to infer global progress. A repair strategy for feasibility may instead minimize the number of violated hard constraints, but that is a different objective whose properties must be stated.

## IC36 | Merge explanations before the next backjump

**Origin.** Adapted from MIT 16.410 Lecture 7a, PDF pages 13–17; notation and reasoning independently reconstructed.

**Question.** A dead variable6 has conflict set {4,1,0}. Variable4 currently has conflict set {2,0}. Index0 is a termination sentinel. Give the deepest-conflict jump, the merged set at4 and the next jump if4 is exhausted too. Explain why a static neighbor list is insufficient.

**Solution.** The deepest actual prior decision in Conf(6) is4, so jump from6 to4 and undo intervening decisions5 and6. Transfer the older causes of the exhausted branch to4: $\operatorname{Conf}(4)\leftarrow\operatorname{Conf}(4)\cup(\operatorname{Conf}(6)\setminus\{4\})$. The result is $\{2,0\}\cup\{1,0\}=\{2,1,0\}$. If every remaining value at4 then fails with this accumulated explanation, the next deepest decision is2, so the next jump is4→2.

Index0 is not a real variable to assign; it represents no earlier decision/termination in this convention. Reasons must justify rejection of every exhausted candidate, and the merge preserves earlier assumptions needed for that explanation. Omitting1 could lead the next failure handling to forget an actual cause.

Static graph adjacency describes possible direct constraints, whereas propagation or earlier backjumps can introduce explanations involving nonadjacent decisions. A full FC/MAC backjumping implementation must track those reasons explicitly; the ordinary binary laboratory does not claim to implement this conflict-directed extension.

## IC37 | A branch deletion is not a global learned fact

**Origin.** Original learning-soundness problem.

**Question.** Boolean X,Y satisfy equality. In branch X=1, propagation deletes Y=0. May the solver permanently delete Y=0 from the original problem? Give a valid learned relation and explain the distinction.

**Solution.** Permanent deletion is unsound because (X,Y)=(0,0) is a valid original solution. The deletion was justified only under X=1. On returning to the root and trying X=0, Y=0 must be available again.

A valid global nogood is the incompatible partial assignment X=1,Y=0. Its negation, “X≠1 or Y≠0,” is implied by the original equality relation. The full original relation also excludes X=0,Y=1. Either logical consequence preserves both legitimate equal assignments. In contrast, deleting Y=0 unconditionally imposes a stronger restriction not implied by the original system.

The distinction is between a conditional inference and a theorem about every solution. Recording an explanation with its assumptions allows safe learning; keeping only the deleted value loses the condition that made the inference true. A trail restores temporary changes, while a learned constraint may survive restoration only if its global logical validity has been established. Neither mechanism can be replaced by a list of values that happened to fail in some prior branch.

## IC38 | Derive the coarser repeated-sweep bound

**Origin.** Course-derived complexity comparison, MIT 16.410 Lecture 6, PDF pages 4–7.

**Question.** AC-1 repeatedly sweeps every directed arc until no domain changes. For n variables, e directed arcs and largest domain d, derive a naive upper bound and compare the reason for AC-3's tighter worklist bound.

**Solution.** One sweep revises all e arcs, each at O(d²) naive pair-check cost, so a sweep costs O(ed²). Every nonfinal changed sweep deletes at least one value. At most nd values can be deleted from the starting domains. Allowing a final unchanged sweep gives O(nd+1) sweeps and time $O(ed^2(nd+1))$, commonly written $O(end^3)$ for nondegenerate n,d≥1. An immediate wipeout return can reduce this count.

AC-3 does not rescan every arc after an unrelated deletion. It schedules an arc when its supporting head domain changes, charging at most O(d) revisions to that arc. This yields O(ed³) under the chapter's directed-arc and constant-lookup contract. The improvement comes from selective dependency tracking, not from making a single REVISE operation asymptotically cheaper.

Both are solution-preserving filters and both can miss the unsatisfiability of an arc-consistent odd cycle. The complexity comparison concerns reaching local consistency, not solving arbitrary CSPs in polynomial time. Initial isolated empty domains still require a separate guard.

## IC39 | Copying domains and trailing have different storage costs

**Origin.** Original implementation-analysis problem.

**Question.** At each depth of a depth-n binary CSP search, a simple implementation copies all n domains of size at most d. Compare its worst path storage with a deletion trail, and separate teaching traces and stored solutions from solver state.

**Solution.** One full domain copy costs O(nd) values. If a recursive path retains one such copy at each of O(n) levels, domain snapshots alone can occupy O(n²d) space. This is safe for rollback but not the lean O(nd) domain-state bound sometimes quoted for a single propagation invocation.

A trail shares one current domain state and records deletions with branch markers. Along one descending branch, a given original variable-value pair can be deleted at most once before restoration, so at most O(nd) such live deletion records are needed, plus recursion/assignment bookkeeping. The implementation must actually restore records in reverse to their markers; the bound does not excuse missing rollback information or mishandled support caches.

If the program stores every visual snapshot or collects exponentially many complete solutions, output storage can dominate either bound. A streaming first-solution solver, a solution enumerator and a teaching recorder therefore have different total memory use. Counts should specify whether relation-table input, temporary queues, recursion and accumulated output are included.

## IC40 | The heuristic can cost more than the next branch

**Origin.** Original heuristic-cost derivation.

**Question.** A selected variable has at most d candidate values and δ unassigned neighbors, each with at most d values. With constant-time binary lookup, derive the cost of one-step deleted-value LCV for all candidates. Contrast trial-MAC LCV.

**Solution.** For one candidate a, inspect each neighbor value b and test the relation with the now-singleton a. There are at most δd such tests, giving O(δd) cost for that candidate. Evaluating every one of at most d candidates gives O(δd²), before ordering their scores. Sorting all scores can add O(d log d), or a first-choice scan can simply select a minimum without constructing a complete sorted list.

Trial-MAC LCV runs an entire propagation invocation for each candidate, potentially costing O(ed³) per candidate with a naive AC-3 implementation, hence O(ed⁴) as a coarse all-candidate bound. Domain copying/restoration and score computation add their own costs. Incremental caching can improve particular implementations but must preserve correct branch state.

Thus “LCV improves search” is a heuristic expectation, not a theorem that its overhead always pays off. State whether the score counts one-step deletions, full propagation deletions or something else; these policies can choose different orders as well as incur different costs.

## IC41 | Constraint lookup is a model assumption

**Origin.** Original representation-cost problem.

**Question.** Compare a hashed explicit binary relation table with a predicate whose evaluation scans a length-L list. How do the REVISE and AC-3 costs change? What cost is hidden by calling the constraint constant time?

**Solution.** A naive revision can test up to d² candidate pairs. With expected constant-time hash membership, its expected lookup work is O(d²), while storing a dense explicit table can cost O(d²) pairs per edge. A deterministic constant-time membership representation such as an indexed Boolean matrix has the same pair-count bound with its stated indexing/input-size assumptions.

If each predicate call scans L items, the same revision instead costs O(Ld²). Combining with O(ed) revisions gives O(eLd³) predicate work for AC-3. Building the tables or compiling/indexing the predicates is separate preprocessing and may itself require significant time or memory.

The number of relation tests and the cost per test are different quantities. A teaching trace can count exact tests independently of runtime. It must not silently use an expensive arithmetic, graph or scheduling oracle inside each test while claiming a whole-algorithm constant-cost bound. Input representation also matters when a higher-arity table has exponentially many tuples.

## IC42 | A failed branch with solutions elsewhere

**Origin.** Original fully specified counterexample used to check the authentic AC-3 scope question.

**Question.** Boolean X,Y,Z satisfy relations $R_{XY}=R_{XZ}=\{(0,0),(1,0),(1,1)\}$ and Y≠Z. Show the initial CSP is arc consistent, explain failure under X=0 and enumerate the original solutions.

**Solution.** Initially X=0 has support zero at either neighbor, and X=1 has both supports. Each neighbor value has support X=1; zero also has support X=0. The Y,Z inequality supplies opposite-value supports. Thus all six directed arcs are consistent on full domains.

In branch X=0, the two X relations force Y=0 and Z=0. The inequality edge then has no valid pair, and MAC detects a wipeout. That proves no complete solution extends X=0.

If X=1, both neighbor domains remain Boolean until their inequality is applied. The allowed completions are (Y,Z)=(0,1) and (1,0). Therefore the original solutions are precisely (1,0,1) and (1,1,0). They verify that an intermediate branch failure cannot be promoted to a statement that the root CSP has no solution. Conversely, the initial nonempty arc-consistent domains did not imply that the branch X=0 would be extendible. Both distractor directions confuse a local statement's scope.

## IC43 | Solve through a component product, not an average

**Origin.** Original application of independence and counting.

**Question.** One independent CSP component has four complete solutions. Another is a three-variable three-color inequality path. A third component has a single fixed compatible variable. Find the total solution count. If a new edge links the first two components, may the product rule still be used unchanged?

**Solution.** The path has $3\cdot2\cdot2=12$ solutions, as each selected parent color permits two different child colors. The fixed-variable component contributes exactly one. With no cross constraints, every combination of component assignments is valid and every full solution decomposes uniquely, giving $4\cdot12\cdot1=48$.

A new linking edge can forbid some of those combinations. The unconditional product rule then no longer applies. One can condition on the linked endpoint values and sum products of conditional counts, or treat the connected union as one problem. Even if the new edge happens to be redundant for the particular solution sets, that fact must be proved; graph connectivity changes invalidate an automatic independence assumption.

Counting alternatives by adding four and twelve would count assignments for only one component at a time, leaving other variables unspecified. Averaging component counts has no solution-set interpretation. The multiplicative formula follows from a Cartesian-product bijection, which is the fact to check before applying it.

## IC44 | Color symmetry needs uniform interchangeable colors

**Origin.** Original symmetry-breaking problem.

**Question.** A three-color triangle has no unary restrictions. If A is fixed to red, count the remaining solutions and recover the original count by symmetry. Give a unary restriction that makes blindly fixing A to red unsound for existence.

**Solution.** Once A is red, B and C must use the two other colors in different orders, giving two solutions. Because the original constraints distinguish only equality/inequality and every vertex initially has the same three-color palette, relabeling colors is a bijection between solutions with A red, A green and A blue. These three disjoint classes have equal size, so the original count is $3\cdot2=6$.

Now impose the unary condition A=green. The restricted original CSP still has two solutions, with B,C red/blue in either order. Fixing A red makes it impossible and destroys every solution. Color names are no longer interchangeable under the unary domain specification.

Symmetry breaking is justified by an actual solution-preserving orbit argument, not by a diagram looking symmetric or colors seeming arbitrary. For counting, one must also know orbit/class sizes; removing symmetric representatives without correct multiplicities can give a wrong total even when existence is preserved.

## IC45 | The gallery capacity constraint is essential

**Origin.** Adapted from Stanford CS221 Spring 2026, Examples, sculpture-gallery prompt.

**Question.** Three sculptures A,B,C use rooms one or two. A and B must occupy different rooms, B and C the same room, and room two can hold at most one sculpture. Find every assignment and explain the role of the capacity constraint.

**Solution.** Equality B=C puts those two sculptures together. They cannot both use room two because that would place two sculptures in a room of capacity one. Thus B=C=1. The inequality A≠B then forces A=2. The assignment (A,B,C)=(2,1,1) satisfies the capacity and both relational conditions, so it is a solution and the deductions show it is unique.

If capacity were omitted, the additional assignment (1,2,2) would satisfy A≠B and B=C. It is precisely the globally invalid capacity use that the missing condition must reject. Since B=C is already known, one can derive a unary restriction B≠2, but that is an inference from both equality and capacity, not an original independent domain fact.

In a general scheduling model the capacity constraint may have higher arity or be represented by several smaller restrictions. Either encoding must preserve the original allowed complete assignments. Do not silently count a locally consistent equality pair as a valid room allocation without checking the room's occupancy limit.

## IC46 | Verify equivalent scheduling encodings by a bijection

**Origin.** Adapted application of Stanford's two event-scheduling formulations; numerical data are original.

**Question.** Event P may use slots one or two, event Q slots two or three, and a slot holds at most one event. Enumerate event-variable solutions. Express the corresponding slot-variable assignments with an empty marker.

**Solution.** Event-variable domains are $D_P=\{1,2\}$, $D_Q=\{2,3\}$, with P≠Q. Their four initial pairs are (1,2),(1,3),(2,2),(2,3); only the equal-slot pair is forbidden. Thus there are three schedules.

In slot variables $(S_1,S_2,S_3)$, those schedules become respectively $(P,Q,\emptyset)$, $(P,\emptyset,Q)$ and $(\emptyset,P,Q)$. Require each event to occur exactly once, each slot to name at most one event, and event-slot eligibility. Then every valid event assignment determines exactly one slot assignment and vice versa, establishing a bijection and the same count.

If “each event exactly once” were weakened to “at most once,” the all-empty slot assignment would be admitted although both events must be scheduled. Conversely omitting the empty marker would force every slot occupied by some event and would make three slots incompatible with just two once-only events. Equivalent models need all occupancy semantics, not just similarly named variables.

## IC47 | Verification searches for a counterexample

**Origin.** Adapted from Stanford CS221 Spring 2026, Examples, program-verification prompt.

**Question.** Over exact real arithmetic, a program sets $a=x^2$, $b=a+y^2$, $c=b-2xy$ and returns c. Encode a counterexample to c≥0 as a constraint problem, then decide it mathematically. State the arithmetic boundary.

**Solution.** Use variables x,y,a,b,c, constraints $a=x^2$, $b=a+y^2$, $c=b-2xy$ and the negated specification c<0. A satisfying assignment would describe a valid program execution whose output violates the requested property. Substituting the first three equations gives $c=x^2+y^2-2xy=(x-y)^2$, which is nonnegative over the reals. Hence the counterexample constraints are unsatisfiable, proving the specification under that exact-real model.

This is not a finite binary domain problem, so the chapter's laboratory does not claim to decide it by AC-3. The proof uses algebraic reasoning. Also, source-language assignment and mathematical equality are different operations: the constraints check consistency of a whole execution tuple and need not be evaluated in program order.

Finite-width floating-point evaluation, overflow, NaNs or other language-specific semantics require a different formal model. The exact-real identity alone is not a certificate for every machine implementation. Tests of finitely many inputs likewise do not establish the universal exact-real assertion, whereas the displayed algebraic proof does.

## IC48 | A cached support must still be alive

**Origin.** Original incremental-support implementation problem.

**Question.** Let $D_X=\{1,2\}$, $D_Y=\{a,b\}$ and relation $R=\{(1,a),(2,b)\}$. A solver caches support a for X=1. Another propagation removes a from Y. What must the solver do, and what goes wrong if it trusts the stale cache?

**Solution.** Before using the cached witness, test that a is still in the current Y domain and that the pair remains allowed. It is no longer alive. Search for a replacement support for X=1 among the remaining domain {b}; pair (1,b) is absent, so X=1 must be removed. X=2 still has support b and remains. The resulting single pair (2,b) is the only complete solution under the new restriction.

A stale-cache shortcut would retain X=1 even though the declared arc-consistency condition fails. Caching can save repeated searches but cannot redefine what counts as a support. Backtracking adds the opposite issue: restored values or support counts must correspond to the restored branch, so a cache update policy needs a clear lifetime/validation contract.

The example uses symbolic a,b conceptually; a finite integer-coded implementation can preserve the same table with an explicit legend. The correctness obligation is membership in the current domain and relation, not whether the candidate once served as a witness earlier in the search.

## IC49 | Count cycle colorings with a two-state recurrence

**Origin.** Original hard mathematical transfer.

**Question.** Derive the number of proper d-colorings of a labeled cycle of length k≥3. Specialize to d=3,k=4 and to d=2 with odd/even k. Explain why domain sizes alone miss the answer.

**Solution.** Fix the first vertex color. Let $a_m$ count proper colorings of a path of m vertices whose last color equals the first, and $b_m$ those whose last color differs. Initially $a_1=1$ and $b_1=0$. To append a vertex, a previous different last color has exactly one choice returning to the first color, so $a_{m+1}=b_m$. A previous equal last color has $d-1$ different choices; a previous different one has $d-2$ choices staying different from the first. Hence $b_{m+1}=(d-1)a_m+(d-2)b_m$.

The total path count for a fixed first color is $a_m+b_m=(d-1)^{m-1}$, because every appended vertex has exactly $d-1$ choices. Substituting $a_m=(d-1)^{m-1}-b_m$ into the second recurrence gives $b_{m+1}=(d-1)^m-b_m$. Its base value is zero. Suppose the claimed formula holds at m; then

$$b_{m+1}=(d-1)^m-\frac{(d-1)^m+(-1)^m(d-1)}{d}=\frac{(d-1)^{m+1}+(-1)^{m+1}(d-1)}{d}.$$

The formula also gives $b_1=0$, completing induction for $d\ge2$. The closing cycle edge requires the last color differ from the first, so the total cycle count is $d b_k=(d-1)^k+(-1)^k(d-1)$. For three colors on a four-cycle this is $16+2=18$. For two colors it is $1+(-1)^k$, zero for odd k and two for even k.

For d=1 every cycle with an edge has zero solutions, handled directly. The identical one-vertex domain size d does not encode the parity/joint closing-edge restriction, explaining AC's limitations on the two-color examples.

## IC50 | Prove the greatest closure instead of guessing it

**Origin.** Original advanced fixed-point proof.

**Question.** A fair AC procedure processes existing arcs and deletes only unsupported tail values until full closure, without stopping early on a wipeout. Show its final domain family contains every arc-consistent subfamily of the original domains. Deduce schedule independence, and explain the early-failure qualification.

**Solution.** Let E be any arc-consistent family contained in the initial domains. Initially every E value is present. Assume this remains true just before deleting a from the current tail domain Di. If a belonged to Ei, arc consistency of E would provide a compatible b in Ej. By induction b is still in the current head domain, contradicting the claim that a has no support. Thus a is not in Ei, and every deletion preserves the containment E⊆D.

At full fair closure, the resulting D* is itself arc consistent, because any head-domain change that could invalidate an earlier arc is eventually reconsidered. The containment proof shows E⊆D* for every initially contained arc-consistent E. Therefore D* is the greatest such family. Two fair full-closure runs each produce that greatest family, so their final domains coincide.

An implementation that stops immediately at the first empty domain returns a valid failure certificate but may leave other domains only partly filtered. Different schedules can then show different intermediate failure snapshots; those snapshots are not both claimed greatest closures. Boolean failure status and the entire returned domain vector have different reproducibility guarantees.
