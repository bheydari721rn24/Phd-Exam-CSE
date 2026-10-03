### The complete conceptual summary

Conditional probability is the normalized mass of the target inside the information event. It defines a new probability measure whenever that information has positive probability. All probability laws then hold with the same conditioning event consistently attached. Reversing a conditional changes its denominator; complementing a target differs from complementing the information.

The multiplication rule factors an intersection along complete prefix histories. It needs no independence, but every denominator written must be positive. A zero-mass branch has zero joint mass throughout its subtree and can be stopped. Probability trees multiply along a path and add the masses of disjoint paths. Sampling without replacement changes the counts remaining; exchangeability of positions does not imply independence.

Total probability decomposes a target into disjoint exhaustive cases. After an observation, both the case rates and the case weights must be conditioned appropriately. A hidden mixture can create dependence even when events are independent in every known stratum. Conversely selection can destroy independence between originally independent coordinates. A reported observation must include the reporting procedure, because different truthful procedures can produce different conditional weights.

Independence is product factorization, including null events. Mutual independence requires every subfamily factorization, while pairwise independence checks only pairs. Complement closure holds for target events inside a fixed probability measure. Shared components invalidate an automatic independent-path argument in reliability; conditioning on a bridge can expose independent coordinate blocks. Conditioning at a continuous exact observation needs a density-based or other specified conditional version, not division by a zero event probability.

### Numerators, denominators, and validity

1. Name the target and the information before choosing a formula. In $P(A\mid B)$, B supplies the denominator, and the numerator is the intersection rather than the unconditioned A mass.

2. Check $P(B)>0$ before taking an elementary conditional ratio. If it is zero, report the ratio as undefined; neither a zero numerator nor an intuitive interpretation supplies a numerical value.

3. Counting retained outcomes is valid only when those outcomes have equal original weights. If weights differ, sum their masses; conditioning preserves their relative likelihoods rather than flattening them.

4. A conditional probability lies between zero and one because its numerator is at most its denominator. A result outside that range reveals either inconsistent premises or a calculation with the wrong event.

5. The identity $P(A^c\mid B)=1-P(A\mid B)$ complements the target only. It provides no value for $P(A\mid B^c)$ unless additional joint information is available.

6. A conditional value one means $P(B\setminus A)=0$. It implies literal containment only under additional support assumptions; a null outcome can violate set containment without affecting any probability.

7. A conditional value zero means $P(A\cap B)=0$. It need not mean the intersection is empty as a set, particularly under continuous models or finite models with zero-weight atoms.

8. Two reversed conditionals share an intersection but use different denominators. For positive marginals they agree precisely when the intersection has mass zero or the marginals are equal.

9. Do not divide two reversed conditionals if their common intersection could be zero. Multiplying by their positive marginal denominators preserves the disjoint case and is the safer algebraic route.

10. Conditioning on B and then C retains $B\cap C$. The ratio $P(A\cap B\mid C)/P(B\mid C)$ is defined only when that intersection has positive mass.

11. Extra information can be removed if it is already implied almost surely by the current information. Otherwise equality of the relevant conditional rates must be established, not assumed from a shorter notation.

12. Conditional union and inclusion-exclusion laws require every term to use the same conditioning event. Mixing a conditional marginal with an unconditional intersection generally counts masses in incompatible universes.

### Joint reconstruction and feasibility

13. For marginals a and b and joint x, reconstruct the cells as $x,a-x,b-x,1-a-b+x$. Nonnegative cells are an immediate feasibility test and expose contradictory premises before further inference.

14. The sharp joint bounds are $\max(0,a+b-1)\le x\le\min(a,b)$. Their sharpness is justified by four-cell constructions, not merely by quoting inequalities.

15. To bound $P(A\mid B)$ with fixed positive b, divide both sharp joint bounds by b. Do not divide by a: that would bound the reversed conditional instead.

16. Data $b,u,v$ for the information weight and the two stratum rates give cells $bu,(1-b)v,b(1-u),(1-b)(1-v)$. Always align the cell order with the row and column labels.

17. The marginal $P(A)=bu+(1-b)v$ is a weighted average. It must lie between the two stratum rates; a value outside that interval makes the supplied data infeasible.

18. If $u\ne v$, the information weight is $(P(A)-v)/(u-v)$. Check the resulting weight range and the existence of the conditionals; algebra alone does not certify a valid model.

19. If u and v are equal, the marginal must equal that common rate. Compatible data then leave b unidentified; dividing by $u-v$ would turn non-identifiability into an invalid operation.

20. Positive association means $x-ab>0$, and negative association means $x-ab<0$. The two conditional changes have the same sign but can have different magnitudes because they divide by different marginals.

21. The determinant of the two-event table equals $x-ab$. This gives an exact independence test; use full cell weights rather than rounded percentages when a rational computation is available.

22. Empirical approximate factorization is not an exact theorem about a population model. If a problem provides exact probabilities, use exact arithmetic; if it gives samples, separate sampling uncertainty from the independence assertion.

### Chains, trees, and sequential experiments

23. The multiplication rule applies to dependent events as well as independent ones. Independence changes conditional factors into marginals; it is not a prerequisite for the chain itself.

24. At stage k, condition on the intersection of all earlier events in the selected path. Retaining only the preceding event assumes a memory-reduction property that the ordinary chain rule does not supply.

25. A positive final intersection guarantees positive prefixes but is not necessary. The final factor can be zero while every denominator used remains positive, yielding a valid zero joint probability.

26. If a prefix has zero mass, all descendant joint events have zero mass by containment. Stop the branch and do not write an undefined later conditional multiplied by zero.

27. Reordering a chain changes its factors but not its intersection. A discrepancy between two valid orderings signals a wrong denominator, an omitted historical event, or mutually inconsistent data.

28. Tree edge labels are local conditional probabilities; node masses are unconditional prefix probabilities. A stage-three edge value cannot be used as the overall chance of reaching and passing that stage.

29. Outgoing edges at a positive-mass node sum to one when they exhaust its alternatives. Their weighted child masses must sum back to the parent mass, providing a useful model consistency check.

30. Add leaf probabilities only when those leaf events are disjoint. Several paths through a network can occur together and are not automatically the mutually exclusive paths of a probability tree.

31. In drawing without replacement, each denominator decreases after a draw and each numerator decreases only when its color is drawn. Track remaining counts rather than reusing the original fractions.

32. A specified color pattern has a falling-product numerator and denominator. Ordinary powers describe repeated independent draws with replacement and answer a different experiment.

33. Uniform sampling without replacement is exchangeable: patterns with the same color counts have equal mass. Dependence remains because observing a removed color changes the remaining composition.

34. Exactly k successes among m draws is a union over position patterns. Multiply the common pattern mass by $\binom mk$ only after verifying that the patterns are disjoint and have equal probabilities.

35. Ordered and unordered counting give the same probability only when both numerator and denominator use the same representation. An ordered numerator divided by an unordered sample count introduces an extra factorial.

36. A coarse history can be compressed when every retained fine history gives the same future rate. Equal remaining urn compositions justify that reduction; a phrase such as “at least one” often retains unequal compositions.

37. Given a fixed total success count in identical independent trials, position patterns with that count are uniform. The common factor $p^k(1-p)^{n-k}$ cancels, provided the condition has positive probability.

38. The parameter cancellation after fixing a count does not preserve trial independence. For distinct positions, the conditional joint is $k(k-1)/(n(n-1))$, rather than the square of the conditional marginal.

39. In a multistage eligibility experiment, combine entry and later success into one per-object event using the multiplication rule. Independence across complete object histories licenses the count-pattern product.

40. Substituting the expected eligible count for a random eligible count generally changes the experiment. Condition and sum over actual counts, or use independent composite indicators when their assumptions hold.

### Partitions, hidden mixtures, and observation

41. The simple total-probability sum needs disjoint exhaustive cases. Overlapping cases double-count the target overlap; nonexhaustive cases omit the target mass outside the chosen union.

42. Countably many cases are valid when they form a measurable partition. Countable additivity justifies the nonnegative sum, and zero-probability cells contribute zero joint mass without requiring undefined ratios.

43. Under an observation B, partition weights become $P(D_i\mid B)$. Keeping the original weights answers the original mixture unless an invariance condition or a special equality makes the result coincide.

44. A within-type target rate remains unchanged after B only under the relevant conditional-independence or equal-rate premise. Knowing original type rates and observation rates alone need not determine the joint target rate.

45. Empty collections satisfy “every trial succeeds” and “no trial fails.” If a random count can be zero, include that case before taking a ratio; removing it changes the problem's event.

46. A geometric mixture can often be summed symbolically before normalizing. Verify its starting index: omitting the zero term changes both the denominator and the interpretation of a conditioned positive-count question.

47. Aggregate rates are convex combinations with the appropriate case weights. Equal averaging is justified by equal weights or equal rates, not by the fact that exactly two types appear in the description.

48. Simpson's reversal can arise from different stratum weights. With the same weights, multiplying and adding all within-stratum inequalities preserves their ordering, so no reversal is possible.

49. A report is an observed message, with its own probability given each hidden state. Truthfulness restricts where a message can occur; it does not determine how frequently each eligible state produces it.

50. When a reporting protocol has equal positive likelihood throughout an event and zero likelihood outside it, conditioning on the report is equivalent to conditioning on that event. Unequal likelihoods require reweighting.

51. In the two-sided card experiment, elementary outcomes include the selected face as well as the card. A same-color card has two ways to produce that color; an opposite-color card has only one.

52. A specified host reveal can depend on tie-breaking. State whether the host knows the prize, always reveals an empty door, and how ties are resolved before inferring a conditional switching rate.

53. Aggregate switching under an informed always-reveal host depends on whether the original choice was wrong. Its success rate can remain unchanged even when the conditional answer after a named reveal changes.

54. A random uninformed reveal, conditioned on being empty, selects cases differently from an informed always-empty reveal. The same visible outcome does not identify the same probability experiment.

### Independence and its boundaries

55. Product factorization is the general event definition of independence. The unchanged-conditional characterization is equivalent only when the conditioning event has positive mass; keep those domains explicit.

56. Independence is symmetric, but conditional probabilities are usually asymmetric. A symmetric product statement and an asymmetric ratio answer different questions and should not be conflated.

57. Independent events remain independent after complementing either target. The proof uses subtraction of joint masses and remains valid when a marginal is zero or one.

58. Disjoint positive-probability events are dependent. Disjoint events are independent exactly when one has zero mass, so an unqualified claim that exclusivity and independence are incompatible misses boundary cases.

59. A nested pair is independent exactly when the smaller event is null or the larger event is certain. This follows from $a=ab$, not from a vague assertion that nesting always prevents independence.

60. An event independent of itself has probability zero or one. The result concerns almost-sure constancy of its indicator and does not require the event to be literally empty or the entire sample space.

61. Pairwise independence checks only pairs. The XOR construction verifies each pair exactly while failing the triple product, so it is a concrete refutation of multiplying three marginals from pairwise premises alone.

62. A full-family product equality alone does not prove mutual independence. Verify every smaller subfamily, or derive those equalities from a model that already supplies mutual coordinate independence.

63. For n events, the nontrivial subfamily conditions number $2^n-n-1$. Counting them describes the definition's requirements, not the number of algebraically independent constraints in every special model.

64. Events determined by disjoint blocks of mutually independent coordinates are independent. If coordinate blocks overlap, this proof fails; the events may still be independent, but that needs calculation.

65. The complement formula for at least one event uses mutual independence of all failures. Pairwise independence is insufficient to factor a three-or-more-event all-failure probability.

66. Exactly one heterogeneous success has probability $\sum_i p_i\prod_{j\ne i}(1-p_j)$. The homogeneous form with a common p is unavailable when the given rates differ.

67. Factoring an exact-one formula by an all-failure product can divide by $1-p_i$. Preserve the unfactored expression if a component can succeed with probability one.

### Conditional independence and reliability

68. Conditional independence uses the product definition inside one fixed positive-probability event. Its ratio equivalent needs the conditioning intersection to have positive mass; otherwise that additional ratio is undefined.

69. Complement closure inside C refers to complementing A or B while C stays fixed. It does not establish independence inside $C^c$, which defines a different probability measure.

70. Unchanged individual marginals after selection do not guarantee unchanged independence. Conditioning fair bits on equality leaves both marginals fair but doubles their joint mass relative to the product.

71. Marginal independence need not survive selection, and conditional independence in every known type need not survive mixing. The two directions fail for different concrete mechanisms and must be checked separately.

72. For two conditionally independent strata, the marginal joint-minus-product is $w(1-w)(u_1-u_2)(v_1-v_2)$. The sign follows the relative directions of the two rate changes.

73. With two nondegenerate strata, marginal independence occurs if one rate list is constant. With more strata, weighted covariance can cancel without a constant list, so do not generalize that criterion blindly.

74. Independent components justify series and parallel formulas applied to those components. They do not justify independent treatment of overlapping path events that share an uncertain edge.

75. For a shared edge followed by two alternatives, reliability is $2p^2-p^3$. Subtracting $p^4$ instead of $p^3$ confuses the path-product assumption with the actual common-component intersection.

76. Conditioning on a bridge partitions the network into simpler configurations. Weight each configuration's reliability by the bridge state probability, and justify independence within each configuration from primitive edge blocks.

77. Endpoint checks catch many reliability errors: the all-failed limit is zero and the all-working limit is one for the connected networks studied here. Also inspect whether a claimed probability exceeds one.

### Continuous boundaries and a final solution method

78. In a uniform planar model, probability ratios use areas rather than projection lengths. After conditioning on a triangle, a coordinate's marginal is weighted by changing cross-section lengths even though area density is uniform.

79. A conditional density at a continuous observation uses a positive marginal density, not a positive point-event probability. State the density version and its support; exact null-point values require additional conventions.

80. Before accepting a final answer, check the information event, positive denominators, joint feasibility, needed independence, and the observation mechanism. Then verify the result with a second representation, a boundary case, or an exact finite enumeration when available.
