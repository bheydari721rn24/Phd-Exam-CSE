## Mathematical constructions for uniform growth claims

### 1. Construct a threshold and quantify what it proves

Consider $F(n)=3n^2+5n$. Its normalized ratio is $3+5/n$. To prove an upper bound with a prescribed constant $c>3$, solve $5/n\le c-3$, giving $n\ge5/(c-3)$. A convenient integer threshold is $\max(1,\lceil5/(c-3)\rceil)$. At $c=3$, the inequality fails at every finite positive size. The limit three is the infimum of valid eventual upper constants, not an attained witness.

To prove equivalence to $3n^2$, normalize by the full proposed equivalent: $F/(3n^2)=1+5/(3n)$. For each error $\varepsilon>0$, choose $n>5/(3\varepsilon)$. This establishes a ratio tending to one. Equivalence to $n^2$ fails because that ratio tends to three, even though both reference functions have the same tight class. These witness calculations explain the difference among exact arithmetic, one-sided bounds, tightness and equivalence.

A negative result has a different quantifier order. To refute $n^2\in O(n)$, defeat every proposed $c,N$ by choosing an integer $n>\max(c,N)$. Such a choice makes $n^2>cn$. Finding one bad small input does not accomplish that universal disproof.

### 2. Classify an oscillating ratio using two envelopes

Assume $g(n)>0$ eventually and put $r(n)=f(n)/g(n)\ge0$. An eventual finite upper bound on $r$ characterizes $O(g)$; an eventual positive lower bound characterizes $\Omega(g)$. Both characterize $\Theta(g)$. A unique limit is unnecessary for these envelope tests.

For $F(k)=k(2+(-1)^k)$, the ratio to $k$ is one or three, and $1\le r(k)\le3$ supplies tight witnesses. For $f(n)=n$ on evens and $n^2$ on odds, the ratio to $n$ is one or $n$; its upper envelope is unbounded, excluding $O(n)$. Relative to $n^2$, the ratio is $1/n$ or one; it has no eventual positive lower envelope, excluding $\Omega(n^2)$.

For a genuinely incomparable pair, use $f(n)=n$ on evens and $n^3$ on odds against $g(n)=n^2$. The even ratios tend to zero and the odd ratios to infinity. This defeats both one-sided bounds, while neither strict ratio limit exists. The normalized samples in the question animations illustrate these different envelope behaviors; the subsequence arguments prove the tail statements.

### 3. Exponentiate a difference, not a broad growth class

For fixed $a>1$, the exact quotient $a^{u(n)}/a^{v(n)}=a^{u(n)-v(n)}$ controls every relation. The original exponentials are tightly equivalent exactly when the exponent difference is bounded above and below eventually. If the difference tends to positive infinity, the first exponential is strict larger order; if it tends to negative infinity, it is strict smaller order. A bounded oscillating difference preserves tightness even if the ratio has no limit.

The distinction is visible for $u=n^2+n$ and $v=n^2$. Their ratio tends to one, but their difference tends to infinity. Thus their exponentials are not tightly equivalent. Conversely, $u=n+(-1)^n$ and $v=n$ have bounded difference, so their base-two exponentials have ratios alternating between one half and two, proving tightness without equivalence.

Logarithms are also conditional. If $f,g>0$ eventually and $f\in\Theta(g)$, then $\ln f-\ln g$ is bounded. If additionally $g\to\infty$, dividing that bounded difference by $\ln g$ proves $\ln f\sim\ln g$. Without that growth premise, take $f=2$ and $g=1$: the original functions are tightly equivalent but their logarithms are not. The reverse implication fails for growing functions too, as the preceding quadratic-exponent example shows.

### 4. Derive harmonic bounds from decreasing rectangles

For $1/x$ decreasing on positive arguments, its integral over $[k,k+1]$ is at most $1/k$. Summing these rectangles gives $\ln(n+1)\le H_n$. On $[k-1,k]$ for $k\ge2$, the integral is at least $1/k$. Summing and separating the first term gives $H_n\le1+\ln n$.

These are rigorous lower and upper bounds. On $n>1$, dividing by $\ln n$ yields a ratio trapped between $\ln(n+1)/\ln n$ and $1+1/\ln n$, both tending to one. Consequently $H_n\sim\ln n$. It is still false that $H_n=\ln n$: the finite rational sum and the logarithm are distinct quantities.

Grouping terms gives another proof of divergence. The block $k=2^{j-1}+1,\ldots,2^j$ contains $2^{j-1}$ terms, each at least $2^{-j}$, so every complete block contributes at least one half. The number of such blocks up to $n$ is logarithmic. This argument explains why infinitely many shrinking positive increments can accumulate an unbounded but sublinear sum.

### 5. Separate fixed parameters from uniformly varying parameters

A witness constant for a one-variable family can depend on a truly fixed coefficient, exponent or logarithm base. It cannot depend on the input variable. In a two-variable bound, decide whether both variables exceed their own thresholds or whether a single combined size tends to infinity; these are different tail conventions.

For $T(m,n)=m\log_2 n+n$ with independent $m,n\ge2$, both contributions must remain. Along $m=n^2$, the first dominates; along $m=\lfloor\sqrt n\rfloor$, the second dominates; both paths grow both variables and remain admissible under the joint-tail convention. Neither single term uniformly replaces the sum. The pointwise maximum does: for nonnegative $A,B$, $\max(A,B)\le A+B\le2\max(A,B)$.

If a constraint supplies $m=n$, the same expression reduces to tight $n\log n$ order. If $m\le n/(\log_2 n)$, it instead has tight linear order in $n$. Changing the domain can change the answer even when the algebraic function is unchanged. State those restrictions before simplifying a graph, matrix or multivariate running time.

### 6. Interpret the retained model animations precisely

The threshold animation uses $F(n)=3n+7$ and candidate upper envelope $4n$. Its normalized ratio is $3+7/n$. The inequality is equivalent to $n\ge7$, not to every positive input. The saved checkpoints at one, two and four show finite exceptions; eight, sixteen and thirty-two show inputs beyond the threshold. Their success alone is not the proof: solving the inequality supplies the universal tail statement.

The encoding animation compares the numerical parameter $2^k$ with its ordinary binary length $k+1$. The doubling animation visits $1,2,4,8,16$ under the guard $x<17$, then exits at 32. Together they illustrate a fixed number of logarithmic stages versus the numerical sizes visited. They do not prove an arbitrary program's cost merely from its largest value, and do not represent the authentic square-root recurrence.

The separate recurrence-tree animation uses the explicitly different model $T(n)=2T(n/2)+n$, with $n=8$ and $T(1)=1$. Internal levels contain one, two and four calls with sizes eight, four and two; the final level contains eight unit-cost base calls. Every displayed level therefore contributes eight, giving total cost thirty-two. Its equal-size splitting and linear toll are stated assumptions. It is an introduction to level accounting, not a simulation of either unequal splitting or the square-root recurrence in the authentic questions.

The question-specific oscillation and binary-floor animations below use each question's actual normalized functions. Their axes label the input and ratio explicitly, and their captions distinguish saved finite samples from the general subsequence proofs. Points on a discrete domain are not a continuous interpolation theorem.
