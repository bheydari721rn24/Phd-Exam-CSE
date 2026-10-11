## Q1

**Correct option: 3.** Count offices, not memberships. Let the three device sets be $A,B,C$, and let $s$ be the number of offices belonging to exactly two sets. The two offices in all three sets contribute six memberships while using only two offices. Each pair-only office contributes one additional duplicated membership. Therefore

$$|A\cup B\cup C|=15+10+8-2\cdot2-s=29-s.$$

The outside count is consequently $32-(29-s)=3+s$. Because $s\ge0$, at least three offices must have no device. A lower bound is not yet a minimum: exhibit a configuration attaining it.

| Exact membership | Number of offices |
| --- | ---: |
| All three | 2 |
| Printer only | 13 |
| Scanner only | 8 |
| Modem only | 6 |
| Exactly two | 0 |
| None | 3 |

The table totals 32 and reproduces all three marginals: $13+2=15$, $8+2=10$, $6+2=8$. Thus the lower bound is attainable. Options one and two would require negative $s$. Four is possible with $s=1$, but it is not the minimum. If using inclusion-exclusion, remember that each pair intersection already includes both triple offices; their compulsory contribution totals six, followed by adding back two, for a net four duplicated memberships removed.

## Q2

**Correct option: 1.** Let $K$ count the occurring events. “At most one” is the disjoint union of $K=0$ and $K=1$. Write $p=1/n$ and $q=1-p$, with $n\ge2$. Mutual independence includes the needed complements, so the all-failure event has probability $q^n$.

For a specified unique index $i$, the event $B_i\cap\bigcap_{j\ne i}B_j^c$ has probability $pq^{n-1}$. These $n$ events are disjoint: two different indices cannot both be the unique success. Consequently

$$P(K\le1)=q^n+npq^{n-1}=q^{n-1}(q+1)=\frac{(n-1)^{n-1}(2n-1)}{n^n}.$$

At $n=2$, the only excluded outcome is two successes, so the result must be $1-1/4=3/4$, agreeing with option one. Option two evaluates to $2/3$, option three to four, and option four to $1/9$; the value four is immediately impossible for a probability. At general $n$, replacing the failure probability by $(n-1)/(n+1)$ changes the specified model. As $n$ grows, the result approaches $2/e$, since $q^{n-1}\to e^{-1}$ and $q+1\to2$. For the omitted endpoint $n=1$, the sole event occurs certainly and the answer is one; compute this case directly rather than interpret $0^0$ implicitly. Pairwise independence alone does not supply all the products used above.

## Q3

**Correct option: 4.** Let $N$ be family size, $G$ the event of no boys, and $H=\{N\ge1\}$. The prior masses $P(N=n)=2^{-n-1}$ sum to one, beginning with $P(N=0)=1/2$. A childless family satisfies $G$: it has no boy. Given size $n$, independent fair genders give $P(G\mid N=n)=2^{-n}$, including value one at zero.

The size classes partition the sample space, so add their joint contributions:

$$P(G)=\sum_{n=0}^{\infty}2^{-n-1}2^{-n}=\frac12\sum_{n=0}^{\infty}4^{-n}=\frac23.$$

| Size contribution | Prior mass | Joint mass with no boys |
| --- | --- | --- |
| Zero | $1/2$ | $1/2$ |
| One | $1/4$ | $1/8$ |
| Two | $1/8$ | $1/32$ |
| All sizes at least one | $1/2$ | $1/6$ |

Subtract only the zero-size joint mass: $P(G\cap H)=2/3-1/2=1/6$. Conditioning renormalizes by the full mass of $G$, not by the mass of $H$:

$$P(H\mid G)=\frac{1/6}{2/3}=\frac14.$$

Option one is the reversed conditional $P(G\mid H)=(1/6)/(1/2)=1/3$. Option two is the unconditional $P(H)=1/2$. Three quarters is the conditional probability of being childless given no boys, $P(H^c\mid G)=(1/2)/(2/3)$. These are valid probabilities of different events, which is precisely why preserving the conditioning direction matters. Removing childless families before computing the denominator changes the question.

## Q4

**Correct option: 1.** Model all 45 tosses as independent fair binary outcomes. The detailed space has $2^{45}$ equally likely elements. If both players obtain $k$ heads, the first player has $\binom{25}{k}$ possible sequences and the second has $\binom{20}{k}$, with $0\le k\le20$. The values of $k$ identify disjoint cases, giving

$$P(\text{equal heads})=2^{-45}\sum_{k=0}^{20}\binom{25}{k}\binom{20}{k}.$$

To evaluate the sum, use $\binom{20}{k}=\binom{20}{20-k}$. Choosing a total of 20 objects from two disjoint groups of sizes 25 and 20, partition according to how many are chosen from the first group. The partition proves, rather than merely names, the identity

$$\sum_{k=0}^{20}\binom{25}{k}\binom{20}{20-k}=\binom{45}{20}.$$

A probabilistic second proof complements the second player's indicators: equal heads means first-player heads plus second-player tails equals 20. Those 45 transformed indicators remain independent and fair, so exactly $\binom{45}{20}$ detailed outcomes qualify. The index 15 in options two and four counts the wrong target. The denominator $2^{20}$ in options three and four ignores the first player's 25 independent outcomes; it does not describe their joint experiment. The identity applies to unequal toss counts $a,b$ as $\binom{a+b}{b}/2^{a+b}$ under independent fair tosses. With unequal coin biases, the weights of the summands change and the fair-count shortcut no longer applies.

## Q5

**Correct option: 2.** Define $I_i$ to be one when the key at position $i$ is smaller than all earlier keys and zero otherwise. Initialization at positive infinity makes $I_1=1$. Distinct keys and a uniform random permutation imply that each of the first $i$ positions is equally likely to contain the prefix minimum. Hence $P(I_i=1)=1/i$.

For each permutation, the assignment count satisfies $Y=I_1+\cdots+I_n$. Adding the expected values gives the exact mean

$$E[Y]=\sum_{i=1}^{n}E[I_i]=\sum_{i=1}^{n}\frac1i=H_n.$$

This step uses linearity, which holds whether or not the indicators are independent; no independence proof is required. Integrating the decreasing function $1/x$ over successive unit intervals yields $\ln(n+1)\le H_n\le1+\ln n$. Thus $H_n/\ln n\to1$, explaining the large-$n$ choice $\ln n$. It is an asymptotic approximation, not an exact equality at finite $n$.

Option one keeps only the compulsory first record. The value $n$ is attained by a decreasing array but is not the mean over all permutations; it is also the number of comparison tests, which remains $n$ for every input. Multiplying that scan length by the expected number of updates produces $n\ln n$, a different quantity with no basis in the requested ledger. If initialization instead uses the first key without counting its assignment, the subsequent record-update mean is $H_n-1$. Duplicates and nonuniform input distributions require a new symmetry argument.

## Q6

**Correct option: 4.** Pre-generate two independent fair bits for each of four coins, even if a second bit is not used. The contribution of coin $i$ is one exactly when its two bits are $HH$. Thus each contribution has probability $1/4$, and contributions from different coins are independent. The other three per-coin outcomes contribute zero.

For exactly two contributions, select their two labels in $\binom42=6$ ways. Every specified successful pair and failed complementary pair has probability $(1/4)^2(3/4)^2$. These cases are disjoint, so

$$P(Y=2)=6\frac1{16}\frac9{16}=\frac{27}{128}.$$

A check by the random eligible count $K$ conditions on the first-round heads:

| $K$ | $P(K)$ | $P(Y=2\mid K)$ | Joint contribution |
| --- | --- | --- | --- |
| 2 | $6/16$ | $1/4$ | $3/32$ |
| 3 | $4/16$ | $3/8$ | $3/32$ |
| 4 | $1/16$ | $6/16$ | $3/128$ |

For $K<2$ the contribution is zero; the three remaining entries sum to $27/128$. Treating the second round as four unconditional fair tosses yields $3/8$, which belongs to a different experiment. Substituting $E[K]=2$ for the random count would yield $1/4$; expectation does not preserve this probability function. The listed values $1/2$, $3/4$, and $17/128$ fail the exact partition. A particular two-stage outcome has its joint probability before eligibility is conditioned on, which explains the factor $1/4$.

## Q7

**Correct option: 4.** At $n=5$, the uniform space contains eight elementary outcomes. Partition it by membership rather than count the same outcome twice:

| Region | Count |
| --- | ---: |
| Both events | 1 |
| First only | 4 |
| Second only | 1 |
| Neither | 2 |

The event union includes the first three rows and has six points, so its mass is $6/8=3/4$. Adding the marginals without correction gives option one's $7/8$, which counts the shared point twice. Option two's $5/8$ counts only $A$, while option three's $1/8$ counts only the intersection. Every point has mass $1/8$ by the stated sampling law; the table itself would not justify equal masses without that premise. The construction also shows the given cardinalities are consistent, since all four region counts are nonnegative and total eight. For later generalization, these rows become $1,n-1,1,2$, so the union always contains $n+1$ points, not $n+2$.

## Q8

**Correct option: 3.** With $n=8$, eleven elementary outcomes each have mass $1/11$. The four region counts are $1$ for both, $8-1=7$ for first only, $2-1=1$ for second only, and $11-(7+1+1)=2$ for neither. Hence

$$P(A\cup B)=\frac{7+1+1}{11}=\frac9{11}.$$

The same result follows from subtracting the outside event: $1-2/11=9/11$. These two calculations use complementary partitions, providing an independent check on the numerator. Option one counts $A$ alone, option two the overlap alone, and option four uses $8+2=10$, which double-counts the common outcome. The exactly-one mass is instead $(7+1)/11=8/11$; in this special instance it equals the first marginal, but their events are different. Such accidental numeric agreement cannot identify an event. If the two outside points were assigned larger probabilities, their count of two would remain unchanged while the union probability would decrease. Both the atomic partition and the uniform law are required.

## Q9

**Correct option: 2.** For every positive integer $n$, four exact membership counts are $1,n-1,1,2$, totaling $n+3$. The union removes only the final region, so its count is $n+1$. Under equal elementary masses,

$$P(A\cup B)=\frac{n+1}{n+3}=1-\frac2{n+3}.$$

This construction proves existence of a model for all stated $n\ge1$, including $n=1$, where $A\subseteq B$ and the union mass is $2/4$. The complement expression confirms the general count. The numerator $n+2$ comes from adding both event sizes without subtracting their shared point. The numerator $n$ leaves out the second-only point, and one counts only the overlap. Substitution at $n=1$ is a boundary check, not the proof of the identity; the partition supplies the universal argument. The result approaches one as $n$ grows because precisely two outside outcomes keep masses $1/(n+3)$ each. It never equals one for a finite positive $n$.

## Q10

**Correct option: 1.** The identity $P(A\cup B)=P(A)+P(B)-P(A\cap B)$ is valid for any probability law. Replacing probabilities by cardinality ratios is the additional step that requires a finite uniform law. Separate these two statements.

For example, retain the $n=5$ membership configuration from question seven, but give the two outside points mass $1/4$ each and the six union points mass $1/12$ each. Total mass is $2(1/4)+6(1/12)=1$. The union now has probability $1/2$, despite its unchanged cardinality ratio $6/8=3/4$. This is a concrete counterexample to option two. Adding both event probabilities without an overlap correction counts the positive shared mass twice, disproving option three. The containment in option four is reversed: $A\cap B\subseteq A\cup B$, and a second-only point witnesses strictness here. Equal likelihood is sufficient for the count rule; exceptional nonuniform laws may produce the same ratio for a particular event, but this does not establish that rule for every event.

## Q11

**Correct option: 4.** At $n=5$, the independent marginals are $a=1/5$ and $b=1/6$. Their overlap is $ab=1/30$. The four atomic masses are

| Both | First only | Second only | Neither |
| --- | --- | --- | --- |
| $1/30$ | $1/6$ | $2/15$ | $2/3$ |

Exactly one selects the middle two cells. Thus $P(A\triangle B)=1/6+2/15=5/30+4/30=3/10$. All four masses total one, checking the partition. Equivalently, $a+b-2ab=1/5+1/6-2/30=9/30$.

Option one adds marginals to obtain $11/30$, counting both twice. Option two is the overlap $1/30$, the event deliberately excluded. Option three is only $B\setminus A$ with mass $2/15$; it omits the first-only alternative. The union mass would be $10/30=1/3$, distinct from both the uncorrected sum and exactly one. Under independence the two disjoint exclusive cases have product probabilities $a(1-b)$ and $b(1-a)$; the cases are disjoint even though the original events are not. At general $n$ their sum is $(2n-1)/(n(n+1))$.

## Q12

**Correct option: 3.** At $n=8$, use denominator $8\cdot9=72$. The intersection has mass one over that denominator. First only has mass $1/8-1/72=8/72$ and second only has mass $1/9-1/72=7/72$. These alternatives exclude each other, so add them:

$$P(\text{exactly one})=\frac8{72}+\frac7{72}=\frac{15}{72}=\frac5{24}.$$

The outside mass is $(7/8)(8/9)=56/72$, and $1+8+7+56=72$ verifies normalization. Option one's $1/72$ is both, option two's $7/72$ is second only, and option four's $17/72=1/8+1/9$ counts the overlap twice. A partition avoids relying on vague meanings of “or.” The inclusive union has mass $16/72$, so subtracting the overlap once changes it to exactly one. Had the events been positively dependent, $P(A\cap B)$ could exceed $1/72$ and the exactly-one probability would decrease for these fixed marginals. The product is justified by the explicit independence premise, not by their different names.

## Q13

**Correct option: 2.** Positive integer $n$ gives $a=1/n$, $b=1/(n+1)$ and, by independence, $q=1/(n(n+1))$. The exact exclusive masses are

$$a-q=\frac{n}{n(n+1)},\qquad b-q=\frac{n-1}{n(n+1)}.$$

Their disjoint sum is $(2n-1)/(n(n+1))$. The remaining cells are $q$ and $(1-a)(1-b)=(n-1)/(n+1)$; they are nonnegative and make total mass one. This gives a valid model throughout the domain, rather than simply testing $n=5$ and eight.

Option one's numerator $n-1$ selects second only. Option three adds both marginals and equals $(2n+1)/(n(n+1))$, too large by $2q$. Option four selects the overlap. At $n=1$, $A$ is certain, $B$ has probability $1/2$, and exactly one is precisely $B^c$, again with probability $1/2$. Some distractors coincide numerically with this boundary value, but they do not agree throughout the domain. For large $n$, the probability is asymptotic to $2/n$ because both rare marginal events contribute at first order and the overlap contributes at second order.

## Q14

**Correct option: 1.** Independence is a relation between masses: $P(A\cap B)=P(A)P(B)$. Mutual exclusivity is a relation between sets: $A\cap B=\varnothing$. Here the independent product $1/(n(n+1))$ is strictly positive at every finite positive $n$, proving that these specified events cannot also be mutually exclusive.

More generally, mutually exclusive events are independent only when at least one has zero probability, since $0=P(A)P(B)$ is then necessary and sufficient. This qualification disproves the positive-probability claim in option two without asserting that disjointness and independence are never compatible. Option three is false because the exactly-one event explicitly removes the intersection. Option four confuses product probability with zero overlap. Quantitatively, independence gives exactly-one probability $a+b-2ab$, while disjointness would give $a+b$ for consistent disjoint marginals. At $n=5$, the first is $3/10$ and the second $11/30$. At $n=1$, the proposed disjoint marginals even sum to $3/2$, exceeding one and making that alternative model impossible.

## Q15

**Correct option: 4.** Five original coins produce five independent contribution indicators, each with success probability $1/4$: first-round heads and second-round heads must both occur. Exactly one successful indicator is partitioned by its unique coin label. Each specified label succeeds and the other four fail with probability $(1/4)(3/4)^4$. Therefore

$$P(Y=1)=5\frac14\left(\frac34\right)^4=\frac{405}{1024}.$$

The supplied option four is this value. The alternative $\binom52(1/4)^2(3/4)^3=135/512$ counts exactly two contributions, not one. The value $5/2^5=5/32$ counts one head among five unconditional fair trials; eligibility halves the success probability per original coin. The value $(3/4)^5=243/1024$ counts no contribution, omitting the unique-success case. A count-space description containing only values $0,1,\ldots,5$ would not make those six outcomes equally likely. Their masses are induced by the detailed two-stage sequences. The factor five counts disjoint choices of the unique success, and is not an independence assumption about those mutually exclusive choices.

## Q16

**Correct option: 3.** With eight original coins, there are eight disjoint ways to designate the unique contributing coin. A contribution has probability $1/4$ and a noncontribution $3/4$, so

$$P(Y=1)=8\frac14\left(\frac34\right)^7=\frac{2187}{8192}.$$

The simplification uses $8/4=2$ and $3^7/4^7=2187/16384$. Option one's $1/32=8/2^8$ is one head in eight ordinary fair tosses. Option two's $6561/65536=(3/4)^8$ is no second-round head. Option four's $5103/16384=\binom82(1/4)^2(3/4)^6$ is exactly two. The binomial coefficient arises because successful coin labels identify disjoint events with equal weights. It should not be applied to the random number of eligible coins as if that number were fixed at four. Conditional on a realized eligibility count $k$, the contribution count uses $k$ fair second tosses; the unconditional calculation here incorporates both stages before grouping outcomes.

## Q17

**Correct option: 2.** For each original coin, consider its independent pair of potential outcomes $HH,HT,TH,TT$. Only $HH$ contributes. For $n$ coins, specifying one contributor and $n-1$ noncontributors has mass $(1/4)(3/4)^{n-1}$. There are $n$ disjoint labels for the contributor, giving

$$P(Y=1)=\frac n4\left(\frac34\right)^{n-1}.$$

This includes $n=1$, when the answer is $1/4$. The no-success formula $(3/4)^n$ in option one counts a different event. Option three's two-success expression has coefficient $\binom n2$ and should be interpreted directly as zero when $n=1$, rather than create a spurious count by informal cancellation. Option four uses probability $1/2$ for contributions, dropping eligibility. For $n\ge1$, the correct probability is positive and tends to zero as $n$ increases: the geometric decay beats the factor $n$. Its successive ratio is $\frac{n+1}{n}\frac34$, so it increases from one through three, ties between three and four, and decreases thereafter. This explains why “more eligible opportunities” need not increase the probability of exactly one success.

## Q18

**Correct option: 1.** The first-round head count $K$ is random, taking values from zero through $n$. Conditional on $K=k$, the second round has exactly $k$ independent fair tosses. Its probability of exactly one head is $k/2^k$ for $k\ge1$, and zero for $k=0$. One may average these conditional probabilities, but cannot replace $K$ by its mean.

For $n=2$, the eligibility masses are $1/4,1/2,1/4$. Hence

$$P(Y=1)=\frac14\cdot0+\frac12\cdot\frac12+\frac14\cdot\frac24=\frac38.$$

The mean eligibility count is one; substituting it into $k/2^k$ gives $1/2$, contradicting the exact result. This finite counterexample disproves option three. Option two contradicts the possible event $K=0$, on which no second toss occurs. Option four omits the first-stage requirement: the per-original-coin joint contribution is $P(HH)=1/4$, although the conditional success probability for an already eligible coin is $1/2$. Conditioning and taking a joint event use different denominators. The independent per-coin model automatically averages eligibility and gives the same $2(1/4)(3/4)=3/8$.
