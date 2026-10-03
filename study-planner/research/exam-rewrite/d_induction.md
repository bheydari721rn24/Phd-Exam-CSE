## Teaching through formulas and conceptual decisions

### Recognize the increment, not only the final closed form

For a sum $S_n=\sum_{j=1}^n f(j)$, the induction step is $S_{k+1}=S_k+f(k+1)$. To test a proposed closed form $F(n)$, compute $F(k+1)-F(k)$ and compare it with $f(k+1)$; also check the first allowed index. The increment and the base together determine the whole sequence. A formula may pass the increment test and still have the wrong additive constant.

For example, $F(n)=n(n+1)(2n+1)/6$ has difference $(n+1)^2$ and $F(0)=0$, proving the sum-of-squares identity. Weighted geometric sums can be checked the same way: for $r\ne1$,

$$\sum_{j=1}^n jr^j=\frac{r-(n+1)r^{n+1}+nr^{n+2}}{(1-r)^2}.$$

The missing case $r=1$ is the arithmetic sum, not a division by zero. Such parameter cases are part of the theorem's statement.

### Bases are a reachability problem

A step $P(k)\Rightarrow P(k+d)$ stays in one residue class modulo $d$. To cover every integer from a starting point, establish a base in every required residue class. A step using the two preceding values needs two consecutive initial values unless a separately proved start supplies the missing dependency. “Strong induction” does not automatically grant statements below the stated starting index.

For postage using nonnegative counts of four-unit and five-unit pieces, 12,13,14,15 are consecutive representable bases. Adding four then covers every integer at least12. Since11 is impossible,12 is the least all-future threshold. Proving isolated larger values would not establish the consecutive interval needed by this step.

### Inequality induction needs a closing inequality

To prove $2^n\ge n^2$ eventually, multiplying the hypothesis by2 yields $2^{k+1}\ge2k^2$. One must separately show $2k^2\ge(k+1)^2$, equivalent to $k^2-2k-1\ge0$. This holds for integer $k\ge3$, and the chosen base $n=4$ closes the proof. Writing the desired next bound without this comparison merely repeats the goal.

## Formula and conceptual problem bank

### Question 1. A weighted geometric sum

Find $\sum_{j=1}^{5}j2^j$.

**A.** 258

**B.** 260

**C.** 320

**D.** 192

**Answer: A.**

The terms are $2,8,24,64,160$, which sum to258. Alternatively the formula at $r=2$ simplifies to $(n-1)2^{n+1}+2$, yielding $4\cdot64+2=258$. The constant2 is fixed by the base case. The option260 has an incorrect constant,320 incorrectly multiplies the last power by the arithmetic sum, and192 does not count the weights correctly.

### Question 2. Closed-form difference test

A proposed formula $S_n=n(n+1)(2n+1)/6$ has what increment $S_{n+1}-S_n$?

**A.** $n^2$

**B.** $(n+1)^2$

**C.** $2n+1$

**D.** $n(n+1)$

**Answer: B.**

Factor the shared $(n+1)/6$. The remaining difference is $(n+2)(2n+3)-n(2n+1)=6(n+1)$. The product is therefore $(n+1)^2$. This matches adding the next square to a sum ending at $n$. The expression $2n+1$ is the increment of $n^2$, not of the cumulative sum of squares.

### Question 3. Step size three

Only the rule $P(k)\Rightarrow P(k+3)$ is available for $k\ge2$. Which base set suffices to establish $P(n)$ for every $n\ge2$?

**A.** $P(2)$ only

**B.** $P(2),P(3)$

**C.** $P(2),P(3),P(4)$

**D.** $P(2),P(5),P(8)$

**Answer: C.**

The starting integers2,3,4 represent all three residue classes modulo3. Repeated use of the step covers respectively2,5,8,...;3,6,9,...;4,7,10,.... OptionD establishes only the first of those chains. Two bases leave one class uncovered. The rule has no operation that transfers a proof between residue classes.

### Question 4. An eventual exponential inequality

What is the smallest $N\ge1$ such that $2^n\ge n^2$ for every integer $n\ge N$?

**A.** 1

**B.** 2

**C.** 3

**D.** 4

**Answer: D.**

At $n=3$, $8<9$, so every candidate threshold at most3 fails. At4 the inequality is equality. If it holds at $k\ge4$, then $2^{k+1}\ge2k^2\ge(k+1)^2$ since $k^2-2k-1>0$. Thus4 is sufficient and necessary. Checking1 and2 alone misses the failure at3; an eventual claim requires all later values.

### Question 5. Consecutive postage bases

Nonnegative combinations of4 and5 represent every integer from what least threshold onward?

**A.** 10

**B.** 11

**C.** 12

**D.** 16

**Answer: C.**

Values12,13,14,15 are $3\cdot4$, $2\cdot4+5$, $4+2\cdot5$, and $3\cdot5$. For any $n\ge16$, subtract4 and use induction. Value11 is not representable: possible numbers of five-unit pieces are0,1,2, leaving11,6,1, none divisible by4. Therefore12 is the least threshold. The four consecutive bases match the four-step recurrence.

### Question 6. A binary-string recurrence

Let $b_n$ count length-$n$ binary strings without adjacent ones, with $b_0=1,b_1=2$. What is $b_5$?

**A.** 8

**B.** 13

**C.** 16

**D.** 21

**Answer: B.**

Partition strings by their start:0 followed by a valid length-$n-1$ string, or10 followed by a valid length-$n-2$ string. These cases are disjoint and exhaustive, yielding $b_n=b_{n-1}+b_{n-2}$. The next values are3,5,8,13. OptionA is $b_4$ andD is $b_6$. The two bases include the one empty string, not zero empty strings.

### Question 7. Divisibility by a step

For every integer $n\ge0$, which divisor always divides $5^n-1$?

**A.** 3

**B.** 4

**C.** 5

**D.** 8

**Answer: B.**

At0 the expression is0, divisible by4. If $5^k-1=4q$, then $5^{k+1}-1=5(5^k-1)+4=4(5q+1)$. This is a direct induction certificate. At $n=1$, the value4 refutes divisors3,5 and8. The factorization of the increment exposes the required constant remainder.

### Question 8. A false induction with a true-looking base

The statement $n^2\le2^n$ is checked at1 and2. A claimed step replaces $2k^2$ by $(k+1)^2$ for all $k\ge1$. What first fails?

**A.** The base at1.

**B.** The necessary inequality at $k=2$, since8 is less than9.

**C.** Every base case.

**D.** The use of ordinary induction itself.

**Answer: B.**

The bases1 and2 satisfy the statement, but at the step from2 to3 the hypothesis yields only $2^3\ge2(2^2)=8$. The desired next square is9. The needed comparison $2k^2\ge(k+1)^2$ fails for $k=2$. Ordinary induction is valid; this particular closing inequality is not. The actual statement is false at3, agreeing with the identified gap.

### Question 9. Hockey-stick boundary

Find $\sum_{j=3}^{8}\binom j3$.

**A.** 56

**B.** 70

**C.** 126

**D.** 210

**Answer: C.**

Pascal gives $\binom j3=\binom{j+1}4-\binom j4$. Summing telescopes to $\binom94-\binom34=126$. The lower term is zero because three objects cannot supply four. The direct terms1,4,10,20,35,56 also sum to126. The upper index is one larger than the last summation index.

### Question 10. Telescoping induction

What is $\sum_{j=1}^{n}1/(j(j+1))$ for integer $n\ge1$?

**A.** $1/n$

**B.** $n/(n+1)$

**C.** $n/2$

**D.** $1/(n+1)$

**Answer: B.**

Write each term as $1/j-1/(j+1)$. Every intermediate reciprocal cancels and the result is $1-1/(n+1)=n/(n+1)$. The base $n=1$ gives1/2. For an induction check, add $1/((k+1)(k+2))$ to $k/(k+1)$ and combine to $(k+1)/(k+2)$. OptionD retains only the discarded final reciprocal.

<!-- CHALLENGE-BANK -->

### Question 11. Challenge: Weighted binomial sum

What is$\sum_{j=0}^{6}j^2\binom6j$?

**A.** 192

**B.** 480

**C.** 672

**D.** 768

**Answer: C.**

Write$j^2=j(j-1)+j$. A subset with one distinguished member is counted by$n2^{n-1}$; one with two ordered distinct distinguished members is$n(n-1)2^{n-2}$. For$n=6$, these counts are192 and480. Their sum is672. The endpoint$j=0$ contributes zero; the two-member part cannot count the repeated-member case, which is why the additional one-member count is necessary. Pascal induction provides another proof of the two identities.

### Question 12. Challenge: Two-step recurrence and bases

A proof step derives$P(k+2)$ from$P(k)$ for every$k\ge0$. Which conclusion is justified from only$P(0)$?

**A.** All$P(n)$ for$n\ge0$.

**B.** Exactly all even-index$P(n)$ are established by this rule.

**C.** Exactly all odd-index$P(n)$ are established.

**D.** No later index is established.

**Answer: B.**

The dependency edges add2 and preserve parity. Starting0 yields2,4,6 and all later even indices by ordinary induction on half the index. There is no predecessor path to1 or any odd index. To cover all nonnegative integers, also establish$P(1)$ and propagate its odd chain. Strong induction cannot fill the missing base without a separately valid rule; changing the name of the proof method does not change reachability.

## Applicable formulas and examination notes

### 1. Increment check

For a sum ending at $n$, verify $F(n+1)-F(n)=f(n+1)$ and one base value. These two conditions prove the candidate closed form by induction. Testing only the increment misses an arbitrary additive constant.

### 2. Weighted powers

For $r\ne1$, use $\sum_{j=1}^n jr^j=[r-(n+1)r^{n+1}+nr^{n+2}]/(1-r)^2$. For $r=2$, this becomes $(n-1)2^{n+1}+2$. At $r=1$, use $n(n+1)/2$; substituting into the fractional formula is undefined.

### 3. Residue-class coverage

A step adding $d$ requires bases covering every required residue modulo $d$. Adding3 from bases2,3,4 covers all integers at least2. Adding3 from2,5,8 does not: these bases are in one residue class.

### 4. Predecessor dependencies

If the step uses $P(k)$ and $P(k-1)$, prove two consecutive starts and specify where the step begins. For $b_n=b_{n-1}+b_{n-2}$, values $b_0,b_1$ determine every later value. Strong induction grants only predecessors within the stated domain.

### 5. Exponential inequality slack

After doubling a quadratic hypothesis, check $2k^2\ge(k+1)^2$. The step is safe for integer $k\ge3$, but the target $2^n\ge n^2$ fails at3, so the all-future proof starts at4. Step validity and base validity are distinct checks.

### 6. Consecutive representation bases

For pieces4 and5, establish12 through15 and then add4. To establish the least threshold, also prove11 impossible. A construction proves sufficiency; the immediately preceding obstruction proves minimality.

### 7. Divisibility increment

For $a^n-1$ modulo $a-1$, rewrite $a^{k+1}-1=a(a^k-1)+(a-1)$. Both terms are divisible by $a-1$. The base at0 is0, and this identity avoids an unsupported “powers preserve the property” assertion.

### 8. Hockey-stick endpoints

$\sum_{j=r}^{n}\binom jr=\binom{n+1}{r+1}$. The upper index increases by1 and so does the lower index. Derive it by Pascal telescoping; starting the sum later subtracts the omitted lower boundary term.

### 9. Telescoping boundary terms

$1/[j(j+1)]=1/j-1/(j+1)$. From1 through$n$, only1 and $-1/(n+1)$ survive. A different lower limit changes the first survivor. A limit of1 does not mean the finite sum equals1.

### 10. Strengthen a weak hypothesis

If a recursive step needs properties of every prefix or every smaller input, state those quantified properties in the induction claim. The auxiliary claim must have its own base and preservation proof; merely asserting the desired next-stage information is circular.

<!-- BOUNDARY-NOTES -->

### 11. Simultaneous induction

When two recursive claims depend on each other, induct on their conjunction and establish both bases. Proving one next claim may use the other claim at smaller indices, but cannot assume the other next claim without a separate valid dependency argument. A dependency diagram distinguishes mutual induction from a circular same-index proof.

### 12. Minimal counterexample measure

Choose the least counterexample in a nonempty set of nonnegative integer measures. A supposed smaller counterexample must remain in the admissible domain. Positive reals are not well ordered; an argument selecting their least member requires an additional hypothesis.

### 13. Uniform strengthened claims

If deleting a vertex or choosing a smaller object changes the object itself, state the induction hypothesis for every object of that smaller size. A proof about one fixed representative does not justify a recursive step on an arbitrary smaller object.
