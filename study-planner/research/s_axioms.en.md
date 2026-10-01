# Sample Spaces, Events, and Probability Axioms

*Probability and Statistics · Chapter 1 · English review draft · 24 fully worked problems*

## 1. Scope, prerequisites, and source selection

Probability starts by specifying what can happen and which outcomes belong to the question being asked. A numerical answer is meaningful only after that model is fixed. This chapter builds the model from elementary outcomes through event algebra, admissible event families, probability axioms, exact identities, feasibility bounds, and countable-event limits. It includes finite weighted models, ordinary uniform interval and area models, and an interactive two-event model. Combinatorial counting techniques and independence are the next chapter's main subjects; conditional probability, Bayes' rule, random-variable distributions, and expectation have later boundaries. A few small finite enumerations appear here to make modeling precise.

Prerequisites are sets, complements, unions, intersections, disjoint partitions, geometric series, and elementary limits. Whenever an infinite sum or a limit is used, its role is explained. Full measure construction and integration theory are outside this chapter; introducing an event family does not require learning those entire subjects first.

The reviewed core texts are MIT 6.041/6.431 Lecture 1 by John Tsitsiklis; Stanford CS109 Lecture Notes 3 by Lisa Yan, based on Chris Piech's handout; Berkeley Stat 210A's *Measure Theory Basics* by Will Fithian; and ETH Zurich's *Probability Theory* by Vincent Tassion, Section 1.1. Oxford's *Probability and Computing* notes by Elias Koutsoupias provide a fifth written perspective on the union bound. They were selected for complementary chapter coverage after a bounded survey, not simply because four links were available. The source audit records the exact portions read, candidate exclusions, and limitations. All explanations, diagrams, and problem statements below are independently written; source-inspired reasoning types are attributed in the problem-bank introduction.

## 2. Constructing a sample space before assigning numbers

### 2.1 Experiment, outcome, and event

An **experiment** is the process being modeled: for example, rolling a marked die once, observing two ordered coin tosses, or measuring a service duration. A **sample space** <span class="math-inline">Ω</span> is a nonempty set whose elements describe the mutually exclusive, collectively exhaustive elementary outcomes of that process. One execution produces one element <span class="math-inline">ω∈Ω</span>. An **event** is an admissible subset <span class="math-inline">A⊆Ω</span>; it occurs exactly when the realized outcome belongs to that subset.

An outcome and a singleton event have different types: <span class="math-inline">ω</span> is an element, whereas <span class="math-inline">{ω}</span> is a set. The expression <span class="math-inline">P(ω)</span> is common shorthand for <span class="math-inline">P({ω})</span> when the singleton is measurable. This shorthand never turns the probability function into a function on arbitrary objects. The impossible event is <span class="math-inline">∅</span>; the event that some permitted outcome occurs is <span class="math-inline">Ω</span>. Whether another event has probability zero or one requires the probability law, not just its set description.

For two distinguishable coin tosses, use <span class="math-inline">Ω={HH,HT,TH,TT}</span>, where the first symbol records the first toss. “At least one head” is <span class="math-inline">{HH,HT,TH}</span>; “exactly one head” is <span class="math-inline">{HT,TH}</span>. The outcome description contains no fairness assumption. The four outcomes have equal probabilities only under an additional model, such as two independent fair tosses. Independence itself will be defined and studied in the next chapter; here, a uniform assignment can simply be stated as the model's probability law.

### 2.2 Translating language into event algebra

Take complements relative to the declared <span class="math-inline">Ω</span>. For events <span class="math-inline">A,B</span>, the following translations determine the set before any probability formula is used.

| Statement | Event |
| --- | --- |
| Both occur | <span class="math-inline">A∩B</span> |
| At least one occurs; inclusive “or” | <span class="math-inline">A∪B</span> |
| Neither occurs | <span class="math-inline">(A∪B)<sup>c</sup>=A<sup>c</sup>∩B<sup>c</sup></span> |
| Exactly one occurs | <span class="math-inline">A△B=(A∖B)∪(B∖A)</span> |
| The first occurs but the second does not | <span class="math-inline">A∖B=A∩B<sup>c</sup></span> |
| They do not both occur | <span class="math-inline">(A∩B)<sup>c</sup>=A<sup>c</sup>∪B<sup>c</sup></span> |
| At least one of a family occurs | <span class="math-inline">⋃<sub>i</sub>A<sub>i</sub></span> |
| Every event in a family occurs | <span class="math-inline">⋂<sub>i</sub>A<sub>i</sub></span> |

“Neither” and “not both” are different. On an outcome where only <span class="math-inline">A</span> occurs, “neither” is false but “not both” is true. “Mutually exclusive” means <span class="math-inline">A∩B=∅</span>; “exhaustive” means <span class="math-inline">A∪B=Ω</span>. Neither condition implies the other. A **partition** of a set is a family of nonempty, pairwise disjoint subsets whose union is that set. Partitions support exact addition because each outcome belongs to exactly one piece.

### 2.3 Granularity and the danger of assuming uniformity

Under a uniform four-outcome model for two coin tosses, record only the number of heads. The summary space is <span class="math-inline">S={0,1,2}</span>, but the masses are <span class="math-inline">1/4,1/2,1/4</span>, not <span class="math-inline">1/3</span> each. The summary value one merges two detailed outcomes. In general, if a description map is <span class="math-inline">g:Ω→S</span>, then a summary event <span class="math-inline">C⊆S</span> receives probability

<div class="formula-block">Q(C)=P(g<sup>−1</sup>(C)), where g<sup>−1</sup>(C)={ω∈Ω:g(ω)∈C}.</div>

This is called the **induced** probability law. Only summary events whose preimages belong to the original event family are assigned probabilities. In the finite full-power-set example this requirement is automatic; in a general space it is the measurability requirement on the reporting map. Preimages preserve complements and countable unions, and disjoint summary events have disjoint preimages. These facts transfer normalization and countable additivity to the induced law.

If every detailed point has mass <span class="math-inline">1/N</span>, the probability of a summary value is its number of detailed preimages divided by <span class="math-inline">N</span>. Summary values are equally likely exactly when those preimage sizes are equal. If two outcomes collapse to one summary value but an event distinguishes them, that event cannot be represented using the summary alone. The model must retain enough information for the question.

The process also matters. “Choose one of three devices uniformly” and “choose one of ten components uniformly, then report its device” need not give the same device probabilities. Similarly, unordered categories are not automatically equally likely simply because their names look symmetric. State the selection mechanism or the weights explicitly. A sequence tree lists possibilities and can preserve timing or stopping information, but its branch labels still require probabilities; the drawing does not generate a law by itself.

<figure class="logic-diagram"><svg viewBox="0 0 720 230" role="img" aria-label="Four equally weighted detailed coin outcomes map to three head-count categories of masses one quarter, one half, one quarter"><rect x="8" y="8" width="704" height="214" rx="12" fill="#f4f8fb" stroke="#b9cfdb"/><text x="35" y="38" font-size="18">Detailed outcomes: each has mass 1/4</text><text x="38" y="86" font-size="21">TT</text><text x="196" y="86" font-size="21">HT</text><text x="354" y="86" font-size="21">TH</text><text x="512" y="86" font-size="21">HH</text><g stroke="#587e97" stroke-width="2"><path d="M52 96 L90 144"/><path d="M210 96 L315 144"/><path d="M368 96 L315 144"/><path d="M526 96 L560 144"/></g><rect x="35" y="148" width="115" height="46" rx="6" fill="#d4e5ee"/><rect x="245" y="148" width="150" height="46" rx="6" fill="#c3dcca"/><rect x="502" y="148" width="115" height="46" rx="6" fill="#d4e5ee"/><text x="51" y="177" font-size="18">0 heads: 1/4</text><text x="264" y="177" font-size="18">1 head: 1/2</text><text x="516" y="177" font-size="18">2 heads: 1/4</text></svg><figcaption>A coarser description preserves probabilities by adding the masses of outcomes it merges. It does not preserve equal likelihood unless the merged groups have equal total mass.</figcaption></figure>

## 3. Which subsets are events?

### 3.1 The event family and its closure rules

A probability space is a triple <span class="math-inline">(Ω,𝓕,P)</span>. The set <span class="math-inline">Ω</span> describes outcomes; <span class="math-inline">𝓕</span> is a collection of subsets of <span class="math-inline">Ω</span>; and <span class="math-inline">P</span> assigns numbers to members of <span class="math-inline">𝓕</span>. Thus <span class="math-inline">A∈𝓕</span> and <span class="math-inline">A⊆Ω</span> are compatible statements at two different levels. The former says that <span class="math-inline">A</span> is an admissible event. The latter says it is made of outcomes.

The standard event family is a **sigma-algebra** (also called a sigma-field). It satisfies three conditions: <span class="math-inline">Ω∈𝓕</span>; if <span class="math-inline">A∈𝓕</span>, then <span class="math-inline">A<sup>c</sup>∈𝓕</span>; and if <span class="math-inline">A<sub>1</sub>,A<sub>2</sub>,…∈𝓕</span>, then <span class="math-inline">⋃<sub>n≥1</sub>A<sub>n</sub>∈𝓕</span>. These closure requirements ensure that “not,” “at least one,” and their combinations remain questions to which the model assigns probabilities. “Countable” includes a finite family padded with empty sets.

The empty set belongs to <span class="math-inline">𝓕</span> because it is the complement of <span class="math-inline">Ω</span>. Countable intersections also belong: by De Morgan's identity, <span class="math-inline">⋂<sub>n≥1</sub>A<sub>n</sub>=(⋃<sub>n≥1</sub>A<sub>n</sub><sup>c</sup>)<sup>c</sup></span>. Complements, countable unions, and one final complement establish membership step by step. Differences and symmetric differences are consequently measurable too. An arbitrary *uncountable* union is not guaranteed by this definition; countable closure cannot be silently strengthened.

### 3.2 Finite spaces, partitions, and information

For a finite or countable <span class="math-inline">Ω</span>, taking <span class="math-inline">𝓕=2<sup>Ω</sup></span>, the power set, is a convenient standard choice. It is not compulsory. If <span class="math-inline">Ω={1,2,3,4}</span> but the only recorded question is “does the outcome belong to <span class="math-inline">A={1,2}</span>?”, the minimal event family that contains this question is <span class="math-inline">{∅,A,A<sup>c</sup>,Ω}</span>. The event <span class="math-inline">{1}</span> is then unavailable: this observation cannot distinguish one from two.

A finite partition <span class="math-inline">C<sub>1</sub>,…,C<sub>r</sub></span> generates a sigma-algebra consisting of all unions of its cells. There are exactly <span class="math-inline">2<sup>r</sup></span> such unions because each nonempty cell is either selected or omitted, and distinct selections yield different sets. Complements omit precisely the selected cells; unions select every cell selected by at least one member. This proves closure directly. The cells are the indivisible **atoms** of this finite event family. They need not be singleton outcomes.

Assigning nonnegative cell masses <span class="math-inline">q<sub>1</sub>,…,q<sub>r</sub></span> with sum one then defines a probability law on this coarse family: add the masses of selected cells. It does not specify how probability is distributed among individual outcomes inside a multi-outcome cell. A finer law requires additional information. This distinction explains why partial marginal probabilities can leave many models possible even when all supplied numbers are valid.

### 3.3 Continuous spaces and ordinary measurable sets

On <span class="math-inline">[0,1]</span>, the standard Borel event family contains intervals and is closed under countable unions and complements. It therefore contains singletons, countable sets, and complements of countable sets. It is the smallest sigma-algebra containing the open sets relative to the interval. The familiar uniform law gives an interval its length. We use this established law here rather than construct it from scratch.

One should not claim that every subset of an uncountable space automatically has a probability under a chosen measure. There exist subsets for which a translation-invariant length assignment on all subsets cannot preserve the usual countably additive structure. Their construction is a separate measure-theory topic. For the ordinary intervals, regions, and countable operations used in this chapter, the events are measurable and the standard length/area model is sufficient. A set diagram alone still says nothing about density: its geometric area represents probability only when a uniform area law has actually been specified.

## 4. Axioms, exact identities, and feasibility

### 4.1 The countably additive probability law

On <span class="math-inline">(Ω,𝓕)</span>, a probability law <span class="math-inline">P:𝓕→ℝ</span> satisfies **nonnegativity**, <span class="math-inline">P(A)≥0</span> for each event; **normalization**, <span class="math-inline">P(Ω)=1</span>; and **countable additivity**: for pairwise disjoint events <span class="math-inline">A<sub>1</sub>,A<sub>2</sub>,…</span>,

<div class="formula-block"><math class="math-limits" display="block"><mrow><mi>P</mi><mo>(</mo><munder><mo>⋃</mo><mrow><mi>n</mi><mo>≥</mo><mn>1</mn></mrow></munder><msub><mi>A</mi><mi>n</mi></msub><mo>)</mo><mo>=</mo><munder><mo>∑</mo><mrow><mi>n</mi><mo>≥</mo><mn>1</mn></mrow></munder><mi>P</mi><mo>(</mo><msub><mi>A</mi><mi>n</mi></msub><mo>)</mo><mo>.</mo></mrow></math></div>

The infinite series is the limit of its nonnegative partial sums. It is not an axiom that probabilities add over overlapping events. Pairwise disjointness means every two different sets in the family have empty intersection; the weaker condition that the intersection of *all* the sets is empty is insufficient. Three sets can have an empty triple intersection while overlapping in pairs.

To derive <span class="math-inline">P(∅)=0</span>, apply countable additivity to the disjoint family <span class="math-inline">Ω,∅,∅,…</span>. Its union is <span class="math-inline">Ω</span>, so normalization gives <span class="math-inline">1=1+∑<sub>n≥1</sub>P(∅)</span>. Nonnegativity forces the repeated empty-set mass to be zero. Finite additivity now follows by padding any finite disjoint family with empty sets. This proof explains why the standard axioms include enough information for both finite and infinite calculations.

### 4.2 Complement, monotonicity, and the difference rule

Because <span class="math-inline">A</span> and <span class="math-inline">A<sup>c</sup></span> are disjoint and cover <span class="math-inline">Ω</span>, finite additivity gives <span class="math-inline">P(A)+P(A<sup>c</sup>)=1</span>. Therefore <span class="math-inline">P(A<sup>c</sup>)=1−P(A)</span>. Since both terms are nonnegative, every event probability lies in <span class="math-inline">[0,1]</span>. The upper bound follows from the axioms; it need not be independently assumed.

If <span class="math-inline">A⊆B</span>, split <span class="math-inline">B</span> into disjoint sets <span class="math-inline">A</span> and <span class="math-inline">B∖A</span>. Thus <span class="math-inline">P(B)=P(A)+P(B∖A)≥P(A)</span>, proving **monotonicity** and the exact difference rule <span class="math-inline">P(B∖A)=P(B)−P(A)</span> for nested events. For arbitrary events, the correct formula is <span class="math-inline">P(A∖B)=P(A)−P(A∩B)</span>. Replacing the intersection with all of <span class="math-inline">B</span> is valid only when the relevant containment holds or the discarded portion has zero mass.

A proper subset can have the same probability as the larger event. Equality in monotonicity means <span class="math-inline">P(B∖A)=0</span>, not necessarily <span class="math-inline">B∖A=∅</span>. This distinction recurs in almost-sure statements and continuous models.

### 4.3 Inclusion-exclusion from disjoint pieces

The sets <span class="math-inline">A∖B</span>, <span class="math-inline">A∩B</span>, and <span class="math-inline">B∖A</span> partition <span class="math-inline">A∪B</span> after empty cells are omitted. Adding <span class="math-inline">P(A)</span> and <span class="math-inline">P(B)</span> counts the overlap twice. Subtracting one copy yields

<div class="formula-block">P(A∪B)=P(A)+P(B)−P(A∩B).</div>

For three events, first add their individual masses, then subtract their three pairwise intersection masses, then add back the triple intersection. An outcome in all three was counted three times, subtracted three times, and must finally be counted once. An outcome in exactly two was counted twice and subtracted once. Thus

<div class="formula-block formula-steps"><div>P(A∪B∪C)=P(A)+P(B)+P(C)</div><div>−P(A∩B)−P(A∩C)−P(B∩C)</div><div>+P(A∩B∩C).</div></div>

For <span class="math-inline">m</span> events the general formula alternates over intersections of each possible size. Write <span class="math-inline">[m]={1,…,m}</span> and sum over nonempty index subsets <span class="math-inline">J⊆[m]</span>:

<div class="formula-block formula-steps"><div><math class="math-limits" display="block"><mrow><mi>P</mi><mo>(</mo><munderover><mo>⋃</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>m</mi></munderover><msub><mi>A</mi><mi>i</mi></msub><mo>)</mo></mrow></math></div><div><math class="math-limits" display="block"><mrow><mo>=</mo><munder><mo>∑</mo><mrow><mo>∅</mo><mo>≠</mo><mi>J</mi><mo>⊆</mo><mo>[</mo><mi>m</mi><mo>]</mo></mrow></munder><msup><mrow><mo>(</mo><mo>−</mo><mn>1</mn><mo>)</mo></mrow><mrow><mo>|</mo><mi>J</mi><mo>|</mo><mo>+</mo><mn>1</mn></mrow></msup><mi>P</mi><mo>(</mo><munder><mo>⋂</mo><mrow><mi>j</mi><mo>∈</mo><mi>J</mi></mrow></munder><msub><mi>A</mi><mi>j</mi></msub><mo>)</mo><mo>.</mo></mrow></math></div></div>

To verify the formula without assuming expectation theory, partition the sample space into the finitely many exact membership patterns of these events. On a cell belonging to exactly <span class="math-inline">r≥1</span> events, its coefficient on the right is <span class="math-inline">∑<sub>k=1</sub><sup>r</sup>(−1)<sup>k+1</sup>C(r,k)=1</span>, by expanding <span class="math-inline">(1−1)<sup>r</sup>=0</span>. A cell belonging to none has coefficient zero. The weighted sum of these cell coefficients therefore equals the union's mass. The formula is finite; an unrestricted infinite alternating inclusion-exclusion expression requires extra convergence conditions and is not asserted here.

### 4.4 Union bounds through disjointification

For events that may overlap, remove everything already included: let <span class="math-inline">D<sub>1</sub>=A<sub>1</sub></span> and <span class="math-inline">D<sub>n</sub>=A<sub>n</sub>∖⋃<sub>k&lt;n</sub>A<sub>k</sub></span>. These events are pairwise disjoint, their union equals the original union, and <span class="math-inline">D<sub>n</sub>⊆A<sub>n</sub></span>. Countable additivity and monotonicity now give the **union bound**:

<div class="formula-block"><math class="math-limits" display="block"><mrow><mi>P</mi><mo>(</mo><munder><mo>⋃</mo><mrow><mi>n</mi><mo>≥</mo><mn>1</mn></mrow></munder><msub><mi>A</mi><mi>n</mi></msub><mo>)</mo><mo>≤</mo><munder><mo>∑</mo><mrow><mi>n</mi><mo>≥</mo><mn>1</mn></mrow></munder><mi>P</mi><mo>(</mo><msub><mi>A</mi><mi>n</mi></msub><mo>)</mo><mo>.</mo></mrow></math></div>

No independence assumption is needed. A bound exceeding one remains algebraically true but can be improved to one and may provide little information. Applied to complements, the finite union bound gives <span class="math-inline">P(⋂<sub>i=1</sub><sup>m</sup>A<sub>i</sub>)≥1−∑<sub>i=1</sub><sup>m</sup>P(A<sub>i</sub><sup>c</sup>)</span>; combine this with zero if the right side is negative. If the sum of the probabilities of all bad events is strictly below one, their union has probability below one. Some outcome consequently avoids every bad event. This existence argument does not require constructing such an outcome.

For two events, equality <span class="math-inline">P(A∪B)=P(A)+P(B)</span> holds precisely when <span class="math-inline">P(A∩B)=0</span>. Empty intersection is sufficient but not necessary. For a finite or countable family, pairwise zero-mass intersections likewise suffice because the overlaps removed during disjointification lie in countable unions of null events.

### 4.5 Four atomic masses and sharp feasibility bounds

Let <span class="math-inline">a=P(A)</span>, <span class="math-inline">b=P(B)</span>, and <span class="math-inline">q=P(A∩B)</span>. The four membership regions have masses

| Region | Mass |
| --- | --- |
| Both | <span class="math-inline">q</span> |
| First only | <span class="math-inline">a−q</span> |
| Second only | <span class="math-inline">b−q</span> |
| Neither | <span class="math-inline">1−a−b+q</span> |

They sum to one. Nonnegativity of each region is equivalent, for <span class="math-inline">a,b∈[0,1]</span>, to the **Fréchet bounds**

<div class="formula-block">max(0,a+b−1) ≤ q ≤ min(a,b).</div>

These bounds are necessary *and sufficient*. For any <span class="math-inline">q</span> in this interval, take four labelled outcomes representing the regions and assign the four listed masses. Their nonnegativity and unit total define a valid probability law. This explicit construction proves sharpness and prevents merely guessing whether supplied marginal numbers can coexist. It concerns consistency of an abstract two-event model; a specified physical mechanism may impose additional restrictions.

By substituting the permissible overlap interval into inclusion-exclusion, the union satisfies <span class="math-inline">max(a,b)≤P(A∪B)≤min(1,a+b)</span>. Exactly one has probability <span class="math-inline">P(A△B)=a+b−2q</span>. It therefore obeys <span class="math-inline">|a−b|≤P(A△B)≤min(a+b,2−a−b)</span>. Another useful stability inequality follows by writing <span class="math-inline">P(A)−P(B)=P(A∖B)−P(B∖A)</span> and applying the real-number inequality <span class="math-inline">|u−v|≤u+v</span> for nonnegative masses:

<div class="formula-block">|P(A)−P(B)| ≤ P(A△B).</div>

If the two events disagree only on a null set, their probabilities are equal. The reverse is false: equal probabilities do not imply that events coincide, even almost surely.

## 5. Constructing valid laws on different spaces

### 5.1 Finite and countable mass assignments

On finite <span class="math-inline">Ω={ω<sub>1</sub>,…,ω<sub>N</sub>}</span> with its full power set, assigning masses <span class="math-inline">p<sub>i</sub>≥0</span> whose sum is one defines <span class="math-inline">P(A)=∑<sub>ω<sub>i</sub>∈A</sub>p<sub>i</sub></span>. Normalization is immediate; disjoint events select disjoint indices, so additivity follows. Conversely, the singleton events partition the finite space, forcing any probability law to have exactly this representation. Negative mass cannot be repaired by arranging other positive masses to sum to one.

When all masses are equal, normalization gives <span class="math-inline">p<sub>i</sub>=1/N</span> and <span class="math-inline">P(A)=|A|/N</span>. This count ratio is a theorem for a finite **uniform** law. A “random” choice without an explicit mechanism does not prove uniformity. The phrase should be clarified by a symmetry assumption, a stated sampling rule, or supplied weights.

On <span class="math-inline">Ω={1,2,…}</span>, a nonnegative sequence with <span class="math-inline">∑<sub>n≥1</sub>p<sub>n</sub>=1</span> similarly defines a law on all subsets by summing their singleton masses. Countable additivity follows from regrouping a nonnegative series over disjoint index sets. Unlike a conditionally convergent signed series, such a series has no order-dependent sum. As an example, <span class="math-inline">p<sub>n</sub>=1/[n(n+1)]</span> works because <span class="math-inline">1/[n(n+1)]=1/n−1/(n+1)</span> and its first <span class="math-inline">m</span> terms sum to <span class="math-inline">1−1/(m+1)→1</span>.

There is no uniform countably additive probability law on the positive integers that gives each singleton the same mass. If that mass is <span class="math-inline">c&gt;0</span>, sufficiently many points have total mass <span class="math-inline">mc&gt;1</span>; if it is zero, countable additivity makes the entire space have mass zero. Both possibilities contradict normalization. An “equal chance of any positive integer” is therefore an invalid assumption in this standard model.

### 5.2 Uniform length and area

For a uniform choice on <span class="math-inline">[u,v]</span> with <span class="math-inline">u&lt;v</span>, ordinary subintervals have probability equal to their length divided by <span class="math-inline">v−u</span>. A singleton has probability zero: it is contained in intervals of arbitrarily small length, so monotonicity bounds its mass by quantities approaching zero. Thus open or closed endpoints do not alter an interval's probability under this law. They still alter the event as a set.

For a uniform point in the unit square, probability is area because the total area is one. The event <span class="math-inline">x+y≤t</span> for <span class="math-inline">0≤t≤1</span> is a right triangle with legs <span class="math-inline">t</span>, giving probability <span class="math-inline">t²/2</span>. For <span class="math-inline">1≤t≤2</span>, its complement is a right triangle near <span class="math-inline">(1,1)</span> with legs <span class="math-inline">2−t</span>, giving probability <span class="math-inline">1−(2−t)²/2</span>. Thresholds below zero have probability zero; thresholds at least two have probability one. No count ratio between infinite cardinalities is used.

### 5.3 Null events, almost sure events, and mixed laws

The implication <span class="math-inline">A=∅⇒P(A)=0</span> is always true; its converse is not. A specified point in a uniform interval is a nonempty event of probability zero. Similarly, <span class="math-inline">P(A)=1</span> means **almost sure**, not necessarily <span class="math-inline">A=Ω</span>. In a uniform <span class="math-inline">[0,1]</span> model, <span class="math-inline">(0,1]</span> is a proper subset with probability one. In a finite model where every singleton has strictly positive mass, null events are empty; allowing zero-mass singleton outcomes removes that implication even in a finite space.

A countable union of null events is null by the union bound. In particular, the rational points in <span class="math-inline">[0,1]</span> have probability zero under a uniform law, and an irrational outcome has probability one. An uncountable union of null singletons can instead be the whole interval of probability one. Countable additivity says nothing about an uncountable sum of singleton masses.

Zero mass for every singleton is also not universal for an uncountable sample space. On <span class="math-inline">[0,1]</span>, put mass <span class="math-inline">α∈[0,1]</span> at zero and spread the remaining <span class="math-inline">1−α</span> uniformly over the interval. For a Borel event, define <span class="math-inline">P(A)=α·1<sub>{0∈A}</sub>+(1−α)λ(A)</span>, where <span class="math-inline">λ</span> is the unit-interval length law. This is a convex combination of two probability measures, so normalization and countable additivity hold term by term. The point zero now has mass <span class="math-inline">α</span>. The sample space alone does not tell us whether a law is discrete, continuous, or mixed.

## 6. Countable event sequences and their limits

### 6.1 Continuity from below

Suppose <span class="math-inline">A<sub>1</sub>⊆A<sub>2</sub>⊆⋯</span>. Define disjoint increments <span class="math-inline">D<sub>1</sub>=A<sub>1</sub></span> and <span class="math-inline">D<sub>n</sub>=A<sub>n</sub>∖A<sub>n−1</sub></span>. Their first <span class="math-inline">m</span> members partition <span class="math-inline">A<sub>m</sub></span>, and all their members cover <span class="math-inline">⋃<sub>n≥1</sub>A<sub>n</sub></span>. Consequently,

<div class="formula-block formula-steps"><div>P(A<sub>m</sub>)=∑<sub>n=1</sub><sup>m</sup>P(D<sub>n</sub>),</div><div>P(⋃<sub>n≥1</sub>A<sub>n</sub>)=lim<sub>m→∞</sub>P(A<sub>m</sub>).</div></div>

The second equality is the defining limit of a nonnegative series together with countable additivity. It is called **continuity from below**. It is continuity along increasing events, not continuity of an arbitrary set-valued function. For uniform <span class="math-inline">[0,1]</span>, the events <span class="math-inline">[0,1−1/n]</span> increase to <span class="math-inline">[0,1)</span> and their probabilities approach one. The union remains a proper subset of the original interval.

### 6.2 Continuity from above

If <span class="math-inline">A<sub>1</sub>⊇A<sub>2</sub>⊇⋯</span>, their complements increase. Apply continuity from below to those complements and use De Morgan's identity and the complement rule:

<div class="formula-block formula-steps"><div>P(⋂<sub>n≥1</sub>A<sub>n</sub>)</div><div>=1−P(⋃<sub>n≥1</sub>A<sub>n</sub><sup>c</sup>)</div><div>=1−lim<sub>n→∞</sub>P(A<sub>n</sub><sup>c</sup>)</div><div>=lim<sub>n→∞</sub>P(A<sub>n</sub>).</div></div>

The total measure is finite because it is a probability law, so the subtraction from one is valid. For general measures with infinite total mass, continuity from above requires an additional finite-mass condition and cannot be transferred automatically. In uniform <span class="math-inline">[0,1]</span>, <span class="math-inline">[0,1/n]</span> decreases to <span class="math-inline">{0}</span>. Its probabilities approach zero while its limiting event is nonempty.

### 6.3 Infinitely often versus eventually always

An arbitrary sequence need not have a single monotone set limit. Two useful events remain well-defined:

<div class="formula-block formula-steps"><div>limsup A<sub>n</sub>=⋂<sub>m≥1</sub>⋃<sub>n≥m</sub>A<sub>n</sub> (infinitely often),</div><div>liminf A<sub>n</sub>=⋃<sub>m≥1</sub>⋂<sub>n≥m</sub>A<sub>n</sub> (eventually always).</div></div>

An outcome belongs to the first if every tail contains at least one occurrence; it belongs to the second if some tail contains only occurrences. These definitions use only countable unions and intersections, so both are measurable. “Eventually always” implies “infinitely often,” hence <span class="math-inline">liminf A<sub>n</sub>⊆limsup A<sub>n</sub></span>.

For a detailed proof, write <span class="math-inline">B<sub>m</sub>=⋂<sub>n≥m</sub>A<sub>n</sub></span> and <span class="math-inline">C<sub>m</sub>=⋃<sub>n≥m</sub>A<sub>n</sub></span>. The first sequence increases and the second decreases. For every <span class="math-inline">n≥m</span>, inclusion gives <span class="math-inline">P(B<sub>m</sub>)≤P(A<sub>n</sub>)≤P(C<sub>m</sub>)</span>. Therefore the first quantity is at most the infimum of the numerical tail, while the last is at least its supremum. Let m tend to infinity. Monotone continuity identifies the limits of the event probabilities as the probabilities of the liminf and limsup events. The definitions of numerical liminf and limsup identify the limits of the tail infima and suprema. This proves

<div class="formula-block formula-steps"><div>P(liminf A<sub>n</sub>)≤liminf P(A<sub>n</sub>)</div><div>≤limsup P(A<sub>n</sub>)≤P(limsup A<sub>n</sub>).</div></div>

These are inequalities, not unrestricted equalities. Even <span class="math-inline">P(A<sub>n</sub>)→0</span> does not force the probability of infinitely many occurrences to be zero. At successive levels, enumerate every half-open dyadic cell partitioning <span class="math-inline">[0,1)</span>. At level <span class="math-inline">k</span>, each cell has mass <span class="math-inline">2<sup>−k</sup></span>; those masses tend to zero as the cells are enumerated. Yet every point lies in one cell at every level and hence belongs to infinitely many of the events. The limsup is the entire interval. This counterexample rules out a tempting but invalid limit interchange.

### 6.4 A summable-error consequence

Suppose instead that <span class="math-inline">∑<sub>n≥1</sub>P(A<sub>n</sub>)&lt;∞</span>. The union bound gives <span class="math-inline">P(⋃<sub>n≥m</sub>A<sub>n</sub>)≤∑<sub>n≥m</sub>P(A<sub>n</sub>)</span>. The tail of a convergent nonnegative series tends to zero. The tail unions decrease to the infinitely-often event, so continuity from above yields <span class="math-inline">P(limsup A<sub>n</sub>)=0</span>. This is the first Borel–Cantelli implication, derived here directly from the axioms. It requires no independence. Divergence of the sum does not reverse the conclusion: taking every event to be the same event of probability <span class="math-inline">1/2</span> gives a divergent sum but an infinitely-often probability of only <span class="math-inline">1/2</span>. Further converse results need additional hypotheses and belong to later probability study.
