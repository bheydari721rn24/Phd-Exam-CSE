1. **Signed contributions and the balance point.** Validate probability weights, keep negative contributions signed, and distinguish $E[|X|]$ from $|E[X]|$ before simplifying any expression. **Worked check.** Multiply each value by its own mass: $E[X]=-2/5+1/2+12/10=13/10$. Absolute values instead give $E[|X|]=2/5+1/2+12/10=21/10$.

2. **Recovering an unknown mass.** Use normalization to remove one unknown, solve the mean equation, and then check every mass; a negative formal solution rejects the proposed law. **Worked check.** Let the mass at two be $a$, so the mass at seven is $3/4-a$. The mean equation is $-3/4+2a+7(3/4-a)=3$, or $9/2-5a=3$.

3. **Outcome weights versus atom weights.** Merge probabilities over fibers of the measurement map; do not replace their sum with a uniform weight over distinct labels. **Worked check.** Using outcomes, the weighted sum is $2/2+2/3+8/6=3$. Using distinct atoms, the value two receives both of the first two outcome weights, totaling $5/6$, while eight has mass $1/6$.

4. **Mean outside the support but inside its hull.** A mean is a convex combination; equality with a support endpoint forces concentration at that endpoint when all remaining values lie strictly on one side. **Worked check.** Write $p=P(X=10)$. The mean is $10p$, with $0\le p\le1$.

5. **A fair entry fee.** Separate gross awards, returned stakes, and entry costs; subtract a fixed fee once rather than weighting it only on losing outcomes. **Worked check.** There are thirty-six equally likely ordered outcomes and only one has sum two. The gross payoff mean is $240/36+12(35/36)=660/36=55/3$.

6. **An infinite mean with a tiny omitted mass.** Bound omitted value-times-mass contributions, not merely omitted probability; normalization and finite expectation are separate requirements. **Worked check.** The masses sum to one by the geometric series. Each included atom contributes $2^k2^{-k}=1$, so the partial mean is $r$.

7. **Symmetry that does not define a mean.** Check the positive and negative parts before using symmetry on an infinite signed support; both divergent parts make the mean undefined. **Worked check.** The total probability is $\sum_{k\ge1}2^{-k}=1$. Each positive contribution to the mean is one half, so the positive-part mean diverges.

8. **Moment existence thresholds.** For a power-law tail, multiplying by $k^r$ changes the exponent; test the resulting series rather than the normalization series alone. **Worked check.** Normalization uses the convergent series $\sum k^{-a}$, hence $c$ is positive and finite. The mean is $c\sum k^{1-a}$, a positive series that converges precisely when $a-1>1$, or $a>2$.

9. **A nonlinear square.** Evaluate raw moments first, then apply polynomial linearity; replacing $E[X^2]$ by $(E[X])^2$ removes the entire spread term. **Worked check.** LOTUS gives $E[X^2]=4/5+1/2+16(3/10)=61/10$. Subtract the square of the mean, not its absolute mean: $Var(X)=61/10-169/100=441/100$.

10. **A many-to-one transformation.** A noninjective transform merges probabilities, not values alone; compute its mean directly from the original law or from correctly aggregated fibers. **Worked check.** Squaring maps the original atoms into zero, one, and four. Their masses are $1/5$, $1/5+1/5=2/5$, and $1/10+3/10=2/5$.

11. **Reciprocals and Jensen's gap.** For positive variables, reciprocal averaging lies above the reciprocal mean; first check positivity, domain, and integrability. **Worked check.** Direct weighting gives $E[X]=5/2$ and $E[1/X]=(1+1/4)/2=5/8$. The reciprocal of the mean is $2/5$, so the gap is $5/8-2/5=9/40>0$.

12. **A clipped payoff.** Evaluate piecewise functions at every supported value; crossing a threshold invalidates a single affine replacement. **Worked check.** The payoff is zero at $-2$ and one, and equals three at four. Its expectation is therefore $3(3/10)=9/10$.

13. **Perfect dependence still permits linearity.** Dependence does not obstruct a finite sum mean; it does obstruct an unjustified product factorization. **Worked check.** Both component means are zero. Linearity therefore gives $3(0)-2(0)+5=5$, even though $Y$ is completely determined by $X$.

14. **Random coefficients are not constants.** A symbol named as a coefficient is not necessarily deterministic; establish constancy or a valid joint-law argument before taking it outside expectation. **Worked check.** Since an indicator satisfies $X^2=X$, the random product $AX$ is just $X$, and its expectation is $2/5$. The product of the separate means is $4/25$, leaving a difference of $6/25$.

15. **Identical marginals, different products.** Do not infer dependence-sensitive quantities from marginals alone; construct a joint coupling when the question concerns products or simultaneous events. **Worked check.** The separate means are always one half, so the sum mean is one in all three couplings. Independently, both equal one with probability one quarter, giving product mean $1/4$.

16. **Zero product gap without independence.** Equality of one product mean is weaker than independence; a single joint atom violating factorization refutes independence. **Worked check.** The odd symmetry gives $E[X]=0$ and $E[XY]=E[X^3]=0$, while $E[Y]=2/3$. Thus the product identity holds.

17. **Nonidentical trial probabilities.** Marginal probabilities suffice for a finite count mean; they need not identify a binomial distribution or its variance. **Worked check.** Let $I_i$ indicate success at trial $i$ and define $N=\sum_{i=1}^5I_i$. This equality holds for every outcome regardless of dependence.

18. **Weighted error costs.** Establish how simultaneous events are charged before using weighted indicators; maximum, union, and cumulative costs have different decompositions. **Worked check.** The charging rule gives the exact random cost $C=8I_1+3I_2+12I_3$. Its mean is $8/4+3/3+12/6=5$.

19. **Expected fixed points.** In uniform permutations, impose constraints by counting remaining free images; use first-order constraints for means and joint constraints for higher moments. **Worked check.** Each specified label is fixed in $3!$ of $4!$ permutations and therefore with probability $1/4$. Summing four fixed-point indicators gives expected count one.

20. **Partial and weighted permutation matches.** Uniform image probabilities apply to fixed targets; outcome-dependent target selection changes the event and can make a supposed match automatic. **Worked check.** For any checked position, its image is uniform among ten labels, so a prescribed target match has probability $1/10$. The expected count of the three matches is $3/10$.

21. **Fixed-point second moment.** Square a count by separating diagonal indicators from distinct pairs; pair probabilities usually require their own combinatorial calculation. **Worked check.** Expand $F^2=\sum_iI_i+2\sum_{i<j}I_iI_j$. The first expectation is one.

22. **Record counts and initialization.** Read initialization and the precise charged operation; subtracting an initial assignment can change a record-count answer by one. **Worked check.** With infinity initialization, position $i$ updates the minimum when it is smallest among the first $i$ values, an event with probability $1/i$. The mean is $H_5=1+1/2+1/3+1/4+1/5=137/60$.

23. **Harmonic bounds as an asymptotic justification.** Derive an approximation through bounds or a stated limit; an asymptotic equivalent must not replace a small-input exact answer. **Worked check.** The decreasing function $1/x$ satisfies $\int_k^{k+1}dx/x\le1/k$, so summing gives the lower bound. For $k\ge2$, $1/k\le\int_{k-1}^kdx/x$; retain the first harmonic term separately to obtain the upper bound.

24. **Inversions in a random ordering.** Specify whether pairs are ordered, then use the symmetry of the two relative orders; do not multiply pair counts twice. **Worked check.** An inversion is an unordered position pair $i<j$ whose values appear in decreasing order. Each of the fifteen position pairs has either ordering with probability one half, by swapping the two relevant values.

25. **Empty and occupied bins.** Distinguish independence of placements from dependence of occupancy events; each role belongs to a different step of the argument. **Worked check.** A specified bin is avoided by each ball with probability $2/3$. Independence between ball placements makes its empty probability $(2/3)^4=16/81$.

26. **Nonuniform occupancy.** Keep nonuniform bin weights inside the sum; a uniform formula with an average probability discards the needed powers. **Worked check.** For bin $j$, the occupied probability is $1-(1-p_j)^2$. The three probabilities are $3/4,5/9,11/36$, totaling $29/18$.

27. **Pair collisions versus crowded bins.** A multiply occupied bin can contain many colliding pairs; determine the counted object before choosing indicator indices. **Worked check.** The four co-located balls form $\binom42=6$ unordered pairs, whereas they occupy only one crowded bin. For independent uniform allocation, each of the six pairs collides with probability $1/n$.

28. **Singleton bins.** An exact occupancy event requires a choice factor for the included balls and an avoidance factor for all others. **Worked check.** For a fixed bin, select which one of the three balls enters it, with three possible choices. That ball chooses the bin with probability $1/4$, and the other two avoid it with probability $(3/4)^2$.

29. **Distinct observed labels.** Fixed-horizon distinct counts use seen-label indicators; waiting to see every label is a different random variable. **Worked check.** For each label, define an indicator that it appears at least once in the fixed five draws. Its complement is five consecutive avoids with probability $(3/4)^5$.

30. **Uniform sampling without replacement.** Uniform subset sampling gives inclusion probability equal to sample size divided by population size; depletion affects the law, not this first-moment identity. **Worked check.** For each marked object, exactly $\binom{11}{4}$ of the $\binom{12}{5}$ possible subsets contain it. The ratio equals $5/12$.

31. **Expected sampled total.** Unbiased sample-average reasoning uses a fixed positive sample size or an explicitly justified random-denominator argument. **Worked check.** Each population object is included with probability $2/4=1/2$. The sampled sum is the weighted sum of its inclusion indicators, so its mean is $(1/2)(-2+1+4+7)=5$.

32. **Unequal inclusion probabilities.** Inverse inclusion weighting is unbiased for a total when every relevant object has a known positive inclusion probability. **Worked check.** Write the estimator as $T=6I_1+32I_2+25I_3$, because each population value is divided by its own positive inclusion probability. Its mean is $6(1/2)+32(1/4)+25(1/5)=3+8+5=16$, the population total.

33. **Head-run starts.** Count starts of runs, including the special first-position boundary; overlapping local events still permit linearity. **Worked check.** A head-run starts at position one if it is a head, with probability $1/3$. At each of the other five positions it starts when the previous result is a tail and the current result is a head, with probability $(2/3)(1/3)=2/9$.

34. **All runs and endpoint accounting.** For a nonempty sequence, run count equals one plus number of adjacent changes; retain the initial deterministic term. **Worked check.** Every nonempty sequence has an initial run. Each of its six neighboring position pairs adds another run exactly when the two bits differ.

35. **Overlapping all-success windows.** Overlapping windows count starts, not disjoint blocks or maximal runs; verify the multiplicity on a concrete sequence. **Worked check.** The allowed starting indices are one through six, producing six windows. A particular window has three heads with probability $1/8$ because its three tosses are independent.

36. **Edges and triangles.** A subgraph indicator probability uses the required edges of that subgraph; dependence between different subgraphs does not prevent summing their means. **Worked check.** There are $\binom52=10$ possible edges, each with presence probability one half, giving expected edge count five. There are $\binom53=10$ vertex triples.

37. **Isolated vertices.** Convert a vertex property to the exact incident-edge event before applying independence or summing indicators. **Worked check.** A fixed vertex has four possible incident edges. It is isolated if all four are absent, giving probability $(2/3)^4=16/81$.

38. **Tail-sum reconstruction.** Match $P(N\ge k)$ starting at one with $P(N>k)$ starting at zero; second moments need odd layer weights. **Worked check.** The tail probabilities at thresholds one, two, and three are $3/4,1/2,1/4$. Their sum is $3/2$, the first moment.

39. **A survival specification.** Derive moments directly from a valid survival law, retaining its support origin before summing geometric series. **Worked check.** The mean is the geometric tail sum $\sum_{k\ge1}2^{-(k-1)}=2$. For the second moment, set $j=k-1$ and use $\sum_{j\ge0}jq^j=q/(1-q)^2$ with $q=1/2$.

40. **Signed integer tails.** Split signed integer variables into nonnegative parts and check both tail sums before subtracting them. **Worked check.** The positive thresholds one through three each have tail probability $1/4$, so the positive-part mean is $3/4$. The negative thresholds one and two each have probability $1/4$, so the negative-part mean is $1/2$.

41. **Total trials versus failures.** State whether the successful trial is counted; translate geometric conventions by the deterministic support offset. **Worked check.** For the total-trial count $T$, survival at integer $k\ge1$ is $(4/5)^{k-1}$. Its tail mean is $1/(1-4/5)=5$.

42. **A capped waiting process.** Executed-trial caps collect all remaining paths at the terminal count; censoring and conditioning produce different laws. **Worked check.** The executed count is $C=\min(T,3)$. It reaches at least one trial surely, at least two after one failure with probability $3/4$, and at least three after two failures with probability $9/16$.

43. **A zero code for failure.** Read terminal failure codes literally; a zero return value does not mean that no trials were executed. **Worked check.** The returned value equals one with probability $1/4$, two with probability $3/16$, and three with probability $9/64$. All-failure paths have probability $27/64$ and return zero.

44. **Conditioning on success before a cap.** A conditional mean divides the event-restricted weighted contribution by the conditioning-event probability, not by the number of supported values. **Worked check.** Success by the cap has probability $1-(3/4)^3=37/64$. The unnormalized successful-trial contribution from Question 43 is $67/64$.

45. **Two geometric waiting segments.** A negative-binomial waiting count changes by the number of required successes when translating total trials into failures only. **Worked check.** The total waiting count is the sum of four first-success waiting segments, each with mean three. Linearity gives mean twelve; segment independence is not required by that final sum step, though the original independent trials justify the repeated geometric waiting model.

46. **Poisson first and second moments.** Use factorial moments to cancel count factorials, then convert raw powers through exact algebraic identities. **Worked check.** In the mean sum, $k/k!=1/(k-1)!$ for $k\ge1$, giving $E[N]=3e^{-3}\sum_{j\ge0}3^j/j!=3$. For the factorial moment, $k(k-1)/k!=1/(k-2)!$ for $k\ge2$, yielding $E[N(N-1)]=9$.

47. **Binomial factorial moments.** A falling factorial counts ordered distinct successes; a binomial coefficient counts unordered subsets and differs by a factorial factor. **Worked check.** Expand $N(N-1)$ as the sum of products $I_iI_j$ over ordered distinct indices. There are $5\cdot4=20$ such pairs.

48. **A count that is not binomial.** Matching $np$ is only a mean check; a binomial law also requires the stated independent-trial construction. **Worked check.** The count is $N=5I$, taking zero or five. Its mean is $5(2/5)=2$, exactly the same as a binomial count with matching marginals.

49. **Raw moments to central moments.** Central moments require expansion about the mean; a zero odd moment is a limited cancellation condition, not a complete law description. **Worked check.** Direct weighting yields $m_1=2$, $m_2=6$, and $m_3=20$. The third central formula gives $m_3-3\mu m_2+2\mu^3=20-36+16=0$.

50. **Negative affine scaling.** Means use the signed scale, variances its square, and standard deviations its absolute value; fixed shifts do not change spread. **Worked check.** Linearity gives $E[Y]=-3(2)+5=-1$. Centering yields $Y-E[Y]=-3(X-2)$, so variance scales by nine: $Var(Y)=9(2)=18$.

51. **Squared-loss optimal prediction.** Name the loss before choosing a prediction; the mean minimizes squared loss when the second moment is finite. **Worked check.** The mean is $13/10$ and variance $441/100$. The expected squared loss of a prediction $c$ is $441/100+(c-13/10)^2$.

52. **Integer-constrained prediction.** For discrete prediction constraints under squared loss, project the mean onto the allowed set and retain all ties. **Worked check.** The loss differs from its unconstrained minimum by $(c-1.3)^2$. The closest integer is one, at distance $0.3$, while two is at distance $0.7$.

53. **Mean, median, and mode disagree.** Mean, median, and mode solve different optimization problems; an unspecified “most expected value” is ambiguous. **Worked check.** The mean is four, so squared loss is minimized there. For absolute loss, the majority mass at zero makes zero a median and the unique optimal prediction: moving right initially adds more loss at zero than it removes at ten.

54. **Moment feasibility.** Test raw-moment feasibility through nonnegative squared deviations; equality often forces an almost-sure identity. **Worked check.** With finite second moment, nonnegative variance requires $E[X^2]\ge(E[X])^2=16$. Twelve would produce variance negative four and is impossible.

55. **Jensen and strict equality.** Attach the convex domain and equality condition to Jensen; neither inequality direction nor strictness is automatic outside that domain. **Worked check.** The reciprocal function has positive second derivative on the positive real axis and is strictly convex. The finite-law weighted Jensen inequality therefore gives $E[1/X]\ge1/E[X]$.

56. **A sharp Markov example.** Distinguish a sharp worst-case bound from an exact probability for a specific law; equality can be tested by a two-point construction. **Worked check.** Pointwise $X\ge5I_{\{X\ge5\}}$, so averaging gives probability at most $2/5$. A law with mass $2/5$ at five and $3/5$ at zero has mean two and tail probability $2/5$, attaining the bound.

57. **Chebyshev from a second moment.** A variance bound concerns squared deviations from the specified mean and can be sharp without identifying the actual tail probability. **Worked check.** Apply Markov to the nonnegative variable $(X-3)^2$. Its mean is four, and the event in question implies it is at least twenty-five, giving bound $4/25$.

58. **The expected value of a category mean.** Weight category means by category probabilities; means of categories do not acquire equal weights merely because two categories are listed. **Worked check.** The two mode events are a positive-probability partition. Their restricted weighted contributions sum to $(1/4)(10)+(3/4)(2)=4$.

59. **Hidden probability and a misleading binomial.** Average conditional probabilities and conditional means separately; a mixture of binomial laws is generally not a binomial law at the mean parameter. **Worked check.** The conditional means are $4/5$ and $16/5$, whose equal mixture has mean two. The zero-count probability is the mixture $[(4/5)^4+(1/5)^4]/2=257/1250$.

60. **Independent random sample size.** For a random number of terms, justify how length is chosen; independence from the increments permits the simple product of means. **Worked check.** Conditional on $N=0$, the empty sum is zero. Conditional on $N=3$, independence from the increment sequence makes its mean $3(4)=12$.

61. **A dependent-length counterexample.** Inclusion can be selected by the value being summed; independent-random-length formulas cannot be applied to such value-dependent selection. **Worked check.** If $X_1=0$, the length is zero and the empty sum is zero. If $X_1=1$, the length is one and the sum is one.

62. **Geometric recursion with a justified finite mean.** Prove existence before solving moment recursions; an algebraic fixed point need not describe an infinite expected stopping time. **Worked check.** The tail-sum argument first establishes finite mean $m=1/p$ and finite second moment for the geometric law, so the algebra is legitimate. A first-step success costs one; a failure costs one plus a fresh waiting count.

63. **Nonnegative countable linearity.** Finite expected nonnegative count implies almost-sure finiteness, but not a deterministic bound on every realization. **Worked check.** The partial counts increase, so nonnegative countable linearity gives mean $\sum_{k\ge1}2^{-k}=1$. An extended nonnegative count with a finite mean cannot be infinite on a positive-probability event: its expectation would exceed every finite bound there.

64. **A safe signed infinite sum.** Summability of expected absolute contributions is a sufficient signed-series interchange condition; pointwise convergence alone is insufficient. **Worked check.** The nonnegative absolute sum has mean at most $\sum_{k\ge1}3^{-k}=1/2$. It is therefore finite almost surely, so the signed series converges absolutely almost surely.

65. **Pointwise convergence that loses the mean.** A limit that discards rare large values can lose expectation; identify an actual convergence theorem before interchanging limit and averaging. **Worked check.** For any fixed positive $U$, eventually $1/n<U$, so $Y_n$ is eventually zero and converges pointwise to zero. Its mean is nevertheless $nP(U\le1/n)=n(1/n)=1$ for every $n$.

66. **Class-uniform versus student-uniform sampling.** Determine the sampled unit; size-biased weights differ from equal group weights and can reverse an informal average interpretation. **Worked check.** Uniform class selection assigns weight one third to each size, giving mean eight. Uniform student selection assigns class probabilities $4/24,8/24,12/24$, since a larger class contains more selectable students.

67. **Population size bias through moments.** Size bias introduces one additional factor of the size and a normalization by its mean; retain both factors and check moment existence. **Worked check.** Student sampling weights each class proportionally to its size. The resulting mean is $E[X^2]/E[X]$, assuming finite second moment and positive finite mean.

68. **A minimum from tail conjunctions.** Extrema are nonlinear; derive their survival or CDF events before averaging, rather than applying the extremum to separate means. **Worked check.** For integer thresholds $k=1,\ldots,6$, both dice must be at least $k$. Their independent survival probability is $[(7-k)/6]^2$.

69. **A maximum without deriving a new law.** Search for outcome-wise identities connecting nonlinear quantities; linearity can then eliminate one quantity without inventing a nonlinear averaging rule. **Worked check.** On every ordered die outcome, minimum plus maximum equals the sum of the dice. Linearity gives mean total seven regardless of the nonlinear individual extrema.

70. **Random pair products under independence.** Apply independence only to the product it actually justifies; shared derived products need not be independent for their means to add. **Worked check.** Each pair is independent, so its product mean factors: $E[XY]=-2$, $E[YZ]=-3$, and $E[ZX]=6$. The outer finite sum then has mean one by linearity.

71. **Pairwise independence is not joint independence.** A product involving three or more variables requires a matching joint-independence argument or its actual joint law; pairwise tests are insufficient. **Worked check.** The four equally likely $(A,B,C)$ outcomes are $(0,0,0),(0,1,1),(1,0,1),(1,1,0)$. Each pair of bits is independent and each mean is one half.

72. **Spaghetti loops and the coefficient of the logarithm.** Determine the number of eligible partners at each stage; exact reciprocal sums reveal coefficients that informal growth descriptions may omit. **Worked check.** When there are $2k$ loose ends, choosing one end leaves $2k-1$ possible partners. Exactly one partner is the other end of its current chain, so the closure probability is $1/(2k-1)$.

73. **Zero mean for a nonnegative variable.** Zero mean forces constancy only when the averaged quantity is nonnegative; use positive threshold events to prove the almost-sure conclusion. **Worked check.** For every positive integer $k$, the pointwise inequality $X\ge(1/k)I_{\{X\ge1/k\}}$ implies $0=E[X]\ge P(X\ge1/k)/k$. Hence every such threshold event has probability zero.

74. **A strict expectation comparison.** Almost-sure order gives mean order; strict mean order needs strict difference on a positive-probability set, not just a displayed example. **Worked check.** The difference $D=Y-X$ is integrable and nonnegative. If its mean were zero, the preceding nonnegative-zero-mean theorem would force $D=0$ almost surely, contradicting positive probability of a strict difference.

75. **A stable variance calculation.** Large shifts can cause catastrophic cancellation in raw-moment variance; center first and distinguish exact algebra from finite-precision computation. **Worked check.** Choose $c=10^9$. The centered variable takes negative one and one equally often, so its first centered mean is zero and its second centered mean is one.

76. **An omitted-tail error bound.** A truncation guarantee must control the whole omitted mean sum; a geometric survival envelope yields an explicit computable error bound. **Worked check.** The omitted mean contribution is $\sum_{k=r+1}^{\infty}P(N\ge k)$, not merely the probability of exceeding $r$. The supplied geometric survival bound gives error at most $\sum_{k=r+1}^{\infty}2^{-k}=2^{-r}$.

77. **No independence needed for expected sample average.** Unbiased averaging requires the specified means; precision improvement requires additional dependence and second-moment assumptions. **Worked check.** For fixed positive $n$, linearity gives $E[\bar X]=(1/n)\sum_iE[X_i]=\mu$ without independence. No universal variance reduction follows.

78. **A theorem with nonexistent components.** An integrable combined expression does not automatically give integrable summands; verify the terms before separating their expectations. **Worked check.** The sum variable is identically zero, so its mean exists and equals zero. Each component has infinite positive and negative parts and therefore no defined expectation.

79. **Expected pairwise equal values from a discrete law.** Pair-collision expectations and all-equal probabilities use different powers of the atom masses; avoid treating overlapping agreement tests as independent. **Worked check.** Each unordered pair agrees with probability $1/4+1/9+1/36=7/18$. There are three pairs, so their expected count is $7/6$.

80. **A compound payoff with a random length and nonlinear term.** Nonlinear compound costs require the corresponding conditional moments, not just the expected length and expected increment. **Worked check.** Conditional on $N=1$, the count is one Bernoulli variable, so its first and second moments are both $1/2$. Conditional on $N=2$, the first moment is one and the second is $3/2$, obtained from the two indicator squares and their independent product.
