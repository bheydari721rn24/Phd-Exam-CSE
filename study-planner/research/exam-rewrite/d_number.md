## Teaching through formulas and conceptual decisions

### Solve linear congruences with a gcd before canceling

For$ax\equiv b\pmod m$ with$m>0$, set$d=\gcd(a,m)$. There are no solutions if$d$ does not divide$b$. Otherwise divide$a,b,m$ by$d$; the reduced coefficient is invertible modulo$m/d$. One solution modulo$m/d$ lifts to exactly$d$ distinct residues modulo$m$, spaced$m/d$ apart. Canceling$a$ while keeping the old modulus is generally false.

For example,$6x\equiv8\pmod{14}$ reduces to$3x\equiv4\pmod7$. The inverse of3 is5, so$x\equiv20\equiv6\pmod7$, giving$x=6,13$ modulo14. The gcd predicts both solvability and the exact number of answers before any inverse is calculated.

### Compatibility precedes Chinese-remainder construction

The system$x\equiv a\pmod m$, $x\equiv b\pmod n$ is solvable exactly when$a\equiv b\pmod{\gcd(m,n)}$. If solvable, it has one residue class modulo$\operatorname{lcm}(m,n)$, not necessarily modulo$mn$. Coprime moduli make every pair compatible and give the familiar product modulus. Substitution$x=a+mt$ reduces the construction to a linear congruence in$t$.

### Prime exponents are a reusable accounting language

If$N=\prod p_i^{e_i}$, divisor count is$\prod(e_i+1)$ and divisor sum is$\prod(1+p_i+\cdots+p_i^{e_i})$. Gcd takes minimum exponents and lcm maximum exponents. In$n!$, the exponent of prime$p$ is $\sum_{j\ge1}\lfloor n/p^j\rfloor$; later terms count numbers contributing more than one factor$p$. Totient is$N\prod_{p\mid N}(1-1/p)$, based on exclusion of multiples of distinct prime divisors.

### Reduce exponents only for units under the theorem used

Euler gives$a^{\phi(m)}\equiv1\pmod m$ when$\gcd(a,m)=1$. For nonunits, residues can have a transient before cycling, so reducing an exponent modulo$\phi(m)$ can fail. An inverse exists exactly for units. Repeated squaring computes powers without an invalid theorem assumption; order gives the exact unit period and divides the totient.

## Formula and conceptual problem bank

### Question 1. Euclidean remainder of a negative integer

Under$-17=5q+r$ with$0\le r<5$, what are$q,r$?

**A.** (-3,-2)

**B.** (-4,3)

**C.** (-3,2)

**D.** (-4,2)

**Answer: B.**

Euclidean remainder must be nonnegative. Taking$q=-4$ yields$-20+3=-17$, so$r=3$. The pair(-3,-2) follows truncating division but violates the required remainder interval. The equation and interval together uniquely determine the pair.

### Question 2. Gcd and lcm

For$a=72$ and$b=90$, what are their gcd and lcm?

**A.** (9,720)

**B.** (18,360)

**C.** (18,180)

**D.** (36,180)

**Answer: B.**

Prime exponents are$72=2^3 3^2$ and$90=2\cdot3^2\cdot5$. Minima give$2\cdot3^2=18$; maxima give$2^3\cdot3^2\cdot5=360$. The identity$\gcd(a,b)\operatorname{lcm}(a,b)=ab$ checks$18\cdot360=6480$. Option A underestimates the common power of three. Option C omits a factor of two from the lcm. Option D gives a supposed gcd that does not divide 90.

### Question 3. Linear congruence count

How many residues modulo14 solve$6x\equiv8\pmod{14}$?

**A.** 0

**B.** 1

**C.** 2

**D.** 6

**Answer: C.**

The gcd of6 and14 is2, which divides8, so exactly two residues solve it. Reducing gives$3x\equiv4\pmod7$, hence$x\equiv6\pmod7$ and the lifted residues6,13. Substitution gives36 and78, both congruent to8 modulo14.

### Question 4. Inconsistent linear congruence

How many residues modulo14 solve$6x\equiv5\pmod{14}$?

**A.** 0

**B.** 1

**C.** 2

**D.** 7

**Answer: A.**

Every multiple of6 is even, and subtracting a multiple of14 preserves parity. It cannot become congruent to odd5. Equivalently the gcd2 does not divide5, so the linear-congruence solvability criterion fails. Trying to invert6 modulo14 is itself invalid because it is not a unit.

### Question 5. A modular inverse

What is the inverse of7 modulo26?

**A.** 3

**B.** 7

**C.** 15

**D.** 19

**Answer: C.**

$7\cdot15=105=4\cdot26+1$, so15 is an inverse. The gcd is1, guaranteeing a unique inverse residue. The other candidates yield remainders21,23 and3. A Bézout computation would supply the same coefficient without searching all residues.

### Question 6. Cancellation changes modulus

From$6x\equiv6y\pmod{15}$, which strongest listed congruence must follow?

**A.** $x\equiv y\pmod{15}$

**B.** $x\equiv y\pmod5$

**C.** $x\equiv y\pmod3$

**D.** $x=y$ as integers.

**Answer: B.**

The condition is$15\mid6(x-y)$. Divide the gcd3 to obtain$5\mid2(x-y)$. Since2 is invertible modulo5, this is$x\equiv y\pmod5$. The old modulus15 cannot be retained: $x=0,y=5$ is a counterexample. The modulus is divided by the common gcd, not by the entire coefficient.

### Question 7. Coprime Chinese remainders

Find the residue modulo15 satisfying$x\equiv2\pmod3$ and$x\equiv3\pmod5$.

**A.** 2

**B.** 3

**C.** 8

**D.** 13

**Answer: C.**

Candidates congruent to3 modulo5 are3,8,13. Only8 has remainder2 modulo3. The moduli are coprime, so this is the unique residue modulo15. Substitution$x=3+5t$ gives$2t\equiv2\pmod3$, hence$t\equiv1$.

### Question 8. Noncoprime compatibility

Which system is inconsistent?

**A.** $x\equiv1\pmod4, x\equiv3\pmod6$

**B.** $x\equiv0\pmod4, x\equiv2\pmod6$

**C.** $x\equiv1\pmod4, x\equiv2\pmod6$

**D.** $x\equiv3\pmod4, x\equiv5\pmod6$

**Answer: C.**

The gcd of4 and6 is2. The residues must therefore agree in parity. OptionC requests both odd and even$x$, impossible. The other residue pairs have matching parity and are compatible. Their solution period is lcm12 rather than the product24.

### Question 9. Totient

What is$\phi(60)$?

**A.** 12

**B.** 16

**C.** 20

**D.** 24

**Answer: B.**

The distinct prime divisors are2,3,5. Apply $60(1-1/2)(1-1/3)(1-1/5)=60\cdot(1/2)(2/3)(4/5)=16$. Repeated powers of a prime do not add repeated product factors. Totient counts unit residue classes, not all proper divisors.

### Question 10. Exponent reduction for a unit

What is$7^{100}\bmod13$?

**A.** 1

**B.** 3

**C.** 9

**D.** 12

**Answer: C.**

Since7 is a unit modulo13, reduce100 modulo12 to4. Compute$7^2\equiv49\equiv10$ and$7^4\equiv100\equiv9$. Euler’s theorem applies because13 is prime and does not divide7. Reducing the base or exponent before checking that condition can fail for nonunits.

### Question 11. A nonunit exponent trap

What is$2^4\bmod8$?

**A.** 0

**B.** 1

**C.** 2

**D.** 4

**Answer: A.**

The exact power16 is divisible by8, giving0. Although$\phi(8)=4$, reducing exponent4 to0 would give1 and is invalid because$\gcd(2,8)=2$. Nonunit powers here eventually reach0 rather than follow the unit-group period from exponent zero.

### Question 12. Divisor count

How many positive divisors does$360$ have?

**A.** 18

**B.** 20

**C.** 24

**D.** 36

**Answer: C.**

$360=2^3 3^2 5^1$. Choose each divisor exponent independently from0 through its corresponding exponent, giving$(3+1)(2+1)(1+1)=24$. Summing exponents counts factor multiplicities, not combinations of divisor exponents. The divisor1 and360 itself are included.

### Question 13. Factorial valuation

What is the exponent of2 in$10!$?

**A.** 5

**B.** 7

**C.** 8

**D.** 10

**Answer: C.**

Legendre’s sum is $\lfloor10/2\rfloor+\lfloor10/4\rfloor+\lfloor10/8\rfloor=5+2+1=8$. The first term counts all even factors, and later terms add the extra twos in multiples of4 and8. Counting only even numbers undercounts repeated factors.

### Question 14. Bézout and integer equations

For which integer$c$ can$12x+18y=c$ have integer solutions?

**A.** Every integer$c$.

**B.** Exactly multiples of3.

**C.** Exactly multiples of6.

**D.** Exactly positive multiples of12.

**Answer: C.**

The gcd is6, so every left-hand value is divisible by6. Bézout gives$6=-12+18$, and multiplying that solution by any integer$t$ produces every$c=6t$. Positive and negative coefficients are permitted. Restricting$x,y$ to nonnegative integers would add constraints not present here.

### Question 15. Number of units

How many invertible residue classes exist modulo18?

**A.** 3

**B.** 6

**C.** 9

**D.** 12

**Answer: B.**

$\phi(18)=18(1-1/2)(1-1/3)=6$. They are1,5,7,11,13,17. Invertibility is equivalent to gcd1 with the modulus. Nonzero residues such as2 and3 can still lack inverses, so counting all seventeen nonzero classes would be wrong.

### Question 16. Multiplicative order

What is the multiplicative order of2 modulo7?

**A.** 2

**B.** 3

**C.** 6

**D.** 7

**Answer: B.**

The powers are2,4,1 modulo7, so the first positive exponent returning1 is3. The order divides$\phi(7)=6$ but need not equal it. Euler gives an exponent that works, while order asks for the least positive such exponent.

<!-- CHALLENGE-BANK -->

### Question 17. Challenge: Congruence solutions in an interval

How many integers$0\le x\le100$ solve$6x\equiv8\pmod{14}$?

**A.** 7

**B.** 13

**C.** 14

**D.** 15

**Answer: C.**

Reduce the congruence to$x\equiv6\pmod7$. The interval solutions are$x=6+7t$ with integer$t\ge0$ and$t\le\lfloor(100-6)/7\rfloor=13$. Thus there are14 values. The two-residues-per14 statement is compatible but does not by itself count a partially filled final interval. Apply floor endpoints after finding the reduced progression.

### Question 18. Challenge: Compatible shared-modulus reconstruction

What is the least nonnegative$x$ satisfying$x\equiv5\pmod{12}$ and$x\equiv11\pmod{18}$?

**A.** 11

**B.** 17

**C.** 29

**D.** 35

**Answer: C.**

The gcd6 compatibility test passes because5 and11 have equal residues modulo6. Put$x=5+12t$; then$12t\equiv6\pmod{18}$. Divide6 to get$2t\equiv1\pmod3$, so$t\equiv2\pmod3$. Therefore$x\equiv29\pmod{36}$ and29 is the least nonnegative solution. The lcm36, not product216, is the fundamental period.

## Applicable formulas and examination notes

### 1. Euclidean interval

For positive$m$, divide$n=qm+r$ with$0\le r<m$. Negative$n$ may require a quotient below truncation-toward-zero. For$-17$ and5 the answer is$q=-4,r=3$.

### 2. Gcd and lcm exponents

Gcd takes minimum prime exponents and lcm maximum exponents. For nonzero integers, their positive product is$|ab|$. Handle the zero pair by the chapter’s stated gcd convention before using an lcm formula with division.

### 3. Linear solvability

$ax\equiv b\pmod m$ is solvable iff$d=\gcd(a,m)$ divides$b$. If so, there are$d$ residues modulo$m$. Reduce by$d$ and lift by multiples of$m/d$; do not search for an inverse of a nonunit.

### 4. Cancellation modulus

$ax\equiv ay\pmod m$ yields$x\equiv y\pmod{m/\gcd(a,m)}$. For$a=6,m=15$, the reduced modulus is5. Keeping15 assumes an inverse that does not exist.

### 5. Inverse check

A modular inverse exists exactly when gcd is1. Verify a candidate by multiplying and obtaining residue1. Bézout supplies the inverse coefficient, which may be negative before conversion to the canonical residue.

### 6. CRT compatibility

Two residue requirements agree iff their residues agree modulo the gcd of their moduli. Compatible solutions repeat modulo the lcm. Coprimality is sufficient for automatic compatibility but is not necessary for a particular system.

### 7. Diophantine family

For$ax+by=c$ and$d=\gcd(a,b)$ dividing$c$, a particular solution generates$x=x_0+(b/d)t$, $y=y_0-(a/d)t$. Nonnegative restrictions become an interval of allowed$t$ values and may remove all integer solutions.

### 8. Totient factors

$\phi(N)=N\prod_{p\mid N}(1-1/p)$ uses each distinct prime once.60 gives16. The result counts residues coprime to$N$, including1, not a count of divisors or arbitrary nonzero residues.

### 9. Safe power reduction

Euler exponent reduction requires gcd1. For$7^{100}$ modulo13, reduce100 to4 and get9. For$2^4$ modulo8, reducing exponent to0 gives a false answer. Use repeated squaring when group conditions are absent.

### 10. Order versus totient

The unit order is the least positive exponent returning1 and divides the totient.2 modulo7 has order3 although the totient is6. A proper divisor must be checked to establish minimality.

### 11. Divisor formulas

If$N=\prod p_i^{e_i}$, count divisors with$\prod(e_i+1)$ and sum them with$\prod(1+p_i+\cdots+p_i^{e_i})$. Include zero exponents in each choice. Square divisors restrict every selected exponent to be even.

### 12. Factorial prime valuation

$v_p(n!)=\sum_{j\ge1}\lfloor n/p^j\rfloor$. For$p=2,n=10$, the terms5,2,1 sum to8. Trailing decimal zeros use the minimum of2- and5-valuations; counting only multiples of5 can miss powers of25.

### 13. Wilson direction

For prime$p$, $(p-1)!\equiv-1\pmod p$; conversely this condition characterizes primes among integers greater than1. Pair units with inverses in the proof and handle the self-inverse residues separately. A Fermat congruence for one base is not an equivalent primality test.

### 14. RSA mathematical scope

For distinct primes$p,q$, choose exponent$e$ invertible modulo$\phi(pq)$ and its inverse$d$. Correctness on units follows from Euler and on nonunits from separate prime-modulus cases. This arithmetic teaching does not certify a cryptographic implementation’s security.

<!-- BOUNDARY-NOTES -->

### 15. Nonnegative Diophantine bounds

After finding $x=x_0+(b/d)t$ and $y=y_0-(a/d)t$, solve both nonnegative inequalities for integer $t$. Their intersection can be empty even when the gcd criterion permits unrestricted integer solutions. Count allowed integers with floor and ceiling endpoints.

### 16. Prime evidence boundaries

A composite can satisfy a Fermat congruence for one base, so that congruence alone is not a primality proof. Wilson's equivalence has a stronger assumption-and-conclusion structure but can be computationally expensive. Do not interchange a screening test and a certificate.

### 17. Additive modular cycles

Adding $a$ modulo $m$ from zero reaches exactly $m/\gcd(a,m)$ residues and returns after that many steps. Multiplicative order applies only to units and is a different orbit formula. Shared terminology about cycles does not make their counts interchangeable.
