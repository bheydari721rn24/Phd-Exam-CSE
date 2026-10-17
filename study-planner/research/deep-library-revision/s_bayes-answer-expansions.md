# Bayes: individually reconstructed solution steps

These additions explain the construction before the earlier result and interpretation. They are independently written. An observation kernel on a null stratum is not an elementary conditional probability.

### SB01

**1. Separate the hidden state from the report.** Let $H_i$ mean source $i$ and let $E$ mean an alert. The supplied triples describe $P(H_i)$ and $P(E\mid H_i)$, respectively. Their entries refer to different conditioning directions.

**2. Construct the joint masses on a common scale.**

$$P(H_1\cap E)=\frac12\frac1{10}=\frac3{60},\quad P(H_2\cap E)=\frac13\frac15=\frac4{60},\quad P(H_3\cap E)=\frac16\frac35=\frac6{60}.$$

**3. Restrict to the alert population and normalize.** There are thirteen sixtieths of alert mass, of which six belong to source 3. Thus the posterior is $(3,4,6)/13$. Source 3 beats source 2 by the ratio $6/4$, even though its prior is smaller. The likelihoods alone would miss the source frequencies.

### SB02

**1. Use products as the sampling units.** Uniform sampling from the combined output makes the factory weights $3/4$ and $1/4$; uniform sampling of a factory first would be another experiment.

**2. Build an exact frequency representation.** A population of two hundred weighted products contains 150 from factory 1 and fifty from factory 2. Their defect masses correspond to three and five products. These are exact scaled model weights, not guaranteed realized counts.

$$P(D)=\frac{3+5}{200}=\frac1{25},\qquad P(H_2\mid D)=\frac5{3+5}=\frac58.$$

**3. Interpret the denominator.** Among all defective products, five eighths came from factory 2. Dividing its five defective cases by its fifty supplied products instead gives its forward defect probability $1/10$.

### SB03

**1. Change the probability measure before calculating.** Since $C$ is known, the source partition has weights $P(H_1\mid C)=2/3$ and $P(H_2\mid C)=1/3$. The likelihoods mean $P(E\mid H_i\cap C)$.

$$P(E\mid C)=\frac23\frac14+\frac13\frac34=\frac2{12}+\frac3{12}=\frac5{12}.$$

**2. Keep the same information in numerator and denominator.**

$$P(H_2\mid E\cap C)=\frac{P(H_2\cap E\mid C)}{P(E\mid C)}=\frac{3/12}{5/12}=\frac35.$$

The alternative $3/4$ results from imposing equal source weights within $C$. Those weights were explicitly excluded by the statement. Extra background information changes the sampling population, not merely a label on the final answer.

### SB04

**1. Refine overlapping explanations into four disjoint states.** Their masses follow by subtraction:

$$P(A\cap B)=\frac15,\quad P(A\cap B^c)=\frac25-\frac15=\frac15,\quad P(A^c\cap B)=\frac12-\frac15=\frac3{10}.$$

The remaining mass is $3/10$. Each outcome now belongs to exactly one state.

**2. Apply its own report likelihood to each cell.** On a common denominator forty, the four report masses are $(8,4,3,0)/40$. Event $A$ contains the first two cells, so

$$P(A\mid E)=\frac{(8+4)/40}{(8+4+3)/40}=\frac45.$$

The numerator includes both $A\cap B$ and $A\cap B^c$. A two-term mixture indexed merely by $A,B$ would overlap and would also omit the neither state.

### SB05

**1. Distinguish a named state from positive probability mass.** The first state contains all prior probability and assigns likelihood zero to the observation. The second state has zero prior mass, so every joint event contained within it also has zero mass.

$$P(E)=P(E\cap H_1)+P(E\cap H_2)=0+0=0.$$

**2. Apply the definition only on its domain.** Both proposed posterior entries would require a ratio with denominator zero. No elementary conditional distribution is defined by that ratio.

A generative model can specify an observation distribution for a state that its prior never selects. That extra specification still contributes zero joint mass. A software implementation must report impossible evidence instead of choosing whichever state has a favorable but unsupported likelihood. Positive prior smoothing would be an explicit model change.

### SB06

**1. Calculate the absolute masses before dropping a factor.**

$$w_1=\frac14\frac15=\frac1{20},\quad w_2=\frac34\frac25=\frac6{20},\quad z=\frac7{20}.$$

**2. Show the invariant ratio.** Replacing likelihoods by five times their original values replaces every $w_i$ and $z$ by five times its value. Therefore

$$\frac{5w_2}{5z}=\frac{w_2}{z}=\frac67.$$

**3. Recover the scale when an absolute probability is requested.** The rescaled sum is $7/4$, so divide it by the removed factor five to recover $7/20$. Calling the number two a probability or the sum $7/4$ an evidence probability is invalid. Only normalization of these nonnegative weights survives unchanged.

### SB07

**1. Recover the intersection using the supplied inverse conditional.**

$$x=P(H\cap E)=P(E)P(H\mid E)=\frac14\frac12=\frac18.$$

**2. Complete both rows of the joint table.** In denominator forty, the cells $(H E,H E^c,H^c E,H^c E^c)$ are $(5,3,5,27)/40$. Their row sums are $8/40$ and $32/40$; their evidence column sums to $10/40$.

**3. Divide by the appropriate class total.** The likelihoods are $5/8$ and $5/32$. All cells are nonnegative, so the reconstruction is feasible. More generally a proposed intersection $x$ must satisfy $\max(0,P(H)+P(E)-1)\le x\le\min(P(H),P(E))$. This example has $0\le1/8\le1/5$ and passes that necessary and sufficient table test.

### SB08

**1. Put the prior and posterior over the same denominator.** Write $z=pa+(1-p)b>0$. Then

$$\frac{pa}{z}-p=\frac{pa-p[pa+(1-p)b]}{z}=\frac{p(1-p)(a-b)}{z}.$$

**2. Inspect every factor rather than guess the direction.** The assumptions make $p$, $1-p$, and $z$ strictly positive. Thus the difference has precisely the sign of $a-b$. Equal likelihoods leave the prior unchanged; a smaller target likelihood lowers it.

**3. Check what the theorem does not say.** An increase from $1/1000$ to $100/1099$ is still below one half. Support relative to the prior and a majority posterior are different comparisons. Boundary priors cannot satisfy the same strict conclusion, because the factor $p(1-p)$ then vanishes.

### SB09

**1. Include the empty family.** Conditional on $N=n$, no boys has likelihood $2^{-n}$. At $n=0$, this equals one because there is no child who can violate the condition.

$$P(G)=\sum_{n=0}^{\infty}\frac12 4^{-n}=\frac{1/2}{1-1/4}=\frac23.$$

**2. Normalize every possible size.**

$$P(N=n\mid G)=\frac{(1/2)4^{-n}}{2/3}=\frac34 4^{-n}.$$

**3. Derive the mean.** Differentiating the convergent geometric series for $0\le r<1$ gives $\sum n r^n=r/(1-r)^2$. Multiplying its value at $r=1/4$ by $3/4$ yields $1/3$. The posterior puts mass $3/4$ at zero, so its positive-size probability is $1/4$, consistent with the authentic question revisited in this chapter.

### SB10

**1. Condition on the number eligible to be retossed.** Write $Y$ for second-round heads. The joint distribution factors as $P(K=k,Y=2)=P(K=k)P(Y=2\mid K=k)$.

| First-round heads $k$ | Prior | Two-head likelihood | Joint mass |
| --- | --- | --- | --- |
| 2 | $6/16$ | $1/4$ | $12/128$ |
| 3 | $4/16$ | $3/8$ | $12/128$ |
| 4 | $1/16$ | $6/16$ | $3/128$ |

Values zero and one cannot generate two second-round heads. The column sum is $27/128$, so the posterior weights are $12/27,12/27,3/27$. Their weighted mean is $(24+36+12)/27=8/3$. Observing two second-round heads changes the distribution of eligibility; fixing eligibility at its prior mean two loses that information.

### SB11

**1. Use one four-cell table for both possible reports.** On scale two thousand, the target/background row totals are twenty and 1,980. The positive counts are eighteen and ninety-nine; the negative counts are two and 1,881.

$$P(+)=\frac{117}{2000},\qquad P(H\mid +)=\frac{18}{117}=\frac2{13},\qquad P(H\mid -)=\frac2{1883}.$$

**2. Explain why complements occur within a class.** The target negative mass is $(1/100)(1-9/10)$; the background negative mass is $(99/100)(1-1/20)$. Complementing the posterior instead would answer whether a positive case is background, not what a negative report implies. Both denominators consist of all cases giving the actually observed report.

### SB12

**1. Count the diagonal cells of the classification table.** A correct decision is either a target alert or a background non-alert, disjoint events with total probability $(18+1881)/2000=1899/2000$.

**2. Compare like objectives.** The always-background rule is correct on 1,980 of these two thousand weighted cases. Under unit cost for each error it therefore performs better, with error $20/2000$ versus $101/2000$.

**3. Make the cost qualification quantitative.** For false-positive cost $c_{FP}$ and false-negative cost $c_{FN}$, the detector's unconditional risk is $(99c_{FP}+2c_{FN})/2000$; always-background risk is $20c_{FN}/2000$. The detector has smaller risk precisely when $c_{FN}/c_{FP}>11/2$. Thus changing the stated objective can reverse the preference without changing a single probability.

### SB13

**1. Translate prevalence into prior odds.** A prior of $1/1000$ means odds $1:999$, not $1:1000$.

$$O(H\mid E)=\frac1{999}\,100=\frac{100}{999},\qquad P(H\mid E)=\frac{100}{100+999}=\frac{100}{1099}.$$

**2. Test the majority condition without decimals.** Since $100<999$, the posterior odds remain below one; equivalently $2\cdot100<1099$. To reach a posterior of one half from this prior would require a likelihood ratio of at least 999. A ratio of one hundred is substantial support but insufficient for that distinct threshold. Absolute likelihood values are unnecessary for the posterior, yet remain necessary for the report frequency.

### SB14

**1. Keep the three-state normalization visible.** The report masses are $(3,4,6)/60$, giving posterior $(3,4,6)/13$.

**2. Restrict to the requested pair.**

$$\frac{P(H_3\mid E)}{P(H_2\mid E)}=\frac{6/13}{4/13}=\frac32,\qquad P(H_3\mid E\cap(H_2\cup H_3))=\frac6{4+6}=\frac35.$$

The unrestricted source-3 probability remains $6/13$, because it must also allow source 1. Converting odds $3/2$ into $3/5$ is correct only for the conditional binary population whose members are sources 2 and 3. Disjointness of those hypotheses justifies the pair denominator; their union is not the whole original space.

### SB15

**1. Form likelihood ratios in the same target-versus-background direction.** Positive and negative ratios are

$$LR_+=\frac{99/100}{1/2}=\frac{99}{50},\qquad LR_-=\frac{1/100}{1/2}=\frac1{50}.$$

**2. Compare evidence on an additive scale.** The log increments are $\log(99/50)$ and $-\log50$. Since $50>99/50>1$, the negative increment has larger absolute magnitude.

Intuitively, an alert is common under either class, while a missing alert is exceptionally rare under the target class. No target posterior can be computed from these ratios alone without a prior. The statement compares changes in odds, not changes of a fixed number of percentage points.

### SB16

**1. Write the requested inequality before substituting a named threshold rule.**

$$\frac{8p}{1+7p}\ge\frac34.$$

For $0\le p\le1$ the denominator is positive. Cross multiplication gives $32p\ge3+21p$, hence $11p\ge3$ and the smallest admissible prior is $3/11$.

**2. Verify the boundary with exact masses.** At that prior, target-alert mass is $12/55$ and background-alert mass is $4/55$. Normalization gives $12/16=3/4$. The posterior response is increasing because its derivative is $8/(1+7p)^2>0$, so every larger prior succeeds and every smaller prior fails. This establishes minimality rather than merely exhibiting one successful prior.

### SB17

**1. Isolate the uncertain background rate.** The target-alert mass is $9/500$, and the background-alert mass is $49f/50$. Credibility at least $9/10$ requires

$$\frac{9/500}{9/500+49f/50}\ge\frac9{10}.$$

The numerator is positive, so the denominator is positive for every admissible $f\ge0$. Multiplication yields $90/500\ge81/500+441f/50$, or $f\le1/490$.

**2. Check feasibility and sharpness.** This bound lies in $[0,1]$. At equality the two alert masses are $9/500$ and $1/500$, giving exactly nine-tenths credibility. Increasing $f$ adds only background alerts and strictly decreases the posterior. Thus the equality is the largest permissible false-positive probability.

### SB18

**1. State the shared-state assumption.** The same hidden class generates every report, and the reports are independent conditional on either class. This is what permits multiplying the ratio five repeatedly.

$$O_n=\frac{5^n}{99},\qquad r_n=\frac{5^n}{99+5^n}.$$

**2. Convert the probability threshold to an integer-power test.** The condition $r_n\ge9/10$ is $10\cdot5^n\ge9(99+5^n)$, or $5^n\ge891$. At four reports the posterior is $625/724<9/10$; at five it is $3125/3224>9/10$. These neighboring checks prove that five is the first successful count. A real-valued logarithm is useful for finding the neighborhood, but is not the required integer answer.

### SB19

**1. Distinguish the second conditional ratio from a marginal ratio.** The supplied $1/6$ compares probabilities of report 2 conditional on report 1 within each hypothesis. The chain rule therefore gives a joint-history ratio $6(1/6)=1$.

$$O_0=\frac23,\qquad O_1=4,\qquad O_2=\frac23.$$

**2. Convert each stage if useful.** The posterior moves from $2/5$ to $4/5$ after report 1 and returns to $2/5$ after report 2. The reports need not be independent; their correctly conditioned factors already contain the dependence. The final support cancels, but the likelihood of actually observing this history remains unknown because neither absolute first-report likelihood nor its common scale was supplied.

### SB20

**1. Treat the complete observed intersection as one evidence event.**

$$w_H=\frac14\frac3{10}=\frac6{80},\qquad w_{H^c}=\frac34\frac1{20}=\frac3{80}.$$

Their sum is $9/80$, so the target posterior is $6/9=2/3$.

**2. Explain order invariance through factorization.** Within each hypothesis, $P(E\mid H)P(F\mid E\cap H)$ and $P(F\mid H)P(E\mid F\cap H)$ represent the same positive joint likelihood. If all factors use that same joint law, either update order gives the same final weights. There is no basis for replacing either expression by a product of marginal likelihoods. Actual interventions or order-dependent measurement procedures could change the joint model and would be different experiments.

### SB21

**1. Compare complete likelihood tables.** For two independent positives the likelihoods are $16/25$ and $1/25$. Prior weighting gives masses $16/250$ and $9/250$, hence posterior $16/25$.

For a duplicated report, the observation event is simply one positive; its likelihoods remain $4/5$ and $1/5$. The masses are $4/50$ and $9/50$, giving $4/13$.

**2. Inspect the second update.** After the first positive, an exact copy is certain under both surviving hypotheses. Its conditional likelihood ratio is $1/1=1$, while a fresh independent positive has ratio four. Two visible messages therefore do not determine how much information was gathered. Counting independent measurements, rather than messages, is essential.

### SB22

**1. Multiply along each class-specific path.** Under $H$, the positive-positive likelihood is $(3/4)(1/2)=3/8$. Under $H^c$ it is $(1/4)(3/4)=3/16$.

$$w_H=\frac13\frac38=\frac18,\qquad w_{H^c}=\frac23\frac3{16}=\frac18.$$

The evidence mass is $1/4$ and the final posterior is one half.

**2. Verify with sequential odds.** Prior odds $1/2$ become $3/2$ after the first ratio three, then become one after the history-specific ratio $2/3$. The first posterior is $3/5$ and the second is $1/2$. The word positive describes the report's name; within the selected first-positive population this second positive is more common under background, so it reduces target belief.

### SB23

**1. Hold the coin identity fixed over the whole experiment.** Conditional independence of its tosses gives likelihoods $125/1000$ and $729/1000$. With equal priors the common factor $1/2000$ cancels, leaving posterior weights $125/854$ and $729/854$.

**2. Condition the prediction on every remaining coin type.**

$$P(H_4\mid HHH)=\frac{125}{854}\frac12+\frac{729}{854}\frac9{10}=\frac{625+6561}{8540}=\frac{3593}{4270}.$$

The result lies strictly between $1/2$ and $9/10$ because both posterior weights are positive. The most likely type is biased, but treating it as certain would discard the posterior fair-coin mass. This weighted prediction is a second total-probability calculation under the already updated measure.

### SB24

**1. Name the newly selected state.** Let $J_4$ be the coin selected for toss four and let $D$ denote the previous three heads. Independent redraw means $P(J_4=i\mid D)=P(J_4=i)=1/2$.

$$P(H_4\mid D)=\sum_{i=1}^2P(J_4=i\mid D)P(H_4\mid J_4=i,D)=\frac14+\frac9{20}=\frac7{10}.$$

**2. Identify which inference remains possible.** Each past head changes the posterior of the coin used on that particular past toss. It cannot change the independent selection of the next coin. The fixed-coin posterior $729/854$ answers a question about one common hidden identity and has no corresponding shared variable in this redrawn experiment.

### SB25

**1. Calculate the two count likelihoods explicitly.**

$$L_1=10\frac{1^3 2^2}{3^5}=\frac{40}{243},\qquad L_2=10\frac{2^3 1^2}{3^5}=\frac{80}{243}.$$

Equal priors give evidence $60/243=20/81$ and second-type posterior $80/(40+80)=2/3$.

**2. Compare with one specified order.** For a fixed three-head/two-tail sequence the two likelihoods are $4/243$ and $8/243$, with evidence $2/81$. Their common factor ten disappears from the posterior but not from the evidence rate. This cancellation uses identical fixed independent-trial models and the same observed count under both hypotheses; an order-sensitive model need not give all compatible orders the same likelihood.

### SB26

**1. Track the remaining inventory within each hypothesis.** After a first red, urn A contains three red among five objects; urn B contains one red among five. Thus the likelihoods of RR are $4/6\cdot3/5=12/30$ and $2/6\cdot1/5=2/30$.

**2. Incorporate the selection prior.** The equal urn priors produce joint masses $12/60$ and $2/60$, with evidence $14/60=7/30$. Hence $P(A\mid RR)=12/14=6/7$.

An independent count uses ordered labeled pairs: urn A has twelve red-red pairs out of thirty possible pairs, while B has two. Drawing with replacement would use four or two red again in the second factor and would instead give posterior $4/5$. The difference diagnoses the sampling assumption.

### SB27

**1. Average likelihoods only after multiplying inside each source.** Both marginal success probabilities equal $(4/5+1/5)/2=1/2$. The two-success mass is

$$\frac12\frac{16}{25}+\frac12\frac1{25}=\frac{17}{50}.$$

**2. Normalize by the first-success probability.** The predictive probability is $(17/50)/(1/2)=17/25$. Equivalently, the first success gives source posteriors $4/5$ and $1/5$, which weight the next success rates.

**3. Quantify the induced dependence.** The covariance of the two success indicators is $17/50-1/4=9/100>0$. Shared uncertainty about source identity creates association after mixing, even though each source separately has independent trials. Multiplying the marginal rates would describe independent redrawn sources instead.

### SB28

**1. Respect both the mixed sequence and unequal prior.** The likelihoods of HHT are $3/64$ and $9/64$. Prior weighting gives $2/64$ and $3/64$, with evidence $5/64$ and posterior $(2/5,3/5)$.

**2. Predict under that posterior.**

$$P(H_4\mid HHT)=\frac25\frac14+\frac35\frac34=\frac2{20}+\frac9{20}=\frac{11}{20}.$$

As a direct check, compute the joint HHTH probability as $(2/3)(3/64)(1/4)+(1/3)(9/64)(3/4)=11/256$. Dividing by $5/64$ gives $11/20$. A head count of two among three trials multiplies both history likelihoods by three and leaves this posterior unchanged, while its evidence probability triples.

### SB29

**1. Translate the stopping report into an exact path.** First head on toss three requires tails on tosses one and two followed by a head. The likelihoods are $8/64$ and $3/64$.

$$P(J=2\mid TTH)=\frac{(1/2)(3/64)}{(1/2)(8/64)+(1/2)(3/64)}=\frac3{11}.$$

The report favors the lower-rate coin because its two initial tails outweigh the final head. Multiplying both likelihoods by three would compute a different report, exactly one head in three trials. In this particular fixed-coin model that common factor happens to cancel from the posterior, so the numerical posterior coincides, but the absolute report probability differs. A numerical coincidence does not make the stopping and count events identical.

### SB30

**1. Complement the entire no-success history within each type.** The likelihoods are $1-(3/4)^3=37/64$ and $1-(1/4)^3=63/64$. The evidence includes all successful counts and all their compatible orders.

$$P(J=2\mid \text{at least one success})=\frac{63}{37+63}=\frac{63}{100}.$$

**2. Compare with stronger information quantitatively.** After three successes the posterior would be $27/(1+27)=27/28$, much larger. The coarse event still includes histories with only one success, which are comparatively compatible with the lower-rate source. It is invalid to replace an existential report by three successes, even when both reports truthfully say that success occurred.

### SB31

**1. Work on four ordered compositions.** BB, BG, GB, GG each have prior mass $1/4$. The at-least-one-boy event has likelihood vector $(1,1,1,0)$, giving BB joint mass $1/4$ and evidence $3/4$, hence posterior $1/3$.

**2. Change the report mechanism explicitly.** For a uniformly selected child, the likelihood vector is $(1,1/2,1/2,0)$. The report masses are $(2,1,1,0)/8$, giving BB posterior $2/4=1/2$.

The mixed compositions have one rather than two opportunities to show a boy under individual sampling. The sentence “a boy was observed” must therefore include how that observation was obtained. Both answers are correct under their own specified experiments.

### SB32

**1. Retain the report weights as functions of its mechanism.** The report mass is $(1+2r)/4$; BB contributes $1/4$. Therefore its posterior is $1/(1+2r)$ for every $0\le r\le1$.

**2. Solve the inverse condition with its domain.**

$$\frac1{1+2r}=\frac25\quad\Longleftrightarrow\quad5=2+4r\quad\Longleftrightarrow\quad r=\frac34.$$

This is admissible. Its report masses in sixteenths are $(4,3,3,0)/16$, so the BB share is $4/10=2/5$. The derivative $-2/(1+2r)^2<0$ shows that increasing mixed-family reporting reduces the BB posterior. The attainable range is $[1/3,1]$, so a requested posterior outside that interval would be impossible under this mechanism.

### SB33

**1. Clarify the population model.** Interpret the stated proportions as exact family proportions in a finite population with compatible counts, or as limiting family proportions with finite mean. A population of six families then has three of size one, two of size two, and one of size three.

**2. Count children rather than families.** Those groups contain three, four, and three children, ten in total. Uniform selection from the children therefore gives $(3/10,4/10,3/10)$.

The general transformation is $P_{\text{child}}(N=n)=n\pi_n/\sum_k k\pi_k$. If family sizes are independently random in a small finite population, the expected ratio of random child counts need not equal the ratio of expected counts. That unstated alternative model would require additional population information.

### SB34

**1. Make the observed door part of the evidence.** Under prize locations 1, 2, 3, the likelihoods of opening empty door 3 are $1/4,1,0$. Equal priors give joint masses $1/12,1/3,0$ and evidence $5/12$.

$$P(\text{prize 2}\mid \text{empty door 3 opened})=\frac{1/3}{5/12}=\frac45.$$

**2. Check the unconditional strategy by considering the other report.** Empty door 2 is opened with probability $7/12$; given that report, switching wins with probability $4/7$. Averaging gives $(5/12)(4/5)+(7/12)(4/7)=2/3$. Thus the specific conditional win rate four fifths is fully consistent with the unconditional two-thirds switching strategy.

### SB35

**1. Include both facts in the event.** The report is that door 3 was selected and that it was empty. Under prize 1 or 2 this happens with probability $1/2$; under prize 3 it cannot happen.

The equal-prior joint masses are $1/6,1/6,0$, so the event probability is $1/3$ and the remaining prize posteriors are $1/2,1/2,0$. Switching to door 2 wins with probability one half.

An informed host would open door 3 with certainty under prize 2; this ignorant host only does so half the time. That change in the likelihood is exactly why the classic switching posterior cannot be imported. Conditioning merely on “some opened door was empty” is another event, although symmetry here gives the same switching win probability.

### SB36

**1. Enumerate the equally likely primitive outcomes.** Unordered pairs number $\binom{10}{2}=45$. Their type counts are one HH, sixteen HL, and twenty-eight LL.

**2. Apply the equality-of-weight evidence.** Assuming each heavy coin has the same heavy weight and each light coin the same distinct light weight, the retained types are exactly HH and LL. The denominator contains $1+28=29$ pairs, of which one is HH.

$$P(HH\mid \text{equal weight})=\frac{1/45}{29/45}=\frac1{29}.$$

Squaring the single-coin heavy fraction gives $1/25$, the with-replacement HH prior, not even the correct without-replacement prior $1/45$. Equal prior probability for type labels HH and LL is also unjustified: these labels represent different numbers of pairs.

### SB37

**1. Distinguish card identities and visible faces.** There are six equally likely card-face positions. Three show red: both faces of RR and the red face of RB. Two of these three have a red hidden face.

**2. Express the same argument as Bayes weights.** The card-prior vector is $(1/3,1/3,1/3)$ and red likelihoods are $(1,1/2,0)$. Weighted masses are $(2,1,0)/6$, giving RR posterior $2/3$.

RR is exactly the event that the hidden face is red once the visible face is known red. Uniformly choosing among cards that possess at least one red face would use likelihoods $(1,1,0)$ and give one half. That altered selection rule counts cards, while the actual observation counts face opportunities.

### SB38

**1. Fix the actual identifier before evaluating its likelihood.** Since the sets are disjoint, the specified identifier has probabilities $1/2$ under source 1 and zero under source 2.

$$P(E)=\frac12\frac12+\frac12\,0=\frac14,\qquad P(H_1\mid E)=\frac{1/4}{1/4}=1.$$

**2. Locate the correct normalization axis.** Within source 1, summing over its two possible identifiers gives one. At this fixed identifier, summing over source labels gives only one half; likelihoods need not normalize along that axis. With equal priors, normalizing likelihoods alone happens to recover the posterior, but the evidence probability still needs the prior factor. The number of possible identifiers in source 2 is irrelevant for an identifier outside its support.

### SB39

**1. Separate failures before the accepted draw from the accepted type.** Let $K$ be the number of rejected pairs. Independence of regenerated pairs yields

$$P(K=k,\text{return }H_i)=(1-z)^k w_i,\qquad w_i=P(H_i\cap E),\quad z=P(E)>0.$$

**2. Sum all possible stopping times.** The geometric sum is $w_i/[1-(1-z)]=w_i/z$, exactly Bayes' posterior. The probability of never accepting is the limit of $(1-z)^k$, which is zero.

**3. Derive the computational cost.** For the number $T=K+1$ of generated pairs, $P(T>k)=(1-z)^k$. Summing these tail probabilities gives $E[T]=1/z$. This algorithm independently redraws the hypothesis after rejection; holding one hypothesis fixed would generally produce a different returned distribution.

### SB40

**1. Recover the target joint mass in each report.**

$$P(H\cap E_1)=\frac15\frac14=\frac1{20},\qquad P(H\cap E_2)=\frac3{10}\frac34=\frac9{40}.$$

Disjointness permits adding these to obtain $11/40$, while the union evidence probability is $1/2$. Their ratio is $11/20$.

**2. Reconstruct the conditional mixture.** Within the union, report 1 has weight $(1/5)/(1/2)=2/5$ and report 2 weight $3/5$. Hence $(2/5)(1/4)+(3/5)(3/4)=11/20$. The result lies between one quarter and three quarters. If the reports overlapped, these two weights would not form a partition and the same addition would double-count their intersection.

### SB41

**1. Invert the evidence-rate equation.**

$$\frac7{20}=p\frac45+(1-p)\frac15=\frac15+\frac35p.$$

Subtracting $1/5$ gives $3/20=(3/5)p$, so $p=1/4$. It lies in $[0,1]$ and the observed report rate lies between the two class likelihoods, as feasibility requires.

**2. Perform the inverse conditional calculation afterward.** Target alerts have mass $1/5=4/20$ and background alerts have mass $3/20$, giving posterior $4/7$. Estimating prevalence from the overall alert frequency is an inverse mixture problem; computing target probability among alerts is a subsequent Bayes problem. They request different quantities even though they share the same two class likelihoods.

### SB42

**1. Use a convex-combination bound before attempting normalization.** For target prior $p$, total evidence is $3/4-p/2$. Its maximum over $[0,1]$ is $3/4$, attained at $p=0$.

**2. Exhibit the algebraic contradiction.**

$$\frac45=\frac34-\frac p2\quad\Longrightarrow\quad p=-\frac1{10}.$$

The solution is outside the allowed prior domain and would give a negative target-evidence mass. Therefore no joint probability model satisfies all the supplied numbers. A negative answer is not a rare-class estimate to be rounded to zero; it is evidence of incompatible premises. Using $4/5$ as a denominator in Bayes anyway would conceal the failed law of total probability.

### SB43

**1. Invert an odds multiplier rather than confuse probabilities with odds.** Posterior probability $3/4$ corresponds to odds three. Dividing by the likelihood ratio six gives prior odds $1/2$ and therefore prior probability $1/3$.

**2. Verify with a general likelihood scale.** Let background likelihood be $c$ and target likelihood $6c$, where $0<c\le1/6$. The weighted masses under prior $1/3$ are $2c$ and $2c/3$. Their normalization is $2c/(8c/3)=3/4$.

The posterior is independent of this admissible common scale, but the evidence probability is $8c/3$ and varies with it. Thus the prior is identified by the supplied odds ratio while the absolute observation frequency is not.

### SB44

**1. Derive the response function from the actual likelihoods.** Canceling their common factor $1/5$ gives $g(p)=4p/[4p+(1-p)]=4p/(1+3p)$.

**2. Establish the location of the extrema.**

$$g'(p)=\frac{4(1+3p)-12p}{(1+3p)^2}=\frac4{(1+3p)^2}>0.$$

Therefore $g(1/10)=4/13$ is the minimum and $g(1/4)=4/7$ is the maximum. Both endpoint priors are allowed, so neither bound can be improved. This is a deterministic sensitivity interval for specified likelihoods, not a posterior probability interval for the unknown prior. A distribution over possible priors would require an additional hierarchical model.

### SB45

**1. Prove which corners control the posterior.** With $d=ps+(1-p)f$, the partial derivatives at an interior prior are

$$\frac{\partial r}{\partial s}=\frac{p(1-p)f}{d^2}>0,\qquad \frac{\partial r}{\partial f}=-\frac{p(1-p)s}{d^2}<0.$$

**2. Evaluate the admissible extreme pairs.** The minimum pair $(s,f)=(3/5,1/5)$ gives target/background masses $3/25,4/25$, hence $3/7$. The maximum pair $(4/5,1/10)$ gives masses $4/25,2/25$, hence $2/3$.

The statement explicitly allows every pair in the rectangle, so both extremes are attainable. If a shared detector constraint linked the two rates, independently choosing these corners might violate that constraint and cease to be sharp.

### SB46

**1. Differentiate using the fixed positive denominator.** Let $d=f+p(s-f)$. The quotient rule simplifies the first derivative to $sf/d^2$; differentiating again gives $-2sf(s-f)/d^3$.

**2. Separate three parameter regimes.** The first derivative is positive for all $s,f>0$. If $s>f$, the second derivative is negative and the response is concave; if $s<f$, it is positive and the response is convex. At equality the response is exactly $p$.

An increasing response when $s<f$ is not a contradiction: increasing the prior raises the posterior, although the same unfavorable report makes the posterior smaller than its corresponding prior. Curvature describes how the response changes as the prior varies, not whether this evidence favors the target.

### SB47

**1. Substitute the common likelihood without removing the prior.**

$$P(E)=pa+(1-p)a=a>0,\qquad P(H\mid E)=\frac{pa}{a}=p.$$

The complementary class posterior is $1-p$, so the complete class distribution is preserved.

**2. Distinguish two identification claims.** The observed event gives no class update, and even exact knowledge of its overall frequency supplies the equation $P(E)=a$, which contains no unknown $p$. Thus that frequency cannot identify prevalence. Equal likelihood for this one event does not prove that every possible observation has identical class distributions; another separately observed event could discriminate between classes. The positive assumption $a>0$ is necessary because at $a=0$ the evidence itself is impossible.

### SB48

**1. Construct joint tables instead of merely quoting feasible bounds.** With two marginal positive rates $3/4$, let the positive-positive cell be $q$. The cells $(++, +-, -+, --)$ are $(q,3/4-q,3/4-q,q-1/2)$. Nonnegativity is exactly $1/2\le q\le3/4$.

At $q=1/2$ the table is $(1/2,1/4,1/4,0)$; at $q=3/4$ it is $(3/4,0,0,1/4)$. Both are valid class-specific models. Equal class priors give two-positive weights $1/4$ and $3/8$, hence posterior $2/5$ for the first class.

Each individual positive has equal likelihood in the classes, yet their dependence patterns differ. Replacing both joint likelihoods by $9/16$ would erase the very information the report pair contains.

### SB49

**1. Apply each optimization criterion to its own objective.** Maximum likelihood compares $1/5$ and $4/5$, so it selects class 2. Maximum posterior compares $9/50$ and $4/50$, so it selects class 1.

**2. Verify the posterior and its classification risks.** Total evidence is $13/50$, giving posterior $(9/13,4/13)$. Under zero-one error loss, predicting class 1 has risk $4/13$ and predicting class 2 has risk $9/13$. Class 1 is therefore the unique lower-risk label.

The observation favors class 2 by a likelihood ratio four, but the prior odds favor class 1 by nine. Their combined posterior odds remain $9/4$ for class 1. This is a fully quantified disagreement, not a failure of either arithmetic rule.

### SB50

**1. Multiply each error cost by the posterior probability of making that error.** Predicting target errs only when background is true; predicting background errs only when target is true.

$$R(\text{target})=1\frac{11}{13}=\frac{11}{13},\qquad R(\text{background})=9\frac2{13}=\frac{18}{13}.$$

Choose target because its expected cost is lower by $7/13$. A risk greater than one is permitted because risk is measured in cost units, not probability units.

**2. Check the threshold direction.** Target is optimal when $(1-r)\le9r$, equivalently $r\ge1/10$. Here $2/13>1/10$ even though it is below one half. The posterior remains $2/13$ throughout; changing a decision objective does not create new evidence.

### SB51

**1. Convert the cost comparison to odds.** The target action is optimal when $2(1-r)\le8r$, or $r/(1-r)\ge1/4$. Prior target odds are $1/19$.

$$\frac{LR}{19}\ge\frac14\quad\Longleftrightarrow\quad LR\ge\frac{19}{4}.$$

**2. Verify equality and interpret strict preference.** At $LR=19/4$ the posterior odds are $1/4$, so $r=1/5$. Both risks equal $8/5$ cost units. Ratios strictly larger than $19/4$ strictly prefer target; equality allows either label. The requested minimum supporting an optimal target action includes the tie. A ratio just above one increases target belief but still leaves it below this decision threshold.

### SB52

**1. Enumerate the truth states where each prediction loses.** For label 1 the loss is one in classes 2 and 3, hence risk $3/7+2/7=5/7$. For label 2 it is $2/7+2/7=4/7$. For label 3 it is $2/7+3/7=5/7$.

**2. Generalize the derivation.** For any posterior vector $(r_1,\ldots,r_m)$ and zero-one loss,

$$R(i)=\sum_{j\ne i}r_j=1-r_i.$$

Minimizing this expression is exactly maximizing $r_i$. Here the maximum is unique at class 2. If two classes had equal largest posterior, both deterministic labels and every randomized mixture between them would attain the same minimum risk. This conclusion relies on the specified symmetric unit-error loss.

### SB53

**1. Include abstention among the candidate actions.** Label target has risk $2/5$, label background risk $3/5$, and abstention risk $1/4$. Since $1/4<2/5<3/5$, abstention is uniquely optimal.

**2. Locate the general abstention region.** For posterior $r$ and constant abstention cost $c$, abstention is optimal when $c\le r$ and $c\le1-r$, or $c\le r\le1-c$. With $c=1/4$, this interval is $[1/4,3/4]$, and $r=3/5$ lies strictly inside it. Endpoints permit a tie with one label. For $c>1/2$, no posterior makes abstention strictly preferable to both labels. This illustrates why the available action set must be stated before invoking maximum posterior.

### SB54

**1. Calculate the observational ratio on the two supported states.** Both $P(A=1)$ and $P(A=1,B=1)$ equal one half, so $P(B=1\mid A=1)=1$.

**2. Give two compatible causal constructions.** In a common-cause model use structural equations $A=C$, $B=C$. Replacing only the equation for $A$ by the external setting one leaves $B=C$, so its success probability is one half. In another model use $A=C$, $B=A$; the observed joint law is identical, but the same intervention now makes $B=1$ certain.

These two constructions have identical observational data and different intervention answers. Therefore the observational distribution cannot identify the intervention effect without causal assumptions. Conditioning and replacing a structural equation perform different mathematical operations.

### SB55

**1. Derive the exact ratio before computing decimal products.** The likelihoods are $100^{-1000}$ and $200^{-1000}$, both positive. Their ratio is $2^{1000}$, so the first posterior is $1/(1+2^{-1000})$.

**2. Normalize shifted log weights.** Let $a=-1000\log100$ and $b=-1000\log200$, ignoring their common log prior. Subtract $a$, the larger value. Exponentiation gives weights one and $\exp(b-a)=2^{-1000}$, avoiding two tiny unscaled products.

**3. Report finite precision honestly.** Ordinary floating-point addition may still round $1+2^{-1000}$ to one. To retain the small complementary posterior, compute it separately as $2^{-1000}/(1+2^{-1000})$ or retain logarithms/high precision. A displayed one is an approximation, not proof that the other hypothesis is impossible.

### SB56

**1. Normalize prior times likelihood.** The uniform prior density is one on $[0,1]$, and the one-head likelihood is $\theta$. The normalizer is $[\theta^2/2]_0^1=1/2$, giving density $2\theta$.

**2. Integrate the requested event and prediction separately.**

$$P(\Theta>1/2\mid H)=\int_{1/2}^{1}2\theta\,d\theta=\frac34,\qquad P(H_2\mid H)=\int_0^1\theta\,2\theta\,d\theta=\frac23.$$

The interval event integrates the posterior density over selected parameter values; the prediction integrates a future-head likelihood against the whole posterior. Neither result is a density height or a probability of an exact parameter point. Conditional independence of tosses given the fixed rate justifies the predictive integrand.

### SB57

**1. Use the exact observed history.** Two heads and one tail in a specified order have likelihood $\theta^2(1-\theta)$. Its integral under the uniform prior is $[\theta^3/3-\theta^4/4]_0^1=1/12$, so the density is $12\theta^2(1-\theta)$.

**2. Predict one more head by adding one likelihood factor.**

$$P(H_{\text{next}}\mid HHT)=12\int_0^1(\theta^3-\theta^4)\,d\theta=12\left(\frac14-\frac15\right)=\frac35.$$

The empirical head fraction $2/3$ is a different statistic. A report of the unordered count would multiply likelihood and normalizer by three, leaving the posterior unchanged. Its evidence probability would be $1/4$ instead of $1/12$; canceling a common factor does not make those evidence events identical.

### SB58

**1. Verify the proposed prior before updating it.** The density $2\theta$ is nonnegative and integrates to one. Multiplication by the one-tail likelihood gives $2\theta(1-\theta)$, whose integral is $2(1/2-1/3)=1/3$.

**2. Normalize and predict.** The posterior is $6\theta(1-\theta)$, with mean

$$\int_0^1\theta\,6\theta(1-\theta)\,d\theta=6\left(\frac13-\frac14\right)=\frac12.$$

A uniform prior would instead give one-tail density $2(1-\theta)$ and mean $2(1/2-1/3)=1/3$. The first prior initially favors larger head rates, so one tail need not lower its predictive rate as far as the uniform-prior update. Both calculations obey the same normalization rule.

### SB59

**1. Retain the boundary term explicitly.** For $t\ge1$, integration by parts gives

$$I(h,t)=\left[\frac{u^{h+1}(1-u)^t}{h+1}\right]_0^1+\frac{t}{h+1}I(h+1,t-1).$$

Both endpoint contributions vanish only in this stated $t\ge1$ case. Repeating the recurrence gives

$$I(h,t)=\frac{t!}{(h+1)(h+2)\cdots(h+t)}I(h+t,0)=\frac{h!t!}{(h+t+1)!}.$$

**2. Supply the terminating case.** For $t=0$, direct integration gives $I(h,0)=1/(h+1)$. When also $h=0$, the integral is one. Applying the zero-boundary recurrence at $t=0$ would discard the nonzero upper endpoint and falsely give zero. A base case is part of the proof, not an optional numerical check.

### SB60

**1. Express prediction as a ratio of normalization integrals.** The posterior after the observed counts is $\theta^h(1-\theta)^t/I(h,t)$. Conditional on $\theta$, the next head has probability $\theta$, hence prediction is $I(h+1,t)/I(h,t)$.

**2. Cancel the factorials explicitly.**

$$\frac{(h+1)!t!}{(h+t+2)!}\frac{(h+t+1)!}{h!t!}=\frac{h+1}{h+t+2}.$$

At $(h,t)=(7,3)$ this is $8/12=2/3$. With no observations it returns $1/2$, the uniform prior mean. The expression is a posterior weighted prediction for a shared rate. A model that redraws an independent rate from the prior before every toss would retain predictive probability one half, regardless of previous counts.

### SB61

**1. Normalize the three-head likelihood.** Its uniform-prior integral is $\int_0^1\theta^3d\theta=1/4$, so the density is $4\theta^3$.

**2. Evaluate two different mathematical objects.** At rate $9/10$ the density height is $4(729/1000)=729/250$. The tail probability is

$$\int_{9/10}^{1}4\theta^3\,d\theta=1-\left(\frac9{10}\right)^4=\frac{3439}{10000}.$$

The first value is probability mass per unit rate; the second is dimensionless total mass over an interval. The exact-point probability remains zero. A quick tail check is that the interval has width one tenth and density at most four, so its probability is at most $2/5$, consistent with the computed $3439/10000$.

### SB62

**1. Compute the distribution function including its boundary pieces.** It is zero for $u<0$, $\sqrt u$ for $0\le u\le1$, and one for $u>1$, because the square function is increasing on the original support.

**2. Differentiate on the interior and check the singular endpoint.** The density is $1/(2\sqrt u)$ for $0<u<1$. Its improper integral from zero to one is $[\sqrt u]_0^1=1$, and its distribution function has no jump at zero, so there is no atom there.

For example $P(U\le1/4)=1/2$, not the $1/4$ that a uniform $U$ prior would assign. Thus uniformity is a coordinate-specific modeling choice. The infinite limiting density at zero does not create positive probability at the single point zero.

### SB63

**1. Keep the evidence positive along each approach.** For $0<\varepsilon\le1$, the first path has evidence $\varepsilon$ and first-hypothesis posterior one half. The second has evidence $(\varepsilon+\varepsilon^2)/2$ and posterior $1/(1+\varepsilon)$.

**2. Compare the limits with the limiting model.** The two posteriors approach $1/2$ and one, respectively. Both likelihood vectors approach $(0,0)$, for which total evidence is zero and the elementary ratio is undefined.

More generally paths $(a\varepsilon,b\varepsilon)$ with fixed $a,b>0$ approach posterior $a/(a+b)$ whenever epsilon is sufficiently small to keep likelihoods admissible. Many interior limits are therefore possible. A chosen limiting posterior contains information about the approach path that the zero-evidence model itself does not contain.
