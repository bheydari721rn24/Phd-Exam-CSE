# Ordinary and Strong Induction

*Discrete Mathematics · Chapter 4 · student-approved English edition · 24 fully worked problems*

## 1. Scope, prerequisites, and source selection

This chapter proves statements indexed by nonnegative or positive integers. The target is to make the *logical engine* of induction explicit: the predicate being proved, its exact domain, the base values, the transition that reaches every remaining value, and the permitted induction hypothesis. We then apply that engine to sums, divisibility, inequalities, finite objects, representation problems, recursive constructions, and proof debugging. Set cardinality, elementary divisibility, algebra, and the quantifiers from the preceding chapters are prerequisites. A full treatment of structural induction, recurrences, and graph algorithms belongs to later chapters.

Five *written* texts were actually consulted: MIT 6.042J Chapter 5, Stanford CS103's induction guide, UC Berkeley CS70 Notes 3–4, Cornell CS2800 §2.3, and ETH Zürich's discrete mathematics §2.6.10. MIT supplies the broad mathematical spine; Stanford sharpens proof obligations; Berkeley develops strong induction and strengthening; Cornell extends the indexed claim to arbitrary finite structures; ETH checks the formal axiom and initial-index convention. The detailed comparison is retained in the project's source audit. This is a bounded selection from accessible material, not a claim to have read every course in the world.

Each problem below is independently written or independently worded from a type discussed by the cited courses. Complete source exercise collections are not reproduced. The chapter closes with a concise but precise review sheet; that sheet complements the detailed explanations rather than replacing them.

## 2. What induction proves

### 2.1 The predicate, domain, and two obligations

Let n₀ be an integer and let P(n) be a definite mathematical statement for each integer n≥n₀. Ordinary induction is the rule

<div class="formula-block">P(n₀) ∧ [∀k≥n₀, P(k) → P(k+1)] ⇒ ∀n≥n₀, P(n).</div>

The **base** proves P(n₀) without assuming it. The **step** fixes an arbitrary k≥n₀, temporarily assumes P(k), and derives P(k+1). The assumption P(k) is conditional within the step, not a claim that P(k) has already been established for all k. The rule then supplies that global conclusion. If one writes “assume the theorem is true” without specifying this arbitrary k and the desired k+1 statement, the central obligation remains hidden.

Why does the rule work? If a counterexample existed, the nonempty set C={n≥n₀ : ¬P(n)} would have a least element m. The base excludes m=n₀. For m>n₀, minimality gives P(m−1), and the step at k=m−1 gives P(m), a contradiction. This relies on the well-ordering of the nonnegative integers. Conversely, the ordinary induction rule implies well-ordering: if a nonempty subset A⊆N had no least element, let P(n) mean that none of 0,…,n belongs to A. P(0) follows because 0∈A would be least. If P(k) holds and k+1∈A, then k+1 would be least, so P(k+1) holds. Induction would make A empty, a contradiction. The two principles express the same absence of an infinite downward escape in N.

An induction proof concerns a *family of claims*. Checking the first million cases does not replace the step. For example, n²−n+41 is prime for n=0,…,40 but at n=41 it equals 41². A finite computation can disprove a universal assertion by finding one counterexample, but cannot certify its infinitely many remaining cases.

### 2.2 A dependency diagram

<figure class="logic-diagram"><svg viewBox="0 0 880 235" role="img" aria-label="Induction dependency: a proved base reaches later claims only through a valid step"><defs><marker id="ind-arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#426f8a"/></marker></defs><rect x="16" y="56" width="156" height="54" rx="9" fill="#e4f1f6" stroke="#8aafc0"/><text x="30" y="90" font-size="18">Prove P(n<tspan baseline-shift="sub" font-size="13">0</tspan>)</text><rect x="252" y="56" width="178" height="54" rx="9" fill="#edf5eb" stroke="#9aab8b"/><text x="266" y="90" font-size="18">Derive P(n<tspan baseline-shift="sub" font-size="13">0</tspan>+1)</text><rect x="505" y="56" width="161" height="54" rx="9" fill="#edf5eb" stroke="#9aab8b"/><text x="521" y="90" font-size="18">Derive P(n<tspan baseline-shift="sub" font-size="13">0</tspan>+2)</text><text x="744" y="90" font-size="25">…</text><path d="M174 83 L244 83" stroke="#426f8a" stroke-width="2.4" marker-end="url(#ind-arrow)"/><path d="M432 83 L496 83" stroke="#426f8a" stroke-width="2.4" marker-end="url(#ind-arrow)"/><path d="M667 83 L729 83" stroke="#426f8a" stroke-width="2.4" marker-end="url(#ind-arrow)"/><rect x="167" y="159" width="522" height="52" rx="8" fill="#fcf2e9" stroke="#c6aa8b"/><text x="190" y="191" font-size="17">Each arrow needs one proof valid for arbitrary k≥n<tspan baseline-shift="sub" font-size="12">0</tspan>.</text></svg><figcaption>The drawing depicts logical reachability, not an experiment or a proof of an unverified arrow. A missing base or a transition that skips indices breaks the chain.</figcaption></figure>

The diagram is deliberately linear. In strong induction, the arrow into k+1 may depend on *several* earlier verified nodes; in a step of size d, there are d parallel chains unless a different argument joins them. These distinctions explain the multiple-base rules below.

### 2.3 Writing an honest proof

First state P(n) with all variables quantified and the correct starting index. Next verify the smallest index. For the step, state the induction hypothesis **verbatim**, compute or reason from the k+1 object, identify precisely where P(k) is used, and finish with exactly P(k+1). The equality or inequality at the end should be checked against the predicate rather than guessed from its familiar pattern. Keep dependencies within their domains: a statement for n≥2 cannot be invoked at n=1, and a claim about one fixed set S is not automatically a claim about every set of that size.

## 3. Ordinary induction in algebra and counting

### 3.1 Sums are old terms plus the new term

If S(n)=∑<sub>i=1</sub><sup>n</sup> f(i), then S(k+1)=S(k)+f(k+1). This identity is the bridge between P(k) and P(k+1). For the arithmetic sum, P(n) asserts that the sum of the first n positive integers is n(n+1)/2, starting at n=1. At k+1, substitute the hypothesis only for the old prefix:

<div class="formula-block formula-steps"><div>∑<sub>i=1</sub><sup>k+1</sup> i</div><div>= k(k+1)/2 + (k+1)</div><div>= (k+1)(k+2)/2.</div></div>

At n=1 both sides equal 1, and the last expression is the right side of P(k+1). This proof establishes the formula *given* the transition; it does not explain how the formula was discovered. Pairing terms or a geometric argument may discover it, after which induction verifies it.

For a geometric sum starting at i=0, G(n)=∑<sub>i=0</sub><sup>n</sup> rⁱ, the closed form (rⁿ⁺¹−1)/(r−1) requires r≠1. At r=1, the correct formula is n+1. The base index n=0 matters: the sum then has one constant term, equal to 1. Treat G(n) as the polynomial 1+r+⋯+rⁿ; its constant term is 1 even at r=0, so G(n)=1 there. This is a stated polynomial convention, not a claim that the expression 0⁰ has a universal value in all mathematical contexts. With that convention the closed form also works at r=0. We use r≥2 in the solved geometric example.

### 3.2 Divisibility, inequalities, and closure

To prove an expression F(n) divisible by d, express F(k+1) as F(k)+d·t or otherwise reduce it to a multiple of d using the hypothesis. Never replace a congruence with an equality. To prove an inequality, calculate the *slack* after the induction hypothesis. A true but weak hypothesis may be unusable: if a step introduces a positive quantity, the old upper bound may need to retain a quantified margin. In §7 we derive such a strengthened bound rather than merely saying “use a stronger induction hypothesis.”

Induction also counts recursively enlarged finite objects. Let a finite set S have n elements. To show |𝒫(S)|=2ⁿ, the predicate must say **every** set of size n has this property. For |S|=n+1, select e∈S, let T=S∖{e}, and partition the subsets of S into those excluding e and those including e. Both classes have |𝒫(T)|=2ⁿ members; the second is in bijection with 𝒫(T) by A↦A∪{e}. Hence |𝒫(S)|=2·2ⁿ=2ⁿ⁺¹. This avoids the invalid substitution of a result for one special T into a claim for arbitrary S.

### 3.3 A coefficient identity as an induction engine

The binomial theorem is a more demanding ordinary induction because its step must also reorganize a *family of coefficients*. Define C(n,j) as the number of j-element subsets of an n-element set, with C(n,j)=0 when j<0 or j>n. Partition the j-subsets according to whether they contain a chosen element. Those that exclude it number C(n−1,j); those that include it correspond to (j−1)-subsets of the remaining n−1 elements and number C(n−1,j−1). Hence Pascal's identity C(n,j)=C(n−1,j)+C(n−1,j−1), including the endpoint cases under the zero convention.

Now define P(n): for all commuting numbers x,y, (x+y)ⁿ=∑<sub>j=0</sub><sup>n</sup>C(n,j)xⁿ⁻ʲyʲ. At n=0, both sides are 1. If P(k) holds for *all* x,y, multiply by x+y and collect the coefficient of xᵏ⁺¹⁻ʲyʲ. The x-product contributes C(k,j), and the y-product contributes C(k,j−1); their sum is C(k+1,j) by Pascal's identity. Terms outside j=0,…,k+1 have coefficient zero, so the endpoints are included. Thus P(k+1) follows. The universal quantification over x,y allows the same fixed pair to be carried through every step. For noncommuting objects, reordering terms is not justified and this familiar coefficient formula can fail.

## 4. Initial values, multiple bases, and step sizes

### 4.1 Shifting the starting index

If a theorem is for n≥12, proving P(0) is irrelevant and may be false. Use n₀=12. The step must be valid for every k≥12. A formula may include terms such as 1/(n−1), so moving the base from n=2 to n=1 can make the predicate undefined. Define the domain before algebraic manipulation. If a claim holds only for n≥N, proving a few smaller cases is optional and cannot repair a gap at N.

### 4.2 The step can skip values

Suppose one establishes P(k)→P(k+2). From P(0) this reaches only even indices; P(1) starts the odd chain. More generally, a step by d>0 from a single base b reaches only indices congruent to b modulo d. To prove every n≥n₀, establish a valid starting value in each needed residue class (often P(n₀),…,P(n₀+d−1)), or provide another transition linking classes. This is a reachability condition, not a cosmetic proof format. A step by −1 needs a different well-founded argument and is not covered by the forward induction rule.

For a recurrence that uses two preceding values, proving P(k+1) from P(k) and P(k−1) requires **two** starting values. Formally, for every k≥n₀+1 establish [P(k−1)∧P(k)]→P(k+1), and prove P(n₀) and P(n₀+1). With only P(n₀), the first use of P(k−1) is undefined or unproved. Strong induction packages the earlier claims but does not remove the need to supply the first usable cases.

### 4.3 Postage as a reachability picture

To represent every amount n≥12 with 4-unit and 5-unit pieces, the transition n↦n+4 preserves the nonnegative coefficients. Four consecutive base amounts 12,13,14,15 cover all residue classes modulo 4. For any later n≥16, n−4≥12 and an already established representation of n−4 gains one 4-unit piece. The following table displays the four starting chains, not all possible representations.

| Residue class | First amount | Initial representation | Next amount by +4 |
| --- | ---: | --- | ---: |
| 0 mod 4 | 12 | 4+4+4 | 16 |
| 1 mod 4 | 13 | 4+4+5 | 17 |
| 2 mod 4 | 14 | 4+5+5 | 18 |
| 3 mod 4 | 15 | 5+5+5 | 19 |

The bound 12 is sharp: 11 cannot be written 4a+5b with a,b≥0. If b=0, 11 is not a multiple of 4; if b=1, the remainder 6 is not; if b=2, the remainder 1 is not; b≥3 exceeds 11. A proof of “all n≥12” should not silently claim any lower threshold.

## 5. Strong induction

### 5.1 The rule and its exact hypothesis

Strong induction proves P(n₀) and, for every k≥n₀, derives P(k+1) from **all** P(j) for n₀≤j≤k. In symbols,

<div class="formula-block">P(n₀) ∧ [∀k≥n₀, (∀j∈[n₀,k] P(j)) → P(k+1)] ⇒ ∀n≥n₀ P(n).</div>

This is logically no more powerful than ordinary induction; it is more convenient when an n-object reduces to an earlier j that need not equal n−1. For example, if n≥2 is composite, n=ab with 2≤a,b<n. The hypothesis for n−1 alone does not directly tell us about a and b, whereas the strong hypothesis does. The base n=2 is prime and already a product of one prime. In the step, if n is prime, use the one-factor product. If composite, apply the strong hypothesis to a and b and concatenate their finite prime products. This proves **existence** of a prime factorization, not its uniqueness; uniqueness requires additional number theory.

The phrase “assume every smaller positive integer has the property” is dangerous when the theorem starts at 2. It should mean every *eligible* j, 2≤j<n. The proof must check that every reduced index lies in that range. A strong-induction step for n=2 may need a separate prime case because no factor a with 2≤a<n exists.

### 5.2 When the same proof can be ordinary induction

Sometimes a strong proof uses only one earlier value n−d. It may be rewritten as d simultaneous ordinary chains with the d appropriate bases. Conversely, define Q(k)=P(n₀)∧P(n₀+1)∧⋯∧P(k). If the strong step supplies P(k+1) from this entire conjunction, then Q(k)→Q(k+1). Ordinary induction proves Q(k) for every k≥n₀, and hence P(k). This derivation explains equivalence instead of merely asserting it. It also shows that “strong” is about the amount of information available in the hypothesis, not about a stronger theorem.

### 5.3 The decreasing measure behind a recursive proof

The induction parameter need not be an input's numeric value. To justify a recursive algorithm, identify a **measure** μ(input)∈N such that every recursive call has strictly smaller measure. Strong induction on μ can then prove termination and an invariant or output property. The predicate must quantify over all inputs of measure n, because a recursive call may reach a *different* input with that measure. The base covers inputs on which no recursive call is made. In the step, each child call has a smaller eligible measure, so the hypothesis applies; combine the child results with the algorithm's local work. A measure that merely never increases is insufficient: equal-measure calls could cycle forever. If the algorithm changes two counters, a lexicographic pair can be used only after proving that its order is well-founded or mapping it to a suitable nonnegative integer for the reachable states.

The Hanoi example in Problem 21 illustrates a subtle version of this point. An induction hypothesis saying “the procedure works from peg A to peg C” is too narrow to justify its recursive call from A to B. The predicate must cover every distinct source-target pair and the third auxiliary peg. Its size parameter counts disks; its object quantification covers peg assignments. Correctness, move count, and optimality are distinct propositions. The first two follow from the constructive recurrence; the lower bound for optimality needs an additional argument.

## 6. Well-ordering and minimal counterexamples

The well-ordering principle says every nonempty subset of N has a least member. For a claim ∀n≥n₀ P(n), assume it is false and choose the least counterexample m≥n₀. If a base P(n₀) has been proved, m>n₀. If every smaller eligible index has P, a strong step yields P(m), contradiction. This is strong induction written as a minimal-counterexample proof. A valid argument must prove (i) the counterexample set is nonempty under the assumption, (ii) it is bounded below in N, (iii) the selected smaller index is still eligible, and (iv) the alleged smaller object really satisfies the property. Choosing a “minimal” real number from an arbitrary nonempty subset of R would be invalid: e.g. (0,1) has no least element.

For ordinary induction, the needed smaller index is exactly m−1. For a recursive split, one may use any j<m covered by strong induction. The method is especially useful when the easiest reasoning starts from a hypothetical failure: a bad smallest tree, counterexample integer, or finite string that can be shortened. The measure must strictly decrease and remain a nonnegative integer; otherwise a reduction might cycle or descend without reaching a base.

## 7. Strengthening the induction statement

### 7.1 Why the desired statement may be too weak

Suppose T(n)=∑<sub>i=1</sub><sup>n</sup>1/i². The true bound T(n)<2 for all positive n is a weak induction hypothesis: T(k)<2 implies only T(k+1)<2+1/(k+1)², which does not close the target. Instead prove the stronger *quantified slack* T(n)≤2−1/n. The base n=1 gives 1≤1. If T(k)≤2−1/k, then

<div class="formula-block">T(k+1) ≤ 2−1/k+1/(k+1)² ≤ 2−1/(k+1),</div>

because 1/k−1/(k+1)=1/[k(k+1)]≥1/(k+1)² for k≥1. Thus T(n)≤2−1/n<2. The proof makes the extra margin explicit. A stronger predicate may be harder at the base; it must be both true and inductively closed.

### 7.2 Universal strengthening over the object

The size n may index a *class* of objects rather than a single object. If every 2ⁿ×2ⁿ board with **any one** square missing can be tiled by L-shaped triominoes, the hypothesis for n must quantify over the position of the missing square. At size n+1, divide the board into four equal quadrants. One contains the original missing square. Place one central L triomino so it occupies one center-adjacent square in each of the other three quadrants. Each quadrant is now a 2ⁿ×2ⁿ board with one missing square, so the hypothesis applies to all four. The base n=0 is a one-square board with that square missing and zero tiles; if an application defines a tileable board only for n≥1, take the n=1 board as base and tile its three present squares with one L. Choosing the base convention must be explicit.

<figure class="logic-diagram"><svg viewBox="0 0 510 280" role="img" aria-label="A deficient square splits into four smaller deficient squares after one central L tile"><rect x="40" y="15" width="208" height="208" fill="#f2f7fa" stroke="#537d94" stroke-width="2"/><path d="M144 15V223 M40 119H248" stroke="#537d94" stroke-width="2"/><rect x="47" y="30" width="19" height="19" fill="#ae6262"/><rect x="132" y="119" width="12" height="12" fill="#79a999"/><rect x="144" y="107" width="12" height="12" fill="#79a999"/><rect x="144" y="119" width="12" height="12" fill="#79a999"/><text x="285" y="70" font-size="17">Red: original missing cell.</text><text x="285" y="112" font-size="17">Green: one central L tile.</text><text x="285" y="154" font-size="17">Each quadrant has one gap.</text><text x="40" y="256" font-size="15">Diagram is schematic; quadrant width is 2<tspan baseline-shift="super" font-size="11">n</tspan> cells, not the pixels shown.</text></svg><figcaption>The three central covered cells become the “missing” positions for the three other subproblems. The diagram explains the construction; the quantified induction hypothesis justifies each recursive tiling.</figcaption></figure>

The number of remaining squares is 4ⁿ−1, divisible by three because 4≡1 mod 3, so the tile count (4ⁿ−1)/3 is an independent necessary check. Divisibility alone is not sufficient to prove tiling; the constructive quadrant argument does that. The induction step also needs the central L to fit without crossing the actual missing square, which it does because that square lies in one quadrant and the L uses only the other three center-adjacent cells.

### 7.3 Strengthening as a design procedure

When a step fails, locate the exact missing information. Is it a margin in an inequality, a different earlier index, an arbitrary position in a structure, an auxiliary invariant, or several connected statements? State the missing fact as a candidate stronger predicate R(n). Check R(n₀) honestly; derive R(k+1) from precisely R(k) or the earlier R(j). Finally show R(n) implies the originally requested P(n). An unproved stronger assertion is not a repair.

### 7.4 Simultaneous and descending induction

Some claims naturally come in pairs P(n), Q(n). If the transition proves P(k+1) only from Q(k) and proves Q(k+1) only from P(k), neither claim can safely be established first in isolation. Set R(n)=P(n)∧Q(n), prove **both** P(n₀) and Q(n₀), and use the two transition arguments to obtain both parts of R(k+1). For example, if a recursively defined process alternates two invariants between successive stages, this joint predicate records the exact dependency. One may also use strong induction on the conjunction when several earlier stages are needed. Merely writing “by mutual induction” without checking both bases and both successor obligations leaves a cycle.

Finite descending induction is the reverse-looking analogue. To prove P(n) for every integer L≤n≤U, one may establish P(U) and prove P(k+1)→P(k) for every L≤k<U. Starting from U, the rule reaches U−1, U−2, and eventually L. The lower bound is essential: a reverse step on all integers with no top base cannot begin. This is ordinary induction after the change of variable m=U−n, whose range is 0≤m≤U−L. For an infinite interval n≥L, a single high base cannot cover arbitrarily large n by descending steps.

## 8. Frequent invalid inductions

**No usable base.** P(k)→P(k+1) can hold for every k even if P(k) is false everywhere. An implication with a false antecedent proves nothing about its consequent. The base anchors the chain.

**Gap in a step by two.** P(0) and P(k)→P(k+2) reach even n only. Adding P(1) closes the odd chain if the step also holds for every eligible odd k.

**A vanished overlap.** The familiar false argument that “all horses have the same color” considers an (n+1)-horse group and compares its first n and last n horses. Each n-subgroup might be monochromatic, but identifying their colors requires an overlapping horse. At the first transition n=1→2 the two subgroups are disjoint. The step was not valid for the first eligible k, so the conclusion fails. Drawing the smallest case exposes the defect.

**Backwards algebra.** Starting from the target at k+1 and simplifying to P(k) is not a forward proof unless each transformation is reversible. Dividing by a quantity that may be zero or squaring an inequality with an unknown sign is especially hazardous. Prefer starting from the k+1 expression and substituting the proven k expression.

**Changing the quantified object.** An induction hypothesis about one set of size k does not imply a property of all size-(k+1) sets after removing an arbitrary element. State P(k) universally over all relevant sets or prove a controlled reduction to the same fixed object.

**Silent range failure.** In a strong step, n−4 must be at least n₀ before invoking P(n−4). For 4/5 postage, the first n reached by that subtraction is 16; n=12,13,14,15 therefore require direct bases. A proof that starts the step at n=13 invokes a nonexistent P(9).

**Circular “strengthening.”** One may not assume an auxiliary statement merely because it makes the step easy. Put it inside the formally stated predicate and prove its base and transition too. Likewise, a recursive algorithm's correctness and termination are separate claims unless the induction measure covers both.

## 9. Fully worked instructional problems

### Problem 1 — The arithmetic series [Cornell/Berkeley type]

**Claim.** For every n≥1, ∑<sub>i=1</sub><sup>n</sup> i=n(n+1)/2.

**Solution.** Let P(n) be exactly this equality. At n=1, both sides are 1. Fix k≥1 and assume ∑<sub>i=1</sub><sup>k</sup> i=k(k+1)/2. Separating the last term gives ∑<sub>i=1</sub><sup>k+1</sup> i=k(k+1)/2+(k+1)=(k+1)(k+2)/2. Since (k+1)[(k+1)+1]/2 is the required right side, the step is complete. The hypothesis was used only on the old prefix.

### Problem 2 — Odd numbers form squares [original]

**Claim.** For n≥0, ∑<sub>i=0</sub><sup>n−1</sup>(2i+1)=n², where the empty sum for n=0 is 0.

**Solution.** The base 0=0² holds by the empty-sum convention. Assume the first k odd numbers total k². The next term is 2k+1, so the first k+1 total k²+2k+1=(k+1)². This proof states the empty-sum convention because without it P(0) is ambiguous. It also displays the geometric fact that a k×k square gains a row and column of 2k+1 cells to become a (k+1)×(k+1) square.

### Problem 3 — A geometric series with a safe domain [MIT/ETH type]

**Claim.** For integer r≥2 and n≥0, ∑<sub>i=0</sub><sup>n</sup>rⁱ=(rⁿ⁺¹−1)/(r−1).

**Solution.** At n=0, both sides are 1. Assume the formula at k. The sum through k+1 equals (rᵏ⁺¹−1)/(r−1)+rᵏ⁺¹=[rᵏ⁺¹−1+(r−1)rᵏ⁺¹]/(r−1)=(rᵏ⁺²−1)/(r−1). All divisions are valid because r−1≥1. The case r=1 has a different closed form n+1 and should not be smuggled into this proof.

### Problem 4 — A telescoping rational sum [Stanford type]

**Claim.** For n≥1, ∑<sub>i=1</sub><sup>n</sup>1/[i(i+1)]=n/(n+1).

**Solution.** At n=1, 1/2=1/2. Suppose the identity holds at k≥1. Adding the next term gives k/(k+1)+1/[(k+1)(k+2)]=[k(k+2)+1]/[(k+1)(k+2)]=(k+1)²/[(k+1)(k+2)]=(k+1)/(k+2). Every denominator is positive on this domain. Independently, 1/[i(i+1)]=1/i−1/(i+1), so direct telescoping gives the same result and checks the inductive answer.

### Problem 5 — A divisibility claim [Berkeley type]

**Claim.** For every integer n≥0, 3 divides n³−n.

**Solution.** P(0) holds because 0 is a multiple of 3. Assume k³−k=3t for some integer t. Then (k+1)³−(k+1)=(k³−k)+3k(k+1)=3[t+k(k+1)]. The bracket is an integer, proving P(k+1). The identity n³−n=n(n−1)(n+1) also provides a direct check: among three consecutive integers one is divisible by 3. The proof does not divide by 3; it constructs the required integer quotient.

### Problem 6 — A step of size two [Stanford type]

**Claim.** Every n≥0 has the same parity as n².

**Solution.** The claim for n=0 is true and for n=1 is true. Suppose it holds for k≥0. Since (k+2)²−k²=4k+4 is even and (k+2)−k=2 is even, the parities of k² and (k+2)² agree, and the parities of k and k+2 agree. Thus P(k)→P(k+2). Bases 0 and 1 start the even and odd chains. With base 0 alone the argument would say nothing about odd n; the extra base is logically necessary for this step format.

### Problem 7 — Two preceding values [Cornell type]

**Claim.** Let F₀=0, F₁=1, and Fₙ₊₂=Fₙ₊₁+Fₙ. Then Fₙ<2ⁿ for all n≥0.

**Solution.** At n=0, 0<1; at n=1, 1<2. Assume Fₖ<2ᵏ and Fₖ₋₁<2ᵏ⁻¹ for some k≥1. Then Fₖ₊₁=Fₖ+Fₖ₋₁<2ᵏ+2ᵏ⁻¹<2ᵏ+2ᵏ=2ᵏ⁺¹. Both hypotheses were needed, and k≥1 keeps k−1 within the proved range. The second strict inequality uses 2ᵏ⁻¹<2ᵏ. This is a growth bound, not an exact Fibonacci formula.

### Problem 8 — Powersets of arbitrary finite sets [Cornell type]

**Claim.** For every finite set S with |S|=n, |𝒫(S)|=2ⁿ.

**Solution.** Define P(n) with the universal phrase “for every finite S of size n.” At n=0, S=∅ and 𝒫(S)={∅} has size 1=2⁰. Assume P(k). Given any S of size k+1, choose e∈S and T=S∖{e}; then |T|=k. Subsets of S excluding e are exactly the 2ᵏ subsets of T. Subsets including e are exactly {A∪{e}:A⊆T}, another 2ᵏ distinct subsets. The two classes are disjoint and exhaustive, so |𝒫(S)|=2ᵏ+2ᵏ=2ᵏ⁺¹. It is crucial that the hypothesis applies to this arbitrary T.

### Problem 9 — Four and five unit pieces [Berkeley/MIT type]

**Claim.** Every integer n≥12 is 4a+5b for nonnegative integers a,b.

**Solution.** Verify 12=4·3, 13=4·2+5, 14=4+5·2, 15=5·3. For n≥16, n−4≥12. Under strong induction, assume every eligible integer below n is representable; write n−4=4a+5b. Then n=4(a+1)+5b with nonnegative coefficients. The same argument can be viewed as ordinary induction on four separate residue chains. Checking only n=12 would leave the other three chains untouched. Moreover 11 is impossible, as shown in §4, so the starting threshold is exact.

### Problem 10 — Prime-product existence [MIT/Berkeley type]

**Claim.** Each integer n≥2 is a product of one or more primes.

**Solution.** Base n=2: 2 itself is prime. Suppose the claim for every j with 2≤j<n, where n>2. If n is prime, its one-term product suffices. Otherwise n=ab with integers 1<a,b<n. The strict upper bounds follow from a,b>1; for instance a=n/b≤n/2<n. Apply the strong hypothesis separately to a and b, obtaining a product of primes for each. Multiplying the two lists yields a product for n. This establishes existence only; the order and uniqueness of factors are not asserted.

### Problem 11 — Binary strings [original]

**Claim.** There are exactly 2ⁿ binary strings of length n for every n≥0.

**Solution.** For n=0 the only string is the empty string, so the count is 1. Given any length-(k+1) string, its first k positions form a unique length-k string, and its final symbol is either 0 or 1. Assuming there are 2ᵏ prefixes, each gives two distinct extensions and every longer string occurs once. Thus the new count is 2·2ᵏ=2ᵏ⁺¹. The empty-string base is not “zero strings”: it is one string of zero length.

### Problem 12 — Strong induction simulated by ordinary induction [Berkeley type]

**Claim.** Any proof using P(n₀) and [P(n₀)∧⋯∧P(k)]→P(k+1) can be converted to ordinary induction.

**Solution.** Define Q(k)=∧<sub>j=n₀</sub><sup>k</sup>P(j). Base Q(n₀) is P(n₀). Assume Q(k); it includes every premise required by the strong step, so derive P(k+1). Together with Q(k), that is Q(k+1). Ordinary induction proves Q(k) for all k≥n₀; each Q(k) contains P(k). This construction does not claim that P(k) alone suffices for the original step; it changes the induction predicate.

### Problem 13 — A least-counterexample audit [original]

**Claim.** If P(5) holds and every n≥6 satisfies [P(5)∧⋯∧P(n−1)]→P(n), then P(n) holds for all n≥5.

**Solution.** Suppose a counterexample exists, and let m be the least one. Since P(5), m≥6. Each eligible j with 5≤j<m satisfies P(j) by the minimality of m. The given implication at n=m has exactly these premises, so P(m) follows, contradicting the choice of m. The use of a least element is valid because the counterexample set is a nonempty subset of integers bounded below by 5. This is the strong induction rule in contrapositive form.

### Problem 14 — A bound that needs slack [Berkeley type]

**Claim.** For n≥1, ∑<sub>i=1</sub><sup>n</sup>1/i²≤2−1/n, and hence the sum is strictly below 2.

**Solution.** At n=1 both sides equal 1. Assume T(k)≤2−1/k. Then T(k+1)≤2−1/k+1/(k+1)². To compare with 2−1/(k+1), subtract: [2−1/(k+1)]−[2−1/k+1/(k+1)²]=1/[k(k+1)]−1/(k+1)²=1/[k(k+1)²]>0. Thus the strengthened bound closes with room to spare. Since 1/n>0, 2−1/n<2. A bare assumption T(k)<2 supplies no such margin.

### Problem 15 — A power inequality with equality conditions [original]

**Claim.** For all n≥0, 2ⁿ≥n+1, with equality exactly at n=0 and n=1.

**Solution.** Base n=0: 1=1. If 2ᵏ≥k+1, then 2ᵏ⁺¹=2·2ᵏ≥2k+2≥k+2 for k≥0. The second comparison is equality only when k=0; thus the transition from n=0 to n=1 retains equality, and every transition with k≥1 is strict. We have checked both equality cases directly. Merely proving a weak inequality does not by itself identify where equality holds.

### Problem 16 — A representation with a different step size [original]

**Claim.** Every n≥6 is 3a+4b with a,b∈N.

**Solution.** Direct bases are 6=3·2, 7=3+4, and 8=4·2, one for each residue class modulo 3. For n≥9, n−3≥6. Assuming the representation of n−3, say n−3=3a+4b, append one 3 to obtain n=3(a+1)+4b. This proves the claim for all subsequent n. The threshold cannot be lowered to 5: neither b=0 nor b=1 yields a nonnegative integer a when 5=3a+4b, and b≥2 exceeds 5.

### Problem 17 — A graph-path induction with correct quantification [Cornell type]

**Claim.** In a directed graph where x→y and y→z always imply x→z, every positive-length directed path from u to v yields a direct edge u→v.

**Solution.** P(n) says that **every** path of length n in this graph has its endpoints joined by an edge. For n=1 this is the definition of a path's single edge. Assume P(k). Take an arbitrary path of length k+1, with first edge u→w and remaining path of length k from w to v. By P(k), w→v. The assumed transitivity gives u→v. The statement is about positive lengths: a length-zero path u to u would require a self-loop, which transitivity alone does not supply. In the induction step, w and v need not be distinct; the given implication still applies.

### Problem 18 — A deficient board [MIT type]

**Claim.** For every n≥0 and every chosen missing cell in a 2ⁿ×2ⁿ board, the remaining cells can be tiled by L triominoes.

**Solution.** For n=0 the board has one cell, which is missing; the empty tiling is valid. Assume the assertion for every missing position in a 2ᵏ×2ᵏ board. For a 2ᵏ⁺¹×2ᵏ⁺¹ board, split into four 2ᵏ×2ᵏ quadrants. Exactly one quadrant contains the prescribed missing cell. Cover the three center-adjacent cells in the other quadrants with one L. Each quadrant now has exactly one absent or already covered cell, so apply the hypothesis to each quadrant separately. Their tilings plus the central L are disjoint and cover every remaining cell. A hypothesis for only corner-missing boards would be too weak because the original missing cell can be an interior cell of its quadrant. The three induced gaps are center-adjacent corners of their respective quadrants; they are not the source of that failure. The universal missing-position hypothesis handles both kinds of subproblem.

### Problem 19 — Locate the horse-proof failure [MIT/Stanford type]

**Claim under audit.** “All horses in any nonempty finite group have the same color.” A proposed step takes the first n and last n horses of an (n+1)-horse group, says each subgroup has one color, and infers those colors agree because the groups overlap.

**Solution.** At n=1, an (n+1)-group has two horses. The first one-horse subgroup and the last one-horse subgroup have empty intersection. Consequently their colors cannot be equated through an overlapping horse. The step n=1→2 is invalid, even though the base n=1 is true and the overlap argument works for n≥2. Since the only established base cannot reach the region where the step works, no induction chain starts. Two differently colored horses are a concrete counterexample to the conclusion.

### Problem 20 — Diagnose a false base-and-step argument [original]

**Proposed argument.** P(n) means n≥10 for n≥0. “If P(k), then k+1≥10, so P(k+1); therefore P(n) for every n≥0.”

**Solution.** The conditional step is valid for every k≥0: if k≥10, then k+1≥10. But P(0) says 0≥10 and is false. There is no true base at 0, so induction yields no assertion for all n≥0. If the theorem is restricted to n≥10, then P(10) is true and the same step proves that *restricted* theorem. This illustrates why a correct implication can coexist with a false universal conclusion.

### Problem 21 — Induction for a recursive algorithm [Cornell type]

**Claim.** The standard three-peg Hanoi procedure transfers n disks legally in exactly 2ⁿ−1 moves, for n≥0.

**Solution.** Define H(0)=0: transferring no disks requires no moves and is legal. Assume the recursive procedure works for k disks, between any selected source and target pegs with the remaining peg auxiliary. For k+1 disks, move the top k from source to auxiliary using H(k) moves; the largest disk remains alone at source. Move that disk to target in one legal move. Move the k small disks from auxiliary to target using another H(k) moves; placing small disks atop the largest is legal. Thus H(k+1)=2H(k)+1=2(2ᵏ−1)+1=2ᵏ⁺¹−1. The strengthened phrase “between any selected source and target” is needed for both recursive calls. This proves the procedure's legality and move count; optimality requires a separate lower-bound argument.

### Problem 22 — A binomial identity with endpoint terms [original]

**Claim.** For n≥1, ∑<sub>j=0</sub><sup>n</sup>(−1)ʲ C(n,j)=0, where C(n,j)=0 outside 0≤j≤n.

**Solution.** At n=1 the sum is C(1,0)−C(1,1)=1−1=0. Let A(n) denote the sum and assume A(k)=0 for some k≥1. By Pascal's identity, A(k+1)=∑<sub>j=0</sub><sup>k+1</sup>(−1)ʲ[C(k,j)+C(k,j−1)]. Separate the two sums. The first equals A(k) after extending the j=k+1 term, which is zero under the out-of-range convention. In the second, put t=j−1; the j=0 term is zero and the remaining sum is −∑<sub>t=0</sub><sup>k</sup>(−1)ᵗ C(k,t)=−A(k). Hence A(k+1)=A(k)−A(k)=0. Independently, the binomial theorem gives (1−1)ⁿ=0 for n≥1, checking the result. At n=0 the sum is 1, so the starting index is essential.

### Problem 23 — Two coupled counting claims [original]

**Claim.** Let Eₙ and Oₙ count, respectively, binary strings of length n with an even and an odd number of 1s. For every n≥1, Eₙ=Oₙ=2ⁿ⁻¹.

**Solution.** At n=1, the strings 0 and 1 give E₁=O₁=1=2⁰. Define R(n) as the conjunction of both equalities. Append 0 to a length-k string to preserve the parity of its number of 1s; append 1 to switch parity. Therefore Eₖ₊₁=Eₖ+Oₖ and Oₖ₊₁=Oₖ+Eₖ. Under R(k), each right side is 2ᵏ⁻¹+2ᵏ⁻¹=2ᵏ, so both claims at k+1 follow together. The transition for one count needs information about the other; proving them as a joint predicate avoids an unjustified circular appeal. At n=0 the sole empty string has even parity, so E₀=1 and O₀=0; the common formula would be false there.

### Problem 24 — Finite descending induction [original]

**Claim.** Fix N≥0. For every integer k with 0≤k≤N, 2ᵏ divides 2ᴺ.

**Solution.** Descend from k=N: 2ᴺ divides itself, with quotient 1. Suppose for some 0≤k<N that 2ᵏ⁺¹ divides 2ᴺ, so 2ᴺ=2ᵏ⁺¹q for an integer q. Then 2ᴺ=2ᵏ(2q), proving divisibility at k. Repeating this valid step reaches all k down to 0. Equivalently, use ordinary induction on m=N−k from m=0 to m=N. The restriction k≤N matters: for k=N+1, 2ᵏ cannot divide 2ᴺ because a positive quotient would have to be 1/2.

## 10. High-yield review: complete rules and traps

The numbered rules below are a fast audit after studying §§2–9. They are intentionally shorter than the teaching body but remain complete statements.

**1. Define the exact predicate.** Write P(n) as the whole assertion to be proved, including quantification over every object of size n; a symbolic formula without its domain is not a complete induction target.

**2. Match the first index.** If the target begins at n₀, prove P(n₀) and perform the step for every k≥n₀. A base outside the claimed domain does not anchor it.

**3. Distinguish hypothesis from theorem.** During the step, P(k) is a temporary conditional assumption for arbitrary k; it becomes globally true only after applying the induction principle to a valid base and step.

**4. State the requested successor.** Before calculation, write what P(k+1) says. The last algebraic line must equal or imply this specific target, not merely resemble the k case.

**5. Separate a sum at its last term.** For S(n)=∑<sub>i=a</sub><sup>n</sup>f(i), use S(k+1)=S(k)+f(k+1) and apply the hypothesis only to S(k). Check a and the empty-sum convention.

**6. For divisibility, construct the quotient.** Transform F(k+1) into F(k)+d·t; if F(k)=d·u, conclude F(k+1)=d(u+t) and verify the bracket is an integer.

**7. Preserve inequality direction.** Every added term, multiplied factor, and denominator needs its sign checked. Multiplication by a negative reverses an inequality; division by zero is forbidden.

**8. Track slack.** If P(k) gives an upper bound that becomes too weak after adding a positive term, seek a stronger bound with an explicit k-dependent margin and prove it from its base.

**9. Count objects by an exhaustive disjoint partition.** When adding one element to a set or one symbol to a string, show each new object is counted once and every new object is counted.

**10. Quantify over arbitrary structures.** To use induction on cardinality, P(n) must generally cover *all* relevant size-n structures; a proof about one fixed S cannot be applied to a newly chosen subset T without justification.

**11. Step size d creates residue chains.** A rule P(k)→P(k+d) preserves k mod d. Prove a base in every residue class needed by the theorem, or supply additional transitions linking them.

**12. Multiple predecessors require multiple bases.** If a step uses P(k) and P(k−1), prove enough consecutive starting claims for the first legal k. Strong induction does not supply unproved starting cases.

**13. Strong induction may use any earlier eligible index.** State the hypothesis as P(j) for all n₀≤j≤k and check that each reduced index actually lies in this interval.

**14. Strong induction does not prove stronger theorems.** It can be converted to ordinary induction on Q(k)=∧<sub>j=n₀</sub><sup>k</sup>P(j); it changes the convenient hypothesis, not the set of valid conclusions.

**15. A prime-product proof has two cases.** For n≥2, n is prime or composite; in the composite case both nontrivial factors are smaller eligible integers. Existence does not imply unique factorization.

**16. Minimal counterexamples need a well-founded set.** Choose a least bad nonnegative integer only after showing such a set would be nonempty; every reduction must remain eligible and strictly lower the chosen measure.

**17. A strengthened claim must itself be proved.** Add the missing margin, object-location quantifier, auxiliary invariant, or simultaneous assertions to P(n), then check its new base and complete step.

**18. A constructive tiling proof is more than a divisibility test.** Area divisibility is necessary; the quadrant construction proves sufficient coverage and must keep the missing cell arbitrary.

**19. Test the earliest transition.** A statement such as “two n-subsets overlap” may be true for n≥2 but false at n=1. If the first needed step fails, later valid steps cannot connect the base to the theorem.

**20. A backward derivation needs reversible steps.** If starting from P(k+1) leads to P(k), reverse every operation only after proving it is an equivalence; a direct forward derivation is usually safer.

**21. A valid step without a true base proves nothing.** The conditional P(k)→P(k+1) may be vacuously true throughout a false region; check the first actual proposition independently.

**22. A base without a valid step proves one case only.** Testing many initial values is valuable for finding errors but cannot establish an infinite claim unless a valid transition covers every later case.

**23. Check threshold sharpness separately.** Proving all n≥N does not automatically say N is the smallest possible start; a lower counterexample or a separate proof settles that claim.

**24. Separate algorithmic claims.** An inductive construction may show that an algorithm is legal and has a stated cost; optimality, termination for other inputs, or uniqueness needs its own justified argument.

**25. Finish with an exact conclusion.** After base and step, explicitly invoke induction to obtain ∀n≥n₀ P(n), then derive any weaker corollary (such as T(n)<2) from that established result.

**26. For binomial identities, justify coefficient grouping.** Derive Pascal's rule by a disjoint partition or an algebraic identity, include out-of-range coefficients as zero, and require commuting variables before combining like terms.

**27. For recursive algorithms, choose a decreasing measure.** Every recursive call must strictly decrease a nonnegative integer measure, and the induction predicate must cover every input and configuration with that measure.

**28. For coupled or descending claims, repair the induction structure.** Prove every component of a joint base and step; for a finite reverse proof, start at the upper endpoint and verify each downward transition through the lower endpoint.

## 11. References and remaining limits

1. Eric Lehman, F. Thomson Leighton, Albert R. Meyer, MIT 6.042J, *Mathematics for Computer Science* (Spring 2015), Chapter 5 §§5.1–5.3, pp. 115–130. [Official PDF](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf).
2. Stanford CS103 course staff, *Guide to Induction* and *Induction Proofwriting Checklist* (2024–25 archive). [Official guide](https://web.stanford.edu/class/archive/cs/cs103/cs103.1252/guide_to_induction); [official checklist](https://web.stanford.edu/class/archive/cs/cs103/cs103.1252/induction_checklist).
3. UC Berkeley CS70, *Discrete Mathematics and Probability Theory*, Summer 2024, Note 3 (Mathematical Induction) and Note 4 (Well-Ordering). [Official Note 3](https://su24.eecs70.org/assets/pdf/notes/n3.pdf); [official Note 4](https://su24.eecs70.org/assets/pdf/notes/n4.pdf).
4. Rafael Pass and Wei-Lung Dustin Tseng, Cornell CS2800, *A Course in Discrete Structures* (Fall 2015), Chapter 2 §2.3, pp. 17–25, and Chapter 4 §4.3, binomial theorem and alternating sum, p. 68. [Official PDF](https://courses.cs.cornell.edu/cs2800/2015fa/handouts/pass_tseng_discmath.pdf).
5. Ueli Maurer, ETH Zürich, *Diskrete Mathematik* (Autumn 2024), §2.6.10, pp. 36–38. [Official PDF](https://crypto.ethz.ch/teaching/DM24/ln/DM24_LN.pdf).

The chapter covers the named induction patterns and the 24 independently solved problems. It does not contain all exercises in the source courses, archived Iranian examination items, or an exhaustive census of global university courses. No text can guarantee a correct answer to every unseen doctoral question; transfer to unfamiliar problems depends on active application, correction of mistakes, and later examination practice. Known in-scope statements here were checked against the source sections and with independent boundary/finite checks, but universal mathematical conclusions rely on the written proofs rather than those finite checks.
