## Q1

**Correct option: 2.** Charge only increments of `Cod`, not loop guards. A body visit has a unique triple $1\le i\le j\le k\le15$. Equal indices are explicitly allowed. Transform it to $(a,b,c)=(i,j+1,k+2)$. Then $1\le a<b<c\le17$. Conversely, any three-element subset of these seventeen positions gives $(i,j,k)=(a,b-1,c-2)$ in the original region. This is a bijection, so the body count is

$$B=\binom{17}{3}=\frac{17\cdot16\cdot15}{6}=680.$$

A second derivation fixes $j$. There are $j$ possible first indices and $16-j$ last indices; hence

$$B=\sum_{j=1}^{15}j(16-j)=16\cdot120-1240=680.$$

The initial ten is part of the requested final variable value: $\operatorname{Cod}_{\text{final}}=10+680=690$. Options 610, 630 and 710 would require 600, 620 and 700 increments respectively; none equals the counted region. A count of strictly increasing triples, $\binom{15}{3}=455$, omits every equality case. A rectangular count of $15^3$ includes tuples that violate the dependent bounds.

The general weak-order count is $\binom{n+2}{3}$, a cubic quantity despite the same three nesting levels as a strict-triple loop. The exact coefficients and endpoints differ. This calculation assumes that the supplied integer types avoid overflow, as the question states. It does not claim that the whole program executes only 680 primitive instructions: each nested invocation also performs header operations. Initialization changes the final accumulator while leaving the body frequency unchanged.

## Q2

**Correct option: 1.** Compare the two current head keys only while both inputs remain nonempty. Copying a leftover suffix performs writes but no further head-key comparison. The complete bottom-up ledger for the stated top-down split is:

| Merge inputs | Keys emitted by comparisons | Comparisons | Uncharged tail |
| --- | --- | ---: | --- |
| $[12]$, $[7]$ | $7$ | 1 | $12$ |
| $[5]$, $[9]$ | $5$ | 1 | $9$ |
| $[3]$, $[8]$ | $3$ | 1 | $8$ |
| $[2]$, $[6]$ | $2$ | 1 | $6$ |
| $[7,12]$, $[5,9]$ | $5,7,9$ | 3 | $12$ |
| $[3,8]$, $[2,6]$ | $2,3,6$ | 3 | $8$ |
| $[5,7,9,12]$, $[2,3,6,8]$ | $2,3,5,6,7,8$ | 6 | $9,12$ |

The total is $4+3+3+6=16$. In the last merge the head pairs are $(5,2),(5,3),(5,6),(7,6),(7,8),(9,8)$. The sixth comparison empties the right list. The remaining $9,12$ are already sorted and cannot be compared with a nonexistent right head.

Ten is the subtotal before the final merge. Twelve and fourteen are also inconsistent with the explicit ledger. The worst-case bound for an equal split of eight distinct keys is $8\log_2 8-8+1=17$; it is an upper envelope over possible inputs, not the exact count of this array. This input's final merge uses six rather than the maximum seven comparisons. Replacing the supplied instance by its worst case would answer a different question.

The accompanying trace distinguishes sixteen comparison checkpoints from seven exhaustion-and-copy checkpoints. It also exposes why comparing all cross pairs is unnecessary: each comparison advances one pointer, and neither pointer moves backward. A complete runtime ledger can charge copying, calls and bounds separately; those costs should not be relabeled as key comparisons.

## Q3

**Correct option: 2.** For each position $i$, define $I_i=1$ when its key is a new minimum, and zero otherwise. Its rank among the first $i$ distinct keys is uniformly distributed over $1,\ldots,i$ under a uniformly random permutation. Exactly one rank causes a record, so $\operatorname{Pr}(I_i=1)=1/i$. The first item certainly replaces positive infinity, hence $I_1=1$.

The replacement count is $Y=\sum_{i=1}^nI_i$. Linearity of expectation gives the exact mean

$$\operatorname{E}[Y]=\sum_{i=1}^n\operatorname{E}[I_i]=\sum_{i=1}^n\frac1i=H_n.$$

No independence assumption is needed for this step. Because $1/x$ decreases, integrating beneath and above unit-width rectangles gives $\ln(n+1)\le H_n\le1+\ln n$. For $n>1$, divide by $\ln n$; both outer ratios tend to one. Therefore $H_n\sim\ln n$, establishing the listed large-size answer. At $n=5$, the mean is $137/60$, whereas $\ln5$ is approximately 1.609; asymptotic equivalence is not an exact finite identity.

Option one counts only the first guaranteed update. Option three is the descending-array maximum, achieved when every key is smaller than all earlier keys. Option four confuses the full scan frequency with the expected frequency of its successful branch. Every input still makes $n$ comparisons against the current minimum, and full scan work is linear in the stated unit-cost model. The random variable describes assignments after successful tests, not all tests or all runtime. Repeated keys, biased permutations, or initialization from the first array entry require a modified probability model and possibly a different count.

## Q4

**Correct option: 4.** Let $m=n/k$ be a positive integer and assume $2\le k\le n$. At stage $j=2,\ldots,k$, the accumulated list contains $(j-1)m$ keys, and the incoming list contains $m$. A normal merge that materializes its output writes exactly $jm$ keys. Consequently the total output traffic across all stages is

$$W=m\sum_{j=2}^k j=m\left(\frac{k(k+1)}2-1\right).$$

This is already a tight $\Theta(nk)$ running-time ledger if each write has fixed positive cost. For a key-comparison-only model, stage $j$ uses at most $jm-1$ comparisons. These maxima can be attained together: give each list $m-1$ small keys and one large maximum, with list maxima increasing by list number and every small key below every maximum. Before merging the last pair of maxima at any stage, all the smaller keys are consumed, and the earlier accumulated maximum is then consumed before the new largest key. Every stage can therefore last until only one of its $jm$ keys remains.

Thus the exact worst-case comparison count is

$$C_{\max}=m\left(\frac{k(k+1)}2-1\right)-(k-1).$$

For $k\ge2$, the parenthesized factor lies between $k^2/2$ and $k^2$; subtracting $k-1$ changes only the tight constant under $m\ge1$. These bounds prove $\Theta(nk)$ uniformly in the legal parameter domain. When $m=1$, the exact comparison count is $k(k-1)/2$, which confirms the same tight order since $n=k$.

Option one omits the unavoidable processing of all keys. Option two is appropriate only when $k$ is fixed, not uniformly for varying $k$. Option three describes a balanced merge arrangement: each of logarithmically many levels processes the total $n$ keys. The question prescribes sequential merging, whose accumulated lengths grow linearly with the stage. Its original options use $O$; interpret the requested bound as the sharp listed standard running-time bound, with the parameter restrictions retained. At $k=1$ there are no merge stages and this ledger must be treated separately.

## Q5

**Correct option: 2.** Fix the middle index $j$. The first index can be any of $1,\ldots,j$, and the last any of $j+1,\ldots,10$, independently after that choice. This gives $j(10-j)$ triples. The row totals are:

| $j$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Valid triples | 9 | 16 | 21 | 24 | 25 | 24 | 21 | 16 | 9 |

Summing gives $10\sum_{j=1}^9j-\sum_{j=1}^9j^2=450-285=165$. An independent bijection sends $(i,j,k)$ to $(i,j+1,k+1)$, three strictly increasing elements of $1,\ldots,11$. Its inverse subtracts one from the last two entries, proving $\binom{11}{3}=165$ without approximating the region.

The first option, $120=\binom{10}{3}$, incorrectly forces $i<j$. The third, $220=\binom{12}{3}$, incorrectly permits $j=k$. The fourth doubles the valid count without a second ordering convention. For general $n$, the answer is $\binom{n+1}{3}=n(n-1)(n+1)/6$. It vanishes at $n=1$ because $j<k$ is impossible. There is no factor $3!$: the indices are already constrained to one prescribed order, and equality cases make a naive symmetry division especially unreliable.

## Q6

**Correct option: 2.** There are 144 tested pairs, but the successful branch is reached only when $j$ is a positive multiple of $i$. A fixed $i$ admits exactly $\lfloor12/i\rfloor$ such values.

| $i$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Successful bodies | 12 | 6 | 4 | 3 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 |

Their sum is 35. Counting instead by the tested target $j$ gives its number of divisors; summing those divisor counts enumerates the same successful pairs exactly once. The number 144 in option four is the rectangle of condition evaluations, not successes. Twenty-three and thirty-six fail the row ledger; proximity to the triangular count is not a counting argument.

For general $n$, let $D(n)=\sum_{i=1}^n\lfloor n/i\rfloor$. Since $n/i\ge1$, the elementary bound $x/2\le\lfloor x\rfloor\le x$ gives $(n/2)H_n\le D(n)\le nH_n$, hence tight $n\log n$ successful-body count. However, the particular program tests all $n^2$ pairs, so its full unit-cost runtime remains quadratic. A different implementation that steps directly through multiples has the same successes and fewer unsuccessful tests. Neither count can be assigned to the other implementation merely because their mathematical output agrees.

## Q7

**Correct option: 2.** Starting from one, the outer loop visits $i=2^r$ for $r=0,\ldots,5$, because $2^5=32$ still satisfies the inclusive guard. The next value 64 fails. There are six outer visits and seven outer guard tests in an ordinary pretest implementation.

| Outer $i$ | 1 | 2 | 4 | 8 | 16 | 32 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Inner executions | 1 | 2 | 4 | 8 | 16 | 32 |
| Cumulative bodies | 1 | 3 | 7 | 15 | 31 | 63 |

Multiplying the sum by two and subtracting the original sum gives $B=2^6-1=63$. Five and thirty-one would follow from the strict guard $i<32$, not the stated one. Six and thirty-two confuse the final row with the sum of rows. Thirty-two outer visits would correspond to additive rather than doubling progress.

For arbitrary integer $N\ge1$, let $h=\lfloor\log_2N\rfloor$. The exact counts are $h+1$ outer visits and $2^{h+1}-1$ inner bodies. Since $2^h\le N\le2^{h+1}-1$, the body count lies between $N$ and $2N-1$, proving tight linear total body work. The logarithmic number of stages does not make their varying costs logarithmic. Counter updates and guard costs add logarithmic or linear terms; none removes the linear lower bound when every body has fixed positive cost. Arithmetic must support the final update to 64 even though that value is not processed.

## Q8

**Correct option: 2.** Number the state before each body by $r=0,1,\ldots$. Repeated squaring gives $i_r=2^{2^r}$: it holds at $r=0$, and squaring $2^{2^r}$ produces $2^{2^{r+1}}$. The successful states are $2,4,16,256,65536$. Their exponents are $1,2,4,8,16$; the next exponent is 32 and the next state $2^{32}$ fails the bound. Hence five bodies execute.

The correct general count for an inclusive upper bound $N\ge2$ is $\lfloor\log_2\log_2N\rfloor+1$. In contrast, the strict guard $i<N$ gives $\lceil\log_2\log_2N\rceil$; these differ at the doubly exponential endpoints. Here $N=2^{16}=2^{2^4}$ lies exactly at such an endpoint, so option one omits a permitted visit. Options three and four do not follow the squaring state sequence; counting the bits of the bound is not counting squarings.

This is a visit count under mathematical integers or a type large enough for all executed arithmetic. The body at 65536 squares it to $2^{32}$ before the following guard, so unsigned 32-bit wraparound could turn it into zero and change termination. Arbitrary-precision squaring also has a cost depending on operand length. Thus a double-logarithmic body frequency is not a double-logarithmic total bit-operation claim. At $N<2$, the body frequency is zero, a separate domain case rather than a logarithm of an invalid or too-small argument.

## Q9

**Correct option: 2.** The branch is kept when $i+j$ is even, equivalently when the two indices have the same parity. For fixed $i$, there are $\lceil i/2\rceil$ kept values in $1,\ldots,i$: odd $i$ keeps its odd positions; even $i$ keeps its even positions. Therefore

$$B=\sum_{i=1}^8\left\lceil\frac i2\right\rceil=1+1+2+2+3+3+4+4=20.$$

The triangle contains $8\cdot9/2=36$ tested pairs, but its diagonal has eight even-sum pairs with no opposite-parity counterpart. Consequently parity does not split this particular finite triangle into equal halves. The rejected pairs number $36-20=16$, explaining option one. Thirty-six ignores the branch; twenty-eight removes the diagonal instead of the odd-sum positions.

For $n=2m$, pair consecutive row counts to get $m(m+1)$. For $n=2m+1$, append $m+1$ to get $(m+1)^2$. These combine as $B=\lfloor(n+1)^2/4\rfloor$. This exact formula, including both parity cases, is stronger than simply reporting quadratic order. The question-specific grid shows all tested positions, colors kept and skipped points differently, and marks the active row. Its finite picture illustrates the counting rule; the paired-row derivation proves the formula for all legal sizes.

## Q10

**Correct option: 1.** A normal invocation of the inner pretest loop with $i$ successful bodies checks `j<=i` at $j=1,\ldots,i$ and once more at $j=i+1$. There is no break, so that final false evaluation occurs in each of the five invocations.

| Outer $i$ | Inner bodies | Inner guard evaluations | Inner updates |
| --- | ---: | ---: | ---: |
| 1 | 1 | 2 | 1 |
| 2 | 2 | 3 | 2 |
| 3 | 3 | 4 | 3 |
| 4 | 4 | 5 | 4 |
| 5 | 5 | 6 | 5 |
| Total | 15 | 20 | 15 |

Thus $B=\sum_{i=1}^5i=15$ and $G=\sum_{i=1}^5(i+1)=B+5=20$. Option two discards the five terminating tests. Option three labels twenty guard checks as bodies and adds another five without a valid operation category. Option four uses the strict triangle with row lengths zero through four, not the specified inclusive inner limit.

For general $n$, the counts are $B=n(n+1)/2$ and $G=n(n+3)/2$. Inner initialization occurs $n$ times; the outer guard occurs $n+1$ times if counted separately. With costs $c_b,c_g,c_u,c_0$, the inner-loop contribution is $c_bB+c_gG+c_uB+c_0n$. Those costs and frequencies are distinct even though their leading growth is quadratic. A `break` during an inner body would invalidate $G=B+n$ for that invocation because control would skip its normal final false header test. A compound guard would additionally require counting each predicate separately.

## Q11

**Correct option: 1.** Start with a current minimum of positive infinity and compare each array element once.

| Position | Key | Minimum before comparison | Update? | Minimum afterward |
| --- | ---: | --- | --- | ---: |
| 1 | 8 | Positive infinity | Yes | 8 |
| 2 | 3 | 8 | Yes | 3 |
| 3 | 7 | 3 | No | 3 |
| 4 | 2 | 3 | Yes | 2 |
| 5 | 6 | 2 | No | 2 |
| 6 | 1 | 2 | Yes | 1 |
| 7 | 5 | 1 | No | 1 |
| 8 | 4 | 1 | No | 1 |

There are four successful assignments, at keys $8,3,2,1$, and eight comparisons. Option two counts only comparisons that return true, ignoring four failed tests. Option three assumes every visited key is a record. Option four would describe a different implementation initialized from the first key and scanning only the remaining seven entries; its later update count is three, but that initial assignment has a different accounting convention.

The state invariant after processing the first $r$ keys is that the stored minimum equals the minimum of that prefix. Each next comparison either preserves it or replaces it by a strictly smaller value, so the induction step proves correctness independent of the number of successful branches. Ascending distinct input gives one update; descending distinct input gives eight; the scan still compares every element. The expected harmonic update count in the authentic probability question relies on a uniformly random permutation and cannot be assigned to this fixed array. The accompanying state trace displays actual keys and branch outcomes rather than a generic growth animation.

## Q12

**Correct option: 3.** A body visit at $(i,j)$ costs $j$ unit operations. The total weighted work is not merely the number of index pairs. Expand the weights as a third index $t=1,\ldots,j$; each operation has one triple $1\le t\le j\le i\le n$. Either this bijection or explicit summation gives

$$W=\sum_{i=1}^n\sum_{j=1}^i j=\frac12\sum_{i=1}^n(i^2+i)=\frac{n(n+1)(n+2)}6.$$

Using the standard finite identities, the intermediate expression is $[n(n+1)(2n+1)/6+n(n+1)/2]/2$, which simplifies to the displayed cubic polynomial. Alternatively, shift the ordered triple to strict positions and obtain $\binom{n+2}{3}$ directly. This shows why a body with varying weight can behave like another counting dimension without another written `for` statement.

For $n\ge1$, $n^3/6\le W\le n^3$, since $n+1\le2n$ and $n+2\le3n$. These fixed positive witnesses establish tight cubic growth. The quadratic distractor counts $n(n+1)/2$ body invocations as though each cost one. The linear distractor ignores the inner region. The $n^2\log n$ distractor requires a logarithmic schedule absent from the program. At $n=0$, work is zero, consistent with the exact polynomial. Header overhead has quadratic order here and does not dominate the cubic weighted body work; the chosen operation model still needs to specify that all $j$ unit operations are actually performed.

## Q13

**Correct option: 1.** The five row lengths are $2,4,6,8,10$. A body belongs to one outer row, so adding those lengths counts each visit once: $B=2+4+6+8+10=30$. Pairing the first and last row lengths gives three equal pairs in the twice-written sum, or equivalently $B=2\sum_{i=1}^5i=2\cdot15$.

The options 25 and 50 replace all actual row lengths by five or ten; the second is a legitimate maximum-row upper estimate but not an exact count. Fifteen counts only $i$ visits per row and drops the factor two. For general $n$, $B=n(n+1)$. A normal inner pretest loop contributes $B+n=n(n+2)$ guard evaluations, even though guards are not charged here. To prove tightness, $n^2\le B\le2n^2$ for $n\ge1$ supplies both witnesses. The distinction between a shape-dependent exact frequency and a maximum-frequency estimate survives even when both have quadratic order.

## Q14

**Correct option: 4.** Add each permitted row rather than multiplying the final row by eight:

$$B=2(1+2+3+4+5+6+7+8)=2\cdot\frac{8\cdot9}{2}=72.$$

The last row has sixteen visits, while the average row has nine. Hence the rectangular upper estimate $8\cdot16=128$ is loose; $8^2=64$ instead assumes a nonexistent constant row length of eight. The triangular value 36 counts one copy of each row, not the stated doubled length.

As an independent check, the count changes from size seven to eight by exactly sixteen, because only the new outer row is added: $8\cdot9-7\cdot8=16$. More generally, the first difference of $n(n+1)$ is $2n$, which matches the program's row contribution. If the bound were changed to $2i-1$, the exact count would become $n^2$; that explains how a superficially similar program could make the first distractor correct. The specified even row length must therefore remain in the derivation.

## Q15

**Correct option: 3.** Write the finite set as $S_n=\{(i,j):1\le i\le n,1\le j\le2i\}$. Partition it into disjoint rows. Then

$$|S_n|=\sum_{i=1}^n2i=2\cdot\frac{n(n+1)}2=n(n+1).$$

The arithmetic identity follows by reversing the list $1,\ldots,n$: the original and reversed sums add to $n$ copies of $n+1$. At $n=0$, the empty region has zero points, consistent with the polynomial. At $n=1$, the two visits are an immediate boundary check.

The other expressions have distinct errors: $n^2$ replaces variable rows by their mean under a different endpoint convention, $2n^2$ prices every row at its maximum, and $n(n+1)/2$ deletes the multiplier two. Both the true count and $n^2$ have tight quadratic growth, but asymptotic agreement does not establish the requested exact identity. An induction supplies another proof: if size $n-1$ gives $(n-1)n$, adding row $n$ gives $(n-1)n+2n=n(n+1)$.

## Q16

**Correct option: 2.** Dependent loop bounds define the actual region. Replacing $j\le2i$ by $j\le i$, $j\le n$ or $j<2i$ gives, respectively,

$$\frac{n(n+1)}2,\qquad n^2,\qquad n^2$$

for positive consecutive inner counters. The latter two equal counts arise from different regions; equal final counts do not imply identical visited pairs. For instance, at outer index one the rectangular variant visits $n$ positions, while the strict-bound variant visits only one. Their exact boundary behavior differs.

Option one equates an exact frequency with a growth-class statement: $n(n+1)$ and $n^2$ disprove that equivalence. Option three guesses the count from two headers, ignoring the bound. Option four assumes all rows have length $2n$, despite row one having length two. A maximum-row product can supply an upper bound when the body is constant cost, but it supplies neither an exact count nor automatically a sharp lower bound. This example also warns that a final numerical result alone does not establish that the right iteration region was analyzed.

## Q17

**Correct option: 1.** The row lengths are $1,4,9,16,25$, which sum to 55. To derive their general sum rather than memorize it, telescope the identity $(i+1)^3-i^3=3i^2+3i+1$ from one to $n$. This gives

$$3\sum_{i=1}^ni^2=(n+1)^3-1-3\frac{n(n+1)}2-n,$$

which simplifies to $n(n+1)(2n+1)/6$. At $n=5$, substitution gives $5\cdot6\cdot11/6=55$. The options 125, 15 and 25 are the maximum-row product $n\cdot n^2$, the linear-row sum, and the single final row. Each measures a different quantity from the sum of actual squared rows.

A simple lower witness uses the last half of the rows: at least $n/2$ rows have length at least $(n/2)^2$, giving a cubic lower bound. The upper witness is $n$ rows of at most $n^2$ visits. Thus two visible loops can yield cubic work. The bound $i^2$ and the arithmetic that computes it must fit the declared model; an overflowed inner limit is not the same mathematical region.

## Q18

**Correct option: 4.** The exact ledger is

$$1+4+9+16+25+36+49+64=204.$$

The independently derived square-sum formula confirms $8\cdot9\cdot17/6=204$. Removing the final row leaves 140, and the difference 64 exactly matches the eight-squared row. This local check detects accidental omission of the inclusive endpoint.

Five hundred twelve assumes every one of the eight rows has length 64. Thirty-six adds row indices rather than their squares. Sixty-four counts only the final row. Those are not alternative approximations to an exact question. If full inner guard frequency were requested, ordinary pretest semantics would add one failed test per outer row and give $204+8=212$; inner updates remain 204. If each body itself cost $i$ operations, the weighted total would instead be $\sum_{i=1}^8i^3$, not 204. The lesson is to preserve both the row-frequency formula and the cost attached to a visit before taking a leading growth term.

## Q19

**Correct option: 3.** Let $S(n)=\sum_{i=1}^ni^2$. A constructive induction proves the proposed formula. The base $S(0)=0$ agrees with $0\cdot1\cdot1/6$. Assuming the formula at $n-1$,

$$S(n)=\frac{(n-1)n(2n-1)}6+n^2=\frac{n(n+1)(2n+1)}6.$$

This establishes the exact identity over all nonnegative integer sizes. At one, several distractors may coincide numerically, so that special case cannot establish a universal expression. At two, the actual five visits disagree with the distractor values three, four and eight.

For $n\ge1$, the explicit formula is at least $n^3/3$ and at most $n^3$, since $n+1\ge n$, $2n+1\ge2n$, and the maximum-row product is $n^3$. These are fixed positive tight cubic witnesses. The other polynomial expressions do not satisfy the correct row-increment identity $S(n)-S(n-1)=n^2$. A symbolic candidate should be checked against that recurrence and its starting value, rather than accepted merely because it has the right degree.

## Q20

**Correct option: 2.** Even with a fixed exponent of two, the index-dependent inner bound creates cubic total work. More generally, fixed $p\ge0$ gives $\sum_{i=1}^ni^p\in\Theta(n^{p+1})$: every term is at most $n^p$, while the last half contribute at least $(n/2)^p$ each. The lower constant $2^{-(p+1)}$ may depend on a truly fixed $p$.

If the exponent changes with the input, that fixed-parameter proof is not uniform. For example, at $p=n$ the final row alone has $n^n$ visits, exceeding every fixed-degree polynomial. This explains the valid statement about a variable exponent without pretending that the original exponent two was itself variable.

The largest row is $n^2$, but it is only part of the total; option one loses all earlier rows. Option three's universal quadratic assertion is refuted by the exact square-sum polynomial. Option four replaces $i^2$ by $i$, turning cubic work into a different quadratic program. Counting headers provides a useful starting point for control-flow inspection, not a theorem about polynomial degree. If a body contains a nonconstant routine, the degree can change again even with the same bounds.

## Q21

**Correct option: 4.** The inclusive stages zero through five contribute $1,2,4,8,16,32$. Their sum is 63. With $S=1+2+\cdots+32$, subtracting $S$ from $2S$ cancels all interior powers and leaves $S=64-1$.

The number 31 omits the stage-five row; 160 multiplies five by the final length 32, both using the wrong stage count and ignoring changing row lengths. Twenty-five treats the program as a square region unrelated to its exponential bound. The first row contributes one, not zero.

The parameter here is the maximum exponent, not the final numerical counter value. There are six stages but a final scale of $N=2^5=32$. General work $2^{n+1}-1$ is exponential in exponent parameter $n$ and linear in numeric scale $N=2^n$. This distinction is necessary when reporting complexity relative to an encoded input. It also shows why replacing the total by the number of outer stages misses the expensive last rows. Ordinary inner guard tests would add six to 63 under a conventional pretest implementation, a separate requested operation count.

## Q22

**Correct option: 3.** Stages zero through eight have nine rows. The exact geometric sum is $2^9-1=511$. A useful ledger splits the last row from the prefix: stages zero through seven contribute 255, then stage eight contributes 256, totaling 511.

The option 255 drops that last row. Sixty-four is $n^2$ and has no correspondence to either the nine stage visits or the row lengths. Two thousand forty-eight is $n2^n$; it overprices the earlier rows and even uses eight instead of nine rows in its rectangular interpretation.

The last row accounts for just over half the total: $256/511>1/2$. This demonstrates the geometric domination principle with its exact constant, rather than merely naming linear order in the final scale. At general exponent $n$, $2^n\le2^{n+1}-1<2\cdot2^n$. The tight bound is therefore in terms of $2^n$, not $n$ alone. A program emitting each counted unit has an output lower bound equal to this total; a program only computing the geometric-sum formula need not execute these 511 bodies and is a different computational task.

## Q23

**Correct option: 2.** Let $S_n=\sum_{j=0}^n2^j$. Algebra gives $2S_n-S_n=2^{n+1}-1$, proving the expression. Alternatively, $S_0=1$ and $S_n=S_{n-1}+2^n$ uniquely determine it. The inclusive zero stage matters: the candidate $2^n-1$ is the prefix terminating at exponent $n-1$.

The remaining candidates, $n^2$ and $n2^n$, replace the exact geometric region by unrelated square or maximum-row counts. Their disagreement can be seen at $n=2$, when the true seven visits differ from four, eight and three. Accidental equality at a smaller parameter cannot establish a universal formula.

For a fixed base $b>1$, the same derivation gives $\sum_{j=0}^nb^j=(b^{n+1}-1)/(b-1)$ when the row lengths are integer-defined. The factor $1/(b-1)$ is fixed only when the base is fixed. If the row multiplier varies by stage, the simple geometric identity no longer applies. These scope conditions explain when the algebra counts a real sequence of visits rather than a superficially similar loop.

## Q24

**Correct option: 1.** Put $N=2^n$ to describe the largest numeric scale. The number of stages is $n+1=\log_2N+1$, but their total inner work lies between $N$ and $2N$. Thus logarithmically many stages can have linear work in the largest scale. They would have logarithmic work only if each stage performed uniformly constant work.

Option two drops the stage weights. Option three assigns the final row length to every earlier row and obtains only a loose upper estimate. Option four erases the actual one-unit row at exponent zero. The paired descriptions “exponential in the exponent” and “linear in the final scale” are compatible because they use different input measures; neither should be reported without stating the parameter.

A useful counterexample to stage-count inference is to charge $2^{2j}$ per stage instead of $2^j$. The number of stages stays $n+1$, while the sum becomes $\sum_{j=0}^n4^j=(4^{n+1}-1)/3$, tight quadratic order in $N$. The unchanged outer control flow does not preserve total cost when the body work changes. This reasoning also applies to allocations, output writes and library routines hidden in an apparently short body.

## Q25

**Correct option: 2.** Fix divisor $j$, then list its targets among $1,\ldots,5$. The permitted targets are all positive multiples of $j$:

| Divisor $j$ | Targets $i$ | Count |
| --- | --- | ---: |
| 1 | $1,2,3,4,5$ | 5 |
| 2 | $2,4$ | 2 |
| 3 | $3$ | 1 |
| 4 | $4$ | 1 |
| 5 | $5$ | 1 |

Their sum is ten. Counting by target instead gives divisor counts $1,2,2,3,2$, again ten; this is a double-counting identity, not a change to the legal pairs. The rectangular twenty-five counts every condition test. Fifteen prices a triangular region that divisibility does not define. Five counts only diagonal pairs and omits, for example, $(4,1)$ and $(4,2)$.

The original all-pairs implementation still performs twenty-five divisibility tests, even though only ten bodies execute. A multiple-stepping implementation can reach the same successful pairs directly with ten bodies. The distinction becomes asymptotically important: successes have tight $n\log n$ growth while the all-pairs condition frequency is $n^2$.

## Q26

**Correct option: 1.** The fixed-divisor row lengths at size eight are $8,4,2,2,1,1,1,1$. Therefore the count is $8+4+2+2+1+1+1+1=20$. Floors are essential: the row for divisor three has targets three and six, not a fractional $8/3$ visits.

Sixty-four in option two counts all tested pairs, and thirty-six is the positive triangular pair count with no divisibility justification. Eight retains only the diagonal. For an independent incremental check, moving from size seven to eight adds the targets of new value eight, whose divisors are $1,2,4,8$; the count grows from sixteen to twenty. Each newly counted pair is uniquely identified by that new target.

For general $n$, this increment is the number of positive divisors of $n$. It is not constant, so the exact divisor sum does not reduce to a linear function even though many rows near the upper bound have one visit each. Reversing the counting order is valid because the finite set is unchanged; it should not be confused with assuming that divisor counts and multiple counts agree pointwise at the same index.

## Q27

**Correct option: 4.** For each fixed divisor $j$, legal targets have the form $i=tj$ with integer $1\le t\le\lfloor n/j\rfloor$. The correspondence between $t$ and target $i$ is one-to-one, and the different divisor rows are disjoint as ordered pairs. Consequently

$$D(n)=\sum_{j=1}^n\left\lfloor\frac nj\right\rfloor.$$

At $n=1$, some distractors coincide with this expression, so that boundary alone cannot identify a universal formula. At $n=3$, the count is five, differing from $n^2=9$, $n(n+1)/2=6$ and $n=3$.

Uniform tight growth follows without treating a floor as equality. For $x\ge1$, $x/2\le\lfloor x\rfloor\le x$; apply this with $x=n/j$ and sum to obtain $(n/2)H_n\le D(n)\le nH_n$. The harmonic bounds then establish $\Theta(n\log n)$. The exact expression is still a discrete floor sum; the asymptotic class is its growth summary, not its finite value. For $n=0$, the empty sum is zero and the corresponding all-pairs region is empty.

## Q28

**Correct option: 3.** The all-pairs code evaluates its condition exactly $n^2$ times, but the successful-body frequency is $D(n)$. These ledgers differ already at $n=2$: four tests but three successes, with pair $(1,2)$ rejected. A skipped body does not undo the test that determined it should be skipped.

For sufficiently large $n$, harmonic comparison gives $D(n)/n^2=O((\log n)/n)\to0$, so an increasing fraction of all-pairs tests are unsuccessful. Option one cannot be justified even by an asymptotic replacement. Option two mistakes reordering a finite double count for changing its set. Option four reverses the causal order of branch evaluation.

Changing the implementation to iterate only over multiples reduces condition overhead while preserving the successful pairs. If `body` is constant cost, this can change full time from quadratic to tight $n\log n$. If instead each successful body costs $n$ operations, the weighted body work becomes $nD(n)$ and can dominate the original rectangle overhead. The charged operation and its cost must therefore be declared before translating a success count into runtime.

## Q29

**Correct option: 3.** The visited indices are one through fifteen. Partition them into five blocks $(1,2,3),(4,5,6),(7,8,9),(10,11,12),(13,14,15)$. Exactly the third index in every block is divisible by three and skipped; the other two run the body. The count is $5\cdot2=10$.

Fifteen counts all visits before filtering. Five counts the skipped multiples. Nine loses one valid nonmultiple despite the final index being skipped anyway. Removing the upper endpoint fifteen would not remove an executed body in this instance; removing index fourteen would. This distinction shows why an endpoint adjustment must be tied to the residue class rather than applied mechanically to every count.

At general inclusive bound $M$, the count is $M-\lfloor M/3\rfloor$. Putting $M=3n$ gives exactly $2n$. The condition is still evaluated on all $3n$ indices in the direct loop. A `continue` skips the later body; in a conventional `for` loop its update expression still executes, ensuring progress to the next index.

## Q30

**Correct option: 2.** There are 24 visited indices and eight skipped multiples, namely $3,6,9,12,15,18,21,24$. Subtracting gives $24-8=16$ body executions. Equivalently, eight complete residue blocks contribute two executions each.

Fifteen in option one wrongly subtracts an extra body at the endpoint. Twenty-four in option three ignores filtering. Eight in option four counts failures rather than successes. Although the number of blocks and the number of skipped indices both equal eight here, their meanings are different and should not be interchanged in a changed filter.

If the inclusive bound were $3n+1$, the extra index is not divisible by three and the answer would become $2n+1$. With bound $3n+2$, it becomes $2n+2$. These boundary cases are immediate tests of the general expression $M-\lfloor M/3\rfloor$. They also expose why a ratio of approximately two thirds is an asymptotic density statement rather than a universally exact multiplication rule for every final bound.

## Q31

**Correct option: 1.** The skipped subset is $\{3t:1\le t\le n\}$, which has exactly $n$ elements. It is a subset of the full $3n$ visited indices, so its complement contains $3n-n=2n$ elements. This complement argument and the two-per-block partition independently establish the exact expression.

The distractor $3n$ neglects the condition, $n$ counts the complement's excluded part, and $2n-1$ makes an unjustified endpoint subtraction. At $n=1$, the executed indices one and two directly confirm the count two. At $n=0$, the empty loop has zero successful bodies, consistent with the formula if this boundary is included.

More generally, skipping multiples of a fixed positive integer $d$ through inclusive bound $M$ gives $M-\lfloor M/d\rfloor$. When $M=dn$, this becomes $(d-1)n$. The special case $d=1$ skips every index; a generic positive linear lower-bound assertion must exclude that case. The residue predicate controls the body frequency, while header and condition frequencies belong to separate ledgers.

## Q32

**Correct option: 4.** A C-style `for` loop executes its update expression after a `continue` in the body. Thus this fragment still progresses and processes all indices:

```c
for (int i = 1; i <= 3*n; ++i) {
    if (i % 3 == 0) continue;
    tick();
}
```

It performs $3n$ divisibility tests and $2n$ calls to `tick`, assuming sufficient integer capacity. In contrast, moving the update into a `while` body creates a different control-flow contract:

```c
int i = 1;
while (i <= 3*n) {
    if (i % 3 == 0) continue;
    tick();
    ++i;
}
```

For $n\ge1$, the second fragment reaches three and then repeats it forever because the update is bypassed. Its finite body-prefix count is not a runtime bound for a terminating program. This concrete counterexample explains why option two's universal update assertion is false. Option one confuses continuing with breaking, and option three confuses a visited-but-skipped index with an index the loop never visits. A correct operation ledger depends on the actual locations of the update and branch, not only on an informal description of the desired filtering.

## Q33

**Correct option: 3.** For five allowed values, shift weakly ordered indices by $(i,j,k)\mapsto(i,j+1,k+2)$ to obtain a strict triple chosen from seven values. This invertible shift gives $\binom73=35$.

A direct middle-index ledger gives $1\cdot5+2\cdot4+3\cdot3+4\cdot2+5\cdot1=35$: fixing $j$ leaves $j$ first-index choices and $6-j$ third-index choices. This independently verifies the bijection and includes equality cases such as $(2,2,2)$.

The rectangular 125 includes illegal orderings. Fifteen counts weak pairs rather than triples. Ten is $\binom53$, valid only when all indices must differ. A useful decomposition classifies weak triples by multiplicities: all distinct contribute ten, exactly two equal contribute $2\binom52=20$, and all equal contribute five. Their sum is 35. The factor two in the middle category records whether the smaller or the larger chosen value is repeated; it is not a permutation multiplier for an already ordered triple.

## Q34

**Correct option: 2.** With eight allowed values, the shifted strict-triple count is $\binom{10}{3}=10\cdot9\cdot8/6=120$. By multiplicity categories, the same count is

$$\binom83+2\binom82+8=56+56+8=120.$$

Thirty-six is a weak-pair count and loses the third index. Fifty-six permits only three distinct values. Five hundred twelve counts the full cube of ordered triples, including reverse or mixed orderings. The weak-order restriction is therefore essential even though all these expressions have familiar polynomial forms.

At size seven, the corresponding count is $\binom93=84$. The difference 36 is precisely the number of triples whose last entry is the newly admitted value eight: first and middle entries form a weak pair in eight values. This recurrence-based check tests the inclusive endpoint and gives a second way to recognize the counting polynomial. No factorial division of $8^3$ handles repeated indices correctly, because their symmetry orbits have different sizes.

## Q35

**Correct option: 1.** The shift to strict positions proves the exact universal formula $\binom{n+2}{3}$. Expanding it gives $n(n+1)(n+2)/6$. A second proof partitions by the last index $k$: the possible first two entries form a weak pair, numbering $k(k+1)/2$, and summing from one to $n$ gives the same cubic polynomial.

Strict triples instead number $\binom n3$. The cube $n^3$ counts unconstrained ordered triples, and $n(n+1)/2$ counts only two entries. At $n=1$, both the true triple count and the pair count equal one; this exceptional equality is not a proof of the pair expression for all sizes. At $n=2$, the valid triples are $(1,1,1),(1,1,2),(1,2,2),(2,2,2)$, already distinguishing four from the pair count three.

Uniform cubic bounds follow from $n^3/6\le\binom{n+2}{3}\le n^3$ for $n\ge1$. Exact lower-order terms retain equality information that a cubic growth class suppresses. If some inequalities become strict, repeat the shift carefully rather than reusing the added-two capacity without checking which repetitions remain legal.

## Q36

**Correct option: 4.** Weak inequalities allow equality; strict inequalities prohibit it. The exact counts for all weak and all strict versions are $\binom{n+2}{3}$ and $\binom n3$. Their difference is

$$\binom{n+2}{3}-\binom n3=n^2,$$

also obtained by counting exactly-two-equal triples, $2\binom n2=n(n-1)$, and all-equal triples, $n$. Thus an exact quadratic number of equality cases is removed even though both main counts have cubic tight growth for growing $n$.

Option one contradicts permitted examples such as $(1,1,1)$. Option two admits illegal rectangle points such as $(2,1,2)$. Option three confuses equality with an ordering violation. At $n=2$, the strict region is empty while the weak region has four triples, a sharp boundary counterexample. A leading-order approximation would hide that difference. Mixed conditions such as $i\le j<k$ have their own shifted formula $\binom{n+1}{3}$ and should be counted from their actual permissions.

## Q37

**Correct option: 1.** At fixed outer stage $i$, represent the inner counter by exponent $r$: its visited values are $2^r$ for $r=i,i+1,\ldots,5$. Inclusive exponent five is visited at every outer stage. The row lengths for $i=0,1,2,3,4$ are $6,5,4,3,2$, totaling twenty.

The candidate fifteen subtracts one endpoint per row, matching a strict upper guard instead. Twenty-five multiplies two maxima, ignoring the correlated start. Thirty-two counts the largest numerical counter value rather than how many times the loop body executes.

At general exponent parameter $n$, the row length is $n-i+1$, so the sum is $n(n+3)/2$. Under a model allowing the powers and one-step doubling, work is quadratic in exponent $n$ and quadratic-logarithmic in final scale $N=2^n$. Ordinary binary representation of $N$ has $n+1$ bits, giving another consistent way to describe the parameter. Computing $2^i$ or multiplying unbounded counters is not necessarily unit cost in a bit model, which must be specified separately.

## Q38

**Correct option: 4.** Eight outer stages, numbered zero through seven, have inner exponent ranges ending inclusively at eight. Their row lengths are $9,8,7,6,5,4,3,2$. Pairing the first and last gives eleven, as do the other three pairs, so the total is $4\cdot11=44$.

Thirty-six counts the ranges with the final exponent omitted. Sixty-four treats every row as length eight, even though the first has nine and the last two. Two hundred fifty-six is the largest counter value $2^8$, not a visit frequency. The maximum-row product $8\cdot9=72$ would be a valid upper estimate, but it also would not be exact.

The independent formula $8(8+3)/2=44$ confirms the pairing count. With an ordinary inner pretest loop, the total header tests become $44+8=52$, because each of the eight invocations contributes its terminating false test. A wrong endpoint therefore propagates once per outer stage, rather than as a single global off-by-one error. This is why the exponent grid and per-row guard contract should be written before simplifying the polynomial.

## Q39

**Correct option: 3.** After $t$ doublings in outer row $i$, the counter is $2^{i+t}$. The inclusive guard is true exactly when $i+t\le n$. Nonnegative integers $t=0,\ldots,n-i$ give $n-i+1$ visits. Summing over $i=0,\ldots,n-1$ yields

$$B=\sum_{i=0}^{n-1}(n-i+1)=\sum_{r=2}^{n+1}r=\frac{n(n+3)}2.$$

The missing row of length one is not an error: outer stage $i=n$ is absent. With that extra outer stage included, the count would be $(n+1)(n+2)/2$. With a strict inner upper guard instead, the original outer stages give $n(n+1)/2$, explaining that distractor.

The square $n^2$ ignores the shifting start, and $2^n$ confuses value with frequency. At $n=1$, the single row visits one and two, giving two, while the three distractors give one, two and one; accidental equality of $2^n$ at that small size does not establish its general claim. At $n=3$, the correct nine differs from the exponential eight. The explicit row derivation resolves the universal-expression question even when isolated checks do not.

## Q40

**Correct option: 2.** Doubling advances the exponent by one, not the counter value by one. For example, row $i=2$ with terminal exponent five visits $4,8,16,32$: four visits across a numerical interval containing 29 integers. Its frequency comes from the exponent interval $2,3,4,5$.

Option one is refuted by the starts one, two and four in the first three rows. Option three is refuted by skipping six between four and eight. Option four incorrectly omits $2^n$, which satisfies the inclusive guard in every row. Replacing the start by one in all rows produces a different rectangular exponent region with $n(n+1)$ visits, not $n(n+3)/2$.

The useful general transformation is to solve the guard inequality for the number of updates. Starting at positive $a$ and multiplying by a fixed $b>1$ while the value is at most $M$ gives $\lfloor\log_b(M/a)\rfloor+1$ visits when $a\le M$. If $a>M$, the count is zero. The domain and guard must be checked before applying the logarithm, especially when a start depends on another loop index.

## Q41

**Correct option: 1.** Two length-five lists contain ten keys. Each head comparison emits one key and advances one pointer. Immediately before a comparison both lists are nonempty, so at most nine keys can be emitted by comparisons before one empties. The bound is attainable with $A=[1,3,5,7,9]$ and $B=[2,4,6,8,10]$: emissions alternate through nine and leave ten as an uncharged suffix. Thus the exact maximum is nine.

Ten charges the final copy as though a second head existed. Twenty-five compares every cross pair despite monotone progress. Four is even below the minimum head comparisons for two nonempty length-five lists: consuming either one requires five advances. The concrete construction proves the lower witness for the maximum, rather than merely assuming a bound can be reached.

For general positive equal length $n$, the minimum is $n$, attained when all keys in one list precede the other's, and the maximum is $2n-1$. These are exact comparison bounds; materializing the output still writes all $2n$ keys in either case. The input-specific trace and the worst-case construction serve different purposes and should be labeled accordingly.

## Q42

**Correct option: 4.** A length-eight interleaving construction uses odd keys $1,3,\ldots,15$ in the first list and even keys $2,4,\ldots,16$ in the second. Fifteen comparisons emit the keys one through fifteen. The first list empties when fifteen is emitted, leaving sixteen to copy without another key comparison.

Sixteen counts that final copy, sixty-four enumerates a rectangle of key pairs the algorithm never visits, and seven cannot exhaust either eight-key input. The number fifteen is both an upper bound, from one advance per comparison and at least one leftover key, and an attained count. Both ingredients are necessary for an exact worst-case statement.

With general unequal positive lengths $p,q$, the same reasoning gives maximum $p+q-1$ and minimum $\min(p,q)$. If one input is empty initially, the head-comparison count is zero, so the nonempty premise cannot be dropped from the maximum formula. Ties require a tie policy for exact traces and stability, but the monotone-pointer upper argument still applies. This problem assumes distinct keys, allowing a clean strict interleaving witness.

## Q43

**Correct option: 3.** There are $2n$ keys. Every comparison consumes exactly one, and the guard stops when one input empties. At least one key remains to append, so $C\le2n-1$. Alternating odd and even sorted inputs attain equality for every positive integer $n$, proving that this bound is the exact worst-case count.

A formal progress measure is the number of unconsumed keys. It decreases by one at each comparison; monotone pointers prevent revisiting any consumed item. The proof therefore counts moves, not all possible pairs between lists. The square $n^2$ lacks an attainable quadratic family for this implementation. The expression $n-1$ is below the minimum required to empty a length-$n$ input. The expression $2n$ includes one step past the stopping condition.

At $n=1$, exactly one comparison selects the smaller singleton and the other is copied, matching $2n-1$. At $n=0$, both inputs are empty and the count is zero, so applying the displayed expression would incorrectly give minus one. The stated positive-size domain is essential for this exact formula even though a zero-size extension has no effect on the asymptotic linear class.

## Q44

**Correct option: 2.** Once one list empties, every remaining key comes from the other already sorted list. No ordering choice between two heads remains. For example, merging $[1,2,3]$ with $[10,11,12]$ uses three head comparisons and then copies three keys. Those copies are necessary output operations but are not three extra head comparisons.

Option one contradicts the exact linear bound $p+q-1$ for nonempty inputs. Option three introduces unnecessary comparisons inside an already ordered suffix. Option four mistakes two moving pointers for two independently nested enumeration ranges. The total number of pointer advances cannot exceed the number of available keys.

The operation ledger should distinguish comparisons, reads and writes. With output materialization, exactly $p+q$ keys are written even on a minimum-comparison input. If an implementation repeatedly copies its entire current prefix instead of appending once, its copying cost may be larger, but that is an additional implementation cost rather than a change to the merge's head-comparison theorem. Defining the counted operation prevents both undercharging full runtime and overcharging comparisons.

## Q45

**Correct option: 2.** Each positive pair $(i,j)$ with $ij\le n$ admits exactly $\lfloor n/(ij)\rfloor$ positive choices of $k$. Hence the exact count is

$$A(n)=\sum_{i=1}^n\sum_{j=1}^{\lfloor n/i\rfloor}\left\lfloor\frac{n}{ij}\right\rfloor.$$

For an upper bound, replace the floor by its argument and enlarge the inner range to $1,\ldots,n$, adding only nonnegative terms. This gives $A(n)\le nH_n^2=O(n(\ln n)^2)$.

For a matching lower bound, set $m=\lfloor n^{1/3}\rfloor$. All $1\le i,j\le m$ satisfy $ij\le n^{2/3}\le n$, so their pairs are feasible. Since $n/(ij)\ge1$, the inequality $\lfloor x\rfloor\ge x/2$ applies. Restricting the exact sum to this square gives

$$A(n)\ge\frac n2\sum_{i=1}^m\sum_{j=1}^m\frac1{ij}=\frac n2H_m^2.$$

For $n\ge64$, $m\ge n^{1/3}/2$. The harmonic lower bound then gives $H_m\ge\ln(m+1)\ge(\ln n)/3-\ln2\ge(\ln n)/6$. Thus $A(n)\ge n(\ln n)^2/72$, an explicit uniform witness. Both bounds establish the requested tight class.

The first option omits one harmonic aggregation. The quadratic and cubic options overcount the product-constrained region as more rectangular than it is; their ratios to $n(\ln n)^2$ diverge. At $n=1$, the exact count is one, although the asymptotic expression vanishes there; exact boundary values are not supplied by a large-size class. The layer-grid animation shows legal $(j,k)$ pairs separately for fixed $i$ on a small instance, complementing the analytic proof rather than replacing it by a finite plot.

## Q46

**Correct option: 2.** For fixed $i$, the two guard conditions require $1\le j\le n$ and $j\le n-i$. Since $i\ge1$, the second is the stronger upper bound. If $i=n$, no positive $j$ satisfies it. The row lengths are therefore $n-1,n-2,\ldots,1,0$, and

$$B=\sum_{i=1}^n(n-i)=\frac{n(n-1)}2.$$

An independent bijection maps $(i,j)$ to $(i,s=i+j)$. The admissible values satisfy $1\le i<s\le n$, so they are exactly the two-element subsets of $1,\ldots,n$. This gives $\binom n2$ and confirms the endpoint convention.

Option one adds one invalid position per outer row. The rectangle $n^2$ ignores the sum constraint. The final option $n-1$ counts only the first row. At $n=1$, the entire region is empty; at $n=2$, it contains only $(1,1)$. Such checks expose a missing empty last row.

For full guard accounting under left-to-right short circuit, `j<=n` is evaluated $n-i+1$ times in each row. The last tested value is $j=n-i+1\le n$, so `i+j<=n` is also evaluated on every such test; it supplies the terminating false outcome. Both predicate frequencies total $B+n=n(n+1)/2$, despite only $B$ body visits. This explains why the logical conjunction and body count must not be treated as one undifferentiated operation.
