## Eight deeper constructions: from a certificate to a complete solution set

### Construction 1. Linear congruences are fibers of a finite homomorphism

Fix a positive modulus $m$ and an integer coefficient $a$. Multiplication defines $T_a:\mathbb Z_m\to\mathbb Z_m$ by $T_a([x])=[ax]$. Changing $x$ by $km$ changes $ax$ by $akm$, so the map is well-defined. Addition is preserved. Write $d=\gcd(a,m)$, $a=da'$ and $m=dm'$. The kernel condition $m\mid ax$ is equivalent to $m'\mid a'x$, and coprimality makes it equivalent to $m'\mid x$. Thus the kernel has the $d$ elements $0,m',2m',\ldots,(d-1)m'$.

If $x_0$ solves $ax\equiv b\pmod m$, then another $x$ solves it exactly when $a(x-x_0)\equiv0$, so every nonempty fiber is the coset $x_0+\ker T_a$ and contains exactly $d$ residues. Existence is equivalent to $d\mid b$: necessity follows because $d$ divides both $a$ and $m$, and sufficiency follows by solving the reduced unit congruence $a'x\equiv b/d\pmod{m'}$. When $m'=1$, the reduced condition is automatic; no inverse computation is needed. Consequently the image has $m/d$ residues, namely the multiples of $d$. A gcd calculation determines multiplicity and image, while the target determines whether its fiber is empty.

For example, multiplication by twelve modulo thirty has kernel $\{0,5,10,15,20,25\}$. Its image is $\{0,6,12,18,24\}$. The fiber above eighteen is $\{4,9,14,19,24,29\}$. These three sets have different roles: the kernel is not the requested fiber, and the fiber count is not the image size. This construction explains why cancellation reduces a modulus and why interval counting is a later operation.

### Construction 2. Generalized CRT is a compatibility test plus a reversible merge

For positive moduli $m,n$, let $d=\gcd(m,n)$. A solution to $x\equiv r\pmod m$ and $x\equiv s\pmod n$ forces $d\mid s-r$. Conversely assume this divisibility and set $x=r+mt$. The second congruence becomes $mt\equiv s-r\pmod n$. Divide by $d$ to get a unit-coefficient equation modulo $n/d$, which determines one residue $t_0$ there. The complete solution set is
$$x=r+mt_0+\frac{mn}{d}k,\qquad k\in\mathbb Z.$$
Reduction of the first term modulo $mn/d$ gives the canonical representative. Differences of any two solutions are divisible by both moduli, hence by their lcm $mn/d$; this proves the smallest positive period. A product period is not minimal when $d>1$.

For many positive moduli $m_i$, consistency is equivalent to pairwise conditions $r_i\equiv r_j\pmod{\gcd(m_i,m_j)}$. Here is a proof of sufficiency, not just an algorithmic assertion. For each prime $p$ occurring in any modulus, choose an index with the largest $p$-exponent $e_p$. Specify the coordinate $x\equiv r_i\pmod{p^{e_p}}$ from that index. Pairwise compatibility ensures agreement with every other prescribed coordinate modulo its smaller power of $p$. Coordinates for distinct primes have coprime moduli; ordinary CRT combines them uniquely modulo $L=\prod_p p^{e_p}=\operatorname{lcm}(m_1,\ldots,m_k)$. The resulting residue satisfies each original condition, because it matches that condition at every prime-power factor. This also establishes uniqueness modulo $L$. Equal largest powers cause no ambiguity, since their targets agree at that full power.

### Construction 3. Orders and transient power tails require different contracts

For a unit $a$ modulo $m>1$, the least positive $t$ with $a^t\equiv1$ is its multiplicative order. Such a $t$ exists: the finite group of units makes two powers coincide, and cancellation gives a return to one. If $a^u\equiv a^v$, cancellation reduces this to a return at the exponent difference. Division of that difference by the least order proves it is a multiple of $t$. Euler supplies a valid period $\varphi(m)$, so the order divides the totient; equality is not required.

For a nonunit, factor $m=\prod p_i^{e_i}$. When $p_i\mid a\ne0$, the coordinate $a^k$ becomes zero modulo $p_i^{e_i}$ exactly when $k\,v_{p_i}(a)\ge e_i$. Its threshold is $\lceil e_i/v_{p_i}(a)\rceil$. When $p_i\nmid a$, the coordinate is a unit and its powers have an order. After all vanishing thresholds have been reached, the combined sequence is periodic with a period dividing the lcm of the unit-coordinate orders; CRT reconstructs each term. Before that threshold, a period of the tail cannot be used to change the exponent arbitrarily. The base zero has its own explicit contract: positive powers are zero, while the algorithmic exponent-zero identity is handled separately.

For $a=2,m=12$, the modulo-four component vanishes at exponent two, while the modulo-three component has order two. The full residues at exponents zero through five are $1,2,4,8,4,8$. The period-two tail starts at exponent two. Reducing exponent one hundred modulo four to zero returns one and is wrong. Reducing it to a sufficiently large exponent congruent modulo the tail period is justified. A power tower requires computing the outer exponent's residue and certifying any necessary lower bound, not pretending that a residue equals the original enormous integer.

### Construction 4. Quadratic roots expose composite-ring boundaries

For an odd prime $p$, $x^2\equiv1\pmod{p^e}$ means $p^e\mid(x-1)(x+1)$. The two factors differ by two, so $p$ cannot divide both. One factor therefore contains the entire $p^e$, giving exactly the roots $1,-1$. Modulo $2^e$, with $e\ge3$, a root must be odd. Of the consecutive even factors $x-1,x+1$, one has two-valuation exactly one and the other at least $e-1$. Thus $x\equiv1$ or $-1$ modulo $2^{e-1}$; each has two lifts modulo $2^e$. The four roots are $1,-1,1+2^{e-1},-1+2^{e-1}$. Direct multiplication checks sufficiency. For $e=1,2$, there are respectively one and two roots; the four-root formula must not be used without its range.

CRT multiplies independent root choices across distinct prime powers. For $m=2^e\prod_{i=1}^r p_i^{f_i}$ with odd distinct primes, the count of roots of one is $2^r$ times the applicable power-of-two count. It need not be two, and a degree-two polynomial over a ring with zero divisors need not have at most two roots.

For $x^k\equiv0\pmod m$ with positive $k$, let $D=\prod_i p_i^{\lceil e_i/k\rceil}$. Nonzero $x$ satisfies the congruence exactly when $D\mid x$, by comparing valuations. Zero also satisfies it directly. Since $D\mid m$, there are exactly $m/D$ solution residues. This is a complete classification and includes zero without assigning it an ordinary finite prime valuation.

### Construction 5. Valuations convert arithmetic questions into coordinate inequalities

For nonzero integers, $v_p(uv)=v_p(u)+v_p(v)$. If $u,v$ are nonzero and $v_p(u)\ne v_p(v)$, then $v_p(u+v)=\min(v_p(u),v_p(v))$: factor out the smaller power, leaving a sum with exactly one term divisible by $p$. If the valuations are equal, only a lower bound is guaranteed; cancellation can raise the valuation or yield zero. For instance $v_2(4)=v_2(12)=2$, but $v_2(4+12)=4$. Apply an exact-minimum rule only after checking its unequal-valuation premise.

The factorial formula counts $p$-layers: $v_p(n!)=\sum_{j\ge1}\lfloor n/p^j\rfloor$. Integer factorial quotients give exact subtraction, so
$$v_p\binom nk=v_p(n!)-v_p(k!)-v_p((n-k)!),\qquad 0\le k\le n.$$
This cancellation takes place in integers, where the binomial coefficient is an integer, not inside a ring where denominators may lack inverses. For a positive base $B=\prod p_i^{a_i}$, the number of trailing base-$B$ zeros of a nonzero $N$ is $\min_i\lfloor v_{p_i}(N)/a_i\rfloor$. Divisor counts use permitted exponent choices instead; confusing a resource minimum with a product of independent choices answers a different question.

### Construction 6. Modular obstructions and existence need separate proofs

Reducing an equation modulo a small integer can rule out solutions, but passing the test may not prove an integer solution exists. For an integer-coefficient polynomial $P$, $x\equiv r\pmod m$ implies $P(x)\equiv P(r)\pmod m$ by repeated use of compatible addition and multiplication. If none of the $m$ residue values is zero, there is no integer root. If a residue is zero, it is only a candidate coordinate. For example $x^2=3$ has no integer solution even though modulo two both sides can be one at odd $x$.

For Laurent coefficient extraction, a different exact sufficiency argument is available. In $(x^a+x^{-b})^N$ with positive $a,b$ and nonnegative $N$, choosing $j$ positive-power factors gives exponent $(a+b)j-bN$. Thus the coefficient of $x^t$ is $\binom Nj$ when $j=(t+bN)/(a+b)$ is an integer in $[0,N]$, and zero otherwise. The chosen factors construct the term, so integrality plus range are sufficient here. If coefficients are not both one or more than two exponent choices occur, multiplicities and possible cancellation need separate treatment.

### Construction 7. Small representatives must be reduced correctly in a minimality proof

Suppose $\gcd(a,m)=1$ with $m>1$. Bezout supplies an inverse, but another proof uses a smallest positive remainder of a positive multiple of $a$. Let this smallest remainder be $b$, with $0<b<m$. Divide $m=qb+r$, $0\le r<b$. Since $b\equiv ka\pmod m$, the number $r=m-qb$ is also congruent to a multiple of $a$. A positive $r$ would contradict minimality, so $b\mid m$. Next divide $a=tb+c$, $0\le c<b$. The remainder $c$ is likewise a multiple of $a$ modulo $m$, because $b$ is such a multiple; minimality forces $c=0$. Thus $b$ divides both $a$ and $m$, and coprimality gives $b=1$.

The existence of a nonzero multiple remainder is immediate from $a\not\equiv0\pmod m$, and negative multiplier representatives can be replaced by nonnegative ones modulo $m$. If instead a proof starts from a value in the interval $(pm,(p+1)m)$, its smaller canonical representative is the difference after subtracting $pm$, not that original value. Carrying the unreduced variable into a claim that it is less than $m$ is a genuine proof error. This reconciliation makes the CMU minimal-positive-representative argument explicit and correctly scoped.

### Construction 8. Extended Euclid and modular power have auditable implementation states

For signed inputs $a,b$, run Euclid on their absolute values and track coefficients against the signed original pair. Start remainder rows as $(|a|,\operatorname{sgn}(a),0)$ and $(|b|,0,\operatorname{sgn}(b))$, using sign zero at input zero. In one guarded iteration with second remainder $r_1>0$, set $q=\lfloor r_0/r_1\rfloor$ and update all rows simultaneously:
$$ (r_0,r_1)\gets(r_1,r_0-qr_1),\quad(s_0,s_1)\gets(s_1,s_0-qs_1),\quad(t_0,t_1)\gets(t_1,t_0-qt_1). $$
The exact identities $r_i=s_i a+t_i b$ hold at every checkpoint. Remainders descend until the second is zero; the first is the nonnegative gcd, and its coefficients give a Bezout certificate. At $(0,0)$, the computational gcd is zero and the identities hold without claiming a greatest positive common divisor exists.

For modular powering, use positive $m$, nonnegative exponent $e$, initial result $1\bmod m$ and reduced base $a\bmod m$. The loop invariant is $result\cdot base^{left}\equiv a^e\pmod m$. If $left$ is odd, multiply the result by the old base. Then square that base and halve $left$ by floor, using the old values in the derivation. Even and odd cases both preserve the invariant. The nonnegative exponent strictly descends when positive. At zero, the result equals the target residue. If every iteration squares, exponent thirteen costs four squarings plus three accumulator products; an implementation omitting the last unused square costs one fewer. For modulus one, the canonical result is always zero, including exponent zero. Primitive multiplication count, division count and bit complexity must be declared separately; fixed-width overflow can destroy an otherwise correct mathematical algorithm.

### Sources for these constructions

- MIT, 6.042J, Spring 2015, Eric Lehman, F. Thomson Leighton and Albert R. Meyer: [Number Theory, printed pages 243–252](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf).
- UC Berkeley, CS70, Fall 2026, course-authored [Note 6](https://www.eecs70.org/assets/pdf/notes/n6.pdf) and [Note 7](https://www.eecs70.org/assets/pdf/notes/n7.pdf).
- Carnegie Mellon, Klaus Sutner, MFCS Fall 2022: [Modular Arithmetic, all 72 slides](https://www.cs.cmu.edu/~sutner/pdf/60-modari.pdf).
- Cambridge, Marcelo Fiore, Part IA Discrete Mathematics 2022–23: [Proofs, Numbers and Sets, physical pages 123–143 and 151–182](https://www.cl.cam.ac.uk/teaching/2223/DiscMath/DiscMathProofsNumbersSetsNotes.pdf).

The constructions are independently written proofs and synthesis, not quotations. The source audit separates fresh scopes from earlier wider readings; no complete worldwide-course census or reproduction of every course exercise is claimed.
