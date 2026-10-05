# Examination rules: recognize the model before using a bound

1. **Specify the objects and the labeling map.** A pigeonhole proof starts with a total function from the objects to the classes. For eight integers modulo seven, the objects are eight indexed positions and the label is the canonical remainder. Two positions sharing a label need not contain identical numerical values. Describe the property induced by label equality before counting classes.

2. **Use a strict domain-versus-image comparison.** More than k objects force a repeated label among k labels. Exactly k do not: a bijection is a counterexample. With values 1,2,4,8, sixteen subset objects have sixteen different sums. The equality boundary is therefore mathematically substantive, not an off-by-one convention.

3. **An available label need not be occupied.** The denominator in a guaranteed maximum may include empty classes. The conclusion is that some class is large; it does not imply surjectivity. Seven objects mapped to five labels may all share a single label. An option asserting that all five labels occur needs additional information.

4. **Keep distinct objects separate from distinct values.** Repeated entries at different positions are separate objects when a problem counts indexed data or people. Two people can share a birthday and remain different people. For divisibility selections from a set, however, repeated numerical values are excluded; allowing repeated copies would change the witness requirements.

5. **Count inclusive endpoints.** An integer interval from L to H has H minus L plus one labels. Nine-digit IDs starting with nine have digit-sum labels nine through eighty-one, giving seventy-three labels. Omitting the lower endpoint or forgetting the added one can change both the collision threshold and the rounded occupancy.

6. **Prove the image-size bound, not merely its notation.** Bounding subset sums by zero through the total gives at most total plus one labels; some labels may be absent. This upper bound is enough for collision. Exact attainability of every label is only needed when making a sharpness claim based on those labels.

7. **Separate existential and specified-class conclusions.** Thirty objects in five bins force six somewhere, but they need not put anything in a designated bin. To force a specified color from a finite stock, account for all other colors that an adversary can draw first. A formula for any color does not answer a specified-color question.

8. **Separate every-input guarantees from a particular witness.** A threshold theorem quantifies over all legal placements. Showing one favorable distribution proves only possibility. Showing one avoiding distribution at the preceding total is useful for sharpness, but it must be paired with a universal sufficient argument at the proposed threshold.

9. **Deterministic pigeonhole bounds need no probability model.** A twelve-bit hash forces collision at 4097 distinct inputs regardless of output probabilities. Birthday-style collision probabilities require random-output assumptions and may become substantial much earlier. Do not replace a universal threshold with an expected or likely threshold.

10. **Construct counterexamples to universal options.** If an option claims that five objects mapped to eight labels must collide, an injection refutes it. If it claims collision is impossible, a constant map refutes it. Both examples fit the same sizes, so cardinalities alone determine neither property below the forcing threshold.

11. **Round integer occupancies upward for a guaranteed maximum.** For N integer objects and k positive bins, some occupancy is at least $\lceil N/k\rceil$. With 43 objects and eight bins this is six. A vector with three sixes and five fives attains the bound, so no stronger universal integer maximum bound follows.

12. **Round downward for a guaranteed minimum.** Some occupancy is at most $\lfloor N/k\rfloor$. With 43 objects and eight bins this is five. This does not say every bin has at most five, and it does not identify the same bin used by the maximum conclusion.

13. **Do not replace weak inequalities with strict ones.** A mean of three guarantees a value at least three, not a value greater than three. The vector with three in every bin refutes the strict conclusion. Test an all-equal vector whenever the stated mean is integral.

14. **A nonintegral integer mean forces both strict directions.** If N is not divisible by k, integer occupancies cannot all equal N divided by k. Some occupancy is above the mean and some below it. For 22 objects in seven bins, their bounds are at least four and at most three respectively.

15. **Above-average and below-average existence are equivalent for a fixed finite list.** If every value is at most the mean and one is strictly smaller, the sum is too small; the reversed argument handles a value strictly larger. Either all entries equal the mean, or both strict directions occur. This uses the actual arithmetic mean of the same list.

16. **Real loads do not admit integer ceilings.** Two servers carrying total load 0.8 need only force maximum load at least 0.4. Loads 0.4 and 0.4 refute an asserted lower bound of one. Ceiling arguments depend on discrete integer counts; weighted or continuous quantities use unrounded averages.

17. **Use positive capacities when normalizing utilization.** For capacities $c_i>0$ and loads totaling N, some utilization is at least $N/\sum_i c_i$. Multiply the proposed strict upper bounds by the corresponding capacities and sum to prove it. An unweighted mean of utilizations generally has a different denominator and meaning.

18. **Balance to demonstrate sharp average bounds.** Write $N=qk+s$ with $0\le s<k$. An occupancy vector with s bins of size q plus one and the remaining bins of size q has the correct total and the smallest possible maximum. This construction requires that no separate bin capacity forbids those occupancies.

19. **Saturation converts a sum into individual equalities.** If each occupancy is bounded above by its capacity and the total equals the sum of capacities, all deficits are nonnegative and sum to zero. Every bin must attain its capacity. Unequal capacities are allowed; a balanced-vector argument is unnecessary and may be illegal.

20. **Attendance totals count incidences, not distinct people.** Four workshop totals 18,16,14,12 add to sixty incidences. With twenty people each attending at most three, saturation forces exactly three workshops per person. It does not force everyone into every workshop or every pairwise intersection.

21. **Force an r-fold occupancy by exceeding avoidance capacity.** With k unrestricted bins, avoiding occupancy r allows at most r minus one in each. The exact threshold is $k(r-1)+1$. Seven bins force five somewhere at twenty-nine objects, not at thirty-five.

22. **Check r equals one explicitly.** Avoiding a positive occupancy in every bin permits only zero total, so one object forces some occupied bin. The generalized threshold agrees. A requirement that every bin be occupied is different and cannot be forced by total size alone when arbitrary concentration is permitted.

23. **Unequal targets give unequal avoidance caps.** To force at least one target $r_i$ in bin i, compare total occupancy with $\sum_i(r_i-1)$ when all bins are unrestricted. The targets must be positive integers. The conclusion is a disjunction of targets, not a simultaneous guarantee in every bin.

24. **Finite stock clips every avoidance cap.** With stock $s_i$, the avoiding occupancy in bin i is at most $\min(s_i,r_i-1)$. Inventories 2,7,9 and a common target four have total avoidance capacity eight; nine draws suffice. Treating the first stock as if three red items existed would produce an incorrect threshold.

25. **An algebraic threshold may be physically infeasible.** If all stocks are smaller than their targets, even the full stock avoids every target. Report impossibility, rather than the impossible draw count one larger than the total stock. For stocks 2,7,9, ten of any color cannot be obtained at any legal draw count.

26. **A specified color uses a different adversarial maximum.** To force r blue items, an adversary may draw every nonblue item and only r minus one blue items. If enough blue stock exists, the threshold is other-stock total plus r. Stocks red two, blue seven, green nine require fifteen draws to force four blue.

27. **Distinct colors use the largest inventories.** To avoid t distinct colors, draw from at most t minus one colors, choosing the largest stocks to maximize avoidance. Stocks 2,7,9 force all three colors only at seventeen draws. This is unrelated to capping each color at t minus one items.

28. **A heavy-bin count needs an upper cap.** With common capacity c and heavy threshold r, h heavy bins permit at most $hc+(k-h)(r-1)$ objects. Solve this inequality for h and round upward, then clip below at zero. Without an upper cap, one heavy bin can absorb arbitrarily many excess objects.

29. **Show feasibility of the heavy-bin bound.** For 31 objects, eight bins, cap six, and heavy threshold three, four heavy bins are necessary and attainable by 6,6,6,5,2,2,2,2. An inequality supplies a lower bound; the actual vector proves it is the minimum for these parameters.

30. **Reject illegal extremal constructions.** A balanced vector 3,3 is not allowed in bins of capacities one and nine. For six objects, legal alternatives are 0,6 or 1,5; their pair counts are fifteen and ten. Domain restrictions apply to the sharpness example as strongly as to the proof.

31. **Count collision pairs within each fiber.** For occupancies $x_i$, the actual pair count is $\sum_i\binom{x_i}{2}$. The vector 5,4,1 has sixteen equal-label pairs. Multiplying different occupancies counts cross-label pairs instead and answers a different question.

32. **Exchange proves pair minimization.** Move one object from a bin of size a to one of size b with a at least b plus two. The pair total decreases by a minus b minus one, which is positive. Repeating the exchange yields balanced occupancies when all placements are unrestricted.

33. **Use the exact balanced-pair formula.** For $N=qk+s$, the minimum is $k\binom q2+sq$. Seventeen objects in five bins give q three, s two, and twenty-one pairs. The largest fiber size four alone would establish only six pairs and lose the contributions of other fibers.

34. **Maximum pair count uses concentration.** For N objects in unrestricted bins, at most $\binom N2$ unordered pairs exist, and putting everything in one bin makes them all collide. Balancing minimizes this quantity; using it to maximize reverses the extremal argument.

35. **Higher equal-label tuples have binomial contributions.** A fiber of size x contributes $\binom xt$ t-element monochromatic subsets. Its marginal cost is $\binom{x}{t-1}$, which is nondecreasing. Balancing is a minimizer without caps, but zero or tied marginal costs can permit other minimizers; uniqueness is not automatic.

36. **Divide with a remainder before rounding.** Eighteen objects in four bins balance as 5,5,4,4, yielding thirty-two pairs. Replacing every occupancy by the ceiling five changes the total to twenty and overcounts. The remainder tells exactly how many bins receive the larger size.

37. **Bit width determines the hash codomain.** A b-bit output has $2^b$ labels, including the all-zero word. The universal first collision threshold is $2^b+1$. Counting only nonzero words changes the function model; counting b labels confuses bits with complete output words.

38. **A guaranteed collision is not a construction of colliding inputs.** Cardinality proves that a pair exists. Finding it can require examining the actual map. The occupancy lab and prefix algorithm construct witnesses for their explicit inputs; a general cryptographic collision may be computationally difficult despite the same finite principle.

39. **Partial image information can strengthen a bound.** If a twelve-bit function is known to use at most one thousand outputs, use one thousand as the image-size bound rather than 4096. The claim must follow from actual restrictions on the function, not an assumption that all theoretically available labels are occupied.

40. **Separate collision counts from repeated-bin counts.** A single triple contributes three pairs, while two doubletons contribute two. Six objects in four bins force at least two pairs, not necessarily two repeated bins in every placement. A question about numbers of pairs and one about numbers of non-singleton fibers require different objectives.

41. **Equal residues support a divisible difference.** If two integers share a remainder modulo m, subtracting yields zero modulo m. Their sum has twice that remainder and need not be divisible. Values one and six modulo five are a direct counterexample to the sum interpretation.

42. **Canonical remainders remove negative-value ambiguity.** Use labels zero through m minus one even when the input integers are negative. For example minus one has canonical remainder four modulo five. Changing an implementation language's signed remainder convention without normalization can break a lookup-table witness.

43. **Include the empty prefix.** For m input values, there are m plus one prefix sums including zero, so m remainder classes force collision. Omitting the empty prefix loses a possible witness starting at the first entry and destroys the universal counting argument at exactly m values.

44. **Translate prefix indices correctly.** If prefix indices i and j coincide modulo m with i less than j, the block is positions i plus one through j. Prefix indices two and five therefore retain positions three through five. Including position i is an off-by-one error that need not preserve divisibility.

45. **A prefix collision guarantees a nonempty contiguous block.** Distinct ordered prefix indices give a nonempty difference of nested index sets. An arbitrary subset collision need not give a zero-sum subset, because its two sides are not nested. Indexed values 2,2 modulo three illustrate a collision with no nonempty zero-sum subset.

46. **The input-length boundary is sharp for the universal prefix theorem.** Four ones modulo five have no nonempty divisible block. Five ones do. Thus m entries suffice and m minus one can fail. Particular shorter inputs may still contain a witness; the bound does not deny that possibility.

47. **Track repunits by recurrence rather than enormous integers.** The next remainder is ten times the previous remainder plus one, reduced modulo m. For seven the remainders at lengths one through six are 1,4,6,5,2,0. This supplies both the multiple 111111 and a shortest-length certificate.

48. **Zero-one multiples allow trailing zeros.** A difference of two repunits is positive and has an initial string of ones followed by zeros. The construction works for every positive modulus. An all-ones multiple needs an additional invertibility condition; modulo six, 1110 works but every all-ones number is odd.

49. **Cancel a modular factor only when justified.** A factor coprime to the modulus has an inverse and can be canceled. Nonzero is enough in a prime modulus but not in a composite modulus. Modulo six, two times one and two times four are congruent while one and four are not.

50. **Prime-square images require a separate p equals two case.** For an odd prime p, opposite nonzero inputs pair up and the square image has $(p+1)/2$ elements. Two such images overlap in a p-element universe. At p two, both residues are squares and direct verification gives x one, y zero; the odd-prime count must not be substituted.

51. **Count indexed subsets even when numerical entries repeat.** A list of n positions has $2^n$ index subsets. Equal values do not merge these objects. Their sum image can be much smaller, which helps collision. A problem asking for subsets of a mathematical set excludes repeated elements and has a different domain.

52. **Include the zero sum of the empty subset.** For positive entries with total T, subset sums lie in zero through T, giving T plus one labels. A comparison with T alone can falsely claim collision at equality. Powers of two realize all T plus one labels distinctly in the boundary construction.

53. **Cancellation removes shared indices, not arbitrary equal values.** From equal sums of two index subsets, delete their common positions from both. The remaining sets are disjoint and still have equal sum. Repeated equal numerical values at different indices may remain, and they are legitimate distinct objects in an indexed problem.

54. **Positivity supplies two nonempty residual sides.** Distinct collided subsets leave at least one nonempty side. If all values are positive, equality of sums rules out an empty other side. A zero entry is a counterexample without positivity: the empty subset collides with its singleton but cannot yield two disjoint nonempty subsets.

55. **Fixed-size subset images can give stronger comparisons.** Four-element subsets of one through eight number seventy, while their sums lie in the seventeen labels ten through twenty-six. Equal sums follow. After canceling a common part, the residual sets remain equal in cardinality, but their cardinality need not remain four.

56. **Product-label cancellation requires units.** Subset products always have remainder labels, including empty product one. If common factors are units modulo m, cancel them to obtain disjoint residual product sets. If some factor is not invertible, the original collision still exists but the canceled congruence may fail.

57. **Complement bins need distinct members.** In one through twenty, pairs summing to twenty-one form ten disjoint two-element bins. Eleven distinct selections force a completed pair; ten can avoid by taking one per bin. Repeated draws of the same value do not create two distinct complementary values.

58. **Handle an involution's fixed point separately.** For sum twenty-two in one through twenty-one, value eleven is self-complementary. It cannot form a pair of distinct selections with itself. Ten two-element bins plus this singleton permit eleven avoiding selections, making twelve the exact forcing threshold.

59. **Odd-part chains encode divisibility, not merely parity.** Every positive integer is uniquely a power of two times an odd core. Equal cores put two distinct values on one divisibility chain. Grouping just into odd and even classes proves equal parity and provides no guarantee that one divides the other.

60. **Generalize cores carefully to another base.** Dividing out all powers of three leaves a core not divisible by three. Among one through 299 there are two hundred such cores. Two hundred and one selections force a quotient that is a positive power of three. For a composite base, dividing out complete base powers still defines chains, but this is not the same as removing every prime factor.

61. **A partition gives a geometric sufficient bound.** If k cells each have diameter at most d, k plus one points force distance at most d. The points must be assigned to exactly one cell, including boundaries. A partition proof does not establish the globally smallest number of points unless a separate avoiding configuration attains the preceding count.

62. **Use cell diameter, not side length.** A square of side s has diameter $s\sqrt2$. To force unit-square distance at most one-quarter by an equal grid, at least six divisions per side are needed. Four divisions give side one-quarter but diameter larger than the target.

63. **Strict distance conclusions need strict geometric hypotheses.** A closed square cell can contain its opposite corners at exactly its diameter. Thus a closed-cell proof gives at most that diameter. Interior-point problems may allow a strict conclusion, but it must follow from the actual locations and cannot be imported from a different closed-domain statement.

64. **A sharp triangle bound needs a four-point counterexample.** Four half-size triangular cells show that five points force distance at most one-half. Three vertices and the centroid give four points whose minimum distance is $1/\sqrt3$, larger than one-half. Together these prove the threshold five, rather than just sufficiency.

65. **Half-open fractional intervals give a strict difference bound.** Partition zero through one into m half-open intervals of length one over m. Two fractional parts in the same interval differ by strictly less than one over m. An endpoint at one is never a fractional part, and endpoints belonging to adjacent intervals must not be double-assigned.

66. **Divide the approximation error by q.** From $|q\alpha-p|<1/m$ and positive q, infer $|\alpha-p/q|<1/(mq)$. The integer q is at most m because it is the difference of two prefix indices in zero through m. A witness may have zero error when alpha is rational, which still satisfies the strict positive bound.

67. **Use ordered ending-length pairs for monotone subsequences.** Assign each value its longest increasing and decreasing subsequence lengths ending there. For an earlier and later unequal value, the smaller-to-larger case increases the increasing label; the larger-to-smaller case increases the decreasing label. Therefore no two positions share the same pair.

68. **The sharp asymmetric threshold is a product plus one.** To avoid increasing length r and decreasing length s, only $(r-1)(s-1)$ ending-label pairs are available. The next entry forces one target. Use r minus one descending blocks of s minus one increasing-block-ordered values to show the preceding length can avoid both.

69. **The symmetric bound uses a ceiling.** A distinct sequence of length N guarantees monotone length $\lceil\sqrt N\rceil$. One hundred force ten and one hundred and one force eleven. A floor agrees at perfect squares and therefore can appear plausible while failing just above them.

70. **Subsequence and duplicate qualifications must remain explicit.** Skipped positions are allowed in a subsequence; contiguous-run length can be much smaller. Repeated equal values invalidate a purely strict increasing-or-decreasing theorem. A constant sequence has strict maximum one, although it is weakly nondecreasing throughout.

71. **Simple undirected degree labels exclude simultaneous extremes.** Degrees lie between zero and n minus one, but an isolated vertex and a universal vertex cannot coexist. Thus at most n minus one labels are used by n vertices. Loops, parallel edges or directed outdegrees change the model and require a new proof.

72. **The Ramsey star is only the first step.** In a six-vertex two-color complete graph, five incident edges force three in one color. Among the three opposite endpoints, either an edge matches that color and closes a triangle with the center, or all three edges have the other color and close a triangle themselves.

73. **Prove the small Ramsey lower bound with an actual coloring.** Color a five-cycle red and its complement blue. Both color graphs are five-cycles and have no triangle, so five vertices can avoid a monochromatic triangle. This concrete certificate establishes sharpness of the six-vertex theorem.

74. **Rectangle labels contain both column pair and color.** A row with four columns and three colors supplies a same-color column pair. There are eighteen pair-color certificates. Repeated certificates in two rows yield a monochromatic rectangle; repeating only a color without a common column pair is insufficient.

75. **Rectangle sharpness depends on a realizable one-certificate row.** When columns equal colors plus one, a row can have exactly one doubled color and all other colors once. Taking each pair-color certificate once yields an avoiding grid. For additional columns, rows can carry several certificates, so the same construction no longer proves the general bound sharp.

76. **Yes-no identification counts complete transcripts.** A depth-q binary decision tree has at most $2^q$ leaves even when questions depend on previous answers. Distinct possibilities need distinct leaves. With unrestricted truthful subset questions, a balanced tree attains the ceiling of the base-two logarithm; question restrictions can prevent that construction.

77. **Strict compression counts all shorter lengths.** Binary strings shorter than n include lengths zero through n minus one, giving $2^n-1$ outputs when the empty string is allowed. There are $2^n$ n-bit inputs. No injective lossless compressor can shorten all of them; most or average inputs require a specified distribution and are different claims.

78. **One-lie packing is a necessary bound.** For q adaptive questions, each hidden possibility produces q plus one distinguishable transcripts under zero or one lie schedules. Unique decoding makes these transcript sets disjoint, giving $N(q+1)\le2^q$. A packing inequality does not itself construct a strategy attaining its integer upper bound.

79. **Adaptive transcript sets are not automatically Hamming balls.** A lie changes later questions, so later truthful answers can also differ from those in the all-truthful run. The first differing lie position proves transcript distinctness, but not a Hamming-distance-one description. That geometric description belongs to a fixed nonadaptive question list or a separately justified code.

80. **A decoding construction is stronger than a state-count bound.** The five-card trick uses a same-suit anchor, a directed cyclic rank gap one through six, and six permutations of three remaining visible cards. Counting visible states only proves a necessary deck-size bound. The four-card variant fails because its visible ordered triples are fewer than its possible hands; no clever ordering repairs that cardinality deficit.
