# Final Summary and Examination Decisions

## A coherent summary

A game-search answer begins with the rules of the model. A state must retain relevant turn, history and information distinctions. A finite deterministic fully observed zero-sum tree is solved by backward induction: MAX takes the greatest child value and MIN the smallest, always in the same utility coordinates. The resulting value is an enforceable guarantee against an optimal adversary; it need not maximize average reward against a known weaker opponent.

Alpha-beta preserves the exact root value of the searched tree by avoiding computations whose result cannot change an ancestor's decision. It does not compute every subtree exactly. A fail-soft return below the original alpha is an upper certificate; one above the original beta is a lower certificate; an interior result is exact. Root action selection, transposition entries and animations must respect that distinction. Equality pruning can preserve a numerical root value while hiding genuine ties, and an equal returned bound can even belong to an inferior move.

The cost depends on tree shape, child order and the metric being counted. A full uniform tree has$b^D$leaves at$D$individual plies. Perfect ordering can reduce examined leaves to $b^{\lceil D/2\rceil}+b^{\lfloor D/2\rfloor}-1$, while worst-case alpha-beta retains exponential full-search work. Leaf evaluations, node visits, generated edges and memory are different quantities.

A depth horizon replaces unknown continuation values by heuristic estimates. The search can be exact for that surrogate and still choose poorly in the real game. A proved uniform frontier error$\varepsilon$passes through min, max and normalized expectation without amplification; a single greedy action then has regret at most$2\varepsilon$. Without such a premise, neither a good-looking evaluation function nor deeper search provides a universal guarantee.

Known randomness is backed up by a weighted expectation. MAX/MIN/CHANCE order must match who acts and what is observed. Finite bounds on unknown contributions can justify chance-node pruning. Strictly increasing transformations preserve deterministic extrema, but expected-utility comparisons generally require preservation of cardinal utility up to a positive affine change. Multiplayer and hidden-information games require their own payoff and strategy constraints.

Monte Carlo tree search allocates simulations using estimated reward and exploration. It requires a consistent reward perspective, explicit unvisited-child handling and correct update counts. A rollout sample is not an exact minimax proof. More samples can reduce noise about the simulated policy while leaving a mistaken opponent model unchanged.

## Complete examination rules

1. **Specify the objective before backing up a tree.** Distinguish worst-case payoff, expected utility, fixed-policy evaluation and a robust criterion over uncertain probabilities. The same terminal data can produce different legitimate decisions under these objectives.

2. **Use one utility perspective in ordinary minimax.** A MIN node minimizes MAX's number; it does not replace the utility function by MIN's coordinates. Convert signs only under an explicitly consistent negamax convention.

3. **Include the player to move in the state.** Identical arrangements with different turns can have different values and actions. Additional rule-history or information variables are also necessary when future behavior depends on them.

4. **Do not infer a finite tree from a finite state count.** Cycles can generate infinitely many histories. Identify a terminal rule, horizon or appropriate cyclic-game solution before claiming exhaustive search terminates.

5. **Check terminality before a heuristic cutoff.** A known terminal payoff takes priority over an estimate. Otherwise the algorithm can discard a proven win solely because the depth budget reached zero.

6. **Distinguish value from action.** A maximum is a number; an argmax identifies one or more choices attaining it. If the question asks for an action, report the corresponding edge as well as the backed-up score.

7. **Distinguish a path from a strategy.** A complete contingent strategy covers possible deviations. One principal variation gives only one sequence of outcomes under selected decisions.

8. **Prove both directions of a minimax value.** Show how MAX enforces at least the proposed value and how MIN restricts it to at most that value. A single attractive terminal leaf supplies neither general certificate.

9. **Keep guarantees conditional on the stated model.** Exact minimax protects against legal adversarial play in the solved tree. It does not certify a mistaken game model, an uncalibrated horizon or every unseen examination question.

10. **Treat a known random opponent as a policy when optimizing expectation.** Its distribution determines a weighted sum. Assuming a minimum discards supplied probabilities and changes the objective.

11. **State the depth unit.** Individual plies and complete two-player rounds differ by a factor of two. Normalize the unit before comparing complexity formulas or decrementing a depth counter.

12. **Count leaves separately from all nodes.** In a full uniform tree, leaves number$b^D$, while all nodes form a geometric sum. Include early terminals and irregular branching when the actual diagram has them.

13. **State the generation/storage model for a space bound.** Depth-first eager sibling storage may cost$O(bD)$; streaming successor generation can use$O(D)$auxiliary stack storage. Materializing the entire tree is a different implementation.

14. **Use alpha and beta as inherited decision thresholds.** They need not enclose the current subtree's exact value. A fail-low subtree can have its true value far below the incoming alpha.

15. **Declare fail-soft or fail-hard.** A fail-soft cutoff may return a score beyond the window; a fail-hard routine may clamp to a threshold. Their trace numbers can differ while both justify the same rejection.

16. **Classify a return against the original call window.** A score at or below original alpha is conservatively an upper bound, a score at or above original beta a lower bound, and an interior result exact. Mutated local thresholds do not define the caller's requested interval.

17. **A MIN cutoff supplies an upper restriction.** Once the branch is proven no better than MAX's existing alternative, its remainder cannot improve MAX's choice. The returned endpoint is not necessarily its exact minimum.

18. **A MAX cutoff supplies a lower guarantee.** A minimizing ancestor can avoid a branch already proven too large. Further MAX alternatives might increase its value without affecting that ancestor's choice.

19. **Look beyond the parent when explaining pruning.** A distant ancestor's alternative can justify a cutoff. Track the inherited thresholds through intervening levels rather than compare only adjacent nodes.

20. **Do not treat every partial working score as an exact-child extremum.** Recursive fail-soft child returns may themselves be bounds. Use their proved direction before asserting a lower or upper property of a working variable.

21. **State whether equality permits pruning.** Nonstrict cutoffs preserve root value but can change visited leaves and retained tied actions. Follow a problem's explicitly strict convention if one is given.

22. **Retain a known root incumbent on an equal bound return.** A candidate returning the same number can have a smaller exact value. Replacing on numerical equality requires stronger evidence of an actual tie.

23. **Re-search when every optimal root action is required.** A search sufficient to find one optimum may deliberately hide equal-valued alternatives. Enumerating all optima requires exact equality information for the relevant candidates.

24. **Separate ordering from selective deletion.** Reordering legal children does not change exhaustive minimax. Removing moves because they look weak can change the answer and requires a separate correctness argument.

25. **Try promising moves early.** Descending value order at MAX and ascending value order at MIN tend to tighten useful thresholds. A heuristic's ordering quality affects work without necessarily affecting exactness.

26. **Use the exact ideal leaf count only under its assumptions.** The expression $b^{\lceil D/2\rceil}+b^{\lfloor D/2\rfloor}-1$assumes a full uniform horizon and suitable ordering. It is not the count for every irregular diagram.

27. **Check odd-depth parity explicitly.** The even formula$2b^{D/2}-1$is an exact simplification only for even$D$. A noninteger expression is a warning that an asymptotic shortcut has replaced a requested count.

28. **Preserve unequal role branching.** With$n$MAX choices and$m$MIN choices for$k$complete rounds, exhaustive leaves are$(nm)^k$and the ideal count is$n^k+m^k-1$. An averaged branching factor does not give exact integers for this tree.

29. **Keep worst-case alpha-beta exponential.** Some orders provide no pruning improvement. Ideal half-exponent savings are not a uniform runtime guarantee for every input.

30. **Label a horizon result as a surrogate result.** Alpha-beta can exactly solve the frontier-evaluation tree while the full game's correct move differs. Exact arithmetic and exact game modelling are separate properties.

31. **Use a uniform error premise when propagating an error bound.** Min, max and normalized expectation are nonexpansive in the supremum norm. An empirical average prediction error is not a uniform worst-case frontier certificate.

32. **Use twice the action-value error for a decision-gap certificate.** A best-action gap greater than$2\varepsilon$cannot reverse when every action estimate has error at most$\varepsilon$. Equality can leave a tie or the full worst-case regret.

33. **Do not claim deeper search always helps.** Different horizons can encounter different heuristic errors. A universal improvement statement needs additional assumptions, not just a larger search depth.

34. **Give quiescence search a termination condition.** A tactical-extension predicate alone can remain true along a cycle. A cap, a valid repetition rule or a proved decreasing measure is needed for finite execution.

35. **Keep an anytime fallback.** Iterative deepening preserves the last completed action, but a legal fallback is also needed before its first iteration completes. An interrupted deeper result is not automatically an exact replacement.

36. **Do not overgeneralize geometric-sum overhead.** A fixed-branching unpruned leaf model gives a simple repeated-depth ratio. Different generation costs, orders and alpha-beta cutoffs change actual work.

37. **Store transposition evidence with its meaning.** A usable entry needs a complete state key, compatible horizon/evaluation semantics and an exact/lower/upper flag. A board hash plus an unlabelled number is insufficient.

38. **Tighten the correct threshold from a table bound.** Lower bounds raise alpha; upper bounds lower beta. A bound-induced window closure permits a cutoff, not an invented exact value.

39. **Do not equate different horizon functions.** A deeper stored value may be useful in an engine's declared policy, but it need not equal a precisely requested shallower recurrence. Reuse must match the intended semantics.

40. **Validate chance probabilities.** They must be nonnegative and sum to one for a normalized expectation. Equal averaging is justified only by equal probabilities.

41. **Resolve mixtures carefully.** “Preferred action with probability0.8, otherwise uniform among all actions” adds the preferred action's share of the uniform component. Excluding that action from the random component defines a different distribution.

42. **Model actual event order and observation.** Maximum of an expectation and expectation of a maximum describe different policy freedoms. Give an agent conditional actions only when the conditioning information is available.

43. **Use finite remainder bounds for chance pruning.** If processed mass$q$contributes$S$and the rest lies in$[L,U]$, the expectation lies in$[S+(1-q)L,S+(1-q)U]$. A small probability alone does not bound an arbitrary outcome's contribution.

44. **Propagate uncertain children as intervals.** Sum weighted lower and upper endpoints separately. Replacing a child bound by an exact score can create an invalid expected-value cutoff.

45. **Merge duplicate chance successors by adding mass.** Repeated histories reaching an identical future state still represent separate probability contributions. Deleting a duplicate edge without its probability changes the model.

46. **Keep comparison precision separate from display precision.** Rounded values can create a false equality cutoff. Prefer exact rational input arithmetic or conservative interval rounding where a bound is being certified.

47. **Distinguish ordinal and cardinal utility.** Strictly increasing transformations preserve deterministic min/max choices, but arbitrary nonlinear changes can reverse expected-utility choices. A positive affine change preserves both under normalized chance probabilities.

48. **Transform outcomes before taking expectations.** In general$E[g(X)]\ne g(E[X])$. Cubing an already computed mean does not solve a problem that cubes terminal utility.

49. **Keep terminal and heuristic scales coherent.** A feature score much larger than a maximum terminal utility can make uncertainty look preferable to a proven win. State how scores approximate the objective and how proof-status ties are treated.

50. **Handle extra turns from state control.** Consecutive MAX or MIN levels are legal when the rules grant them. A sign flip based only on depth can break negamax in that situation.

51. **Propagate one selected payoff vector in max-n.** The controlling player maximizes its own coordinate and returns the whole chosen vector. Coordinatewise maxima from different actions can create an impossible outcome.

52. **Do not replace independent players by a coalition without justification.** Multiple MIN levels share one scalar objective. Distinct utility vectors require an appropriate general-game model and a stated treatment of ties.

53. **Preserve hidden-information constraints.** Indistinguishable histories require consistent action choices. Averaging separately optimized perfect-information worlds can overstate achievable value through strategy fusion.

54. **Do not reveal simultaneous choices by tree order.** A fully observed sequential representation can change a game's value. Mixed-strategy analysis is necessary when a simultaneous zero-sum game has no optimal pure action.

55. **Distinguish a rollout mean from a minimax certificate.** It estimates the continuation under simulated policies. Repeating a biased opponent model more often does not prove adversarial optimality.

56. **Specify UCT reward perspective and scale.** Player-relative edge rewards can be maximized by the selecting player; fixed-MAX statistics need a corresponding MIN rule. Changing reward scale without adjusting the exploration coefficient can change the search.

57. **Handle an unvisited child explicitly.** The usual UCB expression divides by its visit count and is undefined at zero. A specified initial-exploration rule avoids an accidental omission or a numerical error.

58. **Update each visited statistic once under the declared convention.** Reward for a MAX win may be1for MAX and0for MIN in a0–1encoding. Draws, extra turns and node-versus-edge counting must be consistent.

59. **Separate exploration from the final root rule.** Greatest UCB allocates another simulation; greatest visit count is one common final action rule. Neither a finite UCB bonus nor a large sample mean proves perfect play.

60. **Finish with an independent check and an honest scope.** Verify a small tree by full backup, a parameter answer at boundary values, a probability calculation by normalization, and a cutoff by its one-sided inequality. Cite actual source/example provenance and report any unaudited examination or visual scope rather than claim universal completeness.
