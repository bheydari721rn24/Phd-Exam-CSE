### A. Model and language

1. Define the universe before the events. A leading-zero code and a positive integer have different universes, so their unrestricted counts and all their intersections differ even if the required digits are identical.

2. Interpret “or” as inclusive unless exclusivity is stated. The union contains outcomes meeting both conditions, while the exclusive alternative is the symmetric difference and subtracts the shared region twice from the sum of the singles.

3. An intersection requires every named property but permits additional properties. An exact atom requires those properties and the failure of every other named property; replacing an atom by an intersection overcounts higher-multiplicity outcomes.

4. Separate a specified intersection from the sum of all intersections of that size. Multiply by $\binom mj$ only after proving that every specified $j$-index intersection has the same count.

5. In a three-set problem, an inclusive pair overlap includes every triple member. A pair-only overlap excludes the triple members, so add the triple count when converting pair-only data into the union formula.

6. All intersection data must refer to the same underlying objects. Combining a count of ordered assignments with a count of unlabeled partitions in one alternating sum has no mathematical justification.

7. The complementary formula includes the empty index set with intersection equal to the universe. The union formula excludes that index set; exchanging these conventions changes both the constant term and the target predicate.

8. Repeated or nested events do not invalidate inclusion-exclusion, but they often create unnecessary work. If $A\subseteq B$, replace $A\cup B$ by $B$ before enumerating intersections.

9. Independence is a probabilistic factorization property, not a synonym for disjointness. Inclusion-exclusion is valid for dependent events; independence is needed only if you compute an intersection probability by multiplication.

10. “At least one violation” is the bad-event union, whereas “no violation” is its complement. Write the requested predicate explicitly to prevent returning the excluded count as the valid count.

### B. Atom reconstruction and feasibility

11. The only-$A$ atom in three events is $|A|-|A\cap B|-|A\cap C|+|A\cap B\cap C|$. The final addition restores the triple after the two inclusive pair subtractions.

12. Exactly two of three events have count $S_2-3S_3$. Each triple member occurs in all three pair intersections, so subtracting it only once leaves two unwanted copies.

13. Exactly one of three events has count $S_1-2S_2+3S_3$. Verify the coefficients on objects with one, two and three memberships rather than guessing the signs from the ordinary union formula.

14. Check all eight atoms when complete three-event data are given. Nonnegative integer atoms are sufficient for finite-set realizability because disjoint groups of those sizes can be assigned the corresponding memberships.

15. Pairwise overlap inequalities alone are insufficient for feasibility. Even if every pair overlap fits inside each participating set, a single-only atom or the outside atom may be negative.

16. If only aggregate intersection sums are given, invert them to $N_r$. Nonnegative integer $N_r$ with the correct total certify aggregate realizability, but do not certify separately specified individual pair intersections.

17. When a triple overlap is unspecified, express every atom as a function of it. Intersect all lower and upper constraints on that variable; its valid integer range determines whether the question has zero, one or multiple answers.

18. A maximum-union argument needs an attaining arrangement. Minimizing duplicated memberships gives a bound, but only explicit valid atoms prove that the bound can occur with all stated marginal sizes.

19. For two probability events with probabilities $a,b$, the overlap ranges from $\max(0,a+b-1)$ to $\min(a,b)$. These bounds are exactly the nonnegativity constraints on the four atom weights.

20. Do not repair inconsistent survey data by silently changing a supplied number. Identify the negative atom, state infeasibility and, if asked, show what modification would restore it.

### C. General formulas and exact multiplicity

21. For a union, the order-$j$ intersection sum has sign $(-1)^{j+1}$; for its complement it has sign $(-1)^j$. The complement also starts with $S_0=|U|$.

22. The per-object proof counts an object in $r$ events through $\binom rj$ order-$j$ intersections. Summing the alternating binomial coefficients gives the desired indicator and proves the formula for arbitrary finite sets.

23. An order-$j$ intersection sum is $S_j=\sum_{r\ge j}\binom rjN_r$, not $N_j$. An object in many events contributes to many specified intersections and therefore appears with a combinatorial multiplier.

24. The exact-$r$ inversion is $N_r=\sum_{j=r}^m(-1)^{j-r}\binom jrS_j$. It includes $r=0$, where it becomes the complementary formula.

25. The at-least-$r$ formula uses $\binom{j-1}{r-1}$ for positive $r$, not $\binom jr$. The latter belongs to the exact-$r$ formula, so exchanging them changes the requested event.

26. At least zero properties always means the whole universe. Do not substitute $r=0$ into a formula derived for positive $r$ and introduce binomial coefficients with an invalid lower argument.

27. Recover multiplicity counts from the largest index downward if the closed inversion is forgotten. The system is triangular: each new equation has one remaining unknown after higher $N_r$ values are determined.

28. Exactly a specified membership mask and exactly a specified membership count differ. The first is one atom; the second sums all atoms whose masks have the stated number of set bits.

29. The full atom inversion sums over supersets of the desired mask with sign determined by the number of added bits. Summing over subsets would invert a different relation and give incorrect exact regions.

30. The formulas remain valid when some intersections are empty. Keep their counts as zero or prune them only after proving emptiness; do not omit an intersection merely because it looks unlikely.

### D. Bounds and probability

31. Odd-order Bonferroni truncations are upper bounds on a union, and even-order truncations are lower bounds. Taking complements reverses these directions, so the same truncation order bounds the no-event count from the opposite side.

32. The union bound is $|\bigcup A_i|\le S_1$ or its weighted analogue. It is exact only when all positive-weight outcomes have at most one membership; mutual exclusivity is a sufficient condition.

33. Clamp union bounds to zero and the universe size, and probability bounds to zero and one. This strengthens a valid loose inequality without pretending to know omitted higher intersections.

34. A valid second-order lower bound can be numerically farther from the answer than the first-order upper bound. Correct bound direction does not imply decreasing absolute error at each consecutive truncation.

35. Improve several available bounds by taking the maximum of certified lower bounds and the minimum of certified upper bounds. Do not choose the truncation that merely looks closest to an anticipated answer.

36. Pairwise independence does not determine triple or higher intersections. A pairwise-independent bit construction can have a forbidden triple outcome, so check the exact strength of the independence hypothesis.

37. Weighted inclusion-exclusion uses the same integer coefficients as cardinality inclusion-exclusion. Nonuniform outcomes must keep their actual weights; dividing a favorable-object count by the number of objects is valid only under uniformity.

38. For conditional probability, intersect each event intersection with the conditioning event and divide by its positive probability. Conditioning can destroy independence, so do not reuse an unconditioned product without justification.

39. Complement multiplication $\prod_i(1-p_i)$ requires mutual independence of the event indicators. Without it, use actual intersection data or bounds rather than multiplying marginal failure probabilities.

40. If the requested probability depends on an unspecified overlap, give an attainable range or two realizations. A unique numerical answer cannot be obtained from marginal probabilities alone without further structure.

### E. Functions and occupancy

41. Onto maps use missing-value events, with specified intersection count $(m-j)^n$. The factor $\binom mj$ chooses missing codomain labels; those labels are already part of the universe.

42. Do not multiply an onto count by $m!$ afterward. Labeled output values were distinguished from the beginning; an extra factorial would relabel outcomes already counted.

43. To require only a specified subset of $q$ output labels, sum over missing subsets of those required labels. Optional labels remain available, so the intersection base is $m-j$, not $q-j$.

44. Exactly $q$ image values require choosing their labels and then mapping onto the chosen set. The count is $\binom mqO(n,q)$; permitting arbitrary maps to that set allows smaller images and overcounts.

45. Exactly $q$ missing labels has count $\binom mqO(n,m-q)$. This is different from requiring a specified list of $q$ labels to be absent while allowing additional omissions.

46. Divide an onto count by $m!$ to forget labels on nonempty fibers. The division is valid because every partition into exactly $m$ nonempty blocks has the same $m!$ labelings.

47. The empty-function convention gives $O(0,0)=1$. It gives zero for an onto map from an empty domain to a nonempty codomain, and zero for any map from a nonempty domain to an empty codomain.

48. If $n<m$, the onto count must be zero; if $n=m$, it must be $n!$. These quick boundary checks detect an incorrect missing-label multiplier or an omitted last term.

49. Labeled-ball allocations weight an occupancy vector by a multinomial coefficient, while identical-token allocations weight it by one. Stars and bars cannot count arbitrary labeled-ball maps without these weights.

50. The Stirling recurrence gives an independent exact evaluation of onto counts. It avoids severe cancellation in floating-point alternating sums and also clarifies the difference between labeled fibers and unlabeled blocks.

### F. Permutations, fixed points and boards

51. For a specified set of $j$ fixed positions in a permutation, the intersection count is $(n-j)!$. The symbols assigned to those positions are forced, and the remaining symbols may be permuted freely.

52. Exactly $r$ fixed points has count $\binom nrD_{n-r}$. The derangement factor ensures that the remaining positions contribute no additional fixed points.

53. Avoiding fixed points at only $q$ specified positions uses $\binom qj(n-j)!$. Replacing $q$ by $n$ would impose restrictions on positions that the question leaves unrestricted.

54. Simultaneously requiring and forbidding the same fixed position makes the count zero. Resolve contradictory conditions before contracting fixed positions or applying inclusion-exclusion.

55. The initial derangement values are $D_0=1$ and $D_1=0$. The nearest-integer rule for $n!/e$ applies for $n\ge1$ and must not replace the empty-permutation convention.

56. A rook intersection is nonempty only when its forbidden cells have distinct rows and columns. Arbitrary selections of cells are not all compatible, so the rook coefficient is generally smaller than a plain binomial coefficient.

57. Nonconflicting $k$ forbidden cells leave $(n-k)!$ completions. A conflicting selection has zero completions, even if the factorial expression itself is positive.

58. Rook-polynomial multiplication requires disjoint row sets and disjoint column sets between components. Cell-disjoint components sharing a row can still conflict and cannot be multiplied independently.

59. Deletion in the rook recurrence has two different meanings. Excluding the chosen cell deletes only that cell; including it deletes its entire row and column and contributes one power of the polynomial variable.

60. Directed adjacency constraints in a linear arrangement need compatible predecessor/successor degrees and no directed cycles. Only then may the selected edges be contracted into path blocks.

### G. Caps, digits and arithmetic intervals

61. Shift every lower bound before defining upper violations. The residual total and each residual cap change, so an inclusion-exclusion expression in the original variables can miss the available budget.

62. An upper violation starts at one above the allowed cap. Subtracting the cap rather than the cap plus one incorrectly excludes boundary-valid occupancy vectors.

63. Equal caps permit grouping by the number of violated coordinates; unequal caps usually require the actual selected threshold sum. Average caps do not preserve intersection cardinalities.

64. A negative residual total contributes zero in stars-and-bars counting. State this convention explicitly instead of extending the ordinary binomial formula into a different generalized-binomial identity.

65. Check the total against the sum of lower bounds and the sum of upper bounds first. An impossible total has zero solutions, which should agree with any later alternating expression.

66. An unbounded coordinate has no upper-violation event but still counts as a box in the residual composition. Removing the coordinate from the dimension changes the universe.

67. Required-symbol counting with position-dependent alphabets uses the product of the surviving alphabet sizes at each position. A single base raised to the string length is justified only when those sizes agree.

68. Positive decimal integers cannot begin with zero. Excluding required nonzero digits decreases the first-position alphabet differently from later-position alphabets, so treat the first digit separately.

69. Divisibility intersections use the least common multiple. Use a product only after establishing pairwise coprimality; repeated or overlapping prime factors otherwise produce an incorrect intersection denominator.

70. Strict integer endpoints must be converted before floor counts. “Less than 1000” ends at 999, while “at most 1000” includes 1000 and can change several divisor-event counts simultaneously.

71. A residue class in $[L,H]$ is counted by subtracting two mathematical floors. Truncation toward zero fails for negative endpoints, so use true integer floor division in implementations.

72. Congruence intersections may be empty. Check compatibility modulo the greatest common divisor before counting a merged class modulo the least common multiple.

73. Euler's totient product uses each distinct prime divisor once. Prime exponents are already included in the leading factor $n$ and must not generate repeated factors $1-1/p$.

74. The case $\varphi(1)=1$ follows from the positive domain containing only one and an empty prime product. Switching to a domain that excludes one requires explaining the altered convention.

### H. Computation and final solution checks

75. General inclusion-exclusion has exponentially many intersections. Symmetry, redundant-event elimination and incompatibility can reduce the work, but they must be derived from the model rather than assumed to hold in every problem.

76. The superset atom transform takes $O(m2^m)$ arithmetic operations on a complete intersection table. This excludes the potentially additional cost of obtaining the table's intersection counts.

77. Keep integer alternating sums exact. Intermediate terms can be much larger than the final answer, so floating-point cancellation can corrupt a correct formula before any final probability is computed.

78. Verify a hard formula with a structurally different method when possible: atom construction, direct enumeration, a recurrence, an occupancy convolution or a matching dynamic program. Repeating the same formula with renamed variables is not an independent check.

79. A finite enumeration confirms only the enumerated parameter range. Pair it with a general proof for an identity stated for arbitrary sizes; neither replace the proof with a demonstration nor ignore a counterexample from enumeration.

80. Every final answer should pass integrality, nonnegativity, universe-size and boundary checks. For an extremum, add an attaining construction; for incomplete data, state the missing information or a proved range instead of claiming an unsupported exact answer.
