# Conditional Probability, Multiplication, and Independence

## Written courses and the synthesis used here

This chapter combines four primary courses from four universities: MIT 6.041SC, Stanford CS109, Carnegie Mellon's Introduction to Probability for Computing, and Berkeley STAT 134. Oxford Part B Applied Probability supplies an additional, explicitly bounded reading on conditioning at continuous observations. The [source-selection audit](../reviews/s_conditional-sources.html) records the candidate pool, the material actually read, its fingerprints, and the reasons for selection. It does not claim that every probability course in the world was accessible or examined.

Read the probability axioms and counting chapters first. You need intersections, unions, complements, disjoint partitions, finite and geometric sums, and combinations. No named probability distribution is required for the main arguments: when a success-count formula appears, it is derived by counting disjoint patterns. The chapter develops conditioning on events, multiplication along histories, sampling without replacement, independence, conditional independence, observation protocols, and reliability. Systematic posterior odds, likelihood ratios, and inference with several competing hypotheses belong to the next chapter on Bayes' rule; the ratio identities needed here are proved here rather than assumed.

The instruction and solutions are original English explanations. University exercise structures are identified where adapted; source wording, slides, and figures are not reproduced wholesale. Four translated Iranian examination questions are linked to their original booklet, question number, PDF page, and repository revision. Their answers are derived here and are not presented as an official answer key.

## Conditioning defines a new probability measure

### What the vertical bar actually means

Let $A$ be the target event and $B$ the information available. With $P(B)>0$, define

$$P(A\mid B)=\frac{P(A\cap B)}{P(B)}.$$

The numerator retains the outcomes compatible with both the target and the information. The denominator is the probability mass of every outcome compatible with the information. The result is a proportion *within that mass*. The bar does not mean division of $P(A)$ by $P(B)$, an implication, a temporal ordering, or a causal intervention. You can condition an earlier event on a later observation. What matters is the specified joint probability model.

In a finite model with outcome weights $p_\omega$, the conditional weight of an outcome in $B$ is $p_\omega/P(B)$; an outcome outside $B$ receives conditional weight zero. Conditioning preserves ratios among retained weights. It does not make previously unequal outcomes equally likely. If all original outcomes are equally likely, the common weight cancels, yielding $|A\cap B|/|B|$. Counting is a special case of the weighted definition.

**Worked weighted example.** Four outcomes have probabilities $1/10,2/10,3/10,4/10$. Let $A$ consist of the first and third outcomes and $B$ of the first two. The retained mass is $3/10$; the target mass within it is $1/10$. Thus $P(A\mid B)=1/3$, whereas simply counting the retained outcomes would incorrectly give $1/2$. Reversing the question gives $P(B\mid A)=1/4$. One joint mass can produce two different conditionals because their denominators differ.

<!-- FIGURE:atoms -->

### Why the ordinary probability laws remain valid

For a fixed positive-probability event $B$, write $Q(E)=P(E\cap B)/P(B)$. Nonnegativity follows from nonnegativity of $P$; normalization follows from $Q(\Omega)=P(B)/P(B)=1$. If the events $E_i$ are pairwise disjoint, the events $E_i\cap B$ are also pairwise disjoint. Countable additivity of $P$, followed by division by the same positive constant, gives

$$Q\left(\bigcup_i E_i\right)=\sum_i Q(E_i).$$

Therefore $Q$ is a probability measure on the original event family, with all its mass supported in $B$. In finite elementary models, we can equivalently use $B$ as the reduced sample space. Every law about probabilities can now be applied to $Q$ consistently. In particular,

$$P(A^c\mid B)=1-P(A\mid B),$$

$$P(A\cup C\mid B)=P(A\mid B)+P(C\mid B)-P(A\cap C\mid B).$$

The complement in the first formula is the complement of the *target*, while the conditioning event stays fixed. In general, $P(A\mid B^c)$ is not $1-P(A\mid B)$. These are probabilities in two different conditional spaces. This distinction is central to both calculation and independence questions.

### Nested information and null events

Provided $P(B\cap C)>0$, conditioning inside the conditional measure gives

$$P(A\mid B\cap C)=\frac{P(A\cap B\mid C)}{P(B\mid C)}.$$

To prove this, replace both conditional terms on the right by their original ratios and cancel $P(C)$. Conditioning on $B$ and then on $C$ means retaining their intersection, not averaging their separate conditional answers. If $B\subseteq C$ up to a probability-zero difference, then $B\cap C$ has the same mass as $B$, so the extra information $C$ is redundant after $B$.

When $P(B)=0$, the elementary ratio is undefined. Its numerator is also zero; the quotient is $0/0$, not zero or one. The product-definition of independence still makes sense for null events, but the ratio-definition of a conditional does not. A continuous exact observation needs a separately specified conditional distribution or an appropriate limiting construction. The final theory section explains this boundary without smuggling division by zero into a formula.

**Source connection.** MIT Lecture 2 introduces the reduced universe and explicitly excludes a zero denominator. Stanford's conditional paradigm explains why the probability laws survive. CMU Section 2.3 provides event-level examples. The proof above puts these presentations into one precise measure statement.

## Joint tables, feasibility, and reversed conditionals

### The four-atom table is a complete model for two events

Write $a=P(A)$, $b=P(B)$, and $x=P(A\cap B)$. The four disjoint cells have masses

| Cell | Mass |
| --- | --- |
| $A\cap B$ | $x$ |
| $A\cap B^c$ | $a-x$ |
| $A^c\cap B$ | $b-x$ |
| $A^c\cap B^c$ | $1-a-b+x$ |

Every mass must be nonnegative. Consequently a joint model exists exactly when $a,b\in[0,1]$ and

$$\max(0,a+b-1)\le x\le\min(a,b).$$

Necessity follows from the four cells. Sufficiency follows by assigning those four nonnegative numbers to a four-outcome probability space; they sum to one. Thus the inequality is an exact existence criterion, not just a loose bound. If a question supplies conditionals inconsistent with it, there is no probability model satisfying all the premises.

For $b>0$, the feasible range of $P(A\mid B)$ is the interval obtained by dividing the two bounds by $b$. A conditional can exceed the unconditional probability because its denominator has changed; it cannot exceed one. When $P(A\mid B)=1$, the mass of $B\setminus A$ is zero, which is an almost-sure implication. In a finite model with all singleton weights positive, it is also a literal set inclusion; without that positivity it need not be.

<!-- FIGURE:table -->

### Reconstructing a model from conditional data

Suppose $P(B)=b$, $P(A\mid B)=u$, and $P(A\mid B^c)=v$, with $0<b<1$. The four cells are $bu$, $b(1-u)$, $(1-b)v$, and $(1-b)(1-v)$. Therefore

$$P(A)=bu+(1-b)v.$$

This is a weighted average, so it lies between $u$ and $v$. The weights are the population masses of the two strata. The ordinary average $(u+v)/2$ is valid only when the weights are equal, or when the two rates happen to coincide. If $P(A)$, $u$, and $v$ are supplied, solve $b=(P(A)-v)/(u-v)$ when $u\ne v$ and then check $b\in[0,1]$. If $u=v$, compatibility requires $P(A)=u$ and the supplied information does not identify $b$.

**Worked reconstruction.** Let $b=2/5$, $u=3/4$, and $v=1/6$. The four cells, in the table's order, are $3/10,1/10,1/10,1/2$. Hence $P(A)=2/5$ and $P(B\mid A)=3/4$. Equality of these two conditional rates occurs because the marginals are equal; it is not a general symmetry law.

For positive $a$ and $b$, both reversed conditionals use the same intersection:

$$P(A\mid B)P(B)=P(B\mid A)P(A)=x.$$

They are equal if $x=0$ or $a=b$. This covers disjoint positive-probability events as well as equal marginals. Dividing the two conditionals requires $x>0$; forgetting that condition loses the disjoint case. If $P(A\mid B)>P(A)$, then $x>ab$ and, for $a>0$, $P(B\mid A)>P(B)$. The *direction* of association is symmetric even though the conditional probabilities themselves need not match.

## The multiplication rule follows the complete history

### Two events, and what happens when a denominator vanishes

Rearranging the conditional definition gives $P(A\cap B)=P(A)P(B\mid A)$ for $P(A)>0$. Reversing the order gives $P(B)P(A\mid B)$ when $P(B)>0$. No independence is needed. If $P(A)=0$, the intersection probability is zero directly by monotonicity; do not justify it as zero multiplied by an undefined conditional. In a probability tree, a zero-mass node can simply be terminated because every descendant joint mass is zero.

### Many events: proof by telescoping

Define the prefix event $H_k=\bigcap_{i=1}^k E_i$. If all prefixes needed as denominators have positive mass, then

$$P(H_n)=P(E_1)\prod_{k=2}^{n}P(E_k\mid H_{k-1}).$$

Each factor is $P(H_k)/P(H_{k-1})$. Adjacent numerator and denominator terms cancel, leaving $P(H_n)$. Equivalently, prove the statement by induction using $P(H_{k+1})=P(H_k)P(E_{k+1}\mid H_k)$. Positive probability of the final intersection is a sufficient condition for every prefix to be positive, but is stronger than necessary: the final conditional factor may be zero while all denominators remain positive.

At three stages the rule is

$$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B).$$

Replacing the last factor by $P(C\mid B)$ is an additional modeling assertion. It is valid when the relevant conditional probabilities agree, for example under a suitably stated conditional-independence or Markov property. It does not follow from the multiplication rule. Changing the order of the three events changes the conditional factors but not the final joint mass.

**Worked history counterexample.** Two independent fair bits are $X$ and $Y$. Let $A=\{X=1\}$, $B=\{Y=1\}$, and $C=\{X=Y\}$. Then $P(A)=1/2$, $P(B\mid A)=1/2$, and $P(C\mid A\cap B)=1$, giving joint probability $1/4$. However $P(C\mid B)=1/2$. The abbreviated product would give $1/8$. The observation of $A$ matters after $B$ precisely because it determines whether the bits match.

### Trees: multiply down a path, add across incompatible paths

A tree node represents the *entire prefix event*, not merely the last label. Outgoing conditional probabilities at a positive-mass node sum to one. A leaf's mass is the product of its edge probabilities from the root. Leaves representing different complete outcomes are disjoint, so their masses can be added. The mass of a subtree is the sum of its leaves and is also its prefix mass. These equalities provide internal consistency checks before any conditional ratio is taken.

<!-- FIGURE:tree -->

**Worked three-stage calculation.** A trial passes stage one with probability $3/5$. Given that it passes, it passes stage two with probability $2/3$. Given both passes, it passes stage three with probability $1/4$. The probability of passing all three is $(3/5)(2/3)(1/4)=1/10$. Its probability of reaching stage three is $2/5$; conditional on reaching that stage, its completion probability remains $1/4$. The ratio $1/10$ divided by $2/5$ recovers that conditional. A stage's local success probability and the mass arriving at that stage are different quantities.

**Source connection.** MIT Lecture 2 provides the three-event tree; Stanford's probability-of-and reading gives the general chain. CMU Theorem 2.10 and Exercise 2.9 motivate the proof. We explicitly separate positive prefixes from positive final mass and do not silently drop historical conditions.

## Sequential sampling and exchangeability

### Draws without replacement change later denominators

From an urn with $r$ red and $b$ blue objects, draw an ordered sequence without replacement, uniformly among remaining objects at each stage. A specified color pattern with $k$ red positions and $m-k$ blue positions has probability

$$\frac{(r)_k(b)_{m-k}}{(r+b)_m},$$

where $(z)_j=z(z-1)\cdots(z-j+1)$ and $(z)_0=1$. This notation denotes a falling product, not a power. The numerator tracks how many red and blue objects have been removed; the denominator tracks all removed objects. If the pattern requests too many of a color, its probability is zero. Assume $0\le m\le r+b$ so a draw of that length is defined.

Every pattern with the same number of red positions has the same probability: the ordering changes where each numerator factor appears but not their product. Thus the sequence is exchangeable, although the draws are usually dependent. Summing over the $\binom mk$ disjoint position patterns yields

$$P(\text{exactly }k\text{ red})=\frac{\binom rk\binom b{m-k}}{\binom{r+b}m}.$$

This derivation links an ordered tree to unordered counting. Never count an unordered numerator against an ordered denominator. Replacement with uniform red probability $r/(r+b)$ produces a different model: each fixed pattern then has probability $(r/(r+b))^k(b/(r+b))^{m-k}$ under independent draws.

**Worked example.** With four red and three blue objects, the ordered pattern red, blue, red has probability $(4/7)(3/6)(3/5)=6/35$. Exactly two reds in three draws has probability $3(6/35)=18/35$. Given that the first two colors differ, the probability that the third is red is $3/5$: either retained history has removed exactly one red and one blue. Conditioning on the coarser event is harmless here because the two retained histories give the same remaining counts; it is not harmless in every experiment.

### Conditional count information can erase the success-rate parameter

For $n$ independent Bernoulli trials with a common success probability $p\in(0,1)$, every specified binary string with exactly $k$ successes has mass $p^k(1-p)^{n-k}$. Given that the total count is $k$, all $\binom nk$ such strings are equally likely. This statement follows by division by their common total mass, not by assuming every binary string was originally equally likely. Consequently the probability that a specified set of $j$ positions are all successes is

$$\frac{\binom{n-j}{k-j}}{\binom nk}=\frac{(k)_j}{(n)_j},$$

with zero numerator when $j>k$. The parameter $p$ cancels, but the conditioned indicators are dependent. For two distinct positions their joint success probability is $k(k-1)/(n(n-1))$, which differs from $(k/n)^2$ except at degenerate counts. Equal marginal rates do not restore independence.

### Random eligibility: condition on the number selected or combine stages

An object may enter a second stage only if it succeeds in the first. With independent per-object histories and probabilities $u$ for entry and $v$ for success given entry, its overall success probability is $uv$. For $n$ independent objects, exactly $j$ overall successes has probability $\binom nj(uv)^j(1-uv)^{n-j}$. This needs independence across object histories; independence between entry and success within an object is not required because $v$ is already conditional. Replacing the random number of eligible objects by its mean generally gives a different distribution. Authentic Question 4 below verifies both the per-object argument and a sum over the random eligible count.

## Partitions and total probability, including conditioned weights

### Disjoint exhaustive cases

Let $D_i$ be a finite or countable partition: pairwise disjoint events whose union has probability one. Ignore zero-mass cells when writing ratios. The target decomposes into disjoint intersections with the partition, so

$$P(A)=\sum_{i:P(D_i)>0}P(A\mid D_i)P(D_i).$$

Countable additivity justifies the countable version. No independence is involved. With an extra positive-mass observation $B$, the same reasoning inside $Q(E)=P(E\mid B)$ gives

For each cell with $P(D_i\cap B)>0$, define its conditioned rate $q_i=P(A\mid D_i\cap B)$ and its conditioned weight $w_i=P(D_i\mid B)$. Then

$$P(A\mid B)=\sum_iq_iw_i.$$

The sum here runs over the positive-weight cells. A zero-weight cell contributes zero joint mass and does not require a defined conditional rate. This notation keeps the rate and weight visibly separate; it represents exactly the conditional total-probability identity.

Both factors are conditioned consistently. Retaining the original weights $P(D_i)$ after observing $B$ is valid only if the weights are unchanged, or if a special cancellation happens. Likewise, replacing $P(A\mid D_i\cap B)$ by $P(A\mid D_i)$ requires a specific invariance or conditional-independence premise.

**Worked conditioned mixture.** Half the devices are type one and half type two. Within type one, two checks succeed independently with probability $9/10$ each; within type two, independently with probability $1/10$ each. Each check has unconditional success probability $1/2$, but simultaneous success has probability $(1/2)(81/100)+(1/2)(1/100)=41/100$. Given success on the first check, the probability of success on the second is $(41/100)/(1/2)=41/50$. The first result changes the type weights; it does not change the success rate *within a known type*.

### Conditioning can change the case distribution substantially

If $P(N=n)=2^{-n-1}$ for $n\ge0$ and each of $n$ independent binary outcomes is zero with probability $1/2$, then the joint mass of $N=n$ and all zeros is $2^{-2n-1}$. Summing the geometric series gives $2/3$. Under the all-zero observation, the conditional mass at $n$ is $3\cdot4^{-n}/4$. Its mass at zero is $3/4$, so its mass at positive counts is $1/4$. The empty collection contributes probability one to the statement that every outcome is zero. Removing it changes the conditioning event. This is the mechanism in authentic doctoral Question 2.

### Aggregation and Simpson's reversal

Suppose method A succeeds in $9/10$ of easy cases and $2/5$ of hard cases. Method B succeeds in $4/5$ of easy cases and $3/10$ of hard cases. A is better in each stratum. If A receives easy cases with weight $1/10$ but B with weight $9/10$, their aggregate rates are $9/100+36/100=45/100$ and $72/100+3/100=75/100$. The aggregate order reverses because the methods face different case mixtures.

If both methods used the same nonnegative stratum weights summing to one, multiplying each within-stratum inequality by that common weight and adding would preserve the order. Thus the reversal does not contradict arithmetic or the within-stratum comparisons. It signals that aggregate quantities answer a different question. The example is about a probability model, not a causal conclusion about treatment or an observational dataset.

<!-- FIGURE:mixture -->

**Source connection.** MIT's total-probability tree, CMU Section 2.5 and its conditional version, and Berkeley's department-weighting examples motivate this synthesis. The numerical model and its simulation are original.

## Independence is a factorization property

### Product definition, symmetry, and complements

Events $A$ and $B$ are independent exactly when $P(A\cap B)=P(A)P(B)$. This definition is symmetric and includes zero-probability cases. If $P(B)>0$, it is equivalent to $P(A\mid B)=P(A)$. The equivalence follows by dividing by $P(B)$ in one direction and multiplying in the other. A verbal claim that one event does not influence another must be translated into this specified probability model; absence of a causal connection is not a proof of probabilistic independence.

From independence,

$$P(A\cap B^c)=P(A)-P(A\cap B)=P(A)(1-P(B)).$$

Thus $A$ and $B^c$ are independent. Applying the same argument to $A^c$ gives independence of all four pairs formed by complementing either event. The proof does not divide by either marginal, so it remains valid at boundary probabilities.

Disjoint events satisfy $P(A\cap B)=0$. They are independent if and only if at least one has probability zero. A positive-probability event is independent of itself only if its probability is one: the equation is $a=a^2$. More generally, if $A\subseteq B$ up to a null difference, independence requires $a=ab$, so $a=0$ or $b=1$. Containment and independence are therefore strongly constrained but not logically incompatible.

### Pairwise versus mutual independence

For $n$ events, mutual independence requires product factorization for *every* nonempty subfamily. Single-event conditions are automatic. The number of nontrivial equalities is $2^n-n-1$. Pairwise independence checks only the $\binom n2$ pair equations. For three events, the three pair equations and the triple equation are all needed; neither set alone implies the other.

**Worked XOR model.** Two independent fair bits determine $A=\{X=1\}$, $B=\{Y=1\}$, and $C=\{X\ne Y\}$. Each has probability $1/2$. Every pair intersection has probability $1/4$, so the events are pairwise independent. Their triple intersection is empty because two ones cannot differ. Its mass zero differs from $(1/2)^3$. Given $A\cap B$, $C$ is impossible although its marginal is $1/2$.

To see the reverse logical failure, use four equally weighted outcomes with $A=B=\{1,2\}$ and $C=\{1,3\}$. The triple intersection has mass $1/4$, but the product is $1/8$, so this particular example does *not* give triple-only factorization. A correct triple-only example uses eight equally weighted outcomes: let $A=B=\{1,2,3,4\}$ and $C=\{1,5\}$. Then the triple mass is $1/8$, equal to $(1/2)(1/2)(1/4)$, while $P(A\cap B)=1/2\ne1/4$. Explicit cell verification prevents a plausible but false counterexample from entering an exam proof.

### Independent coordinate blocks

If all primitive coordinates are mutually independent, events depending on disjoint coordinate blocks are independent. In a finite model, sum the factorized atom probabilities over the two blocks; the double sum factors into the product of the two separate sums. This justifies independent device histories or edge-disjoint network paths built from independent components. Overlapping coordinate blocks do not automatically destroy independence, but the disjoint-block proof is no longer available. One must calculate rather than infer.

For mutually independent events with success probabilities $p_i$, the probability that none occur is $\prod_i(1-p_i)$, and the probability that at least one occurs is its complement. Exactly one occurs in disjoint patterns, yielding $\sum_i p_i\prod_{j\ne i}(1-p_j)$. Factoring by $\prod_i(1-p_i)$ is permitted only if all $p_i<1$; the unfactored sum still works when a success is certain. The familiar homogeneous expression $np(1-p)^{n-1}$ is a special case, not a substitute for heterogeneous probabilities.

## Conditional independence can be created or destroyed

### Definition and denominator conditions

With $P(C)>0$, events $A,B$ are independent given $C$ when

$$P(A\cap B\mid C)=P(A\mid C)P(B\mid C).$$

When $P(B\cap C)>0$, this is equivalent to $P(A\mid B\cap C)=P(A\mid C)$. To prove it, use the multiplication rule within the conditional measure and divide by $P(B\mid C)$. Without that positive denominator, the equality of two ratios is not a valid definition. The factorization definition remains meaningful even when $P(B\mid C)=0$.

Conditional complement closure holds within a *fixed* conditioning event: if $A$ and $B$ are independent given $C$, then $A$ and $B^c$ are independent given $C$. This says nothing by itself about independence given $C^c$. The complement of a target and the complement of the information play different roles.

### Selection can create dependence

Take independent fair bits $X,Y$ and let $C=\{X=Y\}$. Given $C$, the two retained outcomes are 00 and 11, each of mass $1/2$. Hence $P(X=1\mid C)=P(Y=1\mid C)=1/2$, but their conditional joint mass is $1/2$, not $1/4$. The original bits were independent. The selection rule coupled them by retaining only matching outcomes.

Alternatively condition on $D=\{X=1\text{ or }Y=1\}$. The retained outcomes are 01, 10, 11. Each success marginal is $2/3$, and their joint mass is $1/3$, smaller than $4/9$. Conditioning on a common consequence can create negative association as well. This is sometimes called a selection or collider effect; the numerical event calculation is the justification, not the label.

<!-- FIGURE:xor -->

### A shared hidden type can create marginal dependence

In the two-device-type example, the checks are independent inside each type but dependent when the type is hidden. More generally let a finite partition have weights $w_i$, and let $u_i=P(A\mid D_i)$, $v_i=P(B\mid D_i)$. Assuming conditional independence in each positive-mass cell,

$$P(A\cap B)=\sum_i w_i u_i v_i,$$

$$P(A)P(B)=\left(\sum_iw_i u_i\right)\left(\sum_iw_i v_i\right).$$

The difference is the weighted covariance of the two rate lists. For two strata with weight $w$ and $1-w$, expansion gives

$$P(A\cap B)-P(A)P(B)=w(1-w)(u_1-u_2)(v_1-v_2).$$

Thus the marginal association is positive when both rates change in the same direction and negative when they change in opposite directions. Conditional independence in all strata does not imply marginal independence. In the nondegenerate two-stratum case it implies marginal independence precisely when at least one event's rate is constant across the strata.

Conversely, marginal independence does not imply independence in a stratum, as the matching-bits example shows. One stratum's positive association can cancel another's negative association. Neither marginal factorization nor within-stratum factorization can be transported between probability measures without proof.

**Source connection.** CMU Definitions 2.11–2.13 and Exercises 2.15–2.21 expose these distinctions. Stanford's independence reading supplies complement closure and the conditional paradigm. Oxford Section 2.3 extends the language to random variables; this chapter confines its formal development to events and finite strata.

## The observation protocol belongs in the sample space

### A report is an event generated by a reporting procedure

If a message $M$ is produced from a hidden state $s$, the relevant joint weight is $P(s)P(M\mid s)$. Two truthful procedures can assign different message probabilities to the same state. Therefore being told a true statement is not always identical to conditioning on the entire set of states in which the statement is true. It is identical when the specified procedure reports that statement with the same positive probability throughout that set and never outside it.

**Two-sensor example.** Two independent fair sensors are active or inactive. If a monitor reports whenever at least one is active, the message retains 01, 10, 11 equally; given the report, both are active with probability $1/3$. If instead the monitor uniformly chooses one sensor and reports only when that chosen sensor is active, the message probabilities in those three states are $1/2,1/2,1$. Their original masses are all $1/4$, so the message mass is $1/2$ and its joint mass with 11 is $1/4$. The answer is $1/2$. Truthfulness does not determine the report mechanism.

### The two-sided card example

Three cards have face pairs RR, RB, and BB. Select a card uniformly and select its visible face uniformly. The elementary equally likely outcomes are the six *card-face pairs*. Observing a red face retains three outcomes: two on RR and one on RB. The other face is red in two of those outcomes, so the answer is $2/3$. If instead a procedure selects uniformly from the two cards that contain at least one red face and deliberately displays red, the cards have equal retained weight and the answer is $1/2$. Naming only the remaining card types erases the different likelihoods of the observation.

### A precise door-reveal model

Choose door one among three equally likely prize locations. An informed host always opens an unchosen empty door; when two are available, the host chooses each with probability $1/2$. If door three is opened, the joint weights of prize at one, two, and three are $1/6,1/3,0$. Divide by their sum $1/2$ to obtain conditional probabilities $1/3,2/3,0$. Switching succeeds with probability $2/3$. If the host instead opens an unchosen door uniformly without knowing the prize and we condition on the opened door being empty, the retained weights differ and switching succeeds with probability $1/2$.

Unconditionally, switching under the informed always-reveal protocol succeeds whenever the initial choice was wrong, with probability $2/3$, even if the host's tie-breaking is biased. But conditioning on a *particular named opened door* can depend on that bias. Distinguish the aggregate switching strategy from the posterior after one specific message. These examples are probability calculations under explicit protocols, not magic consequences of the phrase “an empty door was revealed.”

## Reliability with shared components

### Series, parallel, and overlap

For independent components, a series system works only if all components work, giving $\prod_i p_i$. A parallel system works if at least one works, giving $1-\prod_i(1-p_i)$. Those formulas apply to the component events under the stated independence. They do not authorize treating every path as independent.

Consider a common edge $E$ followed by alternative edges $F$ and $G$. Assume the three edge states are mutually independent, each with working probability $p$. The system event is $E\cap(F\cup G)$. Its reliability is

$$p(1-(1-p)^2)=2p^2-p^3.$$

The two path events $E\cap F$ and $E\cap G$ have joint mass $p^3$, while the product of their marginals is $p^4$. They are dependent for $0<p<1$ because they share an edge. Incorrectly applying the independent-parallel formula to these paths gives $2p^2-p^4$, too large by $p^3(1-p)$.

<!-- FIGURE:network -->

### Condition on a difficult component to simplify a network

Use a bridge network with vertices source, upper, lower, destination and independent edges: source-upper, upper-destination, source-lower, lower-destination, and upper-lower. All have working probability $p$. Condition on the bridge edge. If it fails, the two remaining two-edge paths are edge-disjoint, giving $2p^2-p^4$. If it works, upper and lower are connected, so the network works exactly when at least one source-side edge and at least one destination-side edge work. These two pairs are disjoint independent coordinate blocks; the conditional reliability is $(2p-p^2)^2$. Weight the two cases:

$$R(p)=(1-p)(2p^2-p^4)+p(2p-p^2)^2.$$

The conditioning edge is independent of the four remaining edges, so its observation leaves their probabilities unchanged. At $p=1/2$, the conditional reliabilities are $7/16$ and $9/16$, giving $R=1/2$. Always test $R(0)=0$ and $R(1)=1$. The truth-table simulation enumerates all 32 edge states; it illustrates and checks this exact reduction.

## Continuous observations and the zero-denominator boundary

### Positive-area conditioning still uses the same ratio

Let $(X,Y)$ be uniform on the unit square. Condition on $B=\{X+Y\le1\}$, a triangle of area $1/2$. For $0\le t\le1$, the portion of the triangle with $X\le t$ has area $\int_0^t(1-x)\,dx=t-t^2/2$. Hence

$$P(X\le t\mid X+Y\le1)=2t-t^2.$$

At $t=1/2$ the value is $3/4$, not $1/2$. The conditional mass is uniform over the triangle with respect to *area*, but its projection on the horizontal axis is not uniform because vertical slices have different lengths. Probability geometry requires the correct dimension and the correct underlying density.

### An exact real-valued observation is not an ordinary event ratio

For a continuous variable, $P(Y=y)=0$ at each point. If the variables have a suitably regular joint density and $f_Y(y)>0$, a conditional density is defined by $f_{X\mid Y}(x\mid y)=f_{X,Y}(x,y)/f_Y(y)$. Integrating it over the target set gives the conditional probability. This is a density ratio, not the ratio of two event probabilities at a point. Conditional versions at individual null points are not uniquely determined by the joint law without a specified convention; the continuous density version is a natural choice under the regularity assumptions.

For a concrete model with density $2$ on $0<x<y<1$, the marginal density of $Y$ is $2y$ for $0<y<1$. The conditional density of $X$ given $Y=y$ is therefore $1/y$ on $0<x<y$: a uniform distribution on that interval. Its probability of $X\le y/2$ is $1/2$. The elementary quotient $P(X\le y/2,Y=y)/P(Y=y)$ would be undefined and supplies no derivation.

One can also condition on the positive-mass strip $y\le Y\le y+\varepsilon$, compute an ordinary ratio, and take a limit under appropriate continuity and domination conditions. For the preceding smooth interior example, the limit agrees with the density answer. Do not claim that every sequence of shrinking events produces the same answer: the limiting geometry can weight the null set differently. Full density theory and regular conditional probability belong to later chapters; this section establishes the boundary needed to avoid incorrect exam manipulations.

**Source connection.** Oxford Lecture 2, Sections 2.1–2.3, motivates the distinction between a model, its information, and density-based conditioning. Its independence displays contain a printed set-letter typo; the correct event factorization is stated here. This chapter uses only the stated elementary and smooth-density cases and does not claim a proof of general measure-theoretic disintegration.

## Fully worked mathematical and conceptual problems

The bank contains 60 worked questions: four authentic translated examinations and 56 original or explicitly adapted problems. Difficulties are author assessments. Several problems ask for a derivation or counterexample rather than a numerical option; their solutions demonstrate the structure needed to recognize a correct examination alternative. Read a statement, inspect its assumptions, and then read the solution as a second explanation. You are not being asked to take an assessment before learning the chapter.

<!-- INCLUDE:problems -->

## Complete summary and examination rules

<!-- INCLUDE:review -->

## Interactive joint-table laboratory

The laboratory uses integer *weights*, not rounded percentages. Enter the four cells in the order both events, A only, B only, neither. Every displayed conditional is computed from the correct row or column denominator. Empty conditioning events are reported as undefined. The independence result uses exact integer products; it does not infer independence from rounded decimals. Presets contrast independence, positive association, disjointness, and a zero conditioning event.

<!-- LAB:table -->

The underlying exact computation is short, but its denominator choices are the mathematical content:

```text
total = both + A_only + B_only + neither
require total > 0
P_A = (both + A_only) / total
P_B = (both + B_only) / total
P_A_given_B = both / (both + B_only)  # only if denominator > 0
P_B_given_A = both / (both + A_only)  # only if denominator > 0
independent = (both * neither == A_only * B_only)
```

The embedded walkthroughs elsewhere in the chapter animate reduced mass, full histories, sampling, hidden types, selection protocols, Simpson's reversal, shared-edge reliability, and shrinking continuous strips. Their finite states support the written derivations; they do not replace general proofs. Use Previous step and Next step to compare the numerator, denominator, and stated information at each transition.

## References and source locations

1. **Massachusetts Institute of Technology. John N. Tsitsiklis.** *6.041SC Probabilistic Systems Analysis and Applied Probability*, Fall 2013. [Lecture 2 notes](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/resources/mit6_041scf13_l02/), PDF pages 1–2; page 3 contains acknowledgments. Used for the conditional universe, multiplication tree, and total-probability decomposition. The course identifies Sections 1.3–1.4 of its textbook as the corresponding reading.
2. **Stanford University. Chris Piech.** *CS109 / Probability for Computer Scientists* course reader. [Conditional Probability](https://chrispiech.github.io/probabilityForComputerScientists/en/part1/cond_prob/), [Independence](https://chrispiech.github.io/probabilityForComputerScientists/en/part1/independence/), and [Probability of And](https://chrispiech.github.io/probabilityForComputerScientists/en/part1/prob_and/). The complete instructional bodies of these three written readings were reviewed. Used for conditional laws, complement independence, generalized independence, and chain factorization. Missing denominator qualifications are made explicit in this chapter.
3. **Carnegie Mellon University. Mor Harchol-Balter.** *Introduction to Probability for Computing*. Cambridge University Press, 2024. [Chapter 2: Probability on Events](https://www.cs.cmu.edu/~harchol/Probability/chapters/chpt2.pdf), Sections 2.3–2.6, PDF pages 4–14; exercises in Section 2.7, PDF pages 14–21. Used for rigorous event definitions, conditional independence, weighted partitions, and problem structures. The course companion [book page](https://www.cs.cmu.edu/~harchol/Probability/book.html) identifies the text. Exercise adaptations are identified individually in the problem bank.
4. **University of California, Berkeley. David Aldous.** *STAT 134*, Fall 2012. [Lecture 2](https://www.stat.berkeley.edu/~aldous/134/lecture2.pdf), PDF pages 1–12, and [Lecture 3](https://www.stat.berkeley.edu/~aldous/134/lecture3.pdf), PDF pages 1–10. Used for sampling proportions, stratification, observation protocols, independence, and reliability. Board-only content referenced by the slides was not available and is not counted as a reviewed derivation. Relevant source pages with damaged text extraction were inspected visually.
5. **University of Oxford. Matthias Winkel.** *Part B Applied Probability*, Michaelmas Term 2007. [Lecture notes](https://www.stats.ox.ac.uk/~winkel/bs3a07.pdf), Lecture 2, Sections 2.1–2.3, PDF pages 15–20; printed pages 7–12. Supplementary source for model assumptions, conditional densities, and the distinction between marginal and conditional independence. The advanced stochastic-process chapters were not used in this chapter.
6. **Iranian entrance examination archive.** [Phd-Exam-CSE / Exams](https://github.com/bheydari721rn24/Phd-Exam-CSE/tree/bdadf6e2c9cadc4772ae137a96a3da753c7cfd08/Exams). Computer Science PhD 1404: questions 68–69 on PDF page 15 and question 70 on page 16. Computer Engineering MSc 1405: question 35 on PDF page 8. Original pages were visually checked. Translation and independent solutions are provided with source-specific links; no official-key claim is made.

[Read the chapter quality audit and its explicit coverage limits](../reviews/s_conditional-quality.html). The chapter targets the stated concept inventory and common medium-to-hard examination patterns. Mathematical checks and source review support its quality; they cannot guarantee a particular score or correctness on every unseen question.
