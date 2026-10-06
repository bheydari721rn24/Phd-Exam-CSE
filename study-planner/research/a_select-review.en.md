# Examination rules: complete conditions, formulas and traps

1. **Define the answer before selecting a method.** Membership, insertion position, one rank, sorted top-k and full sorting are different outputs. A complexity statement for one cannot silently answer another.

2. **One-based rank converts to zero-based index by subtracting one.** Rank $k$ refers to sorted-array position $k-1$. Check the source's convention before copying its recurrence or branch condition.

3. **Repeated keys occupy an interval of ranks.** Value $v$ is correct precisely when $|L|<k\le|L|+|E|$, where $L$ contains strictly smaller occurrences and $E$ contains equal occurrences. Distinct-value ranks require another contract.

4. **Keys and identities are separate.** Two equal keys can belong to different records. Stable identity selection needs a tie policy such as original index, even when value selection is already correct.

5. **The lower median rank is $\lfloor(n+1)/2\rfloor$.** The upper median rank is $\lceil(n+1)/2\rceil$. For odd length they coincide; for even length they are adjacent ranks.

6. **A numerical even median may not be an input key.** Averaging two middle values requires arithmetic. A comparison-only order-statistic routine returns an input key and does not automatically compute that average.

7. **A partition-selected array need not be sorted.** Its cross-boundary inequalities certify the selected rank. Internal side order remains unconstrained, so binary search over either side requires additional sorting.

8. **A comparator must support consistent elimination.** Intransitive order, NaN without an explicit ordering policy, or keys that mutate during execution can invalidate the partition and binary-search proofs.

9. **Unsuccessful unsorted equality search costs $n$ key tests.** Every occurrence must be ruled out unless an external index or extra information narrows the possibilities.

10. **Successful uniform linear search averages $(n+1)/2$ tests.** This formula assumes one matching occurrence and a uniformly distributed successful position. Repeated matches or nonuniform positions change it.

11. **Include the probability of failure in expected search cost.** With success probability $p$ and a unique uniform conditional position, expectation is $p(n+1)/2+(1-p)n$.

12. **Order equality-search candidates by decreasing access probability when permitted.** The adjacent-exchange argument minimizes $\sum i p_i$. This optimization does not preserve an independent numeric sorting contract.

13. **Wrong-code feedback is not an ordered comparison.** Sorting candidate codes does not allow bisection unless the feedback reveals which ordered region contains the answer.

14. **Identification and successful action have different terminal costs.** After eliminating all but one candidate, its identity is known, but opening a lock may still require the final successful trial.

15. **A sentinel removes loop bounds checks, not linear key-inspection work.** Distinguish the sentinel occurrence from a real match and restore any overwritten input slot.

16. **The unsorted minimum needs $n-1$ comparisons.** Every nonminimum must acquire a comparison-loss certificate, and one comparison can newly eliminate at most one minimum candidate.

17. **Lower bound returns the first key at least the target.** It may return $n$, which is a valid insertion boundary but not a readable element index.

18. **Upper bound returns the first key strictly greater than the target.** Replace the lower-bound `< target` predicate by `<= target`; this changes the equality-side update deliberately.

19. **Separate the unknown elements from the possible boundary.** In the half-open loop the unknown elements lie in $[lo,hi)$ while the possible boundary lies in $[lo,hi]$.

20. **A false lower-bound comparison discards the midpoint itself.** If $A[mid]<x$, set $lo=mid+1$. Keeping $lo=mid$ can fail to progress on a one-element interval.

21. **A true lower-bound comparison retains the midpoint as a possible boundary.** Set $hi=mid$ because that index could be the first qualifying key. Using $mid-1$ under this contract can skip the answer.

22. **Prove termination with an integer measure.** Every update must strictly decrease $hi-lo$ until it reaches zero. Correctly naming a side is insufficient if the bounds remain unchanged.

23. **The exact worst-case lower-bound predicate count is $\lceil\log_2(n+1)\rceil$.** For $n\ge1$ it also equals $\lfloor\log_2 n\rfloor+1$. A final membership equality check is additional.

24. **Do not confuse worst-case and a supplied trace.** A midpoint equality can end ordinary membership search in one probe. A first-occurrence search usually must continue to establish its boundary.

25. **Guard the final membership access.** Test `index < length` before comparing the returned key. Empty arrays and targets above the maximum expose this error immediately.

26. **Frequency is upper bound minus lower bound.** The subtraction counts occurrences, including every repeated target, because the corresponding equal range is half-open.

27. **Strict predecessor is at lower-bound index minus one.** Strict successor is at upper-bound index. Check for missing endpoints before reading these positions.

28. **A closed numeric range uses an upper bound at its upper endpoint.** For $u\le v$, its occurrence count is $\operatorname{ub}(v)-\operatorname{lb}(u)$. Two lower bounds instead count $[u,v)$.

29. **Sortedness is a global precondition.** Checking only visited midpoints cannot certify hidden skipped regions. Revalidating the entire array for each query adds $\Theta(n)$ work.

30. **Use overflow-aware midpoint arithmetic for valid nonnegative fixed-width bounds.** `lo+(hi-lo)//2` avoids the sum overflow in `(lo+hi)//2`; arbitrary signed endpoints still need a range analysis.

31. **Binary search by answer requires monotonicity of feasibility.** Prove that increasing the candidate cannot change true back to false. An attractive numerical parameter alone is not that proof.

32. **Include predicate evaluation cost.** If one feasibility test scans $n$ records, a logarithmic number of tests gives $O(n\log R)$ work over a range of $R$ candidates.

33. **Threshold search can validly return “none.”** In a false-then-true candidate interval $[0,N)$, returned boundary $N$ means no true candidate. It should not be confused with a feasible value inside the domain.

34. **Unknown-bound search needs both doubling and bisection.** With a finite first true index $t$, their combined test cost is $O(\log(t+1))$. If truth never occurs, unrestricted doubling may not terminate.

35. **Real bisection certifies interval width.** After $s$ halves the width is $(b-a)/2^s$. A bound on the function residual requires extra assumptions, and floating-point stagnation needs detection.

36. **Jump search trades block probes against local scans.** Its simplified bound is $n/b+b$, minimized near $\sqrt n$. Endpoint access must be constant-time for this to describe total operations.

37. **Interpolation's expected doubly logarithmic behavior is conditional.** Distribution, numeric arithmetic and progress assumptions matter. Skewed keys can make its worst-case work linear.

38. **Count pointer steps when searching linked representations.** Logarithmically many key comparisons can coexist with linear or worse traversal cost because a midpoint is not directly addressable.

39. **The insertion-gap decision tree uses Boolean tests.** Distinguishing $n+1$ gaps requires at least $\lceil\log_2(n+1)\rceil$ such tests. A different observation primitive needs its own lower-bound argument.

40. **Distinct rotated arrays expose a sorted half.** Repeated equal endpoint/midpoint keys can hide the rotation and force linear worst-case membership work.

41. **Strict bitonicity supplies a peak-search direction.** An increasing middle adjacent pair sends the peak rightward; a decreasing pair sends it leftward. Plateaus require a revised contract and proof.

42. **Pairwise minimum and maximum use $\lceil3n/2\rceil-2$ comparisons for $n\ge2$.** Initialize an even input from one compared pair, and an odd input from one unpaired record.

43. **Tournament runner-up candidates are only the champion's direct losers.** A loser elsewhere has another larger nonchampion witness and cannot be the second-ranked distinct record.

44. **A tournament's exact runner-up cost depends on its path.** Total comparisons are $n-1+d-1$ if the champion played $d$ matches. The balanced-bracket worst bound is $n+\lceil\log_2 n\rceil-2$.

45. **Second occurrence is not second distinct value.** Repeated maxima can occupy both largest record ranks. Excluding all keys equal to the maximum is an extra requirement.

46. **Keep a pivot key constant during partition.** A moving record's original slot may receive another key. Saving the pivot value preserves the invariant's reference threshold.

47. **Three-way partition maintains four regions while scanning.** They are less, equal, unknown and greater. The final unknown region is empty; the equal region can contain many occurrences.

48. **Reinspect the replacement after a greater exchange.** Decreasing the right boundary classifies the outgoing greater key, but the incoming key at the scan cursor is still unknown.

49. **The unknown-length measure decreases once per classification.** Thus an active range of length $m$ has exactly $m$ classification iterations in the presented inclusive-pivot three-way loop.

50. **A classification is not necessarily one Boolean comparison.** The shown `<` then `>` code can use two predicates for a nonless key. Exact-count questions must declare their primitive convention.

51. **A pivot from the active range guarantees a nonempty equal block.** Arbitrary external pivot values can have zero equal occurrences, so a selector using them needs a separate progress argument.

52. **Selection continues in one strict partition.** Sorting continues in both. The pivot-computation recursion in deterministic selection is a separate representative-array call.

53. **A rightward local rank subtracts both lower and equal counts.** Its value is $k-|L|-|E|$. Subtracting one pivot is valid only for the explicitly distinct-key single-pivot contract.

54. **Do not mix fixed global target indices with translated local ranks.** Updating the global left boundary already accounts for discarded positions. Shifting the global target a second time changes the query.

55. **All-equal input finishes in one three-way partition.** A two-way implementation can have very different equal-key behavior and should not inherit this conclusion automatically.

56. **Correctness and runtime are separate proofs.** A valid extreme pivot can preserve rank correctness while causing nearly full scans repeatedly and quadratic work.

57. **Distinct extreme-pivot maximum selection sums $n(n-1)/2$ pivot comparisons.** This exact count assumes one comparison per nonpivot key, excludes pivot-choice work, and follows the explicit active-length sequence.

58. **Conditional uniformity is the randomized guarantee's premise.** Choose an occurrence uniformly from each current active range, conditional on the preceding history. Merely using a random number does not ensure that distribution.

59. **Expected randomized cost applies to every fixed input.** It averages over algorithmic randomness; it is not a promise that the input arrived in random order.

60. **Expected linear work does not exclude quadratic unlucky runs.** A worst-case bound over random choices is a different statement from a worst-input expected bound.

61. **Never substitute $T(E[X])$ for $E[T(X)]$ without justification.** Nonlinear functions generally violate equality, and assuming linearity to prove linearity is circular.

62. **Phase analysis bounds actual conditional work.** A good pivot probability bounded below by a constant gives a bounded expected wait; constant-factor size reductions then yield a geometric expected-work sum.

63. **Small-size rounding needs a real base case.** The conservative randomized proof uses a finite base below eight and a $7/8$ shrink bound above it. Ideal fractions alone need their rounding caveat.

64. **Exact random-selection expectations condition on pivot rank.** The recurrence has one appropriate child per pivot rank and zero child when the pivot itself answers the request. Its stated partition counter must match the question.

65. **A median of medians is usually not the true input median.** Its purpose is to certify enough exclusions for a pivot. The final answer still follows the requested-rank partition rule.

66. **Count certified keys in disjoint original groups.** A full group of five contributes three weak-side occurrences. Exclude problematic boundary groups before assigning a conservative finite guarantee.

67. **Weak certificates are sufficient with duplicates.** A strict greater child excludes every certified at-most-pivot occurrence; a strict less child excludes every certified at-least-pivot occurrence.

68. **Include recursive representative selection in deterministic cost.** The recurrence contains both $T(\lceil n/5\rceil)$ and the one selected strict-child term, plus linear local work.

69. **Unequal children do not fit the ordinary Master theorem.** Use finite induction, a controlled recursion tree or a valid unequal-branch theorem with its assumptions checked.

70. **The finite group-five induction must absorb additive constants.** Child sizes sum to at most $0.9n+7$; a fixed base through 140 and coefficient $c\ge20a$ give the stated linear proof.

71. **Fixed odd group sizes above three give a subunit fraction sum.** Their ideal sum is $3(b+1)/(4b)$. Group-sorting cost remains linear only while the size is fixed.

72. **Groups of seven give ideal fractions $1/7$ and $5/7$.** With toll exactly $n$, linear substitution needs coefficient at least seven; this is not an implementation's exact comparison constant.

73. **A group-three recurrence bound is not a matching algorithm lower bound.** The equality recurrence with linear toll is $\Theta(n\log n)$, while an algorithmic inequality establishes only the corresponding upper bound without an adversarial construction.

74. **Repeated triple grouping changes the certificate.** Two levels yield four original certified keys per representative and the ideal fractions $1/9$ and $7/9$, allowing linear analysis after boundary corrections.

75. **Two-array selection searches feasible left counts.** Use $\max(0,k-n)\le i\le\min(k,m)$ and $j=k-i$. This prevents negative or oversized slices before comparing boundaries.

76. **Cross-boundary inequalities for two sorted inputs are weak.** Accept $A_L\le B_R$ and $B_L\le A_R$. If $A_L>B_R$, decrease the $A$ count; if $B_L>A_R$, increase it.

77. **Exact top-k extraction must control threshold ties.** Keep every strictly smaller key and only enough equal occurrences to reach $k$. Sorting the retained records adds $O(k\log k)$ to offline selection.

78. **Weighted answers follow mass, not record count.** Aggregate equality mass and carry the discarded-lower mass when moving right. Count-balanced pivots can still prove linear runtime.

79. **A true linear hybrid limits cumulative prefix work.** A logarithmic depth cutoff may already spend $\Theta(n\log n)$. A fixed $Bn$ work budget plus a proved linear fallback supports a linear worst-case total.

80. **Verification and preparation claims must have a stated scope.** Finite exhaustive checks, authentic archive examples and course synthesis provide strong evidence within their bounds. They do not prove a literal guarantee of success on every unseen question; use the invariant, model and counterexamples to transfer the knowledge.
