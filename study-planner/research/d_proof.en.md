# Direct Proof, Contradiction, and Counterexamples

**Discrete Mathematics · Chapter 3 · review draft**

This chapter teaches how to turn an exact claim into a valid proof or refutation. It assumes the truth conditions for implication and quantifiers from Chapter 1 and the definitions of sets from Chapter 2. Its boundary includes direct proof, contrapositive, contradiction, cases, two-direction equivalence, witnesses, uniqueness, counterexamples, and diagnosis of invalid arguments. Induction and well-ordering belong to the next chapter. Number-theoretic examples here serve proof technique; they do not replace a later number-theory course. Read the teaching sections before the compact final review: the final review is a recall aid, not the lesson.

## 1. Sources, selection, and coverage

Five written university courses were genuinely reviewed for the relevant sections. MIT 6.042J supplies the main organization of implication, equivalence, cases, and contradiction. Stanford CS103 gives unusually explicit guidance on assumptions, goals, and the order of quantified choices. Berkeley CS70 links the principal techniques and analyzes invalid proofs. Cornell CS2800 compares direct and indirect proofs and connects a counterexample to the quantified claim it refutes. ETH Zürich's discrete mathematics notes supply an explicit account of why implication composition and exhaustive cases are sound and treat a counterexample as an existential witness. These are complementary strengths, not five arbitrary names. The exact reviewed portions and limits are recorded in the project source audit; the official course links appear in [References](#references). A supplementary Oxford course page was also checked for boundary examples. The survey is bounded by accessible written materials and makes no claim to have inspected every course worldwide.

No archived Iranian entrance-exam question is used here. Those booklets are reserved for joint study in the final month. Problems below are original or independently worded adaptations of a *type* found in the named courses, with attribution where relevant; they do not reproduce a course problem bank wholesale.

## 2. Proof obligations: know exactly what must be shown

### 2.1 Claims, domains, and admissible reasons

A **proof** starts from stated hypotheses, definitions, axioms, and previously proved facts and derives the conclusion by valid inferences. Before calculating, write the domain of every variable and expand the logical structure. A property of every integer cannot be established by checking many integers; the choice remains arbitrary. A statement about some integer can be established by one admissible witness. A universal statement is disproved by one counterexample *in its domain*. The same number may be a valid counterexample over ℝ and inadmissible over ℤ.

Consider “Every even integer has an even square.” Its full structure is ∀n∈ℤ (Even(n) → Even(n²)). The proof does not select a convenient even n. It fixes an arbitrary n∈ℤ, assumes Even(n), and must derive Even(n²). The word **arbitrary** is a proof obligation: no later step may use a property that holds only for a chosen sample. Conversely, to disprove the claim, we would need an integer n for which Even(n) is true and Even(n²) is false. A value with a false premise does not refute an implication.

<div class="formula-block">∀n∈ℤ [Even(n) → Even(n²)] &nbsp; versus &nbsp; ∃n∈ℤ [Even(n) ∧ ¬Even(n²)].</div>

For integers a,b, write a∣b when some k∈ℤ satisfies b=ak. This definition even permits a=0: 0∣b iff b=0. One must not divide by a without first establishing a≠0. Even(n) means n=2k for some k∈ℤ; Odd(n) means n=2k+1. A rational number r has representation p/q with p,q∈ℤ and q≠0. “In lowest terms” adds gcd(|p|,|q|)=1 and is a separate assumption that can be obtained by reduction, not inferred from an arbitrary fraction.

### 2.2 Logical forms and their appropriate starting moves

| Goal | Legitimate starting move | Required finish |
| --- | --- | --- |
| ∀x∈D P(x) | Fix an arbitrary x∈D. | Derive P(x) without special choices. |
| P→Q | Assume P. | Derive Q from P and valid background facts. |
| P↔Q | Start two implications, P→Q and Q→P. | Finish both directions; one alone is insufficient. |
| ∃x∈D P(x) | Choose a specified x∈D, or prove existence indirectly. | Verify domain membership and P(x). |
| ∀x∈D ∃y∈E R(x,y) | Fix arbitrary x, then choose y, possibly depending on x. | Verify y∈E and R(x,y) for that x. |
| Uniqueness of x | Prove existence, then compare arbitrary solutions u and v. | Derive u=v. |

These rules follow quantifier order. In ∀x∃y R(x,y), the witness y may be a function of x. In ∃y∀x R(x,y), y must be fixed *before* x varies. These claims are not interchangeable. For example, ∀x∈ℤ ∃y∈ℤ (y=x+1) is true with y=x+1; ∃y∈ℤ ∀x∈ℤ (y=x+1) is false because a fixed y cannot equal both 1 (when x=0) and 2 (when x=1).

### 2.3 A dependency diagram for selecting a proof route

<figure class="logic-diagram"><svg viewBox="0 0 830 240" role="img" aria-label="Three valid proof routes for P implies Q and the separate counterexample route"><defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0 0 L9 4.5 L0 9 Z" fill="#446b85"/></marker></defs><rect x="20" y="20" width="175" height="45" rx="9" fill="#e7f1f7" stroke="#7fa9be"/><text x="39" y="49" font-size="17">Goal: P → Q</text><rect x="245" y="15" width="555" height="48" rx="9" fill="#edf6f0" stroke="#85ad90"/><text x="259" y="44" font-size="16">Direct: assume P; derive Q</text><rect x="245" y="77" width="555" height="48" rx="9" fill="#f1f1fa" stroke="#9898b9"/><text x="259" y="106" font-size="16">Contrapositive: assume ¬Q; derive ¬P</text><rect x="245" y="139" width="555" height="48" rx="9" fill="#faf1ea" stroke="#c6a17c"/><text x="259" y="168" font-size="16">Contradiction: assume P ∧ ¬Q; derive falsehood</text><rect x="245" y="201" width="555" height="33" rx="9" fill="#f8e9e9" stroke="#bd8d8d"/><text x="259" y="223" font-size="15">Refute instead: exhibit a case with P true and Q false</text><path d="M195 43 L235 39 M195 43 L235 100 M195 43 L235 163 M195 43 L235 217" stroke="#446b85" stroke-width="2" fill="none" marker-end="url(#arrow)"/></svg><figcaption>Each proof route establishes the same implication. The final route refutes it, so never mix it into an attempted proof.</figcaption></figure>

The diagram is a strategy map, not an automatic theorem prover. Each arrow still requires valid mathematical steps, and a false target cannot be saved by changing proof style. Scratch calculations may help discover a route, but the final proof must give the logical direction of every step. In particular, working backward from Q can produce a *necessary* condition for Q without showing that P implies Q.

## 3. Direct proofs and definition-driven construction

### 3.1 The anatomy of a direct implication proof

To prove ∀x∈D [P(x)→Q(x)], fix arbitrary x∈D satisfying P(x), explicitly state Q(x) as the goal, unfold the definitions in P, and derive the definition of Q. Each line requires a reason. For example, if a∣b and a∣c, there are integers u,v with b=au and c=av. Consequently b+c=a(u+v). Since u+v∈ℤ, the same definition proves a∣(b+c). The final “u+v is an integer” closes the witness obligation. No cancellation by a was used, so this proof remains valid for a=0.

One often discovers a proof by asking what a *witness for the conclusion* should be. If the conclusion is “6 divides 3n(n+1),” its proof needs an integer t with 3n(n+1)=6t, equivalently an integer expression n(n+1)/2. Two consecutive integers have opposite parity, so n(n+1) is even. Write n(n+1)=2t; then 3n(n+1)=6t. The parity fact can itself be proved by two cases, n=2k or n=2k+1. This is how a top-level direct proof can contain a smaller case proof.

<div class="formula-block">n(n+1)=2t, t∈ℤ &nbsp; ⇒ &nbsp; 3n(n+1)=6t &nbsp; ⇒ &nbsp; 6∣3n(n+1).</div>

### 3.2 Backward discovery versus forward justification

Suppose x,y≥0 and we want (x+y)/2≥√(xy). It is tempting to square the desired inequality, rearrange it into (x−y)²≥0, and declare success. That backward chain is valid only if every transformation is reversible under the current assumptions. Here both sides of the desired inequality are nonnegative, so squaring is reversible, but a clean forward proof begins with the universally true (x−y)²≥0. Expanding gives x²−2xy+y²≥0, hence (x+y)²≥4xy. Both x+y and 2√(xy) are nonnegative, so taking square roots preserves order: x+y≥2√(xy). Equality occurs exactly when (x−y)²=0, equivalently x=y. If x or y were negative, √(xy) might fail to be real, and the proof cannot simply omit the domain hypothesis.

**Illegal reversal trap.** From A=B we may infer A²=B². From A²=B² we may infer A=B *or* A=−B, not A=B alone. Similarly, multiplying an inequality by a negative number reverses its direction; division by zero is undefined; applying a noninjective function to two equal values cannot establish equality of the original inputs. The proof must preserve the direction required by the goal.

### 3.3 Lemmas and chains

A longer proof is often easier when split into named intermediate facts. If P→R and R→Q, then P→Q: starting with P gives R and then Q. This composition is sound because no line assumes Q before deriving it. For quantified results, check that both implications apply to the **same** arbitrary object and with the right domain. A lemma about positive integers may not be used on a negative integer without an added case.

An exact decomposition sometimes replaces heavy algebra. To prove A⊆B∪C from A∖B⊆C, fix x∈A. Either x∈B, so x∈B∪C, or x∉B, in which case x∈A∖B⊆C, again x∈B∪C. This is a direct proof of a set statement that contains a case split. Its conclusion is independent of whether A, B, or C is empty.

## 4. Contrapositive: use the logically equivalent direction

The contrapositive of P→Q is ¬Q→¬P. Their equivalence follows from P→Q≡¬P∨Q and ¬Q→¬P≡Q∨¬P. The **converse** Q→P and **inverse** ¬P→¬Q are generally different. Negate entire predicates correctly. For “if n² is even then n is even,” the contrapositive is “if n is odd then n² is odd.” It is not “if n is even then n² is even,” which is the converse and requires a separate argument.

<div class="formula-block">P→Q ≡ ¬P∨Q ≡ ¬Q→¬P; &nbsp; Q→P is the converse, not the contrapositive.</div>

For any integer n, n odd means n=2k+1 for some integer k. Then n²=4k²+4k+1=2(2k²+2k)+1, an odd integer. The contrapositive proves n² even → n even. This route gives a constructive algebraic step from the negative conclusion. A contradiction proof could instead assume n² even and n odd, derive that n² is odd, and close on the incompatibility; the two proofs use the same lemma but keep different assumptions in view.

For an implication with several hypotheses, keep their connective structure: (P∧R)→Q has contrapositive ¬Q→¬(P∧R), that is ¬Q→(¬P∨¬R). It does **not** generally yield ¬Q→(¬P∧¬R). For quantified claims, include quantifier negation. The contrapositive of “if every x has property A then some x has property B” is “if no x has property B then some x lacks property A.” One cannot leave “every” unchanged when negating its whole assertion.

## 5. Contradiction: derive an actual impossibility

To prove S by contradiction, assume ¬S and derive both R and ¬R, a violation of a stated hypothesis, or another established falsehood. For P→Q, the negation is P∧¬Q; therefore a contradiction proof must use **both** P and ¬Q. If it starts with ¬Q alone and derives ¬P, it is a contrapositive proof. That distinction matters when auditing a difficult argument.

For example, √2 is irrational. Suppose instead √2=p/q with integers p,q, q≠0, and choose the fraction in lowest terms. Squaring and multiplying by q² yields p²=2q², so p² is even. By the odd-square calculation in §4, p must be even; write p=2r. Substitution gives 4r²=2q², or q²=2r²; hence q is even too. Thus p and q have common factor 2, contradicting their reduced form. The proof uses three nontrivial facts: a reduced representation exists for every rational, q is nonzero so multiplication is legal, and even square implies even base. Omitting any of these weakens the proof.

<div class="formula-block">√2=p/q, gcd(|p|,|q|)=1 &nbsp; ⇒ &nbsp; p²=2q² &nbsp; ⇒ &nbsp; 2∣p and 2∣q &nbsp; ⇒ &nbsp; gcd(|p|,|q|)≥2.</div>

### 5.1 Negating compound and quantified targets

| Target S | Assumption ¬S for contradiction |
| --- | --- |
| ∀x∈D P(x) | ∃x∈D ¬P(x). |
| ∃x∈D P(x) | ∀x∈D ¬P(x). |
| ∀x∈D ∃y∈E R(x,y) | ∃x∈D ∀y∈E ¬R(x,y). |
| P→Q | P∧¬Q. |
| P↔Q | (P∧¬Q)∨(Q∧¬P). |
| P∧Q | ¬P∨¬Q. |

The quantifier-domain restriction stays in force. Negating “all nonzero real x satisfy P(x)” produces a *nonzero real* counterexample, not x=0. Negating “there is a unique x with P(x)” is more delicate: either no such x exists, or at least two distinct such x exist. It is false to negate uniqueness merely by assuming no solution.

### 5.2 When the argument is genuinely complete

The final contradiction must be impossible under facts already established. “This seems unlikely,” “my numerical trials failed,” and “this differs from what we wanted” are not contradictions. For a supposed smallest positive integer with a property, producing a smaller positive integer with the same property is a contradiction only if both positivity and the property have been proved for the new object. Minimal-counterexample arguments as a systematic induction technique are reserved for the next chapter; the logical audit of the contradiction is already relevant here.

One should not try to prove a false statement by contradiction and blame a failure to find an impossibility on lack of ingenuity. First test extreme and boundary cases. A single legitimate counterexample ends the proof attempt. Also note that if the starting assumptions are themselves inconsistent, one can derive arbitrary claims; a useful theorem must make its premises explicit rather than hide an impossible premise.

## 6. Exhaustive cases and biconditional proofs

To prove S by cases R₁,…,Rₖ, first prove R₁∨···∨Rₖ under the original hypotheses, then prove Rᵢ→S for each i. Cases may overlap; exhaustiveness, not disjointness, is required. The split “x≥0 or x<0” exhausts the real numbers. The split “x>0 or x<0” misses x=0. In proofs over integers, residue classes modulo m form exhaustive cases only if every residue 0,…,m−1 is treated; this follows from integer division by m>0.

As an example, n(n+1) is even for every integer n. If n=2k, the product is 2[k(n+1)]. If n=2k+1, then n+1=2(k+1), so the product is 2[n(k+1)]. Every integer is even or odd, including negative integers, so the proof is complete. We do not need to show the two cases are equally likely or that their witnesses are the same.

To prove P↔Q, prove P→Q and Q→P. An equivalence chain P↔R↔Q is acceptable only if each displayed step is **biconditional**. If one step is merely P→R, the chain may establish only one direction. For integers n, “n odd iff n² odd” has forward direction by expansion of (2k+1)²; the reverse direction follows by contrapositive from “n even implies n² even.” State both directions explicitly. If a converse is false, say so and give a counterexample rather than trying to turn a one-way theorem into an iff.

## 7. Existence, witness dependence, and uniqueness

An existential proof must give a valid object or establish existence by a sound indirect argument. For every integer n, the equation r²−s²=4n has integer solutions: choose r=n+1 and s=n−1. Then r²−s²=(r−s)(r+s)=2·2n=4n. These witnesses depend on n. A single fixed pair cannot work for all n, since its difference of squares has one fixed value. The choices r and s remain integers even for n=0 or negative n.

<div class="formula-block">∀n∈ℤ ∃r,s∈ℤ : r²−s²=4n; &nbsp; r=n+1, &nbsp; s=n−1.</div>

For a unique-solution statement, existence and at-most-one are logically separate. If a,b∈ℝ and a≠0, the equation ax+b=0 has solution x=−b/a. This is legal because a≠0 and substitution gives a(−b/a)+b=0. If u and v are solutions, au+b=av+b=0; subtract to obtain a(u−v)=0. Since a≠0, u=v. If a=0, the situation splits: b=0 gives every real number as a solution; b≠0 gives none. These boundary cases explain why the hypothesis a≠0 cannot be dropped.

An existence proof may be nonconstructive: a complete case split can show that one of two candidates works without identifying which candidate in advance. That can establish ∃x P(x), but it does not supply an algorithm to compute a witness. A later algorithmic claim needs more than mere classical existence. Conversely, to refute existence, show **every** admissible candidate fails; checking a few failed candidates is insufficient.

## 8. Counterexamples and proof-error diagnosis

### 8.1 The exact form of a counterexample

To refute ∀x∈D P(x), present c∈D and prove ¬P(c). To refute ∀x∈D [P(x)→Q(x)], present c∈D for which P(c) is true and Q(c) is false. This is a constructive proof of ∃x∈D [P(x)∧¬Q(x)]. A sample with P(c) false makes the implication true at c and proves nothing against it. A sample outside D is irrelevant.

For a universal equation over real numbers, a zero or boundary value is often revealing, but it must satisfy the exact domain constraints. To refute “every integer n has n²>n,” n=0 works because 0²=0 is not greater than 0; n=1 also works. To refute “for all nonzero real x, x²>x,” x=1/2 works since 1/4<1/2, whereas x=0 is inadmissible. A finite search is excellent for **finding** such an example; failure to find one in a finite search is not a proof of a universal claim.

### 8.2 Common invalid arguments and their repairs

1. **Affirming the consequent:** From P→Q and Q, infer P. This is invalid. If P is “n is divisible by 4” and Q is “n is even,” n=2 makes Q true and P false. Repair: prove Q→P separately if it is true.
2. **Proving only the converse:** To prove P→Q, deriving P from Q addresses Q→P. Label the required direction before algebra.
3. **Circularity:** “Assume the desired conclusion Q and derive Q” supplies no proof of P→Q. A valid proof may temporarily assume Q only inside a separately justified contradiction or equivalence argument.
4. **Sample-to-universal jump:** Testing n=1,…,10 proves only ten instances. A universal claim needs an arbitrary n argument, exhaustive finite domain, or valid induction in the next chapter.
5. **Invalid cancellation:** From ac=bc infer a=b only if c≠0 in an integral domain. With c=0, every a,b satisfy ac=bc.
6. **Uncontrolled square roots or signs:** From x²=y² infer |x|=|y|, not x=y. From 0≤u²≤v² infer |u|≤|v|; the signs of u,v remain relevant.
7. **Missing cases or shifted domain:** A split that omits zero, negative integers, empty sets, or a boundary equality is incomplete. The theorem may still be true, but the proof is not finished.
8. **Witness smuggling:** In ∀x∃y R(x,y), choosing y before x has been fixed may accidentally prove the stronger and often false ∃y∀x R(x,y).

The appropriate repair depends on the claim: fill a missing case, restore an omitted hypothesis, replace a nonreversible step, or state a weaker true theorem. A counterexample to an overly strong statement can reveal the minimal hypothesis needed for a corrected one.

## 9. Fully worked problems

The problems progress from exact proof obligations to mixed advanced traps. The source labels identify related exercise *types*; every formulation and solution here is independently written.

### Problem 1 — A divisibility witness that survives zero (Berkeley CS70 type)

**Claim.** For all integers a,b,c, if a∣b and a∣c, then a∣(2b−3c). **Solution.** Fix arbitrary integers a,b,c satisfying the two premises. By definition choose u,v∈ℤ with b=au and c=av. Then 2b−3c=2au−3av=a(2u−3v). Because integers are closed under addition and multiplication, 2u−3v∈ℤ; it is the witness demanded by a∣(2b−3c). No step divided by a. If a=0, the premises force b=c=0, and 0∣0 is true under the stated definition. The edge case therefore agrees with the general proof.

### Problem 2 — A direct proof with an inequality boundary (MIT 6.042J type)

**Claim.** For 0≤x≤3, 1+9x−x³≥1. **Solution.** The goal is equivalent to 9x−x³≥0. Factor the expression *before* applying inequalities: 9x−x³=x(3−x)(3+x). The hypotheses imply x≥0, 3−x≥0, and 3+x≥3>0. A product of nonnegative real numbers is nonnegative, so 9x−x³≥0, giving the claim after adding 1. Equality occurs when x=0 or x=3, exactly the zeros of the first two factors in the domain. A proof that asserted strict positivity would be false at both endpoints.

### Problem 3 — A parity proof with two legitimate inner cases

**Claim.** For every integer n, 6∣3n(n+1). **Solution.** To prove divisibility by 6 we need an integer t with 3n(n+1)=6t. Every integer n is either 2k or 2k+1. In the first case, n(n+1)=2[k(n+1)], so take t=k(n+1). In the second case, n+1=2(k+1), so n(n+1)=2[n(k+1)], and take t=n(k+1). Both displayed t values are integers. This exhausts even and odd n, including negatives, and proves the outer universal claim. The witness can differ by case; it need not have a single displayed formula.

### Problem 4 — Set containment from a decomposed hypothesis

**Claim.** For any sets A,B,C, if A∖B⊆C, then A⊆B∪C. **Solution.** Let x be an arbitrary member of A. If x∈B, then x∈B∪C. Otherwise x∉B, hence x∈A∖B. The hypothesis now gives x∈C, and therefore x∈B∪C. The two cases x∈B and x∉B are exhaustive. Since the chosen x was arbitrary, A⊆B∪C. The reverse implication also holds: if A⊆B∪C and x∈A∖B, then x∈B∪C but x∉B, so x∈C. Thus the premise and conclusion are actually equivalent, but the requested forward proof did not assume that stronger fact.

### Problem 5 — Prove a necessary and sufficient inequality, with equality

**Claim.** For nonnegative reals x,y, (x+y)/2≥√(xy), with equality iff x=y. **Solution.** Begin with (x−y)²≥0. Expanding and adding 4xy yields (x+y)²≥4xy. Both x+y and 2√(xy) are nonnegative, so the monotonicity of square root gives x+y≥2√(xy); divide by positive 2. Equality through these steps occurs iff (x−y)²=0, which holds iff x=y. Conversely, if x=y≥0 then both sides equal x. This proves the two directions of the equality condition. The nonnegative domain is needed both for √(xy) and for taking square roots of the comparison without a sign ambiguity.

### Problem 6 — Contrapositive of an even-square claim (Cornell CS2800 type)

**Claim.** If n² is even for n∈ℤ, then n is even. **Solution.** The contrapositive says that odd n has odd n². Assume n is odd, so n=2k+1 for an integer k. Squaring gives n²=4k²+4k+1=2(2k²+2k)+1, which has the definition of an odd integer. Therefore the contrapositive holds, and so does the original implication. Testing only n=2 or n=3 would not prove it; the algebra works for the arbitrary k. The converse, even n→even n², is also true but is a different statement.

### Problem 7 — Negate the *whole* antecedent in a contrapositive

**Claim.** For real x, if x>0 and x²<4, then x<2. **Solution.** The direct proof is immediate because x>0 and x²<4 imply |x|<2, hence x<2. To audit the contrapositive, write it exactly: if x≥2, then **not**(x>0 and x²<4), that is x≤0 or x²≥4. Given x≥2, x²≥4, so the consequent disjunction holds. The common but incorrect transformation “x≥2 implies x≤0 and x²≥4” fails at x=2. De Morgan changes the conjunction to a disjunction.

### Problem 8 — Irrational conclusion by contrapositive (ETH Zürich type)

**Claim.** If t≥0 is irrational, then √t is irrational. **Solution.** The contrapositive is: if √t is rational, then t is rational. Suppose √t=p/q with p,q∈ℤ and q≠0. Squaring gives t=p²/q²; p² and q² are integers and q²≠0, so t is rational. The original claim follows. We used t≥0 so √t is a real number in the domain of the statement. The claim is not a proof that √r is irrational for every rational r: r=4 gives √r=2, a rational number. Keep the direction of the theorem.

### Problem 9 — Irrationality by a complete contradiction (Cornell/ETH type)

**Claim.** √2 is irrational. **Solution.** Assume the negation: √2=p/q for coprime integers p,q with q≠0. From p²=2q², p² is even. Problem 6 implies p even; write p=2r. Then 4r²=2q² and q²=2r², so q² is even and Problem 6 implies q even. Both p and q are divisible by 2, contradicting coprimality. Therefore the rational assumption is false. Reduced form is essential: without it, concluding that numerator and denominator are even would only show that a particular fraction was not reduced.

### Problem 10 — No largest prime, with the right logical target

**Claim.** There is no largest prime. **Solution.** Suppose contrariwise that the primes form a finite list p₁,…,pₖ containing all primes. The list is nonempty because 2 is prime. Let N=p₁···pₖ+1>1. Every integer N>1 has a prime divisor: among the finitely many positive divisors d of N with d>1, choose the least; if d=uv with 1<u<d and 1<v<d, then u would be a smaller divisor of N, so d is prime. Choose a prime divisor q∣N. By the assumed completeness of the list, q=pᵢ for some i, so q divides the product p₁···pₖ. It then divides N−p₁···pₖ=1, impossible for a prime q≥2. Hence no finite complete list exists, and in particular no largest prime exists: a supposed largest prime would bound all primes by a finite integer. N itself need not be prime; claiming that it is would create a gap.

### Problem 11 — A real inequality contradicted without illegal squaring

**Claim.** If x,y≥0, then √(xy)≤(x+y)/2. **Solution by contradiction.** Suppose x,y≥0 and √(xy)>(x+y)/2. Both sides are nonnegative, so squaring preserves the strict inequality: xy>(x+y)²/4. Multiply by positive 4 and rearrange to obtain 0>(x−y)². But a real square is always nonnegative, a contradiction. Therefore the claimed inequality holds. This is a separate valid route from Problem 5; its sign check before squaring is what makes the transformation legitimate.

### Problem 12 — An exhaustive case proof over negative integers too (ETH type)

**Claim.** If 5 does not divide integer n, then 5 divides n⁴−1. **Solution.** Division by 5 gives n=5k+r for a unique r∈{0,1,2,3,4}, even if n is negative. The premise excludes r=0. In the remaining four cases, r⁴ is respectively 1,16,81,256, all congruent to 1 modulo 5. Since n⁴−r⁴ is divisible by 5 by binomial expansion of (5k+r)⁴, n⁴−1 is divisible by 5 in every admissible case. Equivalently, each expansion term other than r⁴ contains a factor 5. The proof's exhaustiveness comes from the division algorithm, not from having tested four attractive examples.

### Problem 13 — A complete split at zero

**Claim.** For every real x, |x|²=x². **Solution.** If x≥0, then |x|=x, so |x|²=x². If x<0, then |x|=−x, and |x|²=(−x)²=x². The two cases cover all real x and do not overlap, although disjointness is not required. If the first case had x>0 instead, x=0 would be missing. The identity is true at zero, but an incomplete proof cannot borrow that fact silently.

### Problem 14 — An iff whose directions need different tactics

**Claim.** For every integer n, n is odd iff n² is odd. **Solution.** Forward: write n=2k+1 and expand n²=2(2k²+2k)+1, so n² is odd. Reverse: suppose n² is odd. To prove n odd by contrapositive, show that even n has even square. If n=2j, then n²=4j²=2(2j²), even. Thus if n² is not even, n cannot be even, so n is odd. The reverse direction is not established by repeating the forward calculation with the conclusion as an assumption; it has its own valid argument.

### Problem 15 — An existential witness chosen after the input (Stanford CS103 type)

**Claim.** For each integer n, there are integers r,s with r²−s²=4n. **Solution.** Fix arbitrary n∈ℤ. We need a difference of squares, so factor backward during discovery: r²−s²=(r−s)(r+s). Choose r−s=2 and r+s=2n; solving gives r=n+1 and s=n−1. Both are integers. Direct verification yields (n+1)²−(n−1)²=4n. This completes the universal proof because the construction works for arbitrary n, including n=0 and negative n. It proves ∀n∃r∃s, not ∃r∃s∀n.

### Problem 16 — Uniqueness requires two separate arguments

**Claim.** For any reals a,b with a≠0, exactly one real x solves ax+b=0. **Solution.** Existence: define x=−b/a. Division is legal since a≠0, and ax+b=−b+b=0. Uniqueness: let u,v be any two solutions. Subtract au+b=0 and av+b=0 to obtain a(u−v)=0. Since a≠0 and ℝ has no zero divisors, u−v=0 and hence u=v. At a=0 the claim can fail both ways: b≠0 gives no solution, while b=0 gives infinitely many. These are counterexamples to deleting the hypothesis.

### Problem 17 — An impossible fixed witness versus a valid dependent witness

**Claim A.** ∀x∈ℤ ∃y∈ℤ (y>x). **Solution.** Let x be arbitrary and take y=x+1. Then y∈ℤ and y>x, since 1>0. **Claim B.** ∃y∈ℤ ∀x∈ℤ (y>x). **Refutation.** Suppose a fixed integer y works for every integer x. Set x=y+1, an admissible integer. Then y>x becomes y>y+1, impossible. The difference between the claims is the dependency order, not a small change in wording.

### Problem 18 — A counterexample must make the premise true

**Claim to assess.** For every integer n, if n is even, then 4∣n. **Solution.** The claim is false: n=2 is an integer and even, but no integer k satisfies 2=4k, so 4∤2. The proposed “counterexample n=3” is invalid because 3 is odd; at n=3 the implication is true vacuously. The repaired theorem “if 4∣n, then n is even” is true: n=4k=2(2k). A refutation should report both the premise check and the failed conclusion.

### Problem 19 — A universal prime formula defeated beyond early samples (ETH type)

**Claim to assess.** For every positive integer n, n²−n+41 is prime. **Solution.** At n=41, the expression is 41²−41+41=41²=1681=41·41, which is composite. The value 41 belongs to the stated positive-integer domain, so it is a legitimate counterexample. Calculating prime values for n=1,…,40 would be evidence for those instances only; it would never establish the universal claim. The factorization at n=41 supplies the exact refutation.

### Problem 20 — Invalid squaring as a proof direction (Berkeley CS70 error type)

**Proposed argument.** “−3=3 because squaring each side gives 9=9.” **Diagnosis and repair.** Squaring preserves equality, so −3=3 would imply 9=9; the true consequent does not establish its antecedent. The map t↦t² is not injective on ℝ: t and −t have the same square. The exact deduction from x²=y² is (x−y)(x+y)=0, hence x=y or x=−y. For x=−3 and y=3, the second alternative holds. A valid proof of x=y from x²=y² would need an additional hypothesis, such as x≥0 and y≥0.

### Problem 21 — Detect a missed case in a claimed set equality

**Claim to assess.** For all sets A,B,C, A∖(B∩C)=(A∖B)∩(A∖C). **Solution.** Take A={1}, B={1}, C=∅. Then B∩C=∅ and A∖(B∩C)={1}. However A∖B=∅ and A∖C={1}, so their intersection is ∅. The claimed equality is false. Elementwise negation explains the correction: x∈A∖(B∩C) iff x∈A and ¬(x∈B∧x∈C) iff (x∈A∖B) or (x∈A∖C). The true identity therefore has a union on the right. The counterexample was chosen to make exactly one of B,C contain the test element.

### Problem 22 — A false uniqueness claim and its precise repair

**Claim to assess.** Every real number t has a unique real square root x satisfying x²=t. **Solution.** The claim fails in two distinct ways. For t=−1, no real x has x²=−1, because x²≥0 for all real x. For t=4, both x=2 and x=−2 satisfy x²=4, so uniqueness fails. The repaired theorem is: for each t≥0 there is exactly one **nonnegative** real x with x²=t, denoted √t. Existence follows from the real square-root property. If u,v≥0 and u²=v²=t, then (u−v)(u+v)=0. For t=0, u=v=0; for t>0, u+v>0, so u−v=0. Both cases yield uniqueness. This illustrates why existence and uniqueness have separate counterexample modes.

## 10. High-yield review: complete decision rules and difficult traps

This is a recall sheet *after* the detailed teaching and solved problems. Each rule states the required action, why it works, and the mistake it prevents. It cannot substitute for reading the preceding proofs.

**1. Parse the quantifier order before any algebra.** In ∀x∃y, choose y after fixing x and allow dependence y=y(x); in ∃y∀x, one fixed y must work for all x. Reversing these moves proves the wrong statement (Problem 17).

**2. Retain the domain in both proof and refutation.** For a universal claim over nonzero reals, a zero counterexample is inadmissible even if the displayed formula fails there. For a square-root claim, check whether its argument is nonnegative and whether the root is real (Problems 8 and 22).

**3. A universal implication needs an arbitrary admissible object.** Fix x∈D, assume P(x), derive Q(x), and only then generalize. A finite number of substitutions proves only finitely many instances unless the domain itself is exhausted (Problems 1 and 19).

**4. A counterexample to P→Q must satisfy P∧¬Q.** A value with false P makes the implication true at that value; it does not refute the theorem. Record the premise and failed conclusion explicitly (Problem 18).

**5. Unfold a definition into its witness form.** To prove a∣b, exhibit k∈ℤ with b=ak; to use a∣b, introduce such a k. Do not divide by a merely because the notation contains a divisor (Problem 1).

**6. Test zero before cancellation.** From ac=bc infer a=b only after c≠0 has been proved. If c=0, the equation contains no information about a and b. The same issue appears when cross-multiplying fractions with unknown denominators.

**7. Compute the exact contrapositive.** P→Q is equivalent to ¬Q→¬P; the converse Q→P is a separate theorem. For (P∧R)→Q, its contrapositive ends in ¬P∨¬R, not ¬P∧¬R (Problem 7).

**8. Distinguish contradiction from contrapositive.** A contradiction proof of P→Q assumes P∧¬Q and derives falsehood. A contrapositive proof assumes ¬Q and derives ¬P. Both are valid when their final obligations are met; an argument that assumes only ¬Q but merely derives Q is usually circular (Problems 6, 9, 11).

**9. Negate a quantified statement one layer at a time.** ¬∀x P(x) is ∃x ¬P(x); ¬∃x P(x) is ∀x ¬P(x). Thus ¬[∀x∃y R(x,y)] is ∃x∀y ¬R(x,y), with the same domains. Leaving either quantifier unchanged can invert the proof target.

**10. An iff has two obligations.** Prove P→Q and Q→P, possibly with different techniques. An arrow chain containing only one-way implications does not establish an equivalence (Problem 14).

**11. Case splits must cover all admissible inputs.** Over ℝ, x≥0 versus x<0 covers zero; x>0 versus x<0 does not. Over ℤ, residues 0,…,m−1 cover all integers when m>0 (Problems 12–13).

**12. Cases may overlap.** Overlap does not damage a case proof; every possible input only needs to belong to at least one proved case. Requiring disjointness wastes effort and may encourage an incorrect split.

**13. Existence requires a witness and verification.** A constructive solution must name an object in the domain and show it satisfies every property. A failed search is not a refutation of existence; to refute ∃x P(x), establish ∀x ¬P(x) (Problems 15–17).

**14. Uniqueness is existence plus at-most-one.** First produce a solution. Then take arbitrary solutions u,v and derive u=v. Showing at-most-one does not prove one exists, and finding one does not show it is unique (Problems 16 and 22).

**15. Prefer an equivalent forward derivation to unsafe reverse work.** Starting from the desired inequality and rearranging may identify an idea, but a final proof must begin from true hypotheses or make each reverse transformation explicitly reversible (Problems 2 and 5).

**16. Squaring loses sign.** x²=y² implies x=y or x=−y. To conclude x=y, add suitable sign assumptions or another argument. When squaring an inequality, first check both sides are nonnegative (Problems 11 and 20).

**17. Contradiction must end in a proved impossibility.** R∧¬R, a real square <0, or a violation of a reduced-fraction assumption is decisive. “This seems unlikely” is not. State precisely which assumption failed (Problems 9 and 11).

**18. Name every needed lemma and its hypotheses.** “Even square implies even integer” can be proved by contrapositive; do not use it as a magic cancellation of squares. A lemma over positive integers cannot automatically be applied to all integers (Problems 6 and 9).

**19. Boundary cases can decide theorem truth.** Try 0, 1, negative values, equality endpoints, and empty sets when their domains allow them. In Problem 2 equality holds at both endpoints; in Problem 21 a singleton and an empty set expose the wrong connective.

**20. Distinguish discovering a counterexample from certifying a theorem.** Computation can find a witness that refutes a universal claim. A finite computation that finds no failure proves only the checked finite domain. A mathematical proof must cover the remaining domain (Problem 19).

**21. The negation of “exactly one” has two branches.** Either no solution exists or at least two different solutions exist. An audit of a uniqueness claim should look for both failure modes (Problem 22).

**22. A proof may contain another proof method.** A direct proof can use cases to establish a sublemma; a contrapositive proof can use direct algebra; a contradiction proof can invoke earlier direct lemmas. Label the top-level obligation and ensure every nested branch closes (Problems 3 and 6).

**23. Make the final line match the exact goal.** Showing b=a·w is not enough for divisibility until w is shown to be an integer. Showing a candidate satisfies an equation is not enough for uniqueness until every other candidate is compared. Restate the quantified conclusion after closing the local argument.

**24. A counterexample is the strongest answer to a false universal claim.** Once an admissible c with ¬P(c) is verified, additional examples are optional. To repair the theorem, identify whether its failure came from a missing hypothesis, incorrect direction, wrong connective, or overly broad domain (Problems 18–22).

### Strategy card

| Statement form seen in a difficult question | First attempt | If blocked, or if false is suspected |
| --- | --- | --- |
| ∀x(P→Q) with algebraic definitions | Fix arbitrary x, assume P, construct a Q witness. | Try ¬Q→¬P; search x with P∧¬Q. |
| Negative target such as irrationality | Write the negation explicitly. | Derive a denominator, parity, or domain contradiction. |
| Piecewise, sign, or residue condition | Prove exhaustive cases, including boundaries. | Test the missing boundary or residue as counterexample. |
| P iff Q | Separate forward and reverse directions. | Test whether one converse fails before claiming iff. |
| ∀x∃y or unique existence | Respect witness order; verify membership and property. | Test fixed-witness confusion; audit existence and uniqueness separately. |

## 11. References and limits

1. Massachusetts Institute of Technology. Eric Lehman, F. Thomson Leighton, and Albert R. Meyer, *Mathematics for Computer Science*, 6.042J, Spring 2015, Chapter 1 §§1.1 and 1.5–1.8. [Official course text](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf).
2. Stanford University. CS103 course staff, *Guide to Proofs*, sections “Direct Proofs,” “Unpacking Compound Statements,” “Existentially-Quantified Statements,” “Proof by Contrapositive,” “Proof by Contradiction,” and “Proof by Cases”; accessed 2026-09-29. [Official guide](https://web.stanford.edu/class/cs103/guide_to_proofs).
3. University of California, Berkeley. CS70, *Discrete Mathematics and Probability Theory*, Summer 2024 Course Notes, Note 2, §§2–8. [Official course note](https://su24.eecs70.org/assets/pdf/notes/n2.pdf).
4. Cornell University. Rafael Pass and Wei-Lung Dustin Tseng, *A Course in Discrete Structures*, CS2800 2015 archive, Chapter 2 §§2.1–2.2. [Official course text](https://courses.cs.cornell.edu/cs2800/2015fa/handouts/pass_tseng_discmath.pdf).
5. ETH Zürich. Ueli Maurer, *Diskrete Mathematik*, Autumn 2024, Chapter 2 §§2.6.1–2.6.9. Original German-language course notes; this chapter independently explains the selected mathematical patterns in English. [Official course notes](https://crypto.ethz.ch/teaching/DM24/ln/DM24_LN.pdf).
6. University of Oxford. *Introduction to University Mathematics*, 2025–26, “4 Logic and Proof,” supplementary comparison of methods and counterexamples. [Official course lesson](https://courses.maths.ox.ac.uk/mod/page/view.php?id=65664).

These references document the accessible course texts actually compared, not an exhaustive catalogue of all university courses. The original exercises are not reproduced as a complete course question bank. The chapter has been checked against its stated proof-method boundary; an unseen problem may combine these methods with later material or require a new insight. Reading the chapter alone cannot establish a literal guarantee of success on every future examination question. The Iranian entrance-exam archive is intentionally deferred to the final month.
