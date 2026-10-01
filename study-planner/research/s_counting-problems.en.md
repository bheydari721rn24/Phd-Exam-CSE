## 9. Fully worked problems and diagnostic counterexamples

These problems are original formulations developed for this chapter. They exercise the counting and independence methods taught in the four reviewed courses; they are not presented as verbatim university examination questions. The source register identifies the course examples that motivated particular methods. Solutions include the model, the calculation, and the reason a tempting alternative fails. Read the solutions as instruction before using the questions for independent practice.

### Problem 1. Codes with a forbidden leading symbol

**Question.** A code has four decimal digits. Its first digit cannot be zero. How many codes are possible if repetition is allowed? How many if all digits must be different?

**Solution.** Positions are named, so a code is an ordered sequence. With repetition there are nine choices for the first position and ten choices for each subsequent position. Every first choice has the same number of continuations. The product rule gives <span class="math-inline">9·10³=9000</span>.

Without repetition, select the first digit in nine ways. Nine digits remain for the second position, including zero; then eight and seven remain. The answer is <span class="math-inline">9·9·8·7=4536</span>. Using <span class="math-inline">9·8·7·6</span> would incorrectly exclude zero from the later positions. Using a combination would lose the positions. The leading restriction and the repetition restriction concern different choices and must be applied separately.

### Problem 2. A branch count that cannot use one constant product

**Question.** How many integer pairs satisfy <span class="math-inline">1≤x&lt;y≤6</span>? Explain why multiplying six choices by five choices is wrong.

**Solution.** Once x is fixed, there are <span class="math-inline">6−x</span> choices for y. The disjoint cases x equal to one through five therefore have counts five, four, three, two, and one. Their sum is 15. Choosing x equal to six has no continuation. There is no common second-stage count of five.

An alternative bijection maps each valid pair to its two-element subset. Every subset has exactly one increasing listing, so the answer is <span class="math-inline">C(6,2)=15</span>. Ordered pairs of distinct elements number 30; dividing by two works because each subset has exactly two ordered listings. The same answer from two models is a useful check, but the reason for division is the constant fiber, not a general permission to erase order.

### Problem 3. Two sample descriptions, one probability

**Question.** Draw three distinct objects uniformly without replacement from five marked and four unmarked objects. Find the probability of exactly two marked draws using both ordered and unordered outcomes.

**Solution.** The mechanism gives all <span class="math-inline">(9)<sub>3</sub>=504</span> ordered outcomes equal probability. Choose which two of the three positions are marked in three ways. Fill those positions with distinct marked objects in <span class="math-inline">(5)<sub>2</sub>=20</span> ways, then fill the remaining position with one of four unmarked objects. There are 240 favorable outcomes, giving <span class="math-inline">240/504=10/21</span>.

For unordered samples the denominator is <span class="math-inline">C(9,3)=84</span>, and the numerator is <span class="math-inline">C(5,2)C(4,1)=40</span>. Their ratio is again <span class="math-inline">10/21</span>. Every subset has six ordered preimages; numerator and denominator both lose that factor. Combining the ordered numerator with the unordered denominator would produce a value greater than one and expose a mismatched sample-space contract.

### Problem 4. Why uniform sequences do not give uniform multisets

**Question.** Make two independent uniform draws from the labels a, b, and c, with replacement. After discarding order, is each resulting multiset equally probable?

**Solution.** The nine sequences each have mass <span class="math-inline">1/9</span>. The multiset containing two a's has only the preimage aa, so its mass is <span class="math-inline">1/9</span>. The multiset containing a and b has preimages ab and ba, so its mass is <span class="math-inline">2/9</span>. The same distinction holds for the other repeated and distinct pairs.

There are six multisets, counted by <span class="math-inline">C(3+2−1,2)=6</span>, but their probabilities are three masses of <span class="math-inline">1/9</span> and three masses of <span class="math-inline">2/9</span>. They sum to one. A different experiment that chooses a multiset uniformly would assign each mass <span class="math-inline">1/6</span>. A count of descriptions alone cannot tell us which experiment was performed.

### Problem 5. Repeated letters and a constant quotient

**Question.** How many distinct words can be made from three A's, two B's, and one C?

**Solution.** Temporarily label the repeated copies. There are <span class="math-inline">6!=720</span> permutations of the six labeled objects. For every visible word, its three A copies can be labeled in <span class="math-inline">3!</span> ways and its two B copies in <span class="math-inline">2!</span> ways. This gives exactly 12 preimages for every word. The constant-fiber quotient is therefore <span class="math-inline">6!/(3!2!)=60</span>.

A direct check chooses the three A positions in <span class="math-inline">C(6,3)</span> ways and then the two B positions from the remaining three in <span class="math-inline">C(3,2)</span> ways. C fills the last position. The product is <span class="math-inline">20·3=60</span>. The factorial denominator corrects interchangeable copies; it does not make the six positions interchangeable.

### Problem 6. Named groups with equal sizes

**Question.** Assign ten distinct people to named groups A, B, and C of sizes four, three, and three. Count the assignments.

**Solution.** Choose A's four members, then B's three from the six remaining people; the rest belong to C. Thus the count is <span class="math-inline">C(10,4)C(6,3)=210·20=4200</span>. Equivalently it is <span class="math-inline">10!/(4!3!3!)</span>.

Although B and C have equal size, exchanging their memberships changes the assignment because the names are part of the outcome. Dividing by two would be wrong. If B and C were genuinely unnamed while A stayed distinguished, every allocation would have exactly two labeled versions and 2100 would be correct. The question's definition of an outcome decides which quotient is legitimate.

### Problem 7. Unnamed pairs

**Question.** Partition six distinct people into three unnamed pairs.

**Solution.** Begin with three named groups of size two. The count is <span class="math-inline">6!/(2!2!2!)=90</span>. Naming the same three pairs can be done in <span class="math-inline">3!=6</span> ways; every partition has exactly those six preimages. The required number is 15.

An independent construction pairs a fixed first person with one of five people. From the remaining four, take a fixed person and choose one of three partners. The last pair is forced. This gives <span class="math-inline">5·3=15</span>. Fixing which person to process next avoids accidentally counting different orders of choosing the pairs. For groups of unequal sizes, a blanket division by the factorial of the number of groups would not generally have the same interpretation.

### Problem 8. Circular symmetry with distinct labels

**Question.** Seat six distinct people around a circle. Rotations are regarded as the same arrangement. Then suppose reflected arrangements are also regarded as the same. Find both counts.

**Solution.** Fix one distinguished person as the reference position. The other five people can be placed clockwise in <span class="math-inline">5!=120</span> ways. Each circular arrangement appears once in this construction, so rotations have already been removed.

Reflection reverses the clockwise order. With six distinct labels, that reversed order cannot equal the original circular order: the two neighbors of the distinguished person would have to coincide. Each reflection class therefore has exactly two circular arrangements. The second answer is 60. With repeated labels, a reflection or rotation can leave some arrangements unchanged; the orbit sizes can differ. These distinct-label counts must not be carried over without a new symmetry analysis.

### Problem 9. A prescribed adjacent block

**Question.** Arrange seven distinct books in a row so that three specified books occupy consecutive positions, in any internal order.

**Solution.** Treat the three specified books as one block. There are now five distinct objects: that block and four other books. Their arrangements number <span class="math-inline">5!</span>. Inside the block, the three books have <span class="math-inline">3!</span> possible orders. The answer is <span class="math-inline">5!3!=720</span>.

Every permitted row has a unique block location and internal order, so the construction is bijective. We are not choosing among all possible triples of books; the triple is prescribed. Multiplying by <span class="math-inline">C(7,3)</span> would solve a different problem and count rows repeatedly when several triples happen to be adjacent.

### Problem 10. Separating specified objects by gaps

**Question.** Arrange seven distinct books so that no two of three specified books are adjacent.

**Solution.** Arrange the four other books first in <span class="math-inline">4!</span> ways. They create five gaps: before the row, three internal gaps, and after the row. Each selected gap may hold only one specified book, because two in the same gap would be adjacent. Choose three gaps in <span class="math-inline">C(5,3)</span> ways and assign the three distinct specified books to them in <span class="math-inline">3!</span> ways. The count is <span class="math-inline">4!C(5,3)3!=1440</span>.

Removing the specified books from any valid final row recovers the background order and the three chosen gaps. This proves uniqueness. The endpoint gaps are real choices; omitting them would undercount. If the specified books were indistinguishable, their internal assignment factor would disappear, but the background books could still be distinct.

### Problem 11. Nonadjacent ones in a fixed-weight binary string

**Question.** Choose uniformly among length-nine binary strings with exactly three ones. Find the probability that no two ones are adjacent.

**Solution.** The total count is <span class="math-inline">C(9,3)=84</span>. If the one positions are <span class="math-inline">i<sub>1</sub>&lt;i<sub>2</sub>&lt;i<sub>3</sub></span> with gaps of at least two, set <span class="math-inline">j<sub>r</sub>=i<sub>r</sub>−(r−1)</span>. The new positions are an arbitrary three-element subset of the seven positions from one through seven. The inverse adds back the offsets, so the count is <span class="math-inline">C(7,3)=35</span>. The probability is <span class="math-inline">35/84=5/12</span>.

Using denominator <span class="math-inline">2⁹</span> would instead model uniform selection among all binary strings. We were told the weight is exactly three. The transformation proves the numerator; the sampling law determines the denominator.

### Problem 12. Stars and bars with lower bounds

**Question.** Count integral solutions of <span class="math-inline">x<sub>1</sub>+x<sub>2</sub>+x<sub>3</sub>+x<sub>4</sub>=12</span> satisfying lower bounds two, one, zero, and three respectively.

**Solution.** Subtract the respective lower bounds. The four new variables are nonnegative and total <span class="math-inline">12−(2+1+0+3)=6</span>. Each original solution gives one new solution, and adding the bounds back is the inverse. Stars and bars counts these by <span class="math-inline">C(6+4−1,4−1)=C(9,3)=84</span>.

The bounds consume six units before any free distribution. Counting with total 12 would include invalid solutions. If the sum of lower bounds exceeded 12, there would be no solution; a factorial expression with a negative argument would not be an acceptable substitute for that case distinction.

### Problem 13. A total inequality requires a slack variable

**Question.** Count nonnegative integral triples whose sum is at most five.

**Solution.** Introduce <span class="math-inline">x<sub>4</sub>=5−(x<sub>1</sub>+x<sub>2</sub>+x<sub>3</sub>)</span>. It is nonnegative, and the four variables total five. Each original triple has exactly one slack value. Conversely every such four-variable solution returns a permitted triple. Stars and bars gives <span class="math-inline">C(5+4−1,4−1)=C(8,3)=56</span>.

Alternatively partition by the original total t. The disjoint counts are <span class="math-inline">C(t+2,2)</span> for t from zero through five; their sum is 56 by the hockey-stick identity. Counting only total exactly five gives 21 and misses all smaller totals. The slack variable converts the inequality into an equality without changing the number of outcomes.

### Problem 14. Upper bounds with overlapping violations

**Question.** Count integral four-tuples with total ten and every coordinate between zero and three.

**Solution.** Without upper bounds there are <span class="math-inline">C(13,3)=286</span> solutions. A specified violation means that coordinate is at least four. Subtract four from it; the remaining total is six and the count is <span class="math-inline">C(9,3)=84</span>. There are four choices of the violated coordinate.

Two specified violations consume eight units, leaving total two and <span class="math-inline">C(5,3)=10</span> solutions. There are six choices of the pair. Three violations would require at least 12 units and are impossible. Inclusion–exclusion gives

<div class="formula-block">286−4·84+6·10=10.</div>

A separate check replaces each coordinate by its deficit from three. The four deficits are nonnegative and total two; no deficit can exceed three when their total is two. Stars and bars again gives ten. Subtracting only the single violations would produce a negative number: overlapping invalid families require the intersection correction.

### Problem 15. Occupancy vectors have unequal multiplicities

**Question.** Four distinct objects choose independently and uniformly among three named bins. Find the probability of occupancy vector <span class="math-inline">(2,1,1)</span>. Compare with a uniform choice of nonnegative occupancy vectors totaling four.

**Solution.** Independent placements produce <span class="math-inline">3⁴=81</span> equally likely labeled assignments. Choose which two objects go to the first bin in six ways, then which of the remaining two goes to the second bin in two ways. The last object goes to the third bin. The 12 assignments give probability <span class="math-inline">12/81=4/27</span>.

There are <span class="math-inline">C(6,2)=15</span> possible vectors, so a different mechanism choosing a vector uniformly gives this vector probability <span class="math-inline">1/15</span>. The vectors do not have equal placement multiplicities. For example, <span class="math-inline">(4,0,0)</span> has just one labeled placement. Stars and bars counts possible vectors, while the multinomial factor counts placements inside each vector.

### Problem 16. Every bin must be occupied

**Question.** Four distinct objects are assigned independently and uniformly to three named bins. Find the probability that every bin is occupied.

**Solution.** Start with 81 assignments. A specified empty bin leaves two choices for each object, giving 16 assignments. There are three specified-empty-bin events. When two specified bins are empty, all objects go to the remaining bin, giving one assignment for each of three pairs. All three bins cannot be empty because four objects are placed. Inclusion–exclusion gives <span class="math-inline">81−3·16+3=36</span> favorable assignments, hence probability <span class="math-inline">36/81=4/9</span>.

Every allowed occupancy has shape two, one, one. There are three choices for the doubled bin and 12 placements for each shape, giving the same 36. Independence belongs to the four object choices. The three events that particular bins are occupied are not automatically independent.

### Problem 17. Exactly two occupied bins

**Question.** Under the mechanism of Problem 16, find the probability that exactly two bins are occupied.

**Solution.** Select the two occupied bins in three ways. All four objects must go to this pair, and both members of the pair must receive something. There are <span class="math-inline">2⁴−2=14</span> assignments onto that pair, after excluding the two assignments using just one bin. The resulting 42 assignments have probability <span class="math-inline">42/81=14/27</span>.

The chosen pair is uniquely determined by an assignment with exactly two occupied bins, so no additional quotient is required. Exactly one occupied bin has three assignments. The consistency check <span class="math-inline">3+42+36=81</span> partitions the entire sample space by the number of occupied bins.

### Problem 18. Hypergeometric sampling and its feasible support

**Question.** A population of 12 objects contains five marked objects. Choose an unordered four-object sample uniformly without replacement. Find the probability of exactly two marked objects and identify every feasible success count.

**Solution.** Select two of the five marked objects and two of the seven unmarked objects. The numerator is <span class="math-inline">C(5,2)C(7,2)=210</span>. There are <span class="math-inline">C(12,4)=495</span> total samples, so the probability is <span class="math-inline">14/33</span>.

The success count can be any integer from zero to four: neither population type constrains it more tightly here. In general its lower endpoint is <span class="math-inline">max(0,m−(N−K))</span> and its upper endpoint is <span class="math-inline">min(m,K)</span>. Sampling without replacement changes later conditional success chances. A binomial calculation with common success probability <span class="math-inline">5/12</span> assumes a different experiment.

### Problem 19. Binomial weights and a complement shortcut

**Question.** Five independent trials each succeed with probability one third. Find the probability of exactly two successes, then of at least one success.

**Solution.** A specified pattern with two successes and three failures has mass <span class="math-inline">(1/3)²(2/3)³=8/243</span>. There are ten choices of the two success positions. Those patterns are disjoint, so exactly two successes has probability <span class="math-inline">80/243</span>. Independence justifies the pattern product; the common trial probability makes its weight the same for all ten patterns.

For at least one success, count the complementary pattern of five failures. Its mass is <span class="math-inline">(2/3)⁵=32/243</span>, so the answer is <span class="math-inline">211/243</span>. Adding five success probabilities gives more than one because an outcome with several successes would be counted repeatedly. The complement avoids that overlap and all the intermediate binomial terms.

### Problem 20. Independent trials with different probabilities

**Question.** Three independent trials have success probabilities one half, one third, and one quarter. Find the probability of exactly one success.

**Solution.** Partition the desired event by the unique successful trial. Their three masses are

<div class="formula-block formula-steps"><div>(1/2)(2/3)(3/4)=1/4,</div><div>(1/2)(1/3)(3/4)=1/8,</div><div>(1/2)(2/3)(1/4)=1/12.</div></div>

Their sum is <span class="math-inline">11/24</span>. The events are disjoint, and independence justifies each product. Their weights differ, so multiplying one pattern's weight by three would be wrong. Replacing the probabilities by their average and applying a binomial formula does not preserve the joint law. For a larger heterogeneous family, the same method sums over success-position subsets; a dynamic program can accumulate those weights without treating them as identical.

### Problem 21. Exact birthday probability and bound directions

**Question.** Four labeled objects independently choose uniformly among ten labels. Find the chance of a collision and compare it with the two bounds in Section 6.

**Solution.** After the first choice, avoiding collisions requires nine, eight, and seven choices at the remaining stages. Thus the no-collision probability is <span class="math-inline">10·9·8·7/10⁴=63/125</span>. The collision probability is <span class="math-inline">62/125=0.496</span>.

The exponential lower bound on collision probability is <span class="math-inline">1−exp(−4·3/20)</span>, approximately 0.4512. The union upper bound is <span class="math-inline">C(4,2)/10=0.6</span>. The exact answer lies between them. Pairwise collision events overlap, so 0.6 is an upper bound rather than an exact sum. With 11 objects and ten labels the collision probability would instead be exactly one by pigeonhole.

### Problem 22. No fixed points and exactly specified counts

**Question.** Choose a permutation of five labels uniformly. Find the probabilities of no fixed points, exactly two fixed points, and exactly four fixed points.

**Solution.** Inclusion–exclusion gives

<div class="formula-block">D<sub>5</sub>=120−120+60−20+5−1=44.</div>

The first probability is <span class="math-inline">44/120=11/30</span>. For exactly two fixed points, choose their positions in ten ways and derange the remaining three labels. Their only derangements are the two three-cycles, so the count is 20 and the probability is <span class="math-inline">1/6</span>.

Exactly four fixed points is impossible: the unused label must occupy the remaining position, making all five fixed. Its count is also <span class="math-inline">C(5,4)D<sub>1</sub>=0</span>. “Choose which positions are fixed and freely permute the rest” would include permutations with extra fixed points and would answer “at least those positions fixed,” not “exactly two.”

### Problem 23. Independence, complements, and degeneracy

**Question.** Suppose <span class="math-inline">P(A)=0.6</span>, <span class="math-inline">P(B)=0.4</span>, and <span class="math-inline">P(A∩B)=0.24</span>. Determine independence and the other three binary-pattern masses. Could two disjoint events with these marginals be independent? When is an event independent of itself?

**Solution.** The joint mass equals <span class="math-inline">0.6·0.4</span>, so A and B are independent. Subtraction gives masses 0.36 for A only, 0.16 for B only, and 0.24 for neither. They are respectively <span class="math-inline">0.6·0.6</span>, <span class="math-inline">0.4·0.4</span>, and <span class="math-inline">0.4·0.6</span>, confirming complement preservation.

If the events were disjoint, their joint mass would be zero rather than 0.24, so they would be dependent. Self-independence requires <span class="math-inline">p=p²</span>; its only solutions in the unit interval are zero and one. Both degenerate cases are legitimate independence cases. A conditional ratio with a null denominator is unnecessary and undefined; the product definition settles the issue directly.

### Problem 24. Pairwise independent bits that determine one another

**Question.** Two independent fair bits X and Y generate Z as their exclusive-or. Prove pairwise independence, then disprove mutual independence of the one-events.

**Solution.** The possible triples are 000, 011, 101, and 110 with equal masses. Each coordinate is one at exactly two points, giving marginal one half. For X and Y the four binary pairs each occur once. For X and Z, and for Y and Z, the same is true. Every pair cell has mass one quarter, equal to the product of its two marginal cell masses. This verifies pair independence including occurrence and complement cases.

No listed triple is 111, so the all-one joint probability is zero. Its three-marginal product is one eighth. The missing triple condition disproves mutual independence. Observing two coordinates determines the third; knowing only one does not. This distinction explains how every two-coordinate test can miss a deterministic higher-order constraint.

### Problem 25. The triple condition alone also fails

**Question.** Consider binary triples with masses <span class="math-inline">P(111)=1/8</span>, <span class="math-inline">P(110)=3/8</span>, <span class="math-inline">P(001)=3/8</span>, and <span class="math-inline">P(000)=1/8</span>. All other points are null. Does the all-one triple factorization prove mutual independence?

**Solution.** The masses are nonnegative and total one. Each coordinate is marginally one half. The all-one mass is one eighth, matching the product of all three marginals. Nevertheless the first two bits are always equal. Their both-one probability is one half, whereas their marginal product is one quarter. Their pair condition fails.

The first and third one-events also have joint mass one eighth rather than one quarter. Thus this model satisfies the triple condition but not the required pair conditions. Together with Problem 24, it shows that neither checking only pairs nor checking only the largest intersection is enough. For three events, all three pairs and the triple must be checked.

### Problem 26. Complement patterns under mutual independence

**Question.** Three mutually independent events have probabilities 0.2, 0.5, and 0.7. Find the probability that the first and third occur but the second does not. Then find the chance that at least one occurs.

**Solution.** Mutual independence is preserved when any selected event is complemented. The specified pattern therefore has mass <span class="math-inline">0.2·(1−0.5)·0.7=0.07</span>. This uses a three-event condition, not merely the pair condition for the first and third events.

None occurring has mass <span class="math-inline">(1−0.2)(1−0.5)(1−0.7)=0.12</span>, so at least one occurs with probability 0.88. With only pairwise independence this three-complement product would be unjustified. In that case inclusion–exclusion would still be valid, but its triple-intersection term would require additional information.

### Problem 27. Disjoint trial groups and overlapping groups

**Question.** Five independent fair bits are generated. Let U mean at least one success in the first two, and V mean exactly one in the last three. Find their joint probability. Why can the same argument fail for overlapping groups?

**Solution.** U has probability <span class="math-inline">1−(1/2)²=3/4</span>. V has probability <span class="math-inline">C(3,1)(1/2)³=3/8</span>. Each event depends on a disjoint group of mutually independent bits, so their joint mass is <span class="math-inline">9/32</span>. Expanding the two events into binary patterns proves the product, rather than assuming that all summaries of independent trials are independent.

For a counterexample use three fair bits and the events “at least one success in positions 1 and 2” and “at least one success in positions 2 and 3.” Each marginal is three quarters. Their joint event holds if bit 2 is one, or if bit 2 is zero and both other bits are one. These disjoint cases have masses one half and one eighth, totaling five eighths. The marginal product is nine sixteenths. The shared bit creates dependence.

### Problem 28. Conditioning destroys independence

**Question.** Two independent fair bits are known to contain at least one one. Under this conditional law, are their one-events still independent?

**Solution.** The conditioning event excludes 00 and has probability three quarters. The three surviving points 01, 10, and 11 each had mass one quarter, so renormalization gives each conditional mass one third. The first bit is one in two surviving points, and so is the second. Both conditional marginals are two thirds.

Their conditional both-one probability is one third; the product of their conditional marginals is four ninths. These differ, so the events are dependent in the conditional law. The original independence statement remains true in the original four-point law. A conditioning event changes the probability measure, and independence must be tested again in that measure.

### Problem 29. A hidden mixture creates dependence

**Question.** Choose one of two coins with equal probability, with heads probabilities three quarters and one quarter. Given the chosen coin, toss twice independently. Find each heads marginal, both-heads probability, and the probability of heads on the second toss given heads on the first.

**Solution.** Partition by the hidden type. A heads marginal is <span class="math-inline">(1/2)(3/4)+(1/2)(1/4)=1/2</span>. Both heads has mass <span class="math-inline">(1/2)(3/4)²+(1/2)(1/4)²=5/16</span>. It exceeds the marginal product one quarter, so the hidden-type mixture is dependent.

Since the first-heads marginal is positive, the conditional probability is <span class="math-inline">(5/16)/(1/2)=5/8</span>. Seeing heads increases the plausibility of the heads-favored type. Given the type, the tosses are independent by construction; after averaging over the shared type they are not. The model explicitly distinguishes conditional independence from unconditional independence.

### Problem 30. Weighted hashing into bins

**Question.** Three distinct objects independently choose among three bins with probabilities 0.5, 0.3, and 0.2. Find the probabilities that all three bins are occupied, that the first bin is occupied, and that at least one of the first two bins is occupied.

**Solution.** With three objects and three bins, all occupied means exactly one object per bin. There are six assignments, each having mass <span class="math-inline">0.5·0.3·0.2=0.03</span>. Their total is 0.18. It is not the uniform-bin answer because assignment weights come from the given nonuniform law.

The first bin is empty exactly when each object avoids it, with mass <span class="math-inline">(1−0.5)³=0.125</span>; its occupied probability is 0.875. Both the first and second bins are empty exactly when every object chooses the third bin, with mass <span class="math-inline">0.2³=0.008</span>. The last requested probability is 0.992. A set of avoided bins has avoidance probability based on its total weight, not on its number of bins alone.

### Problem 31. A race with neutral trials

**Question.** Roll an independent fair die repeatedly. What is the probability that face 1 occurs before either face 2 or face 3?

**Solution.** A relevant trial is 1, 2, or 3. Faces 4, 5, and 6 are neutral, with total probability one half. The event that the first relevant roll is a 1 at position n has probability <span class="math-inline">(1/2)<sup>n−1</sup>(1/6)</span>. These stopping-position events are disjoint. Sum from n equal to one, or reindex with j equal to zero:

<div class="formula-block">(1/6)∑<sub>j=0</sub><sup>∞</sup>(1/2)ʲ=(1/6)·2=1/3.</div>

The probability of indefinitely neutral rolls is zero because <span class="math-inline">(1/2)ⁿ→0</span>. Starting the geometric series at one without shifting its exponent would omit the possibility that the very first roll wins. Conditioning on the first relevant face gives the same one-of-three answer, but the disjoint series makes the stopping mechanism explicit.

### Problem 32. A deterministic threshold before probability

**Question.** Place 17 objects in five bins in any way. Must a bin contain at least four objects? Must a bin contain at least five? What is the probability of a collision when six objects are assigned to five bins by any random mechanism?

**Solution.** If each bin held at most three, the total would be at most 15. Thus at least one bin must hold four or more objects. Five is not forced: the vector <span class="math-inline">(4,4,3,3,3)</span> totals 17 and has no coordinate at least five. The general threshold for forcing at least q in some bin is <span class="math-inline">N&gt;r(q−1)</span>.

Six objects cannot occupy five bins without a repeated bin. A collision occurs in every possible assignment, so its probability is one under any probability law supported on those assignments. No independence, uniformity, or limiting approximation is needed for this conclusion. Check feasibility before evaluating a complicated probability formula.

### Problem 33. A nested-selection identity

**Question.** For integers <span class="math-inline">0≤r≤k≤n</span>, prove <span class="math-inline">C(n,k)C(k,r)=C(n,r)C(n−r,k−r)</span> without using factorial cancellation.

**Solution.** Count pairs of nested subsets <span class="math-inline">R⊆K⊆[n]</span>, where R has size r and K size k. First choose K in <span class="math-inline">C(n,k)</span> ways, then R inside K in <span class="math-inline">C(k,r)</span> ways. This yields the left side.

Alternatively choose R first in <span class="math-inline">C(n,r)</span> ways. K must add <span class="math-inline">k−r</span> elements from the complement of R, which has size <span class="math-inline">n−r</span>. This gives the right side. Both constructions select exactly the same pair, with no overcounting. Empty or identical nested subsets remain valid at the endpoints. Combinatorial identities become easier to remember when the objects counted and the two construction orders are stated explicitly.

### Problem 34. Nonadjacent strings without fixing the weight

**Question.** Count all length-six binary strings with no adjacent ones. Solve by a recurrence and independently by partitioning according to the number of ones.

**Solution.** Let <span class="math-inline">f<sub>n</sub></span> count permitted length n strings. Those beginning with zero leave any permitted length <span class="math-inline">n−1</span> suffix. Those beginning with one, for <span class="math-inline">n≥2</span>, must next have zero and leave a permitted length <span class="math-inline">n−2</span> suffix. These disjoint cases give <span class="math-inline">f<sub>n</sub>=f<sub>n−1</sub>+f<sub>n−2</sub></span>, with <span class="math-inline">f<sub>0</sub>=1</span> for the empty string and <span class="math-inline">f<sub>1</sub>=2</span>. Successive values are 3, 5, 8, 13, and 21, so the answer is 21.

There can be zero, one, two, or three ones. The fixed-weight counts are <span class="math-inline">C(7,0)=1</span>, <span class="math-inline">C(6,1)=6</span>, <span class="math-inline">C(5,2)=10</span>, and <span class="math-inline">C(4,3)=4</span>. Their sum is 21. This connects the gap bijection to a dynamic counting algorithm and checks its base cases. It also separates a fixed-weight question from an all-weights question.

## 10. High-yield review, exam decisions, and boundary checks

### 10.1 A complete decision procedure

1. **State the experiment and the outcome.** Decide which objects are distinct, which positions or bins are named, whether order remains visible, and whether repetition or replacement is allowed. Two questions can use the same set of descriptions while assigning different probability laws to it.
2. **Establish the probability weights before dividing counts.** Use favorable over total only for a finite uniform sample space. Uniform draws do not imply uniform coarsened outcomes when different descriptions have different numbers of preimages.
3. **Test feasibility before counting.** Check total sizes, lower bounds, upper bounds, available distinct objects, and pigeonhole obstructions. An impossible event has probability zero even when a memorized formula is not defined for the supplied parameters.
4. **Choose a construction with a reversible description.** A bijection proves exactness. For a quotient, show every final outcome has the same number of labeled descriptions. For a sum, make the cases disjoint. For a product, show every partial choice has the stated number of continuations.
5. **Identify the simplest restriction mechanism.** Use blocks for required adjacency, gaps or transformed positions for separation, shifts for lower bounds, slack for a total inequality, and inclusion–exclusion for upper bounds or forbidden categories with overlap.
6. **Separate pattern counts from pattern weights.** In Bernoulli sampling, first select the success positions, then compute their probability using the actual independence and trial-probability assumptions. In weighted occupancy, use multinomial multiplicities with the appropriate weights.
7. **Name the independence claim precisely.** Determine whether it concerns two events, every pair, every finite subfamily, or a conditional law. A statement about independent object choices does not automatically apply to overlapping functions of those choices.
8. **Check a second route and the boundaries.** Use ordered and unordered counts, a complementary event, a recurrence, or a small enumeration when available. Verify probabilities are between zero and one and that a partition of cases sums to one.

### 10.2 Exact counting reference with hypotheses

| Task | Exact result | Required interpretation |
|---|---|---|
| Ordered k draws from n labels, repetition allowed | <span class="math-inline">nᵏ</span> | Positions are named; each position can choose any label. |
| Ordered k distinct labels | <span class="math-inline">(n)<sub>k</sub>=n!/(n−k)!</span> | No replacement; use zero when k exceeds n. |
| Unordered k distinct labels | <span class="math-inline">C(n,k)</span> | Every subset is one outcome. |
| Unordered k labels with repetition | <span class="math-inline">C(n+k−1,k)</span> | Each multiplicity vector is one outcome; n is positive. |
| Permutations with multiplicities totaling N | <span class="math-inline">N!/∏m<sub>i</sub>!</span> | Positions remain distinct; copies within each type do not. |
| Nonnegative integral r-tuples totaling N | <span class="math-inline">C(N+r−1,r−1)</span> | Coordinates are named; r is positive and N nonnegative. |
| Nonnegative integral r-tuples totaling at most N | <span class="math-inline">C(N+r,r)</span> | Add one uniquely determined slack variable. |
| Length n binary strings with k nonadjacent ones | <span class="math-inline">C(n−k+1,k)</span> | Treat infeasible positive k separately; the empty choice is valid. |
| Distinct-label circular arrangements | <span class="math-inline">(n−1)!</span> | Rotations are identified; reflections remain distinct. |
| Exactly k fixed points in a permutation | <span class="math-inline">C(n,k)D<sub>n−k</sub></span> | Derange the remainder; freely permuting it permits extra fixed points. |

These are counts, not probability formulas until a probability mechanism has been supplied. The expression for unordered repetition assumes at least one label; with no labels there is one empty selection and no positive-size selection. Nonadjacent strings require <span class="math-inline">k≤⌈n/2⌉</span> for positive k. For the empty string with k equal to zero, there is one outcome.

### 10.3 Independence reference with exact logical strength

- **Two-event independence means product factorization.** The condition is <span class="math-inline">P(A∩B)=P(A)P(B)</span>. When the conditioning event has positive mass, it is equivalent to the other event keeping its original probability after conditioning.
- **Disjointness is a different condition.** Positive-probability disjoint events are dependent. If at least one event is null, disjointness is compatible with independence. Probability-one events are also independent of every event.
- **Pairwise independence checks pairs only.** It cannot justify a triple product, an all-failures product, or independence of arbitrary multibit functions. The parity example supplies exact counterexamples with fair marginals.
- **Mutual independence checks every subfamily.** For three events, three pair equations and one triple equation are required. For a larger family, intermediate intersections cannot be skipped. A single largest-intersection equation is insufficient.
- **Complement preservation has the same scope as the starting claim.** Independent pairs remain independent after either event is complemented. A mutually independent family permits any binary pattern product. Complementing a pairwise independent family does not strengthen it to mutual independence.
- **Disjoint groups of mutually independent inputs can be summarized independently.** Prove this by expanding group events into disjoint patterns. If the input groups overlap or the inputs are merely pairwise independent, recheck the conclusion.
- **Conditioning changes the probability law.** It can introduce dependence by selecting outcomes or remove dependence by revealing a shared latent type. Neither conditional independence nor ordinary independence implies the other without additional assumptions.
- **Zero denominators are handled by the product definition.** A conditional ratio given a null event is undefined in elementary probability. It must not be replaced arbitrarily by zero or canceled through a chain calculation.

### 10.4 Common traps, their repairs, and boundary cases

**A factorial quotient needs an equal-fiber argument.** Dividing by <span class="math-inline">k!</span> correctly removes order from distinct k-subsets because every subset has exactly that many listings. Repeated-label multisets have differing listing counts; their induced probabilities are therefore unequal under uniform sequential sampling.

**Equal-size named groups still have names.** Divide for repeated group-size labels only when the groups are genuinely unnamed. Group membership is a set, so internal order is already removed by each group factorial.

**An upper bound is first violated at one more than the bound.** To forbid a coordinate greater than u, shift by <span class="math-inline">u+1</span> in its inclusion–exclusion violation term. A negative residual total contributes zero. Multiple violations may overlap and must be included with alternating signs.

**Replacement and equal probabilities are separate questions.** Uniform without-replacement sampling gives hypergeometric success counts. Independent trials with one common probability give binomial counts. Independent trials with differing probabilities require weighted subset sums. A hidden mixture can make identically distributed trials dependent.

**Independent placements do not imply independent occupied-bin events.** A single object cannot enter two bins, and occupancy constraints couple bin events. Use a complement, an exact weighted multinomial calculation, or inclusion–exclusion rather than multiplying their marginals without proof.

**The birthday expression has a finite domain.** Use the falling product when the number of draws does not exceed the number of labels. Beyond that threshold, no-collision probability is zero. The exponential expression is a bound or a declared approximation, not an exact replacement.

**Derangements concern every remaining position.** Exactly k fixed points needs a derangement on the other positions. Exactly one nonfixed position is impossible. The empty permutation contributes <span class="math-inline">D<sub>0</sub>=1</span>, which makes the all-fixed case correct.

**Infinite races need a stopping argument.** The first relevant-trial cases are disjoint, the neutral probability must be strictly below one, and the geometric series must start with exponent zero after reindexing. If relevant categories both have zero probability, the usual ratio is undefined.

**Empty products and boundary probabilities have meanings.** An empty selection and an empty placement have one construction. A zero-probability category with positive occupancy contributes zero mass; a zero exponent represents no such occurrence. These conventions follow from the mechanism rather than from arbitrary numerical cancellation.

### 10.5 How to use this chapter after the first reading

First explain the outcome contract for each problem without looking at its solution. Then reconstruct the decisive bijection, overlap correction, or independence test. Only after that calculate the numerical result. When an answer is wrong, identify whether the error concerns the sample space, the weighting law, the combinatorial construction, or the logical strength of independence; each error type requires a different repair.

The lesson and problems provide a rigorous foundation within the stated chapter scope. They do not certify performance on every unseen question. Advanced recurrence methods, general group actions, generating functions, full conditional-probability theory, and distributional limit methods have their own prerequisites and later chapters. Iranian entrance-exam papers remain reserved for the final-month guided work under the student's instruction.

## 11. References and source-use record

### Core reviewed courses

1. **Massachusetts Institute of Technology — John N. Tsitsiklis.** *6.041/6.431 Probabilistic Systems Analysis and Applied Probability*, Fall 2010. [Lecture 3: Independence](https://ocw.mit.edu/courses/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/b200b6217af1cd5dbea8c659ebbf046a_MIT6_041F10_L03.pdf), instructional pages 1–2; [Lecture 4: Counting](https://ocw.mit.edu/courses/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/f25004e3104e9bb7cf51ed0111ed7cf2_MIT6_041F10_L04.pdf), instructional pages 1–2. Used for the counting-to-probability contract, selection models, partitions, the product definition, complement independence, and hidden-mixture examples. The attribution page is separate from the instructional scope.
2. **Stanford University — Lisa Yan; foundational notes credited to Mehran Sahami and Chris Piech where stated.** *CS109: Probability for Computer Scientists*, Spring 2020. [Lecture Notes 01: Counting](https://web.stanford.edu/class/archive/cs/cs109/cs109.1206/lectureNotes/LN01_counting.pdf), pages 1–4; [Lecture Notes 02: Combinatorics](https://web.stanford.edu/class/archive/cs/cs109/cs109.1206/lectureNotes/LN02_combinatorics.pdf), pages 1–7; [Lecture Notes 05: Independence](https://web.stanford.edu/class/archive/cs/cs109/cs109.1206/lectureNotes/LN05_independence.pdf), pages 1–5. Used for staged counting, stars and bars, occupancy, binomial pattern weights, repeated races, and conditional selection. The source's final geometric-series sentence on Lecture Notes 05 page 3 has an indexing slip; Section 6.6 derives the corrected series explicitly. This chapter uses probability *mass*, rather than the source's occasional *density* wording for a binomial law.
3. **University of California, Berkeley — CS70 course staff.** *Discrete Mathematics and Probability Theory*, Summer 2019; course instructors James Hulett and Elizabeth Yang. [Official course archive](https://www.su19.eecs70.org/); [Note 12: Counting](https://www.su19.eecs70.org/static/notes/n12.pdf), pages 1–5; [Note 12.5: Other Counting Techniques and Combinatorial Proofs](https://www.su19.eecs70.org/static/notes/n12.5.pdf), pages 1–4; [Note 14: Conditional Probability](https://www.su19.eecs70.org/static/notes/n14.pdf), independence section on pages 6–11. Used for equal-fiber proofs, occupancy versus placements, combinatorial identities, independence subfamilies, pattern equivalence, and conditional-law distinctions. The PDF notes do not individually name an author; the instructors are identified as instructors, not asserted to be their individual authors.
4. **University of Oxford — Elias Koutsoupias.** *Probability and Computing*, 2016–2017. [Course and instructor](https://www.cs.ox.ac.uk/people/elias.koutsoupias/pc2016-17/index.html); [official written lectures](https://www.cs.ox.ac.uk/people/elias.koutsoupias/pc2016-17/lectures.html), Lecture 2 independence definitions and Lecture 18 pairwise independence and “Bits for free.” Used for the distinction between pairwise and mutual independence and the computational parity perspective. The chapter's continuous parity family and its proof are original extensions; no claim is made to have reviewed unrelated lectures in full.

### Selection and attribution limits

The accompanying source audit records a bounded candidate survey, selection reasons, accessible written sections, and excluded or inaccessible candidates. Four universities contribute genuinely reviewed instructional material. This is not a claim that every course worldwide has been inspected or that exactly four sources will suffice for every later chapter.

The lesson is an original synthesis, with original proofs, figures, finite models, and worked problem formulations. Related university examples are used to choose and cross-check teaching methods; this chapter does not reproduce the courses' complete copyrighted exercise banks. Accordingly, its problem bank is explicitly identified as original, and the linked courses remain the primary locations for their own complete materials. All references and explanatory source notes are in English.
