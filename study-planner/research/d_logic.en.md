# Propositions, Predicates, and Logical Equivalence

**Discrete Mathematics · first-pass chapter · English edition**

This chapter develops classical, two-valued logic from syntax to semantics and then to careful first-order reasoning. It is a complete teaching unit for the chapter boundary shown in the weekly plan. Set theory, formal natural-deduction systems, and induction receive their own chapters. The aim here is to make every definition, law, proof obligation, and edge case in this boundary explicit without padding the lesson with repeated explanations.

## 1. Course selection and how the sources were combined

The source register screened 13 logic-related course entries from MIT, Stanford, UC Berkeley, Carnegie Mellon, Cornell, Princeton, Illinois, Oxford, and ETH Zurich. Several entries are different versions of a course, and some were only available as a syllabus or catalogue; those were not counted as studied texts. The four texts below were selected for **this** chapter because each fills a different need; their relevant pages or complete slide decks were read, and disagreements were checked before the lesson was written.

| University and course | Material actually reviewed | Contribution used here |
| --- | --- | --- |
| MIT, 6.042J *Mathematics for Computer Science*, Leighton and van Dijk (2010) | Chapter 1, all 17 substantive pages of the 19-page PDF | Fundamental truth conditions, implications, quantifier order, validity, and satisfiability |
| Stanford, CS103 *Mathematical Foundations of Computing*, Trevisan (2014) | Lecture 9, all eight pages | Formula syntax, equivalence across variable sets, and free versus bound occurrences |
| UC Berkeley, CS70 *Discrete Mathematics and Probability Theory*, Shahzar and Wu (Summer 2024) | Note 1, all 14 pages and the relation diagrams | Propositional and first-order examples, restricted quantifiers, and inference patterns |
| Carnegie Mellon, 15-311 *Logic and Mechanized Reasoning*, Heule (2026) | Entire propositional and first-order slide decks, including repeated animation frames | Recursive syntax, model semantics, satisfiability, substitution, finite versus infinite models, and quantifier movement |

The source comparison is bounded by material that could be accessed and inspected. It does not establish that these are the four best courses among every course ever offered. Princeton and Illinois had directly accessible logic lectures but their complete relevant sequences were not reviewed; Oxford and ETH Zurich lacked verified open chapter texts in this audit. MIT and Berkeley sometimes use informal explanatory wording; the formal semantics below control any disagreement. CMU's “true or false?” slides include deliberately false prompts before their answers, so the response slides were read as part of the same argument. Full source links and precise review limits are in [References](#references).

## 2. Foundations: syntax and meaning

### 2.1 The language being studied

A **proposition** has a definite truth value, true or false, under a stated interpretation. “The integer 7 is prime” is a proposition. “Is 7 prime?” is a question, and “x is prime” is an **open predicate** until x has been assigned or quantified. A mathematical formula can be syntactically well formed without having a truth value independent of an assignment: P(x) is a formula, while ∀x P(x) is a closed sentence.

In this chapter the truth-value set is {0,1}; 1 means true. An atomic propositional variable such as p receives a value from a **valuation** v. Compound formulas are built from atoms using ¬ (not), ∧ (and), ∨ (inclusive or), → (material implication), and ↔ (biconditional). Exclusive or, p ⊕ q, means exactly one operand is true. Parentheses state scope. When parentheses are omitted, do not rely on an unstated precedence convention in a difficult expression: rewrite the expression with explicit grouping first.

The semantics are determined recursively. For example, v(¬A)=1−v(A); v(A∧B)=1 exactly when both operands are 1; v(A∨B)=1 when at least one operand is 1; and v(A→B)=0 exactly when v(A)=1 and v(B)=0. Equivalently, A→B and ¬A∨B have the same value under every valuation. The following table makes the less intuitive operators explicit.

| p | q | ¬p | p∧q | p∨q | p→q | p↔q | p⊕q |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 | 1 | 1 | 1 | 0 |

The inclusive-or row p=q=1 matters. Everyday “or” can be exclusive; formal ∨ is inclusive unless a different connective is defined. Material implication is true when its antecedent is false. This is **vacuous truth**, not a claim that the consequent was caused by the antecedent.

### 2.2 Formulas, valuations, and exact comparisons

For a formula A, let Var(A) be its propositional variables. A valuation on Var(A) assigns 0 or 1 to each variable. When comparing formulas A and B that use different variables, evaluate both under every valuation on Var(A)∪Var(B). Thus p and p∧(q∨¬q) are equivalent even though only the latter mentions q.

A is **satisfiable** if at least one valuation makes it true; **valid** or a **tautology** if every valuation makes it true; and **unsatisfiable** or a **contradiction** if no valuation does. A and B are **logically equivalent**, written A ≡ B, if every common valuation gives equal values. A set of premises Γ **entails** C, written Γ ⊨ C, if no valuation makes all members of Γ true and C false. If Γ is finite, this is equivalent to validity of (∧Γ)→C and to unsatisfiability of (∧Γ)∧¬C.

These are different claims. A satisfiable formula need not be valid: p is satisfiable but false when p=0. The formulas p and ¬p are separately satisfiable, but their conjunction is not. The disjunction p∨¬p is valid even though neither disjunct is valid. A valid argument can have a conclusion that is false under some valuation: p ⊨ p, but p itself is not valid. Validity says what happens **when the premises are all true**.

### 2.3 The parse tree and a structural bound

Propositional syntax is recursive: each atom is a formula; if A is a formula, ¬A is a formula; and if A and B are formulas, so are (A∧B), (A∨B), (A→B), and (A↔B). The parse tree of (p∧¬q)→r has → at the root, ∧ and r as its children, and ¬ above q. Its structure determines which connective is evaluated first, independently of how a sentence happens to be spoken.

Let c(A) count connective occurrences, and let d(A) be the maximum number of connectives from a root to an atomic leaf. Atoms have c=d=0. Unary and binary construction obey

<div class="formula-block">c(¬A)=1+c(A), &nbsp; d(¬A)=1+d(A)<br>c(A◦B)=1+c(A)+c(B), &nbsp; d(A◦B)=1+max(d(A),d(B)).</div>

Here ◦ is any binary connective. **Claim:** c(A)≤2<sup>d(A)</sup>−1. Prove it by structural induction. For an atom both sides are zero. For ¬A, the induction hypothesis gives c(¬A)≤2<sup>d(A)</sup>≤2<sup>d(A)+1</sup>−1. For A◦B, each child depth is at most d(A◦B)−1; hence

<div class="formula-block">c(A◦B)≤1+(2<sup>d(A)</sup>−1)+(2<sup>d(B)</sup>−1)≤2<sup>d(A◦B)</sup>−1.</div>

The claim concerns syntax size versus tree depth, not truth or computational time. Replacing a formula by a more compact equivalent formula can change c and d while leaving its meaning unchanged.

## 3. Propositional reasoning in depth

### 3.1 Equivalence laws and why they hold

Every equivalence law is a statement about **all valuations**. It can be proved by a truth table, by already established equivalences, or by showing both implications. The most useful laws are

| Law | Equivalence |
| --- | --- |
| Double negation | ¬¬A ≡ A |
| De Morgan | ¬(A∧B) ≡ ¬A∨¬B; &nbsp; ¬(A∨B) ≡ ¬A∧¬B |
| Implication | A→B ≡ ¬A∨B |
| Contrapositive | A→B ≡ ¬B→¬A |
| Biconditional | A↔B ≡ (A→B)∧(B→A) |
| Distribution | A∧(B∨C) ≡ (A∧B)∨(A∧C), and its dual |
| Absorption | A∨(A∧B) ≡ A; &nbsp; A∧(A∨B) ≡ A |
| Identity | A∧1 ≡ A; &nbsp; A∨0 ≡ A |

For example, ¬(A→B) ≡ ¬(¬A∨B) ≡ A∧¬B. The intermediate step explains why merely negating the consequent is wrong. The converse B→A and inverse ¬A→¬B are equivalent to one another, but neither is generally equivalent to A→B. A countervaluation p=0, q=1 makes p→q true and q→p false.

Equivalence must be distinguished from **equisatisfiability**. Two formulas are equisatisfiable if either both have a model or neither does; they need not agree on every valuation. If z is a fresh variable, F=p∧q and G=(z↔(p∧q))∧z are equisatisfiable. They are not formulas over the same variable set, and G is false for assignments where p=q=1 but z=0. Auxiliary-variable encodings are useful in SAT solvers, but a request for an equivalent formula over the original variables requires a stronger property.

### 3.2 Normal forms, including the edge cases

A **literal** is an atom or its negation. A formula is in disjunctive normal form (DNF) if it is a disjunction of conjunctions of literals; it is in conjunctive normal form (CNF) if it is a conjunction of disjunctions of literals. “Canonical” forms specify one minterm for each true truth-table row or one maxterm for each false row.

For variables p₁,…,pₙ, build a minterm for a true row by using pᵢ when its row value is 1 and ¬pᵢ when it is 0. That minterm is true on exactly that row. The disjunction of all such minterms therefore agrees with the function on every row. For a false row, build a maxterm by using ¬pᵢ when the row value is 1 and pᵢ when it is 0. Its disjunction is false on exactly that row; the conjunction of all maxterms agrees with the function. This is a constructive proof that every finite Boolean function has both forms.

If the function is always false, canonical DNF is the empty disjunction, conventionally 0. If it is always true, canonical CNF is the empty conjunction, conventionally 1. An unsimplified canonical form can have up to 2<sup>n</sup> terms or clauses. A shorter equivalent form may exist; do not confuse “canonical” with “minimal.”

Resolution works on CNF clauses. From (A∨x) and (B∨¬x), the **resolvent** is A∨B. To justify the rule, consider x=0: the first parent requires A; if x=1, the second requires B. Thus every model of both parents satisfies A∨B. Resolution is sound, but soundness of a step alone does not mean an arbitrary sequence of steps has found every consequence. Deriving the empty clause proves the starting clauses unsatisfiable.

### 3.3 Satisfiability, validity, and proof search

To show a formula satisfiable, exhibit one complete valuation and evaluate the formula. To show it invalid, exhibit one valuation that makes it false. To prove it valid, establish truth for **all** valuations, perhaps by an exhaustive table, an equivalence chain to 1, or a sound derivation. For n independent atoms a full table has 2<sup>n</sup> rows, but factoring the formula can avoid listing them.

For example, Sat(A∧B) does **not** follow from Sat(A) and Sat(B): the two witnesses might disagree. Valid(A∨B) does **not** imply Valid(A) or Valid(B): p∨¬p is the counterexample. By contrast, Valid(A∧B) holds exactly when both conjuncts are valid, and Sat(A∨B) holds exactly when one disjunct is satisfiable. Write down which quantifier over valuations is being moved before using one of these rules.

SAT asks whether at least one satisfying assignment exists. A displayed assignment is a short certificate for a yes-instance. Failure to find an assignment is not by itself a proof of unsatisfiability; an exhaustive search, a sound refutation, or another complete argument is required. Nothing here asserts that every particular SAT instance must take exponential time.

## 4. Predicates and first-order reasoning

### 4.1 Structures, assignments, and sentences

A propositional variable has a truth value. A first-order **term** denotes an object, and a predicate denotes a property of objects or a relation among them. To evaluate formulas precisely, specify a **structure** M: a domain D, the object denoted by each constant, the function assigned to each function symbol, and the relation assigned to each predicate symbol. An assignment s supplies an object in D for each free variable. The notation M,s ⊨ P(x) means that the object s(x) belongs to the relation interpreting P.

The occurrence of x in ∀x P(x) is bound by ∀x. In P(x)∧∀x Q(x), the first x is free and the second is bound; the presence of one quantifier does not bind every matching letter on the page. A formula with no free occurrences is a **closed sentence**. A formula with free occurrences can still be perfectly well formed; its truth is evaluated relative to s.

Unless explicitly stated otherwise, standard first-order semantics assumes a **nonempty** domain. This matters for some equivalences and inference rules. The empty-domain convention used in certain applications must be declared separately. In an empty domain, ∀x P(x) is vacuously true and ∃x P(x) false, but a language with object-denoting constants normally cannot interpret those constants in an empty domain.

### 4.2 Quantifiers: witnesses and order

M,s ⊨ ∀x A exactly when A holds after replacing s(x) by **every** d∈D; M,s ⊨ ∃x A exactly when it holds for **some** d∈D. A universal proof must address an arbitrary object; an existential proof must supply one witness. An existential counterexample needs to show no witness works, whereas one counterexample object is enough to refute a universal claim.

Quantifier order records who may depend on whom:

<div class="formula-block">∀x∃y R(x,y) &nbsp; versus &nbsp; ∃y∀x R(x,y).</div>

The first permits y to vary with x; the second demands a single common y. On a nonempty domain, the second entails the first. The converse fails for equality on D={0,1}: every x equals some y (choose y=x), but no one y equals both 0 and 1. In general, swapping adjacent quantifiers of the **same** kind is harmless; swapping ∀ and ∃ is not.

<figure class="logic-diagram">
<svg viewBox="0 0 680 190" role="img" aria-label="In the first statement each x may have a different y; in the second a shared y must serve all x values.">
  <defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#577f98"/></marker></defs>
  <rect x="10" y="12" width="318" height="165" rx="12" fill="#edf6f9" stroke="#b8d3e1"/>
  <rect x="352" y="12" width="318" height="165" rx="12" fill="#f3f5fa" stroke="#cbd5e5"/>
  <text x="27" y="38" font-size="17" font-family="Segoe UI,Arial" fill="#1b4059">∀x∃y R(x,y): witness may vary</text>
  <text x="369" y="38" font-size="17" font-family="Segoe UI,Arial" fill="#304661">∃y∀x R(x,y): one shared witness</text>
  <circle cx="63" cy="80" r="19" fill="#fff" stroke="#7aa8bb"/><circle cx="63" cy="135" r="19" fill="#fff" stroke="#7aa8bb"/>
  <circle cx="260" cy="80" r="19" fill="#fff" stroke="#7aa8bb"/><circle cx="260" cy="135" r="19" fill="#fff" stroke="#7aa8bb"/>
  <text x="53" y="86" font-size="17">x<tspan baseline-shift="sub" font-size="12">1</tspan></text><text x="53" y="141" font-size="17">x<tspan baseline-shift="sub" font-size="12">2</tspan></text><text x="250" y="86" font-size="17">y<tspan baseline-shift="sub" font-size="12">1</tspan></text><text x="250" y="141" font-size="17">y<tspan baseline-shift="sub" font-size="12">2</tspan></text>
  <path d="M82 80 L237 80" stroke="#577f98" stroke-width="2" marker-end="url(#arrow)"/><path d="M82 135 L237 135" stroke="#577f98" stroke-width="2" marker-end="url(#arrow)"/>
  <circle cx="405" cy="80" r="19" fill="#fff" stroke="#8397bf"/><circle cx="405" cy="135" r="19" fill="#fff" stroke="#8397bf"/>
  <circle cx="610" cy="107" r="19" fill="#fff" stroke="#8397bf"/>
  <text x="395" y="86" font-size="17">x<tspan baseline-shift="sub" font-size="12">1</tspan></text><text x="395" y="141" font-size="17">x<tspan baseline-shift="sub" font-size="12">2</tspan></text><text x="603" y="113" font-size="17">y</text>
  <path d="M424 80 L588 103" stroke="#577f98" stroke-width="2" marker-end="url(#arrow)"/><path d="M424 135 L588 111" stroke="#577f98" stroke-width="2" marker-end="url(#arrow)"/>
</svg>
<figcaption>The arrows represent witness choices, not a required one-to-one relation.</figcaption>
</figure>

Restricted quantifiers have two distinct translations:

<div class="formula-block">∀x∈S: P(x) &nbsp; means &nbsp; ∀x(S(x)→P(x));<br>∃x∈S: P(x) &nbsp; means &nbsp; ∃x(S(x)∧P(x)).</div>

If S is empty, the universal claim is true and the existential claim false. Replacing → by ∧ in the universal expression would wrongly require every domain object to belong to S. Replacing ∧ by → in the existential expression would allow an object outside S to witness the claim.

### 4.3 Negation, uniqueness, and direction

Negation crosses each quantifier and flips its kind:

<div class="formula-block">¬∀x A ≡ ∃x ¬A, &nbsp; ¬∃x A ≡ ∀x ¬A.</div>

For a nested statement, move the negation one operator at a time. For example,

<div class="formula-block">¬∀x∃y(P(x,y)→Q(y)) ≡ ∃x∀y(P(x,y)∧¬Q(y)).</div>

The final x is a counterexample to the original universal statement: every possible y fails because it satisfies P while violating Q. This is stronger than merely finding one pair on which the implication fails.

“Exactly one x satisfies P” requires both existence and uniqueness:

<div class="formula-block">∃x[P(x)∧∀y(P(y)→y=x)].</div>

The formula ∀x∀y((P(x)∧P(y))→x=y) says **at most one**, since it remains true when there are no P-objects. Conversely, ∃x P(x) says **at least one**. A relation R(a,b) must also keep its argument order: “a likes b” does not imply “b likes a.” If symmetry is intended, state it as an additional premise.

### 4.4 Scope, renaming, and capture-free substitution

The scope of a quantifier is the formula it binds, ordinarily delimited by parentheses. In (∀x P(x,y))∧Q(x), the x inside P is bound; the x in Q and the occurrence of y in P are free. Parentheses are part of the reasoning, not decorative typography. Renaming a bound variable to a **fresh** name leaves meaning unchanged: ∀y R(x,y) ≡ ∀z R(x,z), provided z does not already occur in the quantified body. Choosing a genuinely fresh name prevents both capture of an existing free occurrence and interference with an inner binder.

Substitution must avoid **variable capture**. In A=∀y R(x,y), naively replacing free x by y produces ∀y R(y,y), where the inserted y has become bound and the meaning has changed. First rename the bound y to fresh z; then substitute:

<div class="formula-block">∀y R(x,y) &nbsp; ≡α &nbsp; ∀z R(x,z) &nbsp; ⟶<sub>x↦y</sub> &nbsp; ∀z R(y,z).</div>

Here ≡α denotes alpha-equivalence, not a new logical law about arbitrary free variables. Simultaneous substitutions are also different from sequential ones. Applying {x↦y, y↦x} simultaneously to R(x,y) yields R(y,x); blindly applying x↦y and then y↦x yields R(x,x). State the substitution convention whenever several variables are replaced.

### 4.5 Sound inference and invalid patterns

**Modus ponens** takes A and A→B to B. A valuation making both premises true must make A true and cannot make B false, so the rule is sound. **Modus tollens** takes ¬B and A→B to ¬A, using the contrapositive. The patterns B, A→B ⊢ A (“affirming the consequent”) and ¬A, A→B ⊢ ¬B (“denying the antecedent”) are invalid; take A=0 and B=1 for both counterexamples.

First-order rules need witness conditions. From ∀x A(x), infer A(t) when t denotes an object and substitution is capture-free. From A(c) for a **fresh arbitrary** c, one may infer ∀x A(x) only if c was not chosen using a special property of the premises. From ∃x A(x), one may reason with a fresh witness c inside a subproof, but the final conclusion must not depend on c's accidental identity. Choosing a particular favorable object from an existential premise and then announcing a universal conclusion is invalid.

Semantic entailment and a specific formal proof system are separate notions. This chapter proves soundness of the basic rules and uses model counterexamples. Chapter 3 develops direct proof, contradiction, cases, witness arguments and their side conditions. A complete formal natural-deduction calculus, including its metatheory, is outside these introductory chapter boundaries.

### 4.6 Moving quantifiers safely

A bound variable may be moved past a connective only when its scope and the free variables in the other operand have been checked. If x is not free in B and D is nonempty, then

<div class="formula-block">(∀x A(x))∧B ≡ ∀x(A(x)∧B),<br>(∀x A(x))∨B ≡ ∀x(A(x)∨B),<br>(∃x A(x))∧B ≡ ∃x(A(x)∧B),<br>(∃x A(x))∨B ≡ ∃x(A(x)∨B).</div>

The nonempty-domain assumption is needed for the first and fourth displayed movement laws. In an empty domain, the first right side is true while its left side equals B; the fourth right side is false while its left side equals B. The second and third laws remain valid even in an empty domain under the stated free-variable condition. One convention for the whole lesson is convenient, but the precise dependency matters when an application permits an empty domain.

To prove the first equivalence under its stated conditions, fix a nonempty domain and an assignment for B's free variables. If B is false, the left side is false and every instance A(d)∧B on the right is false, so the right side is false. If B is true, both sides reduce to ∀x A(x). Because x is not free in B, varying x cannot change the value of B. The fourth equivalence follows by the analogous two cases for B: when B is false both sides reduce to ∃x A(x); when B is true both sides are true because the domain is nonempty. For the second law, B true makes both sides true and B false reduces both to ∀x A(x). For the third law, B false makes both sides false and B true reduces both to ∃x A(x). These last two arguments do not require a domain object.

Distinguish movement past a fixed operand from distribution over two quantified operands. Universal quantification distributes over conjunction: ∀x(A(x)∧C(x)) is equivalent to (∀x A(x))∧(∀x C(x)). Both assertions require every object to satisfy both predicates. Existential quantification distributes over disjunction: ∃x(A(x)∨C(x)) is equivalent to (∃x A(x))∨(∃x C(x)); either side has a witness for at least one predicate. The apparent dual distributions fail in general because they change witness dependencies.

**Worked boundary model.** Let D={0,1}, let A hold only at 0, and let C hold only at 1. Every object satisfies A∨C, so ∀x(A∨C) is true, yet neither ∀x A nor ∀x C is true. Both ∃x A and ∃x C are true with different witnesses, yet ∃x(A∧C) is false because no common witness exists. Thus only the implication (∀x A)∨(∀x C) ⇒ ∀x(A∨C) is generally valid in the first comparison, and only ∃x(A∧C) ⇒ (∃x A)∧(∃x C) in the second. A singleton domain conceals these failures, so a two-object model is the smallest useful test.

The side condition “x not free in B” is essential. For example, (∀x P(x))∧Q(x) is an open formula whose Q(x) refers to the external assignment. Moving ∀x across the conjunction to make ∀x(P(x)∧Q(x)) binds that previously free x. Choose D={0,1}, P true everywhere, Q true only at 0, and s(x)=0: the left side is true and the right side false. Rename bound variables and mark all free occurrences before any rearrangement.

### 4.7 Finite search versus infinite models

A finite truth table settles propositional validity because finitely many propositional atoms have finitely many valuations. A few finite structures do **not** settle every first-order question: an infinite domain may behave differently. One sentence can assert the existence of a total, injective, non-surjective function through a binary relation R. Its components say that each x has exactly one R-successor; different x values cannot share a successor; and some z is nobody's successor.

No finite nonempty domain satisfies all three: an injective self-map of a finite set is surjective. The natural numbers with R(x,y) iff y=x+1 do satisfy them: every x has one successor, successors are unique, and 0 has no predecessor. Thus checking every structure up to some finite size cannot establish universal nonexistence of a first-order model. This is a limitation of that finite search, not an instruction to use an infinite structure whenever an ordinary finite countermodel suffices.

## 5. Fully worked problem bank

Problems 1–10 are original to this edition. Problems 11–14 are independently worded adaptations of specific, cited university exercises; their solutions are newly derived here. This bank samples the major reasoning patterns in the chapter without reproducing archived entrance-exam questions. Read each solution as another explanation of the underlying rule before using the problems for self-checking.

### Problem 1 — Count Boolean functions constrained by an implication

**Question.** How many Boolean functions F(p,q,r) make (p→q)→F a tautology?

**Solution.** The outer implication can be false only where p→q is true and F is false. The antecedent p→q is false precisely when p=1 and q=0. For each of the other three choices of (p,q), both values of r occur, giving six rows on which F is forced to 1. When (p,q)=(1,0), the outer antecedent is false, so F is unrestricted at r=0 and r=1. These are two independent output bits, giving 2²=**4 functions**. Counting assignments instead of functions would answer a different question.

### Problem 2 — Negate a statement with two quantified parts

**Question.** Formalize and negate: “If every request is accepted, some request is retryable.” Use R(x) for “x is a request,” A(x) for “x is accepted,” and T(x) for “x is retryable.”

**Solution.** The statement is [∀x(R(x)→A(x))]→∃x(R(x)∧T(x)). Negating an implication preserves its antecedent and negates its consequent. Thus its negation is [∀x(R(x)→A(x))]∧¬∃x(R(x)∧T(x)), equivalently

<div class="formula-block">[∀x(R(x)→A(x))] ∧ [∀x(R(x)→¬T(x))].</div>

The result says that every request is accepted and no request is retryable. If there are no requests, the original antecedent is vacuously true and its existential consequent false, so the original implication is false; the negation above is true. This checks the empty-restricted-set edge case without adopting an empty overall domain.

### Problem 3 — Prove an entailment by cases and by a single formula

**Question.** Do p∨q, p→r, and q→r entail r?

**Solution.** The first premise says at least one of p and q is true. If p is true, p→r gives r. If q is true, q→r gives r. Both cases give r, so the entailment holds. Equivalently, the conjunction of premises and ¬r is unsatisfiable: p→r and ¬r force ¬p, while q→r and ¬r force ¬q; these contradict p∨q. Notice that neither p→r alone nor q→r alone entails r.

### Problem 4 — Produce both normal forms without enumerating eight rows

**Question.** Convert F=(p⊕q)∨r into an equivalent DNF and CNF over p,q,r.

**Solution.** XOR is (p∧¬q)∨(¬p∧q), so a DNF is

<div class="formula-block">F ≡ (p∧¬q)∨(¬p∧q)∨r.</div>

XOR is also (p∨q)∧(¬p∨¬q). Distribute r over that conjunction:

<div class="formula-block">F ≡ (p∨q∨r)∧(¬p∨¬q∨r).</div>

This is a CNF. Check p=q=1,r=0: both formulas are false; p≠q or r=1 makes both true. These compact forms are not the full canonical forms, which would contain one term or clause for each applicable table row.

### Problem 5 — Negate nested quantifiers without losing a dependency

**Question.** Negate ∀x∃y[P(x,y)→∀z Q(y,z)].

**Solution.** First flip the outer quantifier, then the inner one:

<div class="formula-block">¬∀x∃y[P→∀z Q] ≡ ∃x∀y¬[P→∀z Q].</div>

Negating the implication yields P(x,y)∧¬∀z Q(y,z), and negating the last universal gives

<div class="formula-block">∃x∀y[P(x,y)∧∃z¬Q(y,z)].</div>

The z-witness may depend on y, and the chosen x must work against every y. Swapping ∀y and ∃z would demand one z for all y and generally produce a stronger, non-equivalent claim.

### Problem 6 — Refute a quantifier swap with a small model

**Question.** Does ∀x∃y R(x,y) imply ∃y∀x R(x,y)?

**Solution.** No. Let D={0,1} and let R(x,y) mean x=y. For each x, choose y=x; hence ∀x∃y R(x,y) is true. Neither candidate y equals both 0 and 1, so ∃y∀x R(x,y) is false. The reverse implication holds on a nonempty domain: a common y works for each x separately. This model gives a complete counterexample, not merely an intuition about “changing witnesses.”

### Problem 7 — Count satisfying assignments by a disjoint split

**Question.** How many assignments satisfy F=(p→q)∧(q∨r)?

**Solution.** Split on q. If q=1, both factors are true for every p and r, giving 2²=4 assignments. If q=0, p→q requires p=0, and q∨r requires r=1; this gives exactly one assignment. The cases q=1 and q=0 are disjoint and exhaustive. The answer is **5**. A full eight-row table confirms the count but is not needed.

### Problem 8 — Preserve a witness under a symmetry premise

**Question.** Suppose ∀x∃y R(x,y) and ∀x∀y(R(x,y)→R(y,x)). Prove ∀x∃y[R(x,y)∧R(y,x)]. Do the premises also imply ∀x R(x,x)?

**Solution.** Let a be an arbitrary domain object. The first premise supplies a witness b with R(a,b). The symmetry premise, instantiated at a,b, gives R(b,a). The **same** b therefore witnesses R(a,b)∧R(b,a). Since a was arbitrary, universally generalize. The reflexive conclusion does not follow: on D={0,1}, set R={(0,1),(1,0)}. Each object has an outgoing edge and R is symmetric, but neither object relates to itself. Distinguishing a valid witness argument from a plausible extra conclusion is the point of this problem.

### Problem 9 — Express exactly one and test boundary models

**Question.** Write “exactly one student solved the puzzle” with S(x) meaning student and P(x) meaning solved the puzzle.

**Solution.** Use

<div class="formula-block">∃x[S(x)∧P(x)∧∀y((S(y)∧P(y))→y=x)].</div>

The existential part supplies a student solver. The universal part says every student solver is that same object. In a model with no solver the formula is false; in a model with one solver it is true; with two distinct solvers it is false. Using only ∀x∀y(((S(x)∧P(x))∧(S(y)∧P(y)))→x=y) would express “at most one,” because it would pass the no-solver model.

### Problem 10 — Repair a capture error and separate substitution conventions

**Question.** Substitute free x by y in ∀y R(x,y). Then apply {x↦y,y↦x} simultaneously to R(x,y).

**Solution.** Directly writing ∀y R(y,y) would let the old quantifier bind the inserted free y. Rename bound y to fresh z first: ∀y R(x,y) ≡α ∀z R(x,z). Capture-free substitution then gives **∀z R(y,z)**, where y remains free. For the second expression, simultaneous substitution reads the original positions before either replacement, producing **R(y,x)**. Sequentially replacing x and then y would instead produce R(x,x), a different result. State “simultaneous” or “sequential” before manipulating a substitution list.

### Problem 11 — Build every basic connective from NAND

**Source and adaptation.** MIT 6.042J, Problem Set 1, Problem 3, asks for NAND-based expressions. The variable names and presentation below are independent; the exercise type is attributed to the [original sheet](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/52e4d5a499a39c41c129e1eb4e831e20_MIT6_042JF10_assn01.pdf).

**Question.** Write ¬p, p∧q, p∨q, and p→q using only the binary operator ↑, where p↑q means ¬(p∧q). Then construct one always-true and one always-false formula without writing truth constants.

**Solution.** First observe that p↑p=¬p: repeating an input turns NAND into negation. Negating NAND gives conjunction, so (p↑q)↑(p↑q)=p∧q. De Morgan's law gives p∨q=¬(¬p∧¬q)=(p↑p)↑(q↑q). Since p→q is ¬p∨q, substitute the expression for ¬p into the disjunction rule; the simpler result is **p↑(q↑q)**, because this is ¬(p∧¬q). Let N=p↑p=¬p. Then p↑N=¬(p∧¬p)=1 for either value of p. Finally, (p↑N)↑(p↑N)=¬1=0. These identities also prove that NAND alone can express any formula built from ¬, ∧, ∨, and →: replace each connective recursively with its NAND expression. The proof is about Boolean functions; actual circuit cost and timing are separate questions.

### Problem 12 — Separate a familiar inference rule from its invalid converse

**Source and adaptation.** Stanford CS103, Homework 4, Problem 1, contrasts valid and invalid implication patterns. This altered pair and its full analysis are based on that exercise type: [official handout](https://cs.stanford.edu/people/trevisan/cs103-14/hw4b.pdf).

**Question.** Decide whether each formula is valid: (i) ((p→q)∧¬q)→¬p; (ii) ((p→q)∧q)→p. Give a proof or a complete countervaluation, and name the inferential mistake in the invalid case.

**Solution.** For (i), assume the antecedent is true. Then p→q is true and q=0. If p were 1, p→q would be false, a contradiction; hence p=0 and ¬p=1. This covers every valuation with true antecedent, while an implication with false antecedent is automatically true. Thus (i) is valid; this is *modus tollens*. For (ii), set p=0 and q=1. Then p→q=1, q=1, and p=0, so the whole implication is false. This one countervaluation proves invalidity. The tempting move from p→q and q to p is *affirming the consequent*. The presence of an implication never asserts that q has only one possible cause.

### Problem 13 — A dependency hidden in a choice of pebbles

**Source and adaptation.** UC Berkeley CS70, Discussion 1B, Problem 2, uses a red/blue pebble array to expose quantifier order. The explanation below is independently written from the [official discussion sheet](https://su24.eecs70.org/assets/pdf/dis1b.pdf).

**Question.** A nonempty finite board has several nonempty columns, and each cell holds either a red or a blue pebble. Let A mean that one column is entirely red. Let B mean that every selection of exactly one pebble from each column contains a red pebble. Prove A↔B. Explain which step fails if a column is empty.

**Solution.** If A holds, name an all-red column C. Every complete selection must pick one pebble from C, and that selected pebble is red. Therefore B holds. For the converse, prove the contrapositive. If A fails, every column has at least one blue pebble. Because the board has finitely many nonempty columns, choose one blue pebble from each column. The resulting complete selection contains no red pebble, so B fails. Consequently B→A. The finite-board assumption makes the simultaneous choice elementary. If an empty column is admitted and “entirely red” is defined to require at least one pebble, there may be no complete selection; then B can be vacuously true while A is false. For example, take one empty column and one column containing a blue pebble. The nonempty-column condition is therefore essential. Under the alternative convention that an empty column counts as vacuously all-red, the meaning of A changes and the boundary case must be reanalyzed.

### Problem 14 — Detect the trap in a subformula claim

**Source and adaptation.** CMU 15-311, “Propositional Logic,” slide 14, presents a deliberately false subformula claim and its counterexample. The formulation and extended diagnosis below follow the [official slide deck](https://www.cs.cmu.edu/~mheule/15311-s26/slides/prop.pdf).

**Question.** Suppose B is a subformula of A and A is a subformula of B. Must both A and B be atomic? Give the strongest conclusion justified by their syntax trees.

**Solution.** No. Take A=B=¬p. A formula is a subformula of itself, so both premises hold, yet neither formula is atomic. In fact, the premises imply **A and B are the same formula**. A proper subformula has strictly fewer nodes than its parent. If A and B were distinct, B being a proper subformula of A would give size(B)<size(A), while A being a proper subformula of B would give size(A)<size(B), an impossibility. Equality is the only remaining case. The false claim confuses “the subformula relation is antisymmetric” with “mutual membership is possible only at a leaf.” This same size argument is useful whenever a recursive syntax relation is alleged to contain a cycle.

## 6. High-yield review sheet

This section is deliberately compact. It is a **recall aid after the full lesson**, not a substitute for the definitions, countermodels, or worked solutions above. It collects facts that can prevent avoidable errors in later timed problem solving without using any archived entrance-exam question now.

### 6.1 Decide what kind of claim is being asked

| Requested claim | Required evidence | A common insufficient response |
| --- | --- | --- |
| A is satisfiable | One full valuation or one explicitly defined model satisfying A | “It looks consistent” |
| A is invalid | One countervaluation or countermodel | A few confirming examples |
| A is valid | A proof covering every valuation or model in the stated class | One true row |
| A ≡ B | Agreement under every common valuation or model | Both are merely satisfiable |
| Γ ⊨ C | Proof that Γ∧¬C has no model | C is true in one model of Γ |
| A first-order universal is false | One domain object with the required failure | A different unrelated object |
| A first-order existential is true | One witness in the declared domain | An object outside the restricted set |

Keep the **universe of interpretation** visible. A propositional truth table over n atoms has 2<sup>n</sup> valuations. A first-order formula ranges over objects and interpretations of predicates as well; an arbitrary finite list of structures is not a general proof.

### 6.2 Conditional language and negation

“A only if B” means A→B: B is necessary for A. “A if B” means B→A: B is sufficient for A. “A if and only if B” means both implications. When a natural-language sentence is ambiguous, write the intended necessary or sufficient condition in words before translating it. The phrase “all P are Q” means ∀x(P(x)→Q(x)); “some P are Q” means ∃x(P(x)∧Q(x)).

The negation checklist is:

1. Expose the outermost connective and its parentheses.
2. Apply ¬(A→B) ≡ A∧¬B or the relevant De Morgan law.
3. Change each ∀ to ∃ and each ∃ to ∀ as the negation passes it.
4. Stop when negation reaches atomic predicates, unless their internal meaning is separately defined.
5. Check the result in a tiny model, especially when a restricted set could be empty.

For instance, the negation of ∀x(P(x)→Q(x)) is ∃x(P(x)∧¬Q(x)); it is **not** ∀x(P(x)∧¬Q(x)). The first says one counterexample exists; the second demands every object be a counterexample.

### 6.3 Normal-form and inference checks

For canonical DNF, start with the **true** rows and create one minterm per row. For canonical CNF, start with the **false** rows and create one maxterm per row. In a minterm, a row value 1 gives a positive literal; in a maxterm, a row value 1 gives a negative literal. Re-evaluate at least one source row to detect a reversed sign. If a formula introduces auxiliary variables, decide whether the required guarantee is equivalence or only equisatisfiability.

To test an entailment, append the negation of the proposed conclusion to the premises. A model of this conjunction refutes the entailment. Unsatisfiability proves it. Resolution of (A∨x) and (B∨¬x) produces A∨B; do not “resolve” two clauses lacking complementary occurrences of the same atom.

### 6.4 Quantifier and model checks

Mark every free occurrence before moving a quantifier or substituting a term. Universal restriction uses implication; existential restriction uses conjunction. A witness for ∀x∃y may depend on x, while ∃y∀x requires one witness shared by all x. “Exactly one” always has an existence part and a uniqueness part. A binary relation is directed unless symmetry is given. Quantifier movement across another operand requires the bound variable to be absent from that operand's free variables; the domain convention must also be checked.

### 6.5 Exam-oriented decision checklist

The following rules cover the recurring *forms of reasoning* that a difficult logic question can combine. They are not a catalogue of archived entrance-exam questions. For each item, first identify the requested conclusion and then apply the stated check to the whole formula, including its assumptions.

| When the question asks for… | Reliable procedure | Trap to rule out |
| --- | --- | --- |
| A truth-table count | Identify the distinct atoms, count 2<sup>n</sup> valuations, and split into disjoint cases if a full table is long. | Counting satisfying assignments when the question asks for Boolean functions, or vice versa. |
| Validity of an implication | Search for the only falsifying pattern: antecedent true and consequent false. | Treating a true consequent as proof of the antecedent. |
| Equivalence of formulas | Compare outputs under the union of their atom sets, or use a law whose side conditions hold. | Showing only that both formulas are satisfiable. |
| Logical consequence | Conjoin the premises with the negated conclusion and test satisfiability. | Using a valuation in which one premise is false as a counterexample. |
| Canonical DNF or CNF | Use all true rows for DNF and all false rows for CNF, with the correct literal polarity. | Confusing an equivalent compact form with the requested canonical form. |
| A first-order countermodel | State a nonempty domain, every relevant predicate or relation, and a concrete assignment for free variables. | Giving an informal scenario that does not fix the whole interpretation. |
| A quantified negation | Move negation inward one connective or quantifier at a time and preserve parentheses. | Changing ∀ to ∃ without also negating the quantified body. |
| Restricted quantification | Translate ∀x∈S to an implication and ∃x∈S to a conjunction. | Writing ∃x(S(x)→P(x)), which can be witnessed outside S. |
| A quantifier-order claim | Draw the dependency of each existential witness on earlier universal variables. | Reusing a different witness as if it were one common object. |
| Quantifier distribution | Distribute ∀ over ∧ and ∃ over ∨. Check the two-object split-predicate model before claiming either opposite distribution. | Turning different existential witnesses into one common witness, or turning a per-object disjunction into one universal disjunct. |
| Uniqueness | Prove both at least one witness and at most one witness. | Accepting a statement that is vacuously true when no witness exists. |
| Variable substitution | Mark free and bound occurrences; rename bound variables before a replacement could capture a free variable. | Performing several substitutions sequentially when they were defined as simultaneous. |
| A finite search result | State the size bound searched and whether the target claim quantifies over all structures. | Treating failure to find a small model as proof of general unsatisfiability. |

### 6.6 What this chapter intentionally leaves for later

The chapter establishes the logical language needed by the plan. Detailed set identities and relation properties belong to the sets and relations chapters. Chapter 3 develops mathematical proof techniques; a complete formal natural-deduction calculus is outside the present introductory sequence. Gate delay and physical glitches belong to digital logic. Algorithmic performance of SAT solvers belongs to algorithms. This separation prevents a logic chapter from growing through unrelated material while keeping its own definitions and edge cases explicit.

## 7. Interactive truth-table laboratory

The interactive table in the web edition evaluates a selected three-variable formula for all eight assignments. The model is classical propositional logic: each input is exactly 0 or 1, ∨ is inclusive, and → is material implication. It shows **semantic output only**. It does not simulate timing, metastability, short-circuit evaluation, or hardware hazards.

Try comparing p→q with ¬p∨q; their outputs match in all eight rows, including both choices of r. Then compare p→q with q→p; the row p=0,q=1 separates them. These are demonstrations of the definitions, not archived examination questions.

<div class="lab">
<label for="formula-select">Choose a formula:</label>
<select id="formula-select">
  <option value="imp">p → q</option>
  <option value="rewritten">¬p ∨ q</option>
  <option value="converse">q → p</option>
  <option value="biconditional">p ↔ q</option>
  <option value="composite">(p ∨ q) ∧ ¬r</option>
</select>
<div id="truth-output" aria-live="polite"></div>
</div>

## 8. Source references and review limits {#references}

1. Leighton, T., and van Dijk, M. (2010). “Propositions.” *6.042J Mathematics for Computer Science*, Chapter 1, MIT OpenCourseWare. [Original 19-page PDF](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/7853d585044ef21bce5f48ce5fc89d28_MIT6_042JF10_chap01.pdf). All 17 substantive pages were reviewed; equation and symbol rendering was checked against the PDF images.
2. Trevisan, L. (2014). “Mathematical Logic.” *CS103 Mathematical Foundations of Computing*, Lecture 9, Stanford University. [Original eight-page PDF](https://cs.stanford.edu/people/trevisan/cs103-14/lecture09.pdf). All eight pages were reviewed, including scope and free-variable examples.
3. Shahzar, and Wu, H. (2024). “Logic.” *CS70 Discrete Mathematics and Probability Theory*, Note 1, University of California, Berkeley. [Original 14-page PDF](https://su24.eecs70.org/assets/pdf/notes/n1.pdf). All 14 pages and the relevant diagrams were reviewed. The chapter uses new wording and solutions throughout; Problem 13 is explicitly adapted from the course discussion sheet.
4. Heule, M. J. H. (2026). “Propositional Logic” and “First-Order Logic.” *15-311 Logic and Mechanized Reasoning*, Carnegie Mellon University. [Propositional slides](https://www.cs.cmu.edu/~mheule/15311-s26/slides/prop.pdf); [first-order slides](https://www.cs.cmu.edu/~mheule/15311-s26/slides/FOL.pdf). Both decks, including repeated animation frames and the response slides after false prompts, were reviewed.
5. Cornell University (2017). “Lecture 36: Logic.” *CS2800 Discrete Structures*. [Lecture text](https://www.cs.cornell.edu/courses/cs2800/2017fa/lectures/lec36-logic.html). Consulted as a supplementary comparison of inductive semantics; it is not counted toward the four-course minimum.
6. MIT 6.042J (2010). [Problem Set 1, Problem 3](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/52e4d5a499a39c41c129e1eb4e831e20_MIT6_042JF10_assn01.pdf). Exercise type used in Problem 11.
7. Stanford CS103 (2014). [Homework 4, Problem 1](https://cs.stanford.edu/people/trevisan/cs103-14/hw4b.pdf). Exercise type used in Problem 12.
8. UC Berkeley CS70 (2024). [Discussion 1B, Problem 2](https://su24.eecs70.org/assets/pdf/dis1b.pdf). Exercise type used in Problem 13.
9. CMU 15-311 (2026). [Propositional Logic, slide 14](https://www.cs.cmu.edu/~mheule/15311-s26/slides/prop.pdf). Counterexample prompt developed further in Problem 14.

The notes synthesize the selected course texts and independently derive the worked examples. A source comparison cannot establish literal coverage of every course worldwide, and no pre-publication audit can prove that a future, unseen question will be answered correctly with certainty. Identified errors or missing concepts should be corrected in the chapter and its audit rather than hidden behind a “100%” label. Archived Iranian master's and doctoral examination booklets are intentionally absent from this edition; they are reserved for joint, question-by-question study in the final month.
