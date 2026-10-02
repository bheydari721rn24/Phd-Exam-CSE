### Problem 1. Distinguish divisibility from division

**Original · Domain audit.** Decide whether zero divides zero, whether zero divides a nonzero integer, and whether integer divisibility is antisymmetric.

**Solution.** The witness zero proves $0=0·0$, so zero divides zero. Every product with zero is zero, so a nonzero target has no witness. Neither assertion defines division by zero. Antisymmetry fails on all integers because $3 ∣ −3$ and $−3 ∣ 3$ but the integers differ. On nonnegative integers, if exactly one number is zero, mutual divisibility is impossible; if both are positive, mutually dividing quotients are positive integers with product one, so both quotients equal one. If both are zero, equality is immediate. Thus divisibility is a partial order on nonnegative integers, even though its greatest element there is numerically the smallest integer.

### Problem 2. Find a negative dividend's unique representation

**Original · Division theorem.** Divide negative seventeen by five using a nonnegative remainder, and diagnose quotient negative three.

**Solution.** Flooring $−17/5=−3.4$ gives $q=−4$ and $r=−17−(−4)5=3$. These values satisfy both the product equation and $0 ≤ r<5$. Choosing negative three instead forces remainder negative two, which violates the specified interval. Uniqueness is not a matter of choosing the more familiar sign: any two valid remainders differ by a multiple of five and have absolute difference below five, forcing difference zero. This also explains why reading a programming-language remainder without inspecting its signed convention can yield a wrong mathematical answer.

### Problem 3. A common divisor without factorization

**Original · Linear combinations.** Find $gcd(3n+2,5n+3)$ for every nonnegative integer $n$.

**Solution.** A common divisor divides $5(3n+2)−3(5n+3)=1$. Hence it is one, and the gcd is always one. The displayed equality is itself a Bézout certificate, with coefficients five and negative three. It proves the result for every allowed input without factoring either expression or running Euclid separately. Do not replace the certificate by an unsupported assertion that adjacent-looking expressions are coprime; many similar-looking pairs share a factor. The conclusion also extends to all integer inputs after sign normalization because the same identity is valid.

### Problem 4. Read an extended-Euclid trace

**Course-derived · Berkeley Note 6, page 8 inverse exercise, independently explained.** Compute the inverse of twelve modulo thirty-five.

**Solution.** The divisions are $35=2·12+11$ and $12=1·11+1$, so the gcd is one. Substitute the first into the second: $1=12−11=12−(35−2·12)=3·12−35$. Reducing this ordinary integer identity modulo thirty-five gives $3·12 ≡ 1$, so the inverse is three. Substitution checks $36 mod 35=1$. Uniqueness is a residue-class statement: three plus any multiple of thirty-five is also an integer inverse witness, but exactly three is the canonical representative. The Bézout coefficients are not modular quotients; they are signed integer coefficients in an exact identity.

### Problem 5. A larger Bézout certificate

**Original · Extended Euclid.** Find the gcd of 252 and 198 and express it as a linear combination.

**Solution.** Divide successively: $252=198+54$, $198=3·54+36$, and $54=36+18$, followed by $36=2·18$. The gcd is eighteen. Back-substitute: $18=54−36=54−(198−3·54)=4·54−198=4·252−5·198$. The certificate checks as $1008−990=18$. Every common divisor divides this combination, and eighteen divides both original inputs, so the identity establishes the gcd without relying on the trace being trusted. For input negative 252 and positive 198, change the first coefficient to negative four; the gcd remains positive eighteen.

### Problem 6. All integer solutions, not a single witness

**Original · Diophantine equation.** Solve $84x+30y=6$ over integers, then impose nonnegative unknowns.

**Solution.** The gcd is six. The identity $6=3·30−84$ gives a particular pair $(−1,3)$. The complete family is $x=−1+5t$, $y=3−14t$ for integer $t$. Substitution cancels the parameter, and completeness follows from coprimality of fourteen and five after dividing the equation by six. Nonnegative $x$ requires $t ≥ 1$; nonnegative $y$ requires $t ≤ 0$. There is no feasible parameter. Thus an integer solution exists while a purchase using nonnegative quantities does not. Checking only that the gcd divides the target would miss the constraint that changes the answer.

### Problem 7. Count bounded nonnegative solutions

**Original · Feasibility interval.** Find all nonnegative solutions to $14x+9y=100$ and count them.

**Solution.** Reduce modulo nine: $5x ≡ 1$, and the inverse of five modulo nine is two, giving $x=2+9t$. Substituting gives $y=8−14t$. The nonnegative constraints imply $t ≥ 0$ and $t ≤ 0$, so the only pair is $(2,8)$. Direct substitution gives $28+72=100$. The solution family also explains why trying values until one pair is found is insufficient to prove completeness: the parameter interval establishes both uniqueness and feasibility. If strict positivity or an upper inventory bound were requested, add those inequalities before counting.

### Problem 8. The coin threshold with a proof

**Original · Nonnegative versus integer combinations.** Find the greatest amount not representable using denominations four and seven, and show how the threshold works.

**Solution.** The denominations are coprime, so the theorem proved in the lesson gives $4·7−4−7=17$. To see the obstruction concretely, a representation of seventeen satisfies $3y ≡ 1 (mod 4)$, forcing $y ≡ 3$, but three sevens already exceed seventeen. The next four amounts are $18=4+2·7$, $19=3·4+7$, $20=5·4$, and $21=3·7$. Every larger amount has the residue of one of those four and differs from it by a nonnegative multiple of four. Thus all larger amounts are representable. The four consecutive witnesses supply a constructive alternative to merely quoting the threshold formula.

### Problem 9. Prime powers reveal both lattice operations

**Course-derived · CMU valuation/lattice exercise type, changed inputs.** Compute gcd and lcm of 360 and 168; describe the positive divisors of their gcd.

**Solution.** Factor $360=2^3·3^2·5$ and $168=2^3·3·7$. Coordinatewise minima give $gcd=2^3·3=24$, while maxima give $lcm=2^3·3^2·5·7=2520$. Their product is $24·2520=60480=360·168$. A divisor of the gcd chooses the exponent of two from zero through three and the exponent of three from zero through one, giving eight choices: $1,2,3,4,6,8,12,24$. The largest common divisor is therefore twenty-four, and every common divisor divides it. The lcm is a common multiple that divides every common multiple because its prime exponents are the necessary minima for that task.

### Problem 10. Squares and coprimality are different tests

**Original · Prime-product boundary.** Is it true that $m ∣ a^2$ implies $m ∣ a$? Give a counterexample and state a sufficient condition.

**Solution.** Take $m=4$ and $a=2$: four divides four but not two. In exponent language the premise is $v_p(m) ≤ 2v_p(a)$; halving that bound does not generally imply $v_p(m) ≤ v_p(a)$. If $m$ is squarefree, each required exponent is one, so every prime dividing $m$ divides $a$ and their coprime product divides $a$. In particular a prime modulus has the desired implication. This identifies the structural condition rather than memorizing one counterexample. For a general exponent $k$, divisibility of $a^k$ likewise requires ceiling thresholds for valuations.

### Problem 11. Repair invalid cancellation

**Course-derived · CMU slide 38 cancellation exercise, explicit example.** Solve $6x ≡ 6 (mod 15)$ without losing solutions.

**Solution.** The common gcd is three. Dividing the coefficient, target, and modulus gives $2x ≡ 2 (mod 5)$, so $x ≡ 1 (mod 5)$. In the original residue interval the solutions are one, six, and eleven. Their products with six are six, thirty-six, and sixty-six, all congruent to six modulo fifteen. Cancelling the entire factor six while retaining modulus fifteen would incorrectly keep only one. The valid cancellation modulus is $15/gcd(6,15)=5$, which records exactly the information left after multiplication has merged distinct residues into the same fiber.

### Problem 12. No inverse is not the same as no solution

**Original · Linear congruence.** Solve $14x ≡ 30 (mod 100)$ and compare with target thirty-one.

**Solution.** The gcd of fourteen and one hundred is two. Target thirty is divisible by two, so reduce to $7x ≡ 15 (mod 50)$. The inverse of seven is forty-three because $7·43=301 ≡ 1$. Thus $x ≡ 645 ≡ 45 (mod 50)$, giving original residues forty-five and ninety-five. Substitution gives remainders thirty for both. Target thirty-one is not divisible by two, so no solution exists. Fourteen has no inverse modulo one hundred in either case; that fact alone does not decide consistency of a target that lies in its image.

### Problem 13. A multiplication map's image and fibers

**Original · Complete residue map.** Describe multiplication by eight modulo twelve.

**Solution.** Its gcd is four, so its kernel has four elements: zero, three, six, and nine. Its image is zero, four, and eight. For output four, reduce $8x ≡ 4$ by four to $2x ≡ 1 (mod 3)$, giving $x ≡ 2$ and original preimages two, five, eight, and eleven. Each fiber has four elements because two preimages differ by a kernel element, and adding any kernel element to one preimage preserves the output. The three fibers partition all twelve residues. Output six has no preimage. This is an exact many-to-one map, not a permutation with an inconvenient formula for its inverse.

### Problem 14. Zero coefficients and modulus one

**Original · Degenerate cases.** Solve $0x ≡ 12 (mod 6)$, $0x ≡ 13 (mod 6)$, and any linear congruence modulo one.

**Solution.** The first target is zero as a residue, so all six residues solve it. In the second, the target is one, so none solve it. The gcd test agrees: $gcd(0,6)=6$, which divides twelve but not thirteen. Modulo one, every integer has canonical remainder zero, so every congruence is true; its single residue is the only residue solution. After reducing an equation whose gcd equals its modulus, the reduced modulus is one and the solver should return this automatic condition. Asking an ordinary field inverse routine to process that degenerate case obscures a simple answer.

### Problem 15. A three-coordinate CRT construction

**Original · Coprime CRT.** Solve $x ≡ 2 (mod 3)$, $x ≡ 3 (mod 5)$, and $x ≡ 2 (mod 7)$.

**Solution.** The product is 105. The cofactors are thirty-five, twenty-one, and fifteen. Their inverses in the respective moduli are two, one, and one. The selectors are therefore seventy, twenty-one, and fifteen. Combine: $x ≡ 2·70+3·21+2·15=233 ≡ 23 (mod 105)$. Substitution gives remainders two, three, and two. Uniqueness follows because the difference of two solutions is divisible by all three pairwise coprime moduli, hence by 105. There are infinitely many integer solutions, $23+105t$, but exactly one residue class modulo 105.

### Problem 16. Compatible shared factors

**Course-derived · CMU generalized CRT theorem, original inputs and derivation.** Solve $x ≡ 4 (mod 6)$ and $x ≡ 10 (mod 14)$.

**Solution.** The gcd of the moduli is two, and the target difference is six, so compatibility holds. Set $x=4+6t$. Then $6t ≡ 6 (mod 14)$ reduces to $3t ≡ 3 (mod 7)$, yielding $t ≡ 1$. Therefore $x ≡ 10 (mod 42)$, where forty-two is the lcm. In a residue interval of length eighty-four, both ten and fifty-two solve the system. Using the product as a claimed uniqueness modulus would therefore be wrong. If the second target were eleven, the difference would be odd and compatibility would fail immediately.

### Problem 17. Coefficient reduction before CRT

**Original · Mixed modular system.** Solve $6x ≡ 8 (mod 14)$ and $4x ≡ 6 (mod 10)$.

**Solution.** The first gcd is two, so reduce to $3x ≡ 4 (mod 7)$, giving $x ≡ 6$. The second reduces to $2x ≡ 3 (mod 5)$, giving $x ≡ 4$. Set $x=6+7t$ and reduce the second condition: $1+2t ≡ 4 (mod 5)$, hence $t ≡ 4$. Thus $x ≡ 34 (mod 35)$. Substitution gives $6·34 mod 14=8$ and $4·34 mod 10=6$. The original moduli share a factor, while the reduced moduli are coprime. The final period thirty-five belongs to the reduced conditions, not to a blind product of original moduli.

### Problem 18. Pairwise compatibility beyond two equations

**Original · Generalized CRT proof application.** Are $x ≡ 1 (mod 4)$, $x ≡ 3 (mod 6)$, and $x ≡ 9 (mod 10)$ consistent?

**Solution.** Every pair of moduli has gcd two, and all three targets are odd, so pairwise compatibility holds. Merge the first two by setting $x=1+4t$: $4t ≡ 2 (mod 6)$ reduces to $2t ≡ 1 (mod 3)$, so $t ≡ 2$ and $x ≡ 9 (mod 12)$. Then $9+12u ≡ 9 (mod 10)$ gives $2u ≡ 0 (mod 10)$, so $u ≡ 0 (mod 5)$. The final answer is $x ≡ 9 (mod 60)$. The number sixty is the lcm of four, six, and ten. This calculation illustrates the prime-power compatibility theorem and verifies its promised constructive merge.

### Problem 19. Synchronization is an arithmetic progression

**Original · Scheduling model.** One event occurs at times congruent to five modulo twelve, another at times congruent to eleven modulo eighteen. Find their joint times and the first time at least one hundred.

**Solution.** The moduli have gcd six, and the target difference is six, so they are compatible. Put $t=5+12k$. Then $12k ≡ 6 (mod 18)$ reduces to $2k ≡ 1 (mod 3)$, giving $k ≡ 2$. Thus joint times satisfy $t ≡ 29 (mod 36)$. To impose the lower time bound, write $t=29+36u$ and require $u ≥ ⌈71/36⌉=2$. The first requested time is 101. CRT finds all joint times; choosing a “next” event requires the separate inequality and ceiling step.

### Problem 20. Totient and a biased counting shortcut

**Original · Arithmetic functions.** Find the fraction of residues modulo 360 that are units.

**Solution.** Factor $360=2^3·3^2·5$. There are $φ(360)=360(1−1/2)(1−1/3)(1−1/5)=96$ units. The fraction is $96/360=4/15$. Counting “not divisible by two, three, or five” by separately subtracting the three counts without restoring overlaps would be wrong. The product formula is justified by CRT across the coprime prime-power factors, not by assuming independence of arbitrary divisibility events. The zero residue is included in the denominator and is not a unit. Sampling integers from one through 360 yields the same fraction because that interval represents every residue exactly once.

### Problem 21. Exact order can be smaller than the totient

**Original · Power period.** Find the order of two modulo fifteen and compute $2^{1000} mod 15$.

**Solution.** The base is a unit. Its powers begin with two, four, eight, and one, so the first returning exponent is four. None of the previous three powers is one, proving exact order four. Since 1000 is divisible by four, the requested remainder is one. The totient is eight, also a valid period, but calling eight the order would be false. Exact order requires both a returning exponent and evidence that no smaller positive exponent returns. The cycle argument implies that equal powers have exponents differing by a multiple of four.

### Problem 22. A safe large-exponent reduction

**Original · Euler and CRT cross-check.** Compute $7^{222} mod 40$.

**Solution.** The gcd is one, and $φ(40)=16$, so Euler permits reducing 222 modulo sixteen to fourteen. A shorter method observes $7^2=49 ≡ 9$ and $7^4 ≡ 81 ≡ 1$, so the exponent can be reduced modulo four to two, giving nine. For an independent coordinate check, modulo eight the odd square is one, so the result is one; modulo five, $7 ≡ 2$ and $222 ≡ 2 (mod 4)$, so the result is four. The unique residue modulo forty with those coordinates is nine. Reducing the exponent modulo forty without a theorem would have no general justification.

### Problem 23. Nonunit powers require a transient

**Original · Failed exponent shortcut.** Compute $2^{100} mod 12$ and explain why reducing the exponent modulo $φ(12)$ fails.

**Solution.** The gcd of two and twelve is two, so Euler's premise fails. The first residues are $2,4,8,4,8,…$. Every even exponent at least two gives four, so the answer is four. Equivalently, modulo four the power is zero, and modulo three the even exponent gives one; CRT recombines them as four. Since $φ(12)=4$, blindly reducing 100 to zero would produce $2^0=1$, the wrong result. The period-two tail starts only after the transient; using a period requires knowing where that period is valid.

### Problem 24. Split a power across prime powers

**Original · Valuation plus Euler.** Compute $12^{100} mod 175$.

**Solution.** Factor $175=25·7$. The base is coprime to twenty-five, whose totient is twenty; therefore $12^{100} ≡ 1 (mod 25)$. Modulo seven the base is five, and the exponent reduces modulo six to four. Compute $5^2 ≡ 4$, so $5^4 ≡ 2$. Set $x=1+25t$. Modulo seven this becomes $1+4t ≡ 2$, giving $t ≡ 2$. Thus the canonical answer is fifty-one. Although this particular base is also a unit modulo 175, the coordinate technique prepares for mixed cases where a base is a unit in one component and vanishes in another; check those gcds before choosing the reduction.

### Problem 25. A genuinely mixed-coordinate power

**Original · Prime-power thresholds.** Compute $6^{50} mod 200$.

**Solution.** Split $200=8·25$. The two-valuation of six is one, so an exponent at least three makes the power zero modulo eight. Modulo twenty-five the base is a unit and the exponent fifty reduces modulo twenty to ten. Compute $6^2 ≡ 11$, $6^4 ≡ 21$, $6^8 ≡ 16$, and $6^{10} ≡ 16·11 ≡ 1$. Now set $x=25t+1$: modulo eight, $t+1 ≡ 0$, so $t ≡ 7$ and $x=176$. It is zero modulo eight and one modulo twenty-five. Reducing fifty modulo the totient of two hundred would require a unit premise that this base does not satisfy.

### Problem 26. A power tower with an exponent contract

**Original · Nested exponentiation.** Compute $3^{(3^{20})} mod 100$.

**Solution.** The outer base is a unit modulo one hundred, so it is enough to know the exponent modulo $φ(100)=40$. Compute $3^{20} mod 40$: since $3^4=81 ≡ 1$, exponent twenty gives remainder one. Hence the outer answer is $3^1 mod 100=3$. The reduction is performed in two different moduli: the outer value modulo one hundred, its exponent modulo forty. The final calculation does not assert that the enormous exponent equals one as an integer. Exponentiation is right-associated here; $(3^3)^{20}$ would be a different expression with exponent sixty.

### Problem 27. Repeated-squaring proof and operation counts

**Course-derived · Berkeley Note 6, page 3 algorithm-proof exercise.** Prove the lesson's iterative modular-power algorithm and count its multiplications for exponent thirteen.

**Solution.** The loop invariant is $result·base^{left} ≡ a^{13}$. It holds initially because the result is the identity and the base is the reduced input. An odd iteration moves one factor into the result; an even one moves none. Squaring the base and flooring half the exponent preserves the remaining product in both cases. The nonnegative remaining exponent shrinks until it becomes zero, when the result equals the target residue. Thirteen has binary representation 1101, so there are four iterations, four squarings, and three result multiplications. With exponent zero, there are zero iterations and the canonical result is $1 mod m$, including zero for modulus one. This explicitly fixes the degenerate base-case output that a bare return-one pseudocode may leave unreduced.

### Problem 28. More than two square roots of one

**Original · CRT root choices.** Find all roots of $x^2 ≡ 1 (mod 35)$.

**Solution.** Modulo five the roots are one and four; modulo seven they are one and six. There are four independent sign pairs. The two matching signs give residues one and thirty-four. For $x ≡ 1 (mod 5)$ and $x ≡ 6 (mod 7)$, set $x=1+5t$, obtaining $5t ≡ 5$ and $t ≡ 1$, so $x=6$. The other mixed pair is its negative, twenty-nine. Squaring yields one for all four residues. Completeness follows because every root must have one of the two signs in each prime coordinate, and CRT provides exactly one residue for each pair. A composite modulus allows extra roots through zero divisors.

### Problem 29. A prime-power quadratic equation

**Original · Valuation threshold.** Find all roots of $x^2 ≡ 0 (mod 72)$.

**Solution.** Factor $72=2^3·3^2$. Divisibility of the square requires $2v_2(x) ≥ 3$ and $2v_3(x) ≥ 2$, so $v_2(x) ≥ 2$ and $v_3(x) ≥ 1$. Equivalently, twelve divides $x$. The residues are zero, twelve, twenty-four, thirty-six, forty-eight, and sixty. Each square is a multiple of $12^2=144$, hence of seventy-two. This includes zero without assigning it a finite valuation. Necessity for nonzero residues is supplied by their prime exponents; sufficiency and the zero case follow by direct divisibility. Simply requiring seventy-two to divide $x$ would miss five roots.

### Problem 30. Odd squares and powers of two

**Original · Composite-ring roots.** Find every root of $x^2 ≡ 1 (mod 16)$.

**Solution.** Any root is odd. Write $x=2k+1$, giving $x^2−1=4k(k+1)$. Divisibility by sixteen requires four to divide $k(k+1)$. One of the two consecutive factors is odd, so the even factor must itself be a multiple of four. Thus $k ≡ 0$ or three modulo four. In the eight odd residues modulo sixteen, this gives $x=1,7,9,15$. Each checks directly. The factors $x−1,x+1$ can share powers of two, so the prime-product inference that one factor alone is divisible by sixteen is invalid. The four solutions are not a contradiction of the two-root theorem over a prime field.

### Problem 31. Count and sum divisors without listing them

**Original · Arithmetic functions.** Find the number and sum of positive divisors of 360 and determine whether the count is odd.

**Solution.** The factorization is $2^3·3^2·5$. The count is $(3+1)(2+1)(1+1)=24$. The sum is $(1+2+4+8)(1+3+9)(1+5)=15·13·6=1170$. The exponent choices are independent because the factors are distinct primes. The count is even because some exponents are odd; equivalently, 360 is not a square. As a contrasting boundary, the number one has only divisor one, so its count and sum are both one and its count is odd. The empty-product convention matches that direct enumeration.

### Problem 32. Trailing zeros in different bases

**Original · Factorial valuations.** Count trailing zeros of $100!$ in bases ten and twelve.

**Solution.** The five-valuation is $⌊100/5⌋+⌊100/25⌋=20+4=24$. The two-valuation is $50+25+12+6+3+1=97$. A base-ten zero consumes one two and one five, so there are twenty-four. Base twelve is $2^2·3$. The three-valuation is $33+11+3+1=48$, while the supply of pairs of twos is $⌊97/2⌋=48$. Thus there are forty-eight base-twelve zeros. Counting only multiples of the prime ignores extra powers in some factors; counting multiples of twelve alone does not track contributions assembled across different factorial factors.

### Problem 33. Binomial divisibility by valuation subtraction

**Original · Factorial quotient.** Find the two-valuation of the binomial coefficient choosing six objects from ten.

**Solution.** The coefficient is $10!/(6!4!)$. The two-valuations are $v_2(10!)=5+2+1=8$, $v_2(6!)=3+1=4$, and $v_2(4!)=2+1=3$. The quotient therefore has valuation one. Hence it is divisible by two but not by four. The numerical value is 210, which confirms the result. The method avoids constructing factorials and makes clear why division is valid here: the factorial ratio is an integer with exact factor cancellation, not a division inside a residue ring where the denominator might lack an inverse.

### Problem 34. A polynomial obstruction from parity

**Course-derived · CMU slides 21–24, independently generalized.** Let an integer-coefficient polynomial have odd values at zero and one. Prove that it has no integer root.

**Solution.** Every integer is congruent to zero or one modulo two. Polynomial evaluation respects congruence, so its value is congruent to one of those two odd values and is therefore odd. Zero is even, ruling out an integer root. This works for any finite degree, not only the cubic displayed in the source. It does not rule out rational or real roots because those inputs do not belong to either integer residue class. For example, $2x+1$ has odd values at zero and one yet has the rational root negative one half.

### Problem 35. Passing Fermat does not certify primality

**Original · Pseudoprime counterexample.** Show that 341 is composite but passes the base-two Fermat check.

**Solution.** Factor $341=11·31$. The base two is coprime to both factors. The power $2^{10}=1024$ is one modulo eleven and one modulo thirty-one, because their quotients are ninety-three and thirty-three respectively. CRT gives $2^{10} ≡ 1 (mod 341)$. Since 340 is thirty-four times ten, $2^{340} ≡ 1$. This one successful base therefore fails to detect compositeness. A failed Fermat congruence would provide a sound composite certificate; a successful congruence provides only a necessary condition for primality at that base. There is no inference from this example about the failure rates of other primality algorithms.

### Problem 36. Wilson's theorem includes a converse

**Course-derived · CMU Wilson theorem, proof-completion exercise.** Prove the converse and explain why it differs from Fermat's converse.

**Solution.** Assume $n ≥ 2$ and $(n−1)! ≡ −1 (mod n)$. If $n$ were composite, it would have a proper divisor $d$ with $1<d<n$. That divisor is among the factorial's factors, so $d$ divides the factorial. Since $d$ also divides $n$, the congruence would make $d$ divide negative one, impossible. Thus $n$ is prime. This direct contradiction establishes a genuine equivalence, whereas Fermat's test has composites passing a selected base. For prime two, the factorial is one and negative one is also one modulo two, so it fits. A theorem's converse must be proved separately; similarity of its statement to another theorem does not transfer the converse.

### Problem 37. A rotation has several index cycles

**Course-derived · CMU slides 56–59 rotation exercise, changed inputs.** Describe the index cycles for adding eight modulo twenty and explain an in-place rotation's outer-loop count.

**Solution.** The gcd is four, so there are four cycles of length five. Starting at zero gives $0,8,16,4,12$; starting at one gives $1,9,17,5,13$; starting at two gives $2,10,18,6,14$; starting at three gives $3,11,19,7,15$. Each cycle contains precisely one residue class modulo four. They are disjoint and contain twenty indices in total. Returning after five steps follows from $5·8$ being divisible by twenty, and no smaller positive return is possible by the reduced congruence. An in-place cycle method must process four starting cycles; processing only the cycle of zero would leave fifteen elements untreated.

### Problem 38. RSA correctness must include nonunits

**Course-derived · Berkeley Note 7, CRT correctness proof, changed example.** Use $p=5,q=11,e=3,d=27$ to explain correctness for message five.

**Solution.** The modulus is fifty-five and $ed=81=1+2·40$, with $40=(5−1)(11−1)$. Encryption gives $5^3 mod 55=15$. The message has gcd five with the modulus, so Euler directly modulo fifty-five cannot justify recovery. Instead, modulo five both the original message and its power eighty-one are zero. Modulo eleven the base is a unit, and eighty differs from zero by a multiple of ten, so Fermat gives $5^{81} ≡ 5$. CRT therefore gives recovery of five modulo fifty-five. Equivalently, $15^{27} mod 55=5$. Correctness of this arithmetic example says nothing about practical cryptographic security.

### Problem 39. Every identified shortcut needs a premise

**Original · Combined diagnosis.** Explain the flaws in these claims: every pairwise coprime set has gcd one; every set with gcd one is pairwise coprime; coprimality is transitive; the product of distinct primes plus one is prime.

**Solution.** The first implication requires a finite family with at least two members; as stated without that restriction it fails for the singleton set containing six, which is vacuously pairwise coprime but has gcd six. With at least two members it is true: a common prime divisor would divide each pair. The reverse fails for $6,10,15$: their overall gcd is one but each pair shares a prime. Transitivity fails for two, three, and four: each neighboring pair is coprime, while the endpoints are not. For the final claim, $2·3·5·7·11·13+1=30031=59·509$ is composite. Euclid's argument needs a prime divisor not on the list, not primality of the whole constructed number. Each correction identifies what the proof actually establishes and supplies an explicit boundary example.

### Problem 40. Recover factors from a supplied totient

**Original · Synthesis of arithmetic and a quadratic.** Suppose $n=77$ is the product of two distinct primes and $φ(n)=60$. Recover the factors without trying divisors.

**Solution.** For distinct primes, $φ(n)=(p−1)(q−1)=pq−p−q+1$, so $p+q=n−φ(n)+1=18$ and $pq=77$. The factors are roots of $t^2−18t+77=0$. Its discriminant is $18^2−4·77=16$, so the roots are $(18±4)/2$, namely seven and eleven. Substitution verifies both the product and the totient. This calculation illustrates why knowing the totient of a two-prime modulus reveals factor information. The method assumes distinct primes; a prime square has a different totient formula. It does not supply the totient from the public modulus alone.
