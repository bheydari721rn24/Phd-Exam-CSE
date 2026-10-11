# Final rules for second-moment examination reasoning

1. Identify the random variable before calculating its variance. A die face, a success indicator, and a success count have different laws even when they arise from the same experiment.

2. Check that all masses are nonnegative and sum to one. A moment calculation using unnormalized weights is not a population variance until the weights are normalized.

3. Use the actual support in every integral. A factorized expression on a triangular support does not establish independence because the support indicator does not factor.

4. Assume finite second moments before using finite covariance and correlation algebra. Finite means alone do not ensure finite variances or integrable dependent products.

5. The ordinary expectation requires absolute integrability for signed variables. A symmetric principal value for a Cauchy integral cannot be used as its mean.

6. Variance is $E[(X-E[X])^2]$. Signed displacements cancel in expectation and cannot measure spread by themselves.

7. In $E[X^2]-E[X]^2$, the first term squares each outcome before averaging, whereas the second averages first and then squares. Their order of operations is essential.

8. Probability masses are not squared in a raw second moment. The correct finite formula uses $p_ix_i^2$, not $p_i^2x_i$ or $p_i^2x_i^2$.

9. A negative exact variance proves inconsistency in the supplied moments or the calculation. Do not interpret it as negative standard deviation.

10. Variance is in squared units, standard deviation in original units, covariance in product units, and correlation has no units. Check dimensions to reject malformed options.

11. Zero variance means constancy almost surely. It need not mean constancy at every probability-zero point.

12. A deterministic shift changes the mean but leaves variance unchanged. A random shift requires its own variance and covariance terms.

13. Affine scaling multiplies variance by the square of its coefficient. Standard deviation uses the absolute value of that coefficient.

14. A zero scaling produces a constant and makes its Pearson correlation with another variable undefined. Do not cancel zero standard deviations.

15. The mean minimizes squared error over constant predictions. Using a different center adds the square of the prediction bias.

16. A population supported on $[a,b]$ has variance at most $(b-a)^2/4$. A uniform density has only one third of that bound.

17. With a specified mean, the sharper supported-law bound is $(b-\mu)(\mu-a)$. Its equality law uses only the two endpoints.

18. An independent-copy difference gives twice the variance. Repeating the same random variable makes that difference zero, so equality of distributions alone is insufficient.

19. Nonlinear transformations require moments of the transformed law. Mean and variance of $X$ do not generally determine variance of $X^2$.

20. A product variance can require squared joint products. Zero covariance of its factors does not justify factoring $E[X^2Y^2]$.

21. Covariance centers both variables about their own means. Substituting a mean from a different example changes the quantity being integrated.

22. The raw covariance formula is $E[XY]-E[X]E[Y]$. Compute the mixed moment from the joint law, not from marginal laws alone.

23. Covariance is symmetric and bilinear in deterministic coefficients. Translation disappears from either argument.

24. A variable's covariance with itself equals its variance. A variable is not independent of itself unless it is degenerate.

25. Sum variance contains twice each unordered pair covariance. An ordered-pair summation already includes both directions and must not be doubled again.

26. Squared coefficients belong to variance diagonals. Cross terms use the product of the two coefficients and retain its sign.

27. For $X-Y$, the covariance correction is negative; for $X+Y$, it is positive. The correction can itself be negative when covariance is negative.

28. Pairwise uncorrelatedness suffices for finite weighted-sum variance additivity. It does not establish mutual independence or determine the complete sum law.

29. Independence implies zero covariance when the required moments exist. Zero covariance is only a second-moment statement and does not imply independence in general.

30. Symmetric odd moments can vanish despite deterministic nonlinear dependence. Test the joint law directly instead of inferring independence from a canceled covariance.

31. For indicator variables, independence can be checked by comparing intersection probability with the product of their probabilities. For general variables, one equality of mixed means does not establish factorization.

32. Positive covariance describes an averaged centered association. It does not require every outcome or every sample pair to move in the same direction.

33. Normalize covariance by the product of standard deviations only when both are finite and positive. A constant variable has defined zero covariance but undefined Pearson correlation.

34. Correlation lies in $[-1,1]$ by the nonnegativity of every centered squared residual. Values outside that interval certify infeasible moments.

35. Perfect nondegenerate correlation means an affine relation almost surely. Its slope magnitude is a ratio of standard deviations, not variances.

36. A negative change of units reverses correlation's sign. Two negative changes preserve its sign, while positive changes preserve it individually.

37. The variance of a sum is bounded by squared sum and squared difference of standard deviations. These bounds do not automatically construct a coupling with arbitrary fixed marginal laws.

38. Zero covariance gives independence for a jointly Gaussian pair. Normal marginal distributions alone do not supply joint Gaussianity.

39. A Gaussian density with a denominator involving $\sqrt{1-\rho^2}$ requires $|\rho|<1$. At perfect correlation the joint law is singular and needs a different representation.

40. Express overlapping sums in shared primitive variables. Only common primitives contribute covariance when distinct primitives are independent, and shared weights must be multiplied.

41. An indicator equals its square, so its variance is $p(1-p)$. Confusing a count indicator with a numerical measurement defeats this shortcut.

42. Indicator covariance is intersection probability minus product probability. Mutually exclusive positive-probability events have negative covariance and are not independent.

43. For a count, list intersecting event pairs before summing covariance. Independence of primitive trials does not make overlapping derived events independent.

44. Distinguish ordered and unordered pair counts in occupancy, adjacent-run and permutation problems. The variance formula's factor two must match the chosen convention.

45. Random-permutation fixed-point variance is one for at least two labels. For one label the count is constant, so its variance is zero.

46. Pairwise independence can give a binomial-like count variance without giving a binomial count distribution. Use mutual independence when identifying the full binomial law.

47. Empty-box indicators can be dependent even when ball destinations are independent. Compute the probability that both selected boxes are empty.

48. Sampling without replacement creates negative covariance between success indicators. The replacement binomial variance omits the finite-population correction.

49. The without-replacement correction is $(N-n)/(N-1)$ with population size greater than one. Handle $N=1$ directly instead of dividing by zero.

50. Sampling the entire population makes a success count deterministic. Its covariance corrections cancel the diagonal variance terms exactly.

51. Population variance conventions using denominators $N$ and $N-1$ differ by a factor. Convert the convention before applying a finite-population mean formula.

52. The variance of an independent-observation average decreases by the sample size. Repeating the same realization does not decrease its variance.

53. Shared additive noise remains in an average. Only the independent measurement-specific component receives the usual inverse-sample-size reduction.

54. A fixed negative pair covariance across many observations must satisfy a positive-semidefinite constraint. It cannot be replicated for arbitrarily many observations merely because each pair is feasible.

55. A random sum with independent count has both expected conditional variance and variance of conditional mean. Count variation matters whenever the increment mean is nonzero.

56. An independent zero-mean random sum can have finite variance under a finite expected count even when the count variance is infinite. Derive the zero between-count term directly.

57. A stopping count dependent on observed increments is not covered by the independent-count random-sum formula. Conditioning can alter the increment laws.

58. Conditional variance centers about the conditional mean. It is a function of the conditioning information, whereas its expectation is a scalar.

59. In total variance, averaged within-group variance must be supplemented by variance of group means. The two terms are nonnegative and have different meanings.

60. Conditioning on a continuous value uses a conditional density or an appropriate conditional-expectation version. It does not divide by the probability of a singleton.

61. Conditional independence can coexist with unconditional dependence caused by a common latent group. Apply the law of total covariance before discarding association.

62. A constant conditional mean does not imply independence. Conditional variances or higher moments may still depend on the conditioning value.

63. The conditional-mean residual is orthogonal to square-integrable functions of the conditioning information. Orthogonality is weaker than independence.

64. Conditional expectation minimizes squared prediction error among all permitted measurable predictors. The best affine predictor may differ when the conditional mean is nonlinear.

65. More information cannot increase the minimum expected squared prediction error. This result compares expected risks, not pointwise ordering of every conditional variance.

66. The best affine slope is covariance divided by predictor variance. Its intercept adjusts the means, and its residual variance is $Var(X)(1-\rho^2)$ in the nondegenerate pair case.

67. Unrestricted optimal averaging weights can be negative or above one. A convex-weight requirement must be imposed after deriving the unconstrained minimizer.

68. If the averaging denominator equals zero, the centered difference is deterministic and the variance is flat in the weight. Do not apply the ordinary division formula.

69. A covariance matrix is symmetric and positive semidefinite. Every proposed coefficient vector must produce a nonnegative variance quadratic form.

70. Pairwise correlation bounds are insufficient in three or more dimensions. Check the complete matrix, including determinant or eigenvalue constraints as appropriate.

71. A zero-variance covariance-matrix row must be zero. A singular covariance matrix may instead represent a deterministic linear relation among nonconstant components.

72. Under a fixed affine vector map, covariance becomes $A\Sigma A^T$. Matrix dimensions and transpose placement are part of the formula.

73. Markov's inequality requires a nonnegative variable and a positive threshold. A mean-zero signed variable cannot be inserted into its usual bound.

74. Chebyshev is a bound derived from second moments, not an exact probability or a Gaussian assumption. Clip a probability upper bound at one when interpreting it.

75. Check whether the tail event includes its threshold. Endpoint atoms can make strict and non-strict events differ and change whether a sharp bound is attained.

76. Cantelli provides a one-sided bound using the mean and variance. Its attaining two-point law balances an upper threshold atom with a lower atom fixed by the variance.

77. An iid sample-size calculation from Chebyshev is a sufficient moment-based guarantee. It is not necessarily the smallest actual sample size for a known distribution.

78. Random-walk variance concerns the full ensemble. Root-mean-square displacement is not generally expected absolute displacement, and a single trajectory proves neither.

79. Probability-generating second derivatives give factorial second moments; add the first moment before subtracting the squared mean. Moment-generating second derivatives give raw second moments directly when the differentiability conditions hold.

80. Empirical variance, unbiased sample variance and sample-mean variance are distinct. In streaming updates, use the old mean in the first displacement and the updated mean in the second, then apply the denominator appropriate to the stated quantity.
