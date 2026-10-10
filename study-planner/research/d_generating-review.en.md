1. State whether a series is an OGF, EGF, or PGF before extracting a count. The same expression can represent different sequences under different normalizations.

2. The exponent records the chosen size; the coefficient records a count or weight. Combining equal monomials adds their coefficients, not their exponents.

3. Coefficient extraction returns a scalar. The monomial $a_nx^n$ is the term, whereas $[x^n]A$ is only $a_n$.

4. Define negative-index coefficients to be zero for ordinary power series. Introducing negative powers instead changes the ambient domain to Laurent series.

5. Formal addition and multiplication are valid without numerical convergence because every requested coefficient uses finite sums.

6. Ordinary multiplication is convolution: sum products over all index pairs whose sum is the target. It is not coefficientwise multiplication.

7. The multiplicative identity is the series 1,0,0,... . The all-ones sequence is a different series, namely $1/(1-x)$.

8. Over a field, a formal series has an inverse exactly when its constant coefficient is nonzero. Over a general ring that coefficient must be a unit.

9. Reciprocal coefficients are determined recursively by the denominator's coefficients up to the target degree. This provides an exact alternative to roots or numerical expansion.

10. The variable has no inverse in the ordinary power-series ring. Dividing a numerator already divisible by the variable is a valid shift of that particular numerator.

11. A truncated series prefix does not assert that later coefficients vanish. State the known degree whenever a computation depends on truncation.

12. A product coefficient of degree at most $N$ needs only factor coefficients through $N$ when all exponents are nonnegative.

13. A left shift by $m$ may require the original coefficient at degree $N+m$. It reduces the available precision of a known prefix.

14. Multiplication by $x^m$ delays every coefficient by $m$ and inserts $m$ initial zeros. Apply the shift to every index in a coefficient formula.

15. Before a left shift, subtract the complete removed initial polynomial. Omitting it introduces unwanted negative powers.

16. Replacing $x$ by $cx$ multiplies the degree-$n$ coefficient by $c^n$. Scaling the series by a constant instead multiplies every coefficient by the same constant.

17. Replacing $x$ by $-x$ alternates signs. Averaging it with the original series filters even exponents; subtracting it filters odd exponents.

18. Filtering a residue class retains original exponents. Compressing a subsequence creates a new index and a different OGF.

19. A root-of-unity filter projects onto one congruence class because a finite geometric sum vanishes on all other classes.

20. A complex root-of-unity formula assumes an appropriate coefficient field and invertible filter modulus. Do not carry its division unchanged into incompatible modular arithmetic.

21. Formal differentiation shifts an OGF index and multiplies by the new original index. The coefficient of $x^n$ in $A'$ is $(n+1)a_{n+1}$.

22. The Euler operator $xD$ preserves the index and weights its coefficient by $n$. This is the correct operation for an index-weighted sequence.

23. The operator $x^kD^k$ produces falling-factorial weights. It differs from repeating $xD$ $k$ times.

24. The product rule accounts for the extra $xA'$ in $(xD)^2A=xA'+x^2A''$. Omitting this term changes squares into falling squares.

25. Over rational coefficients, formal integration divides by positive integers and fixes an integration constant. The same operation is not universally available in positive characteristic.

26. A polynomial index weight applied to a rational OGF remains rational. Repeated Euler differentiation gives a constructive proof.

27. Divide by $1-x$ to take an inclusive prefix sum. The original constant appears in every prefix; it is not removed automatically.

28. Multiply by $1-x$ for a backward difference with the boundary $a_{-1}=0$. State that boundary when interpreting the first coefficient.

29. Repeated prefix summation creates higher inverse powers of $1-x$. Its coefficients contain binomial weights, not only unweighted sums.

30. The OGF binomial transform includes both a substitution and a prefactor: $B=(1-x)^{-1}A(x/(1-x))$. Dropping either part gives a different transform.

31. Inverting a binomial transform requires alternating signs depending on the index difference. A small two-index check is useful for detecting the sign convention.

32. The coefficient of $(1-cx)^{-k}$ is $c^n\binom{n+k-1}{k-1}$ for nonnegative $n$ and positive integer $k$.

33. A numerator shift changes the target degree, the exponential power, and the binomial coefficient together. Adjusting only one of them is incorrect.

34. Generalized binomial coefficients can be negative or rational. They are not the same as ordinary combinatorial coefficients with impossible targets defined as zero.

35. A normalized fractional power is defined by its constant and formal differential equation. State the chosen normalization before selecting its branch.

36. A logarithmic series has zero constant and needs its own extraction rule. Partial fractions apply only to rational functions.

37. Harmonic numbers arise by prefix summing the positive-index sequence $1/n$. The zero-index coefficient of that sequence is defined separately as zero.

38. Check the denominator constant before expanding a rational expression as an ordinary series. A denominator vanishing at zero can require cancellation or Laurent terms.

39. Cancel common numerator and denominator factors before identifying pole multiplicities or growth. Removable poles do not contribute coefficients.

40. Polynomial division separates an exact finite prefix from a proper rational part. The finite prefix may be ignored for eventual growth, but never for exact initial values.

41. A pole at $\rho$ corresponds to exponential base $1/\rho$. The pole location and sequence base are reciprocals, not equal numbers.

42. A pole of multiplicity $m$ contributes index polynomials of degree at most $m-1$. The surviving coefficients determine which degrees actually occur.

43. For a repeated pole, include every denominator power through its multiplicity in partial fractions. One term alone does not span the full proper rational contribution.

44. To evaluate a partial-fraction coefficient at a pole, remove its zero factor first. Substituting into the original singular quotient is undefined.

45. Complex conjugate poles can combine to real coefficients and periodic behavior. Preserve all surviving contributions before interpreting the sequence.

46. A recurrence sum must begin at the specified first valid index. Extending it to earlier indices without correction changes the problem.

47. Every lagged sum has its own removed initial prefix. The amount removed depends on both the starting index and the lag.

48. A forcing series must reflect when the forcing starts. Constant forcing from index $k$ contributes $x^k/(1-x)$, not the unshifted inverse.

49. An eventual recurrence may leave independent finite prefix values. Their polynomial correction is part of its exact OGF.

50. Resonance appears as a potentially repeated denominator factor. Cancel the numerator before deciding whether the extra polynomial index factor survives.

51. Fixed-lag constant-coefficient recurrences with rational forcing produce rational OGFs. Variable coefficients may instead produce differential equations.

52. Binomial-sum recurrences often simplify as EGF products or substitutions. If a current-index term appears on both sides, prove coefficient uniqueness after moving it left.

53. A counting product requires a unique reconstruction from independent components with additive size. A product of overlapping choice classes can overcount.

54. A disjoint union produces an OGF sum. If alternatives overlap, first separate them or subtract their intersection with an explicit argument.

55. Unrestricted identical copies of weight $w$ contribute $(1-x^w)^{-1}$. Zero-or-one copies contribute $1+x^w$.

56. A lower multiplicity bound contributes a leading monomial. Remove lower bounds before applying upper-bound inclusion-exclusion.

57. Equal upper bounds produce a binomial count of violated boxes. Unequal bounds require different subset-dependent shifts.

58. Under the combinatorial zero convention, a negative residual target contributes zero. Do not replace that zero by a generalized negative-top binomial coefficient.

59. Ordered coin strings use a sequence inverse, while unordered change uses a product of multiplicity factors. Identical denominations alone do not determine which model is intended.

60. The loop order in dynamic programming specifies whether reuse or ordering is allowed. A correct arithmetic update with the wrong loop order counts different objects.

61. Distinguishable types of equal weight need separate choice factors when their quantities matter independently. Merging them by numeric weight erases information.

62. An ordered-sequence construction needs positive component size for local finiteness. Infinitely many zero-size paddings cannot be counted by finite coefficients.

63. A separate component-number marker can make zero-size components legitimate in a two-variable series. Extract the marker coefficient before discarding that restriction.

64. Exactly $k$ positive ordered parts use the $k$th power of their component series. No division by $k!$ is justified when positions remain distinguishable.

65. Integer partitions are unordered multiplicity vectors, not compositions. Their OGF product over part sizes reflects that distinction.

66. An infinite partition product is formally legitimate because only finitely many factors affect any target degree. This is separate from numerical convergence of the product.

67. Ferrers conjugation interchanges number of parts and largest part. Exactly $k$ positive parts require a numerator $x^k$ over the bounded-largest-part denominator.

68. Distinct $k$-part partitions add a staircase of $k(k-1)/2$ beyond the positive-part offset. Their minimum total is $k(k+1)/2$.

69. Odd-part and distinct-part partitions have identical total counts, but the standard cancellation does not preserve number of parts. Parameter markings need a new argument.

70. A Durfee decomposition has a unique square size, an independent arm, and an independent leg. Include the empty square when counting the empty partition.

71. Catalan constructions must specify whether size counts pairs, vertices, or internal vertices. These conventions can shift the coefficient index.

72. The Catalan branch is chosen because its numerator is divisible by the variable and its quotient has the required constant. Direct substitution into its uncanceled quotient is not the formal argument.

73. Standard formal composition of an infinite outer series requires a zero-constant inner series. A polynomial outer expression does not need that restriction.

74. Formal coefficient inversion needs a uniquely invertible zero-constant recursive solution and nonzero linear coefficient. Its factor $k/n$ is essential when extracting a power of that solution.

75. EGF multiplication includes label allocation through binomial coefficients. To recover counts, multiply ordinary extracted coefficients by $n!$ exactly once.

76. Dividing an ordered component product by $k!$ requires a free ordering of nonempty disjoint label blocks. Empty indistinguishable components invalidate that simple divisor.

77. Labelled set construction uses an exponential; labelled ordered blocks use a sequence construction; cycles use their rotational divisor. These are distinct outer structures.

78. Differentiating an EGF introduces one new distinguished label, whereas multiplying the derivative by the variable marks an existing label. State which interpretation is used.

79. A parameter's second derivative gives its falling-factorial second moment. Add the first moment before computing variance, and define both the statistic and probability model.

80. Numerical boundary moments and asymptotic claims require additional conditions beyond formal coefficient algebra. Audit finite moments, cancellations, residue classes, and the exact answer's domain before using them.
