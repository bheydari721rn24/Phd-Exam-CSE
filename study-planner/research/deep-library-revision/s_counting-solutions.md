## Q1

**Correct option: 4.**

### Separate the constraints before counting
The first equation is $x_1+x_2+x_3=5$. Subtract it from $x_1+x_2+x_3+x_4+x_5=20$ to obtain $x_4+x_5=15$. All coordinates are nonnegative integers. Thus a solution is uniquely a choice of a triple totaling 5 and a pair totaling 15. Neither choice changes the other total.

Encode the triple by five stars and two separators. Adjacent separators represent a zero coordinate, so every nonnegative triple is represented. Choosing the two separator positions among seven gives $\binom72=21$. For the pair, choose $x_4$ freely from $0$ through $15$; then $x_5=15-x_4$. There are 16 possibilities. The reversible construction gives

$$N=\binom72\binom{16}1=21\cdot16=336.$$

The multiplication is justified by a Cartesian product of solution sets, not an independence assumption about random variables. Counting five coordinates with total 20 alone would ignore the first equation. Counting positive coordinates would forbid permitted zero values. An extra factorial would order units that the problem treats as indistinguishable. Directly checking the two equations identifies option 4.

**Extension.** For totals $u$ and $v$, the corresponding number is $\binom{u+2}2(v-u+1)$ when $v\ge u\ge0$; otherwise it is zero. This feasibility check must precede the formula.

## Q2

**Correct option: 2.**

### Partition by the number selected from the first block
The ten objects are distinct. The requirement admits exactly four or five objects from the first five. A choice of three from that block and all five from the second block is feasible as a size-eight subset, but fails the explicit lower bound. Fewer than three cannot supply eight objects because the second block contains only five.

For four from the first block, choose its four members in $\binom54=5$ ways and four from the second block in $\binom54=5$ ways. This gives 25 subsets. For five from the first block, all five are forced and the second block contributes three members in $\binom53=10$ ways. The cases cannot overlap because their first-block counts differ:

$$N=\binom54\binom54+\binom55\binom53=25+10=35.$$

An independent complement check starts with all $\binom{10}8=45$ subsets. The only excluded feasible case has three in the first block and five in the second, giving $\binom53\binom55=10$. Hence $45-10=35$, option 2. Selecting four witnesses in the first block and freely adding four other objects would count a subset containing five first-block objects five times. Choose the exact count, not a nonunique witness.

## Q3

**Correct option: 4.**

### Two distinct symmetries require two distinct quotients
First label the three groups $A,B,C$. An ordering of all $3n$ distinct objects determines consecutive blocks of size $n$. For a fixed labeled partition, internal order can change in $(n!)^3$ ways, so the labeled count is $(3n)!/(n!)^3$.

Now erase the group labels. Because $n\ge1$, the three disjoint groups are nonempty and distinct as sets. Every unordered partition admits exactly $3!$ assignments of labels. Consequently

$$N=\frac{(3n)!}{3!(n!)^3}.$$

This is option 4. Keeping the factor $3!$ would count named groups; omitting the three internal factorials would count ordered listings inside groups. These are different outcomes. The quotient argument is valid because the fiber size is constant: six labeled descriptions per final partition. Equal group sizes do not by themselves authorize division when the groups remain named.

**Small check and boundary.** At $n=1$, three singleton objects have exactly one unordered partition, and $3!/(3!\cdot1)=1$. At $n=0$, the displayed quotient would be $1/6$ and is not valid: three empty groups do not create six distinct labeled partitions. An empty-size convention must be specified separately.

## Q4

**Correct option: 2.**

### Count a subset with three marked members in two orders
Let $S$ be an $i$-subset of a seven-element set and let $R$ be a three-subset of $S$. Choosing $S$ first gives $\binom7i\binom i3$. Choosing $R$ first gives $\binom73\binom4{i-3}$, because only the other four elements remain available. This proves the term identity without guessing a simplification.

Sum over $i=3,\ldots,7$. After the three marked members are chosen, each of the four unmarked elements is independently included or excluded as a counting choice. Thus

$$\sum_{i=3}^{7}\binom i3\binom7i=\binom73\sum_{j=0}^{4}\binom4j=35\cdot16=560.$$

The requested quantity is $A=560/10=56$, which belongs to $(30,60]$, option 2. The five individual contributions are $35,140,210,140,35$, another exact check. Summing $\binom7i$ alone discards the choice of the marked triple; keeping only $\binom73$ discards the optional remainder. The multiplier $1/10$ is applied after the entire sum.

## Q5

**Correct option: 1.**

### A monotone map is a multiplicity vector
For a weakly increasing map on a five-element ordered domain with codomain $\{1,2,3,4,5\}$, let $c_j$ count outputs equal to $j$. Each $c_j\ge0$ and $\sum_{j=1}^{5}c_j=5$. Conversely, a vector of these counts reconstructs exactly one weakly increasing output sequence by writing the 1s, then the 2s, and so on. This is a bijection, not merely a bound.

Five stars and four bars give

$$N=\binom{5+5-1}{5-1}=\binom94=126.$$

Thus option 1 is correct. Counting arbitrary maps gives $5^5$, but most violate monotonicity. Requiring strict increase would force the sequence $1,2,3,4,5$ and give one, which is a different requirement. Sorting all arbitrary maps and dividing by $5!$ is invalid because repeated outputs produce different numbers of preimages. For example the constant sequence has one preimage, whereas the all-distinct sequence has 120.

For an ordered domain of size $m$ and a codomain of size $r\ge1$, the weak count is $\binom{m+r-1}{r-1}$. Requiring every output value adds $c_j\ge1$ and changes the answer to $\binom{m-1}{r-1}$ when $m\ge r$.

## Q6

**Correct option: 2.**

### Count positions first, then fill the remaining positions
The word has length four over $\{0,1,2,3\}$, and the number of zeros must be even. The possible zero counts are 0, 2, and 4. For a specified zero count $k$, choose its positions in $\binom4k$ ways; each remaining position has three nonzero choices. The cases are disjoint:

$$A=\binom40 3^4+\binom42 3^2+\binom44 3^0=81+54+1=136.$$

The requested ratio is $A/4=34$, option 2. An independent parity filter uses $E+O=4^4=256$ and $E-O=(3-1)^4=16$, yielding $E=136$. Half the unrestricted count, 128, is wrong: the parity classes are unequal. The all-zero word belongs to the event, and the zero-zero-count term means no zeros, not zero words.

For length $m\ge0$, $E_m=(4^m+2^m)/2$ and $O_m=(4^m-2^m)/2$. At $m=0$, the empty word is a single even-parity word. No limiting argument or random approximation is involved.

## Q7

**Correct option: 4.**

### Surjectivity removes empty target categories
Six domain elements are distinct and four target values are named. There are $4^6$ unrestricted maps. For target $j$, let $B_j$ mean that value $j$ is missing. A selected set of $i$ forbidden target values leaves $(4-i)^6$ maps. Inclusion–exclusion gives

$$A=4^6-\binom41 3^6+\binom42 2^6-\binom43 1^6+\binom44 0^6.$$

The terms are $4096-2916+384-4+0=1560$. Therefore $A/30=52$, option 4. Subtracting only the first missing-category terms would subtract maps missing two categories twice, so the positive pair correction is essential.

**A second construction.** Positive fiber sizes totaling six are either $(3,1,1,1)$ or $(2,2,1,1)$ up to order. The first type contributes $4\cdot6!/3!=480$. The second contributes $\binom42\cdot6!/(2!2!)=1080$. Their sum is 1560. Distinct objects require multinomial weights; stars and bars alone counts only size vectors. Erasing target labels would additionally divide by $4!$, but this problem retains them.

## Q8

**Correct option: 4.**

### Solve the exponent equation before evaluating a coefficient
Choose $j$ of the fourteen factors to contribute $x^2$ and the remaining $14-j$ to contribute $x^{-1}$. The resulting exponent is

$$2j-(14-j)=3j-14.$$

For an $x^{14}$ term, $3j-14=14$, so $j=28/3$, not an integer. No choice of factors produces that exponent. The coefficient $A$ is therefore zero and $A/5=0$, option 4. A binomial coefficient with a rounded index would create a nonexistent term.

More generally, the possible exponents are $-14,-11,-8,\ldots,28$. The coefficient of $x^m$ is $\binom{14}{(m+14)/3}$ if $(m+14)/3$ is an integer between 0 and 14, and is zero otherwise. The expansion is a Laurent polynomial; negative powers are legitimate. At $m=13$, for example, $j=9$ and the coefficient is $\binom{14}9$. An exponent range check alone is insufficient: the congruence condition is equally necessary.

## Q9

**Correct option: 2.**

### Keep parity after shifting the lower bound
Write $a=2j$ and $c=1+c'$ with $j,c'\ge0$. Then $2j+b+c'=19$ with $b\in\{0,1,2,3,4\}$. Fixing $b$ determines $c'=19-b-2j$. It is nonnegative exactly when $0\le j\le\lfloor(19-b)/2\rfloor$.

| $b$ | Admissible $j$ values | Number |
|---|---|---|
| 0 | 0 through 9 | 10 |
| 1 | 0 through 9 | 10 |
| 2 | 0 through 8 | 9 |
| 3 | 0 through 8 | 9 |
| 4 | 0 through 7 | 8 |

Each table entry determines exactly one triple. The rows are disjoint, so $A=10+10+9+9+8=46$. Hence $A/16=23/8$, option 2. Replacing the evenness condition by a factor of one half loses the alternating endpoint effect. Counting $c\ge0$ instead of $c\ge1$ changes the residual total and the row lengths. The floor and its inclusive endpoint are part of the derivation, not a numerical afterthought.

## Q10

**Correct option: 2.** Charge only increments of `Cod`, not loop guards. A body visit has a unique triple $1\le i\le j\le k\le15$. Equal indices are explicitly allowed. Transform it to $(a,b,c)=(i,j+1,k+2)$. Then $1\le a<b<c\le17$. Conversely, any three-element subset of these seventeen positions gives $(i,j,k)=(a,b-1,c-2)$ in the original region. This is a bijection, so the body count is

$$B=\binom{17}{3}=\frac{17\cdot16\cdot15}{6}=680.$$

A second derivation fixes $j$. There are $j$ possible first indices and $16-j$ last indices; hence

$$B=\sum_{j=1}^{15}j(16-j)=16\cdot120-1240=680.$$

The initial ten is part of the requested final variable value: $\operatorname{Cod}_{\text{final}}=10+680=690$. Options 610, 630 and 710 would require 600, 620 and 700 increments respectively; none equals the counted region. A count of strictly increasing triples, $\binom{15}{3}=455$, omits every equality case. A rectangular count of $15^3$ includes tuples that violate the dependent bounds.

The general weak-order count is $\binom{n+2}{3}$, a cubic quantity despite the same three nesting levels as a strict-triple loop. The exact coefficients and endpoints differ. This calculation assumes that the supplied integer types avoid overflow, as the question states. It does not claim that the whole program executes only 680 primitive instructions: each nested invocation also performs header operations. Initialization changes the final accumulator while leaving the body frequency unchanged.

## Q11

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

## Q12

**Correct option: 1.** Let $K$ count the occurring events. “At most one” is the disjoint union of $K=0$ and $K=1$. Write $p=1/n$ and $q=1-p$, with $n\ge2$. Mutual independence includes the needed complements, so the all-failure event has probability $q^n$.

For a specified unique index $i$, the event $B_i\cap\bigcap_{j\ne i}B_j^c$ has probability $pq^{n-1}$. These $n$ events are disjoint: two different indices cannot both be the unique success. Consequently

$$P(K\le1)=q^n+npq^{n-1}=q^{n-1}(q+1)=\frac{(n-1)^{n-1}(2n-1)}{n^n}.$$

At $n=2$, the only excluded outcome is two successes, so the result must be $1-1/4=3/4$, agreeing with option one. Option two evaluates to $2/3$, option three to four, and option four to $1/9$; the value four is immediately impossible for a probability. At general $n$, replacing the failure probability by $(n-1)/(n+1)$ changes the specified model. As $n$ grows, the result approaches $2/e$, since $q^{n-1}\to e^{-1}$ and $q+1\to2$. For the omitted endpoint $n=1$, the sole event occurs certainly and the answer is one; compute this case directly rather than interpret $0^0$ implicitly. Pairwise independence alone does not supply all the products used above.

## Q13

**Correct option: 1.** Model all 45 tosses as independent fair binary outcomes. The detailed space has $2^{45}$ equally likely elements. If both players obtain $k$ heads, the first player has $\binom{25}{k}$ possible sequences and the second has $\binom{20}{k}$, with $0\le k\le20$. The values of $k$ identify disjoint cases, giving

$$P(\text{equal heads})=2^{-45}\sum_{k=0}^{20}\binom{25}{k}\binom{20}{k}.$$

To evaluate the sum, use $\binom{20}{k}=\binom{20}{20-k}$. Choosing a total of 20 objects from two disjoint groups of sizes 25 and 20, partition according to how many are chosen from the first group. The partition proves, rather than merely names, the identity

$$\sum_{k=0}^{20}\binom{25}{k}\binom{20}{20-k}=\binom{45}{20}.$$

A probabilistic second proof complements the second player's indicators: equal heads means first-player heads plus second-player tails equals 20. Those 45 transformed indicators remain independent and fair, so exactly $\binom{45}{20}$ detailed outcomes qualify. The index 15 in options two and four counts the wrong target. The denominator $2^{20}$ in options three and four ignores the first player's 25 independent outcomes; it does not describe their joint experiment. The identity applies to unequal toss counts $a,b$ as $\binom{a+b}{b}/2^{a+b}$ under independent fair tosses. With unequal coin biases, the weights of the summands change and the fair-count shortcut no longer applies.

## Q14

**Correct option: 1.**

### Translate the arithmetic condition into a category condition
Two integers have odd sum exactly when one is odd and the other is even. Thus a four-subset contains such a pair if and only if it contains both parities. There are five odds and five evens in $\{1,\ldots,10\}$.

All four-subsets number $\binom{10}4=210$. The excluded sets are the all-odd and all-even subsets, each counted by $\binom54=5$. They are disjoint, so

$$N=\binom{10}4-2\binom54=210-10=200.$$

This is option 1. A direct partition gives $\binom51\binom53+\binom52\binom52+\binom53\binom51=50+100+50=200$. Choosing an odd-even witness pair and then two remaining elements would overcount: a subset with $r$ odds and $4-r$ evens has $r(4-r)$ witness pairs, which is 3 or 4. There is no constant divisor that corrects both cases. The complement avoids this variable multiplicity.

## Q15

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

## Q16

**Correct option: 3.**

The total is 8 when $n=5$. The positivity shift leaves 5 units, giving $\binom72=21$, option 3. Directly, $u=0,1,2,3,4,5$ leaves respectively $6,5,4,3,2,1$ possibilities for $(v,w)$, totaling 21. The distractor 28 equals $\binom82$ and shifts the total incorrectly; 15 equals $\binom62$ and removes one extra unit. The value 64 is $8^2$ and ignores both positivity and the total coupling. A useful boundary is total three: only $(1,1,1)$ survives, so the general formula must give one at residual zero.

### Construction and proof


For positive integer coordinates with $x+y+z=n+3$, subtract one from each: $u=x-1$, $v=y-1$, $w=z-1$. This reversible shift gives $u+v+w=n$ and $u,v,w\ge0$. A row of $n$ stars and two bars encodes the three counts. The first count is the number of stars before the first bar, the second between the bars, and the third after the second. Adjacent bars and endpoint bars are allowed. Every vector yields exactly one row and vice versa, proving $N=\binom{n+2}2$.

An independent sum fixes $u=0,\ldots,n$. The other pair has $n-u+1$ choices, so $N=1+2+\cdots+(n+1)=(n+1)(n+2)/2$. This agrees with the binomial coefficient. For total $T$ and arbitrary lower bounds $L_1,L_2,L_3$, first form $R=T-L_1-L_2-L_3$. There are no solutions when $R<0$; otherwise the answer is $\binom{R+2}2$. The shift changes the total as well as the coordinates. These are ordered coordinate triples of indistinguishable units; permuting coordinates generally changes the outcome, while permuting units does not.

## Q17

**Correct option: 2.**

At $n=8$, the required total is 11 and the residual after the three lower bounds is 8. Thus $N=\binom{10}2=45$, option 2. The independent row sum is $9+8+7+6+5+4+3+2+1=45$. The proposed 121 is $11^2$, treating two coordinates as free without constraining the third. The values 55 and 36 are neighboring triangular numbers with residual totals 9 and 7. Neither equals the actual residual eight. A positive shift must be performed on all three coordinates, not on two alone.

### Construction and proof


For positive integer coordinates with $x+y+z=n+3$, subtract one from each: $u=x-1$, $v=y-1$, $w=z-1$. This reversible shift gives $u+v+w=n$ and $u,v,w\ge0$. A row of $n$ stars and two bars encodes the three counts. The first count is the number of stars before the first bar, the second between the bars, and the third after the second. Adjacent bars and endpoint bars are allowed. Every vector yields exactly one row and vice versa, proving $N=\binom{n+2}2$.

An independent sum fixes $u=0,\ldots,n$. The other pair has $n-u+1$ choices, so $N=1+2+\cdots+(n+1)=(n+1)(n+2)/2$. This agrees with the binomial coefficient. For total $T$ and arbitrary lower bounds $L_1,L_2,L_3$, first form $R=T-L_1-L_2-L_3$. There are no solutions when $R<0$; otherwise the answer is $\binom{R+2}2$. The shift changes the total as well as the coordinates. These are ordered coordinate triples of indistinguishable units; permuting coordinates generally changes the outcome, while permuting units does not.

## Q18

**Correct option: 1.**

The requested identity is $\binom{n+2}2$, option 1. It holds for every integer $n\ge0$, extending the stated positive domain to include the residual-zero boundary. Expressions $\binom{n+3}2$ and $\binom{n+1}2$ use a wrong residual; $(n+3)^2$ ignores the coupling constraint. To test symbolic claims, use $n=0$: the correct count is one, whereas these three proposals give 3, 0, and 9. Numerical agreement at a single later value would not replace the bijection.

### Construction and proof


For positive integer coordinates with $x+y+z=n+3$, subtract one from each: $u=x-1$, $v=y-1$, $w=z-1$. This reversible shift gives $u+v+w=n$ and $u,v,w\ge0$. A row of $n$ stars and two bars encodes the three counts. The first count is the number of stars before the first bar, the second between the bars, and the third after the second. Adjacent bars and endpoint bars are allowed. Every vector yields exactly one row and vice versa, proving $N=\binom{n+2}2$.

An independent sum fixes $u=0,\ldots,n$. The other pair has $n-u+1$ choices, so $N=1+2+\cdots+(n+1)=(n+1)(n+2)/2$. This agrees with the binomial coefficient. For total $T$ and arbitrary lower bounds $L_1,L_2,L_3$, first form $R=T-L_1-L_2-L_3$. There are no solutions when $R<0$; otherwise the answer is $\binom{R+2}2$. The shift changes the total as well as the coordinates. These are ordered coordinate triples of indistinguishable units; permuting coordinates generally changes the outcome, while permuting units does not.

## Q19

**Correct option: 4.**

Option 4 correctly requires subtracting the sum of the lower bounds before stars and bars. For example $x\ge2$, $y\ge1$, $z\ge3$, and total 10 give residual $10-6=4$ and count $\binom62=15$. Keeping total ten would count forbidden small coordinates. Treating coordinates as unnamed would merge $(2,1,7)$ with other permutations even though their lower bounds have different roles. A negative residual has zero solutions; applying a factorial expression to a negative residual is not a valid substitute for checking feasibility.

### Construction and proof


For positive integer coordinates with $x+y+z=n+3$, subtract one from each: $u=x-1$, $v=y-1$, $w=z-1$. This reversible shift gives $u+v+w=n$ and $u,v,w\ge0$. A row of $n$ stars and two bars encodes the three counts. The first count is the number of stars before the first bar, the second between the bars, and the third after the second. Adjacent bars and endpoint bars are allowed. Every vector yields exactly one row and vice versa, proving $N=\binom{n+2}2$.

An independent sum fixes $u=0,\ldots,n$. The other pair has $n-u+1$ choices, so $N=1+2+\cdots+(n+1)=(n+1)(n+2)/2$. This agrees with the binomial coefficient. For total $T$ and arbitrary lower bounds $L_1,L_2,L_3$, first form $R=T-L_1-L_2-L_3$. There are no solutions when $R<0$; otherwise the answer is $\binom{R+2}2$. The shift changes the total as well as the coordinates. These are ordered coordinate triples of indistinguishable units; permuting coordinates generally changes the outcome, while permuting units does not.

## Q20

**Correct option: 3.**

At total five the row sizes for $x=0,1,2$ are $6,5,4$. Their sum is 15, option 3. The unrestricted 21 includes $x=3,4,5$, whose row sizes $3,2,1$ contribute six excluded triples. The value 18 incorrectly gives all three rows size six; 14 omits one valid endpoint. The restriction does not permit a factor of three times one common row size: later rows have smaller totals.

### Construction and proof


Fix the bounded coordinate $x$. For each allowed integer $x\in\{0,1,2\}$ with $x\le n$, the remaining equation $y+z=n-x$ has $n-x+1$ nonnegative solutions: choose $y$ from zero through $n-x$, then $z$ is forced. Cases with different $x$ cannot overlap. Therefore

$$N=\sum_{x=0}^{\min(2,n)}(n-x+1).$$

For $n\ge2$, this is $(n+1)+n+(n-1)=3n$. Inclusion–exclusion independently starts with $\binom{n+2}2$ unrestricted triples and subtracts those with $x\ge3$. Set $x'=x-3$; the forbidden count is $\binom{n-1}2$ when $n\ge3$, and zero otherwise. Their difference is $3n$ for $n\ge2$. At $n=1$, the two surviving rows have sizes 2 and 1, giving 3; at $n=0$, only $(0,0,0)$ survives, giving one. Thus the compact expression $3n$ happens to hold at $n=1$ but fails at zero. A bound of $u$ is first violated at $u+1$, not at $u$.

## Q21

**Correct option: 2.**

At total eight, the rows contain $9,8,7$ triples and total 24, option 2. Equivalently $\binom{10}2-\binom72=45-21=24$. The distractor 45 ignores the cap; 27 assigns nine pairs to every $x$; 23 loses a permitted endpoint. For example the $x=2$ row includes $(2,0,6)$ through $(2,6,0)$, seven pairs rather than six.

### Construction and proof


Fix the bounded coordinate $x$. For each allowed integer $x\in\{0,1,2\}$ with $x\le n$, the remaining equation $y+z=n-x$ has $n-x+1$ nonnegative solutions: choose $y$ from zero through $n-x$, then $z$ is forced. Cases with different $x$ cannot overlap. Therefore

$$N=\sum_{x=0}^{\min(2,n)}(n-x+1).$$

For $n\ge2$, this is $(n+1)+n+(n-1)=3n$. Inclusion–exclusion independently starts with $\binom{n+2}2$ unrestricted triples and subtracts those with $x\ge3$. Set $x'=x-3$; the forbidden count is $\binom{n-1}2$ when $n\ge3$, and zero otherwise. Their difference is $3n$ for $n\ge2$. At $n=1$, the two surviving rows have sizes 2 and 1, giving 3; at $n=0$, only $(0,0,0)$ survives, giving one. Thus the compact expression $3n$ happens to hold at $n=1$ but fails at zero. A bound of $u$ is first violated at $u+1$, not at $u$.

## Q22

**Correct option: 1.**

The general expression in the positive-integer domain is $3n$, option 1. The full boundary formula is $N(0)=1$ and $N(n)=3n$ for $n\ge1$. The alternatives $3(n+1)$, $3n-1$, and $\binom{n+2}2$ respectively equalize the row lengths, remove an endpoint without a constraint, and ignore the cap. The direct sum proves the identity, while the boundary calculation explains why extrapolating it to zero is incorrect.

### Construction and proof


Fix the bounded coordinate $x$. For each allowed integer $x\in\{0,1,2\}$ with $x\le n$, the remaining equation $y+z=n-x$ has $n-x+1$ nonnegative solutions: choose $y$ from zero through $n-x$, then $z$ is forced. Cases with different $x$ cannot overlap. Therefore

$$N=\sum_{x=0}^{\min(2,n)}(n-x+1).$$

For $n\ge2$, this is $(n+1)+n+(n-1)=3n$. Inclusion–exclusion independently starts with $\binom{n+2}2$ unrestricted triples and subtracts those with $x\ge3$. Set $x'=x-3$; the forbidden count is $\binom{n-1}2$ when $n\ge3$, and zero otherwise. Their difference is $3n$ for $n\ge2$. At $n=1$, the two surviving rows have sizes 2 and 1, giving 3; at $n=0$, only $(0,0,0)$ survives, giving one. Thus the compact expression $3n$ happens to hold at $n=1$ but fails at zero. A bound of $u$ is first violated at $u+1$, not at $u$.

## Q23

**Correct option: 4.**

Option 4 correctly warns that totals below the cap need separate feasible-row accounting. For $n=1$, the $x=2$ row is empty, so the actual two-row sum is $2+1=3$; writing a third row of size zero happens to preserve $3n$. For $n=0$, the formal third row would be negative and the expression $3n$ gives zero instead of one. A negative row is never a negative number of solutions. The cap is on one coordinate and cannot be replaced by limiting every coordinate to two or by a probability factor.

### Construction and proof


Fix the bounded coordinate $x$. For each allowed integer $x\in\{0,1,2\}$ with $x\le n$, the remaining equation $y+z=n-x$ has $n-x+1$ nonnegative solutions: choose $y$ from zero through $n-x$, then $z$ is forced. Cases with different $x$ cannot overlap. Therefore

$$N=\sum_{x=0}^{\min(2,n)}(n-x+1).$$

For $n\ge2$, this is $(n+1)+n+(n-1)=3n$. Inclusion–exclusion independently starts with $\binom{n+2}2$ unrestricted triples and subtracts those with $x\ge3$. Set $x'=x-3$; the forbidden count is $\binom{n-1}2$ when $n\ge3$, and zero otherwise. Their difference is $3n$ for $n\ge2$. At $n=1$, the two surviving rows have sizes 2 and 1, giving 3; at $n=0$, only $(0,0,0)$ survives, giving one. Thus the compact expression $3n$ happens to hold at $n=1$ but fails at zero. A bound of $u$ is first violated at $u+1$, not at $u$.

## Q24

**Correct option: 2.**

For $n=5$, the total is 10. The even-coordinate rows $x=0,2,4,6,8,10$ have $11,9,7,5,3,1$ solutions, totaling 36, option 2. The distractor 66 counts all triples, 21 is the stars-and-bars count for total five instead of ten, and 25 drops the final row and shifts the square. The explicit endpoints distinguish $n^2$ from $(n+1)^2$.

### Construction and proof


Evenness is a structural substitution: set $x=2a$, $a\ge0$. The equation becomes $2a+y+z=2n$. For $a=0,\ldots,n$, choose $y$ from 0 through $2n-2a$; then $z=2n-2a-y$. Thus

$$N=\sum_{a=0}^{n}(2n-2a+1)=\sum_{j=0}^{n}(2j+1)=(n+1)^2.$$

The last equality follows by $2\sum_{j=0}^{n}j+(n+1)=n(n+1)+(n+1)$. For comparison, odd $x=2a+1$ permits $a=0,\ldots,n-1$ and has row counts $2n,2n-2,\ldots,2$, totaling $n(n+1)$. Their sum is $(n+1)(2n+1)=\binom{2n+2}2$, the unrestricted count; their difference is $n+1$. Consequently parity does not split this sample space into two equal classes. At $n=0$, the only solution is the all-zero triple and it belongs to the even class. For a general total $T$, use $\sum_{a=0}^{\lfloor T/2\rfloor}(T-2a+1)$, retaining the floor rather than pretending all totals are even.

## Q25

**Correct option: 1.**

For $n=8$, the row sizes are $17,15,13,11,9,7,5,3,1$. Their sum is 81, option 1. The proposed 153 equals $\binom{18}2$ and ignores parity; 45 uses total eight rather than sixteen; 64 equals $n^2$ and counts an incorrectly truncated odd-number sum. The odd-coordinate count is $8\cdot9=72$, so $81+72=153$ independently checks the total.

### Construction and proof


Evenness is a structural substitution: set $x=2a$, $a\ge0$. The equation becomes $2a+y+z=2n$. For $a=0,\ldots,n$, choose $y$ from 0 through $2n-2a$; then $z=2n-2a-y$. Thus

$$N=\sum_{a=0}^{n}(2n-2a+1)=\sum_{j=0}^{n}(2j+1)=(n+1)^2.$$

The last equality follows by $2\sum_{j=0}^{n}j+(n+1)=n(n+1)+(n+1)$. For comparison, odd $x=2a+1$ permits $a=0,\ldots,n-1$ and has row counts $2n,2n-2,\ldots,2$, totaling $n(n+1)$. Their sum is $(n+1)(2n+1)=\binom{2n+2}2$, the unrestricted count; their difference is $n+1$. Consequently parity does not split this sample space into two equal classes. At $n=0$, the only solution is the all-zero triple and it belongs to the even class. For a general total $T$, use $\sum_{a=0}^{\lfloor T/2\rfloor}(T-2a+1)$, retaining the floor rather than pretending all totals are even.

## Q26

**Correct option: 4.**

The valid general expression is $(n+1)^2$, option 4. The unrestricted binomial coefficient counts both parities; $\binom{n+2}2$ weights the substituted variable $a$ as one unit rather than two; $n^2$ loses a boundary row. A substitution modifies the coefficient in the equation. It does not turn $2a+y+z=2n$ into an ordinary equal-weight stars-and-bars equation.

### Construction and proof


Evenness is a structural substitution: set $x=2a$, $a\ge0$. The equation becomes $2a+y+z=2n$. For $a=0,\ldots,n$, choose $y$ from 0 through $2n-2a$; then $z=2n-2a-y$. Thus

$$N=\sum_{a=0}^{n}(2n-2a+1)=\sum_{j=0}^{n}(2j+1)=(n+1)^2.$$

The last equality follows by $2\sum_{j=0}^{n}j+(n+1)=n(n+1)+(n+1)$. For comparison, odd $x=2a+1$ permits $a=0,\ldots,n-1$ and has row counts $2n,2n-2,\ldots,2$, totaling $n(n+1)$. Their sum is $(n+1)(2n+1)=\binom{2n+2}2$, the unrestricted count; their difference is $n+1$. Consequently parity does not split this sample space into two equal classes. At $n=0$, the only solution is the all-zero triple and it belongs to the even class. For a general total $T$, use $\sum_{a=0}^{\lfloor T/2\rfloor}(T-2a+1)$, retaining the floor rather than pretending all totals are even.

## Q27

**Correct option: 3.**

Option 3 correctly rejects a blind half-count for parity. At $n=1$, even $x$ gives $(0,0,2),(0,1,1),(0,2,0),(2,0,0)$, four solutions, while odd $x$ gives $(1,0,1),(1,1,0)$, two. Pairing $x$ with $x+1$ would remove one unit from the remaining total, changing how many $(y,z)$ pairs exist. A claimed parity symmetry must be a bijection preserving all constraints; this attempted toggle is not one.

### Construction and proof


Evenness is a structural substitution: set $x=2a$, $a\ge0$. The equation becomes $2a+y+z=2n$. For $a=0,\ldots,n$, choose $y$ from 0 through $2n-2a$; then $z=2n-2a-y$. Thus

$$N=\sum_{a=0}^{n}(2n-2a+1)=\sum_{j=0}^{n}(2j+1)=(n+1)^2.$$

The last equality follows by $2\sum_{j=0}^{n}j+(n+1)=n(n+1)+(n+1)$. For comparison, odd $x=2a+1$ permits $a=0,\ldots,n-1$ and has row counts $2n,2n-2,\ldots,2$, totaling $n(n+1)$. Their sum is $(n+1)(2n+1)=\binom{2n+2}2$, the unrestricted count; their difference is $n+1$. Consequently parity does not split this sample space into two equal classes. At $n=0$, the only solution is the all-zero triple and it belongs to the even class. For a general total $T$, use $\sum_{a=0}^{\lfloor T/2\rfloor}(T-2a+1)$, retaining the floor rather than pretending all totals are even.

## Q28

**Correct option: 3.**

With five objects of each color, the three admissible counts are $\binom53\binom52=100$, $\binom54\binom51=25$, and $\binom55=1$. Their sum is 126, option 3. The alternatives 100, 1, and 252 respectively keep only the exactly-three-red case, only the all-red case, or all five-subsets. The independent swap check is $\binom{10}5/2=252/2=126$.

### Construction and proof


Let $r$ be the exact number of red objects in the five-subset. Distinct objects and unordered selection give $\binom nr\binom n{5-r}$ choices. At least three reds requires $r=3,4,5$, so

$$N=\binom n3\binom n2+\binom n4\binom n1+\binom n5.$$

Use the convention that a binomial coefficient is zero when the requested nonnegative subset size exceeds the population. This makes unavailable categories contribute zero. A useful second proof swaps the names of the equal-sized color populations using a fixed bijection of their labels. Every size-five subset with at least three reds is mapped bijectively to one with at least three blues, and no subset can satisfy both conditions because five is odd. These two classes partition all subsets. Hence $N=\binom{2n}5/2$, including the zero count when $2n<5$.

Choosing three red witnesses and then adding two arbitrary remaining objects is not this count. A subset with four reds has four witnessing triples and a subset with five reds has ten. That construction counts witnesses, not subsets, and its fiber sizes vary. Exact category partition or the color-swap bijection repairs the overcount.

## Q29

**Correct option: 2.**

For eight of each color, the category contributions are $56\cdot28=1568$, $70\cdot8=560$, and $56$. Their sum is 2184, option 2. The alternative 1568 counts exactly three reds, 56 counts all-red subsets, and 4368 counts all $\binom{16}5$ subsets. The lower bound includes all three cases; it is not synonymous with equality.

### Construction and proof


Let $r$ be the exact number of red objects in the five-subset. Distinct objects and unordered selection give $\binom nr\binom n{5-r}$ choices. At least three reds requires $r=3,4,5$, so

$$N=\binom n3\binom n2+\binom n4\binom n1+\binom n5.$$

Use the convention that a binomial coefficient is zero when the requested nonnegative subset size exceeds the population. This makes unavailable categories contribute zero. A useful second proof swaps the names of the equal-sized color populations using a fixed bijection of their labels. Every size-five subset with at least three reds is mapped bijectively to one with at least three blues, and no subset can satisfy both conditions because five is odd. These two classes partition all subsets. Hence $N=\binom{2n}5/2$, including the zero count when $2n<5$.

Choosing three red witnesses and then adding two arbitrary remaining objects is not this count. A subset with four reds has four witnessing triples and a subset with five reds has ten. That construction counts witnesses, not subsets, and its fiber sizes vary. Exact category partition or the color-swap bijection repairs the overcount.

## Q30

**Correct option: 1.**

Option 1 is the three-term formula. The competing single term $\binom n3\binom n2$ discards four- and five-red subsets; $\binom n5$ discards mixed subsets; $\binom{2n}5$ omits the red-majority restriction. At $n=3$, the answer is nine, not a nonexistent five-red selection. The binomial-zero convention is important for this small but feasible population.

### Construction and proof


Let $r$ be the exact number of red objects in the five-subset. Distinct objects and unordered selection give $\binom nr\binom n{5-r}$ choices. At least three reds requires $r=3,4,5$, so

$$N=\binom n3\binom n2+\binom n4\binom n1+\binom n5.$$

Use the convention that a binomial coefficient is zero when the requested nonnegative subset size exceeds the population. This makes unavailable categories contribute zero. A useful second proof swaps the names of the equal-sized color populations using a fixed bijection of their labels. Every size-five subset with at least three reds is mapped bijectively to one with at least three blues, and no subset can satisfy both conditions because five is odd. These two classes partition all subsets. Hence $N=\binom{2n}5/2$, including the zero count when $2n<5$.

Choosing three red witnesses and then adding two arbitrary remaining objects is not this count. A subset with four reds has four witnessing triples and a subset with five reds has ten. That construction counts witnesses, not subsets, and its fiber sizes vary. Exact category partition or the color-swap bijection repairs the overcount.

## Q31

**Correct option: 4.**

Option 4 correctly separates “at least” from “exactly.” A concrete five-red subset satisfies the question even though it contains ten triples of red witnesses. A four-red-one-blue subset contains four such witnesses. Dividing a witness count by one common number cannot repair both. Color swapping works here only because the two populations have equal size and the selection size is odd; with an even selection size, equal-color ties form an additional class.

### Construction and proof


Let $r$ be the exact number of red objects in the five-subset. Distinct objects and unordered selection give $\binom nr\binom n{5-r}$ choices. At least three reds requires $r=3,4,5$, so

$$N=\binom n3\binom n2+\binom n4\binom n1+\binom n5.$$

Use the convention that a binomial coefficient is zero when the requested nonnegative subset size exceeds the population. This makes unavailable categories contribute zero. A useful second proof swaps the names of the equal-sized color populations using a fixed bijection of their labels. Every size-five subset with at least three reds is mapped bijectively to one with at least three blues, and no subset can satisfy both conditions because five is odd. These two classes partition all subsets. Hence $N=\binom{2n}5/2$, including the zero count when $2n<5$.

Choosing three red witnesses and then adding two arbitrary remaining objects is not this count. A subset with four reds has four witnessing triples and a subset with five reds has ten. That construction counts witnesses, not subsets, and its fiber sizes vary. Exact category partition or the color-swap bijection repairs the overcount.

## Q32

**Correct option: 3.**

For $n=5$, $N=243-96+3=150$, option 3. By occupancy sizes, $(3,1,1)$ contributes $3\cdot5!/3!=60$ and $(2,2,1)$ contributes $3\cdot5!/(2!2!)=90$. Their sum is 150. The alternative 243 includes empty bins; 147 omits the pair-intersection restoration; 60 counts only the $(3,1,1)$ profile and misses $(2,2,1)$.

### Construction and proof


A map sends each of $n$ distinct objects to one of three named bins, so the unrestricted count is $3^n$. Let $B_j$ be the set of maps leaving bin $j$ empty. Each has size $2^n$; any pair intersection has size $1^n$; all three empty bins have size $0^n$. For $n\ge1$, inclusion–exclusion gives

$$N=3^n-3\cdot2^n+3.$$

Maps leaving two bins empty were subtracted twice in the first correction and must be restored once. A map using a single bin belongs to two emptiness events, explaining this correction concretely. If $n<3$, surjectivity is impossible; the expression returns zero for $n=1,2$. At $n=0$, the full inclusion–exclusion calculation includes the single empty map in every intersection, and gives $1-3+3-1=0$. The simplified formula without the last term is not valid there.

If the three bins are genuinely unnamed and all are nonempty, every final partition has exactly $3!$ labelings and the count divides by six. If emptiness is allowed, label permutations can fix outcomes with several empty bins, so a blind division of $3^n$ by six is not valid. Distinct objects require assignments or multinomial weights; a positive size vector alone does not identify which objects occupy each bin.

## Q33

**Correct option: 2.**

At $n=8$, the exact calculation is $6561-768+3=5796$, option 2. The alternatives 6561 and 5793 respectively omit all restrictions and omit restoration of overlapping exclusions. The value 336 is $3!\binom83$, the count of choosing three distinct witnesses and naming their bins without specifying the other five assignments; it is not a complete outcome count. Under independent uniform placement, the onto probability is $5796/6561$, with the unrestricted count as denominator.

### Construction and proof


A map sends each of $n$ distinct objects to one of three named bins, so the unrestricted count is $3^n$. Let $B_j$ be the set of maps leaving bin $j$ empty. Each has size $2^n$; any pair intersection has size $1^n$; all three empty bins have size $0^n$. For $n\ge1$, inclusion–exclusion gives

$$N=3^n-3\cdot2^n+3.$$

Maps leaving two bins empty were subtracted twice in the first correction and must be restored once. A map using a single bin belongs to two emptiness events, explaining this correction concretely. If $n<3$, surjectivity is impossible; the expression returns zero for $n=1,2$. At $n=0$, the full inclusion–exclusion calculation includes the single empty map in every intersection, and gives $1-3+3-1=0$. The simplified formula without the last term is not valid there.

If the three bins are genuinely unnamed and all are nonempty, every final partition has exactly $3!$ labelings and the count divides by six. If emptiness is allowed, label permutations can fix outcomes with several empty bins, so a blind division of $3^n$ by six is not valid. Distinct objects require assignments or multinomial weights; a positive size vector alone does not identify which objects occupy each bin.

## Q34

**Correct option: 1.**

Option 1 gives $3^n-3\cdot2^n+3$. The proposal without the final positive three omits pair corrections; $3^n$ ignores emptiness; a witness expression $3!\binom n3$ leaves nonwitness assignments unspecified and can represent a final map multiple times. The inclusion–exclusion intersections are counted from the actual missing-bin sets, not guessed from the number of constraints.

### Construction and proof


A map sends each of $n$ distinct objects to one of three named bins, so the unrestricted count is $3^n$. Let $B_j$ be the set of maps leaving bin $j$ empty. Each has size $2^n$; any pair intersection has size $1^n$; all three empty bins have size $0^n$. For $n\ge1$, inclusion–exclusion gives

$$N=3^n-3\cdot2^n+3.$$

Maps leaving two bins empty were subtracted twice in the first correction and must be restored once. A map using a single bin belongs to two emptiness events, explaining this correction concretely. If $n<3$, surjectivity is impossible; the expression returns zero for $n=1,2$. At $n=0$, the full inclusion–exclusion calculation includes the single empty map in every intersection, and gives $1-3+3-1=0$. The simplified formula without the last term is not valid there.

If the three bins are genuinely unnamed and all are nonempty, every final partition has exactly $3!$ labelings and the count divides by six. If emptiness is allowed, label permutations can fix outcomes with several empty bins, so a blind division of $3^n$ by six is not valid. Distinct objects require assignments or multinomial weights; a positive size vector alone does not identify which objects occupy each bin.

## Q35

**Correct option: 4.**

Option 4 correctly divides by $3!$ for unnamed nonempty groups. For five distinct objects the named count is 150 and the unnamed count is 25. Permuting labels changes every named map because all three fibers are nonempty and disjoint, so the action has no nonidentity stabilizer. Allowing empty groups destroys this argument: the all-in-one-bin outcome has only three named descriptions, not six. Erasing labels is a constant-fiber quotient only after the nonemptiness condition is enforced.

### Construction and proof


A map sends each of $n$ distinct objects to one of three named bins, so the unrestricted count is $3^n$. Let $B_j$ be the set of maps leaving bin $j$ empty. Each has size $2^n$; any pair intersection has size $1^n$; all three empty bins have size $0^n$. For $n\ge1$, inclusion–exclusion gives

$$N=3^n-3\cdot2^n+3.$$

Maps leaving two bins empty were subtracted twice in the first correction and must be restored once. A map using a single bin belongs to two emptiness events, explaining this correction concretely. If $n<3$, surjectivity is impossible; the expression returns zero for $n=1,2$. At $n=0$, the full inclusion–exclusion calculation includes the single empty map in every intersection, and gives $1-3+3-1=0$. The simplified formula without the last term is not valid there.

If the three bins are genuinely unnamed and all are nonempty, every final partition has exactly $3!$ labelings and the count divides by six. If emptiness is allowed, label permutations can fix outcomes with several empty bins, so a blind division of $3^n$ by six is not valid. Distinct objects require assignments or multinomial weights; a positive size vector alone does not identify which objects occupy each bin.

## Q36

**Correct option: 2.**

At length five, the even-zero cases $k=0,2,4$ have $243$, $\binom52\cdot27=270$, and $\binom54\cdot3=15$ words. Total $528$, option 2. The alternative 512 halves $4^5$ incorrectly; 496 is the odd count; 243 counts no zeros only. The parity difference $528-496=32=2^5$ checks the signed sum.

### Construction and proof


Distinguish one symbol, say 0, from the other three. A word with exactly $k$ zeros has $\binom nk3^{n-k}$ constructions: choose zero positions and then fill every remaining position. Let $E_n$ and $O_n$ denote even- and odd-zero counts. The binomial theorem gives

$$E_n+O_n=(3+1)^n=4^n,\qquad E_n-O_n=(3-1)^n=2^n.$$

Adding and subtracting proves $E_n=(4^n+2^n)/2$ and $O_n=(4^n-2^n)/2$. This parity filter is an exact algebraic separation of two disjoint sums. It does not assume their sizes are equal. At $n=0$, $E_0=1$ and $O_0=0$, corresponding to the empty word. For a $q$-symbol alphabet with one distinguished symbol, replace 3 by $q-1$ to get $E_n=(q^n+(q-2)^n)/2$ for $n\ge1$; handle the empty word directly, particularly for a two-symbol alphabet. Uniform word probability is $E_n/4^n$ only if independent uniform symbol draws are actually specified.

## Q37

**Correct option: 1.**

At length eight, the five even contributions for $k=0,2,4,6,8$ are $6561,20412,5670,252,1$. Their sum is 32896, option 1. Equivalently $(65536+256)/2=32896$. The proposed 32768 blindly halves the total; 32640 counts odd parity; 6561 permits zero zeros only. Including the all-zero word contributes the final one, not an undefined power.

### Construction and proof


Distinguish one symbol, say 0, from the other three. A word with exactly $k$ zeros has $\binom nk3^{n-k}$ constructions: choose zero positions and then fill every remaining position. Let $E_n$ and $O_n$ denote even- and odd-zero counts. The binomial theorem gives

$$E_n+O_n=(3+1)^n=4^n,\qquad E_n-O_n=(3-1)^n=2^n.$$

Adding and subtracting proves $E_n=(4^n+2^n)/2$ and $O_n=(4^n-2^n)/2$. This parity filter is an exact algebraic separation of two disjoint sums. It does not assume their sizes are equal. At $n=0$, $E_0=1$ and $O_0=0$, corresponding to the empty word. For a $q$-symbol alphabet with one distinguished symbol, replace 3 by $q-1$ to get $E_n=(q^n+(q-2)^n)/2$ for $n\ge1$; handle the empty word directly, particularly for a two-symbol alphabet. Uniform word probability is $E_n/4^n$ only if independent uniform symbol draws are actually specified.

## Q38

**Correct option: 4.**

The exact expression is $(4^n+2^n)/2$, option 4. The half-total proposal misses the signed correction; $(4^n-2^n)/2$ isolates the opposite parity; $3^n$ permits no distinguished symbols. The correction decays as a fraction of the total, but a small relative difference is still an exact counting difference and cannot be omitted in an examination answer.

### Construction and proof


Distinguish one symbol, say 0, from the other three. A word with exactly $k$ zeros has $\binom nk3^{n-k}$ constructions: choose zero positions and then fill every remaining position. Let $E_n$ and $O_n$ denote even- and odd-zero counts. The binomial theorem gives

$$E_n+O_n=(3+1)^n=4^n,\qquad E_n-O_n=(3-1)^n=2^n.$$

Adding and subtracting proves $E_n=(4^n+2^n)/2$ and $O_n=(4^n-2^n)/2$. This parity filter is an exact algebraic separation of two disjoint sums. It does not assume their sizes are equal. At $n=0$, $E_0=1$ and $O_0=0$, corresponding to the empty word. For a $q$-symbol alphabet with one distinguished symbol, replace 3 by $q-1$ to get $E_n=(q^n+(q-2)^n)/2$ for $n\ge1$; handle the empty word directly, particularly for a two-symbol alphabet. Uniform word probability is $E_n/4^n$ only if independent uniform symbol draws are actually specified.

## Q39

**Correct option: 3.**

Option 3 correctly attributes unequal parity classes to the three alternatives at a nondistinguished position. The signed sum changes only the distinguished symbol's contribution from $+1$ to $-1$, leaving the other weight equal to three. It is $2^n$, not $4^n$. At length one there are three even words and one odd word; this immediately disproves the half-total claim. A toggle between zero and a single nonzero symbol would not handle the other two nonzero symbols, so it is not a bijection between the entire parity classes.

### Construction and proof


Distinguish one symbol, say 0, from the other three. A word with exactly $k$ zeros has $\binom nk3^{n-k}$ constructions: choose zero positions and then fill every remaining position. Let $E_n$ and $O_n$ denote even- and odd-zero counts. The binomial theorem gives

$$E_n+O_n=(3+1)^n=4^n,\qquad E_n-O_n=(3-1)^n=2^n.$$

Adding and subtracting proves $E_n=(4^n+2^n)/2$ and $O_n=(4^n-2^n)/2$. This parity filter is an exact algebraic separation of two disjoint sums. It does not assume their sizes are equal. At $n=0$, $E_0=1$ and $O_0=0$, corresponding to the empty word. For a $q$-symbol alphabet with one distinguished symbol, replace 3 by $q-1$ to get $E_n=(q^n+(q-2)^n)/2$ for $n\ge1$; handle the empty word directly, particularly for a two-symbol alphabet. Uniform word probability is $E_n/4^n$ only if independent uniform symbol draws are actually specified.

## Q40

**Correct option: 3.**

The values from length zero through five are $1,2,3,5,8,13$, so option 3's 13 is correct. Partitioning by weight gives $\binom60+\binom51+\binom42+\binom33=1+5+6+1=13$. The alternative 32 counts all binary words, 6 includes only zero or one one, and 8 is the count for length four. Every additional permitted weight must be included.

### Construction and proof


Let $T_n$ count binary words of length $n$ with no adjacent ones. For $n\ge2$, partition by the prefix. A leading 0 leaves any admissible length-$(n-1)$ word. A leading 1 forces the second symbol to be 0, leaving any admissible length-$(n-2)$ word. The prefix classes are disjoint and their suffix deletion is reversible, proving $T_n=T_{n-1}+T_{n-2}$ with $T_0=1$ and $T_1=2$. Thus $T_n=F_{n+2}$ for $F_0=0,F_1=1$.

A second proof fixes the number $j$ of ones. If their positions are $1\le p_1<\cdots<p_j\le n$ with $p_{i+1}\ge p_i+2$, set $q_i=p_i-(i-1)$. Then $1\le q_1<\cdots<q_j\le n-j+1$, a bijection with $j$-subsets. The fixed-weight count is $\binom{n-j+1}j$ and $T_n=\sum_{j=0}^{\lfloor(n+1)/2\rfloor}\binom{n-j+1}j$. The $j=0$ case is one all-zero word. The recurrence counts all feasible weights; a fixed-weight binomial coefficient answers a different question.

## Q41

**Correct option: 2.**

For length eight, extend the recurrence: $T_5=13$, $T_6=21$, $T_7=34$, $T_8=55$, option 2. The fixed-weight check is $1+8+21+20+5=55$ for $j=0,1,2,3,4$. The alternatives 34, 256, and 9 respectively count length seven, all binary words, and only zero-or-one-one words. The four-one case has five placements because an extra zero can occupy any of five gaps.

### Construction and proof


Let $T_n$ count binary words of length $n$ with no adjacent ones. For $n\ge2$, partition by the prefix. A leading 0 leaves any admissible length-$(n-1)$ word. A leading 1 forces the second symbol to be 0, leaving any admissible length-$(n-2)$ word. The prefix classes are disjoint and their suffix deletion is reversible, proving $T_n=T_{n-1}+T_{n-2}$ with $T_0=1$ and $T_1=2$. Thus $T_n=F_{n+2}$ for $F_0=0,F_1=1$.

A second proof fixes the number $j$ of ones. If their positions are $1\le p_1<\cdots<p_j\le n$ with $p_{i+1}\ge p_i+2$, set $q_i=p_i-(i-1)$. Then $1\le q_1<\cdots<q_j\le n-j+1$, a bijection with $j$-subsets. The fixed-weight count is $\binom{n-j+1}j$ and $T_n=\sum_{j=0}^{\lfloor(n+1)/2\rfloor}\binom{n-j+1}j$. The $j=0$ case is one all-zero word. The recurrence counts all feasible weights; a fixed-weight binomial coefficient answers a different question.

## Q42

**Correct option: 1.**

Option 1 is $F_{n+2}$ under the declared seeds $F_0=0,F_1=1$. The adjacent Fibonacci value fails at length one: there are two words, 0 and 1. A proposal of $2^n$ ignores adjacency, and $n+1$ permits at most one one. Fibonacci notation without its indexing convention is insufficient; the recurrence and both base values determine the sequence uniquely.

### Construction and proof


Let $T_n$ count binary words of length $n$ with no adjacent ones. For $n\ge2$, partition by the prefix. A leading 0 leaves any admissible length-$(n-1)$ word. A leading 1 forces the second symbol to be 0, leaving any admissible length-$(n-2)$ word. The prefix classes are disjoint and their suffix deletion is reversible, proving $T_n=T_{n-1}+T_{n-2}$ with $T_0=1$ and $T_1=2$. Thus $T_n=F_{n+2}$ for $F_0=0,F_1=1$.

A second proof fixes the number $j$ of ones. If their positions are $1\le p_1<\cdots<p_j\le n$ with $p_{i+1}\ge p_i+2$, set $q_i=p_i-(i-1)$. Then $1\le q_1<\cdots<q_j\le n-j+1$, a bijection with $j$-subsets. The fixed-weight count is $\binom{n-j+1}j$ and $T_n=\sum_{j=0}^{\lfloor(n+1)/2\rfloor}\binom{n-j+1}j$. The $j=0$ case is one all-zero word. The recurrence counts all feasible weights; a fixed-weight binomial coefficient answers a different question.

## Q43

**Correct option: 4.**

Option 4 correctly keeps one empty word. Setting $T_0=0$ would give $T_2=T_1+T_0=2$, but the valid words 00, 01, and 10 are three. The empty suffix is a real construction when a forced 10 consumes the entire word. The prefix recurrence applies only from length two onward; at length one, the leading-1 branch has no required following position and must be counted directly.

### Construction and proof


Let $T_n$ count binary words of length $n$ with no adjacent ones. For $n\ge2$, partition by the prefix. A leading 0 leaves any admissible length-$(n-1)$ word. A leading 1 forces the second symbol to be 0, leaving any admissible length-$(n-2)$ word. The prefix classes are disjoint and their suffix deletion is reversible, proving $T_n=T_{n-1}+T_{n-2}$ with $T_0=1$ and $T_1=2$. Thus $T_n=F_{n+2}$ for $F_0=0,F_1=1$.

A second proof fixes the number $j$ of ones. If their positions are $1\le p_1<\cdots<p_j\le n$ with $p_{i+1}\ge p_i+2$, set $q_i=p_i-(i-1)$. Then $1\le q_1<\cdots<q_j\le n-j+1$, a bijection with $j$-subsets. The fixed-weight count is $\binom{n-j+1}j$ and $T_n=\sum_{j=0}^{\lfloor(n+1)/2\rfloor}\binom{n-j+1}j$. The $j=0$ case is one all-zero word. The recurrence counts all feasible weights; a fixed-weight binomial coefficient answers a different question.

## Q44

**Correct option: 4.**

For size five, $N=\binom83=56$, option 4. As a recursive check, fixing $c_4$ from zero to five leaves three-type counts $21,15,10,6,3,1$, totaling 56. The alternatives $4^5=1024$, $\binom54=5$, and $5^3=125$ count ordered words, an unrelated subset selection, or unrestricted choices of three coordinates without the fourth-coordinate nonnegativity condition.

### Construction and proof


A multiset on four named types is exactly its multiplicity vector $(c_1,c_2,c_3,c_4)$, where $c_i\ge0$ and $\sum c_i=n$. A row of $n$ identical stars and three separators encodes these four counts, including zero counts through adjacent bars or endpoint bars. Selecting three separator positions among $n+3$ gives $\binom{n+3}3$.

This is the number of summaries, not their probabilities under random sequential draws. A vector has $n!/(c_1!c_2!c_3!c_4!)$ ordered preimages. The all-one-type vector has one; a vector $(n-1,1,0,0)$ has $n$ when $n\ge2$. Consequently uniform ordered words induce nonuniform multiset probabilities. Under independent uniform draws its mass is the preimage count divided by $4^n$.

If every type must appear, subtract one from all four coordinates and count $\binom{n-1}3$ for $n\ge4$, zero otherwise. If repetition is forbidden, use $\binom4n$ for $0\le n\le4$. If order remains visible, use $4^n$. These three modifications are different mechanisms, not corrections to the same multiset formula.

## Q45

**Correct option: 3.**

For size eight, $N=\binom{11}3=165$, option 3. The summation check is $45+36+28+21+15+10+6+3+1=165$. The value 65536 equals $4^8$ and orders occurrences; 70 equals $\binom84$ and chooses four distinct positions from eight rather than four type multiplicities; 512 equals $8^3$ and does not enforce the total constraint. The fourth coordinate is forced only after the first three choices have a sum at most eight.

### Construction and proof


A multiset on four named types is exactly its multiplicity vector $(c_1,c_2,c_3,c_4)$, where $c_i\ge0$ and $\sum c_i=n$. A row of $n$ identical stars and three separators encodes these four counts, including zero counts through adjacent bars or endpoint bars. Selecting three separator positions among $n+3$ gives $\binom{n+3}3$.

This is the number of summaries, not their probabilities under random sequential draws. A vector has $n!/(c_1!c_2!c_3!c_4!)$ ordered preimages. The all-one-type vector has one; a vector $(n-1,1,0,0)$ has $n$ when $n\ge2$. Consequently uniform ordered words induce nonuniform multiset probabilities. Under independent uniform draws its mass is the preimage count divided by $4^n$.

If every type must appear, subtract one from all four coordinates and count $\binom{n-1}3$ for $n\ge4$, zero otherwise. If repetition is forbidden, use $\binom4n$ for $0\le n\le4$. If order remains visible, use $4^n$. These three modifications are different mechanisms, not corrections to the same multiset formula.

## Q46

**Correct option: 2.**

Option 2 is $\binom{n+3}3$. The proposals $n^3$, $4^n$, and $\binom n4$ lack respectively the coupled nonnegative-total constraint, the erasure of order, and the intended population of type labels. At $n=1$, four one-element multisets exist; $\binom43=4$ agrees, while these alternatives give 1, 4, and 0. The accidental equality with $4^1$ does not hold at size two, where there are ten multisets but sixteen words.

### Construction and proof


A multiset on four named types is exactly its multiplicity vector $(c_1,c_2,c_3,c_4)$, where $c_i\ge0$ and $\sum c_i=n$. A row of $n$ identical stars and three separators encodes these four counts, including zero counts through adjacent bars or endpoint bars. Selecting three separator positions among $n+3$ gives $\binom{n+3}3$.

This is the number of summaries, not their probabilities under random sequential draws. A vector has $n!/(c_1!c_2!c_3!c_4!)$ ordered preimages. The all-one-type vector has one; a vector $(n-1,1,0,0)$ has $n$ when $n\ge2$. Consequently uniform ordered words induce nonuniform multiset probabilities. Under independent uniform draws its mass is the preimage count divided by $4^n$.

If every type must appear, subtract one from all four coordinates and count $\binom{n-1}3$ for $n\ge4$, zero otherwise. If repetition is forbidden, use $\binom4n$ for $0\le n\le4$. If order remains visible, use $4^n$. These three modifications are different mechanisms, not corrections to the same multiset formula.

## Q47

**Correct option: 1.**

Option 1 correctly permits repetition and ignores order. The multiset with counts $(2,1,0,0)$ is one outcome although the three words AAB, ABA, and BAA realize it. Requiring every type would disallow this vector and change the lower bounds. Forbidding repeats would permit only counts zero or one. An empty multiset is one outcome, reflected by $\binom33=1$. These conventions are determined by the definition rather than by a factorial shortcut.

### Construction and proof


A multiset on four named types is exactly its multiplicity vector $(c_1,c_2,c_3,c_4)$, where $c_i\ge0$ and $\sum c_i=n$. A row of $n$ identical stars and three separators encodes these four counts, including zero counts through adjacent bars or endpoint bars. Selecting three separator positions among $n+3$ gives $\binom{n+3}3$.

This is the number of summaries, not their probabilities under random sequential draws. A vector has $n!/(c_1!c_2!c_3!c_4!)$ ordered preimages. The all-one-type vector has one; a vector $(n-1,1,0,0)$ has $n$ when $n\ge2$. Consequently uniform ordered words induce nonuniform multiset probabilities. Under independent uniform draws its mass is the preimage count divided by $4^n$.

If every type must appear, subtract one from all four coordinates and count $\binom{n-1}3$ for $n\ge4$, zero otherwise. If repetition is forbidden, use $\binom4n$ for $0\le n\le4$. If order remains visible, use $4^n$. These three modifications are different mechanisms, not corrections to the same multiset formula.

## Q48

**Correct option: 2.**

For five distinct labels, anchor one and permute the remaining four: $4!=24$, option 2. The value 120 counts five named linear seats; 60 equals $5!/2$ and removes a binary symmetry without removing rotations; 32 is $2^5$, unrelated to permutations of distinct labels. If reflections were also identified, the count would be 12, not 60. The exact equivalence relation must be stated before division.

### Construction and proof


Arrange $n\ge1$ distinct labels around a circle, identifying rotations but keeping reflections different. Anchor one specified label at the top. Reading clockwise from it orders the other $n-1$ labels, and every rotational class has exactly one such anchored representation. The count is $(n-1)!$.

Equivalently, the $n!$ linear listings have rotational fibers of size $n$ because all labels are distinct. Dividing by $n$ gives the same answer. For $n\ge3$, identifying reflections as well would divide the rotational count by two, since a distinct-label cyclic arrangement cannot equal its reverse. At $n=1,2$, this extra free-action assumption fails and must be handled directly.

Repeated labels also break the constant rotational-fiber argument. For two As and two Bs, the six linear words separate into the rotational class of AABB (four words) and the class of ABAB (two words). Their quotient has two outcomes, whereas $6/4$ is not an integer. An orbit-counting method is needed when symmetries fix some arrangements. A diagram's top position is an anchor convention, not an additional distinguishable seat.

## Q49

**Correct option: 1.**

For eight labels, anchoring gives $7!=5040$, option 1. The alternatives 40320 and 20160 equal $8!$ and $8!/2$, retaining named-seat rotations. The value 256 is $2^8$ and does not assign each distinct label once. Reflection equivalence would give $7!/2=2520$ for these eight distinct labels. This explains why a factorial divisor has to correspond to the stated symmetry.

### Construction and proof


Arrange $n\ge1$ distinct labels around a circle, identifying rotations but keeping reflections different. Anchor one specified label at the top. Reading clockwise from it orders the other $n-1$ labels, and every rotational class has exactly one such anchored representation. The count is $(n-1)!$.

Equivalently, the $n!$ linear listings have rotational fibers of size $n$ because all labels are distinct. Dividing by $n$ gives the same answer. For $n\ge3$, identifying reflections as well would divide the rotational count by two, since a distinct-label cyclic arrangement cannot equal its reverse. At $n=1,2$, this extra free-action assumption fails and must be handled directly.

Repeated labels also break the constant rotational-fiber argument. For two As and two Bs, the six linear words separate into the rotational class of AABB (four words) and the class of ABAB (two words). Their quotient has two outcomes, whereas $6/4$ is not an integer. An orbit-counting method is needed when symmetries fix some arrangements. A diagram's top position is an anchor convention, not an additional distinguishable seat.

## Q50

**Correct option: 4.**

Option 4's $(n-1)!$ holds on the positive-integer domain. The unrestricted $n!$ fixes an origin that the circle does not retain; $n!/2$ identifies only a twofold distinction and still overcounts rotations when $n>2$; $2^n$ counts binary words, not distinct-label circular permutations. At $n=1$, the anchored list of zero remaining labels is the empty permutation, contributing one.

### Construction and proof


Arrange $n\ge1$ distinct labels around a circle, identifying rotations but keeping reflections different. Anchor one specified label at the top. Reading clockwise from it orders the other $n-1$ labels, and every rotational class has exactly one such anchored representation. The count is $(n-1)!$.

Equivalently, the $n!$ linear listings have rotational fibers of size $n$ because all labels are distinct. Dividing by $n$ gives the same answer. For $n\ge3$, identifying reflections as well would divide the rotational count by two, since a distinct-label cyclic arrangement cannot equal its reverse. At $n=1,2$, this extra free-action assumption fails and must be handled directly.

Repeated labels also break the constant rotational-fiber argument. For two As and two Bs, the six linear words separate into the rotational class of AABB (four words) and the class of ABAB (two words). Their quotient has two outcomes, whereas $6/4$ is not an integer. An orbit-counting method is needed when symmetries fix some arrangements. A diagram's top position is an anchor convention, not an additional distinguishable seat.

## Q51

**Correct option: 3.**

Option 3 correctly requires specifying which symmetries are identified. Rotations only, rotations plus reflections, and labeled seats define different outcomes. Distinct labels make the rotational action free; repeated labels do not. The AABB/ABAB example gives unequal orbit sizes of four and two, proving why division by the number of rotations cannot be transferred blindly to multiset arrangements.

### Construction and proof


Arrange $n\ge1$ distinct labels around a circle, identifying rotations but keeping reflections different. Anchor one specified label at the top. Reading clockwise from it orders the other $n-1$ labels, and every rotational class has exactly one such anchored representation. The count is $(n-1)!$.

Equivalently, the $n!$ linear listings have rotational fibers of size $n$ because all labels are distinct. Dividing by $n$ gives the same answer. For $n\ge3$, identifying reflections as well would divide the rotational count by two, since a distinct-label cyclic arrangement cannot equal its reverse. At $n=1,2$, this extra free-action assumption fails and must be handled directly.

Repeated labels also break the constant rotational-fiber argument. For two As and two Bs, the six linear words separate into the rotational class of AABB (four words) and the class of ABAB (two words). Their quotient has two outcomes, whereas $6/4$ is not an integer. An orbit-counting method is needed when symmetries fix some arrangements. A diagram's top position is an anchor convention, not an additional distinguishable seat.

## Q52

**Correct option: 4.**

Ten objects give $M_5=9\cdot7\cdot5\cdot3\cdot1=945$, option 4. The alternative 113400 equals $10!/2^5$ and still names the five pairs by order; 30240 equals $10!/5!$ and still orients every pair. The value 252 equals $\binom{10}5$ and selects a half-population without matching partners. A factorial quotient must remove both description symmetries.

### Construction and proof


A pairing partitions $2n$ distinct objects into $n$ unordered two-element blocks, with the collection of blocks itself unordered. List all objects, pair adjacent entries, and erase both kinds of order. A fixed pairing has two orientations for each of its $n$ pairs and $n!$ orders of the pairs. The exact constant fiber size is $2^n n!$, giving

$$M_n=\frac{(2n)!}{2^n n!}=(2n-1)(2n-3)\cdots3\cdot1.$$

The second equality follows by separating even factors $(2n)(2n-2)\cdots2=2^n n!$ from the factorial. A second construction takes the smallest remaining label and chooses its partner in $2n-1$ ways, then recursively pairs the rest. This proves $M_n=(2n-1)M_{n-1}$ with $M_0=1$. The empty pairing is the sole partition of no objects. No pair is named by where it appears in a drawing.

Naming all pairs multiplies by $n!$. Orienting all pairs multiplies by $2^n$. These are independent description choices, explaining why each denominator factor is necessary. Choosing merely $n$ of the $2n$ objects does not specify their partners and therefore does not specify a pairing.

## Q53

**Correct option: 3.**

For sixteen objects, the exact product is $15\cdot13\cdot11\cdot9\cdot7\cdot5\cdot3=2027025$, option 3. The alternatives 81729648000 and 518918400 retain pair order and pair orientation respectively. The value 12870 is $\binom{16}8$, only a subset count. Dividing $16!$ by both $2^8$ and $8!$ reproduces the odd-factor product, an arithmetic and conceptual check.

### Construction and proof


A pairing partitions $2n$ distinct objects into $n$ unordered two-element blocks, with the collection of blocks itself unordered. List all objects, pair adjacent entries, and erase both kinds of order. A fixed pairing has two orientations for each of its $n$ pairs and $n!$ orders of the pairs. The exact constant fiber size is $2^n n!$, giving

$$M_n=\frac{(2n)!}{2^n n!}=(2n-1)(2n-3)\cdots3\cdot1.$$

The second equality follows by separating even factors $(2n)(2n-2)\cdots2=2^n n!$ from the factorial. A second construction takes the smallest remaining label and chooses its partner in $2n-1$ ways, then recursively pairs the rest. This proves $M_n=(2n-1)M_{n-1}$ with $M_0=1$. The empty pairing is the sole partition of no objects. No pair is named by where it appears in a drawing.

Naming all pairs multiplies by $n!$. Orienting all pairs multiplies by $2^n$. These are independent description choices, explaining why each denominator factor is necessary. Choosing merely $n$ of the $2n$ objects does not specify their partners and therefore does not specify a pairing.

## Q54

**Correct option: 2.**

Option 2 is $(2n)!/(2^n n!)$. The expressions omitting $n!$ or $2^n$ count ordered blocks or oriented blocks. The subset coefficient $\binom{2n}n$ omits partner assignment entirely. At $n=2$, the three pairings are $12|34$, $13|24$, and $14|23$; this small example makes both the result and its quotient interpretation concrete.

### Construction and proof


A pairing partitions $2n$ distinct objects into $n$ unordered two-element blocks, with the collection of blocks itself unordered. List all objects, pair adjacent entries, and erase both kinds of order. A fixed pairing has two orientations for each of its $n$ pairs and $n!$ orders of the pairs. The exact constant fiber size is $2^n n!$, giving

$$M_n=\frac{(2n)!}{2^n n!}=(2n-1)(2n-3)\cdots3\cdot1.$$

The second equality follows by separating even factors $(2n)(2n-2)\cdots2=2^n n!$ from the factorial. A second construction takes the smallest remaining label and chooses its partner in $2n-1$ ways, then recursively pairs the rest. This proves $M_n=(2n-1)M_{n-1}$ with $M_0=1$. The empty pairing is the sole partition of no objects. No pair is named by where it appears in a drawing.

Naming all pairs multiplies by $n!$. Orienting all pairs multiplies by $2^n$. These are independent description choices, explaining why each denominator factor is necessary. Choosing merely $n$ of the $2n$ objects does not specify their partners and therefore does not specify a pairing.

## Q55

**Correct option: 1.**

Option 1 correctly treats orientations and block order as separate symmetries. For pairing $12|34$, the listings 1234, 2134, 1243, 2143 and the corresponding four listings with block 34 first all encode the same outcome. There are $2^2\cdot2!=8$ descriptions, not four or two. Fixing the smallest remaining label in the recursive construction avoids these symmetries at construction time instead of correcting them afterward.

### Construction and proof


A pairing partitions $2n$ distinct objects into $n$ unordered two-element blocks, with the collection of blocks itself unordered. List all objects, pair adjacent entries, and erase both kinds of order. A fixed pairing has two orientations for each of its $n$ pairs and $n!$ orders of the pairs. The exact constant fiber size is $2^n n!$, giving

$$M_n=\frac{(2n)!}{2^n n!}=(2n-1)(2n-3)\cdots3\cdot1.$$

The second equality follows by separating even factors $(2n)(2n-2)\cdots2=2^n n!$ from the factorial. A second construction takes the smallest remaining label and chooses its partner in $2n-1$ ways, then recursively pairs the rest. This proves $M_n=(2n-1)M_{n-1}$ with $M_0=1$. The empty pairing is the sole partition of no objects. No pair is named by where it appears in a drawing.

Naming all pairs multiplies by $n!$. Orienting all pairs multiplies by $2^n$. These are independent description choices, explaining why each denominator factor is necessary. Choosing merely $n$ of the $2n$ objects does not specify their partners and therefore does not specify a pairing.

## Q56

**Correct option: 2.**

At $n=5$, the alternating terms are $120-120+60-20+5-1=44$, option 2. The recurrence gives $D_2=1,D_3=2,D_4=9,D_5=4(9+2)=44$. The value 119 removes only the identity; 120 removes nothing; 24 counts only five-cycles. Derangements also include products of a two-cycle and a three-cycle, of which there are $\binom52\cdot2=20$; adding these to 24 gives 44.

### Construction and proof


Let $B_i$ be the set of permutations fixing label $i$. An intersection fixing a selected set of $j$ labels contains $(n-j)!$ permutations. Inclusion–exclusion over these $n$ forbidden events gives

$$D_n=\sum_{j=0}^{n}(-1)^j\binom nj(n-j)!=n!\sum_{j=0}^{n}\frac{(-1)^j}{j!}.$$

The forbidden events overlap: the identity belongs to every one of them, and many nonidentity permutations still fix some labels. Removing only the identity does not remove all fixed points. To count exactly $k$ fixed points, select them in $\binom nk$ ways and derange the other $n-k$ labels, giving $\binom nkD_{n-k}$; freely permuting the remainder would permit extra fixed points.

For a recurrence proof, send label 1 to some $j\ne1$ in $n-1$ ways. If $j$ maps back to 1, remove their two-cycle and derange the other $n-2$ labels. Otherwise remove 1 from its cycle: if $i$ previously mapped to 1, redirect it to $j$. This produces a derangement on the other $n-1$ labels. Conversely insert 1 before $j$ in any such derangement, uniquely. Hence $D_n=(n-1)(D_{n-1}+D_{n-2})$, with $D_0=1,D_1=0$. An empty permutation has no fixed points; one label cannot move elsewhere.

## Q57

**Correct option: 1.**

For $n=8$, recurrence values $D_5=44,D_6=265,D_7=1854$ give $D_8=7(1854+265)=14833$, option 1. The values 40320 and 40319 count all permutations or remove only the identity; 5040 counts eight-cycles and misses other cycle decompositions without singleton cycles. Uniform permutation probability is $14833/40320$, not a count divided by an arbitrary nearby factorial.

### Construction and proof


Let $B_i$ be the set of permutations fixing label $i$. An intersection fixing a selected set of $j$ labels contains $(n-j)!$ permutations. Inclusion–exclusion over these $n$ forbidden events gives

$$D_n=\sum_{j=0}^{n}(-1)^j\binom nj(n-j)!=n!\sum_{j=0}^{n}\frac{(-1)^j}{j!}.$$

The forbidden events overlap: the identity belongs to every one of them, and many nonidentity permutations still fix some labels. Removing only the identity does not remove all fixed points. To count exactly $k$ fixed points, select them in $\binom nk$ ways and derange the other $n-k$ labels, giving $\binom nkD_{n-k}$; freely permuting the remainder would permit extra fixed points.

For a recurrence proof, send label 1 to some $j\ne1$ in $n-1$ ways. If $j$ maps back to 1, remove their two-cycle and derange the other $n-2$ labels. Otherwise remove 1 from its cycle: if $i$ previously mapped to 1, redirect it to $j$. This produces a derangement on the other $n-1$ labels. Conversely insert 1 before $j$ in any such derangement, uniquely. Hence $D_n=(n-1)(D_{n-1}+D_{n-2})$, with $D_0=1,D_1=0$. An empty permutation has no fixed points; one label cannot move elsewhere.

## Q58

**Correct option: 4.**

Option 4 is the alternating factorial sum. The proposals $n!$, $n!-1$, and $(n-1)!$ respectively impose no exclusion, exclude only one permutation, or require one full cycle. At $n=4$, the six four-cycles and three products of disjoint transpositions produce nine derangements, already disproving the full-cycle alternative. The expression is exact; $n!/e$ is only an approximation and needs a separate error argument if used.

### Construction and proof


Let $B_i$ be the set of permutations fixing label $i$. An intersection fixing a selected set of $j$ labels contains $(n-j)!$ permutations. Inclusion–exclusion over these $n$ forbidden events gives

$$D_n=\sum_{j=0}^{n}(-1)^j\binom nj(n-j)!=n!\sum_{j=0}^{n}\frac{(-1)^j}{j!}.$$

The forbidden events overlap: the identity belongs to every one of them, and many nonidentity permutations still fix some labels. Removing only the identity does not remove all fixed points. To count exactly $k$ fixed points, select them in $\binom nk$ ways and derange the other $n-k$ labels, giving $\binom nkD_{n-k}$; freely permuting the remainder would permit extra fixed points.

For a recurrence proof, send label 1 to some $j\ne1$ in $n-1$ ways. If $j$ maps back to 1, remove their two-cycle and derange the other $n-2$ labels. Otherwise remove 1 from its cycle: if $i$ previously mapped to 1, redirect it to $j$. This produces a derangement on the other $n-1$ labels. Conversely insert 1 before $j$ in any such derangement, uniquely. Hence $D_n=(n-1)(D_{n-1}+D_{n-2})$, with $D_0=1,D_1=0$. An empty permutation has no fixed points; one label cannot move elsewhere.

## Q59

**Correct option: 3.**

Option 3 correctly excludes all fixed-point events. A swap of labels 1 and 2 with every other label fixed is nonidentity but fails to be a derangement when $n>2$. Conversely the permutation $(12)(34)$ is a derangement on four labels despite not being a four-cycle. Exactly $n-1$ fixed points is impossible because the remaining label is forced to its own position. This boundary is encoded by $D_1=0$.

### Construction and proof


Let $B_i$ be the set of permutations fixing label $i$. An intersection fixing a selected set of $j$ labels contains $(n-j)!$ permutations. Inclusion–exclusion over these $n$ forbidden events gives

$$D_n=\sum_{j=0}^{n}(-1)^j\binom nj(n-j)!=n!\sum_{j=0}^{n}\frac{(-1)^j}{j!}.$$

The forbidden events overlap: the identity belongs to every one of them, and many nonidentity permutations still fix some labels. Removing only the identity does not remove all fixed points. To count exactly $k$ fixed points, select them in $\binom nk$ ways and derange the other $n-k$ labels, giving $\binom nkD_{n-k}$; freely permuting the remainder would permit extra fixed points.

For a recurrence proof, send label 1 to some $j\ne1$ in $n-1$ ways. If $j$ maps back to 1, remove their two-cycle and derange the other $n-2$ labels. Otherwise remove 1 from its cycle: if $i$ previously mapped to 1, redirect it to $j$. This produces a derangement on the other $n-1$ labels. Conversely insert 1 before $j$ in any such derangement, uniquely. Hence $D_n=(n-1)(D_{n-1}+D_{n-2})$, with $D_0=1,D_1=0$. An empty permutation has no fixed points; one label cannot move elsewhere.

## Q60

**Correct option: 3.**

For five elements, choose the common label in five ways and distribute four others in $2^4=16$ ways: $N=80$, option 3. The value 243 equals $3^5$ and fails the exact intersection constraint. The value 160 gives the common element an extra binary assignment even though it is forced into both sets. The value 10 equals $\binom52$ and chooses two labels rather than membership for every label.

### Construction and proof


Let $S$ be a labeled $n$-element ground set and consider ordered pairs $(A,B)$ with $A\cup B=S$ and $|A\cap B|=1$. Choose the common element in $n$ ways. Every other element must belong to exactly one of $A$ or $B$, so each has two independent construction choices. Thus $N=n2^{n-1}$ for $n\ge1$.

The construction is reversible: the unique intersection identifies the common element and the remaining membership labels recover all binary choices. Allowing each element three roles, A-only, B-only, and both, would give $3^n$ but permit arbitrary intersection sizes. A general exact-intersection count is $\binom nr2^{n-r}$ for $0\le r\le n$, because the $r$ shared elements are selected first. Prescribing which element is common removes the leading factor $n$.

If the pair $(A,B)$ becomes unordered, swapping A and B has no fixed outcome for $n\ge2$: a fixed pair would have $A=B=S$, violating intersection size one. The unordered count is then $n2^{n-2}$. At $n=1$, however, the sole pair $A=B=S$ is fixed by swapping and the unordered count remains one, not one half. The empty ground set cannot have a singleton intersection and has zero such outcomes.

## Q61

**Correct option: 2.**

For eight elements, $N=8\cdot2^7=1024$, option 2. The alternatives 6561, 2048, and 28 respectively permit all three membership roles per element, assign an extra choice to the already-common element, or choose two labels only. These counts do not record the exact ordered membership vector. A fixed common element would instead give $2^7=128$, providing a check on the factor eight.

### Construction and proof


Let $S$ be a labeled $n$-element ground set and consider ordered pairs $(A,B)$ with $A\cup B=S$ and $|A\cap B|=1$. Choose the common element in $n$ ways. Every other element must belong to exactly one of $A$ or $B$, so each has two independent construction choices. Thus $N=n2^{n-1}$ for $n\ge1$.

The construction is reversible: the unique intersection identifies the common element and the remaining membership labels recover all binary choices. Allowing each element three roles, A-only, B-only, and both, would give $3^n$ but permit arbitrary intersection sizes. A general exact-intersection count is $\binom nr2^{n-r}$ for $0\le r\le n$, because the $r$ shared elements are selected first. Prescribing which element is common removes the leading factor $n$.

If the pair $(A,B)$ becomes unordered, swapping A and B has no fixed outcome for $n\ge2$: a fixed pair would have $A=B=S$, violating intersection size one. The unordered count is then $n2^{n-2}$. At $n=1$, however, the sole pair $A=B=S$ is fixed by swapping and the unordered count remains one, not one half. The empty ground set cannot have a singleton intersection and has zero such outcomes.

## Q62

**Correct option: 1.**

Option 1 is $n2^{n-1}$. The alternatives $3^n$, $n2^n$, and $\binom n2$ violate respectively the fixed intersection size, the forced common-element role, and the requirement to assign every element's membership. At $n=1$ the formula gives one, namely $(S,S)$; this endpoint is important before attempting any later quotient by exchanging A and B.

### Construction and proof


Let $S$ be a labeled $n$-element ground set and consider ordered pairs $(A,B)$ with $A\cup B=S$ and $|A\cap B|=1$. Choose the common element in $n$ ways. Every other element must belong to exactly one of $A$ or $B$, so each has two independent construction choices. Thus $N=n2^{n-1}$ for $n\ge1$.

The construction is reversible: the unique intersection identifies the common element and the remaining membership labels recover all binary choices. Allowing each element three roles, A-only, B-only, and both, would give $3^n$ but permit arbitrary intersection sizes. A general exact-intersection count is $\binom nr2^{n-r}$ for $0\le r\le n$, because the $r$ shared elements are selected first. Prescribing which element is common removes the leading factor $n$.

If the pair $(A,B)$ becomes unordered, swapping A and B has no fixed outcome for $n\ge2$: a fixed pair would have $A=B=S$, violating intersection size one. The unordered count is then $n2^{n-2}$. At $n=1$, however, the sole pair $A=B=S$ is fixed by swapping and the unordered count remains one, not one half. The empty ground set cannot have a singleton intersection and has zero such outcomes.

## Q63

**Correct option: 4.**

Option 4 correctly distinguishes a prescribed common element from a merely singleton intersection. On a three-element set with the common label fixed, the other two labels supply four assignments. Without prescribing the common label there are three choices of it and twelve ordered pairs. The two formulations differ by a factor of three, not by an intersection probability. An unordered interpretation needs a separate swap-orbit argument and has a special one-element boundary.

### Construction and proof


Let $S$ be a labeled $n$-element ground set and consider ordered pairs $(A,B)$ with $A\cup B=S$ and $|A\cap B|=1$. Choose the common element in $n$ ways. Every other element must belong to exactly one of $A$ or $B$, so each has two independent construction choices. Thus $N=n2^{n-1}$ for $n\ge1$.

The construction is reversible: the unique intersection identifies the common element and the remaining membership labels recover all binary choices. Allowing each element three roles, A-only, B-only, and both, would give $3^n$ but permit arbitrary intersection sizes. A general exact-intersection count is $\binom nr2^{n-r}$ for $0\le r\le n$, because the $r$ shared elements are selected first. Prescribing which element is common removes the leading factor $n$.

If the pair $(A,B)$ becomes unordered, swapping A and B has no fixed outcome for $n\ge2$: a fixed pair would have $A=B=S$, violating intersection size one. The unordered count is then $n2^{n-2}$. At $n=1$, however, the sole pair $A=B=S$ is fixed by swapping and the unordered count remains one, not one half. The empty ground set cannot have a singleton intersection and has zero such outcomes.

## Q64

**Correct option: 1.**

For five couples, the block order count is $5!=120$ and orientation count is $2^5=32$. Their product is 3840, option 1. The value 3628800 counts all ten-person rows without the adjacency restrictions. The value 120 suppresses every internal orientation. The value 768 equals $2^5\cdot4!$ and counts circular rather than linear block arrangements. Position one is part of a linear row's outcome.

### Construction and proof


In a linear row, treat each of $n$ specified couples as a block. Because all people are distinct, the blocks are distinct and can be ordered in $n!$ ways. Every block has two possible internal orientations, independently of all other block orientations, giving $2^n n!$.

The construction is reversible: in any allowed row the two members of every couple occupy adjacent positions. Reading these nonoverlapping blocks from left to right recovers the block order and orientations uniquely. There is no division for swapping partners, because reversing a couple changes the actual person in each seat. Nor are blocks indistinguishable, because their memberships differ.

If the row is replaced by a circle and rotations are identified while reflections remain distinct, the analogous count is $2^n(n-1)!$ for $n\ge2$. The blocks then have a circular order. At $n=1$, however, the two orientations of a single two-person block become the same rotational arrangement, so the circular count is one, not two. For the linear row the positive-domain formula remains valid at $n=1$, and the empty arrangement naturally has one construction at $n=0$.

## Q65

**Correct option: 4.**

Eight couples give $2^8\cdot8!=256\cdot40320=10321920$, option 4. The unrestricted $16!=20922789888000$ ignores adjacency. The value 40320 counts block order only. The value 1290240 equals $2^8\cdot7!$ and erases rotations as if the row were circular. The multiplication counts the actual positions of all sixteen distinct people.

### Construction and proof


In a linear row, treat each of $n$ specified couples as a block. Because all people are distinct, the blocks are distinct and can be ordered in $n!$ ways. Every block has two possible internal orientations, independently of all other block orientations, giving $2^n n!$.

The construction is reversible: in any allowed row the two members of every couple occupy adjacent positions. Reading these nonoverlapping blocks from left to right recovers the block order and orientations uniquely. There is no division for swapping partners, because reversing a couple changes the actual person in each seat. Nor are blocks indistinguishable, because their memberships differ.

If the row is replaced by a circle and rotations are identified while reflections remain distinct, the analogous count is $2^n(n-1)!$ for $n\ge2$. The blocks then have a circular order. At $n=1$, however, the two orientations of a single two-person block become the same rotational arrangement, so the circular count is one, not two. For the linear row the positive-domain formula remains valid at $n=1$, and the empty arrangement naturally has one construction at $n=0$.

## Q66

**Correct option: 3.**

Option 3 is $2^n n!$. The proposals $(2n)!$, $n!$, and $2^n(n-1)!$ respectively remove the adjacency requirement, remove partner orientations, or replace the row by a circle. With one couple the linear arrangements AB and BA are two, so a formula returning one has changed the outcome equivalence relation.

### Construction and proof


In a linear row, treat each of $n$ specified couples as a block. Because all people are distinct, the blocks are distinct and can be ordered in $n!$ ways. Every block has two possible internal orientations, independently of all other block orientations, giving $2^n n!$.

The construction is reversible: in any allowed row the two members of every couple occupy adjacent positions. Reading these nonoverlapping blocks from left to right recovers the block order and orientations uniquely. There is no division for swapping partners, because reversing a couple changes the actual person in each seat. Nor are blocks indistinguishable, because their memberships differ.

If the row is replaced by a circle and rotations are identified while reflections remain distinct, the analogous count is $2^n(n-1)!$ for $n\ge2$. The blocks then have a circular order. At $n=1$, however, the two orientations of a single two-person block become the same rotational arrangement, so the circular count is one, not two. For the linear row the positive-domain formula remains valid at $n=1$, and the empty arrangement naturally has one construction at $n=0$.

## Q67

**Correct option: 2.**

Option 2 correctly notes that a circle changes the block-order factor. For two couples, linear order gives $2^2\cdot2!=8$ rows; modulo whole-row rotation the permitted circular arrangements number $2^2\cdot1!=4$. The single-couple case is exceptional because reversing its block is itself a rotation. A quotient is justified by the actual equivalence classes, not by reusing a familiar factorial denominator without a boundary check.

### Construction and proof


In a linear row, treat each of $n$ specified couples as a block. Because all people are distinct, the blocks are distinct and can be ordered in $n!$ ways. Every block has two possible internal orientations, independently of all other block orientations, giving $2^n n!$.

The construction is reversible: in any allowed row the two members of every couple occupy adjacent positions. Reading these nonoverlapping blocks from left to right recovers the block order and orientations uniquely. There is no division for swapping partners, because reversing a couple changes the actual person in each seat. Nor are blocks indistinguishable, because their memberships differ.

If the row is replaced by a circle and rotations are identified while reflections remain distinct, the analogous count is $2^n(n-1)!$ for $n\ge2$. The blocks then have a circular order. At $n=1$, however, the two orientations of a single two-person block become the same rotational arrangement, so the circular count is one, not two. For the linear row the positive-domain formula remains valid at $n=1$, and the empty arrangement naturally has one construction at $n=0$.

## Q68

**Correct option: 1.**

Put $a=2j$ and $c=2+c'$, where $j,c'\ge0$. The equation becomes $2j+b+c'=16$, with $b=0,1,2,3$. For fixed $b$, $j$ ranges from 0 through $\lfloor(16-b)/2\rfloor$, and $c'$ is then forced.

| $b$ | Upper endpoint for $j$ | Number of triples |
|---|---|---|
| 0 | 8 | 9 |
| 1 | 7 | 8 |
| 2 | 7 | 8 |
| 3 | 6 | 7 |

The exact count is $9+8+8+7=32$, option 1. The proposed counts 33, 34, and 36 do not match this exhaustive disjoint ledger. Notice that $b=1$ and $b=2$ share the same endpoint; treating every increase in $b$ as a decrease of one in $j$ is wrong because $j$ contributes two units. The general row formula is $\max(0,\lfloor(N-b-L)/2\rfloor+1)$ for total $N$ and lower bound $c\ge L$, summed over the permitted $b$. The maximum handles an empty row rather than allowing a negative count.

## Q69

**Correct option: 1.**

Partition by the exact size $k$ of the first target's fiber. This fiber must contain at least two of the five domain elements. Because the other two target values must each be hit, $k\le3$. For a fixed first fiber of size $k$, the remaining $5-k$ elements must map onto two named values. There are $2^{5-k}-2$ such maps, obtained by excluding the two constant maps.

$$N=\binom52(2^3-2)+\binom53(2^2-2)=10\cdot6+10\cdot2=80.$$

Option 1 is correct. Unrestricted onto maps number $3^5-3\cdot2^5+3=150$. The excluded maps with first fiber size one number $\binom51(2^4-2)=70$, confirming $150-70=80$. The values 100 and 120 are not either exact fiber sum. Selecting two witnesses for the first fiber and then assigning the rest would count a size-three fiber three times; the exact-size partition avoids this.

For general domain size $m$, the answer is $\sum_{k=2}^{m-2}\binom mk(2^{m-k}-2)$ with an empty sum equal to zero. This domain restriction expresses surjectivity, rather than leaving impossible large fibers in the count.

## Q70

**Correct option: 2.**

Even numbers of zeros in a length-five ternary word are 0, 2, and 4. Once zero positions are chosen, the other positions have two choices each:

$$E=\binom50 2^5+\binom52 2^3+\binom54 2=32+80+10=122.$$

The odd count is $\binom51 2^4+\binom53 2^2+\binom55=80+40+1=121$. These sum to $3^5=243$ and differ by one, as $(2-1)^5=1$ predicts. Thus option 2 is correct; 121 counts the opposite parity, 123 does not satisfy either parity ledger, and 81 is the total for length four instead of length five.

For length $m$, the same filter gives $E_m=(3^m+1)/2$ and $O_m=(3^m-1)/2$. The parity imbalance is smaller than in the four-symbol example, but it remains exact and cannot be discarded by a symmetry claim. At length zero the single empty word belongs to $E_0$.

## Q71

**Correct option: 1.**

Order the eight distinct objects, pair consecutive entries, and then erase internal pair orientations and the order of the four pairs. Every final pairing is represented by exactly $2^4\cdot4!$ orderings. Hence

$$N=\frac{8!}{2^4 4!}=\frac{40320}{384}=105.$$

An independent anchor argument pairs the smallest remaining object in 7 ways, then the smallest remaining one in 5, then in 3, then in 1. This gives $7\cdot5\cdot3\cdot1=105$, option 1. The count 2520 equals $8!/2^4$ and still orders the pairs; 1680 equals $8!/4!$ and still orients each pair. The value 210 is twice the correct count without a requested binary distinction. A pairing can be displayed as edges between labeled vertices, but the positions of edges on the page are not names of pairs.

## Q72

**Correct option: 1.**

Count pairs $(R,S)$ with $R\subseteq S\subseteq\{1,\ldots,9\}$ and $|R|=3$. By $|S|=k$, the count is $\sum_{k=3}^{9}\binom9k\binom k3$. Alternatively choose the marked triple $R$ in $\binom93=84$ ways; every other element independently joins $S$ or stays outside. This gives

$$\sum_{k=3}^{9}\binom9k\binom k3=\binom93 2^6=5376.$$

This is option 1. The value 84 omits all choices of the six optional elements. Halving or doubling the remaining factor gives 2688 or 10752, but no extra symmetry or binary choice is present. For a fixed size $k$, the two-order identity is $\binom9k\binom k3=\binom93\binom6{k-3}$, so the summation follows from the binomial theorem as well. Distinguish a marked subset from an unmarked subset: one seven-element $S$ contributes $\binom73$ pairs, not one.

## Q73

**Correct option: 1.**

Let $r$ be the number of algebra problems selected. Then $r\ge3$ and $6-r\ge2$, so $r=3$ or $4$. There are five distinct problems in each category, and selection order does not matter.

| Algebra count | Programming count | Subsets |
|---|---|---|
| 3 | 3 | $\binom53\binom53=100$ |
| 4 | 2 | $\binom54\binom52=50$ |

Therefore $N=150$, option 1. The unrestricted count is $\binom{10}6=210$. Its excluded feasible categories are $r=1,2,5$, with counts $5,50,5$; subtracting 60 gives the same 150. The values 175 and 200 fail this category partition. “At least three algebra” alone would also include $r=5$; the second lower bound is an independent restriction. Choosing minimum witnesses before adding elements counts different final subsets a different number of times, so exact category counts are preferable.

## Q74

**Correct option: 1.**

Let $X$ and $Y$ be the heads counts in eight and five independent fair tosses. The two blocks are independent. Equality can occur at $k=0,\ldots,5$, giving

$$P(X=Y)=\frac{1}{2^{13}}\sum_{k=0}^{5}\binom8k\binom5k.$$

Use $\binom5k=\binom5{5-k}$. Vandermonde's identity counts five-subsets of a disjoint union of sets of sizes eight and five, so the numerator is $\binom{13}5=1287$. The probability is $1287/8192$, option 1. A direct sum is $1+40+280+560+350+56=1287$.

Option 2 has the same numerator because $\binom{13}8=\binom{13}5$, but denominator $2^8$ ignores five tosses and even produces a number greater than one. Option 3 retains only one binomial term rather than the disjoint equality cases. Option 4's one-half symmetry is not a symmetry of equality: swapping the blocks maps equality to itself, not to its complement. Counts cannot be uniformly averaged; each count has its own binomial multiplicity.

## Q75

**Correct option: 3.**

A weakly increasing sequence is determined by multiplicities $(c_1,c_2,c_3)$ with total four. Requiring the value 2 means $c_2\ge1$. Write $d_2=c_2-1\ge0$; then $c_1+d_2+c_3=3$. Stars and bars gives $\binom52=10$, option 3.

For a direct check, partition by $c_2=1,2,3,4$. The remaining counts $(c_1,c_3)$ sum to $3,2,1,0$ and yield $4,3,2,1$ possibilities, totaling 10. A complement count starts with all $\binom62=15$ weakly increasing sequences and subtracts the five avoiding 2, determined by $c_1+c_3=4$. Thus option 4's 15 ignores the occurrence requirement, while option 1's 5 counts the excluded event. The proposed 8 does not fit the complete multiplicity ledger.

There is exactly one sorted sequence per vector, so no multinomial factor is used. If arbitrary unsorted length-four words were requested instead, the answer containing at least one 2 would be $3^4-2^4=65$, a different outcome contract.

## Q76

**Correct option: 3.**

For four coordinates with $1\le x_i\le5$ and total 12, set $y_i=x_i-1$. Then $0\le y_i\le4$ and $\sum y_i=8$. The unrestricted nonnegative count is $\binom{11}3=165$.

A violation is $y_i\ge5$, not $y_i\ge4$. For a chosen violating coordinate, subtract five and distribute the remaining three units among four coordinates in $\binom63=20$ ways. There are four choices of violator. Two simultaneous violations would need at least ten units, exceeding eight, so no pair correction survives:

$$N=\binom{11}3-4\binom63=165-80=85.$$

Option 3 is correct. Option 4 counts without upper bounds; option 2 is the excluded count, not the retained count. The proposed 65 results from no complete valid violation partition here. Reflecting $y_i$ to $4-y_i$ preserves the total eight and gives a useful symmetry check, but it does not justify halving the unrestricted count. The shift must preserve both endpoints before inclusion–exclusion is applied.

## Q77

**Correct option: 2.**

The actual experiment generates three independent fair bits. Its eight ordered strings each have probability $1/8$. Reporting only a multiset merges strings, but does not change their original masses.

| Number of ones | Ordered preimages | Reported probability |
|---|---|---|
| 0 | 000 | $1/8$ |
| 1 | 001, 010, 100 | $3/8$ |
| 2 | 011, 101, 110 | $3/8$ |
| 3 | 111 | $1/8$ |

Two zeros and one one is the second row, so the probability is $3/8$, option 2. Option 1 assumes the four summaries are uniform; their fibers have sizes $1,3,3,1$, so this is false. A one-half or two-thirds answer likewise fails the induced mass ledger. Counts of summaries and probabilities of summaries are distinct quantities.

If the original independent bits had success probability $p$, this report would have mass $\binom31p(1-p)^2$. If instead a mechanism chose one of the four multisets uniformly, its probability would be $1/4$. Both are legitimate models, but only the first is specified in this problem.
