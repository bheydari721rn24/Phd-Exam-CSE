## Q19

**Correct option: 2.** With $n=5$, the five disjoint events each have mass $1/6$. Their union is partitioned into exactly those five sets, so finite additivity gives $5(1/6)=5/6$. The complement mass is $1/6$. A concrete realization is a uniform six-point space: five events are distinct singleton points and the sixth point lies outside every event.

Option one's $(5/6)^5=3125/7776$ is a product of five identical failure probabilities. Such a product would require independence, which the given disjoint positive-mass events do not have. Option three counts the complement. Option four makes the events exhaustive, although their total mass is only $5/6$. For two of the given events, the intersection has probability zero while the marginal product is $1/36$, directly disproving independence. The exact sum rests on disjointness, not merely on the fact that five events were named. A union bound would give the same upper number from the marginals, but the partition additionally proves equality.

## Q20

**Correct option: 1.** Eight pairwise disjoint events each have probability $1/9$. No outcome is counted twice by adding their masses, so $P(\bigcup_{i=1}^8A_i)=8/9$. The outside region has the remaining mass $1/9$. The nine-point uniform construction with eight singleton events proves that the premise describes a consistent law.

Option two's $1/9$ is the outside event. The value one in option three incorrectly assumes that the named events cover the whole space. Option four is $(8/9)^8$, the result of multiplying eight failure probabilities as if they were independent. Yet two different events have intersection zero and product $1/81$, so that premise would be false. Even though the events themselves are disjoint, their complements are not: almost every outcome fails several events simultaneously. The complement of their union is the intersection of their complements, whose exact mass is $1/9$, not the unjustified product. This is a finite instance where De Morgan's set identity remains valid while an independence shortcut fails.

## Q21

**Correct option: 4.** The disjoint union contains $n$ events of mass $1/(n+1)$, giving $n/(n+1)$. To prove feasibility over the positive-integer domain, take $\Omega=\{0,1,\ldots,n\}$ with equal point masses and $A_i=\{i\}$ for $1\le i\le n$. The outside point zero accounts for the complementary mass $1/(n+1)$.

The first option is that complement. The second option assumes exhaustiveness, contradicted by its positive mass. The third computes $(n/(n+1))^n$, a product with no stated independence. For $n\ge2$ the events are explicitly dependent, since $P(A_i\cap A_j)=0$ and $P(A_i)P(A_j)>0$. At $n=1$, the single event has mass $1/2$, and the product distractor happens to agree; a general formula must also work for $n=2$, where $2/3\ne(2/3)^2$. The correct union tends to one but remains strictly below one for every finite $n$. The limiting statement does not retroactively make any finite collection exhaustive.

## Q22

**Correct option: 3.** For arbitrary events, separate overlaps before adding masses. Define $D_1=A_1$ and $D_i=A_i\setminus\bigcup_{j<i}A_j$. The sets $D_i$ are disjoint and have the same union as the original events. Because $D_i\subseteq A_i$, monotonicity gives

$$P\left(\bigcup_{i=1}^n A_i\right)=\sum_{i=1}^nP(D_i)\le\sum_{i=1}^nP(A_i).$$

Here the original sets are already disjoint, so $D_i=A_i$ and equality follows. Option one fails for two copies of the same event of probability $1/2$: the union mass is $1/2$ while the summed bound is one. Option two confuses a union with an intersection and also assumes an unsupported product rule. Option four fails for the positive disjoint masses whenever $n\ge2$. No independence is required for the inequality. Conversely, exact equality in probability need not imply literally empty overlaps: zero-mass intersections do not affect the sum. The given pairwise disjointness is a sufficient, particularly transparent condition for equality.

## Q23

**Correct option: 3.** The mass law is normalized: $\sum_{k=1}^{\infty}2^{-k}=(1/2)/(1-1/2)=1$. At threshold five, the event contains outcomes $5,6,7,\ldots$. Its mass is the whole tail

$$P(X\ge5)=\frac1{32}+\frac1{64}+\frac1{128}+\cdots=\frac{1/32}{1-1/2}=\frac1{16}.$$

The sum uses countable additivity of disjoint singleton events. Option four's $1/32$ keeps only the first included outcome. Option one's $15/16$ is $P(X<5)$, the complement. Option two's $1/5$ would arise from a different law and does not follow from these geometric point masses. As a finite check, the first four masses sum to $1/2+1/4+1/8+1/16=15/16$, leaving exactly $1/16$. A strict threshold $X>5$ would start at six and have mass $1/32$; open versus closed endpoints matter in this discrete law because each endpoint has positive mass.

## Q24

**Correct option: 2.** The first mass in the included tail is $P(X=8)=1/256$. Every subsequent term is half the preceding one, so the infinite sum is twice its first term:

$$P(X\ge8)=\frac{1/256}{1/2}=\frac1{128}.$$

The seven excluded point masses total $1-2^{-7}=127/128$, furnishing the complement check. Option three is the endpoint singleton mass, option four is the excluded region, and option one's $1/8$ has no relation to the stated point law. Reindexing with $r=k-8$ gives $2^{-8}\sum_{r=0}^{\infty}2^{-r}$; starting that sum at one would incorrectly omit outcome eight. Under this discrete distribution, the strict tail $P(X>8)$ equals $1/256$, which explains the numerical distractor without making it a valid answer to the included threshold. Normalization must be established before treating a list of nonnegative numbers as a probability law.

## Q25

**Correct option: 1.** For every $n\ge1$, countable additivity on the included singleton points gives

$$P(X\ge n)=\sum_{k=n}^{\infty}2^{-k}=2^{-n}\sum_{r=0}^{\infty}2^{-r}=2^{1-n}.$$

The same expression satisfies $T_n-T_{n+1}=2^{-n}$, exactly the mass removed when the threshold increases by one, with $T_1=1$ and $T_n\to0$. This difference check tests both the starting endpoint and the normalization. Option two keeps only the first term and gives half the correct tail. Option three is its complement, the probability of $X<n$. Option four's $1/n$ coincides at some small parameters but fails, for example, at $n=3$, where the true tail is $1/4$. A finite set of coincident values does not establish an identity. Every finite positive threshold has positive tail mass even though the limiting tail is zero.

## Q26

**Correct option: 4.** The events $A_n=\{n,n+1,\ldots\}$ decrease. No finite positive integer belongs to all of them: for a fixed outcome $k$, the event $A_{k+1}$ excludes it. Hence $\bigcap_{n\ge1}A_n=\varnothing$. Continuity from above for a probability measure gives

$$\lim_{n\to\infty}P(A_n)=P\left(\bigcap_{n\ge1}A_n\right)=0,$$

agreeing with $2^{1-n}\to0$. Every individual $A_n$ is infinite and has positive mass; neither property forces a positive-mass intersection, disproving option one. Option two omits all later outcomes, which have another $2^{-n}$ of mass. Option three drops a positive-mass endpoint and halves the exact tail. Monotonicity of the event sequence is essential for this continuity statement. Merely knowing a numerical sequence of event probabilities tends to zero does not generally determine the probability of infinitely many occurrences; the lesson's moving interval example distinguishes that different limiting event.

## Q27

**Correct option: 2.** Let $C$ be the condition and $S$ a positive signal. At $n=5$, $P(C)=1/5$, $P(C^c)=4/5$, and the two signal likelihoods are $2/3$ and $1/3$. The joint membership table is

|  | Positive signal | Negative signal |
| --- | --- | --- |
| Condition | $2/15$ | $1/15$ |
| No condition | $4/15$ | $8/15$ |

The positive column has mass $6/15$. Restricting to that column and renormalizing gives $P(C\mid S)=(2/15)/(6/15)=1/3$. The numerator is a joint event; the denominator must include both ways to produce a positive signal. Option three's $2/3$ is $P(S\mid C)$, the reversed conditional. Option four's $1/5$ is the prior before observing a signal. Option one's $2/7$ changes the denominator and does not reproduce either column sum. The table totals one and recovers both supplied likelihoods when its rows are renormalized, checking the model independently of the posterior simplification.

## Q28

**Correct option: 1.** At $n=8$, the true-positive contribution is $(1/8)(2/3)=2/24$. The false-positive contribution is $(7/8)(1/3)=7/24$. These disjoint routes partition the positive event, so its mass is $9/24$ and

$$P(C\mid S)=\frac{2/24}{9/24}=\frac29.$$

For completeness, the negative contributions are $1/24$ and $14/24$; all four table entries total one. The positive observation raises the prior $1/8$ to $2/9$, but does not make the condition likely with probability $2/3$. That latter number in option two is a likelihood, not the posterior. Option three ignores the observation. Option four's $1/5=2/(8+2)$ has an incorrect extra unit in the denominator. The false-positive mass is larger than the true-positive mass because the no-condition population is seven times larger, despite its lower conditional signal rate. This example shows mathematically why a moderately informative signal cannot erase a low prior.

## Q29

**Correct option: 4.** In a general positive-integer instance, use denominator $3n$. The four atomic masses, in order $(C,S),(C,S^c),(C^c,S),(C^c,S^c)$, are

$$\frac2{3n},\quad\frac1{3n},\quad\frac{n-1}{3n},\quad\frac{2(n-1)}{3n}.$$

They are nonnegative and total one. The positive column has mass $(n+1)/(3n)>0$, permitting ordinary conditioning. Divide its condition entry by the column total:

$$P(C\mid S)=\frac{2/(3n)}{(n+1)/(3n)}=\frac2{n+1}.$$

Option one reverses the conditional, option two uses the unchanged prior, and option three incorrectly gives denominator $n+2$. At $n=1$, the condition is certain, the false-positive route has mass zero, and the posterior is one, as the formula requires. The no-condition likelihood is then specified only as part of a generative model; it is not an ordinary conditional ratio on a zero-probability event. For large $n$, the posterior remains of order $1/n$, although approximately twice the prior. The exact multiplier is $2n/(n+1)$ rather than exactly two at finite $n$.

## Q30

**Correct option: 3.** The requested denominator is $P(S)$, whereas the reversed conditional uses $P(C)$. Those denominators represent different populations. Algebraically,

$$P(C\mid S)=\frac{P(S\mid C)P(C)}{P(S\mid C)P(C)+P(S\mid C^c)P(C^c)}.$$

For the given model this is $2/(n+1)$, while $P(S\mid C)=2/3$. For example, at $n=8$ they are $2/9$ and $2/3$, so the distinction is substantial. At $n=2$ they happen to agree, which does not prove a general reversal identity. Option one omits the false-positive route and would incorrectly produce certainty whenever the true-positive numerator is positive. Option two is contradicted by the positive false-positive mass when $n>1$. Option four incorrectly removes the prior, contradicted by comparing $n=5$ and eight under unchanged likelihoods. The posterior equals one at the endpoint $n=1$ because the complementary prior is zero; state that endpoint explicitly instead of making a universal certainty claim.

## Q31

**Correct option: 1.** Write $X=I_1+\cdots+I_5$, where each independent indicator has success probability $1/3$. Since $I_i^2=I_i$, its first and second moments are both $1/3$, and its variance is $1/3-1/9=2/9$.

To derive the sum variance, expand rather than assume additivity:

$$E[X^2]=\sum_{i=1}^5E[I_i]+2\sum_{i<j}E[I_iI_j]=\frac53+2\binom52\frac19=\frac{35}{9}.$$

The squared mean is $(5/3)^2=25/9$. Their difference is $10/9$. Option two is the mean, not the variance. Option three's $50/9$ is the variance if all five indicators were the same random bit, so the count were $5I$; its quadratic scaling contradicts independence here. Option four is only one indicator's variance. This calculation also illustrates why a variance may exceed one although each indicator lies in $\{0,1\}$: the total count ranges from zero through five. Normalization bounds probabilities, not the variance of an arbitrary count.

## Q32

**Correct option: 4.** For eight independent $1/3$-success indicators, $E[X]=8/3$. The diagonal terms in the squared count contribute $8/3$, and the $\binom82=28$ distinct pairs have expected products $1/9$. Therefore

$$E[X^2]=\frac83+2\cdot28\cdot\frac19=\frac{80}{9},\qquad E[X]^2=\frac{64}{9}.$$

The variance is $16/9$. The first option confuses it with the mean $8/3$. The second option's $128/9$ would result from perfect positive dependence, $X=8I$ with one shared indicator, because scaling by eight multiplies variance by 64. The third option is the variance $2/9$ of one indicator and drops seven independent contributions. The independent count instead sums eight such variances: $8(2/9)=16/9$. The factor two in the cross term belongs to the algebraic expansion of a square; it is not a probability counted twice. Subtracting the squared mean cancels those independent cross terms precisely.

## Q33

**Correct option: 3.** The identity $X^2=\sum_iI_i+2\sum_{i<j}I_iI_j$ holds for each outcome. Independence gives $E[I_iI_j]=1/9$ for distinct indices, so

$$E[X^2]=\frac n3+\frac{n(n-1)}9,\qquad E[X]^2=\frac{n^2}9.$$

Subtracting gives $2n/9$. This proof works for every positive integer $n$, including the empty pair sum when $n=1$. Option one's quadratic expression $2n^2/9$ belongs to $n$ perfectly correlated copies of one indicator. Option two is a single contribution's variance, and option four is the mean. Agreement of the first two distractors with the answer at $n=1$ does not validate them throughout the domain. More generally, independent Bernoulli indicators with common success probability $p$ give $np(1-p)$, by replacing $1/3$ and $1/9$ with $p$ and $p^2$. The variance formula is not a standalone axiom: it follows from the indicator identity, linearity of expectation and vanishing cross covariances.

## Q34

**Correct option: 2.** Without independence, the exact expansion retains each pair's deviation from its marginal product:

$$\operatorname{Var}(X)=\sum_i\operatorname{Var}(I_i)+2\sum_{i<j}\left(E[I_iI_j]-E[I_i]E[I_j]\right).$$

For a concrete counterexample, take all $I_i=I$ for a single Bernoulli variable with probability $1/3$. Every covariance is $2/9$ and $X=nI$, so the variance becomes $2n^2/9$, not $2n/9$ when $n>1$. This disproves option three. Option one forgets the squared mean: one indicator has variance $p-p^2$, which equals its mean only at $p=0$. Option four confuses a random outcome-dependent count with its deterministic average. Independence is sufficient to cancel the cross terms; pairwise zero covariance is already sufficient for this particular variance identity. Consequently, the absence of mutual independence does not automatically make the numerical sum-of-variances formula false, but it does remove the justification unless the cross terms are checked or otherwise known to sum to zero.

## Q35

**Correct option: 3.** The complement of at least one occurrence is no occurrence. Five mutually independent events each have failure probability $4/5$, so the all-failure event has mass $(4/5)^5=1024/3125$. Subtract it from one:

$$P\left(\bigcup_{i=1}^5A_i\right)=1-\frac{1024}{3125}=\frac{2101}{3125}.$$

The sum of marginal probabilities is one and provides the union bound. It does not make the union exhaustive: the all-failure event above has strictly positive mass. Thus option four reports the bound as if it were an equality. Option one gives the complementary probability. Option two's $4/5$ is the failure probability for one specified event rather than all five. The union event includes outcomes with one, two, three, four or five successes. In a product-space model each success pattern has mass $(1/5)^k(4/5)^{5-k}$, and summing the nonempty patterns agrees with the complement calculation. No disjointness of the original events is present or needed.

## Q36

**Correct option: 2.** For eight mutually independent events of probability $1/8$, De Morgan's identity gives a complement intersection of eight failure events, each of mass $7/8$. Hence

$$P(\text{at least one})=1-\left(\frac78\right)^8=\frac{16777216-5764801}{16777216}=\frac{11012415}{16777216}.$$

Option four's numerator $5764801=7^8$ counts no occurrence, while the denominator $8^8$ is consistent with an eight-coordinate uniform product realization. Option one uses the failure mass of only one event. Option three is the summed marginal upper bound $8(1/8)=1$, which is loose because multiple events can occur together. A complete product-space construction chooses each of eight coordinates uniformly from eight labels and defines event $i$ by one distinguished label in coordinate $i$. Exactly $7^8$ outcome vectors avoid all events. The difference count above therefore checks the probability formula directly, without confusing a bound with the number of admitted outcomes.

## Q37

**Correct option: 1.** For $n\ge2$, mutual independence of event complements gives $P(\bigcap_iA_i^c)=(1-1/n)^n$. The desired union is its complement, so its mass is $1-(1-1/n)^n$. At $n=1$, the only event is certain and the same displayed expression gives one.

Option two is the union bound $\min(1,\sum_i1/n)=1$; it is strictly larger than the union for every $n\ge2$, since the excluded pattern has positive mass. Option three gives no occurrence. Option four describes failure of one event. The limit is $1-e^{-1}$, not one: using $\log(1-x)=-x+O(x^2)$ at $x=1/n$ gives $n\log(1-1/n)\to-1$. This is an asymptotic statement about a changing family of models, not continuity along a declared nested event sequence in one fixed space. The sum of rare-event marginals remains one while their overlaps leave a substantial all-failure mass.

## Q38

**Correct option: 4.** Pairwise independence fixes two-event intersections, not an arbitrary-length product. A counterexample can preserve the exact $n=3$ marginal probability $1/3$. Assign mass $1/9$ to each of the three single-only membership patterns and each of the three pair-only patterns, mass $1/3$ to none, and zero to all three. These eight masses are nonnegative and total one.

Each event occurs in its single-only cell and two pair-only cells, so it has mass $3/9=1/3$. Each pair intersection is its pair-only cell of mass $1/9=(1/3)^2$, establishing pairwise independence. Yet the triple has mass zero instead of $1/27$, and the union has mass $2/3$ instead of the mutually independent value $1-(2/3)^3=19/27$.

This table disproves option two with the very marginals used in the question, rather than an unrelated fair-bit example. Option one confuses an upper bound of one with equality. Option three misstates De Morgan: a union complement is an intersection of complements. Full mutual independence controls every nonempty subset product and therefore supplies the product for all failures; checking only pairs cannot replace that premise.
