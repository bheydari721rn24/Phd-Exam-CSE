1. **BFS queue and parent choices.** In FIFO BFS with discovery on insertion, a state's first parent records a minimum-edge route. A selected goal is not expanded under this chapter's convention, so selection and expansion lists differ at termination.

2. **Early BFS goal testing.** BFS can accept a newly generated goal while preserving minimum depth if the root is checked and FIFO layer order is maintained. Its expansion count then differs from a goal-on-removal implementation.

3. **DFS stack direction.** For a right-top stack, reverse the desired successor removal order when pushing. DFS's successor scheduling changes its first solution and parent tree; a trace must declare this convention.

4. **A weighted BFS counterexample.** Positive unequal costs do not make BFS cost-optimal. Always distinguish the minimum-depth objective from the minimum-sum-of-costs objective; the two can choose different routes even on three vertices.

5. **Relaxation is essential in UCS.** Lazy UCS must reject obsolete records before goal testing or expansion. Physical heap removals, valid selections and expansions can have three different counts in the same execution.

6. **The first generated UCS goal is expensive.** For variable nonnegative costs, UCS accepts a goal on valid minimum-key removal. First generation only provides a candidate upper bound and can be arbitrarily worse than the optimum.

7. **A Boolean discovered bit loses the cheapest route.** UCS requires numerical relaxation for frontier duplicates. “Visited once” is insufficient; rejecting every repeated state on generation can lose both cheaper intermediate paths and cheaper goal routes.

8. **Equal-cost duplicate suppression.** When only one cheapest solution is needed, strict best-cost improvement removes redundant equal-cost routes and prevents finite zero-cost cycles from starving UCS. Enumerating all optimal paths is a different task.

9. **Negative suffix without a cycle.** Absence of negative cycles does not justify UCS. Nonnegative suffix costs are needed for its minimum-frontier stopping proof; even an acyclic three-vertex graph can violate optimality with one negative edge.

10. **Positive edges with no positive lower bound.** Strict positivity of individual edge costs does not ensure UCS completeness in an infinite graph. A positive uniform edge bound, or another finite-sublevel condition, is needed to exclude infinitely many cheaper prefixes.

11. **Full tree size.** For a full tree, $b^d$ counts one depth layer while $(b^{d+1}-1)/(b-1)$ counts the root and all earlier layers. An exact operation question cannot replace the sum by its leading term.

12. **The unary exception.** Handle branching factor one separately: exhaustive IDS through depth $d$ visits $(d+1)(d+2)/2$ nodes. Its overhead over a single chain traversal grows with depth rather than approaching a fixed constant.

13. **Exact IDS repeated work.** In exhaustive IDS, multiply each layer size by the number of iterations that reach it. Do not count every layer equally, and do not apply the exhaustive total to an early-stopping final iteration without adjustment.

14. **IDS overhead at large branching.** Root inclusion changes exact IDS totals because the root occurs in every iteration. Compare counts under the same convention; rounded overhead percentages can conceal several visits without making the algorithms inconsistent.

15. **A BFS extra-layer generation count.** Goal-on-removal BFS can generate depth-$d+1$ nodes before selecting the last depth-$d$ goal. Generated-node, selected-node and expanded-node counts must therefore be calculated separately.

16. **Maximum eager DFS frontier.** An eager full-tree DFS frontier can contain $1+(b-1)m$ entries. This is a frontier bound, not a bound on a global discovered set, materialized adjacency lists or copied full paths.

17. **BFS layer memory budget.** Convert exponential frontier counts into bytes using an explicit per-entry model. A single-layer estimate is a lower accounting component, not the total memory required by graph search.

18. **DLS goal at the boundary.** A depth limit forbids expansion beyond the boundary, not recognition of a boundary goal. Test for success before returning cutoff at zero remaining depth.

19. **Cutoff is not failure.** DLS needs solution, cutoff and failure as distinct outcomes. Any unresolved cutoff propagates through an otherwise unsuccessful parent; IDS may stop only on a solution or genuine failure.

20. **The depth-sensitive duplicate trap.** In depth-limited search, a shallower occurrence of the same state can be strictly more useful. Duplicate elimination must preserve remaining budget; a Boolean global mark can make a sufficient limit appear insufficient.

21. **Resetting IDS state.** IDS must not carry ordinary Boolean discovery marks between iterations. A larger depth limit creates new search obligations even for states encountered before.

22. **An acyclic infinite DFS trap.** Cycle checking prevents repeated-state loops but not infinite acyclic descent. DFS completeness still needs a finite reachable graph or another argument excluding endless preferred branches.

23. **Finite graph DFS complexity.** Complexity depends on the input measure. Global-discovery BFS/DFS are linear in an explicit graph's vertices and edges, while an implicitly defined search space can still grow exponentially with depth.

24. **A UCS cost-depth bound.** With uniform edge lower bound $\varepsilon>0$, selected prefixes of cost at most $C^*$ have depth at most $\lfloor C^*/\varepsilon\rfloor$. Their generated children may lie one level deeper.

25. **Tie breaking changes work.** Equal-key ordering can strongly affect selection and expansion counts without changing UCS's returned optimal cost. Infinite tied frontiers require an additional termination or fairness argument.

26. **Stable heap serial numbers.** Use a separate stable tie key for heap records whose states are not orderable. Tie bookkeeping determines reproducibility but must not be mixed into the mathematical path cost.

27. **Parent updates and immutable records.** A path explanation must agree with the cost stored in its search node. Immutable route records make improvements and stale-entry rejection easier to reason about than mixing old costs with overwritten global parents.

28. **Potentially exponential paths in a small graph.** Many distinct paths can share a small state graph. Duplicate pruning saves repeated suffix work only when the merged state retains all information needed for legal future decisions.

29. **Adding a constant to edge costs.** A constant added to each edge creates a depth-dependent change in total cost. It preserves complete-path ordering only under additional constraints such as equal solution lengths.

30. **Positive scaling preserves order.** Strictly positive cost scaling preserves comparisons and minimizers. Zero scaling destroys distinctions, and negative scaling reverses the objective and can violate the search algorithm's edge assumptions.

31. **Bidirectional ideal growth.** The familiar bidirectional $b^{d/2}$ estimate assumes comparable, searchable fronts. It is an ideal growth argument, not a universal bound on every directed graph or goal predicate.

32. **Reverse edges are not reverse actions.** Backward search enumerates predecessors in the reversed graph. Its computational reverse edge must be translated back into the corresponding legal forward action when reconstructing the plan.

33. **A bidirectional stopping certificate.** Bidirectional UCS may stop when valid frontier minima sum to at least the best complete connection cost, provided relaxation, reverse transitions and crossing updates maintain the required lower-bound invariant.

34. **First contact is only an upper bound.** A feasible connection supplies an upper bound. Weighted bidirectional search needs a frontier lower bound to certify it; the first meeting alone does not establish optimality.

35. **Dictionary segmentation with BFS.** When segmenting a string to minimize dictionary-word count, character index is a sufficient state if future validity and costs depend only on the remaining suffix. Unit-cost BFS then minimizes the number of words.

36. **Previous-word dependent costs.** A state key must determine future transition costs as well as legal actions. History-dependent word costs require retaining the relevant previous-word context rather than merging all paths at one character index.

37. **Maximizing word count is a different problem.** Changing an objective can change both the appropriate edge costs and the correct algorithm. Negative word rewards on an acyclic segmentation graph invite topological dynamic programming, not unqualified UCS.

38. **Collision-free joint states.** For labelled robots occupying distinct cells, use a falling factorial rather than an independent product. Valid joint states do not by themselves guarantee collision-free joint transitions.

39. **State legality does not prevent edge-swap collision.** Collision-free endpoint states are insufficient when edge swaps are forbidden. Put transition-level conflicts into the successor function before applying shortest-path search.

40. **A complete algorithm choice.** Choose search by objective, edge assumptions, state-space finiteness and memory constraints. No single uninformed algorithm dominates every task, and reachability is weaker than minimum-cost optimization.

41. **Failure on a finite cyclic graph.** Finite state count does not make unrestricted tree search terminate on cycles. Global discovery or exhaustive simple-path checking supplies a finite search domain, with different time and memory costs.

42. **Infinite branching defeats the BFS argument.** BFS's finite-depth completeness proof also requires finite, effectively enumerable branching. A shallow goal alone does not guarantee that an infinitely branching root expansion ever finishes.

43. **The start is already a goal.** An initial goal yields a zero-action solution of cost zero. Distinguish that successful empty plan from failure, and count its selection without inventing a successor expansion.

44. **Nondecreasing selected UCS keys.** Nonnegative step costs make valid UCS selection costs nondecreasing. The proof compares newly generated costs with the current minimum, not with arbitrary last-edge magnitudes.

45. **Prefix cost versus last-edge cost.** UCS prioritizes accumulated start-to-node cost. Choosing the cheapest final edge ignores the prefix and does not implement the algorithm's optimality invariant.

46. **A bound with rational edge costs.** Apply the floor after dividing exact cost quantities. A cost-derived depth bound counts possible layers, while actual UCS work depends on which prefixes really lie within the cost contour.

47. **Comparing two IDS depths.** Repeated IDS work remains geometric when fixed branching exceeds one because the weighted reverse-layer series converges. The unary case must not be hidden inside that asymptotic argument.

48. **Generated versus accepted duplicates.** Frontier conservation uses accepted insertions, not every generated candidate. Rejected duplicates never occupy the frontier, while every physical removal reduces its size regardless of later processing.

49. **Discovery at insertion versus removal.** Marking BFS states only on removal can leave duplicate frontier entries. Correctness may survive with later rejection, but the one-entry-per-state storage and count claims no longer follow.

50. **Global discovery can alter a DFS parent.** Eager sibling discovery and recursive-entry discovery can produce different DFS parent trees. An alphabetical traversal description alone does not fix the implementation or returned route.

51. **A sufficient limit is not cost optimality.** DLS's limit is a feasibility boundary. It does not make the first found solution shallowest or cheapest, even when the optimal route lies within the limit.

52. **Finite unsolvable IDS.** Path checking bounds accepted route length by $V-1$ in a finite graph. Correct failure propagation lets IDS terminate on unsolvable finite instances, although repeated simple-path enumeration may be expensive.

53. **All equal zero costs.** Zero costs do not invalidate conditional optimality, but they separate cost optimality from minimum depth and make infinite-space termination assumptions especially important.

54. **A finite graph optimum can be simple.** With sufficient states and nonnegative costs, cycles can be removed without worsening a route. A simple optimum exists on a finite graph, even if infinitely many zero-cycle variants share its cost.

55. **Negative cycle that cannot reach a goal.** A negative cycle makes the goal objective unbounded only when it lies on some start-to-goal walk. This objective condition does not restore UCS's nonnegative-edge guarantees.

56. **Choosing a complete frontier schedule.** Fair eventual processing of each finite-prefix candidate can establish completeness without strict BFS order. Minimum-depth optimality still requires the stronger layer-order argument.

57. **The wrong state key loses a door plan.** Duplicate-state dominance requires identical future capabilities. Retain possession, permissions and other enabling resources in the state key when they change legal continuations.

58. **Cost and fuel need multiple labels.** When future feasibility depends on resources, cheaper prefix cost alone is insufficient dominance. Preserve resource state or retain nondominated labels under explicitly proved monotonicity assumptions.

59. **Depth parity as a hidden state component.** Retain the smallest temporal information that determines future legality. Periodic constraints may require time modulo a period, while deadlines can require a different, larger time representation.

60. **BFS with nondecreasing depth costs.** Equal edge costs are sufficient, not logically necessary, for BFS cost optimality. A common nondecreasing path-cost function of depth also makes a shallowest goal cheapest.

61. **A UCS contour with many cheap states.** UCS must process strictly cheaper reachable states before an optimal goal. Very expensive frontier entries can consume storage without requiring pre-goal expansion.

62. **Heap memory versus state labels.** One best-cost label per state does not imply one physical lazy-heap record per state. Count labels, active entries and stale queued entries separately when analysing storage.

63. **Edge-list order as a declared tie rule.** Tie policies determine particular traces, not every algorithmic guarantee. Preserve the invariant promised by the algorithm while allowing different equally valid routes and operation counts.

64. **Bidirectional search with many goals.** Recognizing goals is not the same as generating them. Bidirectional search needs a usable backward starting representation and must preserve the original multi-goal objective.

65. **Unequal directional branching.** Bidirectional balancing should consider frontier growth, not automatically equalize depths. Different branching factors can favor a much deeper search on the cheaper-growth side.

66. **A complete tree can favor DFS.** DFS can be much faster when a preferred deep branch leads directly to a goal. Instance-specific speed does not strengthen its general minimum-depth, minimum-cost or infinite-space completeness guarantees.

67. **Copying paths changes space costs.** Node-count space bounds assume a record representation. Copying complete paths into every frontier entry can add a depth factor; parent links share history but still require referenced ancestors to remain available.

68. **Unit-cost UCS and BFS.** Unit-cost UCS and BFS share minimum-depth priorities. Exact trace equality additionally requires matching tie breaking, successor order, goal timing and duplicate policies.

69. **A safe lower bound from a partial UCS run.** A valid frontier minimum can lower-bound unresolved solutions, while a discovered complete route upper-bounds the optimum. The bounds certify optimality only when they meet under the correct invariant.

70. **A bound can be tight.** A tight depth bound and a tight branching-node bound are different claims. Demonstrating one extremal path does not establish that all possible branches can also satisfy the same cost contour.

71. **Two depth limits with the same goal.** Exact IDS operation counts must include each restart's root and distinguish boundary selections from successor expansions. A single cumulative depth formula cannot replace those declared event conventions.

72. **Current-path cycle checking preserves a simple solution.** Path-cycle pruning preserves reachability when state equality implies identical legal futures. Its proof is cycle deletion, and it fails if relevant history has been omitted from the state.

73. **A grid with monotone moves.** Problem structure can make every feasible solution have the same length. In such an instance any successful search is optimal for unit costs, without changing DFS's lack of a universal optimality guarantee.

74. **Budget-limited depth and explicit truncation.** An external event cap is not a proof of failure. Report truncation separately from exhausted failure, depth cutoff and successful goal recognition.

75. **A nonnegative graph with no uniform problem-family bound.** Per-instance finite-graph completeness does not imply a common positive edge lower bound across a family. Keep instance assumptions and uniform complexity parameters separate.

76. **An optimal solution need not be unique.** Strict-improvement UCS finds one optimum, not all optimal paths. Enumerating multiplicity requires richer predecessor storage and a separate definition of paths versus cyclic walks.

77. **When a final-layer formula is exact.** In exhaustive DLS, boundary nodes are visited but not expanded. Root inclusion and event definitions determine which geometric sum answers the question.

78. **Visited terminology across sources.** Event names are conventions that must be mapped to actual operations. State insertion, removal and successor enumeration explicitly when reconciling visited or expanded counts across courses and examinations.

79. **A complete conditional proof of BFS optimality.** BFS's proof has two steps: FIFO order establishes minimum depth, and an objective relation converts depth into cost. Do not omit the second step or its nonnegative-cost condition.

80. **Final mixed diagnosis.** Audit a search claim by separating objective, frontier order, goal timing, duplicate dominance and representation costs. Repair each failed condition explicitly rather than renaming an incorrect implementation.
