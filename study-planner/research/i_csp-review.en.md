# Summary and complete examination decisions

## Synthesis: what each layer actually proves

A model defines the problem: variables name choices, domains name permitted values, and relations specify jointly legal tuples. A complete solution must satisfy every original relation. A locally consistent partial assignment has passed only the fully instantiated constraints; it may have no completion. Binary support filtering removes a tail value only when no compatible head value remains. That deletion is sound because any putative solution containing the tail value would itself have supplied a head witness.

AC-3 manages dependencies between these tests. A head-domain change can invalidate incoming supports, so affected arcs return to the queue. Within one invocation, domains only shrink and finitely many values can disappear. A successful fixed point certifies local support, not a joint solution. A wipeout refutes the current branch; it refutes the original problem only when its assumptions are the root conditions, or when a complete surrounding search exhausts every alternative.

Backtracking obtains completeness by eventually trying every necessary candidate under exact rollback. MRV, residual degree and LCV order that work; they are not independent logical pruning rules. MAC combines sound support filtering with complete branching. Tree structure allows a stronger polynomial construction because separately supported child subtrees do not share cross constraints. Conditioning on a supplied cycle cutset recovers that structure at an exponential cost in the cutset size. Global constraints and stronger consistency enforce genuinely joint witnesses that separate pairwise tests may miss. Local repair and narrow beams can be effective, but their unsuccessful termination does not certify impossibility.

Use the following decisions after the full lesson. Each includes a condition or reason so that it can be transferred to a new problem rather than memorized as an isolated slogan.

## Modeling and counting

1. **Name the requested object before counting.** Complete assignments, distinct partial maps, action-order paths, tree nodes and relation tests are different sets; a count for one does not answer a question about another.
2. **Count independent choices only before imposing their coupling constraints.** Uniform domains give $d^n$ complete tuples, but that is generally an upper bound on solutions, not the number of solutions.
3. **Charge the permutation factor only when assignment order is an action choice.** Allowing all variable orders produces $n!d^n$ complete paths; selecting one next variable at each state removes this particular redundancy.
4. **Use the partial-map count for arbitrary scopes.** Each variable is absent or has one of d values, giving $(1+d)^n$ distinct partial assignments; a fixed-order tree visits only prefix scopes.
5. **Include internal nodes when asked for the whole tree.** Its unconstrained fixed-order size is $\sum_{k=0}^n d^k$; for d=1 this is n+1, so a geometric-series division by d−1 must be avoided.
6. **Treat a domain as a set rather than an interval.** Filtering can leave holes, and replacing a set by its minimum–maximum interval silently restores forbidden values.
7. **Distinguish local legality from extendibility.** Satisfying all currently instantiated constraints does not prove that the remaining variables can be assigned.
8. **Check occupancy in alternative encodings.** At-most-one queen or event restrictions permit empty arrangements unless exactly-one requirements are supplied.
9. **Conjoin predicates on the same pair when joint pair support is claimed.** A witness for equality and another for inequality cannot satisfy their conjunction.
10. **Transpose an asymmetric relation on a reversed arc.** Filtering Y against X under X<Y checks the original allowed pairs in reversed coordinate order; it does not add Y<X.
11. **Retain higher-arity information explicitly.** Pairwise projections of even parity are unrestricted and therefore do not reconstruct the original triple relation.
12. **Account for an auxiliary tuple domain.** Hidden-variable conversion is exact, but an arity-k relation can require $d^k$ tuple states and is not automatically a compact encoding.

## Branching and heuristics

13. **Specify the problem's stopping rule.** One verified solution solves feasibility, whereas counting all solutions or proving a weighted optimum requires continued work or a valid certificate.
14. **Restore every temporary deletion before a sibling branch.** A contradiction under X=1 does not justify carrying its empty domains into X=0.
15. **Separate assignments from singleton domains.** Filtering can force a value without increasing recursive assignment depth; traces must identify which record they describe.
16. **Apply MRV to current legal possibilities.** Raw initial sizes can be misleading after earlier assignments unless legal values are recomputed or maintained.
17. **Use residual degree only at its declared priority.** A high-degree variable does not override a strictly smaller domain under MRV-first ordering.
18. **Count unassigned neighbors for the usual degree tie-break.** Already assigned neighbors explain existing restrictions but do not count as remaining search connections.
19. **State a final tie rule when reproducing a trace.** Alphabetical or declared input order makes tied MRV/degree decisions deterministic; the heuristic names alone may not.
20. **Keep variable selection separate from value ordering.** MRV and degree choose a variable; LCV ranks its candidate values and does not independently select a variable.
21. **Define what an LCV score counts.** Deleting three values in one neighbor and deleting one in each of two neighbors reverse the rankings of deleted-value and affected-neighbor policies.
22. **Do not turn an ordering score into an elimination proof.** A poorly ranked value can still be the only path to a solution and must remain available in a complete search.
23. **Include heuristic overhead in a cost comparison.** One-step LCV over all d candidates costs $O(\delta d^2)$ relation tests; trial propagation can be substantially more expensive.
24. **Qualify symmetry breaking by an actual invariance.** Fixing a triangle's first color is safe under interchangeable palettes, but a unary color requirement can destroy that symmetry.

## Propagation and work bounds

25. **Write the arc direction before deleting values.** In $X\to Y$, only X is revised and Y supplies witnesses; interchanging those roles changes the intermediate trace.
26. **Use the correct quantifier order.** Each tail value needs some compatible head value; all tail values need not share the same witness.
27. **Apply unary restrictions as well as binary propagation.** In the authentic numeric question, removing Z=3 is essential before equality can force Z=W=2.
28. **Check isolated empty domains explicitly.** Such a variable never appears in the queue but still makes the CSP impossible.
29. **Requeue only existing incoming arcs after a shrink.** The neighbors of the changed variable may have lost support; unrelated nonedges do not become constraints.
30. **Justify the skipped immediate reverse arc.** A value removed for having no support could not have been supporting any surviving value on the transposed same relation; this proof relies on the representation contract.
31. **Distinguish a popped arc from a full propagation invocation.** One REVISE costs at most $O(d^2)$ naive checks; the worklist can revisit it after later head-domain changes.
32. **Charge repeated processing to strict head shrinkage.** With one initial copy and immediate wipeout return, a directed arc is revised at most d times in one invocation.
33. **Declare whether e counts directed arcs or undirected edges.** Each undirected binary edge supplies two directions; asymptotic order may agree while an exact numerical bound differs by two.
34. **State the relation-lookup assumption.** The $O(ed^3)$ bound counts constant-cost pair tests; an oracle costing L per test changes the corresponding work to $O(eLd^3)$.
35. **Do not reuse the invocation bound for the whole search.** Restoring domains at many backtracking nodes permits many separate AC-3 runs and exponential total work.
36. **Distinguish forward checking from propagated closure.** After A=0 in A=B=C, one layer reduces B, while MAC also carries that consequence to C.
37. **Use the singleton-head cost when it is actually present.** Assigned-value forward checking scans at most $\delta d$ candidate pairs, unlike a generic arbitrary-domain revision.
38. **Interpret a nonempty AC fixed point as necessary local evidence.** A two-color odd cycle supplies a direct counterexample to treating it as a solution certificate.
39. **Scope a wipeout to its assumptions.** A branch can fail while another branch solves the original CSP; the authentic work-bound question explicitly tests this distinction.
40. **Separate full-closure uniqueness from failure snapshots.** Fair complete filtering has a greatest fixed domain family, but immediate failure can stop before other domains reach that closure.
41. **Validate cached witnesses against current domains.** A value that once supported a candidate cannot continue to justify it after that witness is deleted.
42. **Count trace storage separately from solver storage.** Recording every before/after state or collecting every solution can dominate the live domains, queue and recursion memory.

## Structure and stronger consistency

43. **Prove the tree premise before invoking the tree algorithm.** A single reverse sweep plus forward witness selection is complete on a tree; cycles can carry incompatible joint requirements.
44. **Revise parents against children in reverse order.** Child subtrees must already support their surviving values when those values are used to justify a parent.
45. **Check every root or isolated component for emptiness.** A forest is not automatically satisfiable; each component must pass its own domain and support checks.
46. **Explain why forward tree choices do not collide.** Different child subtrees have no cross edges, so choosing a support in one does not invalidate a sibling subtree.
47. **Separate tree existence from tree counting.** A witness constructs one solution; counting requires sums over compatible child choices and products over independent child subtrees.
48. **Include exact-integer costs when counts are large.** The usual $O(nd^2)$ message count measures arithmetic operations, not an unconditional unit-cost bound on arbitrarily large integers.
49. **Verify that a supplied cutset really leaves a forest.** Removing one vertex from K4 leaves a triangle; two vertices are needed for a cycle cutset.
50. **Check internal and boundary constraints in every cutset branch.** A residual tree does not excuse an already invalid cutset assignment or a missing constraint to an assigned vertex.
51. **Retain enumeration cost when the residual graph is empty.** Setting c=n does not make solving cost zero; up to $d^n$ complete cutset assignments still require verification.
52. **Do not charge cutset discovery to an algorithm that assumes it is given.** Finding a good cutset and exploiting a supplied one are separate computational tasks.
53. **Ask whether witnesses must be jointly compatible.** Pairwise inequality can support Z=1 separately against X and Y while global all-different has no joint tuple containing Z=1.
54. **Use Hall's condition on subsets, not just total counts.** Any subset with too few available values disproves a complete distinct-value allocation, even when every binary arc has support.
55. **Distinguish bare k-consistency from strong k-consistency.** A universal extension claim can be vacuous when no lower-order consistent assignment exists; the constructive theorem requires all lower levels and a nonempty unary base.
56. **Recognize that path consistency filters pairs.** Removing a pair with no joint third-variable extension is stronger than merely deleting unsupported individual domain values.

## Learning, repair and weighted objectives

57. **Preserve antecedents when learning from a branch.** Equality under X=1 excludes the pair (X=1,Y=0), not the original value Y=0 in every branch.
58. **Merge all necessary causes when backjumping.** An explanation for one failed candidate does not explain exhaustion of all candidates; earlier causes must survive the conflict-set union.
59. **Do not interpret failed local repair as an impossibility proof.** Min-conflicts can plateau or cycle, and a finite unsuccessful run does not exhaust the complete assignment space.
60. **Require a tie/stopping policy in a convergence argument.** Strict improvement in a finite state space terminates, whereas arbitrary equal-score moves can revisit states forever.
61. **Distinguish feasibility from maximum weight.** A positive product satisfies all hard zero/nonzero restrictions, but another positive assignment can have a larger product.
62. **Use a valid upper bound before pruning a weighted branch.** A partial product can increase after a remaining factor greater than one; multiply by justified remaining-factor bounds instead.
63. **Do not infer strict global ascent after omitting a zero constant.** Improving changed factors leaves a full product zero when an unaffected factor is zero.
64. **State beam-search completeness and cost assumptions.** A narrow beam can discard the only solution; $O(nKd)$ assumes bounded incremental scoring and linear selection, and excludes other representation costs.

## Final answer protocol

For a new question, write its variables, exact domains and original scopes first. State any branch, palette, tree, lookup or queue assumptions before calculating. Show the mathematical operation that changes a domain, count or bound, then verify the proposed result against the original model. If the original wording omits a necessary premise, identify the intended interpretation and its limit explicitly. A complete solution should teach why the answer follows and why its tempting alternatives fail.
