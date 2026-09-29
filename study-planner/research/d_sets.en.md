# Sets and Set Operations

**Discrete Mathematics · Chapter 2 · student-approved English edition**

The prerequisites are the meaning of a proposition, quantifiers, and the basic equivalence laws from Chapter 1. This chapter covers extensional sets, membership and containment, finite and indexed set operations, power sets, products, finite cardinality, and the proof methods that connect them. Relations, functions, systematic counting, and induction are separate chapters. The worked bank is deliberately extensive: a difficult set question usually fails at an exact definition or boundary case, not at a missing formula.

## 1. Course selection and coverage contract

Four principal written courses were read and combined for this chapter: MIT 6.042J (Lehman, Leighton, Meyer, 2015, section 4.1; course instructors Meyer and Chlipala); Stanford CS103 (Amy Liu's Winter 2024 course archive, *Guide to Proofs on Sets*); Cornell CS2800 (Pass and Tseng, 2015, section 1.1); and Carnegie Mellon 15-151 (Sutner, 2022, the Set Operations and Cartesian Products slides). UC Berkeley CS70 Summer 2024 Note 0 was read as a fifth, supplemental text. MIT gives concise definitions and an elementwise distributive proof; Stanford explains proof construction; Cornell ties diagrams and products to computer-science notation; CMU supplies indexed families and subtle edge cases; Berkeley independently confirms the foundational notation. Exact links and review limits appear in [References](#references).

This is a bounded comparison of publicly accessible written course materials, not a claim to have searched every university course worldwide. No syllabus-only entry is counted as a read course. The topic and reasoning-pattern audit is recorded with the manuscript; it controls the scope and the solved-problem bank. Archived Iranian entrance-exam questions are reserved for the final study month, as requested. A finished chapter cannot mathematically guarantee a correct response to every unseen examination question, but the definitions, proofs, counterexamples, and solved problems below are designed to expose the identifiable failure modes in this chapter boundary.

## 2. Objects, membership, and equality

### 2.1 What a set asserts

A **set** is an unordered collection with no repeated members. The notation x∈A means that object x is a member of set A; x∉A means it is not. Thus {2,1,2}={1,2}, whereas (1,2) and (2,1) are different ordered pairs. A set may contain other sets: ∅, {∅}, and {{∅}} are three different objects. The empty set ∅ has no members; the singleton {∅} has one member, namely ∅. Therefore ∅∈{∅}, ∅⊆{∅}, and ∅≠{∅}. The first statement is membership, the second containment, and neither can replace the other.

For any sets A and B, **extensional equality** means exactly the same members:

<div class="formula-block">A=B ⇔ ∀x (x∈A ↔ x∈B).</div>

This is the most reliable route to an identity. Prove both A⊆B and B⊆A, or prove the membership biconditional directly. A Venn diagram can suggest an identity or show a counterexample region, but a correctly quantified elementwise argument proves it. Reordering or repeating entries in roster notation never changes a set.

Set-builder notation {x∈D : P(x)} selects those elements of a specified domain D for which P is true. For example, {n∈ℤ : n²<10}={−3,−2,−1,0,1,2,3}. The displayed domain matters: {x∈ℝ : x²=2} and {x∈ℚ : x²=2} are not equal. Unrestricted phrases of the form “the set of every object satisfying P” can lead to Russell's paradox; in this course, set-builder notation always uses a specified ambient set or an accepted construction. This caution is about legitimate set formation, not a computational procedure.

### 2.2 Subsets, proper subsets, and their logical form

A⊆B means every member of A belongs to B: ∀x(x∈A→x∈B). The relation is **reflexive** (A⊆A) and **transitive** (A⊆B and B⊆C imply A⊆C). It is **antisymmetric**: A⊆B and B⊆A imply A=B. A⊊B means A⊆B and A≠B, equivalently A⊆B and some b∈B∖A exists. The symbol ⊂ is used inconsistently across books, so this chapter always writes ⊆ or ⊊.

The empty set is a subset of every set, including itself, because there is no counterexample x∈∅ with x∉A. It is a **proper** subset of A precisely when A is nonempty. Membership does not transfer to containment: 2∈{1,2}, but 2⊆{1,2} is not a well-formed statement under ordinary typed arithmetic because 2 is an integer, not a set of integers. Conversely {2}⊆{1,2}, while {2}∈{1,2} is false. Some set-theoretic foundations encode numbers as sets; that encoding does not erase the intended types in a discrete-mathematics problem.

To disprove A⊆B, exhibit a **witness** x∈A with x∉B. To disprove A=B, one witness in the symmetric difference suffices. To prove A⊊B, first prove containment and then give a member of B outside A. Showing one common member or a diagram that “looks contained” is insufficient.

## 3. The algebra of finite set operations

### 3.1 Exact membership tests

Fix a universe U containing all sets under discussion whenever a complement is used. For x∈U:

| Operation | Membership statement | Meaning |
| --- | --- | --- |
| A∪B | x∈A or x∈B | Inclusive or; common members appear once. |
| A∩B | x∈A and x∈B | Members shared by both. |
| A∖B | x∈A and x∉B | Remove B's members from A. |
| A<sup>c</sup>=U∖A | x∈U and x∉A | Relative complement in U. |
| A△B | exactly one of x∈A, x∈B | Symmetric difference, (A∖B)∪(B∖A). |

The expression A∖B is generally different from B∖A; it is not numerical subtraction. The operations ∪, ∩, and △ are commutative. Complement changes if U changes: with A={1} and U={1,2}, A<sup>c</sup>={2}; with U={1,2,3}, it is {2,3}. Never cancel or complement sets before establishing their universe.

The four regions determined by A and B in U are A∩B, A∖B, B∖A, and U∖(A∪B). They are pairwise disjoint and their union is U. Every two-set identity can be checked region by region. For three sets there are eight membership patterns (the three yes/no choices), a useful finite model for finding a counterexample. A region diagram is an aid to **discovery**, while membership arguments and the Boolean-pattern table provide the proof.

<figure class="logic-diagram"><svg viewBox="0 0 560 220" role="img" aria-label="Four disjoint regions of a universe formed by two overlapping sets A and B"><rect x="12" y="12" width="536" height="194" rx="10" fill="#f6fafc" stroke="#8caabd" stroke-width="2"/><circle cx="230" cy="110" r="82" fill="#b8d9e9" fill-opacity=".67" stroke="#327795" stroke-width="2"/><circle cx="330" cy="110" r="82" fill="#ebd1aa" fill-opacity=".7" stroke="#ad7944" stroke-width="2"/><text x="28" y="38" font-size="18" fill="#233e52">U</text><text x="185" y="118" font-size="15" fill="#203748">A ∖ B</text><text x="272" y="118" font-size="15" fill="#203748">A ∩ B</text><text x="369" y="118" font-size="15" fill="#203748">B ∖ A</text><text x="42" y="184" font-size="15" fill="#203748">outside A ∪ B</text></svg><figcaption>The four region labels are membership conditions; they do not imply that each region is nonempty.</figcaption></figure>

### 3.2 Laws and a proof strategy

Under the fixed universe U, the following laws are elementwise versions of the propositional laws already studied:

| Law | Set identity |
| --- | --- |
| Identities | A∪∅=A; A∩U=A. |
| Domination | A∪U=U; A∩∅=∅. |
| Idempotence | A∪A=A; A∩A=A. |
| Complements | A∪A<sup>c</sup>=U; A∩A<sup>c</sup>=∅; (A<sup>c</sup>)<sup>c</sup>=A. |
| Commutativity | A∪B=B∪A; A∩B=B∩A. |
| Associativity | (A∪B)∪C=A∪(B∪C); likewise for ∩. |
| Distributivity | A∩(B∪C)=(A∩B)∪(A∩C); A∪(B∩C)=(A∪B)∩(A∪C). |
| Absorption | A∪(A∩B)=A; A∩(A∪B)=A. |
| De Morgan | (A∪B)<sup>c</sup>=A<sup>c</sup>∩B<sup>c</sup>; (A∩B)<sup>c</sup>=A<sup>c</sup>∪B<sup>c</sup>. |

For example, x∈A∩(B∪C) iff [x∈A and (x∈B or x∈C)] iff [(x∈A and x∈B) or (x∈A and x∈C)] iff x∈(A∩B)∪(A∩C). This proof explicitly maps ∩ to “and” and ∪ to inclusive “or.” To negate membership, use De Morgan on the **whole condition**. For example, A∖(B∪C)=(A∖B)∩(A∖C), whereas (A∖B)∪(A∖C)=A∖(B∩C). A parenthesis error swaps the two results.

Symmetric difference is associative because membership is exclusive-or: x∈(A△B)△C iff an odd number of the three membership statements is true, iff x∈A△(B△C). Also A△A=∅, A△∅=A, and A△B=(A∪B)∖(A∩B). A△B=∅ iff A=B. A△B=U iff B=U∖A. These follow region by region; they do not require A and B to be disjoint.

### 3.3 Containment, monotonicity, and disjointness

A⊆B iff A∩B=A iff A∪B=B. Prove the forward direction by membership; for the reverse, if A∩B=A, every x∈A belongs to A∩B and hence B. Equivalently, A∖B=∅. These are useful **decision rules** when an expression contains a hidden containment assertion.

If A⊆B, then A∪C⊆B∪C and A∩C⊆B∩C. Complement reverses containment: B<sup>c</sup>⊆A<sup>c</sup>. Difference is monotone in its left argument but antitone in its right: A⊆B implies A∖C⊆B∖C, while C⊆D implies A∖D⊆A∖C. State the direction before manipulating a difficult inequality. A and B are disjoint iff A∩B=∅; neither set needs to be empty. Pairwise disjoint sets have no element in any two distinct members of the family.

## 4. Families, products, and finite size

### 4.1 Indexed families, including an empty index set

An indexed family (A<sub>i</sub>)<sub>i∈I</sub> assigns a set to each index i∈I. Its union contains x iff at least one i∈I satisfies x∈A<sub>i</sub>; its intersection contains x iff **every** i∈I satisfies x∈A<sub>i</sub>. These are quantified membership tests:

<div class="formula-block">x∈⋃<sub>i∈I</sub>A<sub>i</sub> ⇔ ∃i∈I: x∈A<sub>i</sub>;&nbsp; x∈⋂<sub>i∈I</sub>A<sub>i</sub> ⇔ ∀i∈I: x∈A<sub>i</sub>.</div>

Repeated set values at different indices do not alter the union or intersection. With a common universe U, ⋃<sub>i∈∅</sub>A<sub>i</sub>=∅ and ⋂<sub>i∈∅</sub>A<sub>i</sub>=U: the existential condition is false and the universal condition is vacuously true for every x∈U. Without a declared U, the empty intersection has no canonical set value in ordinary set theory. Do not replace it by ∅. Generalized De Morgan, under U, gives (⋃<sub>i∈I</sub>A<sub>i</sub>)<sup>c</sup>=⋂<sub>i∈I</sub>A<sub>i</sub><sup>c</sup> and its dual, even for I=∅ under these conventions.

If I is empty, “each A<sub>i</sub> is nonempty” holds vacuously but gives no member of ⋂A<sub>i</sub>; the latter depends on U. If I is nonempty and each A<sub>i</sub> is nonempty, their intersection can still be empty: {1}∩{2}=∅. Moving an existential choice outside a universal claim is generally invalid. For example, every A<sub>i</sub> may have some member, but there need not be one member common to all A<sub>i</sub>.

### 4.2 Cartesian products and ordered tuples

The Cartesian product A×B={(a,b):a∈A and b∈B}. Equality of ordered pairs means (a,b)=(c,d) iff a=c and b=d. Hence A×B and B×A generally differ as sets, even when their finite sizes agree. A×∅=∅×A=∅. A² abbreviates A×A; A<sup>n</sup> denotes length-n sequences with entries in A. The n=0 case contains the one empty tuple, so A<sup>0</sup> has one element even if A=∅, under the standard sequence convention. For n>0, ∅<sup>n</sup>=∅.

Products distribute over union and intersection **in the factor being varied**:

<div class="formula-block">A×(B∪C)=(A×B)∪(A×C);&nbsp; A×(B∩C)=(A×B)∩(A×C).</div>

The same holds on the left. For example, (a,b) is in (A×B)∩(A×C) iff a∈A and b∈B and b∈C, iff (a,b)∈A×(B∩C). A more tempting formula, (A×B)∩(C×D)=(A∩C)×(B∩D), is also true by matching **both coordinates**. But A×B⊆C×D does **not** always imply A⊆C and B⊆D: if A or B is empty, the left product is empty whatever C and D are. If A and B are both nonempty, choose witnesses in the opposite factors to derive the two containments.

### 4.3 Power sets and cardinality

The **power set** P(A)={S:S⊆A} is the set of all subsets of A. Always ∅∈P(A) and A∈P(A). P(∅)={∅}, which has one member; ∅ itself has zero. The distinction between ∈ and ⊆ becomes especially important here: S∈P(A) iff S⊆A, but S⊆P(A) means every member of S is itself a subset of A. The statements are different.

If finite A has n elements, each element can be included or excluded independently in a subset, giving |P(A)|=2<sup>n</sup>. More specifically, the subsets of size k number C(n,k); summing over k yields ∑<sub>k=0</sub><sup>n</sup>C(n,k)=2<sup>n</sup>. This identity is stated here as a connection; systematic combinations and counting proofs belong to the counting chapter. For finite A,B, |A×B|=|A||B|. Also |A∪B|=|A|+|B|−|A∩B|. The subtraction corrects double counting, even if one set is empty. These formulas are not asserted for arbitrary infinite cardinals using ordinary integer arithmetic.

For three finite sets, count each element by its membership multiplicity to obtain

<div class="formula-block">|A∪B∪C|=|A|+|B|+|C|−|A∩B|−|A∩C|−|B∩C|+|A∩B∩C|.</div>

An element in exactly one set has coefficient 1. An element in exactly two has coefficient 2−1=1. An element in all three has coefficient 3−3+1=1. This verifies the formula without assuming pairwise disjointness. The general inclusion–exclusion theorem and advanced applications are deferred to the counting chapter.

Finally, A⊆B iff P(A)⊆P(B): if A⊆B, every subset of A is a subset of B; conversely, A∈P(A), so P(A)⊆P(B) forces A∈P(B), meaning A⊆B. For finite A, B, P(A∩B)=P(A)∩P(B). In contrast, P(A∪B) generally **strictly contains** P(A)∪P(B), because a mixed subset may draw elements from both sides without being wholly inside either.

## 5. Worked problems: definitions, proofs, and difficult boundaries

The first problems rehearse exact syntax; later ones combine laws, quantifiers, finite counting, and counterexamples. The wording and solutions below are original, while the proof patterns are linked to the source texts in the references. Read the full solution after first following the membership conditions yourself; no answer is required from the student during the first reading.

### Problem 1 — Nested emptiness and precise notation

Let A={∅,{∅}}. Determine |A|, whether ∅∈A, ∅⊆A, {∅}∈A, {∅}⊆A, and whether {{∅}}⊆A. List P(A).

**Solution.** The two members of A are the empty set and the singleton containing the empty set; they are distinct, so |A|=2. Both ∅∈A and {∅}∈A are true by the roster. ∅⊆A is true for every A. For {∅}⊆A, its sole member is ∅, and ∅∈A, so it is true. For {{∅}}⊆A, its sole member is {∅}, which is also in A, so it is true. The four subsets are ∅, {∅}, {{∅}}, and {∅,{∅}}. Notice that {∅} occurs both as a member of A and as a subset of A, but those truths require different checks. The braces in {{∅}} create a third object, not a duplicate spelling of {∅}.

### Problem 2 — Set builder and the domain trap

Let S={x∈ℤ : x²≤8}, T={x∈ℝ : x²≤8}, and V={x∈ℤ : x²<9}. Decide S=V and S=T.

**Solution.** Among integers, x²≤8 permits x∈{−2,−1,0,1,2}; x²<9 permits exactly the same integers, so S=V. In the real domain, T=[−√8,√8], which includes 1/2 and infinitely many other nonintegers. Since 1/2∈T but 1/2∉S, S≠T. This single witness also proves T⊄S. Although S⊆T, the logical predicates alone do not determine equality without their domains.

### Problem 3 — Proving equality by two inclusions

Prove A=(A∩B)∪(A∖B) for arbitrary sets A and B. Explain why disjointness matters.

**Solution.** If x∈A, either x∈B or x∉B. In the first case x∈A∩B; in the second x∈A∖B. Thus A⊆(A∩B)∪(A∖B). Conversely, membership in either term implies membership in A, so the union is contained in A. The two inclusions give equality. Also (A∩B)∩(A∖B)=∅, since membership would require x∈B and x∉B at once. Thus A has been partitioned into the part inside B and the part outside B; for finite A, their cardinalities add to |A|. This problem follows the two-containment and partition patterns shown in Cornell CS2800, with an independently written proof.

### Problem 4 — A difference identity with every parenthesis visible

Prove A∖(B∪C)=(A∖B)∩(A∖C). Then identify the expression equal to (A∖B)∪(A∖C).

**Solution.** For arbitrary x, x∈A∖(B∪C) iff x∈A and x∉B∪C. The second condition means x∉B and x∉C, so the whole condition is (x∈A and x∉B) and (x∈A and x∉C), exactly membership in (A∖B)∩(A∖C). For the union, membership means (x∈A and x∉B) or (x∈A and x∉C). Distribute the common x∈A to obtain x∈A and (x∉B or x∉C), which by De Morgan is x∈A and x∉B∩C. Thus (A∖B)∪(A∖C)=A∖(B∩C). Replacing ∩ by ∪ in the last expression is the characteristic error.

### Problem 5 — Conditional simplification versus cancellation

Assume A⊆B. Simplify A∩B, A∪B, A∖B, B∖A, and A△B. Does A∪C=B∪C imply A=B?

**Solution.** Containment gives A∩B=A and A∪B=B. Since no member of A lies outside B, A∖B=∅. The set B∖A cannot generally be simplified to ∅: take A={1}, B={1,2}. Because A∖B=∅, symmetric difference reduces to B∖A. Union cannot be cancelled: take A={1}, B={2}, and C={1,2}. Then A∪C=B∪C=C even though A≠B. The algebra of sets resembles Boolean algebra, not a cancellative group under union.

### Problem 6 — Distributive law by element semantics

Prove A∪(B∩C)=(A∪B)∩(A∪C), then give an explicit counterexample to the false formula A∪(B∩C)=(A∪B)∩C.

**Solution.** x∈A∪(B∩C) iff x∈A or (x∈B and x∈C). Distributivity of propositions changes this to (x∈A or x∈B) and (x∈A or x∈C), the right-hand membership condition. For the proposed false formula, let A={1}, B=C=∅. Its left side is {1}; its right side is ({1}∪∅)∩∅=∅. The missing A on the second factor loses elements that belong only to A. This is the dual set-distribution pattern; compare MIT 6.042J's elementwise treatment of the other direction.

### Problem 7 — When does an inclusion become equality?

Prove A∩B⊆A∪B. Characterize exactly when A∩B=A∪B.

**Solution.** Every x∈A∩B is in both sets and hence in at least one, proving the inclusion. If A=B, both sides equal A, so equality holds. Conversely, assume A∩B=A∪B. For any x∈A, x∈A∪B and thus x∈A∩B, giving x∈B; hence A⊆B. Symmetrically B⊆A. Therefore A=B. The equality condition is stronger than merely having a nonempty intersection. With A=B=∅ it still holds.

### Problem 8 — Symmetric difference as parity

Let U={1,2,3,4,5}, A={1,2,4}, B={2,3,4}, C={1,3,5}. Compute (A△B)△C and A△(B△C), and explain why they agree generally.

**Solution.** A△B={1,3}. Hence (A△B)△C={1,3}△{1,3,5}={5}. Next B△C={1,2,4,5}; A△(B△C)={1,2,4}△{1,2,4,5}={5}. For any x, assign a bit to its membership in each set. Symmetric difference is bitwise exclusive-or, so x survives either grouped expression exactly when its three bits contain an odd number of ones. The agreement therefore holds for every x, including elements outside all three sets. A single numeric example illustrates but does not prove the general identity.

### Problem 9 — Symmetric difference determines equality

Show A△B=∅ iff A=B. Then decide whether A△B=A∪B iff A∩B=∅.

**Solution.** If A△B=∅, there is no element exclusively in A or exclusively in B, so every x belongs to A iff it belongs to B; extensionality gives A=B. If A=B, no element belongs to exactly one, so the symmetric difference is empty. Also A△B=(A∪B)∖(A∩B). If A∩B=∅, removing it changes nothing, so A△B=A∪B. Conversely, if these sets are equal and x were in A∩B, then x would be in A∪B but not in A△B, a contradiction. The converse relies on a hypothetical common member, not on cardinalities.

### Problem 10 — Indexed operations and alternating sets

Let U=ℕ={0,1,2,…}; for each n≥0 define A<sub>n</sub>={k∈ℕ:k≥n}. Find ⋃<sub>n≥0</sub>A<sub>n</sub>, ⋂<sub>n≥0</sub>A<sub>n</sub>, and the corresponding union and intersection when the index set is empty.

**Solution.** A<sub>0</sub>=ℕ, so the union is ℕ. For the intersection, fix any k∈ℕ and choose n=k+1; then k∉A<sub>n</sub>. No k is in all A<sub>n</sub>, so the intersection is ∅. With no indices, there is no witness for existential membership, hence the union is ∅. Every x∈U satisfies the universal membership condition over an empty index set, hence the empty intersection is U=ℕ. The nonempty-index intersection ∅ and the empty-index intersection U are different questions. CMU's indexed-family material motivates this boundary check.

### Problem 11 — Quantifier order hidden inside a family claim

For I={1,2}, take A<sub>1</sub>={1} and A<sub>2</sub>={2}. Evaluate “∀i∈I ∃x∈A<sub>i</sub>” and “∃x ∀i∈I (x∈A<sub>i</sub>).”

**Solution.** The first statement is true: choose x=1 for i=1 and x=2 for i=2. The witness may depend on i. The second is false because it requires a single x∈A<sub>1</sub>∩A<sub>2</sub>, but the intersection is empty. In set language, nonempty members of a family do not imply a nonempty common intersection. The attempted exchange of ∀ and ∃ is invalid; this is a logic error disguised as a set fact.

### Problem 12 — Product distribution and the empty-factor exception

Prove (A×B)∩(C×D)=(A∩C)×(B∩D). Then decide if A×B⊆C×D implies A⊆C and B⊆D.

**Solution.** An ordered pair (x,y) belongs to the left side iff x∈A, y∈B, x∈C, and y∈D. Regrouping by coordinate gives x∈A∩C and y∈B∩D, exactly membership on the right. The proposed implication is false without nonemptiness: take A={1}, B=∅, C=∅, D={2}. Both products are empty, so containment holds; A⊆C is false and B⊆D is true. If A and B are nonempty and A×B⊆C×D, choose b₀∈B. For any a∈A, (a,b₀) lies in C×D, so a∈C; thus A⊆C. Similarly choose a₀∈A to prove B⊆D. The nonempty witnesses are indispensable. This product-factor reasoning corresponds to CMU's Cartesian-products slides; the proof here uses ordered-pair membership at every step.

### Problem 13 — Power sets, three different containments

Take A={1,2} and B={2,3}. Find P(A∩B), P(A)∩P(B), and P(A∪B). Give one member of P(A∪B) absent from P(A)∪P(B).

**Solution.** A∩B={2}, so P(A∩B)={∅,{2}}. A subset belongs to both P(A) and P(B) exactly when it is contained in both A and B, hence exactly when it is contained in A∩B; therefore P(A)∩P(B)={∅,{2}}. The union A∪B={1,2,3} has eight subsets. The mixed subset {1,3} is in P(A∪B) but neither P(A) nor P(B), because 3∉A and 1∉B. Thus P(A)∪P(B) is strictly smaller than P(A∪B) here. It is wrong to distribute P over ∪ as if P were an intersection or union symbol.

### Problem 14 — A nested power-set test

Let A={∅,{∅}}. Decide whether ∅∈P(A), {∅}∈P(A), {∅}⊆P(A), and P(∅)∈P(A).

**Solution.** Since ∅⊆A, ∅∈P(A). Since ∅∈A, the singleton {∅} is a subset of A, so {∅}∈P(A). To test {∅}⊆P(A), check its sole member ∅; it is in P(A), so this is true. Finally P(∅)={∅}; this is already known to be a subset of A, hence P(∅)∈P(A). The four statements happen to be true here, but for four separate typed reasons. Replacing any ∈ by ⊆ without checking the objects would be invalid.

### Problem 15 — Counting with overlapping sets

For finite sets A,B,C, suppose |A|=18, |B|=15, |C|=12, |A∩B|=6, |A∩C|=5, |B∩C|=4, and |A∩B∩C|=2. Find |A∪B∪C| and the number in exactly two sets.

**Solution.** Inclusion–exclusion gives 18+15+12−6−5−4+2=32. The pairwise intersections each include the two members of the triple intersection. Hence exactly two sets contain (6−2)+(5−2)+(4−2)=4+3+2=9 members. As a cross-check, exactly three has 2 and exactly one has 32−9−2=21. The seven internal Venn-region counts are nonnegative: AB-only 4, AC-only 3, BC-only 2, A-only 18−4−3−2=9, B-only 15−4−2−2=7, C-only 12−3−2−2=5, triple 2; their sum is 32. This check detects inconsistent data or arithmetic before an answer is accepted.

### Problem 16 — Power-set monotonicity in both directions

Prove P(A)⊆P(B) iff A⊆B. Does P(A)=P(B) imply A=B?

**Solution.** If A⊆B, every S⊆A is also a subset of B by transitivity, so every S∈P(A) lies in P(B). Conversely, suppose P(A)⊆P(B). Because A⊆A, A∈P(A), hence A∈P(B); the definition of P(B) says A⊆B. If the power sets are equal, both subset directions hold and therefore A=B. Using the particular element A∈P(A) makes the reverse implication immediate; checking only singleton subsets would also work but would require more steps.

### Problem 17 — Relative complements and generalized De Morgan

Let U={1,2,3,4}, I={1,2}, A<sub>1</sub>={1,2}, A<sub>2</sub>={2,3}. Verify (⋃<sub>i∈I</sub>A<sub>i</sub>)<sup>c</sup>=⋂<sub>i∈I</sub>A<sub>i</sub><sup>c</sup>. Explain why the same law holds for I=∅ under U.

**Solution.** The union is {1,2,3}, so its complement in U is {4}. The complements are {3,4} and {1,4}; their intersection is {4}. Generally, x lies outside the union iff there is no i with x∈A<sub>i</sub>, iff for every i, x∉A<sub>i</sub>, iff x belongs to every A<sub>i</sub><sup>c</sup>. For I=∅, the left side is (∅)<sup>c</sup>=U; the right side is the empty intersection, also U by the fixed-universe convention. Without U the complement and that empty intersection are not defined by this chapter's notation.

### Problem 18 — A common false inference about differences

Is A∖C=B∖C enough to conclude A=B? If not, give a minimal counterexample and identify an additional condition under which it does follow.

**Solution.** No. With A={1}, B=∅, and C={1}, both differences are ∅ but A≠B; removing C hides the disagreement. If both A and B are disjoint from C, then A∖C=A and B∖C=B, so equality of the differences does imply A=B. More generally, if A∩C=B∩C as well as A∖C=B∖C, the decomposition in Problem 3 gives A=(A∩C)∪(A∖C)=(B∩C)∪(B∖C)=B. The two conditions recover both the part inside C and the part outside it.

### Problem 19 — A power-set identity and a false dual

Prove P(A∩B)=P(A)∩P(B). Find necessary and sufficient conditions for P(A∪B)=P(A)∪P(B).

**Solution.** For any set S, S∈P(A∩B) iff S⊆A∩B iff (S⊆A and S⊆B) iff S∈P(A)∩P(B). For the union identity, if A⊆B, then A∪B=B and P(A)⊆P(B), so both sides equal P(B); the same holds if B⊆A. Conversely, suppose neither A⊆B nor B⊆A. Choose a∈A∖B and b∈B∖A. Then {a,b}⊆A∪B, so {a,b}∈P(A∪B). But b∉A, so {a,b}∉P(A); and a∉B, so {a,b}∉P(B). Therefore equality fails. The identity holds **exactly when A⊆B or B⊆A**. This is a full characterization, not merely one counterexample.

### Problem 20 — Checking a proposed identity with one membership pattern

Someone claims A△(B∩C)=(A△B)∩(A△C). Decide whether it is an identity. If false, give a one-element universe counterexample and explain the pattern.

**Solution.** Let U={x}, A={x}, B=C=∅. On the left, B∩C=∅, so A△(B∩C)={x}. On the right, A△B=A△C={x}, and their intersection is {x}; this pattern happens to agree, so it is **not** a counterexample. Try the pattern x∉A, x∈B, x∈C: take A=∅ and B=C={x}. The left side is ∅△{x}={x}; the right side is ({x})∩({x})={x}, again agreement. Try x∈A, x∈B, x∉C: left side A△∅={x}; right side (A△B)∩(A△C)=∅∩{x}=∅. Thus with A=B={x}, C=∅, the identity is false. The solution demonstrates a disciplined counterexample search: enumerate membership bits and reject candidate patterns that do not actually separate the sides. A Venn diagram alone can conceal this mistake.

## 6. High-yield review: exact decisions and examination traps

This section condenses the already taught material into a usable solving procedure. It cannot replace the definitions and proofs above. Every row states a complete test or an actionable correction rather than a disconnected keyword.

### 6.1 A decision procedure for any set expression

1. **Identify the object types.** Determine which symbols are elements, sets, families of sets, ordered pairs, and integers. If the expression uses ∈, test a member; if it uses ⊆, test every member of the left set. Never exchange the two symbols on visual similarity.
2. **Write the universe when complements occur.** A<sup>c</sup> means U∖A. If U is unspecified, ask what ambient set the problem provides before calculating a complement or an empty indexed intersection.
3. **Reduce each operation to one arbitrary element x.** Translate ∪ to inclusive or, ∩ to and, ∖ to “in left and not in right,” and △ to exclusive-or. Preserve parentheses.
4. **For a claimed equality, prove both membership directions.** Use a biconditional chain or two subset proofs. A finite drawing or tested instance is evidence for discovery, not a general proof.
5. **For a claimed inclusion, seek a violating witness.** One x in the proposed left side but outside the right side disproves it. If the inclusion is true, begin with arbitrary x in the left side and follow its definition.
6. **Check the smallest boundary cases before finalizing.** Try ∅, singletons, overlapping sets, disjoint sets, equal sets, nested sets, and U. For Cartesian-product claims, explicitly test an empty factor. For indexed claims, test an empty index set.
7. **Only then use cardinalities.** Counting equal sizes never proves set equality. If a finite set is already known to be contained in another and the sizes agree, equality follows; without containment it does not.

### 6.2 Formula and boundary sheet

| Situation | Exact rule | Trap and remedy |
| --- | --- | --- |
| Equality | A=B iff ∀x(x∈A↔x∈B), or A⊆B and B⊆A. | Equal cardinality alone is insufficient; find a missing member or prove two inclusions. |
| Proper containment | A⊊B iff A⊆B and ∃b∈B∖A. | A=∅ is not a proper subset of B when B=∅. |
| Empty set | ∅⊆A always; ∅∈A only if ∅ is explicitly a member. | ∅ and {∅} have sizes 0 and 1. |
| Absorption of a subset | A⊆B iff A∩B=A iff A∪B=B iff A∖B=∅. | Do not infer A=B from one of these equalities. |
| Disjointness | A∩B=∅. | The sets can both be nonempty. |
| Difference | x∈A∖B iff x∈A and x∉B. | A∖B differs from B∖A; no cancellation law holds. |
| Symmetric difference | A△B=(A∖B)∪(B∖A)=(A∪B)∖(A∩B). | Shared members are excluded, and A△B=∅ iff A=B. |
| De Morgan | (A∪B)<sup>c</sup>=A<sup>c</sup>∩B<sup>c</sup> and (A∩B)<sup>c</sup>=A<sup>c</sup>∪B<sup>c</sup>. | The complement must use the same U on both sides. |
| Difference distribution | A∖(B∪C)=(A∖B)∩(A∖C); A∖(B∩C)=(A∖B)∪(A∖C). | Complement the entire parenthesized operation. |
| Monotonicity | A⊆B implies A∪C⊆B∪C and A∩C⊆B∩C. | Complement and the right argument of difference reverse inclusion. |
| Indexed union | x∈⋃<sub>i∈I</sub>A<sub>i</sub> iff ∃i∈I with x∈A<sub>i</sub>. | For I=∅, the union is ∅. |
| Indexed intersection | x∈⋂<sub>i∈I</sub>A<sub>i</sub> iff ∀i∈I, x∈A<sub>i</sub>. | For I=∅, the intersection is U only with a fixed U. |
| Product membership | (a,b)∈A×B iff a∈A and b∈B. | Ordered coordinates cannot generally be swapped. |
| Product factor inference | From A×B⊆C×D infer A⊆C and B⊆D only when A and B are both nonempty. | The empty product hides information about its factors. |
| Power-set membership | S∈P(A) iff S⊆A. | S⊆P(A) asks a different question about each member of S. |
| Power-set intersection | P(A∩B)=P(A)∩P(B). | P(A∪B)=P(A)∪P(B) iff A⊆B or B⊆A. |
| Finite power-set size | &#124;P(A)&#124;=2<sup>&#124;A&#124;</sup> for finite A. | P(∅) has one member; a duplicate roster entry does not change &#124;A&#124;. |
| Finite product and union sizes | &#124;A×B&#124;=&#124;A&#124;&#124;B&#124;; &#124;A∪B&#124;=&#124;A&#124;+&#124;B&#124;−&#124;A∩B&#124;. | Do not add overlapping sizes without subtracting the overlap. |

### 6.3 High-difficulty pattern notes

- **An identity involving ∪, ∩, and ∖ is a propositional identity in disguise.** Introduce p=(x∈A), q=(x∈B), r=(x∈C). Prove the resulting Boolean equivalence for all eight bit patterns. For a false identity, the first differing bit pattern gives a one-element-universe counterexample.
- **An expression with a product has two separate coordinates.** Name a candidate ordered pair (a,b) and expand both coordinate tests. A proof that writes “x∈A∩B” when x is an ordered pair is a type error; correct it before using the result.
- **A universal claim about an empty index set is vacuous.** The union and intersection do not therefore have the same value: existential and universal quantifiers differ. Declare U for the empty intersection.
- **A statement about every set in a family may allow a different witness in each set.** It cannot be changed to one witness common to the family unless a separate intersection argument establishes it.
- **Power-set formulas have an extra logical level.** If S belongs to a power set, expand it to a subset condition. If a power set is contained in another, test the special member A∈P(A) to recover A⊆B.
- **To disprove a set identity, a one-element universe is often enough.** Choose the membership bits to distinguish sides, compute both sides, and explicitly state the unequal sets. A large roster can obscure the decisive pattern.
- **Nonempty assumptions matter for reverse product implications.** A×B=∅ iff A=∅ or B=∅. Do not infer either factor separately from an empty product.
- **The two-set four-region decomposition prevents double counting.** Count A∖B, A∩B, B∖A, and outside separately. For three sets, construct seven internal region counts and check all are nonnegative before trusting given totals.
- **No single finite checklist ensures every future question can be answered.** The useful standard is to derive each claim from definitions, check the boundary cases, and correct a discovered gap when practice exposes it.

### 6.4 Exact equivalences worth recognizing immediately

Each equivalence below gives both a fast way to solve a hard-looking condition and a way to check that no hidden assumption was introduced. The displayed statements hold for arbitrary sets unless finiteness or a universe is explicitly required.

**1. A difference inclusion is a union inclusion.** The equivalence

<div class="formula-block">A∖B ⊆ C &nbsp;⇔&nbsp; A ⊆ B∪C</div>

follows by considering any x∈A. Either x∈B, which places x in B∪C immediately, or x∉B, in which case x∈A∖B and the left condition forces x∈C. Conversely, if x∈A∖B and A⊆B∪C, the alternative x∈B is impossible, so x∈C. **Use:** when a problem says “everything in A outside B belongs to C,” write A⊆B∪C. **Trap:** replacing B∪C with B∩C would demand both properties and is too strong. For A={1}, B={1}, C=∅, the original inclusion is true while A⊆B∩C is false.

**2. An intersection inclusion is an implication.** Under a fixed U,

<div class="formula-block">A∩B ⊆ C &nbsp;⇔&nbsp; A ⊆ B<sup>c</sup>∪C.</div>

If x∈A and x∈B, the left condition gives x∈C; if x∈A but x∉B, then x∈B<sup>c</sup>. These are all possibilities. In Boolean form it is (p∧q)→r, equivalent to p→(¬q∨r). **Trap:** complement belongs to B, not A; and B<sup>c</sup> must be relative to U.

**3. A nested difference has a surprising plus term.** For all sets,

<div class="formula-block">A∖(B∖C) = (A∖B)∪(A∩C).</div>

Indeed, x is on the left iff x∈A and not(x∈B and x∉C), iff x∈A and (x∉B or x∈C). Distribution gives the right side. **Trap:** A∖(B∖C) is generally not (A∖B)∖C. Take A=B=C={1}: the former is {1}, while the latter is ∅. The rule “subtract B, then subtract C” silently changes the parentheses.

**4. Equal outside a region means symmetric difference is inside it.** For any C,

<div class="formula-block">A△B ⊆ C &nbsp;⇔&nbsp; A∖C = B∖C.</div>

Proof: outside C, membership in A△B must be false precisely when A and B have the same membership bit. That is the elementwise equality of A∖C and B∖C. **Use:** if two sets may disagree only inside a designated error region C, encode the statement as A△B⊆C. **Trap:** equality inside C is not required; A={1}, B=∅, C={1} satisfies the condition despite A≠B.

**5. Symmetric difference cancels; union does not.** If A△B=A△C, apply △A to both sides. Associativity and A△A=∅ give B=C. By contrast, A∪B=A∪C allows B and C to disagree on elements already in A. For A={1}, B=∅, C={1}, both unions equal {1} while B≠C. **Use:** identify the operator before attempting cancellation. Difference also lacks unrestricted cancellation, as Problem 18 showed.

**6. Product equality reveals factors only when the product exists.** If A×B=C×D≠∅, then A=C and B=D. Since B is nonempty, choose b∈B; each a∈A gives (a,b)∈C×D and thus a∈C. The common product is nonempty, so D is nonempty too; reverse the argument for C⊆A, and then use witnesses for B=D. If the common product is empty, the conclusion can fail: {1}×∅=∅×{2}=∅. **Trap:** a proof that projects an empty product has no pair to project.

### 6.5 High-value transformation and counterexample patterns

**7. Difference of products splits into two coordinate failures.** Expand the ordered-pair test to obtain

<div class="formula-block">(A×B)∖(C×D) = ((A∖C)×B) ∪ (A×(B∖D)).</div>

The left side requires a∈A, b∈B, and not(a∈C and b∈D). Therefore either a∉C or b∉D; the two terms record those failures. **Trap:** the terms can overlap if both failures occur, so their cardinalities cannot simply be added. For A=B={1}, C=D=∅, both terms contain (1,1) but the union contains it once.

**8. A product distributes over a difference only in the varied factor.** The valid law A×(B∖C)=(A×B)∖(A×C) follows because a pair is retained exactly when a∈A, b∈B, and b∉C. It remains valid when A=∅: both sides are ∅. **Trap:** the formula (A×B)∖(C×D)=(A∖C)×(B∖D) is false; a pair survives when **at least one** coordinate test fails, not only when both fail. For A=B={1}, C={1}, D=∅, the left side is {(1,1)} while the proposed right side is ∅.

**9. A union of power sets misses mixed subsets.** P(A)∪P(B)⊆P(A∪B) always. Equality holds exactly when A⊆B or B⊆A, proved in Problem 19. To reject equality quickly when sets are incomparable, choose a∈A∖B and b∈B∖A; {a,b} lies in the larger power set and neither smaller one. **Trap:** choosing only singleton subsets will miss the failure, because {a} and {b} each belong to one smaller power set.

**10. Power set does not turn difference into difference of power sets.** Compare P(A∖B) with P(A)∖P(B). The empty set is always in P(A∖B), but ∅ is also in P(B) and therefore never in P(A)∖P(B). Hence these sets are **never equal**, for any A and B. This one witness is stronger than a single numerical counterexample. Also, P(A)∖P(B) consists of subsets of A that contain at least one element outside B; it need not contain only elements outside B.

**11. A one-element universe is a complete search for pure three-set identities.** If an expression is built only from A, B, C using ∪, ∩, ∖, △, and complement relative to U, membership of any fixed x depends only on three bits p,q,r. Eight rows exhaust all possibilities. An inequality in a row gives a counterexample by taking U={x} and placing x in exactly the sets marked 1. **Trap:** this method does not automatically settle statements about cardinality, order, or quantified families; those require their own semantics. Problem 20 shows why a candidate row must actually be evaluated on both sides before being called a counterexample.

**12. Equal size plus containment is powerful only for finite sets.** If A⊆B and both are finite with |A|=|B|, then B∖A must be empty and A=B. Without the containment, A={1} and B={2} have equal size but differ. For infinite sets, ℕ⊊ℤ yet both can be enumerated: ℤ in the order 0,1,−1,2,−2,… assigns one integer to each natural-number index. Thus the finite inference cannot be exported to arbitrary infinite sets. **Use:** check the word “finite” before invoking a size argument.

### 6.6 Fast quantitative checks

**13. Symmetric-difference size measures disagreement.** For finite A and B, the disjoint pieces A∖B and B∖A yield

<div class="formula-block">|A△B| = |A|+|B|−2|A∩B|.</div>

If A=B, the right side is zero. If A∩B=∅, it is |A|+|B|. A purported answer outside the range 0≤|A△B|≤|A|+|B| reveals an arithmetic or overlap error. **Trap:** subtracting only one copy of |A∩B| computes |A∪B|, not |A△B|.

**14. Shared subsets are controlled by the intersection.** For finite A,B, P(A)∩P(B)=P(A∩B), hence |P(A)∩P(B)|=2<sup>|A∩B|</sup>. If A and B are disjoint, this intersection is {∅} and has size **one**, not zero. **Use:** convert a question about common subsets into an ordinary intersection first; count only after identifying the exact set.

**15. Counting three overlapping sets can be audited region by region.** Start at the center t=|A∩B∩C|. Subtract t from each pairwise intersection to obtain the three exactly-two regions. Subtract these and t from each individual set size to obtain the three exactly-one regions. The seven region counts must be nonnegative integers; their sum must equal the inclusion–exclusion total. **Trap:** if any region becomes negative, the input numbers cannot describe actual finite sets, even if direct substitution into the inclusion–exclusion formula produces a number.

**16. A power set of a finite set cannot be confused with the set itself by size.** If |A|=n, then |P(A)|=2<sup>n</sup>. The two sizes are never equal for finite n≥0: at n=0 they are 0 and 1, and for n≥1, 2<sup>n</sup>&gt;n. This is only a finite observation; the stronger theorem that no set is equinumerous with its power set is beyond this chapter's finite-counting proof. **Trap:** P(∅)={∅}, not ∅.

The fastest reliable solution still ends with a definition check. Each compact identity above has a stated domain, a reason it holds, and a failure pattern for a tempting alternative. Memorizing its shape without those conditions is likely to fail precisely on a difficult question.

## 7. Visual set laboratory

The controls below assign one hypothetical element x to each of A, B, and C. The outputs show the membership of x in four compound expressions. Change one bit at a time to see why a proposed identity may fail. This lab checks the eight Boolean membership patterns; it does not by itself prove a claim about arbitrary sets unless the claimed expression depends only on these membership conditions and all patterns have been logically accounted for.

<div class="lab" id="set-lab"><label>A: <select id="in-a"><option value="0">x ∉ A</option><option value="1">x ∈ A</option></select></label> <label>B: <select id="in-b"><option value="0">x ∉ B</option><option value="1">x ∈ B</option></select></label> <label>C: <select id="in-c"><option value="0">x ∉ C</option><option value="1">x ∈ C</option></select></label><div id="set-lab-output" aria-live="polite"></div></div>

## 8. References and review limits

1. MIT, 6.042J *Mathematics for Computer Science*, Eric Lehman, F. Thomson Leighton, and Albert R. Meyer, 2015, §4.1, printed pp. 81–85; [official course textbook PDF](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf). Relevant section read; the PDF's machine-extracted mathematical symbols were not used unverified.
2. Stanford University, CS103 *Mathematical Foundations of Computing*, Amy Liu (Winter 2024 course instructor), *Guide to Proofs on Sets*, 2024 course archive; [official course handout](https://web.stanford.edu/class/archive/cs/cs103/cs103.1244/guide_to_proofs_on_sets) and [course introduction identifying the instructor](https://web.stanford.edu/class/archive/cs/cs103/cs103.1244/lectures/00/Lecture%20Slides.pdf). Entire accessible set-proof handout read for containment, equality, and operation-proof patterns; only the opening portion of the introductory slides was checked for course identity and foundational alignment.
3. Cornell University, CS2800 *A Course in Discrete Structures*, Rafael Pass and Wei-Lung Dustin Tseng, 2015, §1.1, printed pp. 1–5; [official course PDF](https://courses.cs.cornell.edu/cs2800/2015fa/handouts/pass_tseng_discmath.pdf). Relevant set-theory section, including its diagrams and product notation, read.
4. Carnegie Mellon University, 15-151 *Mathematical Foundations for Computer Science*, Klaus Sutner, 2022, [Set Operations slides](https://www.cs.cmu.edu/~sutner/pdf/10-sets.pdf) and [Cartesian Products slides](https://www.cs.cmu.edu/~sutner/pdf/15-sets.pdf). Relevant slides read for extensionality, indexed operations, symmetric difference, empty families, and product caveats. A slide typo in an ordered-pair proof was corrected in this synthesis.
5. University of California, Berkeley, CS70 *Discrete Mathematics and Probability Theory*, Summer 2024, Note 0 *Mathematical Foundations*; [official PDF](https://su24.eecs70.org/assets/pdf/notes/n0.pdf). Relevant first three to four pages read as an independent foundational check; this concise note was not one of the four principal sources.

The cited course materials support the topic selection and proof patterns; the prose, diagrams, laboratory, and solutions here are independently written. Systematic relations, functions, counting, and induction receive their own chapters. Archived Iranian entrance-exam items were deliberately not examined for this draft. The source search cannot establish global optimality among all courses, and the present review cannot certify performance on every unseen future problem. Those are explicit limits, not unresolved mathematical claims within the taught boundary.

