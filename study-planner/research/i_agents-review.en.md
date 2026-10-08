1. **Percept histories are not physical states.** With $p$ percepts, $a$ actions and decisions after lengths $1$ through $H$, unrestricted tables number $a^{\sum_{t=1}^H p^t}$; memoryless policies number $a^p$. For $p=3,a=2,H=2$, the counts are $4096$ and $8$. Specify whether unreachable histories are counted.

2. **The empty-history convention.** An empty-history decision adds exactly one table entry. With two percepts, three actions and nonempty lengths through two, the count changes from $3^6$ to $3^7$ when an initial action is included.

3. **One percept does not eliminate time dependence.** For one percept and $H$ decisions, arbitrary history-based tables number $a^H$, whereas stationary memoryless rules number $a$. A constant percept does not erase history length; with $a=4,H=5$, the counts are $1024$ and $4$.

4. **Reachable histories versus all tables.** Unreachable table entries do not distinguish behaviour in a fixed environment. If only X and XX occur, three actions give $9$ reachable behaviours even though a two-percept full table through depth two has $729$ assignments.

5. **Contingent policy count.** From a fixed start with $a$ first choices, $p$ possible subsequent observations and $b$ second choices, executable depth-two policies number $ab^p$, while fixed sequences number $ab$. For $(a,p,b)=(2,3,4)$, these are $128$ and $8$.

6. **Counting a specified finite controller.** Count a controller from its declared function signatures. For a two-state, three-percept Moore controller with two output actions, update choices, output choices and initial-state choices give $2^6\cdot2^2\cdot2=512$ labelled implementations.

7. **Vacuum configurations and belief subsets.** Separate physical states from belief subsets and observation-compatible states. A two-room vacuum has $8$ physical states and $255$ nonempty syntactic belief subsets; observing (L, clean) leaves exactly $2$ physical possibilities.

8. **Exactly k dirty rooms.** For $n$ labelled rooms and exactly $k$ dirty rooms, unrestricted robot configurations number $n\binom nk$; requiring a clean robot location gives $(n-k)\binom nk=n\binom{n-1}k$. For $n=6,k=2$, the counts are $90$ and $60$.

9. **Constraints can couple choices.** Count legal combinations before judging predictive sufficiency. Ten stopped floors with either door state plus a single closed-door moving state give $21$ coarse states; direction and segment may still be required for a Markov movement model.

10. **Labelled robots and collision exclusions.** Two labelled robots in distinct rooms contribute $n(n-1)$ position choices. Replacing this by $\binom n2$ requires complete symmetry under label exchange. With four independent dirt bits and four rooms, the labelled count is $192$, and the symmetric quotient is $96$.

11. **Expected utility despite an unlucky outcome.** Expected-utility optimality does not imply success in every run. A lottery paying $10$ with probability $3/5$ and $-2$ otherwise has expectation $26/5>4$, although a loss occurs with probability $2/5$.

12. **A threshold different from one half.** For utilities A=$(12,-4)$ and B=$(5,5)$, the exact decision threshold is $p=9/16$. A is best above it, B below it, and both tie at equality; “H is more likely” is not a sufficient condition for choosing A.

13. **A negative coefficient reverses the inequality.** When comparing A=$(1,9)$ with B=$(4,4)$, $EU(A)-EU(B)=5-8p$. Therefore A is optimal for $p\le5/8$, with equality a tie; division by a negative coefficient reverses the decision inequality.

14. **Weak dominance and zero-probability states.** Weak statewise dominance becomes strict in expectation only when strict improvement occurs on positive-probability states. A=$(7,3)$ and B=$(7,1)$ tie at $P(H)=1$ and differ by $2(1-p)$ otherwise.

15. **Positive affine utility transformation.** The transformation $U'=\alpha U+\beta$ preserves expected-utility rankings for $\alpha>0$ because differences scale by $\alpha$. For $3U-7$, ties and strict preferences are unchanged; nonlinear transformations require a fresh lottery comparison.

16. **Increasing outcome transformations can reverse lotteries.** Increasing utility transformations preserve certain-outcome order but can change lottery order. The lottery $(0,100)$ with equal probabilities beats a certain $40$ in expected money, but loses under square-root utility because $5<\sqrt{40}$.

17. **Expected utility versus maximin.** Expected utility and maximin solve different optimization problems. For A=$(8,-2)$, B=$(3,3)$ and $P(H)=4/5$, expectation chooses A with $6>3$, while maximin chooses B with $3>-2$.

18. **Minimax regret is not maximin.** Compute regret relative to the best action separately in each state. For A=$(10,0)$, B=$(6,5)$, C=$(0,8)$, maximum regrets are $8,4,10$, and minimax regret chooses B.

19. **An objective proxy rewards the wrong action.** Test a proposed score against all allowed actions. A reward of $3$ per costless announcement makes three announcements worth $9$ even without cleaning; a separate score of one per unit cleaned with cost two instead favours stopping. Neither name guarantees the intended task.

20. **A finite penalty is not a hard constraint.** For safe utility $20$ and unsafe utility $30-M$, strict safe preference requires $M>10$. Without a bound on unsafe benefit, no fixed finite penalty is equivalent to forbidding the action.

21. **Known is independent of deterministic.** Knowledge and determinism are separate properties. A known fair-die distribution is stochastic; a reliable door with a fixed but unknown code is deterministic at the physical-state level and unknown to the agent.

22. **Hidden determinism can produce predictive uncertainty.** Uncertainty over a fixed hidden state does not imply stochastic conditional dynamics. A bit sampled once with probability $3/4$ yields uncertain first revelation but identical repeated revelations; independent resampling is a different model.

23. **A static puzzle changes after action.** A static environment may change as a result of the agent's action. A board fixed during thought is static; adding a clock penalty with the same board makes performance semidynamic.

24. **Independent inputs with coupled decisions.** Independent observations do not establish an episodic task. A two-annotation budget shared across ten independent images couples decisions through the remaining budget, making annotation choice sequential.

25. **Discrete does not mean finite.** Discreteness and finiteness differ. An unbounded nonnegative integer counter is discrete and infinite; a capped counter from 0 through 20 has 21 counter states, before any separately declared termination flag.

26. **Single controller, several bodies.** A central controller for three four-action robots has 64 unconstrained joint actions, but an independently choosing opposing controller still makes the task multi-agent. Count decision makers separately from physical bodies.

27. **Partial observability without a memory advantage.** Partial observability need not create a decision disadvantage. If A pays 5 and B pays 1 in both aliased states, A is uniquely optimal for every belief and no memory is needed for this choice.

28. **Aliased histories with incompatible optima.** Identical percepts with different unique optimal actions rule out universal current-percept-only optimality. For utility pairs $(10,0)$ and $(0,10)$, randomization would require both $q=1$ and $q=0$; memory or additional information is needed.

29. **Overlapping optimal-action sets.** A deterministic memoryless optimum exists for a percept class exactly when all its relevant maximizing sets share an action. The sets $\{A,B\},\{B,C\},\{B,D\}$ share B; replacing the third by $\{A,D\}$ destroys the common intersection.

30. **Goal achievement versus maintenance.** Achievement and maintenance are different predicates on runs. Safe→Collision→Destination reaches its destination but violates never-collide; a final-location-only test cannot detect the violation without a retained history flag.

31. **A compiled reflex policy can implement planning.** Online lookahead is not necessary when a correct optimal policy has been compiled for the observed sufficient state. A finite-horizon table may need a time key; changing the model or omitting relevant state invalidates the argument.

32. **Model-based does not mean online planning.** A controller may be both model-based and reflex: it updates a persistent room-cleanliness model, then applies fixed action rules without online search. Unreliable cleaning requires verification or an uncertain state estimate.

33. **Learning without physical stochasticity.** Unknown deterministic dynamics can motivate model learning; known stochastic dynamics need not. A fixed unmapped maze and a fully specified probabilistic maze separate knowledge from randomness.

34. **Exploration can cost more than it is worth.** Information acquisition is justified by net task value. If its total remaining benefit is at most 2 and its cost is 5, net gain is at most −3, so exploration is not rational under that criterion.

35. **Computation has an opportunity cost.** More computation improves net performance only when its expected decision gain exceeds its total cost. Raising action utility from 8 to 10 at delay cost 3 gives net 7, below the fast program's 8.

36. **Current position omits a key.** If legality or transitions depend on a previously collected key, position alone is insufficient. The histories ending at X with and without a key must be distinguished, for example by state $(X,k)$.

37. **Time can matter in stationary physics.** Stationary physical dynamics do not imply a time-independent finite-horizon optimum. A project paying −1 then 5 loses to a certain 2 with one decision left, but wins with two; retain time or horizon in the policy.

38. **Distinct beliefs with identical support.** Belief support is not generally sufficient for expected utility. With A=$(12,-4)$ and B=$(5,5)$, priors $1/4$ and $3/4$ share support $\{H,L\}$ but choose B and A respectively.

39. **Bayesian conditioning must include the prior.** Normalize joint masses, not likelihoods alone. A prior $3/10$ with positive likelihoods $4/5$ in H and $1/5$ in L gives $P(+)=19/50$ and $P(H\mid+)=12/19$, not $4/5$.

40. **The negative observation matters too.** Weight posterior beliefs by their signal probabilities. For prior $3/10$ and likelihoods $4/5,1/5$, the negative branch has probability $31/50$ and posterior $3/31$; weighted averaging with the positive branch returns $3/10$.

41. **An impossible observation has no Bayesian posterior.** Bayesian normalization requires a positive observation probability. If both negative likelihoods are zero, a negative observation is model-inconsistent and its posterior is undefined, not automatically uniform.

42. **Prediction before observation.** Propagate belief through the executed action before conditioning on the next observation. Prior $1/4$, H-retention $4/5$ and L-to-H probability $2/5$ produce predicted H probability $1/2$; likelihoods $3/4,1/4$ then give posterior $3/4$.

43. **Optimize after each signal, then average.** Information value uses the expectation of conditional maxima. With prior $3/10$, likelihoods $4/5,1/5$ and A=$(12,-4)$ versus B=$(5,5)$, optimized free-signal value is $271/50$, a gain of $21/50$ over 5.

44. **Information cost and the exact tie.** A sensor with sample-information value $21/50$ is worth buying only for cost below $21/50$, with indifference at equality. Cost $1/4$ leaves gain $17/100$; cost $1/2$ leaves loss $2/25$.

45. **Perfect information bounds the signal value.** Perfect information for A=$(12,-4)$, B=$(5,5)$ and prior $3/10$ has value $21/10$ above the baseline 5. It bounds costless noisy-signal value only when actions, utilities and timing are held fixed.

46. **Useful sensing can have zero decision value.** Reducing uncertainty can have zero decision value. With A=$(10,9)$ and B=$(0,8)$, perfect state revelation does not change the optimal action and leaves expected value $19/2$ unchanged at prior one half.

47. **Prove nonnegative free-information value.** Costless, noninterfering information that may be ignored has nonnegative optimized expected value: compare every conditional maximum with the fixed prior-optimal action, then apply total expectation. Costs or forced disclosure are additional assumptions.

48. **Randomization cannot beat a one-step maximum.** With fixed single-agent expected utilities 7 and 3, a mixture yields $3+4q\le7$ and cannot improve on the best pure action. Strategic responses that depend on the mixture violate the fixed-payoff premise.

49. **Sensorless vacuum plan by exact belief propagation.** With reliable deterministic movement/cleaning and no new dirt, the sensorless sequence Right, Clean, Left, Clean maps the eight two-room states through belief sizes $8,4,2,2,1$ to $(L,0,0)$.

50. **Shortest plan from a known dirty configuration.** In the reliable local-cleaning vacuum, starting at L with both rooms dirty requires two cleans and at least one move, so Clean, Right, Clean is optimal at cost three. Requiring return to L adds another move.

51. **A locally clean room does not justify stopping.** Branch-specific costs matter. With move cost one, conditional clean cost one and dirt-removal benefit six, visiting an unseen room has value $5p-1$, so the exact threshold is $p=1/5$.

52. **Stopping requires a model assumption.** Verified cleanliness permits permanent stopping only under a model that preserves it without action. Spontaneous dirt recurrence breaks that invariant and requires a revised sensing/maintenance policy.

53. **Belief-set update can merge states.** A deterministic action's set image can merge possibilities. Right maps both clean-room location states to $(R,0,0)$, reducing support size from two to one; injectivity must not be assumed.

54. **Observation filtering versus state prediction.** For an action followed by an observation, predict successors and then filter. Right applied to $\{(L,1,0),(L,0,1),(R,1,1)\}$ followed by right-clean leaves only $(R,1,0)$.

55. **An exact abstraction must preserve legality.** Unioning legal actions of merged states can create unrealizable abstract plans. At a door, merging key/no-key states and allowing Open loses exactness unless preconditions or refinement restore the distinction.

56. **Transition agreement without cost agreement is insufficient.** Exact optimal-cost abstraction needs cost agreement as well as matching successors and goals. An edge costing 1 or 9 in merged states cannot receive one exact abstract cost; a lower bound is a different guarantee.

57. **Goal disagreement breaks abstraction.** Equivalent detailed states must agree on goal status for an exact goal abstraction. Location alone cannot distinguish completed from unfinished deliveries; retain the remaining-delivery mask unless it is provably determined by other state variables.

58. **Depth and cost can rank plans differently.** Depth orders plans by action count, not arbitrary cost. Two edges of 100 cost more than three edges of one. Equal strictly positive step cost makes total cost a positive multiple of depth.

59. **A finite graph can generate an infinite search tree.** A finite state graph need not give a finite search tree. With X→X and X→G, there are two states but infinitely many finite goal paths; a negative-cost self-loop also destroys existence of a cheapest solution.

60. **Zero-length solution versus failure.** The empty plan can be a valid solution when the start is already a goal. Use a separate failure sentinel or success flag; the same untagged empty list cannot represent both outcomes unambiguously.

61. **Finite-horizon policy count.** With n states and a actions everywhere, stationary deterministic policies number $a^n$ and full H-step time-indexed tables number $a^{nH}$. For n=4,a=3,H=2, these are 81 and 6561.

62. **Legal action counts vary by state.** For independent stationary policy entries with state-specific nonempty action sets, policy count is $\prod_s|A(s)|$. Counts 2,3,1 give six policies, not $3^3$; terminal-state conventions must be explicit.

63. **Discount changes a sequential choice.** For rewards A=$(6,-10)$ and B=$(1,8)$ over two steps, discounted return difference is $5-18\gamma$. A wins below $5/18$, B above it, with a tie at equality.

64. **Bounding an infinite discounted return.** Bounded discounted rewards obey $|G|\le R/(1-\gamma)$ and tail after H terms at most $R\gamma^H/(1-\gamma)$. For R=3 and gamma=4/5, these are 15 and $15(4/5)^{10}$ after ten terms.

65. **Random terminal time complicates reward shifts.** Adding a constant to every executed reward can change variable-length episode rankings. Returns 1 over one step and 0 over two steps become 3 and 4 after adding two per step; this is not a common affine transformation of run utility.

66. **Probability of success versus expected reward.** Expected success-indicator utility equals success probability, but unequal success payoffs change the objective. A with success probability 9/10 and payoff one loses in expected payoff to B with probability one half and payoff four.

67. **Information cannot repair impossible actuation.** In a one-step task with one legal action and a noninterfering sensor, information has zero action-selection value by total expectation. Perfect observation cannot compensate for a missing control choice.

68. **Observation accuracy is not task value.** Sensor accuracy alone does not determine action. With prior 1/100, symmetric accuracy 9/10 and A payoffs $(1,-100)$ versus zero, a positive signal yields posterior 1/12, far below the required 100/101.

69. **Optimal action under an interval of priors.** For uncertain prior p in $[1/4,3/4]$, A=$(12,-4)$ has worst expected value zero while B=$(5,5)$ has five, so a fixed maximin-over-priors decision chooses B. A known p=3/4 would choose A instead.

70. **Sensitivity of expected utility to probability error.** For A=$(12,-4)$ versus B=$(5,5)$, prior error epsilon changes the utility difference by at most $16\varepsilon$. A preference is sign-certified when its estimated margin exceeds that bound; p-hat=3/5 and epsilon=1/100 certify A.

71. **A maintenance property needs trajectory information.** A Boolean “ever collided” flag doubles ten position states to twenty syntactic combinations and makes past safety visible to a state predicate. Reachability and collision-termination rules can reduce the actual reachable set.

72. **Joint actions with a shared resource.** Shared resources couple joint actions. Three Idle/Charge robots with at most one charger user have four legal joint commands, not eight; count by permitted charging subsets.

73. **Current observation versus remembered parameter.** Environment labels depend on the declared representation. Exact position with an unknown reversal parameter is fully observed position but unknown dynamics; including the hidden parameter in physical state also makes that state partially observed.

74. **Changing the objective changes sufficient state.** Collect-all objectives generally require a remaining-item mask, not merely position or item count. Equal counts at different locations can require different next routes; a smaller summary needs a proved symmetry.

75. **A constrained elevator with a sufficient moving state.** Six stopped floors with two door states and five directed moving segments give $12+10=22$ configurations when moving doors are forced closed. Passenger requests or continuous position are additional state variables if the task requires them.

76. **A simple rule can encode a winning plan.** In the one-or-two normal-play takeaway game, multiples of three are losing positions. From 14, remove two to leave 12, then make each pair of turns remove three. Changing the terminal winning rule requires a new proof.

77. **A board arrangement need not be a full chess state.** Same chess arrangement and side to move can have different castling rights after different histories. Include rule-relevant history summaries; an incomplete board-only representation must not be confused with intrinsic hidden information.

78. **A transition distribution must be normalized.** Declared nonnegative successor weights 2,3,5 normalize to $1/5,3/10,1/2$ and yield utility $-1/5$ for successor utilities 4,0,−2. Entries already labelled probabilities must satisfy the probability axioms rather than being silently reinterpreted.

79. **Bounded implementability changes the optimization domain.** Bounded optimality maximizes over implementable behaviours on the specified architecture. Utilities 9,8,6 with only 8 and 6 feasible give bounded optimum 8; adding the 9 behaviour cannot lower the same objective's optimum.

80. **Synthesis: choose representation, sensor and action.** For prior 3/10, likelihoods 4/5 and 1/5, A=$(12,-4)$, B=$(5,5)$ and sensing cost 1/4, buy the signal, choose A after positive and B after negative. Net expected utility is $517/100$, a gain of $17/100$, assuming the hidden state and action opportunities do not change during sensing.
