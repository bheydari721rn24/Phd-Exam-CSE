# Variance, Covariance, and Second-Moment Reasoning

## 1. Sources, prerequisites, and chapter boundary

This chapter combines four core written university courses: MIT18.05, CMU36-700, Oxford Prelims Probability, and BerkeleyCS70. Selected ETH Zurich and Cornell sections strengthen the existence and matrix arguments. The [source comparison](../reviews/s_variance-sources.html) states the exact pages read, candidate courses screened, attribution, access limits and corrections. A course home or download alone does not count as a reviewed lecture.

You should already understand probability mass and density functions, joint and conditional distributions, independence, indicator variables, sums, elementary integrals, and expectation. Matrix notation is introduced where needed. The objective is to derive second-moment answers from the stated law and assumptions, rather than identify a formula by superficial resemblance.

The boundary includes population variance, covariance, correlation, weighted sums, dependent indicators, sampling, random sums, conditional decompositions, prediction, covariance matrices, moment inequalities, and exact numerical computation. Distribution-specific machinery is used only as needed; the complete distribution catalogue, inference procedures and measure-theoretic construction of conditional expectation are deferred. The mathematics is written afresh and checked independently. Neither a finite audit nor a chapter can guarantee correct answers to every unseen question.

## 2. What variance measures, and when it exists

Let $X$ be a real random variable with mean $\mu=E[X]$. A signed average displacement contains no spread information because $E[X-\mu]=0$. Squaring preserves every displacement's magnitude while removing its sign. The population variance is

$$Var(X)=E[(X-\mu)^2],\qquad \sigma_X=\sqrt{Var(X)}.$$

For a finite law with values $x_i$ and masses $p_i$, first verify nonnegative masses whose sum is one, then calculate $\mu=\sum_i p_ix_i$ and $Var(X)=\sum_i p_i(x_i-\mu)^2$. The probabilities, rather than the number of distinct values, are the weights. For a density, integrate over its actual support. A region where the density is zero contributes nothing; it may be convenient to integrate over a larger rectangle only after defining the density as zero outside the support.

Variance has squared measurement units; standard deviation has the original units. Multiplying a distance by100 multiplies variance by10000, whereas adding100 leaves variance unchanged. Standard deviation is a scale, not the expected absolute displacement: Cauchy–Schwarz gives $E[|X-\mu|]\le\sigma_X$, with equality only when the absolute displacement is constant almost surely.

For all covariance algebra in this chapter, assume square-integrability: $E[X^2]<\infty$. It implies $E[|X|]<\infty$, so the mean exists, and products of square-integrable variables are integrable. An integrable variable may have infinite variance. For a Pareto density $f(x)=\alpha x^{-\alpha-1}$ on $x\ge1$, its rth moment equals $\alpha/(\alpha-r)$ when $r<\alpha$ and diverges when $r\ge\alpha$. Thus $1<\alpha\le2$ gives a finite mean and infinite variance. The Cauchy law has no ordinary mean: symmetric cancellation of a principal-value integral cannot define its variance.

Nonnegativity of squared displacement proves $Var(X)\ge0$. Equality holds exactly when $X=\mu$ almost surely, not necessarily at every sample point. A probability-zero exception does not change a moment. This distinction becomes important for continuous variables and degenerate joint laws.

<!-- SIM: moments -->

## 3. Raw moments and a reliable calculation protocol

Expand the square and apply linearity, remembering that the mean is a constant:

$$E[(X-\mu)^2]=E[X^2]-2\mu E[X]+\mu^2=E[X^2]-\mu^2.$$

For $P(X=1)=1/4$, $P(X=3)=1/4$, $P(X=5)=1/2$, the mean is7/2 and the second moment is15. Therefore the variance is11/4. The centered calculation reaches the same answer by weighting squared deviations25/4,1/4,9/4. Showing both methods is useful when checking an examination option.

The raw formula squares values, not probabilities. $E[X^2]$ is not $(E[X])^2$. The latter is a scalar square after averaging. The difference must be nonnegative if the supplied moments are valid. For example, a proposed mean4 and second moment12 cannot describe any real square-integrable random variable.

Use this protocol: identify support; normalize the law; compute the first moment; compute the second moment; subtract the squared first moment; verify sign and units. Do not round intermediate rational numbers. If a question supplies a mixture, use conditioning instead of expanding a large mixture density. If it supplies a sum, inspect covariances before invoking additivity.

A useful equivalent identity uses an independent copy $X'$ with the same law:

$$Var(X)=\frac12E[(X-X')^2].$$

Expansion gives two equal second moments and $E[XX']=\mu^2$. Independence of the copy is essential: setting $X'=X$ makes the right side zero for every law. This identity explains variance through distances between two independent outcomes and supports an upper bound for bounded variables.

## 4. The mean is the optimal constant predictor

For a fixed constant $c$, write $X-c=(X-\mu)+(\mu-c)$. The cross term has expectation zero, so

$$E[(X-c)^2]=Var(X)+(\mu-c)^2.$$

The mean uniquely minimizes expected squared error over constants. An incorrect center adds squared bias; it does not change the population variance. If a measurement has mean10 and variance4, predicting7 gives mean squared error13. Predicting10 gives4. These are different quantities even though both are measured in squared units.

For $X$ supported on $[a,b]$, the pointwise inequality $(X-a)(b-X)\ge0$ gives $E[X^2]\le(a+b)\mu-ab$. Subtracting $\mu^2$ yields

$$Var(X)\le(b-\mu)(\mu-a)\le\frac{(b-a)^2}{4}.$$

Equality in the first bound requires support only at the endpoints, except on null sets. Equality in the second additionally requires mean at the midpoint. The sharp range bound therefore belongs to an equally weighted two-endpoint law, not a uniform density. A uniform density on the interval has variance $(b-a)^2/12$.

## 5. Affine changes and nonlinear transformations

For fixed $a,b$, the centered transformed variable is $aX+b-E[aX+b]=a(X-\mu)$. Consequently,

$$Var(aX+b)=a^2Var(X),\qquad \sigma_{aX+b}=|a|\sigma_X.$$

The absolute value in standard deviation is mandatory. If $a=0$, the result is constant; if $a<0$, order reverses but variance stays nonnegative. A random multiplier or random shift cannot be treated as a fixed coefficient. Correlated calibration errors require their own covariance terms.

For a nonlinear function $g$, calculate $E[g(X)]$ and $E[g(X)^2]$ under the original law. In general $Var(g(X))$ is not $g(Var(X))$, and $E[g(X)]$ is not $g(E[X])$. For a standard normal $Z$, $Var(Z^2)=E[Z^4]-E[Z^2]^2=3-1=2$. Knowledge of only mean and variance does not determine a fourth moment.

For independent $A$ and $X$ with finite second moments,

$$Var(AX)=Var(A)Var(X)+Var(A)E[X]^2+Var(X)E[A]^2.$$

Derive this by factoring $E[A^2X^2]$ and $E[AX]$, then expressing second moments as variance plus mean squared. The independence assumption must hold for the full product calculation; zero covariance alone does not factor squared products.

## 6. Joint laws and centered cross-products

Marginal variances do not describe how variables move together. Two variables may each be a fair Bernoulli while always equal, always opposite, or independent. Their marginal means and variances are identical in all three constructions, yet their sum variances are1,0 and1/2.

For square-integrable $X,Y$, define

$$Cov(X,Y)=E[(X-\mu_X)(Y-\mu_Y)]=E[XY]-\mu_X\mu_Y.$$

To prove the second equality, expand the product into four terms and substitute the means. Positive covariance is an average excess of same-sign centered products; negative covariance is an average excess of opposite-sign centered products. Neither sign states that every outcome moves in the same direction.

For a joint table $p_{ij}$, compute both marginals and means, then sum $p_{ij}x_iy_j$ or the centered product. Do not replace $p_{ij}$ by $p_ip_j$ unless independence is established. The units of covariance are the units ofX multiplied by those ofY. Covariance is symmetric, may be negative, and satisfies $Cov(X,X)=Var(X)$.

For continuous variables, integrate $xyf(x,y)$ over the actual joint support. Merely seeing a density that can be written as a product inside a triangular region does not establish independence: the support indicator must also factor. A deterministic relation may create a singular joint law without a two-dimensional density; covariance is still defined by expectation.

<!-- SIM: joint -->

## 7. Covariance algebra and weighted sums

Centering removes constants. Linearity in each argument gives

$$Cov(aX+b,cY+d)=acCov(X,Y).$$

For sums, distribute every centered factor:

$$Var\left(\sum_{i=1}^n a_iX_i\right)=\sum_{i=1}^n a_i^2Var(X_i)+2\sum_{i<j}a_ia_jCov(X_i,X_j).$$

There is one diagonal term per variable and one doubled off-diagonal term per unordered pair. Equivalently, sum $a_ia_jCov(X_i,X_j)$ over all ordered pairs. Mixing these two conventions loses or doubles a factor2. Independent variables have zero covariance, but pairwise uncorrelated variables already suffice for this finite variance identity.

For $Var(X)=4$, $Var(Y)=9$, $Cov(X,Y)=3$, the variance of $2X-Y$ is $16+9-12=13$. The subtraction changes the cross term's sign, not the sign of the squared coefficient. In contrast, $Var(X-X)=0$ because the same random variable appears twice; it is never a sum of independent copies.

Overlap problems become simple when written in a common primitive basis. If $U_i$ are independent Bernoulli(p), $X=U_1+U_2$ and $Y=U_2+U_3$, only the shared $U_2$ contributes to covariance: $Cov(X,Y)=p(1-p)$. For weighted overlap, sum the product of the two weights times the primitive variance at every shared index. “Overlap count times variance” applies only when shared coefficients are both one.

<!-- SIM: quadratic -->

## 8. Correlation, feasibility, and equality conditions

When both variances are finite and positive, Pearson correlation is

$$\rho=\frac{Cov(X,Y)}{\sigma_X\sigma_Y}.$$

It has no units. A positive rescaling does not change it; a negative rescaling reverses its sign. A zero rescaling makes correlation undefined. A zero covariance with a constant is valid, but dividing by its zero standard deviation is invalid.

Set $U=X-\mu_X$ and $V=Y-\mu_Y$. Since $E[(U-tV)^2]\ge0$ for every realt, minimizing at $t=Cov(X,Y)/Var(Y)$ gives

$$Cov(X,Y)^2\le Var(X)Var(Y).$$

This is the centered Cauchy–Schwarz inequality. It proves $|\rho|\le1$ and rejects impossible supplied moments. Equality means the minimizing squared residual vanishes almost surely: $U=tV$ almost surely. With positive variances, $\rho=1$ means a positive affine relation and $\rho=-1$ a negative affine relation. The condition is an affine relation between the random variables, not simply three points in a small sample that appear collinear.

For fixed standard deviations, the possible variance of a sum lies between $(\sigma_X-\sigma_Y)^2$ and $(\sigma_X+\sigma_Y)^2$. These endpoints are attainable by choosing perfect opposite or same-direction standardized variables. Specified non-Gaussian marginal distributions may prevent attaining every covariance in that interval; the bound remains necessary but is not a complete coupling construction for arbitrary fixed marginals.

## 9. Independence, uncorrelatedness, and nonlinear dependence

Independence factors the joint law, and hence $E[XY]=E[X]E[Y]$ when the required expectations exist. Therefore independent square-integrable variables are uncorrelated. The reverse implication fails.

Let $X$ be uniform on $\{-1,0,1\}$ and $Y=X^2$. Then $E[X]=0$, $E[Y]=2/3$ and $E[XY]=E[X^3]=0$. Both variances are positive, so correlation is zero. Nevertheless, $P(Y=0\mid X=0)=1$ while $P(Y=0)=1/3$. The joint law cannot factor. A curve can be a deterministic relation while centered positive and negative contributions cancel.

Even normally distributed marginals do not suffice for the Gaussian exception. If $X$ is standard normal and $S$ is an independent fair sign, $Y=SX$ also has a standard normal marginal and zero covariance withX, but $|Y|=|X|$ deterministically. The pair is not jointly Gaussian.

For a jointly Gaussian pair with positive variances and $|\rho|<1$, its density at zero correlation factors into the two marginal densities; thus zero covariance implies independence in that restricted family. At $|\rho|=1$ the pair is supported on a line and has no nonsingular two-dimensional Gaussian density. Do not insert those endpoints into a formula dividing by $\sqrt{1-\rho^2}$.

<!-- SIM: dependence -->

## 10. Indicator expansions: count events without constructing a large law

An indicator $I_A$ satisfies $I_A^2=I_A$, so $E[I_A]=p$ and $Var(I_A)=p(1-p)$. For two events,

$$Cov(I_A,I_B)=P(A\cap B)-P(A)P(B).$$

Thus a count $S=\sum_i I_i$ has variance given by diagonal Bernoulli terms plus pair-intersection corrections. First identify whether the question counts ordered or unordered pairs. Pairwise independence is enough to remove these covariance corrections, even when the full collection is not mutually independent.

For the numberF of fixed points in a uniform random permutation ofn labels, $P(I_i=1)=1/n$ and, for distincti,j with $n\ge2$, $P(I_i=I_j=1)=1/[n(n-1)]$. Consequently $E[F]=1$ and $E[F^2]=1+1=2$, giving $Var(F)=1$. At $n=1$, F is constant and its variance is0. This boundary cannot be recovered by substituting into a formula containing $n-1$ in its denominator.

For occupancy ofn independent uniformly chosen boxes bym balls, empty-box indicators have $p=(1-1/n)^m$ and pair intersection $q=(1-2/n)^m$, for $n\ge2$. Their count has variance $np(1-p)+n(n-1)(q-p^2)$. The indicators are dependent even though ball destinations are independent. Independence at the primitive level does not imply independence of overlapping derived events.

## 11. Sampling without replacement and negative covariance

Suppose a population ofN binary values containsK ones. Let $p=K/N$ and inspectn distinct positions sampled uniformly without replacement. For $N>1$, each draw indicator has meanp and variance $p(1-p)$. For distinct draws,

$$E[I_iI_j]=\frac{K(K-1)}{N(N-1)},\qquad Cov(I_i,I_j)=-\frac{p(1-p)}{N-1}.$$

Substitution in the sum formula gives

$$Var(S)=np(1-p)\frac{N-n}{N-1}.$$

The finite-population correction explains the reduction relative to independent replacement draws. Ifn=N, the count is exactlyK and variance0. Ifn=1, the correction is1. IfK=0 orK=N, every draw is deterministic. The N=1 case must be handled directly rather than divide by0.

For numerical population values with population variance $v=N^{-1}\sum_j(x_j-\mu)^2$, two ordered draws without replacement have covariance $-v/(N-1)$. Therefore the sample mean variance is $(v/n)(N-n)/(N-1)$. Some statistics texts define population spread with denominatorN−1; substitute $v=(N-1)S^2/N$ before comparing formulas. A denominator convention is part of the model.

<!-- SIM: sampling -->

## 12. Random sums, shared noise, and averages

Let $N$ be a nonnegative integer count independent of an iid sequence $X_i$ with mean $\mu$ and variance $v$, and let $S=\sum_{i=1}^N X_i$, with an empty sum defined as0. Conditional onN, the sum has mean $N\mu$ and varianceNv. When the moments required below are finite,

$$E[S]=E[N]\mu,\qquad Var(S)=E[N]v+Var(N)\mu^2.$$

The second term describes variation in the conditional mean, caused by the count. Omitting it is valid only if the increments have zero mean or the count is fixed. IfN depends on observed increments, conditioning onN can change their distribution; optional stopping is not justified by this formula.

For independent observations with common variancev, the mean ofn observations has variancev/n. If observations instead equal $X_i=Z+\epsilon_i$, with independent common noiseZ and mutually independent zero-mean errors, common-noise variance does not average away:

$$Var(\bar X)=Var(Z)+\frac{Var(\epsilon_1)}{n}.$$

With common pairwise covariancec and common variancev, the sample mean variance is $v/n+(n-1)c/n$. The proposed covariance structure must be feasible. Negative c cannot remain fixed for arbitrarily largen if it violates positive semidefiniteness. Perfect repetition $X_i=Z$ leaves the mean equal toZ, with variancev.

<!-- SIM: averages -->

## 13. Conditional variance and the two sources of spread

For a conditioning variableZ, let $m(Z)=E[X\mid Z]$. The conditional variance is a random quantity determined byZ:

$$Var(X\mid Z)=E[X^2\mid Z]-m(Z)^2.$$

At a fixed valuez, the conditional law is centered aboutm(z), not about the unconditional mean. For a discrete conditioning value with positive probability, divide joint mass by its marginal. In a continuous model, use a valid conditional density or conditional-expectation version; never divide by $P(Z=z)=0$.

Write $X-\mu=(X-m(Z))+(m(Z)-\mu)$ and expand the square. The cross term vanishes after conditioning because $E[X-m(Z)\mid Z]=0$. Taking expectations yields

$$Var(X)=E[Var(X\mid Z)]+Var(E[X\mid Z]).$$

The first term averages within-group spread; the second is spread of group means. Both are nonnegative. For group probabilities1/4 and3/4, means0 and4, and variances1 and9, the overall mean is3, within variance7 and between variance3; total variance10. Simply averaging group variances loses the separation between the means.

The same expansion with two variables gives the law of total covariance:

$$Cov(X,Y)=E[Cov(X,Y\mid Z)]+Cov(E[X\mid Z],E[Y\mid Z]).$$

The two covariance terms need not be nonnegative and may cancel. Conditional independence does not imply unconditional independence: shared group membership can correlate conditionally independent measurements. Similarly, unconditional zero covariance may hide opposite within-group and between-group effects.

<!-- SIM: mixture -->

## 14. Prediction, residual orthogonality, and optimal linear coefficients

For any square-integrable predictorg(Z), the residual $R=X-m(Z)$ has conditional mean0. Multiplying by a square-integrable function ofZ and using conditioning gives $E[Rg(Z)]=0$ whenever the product is integrable. Therefore

$$E[(X-g(Z))^2]=E[Var(X\mid Z)]+E[(m(Z)-g(Z))^2].$$

Conditional expectation is the minimum-squared-error predictor among all measurable functions ofZ; a proof need not invoke a Gaussian distribution. The residual can still depend onZ through its conditional variance. Zero conditional mean is a statement about one moment, not the entire conditional law.

If only affine predictions $a+bY$ are allowed and $Var(Y)>0$, centering first gives

$$b=\frac{Cov(X,Y)}{Var(Y)},\qquad a=E[X]-bE[Y].$$

The minimum mean squared error is $Var(X)-Cov(X,Y)^2/Var(Y)=Var(X)(1-\rho^2)$. Derive this by completing the square in the coefficientb. The fitted residual is uncorrelated withY. It need not be independent ofY. The optimal affine predictor coincides with conditional expectation only when the latter is affine almost surely.

For a linear combination $wX+(1-w)Y$ with equal means, variance is $w^2v_X+(1-w)^2v_Y+2w(1-w)c$. If $v_X+v_Y-2c>0$, the unrestricted minimizer is $w=(v_Y-c)/(v_X+v_Y-2c)$. If weights are constrained to $[0,1]$, clip to that interval after deriving the unconstrained result. If the denominator is0, X−Y is constant almost surely and the variance does not depend onw; do not divide by0.

<!-- SIM: projection -->

## 15. Covariance matrices and positive semidefiniteness

For a column vector $\mathbf X$ of square-integrable variables, its covariance matrix $\Sigma$ has entries $\Sigma_{ij}=Cov(X_i,X_j)$. Its diagonal contains variances, and it is symmetric. For fixed coefficient vectora,

$$Var(a^T\mathbf X)=a^T\Sigma a\ge0.$$

This proves positive semidefiniteness. Conversely, every real symmetric positive semidefinite matrix can be realized as a covariance matrix: factor it as $BB^T$, take independent standard normal componentsZ, and set X=BZ. This construction establishes unrestricted realization, not a realization with arbitrary preassigned marginals.

A two-by-two matrix with diagonalsv1,v2 is feasible exactly when both are nonnegative and its determinant $v_1v_2-c^2$ is nonnegative. If a diagonal is0, its row and column must be0. In three or more dimensions, passing all pairwise correlation bounds is insufficient. The matrix with diagonal1 and all off-diagonal entries−3/4 passes every pairwise absolute bound, yet the all-ones vector has negative quadratic form. For a three-variable correlation matrix with off-diagonalr,s,t, its determinant is $1+2rst-r^2-s^2-t^2$ and must be nonnegative.

For a fixed real matrixA and vectorb, $Cov(A\mathbf X+b)=A\Sigma A^T$. Check shapes: A has output-by-input dimensions. Translation disappears; a singular A can produce a singular covariance. A zero eigenvalue means a centered linear combination is almost surely zero, not that every variable is deterministic.

## 16. Tail bounds and what moments cannot determine

For nonnegativeW andt>0, $W\ge tI_{\{W\ge t\}}$ pointwise. Taking expectations proves Markov's inequality. Apply it to $(X-\mu)^2$:

$$P(|X-\mu|\ge t)\le\min\left(1,\frac{Var(X)}{t^2}\right).$$

The lower bound for the complementary strict event is $P(|X-\mu|<t)\ge1-Var(X)/t^2$, clipped at0. Boundary equality matters when the law places mass exactly at the threshold. A bound larger than1 is valid but uninformative.

Chebyshev is sharp: forv≤t², put massv/(2t²) at each of $\mu-t$ and $\mu+t$, and the remaining mass at $\mu$. The variance isv and the non-strict tail probability isv/t². Using a strict tail removes the endpoint atoms; the same sharp maximum may then be a supremum approached from outside rather than attained by this exact law.

For a one-sided event witht>0 andv>0, apply Markov to $(X-\mu+b)^2$, on which $X-\mu\ge t$ implies a square at least $(t+b)^2$ for b≥0. Its expectation isv+b². Minimizing $(v+b^2)/(t+b)^2$ atb=v/t gives Cantelli's bound:

$$P(X-\mu\ge t)\le\frac{v}{v+t^2}.$$

It is attained by a centered two-point law with upper valuet and lower value−v/t. A variance of0 is handled directly. Moment bounds do not assert a Gaussian law or an exact tail probability. Two distributions with the same mean and variance can have different tails, medians and supports.

<!-- SIM: bounds -->

## 17. Random walks, exact ensembles, and sample-size guarantees

For independent fair signs $\epsilon_i$, $S_n=\sum_i\epsilon_i$ has mean0 and variance n. The root-mean-square displacement is $\sqrt n$; it is not the expected absolute displacement. A single animated path is neither an empirical proof nor a population variance. The exact ensemble updates probability mass by splitting each position's mass equally to its two neighbors.

For signs with right-move probabilityp, the mean is n(2p−1) and variance4np(1−p). Correlated steps require pairwise covariance additions. If every step repeats one initial fair sign, S_n equals±n, giving variancen² instead ofn.

For iid observations with finite variancev, Chebyshev yields $P(|\bar X-\mu|\ge\epsilon)\le v/(n\epsilon^2)$. To guarantee this bound is at mostδ, choose an integer $n\ge v/(\delta\epsilon^2)$. This is a sufficient worst-case moment-based guarantee, not necessarily the smallest actual sample size. A distribution-specific tail formula may require fewer samples.

The finite-variance proof establishes the weak law in this setting. A general iid weak law can hold under a finite first moment even when variance is infinite, but that stronger theorem needs a different proof. The central limit theorem gives a limiting distribution under its assumptions; it does not turn every finite sample into an exact normal law.

<!-- SIM: walk -->

## 18. Continuous second moments and generating functions

For a densityf, compute $E[X^r]=\int x^rf(x)\,dx$ whenever it exists. A uniform[a,b] law gives mean(a+b)/2 and variance(b−a)²/12 by an affine change from uniform[0,1]. For a density2x on0<x<1, the mean is2/3, second moment1/2, and variance1/18. These computations depend on the density, not on a uniform weighting of the interval.

For a rateλ exponential law withλ>0, integration by parts gives $E[X]=1/\lambda$ and $E[X^2]=2/\lambda^2$, hence variance1/λ². Rate and scale are reciprocal conventions; state which one is used. For the standard normal, integrate $z^2e^{-z^2/2}$ by parts and use the unit integral of its normalized density to get variance1. The half-line integral of $z\phi(z)$ equals1/sqrt(2π), not1.

If the moment-generating function $M(t)=E[e^{tX}]$ is finite in an open neighborhood of0, differentiation gives $M'(0)=E[X]$ and $M''(0)=E[X^2]$. Therefore $Var(X)=M''(0)-M'(0)^2$. For $K(t)=\log M(t)$, its second derivative at0 equals variance. Independent-sum MGFs multiply, so their log MGFs and variances add. Mere existence of finite second moments does not imply a finite MGF around0.

For a nonnegative integer variable with probability-generating functionG, derivatives give factorial moments: $G'(1)=E[X]$ and $G''(1)=E[X(X-1)]$ when finite, using a one-sided limit if needed. Consequently $Var(X)=G''(1)+G'(1)-G'(1)^2$. Omitting $G'(1)$ confuses a factorial moment with a raw second moment.

## 19. Population variance, sample variance, and implementation

Population variance is a property of the law. For observed valuesx1,…,xn, the empirical distribution assigning mass1/n has variance $n^{-1}\sum_i(x_i-\bar x)^2$. For iid observations from a population with variancev,

$$E\left[\sum_i(X_i-\bar X)^2\right]=(n-1)v.$$

To prove this, expand around the true mean: $\sum_i(X_i-\bar X)^2=\sum_i(X_i-\mu)^2-n(\bar X-\mu)^2$. Expectations give nv−n(v/n). The denominatorn−1 makes the sample variance unbiased forv whenn>1; it does not alter the variance of the empirical distribution. With dependent observations or a fitted model using additional parameters, do not apply this correction without analyzing the assumptions.

The raw formula can lose precision when a large mean is subtracted from a nearly equal second moment. For equally weighted observations, Welford's update maintainsn,mean andM2, the centered sum of squares. When a new valuex arrives, setδ=x−mean_old, mean_new=mean_old+δ/n, then M2_new=M2_old+δ(x−mean_new). The two displacement factors use different means. The update is an algebraic identity in exact arithmetic; floating-point roundoff still exists.

```python
def centered_moments(values):
    count, mean, m2 = 0, 0.0, 0.0
    for x in values:
        count += 1
        delta = x - mean
        mean += delta / count
        m2 += delta * (x - mean)
    if count == 0:
        raise ValueError("An empty dataset has no empirical mean.")
    population_variance = m2 / count
    sample_variance = m2 / (count - 1) if count > 1 else None
    return mean, population_variance, sample_variance
```

This implementation accepts equally weighted finite data. Probability-weighted streaming updates require a weight accumulator and a derived weighted recurrence. Do not silently interpret fractional probability weights as replicated sample counts. For exact examination examples, retain rational arithmetic until the final approximation.

## 20. Complete chapter summary

Variance is a probability-weighted squared displacement about the mean. Its raw-moment form is second moment minus squared first moment, and its units are squared units. Affine scaling squares the coefficient; translation disappears. The mean minimizes expected squared error, while a wrong center adds squared bias.

Covariance is the centered cross-product expectation. It controls the cross terms in every weighted-sum variance. Independence removes those terms where the moments exist; pairwise uncorrelatedness already suffices for additivity of a finite variance. Zero covariance does not establish independence, and normal marginals do not establish joint normality.

Correlation standardizes covariance only when both variances are positive and finite. Its bounds and equality cases follow from nonnegative squared residuals. Covariance matrices must be positive semidefinite, so several individually plausible pairwise correlations can still be jointly impossible.

Conditioning decomposes total variance into averaged within-condition variance plus variance of conditional means. It also provides the minimum-squared-error predictor and the random-sum formula under the required independence assumptions. Sampling without replacement creates negative covariance and a finite-population correction.

Second-moment inequalities bound tails but do not determine their exact probabilities. Random-walk spread concerns the full distribution, not a single path. Empirical variance, unbiased sample variance and the variance of a sample mean are distinct quantities. Every calculation should end by checking normalization, moment existence, coefficient signs, pair counts, boundary cases, units and the precise event requested.

## 21. Fully worked examination and original problems

The authentic items are checked against original MSc and doctoral PDF pages. Answers are independently derived, not claimed as official keys. Original and reconstructed tasks emphasize medium-to-hard formula and conceptual reasoning; foundational tasks remain where they diagnose a critical misconception. Difficulty labels are qualitative. Visual companions state their exact data and clarify the proof rather than replace it. The current finite bank does not claim to reproduce every university exercise or every examination year.

<!-- QUESTIONS -->

## 22. Final examination reasoning rules

<!-- RULES -->

## 23. Inspectable second-moment laboratory

Use this lab to inspect exact finite weighted laws and covariance contributions after the teaching. It does not request a test answer. Every experiment starts paused; failed validation keeps the last valid experiment. Numbers in drawings use the separate mathematical font; complete structured formulas use native MathML.

<!-- LAB -->

## 24. References and reading scopes

1. Massachusetts Institute of Technology. Jeremy Orloff and Jonathan Bloom, probability-note authors. *18.05 Introduction to Probability and Statistics*, Spring2022; course instructors Jeremy Orloff and Jennifer French Kamrin. [Combined probability notes](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_probability.pdf), PDF pages46–51,70–76,103–112.
2. Carnegie Mellon University. Siva Balakrishnan. *36-700 Probability and Mathematical Statistics I*, Fall2016. [Lecture3](https://www.stat.cmu.edu/~siva/teaching/700/lec3.pdf), pages7–8; [Lecture4](https://www.stat.cmu.edu/~siva/teaching/700/lec4.pdf), pages1–8.
3. University of Oxford. James Martin. *Prelims Probability*, Michaelmas2019. [Course notes](https://courses.maths.ox.ac.uk/mod/resource/view.php?id=48553), PDF pages1–3,23–29,57,64–68.
4. University of California, Berkeley. Rao and Walrand. *CS70 Discrete Mathematics and Probability Theory*, Spring2016. [Lecture17: Variance](https://fa16.eecs70.org/static/notes/n17.pdf), all five pages; archive location is Fall2016, document header is Spring2016.
5. ETH Zurich. Johanna F. Ziegel; translated by Alexander Henzi. *Probability Theory*, FS2020. [Lecture notes](https://people.math.ethz.ch/~ziegelj/WTSkript.pdf), title page and PDF pages8,16.
6. Cornell University. *CS2800 Discrete Structures*, Fall2017. [Lecture9: Expectation and variance](https://www.cs.cornell.edu/courses/cs2800/2017fa/lectures/lec09-expect.html), entire HTML lecture; no lecturer attribution established from that page.
7. Iranian examination repository. [Phd-Exam-CSE](https://github.com/bheydari721rn24/Phd-Exam-CSE/tree/main/Exams). Each authentic item states its immutable commit, booklet, printed question number, PDF page and original option order. Reused items are explicitly identified as revisited placements.

These references document actual written material used. The source audit distinguishes screened-only candidates, errors corrected and mathematical limits. The chapter's own explanations, proofs, diagrams and independently authored questions are not verbatim reproductions of course texts.
