## Mathematical constructions behind the problem bank

The full proof methods above remain the foundation. This section derives the particular counting, algebra and formal-inference tools used in the following questions. An exact calculation should show why it establishes the requested logical claim, rather than merely display a numerical result.

### 1. Quantifier rules retain dependencies

Universal elimination instantiates a known universal assertion at a permitted object. Universal introduction generalizes a derivation at an arbitrary parameter; the parameter must not be fixed by an undischarged assumption. Existential introduction supplies a verified witness. Existential elimination reasons from a fresh provisional witness and must end with a conclusion independent of that witness's special name.

For example, from $\forall xP(x,x)$ instantiate at arbitrary $u$ to obtain $P(u,u)$. Introduce an existential with witness $u$, obtaining $\exists zP(u,z)$. Because the sole undischarged premise does not single out $u$, generalize to $\forall y\exists zP(y,z)$. The witness can depend on the universally selected input. Generalizing instead to $\exists z\forall yP(y,z)$ would change that dependency and does not follow. Equality on a two-object domain satisfies the premise but has no one object equal to every input, providing a countermodel to the altered conclusion.

### 2. Algebraic transformations have exact side conditions

For $cx=d$ over the reals, division by $c$ is reversible only when $c\ne0$. If $c=0$, classify whether $d$ also vanishes. This yields respectively a unique solution, no solution or every real solution. Apply that classification before cancelling parameter-dependent factors. In $(a^2-1)x=a-1$, the two zeros of the coefficient have different outcomes, so one cannot discard them together as an undifferentiated exceptional case.

For inequalities, a nonzero divisor is still insufficient: its sign determines whether the order reverses. The identity $x+1/x-2=(x-1)^2/x$ proves a lower bound on the positive domain and an upper bound on the negative domain. At zero the expression is undefined. For a claimed extremum, prove the bound and separately exhibit an admissible equality witness. A non-attained lower bound is an infimum, not a minimum.

### 3. Composite divisibility uses prime exponents

For positive $m=\prod p_i^{e_i}$, the exponent of $p_i$ in a nonzero square $x^2$ is twice its exponent in $x$. Therefore the least required divisor of the root is

$$d=\prod p_i^{\lceil e_i/2\rceil},\qquad m\mid x^2\Longleftrightarrow d\mid x.$$

This gives $\lfloor M/d\rfloor$ successful positive inputs up to $M$. For squarefree $m$, $d=m$ and the square-to-root converse is valid. For $m=12$, $d=6$, so a root divisible by six suffices even without divisibility by twelve. Zero is handled directly and is divisible by every positive modulus. A proof that treats all composite divisors as primes can therefore give a wrong converse while its forward implication remains valid.

### 4. Sharp thresholds have two proof obligations

To find the minimum number forcing occupancy at least $k$ in one of $n\ge1$ boxes, suppose all occupancies are at most $k-1$. Their sum is at most $(k-1)n$. Thus one more object forces the conclusion. Placing exactly $k-1$ objects in each box proves that the preceding total does not force it. The threshold is $(k-1)n+1$.

For a subset of $\{1,\ldots,2n\}$, the partner function $i\mapsto2n+1-i$ partitions the universe into $n$ disjoint pairs with no fixed points. More than $n$ distinct chosen values force both endpoints of one pair, while one endpoint per pair gives a maximum nonforcing set. This argument fails for repeated selections because repeated visits to a pair need not include both endpoints. A forcing proof alone can establish a sufficient bound; the construction is what establishes sharpness.

### 5. Counterexample counting follows the negated predicate

To refute a bounded universal claim, every counted witness must lie in the domain and satisfy the exact negation. For $x\le y$ on an $n$-value domain, the negation is $x>y$, whose row $x$ has $x-1$ targets. Summing gives $n(n-1)/2$. The diagonal consists of satisfying assignments and must not be counted as failures.

For a modular example, let $E$ and $T$ be inputs divisible by two and three. “Divisible by either but not six” means the symmetric difference, whose size is $|E|+|T|-2|E\cap T|$. The second subtraction excludes a common input after the first has merely corrected its double occurrence. On a complete six-object block, the successful residues are 2,3,4. The two methods derive the same count from different representations of the predicate.

### 6. Vacuous truth is part of an implication's state space

For distinct pairs of atoms, $p_i\Rightarrow q_i$ permits 00,01,11. A false antecedent leaves the consequent free; a true antecedent forces it true. The conjunction of $n$ independent implications therefore has $3^n$ models. Requiring at least one false antecedent excludes precisely the all-11 model, giving $3^n-1$.

This can also be counted by the number $j$ of false antecedents. Choose them in $\binom nj$ ways and choose their consequent values in $2^j$ ways. Every remaining consequent is forced, so summing for $j\ge1$ gives $3^n-1$. Shared atoms invalidate the independence argument; two implications with a common antecedent have a different model space. Truth of an implication alone does not prove its consequent, and inconsistency of all premises makes semantic entailment vacuous rather than making every formula a tautology.

### 7. Exhaustive finite search has a precisely bounded conclusion

For positive triples of total $N\ge3$, subtract one from each variable and distribute $N-3$ nonnegative units over three labelled coordinates. Stars and bars gives $\binom{N-1}2$. A second derivation fixes the first coordinate and sums $N-2,N-3,\ldots,1$ possibilities for the others.

If a predicate is evaluated correctly on every such triple, the resulting finite proof applies to that fixed total. It does not prove the same predicate for all larger totals. Conversely, one admissible failed triple refutes the bounded claim, but an out-of-domain triple does not. Exhaustiveness must be established by a bijection or complete range argument; a long list of samples without such a justification can miss inputs. This is why both handwritten proofs and computational checks should state the exact domain they certify.
