## Mathematical constructions for exact operation ledgers

### 1. Derive a ledger from control-flow events

A conventional pretest loop with $q$ completed iterations has $q$ successful guards, $q$ bodies, $q$ updates and one final false guard. With fixed costs $c_g,c_b,c_u,c_0$, the modeled contribution is $c_0+(q+1)c_g+q(c_b+c_u)$. Initialization is charged once per invocation, not once per body. If an outer loop invokes an inner loop $r$ times, summing its ordinary guard counts adds $r$ final false tests, even when some invocations have zero bodies.

An early `break` changes this event path. If the break occurs on the $q$th body, the header has $q$ successful evaluations and no normal final false evaluation. A `continue` in a C-style `for` reaches the update expression, whereas an update written after a `continue` in a `while` body may never execute. The two displayed fragments in Question 32 make this distinction concrete. A short-circuit guard also has separate predicate frequencies: the right predicate is checked only on visits where the left is true. Analyze that event sequence before assigning costs.

### 2. Recover exact sums by two independent counting views

For $1\le i\le j\le k\le n$, fixing the middle entry gives $j(n-j+1)$ choices. Summing and simplifying yields $n(n+1)(n+2)/6$. Shifting to the strictly ordered triple $(i,j+1,k+2)$ instead gives a bijection with three-element subsets of $n+2$ positions. The two derivations verify the same identity through different representations.

Replacing the last weak inequality by a strict one changes the count to $\binom{n+1}{3}$; making every inequality strict gives $\binom n3$. The equality permissions affect exact counts even when their tight growth remains cubic. The difference between all-weak and all-strict counts is $n^2$, obtained independently by partitioning repeated-index cases. A correct finite formula should match both its small-domain values and the increment when a new maximum index is admitted.

Weighted work can be turned into another counting dimension when the weights are integers. A body at $(i,j)$ costing $j$ operations has operation labels $(i,j,t)$ for $1\le t\le j$. This converts its total into a weakly ordered triple count, explaining the cubic formula in Question 12. It is a proof device, not an assertion that the original code contains a third loop.

### 3. Prove floor-sum bounds without deleting floors

Successful divisibility branches form the finite region $ij\le n$ after reparameterizing each multiple by its multiplier. The exact count is $D(n)=\sum_{i=1}^n\lfloor n/i\rfloor$. Since $x/2\le\lfloor x\rfloor\le x$ for $x\ge1$, it lies between $(n/2)H_n$ and $nH_n$. This supplies uniform lower and upper witnesses; simply replacing a floor by a fractional number is not an exact operation count.

Three-factor regions add a second harmonic aggregation. Restricting the two outer factors to $m=\lfloor n^{1/3}\rfloor$ yields a feasible square with enough small factors to establish the lower bound in Question 45. Enlarging their range gives the matching upper bound. The restriction is chosen to preserve feasibility, not to assume that all pairs in a full square are legal. The small layer animation displays each positive $(j,k)$ pair for a fixed $i$ and labels its exact layer contribution.

The all-pairs branch implementation still tests $n^2$ pairs, even when only $D(n)$ bodies succeed. An implementation that steps directly through multiples performs a different ledger. Count output equivalence and control-flow equivalence separately.

### 4. Change to exponent coordinates before counting doubling

If an inner counter starts at $2^i$ and doubles, its successive values are $2^{i+t}$. An inclusive bound $2^n$ becomes the integer inequality $i+t\le n$, so the visit count is $n-i+1$ when $i\le n$. Adding these correlated exponent rows gives $n(n+3)/2$ for outer stages zero through $n-1$. This is an exact arithmetic triangle in exponent space, not a rectangle of numeric counter values.

The opposite schedule doubles the outer counter but spends its current value in inner work. At final scale $N$, the row sum is $1+2+\cdots+2^{\lfloor\log_2N\rfloor}=2^{\lfloor\log_2N\rfloor+1}-1$, between $N$ and $2N-1$. There are logarithmically many rows but linear total work in $N$. A fixed exponent bound $n$ and final scale $N=2^n$ are different size parameters. State which is encoded as input and whether arithmetic fits in one word.

### 5. Derive an exact reverse-doubling identity

Consider a loop that starts at each $i=1,\ldots,n$ and repeatedly doubles while its value is at most $n$. Counting by start gives $\sum_i(\lfloor\log_2(n/i)\rfloor+1)$. Counting instead by doubling depth gives $\sum_{t\ge0}\lfloor n/2^t\rfloor$, a finite sum whose first term is $n$ and upper bound is $2n$.

There is a sharper identity. Write the binary expansion $n=\sum_{r=0}^h b_r2^r$, with digits $b_r\in\{0,1\}$, and define $s_2(n)=\sum_rb_r$. Each digit at position $r$ contributes $2^r+2^{r-1}+\cdots+1=2^{r+1}-1$ across all the floors. Therefore

$$\sum_{t\ge0}\left\lfloor\frac n{2^t}\right\rfloor=2n-s_2(n).$$

For $n=13$, the binary digits are $1101$, so the count is $26-3=23$, agreeing with $13+6+3+1$. This exact identity explains why summing a maximum logarithmic row count gives a loose $n\log n$ upper bound for a program whose actual count is linear. It also tests floor behavior at powers of two and immediately adjacent sizes.

### 6. Separate a fixed trace from a maximum and an expectation

The supplied merge-sort array has a particular comparison trace, while alternating lists construct an attained merge maximum. The uniformly random permutation in the record-minimum question instead defines an expectation by a distribution. An explicit fixed-array state trace in Question 11 cannot establish that expectation; it verifies one instance and the prefix-minimum invariant.

For sequential merges, accumulated lengths give both a write ledger and a comparison ledger. Every materialized stage writes its full output. A comparison maximum additionally needs one legal input family attaining the stage maxima simultaneously; the increasing-list-maxima construction in Question 4 supplies it. These proof obligations prevent summing independently chosen worst cases that cannot occur together.

The retained triangular and doubling players remain bounded examples with stated models. The separate lower-bound search and deliberately stalled search illustrate interval progress versus a repeated state; the word-versus-bit player illustrates a particular ripple-addition model rather than a physical processor claim. The question-specific parity grid, fixed-array minimum trace and product-layer grid below display their actual predicates and counters. Mathematical conclusions over arbitrary sizes come from the written identities and bounds, not from the finite pictures alone.
