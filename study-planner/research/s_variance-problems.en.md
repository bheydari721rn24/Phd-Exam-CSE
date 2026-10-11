# Individually authored variance and covariance problems

## 1. One law, two variance calculations

Let $ P(X=1)=1/4 $, $ P(X=3)=1/4 $, and $ P(X=5)=1/2 $. Find its mean, variance, and standard deviation.

### Complete solution

The masses are nonnegative and sum to one. Compute $ E[X]=1/4+3/4+5/2=7/2 $ and $ E[X^2]=1/4+9/4+25/2=15 $. Thus $ Var(X)=15-49/4=11/4 $ and the standard deviation is $\sqrt{11}/2 $. Independently, the centered displacements are $-5/2,-1/2,3/2 $. Their weighted squares sum to $25/16+1/16+9/8=11/4 $. The agreement checks both the weights and the center. Taking the square root is the final step, not an operation on individual weighted deviations.

## 2. A probability parameter from a variance

A Bernoulli variable has variance $3/16 $. Find every possible success probability. What extra information resolves the ambiguity?

### Complete solution

Since $ X^2=X $, its mean and second moment both equal $ p $, so its variance is $ p-p^2 $. Solve $ p(1-p)=3/16 $, giving $(p-1/4)(p-3/4)=0 $. Both probabilities are valid and produce the same variance. Variance alone does not distinguish a law from its reflected success/failure law. Knowing that the mean is below $1/2 $, or directly knowing the success probability is below $1/2 $, selects $ p=1/4 $. Selecting the smaller root without that information would discard a legitimate solution.

## 3. Discrete uniform variance

Derive the variance of a uniformly chosen integer from $1 $ through $ n $, including $ n=1 $.

### Complete solution

Use $ E[X]=(n+1)/2 $ and the sum of squares $ n(n+1)(2n+1)/6 $. Dividing that sum by $ n $ gives $ E[X^2]=(n+1)(2n+1)/6 $. Subtracting $(n+1)^2/4 $ and putting terms over denominator 12 yields $(n+1)(4n+2-3n-3)/12=(n^2-1)/12 $. At $ n=1 $ this is zero, as it must be for a constant law. The variance of a continuous uniform interval from 1 to $ n $ would instead be $(n-1)^2/12 $; discreteness changes the distribution, not merely the notation.

## 4. Missing mass and moment feasibility

A law assigns probability $ a $ to 0, probability $2a $ to 2, and the remaining probability to 4. Its mean is 3. Find $ a $ and the variance.

### Complete solution

Normalization gives the last mass $1-3a $, so admissibility requires $0\le a\le1/3 $. The mean is $4a+4(1-3a)=4-8a $. Setting it to 3 gives $ a=1/8 $, with masses $1/8,1/4,5/8 $. The second moment is $4(1/4)+16(5/8)=11 $. Hence the variance is $11-9=2 $. Check by centered displacements $-3,-1,1 $: their weighted squares are $9/8+1/4+5/8=2 $. Solving the mean equation is insufficient unless the resulting masses also define a valid law.

## 5. A negative proposed variance

A proposed random variable has $ E[X]=3 $ and $ E[X^2]=8 $. Decide whether any real probability distribution can have these moments.

### Complete solution

Any square-integrable real variable satisfies $ E[(X-3)^2]=E[X^2]-6E[X]+9 $. The proposed values make this $8-18+9=-1 $, contradicting nonnegativity of a square. Therefore no such law exists. This is a moment-feasibility contradiction, not evidence of negative dispersion or a signed standard deviation. Equivalently Jensen's inequality for the square requires $ E[X^2]\ge E[X]^2=9 $. In a computation, such a result should trigger a check of normalization, support, arithmetic and interpretation before taking a square root.

## 6. Same variance, different tail

Construct two mean-zero, variance-one finite laws with different values of $ P(|X|\ge2)$.

### Complete solution

For the first law, take equal mass at $-1 $ and 1. Its mean is zero and its second moment is 1, but its two-sided tail at 2 is zero. For the second, put mass $1/8 $ at each of $-2 $ and 2 and mass $3/4 $ at 0. Its second moment is $4(1/8+1/8)=1 $ and its mean is zero, while the requested non-strict tail probability is $1/4 $. Both laws satisfy the same first two moments. Those moments therefore cannot identify an exact tail probability; the second law also attains Chebyshev's bound at threshold 2.

## 7. Independent-copy identity

For an independent identically distributed copy $ X'$ of $ X $, prove $ E[(X-X')^2]=2Var(X)$. Explain why it fails if $ X'=X $.

### Complete solution

Expand the square. The two squared terms have expectation $ E[X^2]$ each, and independence gives $ E[XX']=E[X]E[X']=\mu^2 $. Therefore the expectation of the difference squared is $2E[X^2]-2\mu^2=2Var(X)$. If the copy is replaced by the very same variable, the difference vanishes identically. The product term is then $ E[X^2]$, not $\mu^2 $. Equality of marginal distributions is weaker than independence and cannot justify the factorization. This is a useful way to check whether an expression uses a new trial or repeats a previous measurement.

## 8. Sharp range bound

A random variable lies in $[2,8]$ and has mean 5. Find the largest possible variance and characterize an attaining law.

### Complete solution

The pointwise inequality $(X-2)(8-X)\ge0 $ gives $ E[X^2]\le10E[X]-16=34 $. Subtracting the squared mean 25 yields variance at most 9. The equally weighted endpoint law on 2 and 8 has mean 5 and squared displacement 9 at both outcomes, so it attains the bound. Equality requires the nonnegative product to vanish almost surely, forcing endpoint support. A uniform density on the same interval has variance 3 and does not maximize spread. The result is a sharp bound over all supported laws, not a statement that every law has variance 9.

## 9. Finite mean, infinite variance

For the density $ f(x)=\frac32x^{-5/2}$ on $ x\ge1 $, determine the mean and whether variance is finite.

### Complete solution

Integrating the density gives 1. For the mean, integrate $(3/2)x^{-3/2}$ over $[1,\infty)$, obtaining 3. The second moment integral is $(3/2)\int_1^\infty x^{-1/2},dx $, which diverges. Because the mean is finite but the squared centered displacement has the same divergent quadratic tail, the variance is infinite. Writing infinity minus 9 is only a shorthand for this nonnegative integral, not ordinary finite arithmetic. Covariance and correlation formulas requiring finite second moments cannot be used with this variable.

## 10. Zero variance and exceptional outcomes

A random variable equals 7 with probability one but differs from 7 at one probability-zero sample point. Is its variance zero? Is it pointwise constant?

### Complete solution

The mean is 7 because a null event contributes nothing to the expectation. The centered square is zero almost surely, so its integral and hence variance are zero. Nevertheless the stated exceptional point prevents pointwise constancy. The precise theorem is that zero variance implies constancy almost surely. In a finite sample space whose every point has positive probability, that conclusion also forces pointwise constancy; in a continuous or general probability space it need not. Substituting a universal pointwise statement for an almost-sure one is a logical strengthening that the moment calculation does not justify.

## 11. Negative affine scaling

A variable has mean 4 and variance 9. Find the mean, variance and standard deviation of $ Y=-2X+5 $.

### Complete solution

Linearity gives $ E[Y]=-2(4)+5=-3 $. After centering, $ Y-E[Y]=-2(X-4)$, so its variance is $4(9)=36 $. Standard deviation is the nonnegative square root 6. The multiplier for standard deviation is the absolute value 2, not $-2 $. Translation by 5 changes the mean but contributes no variance because it is fixed. These conclusions use no independence assumption: there is only one random variable and two deterministic coefficients.

## 12. Repeated versus independent copies

Let $ Var(X)=5 $, and let $ X'$ be an independent copy. Compare $ Var(X+X)$ with $ Var(X+X')$.

### Complete solution

The first sum equals $2X $, whose variance is $4Var(X)=20 $. The second sum has two independent components, so its variance is $ Var(X)+Var(X')=10 $. In covariance form, the first calculation contains $2Cov(X,X)=10 $ in addition to the two diagonal terms; the second covariance is zero. A shared symbol denotes the same realization, not an independent rerun. If a problem does not specify what the second copy represents, the two formulas cannot be interchanged.

## 13. Random multiplication

Independent variables $ A,X $ have means 2 and 3 and variances 1 and 4. Compute $ Var(AX)$.

### Complete solution

Independence gives $ E[AX]=6 $ and $ E[A^2X^2]=E[A^2]E[X^2]$. The individual second moments are 5 and 13, so the product second moment is 65. Thus the variance is $65-36=29 $. The equivalent decomposition is $1(4)+1(3^2)+4(2^2)=4+9+16=29 $. Treating the random multiplier A as its mean would give only 16 and miss its variation and interaction with X. Zero covariance of A and X would not suffice to factor their squared product.

## 14. Nonlinear square from insufficient moments

Suppose $ E[X]=0 $ and $ Var(X)=1 $. Is $ Var(X^2)$ determined? Give two counterexamples.

### Complete solution

A fair sign variable has $ X^2=1 $ identically, so $ Var(X^2)=0 $. A standard normal also has mean 0 and variance 1, but its fourth moment is 3, so $ Var(X^2)=3-1=2 $. More generally this variance is $ E[X^4]-E[X^2]^2 $ and requires a fourth moment, which may even be infinite. The first two moments do determine $ E[X^2]$, but they do not determine its variance. A nonlinear transformation therefore needs additional distributional or higher-moment information.

## 15. Incorrect prediction center

Let $ E[X]=10 $ and $ Var(X)=4 $. Compute $ E[(X-7)^2]$ and identify the optimal constant prediction.

### Complete solution

Decompose $ X-7=(X-10)+3 $. On squaring, the cross term has expectation $6E[X-10]=0 $, giving mean squared error $4+9=13 $. For an arbitrary constantc, the same argument gives $4+(10-c)^2 $, uniquely minimized atc=10 with value 4. The quantity 13 is not a new variance: variance always centers about the mean. It is prediction error around the chosen constant and explicitly includes squared bias.

A quick consistency check is that prediction error cannot be smaller than the variance. Equality occurs only when the chosen constant equals the mean; here the three-unit bias accounts exactly for the nine-unit excess.

## 16. Independent product with zero means

Independent $ X,Y $ have zero means and variances 4 and 9. Find $ Var(XY)$ and explain the existence assumptions.

### Complete solution

The mean of the product is zero by independence. Its second moment factors into $ E[X^2]E[Y^2]=4(9)=36 $. Thus the product variance is 36. Independence plus finite component second moments ensures the product has finite second moment in this calculation. If X and Y were merely uncorrelated, $ E[XY]=0 $ would still hold, but $ E[X^2Y^2]$ need not equal 36 or even be finite. The distinction matters precisely because a second moment of the product uses fourth-order joint information.

## 17. Variance under a density transformation

Let $ X $ have density $2x $ on $(0,1)$. Find $ Var(3X-1)$ without deriving a new density.

### Complete solution

The density integrates to 1. Compute $ E[X]=\int_0^1 2x^2,dx=2/3 $ and $ E[X^2]=\int_0^1 2x^3,dx=1/2 $. Their difference gives variance $1/2-4/9=1/18 $. The affine transform multiplies variance by 9, giving $1/2 $. Its mean is 1, but that shift does not enter the variance. Using a uniform variance of $1/12 $ would be wrong because the stated density gives more weight to larger values.

Normalization is a separate prerequisite: integrating the density over its stated interval gives one. The second moment is an integral of the squared outcome against that density, so neither the interval length nor its midpoint can substitute for the supplied weighting.

## 18. A symmetric nonlinear counterexample

Let $ X $ be uniform on $\{-2,-1,0,1,2\}$. Find $ Var(X^2)$ and $ Cov(X,X^2)$.

### Complete solution

Symmetry gives $ E[X]=E[X^3]=0 $. The second moment is $(4+1+0+1+4)/5=2 $, and the fourth moment is $(16+1+0+1+16)/5=34/5 $. Therefore $ Var(X^2)=34/5-4=14/5 $ and $ Cov(X,X^2)=E[X^3]-E[X]E[X^2]=0 $. This pair has positive variances and zero correlation, yet X determinesX². Its nonlinear dependence is invisible to a centered cross-product because odd contributions cancel.

A second method derives the law of the square. It equals zero with probability one fifth, one with probability two fifths, and four with probability two fifths. Its second moment is therefore zero plus two fifths plus thirty-two fifths, agreeing with the fourth moment of the original variable. This distinction between a second moment after transformation and a fourth moment before transformation is a useful bookkeeping rule.

## 19. Bernoulli complement

For $ X\sim Bernoulli(p)$, compute $ Cov(X,1-X)$, the variance of their sum, and their correlation when defined.

### Complete solution

The affine covariance rule gives $ Cov(X,1-X)=-Var(X)=-p(1-p)$. Since the sum equals 1, its variance is zero; equivalently its two diagonal terms cancel twice this negative covariance. For $0<p<1 $, both component variances are $ p(1-p)>0 $, so correlation is $-1 $. Atp=0 or 1, both are constant and Pearson correlation is undefined. A formula that mechanically returns $-1 $ after canceling a zero factor would conceal this boundary.

## 20. Lognormal second moment

Let $ Z\sim N(0,1)$ and $ X=e^Z $. Using $ E[e^{tZ}]=e^{t^2/2}$, compute $ Var(X)$.

### Complete solution

Substitutingt=1 gives $ E[X]=e^{1/2}$. Substitutingt=2 gives $ E[X^2]=e^2 $. Therefore $ Var(X)=e^2-e $. It is not $ e^{Var(Z)}=e $, nor the variance of the exponent passed through an exponential. The supplied transform expectation provides the additional information needed for the nonlinear calculation. The MGF of Z exists at those values; this computation says nothing about whether the MGF of X exists for positive arguments.

For a consistency check, the resulting variance is positive because the transformed variable is nonconstant. Its mean is greater than the exponential of the original mean, as expected from convexity. That inequality concerns expectation and does not supply a shortcut for variance.

## 21. A two-by-two joint table

The joint masses for $(X,Y)=(0,0),(0,1),(1,0),(1,1)$ are $1/3,1/6,1/6,1/3 $. Find the covariance and correlation.

### Complete solution

Both marginals are fair Bernoulli, so both means are 1/2 and variances 1/4. The only nonzero contribution to $ E[XY]$ comes from(1,1), giving 1/3. Thus covariance is $1/3-1/4=1/12 $ and correlation is $(1/12)/(1/4)=1/3 $. The distribution is not independent because $ P(1,1)=1/3 $ differs from the product 1/4. The table sums to one, and the covariance respects the bound $|c|\le1/4 $. Those checks prevent accidental use of a marginal mass in place of a joint mass.

## 22. Recover a joint probability

Events A,B have probabilities $2/5,3/5 $ and indicator covariance $1/50 $. Find their intersection probability and verify feasibility.

### Complete solution

Indicator covariance equals intersection probability minus the product of marginals. Therefore $ P(A\cap B)=1/50+6/25=13/50 $. The Fréchet interval is from $\max(0,2/5+3/5-1)=0 $ to $\min(2/5,3/5)=2/5 $. The proposed 13/50 lies inside. The remaining atom masses are $ P(A\cap B^c)=7/50 $, $ P(A^c\cap B)=17/50 $, and $ P(A^c\cap B^c)=13/50 $, all nonnegative. Recovering a number from the covariance equation is not enough unless a valid joint law results.

The four atom masses partition the whole sample space, so their sum must also be one. This explicit construction checks more than the absolute covariance bound: for Bernoulli variables, the intersection probability must obey the tighter marginal-dependent interval.

## 23. Overlapping Bernoulli windows

Independent Bernoulli(p) variables $ U_1,U_2,U_3 $ define $ X=U_1+U_2 $ and $ Y=U_2+U_3 $. Compute covariance and correlation for $0<p<1 $.

### Complete solution

Bilinearity expands the covariance into four primitive terms. Three involve distinct independent trials and vanish. The shared middle term is $ Cov(U_2,U_2)=p(1-p)$. Both sum variances are $2p(1-p)$, so their correlation is 1/2. Sharing exactly one of two equal-variance unit-weight components gives that value. Atp=0 or 1 the variables are constant and correlation is undefined, even though covariance is still zero. A full eight-outcome table gives the same answer but is unnecessary for the symbolic result.

## 24. Zero correlation with a deterministic curve

Let $ X $ be uniform on $\{-1,0,1\}$ and $ Y=X^2 $. Compute the two variances, covariance and a direct failure of independence.

### Complete solution

The moments are $ E[X]=0 $, $ E[X^2]=2/3 $, $ E[Y]=2/3 $ and $ E[Y^2]=2/3 $. Hence $ Var(X)=2/3 $ and $ Var(Y)=2/3-4/9=2/9 $. Symmetry gives $ E[XY]=E[X^3]=0 $, so covariance and correlation are zero. But $ P(X=0,Y=0)=1/3 $ whereas the product of marginals is 1/9. This explicit mismatch disproves independence. Both variances are positive, so the zero correlation is a genuine value rather than a division by zero.

The centered-product calculation adds a positive contribution from the right point and an equally large negative contribution from the left point. The middle point contributes zero because its centered X coordinate is zero. This geometric cancellation explains why a curved deterministic relation can have zero linear correlation.

## 25. Continuous covariance with a corrected center

On the unit square, $ f(x,y)=2x^3+2y^3 $. Compute covariance and correlation; show every required moment.

### Complete solution

The integral of the density is 1. Symmetry gives equal marginal means. Integrating $ x(2x^3+2y^3)$ yields $2/5+1/4=13/20 $. Integrating $ x^2f $ yields $1/3+1/6=1/2 $. Thus both variances are $1/2-169/400=31/400 $. Integrating $ xyf $ yields $1/5+1/5=2/5 $. Covariance is $2/5-169/400=-9/400 $ and correlation is $-9/31 $. The centered integral must use 13/20 in both factors; substituting 7/12 computes a different quantity. This independent recomputation corrects the inconsistent substitutions in the source example.

The negative covariance is plausible because mass increases near either coordinate's upper boundary, without concentrating only where both coordinates are large. The correlation remains inside the mandatory interval from minus one to one. This interpretation supports the computation but cannot replace the two-dimensional integrations.

## 26. Triangle support prevents independence

A pair is uniform on $0<x<y<1 $, with density 2 there. Compute its covariance.

### Complete solution

Integrate over $0<y<1 $ and $0<x<y $. The means are $ E[X]=\int_0^1 y^2,dy=1/3 $ and $ E[Y]=\int_0^1 2y^2,dy=2/3 $. For the mixed moment, the inner integral of $2xy $ is $ y^3 $, giving $ E[XY]=1/4 $. Thus covariance is $1/4-2/9=1/36 $. The constant density inside the triangle does not establish independence: the support imposes $ X<Y $. A rectangular factorization of the density including its support would be required. The marginals have variances 1/18 each, so the correlation is 1/2.

## 27. Linear combinations with a negative cross term

Given variances 4 and 9 and covariance 3, find $ Var(2X-Y)$ and $ Cov(2X-Y,X+Y)$.

### Complete solution

For the variance, the diagonal terms are 16 and 9 and the cross term is $2(2)(-1)(3)=-12 $, giving 13. For the covariance, expand each argument: $2Var(X)+2Cov(X,Y)-Cov(Y,X)-Var(Y)=8+6-3-9=2 $. The symmetry of covariance combines the middle terms. No independence is assumed, and setting the supplied covariance to zero would change both answers. Squared coefficients appear only on variance diagonals; mixed terms keep the product of coefficient signs.

## 28. Random shift is not deterministic translation

Independent $ X,Z $ have variances 4 and 1. Compare $ Var(X+3)$ and $ Var(X+Z)$. What changes if $ Cov(X,Z)=-1 $?

### Complete solution

The deterministic shift 3 contributes no centered randomness, so the first variance is 4. With independent random Z, the second variance is $4+1=5 $. If the variables instead have covariance $-1 $, the general sum formula gives $4+1+2(-1)=3 $. This covariance is feasible because its magnitude 1 does not exceed $\sqrt{4(1)}=2 $. A quantity labeled an error or a shift remains a random variable when it varies by trial; its name does not permit dropping its variance or covariance.

## 29. Sum and difference recover covariance

Suppose $ Var(X+Y)=20 $ and $ Var(X-Y)=8 $. Find $ Cov(X,Y)$ and $ Var(X)+Var(Y)$.

### Complete solution

Add the two identities to cancel covariance:$20+8=28=2(Var(X)+Var(Y))$, so the variance sum is 14. Subtract them to obtain $20-8=12=4Cov(X,Y)$, hence covariance 3. Individual variances are not determined by these two equations, although any proposed pair must sum to 14 and have product at least 9. The factor 4 in the subtraction comes from opposite cross terms $+2c $ and $-2c $, not from a squared scaling of either variable.

## 30. Covariance of a weighted overlap

Independent variables $ U,V,W $ have variances 1,2,3. Let $ X=2U-V+W $ and $ Y=U+3V $. Find covariance and $ Var(X+Y)$.

### Complete solution

Only shared primitive variables contribute to covariance: $ Cov(X,Y)=2(1)(1)+(-1)(3)(2)=-4 $. The individual variances are $4+2+3=9 $ and $1+18=19 $, so the sum variance is $9+19-8=20 $. Alternatively $ X+Y=3U+2V+W $, whose variance is $9+8+3=20 $. This independent check confirms the negative sign from V. Counting common variables without their coefficients would produce the wrong covariance.

Expanding the final sum directly provides a second primitive basis with coefficients three, two and one. Because those primitives are independent, only squared coefficients contribute. Agreement between this calculation and the covariance expansion is an effective way to detect missing factors or signs.

## 31. Impossible supplied correlation

Suppose $ Var(X)=4 $, $ Var(Y)=9 $, and $ Cov(X,Y)=7 $. Is this feasible? Produce a negative squared-residual variance.

### Complete solution

The centered Cauchy–Schwarz bound is $|c|\le\sqrt{4(9)}=6 $, so 7 is impossible. More constructively, minimize $ Var(X-tY)=4-14t+9t^2 $ at $ t=7/9 $. Its minimum is $4-49/9=-13/9 $, contradicting nonnegativity of variance. This gives a direct algebraic certificate. It is not necessary to search for a density or reject only correlations outside an intuitively plausible sample range; the moment inequality is mandatory for every real joint law.

The covariance bound is necessary before any variance calculation. A negative value for a chosen linear combination is a witness rejecting the entire proposed joint model, even if its individual means and variances look reasonable.

## 32. Perfect correlation fixes an affine relation

Variables have means 1 and 5, variances 4 and 9, and correlation 1. Determine Y in terms of X almost surely.

### Complete solution

Standardize the centered variables. Correlation 1 implies the variance of $(X-1)/2-(Y-5)/3 $ is zero. Its mean is zero, so it equals zero almost surely. Therefore $ Y-5=(3/2)(X-1)$, or $ Y=(3/2)X+7/2 $ almost surely. The slope uses the ratio of standard deviations 3/2, not the ratio of variances 9/4. If the correlation were $-1 $, the centered slope would be $-3/2 $. These conclusions require positive variances, as supplied.

## 33. Correlation under changing units

A pair has correlation $-2/5 $. Find the correlation of $ A=-3X+7 $ and $ B=2Y-4 $.

### Complete solution

Covariance is multiplied by $(-3)(2)=-6 $, while the standard-deviation product is multiplied by $|-3||2|=6 $. Thus the new correlation is the negative of the old one, equal to 2/5. Both positive scale magnitudes cancel, and fixed translations disappear. If both multipliers were negative, the sign would be retained. If either multiplier were zero, the new Pearson correlation would be undefined rather than zero because one variable would have zero standard deviation.

## 34. Bounds on a sum variance

Two variables have variances 4 and 9. Give the tight unrestricted interval for $ Var(X+Y)$ and construct both endpoints.

### Complete solution

The covariance lies between $-6 $ and 6, so the sum variance is $13+2c $, ranging from 1 to 25. For an attaining construction, let Z have mean 0 and variance 1, set X=2 Z and Y=3 Z for the upper endpoint, and Y=$-3Z $ for the lower endpoint. Then X+Y equals 5 Z or $-Z $. This establishes attainability when only the variances are prescribed. If full marginal laws were additionally fixed, the same interval is necessary but its endpoints need not be compatible with those specific marginals.

## 35. Normal marginals do not imply Gaussian independence

Let $ X $ be standard normal and S an independent fair sign. Set $ Y=SX $. Show that X,Y have normal marginals, zero covariance and dependence.

### Complete solution

Multiplying a symmetric standard normal by an independent fair sign preserves its marginal law, so Y is standard normal. Since S has mean zero, $ E[XY]=E[SX^2]=E[S]E[X^2]=0 $. Both means are zero, giving covariance zero. But $|Y|=|X|$ always. For example, the events $|X|\le1 $ and $|Y|\le1 $ coincide and have probability strictly between zero and one, so their joint probability is not the product. The Gaussian zero-covariance exception requires the pair to be jointly Gaussian; normal marginals alone are insufficient.

## 36. Zero-variance row

Suppose $ Var(X)=0 $ and $ Var(Y)=5 $. Determine $ Cov(X,Y)$ and whether correlation is defined.

### Complete solution

Zero variance implies X equals its mean almost surely. Therefore its centered product with Y is zero almost surely, giving covariance zero. This also follows from $ Cov(X,Y)^2\le0(5)$. Pearson correlation divides this covariance by $\sqrt0\sqrt5=0 $, so it is undefined. Assigning zero correlation would conflate a defined centered product with an undefined normalized ratio. In a covariance matrix, the same argument forces every entry in a zero-variance row and column to vanish.

## 37. Uncorrelated variables with independent sums?

Let U,V be independent fair signs. Put X=U and Y=UV. Are X,Y independent? Are X,Y and Z=V mutually independent?

### Complete solution

The four combinations of U,V give each pair(X,Y) in ${-1,1}^2 $ once, so X and Y are independent. Likewise every pair among X,Y,Z is independent. ButXYZ equals $ U(UV)V=1 $ identically. Three independent fair signs would have product 1 with probability 1/2, so the triple is not mutually independent. Their pairwise covariances vanish, and variance of their sum is still 3. Finite sum variance uses pairwise second moments and cannot detect this higher-order dependence.

## 38. Optimal linear prediction error

Given $ Var(X)=16 $, $ Var(Y)=9 $, and $ Cov(X,Y)=6 $, find the best centered coefficientb for predicting X byb Y and its residual variance.

### Complete solution

For centered variables, $ Var(X-bY)=16-12b+9b^2 $. Complete the square: this is $9(b-2/3)^2+12 $. Hence $ b=2/3 $ minimizes the error and the residual variance is 12. Equivalently correlation is $6/(4\cdot3)=1/2 $, giving $16(1-1/4)=12 $. If the means are nonzero, add intercept $ E[X]-bE[Y]$. The residual is uncorrelated with Y at the optimum, but without extra distributional assumptions it need not be independent.

The minimizing condition also makes covariance of the residual with the predictor equal to zero. Differentiating the risk and checking that covariance give the same coefficient, linking optimization to the orthogonality condition rather than treating the regression formula as memorized.

## 39. A misleading average-correlation claim

Every variable has variance 1 and every distinct pair has covariance $-1/2 $. For which $ n\ge2 $ can this structure be feasible?

### Complete solution

The equicorrelation matrix has eigenvalue $1+(n-1)(-1/2)=(3-n)/2 $ along the all-ones direction and eigenvalue 3/2 in orthogonal directions. Positive semidefinite ness therefore requires $ n\le3 $. Bothn=2 andn=3 are realizable by a Gaussian construction, with singularity atn=3. Forn=4 the variance of the sum is $4+4(3)(-1/2)=-2 $, impossible. A fixed negative pair covariance cannot be repeated across arbitrarily many variables without violating a collective constraint.

At the singular endpoint, the centered sum is zero almost surely. Individual variables can remain random, with their movements constrained to cancel. Positive diagonal entries therefore do not imply a positive definite matrix.

## 40. Covariance can vanish by cancellation

Variables X,Y,Z have variances 1,1,2 with $ Cov(X,Z)=1 $ and $ Cov(Y,Z)=-1 $. Find $ Cov(X+Y,Z)$. Does its value prove independence?

### Complete solution

Bilinearity gives $ Cov(X+Y,Z)=1-1=0 $. This is cancellation of two associations, not an independence proof. One feasible construction uses independent mean-zero variance-one X,Y and Z=X−Y. Then the supplied moments hold, while X+Y and Z need not be independent for non-Gaussian primitive laws. For fair signs, the sum being zero forces Z to be nonzero, and a nonzero sum forces Z to be zero, establishing dependence. The covariance calculation is exact in either case, but its probabilistic interpretation must remain limited.

## 41. Fixed-point variance and its boundary

Let F count fixed points in a uniform random permutation ofn labels. Derive its variance for n≥2 and evaluate separately atn=1.

### Complete solution

Write F as a sum ofn fixed-point indicators. Each has probability 1/n. For distinct labels, fixing both leaves(n−2)! permutations, so the intersection probability is $1/[n(n-1)]$. Because indicator squares equal indicators, $ E[F^2]=n(1/n)+n(n-1)/[n(n-1)]=2 $. With mean 1, variance is 1. Forn=1 the single permutation fixes the only label, so F is identically 1 and variance 0. The pair-intersection formula has no distinct pair at that boundary and cannot be substituted there.

## 42. Binomial variance without its mass function

Show thatn independent Bernoulli(p) trials have count variance $ np(1-p)$. What independence strength is needed for this variance?

### Complete solution

LetI_i indicate success. Each indicator has variance $ p(1-p)$ because its second moment equals its meanp. The count variance is the sum of those diagonals plus twice all pair covariances. Independent trials make every pair covariance zero, giving $ np(1-p)$. Pairwise independence already suffices for this particular second-moment result. However, identifying the full count distribution as binomial normally uses mutual independence; a pairwise-independent family can have the same variance and a different count law.

## 43. Mutually exclusive events

Three mutually exclusive events each have probability 1/4. Find the variance of their indicator sum.

### Complete solution

The sum is the indicator of their union because at most one event occurs. Its success probability is 3/4, so variance is $(3/4)(1/4)=3/16 $. The covariance method gives three diagonals of 3/16 and three unordered off-diagonal covariances $-1/16 $, doubled: $9/16-6/16=3/16 $. The negative covariances express mutual exclusion. Summing only the diagonals would falsely treat these events as independent. Mutually exclusive positive-probability events cannot be independent.

## 44. Empty boxes with exact covariance

Three balls independently choose one of two boxes uniformly. Find the variance of the number of empty boxes.

### Complete solution

Let I 1,I 2 indicate emptiness. Each box is empty only if all three balls choose the other, givingp=1/8. Both boxes cannot be empty, so their intersection probability is 0 and covariance $-1/64 $. Hence the variance of I 1+I 2 is $2(1/8)(7/8)+2(-1/64)=12/64=3/16 $. Alternatively the count is 1 if all balls agree, with probability 1/4, and 0 otherwise. Its Bernoulli variance is 3/16. The two derivations cross-check the dependence signs and count convention.

## 45. Runs of successes share a trial

In four independent fair tosses, let S count adjacent pairs that are both heads. Compute its variance.

### Complete solution

There are three indicators, each with success probability 1/4 and variance 3/16. Neighboring pair indicators overlap in one toss; their joint success probability is 1/8, so covariance is $1/8-1/16=1/16 $. The first and third use disjoint tosses and have covariance zero. There are two overlapping unordered pairs. Thus variance is $3(3/16)+2(2)(1/16)=13/16 $. Independence of tosses does not make these derived overlapping indicators independent. A careful overlap graph prevents counting the middle overlap twice before the outer factor 2.

## 46. Without-replacement success count

A population of 10 entries contains 4 successes. Three distinct entries are sampled uniformly. Find the count mean and variance.

### Complete solution

Each draw has success probabilityp=2/5, so the count mean is $3p=6/5 $. For distinct draws, covariance is $-p(1-p)/(N-1)=-(6/25)/9=-2/75 $. Therefore variance is $3(6/25)+2\binom32(-2/75)=18/25-4/25=14/25 $. Equivalently use the finite-population correction $3(2/5)(3/5)(7/9)=14/25 $. The corresponding replacement model would have variance 18/25. The mean alone cannot distinguish the two sampling mechanisms.

The sign of the covariance follows from a depleted population: observing a success slightly reduces the probability of another success. The variance stays nonnegative and decreases relative to replacement sampling. The correction tends toward one for a small sample from a large population.

## 47. A complete sample has no count variability

Use indicator covariances to explain why sampling all N population entries without replacement gives a deterministic success count K.

### Complete solution

Each draw indicator has variance $ p(1-p)$, and each distinct pair has covariance $-p(1-p)/(N-1)$ when N>1. The variance of the count is $ Np(1-p)+N(N-1)[-p(1-p)/(N-1)]=0 $. The N(N−1) factor counts ordered cross terms; equivalently double the unordered count. The cancellation reflects that every success is included exactly once, giving count K. For N=1, the conclusion is checked directly. One must not invoke the denominator N−1 at that boundary.

## 48. Numerical finite-population mean

A population is $\{0,2,4,6\}$. Two entries are sampled without replacement and averaged. Find the variance of that mean.

### Complete solution

The population mean is 3 and population variance is $(9+1+1+9)/4=5 $. For sample sizen=2 from N=4, the sample mean variance is $(5/2)(4-2)/(4-1)=5/3 $. As a direct check, the six unordered pairs give means 1,2,3,3,4,5. Their average is 3 and their squared deviations sum to $4+1+0+0+1+4=10 $, yielding 10/6=5/3. A population variance convention using denominator 3 would equal 20/3 and must first be converted before using this formula.

Every unordered pair has the same probability, because uniform ordered draws produce each pair in two orders. Those two orders have the same mean and can be combined. This explains why averaging six pair means is a valid direct enumeration.

## 49. Record minima indicators

In a uniform random permutation ofn distinct numbers, let R count new running minima. Explain why $ Var(R)=H_n-\sum_{i=1}^n1/i^2 $.

### Complete solution

The event at positioni has probability 1/i. Fori<j, the relative ordering of the firstj values is uniform. Conditional on the minimum being atj, the remaining firstj−1 positions retain uniform relative order, so the probability that positioni was an earlier record is 1/i. Thus pair intersection probability is 1/(ij), giving zero pair covariance. Variance is the sum of indicator variances $\sum_i(1/i)(1-1/i)=H_n-\sum_i1/i^2 $. This derivation establishes the second-moment claim by pairwise reasoning; expectation alone would not justify it.

## 50. Count covariance in disjoint categories

In m independent trials, each falls in category A with probabilityp and B with probabilityq, where categories are disjoint. Find $ Cov(N_A,N_B)$.

### Complete solution

Use one pair of category indicators for each trial. Indicators from different trials are independent and contribute zero covariance. Within the same trial the intersection probability is zero, so covariance is $-pq $. There arem such diagonal trial pairs, giving $ Cov(N_A,N_B)=-mpq $. This covariance is negative despite independence of the trials. For category unions, $ Var(N_A+N_B)=m(p+q)(1-p-q)$, consistent with summing the individual binomial variances and twice the negative covariance.

## 51. Conditional variance misses group separation

Group Z has probabilities 1/4 and 3/4. Conditional means are 0 and 4 and conditional variances 1 and 9. Find total mean and variance.

### Complete solution

The mean is $(1/4)0+(3/4)4=3 $. Expected conditional variance is $(1/4)1+(3/4)9=7 $. The conditional-mean variable takes 0 and 4 with the group masses, so its variance is $(1/4)(0-3)^2+(3/4)(4-3)^2=3 $. The total variance is therefore 10. Directly the conditional second moments are 1 and 25, giving unconditional second moment 19 and variance $19-3^2=10 $. Averaging the group variances alone would report 7 and omit the between-group component.

The direct second-moment check uses conditional second moment equal to conditional variance plus squared conditional mean. Averaging those second moments and subtracting the squared global mean provides an independent route to the same total variance.

## 52. A uniform conditional interval

Draw $ Z\sim U(0,1)$ and then $ X\mid Z=z\sim U(z,1)$. Find $ E[X]$ and $ Var(X)$.

### Complete solution

The conditional mean is $(1+Z)/2 $, so its expectation is 3/4 and its variance is $ Var(Z)/4=1/48 $. Conditional variance is $(1-Z)^2/12 $, whose expectation is $(1/12)\int_0^1(1-z)^2,dz=1/36 $. The total variance is $1/36+1/48=7/144 $. These are different sources of spread: random interval centers and randomness within a chosen interval. The endpoint Z=1 has probability zero and can be assigned a degenerate conditional law without changing the result.

The uniform distribution within each interval has variance equal to its width squared divided by twelve. Integrating that expression over the distribution of the lower endpoint is different from first averaging the widths and then squaring.

## 53. Beta-Bernoulli mixture without naming beta

Choose $ P\sim U(0,1)$ and then one Bernoulli(P) outcome X. Find its variance using total variance.

### Complete solution

Conditional on P, the mean is P and the variance is P(1−P). The expected conditional variance is $1/2-1/3=1/6 $, while variance of the conditional mean is $ Var(P)=1/12 $. Their sum is 1/4. This agrees with the unconditional outcome being a fair Bernoulli, because its success probability is $ E[P]=1/2 $. Randomizing a single trial's success probability does not create a new variance beyond that binary law, but it can create dependence between multiple trials sharing the same P.

## 54. Shared latent probability induces dependence

Given one latent $ P\sim U(0,1)$, draw X,Y conditionally independent Bernoulli(P). Find their covariance and the variance of X+Y.

### Complete solution

The conditional covariance is zero by conditional independence. Both conditional means equal P, so total covariance is $ Var(P)=1/12 $. Each unconditional outcome is Bernoulli(1/2), with variance 1/4. Thus $ Var(X+Y)=1/4+1/4+2(1/12)=2/3 $. The joint probability of two successes is $ E[P^2]=1/3 $, not the product 1/4. This gives both a moment argument and a direct failure of unconditional independence. Resampling a new independent P for each trial would describe a different model.

## 55. Random sum with nonzero increment mean

Let N have mean 5 and variance 2, independent of iid increments of mean 3 and variance 4. Find the sum variance.

### Complete solution

Given N, the sum mean is 3 N and its variance 4 N. Averaging the conditional variances gives 20. The variance of conditional means is $ Var(3N)=9(2)=18 $. Thus the total variance is 38 and the mean is 15. Replacing N by its mean 5 would retain only 20 and miss count variation. The formula requires independence of N from the entire increment sequence and enough finite moments; it does not automatically apply when the stopping count is chosen from observed increments.

## 56. Zero-mean random sum

N is independent of iid increments with mean 0 and variance 7, and $ E[N]=3 $. Why does the sum variance equal 21 even without a finite $ Var(N)$?

### Complete solution

Conditional means are zero for every count, so the between-count variance is zero. Conditional squared sums have expectation 7 N, and averaging gives 21. Finite E[N] ensures a finite second moment of the sum under the stated independence and iid assumptions, even if N has an infinite second moment. The general nonzero-mean formula would require more count information. Avoid writing an ambiguous product $0\cdot\infty $; derive the zero conditional-mean term directly rather than multiply an undefined or infinite count variance.

## 57. Compound Poisson variance

Let N be Poisson( $\lambda $ ), independent of iid increments with mean $\mu $  and variance v. Derive the variance and contrast it with $\lambda $ v.

### Complete solution

Poisson N has mean and variance $\lambda $ . Total variance gives $\lambda v+\lambda\mu^2=\lambda E[X_1^2]$. The sum mean is $\lambda $  $\mu $ . The term $\lambda $  $\mu $ ² accounts for the random number of nonzero-average increments; it does not disappear merely because the count is independent. When increments are deterministically equal to 1, the sum equals N and its variance must be $\lambda $ , while the incomplete $\lambda $ v formula would give zero. That degenerate test quickly exposes the missing term.

## 58. Conditional mean can be constant without independence

Let Z be a fair binary group. Given Z=0, X is a fair sign; given Z=1, X is equally likely±2. Show that $ E[X\mid Z]$ is constant but X,Z are dependent.

### Complete solution

Both conditional laws are symmetric, so the conditional mean is 0 in both groups. However the conditional variances are 1 and 4, and the value of $|X|$ determines the group. For example $ P(|X|=1\mid Z=0)=1 $ but its unconditional probability is 1/2. Thus constant conditional mean does not imply independence. The unconditional variance is the average within variance $(1+4)/2=5/2 $, since the variance of conditional means is zero. Mean independence is weaker than equality of the entire conditional distribution.

## 59. More information cannot increase best squared prediction risk

Suppose information sets G⊆H and X is square-integrable. Explain why $ E[Var(X\mid H)]\le E[Var(X\mid G)]$.

### Complete solution

Conditional expectation minimizes squared error among predictors measurable with respect to its information set. Every G-measurable predictor is also H-measurable, so enlarging the set of permitted predictors cannot raise the minimum. Equivalently apply the orthogonal decomposition to the nested conditional means: the old residual risk equals the new residual risk plus $ E[(E[X\mid H]-E[X\mid G])^2]$. The additional term is nonnegative. This comparison is about expected conditional variance; pointwise conditional variances for particular observed values need not be ordered.

## 60. Total covariance can cancel

Two equally likely groups have conditional mean pairs(0,0) and(2,2), and each group's conditional covariance is−1. What is the overall covariance? What feasibility must be checked?

### Complete solution

The average within-group covariance is−1. The two conditional-mean variables are identical with values 0 and 2, each having variance 1, so their covariance is 1. Total covariance is zero. This does not prove independence because dependence can persist inside groups and through membership. To realize the given within covariance, each group's marginal variances must have product at least 1. For example unit conditional variances with perfectly opposite centered residuals achieve−1. Specifying covariances without feasible conditional variances would not define a valid joint model.

## 61. Variance from a covariance matrix

A centered vector has covariance $\Sigma=\begin{pmatrix}4&1\\1&2\end{pmatrix}$. Find the variance of $3X-2Y $.

### Complete solution

Use the quadratic form with coefficient vector(3,−2). The diagonal contributions are $9(4)=36 $ and $4(2)=8 $. The off-diagonal contribution is $2(3)(-2)(1)=-12 $. The variance is 32. Matrix feasibility holds because the diagonal entries are positive and determinant $8-1=7>0 $. Checking feasibility first protects against calculating a formally plausible number from impossible supplied moments. The quadratic form summarizes covariance algebra; it does not assert independence because the off-diagonal entry is nonzero.

## 62. Pairwise bounds are insufficient

A three-by-three matrix has diagonal 1 and all off-diagonals−3/4. Show that every pair passes the correlation bound but the matrix is not a covariance matrix.

### Complete solution

Each two-by-two principal block has determinant $1-9/16=7/16>0 $, so each pair is feasible by itself. But the all-ones vector produces quadratic form $3+6(-3/4)=-3/2 $, a negative proposed variance. Hence the full matrix is not positive semidefinite and cannot be a covariance matrix. Its eigenvalue along the all-ones direction is−1/2. Testing only individual correlation magnitudes misses a collective linear-combination constraint.

## 63. A three-correlation parameter interval

A correlation matrix has correlations $ r_{12}=r_{13}=1/2 $ and $ r_{23}=t $. Determine the full feasible interval fort.

### Complete solution

The determinant is $1+2(1/2)(1/2)t-1/4-1/4-t^2=1/2+t/2-t^2 $. Nonnegativity factors as $-(t-1)(t+1/2)\ge0 $, giving $-1/2\le t\le1 $. Within this interval all two-by-two principal minors are also nonnegative, so the symmetric matrix is positive semidefinite. Its Gaussian factorization supplies an unrestricted realization, including singular endpoints. The pairwise condition $|t|\le1 $ alone would incorrectly allowt below−1/2.

At the upper endpoint, the second and third standardized variables can coincide. At the lower endpoint, a different centered linear relation makes the matrix singular. Both endpoints are allowed for covariance matrices even though a nonsingular joint Gaussian density would fail there.

## 64. Covariance under an affine matrix map

Independent centered X,Y have variances 1 and 4. Set U=X+Y and V=2 X−Y. Find their covariance matrix.

### Complete solution

The two transformed variances are 5 and 8. Their covariance is $2Var(X)-Var(Y)=2-4=-2 $. Hence the matrix has diagonal 5,8 and off-diagonal−2. In matrix notation A has rows(1,1) and(2,−1); multiplication $ A\mathrm{diag}(1,4)A^T $ gives the same result. The determinant is $40-4=36>0 $, matching invertibility of A and positive primitive variances. Adding fixed offsets to U,V would leave this covariance matrix unchanged.

The negative off-diagonal term has a concrete source: Y enters the first output positively and the second output negatively. Its covariance contribution outweighs the positive shared contribution from X. Transformed independence should therefore not be assumed from primitive independence.

## 65. Singular covariance does not mean deterministic components

Let Y=2 X+1 with $ Var(X)=3 $. Find the pair covariance matrix and a centered null combination.

### Complete solution

The variances are 3 and 12, and covariance 6. The matrix is singular because its determinant is $36-36=0 $. Yet neither variable is deterministic: both variances are positive. The coefficient vector(−2,1) gives a zero quadratic form because Y−2 X equals the constant 1. After subtracting means, that linear combination equals zero almost surely. Singularity describes a deterministic relation among components, not necessarily a zero-variance component.

## 66. Realizing an arbitrary feasible pair

Construct centered variables with variances 4,9 and covariance−3 using independent standard normal Z 1,Z 2.

### Complete solution

Set X=2 Z 1 and Y=$-3Z1/2+(3\sqrt3/2)Z2 $. The variance of Y is $9/4+27/4=9 $, while covariance with X is $2(-3/2)=-3 $. Centered means are zero by construction. The coefficient of Z 2 is real because the desired covariance satisfies $9-(-3)^2/4\ge0 $. This explicitly realizes the supplied covariance matrix. A construction from normal primitives is one feasible law; it does not show that every law with these moments is Gaussian.

Check the mixed term separately: the independent second normal contributes no covariance with X, while the shared first normal determines the entire supplied negative covariance. This separates the correlated part from the additional variation needed to reach the stated Y variance.

## 67. Optimal convex averaging weight

Two unbiased estimators have variances 4 and 9 and covariance 3. Find the variance-minimizing weight in $ wX+(1-w)Y $, constrained to 0≤w≤1.

### Complete solution

The variance is $4w^2+9(1-w)^2+6w(1-w)=7w^2-12w+9 $. Its derivative vanishes atw=6/7, which lies inside the allowed interval. Completing the square gives minimum $9-36/7=27/7 $. The covariance changes the optimum from the independence weight 9/13. Because the quadratic coefficient 7 is positive, this is a unique minimum. Feasibility follows from $3^2\le4(9)$. Coefficients sum to one, preserving the common expectation.

At the optimum, small shifts of weight in either direction raise the variance by seven times the squared shift. The complete quadratic therefore verifies both optimality and the numerical minimum rather than relying only on a zero derivative.

## 68. Unrestricted weight outside the interval

Two estimators have variances 1 and 4 and covariance 3/2. Find the best unrestricted weight and the best convex weight.

### Complete solution

The denominator $ v_X+v_Y-2c=1+4-3=2 $ is positive. The unconstrained weight is $(4-3/2)/2=5/4 $, outside[0,1]. The variance quadratic is $2w^2-5w+4 $ and reaches minimum 7/8 atw=5/4. Under the convex constraint it decreases up to the right boundaryw=1, where variance is 1. Negative weight on Y can exploit covariance in the unconstrained problem, but is not permitted in the convex problem. The supplied covariance is feasible since 3/2≤2.

## 69. Degenerate averaging denominator

Two variables have the same mean and $ Var(X-Y)=0 $. Show that every combination $ wX+(1-w)Y $ has the same variance.

### Complete solution

Zero variance means X−Y is constant almost surely. Its expectation is zero because the means match, so X=Y almost surely. Every stated combination therefore equals X almost surely, regardless ofw, and has varianceVar(X). In the formula for an optimal weight, the denominator $ v_X+v_Y-2c $ is exactlyVar(X−Y)=0, so division would be invalid. The variance polynomial is flat rather than a strictly convex optimization problem. Without equal means the difference could be a nonzero constant, but the variance would still be independent ofw.

## 70. Identical observations versus independent observations

Four measurements each have variance 9. Find the mean variance when they are independent, when they are identical, and when every pair covariance is 3.

### Complete solution

For independent measurements, the sum variance is 36 and the mean divides it by 16, giving 9/4. For identical measurements, the mean equals the common measurement and variance is 9. With pair covariance 3, sum variance is $4(9)+2\binom42(3)=36+36=72 $, giving mean variance 9/2. The covariance matrix in the third case is feasible, with eigenvalues 18 along the common direction and 6 orthogonally. Repetition does not guarantee a 1/n variance reduction without controlling dependence.

## 71. Chebyshev with a strict complement

A variable has mean 5 and variance 4. Give a guaranteed lower bound for $ P(1<X<9)$ and explain endpoint atoms.

### Complete solution

The requested open interval is $|X-5|<4 $. Its complement is the non-strict event $|X-5|\ge4 $, bounded by $4/16=1/4 $. Therefore the desired probability is at least 3/4. A law with masses 1/8 at 1 and 9 and mass 3/4 at 5 attains equality. Endpoint atoms belong to the complement, so changing the interval to closed endpoints would change this attaining law's probability. Chebyshev gives a guaranteed bound from the moments; it does not state that every law reaches 3/4.

## 72. Cantelli versus Chebyshev

A centered variable has variance 4. Compare bounds for $ P(X\ge3)$ from Chebyshev and Cantelli, and exhibit an attaining Cantelli law.

### Complete solution

Chebyshev bounds the larger two-sided event by 4/9, so it also bounds the one-sided event by 4/9. Cantelli improves this to $4/(4+9)=4/13 $. An attaining two-point law assigns probability 4/13 to 3 and 9/13 to $-4/3 $. Its mean is $12/13-12/13=0 $ and its second moment is $36/13+16/13=4 $. The lower point balances the mean while all the tail probability sits exactly at the threshold. The event is non-strict; a strict version requires attention to that atom.

## 73. A sufficient sample size

Independent observations have common mean $\mu $  and variance 9. Find an integer sample size sufficient for $ P(|\bar X-\mu|\ge0.5)\le0.01 $ using only these moments.

### Complete solution

The sample mean variance is 9/n. Chebyshev gives tail bound $9/(n\cdot0.25)=36/n $. Requiring this at most 0.01 yields $ n\ge3600 $, so 3600 is a sufficient integer size. This is a worst-case moment-based guarantee, not a statement that every distribution needs exactly 3600 observations. A known Gaussian model or other stronger assumptions could yield a smaller sample size. Using 9 rather than 9/n would ignore averaging; dividing by the error tolerance rather than its square would misuse the inequality.

## 74. Markov requires nonnegativity

A centered fair sign X has mean 0. Why is the purported Markov bound $ P(X\ge1)\le E[X]/1=0 $ invalid?

### Complete solution

The actual probability is 1/2. Markov's inequality requires a nonnegative random variable, while X can equal−1. Its mean cancels positive and negative values, so it cannot upper-bound a positive-event probability in this way. A valid application uses $ X^2 $, which is identically 1 and gives only the uninformative bound 1 for $ P(|X|\ge1)$. Cantelli, using the mean and variance, gives 1/2 for the one-sided threshold 1 and is sharp here. The failure is a missing theorem hypothesis, not a contradiction in probability.

## 75. Strict versus non-strict sharpness

For the law with masses 1/8 at±2 and 3/4 at 0, compare $ P(|X|\ge2)$, $ P(|X|>2)$, and the Chebyshev bound.

### Complete solution

The mean is zero and variance 1. The non-strict tail includes both endpoint masses, giving 1/4, exactly the Chebyshev bound 1/4. The strict tail includes no supported value and is zero. The same variance bound still bounds that smaller event, but the given law does not attain it. To approach sharpness for a strict threshold, move the outer atoms to±(2+ $\epsilon $ ) and adjust their masses to preserve variance 1; their tail probability approaches 1/4 as $\epsilon $  decreases. An attained maximum and a limiting supremum are different claims.

## 76. Absolute displacement is not root mean square

For two independent fair signs, let S be their sum. Find $ E[|S|]$ and $\sqrt{E[S^2]}$.

### Complete solution

The sum takes−2,0,2 with probabilities 1/4,1/2,1/4. Thus expected absolute displacement is $2(1/4+1/4)=1 $. The second moment is $4(1/4+1/4)=2 $, so root mean square is $\sqrt2 $. They are unequal because square root is nonlinear and does not commute with expectation. Cauchy–Schwarz guarantees $ E[|S|]\le\sqrt{E[S^2]}$, with strict inequality here because $|S|$ is not constant. The ensemble, not one walk realization, determines these moments.

The root-mean-square quantity measures a quadratic average over all outcomes. The absolute-value quantity is a linear average after taking absolute values. Rare large displacements affect the quadratic average more strongly, so the two measures need not agree.

## 77. Biased random walk

Six independent steps are+1 with probability 3/4 and−1 otherwise. Find the final mean and variance.

### Complete solution

One step has mean $2(3/4)-1=1/2 $ and second moment 1, hence variance $1-1/4=3/4 $. Six independent steps give mean 3 and variance $6(3/4)=9/2 $. The second moment of the final position is $9/2+3^2=27/2 $, distinct from its variance because its mean is nonzero. Replacing the root-mean-square position by the standard deviation would conflate spread around zero with spread around the drifted mean.

The largest and smallest possible positions are six and minus six. The computed mean lies inside that support, and the variance is below the sharp support-width bound. These checks are necessary but do not replace the independence calculation.

## 78. Perfectly correlated random-walk steps

All six steps repeat one initial fair sign. Find the mean, variance and standard deviation of the final position.

### Complete solution

The position is 6 Z, where Z is a fair sign. Its mean is 0, variance 36 and standard deviation 6. Alternatively six diagonal variances contribute 6 and the 30 ordered off-diagonal covariances contribute 30, totaling 36. The independent-step variance 6 is inapplicable because the same sign controls every step. The path can move only to−6 or 6, not to the intermediate endpoints of an independent walk. This contrast shows how primitive dependence changes both the second moment and the complete support.

## 79. Finite-variance weak-law proof

Prove convergence in probability of the iid sample mean to $\mu $  when the common variance v is finite. Identify what the proof does not establish.

### Complete solution

The sample mean has expectation $\mu $  and variance v/n. For every fixed $\epsilon $ >0, Chebyshev bounds $ P(|\bar X_n-\mu|\ge\epsilon)$ by $ v/(n\epsilon^2)$, which tends to zero. That is convergence in probability. This argument does not establish almost-sure convergence, and it does not prove the general finite-mean weak law when variance is infinite. It also does not give an exact normal distribution at any finite n. The fixed positive tolerance is essential; choosing a shrinking $\epsilon $ _n requires rechecking whether the bound still tends to zero.

## 80. Changing tolerance changes the guarantee

With iid variance v>0, let $\epsilon_n=n^{-1/4}$ or $ n^{-1}$. What does the Chebyshev bound imply in each case?

### Complete solution

The bound is $ v/(n\epsilon_n^2)$. For $ n^{-1/4}$ it equals $ v/\sqrt n $, which tends to zero, giving concentration at that shrinking tolerance. For $ n^{-1}$ it equals vn, clipped at 1, and is uninformative. An uninformative upper bound does not prove that the event probability fails to vanish; it only means this inequality cannot decide the question. Distinguish a theorem's conclusion from a weakness of the chosen estimate. Distribution-specific behavior at very small tolerances requires additional analysis.

## 81. Probability-generating second moment

A nonnegative integer variable has $ G(z)=1/4+z/2+z^3/4 $. Compute mean and variance using derivatives and direct moments.

### Complete solution

Differentiate to get $ G'(1)=1/2+3/4=5/4 $ and $ G''(1)=6/4=3/2 $. The raw second moment is the factorial second moment plus the first moment: $ E[X^2]=3/2+5/4=11/4 $. Therefore variance is $11/4-25/16=19/16 $. Directly the support 0,1,3 with masses 1/4,1/2,1/4 gives those same moments. Using $ G''(1)$ alone as the raw second moment would omit the diagonal contribution X in $ X^2=X(X-1)+X $.

The constant term represents a possible zero outcome and contributes to normalization even though it contributes nothing to positive moments. The first and second derivatives must be evaluated at one, not zero, when using a probability-generating function to recover these moments.

## 82. Moment-generating curvature

A variable has MGF $ M(t)=\exp(2t+3t^2/2)$. Compute its mean and variance from M and fromlog M.

### Complete solution

The logarithm K(t) equals $2t+3t^2/2 $, so $ K'(0)=2 $ and $ K''(0)=3 $. Direct differentiation gives $ M'(0)=2 $ and $ M''(0)=2^2+3=7 $, yielding variance $7-4=3 $. The curvature oflog M is the centered second moment, whereas the second derivative of M is the raw second moment. The given function is the MGF of a normal with mean 2 and variance 3, but identifying that family is not needed for this moment calculation.

The MGF equals one at zero, which is required for a probability law. The logarithm's first two derivatives eliminate products generated by differentiation of the exponential, explaining why its second curvature directly isolates variance.

## 83. Why the denominator n−1 appears

For iid variables with variance v, derive the expectation of $\sum_i(X_i-\bar X)^2 $ and state the validn range for unbiased sample variance.

### Complete solution

Expand around the true mean $\mu $ . The exact identity is $\sum_i(X_i-\bar X)^2=\sum_i(X_i-\mu)^2-n(\bar X-\mu)^2 $. Expectations give $ nv-n(v/n)=(n-1)v $. Dividing by n−1 therefore yields an unbiased estimator of v for n>1. Dividing by n describes the empirical distribution variance and has expectation $(n-1)v/n $. At n=1 the centered sum is zero, but the unbiased formula is undefined. Dependence would change the variance of the sample mean and invalidate this derivation's simplification.

## 84. One streaming update, two centers

Apply Welford updates to the equally weighted observations 2,4,8. Report mean, centered sum $ M_2 $, empirical variance and unbiased sample variance.

### Complete solution

After 2, count 1, mean 2 and $ M_2 $=0. After 4, delta 2 and new mean 3 give increment $2(4-3)=2 $, so $ M_2 $=2. After 8, delta 5 and new mean 14/3 give increment $5(8-14/3)=50/3 $. Thus M 2=56/3. The empirical variance is 56/9; the unbiased sample variance is 28/3. A direct centered-square sum confirms $ M_2 $. The second factor in each increment uses the updated mean; using delta twice would overcount dispersion. These are empirical-data calculations, not a claim about an unknown population law.
