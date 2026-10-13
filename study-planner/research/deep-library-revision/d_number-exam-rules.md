## Final review: thirty-six complete examination decisions

### 1. State the integer and modulus domains before calculating

A congruence in this chapter has integer operands and a positive modulus. Negative inputs are allowed, but their canonical residues still lie in $[0,m)$. A modulus of zero turns divisibility into an equality condition and is not a residue ring with a finite canonical interval. Check whether the question requests integers, nonnegative integers, residue classes or representatives; these are different outcome domains.

### 2. Distinguish divisibility from ordinary division

The statement $a\mid b$ means that $b=ak$ for some integer $k$. It includes $a\mid0$ for every integer $a$, including zero. Zero divides only zero under this convention. A proof that silently excludes $0\mid0$ is using a different definition and must say so rather than mix the conventions.

### 3. Normalize gcd signs and handle the zero pair explicitly

The gcd is nonnegative and depends on absolute values, so $\gcd(-a,b)=\gcd(a,b)$. For a nonzero $a$, $\gcd(a,0)=|a|$. The computational convention $\gcd(0,0)=0$ preserves many algorithmic identities but is not a greatest positive numerical divisor. Do not attach a finite prime-exponent vector to zero.

### 4. A Bezout identity is an exact certificate

An expression $sa+tb=d$ alone does not prove that $d$ is the gcd. Also verify $d\ge0$ and that $d$ divides both inputs. Then every common divisor divides the linear combination, establishing the gcd characterization. Extended Euclid provides both the divisibility result and the coefficients, rather than an approximate numeric guess.

### 5. Common divisors are preserved by remainder reduction

For $a=qb+r$, a number divides both $a,b$ if and only if it divides both $b,r$. This proves the Euclidean gcd identity. The positive second remainder strictly decreases, supplying termination separately from preservation. A decreasing value without a lower bound would not justify termination, and a conserved gcd alone would not justify it either.

### 6. Count Euclidean operations under a stated model

The number of remainder steps is logarithmic in the input magnitude, or linear in the number of input bits. A remainder operation on large integers does not have constant bit cost. Fibonacci worst-case examples have unit intermediate quotients, but their final nonzero division can have quotient two. Do not quote an arithmetic-operation count as a fully specified machine running time.

### 7. Test linear-congruence existence with the target

For $ax\equiv b\pmod m$, let $d=\gcd(a,m)$. There is a solution if and only if $d\mid b$. Testing only the coefficient and modulus misses the target dependence. A nonunit coefficient can have many solutions or none; it does not automatically forbid a solution.

### 8. Divide the modulus along with the coefficient

When $d\mid b$, divide to obtain $(a/d)x\equiv b/d\pmod{m/d}$. Its coefficient is a unit in the reduced domain. Retaining the original modulus after that division generally discards valid answers. The reduced solution class has $d$ lifts modulo the original $m$.

### 9. Count a nonempty fiber in its original domain

A solvable linear congruence has exactly $d$ solution residues modulo $m$, not necessarily one. Multiplication by $a$ has kernel size $d$ and image size $m/d$. A nonempty target fiber is a kernel coset, not necessarily the kernel itself. Name the domain when saying that a solution is unique.

### 10. Treat the reduced modulus-one boundary without a false inverse

If $m/d=1$, the reduced congruence is automatic and all original-domain lifts remain. No ordinary modular inverse search is needed. For positive-modulus algorithms, normalize the exponent-zero identity as $1\bmod m$, which is zero at modulus one. This convention avoids returning a noncanonical one in the one-element residue domain.

### 11. Derive the entire progression before counting an interval

For $x=r+qt$, $q>0$, an inclusive interval gives $\lceil(L-r)/q\rceil\le t\le\lfloor(U-r)/q\rfloor$. The count is the nonnegative part of upper minus lower plus one. Replace a strict integer upper bound $x<U$ by $x\le U-1$ when $U$ is an integer. Negative endpoints require floor and ceiling, not truncation toward zero.

### 12. Cancellation preserves the original modulus only for units

The exact rule is $cx\equiv cy\pmod m$ if and only if $x\equiv y\pmod{m/\gcd(c,m)}$. Keeping modulus $m$ requires coprimality. An explicit difference equal to the reduced modulus often supplies a counterexample to a stronger distractor. Cancellation is not unrestricted field division in a composite ring.

### 13. Check shared-target compatibility before CRT inversion

For two moduli, the targets must agree modulo their gcd. If they conflict, no integer can satisfy both conditions. If they agree, solve the reduced parameter congruence constructively. A shared prime factor can cause inconsistency, but compatible shared factors are entirely permitted.

### 14. Identify the smallest positive period precisely

A consistent two-modulus system repeats with smallest positive period equal to the lcm. The product is also a period but is minimal only for coprime moduli. A multiple of a true period is still a period, so a question offering both needs the word “smallest” or “fundamental.” This clarification repairs ambiguity without changing the mathematical solution set.

### 15. Canonical reconstruction is a separate range step

After constructing a CRT integer, reduce it modulo the combined lcm to obtain the least nonnegative representative. A correct solution outside the canonical interval is not the requested least representative. For a first solution after a deadline, impose an additional ceiling inequality on the progression parameter. The theorem alone does not choose that later occurrence.

### 16. Many overlapping congruences need pairwise compatibility

For every pair, the targets must agree modulo the corresponding gcd. Prime-power maxima prove these conditions are sufficient. The final period is the lcm of all moduli. Pairwise coprimality is stronger than necessary, and a global gcd of one does not make the moduli pairwise coprime.

### 17. Use a unit test before Euler or Fermat exponent reduction

Euler requires $\gcd(a,m)=1$. Fermat's form $a^{p-1}\equiv1$ requires a prime modulus and a base not divisible by that prime. The form $a^p\equiv a$ includes the zero coordinate. Dropping a premise can produce a wrong exponent-zero substitution even when some numerical examples happen to agree.

### 18. Separate a valid period from the exact order

The order is the least positive return to one. Euler's totient is a valid period but may be larger. To prove exact order, show a return and exclude smaller possible returns, often using divisors of the proposed order. The value modulus and the exponent period need not be equal.

### 19. A nonunit sequence can have a transient

Split the modulus into prime powers. At a prime dividing the base, valuation gives the vanishing threshold; at a prime not dividing it, a unit order gives periodicity. Use a tail period only after reaching every required threshold. A negative or zero exponent cannot replace a large positive exponent merely because the residues of the exponents agree.

### 20. Power towers require two different facts about the inner exponent

Compute its residue in the outer unit-coordinate period. Also prove any lower bound needed for a nonunit vanishing coordinate. The enormous exponent need not be constructed as an integer, but both contracts must be established. Declare right association: $a^{(b^c)}$ and $(a^b)^c$ are different expressions.

### 21. Repeated squaring uses old values in its invariant

For an odd remaining exponent, the accumulator receives one old-base factor before that base is squared. Halving the remaining exponent then preserves $result\cdot base^{left}$. The invariant identifies correctness, and the descending nonnegative exponent identifies termination. An implementation updating a coefficient or base too early can violate the proof despite using familiar formulas.

### 22. The last unused operation can still count

If the pseudocode squares the base on every iteration, include its final square in the operation count. If an optimized version omits it, the exact count differs. For positive exponent $e$, the former version has $\lfloor\log_2e\rfloor+1$ squarings and $s_2(e)$ accumulator products. The exponent-zero branch has no iterations and must be handled outside that logarithmic expression.

### 23. Nonzero and invertible are different in a composite ring

A residue is a unit exactly when its gcd with the modulus is one. A nonzero nonunit may be a zero divisor; for example two and three are both nonzero modulo six and their product is zero. Counting nonzero residues as units is valid for a prime field but false for a general composite modulus. Bezout gives the inverse certificate when the gcd is one.

### 24. Factorization coordinates justify the totient product

For $p^e$ with $e\ge1$, exclude exactly the $p^{e-1}$ multiples of $p$, leaving $p^e-p^{e-1}$ units. CRT multiplies these counts across distinct prime powers. Include an exclusion factor only for a prime actually dividing the modulus. When an exponent becomes zero, that prime disappears and the previous symbolic two-prime formula may need a new boundary branch.

### 25. Gcd and lcm use coordinate extrema

For positive integers, gcd takes the minimum exponent at each prime and lcm takes the maximum. Adding exponents computes a product. Missing prime factors have exponent zero. The identity $\gcd(a,b)\operatorname{lcm}(a,b)=ab$ follows from minimum plus maximum equaling the sum at each coordinate; signed inputs require absolute values.

### 26. Divisor counts require a bijective exponent encoding

For $N=\prod p_i^{e_i}$, positive divisors correspond exactly to vectors with $0\le f_i\le e_i$, giving $\prod(e_i+1)$. Repeated appearances of the same prime must be combined before using the product rule. Exponent zero includes the divisor one. Counting negative divisors, proper divisors or divisors with further constraints changes the outcome set and therefore the formula.

### 27. Square restrictions apply to each exponent individually

A positive integer is a square precisely when every prime exponent is even. An even sum of exponents is insufficient. The number of square divisors is $\prod(\lfloor e_i/2\rfloor+1)$. An odd exponent bound still permits even exponent choices; it does not force the divisor set to be empty.

### 28. A divisor sum is a weighted product, not a divisor count

The sum of positive divisors is $\prod(1+p_i+\cdots+p_i^{e_i})$. Multiplying out chooses and weights each divisor once. A factor of $e_i+1$ counts choices but omits their numeric values. At the integer one, both the divisor count and divisor sum are one under the empty-product convention.

### 29. Count every prime-power layer in a factorial

Legendre's formula sums $\lfloor n/p^j\rfloor$ over all positive $j$. Multiples of $p^2$ contribute twice, and multiples of $p^3$ contribute three times. Counting only multiples of $p$ loses those extra occurrences. For two, the independent binary-digit identity $v_2(n!)=n-s_2(n)$ can expose an arithmetic mistake.

### 30. Composite-base powers use the tightest prime supply

For $B=\prod p_i^{e_i}>1$, the largest $B^k$ dividing a nonzero integer $N$ is $\min_i\lfloor v_{p_i}(N)/e_i\rfloor$. A minimum, not a sum, is required because every base power needs every prime supply simultaneously. Show that the proposed $k$ fits all constraints and that $k+1$ fails at least one. This proves maximality rather than merely feasibility.

### 31. Factorial quotients cancel before the bottleneck is applied

For an integer binomial coefficient, subtract denominator factorial valuations from numerator valuations. The result can be zero even when the numerator has many factors of the prime. This is exact integer cancellation, not division by a nonunit in a modular ring. Negative resulting prime exponents would contradict integrality and indicate a calculation error.

### 32. The valuation of a sum has a qualified minimum rule

Unequal prime valuations give the minimum exactly. Equal valuations allow further cancellation and give only a lower bound. If the sum is zero, no ordinary finite valuation can be assigned. Do not reuse the always-additive product rule for addition or assume that matching valuations guarantee no cancellation.

### 33. Modular root counts depend on the ring

A prime field permits at most the polynomial degree in roots for a nonzero polynomial. Composite rings can have more roots through zero divisors. For roots of one, handle odd prime powers and powers of two separately, then combine choices by CRT. For roots of zero, prime-exponent ceilings classify all residues, including the explicitly checked zero residue.

### 34. A modular obstruction proves impossibility, not automatic existence

If an integer equation has no solution in one residue domain, it has no integer solution. Passing selected modular tests is usually only necessary. A full existence argument needs a construction or a theorem whose hypotheses and conclusion supply it. Laurent coefficient extraction is a useful contrast: an integral selection index in range constructs an actual binomial term and therefore is sufficient in that two-term expansion.

### 35. Course proofs and authentic stems must be checked independently

An elegant proof can contain a local notation error, such as using an unreduced value as a purported small remainder. An independently correct solution to a mistranscribed stem is still not a correct solution to the original question. The enlarged original scans here correct the outer exponent to fifteen in MS CS 1405 Q125 and the total to forty in Q129. The latter answer is ninety-six, ratio six, option four, with the right-open endpoint of option three excluded.

### 36. Arithmetic correctness is distinct from security and future performance

RSA's teaching proof must cover zero and nonzero coordinates at each distinct prime, not only units modulo their product. That establishes recovery in the declared arithmetic model. It does not prove cryptographic security or endorse old parameter recommendations. Likewise recorded finite checks and general proofs support the stated chapter claims; they do not certify a literal zero-error guarantee or success on every unseen examination question.

### Source and attribution index

The division, gcd and coefficient-certificate decisions are cross-checked against MIT 6.042J, Spring 2015, Lehman, Leighton and Meyer, [Number Theory](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf). Algorithm, CRT coordinate, Fermat and RSA decisions are cross-checked against UC Berkeley CS70, Fall 2026, course-authored [Note 6](https://www.eecs70.org/assets/pdf/notes/n6.pdf) and [Note 7](https://www.eecs70.org/assets/pdf/notes/n7.pdf). Valuation, cancellation, root-boundary and rotation decisions use Carnegie Mellon, Klaus Sutner, Fall 2022, [Modular Arithmetic](https://www.cs.cmu.edu/~sutner/pdf/60-modari.pdf). Domain, ring and inverse distinctions are compared with Cambridge, Marcelo Fiore, 2022–23, [Proofs, Numbers and Sets](https://www.cl.cam.ac.uk/teaching/2223/DiscMath/DiscMathProofsNumbersSetsNotes.pdf). Proof completions, counterexamples and synthesis are independently authored; exact fresh scopes are recorded in the chapter source audit.
