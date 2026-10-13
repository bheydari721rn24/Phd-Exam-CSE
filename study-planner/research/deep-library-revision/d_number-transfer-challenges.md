## Ten solved transfer challenges

### Challenge 1. Two coefficient equations and a signed interval

**Problem.** Find every integer $x$ in $[-100,100]$ satisfying $18x\equiv30\pmod{42}$ and $10x\equiv20\pmod{30}$. Count them, proving that no others exist.

**Solution.** The first gcd is six and divides thirty. Reduction gives $3x\equiv5\pmod7$, so $x\equiv4\pmod7$ by inverse five. The second gcd is ten and reduction gives $x\equiv2\pmod3$. Write $x=4+7t$. Modulo three this gives $1+t\equiv2$, hence $t\equiv1\pmod3$ and $x=11+21k$. Every reduction was reversible; the period twenty-one belongs to the reduced conditions, not the product of forty-two and thirty.

The interval gives $k\ge\lceil-111/21\rceil=-5$ and $k\le\lfloor89/21\rfloor=4$. Thus there are ten values: $-94,-73,-52,-31,-10,11,32,53,74,95$. The two original left sides at eleven are 198 and 110, whose remainders are thirty and twenty. Adding twenty-one changes them by multiples of their moduli. This verifies every listed member and, with the parameter proof, completeness. A truncation-toward-zero quotient for the negative lower endpoint would miss negative solutions; use the mathematical ceiling.

### Challenge 2. Three overlapping schedules with an incompatible perturbation

**Problem.** Solve $x\equiv1\pmod4$, $x\equiv3\pmod6$, $x\equiv9\pmod{10}$. Count solutions in $[0,500]$. Explain what changes if the last target is eight.

**Solution.** All pairwise gcds are two, and the three targets are odd, so compatibility holds. Put $x=1+4t$. The second condition gives $4t\equiv2\pmod6$, or $2t\equiv1\pmod3$, hence $t\equiv2\pmod3$ and $x\equiv9\pmod{12}$. Write $x=9+12u$. The last condition gives $12u\equiv0\pmod{10}$, hence $u\equiv0\pmod5$. Therefore $x=9+60k$ and the period is $\operatorname{lcm}(4,6,10)=60$.

In the stated interval $k=0$ through eight, giving nine solutions and final one 489. If the last target becomes eight, its even parity conflicts with the first target's odd parity modulo their shared gcd two. No solution exists. The compatibility failure is sufficient to reject that perturbed system; an unsuccessful search is not needed. For the consistent system, the lcm period and parameter bounds make the finite count exact.

### Challenge 3. A mixed unit and vanishing-coordinate power

**Problem.** Compute $18^{60}\bmod1000$ without expanding the integer power.

**Solution.** Factor $1000=8\cdot125$. The base has two-valuation one, so exponent sixty makes its modulo-eight coordinate zero. Modulo 125 the base is a unit. Successive squares have residues $74,101,76,26,51$ at exponents $2,4,8,16,32$. For example $74^2=5476\equiv101$ and $26^2=676\equiv51$. Since $60=32+16+8+4$, multiplication gives $51\cdot26\equiv76$, then $76\cdot76\equiv26$, then $26\cdot101\equiv1$ modulo 125.

Reconstruct $x=1+125t$. Modulo eight the condition is $1+5t\equiv0$, hence $t\equiv3\pmod8$. Thus $x\equiv376\pmod{1000}$; it is already canonical. Direct coordinate checks give $376\bmod8=0$ and $376\bmod125=1$. The original base is not a unit modulo one thousand, so a global Euler reduction is not a valid proof. Valuation handles the nonunit component, repeated squaring handles the unit component, and CRT certifies the final answer.

### Challenge 4. A nonunit power tower with a threshold proof

**Problem.** Compute $2^{(2^{20})}\bmod72$, making the exponent contract explicit.

**Solution.** Split $72=8\cdot9$. The actual outer exponent is at least three, so the modulo-eight coordinate vanishes. Modulo nine, two is a unit of order six: $2^1,2^2,2^3,2^4,2^5,2^6$ give $2,4,8,7,5,1$. The inner power $2^{20}$ has remainder four modulo six, because positive powers of two there alternate two and four, and twenty is even. Thus the modulo-nine coordinate is $2^4\equiv7$.

Write $x=8t$. The second coordinate gives $-t\equiv7\pmod9$, so $t\equiv2$ and $x\equiv16\pmod{72}$. This is the canonical answer. The inner exponent was reduced only for the unit modulo-nine component; the vanishing modulo-eight component used its true lower bound. Right association is part of the problem: $(2^2)^{20}$ has exponent forty and is a different power. A tower can be solved from a residue and a size certificate without ever storing the tower's enormous value.

### Challenge 5. All roots of one across three prime-power coordinates

**Problem.** Count and list every solution to $x^2\equiv1\pmod{360}$.

**Solution.** Factor $360=8\cdot9\cdot5$. Modulo eight the four roots are $1,3,5,7$. Modulo nine the two roots are $1,8$, and modulo five the roots are $1,4$. Thus there are exactly $4\cdot2\cdot2=16$ roots by CRT. First combine the modulo-nine and modulo-five signs: the four roots modulo forty-five are $1,19,26,44$. For example nineteen has coordinates one modulo nine and four modulo five.

Each root modulo forty-five has eight lifts modulo 360, differing by forty-five. A lift squares to one modulo eight precisely when it is odd, and exactly four of those lifts are odd because forty-five is odd. The full sorted list is
$$1,19,71,89,91,109,161,179,181,199,251,269,271,289,341,359.$$
They are grouped before sorting as $1,91,181,271$; $19,109,199,289$; $71,161,251,341$; and $89,179,269,359$. Every listed number has one of the valid coordinates at all three factors, and every possible coordinate tuple has one unique lift. This proves both correctness and completeness. The assertion that a quadratic can have only two roots applies to fields, not this composite ring.

### Challenge 6. Nilpotent residues and an exact solution count

**Problem.** Solve $x^3\equiv0\pmod{2160}$ and count its residue solutions.

**Solution.** The factorization is $2160=2^4\cdot3^3\cdot5$. For a nonzero $x$, divisibility of its cube requires $3v_2(x)\ge4$, $3v_3(x)\ge3$ and $3v_5(x)\ge1$. Hence $x$ must be divisible by $2^2\cdot3\cdot5=60$. Conversely if sixty divides $x$, the cube is divisible by $60^3$, which contains all required prime powers. Zero is checked directly.

The complete residues are $x=60t$ for $t=0,1,\ldots,35$, since $2160/60=36$. Thus there are thirty-six, with last representative 2100. A count using $2160\mid x$ would retain only zero and miss thirty-five nonzero nilpotent residues. A count using merely $30\mid x$ would allow two-valuation one and fail the cube's two-power requirement. The ceiling $\lceil e/3\rceil$ comes from an integer inequality, not rounding to the nearest integer.

### Challenge 7. A factorial quotient and a composite divisibility bottleneck

**Problem.** Find the largest $k$ for which $12^k$ divides $\binom{30}{12}$.

**Solution.** Calculate valuations by subtracting factorial valuations. For two, $v_2(30!)=26$, $v_2(12!)=6+3+1=10$, and $v_2(18!)=9+4+2+1=16$, giving $v_2\binom{30}{12}=0$. For three, the corresponding values are $14$, $4+1=5$ and $6+2=8$, giving three-valuation one. Thus the coefficient is odd, though divisible by three.

Each positive power of twelve requires two factors of two. No such power can divide this coefficient, so $k=\min(\lfloor0/2\rfloor,1)=0$. This is not a failure of the factorial-valuation method: the subtraction shows that all twos in the numerator cancel exactly. The general prime valuations of an integer binomial coefficient are nonnegative; a negative result would reveal an arithmetic mistake. Computing only the supply in $30!$ would solve a different problem and falsely predict a large exponent.

### Challenge 8. Square divisors that satisfy a further exponent condition

**Problem.** How many square divisors of $2^{10}3^{11}5^2$ are divisible by thirty-six but not by twenty-five?

**Solution.** A square divisor has even exponents. Divisibility by $36=2^2 3^2$ requires the two- and three-exponents to be at least two. Their allowed values are respectively $2,4,6,8,10$ and $2,4,6,8,10$, five choices each. The five-exponent is either zero or two; excluding divisibility by twenty-five forces it to be zero. Therefore the exact count is $5\cdot5\cdot1=25$.

The unrestricted square-divisor count would be seventy-two, but imposing both lower bounds removes exponent-zero choices in two coordinates and the exclusion removes the positive five choice. Each permitted triple produces a unique positive divisor, so the product count neither misses nor duplicates any. Counting exponents at least one would violate the square requirement, while excluding the prime five alone happens to be equivalent here only because the allowed square exponent choices are zero and two. A different upper bound could make those conditions distinct.

### Challenge 9. When a compatible residue is not yet an integer root

**Problem.** Explain why the congruences $x^2\equiv3\pmod2$ and $x^2\equiv3\pmod7$ do not together certify an integer solution of $x^2=3$. Use a sound obstruction or inequality to settle the equation.

**Solution.** The first congruence permits odd $x$. The second has no solution: square residues modulo seven are $0,1,2,4$, obtained by squaring representatives zero through six. Thus the stated pair is already inconsistent as a root requirement, and the modulo-seven obstruction proves no integer root. If only the modulo-two test had been used, its passing result would supply no existence proof.

There is also a direct integer argument. A nonnegative integer whose square is three would lie strictly between one and two, since $1^2<3<2^2$. No integer does; negative roots have the same squares as their absolute values. These two independent proofs distinguish a necessary modular condition from a construction of an integer root. Even simultaneous passing tests at selected moduli may be insufficient in other equations; the burden of existence is a separate proof, not an inference from a finite list of failed obstruction attempts.

### Challenge 10. Recovering all RSA messages includes zero coordinates

**Problem.** For distinct primes five and eleven, modulus fifty-five, public exponent three and private exponent twenty-seven, prove decryption recovers every residue, and work through message five.

**Solution.** The exponent product is $3\cdot27=81=1+2\cdot40$, with $40=(5-1)(11-1)$. For any residue $x$, modulo five either $x=0$ and all positive powers remain zero, or $x$ is a unit and Fermat gives $x^{80}=1$; in both cases $x^{81}\equiv x$. Modulo eleven the same argument uses exponent period ten. CRT then gives $x^{81}\equiv x\pmod{55}$ for every residue, including zero and nonunits.

For message five, encryption gives $5^3=125\equiv15\pmod{55}$. Decrypting fifteen gives $15^{27}\equiv5\pmod{55}$. A coordinate check has zero modulo five; modulo eleven, fifteen is four and $4^{27}\equiv4^7\equiv5\pmod{11}$, using successive residues $4^2\equiv5\pmod{11}$, $4^4\equiv3\pmod{11}$ and $3\cdot5\cdot4\equiv5\pmod{11}$. Of the multiples of five modulo fifty-five, only five has modulo-eleven residue five. Direct Euler at modulus fifty-five would be invalid for this message because its gcd is five. This proof establishes arithmetic correctness of a teaching example, not cryptographic security or recommended practical parameters.
