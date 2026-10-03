## Teaching through formulas and conceptual decisions

### Derive the integer index region

Write one summation term for each outer iteration before estimating. A triangular nest with inner index1 through$i$ performs $\sum_{i=1}^n i=n(n+1)/2$ body visits. Three strictly increasing indices choose a three-element subset and perform $\binom n3$ visits. Inclusive equality changes the combinatorial object and the exact formula.

If the inner loop visits multiples of$i$ up to$n$, the count is $\lfloor n/i\rfloor$. Summing gives $\sum_{i=1}^n\lfloor n/i\rfloor$, bounded above by$nH_n$ and below by$nH_n-n$, hence order$n\log n$. In contrast, an outer counter doubling while the inner runs up to that counter produces $1+2+4+\cdots$, order$n$; multiplying maximum iterations of both loops gives a loose and misleading bound.

### Count guards and updates separately

A normally terminating pretest loop with$k$ body executions tests its guard$k+1$ times. A break can remove the final failed test, and a continue in a for-loop still executes the update expression. Header operations therefore require a control-flow trace; “body count plus one” is not universally valid after abrupt exits.

### Nonconstant body cost and input dependence

An inner operation copying$i$ entries contributes$i$ work each time it is executed. If there are$i$ inner visits at outer$i$, its contribution is$i^2$, and summation becomes cubic rather than quadratic. For search with early exit, best-case and worst-case counts require separate input witnesses. An inversion-based shifting procedure costs exactly one shift per inversion, but its comparison count can include unsuccessful comparisons as well.

## Formula and conceptual problem bank

### Question 1. Triangular count

For $i=1,\ldots,20$, an inner loop executes for $j=1,\ldots,i$. How many body executions occur?

**A.** 190

**B.** 200

**C.** 210

**D.** 400

**Answer: C.**

The exact count is $1+2+\cdots+20=20\cdot21/2=210$. Option190 counts strict pairs with$j<i$. Option400 replaces every inner bound by20 and overcounts. The outer loop is inclusive at20, so neither boundary may be dropped before counting.

### Question 2. Strict triples

The body executes for every $1\le i<j<k\le10$. How many executions occur?

**A.** 45

**B.** 120

**C.** 165

**D.** 1000

**Answer: B.**

Each execution corresponds bijectively to a three-element subset of ten indices listed in increasing order. The count is $\binom{10}3=120$. Multiplying ten choices per index ignores strict ordering and distinctness. Option45 counts pairs, not triples; a count allowing equality is a different index region.

### Question 3. Exact multiples

For $i=1,\ldots,6$, visit $j=i,2i,\ldots$ while $j\le6$. What is the total?

**A.** 12

**B.** 14

**C.** 18

**D.** 21

**Answer: B.**

The six inner counts are $\lfloor6/i\rfloor=6,3,2,1,1,1$. Their sum is14. The harmonic expression $6H_6$ is an upper approximation, not the exact integer count. The last three outer values each still have their first multiple; dropping them loses three visits.

### Question 4. Geometric outer, dependent inner

For $i=1,2,4,\ldots,n$ with $n=2^k$, run an inner body exactly$i$ times. What is the exact total?

**A.** $n\log_2 n$

**B.** $n$

**C.** $2n-1$

**D.** $n^2$

**Answer: C.**

The count is $\sum_{r=0}^k2^r=2^{k+1}-1=2n-1$. Maximum inner count$n$ multiplied by the number of outer iterations is only an upper bound and is not tight. Each geometric term must retain its own value; the final term dominates a bounded-ratio sum.

### Question 5. Doubling from every start

For each integer$i$ from1 through$n$, initialize$j=i$ and repeatedly double$j$ while$j\le n$. What is the total tight order?

**A.** $\Theta(\log n)$

**B.** $\Theta(n)$

**C.** $\Theta(n\log n)$

**D.** $\Theta(n^2)$

**Answer: B.**

Reverse the counting: at doubling level$r$, exactly $\lfloor n/2^r\rfloor$ starting values remain legal. Sum these counts over$r\ge0$. The first level gives$n$ as a lower bound, and the infinite geometric upper bound gives at most$2n$. Many starts near$n$ execute only once, so multiplying every start by the longest chain is loose.

### Question 6. Square-root region

For each $i=1,\ldots,n$, count positive$j$ while $j^2\le i$. What is the total tight order?

**A.** $\Theta(n)$

**B.** $\Theta(n\log n)$

**C.** $\Theta(n^{3/2})$

**D.** $\Theta(n^2)$

**Answer: C.**

At outer$i$, there are $\lfloor\sqrt i\rfloor$ visits. Their sum is at most$n\sqrt n$. For at least roughly half the outer indices, $i\ge n/2$, so each contributes order$\sqrt n$, giving a matching lower bound. The square in the condition produces a square-root count, not a quadratic count.

### Question 7. Guard tests

In a pretest while-loop without break or return, the body executes seven times and then the guard becomes false. How many guard evaluations occur?

**A.** 6

**B.** 7

**C.** 8

**D.** 14

**Answer: C.**

Each of the seven executions is preceded by a successful guard test. An eighth test detects termination. There is no extra body execution after that failed test. Seven counts only successful tests; fourteen wrongly assigns one failed test to every iteration. A break would change the premise and can eliminate the final failed test.

### Question 8. A nonconstant body

For $i=1,\ldots,n$, repeat$i$ times a procedure costing exactly$i$ word operations. What is the total tight order?

**A.** $\Theta(n)$

**B.** $\Theta(n^2)$

**C.** $\Theta(n^3)$

**D.** $\Theta(n^4)$

**Answer: C.**

Outer$i$ contributes $i\cdot i=i^2$ operations. Therefore total work is $\sum_{i=1}^n i^2=n(n+1)(2n+1)/6$, cubic in$n$. The quadratic body-visit count applies only if each visit costs a constant. The procedure cost and its invocation count must both appear in the summand.

### Question 9. Squaring counter

A loop begins at integer$j=2$, executes while$j\le n$, and updates$j=j^2$. Ignoring arithmetic cost and overflow, what is its body count order for large$n$?

**A.** $\Theta(\log n)$

**B.** $\Theta(\log\log n)$

**C.** $\Theta(\sqrt n)$

**D.** It never terminates.

**Answer: B.**

After$t$ updates, $j=2^{2^t}$. The guard is true while $2^t\le\log_2 n$, so the number of legal$t$ values is order$\log\log n$. Starting at0 or1 would instead stall forever, but the specified start2 avoids those fixed points. Counting bit arithmetic would require an additional model.

### Question 10. Input-dependent shifts

Insertion-style sorting shifts an earlier entry whenever it exceeds the key being inserted. For $[4,1,3,2]$, how many shifts occur?

**A.** 3

**B.** 4

**C.** 5

**D.** 6

**Answer: B.**

The strict inversions are $(4,1),(4,3),(4,2),(3,2)$, four pairs. Inserting1 shifts4 once; inserting3 shifts4 once; inserting2 shifts4 and3, twice. The total is4. Comparisons can also include a failing comparison and are not identical to this shift count. Equal keys would not create a strict inversion.

<!-- CHALLENGE-BANK -->

### Question 11. Challenge: Three-factor integer region

Count body executions over all positive integer triples$(i,j,k)$ satisfying$ijk\le n$. What is the tight order?

**A.** $\Theta(n\log n)$

**B.** $\Theta(n\log^2n)$

**C.** $\Theta(n^2)$

**D.** $\Theta(n^3)$

**Answer: B.**

The exact count is$\sum_{i=1}^n\sum_{j=1}^{\lfloor n/i\rfloor}\lfloor n/(ij)\rfloor$. Dropping floors and enlarging the inner range gives upper bound$nH_n^2=O(n\log^2n)$. For a lower bound, restrict$i,j$ to at most$n^{1/3}$. Their product is at most$n^{2/3}$, so for sufficiently large$n$ the floor is at least$n/(2ij)$. Summing this restricted square yields a constant times$nH_{\lfloor n^{1/3}\rfloor}^2$, matching the upper order. The feasible product region is not a cube of side$n$.

### Question 12. Challenge: A branch-defined triangular region

For$i=1,\ldots,n$, start$j=1$ and execute the body while$j\le n$ and$i+j\le n$, incrementing$j$ each time. What is the exact count?

**A.** $n(n+1)/2$

**B.** $n(n-1)/2$

**C.** $n^2$

**D.** $n-1$

**Answer: B.**

For a fixed$i$, admissible$j$ values are1 through$n-i$, giving$n-i$ visits including zero visits at$i=n$. Sum these counts to obtain$(n-1)+\cdots+1+0=n(n-1)/2$. The inclusive sum constraint still excludes the diagonal case$i=j=n$, and independent-loop multiplication ignores the stopping condition. Evaluating the region directly resolves both tight order and exact endpoints.

## Applicable formulas and examination notes

### 1. Inclusive arithmetic sum

$\sum_{i=1}^n i=n(n+1)/2$; strict$j<i$ gives$n(n-1)/2$. At$n=20$, these are210 and190. Endpoint conventions often account for the entire difference between two candidate answers.

### 2. Strict ordered indices

$1\le i_1<\cdots<i_r\le n$ yields $\binom nr$ body visits. Increasing order selects one representation per subset. Nondecreasing indices allow repeated values and require a different combination formula.

### 3. Multiples and floors

Visits$i,2i,\ldots\le n$ number $\lfloor n/i\rfloor$. Sum the floors for an exact count; use $nH_n-n\le\sum\lfloor n/i\rfloor\le nH_n$ for tight asymptotic order. Replacing floors by fractions does not give an exact integer answer.

### 4. Reverse the count

For doubling chains starting at every$i$, count legal starts per level: $\sum_{r\ge0}\lfloor n/2^r\rfloor$. This lies between$n$ and$2n$. Reversing the sum exposes why the longest-chain bound overestimates total work.

### 5. Geometric dependent inner work

If outer bounds are1,2,4,...,$n$ and the inner cost equals the bound, the total is$2n-1$ for power-of-two$n$. The independent-loop multiplication rule does not apply to these dependent inner lengths.

### 6. Root constraints

For $j^p\le i$ with fixed positive$p$, the count per$i$ is $\lfloor i^{1/p}\rfloor$ and the total is $\Theta(n^{1+1/p})$. Establish a lower bound from the final half of outer indices; an upper estimate alone is insufficient.

### 7. Headers are distinct events

A normally terminating pretest loop tests its guard one more time than body execution. A break exits without the final false guard; a for-loop continue still reaches the update. Count the actual path before applying an endpoint shortcut.

### 8. Weighted invocation counts

If$i$ calls each cost$i$, the contribution is$i^2$, not$i$. Sum the full operation cost: the resulting square sum is cubic. A procedure call is not a unit-cost event unless the question explicitly supplies that model.

### 9. Supermultiplicative counters

Starting at2 and squaring yields $2^{2^t}$, so iteration count is doubly logarithmic. Starting at0 or1 never progresses. Finite-width overflow and the cost of large-integer squaring are separate issues that can invalidate the idealized count.

### 10. Shifts and inversions

In insertion-style movement, every strict inversion induces one shift. For$[4,1,3,2]$, the shift count is4. Include unsuccessful comparisons separately when asked for comparisons, and specify whether equality causes movement.

<!-- BOUNDARY-NOTES -->

### 11. Early-exit witnesses

An unsorted search can inspect one item in the best case and all $n$ in the worst case. State a concrete input realizing each bound. Multiplying maximum branch counts can be non-tight if those maxima cannot occur together on any one input.

### 12. Independent dimensions

A rectangular loop with $n$ rows and $m$ columns costs $nm$ unit visits. A square specialization $m=n$ gives $n^2$, but the general result must retain both parameters. Constant-size one dimension does not justify dropping it when it is independently variable.

### 13. Nontermination before complexity

A counter initialized to zero and updated by doubling remains zero. A positive-limit guard can then stay true forever, so no finite logarithmic runtime applies. Verify progress and arithmetic semantics before deriving iteration formulas.
