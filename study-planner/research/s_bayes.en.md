# Bayes' Rule, Base Rates, and Evidence

## Written courses and the scope of this synthesis

This chapter combines written instruction from MIT, Stanford, Carnegie Mellon, Oxford, and Berkeley. The four primary selections are MIT 6.1200J/18.062J (Lecture 19), Stanford CS109 (total probability and Bayes' theorem), Carnegie Mellon's *Introduction to Probability for Computing* (Chapter 2), and Oxford SC7 *Bayes Methods* (the opening inference and decision sections). Berkeley STAT 134 supplies a fifth reading on the observation protocol and the hidden-coin model. The [source-selection audit](../reviews/s_bayes-sources.html) identifies the accessible candidate pool, actual reading ranges, selection criteria, failed acquisitions, and exercise coverage. Different pages of one course do not count as different universities.

The prerequisite is the conditional-probability chapter. You should be able to distinguish an event from its probability, factor a joint probability along a history, and recognize a disjoint exhaustive partition. The main development is discrete and requires only algebra, finite sums, geometric series, combinations, and elementary inequalities. An explicitly labeled final bridge uses integration to explain continuous parameter inference; no density is silently treated as a point probability.

The organizing question is precise: a hidden state produced an observed event; how should the observation change the state's probability? We derive the answer, establish when it is defined, and examine how the answer changes when the observation mechanism changes. Two authentic Iranian questions are revisited through the new tools, with links to the original pages. Sixty-three additional problems give complete mathematical and conceptual solutions. Their assessed difficulty is medium to hard; it is not an empirically calibrated difficulty score.

The [quality audit](../reviews/s_bayes-quality.html) records mathematical checks, rendered figures, typography, exact laboratory results, animation controls, and the remaining verification limits.

## Partitions and the law of total probability

### Why the denominator must account for every way the observation can occur

Let the events $H_1,\ldots,H_m$ be disjoint and cover the sample space. These hypotheses might identify the selected factory, coin, family size, or source of a message. Their prior probabilities are $\pi_i=P(H_i)$, with $\pi_i\ge0$ and $\sum_i\pi_i=1$. For positive-prior strata define $L_i=P(E\mid H_i)$. The quantity $L_i$ is the likelihood of the observed event under that hypothesis. It is a probability over observations when the hypothesis is fixed; the list of likelihoods across hypotheses need not sum to one.

Because $E$ is the disjoint union of $E\cap H_i$, countable additivity and multiplication give

$$P(E)=\sum_{i=1}^{m}P(E\cap H_i)=\sum_{i=1}^{m}\pi_iL_i.$$

This is the law of total probability. Its weighted structure is essential: a rare high-likelihood source can contribute less evidence mass than a common low-likelihood source. An unweighted average applies only when the stratum probabilities really are equal. If a stratum has zero prior mass, its joint mass is zero and it contributes zero directly; the conditional probability on that null stratum is not defined by the elementary ratio definition. Do not write an undefined conditional merely because it is multiplied by zero.

For countably many strata the same proof applies to a nonnegative series. No cancellation or rearrangement of a conditionally convergent signed series is involved. The family-size examination problem later uses precisely this extension. If $C$ is already known and $P(C)>0$, perform the entire calculation in the conditional measure:

$$P(E\mid C)=\sum_i P(H_i\mid C)P(E\mid H_i\cap C).$$

Only strata with positive $P(H_i\cap C)$ require a conditional likelihood. Mixing prior weights from the original population with likelihoods from a selected subgroup usually describes no coherent model.

### A three-source derivation

Suppose the priors are $(1/2,1/3,1/6)$ and an alert has likelihoods $(1/10,1/5,3/5)$. The three joint alert masses are $1/20$, $1/15$, and $1/10$. Their sum is $13/60$. These numbers account for every alert exactly once because source membership is a partition. If two candidate events overlap, this summation double-counts the overlap. Replace them by disjoint cells before using total probability.

<!-- FIGURE:partition -->

## Bayes' rule and posterior normalization

### Derivation from two factorizations of the same intersection

For $P(E)>0$ and a positive-prior $H_i$, the intersection has two descriptions:

$$P(H_i\cap E)=P(H_i)P(E\mid H_i)=P(E)P(H_i\mid E).$$

Consequently,

$$P(H_i\mid E)=\frac{\pi_iL_i}{\sum_j\pi_jL_j}.$$

The prior describes uncertainty before this evidence, the likelihood describes how the evidence is produced inside a hypothesis, the evidence probability normalizes the retained mass, and the posterior describes uncertainty after the evidence. The numerator is a *joint* probability, not an isolated likelihood. The denominator is the same positive number for every hypothesis. Summing the posterior probabilities gives one, which is a useful arithmetic check and follows directly from the partition.

For the three-source model, the posterior vector is $(3/13,4/13,6/13)$. The least common source becomes most likely because its alert likelihood compensates for its smaller prior. Neither choosing the largest prior nor choosing the largest likelihood alone is a general inference rule. The expression $P(H_i\mid E)$ reverses the conditioning direction; it does not assert that the observation causes the hidden state.

### What can be canceled, and what cannot

If every likelihood is multiplied by the same positive constant and remains compatible with the stated observation model, the posterior ratios are unchanged. This explains why unnormalized likelihood weights can be used when a common factor is omitted. Such weights must not be relabeled as the actual probabilities $P(E\mid H_i)$ or used to report the absolute evidence probability. Hypothesis-specific factors do not cancel. A count likelihood includes a common binomial coefficient only when all hypotheses refer to the same number of exchangeable trials and the same observed count.

Zero prior mass remains zero after any event with positive evidence mass. Zero likelihood also yields zero posterior for that hypothesis. If all weighted likelihoods vanish, the evidence is impossible under the model: Bayes' formula is undefined. Neither equal posteriors nor a forced posterior of zero is a valid repair. Reconsider the model or the observation description. A limiting sequence can yield different answers depending on how the impossible event is approached.

<!-- FIGURE:normalization -->

## Natural frequencies and base-rate effects

### A synthetic alert model with exact counts

Consider a purely educational detector. The target class has prevalence $p=1/100$, the alert probability inside that class is $s=9/10$, and the alert probability outside that class is $f=1/20$. These are specified mathematical probabilities, not empirical medical or operational advice. In a synthetic population of 2,000 weighted cases there are 20 target cases and 1,980 other cases. Alerts retain 18 target cases and 99 other cases. Therefore

$$P(H\mid +)=\frac{18}{18+99}=\frac{2}{13}.$$

The same algebra gives $ps/[ps+(1-p)f]$. A detector that alerts on 90 percent of target cases need not make an alert 90 percent credible. The much larger background population contributes many false alerts. The frequency display is an exact representation of rational probabilities; it is not a claim that every real sample of 2,000 has those counts.

The non-alert population contains 2 target cases and 1,881 other cases, so $P(H\mid -)=2/1883$. The probability of being outside the class given no alert is $1881/1883$. Keep the target and conditioning direction explicit. Sensitivity is $s$, specificity is $1-f$, the false-negative rate is $1-s$, and the false-positive rate is $f$. None of these is the positive predictive value without a prevalence.

### Overall accuracy is another weighted quantity

If alert means predicting the target class, overall accuracy is

$$P(\text{correct})=ps+(1-p)(1-f).$$

This quantity can be large in a rare-class population even when alerts are usually false. Conversely, the trivial always-background classifier has accuracy $1-p$ but detects none of the target cases. A question asking for accuracy, sensitivity, or posterior credibility requests different conditional or joint quantities. Constructing the full four-cell table prevents accidental substitution.

<!-- FIGURE:frequencies -->

## Posterior odds, likelihood ratios, and evidence strength

Assume both binary priors are positive and both likelihoods are positive. Divide the two Bayes expressions:

$$\frac{P(H\mid E)}{P(H^c\mid E)}=\frac{P(H)}{P(H^c)}\frac{P(E\mid H)}{P(E\mid H^c)}.$$

Posterior odds equal prior odds times the likelihood ratio. For a positive detector observation the ratio is $s/f$; for a negative observation it is $(1-s)/(1-f)$. A ratio above one favors $H$ relative to its competitor, a ratio below one favors the competitor, and a ratio of one leaves the odds unchanged. It does not follow that a ratio above one makes the posterior exceed one half. With prior odds $1/99$ and ratio 18, the posterior odds are $2/11$, hence posterior probability $2/13$.

For any two hypotheses in a larger partition, the posterior pairwise odds use their own priors and likelihoods. The other hypotheses cancel in the ratio but remain necessary to normalize the complete posterior vector. Pairwise odds identify relative support; they are not automatically a binary probability unless the pair is exhaustive or the conditioning explicitly restricts attention to that pair.

The log-odds representation turns multiplication into addition. For positive finite odds,

$$\log O(H\mid E)=\log O(H)+\log\frac{P(E\mid H)}{P(E\mid H^c)}.$$

This is helpful for long histories and numerical stability. Boundary priors or zero likelihoods need separate treatment rather than a finite logarithm of zero. The likelihood ratio measures evidence *relative to the specified competitor*: there is no universal evidence score independent of the competing model.

<!-- FIGURE:odds -->

## Repeated evidence and the full observation history

### The universally valid sequential update

Let $E_1,\ldots,E_n$ denote observed events and let $D_{t-1}$ be their intersection through time $t-1$. At an update with positive $P(D_{t-1})$ and $P(E_t\mid D_{t-1})$, use

$$P(H_i\mid D_{t-1}\cap E_t)=\frac{P(H_i\mid D_{t-1})P(E_t\mid H_i\cap D_{t-1})}{P(E_t\mid D_{t-1})}.$$

The new likelihood generally depends on the history. Only a stated conditional-independence model permits replacing it by a history-free likelihood. If observations are independent conditional on each fixed hypothesis, the joint likelihood factors into their product. Marginal independence of observations is neither necessary nor sufficient for that replacement.

Take prior $1/10$, positive likelihoods $4/5$ and $1/5$ in the two classes, and conditionally independent repetitions. Each positive has likelihood ratio four. After two positives the odds are $16/9$, so the posterior is $16/25$. After one positive it is $4/13$. If the second report merely copies the first report, its likelihood given the first positive is one under either remaining hypothesis. The second likelihood ratio is one and the posterior stays $4/13$. Squaring the first likelihood would count the same observation twice.

### Fixed latent state versus a state redrawn on every trial

A coin is chosen once from a fair coin and a coin with head probability $9/10$, with equal priors. Three heads have likelihoods $1/8$ and $729/1000$. The biased-coin posterior is $729/854$. The next-head probability is a posterior mixture:

$$P(\text{next head}\mid HHH)=\frac{125}{854}\frac12+\frac{729}{854}\frac9{10}=\frac{3593}{4270}.$$

The predictive probability is not $9/10$ merely because the biased coin is the most likely hypothesis. Uncertainty about coin identity remains, so both type-specific predictions receive their posterior weights. The rational expression also provides an exact check on a rounded decimal calculation.

If a fresh coin identity is independently selected on every trial, past heads do not update the identity of the next coin. The next-head probability then stays $7/10$. The phrases “chosen once” and “chosen anew” define different models and cannot be omitted from an exam solution.

For without-replacement sampling, use evolving conditional counts inside each hypothesis. If observing two red draws is the evidence, the likelihood is a product of two changing proportions. It is generally not the square of the initial red proportion. Observing an unordered count additionally sums disjoint orders, or uses the corresponding combination count.

## Observation protocols, selection, and reporting

### Evidence is the actual report, not just a sentence that is true

Suppose a two-child family has four equiprobable ordered compositions. Conditioning on “at least one child is a boy” leaves three compositions and gives $P(BB\mid\text{at least one boy})=1/3$. If one uniformly selected child is observed to be a boy, the report likelihoods are one for $BB$, one half for each mixed composition, and zero for $GG$. Bayes then gives one half. Both reports are truthful; they are different random events.

This is a general selection principle. A source that has more opportunities to generate the observed report can become more likely. Observing a uniformly selected individual does not usually sample families uniformly. If the family-size prior is $\pi_n$ and an individual is drawn uniformly from a large population of all children, the corresponding family-size weights are proportional to $n\pi_n$, subject to finite positive mean. A report mechanism must be specified before computing its likelihood.

### A host's informed choice

You initially choose door 1. The prize is uniformly behind one of three doors. A knowledgeable host always opens an unchosen empty door and always offers a switch. If the prize is behind door 1, let the host open door 3 with probability $q$. If the prize is behind door 2, the host must open door 3; if it is behind door 3, the observed opening is impossible. Given the specific report “door 3 is opened,” the posterior weights are proportional to $(q,1,0)$ and switching to door 2 wins with probability $1/(1+q)$.

With symmetric tie-breaking $q=1/2$, this is $2/3$. At $q=1$ it is $1/2$ for this particular report, despite the unconditional always-switch win probability remaining $2/3$. If an ignorant host instead chooses a random unchosen door and the observed door happens to be empty, the retained likelihoods for prize doors 1 and 2 are both $1/2$, giving a switching posterior of $1/2$. Information about the host is part of the likelihood model, not decorative wording.

<!-- FIGURE:protocol -->

## Sensitivity, inverse problems, and sharp thresholds

For fixed positive $s$ and $f$, define the posterior response

$$g(p)=\frac{ps}{ps+(1-p)f}.$$

Let $d=f+p(s-f)$. Differentiation yields $g'(p)=sf/d^2>0$. Thus an interval of plausible priors $[a,b]$ gives the exact posterior interval $[g(a),g(b)]$. This is a sensitivity calculation within fixed likelihoods, not uncertainty propagation for unknown rates. If $s$ or $f$ also varies, their ranges and any compatibility constraints must be incorporated separately.

For $0<q<1$, solving $g(p)\ge q$ gives

$$p\ge\frac{qf}{s(1-q)+qf}.$$

The denominator is positive under the stated assumptions, so multiplying an inequality does not reverse its direction. This formula quantifies the base rate needed for a target credibility. It includes $q=1/2$ as the threshold $f/(s+f)$. For fixed prior and sensitivity, solving instead for the false-positive rate gives $f\le ps(1-q)/[q(1-p)]$, when $0<p<1$. Values outside $[0,1]$ need interpretation as vacuous or infeasible requirements rather than detector probabilities.

The evidence rate alone does not generally identify prior and likelihoods. If $s$ and $f$ are known and different, $P(+)=f+p(s-f)$ identifies $p$. If $s=f$, every prior produces the same alert rate, so the prior is unidentifiable from that rate. If the observed rate falls outside the interval between $s$ and $f$, no admissible prior fits the model. A posterior number without its likelihood assumptions also cannot identify a unique prior.

Coarsening observations is another weighted average. If disjoint reports $E_1,E_2$ are merged into $E$, the posterior under $E$ is the average of the report-specific posteriors weighted by $P(E_j\mid E)$. It must lie between them in the binary case. Refinement need not always increase the posterior of a particular hypothesis: the direction depends on the observed subevent.

<!-- FIGURE:sensitivity -->

## Inference versus decisions under unequal error costs

The most likely hypothesis minimizes the conditional probability of a wrong label under equal zero-one loss. To prove it, the expected loss of predicting $H_i$ is $1-P(H_i\mid E)$, minimized by the largest posterior. Maximum likelihood instead maximizes $P(E\mid H_i)$. These choices agree with equal priors but can disagree otherwise.

Let the cost of a false positive be $c_{FP}>0$ and of a false negative be $c_{FN}>0$, with zero loss for a correct decision. If the posterior target probability is $r$, the expected losses of choosing target and background are $c_{FP}(1-r)$ and $c_{FN}r$. Choosing target is optimal exactly when

$$r\ge\frac{c_{FP}}{c_{FP}+c_{FN}}.$$

At equality the actions tie. In odds form, choose target if posterior odds are at least $c_{FP}/c_{FN}$. The costs alter the action threshold, not Bayes' posterior itself. With costs $1$ and $9$, posterior $2/13$ is below one half but above one tenth, so the optimal costly-error decision is target. Real costs must be specified; an exercise cannot infer them from probability rates.

Conditioning still does not identify causal effects. A detector report and its target can be statistically associated through a common hidden variable, and selection can create dependence. A Bayesian calculation is valid for the specified joint model even when no causal direction has been established. Changing the process by intervention requires an intervention model, not reversal of the conditional bar.

## A carefully bounded bridge to continuous inference

This section previews later random-variable and statistics chapters. If a parameter $\Theta$ has prior density $\pi(\theta)$ and data $x$ have likelihood density or mass $f(x\mid\theta)$, a regular conditional posterior density at observations with positive finite marginal density is

$$\pi(\theta\mid x)=\frac{f(x\mid\theta)\pi(\theta)}{\int f(x\mid u)\pi(u)\,du}.$$

The denominator is a marginal density when $x$ is continuous; it is not the positive probability of a singleton observation. Posterior probabilities of parameter intervals require integrating the posterior density. A density can exceed one without violating the bound on probabilities. The discrete normalization proof becomes an integral normalization argument, under the existence and integrability assumptions of this density model.

For a coin's unknown head rate $\theta\in[0,1]$, use a uniform prior and conditionally independent Bernoulli tosses. After $h$ heads and $t$ tails in a specified order, the likelihood is $\theta^h(1-\theta)^t$. For an unordered count, the binomial coefficient is constant in $\theta$ and cancels. Define

$$I(h,t)=\int_0^1 u^h(1-u)^t\,du.$$

For nonnegative integers, $I(h,0)=1/(h+1)$. For $t\ge1$, integration by parts gives $I(h,t)=t I(h+1,t-1)/(h+1)$; the boundary term vanishes. Induction yields $I(h,t)=h!t!/(h+t+1)!$. Thus the normalized posterior is $\theta^h(1-\theta)^t/I(h,t)$, and the next-head predictive probability is

$$\frac{I(h+1,t)}{I(h,t)}=\frac{h+1}{h+t+2}.$$

After one head the density is $2\theta$, the probability that $\Theta>1/2$ is $3/4$, and the next-head probability is $2/3$. These are different outputs: interval probability, predictive probability, and density. A uniform prior is a modeling assumption, not a universal absence of information; after a nonlinear reparameterization the induced density is generally not uniform. This bridge does not teach general Markov-chain Monte Carlo, hierarchical estimation, or every advanced Bayesian method in the Oxford course.

<!-- FIGURE:density -->

## Implementing an update and checking its numerical meaning

For finite hypotheses, store nonnegative rational priors and likelihoods. Compute weighted joint masses, reject zero total evidence, and normalize every mass by the same evidence. Exact rational arithmetic avoids premature rounding and makes the sum-to-one test exact. The interactive laboratory below accepts integer fractions and exposes every intermediate result.

```python
from fractions import Fraction

def posterior(priors, likelihoods):
    if len(priors) != len(likelihoods) or not priors:
        raise ValueError("One likelihood is required per hypothesis.")
    if any(p < 0 for p in priors) or sum(priors) != 1:
        raise ValueError("Priors must be nonnegative and sum to one.")
    if any(l < 0 or l > 1 for l in likelihoods):
        raise ValueError("Event likelihoods must be probabilities.")
    weights = [p * l for p, l in zip(priors, likelihoods)]
    evidence = sum(weights, Fraction(0))
    if evidence == 0:
        raise ValueError("The observation is impossible in this model.")
    return evidence, [w / evidence for w in weights]
```

For many small likelihood factors, floating-point products can underflow even when the mathematical evidence is positive. Work with log weights: add log prior and log likelihoods, subtract the largest finite log weight, exponentiate the shifted values, and normalize. The common positive rescaling preserves the posterior. An all-negative-infinity vector means that every represented weight is zero and needs an explicit error, not subtraction of negative infinity from itself. Numerical stability cannot repair an incorrect conditional-independence assumption.

## Fully solved mathematical and conceptual problems

Use each solution as a lesson in modeling and proof. State the evidence, identify the partition, compute likelihoods under each hypothesis, normalize, and explain why the main tempting shortcut fails. The two authentic items also appeared in the prerequisite chapter; they are intentionally revisited through total-probability and posterior methods. Extensions with different questions are labeled original rather than additional authentic examination items. The course-derived inventory is in the source audit; this bank does not reproduce every exercise from every source book.

<!-- INCLUDE:problems -->

## Complete summary and examination rules

<!-- INCLUDE:review -->

## Exact posterior laboratory

The default detector uses prior $1/100$, target likelihood $9/10$, and background likelihood $1/20$. Change these values to observe the base-rate effect. Repetitions mean independent reports conditional on the same fixed hidden state. Selecting the duplicate-report model keeps the one-report likelihood, because copying an observation adds no new evidence. The laboratory states which model is being used and refuses impossible observations.

<!-- LAB:bayes -->

## References and reading boundaries

1. MIT — Zachary Abel, Ben Chapman, Erik Demaine — *6.1200J/18.062J Mathematics for Computer Science*, Spring 2024, [Lecture 19](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/mit6_1200j_s24_lec19.pdf), PDF pages 1–8; Bayes, odds, selection, and background information on pages 4–7.
2. Stanford University — Chris Piech — *CS109 Probability for Computer Scientists*, [Law of Total Probability](https://chrispiech.github.io/probabilityForComputerScientists/en/part1/law_total/) and [Bayes' Theorem](https://chrispiech.github.io/probabilityForComputerScientists/en/part1/bayes_theorem/), complete instructional bodies.
3. Carnegie Mellon University — Mor Harchol-Balter — *Introduction to Probability for Computing*, [Chapter 2: Probability](https://www.cs.cmu.edu/~harchol/Probability/chapters/chpt2.pdf), PDF pages 11–21; Theorems 2.18–2.21 and the screened exercise inventory in the source audit. Public book context: [course/book page](https://www.cs.cmu.edu/~harchol/Probability/book.html).
4. University of Oxford — Geoff K. Nicholls — *SC7 Bayes Methods*, Michaelmas Term 2025, [course notes](https://www.stats.ox.ac.uk/~nicholls/BayesMethods/BLnotes25MT.pdf), PDF pages 6–15, especially Sections 1.2.1 and 1.3.1–1.3.7. Later computation and model-selection chapters are outside this chapter's reading claim.
5. University of California, Berkeley — David Aldous — *STAT 134*, [Lecture 3](https://www.stat.berkeley.edu/~aldous/134/lecture3.pdf), PDF pages 1–10; reporting protocol and hidden-coin prompts. Calculations omitted from lecture slides are independently derived here.
6. Iranian examination archive — [Phd-Exam-CSE](https://github.com/bheydari721rn24/Phd-Exam-CSE/tree/bdadf6e2c9cadc4772ae137a96a3da753c7cfd08/Exams), CS doctoral 1404 Q69 (PDF page 15), CE master's 1405 Q35 (PDF page 8). Translations were checked against rendered originals; all answers here are independently derived, not an official key.
