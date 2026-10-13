## Deeper recurrence constructions and proof repairs

This section extends the complete lesson; it does not replace the full prerequisite instruction or the forty derivation tutorials. Its models are explicit mathematical recurrences. An algorithmic upper inequality, an equality and a lower bound are identified separately.

### Construction 1. Derive the complete level sum before classifying it

Let the input be exactly $N=b^h$, where $b>1$ is fixed, and let the mathematical recurrence be $T(N)=aT(N/b)+f(N)$ with $a>0$ and seed $T(1)=c$. For an actual call tree, $a$ must be a positive integer; the algebraic recurrence also permits positive noninteger weights. Repeated substitution proves the exact identity

$$T(b^h)=a^hc+\sum_{j=0}^{h-1}a^jf(b^{h-j}).$$

The first term is the complete base contribution. The index $j$ is depth from the root; $h-j$ is the remaining logarithmic size. The identity follows by induction on $h$: multiplying the corresponding child identity by $a$ shifts every depth by one, and the root adds the missing $j=0$ toll. Thus a fully counted tree, with a stopping rule and a justified sum, is already a proof.

For $f(N)=N^d$, put $q=a/b^d$. The internal sum is $N^d\sum_{j=0}^{h-1}q^j$. If $q<1$, a finite geometric sum gives root domination; if $q=1$, every internal level contributes $N^d$ and the count of levels supplies a factor $\log N$; if $q>1$, later levels dominate. In the last case, the internal sum and the positive base contribution both have order $N^{\log_ba}$. These calculations establish lower bounds as well as upper bounds when the toll and bases are positive as stated. If the source specifies only $f\in O(N^d)$, the same calculation supplies an upper envelope, not a matching positive toll automatically.

There is no rule that multiplies an arbitrary root toll by depth. One half-size child with linear toll has geometrically decreasing level work and linear total. Two half-size children have constant linear aggregate work and $\Theta(N\log N)$ total. Four have increasing aggregate work and quadratic total. The difference is multiplicity, even when the shrink map and root toll are identical.

### Construction 2. Every real logarithmic power at the critical exponent

Put $p=\log_ba$. Assume $f(N)=N^p(\log_bN)^k$ for $N>b$, with a separately defined positive bounded base region containing $N\le b$. This avoids evaluating a negative power of zero at $N=1$. On exact powers, normalization by $N^p$ gives a weighted harmonic sum with the depth direction reversed:

$$\frac{T(b^h)}{b^{ph}}=C+\sum_{r=2}^{h}r^k.$$

The constant $C>0$ incorporates the base threshold. For $k>-1$, integral comparison bounds the sum above and below by positive multiples of $h^{k+1}$. For $k=-1$, it is a harmonic sum of order $\log h$. For $k<-1$, it converges to a finite positive limit and is bounded below by its positive seed. Therefore

- For $k>-1$, the answer is $T(N)\in\Theta(N^p(\log N)^{k+1})$.
- For $k=-1$, the answer is $T(N)\in\Theta(N^p\log\log N)$.
- For $k<-1$, the answer is $T(N)\in\Theta(N^p)$.

The threshold is negative one, not zero. A reciprocal logarithm gives a double logarithm, while a reciprocal squared logarithm gives no unbounded extra factor. These are independently derived extensions of the level identity; a university theorem stated only for nonnegative integer logarithmic powers must not be cited as if its statement covered every real $k$.

For $k=-1$, the explicit bounds $\log(h+1)-\log2\le\sum_{r=2}^{h}1/r\le1+\log h$ show where the double logarithm comes from. For $k=-2$, the upper bound $\sum_{r=2}^{\infty}r^{-2}\le\int_1^{\infty}x^{-2}\,dx=1$ gives a finite normalized envelope. Keeping the positive normalized base supplies the matching lower bound in both cases.

### Construction 3. Integer stopping rules and square-root rounding

A nonlinear shrink must first be transformed. For $T(N)=aT(\lfloor\sqrt N\rfloor)+\log_2N$, use $m=\log_2N$. For $N\ge4$, the transformed child lies in $[m/2-1,m/2]$. After $j$ steps, its logarithmic size lies in $[m/2^j-2,m/2^j]$, obtained by summing the geometrically damped one-unit errors. For two children, the total level toll is therefore at most $m$ and at least $m-2^{j+1}$ while the full level stays above the fixed base. The first $\Theta(\log m)$ levels each cost a positive multiple of $m$, and the entire tree has $O(m)$ leaves. This is a direct rounding proof of $\Theta(m\log m)$.

For the exact grid $N=2^{2^h}$ with a base at two, the square root decrements $h$ and the logarithmic toll is $2^h$. Thus $U_h=2U_{h-1}+2^h$ with $U_0=1$, giving $(h+1)2^h$ exactly. Restoring the original variable is a second mandatory step: $h=\log_2\log_2N$ and $2^h=\log_2N$. Neither $h$ nor $m$ is the original input.

By contrast, $N-\lceil\sqrt N\rceil$ is a slowly shrinking chain. Its square-root potential decreases by a number between one-half and two on each step. Its depth is $\Theta(\sqrt N)$, not $\Theta(\log\log N)$. Similar-looking square-root notation can denote fundamentally different maps. The fixed base must also stop at any fixed point of the map: square-root recursion at one never progresses.

### Construction 4. Unequal branches and the critical exponent

For an unperturbed recurrence $T(x)=\sum_{i=1}^{r}a_iT(b_ix)+g(x)$, assume fixed $a_i>0$, $0<b_i<1$, a fixed terminal interval with bounded positive costs, and the regularity hypotheses stated in the source theorem. The critical exponent $p$ is the unique real solution of $\sum_i a_ib_i^p=1$. Uniqueness follows because the left side is continuous and strictly decreasing in $p$, ranging from infinity to zero. The retained theorem states

$$T(x)\in\Theta\left(x^p\left(1+\int_1^x\frac{g(u)}{u^{p+1}}\,du\right)\right).$$

The integral's lower endpoint can be any fixed positive threshold appropriate to the toll; changing it adds a constant to the normalized expression. It cannot be placed at a logarithmic singularity without qualification. For two mass-conserving children, $b_1+b_2=1$, $a_1=a_2=1$ gives $p=1$. A linear toll then integrates to $\log x$. A quadratic toll integrates to order $x$, giving quadratic total. For $2T(x/2)+3T(x/3)$, the exponent solves $2(1/2)^p+3(1/3)^p=1$; it is neither a two-child nor a three-child equal-split exponent.

The theorem is not a license to insert arbitrary rounding maps, variable ratios, or oscillating tolls outside its hypotheses. Whenever a concrete tree or induction proof is short, it gives a clearer independently checked result. For $2T(x/2)+3T(x/3)+x^2$, the squared-size coefficient is $2/4+3/9=5/6$, so $Cx^2$ is an upper envelope when $C\ge6$ and the base is covered. The root supplies the lower bound. No numerical approximation of the branching exponent is needed for this example.

### Construction 5. Exact balanced merging away from powers of two

Define a mathematical size-toll recurrence by $A(1)=0$ and $A(n)=A(\lfloor n/2\rfloor)+A(\lceil n/2\rceil)+n$ for integers $n\ge2$. Put $L=\lfloor\log_2n\rfloor$. All depths below $L$ are complete and contribute total size $n$. At depth $L$, nodes have sizes one or two; the number of size-two nodes is $n-2^L$, each contributing two. Thus

$$A(n)=nL+2(n-2^L).$$

Ordinary worst-case merge comparisons have local toll $n-1$, not $n$. A full binary partition tree with $n$ singleton leaves has exactly $n-1$ internal nodes. Consequently subtracting one per internal node gives

$$C(n)=A(n)-(n-1)=nL+n-2^{L+1}+1.$$

Equivalently, with $H=\lceil\log_2n\rceil$, this is $nH-2^H+1$; the two expressions agree at powers of two and between them. For $n=13$, $A(13)=49$ and $C(13)=37$. These exact recurrences model different counted operations even though both have $\Theta(n\log n)$ order. Achieving the merge comparison maximum recursively requires interleaving child outputs; the comparison recurrence here explicitly counts that worst-case arrangement rather than claiming every input has its maximum. Constant leaf work would add its own $n$-fold contribution.

### Construction 6. Nonconstant multipliers and normalization

For $T_n=a_nT_{n-1}+b_n$ with every $a_n\ne0$, define $P_0=1$ and $P_n=\prod_{j=1}^{n}a_j$. Dividing the equation by $P_n$ gives

$$\frac{T_n}{P_n}=\frac{T_{n-1}}{P_{n-1}}+\frac{b_n}{P_n},\qquad T_n=P_n\left(T_0+\sum_{j=1}^{n}\frac{b_j}{P_j}\right).$$

This is an exact identity proved by telescoping; convergence is irrelevant for a finite sum. If a multiplier is zero, division by the product fails. At that index the recurrence resets to the current toll; restart the product after it rather than divide by zero. For signed multipliers, exact cancellation can occur, so positive-tree lower-bound arguments are inapplicable without further conditions.

The sequence $T_n=nT_{n-1}+n!$ with $T_0=1$ has $P_n=n!$, so $T_n/n!=1+n$ and $T_n=(n+1)n!$. An asymptotic answer of order $n!$ would be too small by the unbounded factor $n+1$. The authentic product question has $b_n=0$ and $a_n=2^n$, yielding $P_n=2^{n(n+1)/2}$. Taking logarithms is convenient only when the values are positive; it does not repair a zero or negative-value domain.

### Construction 7. Expected cost requires conditioning

If a random child size is $J$, the expected recurrence contains $\mathbb E[T(J)]$, not generally $T(\mathbb E[J])$. The latter replacement would need extra properties, and it is false in general: for equally likely sizes one and three and $T(j)=j^2$, the first expression is five while the second is four.

For an illustrative uniform-pivot process that always follows the larger child, $J=\max(R,n-1-R)$ for uniform rank $R$ in $0,\ldots,n-1$. Conditional on the current input, explicitly average every rank. For even $n=2m$, each size $m,\ldots,2m-1$ occurs twice, so $\mathbb E[J]=(3m-1)/2=3n/4-1/2$. For odd $n=2m+1$, size $m$ occurs once and each size $m+1,\ldots,2m$ twice; the mean is $(3m^2+2m)/(2m+1)$, below $3n/4$. The pointwise induction hypothesis $T(j)\le Cj$ therefore gives $\mathbb E[T(J)]\le C\mathbb E[J]\le3Cn/4$. With toll at most $cn$, choosing $C\ge4c$ closes the upper induction after covering bases. A compulsory linear root scan gives the lower bound and hence expected $\Theta(n)$ work for this stated process.

This argument uses a linear envelope after conditioning. It does not assume the unknown expected-cost function commutes with expectation. Actual QuickSelect may follow a smaller child for some target ranks, which only reduces this upper envelope. A worst-case pivot sequence remains a different model and can be quadratic. Probabilistic claims require specifying both the distribution and the conditioning state.

### Construction 8. Reconcile source errors before borrowing formulas

The four principal course scopes and Cornell supplement were actually read. Their disagreements are resolved by derivation. MIT's supplemental Akra–Bazzi example has critical exponent two and toll $\Theta(x^2/\log x)$ beyond a fixed threshold. Its normalized integral is $\int du/(u\log u)=\log\log u$, so the answer multiplies by $\log\log x$. The source's printed division by that factor is an error. The same proof's final lower-constant line needs the lower toll constant, not the upper one. The chapter uses independently verified statements rather than copying these lines.

A polynomial bound on the derivative alone does not establish uniform multiplicative comparability of a nonnegative toll: $g(x)=\sin^2x$ has bounded derivative but infinitely many zeros. Cornell's unequal-tree discussion prints a different equation than its intended one-third/two-thirds tree; the child sizes in the diagram and recurrence must agree. Its substitution comparison must recur on the envelope itself, rather than mix unknown original children into its definition.

Stanford's notes identify Winter 2026 in the actual retrieved header despite the URL's 2025 path. Its polynomial-toll theorem is an upper-bound formulation. MIT's recurrence exercises also use upper inequalities in places. A claimed tight class is supported here by a separate lower proof or exact positive recurrence. Princeton's size-toll merge formula is kept distinct from comparisons with toll size minus one. These repairs are recorded with exact reading scopes; screened universities are not represented as courses whose full notes were read.
