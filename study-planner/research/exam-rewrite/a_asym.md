## Teaching through formulas and conceptual decisions

### Decide the relation before comparing growth

For eventually positive $g$, $f\in O(g)$ means one constant upper bound on $f/g$ beyond some threshold. $f\in\Omega(g)$ means an eventual positive lower bound; $\Theta$ requires both. Little-oh requires $f/g\to0$, a strictly stronger conclusion than boundedness. A positive finite ratio limit proves $\Theta$, but the absence of a limit does not refute $\Theta$: a ratio oscillating between1 and3 is still bounded above and below.

### Transform exponents and logarithms exactly

For fixed positive bases with logarithms defined, $a^{\log_b n}=n^{\log_b a}$. This is an exact identity obtained by taking natural logarithms. In contrast, $a^{\log_b^2n}$ has exponent proportional to $(\ln n)^2$ and grows faster than every fixed polynomial. Constants inside an exponent are not multiplicative constants outside it: $2^{2n}/2^n=2^n$ is unbounded.

For fixed integer$r$, $\binom nr=\Theta(n^r)$ because the numerator is a product of$r$ linear factors and$r!$ is constant. If$r$ grows with$n$, this reasoning fails. In particular, central binomial coefficients are exponential up to a polynomial factor; the fixed-index theorem must not be silently generalized.

### Cancellation and several variables need their own analysis

Knowing $f,g\in\Theta(n^2)$ does not determine $f-g$: cancellation can leave zero, a linear term or an oscillatory residual. For two independent parameters, a proposed $O(n)$ bound on $n+m$ fails on the path $m=n^2$. Conversely, $n+m\in\Theta(\max(n,m))$ follows from the two inequalities $\max(n,m)\le n+m\le2\max(n,m)$. Choose parameter paths to refute a uniform claim.

## Formula and conceptual problem bank

### Question 1. A strict growth relation

For $f(n)=n\log_2n$ and $g(n)=n^{1.1}$, which strongest listed relation holds?

**A.** $f\in\Theta(g)$

**B.** $f\in o(g)$

**C.** $f\in\omega(g)$

**D.** The functions are incomparable.

**Answer: B.**

The ratio is $\log_2 n/n^{0.1}$, which tends to zero because every fixed positive power dominates a logarithm. Thus little-oh holds and also implies big-oh. A finite crossover is not relevant to an eventual limit. The exponent gap0.1 is positive and fixed; a gap tending to zero would require a different calculation.

### Question 2. An exponent identity

For $n>0$, what is $4^{\log_2n}$?

**A.** $n$

**B.** $n^2$

**C.** $n^4$

**D.** $4\log_2n$

**Answer: B.**

Write4 as $2^2$: $(2^2)^{\log_2 n}=2^{2\log_2 n}=n^2$. Equivalently use $a^{\log_b n}=n^{\log_b a}$. Multiplying the exponent does not multiply the final function by4. The identity is exact, so its asymptotic consequence follows immediately.

### Question 3. An oscillating tight bound

Let $f(n)=n(2+(-1)^n)$ for positive integers$n$. Which statement is correct?

**A.** $f\in\Theta(n)$ but $f/n$ has no limit.

**B.** $f\in o(n)$

**C.** $f\notin O(n)$

**D.** $f/n\to2$

**Answer: A.**

The factor is1 on odd$n$ and3 on even$n$, hence $n\le f(n)\le3n$ for every$n$. This proves tight order without a ratio limit. Odd and even subsequences give limits1 and3, so no full limit exists. A ratio method is a sufficient tool when a limit exists, not a necessary definition of tight order.

### Question 4. A cancellation residual

What is the tight order of $(n+1)^3-n^3$?

**A.** $\Theta(n)$

**B.** $\Theta(n^2)$

**C.** $\Theta(n^3)$

**D.** $\Theta(1)$

**Answer: B.**

Expand before comparing: $(n+1)^3-n^3=3n^2+3n+1$. The cubic terms cancel and the quadratic term dominates. For $n\ge1$ it is between $3n^2$ and $7n^2$. Subtracting the labels $\Theta(n^3)$ from each other is not an algebraic operation on the actual functions.

### Question 5. Factorial logarithm

What is the tight order of $\log_2(n!)$?

**A.** $\Theta(\log n)$

**B.** $\Theta(n)$

**C.** $\Theta(n\log n)$

**D.** $\Theta(n^2)$

**Answer: C.**

Upper bound each of$n$ factors by$n$, obtaining $n!\le n^n$. For the lower bound, at least roughly$n/2$ factors are at least$n/2$, so $\log(n!)\ge(n/2)\log(n/2)$ up to integer rounding. Both bounds are order$n\log n$. No exact Stirling constant is needed to establish this order.

### Question 6. Fixed-index combination

For fixed $r=4$, what is the tight order of $\binom n4$ as $n\to\infty$?

**A.** $\Theta(n)$

**B.** $\Theta(n^2)$

**C.** $\Theta(n^4)$

**D.** $\Theta(4^n)$

**Answer: C.**

The exact expression is $n(n-1)(n-2)(n-3)/24$. Dividing by$n^4$ gives a ratio tending to1/24. Thus the order is$n^4$. The fixed lower index is essential; treating$r$ as a growing input would invalidate the constant-factor product argument.

### Question 7. Independent parameters

For independently unbounded positive$n,m$, which uniform tight bound holds for$n+m$?

**A.** $\Theta(n)$

**B.** $\Theta(m)$

**C.** $\Theta(\max(n,m))$

**D.** $\Theta(nm)$

**Answer: C.**

The maximum is at most the sum, and the sum is at most twice the maximum. These bounds use constants independent of both parameters. Taking$m=n^2$ refutes a uniform linear bound in$n$, and taking$n=m^2$ refutes the corresponding bound in$m$. Taking$n=m$ refutes tight order$nm$.

### Question 8. Exponential constants

Which comparison is true?

**A.** $2^{2n}\in\Theta(2^n)$

**B.** $2^{2n}\in\omega(2^n)$

**C.** $2^{2n}\in o(2^n)$

**D.** $2^{2n}\in O(n^2)$

**Answer: B.**

The ratio $2^{2n}/2^n=2^n$ tends to infinity, which is precisely the strict lower-growth relation inB. The constant2 multiplies$n$ inside an exponent and cannot be discarded as a multiplicative constant on the function. Every exponential here also outgrows fixed$n^2$.

### Question 9. Superpolynomial but subexponential

For $f(n)=n^{\log_2n}$, which assertion is correct?

**A.** $f\in\Theta(n^2)$

**B.** $f\in O(n^{100})$

**C.** $n^k\in o(f)$ for every fixed$k$, and $f\in o(2^n)$.

**D.** $f\in\Theta(2^n)$

**Answer: C.**

Taking natural logarithms gives $\ln f=(\ln n)^2/\ln2$. Compared with $\ln(n^k)=k\ln n$, the difference tends to infinity; hence every fixed polynomial is smaller. Compared with $\ln(2^n)=n\ln2$, the difference tends to negative infinity, so the ratio to$2^n$ tends to zero. Comparing logarithms establishes ratio behavior only after examining their difference.

### Question 10. Big-oh is not equality

If a positive runtime belongs to $O(n^2)$, which further statement must hold?

**A.** It belongs to $\Theta(n^2)$.

**B.** It belongs to $O(n^3)$.

**C.** It belongs to $\Omega(n^2)$.

**D.** It belongs to $o(n^2)$.

**Answer: B.**

For $n\ge1$, $n^2\le n^3$, so transitivity gives the weaker cubic upper bound. A linear runtime is a counterexample toA andC. A quadratic runtime is a counterexample toD. An upper bound states a permitted ceiling, not automatically the exact rate or a strict relation.

<!-- CHALLENGE-BANK -->

### Question 11. Challenge: Oscillation across growth classes

For positive integer$n$, let$f(n)=n^{2+\sin(\ln n)}$ and$g(n)=n^2$. Which statement holds?

**A.** $f\in\Theta(g)$

**B.** $f\in O(g)$ but not$\Omega(g)$

**C.** $f\in\Omega(g)$ but not$O(g)$

**D.** Neither big-oh nor big-omega relation holds.

**Answer: D.**

The ratio is$n^{\sin(\ln n)}$. Near logarithmic phases$\pi/2+2k\pi$, it grows like$n$ and is unbounded. Near$3\pi/2+2k\pi$, it behaves like$1/n$ and tends to zero. Integer indices can be chosen by rounding the corresponding exponentials; their logarithmic error tends to zero. Thus no uniform upper constant or positive lower constant works. A ratio lacking a limit does not always cause incomparability, but these two subsequences do.

### Question 12. Challenge: A floor inside an exponent

For$n\ge1$, what is the relation between$f(n)=2^{\lfloor\log_2 n\rfloor}$ and$n$?

**A.** $f\in\Theta(n)$, but$f/n$ need not converge.

**B.** $f\in o(n)$

**C.** $f\in\omega(n)$

**D.** $f/n\to1$

**Answer: A.**

If$2^k\le n<2^{k+1}$, then$f=2^k$, so$n/2<f\le n$. These constant bounds establish tight linear growth. At powers of two the ratio is1, while near the top of each interval it tends to1/2. Hence there is no limit1 or any single ratio limit. Rounding the logarithm changes a bounded factor without creating a strict growth relation.

## Applicable formulas and examination notes

### 1. Ratio outcomes

For eventually positive$g$, a ratio limit0 gives little-oh; a positive finite limit gives tight order; infinity gives little-omega. Failure of a limit leaves the question open: bounded positive oscillation can still give tight order.

### 2. Polynomial versus logarithm

For fixed $\epsilon>0$, $(\log n)^k/n^\epsilon\to0$ for fixed$k$. Thus $n\log n\in o(n^{1.1})$. A varying exponent or logarithm power is not covered by the fixed-parameter theorem.

### 3. Move exponents correctly

$a^{\log_b n}=n^{\log_b a}$ for fixed valid bases. Thus $4^{\log_2n}=n^2$. Squaring the logarithm in the exponent instead yields superpolynomial growth; parentheses determine which expression is being compared.

### 4. Exponential ratios

Compare $a^{cn}$ with $a^n$ by the ratio $a^{(c-1)n}$ for fixed$a>1$. When$c>1$, the ratio diverges. A coefficient inside an exponent is not a dispensable outside constant.

### 5. Factorial logarithms

Use $\log(n!)=\sum_{j=1}^n\log j$ and upper/lower blocks to establish $\Theta(n\log n)$. This does not imply $n!\in\Theta(n^n)$: exponentiating a tight-order logarithm does not preserve multiplicative tight order.

### 6. Fixed binomial index

$\binom nr\in\Theta(n^r)$ only when$r$ is a fixed nonnegative integer. For$r=4$, expand four linear factors and divide by24. If$r$ grows with$n$, analyze its factorials instead of treating$r!$ as constant.

### 7. Subtract actual functions

Expand $(n+1)^3-n^3$ before selecting its dominant term; the answer is quadratic. Bounds on each operand alone do not specify the difference. A difference can even be zero or change sign.

### 8. Independent variables

$n+m\in\Theta(\max(n,m))$ uniformly, with constants1 and2. To reject a single-variable guess, choose a legal path such as$m=n^2$. A relation imposed between parameters can change the answer and must be stated.

### 9. Quantified bound witnesses

To prove big-oh, give a constant$c$ and threshold$n_0$ working for every larger input. To refute it, show that every proposed$c,n_0$ admits a violating larger input. A few measured values establish neither statement.

### 10. Hierarchy through log differences

For $n^{\log_2n}$, compare $\ln f$ with the log of a candidate using their difference, not just their ratio. The difference with a fixed polynomial log diverges upward; the difference with$n\ln2$ diverges downward. This gives strict ratio conclusions.

<!-- BOUNDARY-NOTES -->

### 11. Little relations and transitivity

$f\in o(g)$ implies $f\in O(g)$ but not conversely. $f\in\Theta(g)$ is symmetric, while big-oh is not. With positive functions, transitivity preserves upper bounds; subtracting or exponentiating their class labels generally does not preserve a tight relation.

### 12. Floors and shifts

For fixed positive $c$, $\lfloor cn\rfloor$ is tightly linear once $n$ is large. A fixed additive shift does not alter a monotone polynomial's order, but applying it inside an arbitrary oscillating or exponential-indexed function requires analysis of that actual function.

### 13. Upper algorithm versus lower problem bound

An algorithm's upper bound establishes existence of one method with that cost. A problem lower bound quantifies over every algorithm in the specified model. A slow algorithm cannot prove a problem requires its runtime.
