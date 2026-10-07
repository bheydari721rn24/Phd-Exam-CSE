# Discrete Random Variables and Common Distributions

## 1. Reading route, sources, and chapter boundary

Read Sections 2–9 before named distributions: the same event-to-mass calculation underlies every family. Sections 10–17 derive the common laws and model-selection conditions. Sections 18–22 build more demanding distributions from those foundations. The complete problem bank and final examination rules are teaching material, not a request to take a test before studying.

The primary synthesis uses four genuinely reviewed written university courses. Oxford supplies precise event and support definitions; MIT supplies PMF–CDF construction and distribution contracts; Berkeley supplies fiber aggregation and computing examples; Stanford supplies binomial decision models and erroneous-count diagnosis. Harvard contributes a bounded additional review of three distribution/CDF exercise families. [The source comparison](../reviews/s_discrete-sources.html) records selection, access failures, actual reading scopes, and limitations.

| University | Course and author | Material actually reviewed for this chapter |
|---|---|---|
| Oxford | Prelims Probability, James Martin, Michaelmas 2019 | Chapter 2 definitions and classical laws through Exercise 2.5, PDF pages 18–21 |
| MIT | 18.05 Introduction to Probability and Statistics, Jeremy Orloff and Jonathan Bloom, Spring 2022 | Complete Class 4 discrete-variable reading, combined PDF pages 28–39 |
| UC Berkeley | CS 70 Discrete Mathematics and Probability Theory, Rao and Walrand, Spring 2016 | Note 16, PDF pages 1–5: maps, fibers, permutation law, binomial packet model |
| Stanford | CS 109 Probability for Computer Scientists, Chris Piech, Winter 2025 | Lecture 6 textual slides, PDF pages 1–124; progressive duplicate slides and mathematical figures checked |
| Harvard, additional | Statistics 110, Joe Blitzstein, Strategic Practice 4, Fall 2011 | Section 1 problems 1–3 and their page 4 solutions via the web PDF reader; not the full exercise sheet |

This is a rigorous chapter within a declared boundary. Expectation, its existence and linearity receive their own next chapter; covariance, full joint laws, general transformations, generating-function theory and approximation error bounds have later units. Here they appear only where a short bridge is necessary to understand a law. Week 4 returns to binomial, geometric and Poisson with moments and deeper identities. This chapter derives their probabilities now rather than postponing the model-selection skills.

The instruction and examples are independently written. No finite bibliography establishes that all courses in existence were examined; no teaching resource can guarantee success on every unseen problem. The audits state exactly what was checked and what remains outside scope.

## 2. Outcomes, measurements, and the meaning of a random variable

A probability experiment has a sample space $\Omega$, an event family $\mathcal F$ and a probability measure $P$. A real random variable is a measurable map $X:\Omega\to\mathbb R$. Measurability means that every set $\{\omega:X(\omega)\le t\}$ belongs to $\mathcal F$, so its probability is defined. On a finite sample space with all subsets allowed, every real-valued map has this property automatically.

There are three different objects: the outcome $\omega$, the fixed mapping $X$, and the realized number $X(\omega)$. The mapping does not randomly change during an experiment. Uncertainty concerns which outcome is selected. For two die rolls, an outcome is the ordered pair $(i,j)$; the sum, maximum, absolute difference, and indicator of equal faces are four different maps on the same experiment. Knowing only the sum normally loses the original pair.

Write the event explicitly before calculating:

$$\{X=x\}=\{\omega\in\Omega:X(\omega)=x\}.$$

The braces can be suppressed inside $P(X=x)$, but the probability still belongs to a set of outcomes. The notation $X\le t$ is also an event, not an assertion that every outcome obeys the inequality.

**Worked construction.** Suppose four elementary outcomes have probabilities $1/10,2/10,3/10,4/10$ and map respectively to $-1,2,-1,5$. The outcome probabilities differ, so merely counting two of four outcomes is insufficient. The event $X=-1$ contains the first and third outcomes and has probability $4/10$. The event $X\le2$ contains the first three and has probability $6/10$.

<!-- SIM: mapping -->

Every finite or countable law can also be constructed on its own value space: take $\Omega=S$, set $P(\{x\})=p(x)$, and use $X(\omega)=\omega$. That construction proves existence, but does not restore dependence information discarded from an earlier experiment. [Oxford, Chapter 2](https://courses.maths.ox.ac.uk/mod/resource/view.php?id=48553); [Berkeley, Note 16](https://fa16.eecs70.org/static/notes/n16.pdf).

## 3. Discreteness, range, and effective support

We call a law discrete when its probability is concentrated on a finite or countable set $S$:

$$P(X\in S)=1.$$

The effective atom set is $S_+=\{x:P(X=x)>0\}$. A formal range may contain zero-probability values; an examination's advertised support sometimes means that range, and sometimes means $S_+$. We will state which is intended. In particular, when a parameter reaches an endpoint, a family's effective support can shrink. Bernoulli with $p=0$ is concentrated at zero even though its general formula lists both zero and one.

Discrete does not mean integer-valued, equally spaced, finite, or physically countable in units. A variable with values $\sqrt2,\pi,7/3$ is discrete. A law assigning mass $2^{-k}$ to $1/k$ for $k\ge1$ is discrete even though its values accumulate at zero. A law assigning positive masses to a countable dense set can be discrete without flat CDF intervals between every pair of atoms. Consequently, “every discrete CDF has isolated equally spaced steps” is too strong. A finite atom plot has ordinary separated steps; the general law is a countable sum of jumps.

A continuous sample space can yield a discrete variable: for a uniform draw $U$ from $[0,1]$, the indicator $I=1_{\{U<1/4\}}$ has only two values. Conversely, a real variable with zero mass at each point need not possess an ordinary density; more advanced singular distributions exist. The safe criterion here is concentration on a countable atom set, not a name such as “time” or “measurement.”

## 4. PMF validity and the partition proof

The probability mass function is $p_X(x)=P(X=x)$, defined for all real $x$. It is zero outside the atom set. A discrete PMF must satisfy

$$p_X(x)\ge0,\qquad \sum_{x\in S}p_X(x)=1.$$

**Why normalization holds.** Fibers $\{X=x\}$ for different values are disjoint: a function assigns exactly one value to an outcome. Their union over the concentrated countable set has probability one. Countable additivity therefore gives the displayed sum. For a discrete elementary experiment this also yields

$$p_X(x)=\sum_{\omega:X(\omega)=x}P(\{\omega\}).$$

The two sums act at different levels. The first combines masses of value-events; the second explains where those masses came from. A uniform elementary experiment gives $p_X(x)=|\{X=x\}|/|\Omega|$ only when all elementary outcomes really are equally likely.

**Reverse construction.** Given nonnegative weights summing to one on a countable set, defining singleton probabilities by those weights and summing them on arbitrary subsets constructs a probability measure. Thus nonnegativity plus normalization is both necessary and sufficient for a countable PMF; a formula need not match a named family.

**Parameter audit.** If $p(k)=c(k+1)$ for $k=0,1,2,3$, summing gives $c(1+2+3+4)=10c=1$, hence $c=1/10$. If instead the weights are $(\theta,1-2\theta,\theta)$, normalization holds for every $\theta$, while nonnegativity requires $0\le\theta\le1/2$. Solving only the sum equation would miss the parameter restriction. If all three atoms must have positive mass, the endpoints are excluded.

A PMF ordinate is a probability, not a density height. Connecting PMF points by a smooth curve does not turn the interpolated heights into probabilities. A stem plot is a useful visual contract: location identifies the atom; height identifies its mass. [MIT, Class 4](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_probability.pdf).

## 5. CDF construction and its general properties

The cumulative distribution function is defined for every real threshold:

$$F_X(t)=P(X\le t)=\sum_{x\le t}p_X(x).$$

For atoms $-2,1,4$ with masses $1/5,1/2,3/10$, the CDF is zero below $-2$, $1/5$ on $[-2,1)$, $7/10$ on $[1,4)$ and one on $[4,\infty)$. In particular $F(1)=7/10$, while $F(1^-)=1/5$. A closed dot belongs to the value at an atom; an open dot marks the excluded left limit. A vertical dashed segment illustrates a jump, but intermediate ordinates on that segment are not CDF values at the same threshold.

<!-- SIM: cdf -->

**Monotonicity.** If $a\le b$, then $\{X\le a\}\subseteq\{X\le b\}$; hence $F(a)\le F(b)$. Bounds zero and one follow from the probability axioms.

**Limits.** The events $\{X\le n\}$ increase to the whole sample space as integers $n\to\infty$, giving $F(n)\to1$. The events $\{X\le-n\}$ decrease to the empty set, giving $F(-n)\to0$. These statements assume a real finite-valued variable; if a stopping experiment has nontermination mass, extending it to $+\infty$ changes the upper-limit statement.

**Right continuity.** For thresholds $t_n\downarrow t$, the events $\{X\le t_n\}$ decrease to $\{X\le t\}$. Continuity of a probability measure from above gives $F(t_n)\to F(t)$. This property explains why the interval beginning at each atom includes its left endpoint. Being nondecreasing with correct endpoint limits is insufficient if a proposed function chooses the wrong value at a jump.

**Left limit.** For $t_n\uparrow t$ with $t_n<t$, the event union is $\{X<t\}$. Thus $F(t^-)=P(X<t)$ and

$$p_X(t)=F(t)-F(t^-).$$

The jump formula works at any real atom, not only integers. For an integer-valued variable it simplifies to $p(k)=F(k)-F(k-1)$ because no atoms lie between those integer thresholds. That simplification fails for support $\{0,1/2,1\}$.

## 6. Interval probabilities and exact endpoint handling

Subtracting CDF values is set subtraction. For $a<b$, the following four contracts are different:

| Event | Probability |
|---|---|
| $a<X\le b$ | $F(b)-F(a)$ |
| $a\le X\le b$ | $F(b)-F(a^-)$ |
| $a<X<b$ | $F(b^-)-F(a)$ |
| $a\le X<b$ | $F(b^-)-F(a^-)$ |

Each follows by subtracting the excluded lower event from the included upper event. A useful check is to ask whether mass at each endpoint is included. For the three-atom law above, $P(1<X\le4)=3/10$, $P(1\le X\le4)=4/5$, and $P(1\le X<4)=1/2$.

If $X$ is integer-valued and $a,b$ are real, first translate the inequalities into integer bounds. Then

$$P(a\le X\le b)=F(\lfloor b\rfloor)-F(\lceil a\rceil-1).$$

An empty interval of feasible integers has probability zero; do not evaluate a subtraction with reversed bounds and accept a negative answer. “At most $r$” includes $r$; “fewer than $r$” excludes it. Therefore $P(X\ge r)=1-F(r^-)$ for real thresholds, and $1-F(r-1)$ for integer $r$ when $X$ is integer-valued. The expression $1-F(r)$ describes $X>r$.

<!-- SIM: interval -->

These corrections matter in both exact probabilities and later normal approximations. A continuity correction belongs to an explicitly chosen approximation, not to the definition of the discrete event.

## 7. Recovering a law, quantiles, and inverse selection

A discrete CDF determines its masses by its jumps. Conversely its masses determine the entire CDF, including all non-support thresholds. A candidate finite CDF must have nonnegative jumps, no missing probability after its final atom, correct constant tails, and right continuity. A piecewise function containing a truly increasing linear segment has a continuous component and is not a purely finite-atom law.

For $0<u<1$, define the lower quantile

$$Q(u)=\inf\{x:F(x)\ge u\}.$$

For a finite sorted support, it is the first value whose cumulative mass reaches $u$. It is not generally an ordinary inverse function: flat intervals make $F$ noninjective and jumps omit probability levels. With masses $(1/5,1/2,3/10)$ at $(-2,1,4)$, $Q(1/5)=-2$, while $Q(1/5+\varepsilon)=1$ for a sufficiently small positive $\varepsilon$.

**Sampling contract.** For computation with $U\in[0,1)$, assign the first atom on the interval $[0,p_1)$, the second on $[p_1,p_1+p_2)$, and so on. Choose the first cumulative sum strictly greater than $U$. The boundary convention differs from lower $Q(u)$ at finitely many cumulative endpoints. Since an ideal continuous uniform draw hits each such point with probability zero, both conventions produce the same law. A digital generator has finite possible outputs, so explicit half-open intervals prevent ambiguity in implemented checkpoints.

<!-- SIM: inverse -->

**Proof of the law.** The uniform interval assigned to atom $x_i$ has length $p_i$. Consequently its selection probability is exactly $p_i$ under the ideal uniform model. This is an exact distribution construction; a small random histogram is merely an estimate, not a proof that a sampler is unbiased.

## 8. Changing the measurement: collisions and pushforward mass

Let $Y=g(X)$. Its law comes from preimages:

$$p_Y(y)=\sum_{x:g(x)=y}p_X(x).$$

The proof partitions $\{g(X)=y\}$ into disjoint atom-events $\{X=x\}$. Nonnegative summands allow countable rearrangement. The rule does not require injectivity or differentiability, and it never needs a Jacobian in the discrete case.

**Many-to-one example.** If $X$ has atoms $-2,-1,0,1,2$ with masses $(1,2,4,5,8)/20$ and $Y=X^2$, then $P(Y=0)=4/20$, $P(Y=1)=(2+5)/20$ and $P(Y=4)=(1+8)/20$. There are three destination atoms, but they are not equally likely. The zero preimage is counted once, not twice.

**Decreasing affine example.** For $Y=aX+b$ with $a<0$, solving $Y\le t$ reverses the inequality:

$$F_Y(t)=P\left(X\ge\frac{t-b}{a}\right)=1-F_X\left(\left(\frac{t-b}{a}\right)^-\right).$$

Using $1-F_X((t-b)/a)$ would exclude the mass on the boundary. For $a>0$, $F_Y(t)=F_X((t-b)/a)$; for $a=0$, $Y$ is concentrated at $b$. Full transformation theory comes later, but these event manipulations are necessary now to avoid wrong discrete answers.

<!-- SIM: transform -->

## 9. Same law does not mean same variable or independence

If $X$ and $Y$ have identical PMFs, then they have the same one-variable distribution. This says nothing about $P(X=Y)$ without their joint experiment. Let a fair bit be $B$. Then $X=B$ and $Y=1-B$ have the same law but are never equal. Taking $Y=B$ preserves that same marginal law but makes them always equal. Taking an independently generated fair bit for $Y$ gives equality probability $1/2$.

For four outcomes of equal probability, define $(X,Y)$ respectively as $(0,0),(0,1),(1,0),(1,1)$. This is the independent construction. For only two outcomes $(0,0),(1,1)$ of equal probability, both marginals remain fair but dependence is perfect. Thus a request for the law of a sum cannot usually be answered from two marginals alone.

Independence of discrete variables means $P(X=x,Y=y)=p_X(x)p_Y(y)$ for every pair of atom values. It permits multiplication for conjunctions of the corresponding events. Merely giving equal distributions is not that condition. The chapter uses independence only where explicitly stated. [Harvard, Strategic Practice 4, Section 1](https://stat110.hsites.harvard.edu/sites/g/files/omnuum10111/files/stat110/files/strategic_practice_and_homework_4.pdf).

## 10. Bernoulli, indicators, categorical, and discrete uniform laws

A Bernoulli variable records one binary event: $I=1_A$ is one on $A$ and zero outside it. Its masses are $p_I(1)=P(A)=p$ and $p_I(0)=1-p$, with $0\le p\le1$. It need not be the output of an actual coin. It may record a packet's successful arrival, a parity condition, or a complicated event involving an entire experiment.

Repeated appearances of the same indicator do not create independent trials. For $I+I$, the possible counts are zero and two, with masses $1-p,p$. A binomial with two independent trials has positive mass at one when $0<p<1$. The change in support is already a decisive counterexample.

A categorical law assigns masses $p_1,\ldots,p_m$ to $m$ distinct labels encoded as values. These probabilities need not be equal. A discrete uniform law on $m$ distinct values has mass $1/m$ at each. For integers $a\le X\le b$, the number of atoms is $b-a+1$, not $b-a$, and

$$P(X\in A)=\frac{|A\cap\{a,a+1,\ldots,b\}|}{b-a+1}.$$

Relabeling by a bijection preserves uniformity on the new finite value set. A many-to-one map generally does not: equal fiber sizes are needed for a uniform resulting law. A modulo operation on an integer interval can create unequal fiber counts when its length is not a multiple of the modulus.

## 11. Binomial law: derive the sequence count before using the formula

Let $I_1,\ldots,I_n$ be independent Bernoulli variables with the same success probability $p$, and set $X=\sum_{j=1}^n I_j$. Every length-$n$ success/failure sequence containing $k$ successes has probability $p^k(1-p)^{n-k}$. There are $\binom nk$ such sequences, and their events are disjoint. Thus

$$p_X(k)=\binom nk p^k(1-p)^{n-k},\qquad k=0,1,\ldots,n.$$

Normalization is the binomial theorem: the sum is $(p+(1-p))^n=1$. Interpret $p=0$ and $p=1$ as point masses, avoiding ambiguous programming evaluations such as $0^0$. For $n=0$, the empty sum is zero with probability one.

The model requires a fixed number of trials, mutual independence, common success probability and a count of successes. A finite integer range alone is insufficient. Sampling without replacement creates dependence; independent trials with unequal probabilities create a different count law; waiting until a target number of successes changes the stopping rule.

**Dynamic derivation.** Let $b_j(k)$ be the probability of $k$ successes after $j$ trials. The last trial partitions the event into a failure after $k$ previous successes and a success after $k-1$ previous successes:

$$b_j(k)=(1-p)b_{j-1}(k)+p b_{j-1}(k-1).$$

Start with $b_0(0)=1$ and treat impossible indices as zero. Each old mass splits into two destinations; the total remains one. The visualization exposes both incoming contributions and each row's actual probabilities rather than showing a decorative falling ball.

<!-- SIM: binomial -->

**Calculation.** For five independent devices working with probability $3/4$, exactly four work with probability $\binom54(3/4)^4(1/4)=405/1024$. At least four work adds the all-five event, producing $(405+243)/1024=81/128$. Multiplying only $\binom54(3/4)^4$ counts overlaps and ignores failed devices; its value can exceed one.

## 12. Binomial tails, modes, and two-stage eligibility

For integer $r$, $P(X\ge r)=\sum_{k=r}^n p_X(k)=1-\sum_{k=0}^{r-1}p_X(k)$. A short lower tail is often easier than a long upper tail. Outside support, the event may be certain or impossible; handle this before evaluating factorials.

For $0<p<1$ and $0\le k<n$, adjacent masses obey

$$\frac{p_X(k+1)}{p_X(k)}=\frac{n-k}{k+1}\frac{p}{1-p}.$$

The ratio exceeds one precisely when $k+1<(n+1)p$. Therefore if $(n+1)p$ is noninteger there is a unique mode $\lfloor(n+1)p\rfloor$; if it is an integer $m$, the two modes are $m-1,m$. This ratio is often more useful than fully evaluating all masses. Endpoint parameters are degenerate cases and must be handled separately.

**Eligibility then success.** Suppose each object independently qualifies with probability $a$ and, conditional on qualification, succeeds with probability $b$. Across objects, assume the complete per-object experiments are independent. Each object contributes one with probability $ab$; thus the total is $\operatorname{Bin}(n,ab)$. An alternative derivation conditions on the number of eligible objects and sums binomial probabilities. Using $b$ alone ignores qualification; fixing the random eligibility count at its mean changes the law.

For four fair coins tossed again only after a first head, the successful per-coin event is two heads with probability $1/4$. The second-round head count is therefore $\operatorname{Bin}(4,1/4)$, even though the number of actual second tosses is random. Its original examination version appears in the solved bank with both derivations.

## 13. Independent unequal trials and shared random environments

For independent Bernoulli trials with probabilities $p_1,\ldots,p_n$, the sum has a Poisson-binomial law. Its PMF is the coefficient of $z^k$ in

$$\prod_{j=1}^n((1-p_j)+p_jz).$$

This identity records a choice of success or failure from each factor. It is not yet a general generating-function course; it is a compact encoding of the same disjoint sequence sum. The recurrence in Section 11 works with the current $p_j$. For two trials with probabilities $1/4,3/4$, the masses at zero, one and two are $3/16,10/16,3/16$. Replacing both probabilities by their mean $1/2$ would give $4/16,8/16,4/16$.

If a random parameter is chosen once for a whole experiment, conditional independence does not imply unconditional independence. Suppose a device chooses a coin with success probability $1/4$ or $3/4$ equally likely, then tosses that chosen coin twice. The count masses are $5/16,6/16,5/16$, obtained by averaging the two conditional binomial laws. Each single toss is marginally fair, yet the two-toss count is not $\operatorname{Bin}(2,1/2)$. If the coin type is freshly and independently chosen before each toss, the count really is that binomial. The timing of the hidden choice is part of the model.

<!-- SIM: unequal -->

## 14. Hypergeometric sampling and support constraints

An urn has $N$ distinct objects, $K$ marked successes and $N-K$ failures. Select $n$ objects uniformly without replacement. Every $n$-subset is equally likely. Exactly $k$ marked objects can be selected in $\binom Kk\binom{N-K}{n-k}$ ways, so

$$p_X(k)=\frac{\binom Kk\binom{N-K}{n-k}}{\binom Nn}.$$

The parameter conditions are integers $0\le K\le N$ and $0\le n\le N$, with $N\ge1$. Feasible counts satisfy

$$\max(0,n-(N-K))\le k\le\min(n,K).$$

The lower bound forces enough successes when failures cannot fill all selected slots. The upper bound prevents choosing more successes than available or more than the sample size. Normalization follows by partitioning all $n$-subsets according to their number of successes, equivalently Vandermonde's identity.

For $N=8,K=3,n=4$, feasible counts are zero through three. The respective numerators are $5,30,30,5$, over denominator $70$. The probability of at least two successes is $35/70=1/2$. A binomial with $p=3/8$ would correspond to replacement and has different masses.

**Sequential state derivation.** After $j$ draws with $k$ successes, the next success probability is $(K-k)/(N-j)$, and the next failure probability is $(N-K-(j-k))/(N-j)$. Propagate the probability of each feasible state along these two branches. Although the drawing order has more elementary outcomes than subset selection, both constructions yield the same success-count law. The laboratory checks that equivalence on exact finite examples.

<!-- SIM: hypergeometric -->

## 15. Geometric waiting and the off-by-one distinction

Let independent trials have constant success probability $p$ with $0<p\le1$ and write $q=1-p$. Let $T$ count all trials through the first success, and let $G=T-1$ count failures before it. Then

$$P(T=t)=q^{t-1}p\quad(t\ge1),\qquad P(G=g)=q^gp\quad(g\ge0).$$

The event $T=t$ requires exactly the first $t-1$ failures followed by success. There is only one such binary pattern; a binomial coefficient would count inadmissible earlier successes. Summing either geometric series gives one. At $p=1$, $T=1$ and $G=0$ surely. At $p=0$, success never occurs; this does not define a normalized finite waiting-time PMF.

For integer $m\ge0$, $P(T>m)=q^m$: the first $m$ trials all fail. Thus for real $x\ge1$,

$$F_T(x)=1-q^{\lfloor x\rfloor}.$$

Below one the CDF is zero. For $G$, $P(G>m)=q^{m+1}$ and $F_G(x)=1-q^{\lfloor x\rfloor+1}$ for $x\ge0$. A shift of one in support creates a shift of one in the exponent.

**Memorylessness.** For nonnegative integers $s,t$ with $P(T>s)>0$,

$$P(T>s+t\mid T>s)=\frac{q^{s+t}}{q^s}=q^t=P(T>t).$$

This describes the remaining number of trials after known failures. With $p=1$, conditioning on survival beyond a positive trial is impossible; never divide by that zero-probability event. For varying independent success probabilities $p_j$, the survival becomes $\prod_{j=1}^m(1-p_j)$ and generally loses memorylessness. A fixed cap also changes the stopping variable.

<!-- SIM: geometric -->

**Characterization.** A positive integer waiting variable with $S(m)=P(T>m)$ and $S(s+t)=S(s)S(t)$ obeys $S(m)=S(1)^m$ by induction. If it is proper, $S(1)<1$, so its jumps are a geometric PMF. No finite collection of observations proves this identity for an unknown process; it is a theorem under the stated condition.

## 16. Negative binomial stopping and capped waiting

Let $T_r$ count all independent trials through the $r$ th success, for integer $r\ge1$ and constant $0<p\le1$. The last trial must be a success. Among the preceding $t-1$ trials, choose exactly $r-1$ successful positions. Hence

$$P(T_r=t)=\binom{t-1}{r-1}p^r q^{t-r},\qquad t=r,r+1,\ldots.$$

The failures-before-$r$ th-success convention is $G_r=T_r-r$, with

$$P(G_r=g)=\binom{g+r-1}{r-1}p^r q^g,\qquad g\ge0.$$

One normalization proof sums all disjoint stopping sequences and observes that independent trials with $p>0$ reach the fixed target almost surely. More algebraically, expanding the product of $r$ geometric series gives $(1-q)^{-r}=\sum_{g\ge0}\binom{g+r-1}{r-1}q^g$; multiplying by $p^r$ gives one. The coefficient counts compositions of $g$ failures across $r$ inter-success waits.

**Fixed-time link.** For integer $m\ge r$, $T_r\le m$ precisely when the first $m$ trials contain at least $r$ successes. Thus $P(T_r\le m)=P(\operatorname{Bin}(m,p)\ge r)$. This translates a stopping event into a fixed-count event without treating $T_r$ itself as binomial.

For a cap $c\ge1$, the variable $W=\min(T,c)$ has masses $pq^{w-1}$ for $1\le w<c$, but $P(W=c)=q^{c-1}$. The final mass includes both success at trial $c$ and continued failure. If the experiment instead returns a distinct “no success” code, its mass is $q^c$ and success at $c$ remains separate. Censoring and conditioning on success by the cap are different operations.

<!-- SIM: stopping -->

## 17. Poisson counts, normalization, and the rare-event limit

For $\lambda\ge0$, a Poisson law has

$$p_X(k)=e^{-\lambda}\frac{\lambda^k}{k!},\qquad k=0,1,2,\ldots.$$

At $\lambda=0$, define the law as concentrated at zero. For positive $\lambda$, normalization is the exponential series $e^{-\lambda}\sum_{k\ge0}\lambda^k/k!=1$. A Poisson variable counts events in a specified window; $\lambda$ is the mean count parameter for that window. If a homogeneous arrival-rate model with rate $r$ is explicitly given, a window of length $t$ uses $\lambda=rt$. A count having a stated average alone does not establish a Poisson law or independent increments.

Adjacent probabilities satisfy $p(k+1)/p(k)=\lambda/(k+1)$. If $\lambda$ is noninteger, the unique mode is $\lfloor\lambda\rfloor$; for positive integer $\lambda=m$, the modes are $m-1,m$. The zero-parameter case has one mode at zero.

For $X_n\sim\operatorname{Bin}(n,\lambda/n)$ and a fixed nonnegative integer $k$, write

$$P(X_n=k)=\frac{\lambda^k}{k!}\prod_{j=0}^{k-1}\left(1-\frac jn\right)\left(1-\frac\lambda n\right)^n\left(1-\frac\lambda n\right)^{-k}.$$

As $n\to\infty$, the finite product and final factor approach one while the middle factor approaches $e^{-\lambda}$. This proves the pointwise rare-event limit. It is not a blanket assertion that any finite binomial tail is exactly Poisson. At finite $n$, $p=\lambda/n$ must lie in $[0,1]$; a precision requirement needs an error analysis beyond a resemblance of plotted bars.

A displayed finite Poisson prefix is not the entire support. Its omitted upper tail remains a separate probability, never silently renormalized onto visible bars. The lab exposes that tail and can inspect its growth as the displayed cutoff increases.

<!-- SIM: poisson -->

## 18. Conditioning, truncation, and mixtures of discrete laws

For an event $A$ with $P(A)>0$, the conditional PMF is

$$p_{X\mid A}(x)=\frac{P(X=x,A)}{P(A)}.$$

When $A=\{X\in B\}$, this simplifies to $p_X(x)/P(X\in B)$ on $B$ and zero outside it. The conditioning denominator is the retained mass. A zero-truncated Poisson therefore has $e^{-\lambda}\lambda^k/(k!(1-e^{-\lambda}))$ at $k\ge1$ for $\lambda>0$. It is not an ordinary Poisson with a merely shifted parameter.

For a geometric waiting time conditioned on $T\le c$, masses $pq^{t-1}$ at $1\le t\le c$ divide by $1-q^c$. Capped $\min(T,c)$ instead accumulates all later mass at its final atom, as Section 16 shows. An examination can distinguish the two using only their last mass.

A mixture chooses a regime $H$ with probabilities $w_h$ and then draws according to $p_h$. Total probability yields $p_X(x)=\sum_hw_hp_h(x)$. Both the weights and each component law must normalize. Zero mass in one component does not prevent another component from assigning that atom positive mass. The family-size examination problem in the bank gives a countable mixture whose conditioning changes the entire geometric parameter.

<!-- SIM: conditional -->

## 19. Combining independent measurements: convolution and extrema

For independent discrete $X,Y$, the law of $Z=X+Y$ is

$$p_Z(z)=\sum_xp_X(x)p_Y(z-x).$$

To derive it, partition $\{X+Y=z\}$ by the value of $X$, then use independence on each corresponding pair. Each pair appears on exactly one sum diagonal. Without independence, use the joint mass $P(X=x,Y=z-x)$ instead of the product. The finite lab highlights the actual contributing cells, accumulating their numeric masses into the chosen sum atom.

For two independent uniform values on $\{1,2,3\}$, sum masses on $2,3,4,5,6$ are $(1,2,3,2,1)/9$. The sum is not uniform: there are three pairs yielding four but one yielding two. Independent binomials with the same $p$ add to a binomial because their underlying independent trial blocks concatenate. Unequal $p$ does not generally preserve that family. Independent Poisson laws add to a Poisson by the binomial theorem applied to the convolution sum.

<!-- SIM: convolution -->

For independent variables with CDFs $F_j$, the maximum $M$ obeys $F_M(t)=\prod_j F_j(t)$ because all values must be at most $t$. The minimum $L$ satisfies $P(L>t)=\prod_j(1-F_j(t))$, hence $F_L(t)=1-\prod_j(1-F_j(t))$. Strict threshold tails are used consistently. For iid integer variables, differencing the resulting CDF recovers atom masses. For two uniform dice on $1,\ldots,m$, $P(M=k)=(k^2-(k-1)^2)/m^2=(2k-1)/m^2$. This proof uses nested squares of elementary outcomes, not a claim that the maximum is uniform.

<!-- SIM: extrema -->

## 20. Exact computational methods and numerical limits

The shortest correct method depends on the requested event. Use a finite fiber table for a nonlinear measurement on a small experiment; a CDF difference for an interval; a complement for a short excluded tail; dynamic propagation for unequal independent trials; subset counting for sampling without replacement; a survival product for waiting. Formula recognition follows the experiment contract, not the other way around.

```python
from fractions import Fraction

def success_count(probabilities):
    # Input probabilities are exact Fractions in [0, 1].
    row = [Fraction(1)]
    for p in probabilities:
        nxt = [Fraction(0)] * (len(row) + 1)
        for k, mass in enumerate(row):
            nxt[k] += mass * (1 - p)
            nxt[k + 1] += mass * p
        assert sum(nxt) == 1
        row = nxt
    return row
```

**Correctness proof.** Initially only the empty experiment is possible, with count zero. Assume the current row is the true law after the preceding trials. Partition the event after the next independent trial by its final success indicator. Each old mass contributes to its unchanged count on failure and its count plus one on success. These cases are disjoint and exhaustive. The update therefore yields the next true law, and conservation follows because each split has weights $1-p,p$. Induction proves the whole algorithm. Its arithmetic cost is $O(n^2)$ with $O(n)$ storage; direct enumeration needs $2^n$ binary sequences. Exact rational arithmetic also has a growing bit cost that the simple operation count omits.

Large factorial expressions can overflow even when the final probability is small. For ordinary numerical work, use log-factorials, stable recurrences, or established probability routines. Starting a long binomial recurrence at an underflowed $p(0)$ cannot recover the lost masses; a centered recurrence or log representation is safer. Rounding intermediate probabilities can make their sum slightly differ from one. Never use such rounding to hide a genuinely unnormalized PMF. The visual lab uses bounded finite-precision inputs; the audit separately compares small exact rational calculations and analytic tail identities.

## 21. A complete model-selection decision

Suppose a packet system transmits a fixed block of five packets. If packet successes are mutually independent and each succeeds with probability $4/5$, its success count is binomial. If exactly three of eight physical packets are marked and four are chosen without replacement, the marked-count law is hypergeometric. If independent attempts continue through the first success, the trial-count law is positive-based geometric. If attempts continue through the third success, it is negative binomial with total-trial support starting at three. If an explicitly specified homogeneous count process has rate two per unit time, its three-unit count is Poisson with parameter six. These are different experiments even when each statement contains “count.”

Now remove independence from the five-packet experiment. Let one Bernoulli event determine whether all five succeed together. Each individual success probability is still $4/5$, but the count has only atoms zero and five, with masses $1/5,4/5$. This example shows exactly which assumption supports the binomial formula. Likewise, a changing success probability destroys the simple geometric survival power, and a common latent probability produces a mixture rather than a binomial with the marginal average.

When several methods are available, agreement is a useful check. The hypergeometric subset formula and sequential propagation should agree; the two-stage eligible-count conditioning sum and per-object thinning should agree; a PMF interval sum and a CDF difference should agree. Disagreement identifies an endpoint, support, dependence, or counting error that must be resolved before a result is accepted.

## 22. Chapter synthesis

A discrete variable is a numeric measurement on an experiment whose law is concentrated on countably many atoms. Its PMF aggregates elementary probability by fibers, and its CDF aggregates atom probability by thresholds. Right continuity fixes included jump endpoints; left limits distinguish strict events. A deterministic transformation sums all preimage masses. A marginal law does not determine dependence.

The common families encode different experiment contracts: Bernoulli for one event, uniform for equal atom masses, binomial for fixed independent equal-probability trials, Poisson-binomial for independent unequal trials, hypergeometric for uniform sampling without replacement, geometric for first-success waiting, negative binomial for a fixed-success stopping target, and Poisson for a specified count law or a carefully qualified rare-event approximation. Conditioning, capping and mixtures change those contracts in distinct ways.

Mastery requires reconstructing the event, verifying support and normalization, choosing a derivation, keeping endpoint conventions, and interpreting the answer. The final rules give concrete calculation triggers and counterexamples; the solved bank develops the same reasoning across medium and hard problems.

## 23. Fully worked mathematical and conceptual problems

Three authentic questions retain the source scan's option order and explicitly identify independently derived answers. Eighty independently authored or reconstructed course-inspired problems cover the declared chapter boundary. Course-inspired wording and data are independent; these are not a verbatim collection of every copyrighted course exercise. Every solution states the operative event or contract, develops the calculation, and explains the main alternative mistake. Relevant simulations sit inside the corresponding solutions.

<!-- INCLUDE: problems -->

## 24. Examination rules, edge cases, and final notes

Read these rules after the full derivations. Each rule connects a question trigger to its conditions, computation, and likely error. They are complete statements, not unexplained formulas or generic study advice.

<!-- INCLUDE: review -->

## 25. Editable distribution laboratory

Choose a model and edit its stated inputs. Each computation begins paused and exposes its exact stored states, operation, cause, probability checks and state changes. Finite diagrams illustrate a specified calculation; their checkpoints are not proofs about every possible input. Infinite laws display a prefix with a separately labelled omitted tail. The written arguments supply general proofs.

<!-- LAB: discrete -->

## 26. References and provenance

1. James Martin. *Prelims Probability*, Michaelmas Term 2019, version of 20 October 2019. University of Oxford. Chapter 2 definitions and Section 2.1, PDF pages 18–21. [Lecture notes](https://courses.maths.ox.ac.uk/mod/resource/view.php?id=48553). Earlier note versions by Christina Goldschmidt and others are acknowledged in the source.
2. Jeremy Orloff and Jonathan Bloom. *18.05 Introduction to Probability and Statistics*, Spring 2022. Massachusetts Institute of Technology. Class 4, Discrete Random Variables, combined probability-reading PDF pages 28–39. [Written course material](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_probability.pdf).
3. Rao and Walrand. *CS 70 Discrete Mathematics and Probability Theory*, Spring 2016. University of California, Berkeley. Note 16, Random Variables: Distribution and Expectation, reviewed PDF pages 1–5, hosted in the Fall 2016 archive. [Note 16](https://fa16.eecs70.org/static/notes/n16.pdf).
4. Chris Piech. *CS 109 Probability for Computer Scientists*, Winter 2025. Stanford University. Lecture 6, Random Variables and Binomial, textual slides and checked mathematical figures. [Lecture slides](https://web.stanford.edu/class/archive/cs/cs109/cs109.1254/lectures/6-RandomVariables/6-RandomVariables.pdf). The slides also credit the course teaching team and earlier contributors.
5. Joe Blitzstein. *Statistics 110: Probability*, Fall 2011. Harvard University. Strategic Practice 4, Section 1, problems 1–3 and corresponding PDF page 4 solutions, reviewed through the web PDF reader. [Practice and solutions](https://stat110.hsites.harvard.edu/sites/g/files/omnuum10111/files/stat110/files/strategic_practice_and_homework_4.pdf). Direct file acquisition was blocked; no full-file review is claimed.
6. *Iranian MSc Computer Engineering Examination 1405*, Q 35, original PDF page 8; *Iranian PhD Computer Science Examination 1404*, Q 68–69, original PDF page 15. [Project examination archive](https://github.com/bheydari721rn24/Phd-Exam-CSE/tree/bdadf6e2c9cadc4772ae137a96a3da753c7cfd08/Exams). English adaptations preserve checked option order; answers are independently derived, not official keys.

Source hashes, bounded reading scopes, mathematical checks, model checks, real-browser review and library-retention evidence are available through the chapter's [source audit](../reviews/s_discrete-sources.html) and [quality audit](../reviews/s_discrete-quality.html). No source claim relies on an unread index or an unavailable download.
