## Teaching through formulas and conceptual decisions

### Distinguish the three objects being counted

A truth assignment supplies one bit per atom. With $n$ distinct atoms there are $2^n$ assignments. A Boolean function supplies one output bit for each assignment, so there are $2^{2^n}$ functions. A formula is a syntactic expression representing a function; many different formulas represent the same function. Consequently “how many formulas?” is not answered by the function count unless the allowed syntax and size are specified.

Suppose a formula $G$ has $g$ satisfying rows. Requiring $G\Rightarrow F$ to be valid forces the output of $F$ to one on those rows; its other $2^n-g$ outputs are free. Thus there are $2^{2^n-g}$ possible functions. Requiring $F\Rightarrow H$ forces zero outside $H$. If both conditions are required, first test whether $G\Rightarrow H$ is valid. A row satisfying $G$ but not $H$ would force both output values and makes the count zero. Otherwise, if $H$ has $h$ true rows, exactly $h-g$ rows are free and the answer is $2^{h-g}$.

This method converts a verbal validity condition into forced bits. It is more reliable than counting examples of formulas. On each row write “forced one,” “forced zero” or “free,” then multiply the independent choices.

### Count models by conditioning on a useful atom

For $F=(p\Rightarrow q)\land(q\lor r)$, split on $q$. When $q=1$, both factors hold and there are four choices for $p,r$. When $q=0$, the first factor requires $p=0$ and the second requires $r=1$, adding one row. Hence five of eight assignments satisfy the formula. The cases are disjoint, so addition is justified. A variable absent from the reduced formula still multiplies a count by two if it remains part of the specified assignment domain.

An implication is false on antecedent-true/consequent-false rows. For a chain $p_1\Rightarrow p_2,\ldots,p_{n-1}\Rightarrow p_n$, any true bit forces all later bits true. The satisfying strings are a prefix of zeros followed by a suffix of ones, with $n+1$ possible boundaries.

### Canonical forms are row encodings

Fix atom order before numbering rows. For $F=(p\oplus q)\lor r$ with $p$ as the most significant bit, true rows are $1,2,3,4,5,7$ and false rows are $0,6$. A true row contributes a minterm with positive literals at ones; a false row contributes a maxterm with negative literals at ones. Therefore its canonical DNF has six three-literal terms, and its canonical CNF has two three-literal clauses. A simplified equivalent expression can have fewer terms without being the requested canonical representation.

### Quantifiers become row or column constraints

For a binary relation on a fixed labeled domain of size $m$, use an $m$-by-$m$ Boolean matrix. There are $2^{m^2}$ possible relations. The sentence $\forall x\exists y\,R(x,y)$ says each row is nonempty: each row has $2^m-1$ choices, independently, giving $(2^m-1)^m$ models. The sentence $\forall x\exists!y\,R(x,y)$ says each row has exactly one one and gives $m^m$ models, the number of self-functions.

By contrast, $\exists y\forall x\,R(x,y)$ requires at least one full column. Full-column events overlap, so simply multiplying the choices for a single column by $m$ overcounts. Inclusion-exclusion gives:

$$\sum_{j=1}^{m}(-1)^{j+1}\binom{m}{j}2^{m(m-j)}.$$

For $m=3$, this is $3\cdot64-3\cdot8+1=169$, while the nonempty-row condition gives $7^3=343$. The different counts make the witness-dependency distinction numerically visible.

### How to solve a conceptual multiple-choice question

To refute an entailment, construct a model satisfying every premise and falsifying the proposed conclusion. An arbitrary false conclusion is insufficient if a premise is also false. To refute a quantifier swap, a two-object relation matrix is often enough. To negate a formula, push the negation through one outer operator at a time. These methods are executable procedures; the proofs and model semantics in the detailed lesson establish why they work.

## Formula and conceptual problem bank

### Problem 1 — Assignments versus functions

**Question.** For four independent propositional atoms, what are the numbers of assignments and Boolean functions, respectively?

**Options.** A: $(4,16)$; B: $(16,256)$; C: $(16,65536)$; D: $(256,65536)$.

**Correct option: C.**

**Solution.** Each of four atoms has two choices, giving $2^4=16$ input rows. Each row has an independently chosen output bit, giving $2^{16}=65536$ functions. Option B incorrectly uses $2^{2n}$; D confuses an input assignment with a pair of assignments. Nothing here counts distinct syntactic formulas, whose number requires a separate syntax bound.

### Problem 2 — Count a constrained truth table

**Question.** How many assignments to $p,q,r$ satisfy $(p\Rightarrow q)\land(q\lor r)$?

**Options.** A: 3; B: 4; C: 5; D: 6.

**Correct option: C.**

**Solution.** For $q=1$, the implication is true and the disjunction is true, leaving two free bits and four rows. For $q=0$, the implication forces $p=0$ and the disjunction forces $r=1$, leaving one row. Add the disjoint counts to obtain five. Counting each factor separately and multiplying would be invalid because the factors share $q$.

### Problem 3 — A logically constrained unknown function

**Question.** How many functions $F(p,q,r)$ make $(p\Rightarrow q)\Rightarrow F$ a tautology?

**Options.** A: 2; B: 4; C: 6; D: 64.

**Correct option: B.**

**Solution.** The inner implication is false only at $p=1,q=0$, with either value of $r$. It is true on the other six rows, where $F$ must equal one. The two remaining outputs are independent and unconstrained, so there are $2^2=4$ functions. Six is the number of forced rows, not the number of permitted functions.

### Problem 4 — Two-sided function constraints

**Question.** Require $G\Rightarrow F$ and $F\Rightarrow H$ to be valid, where $G=p\land q$ and $H=p\lor r$. How many $F(p,q,r)$ are possible?

**Options.** A: 0; B: 4; C: 16; D: 64.

**Correct option: C.**

**Solution.** Every row satisfying $G$ satisfies $H$ because $p=1$, so the constraints are compatible. There are two true rows of $G$ and six true rows of $H$. The outputs are forced one on the first two, forced zero outside the six, and free on the four-row difference. Thus the count is $2^4=16$. The general exponent is the number of free outputs, not all allowed-one rows.

### Problem 5 — Detect incompatible constraints

**Question.** Require $p\Rightarrow F$ and $F\Rightarrow q$ to be valid for a function of $p,q$. How many functions satisfy both?

**Options.** A: 0; B: 1; C: 2; D: 4.

**Correct option: A.**

**Solution.** At the row $p=1,q=0$, the first requirement forces $F=1$ and the second forces $F=0$. One conflicting row makes the whole specification impossible. A formula such as $p\land q$ satisfies the upper constraint but violates the lower one on that row; $p\lor q$ has the opposite problem. Check compatibility before exponentiating a proposed number of free rows.

### Problem 6 — A chain of implications

**Question.** How many assignments to six atoms satisfy $\bigwedge_{i=1}^{5}(p_i\Rightarrow p_{i+1})$?

**Options.** A: 6; B: 7; C: 12; D: 32.

**Correct option: B.**

**Solution.** A one followed later by a zero would force a forbidden one-to-zero transition. Therefore each valid string is zeros followed by ones. The boundary can occur before the first position, after the sixth, or at any of the five internal gaps: seven choices. The all-zero and all-one strings are valid and explain why the answer is one more than the atom count.

### Problem 7 — Canonical row indices

**Question.** With atom order $p,q,r$, which is the canonical minterm set of $(p\oplus q)\lor r$?

**Options.** A: $\{1,2,3,4,5,7\}$; B: $\{0,6\}$; C: $\{1,3,5,7\}$; D: $\{2,3,4,5\}$.

**Correct option: A.**

**Solution.** All four rows with $r=1$ satisfy the formula, yielding indices one, three, five and seven. For $r=0$, unequal $p,q$ give indices two and four. Their union is the six indices in A. B lists the false rows, while C and D omit one of the two satisfying mechanisms.

### Problem 8 — Canonical CNF polarity

**Question.** What is the canonical CNF of $p\Rightarrow q$ on the two atoms $p,q$?

**Options.** A: $p\lor\neg q$; B: $\neg p\lor q$; C: $p\land q$; D: $\neg p\land q$.

**Correct option: B.**

**Solution.** The only false row is $(1,0)$. Its maxterm must be false there, so the first literal is $\neg p$ and the second is $q$. Their disjunction is false exactly on that row and true on the other three. Minterm signs run in the opposite direction; confusing the two procedures produces D instead of the required maxterm.

### Problem 9 — Negation of nested quantifiers

**Question.** Which formula negates $\forall x\exists y[P(x,y)\Rightarrow\forall z\,Q(y,z)]$?

**Options.** A: $\exists x\forall y[P(x,y)\land\exists z\neg Q(y,z)]$; B: $\forall x\exists y[P(x,y)\land\neg Q(y,z)]$; C: $\exists x\exists y[\neg P(x,y)\lor\exists z\neg Q(y,z)]$; D: $\exists z\forall x\forall y[P(x,y)\land\neg Q(y,z)]$.

**Correct option: A.**

**Solution.** Negation flips the outer universal to existential and the next existential to universal. The negated implication becomes its unchanged antecedent conjoined with the negated consequent. Finally the negated universal over $z$ becomes an existential with negated body. Its witness may depend on $y$. D incorrectly requires one shared witness before the other variables are chosen; B leaves a variable free.

### Problem 10 — Quantified relation count

**Question.** On a labeled three-object domain, how many binary relations satisfy $\forall x\exists y\,R(x,y)$?

**Options.** A: 27; B: 169; C: 343; D: 512.

**Correct option: C.**

**Solution.** Each relation is a three-by-three Boolean matrix. Every row must contain at least one one and therefore has seven choices. Rows are independently chosen, giving $7^3=343$. The 27 count requires exactly one one per row; 169 requires a common full column; 512 allows empty rows as well.

### Problem 11 — A common witness and overlapping events

**Question.** On the same domain, how many relations satisfy $\exists y\forall x\,R(x,y)$?

**Options.** A: 64; B: 169; C: 192; D: 343.

**Correct option: B.**

**Solution.** There are three full-column events. Fixing one full column leaves six free bits, so each event has 64 models. Fixing two leaves three free bits, so each pairwise intersection has eight. Fixing all three gives one model. Inclusion-exclusion yields $3(64)-3(8)+1=169$. The naive 192 count counts relations with multiple full columns more than once.

### Problem 12 — Exactly one successor

**Question.** On a labeled four-object domain, how many relations satisfy $\forall x\exists!y\,R(x,y)$?

**Options.** A: 16; B: 24; C: 256; D: 65536.

**Correct option: C.**

**Solution.** Each of four rows must select exactly one of four columns. Independent choices give $4^4=256$. This need not select different columns for different rows. If distinctness were imposed as injectivity, the answer would instead be $4!=24$. The 65536 answer counts all four-by-four Boolean matrices without the single-successor restriction.

### Problem 13 — Valid consequence

**Question.** Assume $p\lor q$, $p\Rightarrow r$ and $q\Rightarrow r$. Which conclusion must hold?

**Options.** A: $p\land q$; B: $p\Leftrightarrow q$; C: $r$; D: $\neg r$.

**Correct option: C.**

**Solution.** If $p$ is true, its implication forces $r$; if $q$ is true, the other implication does. The disjunction ensures at least one case. The assignment $p=1,q=0,r=1$ satisfies all premises and refutes both A and B. D contradicts the forced conclusion. This explicitly tests the premises rather than using arbitrary assignments as purported counterexamples.

### Problem 14 — Exactly one is stronger than at most one

**Question.** Which formula expresses exactly one object satisfying $P$?

**Options.** A: $\forall x\forall y((P(x)\land P(y))\Rightarrow x=y)$; B: $\exists x[P(x)\land\forall y(P(y)\Rightarrow y=x)]$; C: $\exists xP(x)$; D: $\forall xP(x)$.

**Correct option: B.**

**Solution.** B supplies a witness and forces every other witness to be equal to it. A permits no witnesses and expresses at most one; C allows several and expresses at least one. D requires the entire domain to satisfy the predicate and has no uniqueness requirement on domains with multiple objects. Testing zero, one and two satisfying objects separates all four alternatives.

### Problem 15 — Quantifier distribution

**Question.** Which equivalence is valid for every interpretation on a nonempty domain?

**Options.** A: $\forall x(P\lor Q)\Leftrightarrow(\forall xP)\lor(\forall xQ)$; B: $\exists x(P\land Q)\Leftrightarrow(\exists xP)\land(\exists xQ)$; C: $\forall x(P\land Q)\Leftrightarrow(\forall xP)\land(\forall xQ)$; D: $\forall x\exists yR\Leftrightarrow\exists y\forall xR$.

**Correct option: C.**

**Solution.** Every object satisfies both predicates exactly when every object satisfies each predicate separately. A two-object domain with $P$ true only at the first object and $Q$ only at the second refutes A and B. Equality on that domain refutes D: each object has its own equal witness, but there is no witness equal to both. Distribution rules must preserve whether witnesses are shared.

### Problem 16 — Capture-free substitution

**Question.** Substitute free $x$ by $y$ in $\forall yR(x,y)$. Which result preserves the intended free variable?

**Options.** A: $\forall yR(y,y)$; B: $\forall zR(y,z)$ with fresh $z$; C: $\forall xR(x,y)$; D: $\exists zR(y,z)$.

**Correct option: B.**

**Solution.** Rename the bound $y$ to fresh $z$ before inserting the formerly free replacement $y$. Then the replacement remains free and the old bound occurrences remain bound to $z$. A captures the inserted variable, C binds the wrong object, and D changes the quantifier. On an equality relation over two objects, the naive result and the correctly substituted open formula have visibly different assignment behavior.

### Problem 17 — Count false implication rows

**Question.** Count assignments to five atoms $p,q,r,s,t$ falsifying $(p\land q)\Rightarrow(r\lor s)$.

**Options.** A: 1; B: 2; C: 4; D: 8.

**Correct option: B.**

**Solution.** Falsity requires $p=q=1$ and $r=s=0$. The fifth atom $t$ is not used by the formula but remains part of the specified assignment domain, so it has two independent choices. There are two false rows. Forgetting the unused atom produces A; treating a required bit as free produces C or D.

### Problem 18 — Minimal refutation size

**Question.** What is the smallest nonempty domain permitting $\forall x(P(x)\lor Q(x))$ true but $(\forall xP(x))\lor(\forall xQ(x))$ false?

**Options.** A: 1; B: 2; C: 3; D: No finite domain.

**Correct option: B.**

**Solution.** On a singleton, the first condition says that its sole object satisfies at least one predicate, which makes the corresponding universal true. Thus one object cannot refute the implication. With two objects, let only the first satisfy $P$ and only the second satisfy $Q$. Each satisfies the disjunction, yet each universal predicate fails on the other object. This both constructs a witness model and proves minimality.

<!-- CHALLENGE-BANK -->

### Question 19. Challenge: Count two-sided logical specifications

For four Boolean atoms, $G=p\land q$ and $H=p\lor r$. How many functions$F(p,q,r,s)$ satisfy both$G\Rightarrow F$ and$F\Rightarrow H$ on every row?

**A.** 16

**B.** 64

**C.** 256

**D.** 4096

**Answer: C.**

First check compatibility: every row with$G=1$ has$p=1$ and therefore$H=1$. Among sixteen rows,$G$ is true on four, while$H$ is true on twelve. Thus four outputs are forced1, four forced0, and eight free. The count is$2^8=256$. Free rows are the difference of the two true sets, not the full$H$ set. The otherwise unused atom$s$ doubles each relevant row count and cannot be discarded when counting tables.

### Question 20. Challenge: Mix row and column constraints

On a labeled three-object domain, how many relations satisfy both$\forall x\exists yR(x,y)$ and$\exists y\forall xR(x,y)$?

**A.** 169

**B.** 192

**C.** 343

**D.** 512

**Answer: A.**

A full column already supplies an outgoing witness in every row, so the second condition implies the first. Count only matrices with at least one full column. Three single-column events each leave six bits free and contribute64; three two-column intersections each leave three bits free and contribute8; the all-column intersection contributes1. Inclusion-exclusion gives$3(64)-3(8)+1=169$. Multiplying counts of the two conditions would incorrectly treat them as independent constraints.

## Applicable formulas and examination notes

### 1. Recognize the counting unit before exponentiating

Use $2^n$ for assignments and $2^{2^n}$ for unrestricted functions. For three atoms these are eight and 256. A formula-size question needs an additional syntactic bound; neither number counts expressions automatically.

### 2. Convert validity constraints into forced outputs

For $G\Rightarrow F$, force ones on the true rows of $G$. If there are $g$ such rows, use $2^{2^n-g}$. For $F\Rightarrow H$, force zeros outside $H$. With both constraints, check $G\Rightarrow H$ first; then use $2^{h-g}$. A single conflicting row gives zero functions.

### 3. Count implication failures rather than all rows

The only failure is antecedent one and consequent zero. In $(p\land q)\Rightarrow(r\lor s)$, four bits are fixed. Any additional unused specified atom doubles the number of false assignments.

### 4. Use disjoint cases on a shared atom

Condition on an atom connecting the factors, evaluate each branch, and add. In $(p\Rightarrow q)\land(q\lor r)$ the branches contribute four and one. Multiplying separate factor counts fails because their choices are dependent.

### 5. Canonical forms have opposite literal polarity

A minterm uses a positive atom for a row bit one; a maxterm uses its negation. Canonical DNF uses true rows and canonical CNF false rows. A compact equivalent formula may fail an option asking specifically for canonical form.

### 6. A chain of implications has a boundary count

A chain of $n$ ordered atoms permits only zeros followed by ones and has $n+1$ models. Cyclic implications force every atom equal and therefore have two models when the cycle is nonempty.

### 7. Entailment counterexamples must preserve every premise

Test satisfiability of the premises conjoined with the negated conclusion. A witness refutes entailment. For $p\lor q$, $p\Rightarrow r$, $q\Rightarrow r$, setting $r=0$ forces $p=q=0$ and contradicts the disjunction; hence no witness exists.

### 8. Translate relation quantifiers to matrix constraints

On $m$ labeled objects, unrestricted binary relations number $2^{m^2}$; nonempty rows number $(2^m-1)^m$; exactly one one per row gives $m^m$; exactly one one per row and column gives $m!$. These answer different specifications.

### 9. A common witness creates overlapping full-column events

For at least one common successor, use inclusion-exclusion over full columns:
$$\sum_{j=1}^{m}(-1)^{j+1}\binom{m}{j}2^{m(m-j)}.$$
The three-object result is 169, not $3\cdot64$, because two-column and three-column overlaps must be corrected.

### 10. Negate one outer operator at a time

Use $\neg(A\Rightarrow B)\equiv A\land\neg B$, flip every crossed quantifier, and preserve the remaining scope. In $\neg\forall x\exists yR$, the result is $\exists x\forall y\neg R$, not a formula with the original witness order.

### 11. Distinguish the two valid distributions

Universals distribute over conjunction and existentials over disjunction. The reverse pair fails on a split-predicate two-object model. For movement past a fixed operand, also check that the bound variable is not free there and that the required domain convention holds.

### 12. Exactly one requires an existence clause

Combine a witness with the condition that every witness equals it. A pairwise uniqueness condition alone is true when there are no witnesses. A zero-witness model is therefore the fastest distractor test for “at most one” versus “exactly one.”

### 13. Restricted universals and existentials use different connectives

Write $\forall x(S(x)\Rightarrow P(x))$ and $\exists x(S(x)\land P(x))$. An empty restricted set makes the first true and the second false. An existential implication can be witnessed by an object outside the restriction and is generally wrong.

### 14. Rename before a potentially capturing substitution

In $\forall yR(x,y)$, replacing free $x$ by $y$ first requires a fresh bound name. Simultaneous substitutions operate on original positions; sequential substitutions may overwrite earlier replacements. The distinction changes the resulting relation, not just its printed variable names.

<!-- BOUNDARY-NOTES -->

### 15. Empty-domain exceptions

The four movement laws for a variable absent from the other operand must track the quantifier and operator. On an empty domain, an existential side is false and a universal side true; moving a quantifier across an unrelated operand can therefore change a formula. For example, with an empty domain and a true closed $Q$, $(\exists xP(x))\lor Q$ is true while $\exists x(P(x)\lor Q)$ is false. Never use a nonempty-domain movement theorem after silently changing the domain.

### 16. Free variables and truth assignments

A first-order formula with $k$ free variables on an $m$-object domain has $m^k$ assignments to those variables once the structure is fixed. This is not a count of structures or Boolean truth tables. Bound variables contribute no free assignment choice; repeated free occurrences of one name share one value.

### 17. Finite and infinite models

A quantified claim can have an infinite model and no finite model, such as a strict relation where every object has a larger successor under suitable order axioms. A finite truth-table check does not decide arbitrary first-order validity. Use the stated domain class in a conceptual question.
