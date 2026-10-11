## Final review: actionable mathematical and conceptual rules

### 1. Identify the mathematical object before choosing the exponent

An assignment to $k$ independent Boolean atoms is one of $2^k$ input rows. A Boolean function on those atoms is one of $2^{2^k}$ output tables. A unary predicate on $n$ labelled objects has $2^n$ interpretations; a binary relation has $2^{n^2}$. For example, two atoms give four valuations but sixteen functions. **Examination trap:** a question asking how many functions satisfy an implication is not asking how many assignments make the implication true.

### 2. Falsify an implication at a true antecedent and false consequent

The only failing pattern is $(A,B)=(1,0)$, so $\neg(A\Rightarrow B)\equiv A\land\neg B$. A false consequent with a false antecedent is not a counterexample. To refute $\forall x\forall y(R(x,y)\Rightarrow R(f(x),f(y)))$, exhibit a pair with the first relation true and the second false. The cyclic-successor example in Question 1 gives $(3,4)$, transformed into $(4,0)$. **Trap:** a few order-preserving pairs do not establish a universally order-preserving function.

### 3. Reverse an implication only by contraposition

The contrapositive $\neg B\Rightarrow\neg A$ is equivalent to $A\Rightarrow B$; the converse $B\Rightarrow A$ is not. Assignment $A=0,B=1$ distinguishes them. When chaining $p\Rightarrow q$ and $q\Rightarrow s$, derive $p\Rightarrow s$, not $s\Rightarrow p$. **Trap:** a relation or conditional does not become symmetric merely because both directions use the same objects.

### 4. Canonical minterms select true rows; maxterms exclude false rows

With three atoms, index $i=4p+2q+r$. At row 101 the minterm is $p\land\neg q\land r$ and the maxterm is $\neg p\lor q\lor\neg r$. The minterm is true only there; the maxterm is false only there. A canonical DNF lists true indices and a canonical CNF lists false indices. **Trap:** an equivalent expression can still be the wrong requested normal form, as in Questions 6 and 7.

### 5. Canonical size does not measure the size of every representation

Odd parity on $n\ge1$ bits has $2^{n-1}$ false rows and therefore that many canonical CNF clauses. Flipping one bit bijects false and true rows. An XOR circuit instead uses $n-1$ binary XOR gates. Auxiliary-variable CNF encodings are another representation again. **Trap:** do not interpret a short circuit as a one-clause CNF over the original atoms; state which variables and connectives the representation permits.

### 6. Entailment excludes premise-true, conclusion-false models

To prove $\Gamma\models C$, prove $\bigwedge\Gamma\land\neg C$ unsatisfiable. To refute it, give one complete valuation making every premise true and $C$ false. With $n$ disjoint forward-implication pairs and the conjunction of their converses as conclusion, countermodels number $3^n-2^n$. **Trap:** a valuation falsifying a premise cannot refute the argument; a majority of supporting valuations cannot prove validity.

### 7. The same quantified variable must retain the same chosen object

Evaluate functions from their innermost arguments outward, then relation membership, then connectives, then quantifiers. In Question 2, testing $R(f(y),0)$ requires computing $f(y)$, not substituting $y$ directly. A universal formula is a conjunction over all assignments to its bound variable. **Trap:** finding one successful quantified instance proves an existential, not a universal; free variables remain fixed by the external assignment.

### 8. Quantifier order determines witness dependence

$\forall x\exists yR(x,y)$ permits a different $y$ for each $x$. $\exists y\forall xR(x,y)$ requires one shared witness. A full column in a finite relation matrix establishes the second; all nonempty rows establish the first. The identity matrix on two objects satisfies only the first. **Trap:** swapping unlike quantifiers is not a harmless reordering of loops or symbols.

### 9. Negate every binder and the body, keeping scope explicit

$\neg\forall x\exists yR(x,y)\equiv\exists x\forall y\neg R(x,y)$. This asks for one entirely empty row. Merely writing $\forall x\exists y\neg R(x,y)$ asks for a zero somewhere in every row and is not equivalent. The matrix with rows 00 and 11 separates the two. **Trap:** “one failing pair exists” is generally too weak to negate an existential witness requirement inside a universal input requirement.

### 10. Restricted universal and existential claims use different connectives

“Every $S$-object has $P$” means $\forall x(S(x)\Rightarrow P(x))$; “some $S$-object has $P$” means $\exists x(S(x)\land P(x))$. If no $S$-objects exist, the first is true and the second false. **Trap:** an existential implication may be satisfied by an object outside $S$, and a universal conjunction wrongly asserts that every domain object belongs to $S$.

### 11. Expand unique existence into existence plus uniqueness

$\exists!yR(x,y)$ requires one target and forbids a second distinct target for that same input. Its negation means zero targets or at least two distinct targets. Sharing a target between different inputs is allowed. On an $n$-object domain, unique existence for every input gives $n^n$ function graphs. **Trap:** at-most-one is vacuously true on an empty row and does not imply existence or injectivity.

### 12. Use rows for totality and columns for surjectivity or shared witnesses

For $a$ inputs and $b\ge1$ targets, nonempty rows give $(2^b-1)^a$ relations; singleton rows give $b^a$ function graphs. On a finite square domain, requiring distinct targets changes the latter count to $n!$. **Trap:** a constant function is total despite its many empty columns. A full column is a common witness, not a statement that the function is injective.

### 13. Prove independence before multiplying local choices

Disjoint implication pairs give three allowed states per pair; disjoint conjunction pairs have three failed states per pair. Thus the corresponding counts are $3^n$ and $4^n-3^n$. Shared atoms invalidate these products. For example, $(p\land q)\lor(p\land r)$ has three true assignments among eight, whereas two disjoint conjunctions have seven among sixteen. **Trap:** repeated occurrences of an atom are not independent copies of that atom.

### 14. Remove overlap when counting existential witnesses

At least one empty row has count $2^{n^2}-(2^n-1)^n$. Choosing a named empty row and multiplying by unrestricted choices counts a matrix once per empty row. Exactly $t$ empty rows instead has $\binom nt(2^n-1)^{n-t}$ interpretations. **Trap:** “there exists a witness” does not make that witness unique or part of the object being counted. Use complement counting, disjoint cases, or inclusion-exclusion.

### 15. Treat empty-domain changes as changes of assumptions

On an explicitly permitted empty domain, universals are true and existentials false. On a nonempty $n$-object domain, predicates with some true and some false object number $2^n-2$. At $n=0$, the two excluded extreme subsets coincide, so that subtraction is invalid and the actual count is zero. **Trap:** substituting outside a formula's stated range does not extend its proof; a language with object-denoting constants also needs objects to interpret those constants.

### 16. Keep scope, capture and assignment conventions separate

In $P(x)\land\forall xQ(x)$, the first occurrence of $x$ remains free. Substituting $y$ for free $x$ in $\forall yR(x,y)$ requires renaming the binder first, yielding $\forall zR(y,z)$ with fresh $z$. Simultaneously swapping $x,y$ in $R(x,y)$ gives $R(y,x)$; sequential replacements can instead give $R(x,x)$. **Trap:** matching letters on the page do not imply matching binders or identical substitution operations.

### 17. Separate finite verification from a general proof

Enumeration of all relations on a fixed three-object domain checks exactly 512 matrices, not every first-order structure. General counting formulas need size-independent bijections or proofs. Finite injective self-maps are surjective, but $k\mapsto k+1$ on the natural numbers is injective and not surjective. **Trap:** passing small finite tests cannot establish a theorem whose assumptions allow an infinite domain. State the structure class and give a general argument or an explicit countermodel.
