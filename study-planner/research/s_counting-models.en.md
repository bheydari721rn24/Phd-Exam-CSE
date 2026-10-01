## 6. Probabilities built from counted families

### 6.1 Uniform sampling without replacement

Uniform sequential draws without replacement from n distinct objects assign each ordered length k sample mass <span class="math-inline">1/(n)<sub>k</sub></span>. Every unordered k-subset has <span class="math-inline">k!</span> ordered preimages, so the induced subset law is uniform with mass <span class="math-inline">1/C(n,k)</span>. This conclusion depends on the uniform sequential mechanism, not merely on naming subsets.

Suppose K of N labeled objects are marked successes, and an unordered sample of size m is uniform without replacement. Exactly k successes require choosing k of the K marked objects and <span class="math-inline">m−k</span> of the others. The favorable and total counts give

<div class="formula-block formula-steps"><div>P(exactly k successes)</div><div>=C(K,k)C(N−K,m−k)/C(N,m).</div></div>

This is the hypergeometric counting probability. Its support is <span class="math-inline">max(0,m−(N−K))≤k≤min(m,K)</span>, for integers <span class="math-inline">0≤m≤N</span>. Values outside the support have probability zero. Vandermonde's identity makes the sum of favorable counts equal the denominator, verifying normalization.

An ordered derivation gives the same result. Choose the success positions in <span class="math-inline">C(m,k)</span> ways, place distinct marked labels in <span class="math-inline">(K)<sub>k</sub></span> ways, and distinct unmarked labels in <span class="math-inline">(N−K)<sub>m−k</sub></span> ways. Divide by <span class="math-inline">(N)<sub>m</sub></span>. Expanding factorials reduces this to the subset formula. This equivalence is a useful check that numerator and denominator use consistent objects.

### 6.2 Independent repeated trials and binomial counts

In n mutually independent binary trials with common success probability p, a particular pattern of k successes and <span class="math-inline">n−k</span> failures has probability <span class="math-inline">pᵏ(1−p)<sup>n−k</sup></span>. There are <span class="math-inline">C(n,k)</span> such patterns, and distinct patterns are disjoint events. Therefore

<div class="formula-block">P(exactly k successes)=C(n,k)pᵏ(1−p)<sup>n−k</sup>.</div>

Independence justifies the within-pattern product; disjointness justifies adding different patterns; counting supplies the coefficient. These are three separate steps. The binomial expansion of <span class="math-inline">(p+(1−p))ⁿ</span> verifies the total is one. For <span class="math-inline">p=0</span> or <span class="math-inline">p=1</span>, only one pattern has nonzero probability. Empty products give the correct boundary values; no division by p is required.

If independent trials have different success probabilities <span class="math-inline">p<sub>i</sub></span>, patterns with the same number of successes need not have the same mass. For a success-position set S, multiply <span class="math-inline">p<sub>i</sub></span> over positions in S and <span class="math-inline">1−p<sub>i</sub></span> over positions outside S, then sum over all k-element S. One binomial coefficient times a common weight is generally invalid. Independence and identical trial probabilities are different hypotheses.

At least one success in independent trials has probability <span class="math-inline">1−∏(1−p<sub>i</sub>)</span>. For common p this is <span class="math-inline">1−(1−p)ⁿ</span>. Directly adding success marginals overcounts multiple successes. Conversely, without replacement from a mixed population, trial success probabilities update with previous draws; the binomial formula generally fails and the hypergeometric model is appropriate.

### 6.3 Multinomial occupancy and the wrong uniform model

Place N distinct objects independently into r named bins, each object choosing bin i with probability <span class="math-inline">p<sub>i</sub></span>, with nonnegative probabilities summing to one. A specified labeled placement with occupancy vector x has mass <span class="math-inline">p<sub>1</sub><sup>x<sub>1</sub></sup>⋯p<sub>r</sub><sup>x<sub>r</sub></sup></span>. There are <span class="math-inline">N!/(x<sub>1</sub>!⋯x<sub>r</sub>!)</span> placements with that vector, so

<div class="formula-block formula-steps"><div>P(occupancies x<sub>1</sub>,…,x<sub>r</sub>)</div><div>=N!/(x<sub>1</sub>!⋯x<sub>r</sub>!)</div><div>× p<sub>1</sub><sup>x<sub>1</sub></sup>⋯p<sub>r</sub><sup>x<sub>r</sub></sup>.</div></div>

The vector must be nonnegative integral with total N. An empty group contributes exponent zero, interpreted as an empty product of one even when its probability is zero. A positive occupancy of a zero-probability bin has mass zero. The formula follows by grouping a normalized independent placement law; it is not a uniform law on the stars-and-bars vectors.

For a set T of bins, the probability that none of N independent objects enters T is <span class="math-inline">(1−∑<sub>i∈T</sub>p<sub>i</sub>)ᴺ</span>. Inclusion–exclusion over omitted bins gives the probability that each of a specified bin set is occupied. Under uniform choices, the all-bins-occupied count from Section 4 divided by <span class="math-inline">rᴺ</span> is the same result. The events “bin 1 is occupied” and “bin 2 is occupied” are generally dependent even when individual object placements are independent. Independence must refer to the particular events being multiplied.

### 6.4 Birthday collisions and a justified bound

Let m labeled objects choose independently and uniformly among n labels. All <span class="math-inline">n<sup>m</sup></span> sequences are equally likely. If <span class="math-inline">m≤n</span>, no collision requires all labels distinct, giving

<div class="formula-block formula-steps"><div>P(no collision)=(n)<sub>m</sub>/n<sup>m</sup></div><div>=∏<sub>j=0</sub><sup>m−1</sup>(1−j/n).</div></div>

With <span class="math-inline">m&gt;n</span>, the probability is zero by pigeonhole. With m equal to zero or one it is one. A collision probability is the complement of this expression; a naive sum of pairwise collision probabilities counts an outcome with several collisions repeatedly.

For <span class="math-inline">0≤x&lt;1</span>, the inequality <span class="math-inline">log(1−x)≤−x</span> follows because the derivative of <span class="math-inline">log(1−x)+x</span> is <span class="math-inline">−x/(1−x)≤0</span> and its value at zero is zero. If elementary calculus is not yet available, the equivalent inequality <span class="math-inline">1−x≤e<sup>−x</sup></span> may be used as the stated analytic input. Multiplying it over the factors gives the rigorous bound

<div class="formula-block">P(no collision)≤exp(−m(m−1)/(2n)), m≤n.</div>

Thus collision probability is at least one minus that exponential. The commonly used exponential approximation is not an identity. A complementary union-bound upper bound is <span class="math-inline">min(1,C(m,2)/n)</span>, since each specified pair matches with probability <span class="math-inline">1/n</span>. Both bounds have directions; neither replaces the exact finite product without a stated reason.

### 6.5 Derangements and exact fixed-point counts

A derangement is a permutation of n distinct labels in which none occupies its original position. Let the forbidden event i be that label i is fixed. If a specified j-set is fixed, the remaining labels can be permuted in <span class="math-inline">(n−j)!</span> ways. Inclusion–exclusion over the fixed-position events gives

<div class="formula-block formula-steps"><div>D<sub>n</sub>=∑<sub>j=0</sub><sup>n</sup>(−1)ʲ C(n,j)(n−j)!</div><div>=n!∑<sub>j=0</sub><sup>n</sup>(−1)ʲ/j!.</div></div>

Here <span class="math-inline">D<sub>0</sub>=1</span> and <span class="math-inline">D<sub>1</sub>=0</span>. Under a uniform random permutation, no fixed points has probability <span class="math-inline">D<sub>n</sub>/n!</span>. Exactly k fixed points is counted by choosing those k positions and deranging the remainder: <span class="math-inline">C(n,k)D<sub>n−k</sub></span>. A permutation cannot have exactly <span class="math-inline">n−1</span> fixed points because the last label is then forced to be fixed too; the formula captures this through <span class="math-inline">D<sub>1</sub>=0</span>.

Fixing positions is not an independent family of events. The probability of one fixed position is <span class="math-inline">1/n</span>, but the probability that two specified positions are fixed is <span class="math-inline">1/[n(n−1)]</span>, not <span class="math-inline">1/n²</span> for <span class="math-inline">n≥2</span>. The frequently quoted large-n limit <span class="math-inline">1/e</span> is not an exact finite answer. The finite alternating sum is the relevant exact formula here.

### 6.6 Repeated races: sum disjoint stopping cases

On each of an independent sequence of identical trials, category A occurs with probability a, disjoint category B with probability b, and neither with probability <span class="math-inline">1−a−b</span>. Assume <span class="math-inline">a+b&gt;0</span>. The event that A appears before B is partitioned by its first relevant trial n. Its nth piece has probability <span class="math-inline">(1−a−b)<sup>n−1</sup>a</span>.

To derive the required series, let <span class="math-inline">S<sub>M</sub>=1+r+⋯+r<sup>M</sup></span>. Subtracting its r-multiple cancels all middle terms and gives <span class="math-inline">(1−r)S<sub>M</sub>=1−r<sup>M+1</sup></span>. For <span class="math-inline">0≤r&lt;1</span>, the last power tends to zero, so the sum tends to <span class="math-inline">1/(1−r)</span>. This proof also covers r equal to zero.

The stopping pieces are disjoint, so countable additivity and this geometric series give probability <span class="math-inline">a/(a+b)</span>. Indeed <span class="math-inline">∑<sub>n=1</sub><sup>∞</sup>r<sup>n−1</sup>=∑<sub>j=0</sub><sup>∞</sup>rʲ=1/(1−r)</span>. The chance of never seeing a relevant category is the limit <span class="math-inline">rⁿ→0</span>. If both a and b are zero, neither category ever appears and the ratio is undefined; the event of A preceding B then has probability zero under the strict-occurrence interpretation. Nonidentical or dependent trials require a different model.

## 7. Independence: definitions, proofs, and hidden dependence

### 7.1 The product definition and its conditional interpretation

Two measurable events A and B are **independent** if <span class="math-inline">P(A∩B)=P(A)P(B)</span>. This is a property of both the events and the probability law. It applies to nonuniform laws and does not require disjointness. It is symmetric, even though a sequential interpretation may make one event occur later.

For <span class="math-inline">P(B)&gt;0</span>, define <span class="math-inline">P(A|B)=P(A∩B)/P(B)</span>. It is the probability after restricting the universe to B and renormalizing its mass. With that positive-denominator condition, independence is equivalent to <span class="math-inline">P(A|B)=P(A)</span>. Multiplying back establishes both directions. If B is null, the conditional ratio is undefined, but the product definition of independence still works: the intersection is null by monotonicity, so every null event is independent of every event.

For dependent events the correct multiplication is <span class="math-inline">P(A∩B)=P(B)P(A|B)</span> when the conditional factor is defined. A sequential chain repeats this identity while conditioning on every preceding event. Positive probabilities of the conditioning prefixes are required. If a prefix is null, the entire joint event is null; undefined later ratios must not be evaluated as ordinary numbers. Full chain-rule and Bayes applications are developed in the next chapter.

### 7.2 Complement preservation and degenerate events

If A and B are independent, split B into <span class="math-inline">A∩B</span> and <span class="math-inline">A<sup>c</sup>∩B</span>. Then

<div class="formula-block formula-steps"><div>P(A<sup>c</sup>∩B)=P(B)−P(A∩B)</div><div>=(1−P(A))P(B)=P(A<sup>c</sup>)P(B).</div></div>

Thus complementing one event preserves independence. Apply the result to the other event as well to obtain independence of any choice of A or its complement with B or its complement. Conversely, complement the changed events again, so each of these independence statements is equivalent to the original one.

Two disjoint events are independent exactly when at least one marginal is zero: their intersection mass is zero, so the product must be zero. Positive-probability disjoint events are dependent. An event independent of itself satisfies <span class="math-inline">P(A)=P(A)²</span>, hence has probability zero or one. Conversely, any null or probability-one event is independent of every event. For the probability-one case, its complement is null, so its intersection with B loses no mass from B. These facts cover degenerate boundaries without conditional divisions.

### 7.3 Mutual independence tests every subfamily

Events <span class="math-inline">A<sub>1</sub>,…,A<sub>n</sub></span> are **mutually independent** if for every index subset I with at least two members, their joint probability equals the product of their marginals. There are <span class="math-inline">2ⁿ−n−1</span> displayed intersection conditions, although numerical constraints can be redundant in degenerate models. The empty and singleton cases already hold automatically.

For three events, check the three pairs **and** the triple. Checking only the triple does not imply the pairs; checking all pairs does not imply the triple. For n greater than three, all intermediate subfamily sizes matter too. An infinite family is called independent if every finite subfamily satisfies these conditions; this chapter computes finite families rather than constructing infinite product measures.

An equivalent condition requires every binary occurrence pattern to factor. Choose <span class="math-inline">B<sub>i</sub></span> to be either <span class="math-inline">A<sub>i</sub></span> or <span class="math-inline">A<sub>i</sub><sup>c</sup></span>. Then

<div class="formula-block">P(B<sub>1</sub>∩⋯∩B<sub>n</sub>)=∏<sub>i=1</sub><sup>n</sup>P(B<sub>i</sub>).</div>

**Proof from subfamilies to patterns.** For any subfamily intersection, replace one event by its complement. The replacement intersection is the intersection of all the other selected events minus the original intersection. Their product probabilities differ by a factor of <span class="math-inline">1−P(A<sub>i</sub>)</span>. An induction on the number of complemented events repeats this subtraction and proves every pattern formula, including partial patterns.

**Proof from full patterns to subfamilies.** A subfamily intersection is the disjoint union of its full patterns over every choice of occurrences and nonoccurrences outside that subfamily. Sum the pattern products. For each unselected index, its two factors sum to <span class="math-inline">P(A<sub>i</sub>)+P(A<sub>i</sub><sup>c</sup>)=1</span>. Only the selected-index marginal product remains. This proves the equivalence and justifies complementing any number of events without losing mutual independence.

### 7.4 Pairwise independence leaves higher-order structure free

Pairwise independence requires only the two-event conditions. Take two independent fair bits X and Y, and set Z to their exclusive-or. The four possible triples are <span class="math-inline">000,011,101,110</span>, each with mass <span class="math-inline">1/4</span>. Every bit is marginally fair. For any chosen pair, each of the four pair values appears exactly once, so its probability is <span class="math-inline">1/4</span>. All pairs are independent.

Yet Z is determined by X and Y. For the events that the respective bits equal one, the triple intersection is empty and has mass zero, while the product of the three marginals is <span class="math-inline">1/8</span>. Pairwise independence therefore cannot justify a three-factor product or a product of three failure complements. It conceals the parity constraint.

A continuous family of finite laws makes the gap visible. On the eight triples <span class="math-inline">(x,y,z)∈{0,1}³</span>, assign

<div class="formula-block formula-steps"><div>P<sub>θ</sub>({(x,y,z)})</div><div>=[1+θ(−1)<sup>x+y+z</sup>]/8, −1≤θ≤1.</div></div>

Even-parity points receive <span class="math-inline">(1+θ)/8</span>; odd-parity points receive <span class="math-inline">(1−θ)/8</span>. The eight masses are nonnegative and total one. For each fixed pair, the two possible values of the remaining bit have opposite parity, so their masses sum to <span class="math-inline">1/4</span>, regardless of θ. Each marginal is therefore <span class="math-inline">1/2</span> and every pair is independent for every θ.

The all-one point has odd parity and mass <span class="math-inline">(1−θ)/8</span>. It equals the marginal product <span class="math-inline">1/8</span> exactly when θ is zero. At zero the entire space is uniform, so mutual independence holds. At either endpoint the model has a deterministic parity constraint. These facts distinguish a valid dependent probability model from a numerical mistake.

### 7.5 Functions of disjoint independent groups

Suppose a finite collection of binary events is mutually independent. Divide its indices into disjoint groups. Any event whose truth is determined entirely by the bits in one group is independent of any event determined by another group. To prove this, expand each group's event as a disjoint union of that group's binary patterns. The joint event is a disjoint union of combined patterns. Mutual independence factors each combined mass, and the two finite sums separate into a product of the group-event probabilities.

This result justifies, for example, independence of “at least one success among the first two trials” and “exactly one success among the next three” when all five trials are mutually independent. If the groups share a trial, the result does not apply. Nor does pairwise independence of the original bits establish independence of arbitrary functions of several bits: the parity construction is a counterexample.

### 7.6 Conditioning can change the law and its independence

Independent fair bits have four equally likely pairs. Condition on at least one being one. The retained pairs are <span class="math-inline">01,10,11</span>, each with conditional mass <span class="math-inline">1/3</span>. Both one-events now have probability <span class="math-inline">2/3</span>, but their joint probability is <span class="math-inline">1/3</span>, which differs from <span class="math-inline">4/9</span>. Selection created dependence by removing one pattern.

The reverse effect is also possible. Choose a hidden coin type uniformly: one has heads probability <span class="math-inline">3/4</span>, the other <span class="math-inline">1/4</span>. Given its type, toss it twice independently. Each toss is marginally fair when the type is hidden, but both-heads probability is <span class="math-inline">(1/2)(3/4)²+(1/2)(1/4)²=5/16</span>, exceeding <span class="math-inline">1/4</span>. The shared hidden type creates dependence. Once its type is conditioned on, the two tosses are independent under that conditional law.

The definition of conditional independence given C is the same product equality in the renormalized law, with <span class="math-inline">P(C)&gt;0</span>. Ordinary and conditional independence imply neither one another in general. These two finite examples establish that fact without assuming an entire graphical-model theory.

## 8. Interactive laboratory: identical pairs, different triples

The laboratory changes θ in the exact parity law above. All three marginal probabilities and all three pairwise joint probabilities remain fixed. The eight displayed point masses and the all-one joint probability change. This is an exact finite model, not sampled evidence or a claim about physical random generators.

<section class="independence-lab" aria-labelledby="parity-title">
<h3 id="parity-title">Inspect the hidden three-way constraint</h3>
<label for="parity"><span>Parity parameter θ</span><input id="parity" type="range" min="-100" max="100" value="100"><output id="parity-value" for="parity">1.00</output></label>
<div id="parity-result" aria-live="polite"></div>
<table><thead><tr><th>Outcome</th><th>Probability</th><th>Mass</th></tr></thead><tbody id="parity-masses"></tbody></table>
<noscript><p>At θ equal to one, the four even-parity points each have mass 1/4 and the other four are null. Every pair is independent, but the three events are not mutually independent.</p></noscript>
</section>

At θ equal to zero, inspect all eight equal masses and the all-one probability matching the three-factor product. At either endpoint, inspect the four missing points and the parity rule. The laboratory measures independence of the named one-events. It does not turn pairwise information into evidence of higher-order factorization.
