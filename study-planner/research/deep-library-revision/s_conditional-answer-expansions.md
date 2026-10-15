### SC01

**Build the conditional measure explicitly.** Label the outcomes $1,2,3,4$ and write their original probabilities as their weights divided by ten. The information event $B=\{1,2\}$ has probability $(1+2)/10=3/10$. The conditional measure assigns zero to outcomes3and4 and divides each retained original probability by $3/10$:

$$Q(1)=\frac{1/10}{3/10}=\frac13,\qquad Q(2)=\frac{2/10}{3/10}=\frac23.$$

Only outcome1also belongs to $A$, so its conditional weight is the answer. For the reverse direction retain outcomes1and3instead, with total weight four. The same target atom now has fraction one quarter. As an independent check, multiplying either conditional by its own information probability must recover the same joint mass one tenth. This check would immediately expose using the wrong denominator.

### SC02

**Construct a normalized joint table before testing independence.** The mass in $B$ is $2/5$ and its target fraction is $3/4$, giving $P(A\cap B)=3/10$. The remaining mass within $B$ is $1/10$. The mass outside $B$ is $3/5$; its target fraction is $1/6$, giving $P(A\cap B^c)=1/10$ and leaving $1/2$ outside both.

The two target cells sum to $2/5$. Multiplying the marginals gives $4/25$, which differs from the intersection $3/10$ by $7/50>0$. The determinant check gives the same difference: $(3/10)(1/2)-(1/10)(1/10)=7/50$. Thus the reconstructed table is valid and positively associated, rather than independent. Equal marginal probabilities do not force its internal cells to factor.

### SC03

**Expose the contradiction as a negative cell.** The information mass is $3/5$, so its stipulated one-half target fraction demands intersection mass $3/10$. But the target's entire marginal is only $1/5=2/10$. Completing the four-cell table would require

$$P(A\cap B^c)=P(A)-P(A\cap B)=\frac{2}{10}-\frac{3}{10}=-\frac1{10}.$$

A probability measure cannot assign negative mass to an event. No placement of the unspecified outcomes can repair that contradiction, since the intersection is a subset of $A$. A formal reverse ratio would be $(3/10)/(1/5)=3/2$, outside the unit interval; this is another symptom of the inconsistent premises, not a permissible answer to the original probability question.

### SC04

**Derive attainability as well as bounds.** Write the intersection as $x$. The target-only, information-only and neither cells are $7/10-x$, $3/5-x$ and $x-3/10$. Their nonnegativity requires $3/10\le x\le3/5$. The information denominator is fixed and positive, so division preserves order and gives $1/2\le P(A\mid B)\le1$.

At the lower bound all mass lies in the union, with neither cell zero. At the upper bound the information-only cell is zero, so the information event implies the target almost surely. The displayed endpoint tables in the verification below are nonnegative and sum to one. Convexly mixing those endpoint tables preserves both marginals and realizes every intermediate intersection, proving the entire interval is feasible, not merely its endpoints.

### SC05

**Keep the unknown population weight visible.** Let $b=P(B)$. The two disjoint pieces of the target have masses $4b/5$ and $(1-b)/5$. Their sum must equal one half, so

$$\frac12=\frac{4b}{5}+\frac{1-b}{5}=\frac15+\frac{3b}{5},\qquad b=\frac12.$$

The common intersection is then $2/5$. Reversing the conditional divides that joint mass by the target's marginal one half, giving $4/5$. The solution is identifiable because the two supplied stratum rates differ. If they had both equaled one half, the same target marginal would have been compatible with every positive stratum weight; division by their rate difference would then be invalid. The reconstructed positive cells below verify that no impossible rate was introduced while solving for the weight.

### SC06

**Avoid division by the common intersection.** With positive marginals $a,b$ and nonnegative intersection $x$, equality of the reverse conditionals is

$$\frac xb=\frac xa\quad\Longleftrightarrow\quad ax=bx\quad\Longleftrightarrow\quad x(a-b)=0.$$

The equivalence multiplies by $ab>0$, so it remains valid when $x=0$. There are two branches: a zero joint mass or equal marginals. The unequal-marginal disjoint example below realizes the first branch. If the question additionally required a positive intersection, only the equal-marginal branch would survive. Characterizing the zero set before canceling a factor prevents silently discarding a whole valid family of models.

### SC07

**Use one common signed quantity.** Put $d=P(A\cap B)-P(A)P(B)$. Subtracting each target marginal from the relevant conditional gives

$$P(A\mid B)-P(A)=\frac{d}{P(B)},\qquad P(B\mid A)-P(B)=\frac{d}{P(A)}.$$

Both denominators are positive, so both changes have the sign of $d$. This proves the requested strict inequality and also the corresponding equality and negative-association statements. Their magnitudes need not agree: for marginals $1/2,1/4$ and intersection $1/5$, $d=3/40$, producing increases $3/10$ and $3/20$ respectively. The same positive association can therefore have different numerical effects in the two conditioning directions.

### SC08

**Resolve four mutually exclusive cases inside the information event.** In the measure conditioned on $C$, put both mass at $1/3$. Subtract it from the two target marginals, giving A-only mass $1/3$ and B-only mass $1/6$. The remaining mass is $1-1/3-1/3-1/6=1/6$.

The union consists of the first three cells, exactly one consists only of the middle two, and neither is the fourth. Thus the requested results are $5/6,1/2,1/6$. Their interpretation is checked by $P(\text{exactly one}\mid C)+P(\text{both}\mid C)+P(\text{neither}\mid C)=1$. An unconditional probability of $C$ is unnecessary because all four cells have already been normalized within it.

### SC09

**Separate set membership from positive probability.** In the proposed three-outcome construction, the exceptional outcome3has zero probability. It can still belong to $B\setminus A$. The conditional ignores its mass, so the conditional value is one even though the set difference is nonempty.

In general, with $P(B)>0$,

$$P(A\mid B)=1\quad\Longleftrightarrow\quad P(A\cap B)=P(B)\quad\Longleftrightarrow\quad P(B\setminus A)=0.$$

The last equivalence uses the disjoint split of $B$ into its intersection with $A$ and its difference from $A$. It does not say that the difference contains no outcomes. In a finite space where every singleton has positive probability, a nonempty difference would necessarily have positive mass, so literal containment would then follow. State that support condition rather than silently importing it.

### SC10

**List the retained atoms at each level.** The outer information $C$ retains weights $1,2,3,4$, totaling ten. The inner event $B$ retains weights $1,2,4$, totaling seven. Their intersection is just $B$, while the target retained inside it has weights $1,4$, totaling five.

$$P(A\cap B\mid C)=\frac5{10},\qquad P(B\mid C)=\frac7{10},\qquad \frac{5/10}{7/10}=\frac57.$$

The outer normalizer cancels because numerator and denominator are probabilities under the same outer information. Averaging $5/7$ and $5/10$ would mix two distinct sample spaces and has no conditional-measure justification. The fifth atom is outside $C$ and contributes to neither term; its positive original weight is irrelevant once that outer observation is fixed.

### SC11

**Identify each denominator rather than only the final intersection.** The first factor is a marginal $2/5$. The denominator for the second factor is this positive mass. Their product gives prefix mass $P(A\cap B)=3/10$, which is the denominator for the final conditional. Both required ratios therefore exist.

$$P(A\cap B\cap C)=\frac25\frac34\,0=0.$$

The conclusion uses multiplication of three defined numbers. A hypothetical fourth conditional given this zero-mass triple would not be defined by the elementary ratio. Its descendant joint probability would still be zero by containment. This distinction explains why “zero times an undefined number” is not an acceptable derivation even when the final joint mass can be established by another argument.

### SC12

**Enumerate the entire four-state model.** The equally likely states are $00,01,10,11$. The triple intersection retains only $11$. Given $A\cap B$, equality is therefore certain. Given only $B$, the retained states are $01,11$, only one of which has equal bits.

$$P(A)P(B\mid A)P(C\mid A\cap B)=\frac12\frac12\cdot1=\frac14,$$

$$P(A)P(B\mid A)P(C\mid B)=\frac12\frac12\frac12=\frac18.$$

The first product matches direct enumeration and the second does not. The missing information specifies the first bit and thus changes the last event's truth. A shorter conditional factor requires a genuine conditional-independence property, not merely the visual appearance of neighboring stages in a tree.

### SC13

**Compute one joint mass and then divide by the new prefix.** In the original order the triple mass is $(3/5)(1/2)(2/3)=1/5$. In the reverse order the prefix $B\cap C$ has mass $(2/5)(3/4)=3/10$. Thus the requested conditional is $(1/5)/(3/10)=2/3$.

This ratio is defined and below one, but that alone is not a complete compatibility proof. The explicit six positive cells below sum to one and recover $P(A)=3/5$, $P(A\cap B)=3/10$, $P(C)=2/5$ and $P(B\cap C)=3/10$. Their unused two cells can be zero. Constructing a complete joint law proves that no hidden constraint among the supplied marginals prevents the calculation from describing a real model.

### SC14

**Use the history-reduction premise exactly where needed.** The initial-one mass is $2/5$. Along $101$, both transitions change the bit, so the path has weight $(2/5)(1/3)^2=2/45$. Along $111$, both preserve it, giving $(2/5)(2/3)^2=8/45$.

The retained event is the disjoint union of these two full paths, with mass $10/45=2/9$. Renormalization gives masses $1/5$ and $4/5$, whose sum is one. Their conditional odds are one to four, equal to the ratio of the original path masses. Conditioning preserves that ratio. Without the stated Markov property, a single-step change rate would not determine the second transition conditional on the first transition's history.

### SC15

**Start with ordered outcomes.** There are sixteen equally likely pairs before observing the minimum. Requiring minimum two excludes every pair containing one and every pair with both entries above two. The surviving five states are $22,23,32,24,42$, each of original mass $1/16$ and conditional mass $1/5$.

The maximum groups these states into disjoint fibers of sizes one, two and two. Their probabilities therefore sum to $(1+2+2)/5=1$. If unordered pairs were used, the off-diagonal possibilities would need twice the weight of $22$; three equal unordered weights would not reproduce the original experiment. The calculation demonstrates that a derived statistic's values need not be equiprobable even when the underlying ordered outcomes are.

### SC16

**Track inventory after each draw.** A first red removes one of four reds from seven objects. A following blue removes one of three blues from the remaining six. A final red then has three available successes among five remaining objects. This produces $36/210=6/35$ for the one specified pattern.

For exactly two reds there are three disjoint position patterns. Exchangeability gives each the same factors, though in a different order, so the total is $18/35$. The unordered route chooses two of four reds and one of three blues from a three-object subset of seven: $6\cdot3/35=18/35$. The agreement checks that ordered and unordered sample representations were normalized consistently. Treating the successive draws as independent would use powers instead of decreasing inventories and fail both derivations.

### SC17

**Condition on a partition of the retained history.** The different-color event is the disjoint union of $RB$ and $BR$. Each has mass $(4/7)(3/6)=2/7$, so within their union each weight is one half. Either history leaves exactly three red and two blue objects.

$$P(R_3\mid R_1B_2\cup B_1R_2)=\frac12\frac35+\frac12\frac35=\frac35.$$

The equal weights are verifiable here, but they are not essential to the final result: any weights summing to one would average two identical rates to $3/5$. The reason history compression works is equal remaining composition, not independence of successive draws. A condition retaining $RR$ would require another rate and different weights.

### SC18

**Keep both kinds of eligible history.** The first-two-draw masses are $P(RR)=2/7$, $P(RB)=2/7$, $P(BR)=2/7$ and $P(BB)=1/7$. Retaining at least one red gives total mass $6/7$, so the three retained histories have conditional weights one third each.

After $RR$, the remaining red fraction is $2/5$. After either mixed history it is $3/5$. The required weighted rate is

$$\frac13\frac25+\frac13\frac35+\frac13\frac35=\frac8{15}.$$

This gives a second explicit derivation of the subtraction calculation below. The answer lies between the retained-history rates $2/5$ and $3/5$, providing a convexity check. Selecting a single representative urn would erase the uncertainty about how many red objects were removed.

### SC19

**Count compatible success-position sets.** Conditioning on three successes in eight trials retains $\binom83=56$ equally weighted sets of three positions. The equality of those weights follows from their common original mass $p^3(1-p)^5$, not from an assumption that all binary strings were initially equiprobable.

Fixing the first two positions leaves one success to choose from positions3through8, giving six favorable sets. Thus $6/56=3/28$. The sequential alternative is $(3/8)(2/7)$: after learning that position1is a success, two successes remain among seven positions. Its second factor is not $3/8$. The changed factor quantifies the dependence created by fixing a total count, even though the original trials were independent.

### SC20

**Write the favorable strings before counting starts.** Exactly three successes in six positions gives twenty equally likely strings. A run of three must use all three successes. The favorable strings are $111000,011100,001110,000111$.

They are distinct and exhaust the possibilities, so the answer is $4/20=1/5$. No subtraction for overlapping runs is needed here because two different length-three runs would require at least four successes. If the total number of successes were larger, the same start-counting argument could overcount. This is why the fixed-count premise is part of the proof, not incidental context. The common original pattern weight cancels for every $0<p<1$; at endpoint probabilities the stipulated three-success information would have probability zero.

### SC21

**Enumerate disjoint permutations, not equally likely label values.** The event requires one occurrence of every label. Its six ordered permutations each have product mass $(1/2)(1/3)(1/6)=1/36$ because the draws are independent. Their disjoint union therefore has probability $6/36=1/6$.

The conditional chance of a new label depends on which labels have appeared: after label1the unused mass is one half, whereas after label3it is five sixths. Thus a uniform birthday-product shortcut would replace genuine history-dependent rates by incorrect common rates. Enumerating complete permutations works because multiplying the same three probabilities in a different order leaves their product unchanged, even though individual labels were never uniform.

### SC22

**Define the counted event for one object first.** An object contributes a success exactly when it enters and subsequently succeeds. Its probability is $(2/3)(3/4)=1/2$, using the conditional multiplication rule. It fails to contribute with probability one half, combining nonentry and later failure.

For a fixed set of two successful objects, independence across complete object histories gives mass $(1/2)^2(1/2)^3=1/32$. There are ten distinct choices of that set, producing $10/32=5/16$. This derivation does not assume independence between entry and a later event inside one history; the later rate is already conditional. The expected eligible count $10/3$ describes a mean across experiments and cannot replace the experiment's random integer count.

### SC23

**Separate population weights, joint success masses and selected weights.** Type1has original weight one quarter, so its successful mass is $(1/4)(4/5)=1/5$. Type2has original weight three quarters and successful mass $(3/4)(2/5)=3/10$. Adding the disjoint pieces gives total success mass one half.

Conditioning on success divides each successful type mass by that same half, giving selected weights $2/5$ and $3/5$. They sum to one. The more reliable type gains relative weight after success, but its within-type success probability and its prior prevalence are different quantities. Averaging the two original rates equally would ignore prevalence and give the wrong aggregate, while using the prior one-quarter weight after selection would ignore the observation.

### SC24

**Update the case weights and justify the rates separately.** The observed $B$ masses in the two strata are $3/8$ and $1/8$. Their sum is one half, so conditional stratum weights are $3/4$ and $1/4$. Within each stratum the stipulated independence says that learning $B$ leaves the $A$ rate unchanged.

Thus $P(A\mid B)=(3/4)(2/3)+(1/4)(1/3)=7/12$. Direct joint addition gives $P(A\cap B)=1/4+1/24=7/24$; dividing by $P(B)=1/2$ agrees. This independent route checks both the new weights and the rate invariance. Without within-stratum independence, the two marginal rate lists alone would not determine those joint masses.

### SC25

**Normalize an infinite sequence of joint weights.** Let $G$ denote all checks passing. The joint mass at count $n$ is $(1-r)(rq)^n$, including count zero because an empty collection has no failed checks. The series converges since $0<rq<1$ and sums to $(1-r)/(1-rq)$.

After dividing by this sum, the conditional count law is $(1-rq)(rq)^n$. Its zero-count mass is $1-rq$, so its positive-count mass is $rq$. Summing that conditional law directly verifies normalization. Excluding count zero before conditioning would define a different information event, and the question of positive count would then be certain rather than $rq$. The starting index determines the event being modeled.

### SC26

**Expand each weighted conditional into its joint event.** The proposed sum is $P(A\cap B)+P(A\cap C)$. These two events overlap on $A\cap B\cap C$. Since $B\cup C$ covers the sample space, their union is exactly $A$.

$$P(A\cap B)+P(A\cap C)=P(A)+P(A\cap B\cap C).$$

The correction is subtraction of that triple overlap. An explicit example takes $B=C=\Omega$ and a target with probability one third: the proposed sum gives two thirds, exactly one extra copy of the target. The simple total-probability formula requires disjoint cases, not merely exhaustive cases. For a particular target the overcount can vanish even if the cases themselves overlap, because their overlap may contain no target mass.

### SC27

**Calculate each method under its own case distribution.** For methodA, the easy contribution is $9/100$ and the hard contribution is $36/100$, totaling $9/20$. For methodBthey are $72/100$ and $3/100$, totaling $3/4$. The reversal is compatible with A's larger within-stratum rates because B receives far more easy cases.

With a common easy weight $w$, subtracting the two aggregate rates gives $w(9/10-4/5)+(1-w)(2/5-3/10)=1/10$. This is positive for every $0\le w\le1$. Therefore changing only the common mixture cannot reverse these stratum inequalities. No causal superiority conclusion follows from the unadjusted aggregate without specifying how cases were assigned.

### SC28

**Use factorization, which covers null events.** Disjointness fixes the intersection at zero, so independence is exactly $0=ab$. For nonnegative probabilities, this holds if and only if at least one marginal is zero.

When both marginals are positive, learning $B$ makes $A$ impossible, changing its probability from $a$ to zero. That ratio explanation is valid only for positive $P(B)$. The product proof also covers the boundary where $B$ is null and its conditional ratios are undefined. A null event can still be independent of another event because product independence does not require conditioning on it. Distinguish the validity of a relationship between events from the definability of a particular observed-event ratio.

### SC29

**Exploit containment as an intersection identity.** Since $A\subseteq B$, the joint probability equals $a$. Independence would require $a=ab$, or $a(1-b)=0$. Thus either the smaller event is null or the larger event is certain.

The almost-sure containment version gives the same conclusion: a null difference leaves the joint mass equal to $a$ even if some zero-mass outcomes violate literal containment. For a positive $a$ and $b<1$, the conditional $P(B\mid A)$ is one, strictly above $b$, so the events are dependent. This interpretation agrees with the algebra but cannot replace its boundary cases. Nested events are not universally dependent; certainty and nullity are valid exceptions.

### SC30

**Prove complement closure without fragile division.** Inclusion-exclusion gives $P(A^c\cap B^c)=1-a-b+P(A\cap B)$. Under independence substitute $ab$ and factor the result as $(1-a)(1-b)$.

The factors are the two complement marginals, establishing independence of the complements. Similarly $P(A\cap B^c)=a-ab=a(1-b)$ proves independence when only one event is complemented. Every step uses subtraction and multiplication of defined probabilities, so it remains valid when a marginal is zero or one. A proof based on $P(A^c\mid B^c)$ would require splitting off the case $P(B)=1$; the product route covers it automatically.

### SC31

**Use the idempotence of intersection, not an intuition about repeated observations.** Since $A\cap A=A$, self-independence says $a=a^2$. The only roots in the unit interval are zero and one.

For an interior probability, observing $A$ makes its own conditional probability one, which differs from the marginal $a$. At probability zero, that conditional is undefined even though product independence still holds. A singleton under a uniform continuous distribution is nonempty but null; the interval with one point removed has probability one without being the entire sample space. Thus the two probability endpoints describe almost-sure behavior, not necessarily literal emptiness or literal universality of the event.

### SC32

**Verify all three pair equations explicitly.** The four equal states give event lists $A=\{10,11\}$, $B=\{01,11\}$ and $C=\{01,10\}$. Each marginal is one half. Their pair intersections are respectively $\{11\},\{10\},\{01\}$, all of mass one quarter.

The triple intersection is empty, with mass zero rather than one eighth. Hence the family is pairwise independent but not mutually independent. Given both first events, the third event is impossible, demonstrating precisely which final chain factor differs from its marginal. Listing all cells checks that the counterexample is a single coherent probability model rather than three separately specified pair tables that might be mutually incompatible.

### SC33

**Check the subfamilies instead of only the largest intersection.** In eight equal atoms, take $A=B=\{1,2,3,4\}$ and $C=\{1,5,6,7\}$. All three marginal probabilities are one half. Their full intersection is only atom1and has probability one eighth, agreeing with $(1/2)^3$.

Nevertheless $A\cap B=A$ has probability one half instead of the product one quarter. Hence full-family factorization holds while the pair condition fails. Mutual independence requires both the triple equation and all the pair equations; the full intersection alone is insufficient. The three positive marginals and complete explicit sets ensure that this is a genuine finite model rather than a boundary trick. Checking both equalities numerically is essential when proposing a counterexample: a plausible description that fails its own advertised equality proves nothing about the intended implication.

### SC34

**Count subfamilies by size.** Five events have ten pairs, ten triples, five four-event subsets and one full five-event subset. Their total is $10+10+5+1=26$, agreeing with $2^5-5-1$.

The five singleton equalities and the empty-family convention supply no additional nontrivial product checks. Pairwise independence covers only the ten pair equations. The remaining sixteen conditions address larger intersections. This count describes the definition's required equalities; it is not a claim that those equations are algebraically independent in every special model. A construction from mutually independent primitive coordinates may establish them together without checking twenty-six unrelated formulas one by one.

### SC35

**Partition by which single event succeeds.** The three favorable patterns are success-failure-failure, failure-success-failure and failure-failure-success. Mutual independence gives their masses $1/4,1/8,1/12$, summing to $11/24$.

The all-failure pattern also has mass $(1/2)(2/3)(3/4)=1/4$, so the at-least-one event has probability $3/4=18/24$. Exactly one is a subset of at least one, consistent with $11/24\le18/24$; the remaining $7/24$ is the chance of at least two. The success rates differ, so substituting them into the equal-rate expression $3p(1-p)^2$ would be unjustified. Disjoint pattern addition and independent coordinate multiplication are distinct operations used at different steps.

### SC36

**Compare complete joint tables with the same pair marginals.** Three independent fair bits have eight states of mass one eighth. The parity construction instead has four states $000,011,101,110$, each of mass one quarter.

Every two coordinates in the parity construction realize the four binary pairs exactly once, so every pair is independent and fair. But the all-failure state has mass one quarter instead of one eighth. Hence equal pair data admit different answers to the requested three-way event. Pairwise factorization does not determine the final conditional factor after two coordinates have been observed: in the parity model that final bit is fixed by the first two.

### SC37

**Renormalize the selected atoms before multiplying marginals.** Equality retains $00$ and $11$, each of original mass one quarter. The information mass is one half, so each retained atom receives conditional weight one half.

Both individual one-events have conditional marginal one half, but their joint is the entire $11$ atom and also has mass one half. Their factorization discrepancy is $1/2-(1/2)(1/2)=1/4$. The original individual marginals happened to remain unchanged. Their joint did not. Selection altered dependence while preserving single-coordinate fairness, showing why inspecting marginal rates alone is insufficient to claim that independence survives an observation.

### SC38

**Retain the three compatible states with their original weights.** At least one success excludes only $00$, so its mass is three quarters. The retained states $01,10,11$ each have conditional mass one third.

Each marginal success event retains two states and has rate two thirds, while both successes retain one state and have rate one third. The discrepancy is $1/3-4/9=-1/9$. Given that the first bit is zero within this selected universe, the second must be one; given that the first is one, the second is still equally likely to be zero or one. This conditional contrast gives a direct interpretation of the induced negative association.

### SC39

**Build the mixture's full table.** In type1the both-success and both-failure rates are $81/100$ and $1/100$, with each single-success rate $9/100$. Type2reverses the both-success and both-failure rates while keeping each single-success rate $9/100$.

Equal mixing therefore gives joint cells $41/100,9/100,9/100,41/100$. The marginals are each one half. Their product is one quarter, below the actual both-success mass by $16/100$. Dividing $41/100$ by one half gives $41/50$ for the requested second success rate. The complete table supplies a normalization check and explains the dependence: a shared favorable type raises the chances of both outcomes together.

### SC40

**Write both stratum tables and then mix them.** Inside $C$ the four conditional cells are all one quarter. Inside $C^c$ only $00$ and $11$ have mass one half. The second table fails independence because its both-success mass one half differs from the product one quarter.

Equal mixing yields unconditional cells $3/8,1/8,1/8,3/8$. Thus both marginals remain one half, but the joint three eighths exceeds their product one quarter. Complement closure inside a fixed conditional measure concerns replacing target events by their complements. Replacing the information $C$ by $C^c$ selects a different table, for which no independence relation was supplied.

### SC41

**Make the division premise explicit.** In the conditional measure given $C$, the multiplication identity is

$$P(A\cap B\mid C)=P(A\mid B\cap C)P(B\mid C).$$

The last factor is $P(B\cap C)/P(C)>0$, so dividing by it proves the ratio equivalence. Multiplying back proves the converse. If this factor were zero, product independence would hold automatically because both its joint and the product would be zero. The ratio conditioned on $B\cap C$ would nevertheless be undefined. An equivalent ratio formulation therefore has a narrower domain than the product definition and must retain its positive-intersection hypothesis.

### SC42

**Calculate association through the joint table, not through equal marginals.** The two within-type both-success rates are both $4/25$, so equal mixing leaves joint mass $4/25$. Each marginal is one half, giving discrepancy $4/25-1/4=-9/100$.

The table is therefore $4/25,17/50,17/50,4/25$ in the standard cell order; all entries are nonnegative and sum to one. The hidden type makes one outcome more likely when it makes the other less likely. That opposing movement produces negative marginal association despite within-type independence. It is a mixture effect, not a claim that the primitive checks interfere causally with each other.

### SC43

**Expand before factoring.** The joint is $wu_1v_1+(1-w)u_2v_2$. Subtract $[wu_1+(1-w)u_2][wv_1+(1-w)v_2]$ and collect the four cross terms. The result is $w(1-w)(u_1-u_2)(v_1-v_2)$.

For $0<w<1$, the weight factor is positive, so the product vanishes precisely when one rate difference vanishes. At endpoint weights only one stratum is present and independence holds under its premise without restrictions on unused-stratum rates. With three strata, nonzero positive and negative contributions can cancel, so the two-stratum necessity cannot be carried over unchanged.

### SC44

**Augment each hidden state by its reporting probability.** The original states $00,01,10,11$ each have prior weight one quarter. Protocol1has message likelihoods $0,1,1,1$, leaving three equal retained weights and both-active rate one third.

Protocol2has likelihoods $0,1/2,1/2,1$. Its joint message weights are $0,1/8,1/8,1/4$, summing to one half. After renormalization the retained weights are $0,1/4,1/4,1/2$, giving both-active rate one half. Truthfulness rules out a message in state00but does not fix the three other likelihoods. Those unequal likelihoods, rather than a disagreement about conditional probability, explain the different answers.

### SC45

**Count card-face outcomes rather than card names.** There are six equally likely outcomes before observing the visible color: two for RR, two for RB and two for BB. The red observation retains both RRfaces and one RBface, so its chance is three sixths. The joint event that the hidden face is red retains the two RRoutcomes and has chance two sixths.

Their ratio is two thirds. In the deliberately-red protocol the card itself is chosen uniformly from RRandRB, so the corresponding hidden-red rate is one half. Both show red, but they do not produce the same distribution of hidden cards. The sample-space construction must include the face-selection step if that step is random.

### SC46

**Keep the host likelihood parameter throughout normalization.** Given prize doors1,2,3, opening door3has likelihoods $t,1,0$. Multiplying by the equal priors gives weights $t/3,1/3,0$. Their sum $(1+t)/3$ is positive throughout the allowed range.

Switching to door2therefore succeeds with probability $1/(1+t)$. This is decreasing on $[0,1]$, so the attainable interval is $[1/2,1]$. The fair tie case gives two thirds. Before conditioning on a named revealed door, switching wins whenever the initial choice was wrong, independently of how a knowledgeable host breaks ties when the initial choice was right. That aggregate argument and the named-message posterior answer different questions.

### SC47

**Condition on a reveal that could have exposed the prize.** The unknowing host produces an empty reveal with probability one when the prize is at the initial door, but only one half at each other prize location. Thus the retained weights are $1/3,1/6,1/6$ and normalize to $1/2,1/4,1/4$.

The initial door wins in the first retained case; switching wins in the other two. Their conditional probabilities are both one half. Removing prize-reveal cases selectively favors the initial door, unlike an informed host who never produces such cases. A visible empty door does not reveal whether the underlying experiment used informed choice or random choice followed by selection.

### SC48

**Write the system event from primitive edges.** It is $E\cap(F\cup G)$. Independence of $E$ from the disjoint coordinate block $(F,G)$ gives $p[1-(1-p)^2]=2p^2-p^3$.

The two complete paths share $E$, so their intersection is $EFG$ and has mass $p^3$. Treating the paths as independent would replace that intersection with $p^4$. Its resulting reliability overestimate is $p^3(1-p)$, positive for interior rates and zero at the endpoints. At $p=1/2$ the exact event retains three of eight equal edge states, giving $3/8$, independently confirming inclusion-exclusion. A path is a derived event, not a new independent primitive merely because it is drawn as a separate route.

### SC49

**Condition on the fifth edge, then justify each reduced formula.** When the bridge fails, the remaining upper and lower routes use disjoint two-edge blocks. Their series rates are $p^2$, giving parallel reliability $2p^2-p^4$. When the bridge works, source-side edges form one parallel block and destination-side edges form another disjoint parallel block. Their rates are both $2p-p^2$, so the conditional reliability is their product.

Weighting by bridge failure and success gives

$$R(p)=2p^2+2p^3-5p^4+2p^5.$$

This polynomial agrees with the conditioned expression and gives $R(0)=0$, $R(1)=1$, $R(1/2)=1/2$. Enumerating the thirty-two primitive edge states offers an independent check; it does not require incorrectly declaring the overlapping full-network paths independent.

### SC50

**Identify the independent blocks correctly.** Each two-hop path uses two distinct primitive edges and succeeds with probability $p^2$. Different paths use disjoint edge blocks, and all sixteen primitive edges are mutually independent. Thus the eight path events are mutually independent here, unlike shared-edge paths.

Every path failing has probability $(1-p^2)^8$, so taking the complement gives the requested reliability. The sum $8p^2$ is an upper bound, not the exact union probability, because several paths can work in the same trial. At $p=1/2$ the exact expression is $1-(3/4)^8<1$, while the naive sum is two. The extreme-rate checks alone already refute that sum as a general reliability formula.

### SC51

**Recover marginals by summing rows and columns.** The first-one row has mass $1/8+3/8=1/2$. Within it, the both-one cell has mass $3/8$. Their ratio is three quarters.

Independence would require both-one mass $(1/2)(1/2)=1/4$, but the table supplies three eighths, an excess of one eighth. Its determinant is $(3/8)^2-(1/8)^2=1/8$, confirming the same sign and magnitude. Marginal fairness describes separate row and column sums. It does not determine how probability is arranged across their joint cells, and a symmetric-looking table can be strongly dependent.

### SC52

**Integrate cross-sections in the retained region.** In the unit square the condition is the triangle below $y=1-x$. Its area is one half. Restricting $0\le x\le1/2$ gives vertical slice height $1-x$, so the target joint area is $[x-x^2/2]_0^{1/2}=3/8$.

The ratio is $(3/8)/(1/2)=3/4$. As a second check, the excluded right triangle has legs one half and area one eighth, hence conditional complement mass one quarter. A horizontal-length ratio would assign equal mass to slices of different heights and fail this area calculation. The original square has constant area density; conditioning keeps that density constant on the triangle but does not make the horizontal marginal density constant.

### SC53

**Normalize a density along the specified fiber.** Integrating the joint density two over $0<x<y$ gives $f_Y(y)=2y$ at an interior $y$. Division by this positive marginal density gives $f_{X\mid Y}(x\mid y)=1/y$ on that interval.

Its integral over the whole fiber is one, and its integral over $0<x\le y/3$ is $(y/3)/y=1/3$. The event $Y=y$ itself has probability zero, so this result is a conditional-density version rather than an elementary event quotient. At individual null values conditional versions can be changed without changing the joint law; the natural interior density convention and support are part of the specification here.

### SC54

**Compute both masses at a positive strip width before taking a limit.** The information strip has joint density integral $\int_y^{y+\varepsilon}2u\,du=2y\varepsilon+\varepsilon^2$. The target part is a rectangle of width $y/2$ and height $\varepsilon$, lying entirely below the variable upper boundary $x=u$ because $u\ge y$.

Its mass is twice its area, or $y\varepsilon$. Dividing gives $y/(2y+\varepsilon)$, tending to one half as $\varepsilon\downarrow0$. Every finite denominator is positive. The argument constructs this particular natural limiting version; it never turns the zero-mass line into a positive-probability event, nor proves that every differently shaped shrinking region must select the same version.

### SC55

**Solve all eight cells from the pair data.** Set the111cell to $t$. Each pair intersection is one quarter, so the110,101,011cells are each $1/4-t$. Subtracting from a marginal one half then makes each100,010,001cell equal to $t$. Normalization forces000to $1/4-t$.

There are four cells of each expression, so their sum is $4t+4(1/4-t)=1$. Nonnegativity is exactly $0\le t\le1/4$, and every value in that interval realizes all required marginals and pairs. At either endpoint four cells vanish but the model remains valid. Mutual independence requires $t=1/8$, giving eight equal cells. This makes the unidentifiability from pair data a whole feasible interval rather than merely two isolated counterexamples.

### SC56

**Relate determinant to an independence discrepancy.** In the four-cell order the determinant is

$$bu(1-b)(1-v)-(1-b)vb(1-u)=b(1-b)(u-v).$$

The target marginal is $a=bu+(1-b)v$, so subtracting $ab$ from the joint $bu$ also yields $b(1-b)(u-v)$. Thus zero determinant and product independence coincide. With $0<b<1$, the remaining factor vanishes exactly when the two stratum rates agree. At endpoint weights, the absent stratum's conditional rate would not be identified by an elementary ratio, explaining why those endpoints were excluded from the stem. The determinant is meaningful only after the four entries have been checked as a normalized nonnegative joint table.
