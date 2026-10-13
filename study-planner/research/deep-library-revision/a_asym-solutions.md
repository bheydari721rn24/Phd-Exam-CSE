# Individually authored asymptotic solutions — revision draft

## Q1

**Correct option: 2.** The hypotheses make both shrink factors fixed numbers strictly between zero and one. This matters: the recurrence describes two unequal children whose sizes sum to their parent's size, rather than two equal children. Let $B>0$ be a fixed stopping size, $\delta=\min(\alpha,\beta)$ and $q=\max(\alpha,\beta)$. First consider exact real-size splits so their tree geometry is visible.

Every node at depth $j$ has size between $n\delta^j$ and $nq^j$. Before $n\delta^j$ reaches $B$, all nodes at that depth are internal. Their sizes sum to $n$, because splitting conserves size. Consequently each such full level contributes exactly $n$ units of nonrecursive work. There are $\Theta(\ln n)$ full levels, with the constant depending on the fixed $\delta$. This supplies the lower bound $\Omega(n\ln n)$.

Every path terminates once $nq^j\le B$, which requires only $O(\ln n)$ levels. At a partly terminated level, the active-node sizes sum to at most $n$. Therefore all internal tolls total $O(n\ln n)$. A nonroot leaf has size greater than $\delta B$ and at most $B$, because its parent exceeded $B$. Leaf sizes sum to $n$, so there are $\Theta(n)$ leaves; their bounded base costs add at most linear work. Both bounds establish $T(n)\in\Theta(n\ln n)$.

For ordinary integer rounding, the same order follows from the standard bounded-perturbation version of the divide-and-conquer recurrence theorem. Its branching exponent solves $\alpha^p+\beta^p=1$: here $p=1$, and the toll integral is $\int_1^n u/u^2\,du=\ln n$. This application requires fixed shrink factors, a fixed base region and the usual bounded rounding errors; it is not an assertion for arbitrary size-dependent perturbations.

Options 1 and 4 have linear order because $\alpha,\beta$ are constants and $\ln n=O(n)$. They cannot upper-bound the derived cost. Option 3 is also too small: its ratio to $n\ln n$ is $\beta n^{\alpha-1}\to0$. Option 2 is the valid listed upper bound. If $\alpha$ were permitted to approach zero with $n$, the fixed-depth constants used above would cease to be uniform.

## Q2

**Correct option: 3.** Take logarithms in one fixed base; changing that base multiplies the toll by a fixed positive constant. Put $L=\ln n$ and $a=\ln(3/2)>0$. After $j$ exact recursive reductions, the argument is $(2/3)^jn$, so its logarithm is $L-ja$. With a fixed base threshold, the number of nonbase levels is $h=L/a+O(1)$.

Unrolling the single chain gives

$$T(n)=O(1)+\sum_{j=0}^{h-1}(L-ja)^2.$$

There are $O(L)$ terms, each at most $L^2$, proving $O(L^3)$. For a lower bound, consider only $0\le j\le L/(2a)$, leaving aside a fixed endpoint adjustment. There are $\Theta(L)$ such terms, and each has $L-ja\ge L/2$. Their sum is at least a positive fixed multiple of $L^3$. Thus $T(n)\in\Theta((\ln n)^3)$.

A concrete exact subsequence checks the accumulation. For $n=(3/2)^h$ and a base at one, the toll sum is $a^2\sum_{r=1}^h r^2=a^2h(h+1)(2h+1)/6$. The cubic power comes from summing squared decreasing logarithms, not from multiplying arbitrary complexity symbols.

Option 2 counts only the largest toll, omitting the many other large tolls. Option 4 multiplies a root-sized squared-logarithm toll by a linear number of inputs rather than a logarithmic number of levels: its proposed tight order is $\Theta(n\log^2 n)$, whose ratio to the actual cost grows as $n/\log n$. Option 1 is a loose upper bound for sufficiently large $n$, but it asserts a *tight linear* order, which fails because $(\ln n)^3/n\to0$. In this question the options use $\Theta$, so a loose upper bound does not make another option correct. Rounding the argument must still guarantee eventual reduction into the fixed base region.

## Q3

**Correct option: 1 under the smallest-listed-upper-bound convention.** The tight order is $\Theta(\ln n\,\ln\ln n)$. The original options use $O$, so options 2 and 3 are valid looser upper bounds as well. Preserve that wording ambiguity when using this authentic question; the derivation identifies the tight order without treating three true upper bounds as logically exclusive.

Let $m=\log_2 n$. Ignoring rounding momentarily, taking a square root halves $m$, so $S(m)=T(2^m)$ satisfies $S(m)=2S(m/2)+m$. At depth $j$, there are $2^j$ nodes, each with toll $m/2^j$. Total toll is exactly $m$ per nonbase level. There are $\Theta(\log m)$ levels, and the leaves contribute $O(m)$ bounded base work. Hence $S(m)\in\Theta(m\log m)$.

The floor does not invalidate this reasoning, but it requires control. Use a constant base region containing one and two. For $x\ge4$, $\sqrt x/2\le\lfloor\sqrt x\rfloor\le\sqrt x$. Taking base-two logarithms gives

$$m/2-1\le\log_2\lfloor\sqrt x\rfloor\le m/2.$$

Repeated reduction bounds a level-$j$ logarithmic argument between $m/2^j-2$ and $m/2^j$. Therefore a level's toll is at most $m$, and, while $2^j\le m/4$, at least $m-2^{j+1}\ge m/2$. There are $\Theta(\log m)$ significant levels and only $O(m)$ leaves, giving matching upper and lower bounds despite rounding. Small endpoint levels alter constants only. Stopping solely below one would fail to terminate at one because its square root remains one.

Substitution returns $m\log m=\Theta(\log n\log\log n)$. Option 2 adds a factor $n$ to the tight upper bound. Option 3 replaces the leading $\log n$ by $n$; its ratio to the tight bound is $n/\log n\to\infty$. Both are valid loose upper bounds. Option 4 omits the required $\log n$ factor and is too small. On $n=2^{2^h}$, all square roots are exact until the base, providing the independent check $S(2^h)/2^h=S(1)+h$ under a unit base-two logarithmic toll.

## Q4

**Correct option: 4.** This recurrence multiplies the previous value by a changing factor. Its expansion is a product, unlike an additive-toll recurrence:

$$T(n)=2^n2^{n-1}\cdots2^1T(0)=2^{1+2+\cdots+n}=2^{n(n+1)/2}.$$

The base value $T(0)=1$ is essential for this exact identity. Taking a base-two logarithm gives the simple additive relation $\log_2T(n)-\log_2T(n-1)=n$, with zero initial logarithm.

| $n$ | Multiplying factor | Exact $T(n)$ | $\log_2T(n)$ |
| ---: | ---: | ---: | ---: |
| 0 | Base | 1 | 0 |
| 1 | 2 | 2 | 1 |
| 2 | 4 | 8 | 3 |
| 3 | 8 | 64 | 6 |
| 4 | 16 | 1024 | 10 |

The fourth expression is exactly $(\sqrt2)^{n^2+n}=2^{(n^2+n)/2}$. For option 3, dividing its candidate by the exact result gives $2^{(n^2-n)/2}\to\infty$, so it is not a tight class. Option 2 has logarithm $n+\log_2\log n$, which is negligible beside the quadratic exact logarithm. Option 1 has logarithm $2n\log_2 n$; since $(\log n)/n\to0$, it too is much smaller than the true value.

The tempting replacement $2^{n(n+1)/2}\in\Theta(2^{n^2})$ is false. The exponent itself has quadratic order, but exponentiation amplifies a constant-factor difference in that exponent into an unbounded ratio. Writing $T=2^{\Theta(n^2)}$ is a valid broad family description; it does not select the tighter fourth expression automatically.

## Q5

**Correct option: 2.** Work on $n\ge2$, where the fixed-base logarithm is positive. Normalize by the proposed leading term:

$$\frac{n\log n+n^{3/4}}{n\log n}=1+\frac{1}{n^{1/4}\log n}\to1.$$

For sufficiently large $n$, the ratio lies, for example, between one and two. These are actual lower and upper constant witnesses, proving $f\in\Theta(n\log n)$. Also $\log n=O(n)$ and $n^{3/4}\le n^2$, so $f\in O(n^2)$. That second statement is deliberately loose.

Option 1 fails because $f/n=\log n+n^{-1/4}\to\infty$, refuting the upper half of $\Theta(n)$. Option 3 fails because the first displayed ratio tends to one rather than zero. Option 4 fails because $f/n^2=(\log n)/n+n^{-5/4}\to0$, refuting $\Omega(n^2)$. Thus a true larger upper bound and a correct smaller tight class can coexist without contradiction.

The lower-order summand remains positive at every finite $n$; discarding it means classifying growth, not claiming equality. If a question asked the exact value or a finite crossover, retain it. If the exponent $3/4$ were replaced by an input-dependent exponent, its comparison would require a fresh argument.

## Q6

**Correct option: 3.** Divide the exponentials before comparing them:

$$\frac{f(n)}{g(n)}=\frac{2^{n^2+n}}{2^{n^2}}=2^n,\qquad\frac{g(n)}{f(n)}=2^{-n}\to0.$$

The latter ratio proves $g\in o(f)$ directly. For every $\varepsilon>0$, choose an integer threshold exceeding $\log_2(1/\varepsilon)$; all later ratios are below $\varepsilon$. Conversely, for every proposed upper constant $c$, an integer $n>\log_2 c$ makes $f(n)>cg(n)$. Therefore $f\notin O(g)$ and cannot be in $\Theta(g)$.

Option 2 reverses the strict relation. Option 4 replaces an exponential quotient by the exponent difference; subtraction produces $n$ *inside* the power of two, not as the final ratio. At $n=3$, the ratio is eight, already illustrating that distinction.

Both logarithms have quadratic order: $\log_2f=n^2+n$ and $\log_2g=n^2$. They are even asymptotically equivalent, yet the original functions are not tightly equivalent. The correct exact criterion for fixed base $a>1$ is that $a^{u(n)}/a^{v(n)}=a^{u(n)-v(n)}$ stay bounded above and below by fixed positive constants. This is equivalent to a bounded exponent difference, not merely $u\in\Theta(v)$.

## Q7

**Correct option: 3.** For every positive integer, $n\le f(n)\le n^2$, giving the declared $\Omega(n)$ and $O(n^2)$ bounds with constant one and threshold one. Tightness requires a second inequality on *all* sufficiently large integers.

| Subsequence | $f(n)/n$ | $f(n)/n^2$ | Consequence |
| --- | --- | --- | --- |
| Even $n=2k$ | 1 | $1/(2k)$ | No positive eventual quadratic lower constant |
| Odd $n=2k+1$ | $2k+1$ | 1 | No finite eventual linear upper constant |

To refute $O(n)$, let any $c>0$ and threshold $N$ be proposed. Choose an odd integer $n>\max(c,N)$. Then $f(n)=n^2>cn$. To refute $\Omega(n^2)$, choose an even $n>\max(1/c,N)$. Then $f(n)=n<cn^2$. These constructions defeat arbitrary proposed witnesses, rather than a few numerical samples.

Option 1 therefore fails its upper half; option 2 fails its lower half; option 4 contradicts the explicit valid quadratic upper bound. The two subsequences are both unbounded, so neither can be omitted as a finite exception. Also do not infer $f\in o(n^2)$: its normalized ratio remains one on odd sizes. An absent tight class does not automatically produce a strict growth relation.

## Q8

**Correct option: 3.** Directly assigning linear order to each large term would ignore their subtraction. Multiply numerator and denominator by the conjugate:

$$\sqrt{n^2+n}-n=\frac{(n^2+n)-n^2}{\sqrt{n^2+n}+n}=\frac{1}{\sqrt{1+1/n}+1}.$$

For $n\ge1$, $1\le1+1/n\le2$, so

$$\frac1{\sqrt2+1}\le f(n)<\frac12.$$

These positive constants establish a tight constant order immediately. The denominator tends to two, giving the sharper limit $f(n)\to1/2$; it is not exactly one half for any finite positive $n$.

Option 1 predicts unbounded linear growth, option 2 unbounded square-root growth, and option 4 decay to zero. Each contradicts the explicit positive constant sandwich. For another check, at $n=1$ the value is $\sqrt2-1$, and rationalizing yields the same lower-end value $1/(\sqrt2+1)$.

More generally, for fixed $a>0$, $\sqrt{n^2+an}-n\to a/2$ by the same calculation. Changing the added term to one instead of $n$ gives $\sqrt{n^2+1}-n=1/(\sqrt{n^2+1}+n)\in\Theta(1/n)$. This pair explains precisely when option 4 would become appropriate: the numerator left after cancellation has changed.

## Q9

**Correct option: 3.** The exponent is not a fixed polynomial degree. For $n>1$, let $t=\log_2 n>0$. Then $n=2^t$ and

$$n^{1/\log_2 n}=(2^t)^{1/t}=2.$$

This is an exact identity, so the function has tight constant order. Equivalently, its natural logarithm is $(\ln n)/(\log_2 n)=\ln2$, confirming the same value without numerical approximation.

Options 1 and 2 describe functions growing without bound; option 4 describes a function tending to zero. None can be tightly equivalent to the constant two. At $n=2,4,16$, the powers are respectively $2^1$, $4^{1/2}$ and $16^{1/4}$, all two. These examples check the grouping, while the algebra proves the identity for the entire domain.

At $n=1$, the exponent contains division by zero; the original domain correctly excludes it. For any fixed logarithm base $b>1$, the corresponding expression is exactly $b$. If the base varies with $n$, so does that result: a variable-base expression cannot be classified using fixed-base shorthand. A useful related identity is $n^{c/\log_b n}=b^c$ for fixed $c$ and admissible $n$.

## Q10

**Correct option: 1.** The declared expression retains two independent nonnegative contributions. Under a uniform bound on admissible pairs, constants cannot depend on either growing input parameter. The original lesson uses a joint-tail convention: both $m$ and $n$ exceed independently chosen fixed thresholds. The following counterexamples grow *both* parameters, so they also work under that stricter convention.

For option 2, take $m=n^2$. Then

$$\frac{T(m,n)}{n\log n}=n+\frac1{\log n}\to\infty.$$

Thus no uniform upper constant for that class exists. For option 4, use $m=\lfloor\sqrt n\rfloor$. Its ratio is $T/(m\log n)=1+n/(m\log n)$, which diverges because $\sqrt n/\log n\to\infty$. The omitted additive $n$ term can dominate even though both parameters tend to infinity.

Option 3 is a valid broad upper bound: for base-two logarithms and $m,n\ge2$, $m\log_2 n+n\le mn+mn/2$. But along $m=n$, the ratio to $mn$ is $(\log n+1)/n\to0$, refuting the matching lower bound and hence the proposed $\Theta(mn)$ class. Other fixed bases merely change constants.

Option 1 is tight by equality, with lower and upper witness one. It can equivalently be written $\Theta(\max(m\log n,n))$, since the sum of two nonnegative terms lies between their maximum and twice that maximum. A restriction such as $m=n$ would allow simplification to $\Theta(n\log n)$, but that relationship is absent from this question.

## Q11

**Correct option: 1.** Define $k=\lfloor\log_2 n\rfloor$. The defining floor interval gives $k\le\log_2 n<k+1$. Exponentiating the entire interval, using monotonicity, yields $2^k\le n<2^{k+1}$. Rearranging gives

$$n/2<2^k=f(n)\le n.$$

These are exact bounds for every positive integer, including $n=1$. In particular, $f\in\Theta(n)$ with witnesses one half and one. Equality at the upper endpoint holds precisely when $n$ is a power of two.

At $n=3$, $f=2$, refuting option 2's reversed lower bound and option 3's universal equality. At $n=2$, $f=2>\log_2 2=1$, refuting option 4. The strict lower bound cannot be replaced by equality at an integer: $n<2^{k+1}$ is strict throughout the corresponding floor interval.

The ratio has no limit. At $n=2^k$ it equals one; at $n=2^{k+1}-1$ it equals $2^k/(2^{k+1}-1)\to1/2$. A bounded oscillating ratio preserves tightness while defeating asymptotic equivalence to $n$. Compare $2^{\lceil\log_2n\rceil}$, whose analogous bounds are $n\le f(n)<2n$; that expression would match option 2.

## Q12

**Correct option: 2.** At least the last $\lceil n/2\rceil$ factorial factors are at least $n/2$. For $n\ge2$,

$$n!\ge(n/2)^{n/2},\qquad\frac{n!}{2^n}\ge\left(\frac n8\right)^{n/2}\to\infty.$$

For example, once $n\ge16$, the displayed lower bound is at least $2^{n/2}$ and hence unbounded. Its reciprocal tends to zero, proving $2^n\in o(n!)$ and disproving option 1's proposed factorial upper bound.

Option 3 is also false. In $n!/n^n=\prod_{j=1}^n(j/n)$, the first $\lfloor n/2\rfloor$ factors are at most one half and the others at most one. Therefore the ratio is at most $2^{-\lfloor n/2\rfloor}\to0$. This disproves the required positive lower constant for $\Theta(n^n)$.

Finally, taking natural logarithms of elementary factorial bounds gives $\ln(n!)\le n\ln n$. For $n\ge4$, the lower bound is at least $(n/4)\ln n$, because $\ln(n/2)\ge(\ln n)/2$. Thus $\ln(n!)\in\Theta(n\ln n)$, not $\Theta(n)$, eliminating option 4. No appeal to a memorized Stirling approximation is needed for these order statements.

These proofs assume the compared exponential base is fixed. They extend to any constant base $B>1$ by replacing $n\ln2$ with $n\ln B$. They do not imply a factorial is tightly equivalent to a chosen exponential whose exponent merely has order $n\ln n$; tight equivalence still requires controlling the actual ratio.

## Q13

**Correct option: 3.** At $n=5$, the numerator is $3(25)+5(5)=100$ and the denominator is 25, giving exactly four. Termwise normalization gives the same result:

$$\frac{3n^2+5n}{n^2}=3+\frac5n,\qquad3+\frac55=4.$$

Option 4 gives the *limit* three instead of this finite value. Option 1 adds the coefficients as though the denominator changed $5n$ into five; option 2 retains multiplication by $n$ rather than dividing the lower-degree term by it.

For the additional bound analysis, on all $n\ge1$, $3n^2\le F(n)\le8n^2$. Thus valid tight witnesses are $c_1=3,c_2=8,N=1$. If the requested upper constant is a prescribed $c>3$, it works once $n\ge5/(c-3)$. For $c=3$, no finite threshold works because $5/n>0$ everywhere. The infimum possible upper constant is therefore three, but that infimum is not an attained upper witness. This distinguishes the exact finite calculation, an eventual tight class, and optimal witness constants.

## Q14

**Correct option: 2.** Here $F(8)=3(64)+5(8)=232$. Dividing by 64 and reducing gives $232/64=29/8$. The normalized identity is $3+5/8=29/8$, not the limiting value three.

| Candidate operation | Result at eight | Mathematical error |
| --- | --- | --- |
| Correct termwise division | $29/8$ | None |
| Discard the positive lower-order term | 3 | Replaces exact arithmetic by a limit |
| Add coefficients | 8 | Forgets the factor $1/n$ |
| Multiply the remaining coefficient by $n$ | 43 | Reverses the exponent subtraction |

To quantify the approximation, the normalized error relative to three is exactly $5/n$. Making it at most $1/10$ requires $n\ge50$, so eight is far below that threshold. Nevertheless the tight class is already established by the global sandwich $3n^2\le F\le8n^2$. A finite example can have a noticeable relative correction without contradicting an eventual theorem.

## Q15

**Correct option: 1.** For every positive integer, distribute division over the sum and subtract exponents:

$$\frac{F(n)}{n^2}=\frac{3n^2}{n^2}+\frac{5n}{n^2}=3+5n^{1-2}=3+\frac5n.$$

The alternative three omits a positive term; eight is correct only at $n=1$, not throughout the domain; $3+5n$ treats the second term as though the denominator had no effect. The symbolic answer must be valid at arbitrary $n$, rather than match a favorable exceptional case.

Its limit is three, so $F\in\Theta(n^2)$. More precisely, $F/(3n^2)=1+5/(3n)\to1$, proving equivalence to $3n^2$, not to $n^2$. For any $\varepsilon>0$, the condition $n>5/\varepsilon$ makes $|F/n^2-3|<\varepsilon$. This explicit threshold proves convergence and illustrates the order of quantifiers: the threshold may depend on the requested error, while a tight witness must not change with the subsequently varying input.

## Q16

**Correct option: 4.** The finite ratio is $3+5/n$, while its limit is three. Their difference $5/n$ remains strictly positive at every finite positive size. Option 1 therefore confuses a vanishing limit with pointwise equality.

Option 2 is false because a finite positive limit supplies *both* bounds. If $F/n^2\to3$, choose error $3/2$ in the definition of convergence. Beyond its threshold, $3/2<F/n^2<9/2$, giving positive lower and finite upper witnesses. Our particular polynomial admits even simpler global witnesses three and eight.

Option 3 is refuted by the nonzero function $f(n)=n$ compared with $g(n)=n^2$. Its ratio $1/n\to0$, yet $f$ is never zero. A zero ratio limit establishes $f\in o(g)$ under eventual positivity, rather than an identity for $f$.

The lesson transfers to numerical error estimates: an approximation whose relative error vanishes can still differ at every input. State separately whether a question requests the exact ratio, its limit, tight growth or asymptotic equivalence. Those four answers can be related without being interchangeable.

## Q17

**Correct option: 4.** The two powers are $3^5=243$ and $2^5=32$. Thus $F(5)=275$ and $F(5)/3^5=275/243$. General normalization yields

$$\frac{3^n+2^n}{3^n}=1+\left(\frac23\right)^n.$$

Option 1 retains only the smaller summand's ratio. Option 2 replaces that ratio by one as though the two bases agreed. Option 3 divides by the wrong exponential, producing $1+(3/2)^5=275/32$. Orientation of the denominator determines whether the residual factor decays or grows.

For the growth proof, $0<(2/3)^n\le1$, so $3^n\le F(n)\le2\cdot3^n$ on $n\ge0$. The residual geometric sequence tends to zero, proving $F/3^n\to1$. A prescribed relative excess $\varepsilon\in(0,1)$ is reached once $n\ge\ln(1/\varepsilon)/\ln(3/2)$ for a nonstrict error target. At five, the excess is the exact fraction $32/243$, rather than zero.

## Q18

**Correct option: 3.** Compute $3^8=6561$, $2^8=256$ and their sum $6817$. The exact requested quotient is $6817/6561=1+256/6561$.

The fourth option omits the leading one and gives only the relative contribution of the smaller term. The first option two would be appropriate for two identical copies of $3^8$, not for this input. The second option $6817/256$ normalizes by $2^8$; it grows with $n$, whereas the requested ratio approaches one.

The residual at eight is smaller than at five by the exact factor $(2/3)^3=8/27$. This is geometric convergence, rather than a reciprocal polynomial correction. For a one-percent target, solving $(2/3)^n\le1/100$ gives $n\ge\ln100/\ln(3/2)$, so the first integer that qualifies is 12. Finite arithmetic therefore reveals how far a specific input is from the asymptotic approximation. It does not change the established bound $F\in\Theta(3^n)$.

## Q19

**Correct option: 2.** Distribute the denominator, then combine equal exponents into a quotient of bases:

$$F(n)/3^n=3^n/3^n+2^n/3^n=1+(2/3)^n.$$

This identity holds throughout the positive-integer domain. Option 1 reverses the quotient; option 3 omits the first summand; option 4 freezes a changing ratio at two. At $n=1$, the true value is $5/3$, immediately separating all four alternatives.

The normalized residual converges to zero because its fixed base lies strictly between zero and one. Thus $F\sim3^n$. Dividing instead by $2^n$ gives $1+(3/2)^n\to\infty$, proving $F\notin O(2^n)$. The same sum therefore has a tight relation to its larger exponential and a strict growth advantage over its smaller one.

For fixed $a>b>1$, the general calculation is $(a^n+b^n)/a^n=1+(b/a)^n$. If the bases change with input, the residual need not vanish: taking $b_n/a_n=1-1/n$ produces a residual tending to $e^{-1}$ rather than zero. The fixed-base premise is substantive.

## Q20

**Correct option: 1.** For fixed $a>b>1$, $a^n/b^n=(a/b)^n\to\infty$. No fixed upper constant can tightly equate those exponentials. To defeat any proposed constant $c$, choose $n>\ln c/\ln(a/b)$, in addition to any prescribed tail threshold.

Option 2 confuses fixed constants *outside* exponentials with different constants *inside* their bases. Option 3 is false because adding a positive term cannot reduce a value: $a^n+b^n\ge a^n$. Also it is at most $2a^n$, establishing both sides directly. Option 4 reverses the quotient that arises when dividing by the larger summand.

For this question, $F/3^n=1+(2/3)^n\to1$, while $3^n/2^n=(3/2)^n\to\infty$. Changing the logarithm base in $\log n$ introduces a fixed multiplicative factor; changing the exponential base in $a^n$ generally introduces an input-dependent multiplicative ratio. These algebraic operations look superficially similar but have different consequences for tightness.

## Q21

**Correct option: 1.** Preserve the nested parentheses. At $n=5$, $N=2^{2^5}=2^{32}$, so $\log_2N=32$ and then $\log_2(\log_2N)=\log_2 32=5$.

The first logarithm removes the outer power of two; it does not remove both exponentials at once. Option 2 gives the intermediate value 32. Option 3 gives $n^2=25$, which is not either logarithmic step. Option 4 gives six, the bit length of the intermediate integer 32, rather than its logarithm five.

For comparison, the *square* of the first logarithm is $(\log_2N)^2=32^2=1024$. It is not 25, five or 32. This explicitly checks the meaning of iterating an operation versus raising its output to a power.

The general identity is $\log_2(\log_2(2^{2^n}))=n$, valid for all real $n$ for which the displayed positive logarithms are interpreted, including the question's positive integers. No enormous integer needs to be materialized: symbolic exponent cancellation computes the answer exactly. This computational convenience does not make writing all bits of $N$ cheap.

## Q22

**Correct option: 4.** At eight, $N=2^{256}$. The first base-two logarithm returns 256 and the second returns eight. Both are exact, even though a decimal expansion of $N$ would be inconvenient.

| Quantity | Value |
| --- | ---: |
| Exponent of outer power | 256 |
| $\log_2N$ | 256 |
| $\log_2(\log_2N)$ | 8 |
| Binary bit length of $\log_2N$ | 9 |
| $n^2$ | 64 |

Options 1, 3 and 2 therefore correspond respectively to stopping early, counting binary digits rather than a logarithm, and squaring the index. Notice that the bit length of $N$ itself is 257, not any listed answer. Each operation has a distinct input and output.

For a size threshold $M=2^{2^h}$, its double logarithm measures the nested exponent index $h$. Replacing a logarithm by a bit length introduces rounding and a plus-one boundary at powers of two. Those corrections can be negligible for growth while still deciding an exact multiple-choice answer.

## Q23

**Correct option: 3.** Apply the outer logarithm first to its actual argument:

$$\log_2 N=2^n,\qquad\log_2(\log_2N)=\log_2(2^n)=n.$$

Option 4 is the intermediate value. Option 1 squares $n$ without any operation in the definition permitting it. Option 2 adds a digit-count correction that belongs to a different question. Checking $n=3$ gives $N=256$, then logarithms eight and three; the general identity follows from the exponential-logarithm inverse law, not from the example.

For fixed bases $a,b>1$, applying $\log_b$ twice to $a^{a^n}$ yields $n\log_b a+\log_b(\log_b a)$. The exact constants depend on the bases, even though the resulting function has linear order in $n$. In the present base-two expression those constants reduce to one and zero. Fixed-base growth equivalence therefore does not authorize replacing bases in an exact arithmetic calculation.

## Q24

**Correct option: 2.** Composition and exponentiation are different operations. Set $x=\log_2N=2^n$. The iterated logarithm is $\log_2x=n$, whereas the squared logarithm is $x^2=2^{2n}$. At $n=2$, those outputs are two and sixteen, respectively.

Option 1 treats the intermediate $2^n$ as though it already equaled $n$. Option 3 confuses applying a function twice with multiplying its first result by itself. Option 4 misuses change of base: for fixed $b>1$, $\log_bN=(\log_2N)/(\log_2b)$, but that constant factor does not equate polynomial and exponential functions of $n$.

A useful grouping check is to rewrite nested notation with explicit parentheses before simplifying: $\log_2(\log_2N)$ and $(\log_2N)^2$ cannot be transformed into one another by a logarithm rule. Likewise $\log_2(N^2)=2\log_2N$ is a third expression. The location of the square determines which identity applies.

## Q25

**Correct option: 2.** Use denominator 60 for all five reciprocals:

$$H_5=1+\frac12+\frac13+\frac14+\frac15=\frac{60+30+20+15+12}{60}=\frac{137}{60}.$$

Option 3, five, would count five unit terms. Option 4, one fifth, retains only the last term. Option 1, three, comes from $(n+1)/2$ at five and is an arithmetic-average-style expression for a different sequence. Reciprocals are unequal and cannot be summed as consecutive integers.

For growth, the decreasing positive function $1/x$ gives $\ln(n+1)\le H_n\le1+\ln n$. At five this places the exact rational answer between $\ln6$ and $1+\ln5$. The bounds explain the logarithmic class without claiming an exact logarithm. The increment $H_{n+1}-H_n=1/(n+1)$ is positive but decreasing: the sum grows forever while its marginal addition shrinks.

This separates three requests: the exact partial sum is $137/60$, its growth is $\Theta(\ln n)$, and its normalized ratio $H_n/\ln n$ tends to one. None makes the finite sum equal to a logarithm.

## Q26

**Correct option: 1.** Continue from $H_5=137/60$, rather than restart with rounded decimals:

$$H_8=\frac{137}{60}+\frac16+\frac17+\frac18=\frac{1918+140+120+105}{840}=\frac{761}{280}.$$

The numerator 2283 is divisible by three, giving the reduced fraction. Option 2 counts eight unit contributions; option 3 retains only the last reciprocal; option 4 equals $(8+1)/2$ and is unrelated to the reciprocal sum. The correct value is strictly greater than $H_5$ but increases by less than $3/6=1/2$, because the three added terms are at most one sixth. The exact difference is $73/168$.

Integral bounds provide a second independent check: $\ln9\le H_8\le1+\ln8$. They are bounds, not substitute option values. To understand unbounded growth, group terms from $2^{j-1}+1$ through $2^j$. Each group has $2^{j-1}$ terms, each at least $1/2^j$, so each group contributes at least one half. Infinitely many such groups force divergence, while their logarithmic number up to $n$ explains the slow rate.

## Q27

**Correct option: 4.** The exact sum has no replacement by any of the first three elementary expressions. Its defining recurrence is $H_0=0$ and $H_n=H_{n-1}+1/n$ for $n\ge1$. Expanding this recurrence produces precisely $\sum_{k=1}^n1/k$.

The apparent agreement of several alternatives at $n=1$ is accidental. At $n=2$, the correct value is $3/2$; $n$ and $1/n$ already fail. At $n=3$, $H_3=11/6$, whereas $(n+1)/2=2$, eliminating the remaining competitor. A universally quantified symbolic identity must survive these inputs.

The integral comparison is derived from monotonicity: on $[k,k+1]$, $1/x\le1/k$, giving $\int_1^{n+1}1/x\,dx\le H_n$. On $[k-1,k]$ for $k\ge2$, $1/x\ge1/k$, giving $H_n-1\le\int_1^n1/x\,dx$. Hence $\ln(n+1)\le H_n\le1+\ln n$ and $H_n\in\Theta(\ln n)$. These inequalities support approximation and classification, while the displayed sum remains the exact answer.

## Q28

**Correct option: 3.** For $n>1$, the integral sandwich yields

$$\frac{\ln(n+1)}{\ln n}\le\frac{H_n}{\ln n}\le1+\frac1{\ln n}.$$

Both envelopes tend to one, so $H_n\sim\ln n$. Asymptotic equivalence means vanishing *relative* discrepancy, rather than finite equality. At $n=1$, $H_1=1$ while $\ln1=0$ already disproves any universal identity; a tail claim remains meaningful after excluding that endpoint.

Option 1 fails because $1/k$ decreases strictly as $k$ increases. Option 2 fails because the harmonic sum diverges yet $H_n/n\to0$, so it is not tightly linear. Option 4 confuses the ratio limit with pointwise equality. A divergent function can be much slower than a linear one.

For another useful contrast, a bounded additive error is enough here for relative equivalence because $\ln n\to\infty$: $0<H_n-\ln n\le1$. A bounded error added to a function tending to zero or staying constant would not automatically become relatively negligible. State what grows before dividing an error term by it.

## Q29

**Correct option: 4.** At $n=5$, $N=25$ and $\sqrt N=5$. The requested quantity is $(25-5)/25=20/25=4/5$. Algebraically, positivity of $n$ allows $\sqrt{n^2}=n$, giving $1-1/n$.

The first option changes subtraction into addition, producing $6/5$. The second divides the numerator by $n$ rather than $N=n^2$, producing four. The third keeps only the removed term's relative size $1/5$, rather than the amount remaining. The answer is less than one because a positive quantity was subtracted, and greater than zero because $n>1$; this sign and magnitude check already rules out two alternatives.

For all $n\ge2$, $n^2/2\le n^2-n<n^2$, so the unnormalized difference has tight quadratic order. Its normalized relative deficit is exactly $1/n$. The numerical subtraction does not cancel the quadratic leading term. In contrast, $(n^2+n)-n^2=n$ would cancel it and have linear order. Identify which power actually survives before applying a dominant-term rule.

## Q30

**Correct option: 3.** At eight, $N=64$, $\sqrt N=8$ and the difference is 56. Dividing by the prescribed denominator 64 gives $56/64=7/8$.

Option 1, seven, omits one factor of eight in the denominator. Option 2, one eighth, computes the removed fraction rather than the retained fraction. Option 4 changes the sign, giving one plus the removed fraction. Both the exact arithmetic and the general identity $1-1/n$ determine the selected option.

The retained fraction exceeds the value at five by $7/8-4/5=3/40$. More generally its increment from $n$ to $n+1$ is $1/n-1/(n+1)=1/(n(n+1))>0$, so it rises monotonically toward one. To retain at least 99 percent of $N$, solve $1-1/n\ge99/100$, obtaining $n\ge100$. This is a finite threshold calculation; the tight quadratic order alone would not supply that number.

## Q31

**Correct option: 2.** The domain is positive integers. On that domain,

$$\frac{N-\sqrt N}{N}=\frac{n^2-n}{n^2}=1-\frac1n.$$

If $n$ were negative, $\sqrt{n^2}=|n|$ rather than $n$; if it were zero, division by $N$ would be undefined. The stated domain makes both simplifications valid.

The first option is the removed fraction, the third has the wrong sign, and the fourth leaves the denominator only partially applied. At one the true expression is zero; at two it is one half. An alternative can coincide at a boundary without becoming a universal identity, so both checks are useful.

The numerator is nonnegative on $n\ge1$ and positive on $n\ge2$. Since the ratio tends to one, $n^2-n$ is asymptotically equivalent to $n^2$ and hence tightly quadratic. The zero at one does not defeat an eventual lower bound, whose threshold may be two. This is why eventual positivity is sufficient for the runtime convention while division still requires checking the exact denominator at every requested input.

## Q32

**Correct option: 1.** The explicit identity is $n^2-n=n^2(1-1/n)$. For $n\ge2$, its multiplier lies between one half and one, giving $n^2/2\le n^2-n\le n^2$. Thus subtracting this particular lower-order term preserves a tight quadratic bound after proving positivity and a quantitative lower envelope.

Option 2 asserts that no subtraction can preserve a lower bound; the displayed sandwich refutes it. Option 3 asserts the opposite unsafe generalization: $(n^2+n)-n^2=n$ shows that cancelling the leading term changes the order. Option 4 permits a negative expression as a nonnegative runtime without stating another convention; for example, $n-n^2$ is eventually negative and fails that model.

A general version is useful. If $g>0$ eventually and $|h|/g\to0$, choose a threshold making $|h|\le g/2$. Then $g/2\le g+h\le3g/2$, proving tight equivalence in order even when $h$ is signed. This establishes a valid subtraction rule under explicit small-error assumptions, rather than attempting to subtract two unspecified $\Theta$ classes.

## Q33

**Correct option: 4.** At five, the numerator is $125+25=150$, so the quotient is $150/125=6/5$. The general cancellation of powers is

$$\frac{n^3+n^2}{n^3}=1+n^{2-3}=1+\frac1n.$$

Option 1 uses an exponent difference of negative two instead of negative one. Option 2 replaces the changing lower-order term by another full copy of the leading term. Option 3 divides by $n^2$ rather than $n^3$. The exact denominator is part of the mathematical task.

For all $n\ge1$, $n^3\le n^3+n^2\le2n^3$. The upper and lower constants one and two prove cubic tightness without a limit. The limit of the normalized ratio is one, which proves the sharper equivalence to $n^3$. Its positive error is exactly $1/n$, so a required error at most $\varepsilon>0$ means $n\ge1/\varepsilon$. Finite correction and eventual equivalence are both derived from the same identity but answer different questions.

## Q34

**Correct option: 3.** At eight, $n^3=512$ and $n^2=64$, so $(512+64)/512=576/512=9/8$. The alternative $65/64$ would come from the different residual $1/n^2$. Nine omits a factor of eight from the normalization; two assumes both summands have equal magnitude.

The normalized error falls from $1/5$ at five to $1/8$ at eight. This is reciprocal convergence: each increment in $n$ reduces the error by $1/(n(n+1))$. It is slower than the geometric residual $(2/3)^n$ in Questions 17–20 for sufficiently large sizes.

An upper constant $c$ for the unnormalized cubic expression must satisfy $1+1/n\le c$ eventually. Every $c>1$ works beyond $n\ge1/(c-1)$; $c=1$ never works at a finite input. Conversely, the exact lower constant one works globally. Tightness and equivalence can thus coexist with an unattained infimum of upper witness constants.

## Q35

**Correct option: 2.** The identity $n^3/n^3+n^2/n^3=1+1/n$ holds for every positive integer. Option 1 would be the result after normalizing by $n^2$; option 3 uses the wrong exponent difference; option 4 gives the value at one but is not constant across the domain.

The fixed two-term nonnegative sum satisfies

$$\max(n^3,n^2)\le n^3+n^2\le2\max(n^3,n^2).$$

Since $n^3\ge n^2$ on the domain, this becomes the cubic sandwich. Notice the proof uses an actual maximum, not a vague largest-term slogan, and supplies both required inequalities.

For a growing number of summands this constant changes. The sum of $n$ copies of $n^3$ is $n^4$, while the maximum individual term remains $n^3$. For signed terms the lower inequality can fail through cancellation. The present exact identity is safe because there are two positive terms, their normalization is defined, and no varying summand count or sign change is hidden.

## Q36

**Correct option: 1.** If a fixed number $r$ of summands are nonnegative, their pointwise maximum $M$ satisfies $M\le\sum_{i=1}^r f_i\le rM$. Because $r$ does not vary with input, these are valid fixed lower and upper witnesses. For the question, $r=2$ and $M=n^3$.

Option 2 is refuted by $n^3+(-n^3)=0$: cancellation destroys a positive lower envelope. Option 3 is refuted by $\sum_{i=1}^n1=n$, whose maximum summand is one. Option 4 is refuted by $1\in O(n)$ but $1\notin\Omega(n)$; an upper bound alone does not give tightness.

The fixed-count hypothesis makes the general maximum rule valid, but it is a sufficient general condition rather than a claim that every growing-count sum must fail to match its maximum. A convergent geometric tail can have a bounded sum-to-maximum ratio despite increasing term count. What must be proved in any particular application is a uniform constant-factor sandwich. This distinction prevents overextending either the rule or its counterexample.

## Q37

**Correct option: 2.** Substitute the entire argument $k=2n$, not only its sign factor. At $n=5$, $k=10$ is even, so $(-1)^{10}=1$ and $F(10)=10(2+1)=30$.

Option 3, ten, uses the odd multiplier one. Option 4, fifteen, applies the even multiplier to $n$ instead of $2n$. Option 1, twenty, omits the alternating term and keeps only the central multiplier two.

The two parity classes are explicit:

| Argument | Multiplier | Function value | Ratio to argument |
| --- | ---: | ---: | ---: |
| $k=2n$ | 3 | $6n$ | 3 |
| $k=2n+1$ | 1 | $2n+1$ | 1 |

Both classes satisfy $k\le F(k)\le3k$, proving tight linear order for all positive arguments. Their ratios have different subsequential limits, so $F(k)/k$ has no unique limit. Calculating a single even input establishes its exact value; the parity analysis is needed to establish the global relation.

## Q38

**Correct option: 1.** With $n=8$, the substituted argument is 16. Its sign factor is positive one, so $F(16)=16\cdot3=48$.

The second option, sixteen, selects the odd-argument multiplier. The third option, twenty-four, uses the correct multiplier but the wrong argument. The fourth option, thirty-two, ignores the alternating contribution. Each mistake changes a separate part of the substitution.

Compare neighboring arguments: $F(15)=15$, $F(16)=48$ and $F(17)=17$. This sequence is not monotone, although every value lies between its argument and three times its argument. Thus nonmonotonicity does not defeat tight growth, and a dramatic finite jump need not change the class.

No constant $c>0$ makes $F(k)\sim ck$ on all integers: its normalized ratio would alternate between $1/c$ and $3/c$, which cannot both tend to one. The exact even-subsequence relation $F(2n)=6n$ is stronger on that restricted domain and does not extend unchanged to odd arguments.

## Q39

**Correct option: 4.** For every positive integer $n$, the substituted argument $2n$ is even. Therefore

$$F(2n)=2n(2+(-1)^{2n})=2n(2+1)=6n.$$

The alternative $2n$ uses the wrong parity multiplier; $3n$ drops the factor two in the argument; $4n$ drops the sign term. The parity decision and the outer argument must both be substituted consistently.

The identity gives an exact linear formula on the even subsequence, not merely a tight class. On all positive arguments, however, $F(k)=k$ for odd $k$ and $3k$ for even $k$. The witnesses one and three prove $\Theta(k)$ globally while the ratio's two distinct subsequential limits rule out equivalence to a single constant multiple.

If one instead defined a sign term $(-1)^n$ while still multiplying by $2n$, the result would alternate between $2n$ and $6n$. That is a different function: replacing the exponent $2n$ by $n$ cannot be justified by the fact that both functions happen to have linear growth.

## Q40

**Correct option: 3.** The multiplier $2+(-1)^k$ is either one or three, so $k\le F(k)\le3k$ for every positive integer. Those two fixed witnesses establish a tight linear bound.

The ratio is one on odd arguments and three on even arguments. If it had a limit, both unbounded subsequences would share that limit; they do not. A finite positive ratio limit is therefore sufficient for tightness but not necessary.

Option 1 is false because the multiplier never becomes negative. Option 2 improperly extends the even formula $F(2n)=6n$ to odd arguments; $F(2n+1)=2n+1$ is an explicit counterexample. Option 4 treats a sufficient limit test as an equivalent definition and is contradicted by the global sandwich.

Contrast Question 7, where the ratio to $n$ grows without bound on one subsequence, with this example's ratio confined to a fixed positive interval. The existence of oscillation is not the decisive feature. Its lower and upper envelopes determine whether a tight bound survives, whether a one-sided bound fails, or whether both fail.

## Q41

**Correct option: 3.** At five, $n!=120$. Neighboring powers satisfy $2^6=64<120\le128=2^7$. Hence seven is the smallest integer height satisfying the capacity inequality.

Option 4, six, is too small and corresponds to rounding the logarithm downward. Option 1, twenty-five, uses $n^2$ rather than the factorial's logarithm. Option 2, fifteen, uses $n\lceil\log_2n\rceil$; that expression may overestimate the needed capacity but is not its minimum.

The exact ceiling logarithm can be computed without floating point: for an integer $M\ge1$, the least $h\ge0$ with $2^h\ge M$ is the binary bit length of $M-1$. For $M=120$, 119 has seven bits. For $M=1$, the result is zero under the ordinary zero-bit-length convention for this helper.

This is an information-capacity lower bound for a binary decision tree distinguishing $n!$ outputs. It does not, by itself, produce an algorithm reaching that height with a particular restricted comparison set. Sufficient leaf count and realizable decision partitions are separate questions.

## Q42

**Correct option: 2.** Compute $8!=40320$. The neighboring capacities are $2^{15}=32768$ and $2^{16}=65536$, so the least permitted height is 16.

| Proposed height | Leaves available | Meets the threshold? |
| ---: | ---: | --- |
| 15 | 32768 | No |
| 16 | 65536 | Yes; the previous height fails |

The third option rounds downward. Twenty-four is $8\lceil\log_2 8\rceil$, which counts a different upper expression. Sixty-four is $8^2$, unrelated to minimal binary capacity. Larger values can satisfy the inequality without satisfying the question's word “smallest.”

The required number of unused leaves at height 16 is $65536-40320=25216$. Not every leaf needs to correspond to an admissible output: the capacity inequality is an upper limit on available leaves, not an equality requirement. Conversely, having that many leaves does not prove a legal comparison tree can use them in the necessary balanced manner. The exact arithmetic determines only the information bound requested here.

## Q43

**Correct option: 1.** A nonnegative integer height is admissible exactly when $2^h\ge n!$. Monotonicity of the logarithm gives $h\ge\log_2(n!)$, so the least such integer is

$$h=\lceil\log_2(n!)\rceil.$$

The floor fails whenever $n!$ is not a power of two. For instance, $3!=6$ requires height three, while the floor is two. Option 3, $n^2$, and option 4, $n\lceil\log_2n\rceil$, are not the least height; a bound exceeding a threshold does not automatically minimize it.

At $n=1$, the answer is zero because one output requires no binary decision; at $n=2$, the answer is one. For all $n\ge4$, elementary factorial bounds place its logarithm between $(n/4)\log_2 n$ and $n\log_2 n$. The ceiling adds less than one, preserving $h\in\Theta(n\log n)$.

If each decision had up to $r>1$ outcomes, the corresponding capacity bound would be $\lceil\log_r(n!)\rceil$. This substitution requires the *effective* branch count of the permitted observation, rather than the surface syntax of the comparison operation.

## Q44

**Correct option: 4.** The logarithm measures representation scale, not the original quantity. We have $\log_2(n!)\in\Theta(n\log n)$ while $n!$ grows faster than every fixed-base exponential. A polynomially bounded logarithm therefore does not make enumerating $n!$ objects polynomial.

Option 1 is disproved by $f(n)=2^n$: its logarithm is linear although the original value is exponential. Option 2 fails already at $3!=6$, where the floor height two has only four leaves. Option 3 confuses a small bit description of a count with the work required to materialize that many objects.

A related counterexample shows why even comparing two logarithms can be insufficient. The logarithms of $2^{n^2}$ and $2^{n^2+n}$ are asymptotically equivalent, but their original ratio is $2^n\to\infty$. Thus equal tight logarithmic classes do not imply equal original tight classes.

The safe inference is one-way: an exact logarithmic identity or a controlled exponent difference can be exponentiated. A statement giving only a broad order for logarithms loses the precision needed to bound original ratios. Retain that distinction when analyzing multiplicative recurrences or information capacities.

## Q45

**Correct option: 4.** Since $g(n)=n^2>0$, the relevant ratio is $R(n)=n^{\sin(\ln n)}$. Merely saying the sine oscillates would not prove the existence of suitable *integer* subsequences, so construct them explicitly.

Let $t_k=\pi/2+2\pi k$, $x_k=e^{t_k}$ and $n_k=\lfloor x_k\rfloor$. The relative rounding error tends to zero, giving $\ln n_k-t_k\to0$. Continuity of sine then gives $\sin(\ln n_k)\to1$. Beyond a fixed index it is at least one half, so $R(n_k)\ge\sqrt{n_k}\to\infty$. Any proposed eventual upper constant is exceeded along this integer subsequence.

Similarly, let $u_k=3\pi/2+2\pi k$ and $m_k=\lfloor e^{u_k}\rfloor$. Then $\ln m_k-u_k\to0$ and $\sin(\ln m_k)\to-1$. Eventually it is at most negative one half, giving $0<R(m_k)\le1/\sqrt{m_k}\to0$. Any proposed positive eventual lower constant fails on this second integer subsequence.

To justify the logarithmic rounding claim quantitatively, for $x>1$, $1-1/x\le\lfloor x\rfloor/x\le1$. Its logarithm is trapped between $\ln(1-1/x)$ and zero, both tending to zero. Thus discretization does not remove either construction.

The first subsequence refutes $O(g)$ and the second refutes $\Omega(g)$. Consequently options 1, 2 and 3 each assert a bound that fails. Although $n\le f(n)\le n^3$ globally, those wider envelopes do not make $f$ tightly quadratic. Also neither $f\in o(g)$ nor $f\in\omega(g)$ holds: each would require one uniform ratio limit rather than these incompatible subsequences.

## Q46

**Correct option: 1.** For $k=\lfloor\log_2n\rfloor$, the exact interval is $2^k\le n<2^{k+1}$. Hence $n/2<f(n)\le n$, establishing $\Theta(n)$ with fixed witnesses.

To test convergence, use two exact integer sequences. At $a_k=2^k$, $f(a_k)/a_k=1$. At $b_k=2^{k+1}-1$, $f(b_k)/b_k=2^k/(2^{k+1}-1)\to1/2$. Both arguments tend to infinity, but their ratios have different limits. Therefore no single ratio limit exists.

| Input position in a binary block | Example | Normalized ratio |
| --- | --- | --- |
| First integer | $n=8$ | $8/8=1$ |
| Interior integer | $n=12$ | $8/12=2/3$ |
| Last integer | $n=15$ | $8/15$ |
| First integer of next block | $n=16$ | $16/16=1$ |

Option 2 would require the ratio to tend to zero, impossible because it always exceeds one half. Option 3 would require divergence to infinity, impossible because the ratio never exceeds one. Option 4 contradicts the second subsequence.

The floor's effect is bounded in the exponent by less than one, so it changes the power of two by a bounded factor. It can preserve a tight class while destroying exact equality and asymptotic equivalence. That precise distinction is more informative than saying floors can always be ignored.
