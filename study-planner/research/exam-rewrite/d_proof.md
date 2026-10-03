## Teaching through formulas and conceptual decisions

### Convert a claim into the exact proof obligation

An implication fails only when its premise is true and conclusion false. Consequently, a proposed counterexample must satisfy the premise; an object that violates the premise proves nothing. The contrapositive of $P\Rightarrow Q$ is $\neg Q\Rightarrow\neg P$. For a compound antecedent $P\land R$, the negative is $\neg P\lor\neg R$, not a conjunction. A biconditional requires two independently justified implications.

Existence means producing an admissible witness. Uniqueness means comparing any two possible witnesses and proving equality. For $ax=b$ over the reals, a unique solution requires $a\ne0$; if $a=0$, the equation has all real solutions when $b=0$ and none otherwise. Dividing by $a$ before splitting these cases silently assumes precisely the fact to be tested.

### Let algebra expose the equality and domain conditions

For real $x,y$, $(x-y)^2\ge0$ gives $x^2+y^2\ge2xy$, with equality exactly when $x=y$. Squaring a comparison is reversible only after sign conditions make the square function monotone on the permitted interval. The statement $x^2>y^2\Rightarrow x>y$ is false: $x=-3,y=2$ refutes it. Cancellation of a zero factor is another lost branch: from $x(x-1)=0$, either factor may vanish.

Integer proofs often reduce a quantified assertion to a finite remainder table. Every integer, including negative integers, has exactly one remainder in $\{0,1,\ldots,m-1\}$ under Euclidean division by positive $m$. A residue argument is exhaustive only when all these classes are handled. Observing many positive examples is not a proof over all integers.

## Formula and conceptual problem bank

### Question 1. Negate the whole implication

Which statement is the contrapositive of “If $x>0$ and $y>0$, then $xy>0$”?

**A.** If $xy\le0$, then $x\le0$ and $y\le0$.

**B.** If $xy\le0$, then $x\le0$ or $y\le0$.

**C.** If $xy>0$, then $x>0$ and $y>0$.

**D.** If $x\le0$ or $y\le0$, then $xy\le0$.

**Answer: B.**

Negate the conclusion to obtain $xy\le0$. Negate the whole antecedent using De Morgan: $\neg(x>0\land y>0)$ is $x\le0\lor y\le0$. This produces B. Option A is stronger and false when $x=-1,y=1$. Options C and D are converse and inverse, respectively, and both fail for two negative inputs. Equivalence applies to the full grouped antecedent.

### Question 2. Valid counterexample

Which pair disproves “For all real $x,y$, if $x^2>y^2$ then $x>y$”?

**A.** $(1,2)$

**B.** $(3,2)$

**C.** $(-3,2)$

**D.** $(2,2)$

**Answer: C.**

For $x=-3,y=2$, the premise is $9>4$ and the conclusion is $-3>2$, which is false. Option A has a false premise, B satisfies the implication, and D also has a false premise. A counterexample must hit the one failing truth row; it is not enough for the conclusion alone to fail.

### Question 3. A residue proof

For integer $n$, which condition is equivalent to $3\mid(n^2-1)$?

**A.** $3\mid n$

**B.** $3\nmid n$

**C.** $n$ is odd

**D.** $n>0$

**Answer: B.**

The three residues of $n$ modulo 3 are 0,1,2. Their squares are 0,1,1, so $n^2-1$ has residue 2,0,0. Exactly the nonmultiples of 3 satisfy the divisibility claim. This proof handles negative integers too. Oddness and positivity are unrelated to the residue condition; for example 2 satisfies it and 3 does not.

### Question 4. Existence and uniqueness parameter

Over the real numbers, for which parameters $a$ does $ax=1$ have exactly one solution?

**A.** All real $a$

**B.** $a=0$

**C.** $a\ne0$

**D.** $a>0$ only

**Answer: C.**

If $a\ne0$, the witness $x=1/a$ satisfies the equation. If two solutions $x,y$ exist, $a(x-y)=0$ and nonzero $a$ implies $x=y$. If $a=0$, the equation becomes $0=1$ and has no solution. Negative nonzero values are just as valid as positive ones; D unnecessarily restricts the parameter.

### Question 5. A rationality implication

For real numbers $a,b$, which assertion is always true?

**A.** The sum of two irrational numbers is irrational.

**B.** The product of two irrational numbers is irrational.

**C.** A nonzero rational times an irrational is irrational.

**D.** A rational divided by an irrational is always irrational.

**Answer: C.**

Let $r$ be nonzero rational and $u$ irrational. If $ru$ were rational, division by the nonzero rational $r$ would make $u$ rational, a contradiction. The nonzero condition is essential. Two irrationals can sum to zero or multiply to an integer. Option D fails when its rational numerator is zero. Rationality closure must be paired with legal division.

### Question 6. Equality case of an inequality

For real $x,y$, when does $x^2+y^2=2xy$ hold?

**A.** $x=-y$

**B.** $x=y$

**C.** $xy=0$

**D.** $x,y\ge0$

**Answer: B.**

Transfer all terms to one side: $x^2-2xy+y^2=(x-y)^2=0$. A real square is zero exactly when its base is zero, giving $x=y$. Equal negative values work too. Opposite values work only at zero, and nonnegativity alone does not force equality. The equality condition comes from the precise nonnegative term used in the proof.

### Question 7. Cancellation with a lost case

A purported proof cancels $x$ in $x^2=x$ and concludes $x=1$. Which set is the actual real solution set?

**A.** $\{1\}$

**B.** $\{0\}$

**C.** $\{0,1\}$

**D.** $\mathbb R$

**Answer: C.**

Rearrange without division: $x^2-x=x(x-1)=0$. The real zero-product property gives $x=0$ or $x=1$. Both substitute correctly into the original equation. Cancellation was legal only on the branch $x\ne0$ and omitted the other branch. D mistakes a particular equation for an identity.

### Question 8. Construct a witness after the input

For every real $x$, there exists real $y$ such that $x+y=0$. Which witness construction proves the claim?

**A.** $y=0$ for every $x$

**B.** $y=-x$

**C.** $x=0$ for every $y$

**D.** A single fixed $y$ chosen before $x$

**Answer: B.**

Given an arbitrary $x$, choose $y=-x$; then $x+y=0$ by additive inverses. The witness is allowed to depend on the universally chosen input because the existential quantifier follows it. A fixed $y$ cannot work for both $x=0$ and $x=1$. Changing which variable is arbitrary changes the claim rather than proving it.

### Question 9. Prime construction trap

For $N=p_1p_2\cdots p_k+1$, where the $p_i$ are positive primes, which conclusion always follows?

**A.** $N$ is prime.

**B.** No prime divisor of $N$ equals any $p_i$.

**C.** $N$ is smaller than every $p_i$.

**D.** $N$ has no prime divisor.

**Answer: B.**

Each $p_i$ divides the product, so $N$ has remainder 1 on division by $p_i$. Thus none divides $N$. Since $N>1$, some prime divisor exists, but $N$ itself need not be prime; $2\cdot3\cdot5\cdot7\cdot11\cdot13+1=30031=59\cdot509$. The proof needs a new prime divisor, not the false assertion that the constructed integer is always prime.

### Question 10. Exactly one means two obligations

A proof of “there exists exactly one $x$ with $P(x)$” establishes only that $P(a)$ is true. What is missing?

**A.** A second witness distinct from the first.

**B.** A proof that every $x$ satisfying $P(x)$ equals $a$.

**C.** A proof that every $x$ fails $P(x)$.

**D.** No further argument.

**Answer: B.**

The verified witness supplies existence. Uniqueness still requires taking any arbitrary satisfying $x$ and deducing $x=a$. Producing another distinct witness would refute uniqueness rather than establish it. A proof that every input fails contradicts existence. Keeping the arbitrary candidate separate from the constructed witness prevents circular uniqueness arguments.

<!-- CHALLENGE-BANK -->

### Question 11. Challenge: A universal prime claim

Which$n$ is a counterexample to “$n^2+n+41$ is prime for every integer$n\ge0$”?

**A.** 0

**B.** 1

**C.** 2

**D.** 40

**Answer: D.**

At$n=40$, the value is1600+40+41=1681=$41^2$, a composite. It satisfies the nonnegative-domain premise and falsifies the conclusion. At0,1,2 the values41,43,47 are prime and do not disprove the claim. The argument needs one verified composite, not a characterization of every earlier input. Recognizing that substituting one less than the constant yields its square constructs the counterexample rather than guessing.

### Question 12. Challenge: An inequality with domain-sensitive division

For real$x>0$, which statement about$x+1/x$ is correct?

**A.** Its minimum is0.

**B.** Its minimum is2, attained only at$x=1$.

**C.** It is always strictly greater than2.

**D.** It has the same lower bound for all nonzero real$x$.

**Answer: B.**

Compute$x+1/x-2=(x-1)^2/x$. The numerator is nonnegative and the denominator positive, proving the lower bound2. Equality forces$x-1=0$, and$x=1$ is admissible. Strictness fails at that witness. If negative$x$ were admitted, dividing by$x$ would reverse the sign argument and the expression could be negative without this lower bound. The domain and equality case are both part of the conclusion.

## Applicable formulas and examination notes

### 1. Implication failure

A counterexample to $P\Rightarrow Q$ must satisfy $P\land\neg Q$. For $x^2>y^2\Rightarrow x>y$, use $(-3,2)$, not $(1,2)$. A false premise makes the implication true and cannot be used to reject it.

### 2. Contrapositive grouping

For $(P\land R)\Rightarrow Q$, start from $\neg Q$ and target $\neg P\lor\neg R$. For $(P\lor R)\Rightarrow Q$, target $\neg P\land\neg R$. Negate the grouped expression before choosing a proof tactic.

### 3. Biconditional obligations

To prove $P\Leftrightarrow Q$, prove $P\Rightarrow Q$ and $Q\Rightarrow P$. Showing two examples where both are true establishes neither universal direction. A divisibility equivalence can often be tested and proved by an exhaustive residue table.

### 4. Zero-factor branch

Before dividing by a variable expression $g(x)$, split $g(x)=0$ and $g(x)\ne0$. In $x^2=x$, the zero branch is a real solution. Cancellation can simplify a branch but cannot erase it from the answer set.

### 5. Squaring a comparison

Squaring preserves order for nonnegative operands. Without that premise, $-3<2$ yet $9>4$. Solve or prove a squared inequality by tracking signs or by factoring, rather than assuming the squaring step is reversible.

### 6. Equality from the proof

In $x^2+y^2\ge2xy$, equality holds precisely when $(x-y)^2=0$. The source of nonnegativity identifies the equality condition. For a sum of nonnegative terms, equality requires every term to vanish, not only their product.

### 7. Unique linear witness

For $ax=b$, nonzero $a$ yields exactly one real solution. If $a=0$, $b=0$ yields all reals and $b\ne0$ yields none. Parameter questions demand this split before substitution of $b/a$.

### 8. Rational closure conditions

If $r\ne0$ is rational and $u$ irrational, $ru$ is irrational because a rational result would imply $u=(ru)/r$ rational. Remove the nonzero condition and the proof fails at $r=0$. Sums or products of two irrational numbers have no automatic irrationality guarantee.

### 9. Euclidean residues include negatives

For modulus 3, every integer has remainder 0,1 or2. Hence $3\mid n^2-1$ exactly when the remainder is 1 or2. A residue proof does not need separate positive and negative cases once the division convention is specified.

### 10. Constructed integer versus prime divisor

For a product of listed primes plus one, prove that none of the listed primes divides it. The constructed integer can be composite. Extract a prime divisor to contradict completeness of the list; primality of the whole integer is unnecessary and generally false.

<!-- BOUNDARY-NOTES -->

### 11. Negating nested targets

The negation of $\forall x\exists yP(x,y)$ is $\exists x\forall y\neg P(x,y)$. A contradiction proof assumes that whole negation, including the changed witness dependence. Choosing one bad pair instead does not refute the original dependent-witness claim.

### 12. Contradiction need not use every assumption

A contradiction must follow validly from the stated hypotheses and the negated target. It may use only a subset of available assumptions. The failure is circular reasoning or an invalid step, not merely leaving an irrelevant premise unused.

### 13. Exhaustive cases

A split into positive, zero and negative values covers all real numbers; a split into positive and negative omits zero. Check coverage before proving each branch. A proof can have correct algebra in every written branch and still fail because an admissible branch is missing.
