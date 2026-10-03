## Teaching through formulas and conceptual decisions

### A Boolean expression is a truth table under a stated variable order

An$n$-input function has$2^n$ input rows and$2^{2^n}$ possible output tables. A minterm selects one row with a positive literal for a1 input and a complemented literal for a0 input. A maxterm rejects one row with the opposite polarity rule. With variable order$a,b,c$ and$a$ most significant, row101 has minterm$a\neg b c$ and maxterm$\neg a\lor b\lor\neg c$.

### Cofactors reduce dimensionality

Set$a=0$ and$a=1$ to obtain$F_0,F_1$. Shannon decomposition is $F=\neg a F_0\lor aF_1$. If the cofactors agree, the function does not depend on$a$. Boolean difference is$F_0\oplus F_1$, describing sensitivity to an$a$ transition while other inputs are fixed. Existential elimination is$F_0\lor F_1$ and universal elimination is$F_0\land F_1$; these operations answer different questions from ordinary substitution.

### Use algebraic identities only inside their semantics

Absorption$a\lor ab=a$ follows from the two$a$ cases. The consensus identity$ab\lor\neg a c\lor bc=ab\lor\neg a c$ says that$bc$ does not change the steady-state truth table; it does not say that the extra term has no timing benefit. XOR uses parity: repeated terms cancel and AND distributes over XOR, but ordinary OR does not behave as arithmetic addition modulo2.

To form the algebraic normal form, determine coefficients over the two-element field. For two inputs, the constant coefficient is$F(0,0)$, linear coefficients compare their one-input rows to the constant, and the product coefficient is the XOR of all four output rows. Care-set equivalence is equality only on specified rows; unconstrained outputs are independent bits when counting legal completions.

## Formula and conceptual problem bank

### Question 1. Count function tables

How many Boolean functions of three labeled inputs exist?

**A.** 8

**B.** 64

**C.** 128

**D.** 256

**Answer: D.**

Three inputs have eight distinct assignments. Each row chooses its output bit independently, so there are$2^8=256$ tables. Eight counts rows, not functions. Expression syntax can describe the same function in many ways and is not what this count measures.

### Question 2. Canonical maxterm polarity

With variable order$a,b,c$, which maxterm is false exactly at input101?

**A.** $a\lor\neg b\lor c$

**B.** $\neg a\lor b\lor\neg c$

**C.** $a\land\neg b\land c$

**D.** $\neg a\land b\land\neg c$

**Answer: B.**

A maxterm is an OR of literals each false at the target row. At101, choose$\neg a$, $b$ and$\neg c$. Their disjunction is false there and true on every other row. OptionC is the corresponding minterm, true at101, not a maxterm false there.

### Question 3. Absorption and distribution

Simplify $(a\lor b)\land(a\lor\neg b)$.

**A.** $a$

**B.** $b$

**C.** $a\lor b$

**D.** $0$

**Answer: A.**

Distribute in the Boolean lattice: $(a\lor b)(a\lor\neg b)=a\lor(b\land\neg b)=a$. A cofactor check gives0 when$a=0$ and1 when$a=1$, independent of$b$. Treating OR as ordinary addition would not preserve this identity.

### Question 4. Consensus term

Which term is redundant in the steady-state SOP$ab\lor\neg a c\lor bc$?

**A.** $ab$

**B.** $\neg a c$

**C.** $bc$

**D.** All terms.

**Answer: C.**

If$bc=1$, both$b$ and$c$ are1. For$a=1$, the$ab$ term is1; for$a=0$, the$\neg a c$ term is1. Thus every row covered by$bc$ is already covered by another term. Removing either main term loses rows not covered by the other terms. Timing hazards are a separate implementation question.

### Question 5. XOR cancellation

Simplify $a\oplus b\oplus a\oplus1$.

**A.** $b$

**B.** $\neg b$

**C.** $a\lor b$

**D.** $0$

**Answer: B.**

XOR is associative and each duplicated$a$ cancels to0. The remaining$b\oplus1$ is$\neg b$. OR would not permit this cancellation; the identity uses parity arithmetic. Neither the result nor its dependence includes$a$.

### Question 6. Shannon reconstruction

The$a$-cofactors are$F_0=b$ and$F_1=c$. Which expression represents$F$?

**A.** $ab\lor\neg a c$

**B.** $\neg a b\lor ac$

**C.** $b\lor c$

**D.** $bc$

**Answer: B.**

Shannon attaches the0 cofactor to$\neg a$ and the1 cofactor to$a$. Thus$F=\neg a b\lor ac$. OptionA exchanges the control polarity and chooses the wrong data input in each$a$ case. C andD discard the selector and cannot reproduce both arbitrary cofactors.

### Question 7. Sensitivity

For$F=\neg a b\lor ac$, what is the Boolean difference with respect to$a$?

**A.** $b\lor c$

**B.** $bc$

**C.** $b\oplus c$

**D.** $a$

**Answer: C.**

The two cofactors are$b$ and$c$, so their XOR is$b\oplus c$. Changing$a$ affects the output exactly when those two possible data values differ. OR would incorrectly mark sensitivity when$b=c=1$, where both cofactor outputs are identical.

### Question 8. Existential elimination

For$F=ab\lor\neg a c$, what is$\exists a\,F$?

**A.** $b\land c$

**B.** $b\lor c$

**C.** $b\oplus c$

**D.** $F$

**Answer: B.**

The cofactor at0 is$c$ and at1 is$b$. Some$a$ value makes$F$ true exactly when at least one cofactor is true, giving$b\lor c$. AND is universal elimination and would require both choices of$a$ to work. XOR instead asks whether the choices differ.

### Question 9. Algebraic normal form

Which XOR-polynomial represents$a\lor b$?

**A.** $a\oplus b$

**B.** $a\oplus b\oplus ab$

**C.** $ab$

**D.** $1\oplus ab$

**Answer: B.**

At00 the output is0, at01 and10 it is1, and at11 the expression$1\oplus1\oplus1$ is1. The product term repairs XOR at the both-one row. OptionA is exclusive OR and fails there; C is AND and misses the single-one rows.

### Question 10. Don’t-care completions

A four-input function has five unconstrained output rows and every other row fixed consistently. How many complete tables satisfy the specification?

**A.** 5

**B.** 16

**C.** 32

**D.** 2048

**Answer: C.**

Each of the five unspecified outputs is an independent bit, producing$2^5=32$ completions. The remaining eleven fixed rows add no choices. Eleven is not the free-row count, so2048 exponentiates the wrong set. Consistency of all fixed requirements is assumed; a contradictory fixed row would give zero.

### Question 11. Monotonicity through cofactors

For a Boolean function$F$, which condition is equivalent to being nondecreasing in input$a$?

**A.** $F_0=F_1$ only

**B.** $F_0\Rightarrow F_1$ for every assignment of other inputs

**C.** $F_1\Rightarrow F_0$

**D.** $F_0\oplus F_1=1$ everywhere

**Answer: B.**

Changing$a$ from0 to1 must never change the output from1 to0. That is exactly the implication from the0 cofactor to the1 cofactor pointwise. Equal cofactors are sufficient but unnecessarily strong. The reverse implication describes nonincreasing behavior. Always unequal cofactors can include prohibited falling transitions.

### Question 12. Self-dual tables

How many self-dual Boolean functions of three inputs satisfy $F(\neg x)=\neg F(x)$?

**A.** 4

**B.** 8

**C.** 16

**D.** 128

**Answer: C.**

The eight input rows form four complementary pairs. Choose one output bit per pair freely; the partner output is then its complement. Thus there are$2^4=16$ functions. No row equals its own bitwise complement for a positive input count, so no impossible self-pair occurs.

<!-- CHALLENGE-BANK -->

### Question 13. Challenge: Count monotone three-input functions

How many Boolean functions of three inputs are nondecreasing in every input?

**A.** 8

**B.** 16

**C.** 20

**D.** 256

**Answer: C.**

A monotone function is determined by the antichain of its minimal true subsets in the three-element subset lattice. Count antichains: one empty antichain, eight single-member choices, nine incomparable pairs, and two incomparable triples. The pairs consist of three pairs of singletons, three pairs of two-element sets, and three singleton/complement-pair choices. The triples are all three singletons or all three two-element sets. Total1+8+9+2=20; no larger antichain exists. The empty and bottom-containing cases include both constant functions.

### Question 14. Challenge: Self-dual care constraints

A self-dual function on three inputs has$F(000)=0$ and$F(111)=1$ fixed. No other rows are specified. How many completions exist?

**A.** 4

**B.** 8

**C.** 16

**D.** 64

**Answer: B.**

The eight rows form four complement pairs. The given values constrain the same pair consistently, leaving three independent pairs. Choose one bit in each remaining pair and force its complement in the partner row, giving$2^3=8$. Treating the two given rows as two independent pair constraints would give4; treating all six remaining rows as independent ignores self-duality.

## Applicable formulas and examination notes

### 1. Rows versus functions

$n$ inputs give$2^n$ rows and$2^{2^n}$ functions. A constraint on$r$ otherwise independent outputs reduces the free bit count accordingly. Count tables rather than syntactic expressions.

### 2. Canonical polarity

A minterm matches a row: positive for1, negative for0. A maxterm rejects a row: negative for1, positive for0. For101, the minterm is$a\neg b c$ and the maxterm is$\neg a\lor b\lor\neg c$.

### 3. Absorption

Use$a\lor ab=a$ and$(a\lor b)(a\lor\neg b)=a$. Verify by the two$a$ cases if a longer expression hides the pattern. Boolean distributivity has two dual forms and is not ordinary numeric multiplication over addition.

### 4. Consensus

In$ab\lor\neg a c\lor bc$, the$bc$ term is truth-table redundant. It can still cover a transient static hazard in a two-level realization. Functional equivalence does not prove equal delay or hazard behavior.

### 5. XOR field arithmetic

Repeated XOR terms cancel, and$a\lor b=a\oplus b\oplus ab$. The product term matters at11. Negation is XOR with1, not deletion of a literal.

### 6. Shannon polarity

$F=\neg aF_0\lor aF_1$. Write the cofactor subscripts beside their control literals before mapping a selector. Equal cofactors remove dependence on$a$; different cofactors do not necessarily make$a$ monotone.

### 7. Boolean difference

$\partial_aF=F_0\oplus F_1$ identifies settings where changing$a$ changes$F$. This is a Boolean sensitivity function, not a real derivative or the OR of both cofactors.

### 8. Quantified elimination

Existential elimination uses$F_0\lor F_1$; universal elimination uses$F_0\land F_1$. A single input witness is enough for the first, while both values must work for the second. Cofactor substitution itself is neither operation.

### 9. Algebraic normal form

All coefficients are Boolean and the sum operation is XOR. The constant coefficient is the all-zero output. For two inputs, the product coefficient is the XOR of all four table values; check the11 row after determining the linear coefficients.

### 10. Care-set equivalence

Two circuits meet a partial specification if they agree on every cared-about row. Five independent don’t-care outputs admit32 completions. An implementation that differs on a care row fails even if it is simpler or agrees on most inputs.

### 11. Unateness test

Nondecreasing in$a$ means$F_0\Rightarrow F_1$; nonincreasing means$F_1\Rightarrow F_0$. Equal cofactors satisfy both and mean independence. A syntactic complemented occurrence is not by itself a semantic monotonicity proof.

### 12. Self-dual pair count

For$n\ge1$, complementary input rows form$2^{n-1}$ pairs, so self-dual tables number$2^{2^{n-1}}$. One output per pair is free and the other forced opposite. Complementing only an output is not the self-dual condition.

<!-- BOUNDARY-NOTES -->

### 13. Duality versus complement

The dual exchanges AND with OR and zero with one while retaining literal polarities. Complementing additionally negates the result and applies De Morgan to its literals. These transformations answer different algebra questions and coincide only under special structure.

### 14. Cube coverage

A product term fixing $k$ of $n$ inputs covers $2^{n-k}$ rows. A contradictory term containing both a variable and its complement covers none. Overlapping product terms need union accounting rather than simple addition of coverage sizes.

### 15. Universal elimination

Universal elimination over one input is the AND of its two cofactors. If $F_0=b$ and $F_1=c$, it is $bc$, while existential elimination is $b\lor c$. Do not confuse a universal guarantee with the existence of one selecting value.

### 16. Equivalence miter

Two complete Boolean implementations are equivalent exactly when their XOR miter is zero on every input. Under a care set, test the miter only on cared-about rows. A single legal row with miter one is a complete counterexample.
