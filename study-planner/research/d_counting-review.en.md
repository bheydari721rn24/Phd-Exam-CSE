### Model selection and proof obligations

1. State what one outcome records before counting it. A committee records membership; an officer assignment records both membership and named roles. Two models with the same selected people can have different counts because their surviving information differs.

2. Treat positions as labels unless the statement explicitly erases their order. A word, a function on a labeled domain, and an ordered tuple retain positions even when their entries repeat.

3. A set cannot contain duplicate members. A multiset can contain repeated types but forgets their order. Do not use a subset coefficient to count a multiset without first establishing a bijection.

4. Separate “identical objects” from “identically sized groups.” Distinct people remain distinct when groups have equal sizes; identical tokens do not acquire identities merely because their boxes have labels.

5. Product-rule branches may depend on earlier choices in identity. Their counts must be uniform across all legal prefixes at that depth. This is weaker than independence of choices and is unrelated to probabilistic independence unless a probability model is supplied.

6. When completions vary with the prefix, sum their counts. For $1\le i\le j\le n$, the completion count is $n-i+1$, so the total is a triangular sum rather than $n^2$.

7. Before adding cases, identify an outcome property with exactly one value in every outcome. Exact category size, first symbol, or used multiplicity vector often gives a disjoint partition; overlapping “contains A” cases do not.

8. A counting bijection needs validity, coverage, and uniqueness. Write its inverse when the encoding is nonobvious. Losing even one necessary identity makes the inverse fail and changes the count.

9. Divide only after determining every fiber size. The phrase “order does not matter” alone does not prove that every outcome has $k!$ ordered representations.

10. Check the model on a small instance with the same constraints. A noninteger count is decisive evidence of an invalid expression, but an integer answer alone does not establish correctness.

### Permutations, subsets, and role assignments

11. For $0\le k\le n$, ordered distinct selections have $P(n,k)=n!/(n-k)!$. For $k>n$ their count is zero; do not evaluate a negative factorial.

12. The empty selection exists exactly once. Thus $P(n,0)=1$, $\binom n0=1$, and $0!=1$. An empty product equals one because it contributes no choice constraint.

13. An unrestricted length-$k$ word over $n$ symbols has $n^k$ outcomes when reuse is unlimited. A finite inventory is a different model, even if every symbol appears in the alphabet.

14. A $k$-subset has $k!$ orderings because all its members are distinct. This constant fiber proves $\binom nk=P(n,k)/k!$; it does not apply unchanged when repeated entries are allowed.

15. For nonnegative integer upper arguments, use zero for infeasible binomial lower arguments. Negative upper arguments need a separate algebraic definition and must not accidentally count impossible residual allocations.

16. A chair chosen from a $k$-committee contributes a factor $k$, not $n$. A chair outside that committee contributes $n-k$. State which of these models the problem requires.

17. Two distinct ordered roles inside a committee contribute $k(k-1)$. If the same person may hold both roles, the factor is $k^2$. The role names retain order in either case.

18. At-least category restrictions require all feasible exact counts. For $k$ selections from populations $a,b$, the first-category count cannot exceed $thethe smaller of a and k or fall below $thethe larger of zero and k minus b; apply any extra bounds within that range.

19. Requiring exactly one of two distinguished people gives $2\binom{n-2}{k-1}$. Requiring both gives $\binom{n-2}{k-2}$; forbidding both together gives its complement within all $k$-subsets.

20. Complementation preserves counts of $k$-subsets and $(n-k)$-subsets through an explicit inverse. It does not imply arbitrary category inequalities have equal counts unless a valid symmetry maps one family to the other.

### Repeated symbols and bounded inventories

21. A fixed-content word has $n!/\prod_i n_i!$ arrangements when the nonnegative multiplicities sum to n. Erasing labels on identical copies has a constant fiber precisely because their multiplicities are fixed.

22. Fixed positions consume inventory first. If one A is fixed at an endpoint, decrease the A multiplicity by one before computing the interior multinomial. There is no additional choice for an already fixed symbol.

23. Equal endpoints require a sum over every symbol with at least two available copies. Reduce that symbol's multiplicity by two in each disjoint case. A symbol with only one copy contributes zero.

24. A partial word from finite stock requires summing over all feasible used-multiplicity vectors. The total stock factorial counts full arrangements, and $n^k$ permits unbounded stock; neither automatically handles a partial inventory.

25. Requiring exactly r distinct symbols means choosing the used symbol set and ensuring every selected symbol occurs. An unrestricted $r^k$ factor includes words using fewer than r symbols and therefore overcounts.

26. Multiplicity patterns with repeated part sizes require careful assignment to symbol types. For pattern 2,2,1, choose the singleton type; do not also order the two types with multiplicity two unless that artificial order is later removed.

27. Labeled tokens placed in labeled boxes have $m^N$ assignments without occupancy restrictions. Identical tokens in those boxes instead give occupancy vectors counted by stars and bars. Their probability distributions also differ.

28. Choosing occupied positions for each symbol gives a constructive multinomial proof. The successive pools must shrink; repeatedly choosing from the original position set permits overlapping symbol assignments.

29. A zero multiplicity contributes $0!=1$, not zero. Omitting an unused symbol from the displayed denominator is harmless; forcing it to occur changes the outcome family.

30. An unordered replacement selection cannot generally be counted as $n^k/k!$. All-equal words and all-distinct words have different ordering fibers, so the single denominator fails.

### Blocks, gaps, and separation

31. Contract a specified consecutive block only when expansion is unique. Distinct specified members in an arbitrary internal order add a factorial; a fixed internal word adds no internal permutation factor.

32. Several disjoint blocks contract independently. Overlapping required blocks may force a unique longer chain, be inconsistent, or have several representations; analyze their shared elements rather than reusing the disjoint formula.

33. Two specified distinct people adjacent in a line have $2(n-1)!$ arrangements. The two orientations are distinct. Their nonadjacent count is the complement within all $n!$ linear orders.

34. Arranged unmarked elements create one more linear gap than their number. Both endpoint gaps are legal unless the statement excludes them. Omitting either endpoint removes valid separated arrangements.

35. Identical marked symbols inserted into selected gaps need no permutation factor. Distinct marked objects do need a factorial to assign their identities to the ordered selected gaps.

36. Repeated unmarked symbols change the base-arrangement factorial to a multinomial. Their gap positions are still ordered along the resulting word; equal neighboring symbols do not make different gap locations identical.

37. For k separated ones in n positions, compress $a_i$ to $a_i-(i-1)$. The inverse proves $\binom{n-k+1}{k}$, rather than merely suggesting it from a diagram.

38. At least s zeros between successive ones consumes $s(k-1)$ interior positions. It does not consume $sk$ positions unless an endpoint condition adds the missing requirement explicitly.

39. Fix endpoints before applying a gap formula. A final one forces its preceding position to zero under nonadjacency; count the remaining interior interval after removing those fixed positions.

40. Feasibility should precede numerical evaluation. With k positive separated ones and spacing s, at least $k+s(k-1)$ positions are needed. When this minimum exceeds the available length, the count is zero.

### Circular arrangements and group identities

41. Distinct people around an unnumbered oriented circle have $(n-1)!$ orders for $n\ge1$. Numbered seats retain rotational position and give $n!$ instead.

42. Dividing oriented circular orders by two to identify reflection requires $n\ge3$ distinct objects. For one or two objects, reversal can preserve the same circular class, so the factor two fails.

43. Circular adjacency includes the boundary between the last and first displayed entries. A linear word used to draw a circle does not create an exempt endpoint pair.

44. A circle of p arranged unmarked people has p gaps. A line has $p+1$. Removing marked people from the completed circle verifies which cyclic gaps they occupied.

45. Repeated-color words can have short rotation orbits. A periodic word and an aperiodic word need not have the same number of distinct seat-labeled representations. Test periodicity before dividing by n.

46. The orbit-counting average uses the number of words fixed by each group element. It is not an average of orbit sizes. Counting fixing pairs proves why each orbit contributes the same total.

47. Rotation by r places in n seats has $\gcd(n,r)$ cycles. An unrestricted q-color fixed word is constant on each cycle and has $q^{\gcd(n,r)}$ choices.

48. Prescribed color totals impose cycle-inventory equations. If every cycle length is even, a word with an odd total of a specified color cannot be fixed. Unrestricted fixed-color counts would include forbidden inventories.

49. For unlabeled nonempty blocks of distinct elements, internal orders and external block labels are separate redundancies. Equal-sized blocks still contain different sets, so their label permutations create distinct labeled representations.

50. With a_j blocks of size j, the denominator contains both $(j!)^{a_j}$ and $a_j!$. Divide externally only among slots of equal size; unequal block sizes already identify their respective roles.

51. Allowing empty boxes can destroy free group-label action. A partition with two empty boxes has fewer distinct labelings than one with no empty boxes. Do not use $m!$ without a fiber argument.

52. For distinct elements, nonempty unlabeled partitions are counted by $S(N,m)$ and labeled onto allocations by $m!S(N,m)$. Identical elements in unlabeled boxes require integer partitions instead.

### Integer bounds and coupled constraints

53. Stars and bars counts nonnegative occupancies in labeled boxes. The order of bars fixes box identities; the identities of the stars have been discarded. These assumptions should be stated.

54. Adjacent bars and endpoint bars encode empty boxes and are legal for nonnegative allocations. Positive allocations prohibit those patterns after interpretation, or more simply use a lower-bound translation.

55. Translate lower bounds with new variable names. The forward map subtracts each bound and the inverse adds it. If the residual total is negative, there are no solutions.

56. Positive m-variable solutions of total N number $\binom{N-1}{m-1}$ only for $N\ge m\ge1$. A residual total of zero has one allocation, with every translated variable zero.

57. A total inequality gains one uniquely determined slack variable. The count of m nonnegative coordinates with total at most N is $\binom{N+m}{m}$; the slack is not an independent additional decision.

58. For totals in the inclusive interval [L,U], subtract the at-most-(L-1) family from the at-most-U family. If L=0, the removed family is empty rather than a negative-total stars-and-bars expression.

59. A bound $x\le u$ forbids $x\ge u+1$, so the subtraction shift is $u+1$. Using u instead removes the allowed boundary value.

60. Several upper-bound violations can overlap. A short exact sum over bounded coordinates avoids double subtraction; otherwise retain the required intersection corrections taught in the next chapter.

61. A divisibility condition changes the spacing of legal values. Set $x=hj+r$ with the actual residue and derive the integer range of j; do not treat the coefficient h as one in a stars-and-bars equation.

62. When a short bounded variable and a weighted variable coexist, fix the bounded variable and count the resulting interval of integers. The forced last variable does not supply another multiplicative factor.

63. Eliminate shared sums in coupled equations before multiplying. The product rule applies to disjoint residual groups only after their totals and all remaining constraints have been resolved.

64. Linear dimension is not an integer-point count. A family can have infinitely many real solutions but finitely many nonnegative integer solutions. Rank information alone does not supply the allocation cardinality.

### Identities, coefficients, and parity

65. Pascal's identity partitions subsets by one specified member. This proves both disjointness and completeness; a numerical pattern in a triangle is an illustration rather than the proof.

66. Vandermonde requires complementary lower indices totaling the selected size. Interpret the factors as choices from disjoint populations and sum over the unique first-population count.

67. The sum of squared coefficients becomes Vandermonde after symmetry changes one lower index to n minus that index. Without the shared upper n, the same squared-sum shortcut is not automatically valid.

68. A product $\binom ni\binom ir$ records an i-subset with r marked members. Reversing the choice order gives $\binom nr\binom{n-r}{i-r}$ and exposes any later free subset.

69. Two ordered distinct marks contribute $i(i-1)$; two marks allowed to coincide contribute $i^2$. Decompose the latter into distinct and coincident cases before applying moment identities.

70. A hockey-stick sum partitions subsets by their unique extreme element. Truncated index ranges remove terms from the full identity; do not retain the unadjusted upper coefficient.

71. In a binomial expansion, each factor is a labeled choice position. The coefficient counts the selections yielding a specified monomial, even though products are collected into unordered exponent data afterward.

72. Solve the exponent equation before computing a coefficient. A fractional or out-of-range selected-factor count means coefficient zero. Merely being between the minimum and maximum degree is not sufficient.

73. Scalars attached to summands are raised to their own multiplicities. The position-assignment coefficient and the scalar-power coefficient both contribute and should not be conflated.

74. A multinomial with a single variable can have several multiplicity vectors yielding the same degree. Enumerate all feasible vectors and add their disjoint contributions; separate-variable exponents may determine a unique vector.

75. The even/odd marked-symbol filter uses the signed expansion as well as the ordinary expansion. Unequal marked and unmarked alphabet sizes generally prevent an equal half split.

76. For empty words, zero marked occurrences is even. Treat length zero explicitly rather than relying on ambiguous zero-power substitutions in a formula derived for positive length.

### Monotone sequences, paths, and numerical checks

77. Weakly increasing k-term sequences over n values correspond to nonnegative value multiplicities and count $\binom{n+k-1}{k}$. Strictly increasing sequences instead count $\binom nk$, with infeasible k giving zero.

78. Inclusive weak triple loops count $\binom{n+2}{3}$. A strict inequality changes the index family; split by the remaining equality cases or construct a new compression instead of keeping the old formula.

79. A monotone path through a point splits uniquely into prefix and suffix, so multiply their counts. Two required points must be coordinatewise comparable in the required chronological order; otherwise the answer is zero.

80. Exact enumeration verifies finite cases and helps detect bad models, but does not prove a formula for arbitrary parameters. Keep the bijection or case proof, use exact integer arithmetic, and inspect overflow and variable-size operand costs when implementing the count.
