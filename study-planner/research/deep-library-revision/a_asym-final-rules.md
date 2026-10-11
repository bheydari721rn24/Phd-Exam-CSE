## Complete asymptotic rules and examination traps

### 1. Identify the function and its model

State whether the object is an exact operation count, a worst-case maximum, a distributional average or a randomized expectation. A statement about one input is not a worst-case bound. A bound on one algorithm is not automatically a lower bound for the whole problem.

### 2. Translate each bound into its quantifiers

For $O$, one upper constant and one threshold must work for every later input. For $\Omega$, a positive lower constant must work on that same kind of tail. For $\Theta$, both inequalities must hold. Constants may not change with the input being bounded.

### 3. Finite exceptions do not refute tail claims

A lower bound may start after a small zero or negative value if the function is eventually nonnegative. One small violation does not refute an asymptotic relation. To disprove it, construct violations beyond any proposed threshold.

### 4. Infinitely many successes are insufficient

An alternating function can satisfy a lower inequality on every odd input and fail it on every even input. An eventual bound requires all sufficiently large inputs. Check every unbounded parity class or other relevant subsequence.

### 5. Use the proper normalized ratio

Divide by the entire proposed comparison function, retaining coefficients and parentheses. If that denominator is eventually positive, ratio zero gives little-oh, a finite positive limit gives tightness and infinity gives little-omega. An undefined denominator requires another formulation.

### 6. A nonexistent limit is not a verdict

Inspect eventual upper and lower envelopes. Ratios alternating between one and three establish tightness; ratios approaching zero and infinity on separate subsequences refute both one-sided bounds. Oscillation by itself proves neither conclusion.

### 7. Tightness and equivalence are distinct

The relation $f\sim g$ requires ratio one. The relation $f\in\Theta(g)$ requires only positive finite envelopes. A ratio tending to seven proves the latter but not the former; a bounded oscillating ratio may prove tightness without any limit.

### 8. Strict bounds quantify over every constant

Little-oh requires the ratio to fall below every prescribed positive constant eventually. Little-omega requires it to exceed every such constant. Failure of a tight relation does not imply either strict relation when subsequences behave differently.

### 9. Upper bounds need not be tight

A function of tight order $n\log n$ also belongs to $O(n^2)$. In a multiple-choice question using only $O$, more than one option can be literally true. Distinguish the mathematically true statements from a source's conventional request for the smallest listed upper bound.

### 10. Simplify cancellations before reading degrees

Compute the full expression before selecting its highest surviving power. Subtracting two quadratic expressions can leave zero, a linear function or another quadratic function. Subtracting unspecified $\Theta$ classes does not determine a tight answer.

### 11. Prove positivity for signed expressions

The default runtime convention is eventually nonnegative. If $g>0$ and $|h|=o(g)$, an eventual bound $|h|\le g/2$ gives $g/2\le g+h\le3g/2$. This justifies lower-order signed perturbations without permitting arbitrary negative runtimes.

### 12. Use a conjugate for close square roots

The identity $\sqrt{A}-\sqrt{B}=(A-B)/(\sqrt{A}+\sqrt{B})$ exposes cancellations. For example, $\sqrt{n^2+n}-n$ tends to one half, whereas $\sqrt{n^2+1}-n$ has reciprocal-linear order. The leftover numerator determines the distinction.

### 13. Fixed logarithm bases change a constant

For fixed $a,b>1$, $\log_a n=(\log_b n)/(\log_b a)$. This preserves tight order while changing exact values. If the base varies, redo the algebra: $\log_n n=1$ is not tightly logarithmic.

### 14. Iteration is different from a power

Write parentheses explicitly. The expressions $\log(\log n)$, $(\log n)^2$ and $\log(n^2)$ apply different operations. A nested exponential can collapse under iterated logarithms without making its full output small.

### 15. Recheck variable exponents

The polynomial-degree rule assumes a fixed exponent. Here $n^{1/\log_2 n}=2$ exactly, while $n^{\log_2 n}$ is larger than every fixed polynomial and smaller than $2^n$. Taking logarithms of ratios reveals which situation applies.

### 16. Distinguish coefficients inside and outside powers

A fixed positive factor outside $a^n$ preserves its tight class. Replacing $a^n$ by $a^{cn}$ generally does not when $a>1$ and fixed $c\ne1$. An additive unbounded change in the exponent can also destroy tightness.

### 17. Compare exponent differences directly

For fixed $a>1$, the quotient $a^u/a^v=a^{u-v}$. A bounded exponent difference yields tightness, and a difference tending to positive or negative infinity gives strict growth in the corresponding direction. Equal broad orders of $u$ and $v$ are insufficient.

### 18. Taking logarithms loses multiplicative precision

The logarithms of $2^{n^2}$ and $2^{n^2+n}$ are equivalent, but the original ratio is $2^n$. A polynomial logarithm describes the quantity's scale of representation, not polynomial enumeration work. Do not exponentiate a broad tight class as though it were an exact identity.

### 19. Use the hierarchy with fixed hypotheses

For fixed positive $k,\varepsilon$ and fixed $a>1$, $(\ln n)^k=o(n^{\varepsilon})$ and $n^{\varepsilon}=o(a^n)$. If a power, base or coefficient varies with input, those fixed-parameter theorems may not apply.

### 20. Factorial bounds can be elementary

The sandwich $(n/2)^{n/2}\le n!\le n^n$ for $n\ge2$ yields $\ln(n!)\in\Theta(n\ln n)$. A fixed-base exponential is strict smaller order than $n!$, while $n!=o(n^n)$. A sharper approximation is unnecessary for these class statements.

### 21. Round integer capacities upward

The least nonnegative $h$ with $2^h\ge M$ is $\lceil\log_2M\rceil$ for integer $M\ge1$. Check neighboring powers rather than rely on floating-point rounding. Having enough leaves is a necessary capacity condition, not proof of an attainable optimal algorithm.

### 22. Floors inside exponentials need control

The exact bound $n/2<2^{\lfloor\log_2 n\rfloor}\le n$ preserves tight linear order. Its ratio alternates through binary blocks and has no unique limit. A bounded rounding change can preserve tightness while destroying equivalence.

### 23. A factorial argument shift can matter

The ratio $(2n)!/n!=\prod_{j=n+1}^{2n}j$ is unbounded. The corresponding logarithms still share tight $n\log n$ order. Tight equivalence of logarithms cannot be transferred back to the factorials.

### 24. Fixed-index binomial coefficients are a special case

For fixed $r$, $\binom nr/n^r\to1/r!$. If $r$ varies with $n$, neither the factorial denominator nor the number of factors is fixed. The fixed-degree polynomial proof cannot be reused without its hypothesis.

### 25. Harmonic growth is not exact logarithmic equality

The bounds $\ln(n+1)\le H_n\le1+\ln n$ prove logarithmic order and equivalence to $\ln n$. Exact partial sums remain rational sums of unequal reciprocals. Divergence says the sum is unbounded; it does not imply linear growth.

### 26. The maximum rule needs a uniform multiplier

For a fixed number $r$ of nonnegative summands, the sum lies between the maximum and $r$ times that maximum. A growing term count can introduce another factor, and opposite signs can cancel. In special varying-count families, prove a bounded multiplier explicitly.

### 27. Products and transitivity combine witnesses

Multiply nonnegative upper inequalities to obtain a product upper bound, and combine both sides for a tight product. Take the maximum of the original thresholds. Transitivity multiplies witness constants, which remain independent of input.

### 28. Reciprocation reverses inequalities

If $0<f\le cg$ eventually, then $1/f\ge1/(cg)$. Thus an upper bound becomes a reciprocal lower bound, rather than automatically a reciprocal tight bound. Two-sided positive witnesses are required to preserve tightness under inversion.

### 29. Composition must reach the original tail

Substituting an inner argument tending to infinity preserves a valid eventual inequality if it stays in the domain. A bounded inner argument may keep hitting values outside the proven tail. Applying an outer exponential to the values is a different operation and may amplify constants into unbounded ratios.

### 30. Declare the multivariate domain and tail

A joint-tail convention requires both parameters past their own thresholds. A combined-size convention can include one parameter fixed. Test allowed paths that grow both variables when needed, and retain graph or matrix restrictions before simplifying.

### 31. Count significant recurrence levels and their tolls

A shrinking one-branch recurrence with squared-logarithm toll can accumulate cubic-logarithm cost. A square-root recurrence should be studied in logarithmic size, with floors and a terminating base region controlled. Multiplying recurrences require products or logarithms, not additive toll formulas.

### 32. Finite graphs illustrate; proofs establish tails

A plotted prefix cannot certify a uniform bound over infinitely many inputs. Use explicit witnesses, justified limits or counterexample subsequences to prove the claim. Finite crossovers remain separate exact calculations even after the tight classes are known.
