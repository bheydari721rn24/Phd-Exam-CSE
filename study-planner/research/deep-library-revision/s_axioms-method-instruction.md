## Mathematical constructions for the revised question bank

### 1. Recover an entire two-event law before computing a target

Given $a=P(A)$, $b=P(B)$ and $u=P(A\cup B)$, recover $q=a+b-u$. The four masses in order both, first only, second only, neither are $q,a-q,b-q,1-u$. A tuple can have each supplied number in $[0,1]$ and still be impossible: for example $a=4/5,b=7/10,u=1/2$ implies $a-q=-1/5$. Check every atomic mass, not just normalization.

With only $a,b$ known, all possible overlaps satisfy $\max(0,a+b-1)\le q\le\min(a,b)$. Necessity follows from the four nonnegative masses. Sufficiency follows by constructing a four-point space carrying those masses. Because exactly one has probability $a+b-2q$, its sharp range is $|a-b|\le P(A\triangle B)\le\min(a+b,2-a-b)$. The coefficient minus two makes this target decrease as overlap increases. A proof of a bound must show why no model can exceed it and supply a model attaining the claimed endpoint.

### 2. Invert a three-event table and prove feasibility constructively

Write $a,b,c$ for marginals; $d,e,f$ for $AB,AC,BC$ intersections; and $t$ for the triple. The exact atoms are

$$t,\quad d-t,\quad e-t,\quad f-t,\quad a-d-e+t,\quad b-d-f+t,\quad c-e-f+t,\quad1-a-b-c+d+e+f-t.$$

Their eight nonnegativity inequalities reduce to

$$\max(0,d+e-a,d+f-b,e+f-c)\le t\le\min(d,e,f,1-a-b-c+d+e+f).$$

If the lower endpoint exceeds the upper, no probability law realizes the given data. Otherwise, placing these masses on eight binary membership strings constructs every permissible value of $t$. Summing the strings with first bit one recovers $a$; summing those with first two bits one recovers $d$. This verifies sufficiency without imposing independence. In a physical model, additional mechanism constraints may narrow the abstract interval. The checkpoint model displays the actual atoms and their total rather than drawing overlapping circles whose areas might misleadingly suggest prescribed masses.

### 3. Change descriptions by preimages and conditioning by renormalization

A reporting map $g:\Omega\to S$ induces $Q(C)=P(g^{-1}(C))$. It merges masses of detailed outcomes. In a finite uniform space, the mass of a reported value is its fiber size divided by $|\Omega|$; a uniform input need not induce a uniform report. Preimages preserve complements and disjoint unions, so the induced law preserves the probability axioms whenever the relevant preimages are measurable.

Conditioning on an event $H$ with positive mass instead restricts outcomes to $H$ and uses $P_H(E)=P(E\cap H)/P(H)$. For disjoint $E_i$, the intersections $E_i\cap H$ remain disjoint, so division by the fixed positive denominator preserves additivity. The conditioned space has total mass $P(H)/P(H)=1$. In a finite uniform model, its surviving detailed points remain uniform, but coarser categories still require their inherited weights. A probability-zero condition cannot be handled by this division; later continuous conditioning needs additional definitions, not division by zero.

### 4. Derive product-model and indicator tools needed by the archived questions

For independent binary coordinates with success probabilities $p_i$, assign a binary pattern $s$ mass $\prod_i p_i^{s_i}(1-p_i)^{1-s_i}$. Summing over all patterns gives $\prod_i(p_i+(1-p_i))=1$. Fixing some coordinates and summing over the others proves the needed subset products. This construction explains which independence premise supports a many-event multiplication; pairwise products alone do not specify every pattern.

If $K=\sum_iI_i$, exactly zero uses the all-zero pattern, and exactly one is a disjoint sum over its unique successful index. Expectations require a different argument: in a finite model, interchange finite sums in $E[K]=\sum_\omega P(\omega)\sum_iI_i(\omega)$ to obtain $\sum_iE[I_i]$, with no independence requirement. Expand the square to obtain the variance identity with all covariances. Pairwise independence suffices for those second-order products, although it does not suffice for an arbitrary-length all-failure product. These tools are included here to make the existing authentic applications self-contained; their systematic theory continues in the later counting, conditional-probability and random-variable chapters.

### 5. Distinguish exact unions, bounds and higher-order overlap corrections

For three events, the sum of marginals counts an outcome belonging to $r$ events exactly $r$ times. Subtracting the three pair intersections removes $\binom r2$ copies; adding the triple restores $\binom r3$. For $r=1,2,3$, the final coefficient is always one. This outcome-wise coefficient calculation proves inclusion-exclusion on arbitrary weighted atoms, not only on uniform outcomes.

The union bound retains the initial nonnegative overcount, so it needs no independence. Its gap for a finite family equals $E[K]-P(K\ge1)=E[(K-1)1_{\{K\ge1\}}]$, where $K$ is the number of occurring events. Thus the gap vanishes precisely when multiple occurrence has probability zero. In the three-label collision problem, exactly one repeated pair contributes no gap, while each all-equal outcome contributes two extra counts. A bound of one does not prove certainty; it may simply be the point at which the numerical upper bound becomes uninformative.

### 6. Separate monotone event limits from numerical limits

If $A_n$ increases, disjoint increments $D_1=A_1$ and $D_n=A_n\setminus A_{n-1}$ partition each stage. Countable additivity identifies the limiting partial sum with $P(\bigcup_nA_n)$. Decreasing continuity follows by taking complements; probability measures have finite total mass, so subtraction is legitimate. These are proofs about nested sets in one fixed space.

For arbitrary events, the infinitely-often event is $\bigcap_m\bigcup_{n\ge m}A_n$, whereas eventual permanent occurrence is $\bigcup_m\bigcap_{n\ge m}A_n$. A moving dyadic interval can have probability tending to zero while almost every point belongs to infinitely many intervals. A stronger summability condition $\sum_nP(A_n)<\infty$ makes each tail union at most the numerical series tail, forcing infinitely-often probability zero by decreasing continuity. Every use of a limit must identify the sets and the applicable theorem; numerical convergence alone is not a set-limit theorem.
