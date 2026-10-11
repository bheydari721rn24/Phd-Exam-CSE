## Complete probability-modeling rules and examination traps

### 1. Declare the actual experiment

State what is selected, in what order, with which probabilities and whether replacement occurs. Identical objects in a picture do not imply equally likely reported categories. A numerical model must follow the described selection mechanism.

### 2. Retain enough information for the target

If two detailed outcomes are merged but the question distinguishes them, the reporting space has discarded required information. Keep the detailed space until the target is a union of its reporting fibers.

### 3. Separate outcomes from events

An outcome is an element $\omega$; an event is a measurable set. Interpret $P(\omega)$ as singleton shorthand only when $\{\omega\}$ is an admissible event. A probability law is defined on its declared event family.

### 4. State the event family

A sigma-algebra contains the whole space and is closed under complements and countable unions. These properties imply empty-set and countable-intersection membership. They do not guarantee closure under arbitrary uncountable unions.

### 5. Count only under a uniform finite law

The ratio $|A|/|\Omega|$ is justified by equal elementary masses. For nonuniform outcomes, add their actual weights. Infinite cardinalities cannot replace probability masses in this ratio.

### 6. Push masses forward when grouping outcomes

A reported value receives the sum of masses in its preimage. The head-count values from three fair tosses have masses $1/8,3/8,3/8,1/8$, although all eight detailed sequences have equal mass.

### 7. Check normalization and nonnegativity separately

Masses summing to one are not enough if any are negative. In finite event-data problems, reconstruct all membership atoms and check every one. In infinite discrete models, verify the entire nonnegative series sums to one.

### 8. Translate “or” before calculating

Inclusive “or” denotes a union and includes simultaneous occurrence. Exactly one denotes a symmetric difference. Neither is the complement of a union; not both is the complement of an intersection. These four targets require different formulas.

### 9. Disjointify before adding arbitrary events

The union equals the disjoint union of each event with earlier events removed. Summing original masses gives only an upper bound unless the removed overlaps have zero probability. No independence premise is needed for the bound.

### 10. Correct overlap once for a union and twice for exactly one

For two events, union mass is $a+b-q$ and exactly-one mass is $a+b-2q$, where $q$ is overlap. The second subtraction removes the overlap entirely after it was counted twice in the marginals.

### 11. Use the four-cell feasibility test

Check $q,a-q,b-q,1-a-b+q\ge0$. Equivalently, $\max(0,a+b-1)\le q\le\min(a,b)$. Constructing these four masses proves the endpoints are attainable in an abstract probability space.

### 12. Use eight cells for three-event data

Every pair intersection includes the triple. Subtract the triple for pair-only cells, restore it for single-only cells, and compute the outside cell from inclusion-exclusion. Testing only $t\le\min(a,b,c)$ misses stronger pair and single-only constraints.

### 13. Prove sufficiency as well as necessity

An interval of algebraic bounds is only a candidate until its masses construct a law. Assign them to membership strings, verify a unit total, and recover every supplied marginal and intersection.

### 14. Distinguish independence from disjointness

Independence requires an intersection mass equal to a product; disjointness requires an empty intersection. Positive-probability disjoint events are dependent. A zero-probability event is independent of any other event.

### 15. Inspect the required degree of independence

A product across all $n$ success or failure events requires the appropriate joint independence. Pairwise independence fixes only second-order intersections. Three-event membership tables can preserve all pair products while changing the triple and union.

### 16. Complement before computing at least one

Under the stated product model, at least one has mass $1-\prod_i(1-p_i)$. The complement is an intersection of failures, not a union. Without a product premise, compute that intersection from the actual joint law.

### 17. Include zero in “at most one”

Add the disjoint zero-success and exactly-one cases. Exactly one in a common-$p$ independent model has mass $np(1-p)^{n-1}$; adding $(1-p)^n$ changes the event being measured.

### 18. Keep conditional denominators visible

For a positive-mass condition $H$, use $P(E\cap H)/P(H)$. Reversing the condition changes the denominator. Write the events by name before substituting fractions to avoid confusing a likelihood with a posterior.

### 19. Renormalize the surviving detailed outcomes

Conditioning does not make coarse categories equally likely. In the two-ball urn, the retained red-red and mixed groups have three and six detailed pairs. Use their inherited masses, not a count of category names.

### 20. Include zero-size cases when the model permits them

A childless family satisfies “no boys.” Omitting it changes both the conditioning population and the denominator. Determine the truth of the event on the empty configuration instead of excluding it by intuition.

### 21. Do not replace a random trial count by its mean

Conditional success probabilities must be averaged over the distribution of the eligibility count. For a nonlinear function $f$, $E[f(K)]$ need not equal $f(E[K])$. The two-coin retoss example gives $3/8$ versus $1/2$.

### 22. Combine eligibility and success into one joint indicator

A retoss head from an original fair coin requires two heads, so its contribution probability is $1/4$. For an already eligible coin the conditional probability is $1/2$. These numbers describe different events and denominators.

### 23. Linearity of expectation needs no independence

An outcome-wise sum of indicators gives an expectation equal to the sum of their success probabilities. Keep this proof separate from any multiplication rule. For uniform distinct-key permutations, prefix symmetry gives record probability $1/i$.

### 24. A count's variance is not its mean

An indicator has variance $p-p^2$. Expanding a sum's squared count introduces pair covariances. Independence cancels them; more generally they must be checked rather than silently omitted.

### 25. Distinguish exact values from asymptotic approximations

The exact running-record mean is $H_n$, whereas $\ln n$ is its first-order large-size approximation. A question specifying a small finite size requires the rational sum; a growth approximation may select a large-size option only under that convention.

### 26. Preserve discrete endpoints in tails

The event $X\ge n$ includes the mass at $n$, while $X>n$ excludes it. A geometric tail includes every later singleton, not only its first term. Check by subtracting consecutive tails and recovering the point mass.

### 27. Endpoint irrelevance depends on the law

Uniform continuous laws assign singleton mass zero, so changing an interval endpoint does not change its probability. A mixture may place positive mass at that endpoint. Inspect the actual measure before applying a continuous-model shortcut.

### 28. A null event need not be empty

A singleton in a uniform interval is nonempty and null. Likewise, an event of probability one need not equal the entire sample space. Under a finite law with strictly positive mass at every point, null events are empty; state that extra premise.

### 29. Countable and uncountable null unions differ

A countable union of null events is null by the union bound. An uncountable union of null singletons can fill a probability-one interval. Countable additivity supplies no unrestricted uncountable singleton sum.

### 30. Name the monotone event sequence for continuity

An increasing union or decreasing intersection permits the corresponding probability limit. Convergence of probabilities of arbitrary events does not identify their infinitely-often event. Models varying with a size parameter are not automatically nested events in one fixed space.

### 31. Summability controls infinitely many errors

If $\sum_nP(A_n)<\infty$, tail union bounds approach zero and imply $P(\limsup A_n)=0$ without independence. A divergent sum alone gives no converse; additional hypotheses are needed.

### 32. Audit the source wording before choosing a model

Without-replacement draws of distinct labeled objects cannot repeat an object. A source that asks for repetition under that rule but offers no zero option has a modeling conflict. Record it openly; an independently authored with-replacement question must be labeled as such rather than presented as a corrected authentic quotation.
