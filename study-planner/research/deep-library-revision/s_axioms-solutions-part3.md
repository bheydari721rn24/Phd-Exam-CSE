## Q39

**Correct option: 1.** Interpret the pair data in the declared order: $P(A\cap B)=3/10$, $P(A\cap C)=2/10$, $P(B\cap C)=1/10$. The triple mass $t$ is included in every pair mass. Subtract it to obtain the pair-only cells; subtract the pair intersections from each marginal and add the triple back to obtain the single-only cells.

| Exact membership | Probability |
| --- | --- |
| $111$ | $t$ |
| $110$ | $3/10-t$ |
| $101$ | $2/10-t$ |
| $011$ | $1/10-t$ |
| $100$ | $1/10+t$ |
| $010$ | $1/10+t$ |
| $001$ | $1/10+t$ |
| $000$ | $1/10-t$ |

For example, first only is $6/10-3/10-2/10+t=1/10+t$. The outside mass follows from inclusion-exclusion: $1-(6/10+5/10+4/10-3/10-2/10-1/10+t)=1/10-t$. All cells must be nonnegative, yielding $0\le t\le1/10$; the other upper bounds $t\le2/10,3/10$ are weaker.

To prove sufficiency, use the eight membership strings as elementary outcomes and assign the listed masses. Their sum is one for every $t$, and their marginal and intersection sums recover all supplied numbers. At $t=0$ the triple is empty in mass; at $t=1/10$ both the second-and-third-only cell and the outside cell have zero mass. Both endpoints are admissible. Options two and three permit a negative $011$ or outside cell; option four discards feasible interior choices such as $t=1/20$. A range of possible triple probabilities represents genuine incompleteness of the supplied information, not an algebraic error.

## Q40

**Correct option: 1.** Solve for overlap from the given union: $q=2/5+1/2-7/10=1/5$. The complete atomic table is

| Both | First only | Second only | Neither |
| --- | --- | --- | --- |
| $1/5$ | $1/5$ | $3/10$ | $3/10$ |

Exactly one selects first only and second only, giving $1/5+3/10=1/2$. Independence is a separate check: the product of marginals is $(2/5)(1/2)=1/5=q$, so these two events are independent. In fact, first-only mass equals $(2/5)(1-1/2)=1/5$, and the outside mass equals $(1-2/5)(1-1/2)=3/10$, confirming the product partition.

Option two uses the inclusive union $7/10$, which additionally contains both. Option three gets the exclusive probability right but incorrectly labels dependence. Option four gives only the second-only or outside mass and incorrectly labels dependence. Nonempty overlap does not demonstrate dependence: independent events with positive marginals generally overlap. Zero overlap is a disjointness claim, while the correct independence test compares its mass with the product. An atomic probability table makes both distinctions explicit and checks the supplied union is feasible.

## Q41

**Correct option: 2.** Label the physical balls $R_1,R_2,R_3,B_1,B_2$. Under uniform sampling without replacement, each unordered two-ball subset has the same probability $1/\binom52=1/10$. There are three red-red pairs, six mixed pairs, and one blue-blue pair.

| Type | Detailed pair count | Meets at least one red? | Meets both red? |
| --- | ---: | --- | --- |
| Red-red | 3 | Yes | Yes |
| Red-blue | 6 | Yes | No |
| Blue-blue | 1 | No | No |

The conditioning event removes only $\{B_1,B_2\}$. Each of the nine retained detailed pairs has conditional mass $(1/10)/(9/10)=1/9$. Three qualify for the target, so the answer is $3/9=1/3$.

An ordered check starts with 20 equally likely ordered draws. Six are red-red, 12 mixed and two blue-blue; conditioning retains 18, giving $6/18=1/3$. The factor two cancels because both numerator and denominator use the same representation. Option one is the unconditional red-red probability $3/10$. Option three is a single-draw red fraction, and option four treats red-red and mixed categories as equally likely although they contain three and six detailed pairs. Conditioning must preserve the induced weights when outcomes are grouped.

## Q42

**Correct option: 2.** The two independent fair bits define four elementary outcomes of mass $1/4$. Their exact membership table is

| $X,Y$ | $A$ | $B$ | $C$ |
| --- | --- | --- | --- |
| $0,0$ | No | No | No |
| $0,1$ | No | Yes | Yes |
| $1,0$ | Yes | No | Yes |
| $1,1$ | Yes | Yes | No |

Each event occurs in two rows and has probability $1/2$. The intersections $A\cap B$, $A\cap C$, and $B\cap C$ occur in precisely one row apiece, so each has mass $1/4=(1/2)(1/2)$. Every pair is independent, disproving options three and four.

The triple occurs in no row: $A$ and $B$ force $(X,Y)=(1,1)$, whose XOR is zero. Thus its probability is zero, whereas mutual independence would require $(1/2)^3=1/8$. This disproves option one. Pairwise independence does not claim the entire event-membership vector contains three independent bits. Here knowing the first two bits determines the third parity bit. Two independent elementary variables can produce several derived events that are pairwise independent but jointly constrained. The finite table is a complete counterexample; no approximate simulation is needed.

## Q43

**Correct option: 1.** The sampling law is uniform on eight ordered three-toss sequences, because the fair tosses are independent. Group them by the reported head count:

| Reported count | Detailed preimages | Mass |
| --- | --- | --- |
| 0 | $TTT$ | $1/8$ |
| 1 | $HTT,THT,TTH$ | $3/8$ |
| 2 | $HHT,HTH,THH$ | $3/8$ |
| 3 | $HHH$ | $1/8$ |

The event $K\ge2$ selects the final two groups, giving $(3+1)/8=1/2$. But the four summary outcomes do not have equal mass: their preimage counts are $1,3,3,1$. Option two has the correct target number but asserts the false uniformity premise. Option three gets the probability wrong despite recognizing nonuniformity. Option four gets both claims wrong.

Counting two admitted summary values out of four also yields $1/2$ here, an accidental agreement caused by the complement symmetry of head and tail counts. Test another event: $P(K=1)=3/8$, whereas uniform summary counting would give $1/4$. A valid induced law sums detailed masses within each reporting-map fiber. It never reassigns equal probability merely because four different labels were retained. The diagram's converging arrows represent this sum, not independent transitions between the summary values.

## Q44

**Correct option: 1.** The singleton masses must total one. A geometric series starting at one gives

$$\sum_{k=1}^{\infty}3^{-k}=\frac{1/3}{1-1/3}=\frac12,$$

so $c/2=1$ and $c=2$. The included threshold four starts with mass $2/81$ and includes every later integer. Its total is

$$P(N\ge4)=2\sum_{k=4}^{\infty}3^{-k}=\frac{2/81}{1-1/3}=\frac1{27}.$$

A complement check sums the first three normalized masses: $2/3+2/9+2/27=26/27$. Their complement is exactly $1/27$. Option two leaves total mass $1/2$ by using $c=1$, so it fails normalization before the tail is even tested. Option three uses the proper normalizer but omits part of the tail and even misses the endpoint's factor two. Option four makes total mass $3/2$, impossible for a probability measure. The strict event $N>4$ instead has mass $1/81$. Distinguish that valid strict-tail number from the included-tail number in the question. For a law $c r^{-k}$ with $r>1$, the same normalization gives $c=r-1$ and the included tail is $r^{1-n}$.

## Q45

**Correct option: 1.** These draws are independent with replacement. Four possible labels for each of three ordered positions give $4^3=64$ equally likely detailed outcomes. Distinct labels have $4\cdot3\cdot2=24$ outcomes, so repetition has $64-24=40$, with mass $40/64=5/8$.

To compare the exact value with the bound, let $E_{12},E_{13},E_{23}$ denote the three pair-equality events. Each fixes equality in one pair and leaves the third label free, so it contains $4^2=16$ outcomes and has mass $1/4$. The union bound is consequently $3/4=48/64$.

| Pattern | Outcome count | Number of pair equalities |
| --- | ---: | ---: |
| All distinct | 24 | 0 |
| Exactly one repeated pair | $3\cdot4\cdot3=36$ | 1 |
| All equal | 4 | 3 |

The bound counts $36+3(4)=48$ pair occurrences, whereas the union counts $36+4=40$ outcomes. The excess eight is exactly the two redundant counts of each all-equal outcome. Inclusion-exclusion agrees: each pairwise intersection of equality events forces all three labels equal, so the correction is $3/4-3(1/16)+1/16=5/8$. Options two and three misuse the bound, and option four reports the all-distinct complement. The original archive's separate Q67 wording says without replacement while asking about repetition and offers no zero option; that inconsistent statement is not silently substituted for the explicit with-replacement model here.

## Q46

**Correct option: 2.** For five distinct keys in a uniform random permutation, position $i$ is the prefix minimum with probability $1/i$. The number of updates is the sum of those five record indicators, with the first certainly one. Exact linearity gives

$$E[Y]=1+\frac12+\frac13+\frac14+\frac15=\frac{60+30+20+15+12}{60}=\frac{137}{60}.$$

This expectation is about $2.2833$; a noninteger mean is allowed because it averages integer counts across permutations. An enumeration check counts assignments over all $5!=120$ orders: the sum must be $120(137/60)=274$. It is a check of this finite case, while the prefix symmetry argument establishes the result.

Option one gives $5/2$, an inaccurate shortcut. Option three's two is attained on some permutations but is not the mean. Option four counts every scan comparison or the descending-array maximum. Using $\ln5$ would supply neither the exact finite answer nor an accurate substitute at this small size. The expectation proof does not require indicator independence. If the first-key assignment were excluded from the update ledger, subtract one and obtain $77/60$; the specified infinity initialization makes that alteration invalid here.

## Q47

**Correct option: 2.** The three marginals are $1/2$ and all three pair intersections are $3/10$. Exact membership cells, not only marginal inequalities, determine feasibility:

| Membership type | Number of such cells | Mass per cell |
| --- | ---: | --- |
| All three | 1 | $t$ |
| Exactly two | 3 | $3/10-t$ |
| Exactly one | 3 | $t-1/10$ |
| None | 1 | $2/5-t$ |

For a specific single-only cell, subtract its two pair intersections from its marginal and restore the triple: $1/2-3/10-3/10+t=t-1/10$. The outside cell is $1-(3/2-9/10+t)=2/5-t$. Nonnegativity requires $t\ge1/10$ and $t\le3/10$; the outside requirement $t\le2/5$ is weaker.

Conversely, these eight masses sum to one and reproduce every marginal and pair intersection for each $t$ in $[1/10,3/10]$, establishing sufficiency. At $t=1/10$, all single-only cells have zero mass. At $t=3/10$, all pair-only cells have zero mass. Option one permits negative single-only cells below $1/10$, and option three permits negative pair-only cells above $3/10$. The isolated value $1/8$ in option four is feasible, but not required; it is the triple product for independent half-probability events, whose pair products would be $1/4$, inconsistent with the given $3/10$. A feasible triple value does not make the whole joint model independent.

## Q48

**Correct option: 4.** This distribution is a mixture of two laws: a point mass at zero with weight $1/4$, and the uniform interval law with weight $3/4$. For a measurable event $E$,

$$P(E)=\frac14\,1_{\{0\in E\}}+\frac34\lambda(E\cap[0,1]),$$

where $\lambda$ denotes interval length. The weights add to one, and each component is countably additive, so the mixture defines a valid probability law. For $E=[0,1/2]$, the point is included and the interval length is $1/2$, giving $1/4+(3/4)(1/2)=5/8$.

Option one keeps only the atom, option two keeps only the continuous contribution $3/8$, and option three treats the entire law as uniform. The continuous component assigns zero mass to every singleton, but the combined law has $P(\{0\})=1/4$. Therefore replacing the included endpoint zero by an excluded endpoint changes the answer: $P(0<X\le1/2)=3/8$. By contrast, excluding $1/2$ does not change it, since that endpoint has no atom. The cumulative probability jumps from zero to $1/4$ at zero and then increases linearly to one. The jump and line segment encode different parts of the measure, so an uncountable sample space alone does not justify assuming a continuous distribution.
