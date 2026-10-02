### A complete conceptual summary

A recurrence is a domain-sensitive mathematical specification. Derive it from the calls actually executed and the resource actually measured; specify every base input and verify smaller-child progress. Equalities, upper inequalities, and asymptotic toll classes do not convey the same information. A tight conclusion needs a lower bound as well as an upper bound. Comparison with self-recursing envelopes is a strong-induction argument when coefficients are nonnegative.

Unrolling turns additive chains into sums and multiplicative chains into weighted sums. Summation factors handle variable coefficients when division is valid. Elementary characteristic roots solve homogeneous constant-coefficient equations, but initial coefficients and resonance can change the result. A complete recursion tree gives an exact cost identity when all level contributions and terminal costs are counted correctly. Substitution proves a proposed bound with one fixed set of constants and a base range; lower-order slack can make a correct guess provable.

The master theorem compares the toll with the leaf exponent and has explicit polynomial-gap and regularity conditions. At the critical exponent, logarithmic powers are classified by a power sum over depth: above negative one, add one to the log exponent; at negative one, obtain log log; below it, the positive leaves dominate. Unequal fixed ratios require a mass argument, substitution, or a suitable Akra–Bazzi theorem. Rounding affects exact answers, changes of variables must be inverted, and work, expected cost, span, and live storage need distinct models.

### Choose a method from the recurrence structure

| Structure or question | First check | Method and proof obligation |
| --- | --- | --- |
| Constant decrement | Which residue class reaches which base? | Expand the enabled chain and estimate its sum. |
| First-order multiplier | Are the multipliers nonzero on the normalization interval? | Divide by their cumulative product; restart after zero multipliers. |
| Constant-coefficient linear equation | What initial values and forcing are specified? | Use characteristic modes, resonance, and direct verification. |
| Equal fixed-ratio children | Does the toll satisfy a precise master case? | Compare to the critical exponent; count leaves and verify all hypotheses. |
| Critical power times a log power | Is the log toll defined above a safe fixed threshold? | Sum the reversed-depth log-power series. |
| Unequal fixed ratios | Is total linear mass shrinking, or is an integral theorem applicable? | Use a mass/induction proof or solve the characteristic equation and integral. |
| Floors, ceilings, offsets | Do all children become smaller? | Prove a valid envelope or substitution bound; retain terms for exact counts. |
| Nonlinear argument reduction | Which new variable simplifies the child map? | Transform the entire equation and restore the original variable. |
| Parallel or storage cost | Which calls are simultaneous and which allocations remain live? | Use the actual dependency or liveness rule rather than copying the time sum. |
| Random child size | What is the conditional cost distribution? | Average conditional costs, not merely their input sizes. |

### Specification and model rules

1. A recurrence needs a domain, a base range, and a rule for every larger admissible input before it defines a unique function.
2. Every recursive child must lie in the specified domain and be smaller than its parent; ceilings can violate this at small inputs.
3. A base threshold must cover all exceptional nonshrinking sizes, including offsets introduced by rounding or representation choices.
4. Define whether the size counts elements, digits, bits, or another quantity before assigning primitive costs.
5. Count recursive calls actually executed; two uses of one stored result do not create two independently computed subtrees.
6. A conditional selecting one child does not sum the costs of both unexecuted alternatives.
7. Repeated argument values still cost repeated execution unless memoization or another real reuse mechanism prevents it.
8. Specify worst-case, best-case, expected, or exact cost before using a recurrence derived from a particular input.
9. Replacing each child by its separate worst-case value always requires an inequality unless simultaneous attainability is justified.
10. An exact equality, an upper inequality, and an equation with an asymptotic toll represent different amounts of information.
11. An $O(n)$ toll may actually be constant, so it does not alone force the same lower bound as a $Θ(n)$ toll.
12. A matching lower bound must come from positive compulsory work, realized inputs, or a justified reverse comparison.
13. Comparison envelopes must recurse on themselves and bound the original base values and local tolls.
14. Nonnegative recurrence coefficients preserve comparison inequalities; signed linear equations need their own argument.
15. Index-based search and copy-based search may have identical comparison counts but different total time recurrences.
16. A symbol for arithmetic on arbitrarily large integers does not make that operation unit cost.

### Sums and elementary linear equations

17. An additive chain sums only the tolls at enabled steps, then adds the specified final base value.
18. For a fixed power toll above exponent negative one, additive accumulation increases the power exponent by one.
19. The reciprocal first-power toll produces a harmonic sum, so its additive accumulation is logarithmic.
20. A positive toll with power exponent below negative one has a convergent infinite sum and bounded accumulated cost.
21. A constant decrement follows one residue class; include the corresponding base value instead of pretending all indices occur.
22. A size-dependent decrement requires its own depth calculation and cannot be replaced by a constant decrement casually.
23. Multiplicative first-order expansion weights earlier tolls by the intervening multiplier product.
24. A summation factor is valid only where its divisor is nonzero; a zero multiplier resets the chain and requires restarting the normalization.
25. Compute early values to form a conjecture, then verify its initial values and recurrence algebra to establish it.
26. A nondegenerate second-order constant-coefficient recurrence uses two independent modes and two initial values; a zero last coefficient requires checking the resulting lower-order equation separately.
27. Distinct characteristic roots give independent exponential modes, while a repeated nonzero root requires an additional polynomial factor.
28. A dominant characteristic mode can have zero coefficient because of the initial values, so its root magnitude alone does not force the sequence's growth.
29. Add a particular solution to the homogeneous family when the recurrence contains forcing.
30. A forcing term coinciding with a homogeneous mode requires a resonant trial shape with an additional factor, verified by substitution.

### Tree accounting and induction

31. At ideal depth $j$, node count is $a^j$ and each node's size is $n/b^j$; multiply these with the local toll to obtain the level contribution.
32. Tree height, nodes per level, local toll, and total work are distinct quantities and must not be substituted for one another.
33. Internal levels end before the terminal depth; positive leaf costs must be counted separately using the stated base value.
34. The critical exponent $log_b a$ comes from the leaf population, not from the local toll's power.
35. For a pure-power toll, the geometric level ratio is $a/b^q$, with numerator for branching and denominator for shrinking work.
36. A geometrically decreasing level sequence sums to the root order; logarithmic depth alone does not add a logarithmic factor.
37. Geometrically increasing levels and positive leaves establish the leaf order even when the root toll is cheap.
38. Equal internal level contributions produce an extra factor proportional to the number of internal levels.
39. A fully specified level sum is a proof; unexplained diagram dots and guessed termination patterns are insufficient.
40. Unequal branches can stop at different depths, so the longest path does not establish a matching lower bound for total cost.
41. Substitution must use the same constant at every inductive application, rather than hiding a growing multiplier inside asymptotic notation.
42. A failed induction can indicate a wrong growth guess or merely missing lower-order slack; diagnose which obstruction remains.
43. Constant tolls may require a subtractive constant in a linear upper hypothesis so that branching creates enough slack.
44. A bound beginning at a large threshold must also cover the finite band of smaller child inputs it invokes.
45. A logarithmic candidate vanishes at one; use a separate base clause or a positive lower-order term before dividing or fitting constants.
46. Substituting into an upper recurrence proves only an upper bound unless a separate lower argument is supplied.

### Master cases and logarithmic boundaries

47. The leaf case requires a fixed positive polynomial gap; a reciprocal logarithm does not supply that gap.
48. The balanced classical case requires the toll to stay within positive constant multiples of the critical power.
49. The root case requires both a positive polynomial gap and a fixed regularity ratio below one.
50. Checking that the toll is larger than the critical power does not by itself verify root dominance.
51. An oscillating toll can have large children below a cheaper parent and invalidate a root-order claim despite a polynomial lower estimate.
52. Failure of a sufficient theorem hypothesis does not imply the recurrence has no solution or that its proposed conclusion is necessarily false.
53. Two exact monomial envelope recurrences can prove a tight order for a toll bounded by constant multiples of a monomial even when that toll's own regularity ratio fails.
54. In a pure-power parameter family, locate the equality threshold before assigning the regions on either side.
55. The equality threshold adds a logarithm and must not be merged with a strict-inequality case.
56. The generalized critical log-power classification requires a fixed base cutoff where its logarithmic toll is defined.
57. For critical log exponent above negative one, sum over reversed depth to add one to that log exponent.
58. At critical log exponent negative one, a harmonic depth sum yields a log-log factor.
59. Below critical log exponent negative one, the normalized series converges and positive leaf work preserves the critical power.
60. A negative log exponent does not automatically imply leaf dominance; compare it with negative one, not merely with zero.

### Rounding, unequal ratios, and resources

61. Adjacent-power sandwiches require monotonicity or another established envelope; they cannot be assumed for every recurrence.
62. Repeated floor division by an integer factor equals one floor division by its power, but the stopping-depth formula must match the actual base interval.
63. Exact merge comparison toll is size minus one for two nonempty halves; a size toll gives the same leading order but a different exact count.
64. Rounding in balanced splits affects leaf depths and lower-order periodic terms, even when the asymptotic growth remains unchanged.
65. Constant additive child offsets require explicit progress and finite-threshold checks before they can be treated as harmless.
66. For linear tolls and total child mass strictly below the parent mass, use a geometric mass bound and account for terminal leaf costs.
67. An unequal-recursion upper inequality gives a linear upper bound under the shrinking-mass condition; mandatory linear work is needed for tightness.
68. In Akra–Bazzi, preserve every child ratio and coefficient when solving the characteristic equation; an average child size is not a substitute.
69. The critical equation has a unique real root because its positive weighted expression is continuous and strictly decreasing.
70. The integral theorem requires positive bounded base values, strict shrinkage, nonnegative locally integrable tolls bounded on finite intervals, and multiplicative-interval comparability; exponentially growing or arbitrary oscillatory tolls are not automatically included.
71. The additional one in the Akra–Bazzi formula preserves the base contribution when its normalized toll integral converges.
72. Distinguish an unperturbed real-size theorem from a perturbation theorem; floors and variable offsets require a proven extension or an independent argument.
73. A fractional recurrence coefficient represents a weighted equation and cannot literally count an integer number of recursive calls.
74. A change of variables must transform both child arguments and tolls, and its final answer must be translated back to the original size.
75. A square-root reduction halves log size, a fixed-ratio reduction decreases log size by a constant, and a constant decrement decreases size itself.
76. Work sums concurrent children, whereas span follows a longest dependent chain with the actual combine span.
77. Live stack storage depends on active frames and retained allocations, not the total node population of an execution tree.
78. Memoization changes repeated-call trees into dependency graphs and can change time while leaving a long recursion chain.
79. Expected cost averages conditional costs; in general the cost at an expected size differs from the expected cost.
80. End each answer with its input domain, theorem assumptions, exact or asymptotic claim, and the independent lower or completeness argument required by the question.

### A reusable solution procedure

Identify the measured resource and admissible input sizes. Derive actual calls and local tolls, specify all base inputs, and check progress. Compute a few values to detect a modeling mistake. Choose unrolling, normalization, a verified master case, substitution, a mass argument, or a theorem with stated hypotheses. Keep constants fixed and establish a lower bound separately when needed. Restore transformed variables, check exceptional inputs, and distinguish the exact quantity from a leading asymptotic order.
