# Discrete Distributions: Counts, Waiting Times, and Exact Model Selection

## 1. Written sources and the purpose of this chapter

Four core courses supply complementary foundations: Oxford Prelims Probability by James Martin; Cambridge Introduction to Probability by Mateja Jamnik and Thomas Sauerwald; Berkeley CS 70 by Rao and Walrand; and MIT 18.05 written notes by Jeremy Orloff and Jonathan Bloom. Chris Piech's Stanford CS 109 Poisson slides supply an additional reviewed application perspective. Exact page ranges, candidate decisions and corrected source statements are in the source audit. These materials were actually read; an unread course title is not a source contribution.

Earlier chapters introduced random variables and moments. Here the objective is to derive, recognize and manipulate the named discrete laws under explicit experimental contracts. A formula is useful only after its support, parameter convention, stopping rule and independence conditions are identified. The theory, worked bank and final notes connect these contracts to numerical and conceptual examination questions.

## 2. Begin with the experiment, not the distribution name

A Bernoulli trial is a binary observation with success probability $p$ and failure probability $q=1-p$. An independent identically distributed sequence means that every finite collection of specified outcomes has probability equal to the product of its individual probabilities. Pairwise independence alone is weaker and does not establish a binomial count law.

Three questions about the same sequence define different random variables. The number of successes among a fixed number $n$ of trials is a binomial count. The number of trials through the first success is a positive geometric waiting time. The number of trials through the $r$th success is a negative-binomial waiting time. The last two have random horizons; their final trials are forced successes. That final constraint changes the combinatorial coefficient.

Sampling a fixed-size subset without replacement uses a hypergeometric count because successive draws deplete a finite population. A Poisson law is an unbounded count model with a dimensionless expected count parameter. The average count alone never establishes that model.

Before calculating, write a sentence defining the random variable, list its possible values, identify every random input and specify which inputs are independent. A count of eligible successes is not a count of attempted trials. A deterministic horizon cannot be replaced by its average when the horizon is random.

## 3. Bernoulli laws and what two moments can establish

For $B\in\{0,1\}$ with $P(B=1)=p$, the complete law is

$$P(B=0)=q,\qquad P(B=1)=p,\qquad 0\le p\le1.$$

Because every positive integer power equals the indicator itself, $E[B^m]=p$ for $m\ge1$. Thus

$$E[B]=p,\qquad Var(B)=pq,\qquad G_B(z)=q+pz.$$

The variance is at most $1/4$, attained at $p=1/2$. A given variance below that maximum usually admits two success probabilities related by reflection. Its mean resolves that ambiguity.

The converse needs a support condition. If a real variable is known to lie in $[0,1]$ and satisfies $E[X]=E[X^2]$, then $E[X(1-X)]=0$. The nonnegative integrand must vanish almost surely, so $X$ is supported on the endpoints and is Bernoulli. Without the interval restriction, an equality of two moments need not force a binary law.

At $p=0$ or $p=1$ the law is constant. Its variance is zero and Pearson correlation with another variable is undefined. These endpoints are legitimate count laws; geometric success waiting at $p=0$ requires a different extended-valued interpretation.

## 4. Deriving the binomial law by grouping sequences

Let $B_1,\ldots,B_n$ be mutually independent Bernoulli variables with common probability $p$, and set $S_n=\sum_{i=1}^nB_i$. A specified sequence with $k$ successes has probability $p^kq^{n-k}$. There are $\binom nk$ positions for those successes. Therefore

$$P(S_n=k)=\binom nk p^kq^{n-k},\qquad k=0,\ldots,n.$$

Disjoint sequences justify addition; independence justifies multiplication within each sequence; identical probabilities justify assigning every sequence in the group the same weight. Omitting any one of these steps can invalidate the binomial formula.

Normalization follows from the binomial theorem: the sum of the masses is $(p+q)^n=1$. Define the endpoint laws directly to avoid interpreting an ambiguous $0^0$ term: if $p=0$, all mass is at zero; if $p=1$, all mass is at $n$. At $n=0$ the empty count is also zero.

For four independent objects that each qualify with probability $1/2$ and then independently succeed with probability $1/2$, a final success has probability $1/4$. The resulting count is binomial with four trials and probability $1/4$, not a fair binomial with an average of two trials.

<!-- SIM: binomial -->

## 5. Factorial moments and generating functions

The probability generating function, defined by $G_X(z)=E[z^X]$, encodes a nonnegative integer law. Its coefficients recover the masses, so equal PGFs near zero imply equal laws. Independent sums multiply PGFs; a scaled copy uses substitution instead.

For the binomial law,

$$G_{S_n}(z)=(q+pz)^n.$$

Differentiate $j$ times and evaluate at one:

$$E[(S_n)_j]=(n)_jp^j,$$

where $(x)_j=x(x-1)\cdots(x-j+1)$ and $(x)_0=1$. There is also a counting proof: expand the factorial count as a sum over ordered distinct success positions. Each ordered $j$-tuple contributes probability $p^j$, and there are $(n)_j$ such tuples. For $j>n$ the factorial moment is zero.

In particular,

$$E[S_n]=np,\qquad E[S_n(S_n-1)]=n(n-1)p^2,$$

$$Var(S_n)=n(n-1)p^2+np-n^2p^2=npq.$$

The second derivative is a factorial moment, not a raw second moment. Restore the missing first moment using $X^2=X(X-1)+X$. More generally a fixed number of independent copies and a deterministic multiple are different operations: $G_{X_1+\cdots+X_m}(z)=G_X(z)^m$, while $G_{mX}(z)=G_X(z^m)$.

## 6. Adjacent ratios, modes and recovering parameters

For an interior binomial law with $0<p<1$,

$$\frac{P(S_n=k+1)}{P(S_n=k)}=\frac{n-k}{k+1}\frac p q.$$

The ratio is above one precisely when $k+1<(n+1)p$. If $(n+1)p$ is not an integer, the unique mode is its floor. If it equals an integer $m$ with $1\le m\le n$, the adjacent modes are $m-1$ and $m$. Endpoint laws have their single deterministic modes. A mean is not automatically a mode, and a tied ratio must not be discarded.

Suppose a claimed binomial law has mean $\mu>0$ and variance $v$. Then $v=\mu(1-p)$, so $p=1-v/\mu$ and $n=\mu/p$ when $p>0$. These equations are necessary; they must yield an admissible probability and an integer trial count. If $v=\mu>0$, no finite nondegenerate binomial law satisfies them. If $v=0$, a binomial law is deterministic and its positive mean must equal an integer horizon.

An adjacent probability ratio can identify $p$ only when $n$ and the two support indices are known. A zero denominator or an endpoint law requires direct analysis rather than division.

## 7. Complements, parity, tails and conditional counts

The failure count $n-S_n$ is binomial with success probability $q$. Thus a lower tail can be reflected into an upper tail without changing the number of trials. For a fair law and odd $n$, symmetry gives $P(S_n\le(n-1)/2)=1/2$. For even $n$ the central atom must be handled separately.

Parity is encoded by the PGF at minus one:

$$E[(-1)^{S_n}]=(q-p)^n.$$

Since even outcomes contribute one and odd outcomes contribute minus one,

$$P(S_n\text{ is even})=\frac{1+(1-2p)^n}{2}.$$

Conditioning changes the law. Given $S_n=k$ with positive probability and $0<p<1$, every success-position subset of size $k$ has the same conditional probability $1/\binom nk$. The number of successes among the first $m$ trials is then hypergeometric:

$$P(S_m=j\mid S_n=k)=\frac{\binom mj\binom{n-m}{k-j}}{\binom nk}.$$

The successes inside the conditioned horizon are dependent. A product of the original marginal probabilities is not a conditional joint probability.

For integer-valued $X$, translate a noninteger threshold before summing: $P(X<t)=P(X\le\lceil t\rceil-1)$ and $P(X\le t)=P(X\le\lfloor t\rfloor)$. The distinction is especially important at an integer endpoint.

## 8. Thinning, classification and dependence after splitting

Let $N\sim Bin(n,p)$. Independently retain each success with probability $a$. Define $K$ as the retained count. Each original trial becomes retained with probability $pa$, so $K\sim Bin(n,pa)$. Conditioning on $N$ gives a second proof through PGF composition:

$$G_K(z)=G_N(1-a+az)=(1-pa+paz)^n.$$

Classify each trial into retained success, rejected success and original failure, with probabilities $pa,p(1-a),q$. Their joint count law is multinomial. Retained and rejected counts have covariance $-np^2a(1-a)$ because one fixed trial cannot contribute to both categories. They are generally not independent, despite independent marking of each object.

This contrasts with Poisson splitting, where a random unbounded total produces independent classified counts. The difference is in the total-count law, not in whether the marks were chosen independently.

<!-- SIM: splitting -->

## 9. Unequal trials and the Poisson-binomial distribution

Independent indicators with probabilities $p_1,\ldots,p_n$ have count PGF

$$G_S(z)=\prod_{i=1}^n(1-p_i+p_iz).$$

Their mean is $\sum_i p_i$ and their variance is $\sum_i p_i(1-p_i)$. A common average probability generally does not give the same law. In fact, if $\bar p$ is the average,

$$n\bar p(1-\bar p)-Var(S)=\sum_i(p_i-\bar p)^2.$$

The heterogeneous count has smaller variance than the common-probability independent count with the same mean. A shared latent probability creates the opposite kind of effect and must not be confused with fixed unequal probabilities.

To compute all masses, start with $a_0=1$. Incorporating a new probability $p$ uses $b_k=(1-p)a_k+pa_{k-1}$, with out-of-range entries zero. These are two mutually exclusive ways to reach the new success count. Update a separate buffer, or update indices in descending order; an ascending in-place update would reuse values from the current trial and overcount.

<!-- SIM: heterogeneous -->

## 10. Geometric support, survival and two conventions

Let $T$ be the number of iid Bernoulli trials through the first success, with $0<p\le1$. For $0<p<1$,

$$P(T=t)=q^{t-1}p,\qquad t=1,2,\ldots.$$

The first $t-1$ trials must fail and the final trial must succeed. There is no binomial coefficient because only one terminal pattern is allowed. Let $F=T-1$ be the failures before success; then $P(F=f)=q^fp$ for $f\ge0$.

For integers $m\ge0$, $P(T>m)=q^m$. Hence for real $x\ge1$,

$$P(T\le x)=1-q^{\lfloor x\rfloor}.$$

For $x<1$ the CDF is zero. Positive and zero-based means differ by one, while their variances agree:

$$E[T]=1/p,\qquad E[F]=q/p,\qquad Var(T)=Var(F)=q/p^2.$$

One derivation differentiates $\sum_{j\ge0}z^j=(1-z)^{-1}$ inside its convergence radius. Another uses the tail-sum identity $E[T]=\sum_{m\ge0}P(T>m)$. A first-step second-moment recursion gives $E[T^2]=p+qE[(1+T')^2]$, where $T'$ is an independent fresh wait with the same law. Substituting the mean yields $E[T^2]=(2-p)/p^2$.

At $p=1$, $T=1$ and $F=0$. At $p=0$, success never occurs; no probability-one finite waiting distribution exists. A displayed prefix of an infinite geometric law must retain its omitted tail $q^m$.

<!-- SIM: geometric -->

## 11. Memorylessness and the converse

For nonnegative integers $m,n$ with $P(T>m)>0$,

$$P(T>m+n\mid T>m)=q^{m+n}/q^m=q^n.$$

Equivalently $T-m$, conditional on surviving past trial $m$, has the original positive waiting law. The elapsed time is not forgotten; the distribution of the remaining trials is unchanged.

The zero-based variable requires careful wording: $P(F\ge m+n\mid F\ge m)=q^n$. Replacing both weak inequalities by the same strict inequalities changes the offset and may yield a wrong identity.

For the converse, suppose a positive integer-valued proper waiting law has survival $a_m=P(T>m)$, with $a_0=1$, and $a_{m+n}=a_ma_n$. Repeatedly setting $n=1$ gives $a_m=a_1^m$. Properness forces $a_1<1$. Differences $a_{t-1}-a_t$ give the geometric PMF with $p=1-a_1$. If survival ever becomes zero immediately, the deterministic $T=1$ case is included.

A waiting law with a time-varying success probability has $P(T>m)=\prod_{i=1}^m(1-p_i)$ and is generally not memoryless. A mixture over a shared hidden $p$ is also generally not geometric: survival conditions reweight the hidden parameter toward smaller probabilities.

## 12. Capping, truncation and administrative failure codes

These operations are mathematically distinct. A capped trial count $C=\min(T,m)$ has ordinary geometric masses for $1\le t<m$ and terminal mass $P(T\ge m)=q^{m-1}$ at $m$. That terminal atom includes both success at the last trial and all later success times.

A truncated law, conditional on success by $m$, has

$$P(T=t\mid T\le m)=\frac{q^{t-1}p}{1-q^m},\qquad 1\le t\le m.$$

Its normalizer is required. A failure code that reports zero when no success occurs by $m$ has mass $q^m$ at zero and mass $q^{t-1}p$ at each reported successful time $t\le m$. That code is not the capped count.

For the capped count, tail sums give $E[C]=(1-q^m)/p$. For its second moment use $C^2=\sum_{i=1}^C(2i-1)$, so $E[C^2]=\sum_{i=1}^m(2i-1)q^{i-1}$. These finite sums require no approximation or fabricated infinite tail.

<!-- SIM: censoring -->

## 13. Parallel waits, races and ties

For independent positive geometric waits $T_i$ with probabilities $p_i$, their minimum has survival $\prod_iq_i^m$ and is geometric with success probability $1-\prod_iq_i$. Their maximum has CDF $\prod_i(1-q_i^m)$ for integer $m\ge0$ and is generally not geometric.

With two waits, distinguish strict victory from a tie:

$$P(T_1<T_2)=\sum_{t\ge1}p_1q_1^{t-1}q_2^t=\frac{p_1q_2}{1-q_1q_2},$$

$$P(T_1=T_2)=\frac{p_1p_2}{1-q_1q_2}.$$

Together with the reverse strict victory, these probabilities sum to one. The continuous-race intuition that ties have probability zero is wrong on the discrete time lattice.

For iid waits with failure probability $q$, inclusion–exclusion in the maximum tail gives

$$E[\max_iT_i]=\sum_{j=1}^m(-1)^{j+1}\binom mj\frac1{1-q^j}.$$

The formula follows by expanding $1-(1-q^t)^m$ and summing each geometric tail. The number $m$ of competitors is fixed, and $0\le q<1$ ensures convergence.

## 14. Negative-binomial waiting: the forced final success

Let $T_r$ count trials through the $r$th success, where $r$ is a positive integer and trials are iid with $0<p\le1$. For $t\ge r$, the final trial succeeds, and the preceding $t-1$ positions contain exactly $r-1$ successes:

$$P(T_r=t)=\binom{t-1}{r-1}p^rq^{t-r}.$$

The binomial coefficient $\binom tr$ would also count sequences whose $r$th success occurs before the terminal trial, contradicting the stopping definition. The failure count $F_r=T_r-r$ has

$$P(F_r=f)=\binom{f+r-1}{r-1}p^rq^f,\qquad f\ge0.$$

The waiting increments between successive successes are independent positive geometric waits. To justify independence, specify any finite vector of increment lengths: the required disjoint blocks have probability equal to the product of their geometric masses. Therefore

$$E[T_r]=r/p,\qquad E[F_r]=rq/p,\qquad Var(T_r)=Var(F_r)=rq/p^2.$$

The count–wait duality is an event identity:

$$P(T_r\le n)=P(S_n\ge r).$$

It converts a waiting-time CDF into a binomial upper tail; it does not identify the two random variables. At $p=1$, the total wait is $r$; at $r=1$ it reduces to the positive geometric law.

<!-- SIM: negative -->

## 15. Negative-binomial algebra, modes and generalized shapes

For the failure convention,

$$G_{F_r}(z)=\left(\frac p{1-qz}\right)^r,\qquad |qz|<1.$$

Independent failure counts with the same $p$ add their shapes. Unequal probabilities do not generally give a negative-binomial law with a common averaged parameter.

For adjacent failure masses,

$$\frac{P(F_r=f+1)}{P(F_r=f)}=q\frac{f+r}{f+1}.$$

When $r>1$, the modes are determined by $(r-1)q/p$: the floor is unique unless that quantity is a positive integer $a$, in which case $a-1$ and $a$ tie. For $r=1$ and $p>0$, the mode is zero. Add $r$ to convert failure modes into total-wait modes.

The distribution also extends to a positive real shape by replacing the combinatorial coefficient with $\Gamma(f+r)/(\Gamma(r)f!)$. To verify this extension, expand $A(z)=(1-qz)^{-r}$ near zero. Its differential equation $(1-qz)A'(z)=rqA(z)$ gives coefficient recursion $a_0=1$ and $a_{f+1}=q(f+r)a_f/(f+1)$. Therefore $a_f=q^f r(r+1)\cdots(r+f-1)/f!$, which is nonnegative. At z equal to one its sum is $p^{-r}$, so multiplying by $p^r$ normalizes the coefficients. This establishes a genuine law, not merely a symbolic substitution into an integer formula.

The resulting PGF is $(p/(1-qz))^r$; differentiating at one gives first factorial moment $rq/p$ and second factorial moment $r(r+1)q^2/p^2$. Restoring the first moment and subtracting the squared mean gives variance $rq/p^2$. A noninteger shape still has no literal interpretation as waiting for a noninteger number of successes. Later continuous-mixture theory can derive it from a gamma-mixed Poisson rate. The present chapter keeps that extension distinct from the iid trial-count construction.

## 16. Hypergeometric sampling and exact support

Choose a uniform subset of size $n$ from a population of $N$ objects containing $K$ successes. The success count $H$ has

$$P(H=h)=\frac{\binom Kh\binom{N-K}{n-h}}{\binom Nn}.$$

Its positive-mass support is

$$\max(0,n-N+K)\le h\le\min(n,K).$$

The upper limit reflects both the sample size and the success pool. The lower limit prevents requesting more failures than exist. Writing the broader range $0,\ldots,n$ is acceptable only if impossible masses are assigned zero.

The numerator chooses a success subset and a failure subset; the denominator counts every possible sample. Vandermonde's identity proves normalization by partitioning all samples according to their success counts.

The same formula follows from uniform ordered sampling without replacement: every subset has $n!$ orders, so those factors cancel. Treating each draw as an independent Bernoulli trial with the original success fraction ignores depletion.

<!-- SIM: hypergeometric -->

## 17. Finite-population moments, ratios and symmetry

Let $p=K/N$ and $N>1$. Draw-position indicators each have mean $p$, and two distinct positions have joint success probability $K(K-1)/(N(N-1))$. Hence their covariance is $-pq/(N-1)$. Summing every diagonal and ordered off-diagonal contribution gives

$$E[H]=np,\qquad Var(H)=npq\frac{N-n}{N-1}.$$

The correction equals zero for a complete sample. It approaches one when the sampling fraction is small, but is never a license to declare the exact law binomial. The one-object population is deterministic and is handled directly; its variance formula cannot divide by zero.

For feasible adjacent indices,

$$\frac{P(H=h+1)}{P(H=h)}=\frac{(K-h)(n-h)}{(h+1)(N-K-n+h+1)}.$$

The ratio decides the mode while retaining tied cases and respecting effective support. The usual mode candidate is $\lfloor(n+1)(K+1)/(N+2)\rfloor$; if the unfloored value is an interior integer, the adjacent lower value also ties. Verify endpoint cases through the ratio rather than dividing by an impossible zero mass.

Population-complement symmetry turns $H$ into the sample failure count $n-H$. Sample-complement symmetry turns it into $K-H$ for the unselected subset. A third counting identity exchanges $n$ and $K$ in the hypergeometric count formula. These are law relationships, not statements that different experiments yield the same realized count.

## 18. Stopping without replacement: negative-hypergeometric waiting

Let $T_r$ be the position of the $r$th success in a uniform random ordering of a population with $K$ successes among $N$ objects, where $1\le r\le K$. A uniformly chosen set of $K$ success positions makes the probability

$$P(T_r=t)=\frac{\binom{t-1}{r-1}\binom{N-t}{K-r}}{\binom NK},\qquad r\le t\le N-K+r.$$

The last observed position is forced to be successful. Choose $r-1$ earlier success positions and $K-r$ later success positions. This is finite-population waiting, so geometric memorylessness fails.

There are $K+1$ gaps of failures before, between and after the success positions. A success-position set is equivalent to a weak composition of $N-K$ failures into those gaps. Symmetry makes every gap have mean $(N-K)/(K+1)$. The $r$th success follows $r$ leading gaps and $r$ successes, giving

$$E[T_r]=\frac{r(N+1)}{K+1}.$$

Here is the moment derivation rather than an appeal to a table. Write $F=N-K$ and $d=K+1$. There are $\binom{F+d-1}{d-1}$ weak compositions, all equally likely because each corresponds to exactly one success-position subset. For one gap, the generating sum of the falling factorial $(g)_j$ is $j!z^j/(1-z)^{j+1}$. The remaining $d-1$ gaps contribute $(1-z)^{-(d-1)}$. Dividing the coefficient of $z^F$ by the total number of compositions gives

$$E[(G)_j]=\frac{j!(F)_j}{d(d+1)\cdots(d+j-1)}.$$

In particular, $E[G]=F/d$ and $E[G(G-1)]=2F(F-1)/(d(d+1))$. Add the first moment to obtain the second raw moment, then subtract the squared mean:

$$Var(G)=\frac{F(d-1)(F+d)}{d^2(d+1)}.$$

Exchangeability and the constant gap total give $0=dVar(G)+d(d-1)Cov(G_i,G_j)$ for distinct gaps when $d>1$. Hence $Cov(G_i,G_j)=-F(F+d)/(d^2(d+1))$. The rth success position is r plus the sum of its r preceding gaps. Including both diagonal variances and ordered cross terms yields

$$Var(T_r)=\frac{r(K-r+1)(N+1)(N-K)}{(K+1)^2(K+2)}.$$

These moment identities can be checked directly from the displayed finite PMF. After observing a failure, the remaining population has changed; there is no fresh identical wait. The failure-before-stop convention subtracts $r$ from $T_r$ and leaves its variance unchanged.

<!-- SIM: finite-wait -->

## 19. Poisson counts, factorial moments and units

For $\lambda\ge0$,

$$P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!},\qquad k=0,1,\ldots.$$

The exponential series establishes normalization. At $\lambda=0$, all mass is at zero. For a positive parameter, shifting the factorial sum gives

$$E[(X)_j]=\lambda^j,\qquad E[X]=Var(X)=\lambda.$$

The PGF is $\exp(\lambda(z-1))$. Equal mean and variance are necessary for a Poisson law but do not identify it: a finite two-point law can satisfy the same moments.

The adjacent ratio is $\lambda/(k+1)$. If $\lambda$ is not an integer, its floor is the unique mode. If $\lambda=m$ is a positive integer, both $m-1$ and $m$ are modes. At zero there is only the deterministic mode zero.

For a homogeneous Poisson process with rate $\rho$ per unit time, the count over exposure $t$ has parameter $\lambda=\rho t$. The rate carries inverse-time units; the PMF parameter is an expected count. Constant mean rate by itself does not imply independent increments or Poisson counts. A finite interval can contain multiple arrivals. The correct small-interval statements are $P(N(h)=1)=\rho h+o(h)$ and $P(N(h)\ge2)=o(h)$.

<!-- SIM: poisson -->

## 20. Superposition, conditional allocation and independent splitting

Independent Poisson counts with parameters $\lambda_1,\lambda_2$ have sum parameter $\lambda_1+\lambda_2$, by PGF multiplication or convolution. Conditional on their sum $n$,

$$P(X=k\mid X+Y=n)=\binom nk\left(\frac{\lambda_1}{\lambda_1+\lambda_2}\right)^k\left(\frac{\lambda_2}{\lambda_1+\lambda_2}\right)^{n-k},$$

provided the total rate is positive and the conditioning event has positive probability.

If a Poisson total of mean $\lambda$ is independently classified with probabilities $a_1,\ldots,a_m$, the joint PGF is

$$\exp\left(\lambda\left(\sum_i a_i z_i-1\right)\right)=\prod_i\exp(\lambda a_i(z_i-1)).$$

The factorization proves that category counts are independent Poisson with means $\lambda a_i$. Given the total, those same category counts are multinomial and dependent. Conditional and unconditional independence must be stated separately.

A random rate $\Lambda$ produces a mixed Poisson law. Total variance gives $E[X]=E[\Lambda]$ and $Var(X)=E[\Lambda]+Var(\Lambda)$ when the required moments exist. An excess variance can reveal heterogeneity, but it does not uniquely identify a mixing distribution.

## 21. Rare-event limits with an explicit error interpretation

For fixed $\lambda$ and $k$, a binomial law with $p=\lambda/n$ has

$$P(S_n=k)=\frac{\lambda^k}{k!}\left(\prod_{j=0}^{k-1}(1-j/n)\right)(1-\lambda/n)^n(1-\lambda/n)^{-k}.$$

As $n$ tends to infinity with $n\ge\lambda$, the factors tend respectively to one, $e^{-\lambda}$ and one. This proves the Poisson point-mass limit. It is not an assertion that every finite binomial tail equals a Poisson tail or that $k$ may grow arbitrarily with $n$ in this argument.

A useful quantitative bound has a short coupling derivation. A Bernoulli variable with probability $p$ and a Poisson variable of mean $p$ have total variation distance $p(1-e^{-p})\le p^2$: the sole positive difference of Bernoulli mass over Poisson mass is at one. Couple them so that their mismatch probability is that distance, using their common masses first. Independently couple each pair of coordinates. A union bound shows that the two sums disagree with probability at most $\sum_i p_i^2$.

Thus for independent unequal rare indicators and a Poisson law with $\lambda=\sum_i p_i$, every count event has absolute probability error at most $\min(1,\sum_i p_i^2)$. This is an absolute, not relative, bound. A small bound can still be large relative to an extremely rare tail. Dependence requires a separate argument; the same mean and small marginal probabilities do not automatically justify this certificate.

<!-- SIM: approximation -->

## 22. Shared latent parameters and censored observations

Suppose a single hidden probability $P$ is drawn and then $n$ trials are conditionally independent given $P$. The count law is a mixture of binomial laws:

$$P(S_n=k)=E\left[\binom nk P^k(1-P)^{n-k}\right].$$

It usually differs from $Bin(n,E[P])$. Total variance gives

$$Var(S_n)=n\bar p(1-\bar p)+n(n-1)Var(P),\qquad \bar p=E[P].$$

The shared parameter contributes positive dependence. By contrast, drawing a fresh independent parameter for every trial can produce independent Bernoulli trials with success probability $\bar p$.

A success-only waiting log samples a truncated law. A log that includes capped failures samples a censored law. If the experiment stops because an outcome-dependent rule is satisfied, the observed count cannot be analyzed by silently treating that horizon as fixed.

For example, a family-size prior and the observation of no boys combine as prior mass times a likelihood $2^{-n}$. The likelihood reweights the prior over sizes; the posterior success probability is not obtained by conditioning each individual child independently and retaining the original size distribution.

## 23. Numerically reliable discrete probabilities

For a moderate binomial parameter, direct factorial products can overflow before the final small probability is formed. Work in log space:

$$\log P(S_n=k)=\log\Gamma(n+1)-\log\Gamma(k+1)-\log\Gamma(n-k+1)+k\log p+(n-k)\log q.$$

Handle $p=0,1$ before logarithms. A log-mass remains meaningful even when its exponential underflows. Adjacent ratios can build a local PMF from a mode without starting from an underflowed endpoint.

For tiny success probabilities, compute $q^n$ as $\exp(n\log(1-p))$ with a numerical log-one-plus routine, and compute $1-q^n$ with a numerical exp-minus-one routine. Subtracting two nearly equal rounded numbers loses significant digits. For upper tails, sum the upper-tail masses directly rather than always subtracting a near-one CDF.

The following exact-rational dynamic program computes an independent unequal-trial count. It does not use random simulation as a substitute for a probability law.

```python
from fractions import Fraction

def independent_count(probabilities):
    masses = [Fraction(1)]
    for probability in probabilities:
        p = Fraction(probability)
        if not 0 <= p <= 1:
            raise ValueError("Every probability must be between zero and one.")
        next_masses = [Fraction(0)] * (len(masses) + 1)
        for k, mass in enumerate(masses):
            next_masses[k] += (1 - p) * mass
            next_masses[k + 1] += p * mass
        masses = next_masses
    assert sum(masses) == 1
    return masses
```

### Uniform integer laws and transformed lattices

A variable uniform on the integers one through m assigns each integer mass $1/m$. It has mean $(m+1)/2$. The identity $\sum_{k=1}^m k^2=m(m+1)(2m+1)/6$ gives its second raw moment $(m+1)(2m+1)/6$, and subtraction of the squared mean gives variance $(m^2-1)/12$. These sum identities follow by telescoping successive squares and cubes, respectively, so the formulas also hold at the constant-law boundary m equal to one.

For a uniform variable on integers a through b, let $m=b-a+1$ and shift the preceding law by a minus one. The mean becomes $(a+b)/2$, while the variance remains $(m^2-1)/12$. A nonzero affine scale preserves equal atom probabilities but changes the support spacing. For example, $Y=2X-3$ with X uniform on one through m is uniform on the odd arithmetic progression from minus one through $2m-3$, not on every integer between those endpoints. A zero scale instead collapses all mass to one value.

For an event bounded by real thresholds, first solve the inequality for X and then intersect its admissible integer endpoints with the declared support. Conditioning on a retained subset divides its atom probabilities by that subset's probability. A subset containing gaps need not be a consecutive-integer uniform law, even though its retained atoms remain equally weighted.

<!-- SIM: uniform -->

## 24. Complete-sentence summary

A distribution name compresses an experiment only when its assumptions are satisfied. A binomial law counts common-probability independent successes on a fixed horizon. A positive geometric law counts trials through a first success; its failure-based version subtracts one. A negative-binomial law stops at the required final success and uses a coefficient counting only preceding success positions. Hypergeometric counts use uniform finite-population sampling without replacement and an effective support constrained by both pools. Finite-population stopping has a negative-hypergeometric law and changed hazards. A Poisson parameter is the expected count over the specified exposure, and its unbounded support differs from a finite binomial support.

PGFs distinguish independent sums from scaled copies, express thinning as composition and recover factorial moments from derivatives. Adjacent ratios identify tied modes without guesswork. Count–wait duality translates events but does not identify random variables. Conditioning can create dependence; Poisson splitting can remove the dependence induced by a fixed total. Truncation, capping and failure codes place different masses at their endpoints. Mixtures over shared parameters change both probabilities and covariance. Approximation statements require an error scale and a declared limiting regime. Every calculation should end with checks of support, normalization, parameter units and the event's strict or non-strict threshold.

## 25. Worked examination and concept problems

<!-- QUESTIONS -->

## 26. Final reasoning rules and examination traps

<!-- RULES -->

## 27. Editable distribution laboratory

<!-- LAB -->

## 28. References and remaining boundaries

1. James Martin. Prelims Probability. University of Oxford, Michaelmas 2019. PDF 18–26 and 39–44. https://courses.maths.ox.ac.uk/mod/resource/view.php?id=48553
2. Mateja Jamnik and Thomas Sauerwald. Introduction to Probability, Lecture 4. University of Cambridge, 2023–24 archive. All 23 PDF pages. https://www.cl.cam.ac.uk/teaching/2324/IntroProb/slides/04-poisson-geometric-discr-rv-all-handout.pdf
3. Rao and Walrand. CS 70, Note19: Some Important Distributions. UC Berkeley, Spring 2016 notes in Fall 2016 archive. All 8 PDF pages. https://fa16.eecs70.org/static/notes/n19.pdf
4. Jeremy Orloff and Jonathan Bloom. MIT 18.05 combined probability readings, Spring 2022, Classes 4–5, PDF 34–51. Course instructors: Jeremy Orloff and Jennifer French Kamrin. https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_probability.pdf
5. Chris Piech. CS 109 Lecture 8: Poisson. Stanford University, Winter 2022. All 66 textual slides, including progressive duplicates. https://web.stanford.edu/class/archive/cs/cs109/cs109.1224/lectures/8-Poisson/8-Poisson.pdf

The questions, explanations and models are independently authored or clearly attributed English adaptations. Original examination identities and PDF evidence are recorded separately. These sources support the declared chapter but do not establish an exhaustive review of every course or guarantee performance on every unseen examination question. Continuous distributions, general stochastic-process theory and estimation procedures receive their full treatment in later chapters; the relevant interfaces are stated here.
