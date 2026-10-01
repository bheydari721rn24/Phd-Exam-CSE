# Counting Probabilities and Independence

*Probability and Statistics · Chapter 2 · Approved English chapter*

## 1. Scope, prerequisites, and reviewed sources

The preceding chapter defined a probability model and event algebra. This chapter answers two further questions: how many elementary outcomes satisfy a constraint, and when the probability of a joint event factors into simpler probabilities. These questions interact, but their assumptions differ. A valid counting argument need not imply independence; a correctly counted family need not be uniformly distributed.

The teaching progresses through sum and product rules, bijections and constant-size fibers, permutations and combinations, repeated objects, labeled group allocation, stars and bars, constrained counts, combinatorial identities, uniform sampling, collisions, occupancy, repeated trials, and event independence. Advanced cases include derangements, bounded allocations, pairwise versus mutual independence, complement patterns, conditioning effects, and a laboratory showing dependence invisible to every pairwise test. Full Bayes calculations and the systematic theory of conditional probability belong to the next chapter. The small conditional-probability bridge here is necessary to explain independence precisely.

Prerequisites are finite sets, event operations, factorial notation once introduced below, elementary algebra, and the axioms chapter. The geometric series used for a repeated race is derived with its convergence condition. No expectation or variance theory is assumed. Every count and probability model states whether labels, order, repetition, and equal likelihood matter.

Four courses were selected after comparing a documented pool of accessible written material: MIT 6.041/6.431 Lectures 3–4 by John N. Tsitsiklis; Stanford CS109 Lecture Notes 1, 2, and 5 by Lisa Yan; UC Berkeley CS70 Summer 2019 Notes 12, 12.5, and the relevant part of Note 14; and Oxford's Probability and Computing notes by Elias Koutsoupias, Lectures 2 and 18. The exact portions read, selection reasons, exclusions, and source corrections are recorded in the source audit and final references. These are four genuinely reviewed course texts, rather than four syllabus links. The survey is bounded and does not establish that every worldwide course was found. All prose, questions, diagrams, and laboratory code here are independently authored.

## 2. Counting principles and the probability contract

### 2.1 Count precisely specified objects

Before selecting a formula, define one counted object. An ordered sequence, a subset, a multiset of values, a placement of labeled items, and a partition into named groups are different objects. The phrase “select three items” does not determine which one is intended. Ask whether interchanging positions changes the result, whether the same item may recur, whether equal-looking objects retain distinct labels, and whether destinations are named.

For a finite uniform sample space, <span class="math-inline">P(A)=|A|/|Ω|</span>. Numerator and denominator must describe compatible objects under the same selection mechanism. Counting favorable subsets but dividing by the number of all ordered sequences mixes two representations. It can be repaired only by a justified conversion factor or by returning to one common representation. Nonuniform laws require weighted sums instead of raw counts.

### 2.2 Disjoint cases and complements

If a finite set is partitioned into disjoint cases, its size is the sum of the case sizes. Cases must be exhaustive and pairwise nonoverlapping. If a constraint says “contains either type,” the cases “contains the first type” and “contains the second type” can overlap. Use inclusion–exclusion, or make the cases disjoint by separating first only, second only, and both.

The complement method counts the whole family and subtracts the forbidden family. For length n binary strings, “at least one zero” has count <span class="math-inline">2ⁿ−1</span>: only the all-one string is excluded. This is a count even without a probability law. Dividing by <span class="math-inline">2ⁿ</span> gives a probability only if every binary string is equally likely.

For finite sets, the two-event and three-event inclusion–exclusion identities from the preceding chapter hold with cardinalities in place of probabilities. Their proof is the same membership-region count: each favorable object must end with coefficient one. In particular, an object satisfying two constraints cannot be counted twice merely because either one makes it acceptable.

### 2.3 Product rule versus variable branching

Suppose an object is built in r successive stages, and every valid prefix has exactly <span class="math-inline">n<sub>i</sub></span> possible continuations at stage i. Also require that complete choice sequences encode counted objects uniquely. Then the number of objects is <span class="math-inline">n<sub>1</sub>⋯n<sub>r</sub></span>. A tree proof follows by counting leaves: every stage multiplies the number of existing prefixes by the same continuation count.

Available choices may depend on earlier values while their *number* stays fixed. Selecting two distinct labels from an n-element set gives n first choices and <span class="math-inline">n−1</span> second choices. The remaining labels depend on the first choice, yet the count is <span class="math-inline">n(n−1)</span>. This argument is valid without assuming random choices or independent events.

If continuation counts differ between prefixes, sum those counts instead. For sequences <span class="math-inline">(i,j)</span> with <span class="math-inline">1≤i≤n</span> and <span class="math-inline">1≤j≤i</span>, there are <span class="math-inline">∑<sub>i=1</sub><sup>n</sup>i=n(n+1)/2</span> objects. Multiplying n by n would include invalid continuations. A recurrence or an explicit sum handles unequal branching; a product of averages is not automatically valid.

### 2.4 Bijections, constant-size fibers, and overcounting

A **bijection** pairs every object in one finite family with exactly one object in another and conversely. Their cardinalities are equal. A useful example pairs subsets of an n-element set with length n indicator strings. Each position records membership, giving <span class="math-inline">2ⁿ</span> subsets.

More generally, a surjective reporting map from a fine family S to a coarse family T partitions S into fibers. The fiber of t consists of all fine objects reporting the same t. If every fiber has exactly c elements, then <span class="math-inline">|S|=c|T|</span>, so division by c is justified. If the sizes vary, there is no such uniform divisor. Under a uniform fine model, a coarse object's probability equals its fiber size divided by <span class="math-inline">|S|</span>, not necessarily <span class="math-inline">1/|T|</span>.

For two draws with replacement from three labels, the ordered family has nine members. The six unordered multisets are <span class="math-inline">{1,1},{2,2},{3,3},{1,2},{1,3},{2,3}</span>. Each equal-label multiset has one ordering and each distinct-label multiset has two. Dividing nine by two does not count the multisets. Nor are the six multisets uniform under ordered uniform draws. This small example diagnoses both a counting error and a probability error.

<figure class="logic-diagram"><svg viewBox="0 0 650 220" role="img" aria-label="Repeated draws have unequal reporting fibers: one ordering for a repeated pair and two orderings for a distinct pair"><rect x="8" y="8" width="634" height="204" rx="12" fill="#f2f7f7" stroke="#b5d1cd"/><text x="38" y="42" font-size="19">Ordered uniform draws → unordered report</text><text x="70" y="93" font-size="22">(1,1)</text><text x="280" y="93" font-size="22">(1,2)</text><text x="440" y="93" font-size="22">(2,1)</text><path d="M95 105 L95 145 M310 105 L368 145 M470 105 L395 145" stroke="#3a807b" stroke-width="2"/><text x="48" y="174" font-size="20">{1,1}: mass 1/9</text><text x="280" y="174" font-size="20">{1,2}: mass 2/9</text></svg><figcaption>Forgetting order changes the mass of a report according to the number of detailed outcomes it combines. It does not generate a new uniform experiment.</figcaption></figure>

## 3. Permutations, combinations, and repeated selections

### 3.1 Factorials and ordered distinct samples

For an integer <span class="math-inline">n≥1</span>, define <span class="math-inline">n!=n(n−1)⋯1</span>, and define <span class="math-inline">0!=1</span>. The latter represents the single empty arrangement, not zero arrangements. Arranging n distinct labeled objects in n positions has n choices first, <span class="math-inline">n−1</span> next, and so on, giving <span class="math-inline">n!</span> permutations.

An ordered length k selection without replacement has the falling-factorial count

<div class="formula-block formula-steps"><div>(n)<sub>k</sub>=n(n−1)⋯(n−k+1)</div><div>=n!/(n−k)!, 0≤k≤n.</div></div>

The empty product at <span class="math-inline">k=0</span> equals one. For <span class="math-inline">k&gt;n</span> the count is zero; factorials of negative integers must not be inserted into the formula. With replacement there are n choices at every position, giving <span class="math-inline">nᵏ</span> sequences for <span class="math-inline">n≥1</span>. Equal probabilities of those sequences require an appropriate sampling law, such as independent uniform draws.

### 3.2 Unordered distinct samples

Each k-element subset has exactly <span class="math-inline">k!</span> orderings because all selected labels are distinct. The constant-fiber rule gives the binomial coefficient, written <span class="math-inline">C(n,k)</span> or with stacked notation:

<div class="formula-block"><math class="math-limits" display="block"><mrow><mo>(</mo><mfrac linethickness="0"><mi>n</mi><mi>k</mi></mfrac><mo>)</mo><mo>=</mo><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mi>k</mi><mo>!</mo><mo>(</mo><mi>n</mi><mo>−</mo><mi>k</mi><mo>)</mo><mo>!</mo></mrow></mfrac><mo>.</mo></mrow></math></div>

Set <span class="math-inline">C(n,k)=0</span> when the integer k is negative or exceeds the nonnegative integer n. Within range, <span class="math-inline">C(n,0)=C(n,n)=1</span>. Complementing a subset gives the symmetry <span class="math-inline">C(n,k)=C(n,n−k)</span>. The value counts subsets; it does not assign them probabilities until a uniform-subset law is specified or induced from constant-size ordered fibers.

### 3.3 Indistinguishable copies and fixed multiplicities

Suppose a length n arrangement contains <span class="math-inline">n<sub>1</sub>,…,n<sub>r</sub></span> copies of r different symbols, with total n. Temporarily label every copy. This gives <span class="math-inline">n!</span> arrangements. For each visible arrangement, labels can be permuted among positions of the same symbol in <span class="math-inline">n<sub>1</sub>!⋯n<sub>r</sub>!</span> ways. This number is constant for the fixed multiplicities, so the visible count is

<div class="formula-block">n!/(n<sub>1</sub>!⋯n<sub>r</sub>!), ∑<sub>i=1</sub><sup>r</sup>n<sub>i</sub>=n.</div>

It is the **multinomial coefficient**. Zero multiplicities cause no difficulty because <span class="math-inline">0!=1</span>. Do not divide by factorials of symbols that are distinguishable in the actual experiment. A sequence of five physically labeled tokens differs from a sequence reporting only their colors.

The same formula allocates n distinct objects to r **named** groups of prescribed sizes. Choose the first group's members, then the second's from the remainder, and continue. The product of binomial coefficients telescopes to the displayed factorial ratio. The formula does not specify within-group positions: if each member also occupies a distinct slot, multiply by the within-group arrangement counts as appropriate.

### 3.4 Unordered selections with repetition

For n available types and a multiset of total size k, let <span class="math-inline">x<sub>i</sub></span> be the number of copies of type i. Counting the multisets is equivalent to counting nonnegative integer solutions of <span class="math-inline">x<sub>1</sub>+⋯+x<sub>n</sub>=k</span>. Section 4 derives the count <span class="math-inline">C(n+k−1,k)</span> for <span class="math-inline">n≥1</span>. It is not <span class="math-inline">nᵏ/k!</span>, because different multisets have different numbers of orderings.

| Counted object | Repetition allowed? | Count |
|---|---|---|
| Ordered length k sequence | Yes | <span class="math-inline">nᵏ</span> |
| Ordered length k sequence | No | <span class="math-inline">(n)<sub>k</sub></span> |
| Unordered k-element subset | No | <span class="math-inline">C(n,k)</span> |
| Unordered multiset of size k | Yes | <span class="math-inline">C(n+k−1,k)</span> |

Here n counts distinct available labels or types, <span class="math-inline">k≥0</span>, and <span class="math-inline">n≥1</span>. The no-repetition rows require <span class="math-inline">k≤n</span> or give zero. Each row counts a different family. There is no fifth rule saying that all four families inherit uniform probabilities from the same physical draw.

## 4. Constraints, allocations, and symmetry

### 4.1 Block and gap constructions

To require a specified collection of t distinct objects to occur consecutively in a linear ordering, treat the collection as one block. There are <span class="math-inline">n−t+1</span> distinct units to arrange and <span class="math-inline">t!</span> internal block orders, giving <span class="math-inline">(n−t+1)!t!</span>. This applies to one specified block of distinct items; several overlapping adjacency requirements need a new analysis.

To require t specified distinct objects to be pairwise nonadjacent, first arrange the other <span class="math-inline">n−t</span> objects. They create <span class="math-inline">n−t+1</span> gaps, including the two endpoints. Choose t different gaps and arrange the t special objects in them. The count is <span class="math-inline">(n−t)!C(n−t+1,t)t!</span>, zero when there are too few gaps. Selecting several objects for the same gap would violate nonadjacency; the gap selection is without repetition.

For binary strings with exactly k ones and no adjacent ones, the zeros create <span class="math-inline">n−k+1</span> gaps and each receives at most one indistinguishable one. The count is <span class="math-inline">C(n−k+1,k)</span>. Equivalently, for one positions <span class="math-inline">i<sub>1</sub>&lt;⋯&lt;i<sub>k</sub></span> satisfying successive gaps at least two, set <span class="math-inline">j<sub>r</sub>=i<sub>r</sub>−(r−1)</span>. These transformed positions form an arbitrary k-subset of <span class="math-inline">{1,…,n−k+1}</span>, giving an explicit bijection.

### 4.2 Stars and bars from a bijection

Count solutions of <span class="math-inline">x<sub>1</sub>+⋯+x<sub>r</sub>=N</span> with nonnegative integer coordinates, <span class="math-inline">N≥0</span>, and <span class="math-inline">r≥1</span>. Write N identical stars and <span class="math-inline">r−1</span> separators. The number of stars before the first separator is the first coordinate; the counts between separators give successive coordinates. Adjacent separators represent zero, as do separators at the endpoints. The map between solutions and strings is bijective.

There are <span class="math-inline">N+r−1</span> positions and one selects the separator positions. Hence the number of solutions is <span class="math-inline">C(N+r−1,r−1)</span>. For example, the vector <span class="math-inline">(2,0,1,2)</span> is encoded by <span class="math-inline">**||*|**</span>. The separators retain the order of the **named** coordinates; they do not make destinations interchangeable.

<figure class="logic-diagram"><svg viewBox="0 0 420 190" role="img" aria-label="Stars and bars for the occupancy vector two, zero, one, two. Five stars and three separators encode four named coordinates; adjacent separators encode the zero coordinate."><rect x="5" y="5" width="410" height="180" rx="12" fill="#f2f7f7" stroke="#b5d1cd"/><text x="24" y="35" font-size="18">Five identical stars, four named coordinates</text><g fill="#428d88"><circle cx="48" cy="82" r="10"/><circle cx="78" cy="82" r="10"/><circle cx="183" cy="82" r="10"/><circle cx="289" cy="82" r="10"/><circle cx="319" cy="82" r="10"/></g><g stroke="#34536b" stroke-width="3"><path d="M110 61 V104 M142 61 V104 M238 61 V104"/></g><text x="39" y="137" font-size="18">x<tspan baseline-shift="sub" font-size="13">1</tspan>=2</text><text x="114" y="137" font-size="18">x<tspan baseline-shift="sub" font-size="13">2</tspan>=0</text><text x="172" y="137" font-size="18">x<tspan baseline-shift="sub" font-size="13">3</tspan>=1</text><text x="283" y="137" font-size="18">x<tspan baseline-shift="sub" font-size="13">4</tspan>=2</text><text x="24" y="167" font-size="17">Adjacent separators preserve an empty coordinate.</text></svg><figcaption>Separator positions identify the named coordinates. The second coordinate is empty and is still represented; omitting it would destroy the bijection.</figcaption></figure>

If every coordinate must be at least <span class="math-inline">l<sub>i</sub>≥0</span>, replace it by <span class="math-inline">y<sub>i</sub>=x<sub>i</sub>−l<sub>i</sub></span>. The remaining total is <span class="math-inline">M=N−∑l<sub>i</sub></span>. If M is negative there are no solutions; otherwise there are <span class="math-inline">C(M+r−1,r−1)</span>. In particular, requiring every coordinate positive gives <span class="math-inline">C(N−1,r−1)</span> when <span class="math-inline">N≥r</span>. For a sum at most N, add one nonnegative slack coordinate to turn the inequality into an equality, giving <span class="math-inline">C(N+r,r)</span>.

### 4.3 Upper bounds need exclusion as well as shifting

Suppose all coordinates also satisfy <span class="math-inline">x<sub>i</sub>≤u<sub>i</sub></span>. After removing the lower bounds, let <span class="math-inline">v<sub>i</sub>=u<sub>i</sub>−l<sub>i</sub></span>. A negative capacity means infeasibility. Otherwise begin with all nonnegative y-solutions of total M, and exclude those with <span class="math-inline">y<sub>i</sub>≥v<sub>i</sub>+1</span>. For a chosen violation subset J, subtract <span class="math-inline">v<sub>i</sub>+1</span> from each violating coordinate. This is a bijection with unconstrained solutions of the reduced total.

Define <span class="math-inline">T<sub>J</sub>=M−∑<sub>i∈J</sub>(v<sub>i</sub>+1)</span>. Its contribution is <span class="math-inline">C(T<sub>J</sub>+r−1,r−1)</span> if <span class="math-inline">T<sub>J</sub>≥0</span>, and zero otherwise. Inclusion–exclusion adds these contributions with sign <span class="math-inline">(−1)<sup>|J|</sup></span>, including the empty subset. The shift uses capacity plus one because that is the *first forbidden value*. Subtracting just the capacity is an off-by-one error.

For equal upper bound u and zero lower bounds, all violation subsets of size j have the same contribution. The count simplifies to

<div class="formula-block formula-steps"><div>∑<sub>j=0</sub><sup>r</sup>(−1)ʲ C(r,j)</div><div>× C(N−j(u+1)+r−1,r−1),</div></div>

where terms with negative remaining total are zero. This is a finite formula; it does not treat negative factorials as numbers. Section 9 works through a case where pairwise violations must be added back.

### 4.4 Distinct objects, empty groups, and occupancy

Placing N **distinct** objects into r named bins, with no size restrictions, has count <span class="math-inline">rᴺ</span>: each object chooses a bin. This differs from stars and bars, which counts only occupancy vectors of indistinguishable objects. A vector of fixed occupancies has <span class="math-inline">N!/(x<sub>1</sub>!⋯x<sub>r</sub>!)</span> labeled placements and generally has a different mass from another vector under uniform placement.

To require every named bin nonempty, exclude events that a bin is unused. If a specified j-bin set is empty, every object has <span class="math-inline">r−j</span> destinations. Inclusion–exclusion gives the surjection count

<div class="formula-block">∑<sub>j=0</sub><sup>r</sup>(−1)ʲ C(r,j)(r−j)ᴺ.</div>

For <span class="math-inline">N&gt;0</span>, the all-bins-excluded term is zero. With <span class="math-inline">N=0</span>, the empty assignment is the one function to any destination set; treating <span class="math-inline">0⁰=1</span> in this combinatorial formula then produces zero surjections to a positive number of bins. Exactly s occupied bins are obtained by choosing the occupied-bin set in <span class="math-inline">C(r,s)</span> ways and multiplying by the surjection count onto those s bins. If <span class="math-inline">N&gt;0</span> and <span class="math-inline">s&gt;N</span>, the answer is zero.

### 4.5 Unlabeled groups and circular orderings

Removing group labels is another fiber problem. Splitting n distinct items into g nonempty unlabeled groups each of size t, where <span class="math-inline">n=gt</span>, has count <span class="math-inline">n!/[(t!)<sup>g</sup>g!]</span>. First form g named t-member groups; each unlabeled partition is reported by exactly <span class="math-inline">g!</span> labelings. Distinct disjoint nonempty groups ensure this fiber size. For prescribed unequal group sizes, divide only by the factorial multiplicity of each repeated size. The groups of different sizes are already distinguishable by their sizes. Allowing indistinguishable empty groups changes the labeling multiplicity; a blind division by the total number of group factorials fails.

For n distinct objects on a circle, consider rotations equivalent but keep clockwise orientation distinct from reflection. With <span class="math-inline">n≥1</span>, fix one specified object at an anchor position and arrange the rest. This gives <span class="math-inline">(n−1)!</span>. Equivalently, every rotation class of a labeled linear arrangement has exactly n members. If mirror images are also equivalent and <span class="math-inline">n≥3</span>, there are <span class="math-inline">(n−1)!/2</span> classes: reflection pairs distinct circular orders of distinct labels. Repeated symbols may have rotational or reflection symmetries and different fiber sizes. Their general orbit counts are outside this elementary formula; division by n or by two cannot be assumed.

### 4.6 Deterministic collision guarantees

The pigeonhole principle says that distributing N objects among r bins forces at least one occupancy to be at least <span class="math-inline">⌈N/r⌉</span>. If every occupancy were smaller, each would be at most that integer minus one, making the total strictly less than N. This is a deterministic conclusion, requiring neither random placement nor independence.

To force an occupancy at least t, it suffices and is necessary as a worst-case threshold to have <span class="math-inline">N&gt;r(t−1)</span>. With <span class="math-inline">N=r(t−1)</span>, the arrangement placing exactly <span class="math-inline">t−1</span> objects in each bin avoids it. A random collision probability is a separate question: below the threshold a collision can be highly likely without being logically forced.

## 5. Combinatorial identities as proofs, not memorized patterns

### 5.1 Pascal's recurrence

Count k-subsets of n labels by whether they contain a specified label. Those containing it choose <span class="math-inline">k−1</span> other members from <span class="math-inline">n−1</span>; those omitting it choose k. The cases are disjoint and exhaustive, so

<div class="formula-block">C(n,k)=C(n−1,k−1)+C(n−1,k), n≥1.</div>

The zero convention outside the valid range makes endpoint cases work. This proof also supports an exact dynamic-programming table without enormous intermediate factorials.

### 5.2 Vandermonde and the subset-sum identity

Take disjoint groups of a and b labels. A k-subset of their union has a unique number j selected from the first group. Summing these disjoint cases gives

<div class="formula-block">C(a+b,k)=∑<sub>j=0</sub><sup>k</sup>C(a,j)C(b,k−j).</div>

Invalid choices give zero, so summation endpoints remain unambiguous. This identity later verifies normalization of sampling-without-replacement probabilities. Separately, count all subsets of an n-set by their sizes to obtain <span class="math-inline">∑<sub>k=0</sub><sup>n</sup>C(n,k)=2ⁿ</span>. Each object is included or excluded, giving the alternative binary-string count.

### 5.3 The hockey-stick identity and weighted subsets

For <span class="math-inline">0≤r≤n</span>, count <span class="math-inline">(r+1)</span>-subsets of <span class="math-inline">{1,…,n+1}</span> by their largest member. If it is <span class="math-inline">j+1</span>, the other r members are selected from the first j labels. Thus <span class="math-inline">∑<sub>j=r</sub><sup>n</sup>C(j,r)=C(n+1,r+1)</span>. This proves the identity with exact endpoints rather than recognizing a diagonal in a table.

Expand the finite product <span class="math-inline">(x+y)ⁿ</span>. Each term selects x or y from each factor. Exactly k x-selections occur in <span class="math-inline">C(n,k)</span> ways. Therefore the expansion is <span class="math-inline">∑<sub>k=0</sub><sup>n</sup>C(n,k)xᵏy<sup>n−k</sup></span>. Taking <span class="math-inline">x=p</span> and <span class="math-inline">y=1−p</span> establishes unit total for the repeated-trial probabilities taught next. The counting coefficient and the weight of one pattern have separate roles.
