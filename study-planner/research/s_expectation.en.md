# Expectation, Linearity, Indicators, and Moments

## 1. Sources, scope, and how to study this chapter

This chapter synthesizes genuinely inspected written material from four core university courses: Oxford Prelims Probability, MIT 18.05, UC Berkeley CS70, and CMU 36-700. Cornell CS2800 provides an additional finite-experiment cross-check. The [source audit](../reviews/s_expectation-sources.html) records the located candidate pool, exact reading scopes, selection reasons, acquisition evidence, and corrections. A title or syllabus alone does not count as a reviewed course. The prose, proofs, numerical examples, questions, and simulations below are independently written.

Prerequisites are the event axioms, conditional probability for positive-probability events, finite counting, convergent geometric series, and the previous chapter's random-variable and PMF definitions. Read Sections 2–8 before the counting applications. Then study the worked problems by family, and revisit the final rules with their stated hypotheses. The laboratory is a way to inspect a calculation; its finite demonstrations are not substitutes for the symbolic proofs.

The scheduled topic is expectation and its linearity. Moments, variance identities, a finite partition rule, and simple expectation bounds are included to explain what expectation does and does not determine. Full covariance theory, joint continuous distributions, conditional expectation as a random variable, convergence theorems, and statistical inference remain separate chapters. No finite course pool or practice bank can certify universal success on unseen questions.

## 2. A weighted average with a precise meaning

Let a discrete random variable $X$ have distinct atoms $x_j$ with masses $p_j=P(X=x_j)$. The masses must be nonnegative and sum to one. For finite support, define

$$\mu=E[X]=\sum_j x_jp_j.$$

The operation multiplies each value by the probability of that value, then adds the signed contributions. It does not average the list of labels unless those labels are equally likely. If elementary outcomes have different weights, use those weights even when several outcomes map to the same value. Expectation is a property of the probability law and the specified measurement, not a prediction of the next outcome.

For atoms $-2,1,4$ with masses $1/5,1/2,3/10$, the contributions are $-2/5,1/2,6/5$, so $E[X]=13/10$. The mean is neither an atom nor the most likely value. The most likely value is $1$. A location summary alone loses information: a variable constantly equal to zero and a fair variable taking values $-100,100$ have the same mean and very different behavior.

The physical balance interpretation is exact. Place mass $p_j$ at coordinate $x_j$. The total signed torque about a proposed balance coordinate $c$ is $\sum_jp_j(x_j-c)=\mu-c$. It vanishes precisely at $c=\mu$. For support contained in $[a,b]$, multiplying $a\le X\le b$ by nonnegative masses and summing proves $a\le\mu\le b$. A finite mean can lie in the convex hull without belonging to the support.

<!-- SIM: mean -->

## 3. Finite means, extended means, and undefined means

An infinite support requires a convergence check. Define the nonnegative parts $X^+=\max(X,0)$ and $X^-=\max(-X,0)$, so $X=X^+-X^-$ and $|X|=X^++X^-$. There are three different contracts:

| Positive-part mean | Negative-part mean | Conclusion |
|---|---|---|
| Both finite | Both finite | A finite, order-independent expectation exists |
| Infinite | Finite | Extended expectation is positive infinity |
| Finite | Infinite | Extended expectation is negative infinity |
| Infinite | Infinite | Expectation is undefined; infinity minus infinity is not a number |

Thus a finite mean requires $\sum_j|x_j|p_j<\infty$. Absolute convergence permits regrouping atoms, changing their order, and separating finite linear combinations. A convergent symmetric principal value does not repair an undefined expectation. Some introductory texts say that an infinite mean “does not exist”; here that means that no finite expectation exists. We retain the distinction between a legitimate extended mean and an undefined signed mean.

For $P(X=2^k)=2^{-k}$, $k\ge1$, normalization follows from the geometric series, but each mean contribution equals one. Therefore $E[X]=+\infty$. For the symmetric law $P(X=\pm2^k)=2^{-k-1}$, both positive and negative means diverge. Pairing the two signs produces zero in each finite symmetric truncation, but the full expectation is undefined. This is why a bare symmetry argument is insufficient.

<!-- SIM: existence -->

## 4. From outcome weights to value weights

On a finite or countable elementary outcome space, expectation may also be written as $\sum_{\omega}X(\omega)P(\{\omega\})$. Group all outcomes with the same value. Their events are disjoint, and their probabilities sum to $P(X=x)$. Consequently

$$\sum_{\omega}X(\omega)P(\{\omega\})=\sum_x x\sum_{\omega:X(\omega)=x}P(\{\omega\})=\sum_x xP(X=x).$$

For countable signed sums this regrouping uses absolute convergence. For nonnegative contributions it remains valid with extended values because partial sums increase. The elementary-outcome formula is not a general instruction to sum singleton masses on a continuous space: continuous singleton probabilities may all be zero. The value-distribution definition, later expressed by an integral, is the appropriate general construction.

An instructive finite experiment has three outcomes with weights $1/2,1/3,1/6$ and values $2,2,8$. The atom $2$ has mass $5/6$, not one half. Either route gives $E[X]=2(5/6)+8(1/6)=3$. Counting distinct values as equally likely would incorrectly give $5$.

## 5. LOTUS: averaging a function without finding its entire law

Let $Y=g(X)$. If $E[|g(X)|]<\infty$, then the law of the unconscious statistician gives

$$E[g(X)]=\sum_x g(x)P(X=x).$$

To prove it, group the original atoms by their image $y=g(x)$. The mass at $y$ is the sum of original masses over that fiber. Replace each $g(x)$ in the fiber by $y$, and then use the definition of $E[Y]$. If $g(X)$ is nonnegative, the same proof works with a possibly infinite result. A many-to-one map does not require distinct transformed values: LOTUS counts each original mass exactly once.

For the law from Section 2, $E[X^2]=4/5+1/2+48/10=61/10$, whereas $(E[X])^2=169/100$. Their difference is $441/100$. For $g(x)=|x|$, the mean is $21/10$, which differs from $|E[X]|=13/10$. The operation $E$ commutes with affine functions, not with arbitrary nonlinear functions. If $g$ is undefined at a positive-mass atom, first repair or specify the random variable; an algebraic expression is not automatically a valid measurement.

<!-- SIM: lotus -->

## 6. Linearity and the reason independence is unnecessary

Suppose $X_1,\ldots,X_n$ have finite means and $a_1,\ldots,a_n,b$ are fixed real constants. Then

$$E\left[b+\sum_{i=1}^n a_iX_i\right]=b+\sum_{i=1}^n a_iE[X_i].$$

The variables are added on the same outcome: $S(\omega)=b+\sum_i a_iX_i(\omega)$. The triangle inequality shows $E[|S|]\le|b|+\sum_i|a_i|E[|X_i|]<\infty$. Expand its expectation, distribute the finite sum, and use $\sum_\omega P(\{\omega\})=1$. This proves both integrability and the identity. On a general space the same proof uses linearity of the integral.

Alternatively, for two discrete variables sum $(ax+by)p_{X,Y}(x,y)$ over the joint atoms. Separate the two absolutely convergent contributions, then sum each row or column to recover its marginal. No product factorization of the joint masses is used. Independence therefore has no role in this theorem.

For a fair sign $X\in\{-1,1\}$ and $Y=-X$, the variables are completely dependent. Nevertheless $X+Y=0$ on every outcome, and $E[X]+E[Y]=0$. The stronger statement that the two summands have independent laws would be false and unnecessary. A random coefficient is different: $E[AX]$ cannot generally be replaced by $E[A]E[X]$.

<!-- SIM: linearity -->

## 7. Products, powers, and dependence traps

If $X,Y$ are independent and integrable, their joint mass factorizes. Also $E[|XY|]=E[|X|]E[|Y|]<\infty$. The product expectation is therefore

$$E[XY]=\sum_{x,y}xy\,p_X(x)p_Y(y)=E[X]E[Y].$$

The conditions matter. For the same Bernoulli indicator $I$ with success probability $p$, $I^2=I$ on every outcome, hence $E[I^2]=p$, while $(E[I])^2=p^2$. Equality occurs only at the degenerate endpoints. For the fair sign example with $Y=-X$, $E[XY]=-1$ but $E[X]E[Y]=0$.

Conversely, one product identity does not prove independence. Take $X$ uniform on $-1,0,1$ and $Y=X^2$. Then $E[X]=E[XY]=0$, so $E[XY]=E[X]E[Y]$, yet $Y$ is determined by $X$ and is nonconstant. Checking independence requires the joint law, not one canceled moment. Powers need LOTUS; the special indicator identity is not an identity for general counts.

## 8. Indicators: turn counts into probabilities

For an event $A$, its indicator $I_A$ is one when $A$ occurs and zero otherwise. Directly, $E[I_A]=P(A)$. A count becomes tractable when it has an outcome-by-outcome decomposition

$$N=\sum_{i=1}^m I_{A_i},\qquad E[N]=\sum_{i=1}^m P(A_i).$$

The events may overlap or be dependent. The first equation must be verified before the second: the indicators must count exactly the intended objects and multiplicities. If an object is counted by several indicators but should be counted once, the decomposition is wrong. Conversely, counting unordered pairs requires one indicator for each pair, not one for each object.

For weighted counts $C=\sum_i c_i I_{A_i}$, fixed costs $c_i$ give $E[C]=\sum_i c_iP(A_i)$. Countability is allowed for nonnegative terms. For signed infinite weighted counts, a sufficient condition is $\sum_i|c_i|P(A_i)<\infty$. This separates the algebra of the count from the probability model used to evaluate an individual indicator.

## 9. Permutations: fixed points and prescribed matches

In a uniform random permutation of $n\ge1$ labels, let $I_i$ indicate that label $i$ maps to itself. Exactly $(n-1)!$ of $n!$ permutations fix that label, giving $P(I_i=1)=1/n$. The number of fixed points $F$ satisfies $E[F]=n/n=1$. For a prescribed target permutation, the number of matches also has mean one, because each target image remains one of $n$ equally likely images.

The indicators are generally dependent: for distinct labels and $n\ge2$, fixing both has probability $1/[n(n-1)]$, not $1/n^2$. This dependence changes second moments, not the mean. If only a subset of $r$ positions is checked, its expected number of matches is $r/n$. If the permutation is conditioned to be a derangement, every fixed-point indicator is zero and the expectation is zero; the original $1/n$ probability no longer applies.

<!-- SIM: permutations -->

## 10. Records and the authentic running-minimum pattern

For a uniform random ordering of $n$ distinct values, position $i$ is a new running minimum precisely when it holds the smallest of the first $i$ values. Those $i$ relative ranks are equally likely, so its indicator has mean $1/i$. Thus the number of updates is

$$E[R]=H_n=\sum_{i=1}^n\frac1i.$$

The first position counts as an update when the initial minimum is positive infinity. If initialization uses the first array value and counting begins afterward, the answer is $H_n-1$. Integral comparison gives $\ln(n+1)\le H_n\le1+\ln n$. Therefore logarithmic growth is an asymptotic description, not an exact value. The loop still performs exactly $n$ comparisons under the infinity initialization; successful updates and tests are different costs.

An original-PDF-checked doctoral question in the bank asks this pattern. Its illustration uses an explicitly labelled five-element realization; that trace demonstrates the update rule, while the indicator proof handles all uniform permutations.

<!-- SIM: records -->

## 11. Occupancy: empty boxes, used labels, and collisions

Place $m$ independently allocated balls into $n\ge1$ bins. If each ball chooses bin $j$ with probability $p_j$, define $J_j$ to indicate that bin $j$ is empty. All $m$ balls must avoid it, so $E[J_j]=(1-p_j)^m$. Hence

$$E[\text{empty bins}]=\sum_{j=1}^n(1-p_j)^m.$$

The number of occupied bins is the complement count, with mean $\sum_j[1-(1-p_j)^m]$. Uniform allocation makes these $n(1-1/n)^m$ and $n[1-(1-1/n)^m]$. Bin emptiness indicators are dependent, although the individual ball placements are independent. When $m=0$, all bins are empty, including a bin with selection probability one; this boundary is best handled directly.

For collisions, define an indicator for each unordered pair of balls that lands in the same bin. Its probability is $\sum_jp_j^2$, so the expected pair count is $\binom m2\sum_jp_j^2$. This is not the number of multiply occupied bins: a bin with four balls contributes six colliding pairs and one multiply occupied bin. The expected number of singleton bins is $\sum_jmp_j(1-p_j)^{m-1}$ for $m\ge1$.

<!-- SIM: occupancy -->

## 12. Sampling without replacement and weighted populations

Draw a uniform size-$r$ subset from a population of $N$ labeled objects, $K$ of which are marked. An indicator for a particular marked object has inclusion probability $r/N$, by counting subsets containing it. Summing the $K$ indicators proves that the expected marked count is $rK/N$. Dependence from depletion does not invalidate the result.

For population measurements $v_1,\ldots,v_N$, the sampled total has mean $(r/N)\sum_i v_i$. If $r>0$, the sample average has mean $(1/N)\sum_i v_i$. These identities require uniform subset sampling, or explicitly known inclusion probabilities. In a nonuniform design with inclusion probabilities $\pi_i>0$, the weighted estimator $\sum_{i\text{ sampled}}v_i/\pi_i$ is unbiased for the population total. This follows from an indicator proof and does not require independent selections. A sample average at $r=0$ is undefined.

## 13. Patterns in sequences and graphs

In independent Bernoulli trials with success probability $p$, a run of heads starts at the first position if it is a head, and at a later position if a tail is followed by a head. For length $n\ge1$, the expected number of head-runs is $p+(n-1)(1-p)p$. For all constant-symbol runs, each change creates a new run, giving $1+2(n-1)p(1-p)$. Overlapping length-$r$ all-head windows have expected count $(n-r+1)p^r$ when $1\le r\le n$. Overlap prevents independent window indicators but does not affect the expectation sum.

For a simple random graph on $n$ vertices with independent edges of probability $p$, edge indicators give mean edge count $\binom n2p$. Triangle indicators give $\binom n3p^3$, because three specified edges must be present. Independence within one triangle is used to find its probability; independence between different triangle indicators is unnecessary. An isolated vertex has probability $(1-p)^{n-1}$, so the expected isolated count is $n(1-p)^{n-1}$.

These examples distinguish two separate questions: does the count have a correct indicator decomposition, and does the proposed experiment justify the probability of one indicator? Linearity answers neither modeling question automatically.

## 14. Tail sums and the layer-cake proof

For a nonnegative integer variable $N$, the outcome-wise identity $N=\sum_{k\ge1}I_{\{N\ge k\}}$ counts one layer for every integer below its realized height. The terms are nonnegative, so increasing finite sums can be averaged and taken to the limit:

$$E[N]=\sum_{k\ge1}P(N\ge k)=\sum_{k\ge0}P(N>k).$$

The identity is valid even if the result is infinite. It is not $\sum_{k\ge1}P(N>k)$, which misses one unit whenever $N>0$. Squaring the height uses odd-width increments, since $k^2-(k-1)^2=2k-1$:

$$E[N^2]=\sum_{k\ge1}(2k-1)P(N\ge k).$$

More generally, for nondecreasing $h$ on nonnegative integers, $E[h(N)]=h(0)+\sum_{k\ge1}[h(k)-h(k-1)]P(N\ge k)$ whenever the nonnegative increment sum is defined. For a signed integer $X$, apply the two tail identities separately to its positive and negative parts: $E[X]=\sum_{k\ge1}P(X\ge k)-\sum_{k\ge1}P(X\le-k)$, provided the subtraction is meaningful. The later continuous chapter develops the corresponding tail integral.

<!-- SIM: tails -->

## 15. Waiting times: conventions, caps, and finite checks

Let $T$ be the total number of independent trials through the first success, with fixed $p\in(0,1]$ and $q=1-p$. Since $P(T\ge k)=q^{k-1}$, the tail sum gives $E[T]=1/p$. The failures-before-success count is $G=T-1$, so its mean is $q/p$. If $p=0$, no finite first success occurs; substituting zero in a finite-mean formula is invalid.

If a process stops after at most $r\ge1$ trials, its executed trial count is $C=\min(T,r)$, giving $E[C]=\sum_{k=1}^rq^{k-1}=(1-q^r)/p$. The last atom collects success at trial $r$ and no success by trial $r$. Conditioning on a success before the cap creates a different law. Returning zero when no success occurs creates yet another measurement. A problem must name which of these objects is being averaged.

For $p=1/4$ and $r=3$, the executed-trial mean is $1+3/4+9/16=37/16$. It is smaller than the uncapped mean four. At $p=1$ it is one; as $p$ decreases toward zero it approaches the cap $r$. The finite tail expression handles these limits without canceling a denominator prematurely.

<!-- SIM: waiting -->

## 16. Classical count means derived, not merely recalled

Bernoulli indicators have mean $p$. A count of $n$ trials each having marginal success probability $p$ has mean $np$, even if their dependence means it is not binomial. Independent unequal success probabilities give mean $\sum_i p_i$. The binomial PMF also verifies the result directly, using $k\binom nk=n\binom{n-1}{k-1}$ and the binomial normalization.

For a Poisson variable with parameter $\lambda\ge0$, shift the index in its nonnegative mean sum to obtain $E[N]=\lambda e^{-\lambda}\sum_{j\ge0}\lambda^j/j!=\lambda$. At $\lambda=0$, the variable is identically zero. For total trials through $r$ successes in independent fixed-$p$ trials, write the waiting time as a sum of $r$ geometrically distributed waiting segments. Each segment has mean $1/p$, so the total mean is $r/p$. A failures-only convention subtracts $r$.

The formulas are useful only after their contracts are matched. A random hidden success probability, dependent trials, time-varying probabilities, or finite-population depletion can preserve a simple mean while changing the distribution. Never infer a full law from a single matching expectation.

## 17. Raw, central, and factorial moments

The $r$th raw moment is $m_r=E[X^r]$, when $E[|X|^r]<\infty$. The central moment is $c_r=E[(X-\mu)^r]$. In particular, $c_1=0$ and $c_2=Var(X)$. The zero first central moment measures cancellation, not absence of spread. For finite second moment,

$$Var(X)=E[(X-\mu)^2]=m_2-\mu^2.$$

Expand the square, use linearity, and remember that $\mu$ is a constant. The result cannot be negative. Variance zero implies $(X-\mu)^2=0$ almost surely: a nonnegative variable with zero mean has zero probability of exceeding any positive threshold. Conversely, a constant variable has zero variance. The third central moment is $m_3-3\mu m_2+2\mu^3$. Its sign alone is not a complete distributional description.

Factorial moments of integer counts use $N(N-1)\cdots(N-r+1)$. For a sum of Bernoulli indicators, the second factorial moment counts ordered distinct successful pairs. Under independent identical success trials, $E[N(N-1)]=n(n-1)p^2$. Since $N^2=N(N-1)+N$, $E[N^2]=n(n-1)p^2+np$. This proves binomial variance $np(1-p)$ without a lengthy PMF sum. For Poisson counts, index shifting gives $E[N(N-1)]=\lambda^2$ and variance $\lambda$.

<!-- SIM: moments -->

## 18. Affine transformations and least-squares prediction

For fixed $a,b$, $E[aX+b]=a\mu+b$. Centering removes the shift: $(aX+b)-E[aX+b]=a(X-\mu)$. Squaring proves $Var(aX+b)=a^2Var(X)$. Negative scaling reverses locations but cannot make variance negative. Standard deviation scales by $|a|$. A random multiplier cannot be treated as fixed.

Suppose a constant prediction $c$ is scored by squared error. Expand about $\mu$:

$$E[(X-c)^2]=Var(X)+(c-\mu)^2.$$

The cross term vanishes because $E[X-\mu]=0$. Therefore the unique real constant minimizing expected squared loss is $c=\mu$, provided the second moment is finite. If predictions must be integers, choose the nearest integer or both tied integers. Absolute loss has a different optimizer, a median; maximizing the probability of an exact hit uses a mode. “Best prediction” is incomplete until the loss function is specified.

<!-- SIM: loss -->

## 19. Nonlinearity, Jensen, and safe elementary bounds

For an integrable variable, $|E[X]|\le E[|X|]$ follows from the triangle inequality. With finite second moment, $E[X^2]\ge(E[X])^2$ follows from nonnegative variance. More generally, convex $g$ gives $g(E[X])\le E[g(X)]$ when the quantities are well-defined. In a finite law, repeated use of the defining chord inequality proves this weighted Jensen inequality. Strict convexity gives equality only when the positive-mass values coincide.

For $X>0$, reciprocal convexity yields $E[1/X]\ge1/E[X]$ whenever $E[X]$ is finite and positive; the left side may be infinite. Concavity of logarithm reverses the inequality. A nonlinear function cannot be moved outside expectation merely because its formula is familiar.

If $X\ge0$ and $t>0$, then $X\ge tI_{\{X\ge t\}}$ pointwise. Taking means gives Markov's bound $P(X\ge t)\le E[X]/t$. A bound above one is replaced by the trivial bound one. Applying it to $(X-\mu)^2$ gives Chebyshev's bound $P(|X-\mu|\ge t)\le Var(X)/t^2$. These are upper bounds, not exact probabilities and not guarantees about any single realization.

## 20. A finite partition bridge and mixture means

For disjoint events $B_1,\ldots,B_r$ covering the space and having positive probabilities, expand the joint mass of each value and its category. This proves

$$E[X]=\sum_{j=1}^r P(B_j)E[X\mid B_j].$$

This section uses event-conditioned weighted means, not the full later theory of conditional expectation as a random variable. Category means must be weighted by category probabilities, not averaged uniformly unless the categories are equiprobable. Zero-probability categories can be omitted; their conditional means are not defined by division.

For a device that chooses a slow mode with probability $1/4$ and a fast mode otherwise, with mean costs $10$ and $2$, the overall mean cost is four. A hidden success probability can be handled similarly: a count of $n$ trials conditionally independent given $P$ has conditional mean $nP$, so its unconditional mean is $nE[P]$. It need not be binomial with parameter $E[P]$. This mean identity does not make the trials unconditionally independent.

## 21. Random numbers of summands and what can go wrong

For a nonnegative integer $N$ independent of an integrable identically distributed sequence $X_i$, assume $E[N]<\infty$. Rewrite the random sum as $S=\sum_{i\ge1}X_iI_{\{N\ge i\}}$. Independence gives $E[|X_i|I_{\{N\ge i\}}]=E[|X_1|]P(N\ge i)$, so the absolute expected contributions sum to $E[|X_1|]E[N]<\infty$. Consequently $E[S]=E[X_1]E[N]$.

This is an independent-random-length result, not an unrestricted stopping theorem. For a fair $X_1\in\{0,1\}$, choose $N=1$ if $X_1=1$ and $N=0$ otherwise. Then $S=X_1$ has mean $1/2$, while $E[N]E[X_1]=1/4$. The dependence invalidates the proposed factorization. Some stopping times do satisfy a Wald identity under additional assumptions; those assumptions require a separate proof.

## 22. Infinite sums: two safe routes and a counterexample

For nonnegative $Y_i$, partial sums increase and their expectations increase to the expectation of the infinite sum. Thus $E[\sum_iY_i]=\sum_iE[Y_i]$ with extended values allowed. For signed $Y_i$, the condition $\sum_iE[|Y_i|]<\infty$ ensures an integrable absolutely convergent total and permits the same interchange. Neither result says that pointwise convergence alone allows exchanging a limit and expectation.

For a variable $U$ uniform on $(0,1)$, let $Y_n=nI_{\{U\le1/n\}}$. For every fixed positive $U$, eventually $Y_n=0$, so the pointwise limit is zero. But $E[Y_n]=1$ for every $n$. This short continuous-space counterexample illustrates a convergence boundary; it does not require a general density calculation. A mass that becomes rarer and taller can retain its mean while disappearing pointwise. Inspect tails, domination, or an appropriate convergence theorem before interchanging operations.

## 23. Numerical computation and an auditable implementation

For a finite law, validate its support and probability masses, merge repeated values if needed, and compute products before summing. For a very large shifted measurement, computing variance as a difference of two nearly equal large numbers can lose precision. Center around a nearby fixed value $c$ instead: $Var(X)=E[(X-c)^2]-(E[X]-c)^2$. The identity follows by expansion and is useful even before specialized stable algorithms are introduced.

```python
from math import fsum, isfinite

def finite_mean(values, masses):
    if len(values) != len(masses) or not values:
        raise ValueError("The value and mass lists must have equal positive length.")
    if not all(isfinite(x) for x in values):
        raise ValueError("Every value must be finite.")
    if not all(isfinite(p) and p >= 0 for p in masses):
        raise ValueError("Every mass must be finite and nonnegative.")
    if abs(fsum(masses) - 1.0) > 1e-9:
        raise ValueError("Masses must sum to one; weights are not silently normalized.")
    return fsum(x * p for x, p in zip(values, masses))
```

A truncated infinite PMF is not a normalized finite law unless the omitted tail is explicitly represented or conditioning is intended. Report the partial contribution, omitted mass, and any justified tail bound. Tiny omitted probability alone does not bound mean error when the omitted values can be arbitrarily large. The heavy-tail example has omitted probability $2^{-r}$ after $r$ atoms and an infinite omitted mean.

## 24. A complete examination workflow

First identify the random object, sample mechanism, support, and units. Ask whether the mean is finite before applying signed algebra. Decide whether direct weighting, LOTUS, indicators, a tail sum, or a finite partition is the shortest justified route. Write the exact outcome-wise decomposition. Compute one contribution using the actual experiment. Sum it, retain boundary conditions, and check the result against support bounds and units.

For counts, check whether indices represent trials, bins, unordered pairs, ordered pairs, windows, or vertices. For a product, check independence or use the joint law. For a nonlinear payoff, use LOTUS or available raw moments. For a stopped process, distinguish executed trials from successes, failures, and a failure return code. For a mean-of-means question, identify the sampling unit before choosing weights. For an asymptotic answer, keep the exact expression until approximation is explicitly justified.

The solved bank deliberately mixes these choices. Its authentic examination item retains the printed options and an independently derived answer. Course-inspired questions are independently reconstructed families, not a claim to reproduce every exercise in the source courses. A numerical animation proves a calculation for its supplied data; a general theorem requires the accompanying proof.

## 25. Final summary with conditions attached

| Task | Exact rule | Required condition or warning |
|---|---|---|
| Finite-law mean | $E[X]=\sum_x xp_X(x)$ | Nonnegative masses totaling one |
| Finite mean on infinite support | $\sum_x|x|p_X(x)<\infty$ | Symmetric cancellation is insufficient |
| Function mean | $E[g(X)]=\sum_xg(x)p_X(x)$ | Integrable transformed value or nonnegative extended case |
| Finite linear combination | $E[\sum_i a_iX_i+b]=\sum_i a_iE[X_i]+b$ | Fixed coefficients; finite component means; no independence needed |
| Product | $E[XY]=E[X]E[Y]$ | Independence and integrability are sufficient, not necessary |
| Count | $E[\sum_iI_{A_i}]=\sum_iP(A_i)$ | Correct outcome-wise count; finite or nonnegative countable sum |
| Integer tail mean | $E[N]=\sum_{k\ge1}P(N\ge k)$ | Nonnegative integer variable |
| Second raw moment | $E[N^2]=\sum_{k\ge1}(2k-1)P(N\ge k)$ | Same tail contract |
| Variance | $Var(X)=E[X^2]-(E[X])^2$ | Finite second moment for ordinary algebra |
| Squared-loss optimum | $E[(X-c)^2]=Var(X)+(c-\mu)^2$ | Finite second moment |
| Finite category mean | $E[X]=\sum_jP(B_j)E[X\mid B_j]$ | Positive-probability partition categories |
| Independent random-length sum | $E[S]=E[N]E[X_1]$ | Independent length, integrable identical increments, finite mean length |

The next chapter develops variance, covariance, and correlation systematically. This chapter has already established the moment identities needed there, while preserving their existence conditions and the distinction between linearity and independence.

## 26. Fully worked mathematical and conceptual problems

<!-- INCLUDE: problems -->

## 27. Examination rules, traps, and transfer notes

<!-- INCLUDE: review -->

## 28. Editable expectation laboratory

<!-- LAB: expectation -->

## 29. References and reading provenance

1. James Martin. *Prelims Probability*. University of Oxford, Michaelmas 2019, version of 20 October 2019. [Written lecture notes](https://courses.maths.ox.ac.uk/mod/resource/view.php?id=48553), PDF pages 21–29, expectation, transformations, partition means, linearity, products, and moment boundaries.
2. Jeremy Orloff and Jonathan Bloom. *18.05 Introduction to Probability and Statistics*. MIT, Spring 2022. [Combined probability readings](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_probability.pdf), PDF pages 40–45, complete Class 4 expectation reading.
3. Rao and Walrand. *CS70 Discrete Mathematics and Probability Theory*, Note 16. UC Berkeley, Spring 2016 material in the Fall archive. [Written note](https://fa16.eecs70.org/static/notes/n16.pdf), PDF pages 6–10, expectation, proof of linearity, fixed points, and occupancy.
4. Siva Balakrishnan. *36-700 Probability and Mathematical Statistics I*, Lecture 3, 2 September 2016. Carnegie Mellon University. [Written lecture](https://www.stat.cmu.edu/~siva/teaching/700/lec3.pdf), PDF pages 3–8, Sections 3.4–3.7.1; continuous transformations outside the declared scope.
5. Cornell University. *CS2800 Discrete Structures*, Fall 2017, Lecture 9. [Expectation and variance](https://www.cs.cornell.edu/courses/cs2800/2017fa/lectures/lec09-expect.html), complete accessible lecture text, additional finite-experiment check. The page itself does not identify a lecturer; no lecturer attribution is invented.
6. Original examination archive. *PhD Computer Science 1404*, booklet 892A, Question 72, PDF page 16; and *MSc Computer Science 1405*, booklet 257A, Question 121, PDF page 26. Repository commit `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`; immutable source links appear beside the adapted questions. Answers are independently derived, not official answer keys.

See the [quality audit](../reviews/s_expectation-quality.html) for independent mathematical checks, visual checks, source discrepancies, and remaining limits. The source texts motivate and verify the synthesis; none is assumed infallible.
