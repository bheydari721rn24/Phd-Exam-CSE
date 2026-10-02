# Divisibility, Modular Arithmetic, and Number Theory

## Sources, prerequisites, and chapter boundary

This is Discrete Mathematics Chapter 8, assigned to Week 2. It assumes integer algebra, ordinary and strong induction, equivalence relations, functions, and the invariant principle from the approved chapters. No previous experience solving modular equations is assumed.

Four principal written university courses were compared and actually read for this chapter: MIT's *Mathematics for Computer Science* by Eric Lehman, F. Thomson Leighton, and Albert R. Meyer; UC Berkeley CS 70, Spring 2022, taught by Satish Rao and Koushik Sen; CMU 15-151, Klaus Sutner's Fall 2022 modular-arithmetic slides; and Cambridge's *Discrete Mathematics: Proofs, Numbers, and Sets*, Marcelo Fiore, 2022–23. MIT supplies the invariant and linear-combination perspective; Berkeley supplies algorithm derivations and the coordinate interpretation of CRT; CMU supplies valuations, complete linear-congruence counts, rotations, Wilson's theorem, and generalized CRT; Cambridge supplies explicit domain conventions and the connection between gcd, linear combinations, rings, and fields. The [source comparison and exact reading ledger](../reviews/d_number-sources.html) distinguishes genuinely read material from course candidates.

**Boundary.** The chapter covers integer divisibility; division with negative dividends; gcd, lcm, and prime factorization; extended Euclid; integer linear equations; residue classes and valid cancellation; linear congruences; ordinary and generalized CRT; totient, Fermat, Euler, order, and safe exponent reduction; prime-power methods and selected quadratic equations; divisor functions and factorial valuations; elementary primality certificates; additive cycles and a mathematical RSA example. Analytic number theory, quadratic reciprocity, general discrete logarithms, advanced factorization algorithms, and a security-engineering course are outside this chapter. The final-month Iranian examination archive is not used here.

Read the lesson before the problem bank. The final review sheet is a separate tool for retrieving assumptions and methods; it does not replace any proof. The interactive laboratory displays a complete residue map for small moduli and a Bézout certificate, not an assertion about every possible large input or a test of your current knowledge.

## Divisibility and the division theorem

### Divisibility is an existential statement

For integers $a,b$, write $a ∣ b$ when some integer $k$ satisfies $b=ak$. This definition includes negative integers. Thus $−3 ∣ 12$, $5 ∣ 0$, and $0 ∣ 0$ are true; $0 ∣ 7$ is false. In ordinary expressions, dividing by zero is undefined. The assertion that zero divides zero is about an existential product equation, not permission to evaluate a quotient.

If $a ∣ b$ and $b ∣ c$, choose witnesses $b=ak$ and $c=bℓ$. Then $c=a(kℓ)$, establishing transitivity. If $d ∣ a$ and $d ∣ b$, every integer linear combination $ua+vb$ is divisible by $d$: substitute $a=dα$ and $b=dβ$ to obtain $ua+vb=d(uα+vβ)$. Conversely, divisibility of a combination does not imply divisibility of each summand. For example, five divides $2+3$ but divides neither two nor three.

On positive integers, divisibility is a partial order. To prove antisymmetry, $a ∣ b$ and $b ∣ a$ give positive integer quotients $b=ak$ and $a=bℓ$, hence $kℓ=1$ and both quotients are one. On all integers, this fails: three and negative three divide each other. What survives is equality of absolute values. On nonnegative integers, zero is the greatest element in the divisibility order because every nonnegative integer divides zero; this is unrelated to zero being the smallest number in the usual numerical order.

### Why the remainder must be specified

For an integer $a$ and a positive integer $m$, there are unique integers $q,r$ satisfying $a=qm+r$ and $0 ≤ r < m$. Existence follows by choosing $q=⌊a/m⌋$, which ensures $q ≤ a/m < q+1$. Multiply by the positive modulus and subtract $qm$ to obtain the required bounds. For uniqueness, two representations imply $(q−q')m=r'−r$. The right side has absolute value smaller than $m$, so its only possible multiple of $m$ is zero. Hence both remainders and both quotients agree.

For $a=−17$ and $m=5$, the quotient is negative four and the remainder is three: $−17=(−4)5+3$. A programming language using truncation toward zero might instead report quotient negative three and remainder negative two. Both are product identities, but only the first satisfies the mathematical remainder convention. This chapter always uses a positive modulus and the nonnegative canonical remainder, written $a mod m$.

Repeated subtraction is a possible algorithm when the dividend is nonnegative: initialize $q=0,r=a$ and repeatedly replace $(q,r)$ by $(q+1,r−m)$ while $r ≥ m$. The invariant $a=qm+r$ proves correctness, and the nonnegative rank $r$ proves termination. However, its iteration count is the quotient, which can be exponential in the bit length of the dividend. A division theorem, a correct algorithm, and an efficient bit algorithm are three different claims.

## Gcd, prime factors, and the divisibility lattice

### Greatest common divisors and the exceptional zero pair

If $a,b$ are not both zero, their gcd is the greatest positive common divisor of their absolute values. We extend the definition by the explicit computational convention $gcd(0,0)=0$. The phrase “greatest positive common divisor” cannot justify that convention: every positive integer divides both zeros, so no greatest positive divisor exists in numerical order. The universal divisibility characterization does extend: $g ∣ a$, $g ∣ b$, and every common divisor divides $g$; for two zeros this selects zero among nonnegative integers.

For $b>0$, write $a=qb+r$. An integer divides both $a,b$ exactly when it divides both $b,r$. One direction uses $r=a−qb$; the other uses $a=qb+r$. Consequently $gcd(a,b)=gcd(b,r)$. This equivalence preserves the entire set of common divisors, not merely its largest member.

Euclid's algorithm normalizes signs, then repeatedly replaces $(a,b)$ by $(b,a mod b)$ until the second component vanishes. The invariant is equality of the current gcd and the original gcd; the positive second component strictly decreases while the loop is enabled. At exit, the first component is the gcd, including input pairs with one zero. For two zero inputs, the loop is empty and the explicit convention returns zero.

### Arithmetic-operation count versus bit cost

For a sorted pair $a ≥ b>0$, within two remainder steps the algorithm either terminates or its larger positive argument becomes at most half its old value. If $b ≤ a/2$, the next larger argument is already at most half. Otherwise the first quotient is one and $a mod b=a−b<a/2$ becomes the larger argument after the following step. Thus the number of divisions is logarithmic in the positive input magnitude. A division of large integers is not a unit-cost physical operation: with school arithmetic on at most $L$-bit operands, a conservative bound is $O(L^3)$ bit operations from $O(L)$ divisions costing at most $O(L^2)$ each. This loose bound does not claim optimality. Consecutive Fibonacci inputs produce long quotient chains; the final quotient need not be one.

### Bézout's identity, derived constructively

Every pair that is not both zero has integer coefficients $s,t$ satisfying $sa+tb=gcd(a,b)$. During Euclid, keep a coefficient pair for each current remainder. Initially $a=1a+0b$ and $b=0a+1b$. If $r_0=s_0a+t_0b$, $r_1=s_1a+t_1b$, and $q=⌊r_0/r_1⌋$, the next remainder is

$r_2=r_0−qr_1=(s_0−qs_1)a+(t_0−qt_1)b$.

The last nonzero remainder is the gcd, so its recorded coefficients prove the identity. This method is called extended Euclid; MIT also calls it the Pulverizer. For signed inputs, run the algorithm on absolute values and multiply the corresponding coefficients by the input signs. The following original implementation returns a certificate even at the zero pair, where it returns $(0,0,0)$.

```python
def egcd(a, b):
    if a == 0 and b == 0:
        return 0, 0, 0
    r0, r1 = abs(a), abs(b)
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    while r1:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    return r0, s0 * (-1 if a < 0 else 1), t0 * (-1 if b < 0 else 1)
```

The parallel assignments use the old values on both right-hand sides. Updating the first coefficient and then using its new value to update the second would implement a different algorithm. Each update preserves both remainder representations and the common-divisor set; decreasing nonnegative remainders prove termination.

Bézout gives a stronger statement: the integer combinations of $a,b$ are exactly the multiples of their gcd. Every combination is divisible by the gcd; conversely, multiply a Bézout identity by any integer. This is why the gcd is the correct obstruction for integer linear equations, but nonnegative coefficients require additional inequalities.

### Prime factors: existence is not uniqueness

A positive integer $p ≥ 2$ is prime when its only positive divisors are one and itself. One is neither prime nor composite. Every integer $n ≥ 2$ has a prime divisor: choose its least divisor larger than one; a nontrivial factorization of that divisor would contradict minimality.

If $gcd(c,a)=1$ and $c ∣ ab$, multiply a Bézout identity $uc+va=1$ by $b$. Both terms on its right are divisible by $c$, so $c ∣ b$. In particular, if a prime divides a product, it divides at least one factor. The adjective “prime” matters: six divides $2·3$ without dividing either factor.

Strong induction proves that every $n ≥ 2$ is a product of primes. If it is composite, split it into smaller positive factors and invoke induction on both. For uniqueness, compare two prime products, use the prime-product lemma to match the first prime from one product with a prime in the other, cancel that ordinary integer factor, and continue. Thus a positive integer has a unique list of prime exponents, apart from order. A signed integer also needs its sign. Zero has no finite prime factorization.

Euclid's infinitude argument assumes a finite complete prime list and forms one plus their product. None of the listed primes divides this number, but it has some prime divisor. The constructed number itself need not be prime; the missing prime divisor is enough for the contradiction.

### Valuations and lattice operations

For a prime $p$ and nonzero integer $n$, let $v_p(n)$ be the exponent of $p$ in $|n|$. Then $v_p(ab)=v_p(a)+v_p(b)$. For positive integers, $a ∣ b$ exactly when every prime exponent in $a$ is at most its exponent in $b$. Gcd takes coordinatewise minima; lcm takes coordinatewise maxima. Therefore $gcd(a,b)·lcm(a,b)=ab$ for positive inputs. With signed inputs, the right side becomes $|ab|$; with a zero input define the lcm to be zero. Avoid applying finite valuations to zero without explicitly using the extended value infinity.

<!-- FIGURE:lattice -->

The gcd and lcm are the meet and join in divisibility order: every common divisor divides the gcd, and the lcm divides every common multiple. Their numerical sizes alone are insufficient to prove these order-theoretic statements. The exponent description also proves associativity, commutativity, distributivity, and absorption, because minima and maxima on a totally ordered exponent coordinate have those properties.

## Integer linear equations and nonnegative constraints

For integers $a,b,c$ with $(a,b) ≠ (0,0)$, the equation $ax+by=c$ has integer solutions exactly when $d=gcd(a,b)$ divides $c$. Necessity follows because $d$ divides every combination. Sufficiency follows by scaling Bézout coefficients by $c/d$.

If $(x_0,y_0)$ is one solution, all solutions are

$x=x_0+(b/d)t$, $y=y_0−(a/d)t$, where $t ∈ ℤ$.

To prove completeness, subtract the particular solution and divide by $d$: $(a/d)(x−x_0)=−(b/d)(y−y_0)$. The reduced coefficients are coprime. Hence $b/d$ divides $x−x_0$ when it is nonzero, giving the parameter; substitution determines the other difference. If a coefficient is zero, solve the remaining one-variable equation directly; the same parameterization is valid with a signed nonzero reduced coefficient of magnitude one. If both coefficients are zero, every pair solves the equation when $c=0$, and no pair solves it otherwise.

For positive coefficients and nonnegative unknowns, impose both inequalities on the parameter. If $a,b>0$, then $t ≥ ⌈−x_0d/b⌉$ and $t ≤ ⌊y_0d/a⌋$. Existence requires the lower integer bound not to exceed the upper; the number of pairs is the upper minus lower plus one. Bézout alone does not establish that a purchase or a population is feasible, because negative coefficients may appear in its certificate.

For coprime positive denominations $a,b$, the greatest nonrepresentable nonnegative amount is $ab−a−b$ when both exceed one. Here is a proof with explicit boundaries. In each residue modulo $a$, exactly one of $0,b,2b,…,(a−1)b$ lies in that residue, because multiplication by $b$ is invertible. Write any target $N$ in that residue as $jb+ka$ with $0 ≤ j<a$. If $N>ab−a−b$ and $k<0$, then $N ≤ jb−a ≤ (a−1)b−a=ab−a−b$, a contradiction. Conversely, a representation of $ab−a−b=ax+by$ would give $b(y+1) ≡ 0$ modulo $a$, so $y+1 ≥ a$; then $by ≥ (a−1)b$ exceeds the target by $a$. Thus it is not representable. If a denomination is one, every nonnegative target is representable. If the denominations are not coprime, infinitely many targets fail the gcd test.

## Residue classes, units, and linear congruences

### Congruence and remainder are different objects

For $m>0$, define $a ≡ b (mod m)$ by $m ∣ a−b$. This is a relation between integers, whereas $a mod m$ is a single canonical integer. The relation is reflexive, symmetric, and transitive by elementary divisibility. Its classes are $[a]_m={a+km:k ∈ ℤ}$, and there are exactly $m$ classes.

Addition and multiplication of classes are well-defined. If $a'=a+um$ and $b'=b+vm$, their sum differs from $a+b$ by $(u+v)m$, and their product differs from $ab$ by $m(av+bu+uvm)$. Thus changing representatives does not change the output class. Subtraction and nonnegative integer powers are also compatible. It follows by structural induction that any integer-coefficient polynomial may be evaluated after reducing its inputs and intermediate results.

This justification does not allow reducing an exponent modulo $m$. The exponent controls the number of multiplications; it is not a factor in the polynomial expression. Nor does it allow ordinary division or taking real square roots of congruences. For example, $2 ≡ 7 (mod 5)$ but $2^2 ≡ 4$ and $2^7 ≡ 3$ modulo five.

### Exactly when an inverse exists

For $m ≥ 2$, a residue $a$ has a multiplicative inverse exactly when $gcd(a,m)=1$. If $au ≡ 1$, the integer equation $au+mv=1$ rules out every common divisor larger than one. Conversely, Bézout supplies such an integer $u$ when the gcd is one. The canonical inverse is $u mod m$. If both $u,v$ are inverses, then $u ≡ u(av) ≡ (ua)v ≡ v$, proving uniqueness modulo $m$.

A residue with an inverse is called a unit. A nonzero nonunit is a zero divisor: for $d=gcd(a,m)>1$, the residue $m/d$ is nonzero and $a(m/d) ≡ 0$. Conversely, a unit cannot multiply a nonzero residue to zero. Therefore for $m ≥ 2$, the ring of residues is a field exactly when $m$ is prime. A composite modulus provides a proper factor that is a nonzero zero divisor. Modulus one has one residue, with zero equal to one; this chapter treats its congruence as automatically true and handles it separately, rather than applying field or order terminology to that degenerate ring.

### Cancellation changes the modulus when necessary

Let $m>0$ and $d=gcd(a,m)$. Then

$ax ≡ ay (mod m) ⇔ x ≡ y (mod m/d)$.

Write $a=da'$, $m=dm'$ with $gcd(a',m')=1$. The left condition is $dm' ∣ da'(x−y)$, equivalent by ordinary nonzero integer cancellation to $m' ∣ a'(x−y)$. Euclid's coprimality lemma removes $a'$, yielding the right condition. The reverse follows by multiplying back. This also handles $a=0$, where the new modulus is one and both sides are automatic. Cancelling a nonunit while keeping the old modulus loses legitimate solutions.

### Solving and counting every linear congruence

To solve $ax ≡ b (mod m)$, compute $d=gcd(a,m)$. There are no solutions unless $d ∣ b$. When it divides, divide **the coefficient, target, and modulus** by $d$, solve the reduced unit equation modulo $m'=m/d$, and obtain a single class $x ≡ x_0 (mod m')$. In the original residue interval there are exactly $d$ solutions:

$x_0, x_0+m', …, x_0+(d−1)m'$,

where the reduced representative satisfies $0 ≤ x_0<m'$. Distinctness and completeness follow from the spacing and the reduced class condition. If $m'=1$, all original residues satisfy the equation; no inverse calculation is needed. An equation with coefficient zero is either inconsistent or automatic.

The multiplication map $T_a:[x]_m ↦ [ax]_m$ makes this structure visible. Its kernel consists of $d$ equally spaced residues; its image consists of exactly the multiples of $d$ modulo $m$; each attainable output has exactly $d$ preimages. It is bijective precisely when $d=1$. This connects number theory to the earlier chapter's fibers and cancellation of functions.

<!-- FIGURE:fibers -->

## Chinese remainders and compatible systems

### Construction for coprime moduli

Suppose $m,n$ are positive and coprime. Choose $u,v$ with $um+vn=1$. To satisfy $x ≡ a (mod m)$ and $x ≡ b (mod n)$, take $x=avn+bum$. The first term is $a$ modulo $m$ and zero modulo $n$; the second is zero modulo $m$ and $b$ modulo $n$. Any two solutions differ by a multiple of both moduli, hence by a multiple of $mn$. There is exactly one canonical representative in the inclusive interval from zero to $mn−1$.

For pairwise coprime moduli $m_i$, let $M$ be their product and $M_i=M/m_i$. Let $u_i$ be an inverse of $M_i$ modulo $m_i$. The selector $e_i=M_iu_i$ is one in its own residue coordinate and zero in every other coordinate. The sum of $a_ie_i$, reduced modulo $M$, is the required solution. A product of noncoprime moduli does not produce this selector construction because the necessary inverses may fail.

<!-- MATH:crt -->

<!-- FIGURE:crt -->

The coordinate map $[x]_M ↦ ([x]_{m_1},…,[x]_{m_k})$ is a bijection preserving addition and multiplication. Thus a calculation modulo a squarefree or prime-power-factored modulus can be split into independent coordinates and recombined. This is more than a mnemonic for solving clock puzzles; it explains why roots and units combine independently across coprime factors.

### Shared factors impose compatibility

For arbitrary positive $m,n$, the two residue requirements are solvable exactly when $g=gcd(m,n)$ divides $b−a$. Necessity follows because the difference of the two requirements must vanish modulo every common divisor. For sufficiency, write $x=a+mt$. Substitution gives $mt ≡ b−a (mod n)$. The linear-congruence criterion is exactly the compatibility condition. Divide by $g$ and solve for $t$ modulo $n/g$. Substituting back gives one class modulo $m(n/g)=lcm(m,n)$.

For several congruences, merge them successively, carrying the current canonical solution and current lcm. Pairwise compatibility $a_i ≡ a_j (mod gcd(m_i,m_j))$ is necessary and sufficient. To justify sufficiency beyond two equations, factor the moduli into prime powers. For each prime, choose a congruence with largest exponent. Pairwise compatibility forces its residue to agree with every weaker power of that prime. The maximal prime-power conditions have coprime moduli, so ordinary CRT supplies a solution satisfying all original conditions. This proof prevents an unjustified leap from the two-equation case.

Mixed systems $a_ix ≡ b_i (mod m_i)$ must first pass each gcd solvability test and become simple residue requirements modulo reduced moduli. Only then check compatibility between equations. Pairwise coprimality of the **original** moduli is not the only relevant property after coefficient reduction.

## Totient, power cycles, and safe exponent reduction

### Counting units and proving Euler's theorem

For $n>0$, define $φ(n)$ as the number of residues relatively prime to $n$, with $φ(1)=1$. For $p$ prime and $e ≥ 1$, exactly $p^{e−1}$ residues modulo $p^e$ are divisible by $p$, so $φ(p^e)=p^e−p^{e−1}$. For coprime $m,n$, CRT pairs their residues, and a residue is a unit modulo $mn$ exactly when both coordinates are units. Consequently $φ(mn)=φ(m)φ(n)$. Applying this to distinct prime-power factors gives

<div class="formula-block"><math display="block" aria-label="phi of n equals n times the product over distinct primes dividing n of one minus one over p"><mrow><mi>φ</mi><mo>(</mo><mi>n</mi><mo>)</mo><mo>=</mo><mi>n</mi><munder><mo>∏</mo><mrow><mi>p</mi><mo>∣</mo><mi>n</mi></mrow></munder><mo>(</mo><mn>1</mn><mo>−</mo><mfrac><mn>1</mn><mi>p</mi></mfrac><mo>)</mo></mrow></math></div>

The product ranges over distinct prime divisors, not every repeated prime factor. The formula is efficient once a factorization is known; that qualification does not provide a fast method for factoring arbitrary large integers.

If $gcd(a,n)=1$ and $n ≥ 2$, multiplication by $a$ permutes the $φ(n)$ units. Multiply all elements before and after the permutation. The resulting congruence is $a^{φ(n)}P ≡ P (mod n)$, where $P$ is the product of all units and is itself a unit. Multiply by its inverse to cancel it and obtain **Euler's theorem**: $a^{φ(n)} ≡ 1 (mod n)$. For prime $p$, this becomes **Fermat's little theorem**, $a^{p−1} ≡ 1$ when $p$ does not divide $a$. For any integer $a$, including multiples of $p$, the all-base form is $a^p ≡ a (mod p)$.

### Multiplicative order is the exact period

For a unit $a$ modulo $n ≥ 2$, its order is the least positive $h$ for which $a^h ≡ 1$. Euler guarantees existence. If $a^k ≡ 1$, divide $k$ by $h$: $k=qh+r$ with $0 ≤ r<h$. The congruence reduces to $a^r ≡ 1$, so minimality forces $r=0$. Thus the order divides every returning exponent, particularly $φ(n)$. Two nonnegative powers agree exactly when their exponents agree modulo the order: cancel the smaller power, which is a unit, and apply the returning-exponent argument. Negative exponents are defined only for units, through powers of the inverse.

An order bound need not be the order itself. Modulo eight, every odd residue has square one, yet $φ(8)=4$. This does not contradict Euler; it shows that four is a valid but loose exponent period. Testing divisors of $φ(n)$ can discover a smaller order. A primitive root has order $φ(n)$; not every composite modulus has one, as the modulo-eight example already demonstrates.

### Nonunits have a transient before a cycle

If the base shares a prime factor with the modulus, Euler reduction is invalid. Factor $n$ into prime powers. For each $p^e$, let $v=v_p(a)$ when $a ≠ 0$. If $v>0$, then $a^k$ vanishes modulo $p^e$ once $kv ≥ e$; before that threshold, its valuation is exactly $kv$. If $v=0$, the base is a unit in that coordinate and Euler or its actual order applies. Solve each coordinate and recombine by CRT. If $a=0$, every positive power is zero, while the exponent-zero algorithm convention returns the multiplicative identity.

<!-- FIGURE:powers -->

For example, modulo twelve, the powers of two beginning with exponent zero are $1,2,4,8,4,8,…$. The repeating tail starts at exponent two; replacing exponent four by zero would return one rather than four. A finite-state transition $r ↦ ar mod n$ always eventually repeats, but its initial state need not lie on that cycle. For power towers, first determine the exponent information needed in each coordinate; recursively reducing all exponents by the original modulus has no justification.

### Repeated squaring with a precise contract

The following original implementation accepts any integer base, a nonnegative integer exponent, and a positive integer modulus. It returns a canonical residue even for modulus one. The exponent-zero convention is explicitly the empty product; the code is not a claim about analytic limits of zero to the power zero.

```python
def modpow(a, e, m):
    if m <= 0 or e < 0:
        raise ValueError('Use a positive modulus and a nonnegative exponent.')
    base, left, result = a % m, e, 1 % m
    while left:
        if left % 2:
            result = (result * base) % m
        base = (base * base) % m
        left //= 2
    return result
```

At every loop head, $result·base^{left} ≡ a^e (mod m)$. For an even remaining exponent, squaring the base and halving the exponent preserves the product. For an odd remaining exponent, first move one base factor into the result, then square and halve. At exit the remaining exponent is zero, so the result has the required residue. Positive remaining exponents strictly shrink; all intermediate residues stay canonical. For $e>0$, the loop has exactly $⌊log_2 e⌋+1$ iterations, one per binary digit; $e=0$ has none. There are that many squarings and as many extra multiplications as one bits in the exponent. These are arithmetic counts, not constant-cost operations on unbounded integers.

## Further consequences and examination boundaries

### Divisor counts, sums, and factorial valuations

For $n=p_1^{e_1}…p_k^{e_k}>0$, choosing a divisor means independently choosing each exponent from zero to its maximum. Hence the number of positive divisors is $τ(n)=∏(e_i+1)$. Summing all choices yields $σ(n)=∏(1+p_i+…+p_i^{e_i})$, with each factor also equal to $(p_i^{e_i+1}−1)/(p_i−1)$. Empty products at $n=1$ give both functions value one. Their multiplicativity holds for coprime factors; applying it to overlapping prime powers double-counts exponent choices. A positive integer has an odd divisor count exactly when every prime exponent is even, equivalently when it is a square.

For a prime $p$, the exponent of $p$ in $N!$ equals the sum of $⌊N/p^j⌋$ over positive $j$. The first term counts one contribution from each multiple of $p$, the next adds a second contribution for multiples of $p^2$, and so on. Only finitely many terms are nonzero. In a binomial coefficient, subtract the valuations of the two denominator factorials. This computes divisibility without evaluating huge factorials. A trailing-zero count in base ten is the minimum of the two- and five-valuations, whereas base twelve uses the minimum of the floor of the two-valuation divided by two and the three-valuation.

<div class="formula-block"><math display="block" aria-label="the p valuation of N factorial equals the sum over j from one through infinity of floor N over p to the j"><mrow><msub><mi>v</mi><mi>p</mi></msub><mo>(</mo><mi>N</mi><mo>!</mo><mo>)</mo><mo>=</mo><munderover><mo>∑</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mo>∞</mo></munderover><mo>⌊</mo><mfrac><mi>N</mi><msup><mi>p</mi><mi>j</mi></msup></mfrac><mo>⌋</mo></mrow></math></div>

### Squares, Wilson's theorem, and primality evidence

For a positive prime power $p^e$, the roots of $x^2 ≡ 0 (mod p^e)$ are exactly the multiples of $p^{⌈e/2⌉}$. Necessity follows because the exponent of $p$ in a nonzero square is twice its exponent in the base; sufficiency follows by squaring a multiple of that threshold. Zero itself is checked directly. There are $p^{⌊e/2⌋}$ distinct roots in the original interval. For a general positive modulus, multiply these independent local counts and combine the local roots by CRT. This is a complete classification of the square-zero equation, even though its answer need not consist only of the zero residue.

The square-one equation also has a complete elementary classification. If $p$ is odd and $p^e ∣ (x−1)(x+1)$, then $p$ cannot divide both factors, since their difference is two. Therefore the entire prime power must divide one factor: the only roots modulo $p^e$ are one and negative one. For powers of two, the answer differs. Modulo two there is one root, and modulo four there are two. For $e ≥ 3$, every root is odd, so the two even factors $x−1$ and $x+1$ are separated by two. Exactly one has two-valuation one and the other must be divisible by a power of two with exponent at least $e−1$. Thus a root satisfies $x ≡ 1$ or negative one modulo $2^{e−1}$. Lifting those two classes to modulus $2^e$ gives exactly four candidates: $1$, $−1$, $1+2^{e−1}$, and $−1+2^{e−1}$. They are distinct for $e ≥ 3$, and direct squaring verifies each, because both the cross term and the square of the added power are divisible by $2^e$.

Consequently, if a modulus has $r$ distinct odd prime divisors, its square-one root count is $2^r$ times its two-power contribution: one when the two-exponent is zero or one, two when it is two, and four when it is at least three. A modulus of one has its single automatic residue and is handled separately. The count comes from a bijection of local root choices, not merely from finding several examples. For instance, modulo seventy-two the factors eight and nine have four and two square-one roots, producing eight roots; repeated prime factors alone do not create extra choices in an odd prime-power coordinate.

Modulo an odd prime, $x^2 ≡ 1$ factors as $(x−1)(x+1) ≡ 0$. The prime-product lemma forces $x ≡ 1$ or negative one. For a product of distinct odd primes, choose a sign independently in each CRT coordinate, producing more than two roots. Thus a theorem about polynomial root counts over a field cannot be applied unchanged to a composite residue ring. For powers of two, odd squares are one modulo eight; higher-power root counts require separate reasoning rather than a prime-field argument.

For an integer $n ≥ 2$, Wilson's theorem says that $n$ is prime exactly when $(n−1)! ≡ −1 (mod n)$. For a prime, pair each nonzero residue with its inverse; only one and negative one are self-inverse, leaving product negative one. The prime two satisfies the statement directly. Conversely, if $n$ has a proper divisor $d$ with $1<d<n$, that divisor occurs in the factorial. The claimed congruence would force $d$ to divide negative one, impossible. Wilson is an exact mathematical criterion, but computing its enormous factorial product is not automatically an efficient primality test.

A Fermat witness with $a^{n−1} ≢ 1 (mod n)$ and $gcd(a,n)=1$ proves that $n$ is composite. Passing the congruence does not prove primality. For example, $341=11·31$ satisfies $2^{340} ≡ 1$ because $2^{10} ≡ 1$ modulo both factors. Distinguish primality testing from factorization: knowing that an integer is composite is not the same as obtaining its prime factors. Historical slides' claims about which practical algorithms exist are not used as current software guidance.

### Additive cycles and mathematical RSA

Repeated addition of a step $s$ modulo $n>0$ returns to its starting residue at the least positive $k$ satisfying $ks ≡ 0$. The linear-congruence theorem gives $k=n/gcd(s,n)$. Every cycle has this length, and there are $gcd(s,n)$ disjoint cycles. This proves how many separate index cycles an in-place array rotation must traverse; visiting just one cycle loses elements when the gcd exceeds one.

For distinct primes $p,q$, let $n=pq$ and choose positive exponents $e,d$ with $ed ≡ 1 (mod (p−1)(q−1))$. The transformation $x ↦ x^e mod n$ is reversed by raising to $d$ for **every** residue, including nonunits. To prove this, work modulo $p$. If $p ∣ x$, both $x^{ed}$ and $x$ are zero. Otherwise Fermat applies, and $p−1$ divides $ed−1$, giving equality. Repeat modulo $q$, then use CRT. Applying Euler directly modulo $n$ proves only the unit case and leaves a gap for messages sharing a prime factor. This is a mathematical illustration of exponentiation permutations; it does not provide production encryption, padding, key-size recommendations, or a proof of security.

## Fully explained problem bank

<!-- INCLUDE:problems -->

## Complete summary and examination rules

<!-- INCLUDE:review -->

## Interactive residue-map laboratory

Choose a modulus, coefficient, and target. The laboratory shows every residue's image under multiplication, all solutions, and an extended-Euclid certificate. It explicitly distinguishes an empty fiber, a many-element fiber, and a unit permutation. Moduli are restricted to two through sixty so the displayed table remains inspectable. All computations use exact integers within these limits. The displayed Bézout identity is checked by substitution before the solution report is produced.

<!-- LAB:number -->

## References and explicit limits

- Eric Lehman, F. Thomson Leighton, Albert R. Meyer. *Mathematics for Computer Science*, MIT, 2015. [Official reading page](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/). Chapter 8, selected sections on divisibility, gcd, remainder arithmetic, inverses, and cancellation. Exact PDF ranges are recorded in the source audit.
- Satish Rao, Koushik Sen. UC Berkeley CS 70, Spring 2022. [Note 6: Modular Arithmetic](https://www.sp22.eecs70.org/assets/pdf/notes/n6.pdf), all eleven pages. [Note 7: Public Key Cryptography](https://www.sp22.eecs70.org/assets/pdf/notes/n7.pdf), pages 2 and 4 for the mathematical RSA construction and CRT proof.
- Klaus Sutner. CMU MFCS 15-151, Fall 2022. [Modular Arithmetic](https://www.cs.cmu.edu/~sutner/pdf/60-modari.pdf), all seventy-two slides; proof details and algorithmic qualifications are supplied independently in this lesson.
- Marcelo Fiore. Cambridge Part IA Discrete Mathematics, 2022–23. [Proofs, Numbers, and Sets](https://www.cl.cam.ac.uk/teaching/2223/DiscMath/DiscMathProofsNumbersSetsNotes.pdf), PDF pages 123–143 and 151–182. [Official course materials](https://www.cl.cam.ac.uk/teaching/2223/DiscMath/materials.html).

The source audit records a bounded candidate comparison, actual reading scopes, selected course exercise adaptations, and reconciled conventions. It does not establish that every course worldwide was reviewed, reproduce entire exercise collections, or guarantee success on every unseen examination question. Independent finite checks supplement general proofs. This chapter has been approved by the student.
