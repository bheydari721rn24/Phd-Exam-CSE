## Ten solved transfer challenges

These are newly worded mathematical problems informed by the reviewed university material. They are not represented as additional authentic Iranian questions or as verbatim university assessment questions. Each recurrence has a declared domain and base. The questions combine symbolic classification with a complete proof or exact calculation.

### Challenge 1. Five quarter-size children and a linear toll

**Problem.** On $N=4^h$, define $T(1)=1$ and $T(N)=5T(N/4)+2N$. Find an exact expression, its tight order, the number of depth-four descendants and the first input depth with descendant size $N/1024$.

**Solution.** At depth $j$ there are $5^j$ nodes of size $N/4^j$, so the combined toll is $2N(5/4)^j$. The leaves cost $5^h$. Summing the finite geometric progression gives

$$T(4^h)=5^h+2\cdot4^h\frac{(5/4)^h-1}{1/4}=9\cdot5^h-8\cdot4^h.$$

The seed at $h=0$ is one. At $h=1$, the original recurrence gives $5+8=13$, matching $45-32$. The critical exponent is $\log_45>1$, so the tight order is $\Theta(N^{\log_45})$. Depth four contains $5^4=625$ descendants, provided the root is large enough to reach that depth. Dividing size by 1024 requires five quartering steps, since $4^5=1024$; branch multiplicity five does not determine size reduction. At $h=5$, the exact total is 19933. The model keeps the terminal contribution separate from the increasing internal level costs. This is an exact variant of the Stanford concept check, with a specified seed added by the author.

### Challenge 2. A critical fourth-root exponent

**Problem.** For $N=81^h$, define $T(1)=1$ and $T(N)=3T(N/81)+10N^{1/4}$. Obtain the exact total and classify it.

**Solution.** Because $81^{1/4}=3$, the branching exponent is $p=\log_{81}3=1/4$. At depth $j$, combined toll is $3^j10(N/81^j)^{1/4}=10N^{1/4}$. There are exactly $h$ internal depths, and the $3^h=N^{1/4}$ unit leaves contribute another $N^{1/4}$. Hence

$$T(81^h)=(10h+1)3^h.$$

For depth four, the value is $41\cdot81=3321$. Normalization also proves it: $U_h=T(81^h)/3^h$ satisfies $U_h=U_{h-1}+10$ with $U_0=1$. Restoring $h=\log_{81}N$ gives $\Theta(N^{1/4}\log N)$. Keeping $N^{1/4}$ without the depth factor would lose all but a constant number of equal-cost levels. Conversely, multiplying by the original input rather than $h$ would confuse the two variables. The model explicitly labels input, multiplicity, local toll, aggregate toll and leaf work. This is independently derived from the reviewed critical-case example.

### Challenge 3. Two logarithmic thresholds on the same tree

**Problem.** For $N=2^h$, stop at $N\le2$ with cost one. For larger inputs define $T_k(N)=2T_k(N/2)+N/(\log_2N)^k$. Compare $k=1$ and $k=2$, with exact normalized finite sums.

**Solution.** Write $V_h=T_k(2^h)/2^h$. The base is $V_1=1/2$. Dividing each step gives $V_h=V_{h-1}+1/h^k$, hence

$$T_k(2^h)=2^h\left(\frac12+\sum_{r=2}^{h}\frac1{r^k}\right).$$

For $k=1$, harmonic integral bounds give a normalized value of order $\log h$, so $T_1(N)\in\Theta(N\log\log N)$. For $k=2$, the normalized sum stays between $1/2$ and $3/2$, so $T_2(N)\in\Theta(N)$. The unit base supplies the strictly positive lower constant even when the toll sum converges. At $h=4$, the exact totals are $T_1(16)=76/3$ and $T_2(16)=133/9$; these are mathematical costs with rational tolls, not literal integer operation counts.

The threshold at $N=2$ prevents division by zero at $N=1$. A nonnegative-log-power-only Master theorem does not cover these tolls. The finite normalized sum directly proves them and explains why a reciprocal logarithm and its square have different outcomes. The animation plots the actual finite terms and partial sums for each scenario rather than using the same generic tree for both.

### Challenge 4. A regularity counterexample with positive polynomial tolls

**Problem.** On $N=2^h$, let $T(1)=1$ and $T(N)=2T(N/2)+f(N)$, where $f(N)=N^3$ at even $h$ and $f(N)=N^2$ at odd $h$. Determine the tight order and explain why a root-dominated Master conclusion fails.

**Solution.** The toll is always at most $N^3$. Its complete-tree upper sum is bounded by $N^3\sum_{j\ge0}4^{-j}$ plus $N$ unit leaf work, so $T(N)=O(N^3)$. At even $h$, the root supplies $N^3$. At odd $h\ge3$, its two children have even logarithmic depth and each contributes root toll $(N/2)^3$, totaling $N^3/4$. Therefore every sufficiently large grid input has a cubic lower bound and $T(N)\in\Theta(N^3)$.

Although $f(N)\ge N^2$ is polynomially above the critical leaf exponent one, regularity fails at odd depths:

$$\frac{2f(N/2)}{f(N)}=\frac{N}{4}.$$

No constant less than one bounds that ratio. At the same odd inputs, $T(N)/f(N)\ge N/4\to\infty$, refuting $T\in\Theta(f)$ for this toll. The exact sequence at depths zero through five is $1,6,76,216,4528,10080$. Every value includes both the appropriate current toll and twice the previous value. Polynomial dominance alone is insufficient for that version of the root case; the regularity condition serves a mathematical purpose.

### Challenge 5. Mixed child sizes with a quadratic toll

**Problem.** Consider the unperturbed real-size recurrence $T(x)=2T(x/2)+3T(x/3)+x^2$ above a fixed base threshold. Base costs are bounded and positive. Find its tight order using a complete induction envelope.

**Solution.** The root toll gives $T(x)\ge x^2$ at every nonbase input. For the upper bound, suppose smaller nonbase and base arguments satisfy $T(y)\le Cy^2$. A terminal interval must be chosen bounded away from zero for this envelope, or use an equivalent positive constant addition to the envelope at smaller inputs. Above a suitable fixed threshold the direct calculation is

$$T(x)\le C\left(2\frac{x^2}{4}+3\frac{x^2}{9}\right)+x^2=\left(\frac{5C}{6}+1\right)x^2.$$

Taking $C\ge6$ makes this at most $Cx^2$, and increasing $C$ covers every terminal argument reachable from a parent just above the threshold. A rigorous real-size induction can proceed on intervals whose width is fixed and whose children lie in earlier intervals; the threshold is enlarged if necessary. Thus $T(x)=O(x^2)$ and the root lower bound gives $\Theta(x^2)$.

The branching equation is $2(1/2)^p+3(1/3)^p=1$. Its left side is $5/6$ at $p=2$, so its unique solution lies below two; this corroborates the quadratic toll dominance. Replacing the expression by five equal children would be a different recurrence. The compact diagram displays two half-size and three third-size branches, together with their individual quadratic weights. The constant six follows from the slack $1-5/6$, not from the number of branches alone.

### Challenge 6. Exact merge work at thirteen elements

**Problem.** Balanced recursive merging stops at singleton arrays. Compute the size-toll total and the worst-case comparison total for thirteen elements; prove the general formulas.

**Solution.** With $L=\lfloor\log_2n\rfloor$, the first $L$ complete depths each have total active size $n$. At depth $L$, the balanced nodes have size one or two. There are $n-2^L$ size-two nodes and their size toll adds $2(n-2^L)$. Thus $A(n)=nL+2n-2^{L+1}$. The full binary tree has $n$ singleton leaves and $n-1$ internal nodes. Ordinary worst-case merging uses size minus one comparisons, so subtracting one at every internal node gives $C(n)=nL+n-2^{L+1}+1$.

For thirteen, $L=3$, and

$$A(13)=39+26-16=49,\qquad C(13)=49-12=37.$$

Direct recurrence checking gives $C(6)=11$, $C(7)=14$ and $C(13)=11+14+12=37$. For the size toll, $A(6)=16$, $A(7)=20$ and $A(13)=16+20+13=49$. The two totals share the same recursive partition but count different local operations. The animation reveals the actual rounded split tree and an exact depth ledger, including the incomplete final internal depth; it never labels thirteen as a power of two.

This is an independently specified recurrence calculation. An implementation's actual comparisons depend on its input order. The word worst case here includes the standard interleavings that make each merge perform the full size-minus-one count. A unit leaf cost would add thirteen to either zero-leaf model and must be stated separately.

### Challenge 7. A factorial multiplier with a nonzero toll

**Problem.** Let $T_0=1$ and $T_n=nT_{n-1}+n!$ for $n\ge1$. Derive an exact solution and decide whether $\Theta(n!)$ is a valid tight answer.

**Solution.** Divide by $n!$ and put $V_n=T_n/n!$. The coefficient cancels exactly: $nT_{n-1}/n!=T_{n-1}/(n-1)!$. Hence $V_n=V_{n-1}+1$, with $V_0=1$. It follows that

$$T_n=(n+1)n!.$$

For $n=5$, $T_5=6\cdot120=720$. Iteration gives $1,2,6,24,120,720$, matching the closed form at every shown index. Induction verifies $n[n(n-1)!]+n!=(n+1)n!$; the base is also correct. The order is $\Theta(n\,n!)$ for positive large $n$, not $\Theta(n!)$, because the quotient by $n!$ is $n+1\to\infty$.

The product normalizer is nonzero at every index, including $0!=1$, so division is justified. If a different problem introduced a zero multiplier, the normalizer would fail and the recurrence would need to restart at that index. Omitting the toll would yield just $n!$, demonstrating precisely where the extra factor arises. This example extends the first-order variable-coefficient normalization in the Princeton scope and keeps the exact finite sum rather than replacing it by a vague dominant multiplier.

### Challenge 8. Expected size and expected cost

**Problem.** A process on four elements chooses a pivot rank uniformly in $0,1,2,3$ and follows its larger partition. Let that partition size be $J$. First compare $\mathbb E[J^2]$ with $(\mathbb E[J])^2$. Then prove a linear expected upper bound for the corresponding recurrence with linear toll at general size.

**Solution.** The four equally likely sizes are $3,2,2,3$. Therefore

$$\mathbb E[J]=\frac52,\qquad\mathbb E[J^2]=\frac{13}{2},\qquad(\mathbb E[J])^2=\frac{25}{4}.$$

The two quadratic quantities differ by one-quarter. A recurrence involving expected child cost therefore cannot replace that cost by the cost of the average child without a separate justification.

For general $n$, uniform ranks give $\mathbb E[J]\le3n/4$ by explicitly summing the symmetric rank distribution. Assume a pointwise induction envelope for every smaller size: $T(j)\le Cj$. Taking its conditional expectation preserves the inequality and gives $\mathbb E[T(J)]\le C\mathbb E[J]\le3Cn/4$. If the local toll is at most $cn$, choosing $C\ge4c$ closes the bound, with bases included by increasing $C$. A compulsory linear scan supplies $\Omega(n)$ expected work, so the tight class is $\Theta(n)$ for this stated process.

The expectation is conditional on the current size and a newly uniform pivot. A deterministic adversarial pivot distribution does not satisfy the same mean-shrink bound. The diagram shows all four outcomes with their probabilities, means and second moments rather than animating a fictitious child of fractional size 2.5.

### Challenge 9. Exact exponential comparison

**Problem.** For $T_0=1$ and $T_n=2^nT_{n-1}$, compare its exact answer with $2^{n^2}$ and $2^{n^2/2}$. Which, if either, is in the same tight class?

**Solution.** Expanding the changing multipliers gives $T_n=2^{n(n+1)/2}$. Relative to $2^{n^2}$, the ratio is $2^{(-n^2+n)/2}\to0$, so that larger exponential is not a matching tight answer. Relative to $2^{n^2/2}$, the ratio is $2^{n/2}\to\infty$, so even deleting only the linear part of the exponent changes the tight class. Neither is in $\Theta(T_n)$.

The exact expression $(\sqrt2)^{n^2+n}$ is in that class by equality. A constant additive error in the exponent would produce a bounded positive multiplicative factor; a linear or quadratic unbounded exponent error generally would not. For example, multiplying $T_n$ by two changes the exponent by one and preserves its tight class. Replacing the exponent by its leading polynomial term does not.

At $n=4$, the actual value is 1024, while the two proposed values are 65536 and 256. The logarithmic display records these exponents 10,16,8 exactly and continues through several indices so the changing differences are visible. Finite data is illustrative; the two ratio limits are the proof. This example tests exponential sensitivity rather than applying a polynomial simplification rule in the wrong domain.

### Challenge 10. A DAG reduction with a changed local toll

**Problem.** A program requests the same half-size state twice but reuses the first result. Its local work is $\log_2N$, its unit base is at one, and $N=2^h$. Find the exact reused cost and compare it with the unreused version.

**Solution.** The reused program executes one recursive child, so $U_h=U_{h-1}+h$ with $U_0=1$. It follows that

$$U_h=1+\frac{h(h+1)}2,$$

which is $\Theta((\log N)^2)$ in the original size. At $N=32$, $h=5$ and the cost is 16. In contrast, two executed children give $V_h=2V_{h-1}+h$ with $V_0=1$. The zero-seed weighted-index solution plus the homogeneous seed yields $V_h=3\cdot2^h-h-2$. At $h=5$ this equals 89 and has order $\Theta(N)$.

Both programs have logarithmic depth and the same local toll, but their total executed work differs because one follows a chain and the other expands a binary tree. The recursion arguments refer to the identical state, not simply two different states of equal size. A bounded lookup per reuse adds a bounded cost per level and preserves the reused quadratic-logarithm order, although its exact polynomial constant changes. The model labels the reused edge as a reference, not an extra executed child, and shows the two exact ledgers side by side through every transformed index.

Each exact formula satisfies its own seed and step equation. Confusing the two child counts or dropping the unit leaf seed would change the finite values, even where the broad growth class stayed the same.
