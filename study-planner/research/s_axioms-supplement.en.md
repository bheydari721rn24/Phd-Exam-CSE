## 7. Interactive laboratory: four regions, one probability law

Two event probabilities do not determine their overlap. This laboratory displays the four disjoint regions underlying every pair of events. Change the two marginal probabilities and their proposed overlap. A negative region makes the proposal impossible; a valid proposal supplies an explicit probability model. No independence assumption is made.

<section class="probability-lab" aria-labelledby="lab-title">
<h3 id="lab-title">Explore the overlap constraint</h3>
<p>Values are percentages. The starting model has event probabilities 65% and 45%, with 25% overlap.</p>
<div class="lab-controls">
<label for="pa"><span class="lab-label">Probability of A</span><input id="pa" type="range" min="0" max="100" value="65"><output id="pa-value" for="pa">65%</output></label>
<label for="pb"><span class="lab-label">Probability of B</span><input id="pb" type="range" min="0" max="100" value="45"><output id="pb-value" for="pb">45%</output></label>
<label for="pq"><span class="lab-label">Proposed overlap</span><input id="pq" type="range" min="0" max="100" value="25"><output id="pq-value" for="pq">25%</output></label>
</div>
<div id="lab-result" aria-live="polite"></div>
<div id="lab-regions" class="lab-regions"></div>
<noscript><p>The starting masses are 25% in both events, 40% in A only, 20% in B only, and 15% in neither. JavaScript enables changes to this exact model.</p></noscript>
</section>

The display represents probability mass, not necessarily geometric area in the original experiment. A valid four-region model proves feasibility of these three probabilities; it does not establish that a particular physical experiment actually follows that law. Use the calculation to inspect assumptions, not to invent observations.

## 8. Fully worked problems

The problems below are original formulations. Their instructional targets synthesize the reviewed courses: MIT and Stanford inform finite experiment modeling; Berkeley and ETH inform measurable events, axioms, and limits; Oxford informs union-bound reasoning. None is represented as a verbatim university examination question. Counting methods and conditional-probability exercises are reserved for the next chapter. Each solution makes its model explicit before using a formula.

### Problem 1. Translate a verbal event before calculating

Two independent fair coins are tossed in order. Let A mean that the first coin is heads and B mean that the second is heads. Find the probabilities of “at least one head,” “exactly one head,” and “the first is heads but the second is not.”

**Solution.** The ordered space is <span class="math-inline">Ω={HH,HT,TH,TT}</span>, and the stated fair independent model assigns mass <span class="math-inline">1/4</span> to every outcome. Thus <span class="math-inline">A={HH,HT}</span> and <span class="math-inline">B={HH,TH}</span>. “At least one” is the union <span class="math-inline">{HH,HT,TH}</span>, with mass <span class="math-inline">3/4</span>. “Exactly one” is the symmetric difference <span class="math-inline">{HT,TH}</span>, with mass <span class="math-inline">1/2</span>. “First but not second” is <span class="math-inline">A∖B={HT}</span>, with mass <span class="math-inline">1/4</span>.

The union includes the two-head outcome, whereas the symmetric difference excludes it. Treating the word “or” as “exactly one” changes the event and therefore the answer. The probabilities used here come from the stated law; the list of four outcomes alone would not imply equal masses.

### Problem 2. A smaller sample space need not be uniform

In Problem 1, retain only the number of heads. A proposed answer says that the three possible results 0, 1, and 2 each have probability <span class="math-inline">1/3</span>. Diagnose and repair it.

**Solution.** The reporting map sends TT to 0, HT and TH to 1, and HH to 2. The probability of a reported value equals the sum of the masses of its preimages. Consequently,

<div class="formula-block">Q({0})=1/4, Q({1})=1/2, Q({2})=1/4.</div>

The map merges two elementary outcomes for the middle category and one for each other category. It does not create a new randomization mechanism. The repaired model gives <span class="math-inline">Q({1,2})=3/4</span>, agreeing with the ordered model. The incorrect uniform model gives <span class="math-inline">2/3</span>. A valid change of representation preserves the probabilities of corresponding events; it need not preserve equal likelihood of the newly named outcomes.

### Problem 3. Normalize a weighted finite law

Four outcomes have masses <span class="math-inline">k,2k,3k,4k</span>. Determine k and the probability of the event containing the second and fourth outcomes. Explain why normalization alone would not suffice for arbitrary proposed weights.

**Solution.** The total mass is <span class="math-inline">10k</span>, so normalization forces <span class="math-inline">k=1/10</span>. All four masses are then nonnegative. On the full power set, assigning an event the sum of its singleton masses gives a probability law: disjoint events collect disjoint summands, and the total is one. The requested probability is <span class="math-inline">2k+4k=3/5</span>.

A collection such as <span class="math-inline">(0.6,0.6,−0.2)</span> sums to one but cannot be a probability law because one singleton has negative mass. Always check both nonnegativity and normalization. For a countably infinite space, also verify the infinite series rather than merely a finite partial sum.

### Problem 4. Test a proposed event collection

Let <span class="math-inline">Ω={1,2,3,4}</span>. A proposed event collection contains only the empty set, Ω, and <span class="math-inline">{1,2},{3,4},{1,3},{2,4}</span>. Is it a sigma-algebra? What sigma-algebra do these sets generate?

**Solution.** The collection contains complements, but this is only one closure requirement. The intersection of <span class="math-inline">{1,2}</span> and <span class="math-inline">{1,3}</span> is <span class="math-inline">{1}</span>, which is missing. Closure under complements and unions would imply closure under intersections by De Morgan's identity, so the collection fails. Its union <span class="math-inline">{1,2,3}</span> is another missing event.

To find the generated collection, intersect each of the two crossing sets or its complement. The resulting four regions are the four singletons. Every subset of Ω is a union of these singletons, so the generated sigma-algebra is the full power set, containing <span class="math-inline">2⁴=16</span> events. This argument identifies the information atoms before counting their possible unions.

### Problem 5. A coarse event collection hides singleton probabilities

Suppose the only events are <span class="math-inline">∅,Ω,{1,2},{3,4}</span>, and the first pair has probability 0.3. Can the probability of <span class="math-inline">{1}</span> be recovered?

**Solution.** The stated collection is a sigma-algebra generated by a two-cell partition. Normalization assigns mass 0.7 to the second cell. The singleton <span class="math-inline">{1}</span> is not an event of this probability space, so its probability is not defined by this law.

Even if we choose to extend the law to all subsets, uniqueness fails. The singleton masses <span class="math-inline">(0.1,0.2,0.3,0.4)</span> and <span class="math-inline">(0.25,0.05,0.6,0.1)</span> both reproduce the two stated cell masses but disagree on the requested singleton. Indeed any first mass in <span class="math-inline">[0,0.3]</span> can be paired with the remaining mass in the first cell. An undefined probability is different from a probability that happens to be zero.

### Problem 6. Recover overlap and one-sided differences

Given <span class="math-inline">P(A)=0.55</span>, <span class="math-inline">P(B)=0.40</span>, and <span class="math-inline">P(A∪B)=0.70</span>, find the overlap, A only, B only, and neither. Check that the data define a possible model.

**Solution.** Inclusion–exclusion gives overlap <span class="math-inline">0.55+0.40−0.70=0.25</span>. Subtract it from each marginal: A only has mass 0.30 and B only has mass 0.15. The complement of the union has mass 0.30. The four masses are <span class="math-inline">0.25,0.30,0.15,0.30</span>; all are nonnegative and their sum is one.

Assign these masses to four elementary outcomes labeled both, A only, B only, and neither. The events A and B formed from these labels have exactly the supplied probabilities. This establishes feasibility, rather than merely producing algebraic answers. Notice that A only is a difference event; it is not the complement of B, which also includes neither.

### Problem 7. Detect an impossible proposed overlap

Can two events satisfy <span class="math-inline">P(A)=0.7</span>, <span class="math-inline">P(B)=0.6</span>, and <span class="math-inline">P(A∩B)=0.2</span>?

**Solution.** The implied union probability is <span class="math-inline">0.7+0.6−0.2=1.1</span>, exceeding one. Equivalently, the neither region has mass <span class="math-inline">1−0.7−0.6+0.2=−0.1</span>. Both contradictions come from the same four-region partition.

For these marginals the admissible overlap interval is <span class="math-inline">[max(0,0.7+0.6−1),min(0.7,0.6)]=[0.3,0.6]</span>. Every value in this interval is realizable by the four-region construction. The upper bound alone would not detect the proposed error; the lower bound is essential when the marginals sum to more than one.

### Problem 8. Find sharp bounds without assuming dependence

Only <span class="math-inline">P(A)=0.4</span> and <span class="math-inline">P(B)=0.5</span> are known. Find the smallest and largest possible union probabilities, and construct laws attaining them.

**Solution.** The overlap can range from zero to 0.4. Since union mass is <span class="math-inline">0.9−q</span>, the union lies in <span class="math-inline">[0.5,0.9]</span>. For the lower endpoint take the four masses in the order both, A only, B only, neither to be <span class="math-inline">(0.4,0,0.1,0.5)</span>. Here A lies inside B up to a null region. For the upper endpoint use <span class="math-inline">(0,0.4,0.5,0.1)</span>; here the two positive-mass regions are disjoint.

The constructions prove that neither bound can be improved from the marginals alone. Multiplying the marginals to set overlap to 0.2 would impose an additional independence assumption and give just one admissible model, not the sharp range.

### Problem 9. Distinguish exclusive and inclusive alternatives

Let <span class="math-inline">P(A)=0.65</span>, <span class="math-inline">P(B)=0.45</span>, and overlap be 0.25. Find exactly one, at least one, neither, and the probability that A fails while B occurs.

**Solution.** The region masses are both 0.25, A only 0.40, B only 0.20, and neither 0.15. Exactly one therefore has mass <span class="math-inline">0.40+0.20=0.60</span>. At least one also includes both and has mass 0.85. Neither is 0.15. The last event is B only and has mass 0.20.

The symmetric-difference formula yields the same first answer: <span class="math-inline">0.65+0.45−2(0.25)=0.60</span>. Two copies of overlap must be removed because neither occurrence of the intersection belongs to “exactly one.” In contrast, the union subtracts overlap once because it should retain one copy.

### Problem 10. Audit three-event inclusion–exclusion

Three events have eight membership-region masses as follows. Calculate each marginal, the union, exactly one occurrence, exactly two occurrences, and at least two occurrences.

| Membership region | Mass |
|---|---:|
| None | 0.05 |
| A only | 0.10 |
| B only | 0.15 |
| C only | 0.20 |
| A and B only | 0.10 |
| A and C only | 0.15 |
| B and C only | 0.05 |
| All three | 0.20 |

**Solution.** The listed masses sum to one and are nonnegative. Add the rows containing each event: <span class="math-inline">P(A)=0.55</span>, <span class="math-inline">P(B)=0.50</span>, and <span class="math-inline">P(C)=0.60</span>. Pairwise intersections include the last row, so their probabilities are 0.30, 0.35, and 0.25, respectively. Inclusion–exclusion gives

<div class="formula-block">P(A∪B∪C)=0.55+0.50+0.60−0.30−0.35−0.25+0.20=0.95.</div>

This agrees with one minus the none row. Exactly one is <span class="math-inline">0.10+0.15+0.20=0.45</span>. Exactly two is <span class="math-inline">0.10+0.15+0.05=0.30</span>, and at least two is <span class="math-inline">0.30+0.20=0.50</span>. Adding pairwise-intersection probabilities gives 0.90, which counts the triple region three times and is not the probability of either of these last events.

### Problem 11. Pairwise feasibility does not establish joint feasibility

Suppose three events each have probability 0.5, and every pairwise intersection has probability zero. Each pair satisfies its two-event overlap bounds. Can all three conditions hold together?

**Solution.** The triple intersection is contained in every pairwise intersection and therefore also has probability zero. Inclusion–exclusion forces the union probability to be <span class="math-inline">0.5+0.5+0.5=1.5</span>, a contradiction. Equivalently, removing the null overlaps leaves three disjoint positive-mass regions whose masses already exceed the total mass.

The pairwise overlap interval for two marginals 0.5 is <span class="math-inline">[0,0.5]</span>, so each individual pair passes. Their three simultaneous constraints do not. For three or more events, write all membership regions or additional joint constraints; pairwise checks are necessary but not sufficient.

### Problem 12. Reliability bounds with unknown dependence

Three possible faults have probabilities at most 0.01, 0.02, and 0.03. No dependence information is available. What guaranteed lower bound follows for no fault? Can a product formula be used?

**Solution.** The event of at least one fault is the union of the three fault events. The union bound gives probability at most <span class="math-inline">0.01+0.02+0.03=0.06</span>. Taking its complement gives no-fault probability at least 0.94.

This guarantee remains valid whether faults tend to occur together or separately. A product of three success probabilities would require independence and exact marginal values; neither is supplied. The bound is attainable when the three fault events are disjoint with the stated masses and the remaining 0.94 is assigned to no fault. If a sum of fault bounds exceeds one, cap the union bound at one and the resulting success lower bound at zero.

### Problem 13. Work with a mixed continuous and atomic law

On <span class="math-inline">[0,1]</span>, place mass <span class="math-inline">2/5</span> at zero and distribute the rest uniformly. Find the probabilities of <span class="math-inline">{0}</span>, <span class="math-inline">(0,1/2]</span>, <span class="math-inline">[0,1/2]</span>, and the rational points in the interval.

**Solution.** Apply the mixed-law formula to each event. The singleton zero receives the atomic mass <span class="math-inline">2/5</span>; its length is zero. The half-open interval excludes the atom and has length <span class="math-inline">1/2</span>, so its mass is <span class="math-inline">(3/5)(1/2)=3/10</span>. The closed half-interval includes the atom, so its mass is <span class="math-inline">2/5+3/10=7/10</span>.

The rational points are a countable Borel set of length zero, but contain zero. Their total mass is therefore <span class="math-inline">2/5</span>, not zero. The irrational points carry the remaining <span class="math-inline">3/5</span>. A countable set is null under this uniform component; countability alone does not make it null under every probability law.

### Problem 14. Normalize a telescoping countable law

On the positive integers, set <span class="math-inline">p<sub>n</sub>=1/[n(n+1)]</span>. Prove that these weights define a law and find the probability of an outcome at least m.

**Solution.** Every weight is nonnegative. Rewrite it as <span class="math-inline">1/n−1/(n+1)</span>. The first N weights sum to <span class="math-inline">1−1/(N+1)</span>, whose limit is one. Thus assigning each subset the sum of its weights gives a normalized countably additive law.

For integers <span class="math-inline">N≥m≥1</span>, the finite tail sum is <span class="math-inline">1/m−1/(N+1)</span>. Taking N to infinity gives <span class="math-inline">P({m,m+1,…})=1/m</span>. In particular, <span class="math-inline">P({1,2,3})=1−1/4=3/4</span>. The calculation depends on the infinite-series limit, not on treating the positive integers as equiprobable.

### Problem 15. Separate odd and even outcomes in a countable model

Let <span class="math-inline">p<sub>n</sub>=2/3ⁿ</span> for <span class="math-inline">n≥1</span>. Verify normalization, then calculate even-outcome probability and the tail probability from m onward.

**Solution.** The geometric sum is <span class="math-inline">2(1/3)/(1−1/3)=1</span>. Even outcomes have indices <span class="math-inline">n=2k</span>, so their total mass is <span class="math-inline">2∑<sub>k≥1</sub>(1/9)ᵏ=2(1/9)/(1−1/9)=1/4</span>. The complement gives odd-outcome probability <span class="math-inline">3/4</span>.

Factoring the first term out of the tail yields <span class="math-inline">∑<sub>n≥m</sub>2/3ⁿ=(2/3ᵐ)/(1−1/3)=3<sup>1−m</sup></span>. The even and odd sets have the same countably infinite cardinality but unequal probability. Cardinality ratios cannot replace weighted sums in an infinite probability model.

### Problem 16. Prove that uniform positive-integer sampling is impossible

A model claims to select each positive integer with the same probability c. Show that no countably additive probability law on all subsets can satisfy this claim.

**Solution.** Nonnegativity requires <span class="math-inline">c≥0</span>. If <span class="math-inline">c&gt;0</span>, choose a finite number N with <span class="math-inline">Nc&gt;1</span>. Finite additivity makes the first N integers have probability <span class="math-inline">Nc</span>, contradicting the upper bound one. Therefore c must be zero. Countable additivity would then assign the union of all singleton integers probability <span class="math-inline">∑0=0</span>, contradicting normalization.

These two cases exhaust the possible common masses. A uniform draw from the finite set <span class="math-inline">{1,…,N}</span> is valid for each N, but those finite laws do not justify a uniform law on the entire positive-integer space. The failure is a property of the proposed law, not a prohibition on nonuniform countable laws.

### Problem 17. Compute a continuous probability by area

A point is uniform in the unit square. Find the probability that its coordinates sum to at most <span class="math-inline">3/2</span>. Why is this an area calculation rather than a count of favorable points?

**Solution.** The excluded region satisfies <span class="math-inline">x+y&gt;3/2</span>. Inside the square it is the corner triangle with vertices <span class="math-inline">(1/2,1),(1,1/2),(1,1)</span>. Its two perpendicular legs each have length <span class="math-inline">1/2</span>, so its area is <span class="math-inline">(1/2)(1/2)(1/2)=1/8</span>. The desired probability is <span class="math-inline">1−1/8=7/8</span>.

The line boundary has area zero, so including it does not change this probability under the specified area law. Both the favorable set and the square contain uncountably many points; dividing their cardinalities is not the definition of this law. The uniform-area assumption is the reason that geometric area gives probability.

<svg class="lesson-diagram" viewBox="0 0 500 285" role="img" aria-labelledby="triangle-title"><title id="triangle-title">Unit square with the upper right excluded triangle for a coordinate sum greater than three halves</title><rect x="120" y="30" width="210" height="210" fill="#edf5f5" stroke="#486977" stroke-width="2"/><path d="M225 30 L330 135 L330 30 Z" fill="#e5b8a1"/><path d="M225 30 L330 135" stroke="#975f46" stroke-width="2"/><text x="225" y="263" text-anchor="middle">x</text><text x="98" y="135" text-anchor="middle">y</text><text x="108" y="257">0</text><text x="330" y="257" text-anchor="middle">1</text><text x="100" y="36">1</text><text x="280" y="57" text-anchor="middle" font-size="14">Excluded</text><text x="280" y="78" text-anchor="middle" font-size="14">area = 1/8</text><text x="215" y="187" text-anchor="middle" font-size="16">Included area = 7/8</text></svg>

### Problem 18. Distinguish impossible from null, and certain from exhaustive

On <span class="math-inline">Ω={u,v,w}</span>, assign masses <span class="math-inline">(1/2,1/2,0)</span>. Give a nonempty null event and a proper event with probability one. How does the answer change if every singleton has positive mass?

**Solution.** The event <span class="math-inline">{w}</span> is nonempty but has probability zero. The event <span class="math-inline">{u,v}</span> is proper because it omits w, yet has probability one. Normalization concerns total mass; it does not require every named outcome to carry positive mass.

If every singleton in a finite space has positive mass, any nonempty event contains at least one positive-mass singleton, so it has positive probability by monotonicity. A proper event then has a nonempty complement of positive mass, making its own probability less than one. The extra strict-positivity assumption is indispensable. It cannot be extended to uniform continuous laws, where individual points have mass zero.

### Problem 19. Add events whose overlap is nonempty but null

Under the uniform law on <span class="math-inline">[0,1]</span>, take <span class="math-inline">A=[0,1/2]</span> and <span class="math-inline">B=[1/2,1]</span>. They are not disjoint. Is adding their probabilities nonetheless correct?

**Solution.** Each interval has mass <span class="math-inline">1/2</span>. Their intersection is the singleton <span class="math-inline">{1/2}</span>, which is nonempty but has mass zero. Inclusion–exclusion therefore gives union probability <span class="math-inline">1/2+1/2−0=1</span>.

Disjointness is a sufficient set-theoretic condition for adding two event probabilities. The more general numerical condition is a zero-probability intersection. Do not reverse the implication: equality of the union probability and the sum does not force the intersection to be empty. If the model placed positive atomic mass at the shared endpoint, the subtraction would become essential.

### Problem 20. Equal event probabilities do not mean equal events

On four equally likely outcomes, let <span class="math-inline">A={1,2}</span> and <span class="math-inline">B={3,4}</span>. Evaluate both sides of <span class="math-inline">|P(A)−P(B)|≤P(A△B)</span>, then explain when the right side being zero is informative.

**Solution.** Both probabilities are <span class="math-inline">1/2</span>, so the left side is zero. The events are disjoint and their symmetric difference is the entire space, so the right side is one. Equal probabilities carry very little information about agreement of events.

Conversely, if <span class="math-inline">P(A△B)=0</span>, the two one-sided differences are null. They therefore have equal probabilities and agree outside a null set. They need not be literally equal: two continuous events can differ by one endpoint. The inequality follows by subtracting the two difference-region masses and using <span class="math-inline">|x−y|≤x+y</span> for nonnegative x and y.

### Problem 21. Find an increasing union without adding its overlap repeatedly

For a uniform point on <span class="math-inline">[0,1]</span>, let <span class="math-inline">A<sub>n</sub>=[0,1−1/n]</span>. Find the union and its probability. Explain why summing the individual probabilities fails.

**Solution.** The events increase. Every point less than one eventually belongs because an integer n can be chosen with <span class="math-inline">1/n≤1−x</span>. The endpoint one never belongs. Thus the union is <span class="math-inline">[0,1)</span>, whose mass is one. Continuity from below gives the same result from <span class="math-inline">P(A<sub>n</sub>)=1−1/n→1</span>.

These events are nested, not disjoint. Their probabilities cannot be added; that series diverges. To use countable additivity directly, split the union into the initial event and consecutive difference events. Those disjoint increments telescope to the limit of the original probabilities. This is why monotone continuity and countable additivity are compatible.

### Problem 22. A decreasing limit retains an atom

In the mixed law with atomic mass α at zero, let <span class="math-inline">A<sub>n</sub>=[0,1/n]</span>. Find each probability and the probability of the intersection. Compare with the purely uniform case.

**Solution.** Every interval includes the atom and has length <span class="math-inline">1/n</span>. Therefore <span class="math-inline">P(A<sub>n</sub>)=α+(1−α)/n</span>. The events decrease to <span class="math-inline">{0}</span>: zero belongs to all of them, while any positive point is excluded once n is sufficiently large. Continuity from above gives the limit α, exactly the atom's mass.

For <span class="math-inline">α=0</span>, the limit is zero although the intersection is nonempty. For <span class="math-inline">α=1</span>, every interval and its singleton intersection have mass one. The same sequence of sets exhibits different probabilities under different laws. Set geometry cannot determine probability without a specified measure.

### Problem 23. Bound all future failures using a summable tail

Failure events satisfy <span class="math-inline">P(A<sub>n</sub>)≤2<sup>−n−2</sup></span> for all <span class="math-inline">n≥1</span>. Bound the probability of any failure from step m onward, and determine an m making that bound at most 0.001. What follows about infinitely many failures?

**Solution.** Countable union bounding and a geometric tail give

<div class="formula-block">P(⋃<sub>n≥m</sub>A<sub>n</sub>)≤∑<sub>n≥m</sub>2<sup>−n−2</sup>=2<sup>−m−1</sup>.</div>

For m equal to 9, the bound is <span class="math-inline">1/1024≈0.0009765625</span>, at most 0.001. For m equal to 8 it is <span class="math-inline">1/512≈0.001953125</span>, so 9 is the smallest integer justified by this bound.

The tail union events decrease as m increases, and their probabilities tend to zero. Their intersection is the event of infinitely many failures. Continuity from above therefore makes that event null. This argument requires no independence. It gives an almost sure statement, rather than a claim that every mathematical outcome has only finitely many failures.

### Problem 24. Vanishing probabilities can still occur infinitely often

Partition <span class="math-inline">[0,1)</span> into half-open intervals of length <span class="math-inline">2⁻ᵏ</span> for each level <span class="math-inline">k=1,2,…</span>. Enumerate all cells at level 1, then all at level 2, and so on, using each cell as the next event. Under the uniform length law, find the limiting individual probabilities, the infinitely-often event, and the eventually-always event.

**Solution.** There are finitely many cells at each level. Hence an index tending to infinity eventually passes every fixed level, and its level tends to infinity. Each event at level k has probability <span class="math-inline">2⁻ᵏ</span>, so the individual event probabilities tend to zero.

Each point belongs to exactly one cell at every level, including dyadic boundary points because the cells are half-open. It therefore belongs to infinitely many enumerated events. The infinitely-often event is the whole sample space, with probability one. At every level there are also cells omitting that point; after any proposed starting index, a later level supplies such an omission. No point is in all events of a tail. The eventually-always event is empty, with probability zero.

At each level the sum of the probabilities of its cells is one, so the series of all event probabilities diverges. There is no contradiction with the summable-error theorem. The example shows exactly why a limit of individual probabilities cannot be substituted for the probability of a limsup event.

## 9. High-yield review and examination reasoning

This review compresses established conclusions, not their prerequisites or proofs. If a rule seems unfamiliar, return to the indicated argument in the lesson and reconstruct it. Every hypothesis below is part of the rule.

### 9.1 Modeling and event-language checklist

1. **Specify all three parts of the model.** A probability space consists of a sample space, a sigma-algebra of admissible events, and a normalized countably additive probability law. Naming outcomes alone does not assign their probabilities.
2. **Separate an outcome from its singleton event.** The point ω is an element of Ω; the set containing ω is a subset. Probability is evaluated on an admissible set, not automatically on the point itself.
3. **Make elementary outcomes mutually exclusive and collectively exhaustive.** Overlapping outcome descriptions double-count possibilities, while an omitted possibility invalidates normalization. Event descriptions may overlap; elementary outcome categories must not.
4. **Translate verbal quantifiers into sets before calculating.** “At least one” means union, “all” means intersection, “none” means the complement of a union, and “exactly one of two” means symmetric difference. Inclusive and exclusive alternatives differ precisely on their overlap.
5. **Treat equal likelihood as an assumption needing justification.** Favorable-count divided by total-count is valid in a finite uniform model. A list of equally short labels, equal cardinality of infinite sets, or an unspecified selection mechanism does not establish uniformity.
6. **Preserve probability under a change of reporting granularity.** A coarse event receives the sum of the masses of its preimages. Merging a different number of equally likely fine outcomes usually produces unequal coarse masses.
7. **Check measurability when the event domain is restricted.** A finite partition produces events that are unions of its atoms. With r nonempty atoms there are exactly <span class="math-inline">2<sup>r</sup></span> such events. A subset cutting through one atom need not be admissible.
8. **Check the law as well as the event family.** Nonnegative weights summing to one yield a law on a finite or countable power set. An event collection must independently satisfy closure under complements and countable unions. Neither check replaces the other.

### 9.2 Algebra, bounds, and feasibility checklist

9. **Subtract overlap when adding event probabilities.** The union formula is <span class="math-inline">P(A)+P(B)−P(A∩B)</span>. For exactly one, subtract the overlap twice. For A only, subtract it from A's marginal alone.
10. **Use the four membership regions to audit every two-event proposal.** Their masses are q, a minus q, b minus q, and one minus a minus b plus q. All must be nonnegative. This detects errors hidden by individually plausible numbers.
11. **Use both overlap bounds.** Feasibility is equivalent to <span class="math-inline">max(0,a+b−1)≤q≤min(a,b)</span>. These bounds are sharp because the four-region construction realizes every allowed q.
12. **Do not invent dependence information.** Marginals alone imply <span class="math-inline">max(a,b)≤P(A∪B)≤min(1,a+b)</span>. An intersection product requires independence, which is an additional condition covered later.
13. **Remember that disjointness and independence impose different restrictions.** Disjointness makes intersection empty. Independence specifies its probability as a product. Two disjoint positive-probability events cannot be independent; a zero-probability marginal is a boundary case.
14. **Audit more than pairwise constraints for three or more events.** Eight nonnegative membership masses govern three events. Pairwise overlap bounds do not guarantee a jointly valid model, as Problem 11 demonstrates.
15. **Alternate signs correctly in inclusion–exclusion.** Add single-event masses, subtract pairs, add triples, and continue. Pair intersections include higher-order overlaps; “exactly two” is not their raw sum.
16. **Use the union bound without assuming independence.** Finite and countable unions have probability at most the sum of member probabilities. Cap a numerical upper bound at one. Complementing it gives a lower bound for avoiding every bad event.
17. **Keep inequalities in the right direction.** Subset implies no larger probability. Complement reverses set inclusion. If an upper bound is complemented, the result is a lower bound. An upper bound on failure does not give an upper bound on success.
18. **Equality of probabilities is weaker than equality of events.** The symmetric-difference mass measures disagreement. A zero difference of marginal probabilities need not mean small disagreement, while a null symmetric difference implies equality up to a null set.

### 9.3 Countable, continuous, and limiting-event checklist

19. **Distinguish impossibility from probability zero.** The empty set always has zero probability, but a nonempty set may also be null. Probability one means almost sure; a proper subset may have probability one. In a finite model, strict positivity of every singleton restores the stronger converses.
20. **Never add an uncountable collection using the countable axiom.** Uniform interval points each have zero mass but their uncountable union has mass one. Countable unions of null events are null. The word “countable” changes the conclusion.
21. **Do not use an equal-mass law on the positive integers.** A positive common mass eventually violates the upper bound one, while a zero common mass violates countable normalization. Use a genuinely normalized nonuniform series instead.
22. **Use length or area only under the corresponding uniform measure.** Continuous uniform probability is normalized geometric measure, not a ratio of cardinalities. Boundaries are negligible under these models when they have zero length or area; an added atom can change this.
23. **Prove monotonicity of an event sequence before applying continuity.** Increasing events use their union; decreasing events use their intersection. Probability laws have finite total mass, making both forms valid. Arbitrary event sequences do not qualify.
24. **Distinguish set limits from numerical limits.** Infinitely often is the intersection of tail unions. Eventually always is the union of tail intersections. Their probabilities bound numerical liminf and limsup, but need not equal them.
25. **Use summability for the first Borel–Cantelli implication.** A finite sum of event probabilities makes infinitely many occurrences null. Independence is unnecessary for this direction. A divergent sum alone establishes no converse conclusion.
26. **Test boundary cases before trusting a derivation.** Examine zero or unit marginals, empty or full events, containment, disjointness, identical events, and atomic endpoints. A formula giving a negative probability or a value above one fails immediately.
27. **State the strength of a conclusion accurately.** A feasible abstract law proves consistency, not physical truth. A bound guarantees an interval, not a specific value. Almost sure behavior allows null exceptions. A result requiring independence cannot be applied to unspecified dependence.
28. **Solve in a reproducible order.** Write the sample space and law; translate the event; choose a partition, complement, bound, or limit theorem; check every hypothesis; compute; then validate the result against nonnegativity, normalization, and a simple extreme case.

### 9.4 Compact formula map

| Goal | Formula or construction | Required condition |
|---|---|---|
| Complement | <span class="math-inline">P(A<sup>c</sup>)=1−P(A)</span> | A is measurable. |
| Difference | <span class="math-inline">P(A∖B)=P(A)−P(A∩B)</span> | A and B are measurable. |
| Two-event union | <span class="math-inline">P(A∪B)=a+b−q</span> | q is the actual overlap mass. |
| Exactly one of two | <span class="math-inline">P(A△B)=a+b−2q</span> | The word “one” excludes overlap. |
| Feasible overlap | <span class="math-inline">max(0,a+b−1)≤q≤min(a,b)</span> | Marginals a and b lie in the unit interval. |
| Countable union bound | <span class="math-inline">P(⋃A<sub>n</sub>)≤∑P(A<sub>n</sub>)</span> | All events are measurable; the family is countable. |
| Finite uniform model | <span class="math-inline">P(A)=|A|/|Ω|</span> | A finite nonempty Ω has equal singleton masses. |
| Weighted countable model | <span class="math-inline">P(A)=∑<sub>n∈A</sub>p<sub>n</sub></span> | Nonnegative weights sum to one. |
| Increasing-event limit | <span class="math-inline">P(⋃A<sub>n</sub>)=lim P(A<sub>n</sub>)</span> | The events increase. |
| Decreasing-event limit | <span class="math-inline">P(⋂A<sub>n</sub>)=lim P(A<sub>n</sub>)</span> | The events decrease; this is a probability measure. |
| Infinitely many occurrences | <span class="math-inline">limsup A<sub>n</sub>=⋂<sub>m≥1</sub>⋃<sub>n≥m</sub>A<sub>n</sub></span> | Do not interchange this with a numerical limit. |

## 10. References and scope audit

### 10.1 Reviewed university materials used in this chapter

1. **MIT — John N. Tsitsiklis.** *6.041/6.431: Probabilistic Systems Analysis and Applied Probability*, Fall 2010, Lecture 1, pages 1–3. Used for experiment modeling, finite and continuous examples, and the extension from finite to countable additivity. [Official lecture PDF](https://ocw.mit.edu/courses/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/fee036e2e13527166fb7f8bcd0647844_MIT6_041F10_L01.pdf).
2. **Stanford — Lisa Yan, with lecture-note material based on Chris Piech's handout.** *CS109: Probability for Computer Scientists*, Spring 2020, Lecture Notes 3, April 10, pages 1–5. Used for event operations, finite axioms, inclusion–exclusion, and consistency of coarse and fine models. Its introductory axioms are supplemented here with explicit countable additivity. [Official lecture PDF](https://web.stanford.edu/class/archive/cs/cs109/cs109.1206/lectureNotes/LN03_probability.pdf).
3. **University of California, Berkeley — Will Fithian.** *Stat 210A: Theoretical Statistics*, “Measure Theory Basics,” August 24, 2023, the “Measures” section and its probability-space examples. Used for the event-domain distinction, sigma-algebras, and measures. The subsequent integration development is outside this chapter. [Official course notes](https://www.stat.berkeley.edu/~wfithian/courses/stat210a/measure-theory-basics.html).
4. **ETH Zurich — Vincent Tassion.** *Probability Theory*, Fall 2025 notes, updated December 27, 2025, Section 1.1, printed pages 8–10 (PDF pages 14–16), with the opening of Section 1.2 reviewed for context. Used for probability-space definitions, monotone continuity, and union bounds. Proofs are supplied explicitly here rather than relying on assumed measure-theory prerequisites. [Official course notes](https://metaphor.ethz.ch/x/2025/hs/401-3601-00L/main.pdf).
5. **University of Oxford — Elias Koutsoupias.** *Probability and Computing*, 2016–17, Lecture 2, “Introduction to probability,” and Lecture 6, “Union bound.” Used as an additional treatment of event algebra and avoiding bad events. The course warns that its informal lecture notes may contain errors; this chapter uses independently derived statements with their exact hypotheses. [Official lecture notes](https://www.cs.ox.ac.uk/people/elias.koutsoupias/pc2016-17/lectures.html); [course information](https://www.cs.ox.ac.uk/people/elias.koutsoupias/pc2016-17/index.html).

The source-selection record compares a documented accessible candidate pool. It distinguishes complete relevant-text review from metadata-only screening and failed access. It does not claim that every course ever offered worldwide was obtainable or reviewed. The main synthesis uses four distinct universities, with a fifth selected where it adds value. Explanations, diagrams, laboratory code, and problem statements in this chapter are independently authored; source attribution does not imply university endorsement.

### 10.2 Coverage and remaining boundaries

This chapter develops model specification, event algebra, sigma-algebras at an introductory level, probability axioms and their consequences, finite and countable weighted laws, uniform length and area examples, mixed laws, null events, sharp two-event bounds, inclusion–exclusion, monotone continuity, limiting events, and the summable-event implication. Every worked problem includes a full solution, and the final review preserves the assumptions needed for each rule.

Counting techniques, conditional probability, independence as a developed theory, Bayes' rule, random variables, distributions, expectation, and concentration receive their own subsequent chapters. Construction of Lebesgue measure, nonmeasurable-set proofs, and the independence-based converse Borel–Cantelli theorem are not assumed to have been taught here. The short introduction to the first Borel–Cantelli implication is an original proof extension of the axioms and continuity results, not a claim to have reproduced the entire ETH course.

Iranian entrance-examination archives remain reserved for the final month under the current study policy. This chapter therefore makes no claim that those archives have been audited against it. Mathematical derivations, exact finite-model checks, numerical examples, references, and rendered formulas have separate audit records. These checks support a rigorous chapter within its stated scope; they cannot guarantee flawless performance on every unseen question or certify literal universal coverage.
