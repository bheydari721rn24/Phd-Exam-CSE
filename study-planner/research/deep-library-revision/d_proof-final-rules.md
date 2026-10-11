## Proof rules, mathematical checks and examination traps

### 1. Write the quantified target before choosing a method

A universal implication $\forall x\in D(P(x)\Rightarrow Q(x))$ requires an arbitrary admissible input and a derivation from $P(x)$ to $Q(x)$. A counterexample requires an input in $D$ with $P$ true and $Q$ false. For the false claim “even sum implies both summands even,” $(3,5)$ qualifies, while $(1,2)$ does not activate the premise. The domain is part of the statement.

### 2. Direct proof closes the definition of the conclusion

To show $a\mid b$, construct an integer $k$ with $b=ak$. From $a\mid u$ and $a\mid v$, writing $u=ar,v=as$ gives $2u-3v=a(2r-3s)$ with an integer witness. No division by $a$ is used, so zero is handled correctly. A candidate expression is not a complete witness until its domain and required equation are verified.

### 3. Contrapositive reverses and negates both predicates

$P\Rightarrow Q$ is equivalent to $\neg Q\Rightarrow\neg P$. The converse $Q\Rightarrow P$ and inverse $\neg P\Rightarrow\neg Q$ require separate proofs and can fail. For $4\mid n\Rightarrow2\mid n$, $n=2$ refutes the converse. Negating a conjunction produces a disjunction; do not strengthen the negated conclusion accidentally.

### 4. Contradiction needs an established impossibility

To prove an implication, assume $P\land\neg Q$ and derive a contradiction from valid facts. To prove irrationality of $\sqrt2$, use a reduced fraction, derive that both numerator and denominator are even, and contradict their coprimality. A result that merely differs from a desired answer is not a contradiction. Record which temporary assumption is discharged.

### 5. Negate whole quantifiers and keep their domains

$\neg\forall x\exists yR(x,y)$ becomes $\exists x\forall y\neg R(x,y)$. Negation does not swap variables' domains or preserve quantifier types. The negation of unique existence is either no witness or two distinct witnesses. Testing only the no-solution possibility omits a second way uniqueness can fail.

### 6. A witness can depend only on choices already made

For $\forall x\in\mathbb Z\exists y\in\mathbb Z(y>x)$, choose $y=x+1$ after $x$ is fixed. For $\exists y\forall x(y>x)$, any proposed $y$ is defeated by $x=y$. Generalizing a special witness as though it were arbitrary is invalid. In natural deduction, universal introduction requires that its parameter not be fixed by an undischarged assumption.

### 7. Existence and uniqueness are separate obligations

Substitution can prove that a candidate solves $cx=d$, but uniqueness needs comparison of arbitrary solutions or a proved injectivity theorem. For $c\ne0$, subtracting two solution equations gives $c(x_1-x_2)=0$, hence equality. If $c=0$, distinguish $d=0$ from $d\ne0$; those give all solutions and no solutions respectively.

### 8. Every cancellation checks its exact factor

The condition $x\ne0$ does not imply $x-y\ne0$. If $x=y$, cancellation of $x-y$ divides by zero even when both original variables are nonzero. From $cz=cw$ with $c=0$, nothing about $z,w$ follows. Classify parameter values making a divisor zero before simplifying the remaining cases.

### 9. Square and square-root steps retain signs

$x^2=y^2$ implies $x=y$ or $x=-y$, not just equality. The equivalence between $u\ge v$ and $u^2\ge v^2$ requires suitable nonnegative signs. In AM-GM, nonnegative inputs ensure both a real square root and nonnegative sides. Two negative inputs may have positive product while their arithmetic mean is negative, refuting an unsupported extension.

### 10. Inequality division checks positivity, not just nonzeroness

Dividing an inequality by a negative number reverses its direction. The identity $x+1/x-2=(x-1)^2/x$ gives a lower bound two when $x>0$. On the negative domain, use the different identity $x+1/x+2=(x+1)^2/x$ to obtain an upper bound minus two. Equality occurs at $x=1$ and $x=-1$ respectively; zero is excluded. A claimed minimum also requires an admissible attaining input, not only a bound.

### 11. A case split must cover every allowed input

Even and odd cases cover all integers, including negatives. The real cases $x>0$ and $x<0$ omit zero unless the theorem excludes it. Cases may overlap if their union is exhaustive. A missed boundary can invalidate a proof even when every handled branch is correct. State why the split covers the domain before using its branches.

### 12. Biconditionals need both implication directions

Proving $P\Rightarrow Q$ does not establish $P\Leftrightarrow Q$. A chain of rearrangements establishes equivalence only when every step is reversible under the hypotheses. For $6\mid n\Leftrightarrow6\mid n^2$, the forward direction is algebraic and the converse uses the prime structure of six. Replacing six by four refutes the converse but preserves the forward direction.

### 13. A composite-square converse has a prime-exponent test

For $m=\prod p_i^{e_i}>0$, $m\mid x^2$ is equivalent to $\prod p_i^{\lceil e_i/2\rceil}\mid x$. Thus root divisibility by the original $m$ follows for every input precisely when $m$ is squarefree. For $m=12$, $x=6$ supplies a counterexample to an unrestricted root-divisibility claim. Necessary prime factors alone do not account for their multiplicities.

### 14. Residue compatibility can screen without constructing

A square has residue zero or one modulo four, so residue three proves impossibility. But 17 has compatible residue one and is not a square. A necessary condition is not automatically sufficient. A parity equivalence can be sufficient when both directions are proved; do not transfer that sufficiency to arbitrary congruence tests.

### 15. Sharp bounds pair an impossibility proof with a construction

$n$ boxes capped at $k-1$ each hold at most $(k-1)n$ objects. One more forces the cap to be exceeded. An actual arrangement at that preceding total proves sharpness. A larger sufficient count is not a correct minimum. Empty boxes do not invalidate an upper-capacity sum, and the average need not reach integer $k$ before some occupancy does.

### 16. A pairing proof needs a genuine partition of distinct values

The involution $i\mapsto2n+1-i$ forms $n$ disjoint complementary pairs. A subset with $n+1$ distinct values forces a full pair; choosing one endpoint per pair constructs a nonforcing subset of size $n$. Repeated samples can revisit one endpoint and break this argument. For unordered or repeated objects, rederive the counting model rather than reusing a subset threshold.

### 17. Semantic entailment tests premise-true, conclusion-false models

A true implication alone does not supply its antecedent or its consequent. Independent implication pairs permit states 00,01,11; requiring some false antecedent gives $3^n-1$ models. Contradictory premises have no satisfying model and classically entail every formula, but this does not make those formulas tautologies. Keep the premise set attached to the conclusion.

### 18. Finite verification is complete only for its stated finite scope

An exhaustive check of all positive triples with fixed total $N$ proves a property on that finite domain if the enumeration and evaluations are correct. It proves no unbounded-total theorem by itself. To refute a universal statement, one verified admissible failure suffices: $40^2+40+41=41^2$ refutes the universal prime claim despite earlier prime outputs. Separate discovering a pattern from proving its quantified scope.
