### Model-selection and examination review sheet

### Experimental contracts

1. Define the random variable before naming its law. State whether it counts successes, failures, trials, marked sample objects or arrivals over an exposure.

2. A binomial experiment has a fixed integer horizon, mutually independent trials and a common success probability. A familiar-looking coefficient does not establish these assumptions.

3. Pairwise independence does not imply a binomial law. Three pairwise independent fair bits can have only even total counts.

4. Matching the first two moments of a named law does not identify that law. Verify its support and probability structure as well.

5. A random horizon cannot ordinarily be replaced by its expected value. Doing so can preserve a mean while changing the support and variance.

6. Distinguish unconditional independence from independence conditional on a shared parameter. Mixing over that parameter can create dependence.

7. Sampling without replacement changes the success hazard after a draw. Use the remaining population, rather than repeating the initial probability.

8. Separate a success probability from an event rate. A probability is dimensionless; a rate needs a time or exposure unit.

### Bernoulli and binomial counts

9. A Bernoulli variable has support zero and one, mean $p$ and variance $p(1-p)$. Every positive integer power equals the variable itself.

10. Bernoulli variance is at most one quarter. A variance below this maximum can correspond to two reflected success probabilities.

11. If $0\le X\le1$ and $E[X]=E[X^2]$, nonnegativity of $X(1-X)$ forces X to be Bernoulli almost surely. The interval assumption is essential.

12. The binomial mass is $\binom nk p^k(1-p)^{n-k}$ on integers zero through n. The coefficient counts distinct success-position sets.

13. A binomial variable has mean $np$ and variance $np(1-p)$. Zero trials, zero success probability and certain success are legitimate constant-law boundaries.

14. For positive mean and nondegenerate variance, moment recovery gives $p=1-v/\mu$ and $n=\mu/p$. The recovered n must be an integer.

15. A binomial adjacent-mass ratio is $(n-k)p/[(k+1)(1-p)]$. Locate its crossing of one to identify modes and ties.

16. For $0<p<1$, a noninteger $(n+1)p$ gives the single mode $\lfloor(n+1)p\rfloor$. If it is an integer, that integer and its predecessor tie.

17. The probability of an even binomial count is $[1+(1-2p)^n]/2$. Its PGF at minus one gives even probability minus odd probability.

18. For a fair even-sized count, the probability strictly below the midpoint is half the probability left after removing the central atom.

19. Complementing a binomial count changes its success probability to $1-p$. A biased law is not generally symmetric around its mean.

20. Given k total common-probability successes among n trials, their positions form a uniform k-subset. Counts in a sub-block are hypergeometric.

21. Independent qualification with probability p followed by independent passing with probability a produces per-object success probability $pa$. Combine the stages before identifying the final count.

22. Counts of competing labels at a fixed horizon are usually negatively correlated. Their binomial marginals do not imply independent counts.

23. Independent unequal-probability trials produce a Poisson-binomial count with PGF $\prod_i(1-p_i+p_i z)$. The ordinary binomial formula is generally inapplicable.

24. The heterogeneous-count variance is $\sum_i p_i(1-p_i)$. For a fixed average success probability, it is at most the same-mean binomial variance.

25. A shared random probability produces variance $n\bar p(1-\bar p)+n(n-1)Var(P)$. Drawing a fresh independent probability each trial is a different model.

26. Derivatives of a count PGF at one give falling-factorial moments. Convert those moments into ordinary powers before calculating variance or higher raw moments.

### First-success waiting

27. A positive geometric variable counts trials through the first success and has mass $p(1-p)^{t-1}$ at positive t.

28. A failure-based geometric variable subtracts one from the positive wait. Its support starts at zero, its mean is $(1-p)/p$, and its variance remains $(1-p)/p^2$.

29. Positive geometric survival is $P(T>m)=(1-p)^m$ for nonnegative integer m. The distinction between greater-than and greater-than-or-equal changes the exponent.

30. Convert real thresholds into admissible integer endpoints before applying a discrete survival formula. Fractional exponents do not directly count integer waiting outcomes.

31. Positive geometric memorylessness gives $P(T>m+n\mid T>m)=P(T>n)$. The conditioning event must have positive probability.

32. Conditional residual waiting has mean $1/p$, but the conditional total wait after m failures has mean $m+1/p$.

33. The integer survival multiplicative identity, together with positive support, characterizes a geometric law. A single mean or one tail value does not.

34. For changing independent hazards, survival is a product of failure probabilities. Almost-sure success does not necessarily imply finite expected waiting.

35. A shared hidden success probability usually destroys unconditional memorylessness. Past failures reweight its posterior distribution.

36. Capping at c moves every wait at or beyond c onto the endpoint. Its endpoint mass is $P(T\ge c)$, not merely $P(T=c)$.

37. Truncating to successes by c discards other attempts and renormalizes all retained masses by $P(T\le c)$. It differs from capping.

38. Coding unresolved attempts as zero creates a finite observed law. Its zero label is not automatically a geometric failure count.

39. For a positive integer variable, the tail-sum mean is $\sum_{m\ge0}P(T>m)$. This identity also diagnoses infinite expectations.

40. Independent discrete waiting clocks can tie. Their minimum has product survival, while their maximum has union survival.

41. For independent positive geometric clocks, the tie probability is $p_1p_2/[1-(1-p_1)(1-p_2)]$. A continuous-race argument would lose this atom.

42. Pointwise, the minimum plus the maximum equals the sum of two waits. This expectation identity does not require independence, although the product-survival calculation does.

### Multiple successes and finite-population waits

43. A total-trial negative-binomial wait through r successes has support r onward and mass $\binom{t-1}{r-1}p^r(1-p)^{t-r}$.

44. The final trial in a stopped success wait is forced to succeed. Replacing its coefficient with $\binom tr$ includes invalid arrangements.

45. The failure-based negative-binomial variable is the total wait minus r. Its mean is $r(1-p)/p$ and its variance is $r(1-p)/p^2$.

46. The total-trial negative-binomial mean is $r/p$. It can be derived by adding independent inter-success geometric increments.

47. Count–wait duality states $P(T_r\le n)=P(Bin(n,p)\ge r)$. It identifies events in a shared sequence, not the two random variables.

48. Independent negative-binomial counts with the same success probability add their success targets. Different probabilities generally prevent closure in the same family.

49. Failure-count adjacent ratios equal $(1-p)(f+r)/(f+1)$. Check the crossing of one and valid support before assigning modes.

50. A noninteger shape extension defines a valid analytic count law for appropriate parameters, but it is not literally the number of trials through a fractional success target.

51. A hypergeometric count uses a uniform sample without replacement. Its PMF is $\binom Kk\binom{N-K}{n-k}/\binom Nn$.

52. Hypergeometric effective support is $\max(0,n-N+K)$ through $\min(n,K)$. Check both marked and unmarked pool constraints.

53. Hypergeometric mean is $nK/N$, but its variance differs from replacement sampling by the finite-population factor $(N-n)/(N-1)$ for $N>1$.

54. If the whole population is drawn, the marked count is constant. At $N=1$, use that direct law rather than evaluating an undefined variance ratio.

55. The complement of a uniform sample is uniform. The number of marks left behind has the corresponding complementary-sample hypergeometric law.

56. Hypergeometric adjacent ratios use both depleted pools. A mode formula must be checked for ties and clipped to the effective support.

57. A finite-population rth-mark position has bounded support r through $N-K+r$. It is negative hypergeometric, not a constant-hazard negative-binomial wait.

58. The finite rth-mark PMF counts r minus one marks before its endpoint and K minus r afterward. Its denominator counts all K-position subsets.

59. Uniform mark positions correspond bijectively to uniform weak compositions of the unmarked gaps. Gap symmetry yields the mean wait $r(N+1)/(K+1)$.

60. Gap variables are exchangeable but dependent because their sum is fixed. Include their negative covariance when calculating a partial-gap sum variance.

61. A finite-population wait–count event uses a hypergeometric count at the fixed horizon. Changing it to binomial would assume replacement.

### Poisson counts, conditioning and approximation

62. A Poisson count has mass $e^{-\lambda}\lambda^k/k!$ at nonnegative integer k. Its mean and variance both equal lambda.

63. Equal mean and variance do not characterize a Poisson law. A two-point non-Poisson law can share those moments.

64. A homogeneous rate over exposure t produces parameter $\lambda=\rho t$. Convert units before multiplying the rate and duration.

65. A positive finite interval in a Poisson process is not exactly Bernoulli. Multiple events have nonzero probability, even though their small-interval probability is of smaller order.

66. Poisson adjacent ratios are $\lambda/(k+1)$. A positive integer lambda gives two modes, lambda minus one and lambda; a noninteger lambda gives its floor.

67. Poisson falling-factorial moments are powers of lambda. Its ordinary third and fourth moments need the lower-order polynomial corrections.

68. Independent Poisson counts add their parameters. A scaled copy instead changes lattice spacing and multiplies variance by the square of its scale.

69. Given the sum of independent Poisson counts, their allocation is binomial or multinomial with probabilities proportional to their parameters.

70. Independent labeling of a Poisson total creates independent Poisson category counts. Given a fixed total, those category counts are dependent.

71. A random-intensity mixture has variance equal to its mean plus the variance of its intensity. A shared rate can also make different observations dependent.

72. Conditioning a Poisson law on positivity requires renormalizing its positive atoms. It differs from size bias, which multiplies masses by their counts.

73. A size-biased positive-parameter Poisson variable equals one plus a Poisson variable. Verify the sampling mechanism before using this identity.

74. Rare independent Bernoulli counts can be approximated by a Poisson law with parameter $\sum_i p_i$. A coupling gives event-probability error at most $\sum_i p_i^2$.

75. An absolute error bound does not imply a relative accuracy guarantee for a tiny event. State which scale the approximation controls.

76. Fixed-k pointwise limits do not by themselves justify moving-index or uniform approximations. Such claims need a separate argument.

77. Small individual probabilities and a matched mean are insufficient when rare-event indicators are dependent. A shared indicator gives a direct counterexample.

78. A finite binomial count cannot exceed its horizon, even when an unbounded Poisson approximation assigns mass there. Exact support takes precedence in exact questions.

### Calculation and final checks

79. Use exact rational arithmetic for small finite laws, log-mass formulas for large factorials, and stable log-one-plus and exp-minus-one routines for tiny tails. Handle endpoint laws first.

80. Finish every answer by checking support, total probability, parameter domains, units, conditioning direction and strict threshold meaning. A plausible number is not a substitute for a valid experiment.

81. A variable uniform on consecutive integers a through b has mean $(a+b)/2$ and variance $((b-a+1)^2-1)/12$. Count the endpoints when determining the support size.

82. A nonzero affine map of uniform integer atoms preserves equal probabilities but can change lattice spacing. Missing intermediate integers have probability zero.

83. A conditioning event of zero probability does not define an ordinary event-ratio conditional law. A limit from nearby models is a separate construction.

84. A displayed finite prefix of an infinite count law must retain an explicit omitted-tail probability. Renormalizing that prefix changes the law to a truncated one.
