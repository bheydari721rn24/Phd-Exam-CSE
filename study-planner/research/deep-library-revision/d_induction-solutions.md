# Individual mathematical solutions for ordinary and strong induction

The retained authentic questions have their original option order. Every answer identifies its parameter domain, establishes the actual mathematical result and distinguishes the relevant alternatives. Prior university readings are reused within the recorded source audit.

## Q1

**Correct option: 2.** The summand counts a subset together with three marked members. Choosing an $i$-element subset of a seven-element set and then three of its members gives $\binom7i\binom i3$. Choosing the marked triple first and the other $i-3$ members from the remaining four gives $\binom73\binom4{i-3}$. Both constructions specify the same object uniquely, so

$$\binom7i\binom i3=\binom73\binom4{i-3}.$$

Set $j=i-3$. The indices $i=3,\ldots,7$ become $j=0,\ldots,4$, including the empty optional subset. Then

$$A=\frac{\binom73}{10}\sum_{j=0}^{4}\binom4j=\frac{35}{10}(1+4+6+4+1)=56.$$

The binomial sum equals $2^4$ because each of the four unmarked elements is independently either present or absent. Thus $30<56\le60$, selecting option 2. The first interval ends below 56, the third begins above it and the fourth begins above 90. Omitting optional elements gives 3.5, which counts a different object; omitting the normalizing factor gives 560.

For $0\le r\le N$, the same reasoning proves $\sum_{i=r}^{N}\binom Ni\binom ir=\binom Nr2^{N-r}$. At $r=N$ the only term is one. At $r=0$ every subset has the unique empty marked set and the answer is $2^N$. These boundary checks explain why neither an extra factorial nor a symmetry divisor belongs in the identity.

## Q2

**Correct option: 1.** Compute the exceptional first step before simplifying the recurrence. It gives $c_1=c_0=1$. For $n\ge1$, the two original equations are

$$c_{n+1}=\sum_{i=0}^{n}c_i,\qquad c_n=\sum_{i=0}^{n-1}c_i.$$

Their difference is $c_{n+1}-c_n=c_n$, hence $c_{n+1}=2c_n$. Induction from $c_1=1$ proves $c_n=2^{n-1}$ for every $n\ge1$. This formula is not the index-zero initial value. The first coefficients make that separation visible.

| Index | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| $c_n$ | 1 | 1 | 2 | 4 | 8 |

In formal power series, geometric inversion gives

$$C(x)=1+\sum_{n=1}^{\infty}2^{n-1}x^n=1+\frac{x}{1-2x}=\frac{1-x}{1-2x}.$$

Thus $\alpha=2$. This formal identity requires no convergence claim; if interpreted as an ordinary real or complex series, it holds for $|x|<1/2$. Expanding the proposed family gives $(1-x)/(1-\alpha x)=1+(\alpha-1)x+\cdots$. The known coefficient $c_1=1$ already forces $\alpha-1=1$, independently eliminating 3,4,5. Starting doubling at zero would instead produce $1,2,4,\ldots$, violating the first original recurrence.

## Q3

**Correct option: 2.** Use the root depth zero, so its available mass is one. A node at depth $d$ has mass $2^{-d}$; each existing child receives half of it. Two children consume the parent mass exactly. One child consumes half, leaving the other half unused. Leaves in different descendant subtrees therefore receive disjoint allocations of the original unit mass.

A precise structural proof covers every finite binary tree. For a root leaf, the sum is $2^0=1$. For a nonleaf root with one subtree $T_1$, the induction hypothesis gives $\alpha(T)=\alpha(T_1)/2\le1/2$. With two subtrees, each child depth is shifted by one, so

$$\alpha(T)=\frac{\alpha(T_1)+\alpha(T_2)}2\le1.$$

These cases are exhaustive because a binary node has at most two children. The smaller-tree hypotheses quantify over all eligible subtree shapes, not only one chosen shape. The root-only tree refutes option 4's strict upper bound. A root with one leaf child has $\alpha=1/2$, refuting option 1's claimed equality. The proved bound refutes option 3.

For a finite tree, equality holds exactly when every internal node has two children: structural equality requires two children and equality in both subtree bounds, recursively. Thus full trees attain one even when their leaves are at different depths. If infinite trees are allowed, every finite collection of leaves still has disjoint unit-mass allocations and the nonnegative infinite sum is at most one; fullness alone need not then force equality. The finite-tree equality characterization must retain its finiteness assumption.

## Q4

**Correct option: 1.** Only parity is requested, so reduce the integer recurrence modulo two. The coefficient reductions $3\equiv5\equiv1$ and $4\equiv0$ give $a_n\equiv a_{n-1}+a_{n-2}\pmod2$. Both specified terms are odd, yielding the following exact state cycle.

| Index | 16 | 17 | 18 | 19 | 20 | 21 |
|---|---:|---:|---:|---:|---:|---:|
| Residue modulo two | 1 | 1 | 0 | 1 | 1 | 0 |

The adjacent-pair transition is $(u,v)\mapsto(v,u+v\bmod2)$. Starting from $(1,1)$, it successively gives $(1,0),(0,1),(1,1)$, so the deterministic state returns after three steps. Induction on the number of cycles now proves repetition; observing three samples alone would not prove it. From these initial indices, even terms have index divisible by three.

The requested inclusive range is 100 through 113. Its multiples of three are 102,105,108,111. Equivalently, $\lfloor113/3\rfloor-\lfloor99/3\rfloor=37-33=4$. This selects option 1. Options 2 and 4 add nonexistent even positions; option 3 treats parity as an equal split, although the proved pattern contains one even term per three, not one per two. The pair of initial parities anchors the phase of the cycle; the period alone would not locate its even indices.

## Q5

**Correct option: 1.** Define $S_n=\sum_{k=1}^{n}k2^{k-1}$. At $n=1$, the sum and candidate $(n-1)2^n+1$ both equal one. Assume this equality at an arbitrary $n\ge1$. The only new summand is $(n+1)2^n$, so

$$S_{n+1}=(n-1)2^n+1+(n+1)2^n=n2^{n+1}+1.$$

The last expression is precisely $((n+1)-1)2^{n+1}+1$, proving the successor and hence the identity for all eligible indices. The hypothesis replaces the old prefix, not the whole next sum. Option 2 already gives two at $n=1$; option 3 gives three there. Option 4 coincides at $n=1$ but gives three at $n=2$, whereas the actual sum is $1+4=5$; one base agreement cannot certify its step.

An independent algebraic derivation uses $2S_n-S_n$. After shifting one of the sums, its unmatched final term is $n2^n$ and its remaining terms contribute $-(2^n-1)$, giving $S_n=(n-1)2^n+1$. The constant one records the lower summation boundary. For an empty sum at $n=0$, both sides are zero, but that extension follows from the stated empty-sum convention; the original positive-index induction is already complete.

## Q6

**Correct option: 4.** A step from $n$ to $n+4$ preserves the residue of the index modulo four. Starting with 3 alone therefore reaches $3,7,11,\ldots$ and supplies no premise for the chain through 4,5 or6. The four bases 3,4,5,6 start all four residue classes.

For any target $t\ge3$, integer division of $t-3$ gives a unique $q\ge0$ and $r\in\{0,1,2,3\}$ with $t=3+r+4q$. The base is $3+r$. Induction on $q$ using the stated transition establishes the target. Every invoked predecessor is at least three, so the rule is used within its domain.

| Base | Residue | First reachable values |
|---:|---:|---|
| 3 | 3 | 3,7,11 |
| 4 | 0 | 4,8,12 |
| 5 | 1 | 5,9,13 |
| 6 | 2 | 6,10,14 |

To prove necessity for this rule, define $P(t)$ to be true exactly in the residue classes represented by a proposed smaller base set. Every provided base is then true and every implication $P(t)\Rightarrow P(t+4)$ is true, but an omitted class remains false. This supplies actual countermodels to options 1,2,3. Strong induction cannot infer an omitted base from a premise that never reaches its class; a different valid transition could change the required bases, but none is supplied here.

## Q7

**Correct option: 1.** For the first assertion, the base $n=0$ gives $5^0-1=0$, divisible by eight. Suppose $5^{2n}-1=8t$ for an integer $t$. Then

$$5^{2(n+1)}-1=25(5^{2n}-1)+24=8(25t+3).$$

The last bracket is an integer, so the step explicitly constructs the required quotient. Induction proves the assertion for every $n\ge0$. Equivalently, $5^2\equiv1\pmod8$ and taking its nonnegative powers preserves that residue. This congruence argument includes the zero exponent.

Option 2 fails at $n=1$, because $5-1=4$ is not divisible by eight. Option 3 fails there because $5^2-1=24$ is not divisible by sixteen. Option 4 fails at $n=0$, where its expression is two, not a multiple of three. These are admissible counterexamples, not merely insufficient attempts at proof.

The successor adds a term divisible by eight; merely writing $5^{2n}-1\equiv0$ and multiplying the *whole desired expression* by 25 would miss the extra 24. The exact factorization shows both the use of the induction hypothesis and the new boundary correction. Negative exponents are outside the stated integer-expression domain and are not covered by the proof.

## Q8

**Correct option: 2.** The original recurrence first gives $u_1=u_0=2$. From the two neighboring prefix equations, valid for $n\ge1$, subtract to obtain $u_{n+1}-u_n=u_n$. Thus $u_{n+1}=2u_n$ starts at the positive index one, not zero.

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $u_n$ | 2 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 |

Induction on positive indices proves $u_n=2\cdot2^{n-1}=2^n$. Substituting eight gives 256. Option 1 stops one doubling early. Option 3 starts doubling immediately from $u_0$ and produces $2\cdot2^8=512$, although that false sequence already violates $u_1=2$. Option 4 makes another unnecessary doubling.

The derived formula would give one at zero, contradicting the actual initial value two. That is no defect in the proof, because its domain is $n\ge1$. A recurrence transformation can have a narrower range than the original recurrence. Always retain its first valid transition and compute the seed from the original equation before propagating a simplified rule.

## Q9

**Correct option: 3.** The first few exact comparisons identify both failures and equalities, but the tail still needs a proof.

| $n$ | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| $2^n$ | 2 | 4 | 8 | 16 | 32 |
| $n^2$ | 1 | 4 | 9 | 16 | 25 |
| Strict inequality? | Yes | No | No | No | Yes |

For arbitrary $n\ge5$, $2n^2-(n+1)^2=n^2-2n-1=(n-1)^2-2>0$. If $2^n>n^2$, doubling gives $2^{n+1}>2n^2>(n+1)^2$. The verified base at five and this universal step prove the inequality for every $n\ge5$.

At four there is equality, so no threshold at most four can make the strictly greater relation true on its entire tail. Thus five is the smallest. Options 1 and2 include the failed index four, whereas option 4 is sufficient but not minimal. Truth at one does not imply that the whole early interval is a valid base: the step's positive-slack condition is unavailable there. Asymptotic exponential dominance establishes eventual growth but does not by itself identify this exact threshold.

## Q10

**Correct option: 2.** Let $I=17$ count internal nodes and let $L$ count leaves. Each internal node has exactly three children, so the number of parent-child edges is $3I$. Independently, every node except the root has one parent, so a finite rooted tree with $I+L$ nodes has $I+L-1$ edges. Equating these counts gives

$$3I=I+L-1,\qquad L=2I+1=35.$$

The root-only base has $I=0,L=1$. Replacing a leaf by an internal node with three new leaf children changes $I$ by one and $L$ by two, preserving the formula inductively. Every finite full ternary tree can be built this way, or proved by structural induction on its three subtrees. A missing child would invalidate the first edge count.

Option 1 omits the root-only constant and gives $2I=34$. Option 3 adds a nonexistent extra constant. Option 4, $3I=51$, counts edges rather than leaves: the total node count is 52, of which seventeen are internal and thirty-five are leaves. Neither balance nor equal leaf depth is required. The formula concerns branching at each internal node and finiteness, not a fixed geometric tree shape.

## Q11

**Correct option: 1.** Two initial values are required because the recurrence uses two predecessors. The proposed formula $a_n=n+2$ gives $a_0=2$ and $a_1=3$, both correctly. Suppose it holds at the two indices $n-1,n-2$ for an arbitrary $n\ge2$. Then

$$a_n=2[(n-1)+2]-[(n-2)+2]=2(n+1)-n=n+2.$$

Strong induction, or ordinary induction on the pair of consecutive assertions, now proves the formula for every $n\ge0$. A proof using only the hypothesis at $n-1$ would leave the second predecessor unproved.

Subtract adjacent sequence values to obtain $a_n-a_{n-1}=a_{n-1}-a_{n-2}$. The first difference is $a_1-a_0=1$, so all differences are one; telescoping yields $a_n=2+n$. This is an independent explanation of why the sequence is linear.

Option 2 gives three instead of two at zero. Option 3 gives zero there. Option 4 matches the two bases but fails the next recurrence: it proposes $a_2=6$, while the recurrence requires $2\cdot3-2=4$. Agreement at all initial indices does not excuse failure of the transition. The recurrence plus both initial values determines each later term uniquely.

## Q12

**Correct option: 2.** Count a subset of an eight-element set with two marked members. Selecting the subset size $k$ first gives $\binom8k\binom k2$. Selecting the marked pair first gives $\binom82=28$ choices, followed by any subset of the remaining six elements, giving $2^6=64$ choices. Thus

$$\sum_{k=2}^{8}\binom8k\binom k2=28\cdot64=1792.$$

Algebraically, factorial cancellation proves $\binom8k\binom k2=\binom82\binom6{k-2}$; changing index and summing the binomial coefficients gives the same result. The marked pair is unordered, which is why its count is $\binom82$, not $8\cdot7$.

Option 1, 896, removes half of the objects without a symmetry identification in the stated model. Option 3,3584, instead orders the two marked members. Option 4,28, keeps only the marked pair and omits all optional subset choices. The lower index two is necessary for two marks to exist; its term counts a subset consisting only of those marks. The upper term counts the whole eight-element set with any marked pair. The endpoints are genuine objects and cannot be deleted from the sum.

## Q13

**Correct option: 2.** The five exact summands and successive prefixes are:

| $k$ | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| $k2^{k-1}$ | 1 | 4 | 12 | 32 | 80 |
| Prefix sum | 1 | 5 | 17 | 49 | 129 |

Thus the requested sum is 129. These values also instantiate the proved general formula $S_n=(n-1)2^n+1$: at five it gives $4\cdot32+1=129$. Its inductive successor adds $(n+1)2^n$, converting $(n-1)2^n+1$ to $n2^{n+1}+1$, the same formula at the next index. The new term is multiplied by its index; it is not merely the next power of two.

Option 1,31, sums $1+2+4+8+16$ and omits the weights. Option 3,160, uses $n2^n$ and differs from the correct value by $2^n-1=31$. Option 4,191, uses $(n+1)2^n-1$ and differs by $2^{n+1}-2=62$. Neither an approximate leading term nor a near value answers an exact finite sum. The smallest base $S_1=1$ and the exact increment both certify the general formula; the displayed five terms independently verify this particular requested value.

## Q14

**Correct option: 1.** Instead of assuming a formula from the earlier numerical example, derive it through a shifted subtraction. Multiplication of $S_n$ by two shifts each power up by one. Aligning the two finite sums and subtracting leaves

$$2S_n-S_n=n2^n-\sum_{j=0}^{n-1}2^j=n2^n-(2^n-1).$$

Hence $S_n=(n-1)2^n+1$. At $n=8$, this is $7\cdot256+1=1793$. Direct prefix accumulation yields $1,5,17,49,129,321,769,1793$, confirming the endpoint and the inclusion of the eighth term $8\cdot128=1024$.

Option 2,2048, counts $8\cdot256$ and neglects the subtracted geometric boundary. Option 3,2303, adds rather than reconciles that boundary. Option 4,255, is the unweighted geometric sum and ignores all factors $k$. The subtraction is between finite sums, so aligning terms is legitimate. No infinite-series rearrangement is used, and the resulting constant one cannot be dropped in an exact answer even though it is negligible in asymptotic growth.

## Q15

**Correct option: 4.** Let $F(n)=(n-1)2^n+1$. First verify $F(1)=1=S_1$. For every $n\ge1$, compute its difference explicitly:

$$F(n+1)-F(n)=n2^{n+1}-(n-1)2^n=(n+1)2^n.$$

That is exactly $S_{n+1}-S_n$. Thus if $S_n=F(n)$, the equal increments imply $S_{n+1}=F(n+1)$, proving the formula for every positive integer. This argument gives a complete induction rather than promoting agreement at $n=5,8$ to a theorem.

Option 1 already gives two instead of one at the first index. Option 2 gives three there. Option 3 passes the first index but gives $2^2-1=3$ at the second, while the actual sum is five. It has increment $2^n$, lacking the factor $n+1$ required by the summand. The correct expression also extends to $n=0$ under an empty-sum convention: $(-1)\cdot1+1=0$. An extension to negative or noninteger indices is not supplied by this finite-index definition or by integer induction.

## Q16

**Correct option: 3.** The constant one belongs to the exact identity and must survive the successor calculation. Starting from $S_n=(n-1)2^n+1$ and adding $(n+1)2^n$ gives $n2^{n+1}+1$, not merely its exponential term. Dropping one produces a formula whose base already fails.

Option 1 is circular: assuming $S_{n+1}=n2^{n+1}+1$ while proving that same equality supplies the desired result as an unproved premise. Option 2 is refuted by changing the lower limit to two. Removing the first term gives $\sum_{k=2}^{n}k2^{k-1}=S_n-1=(n-1)2^n$, with a different constant. Option 4 is refuted by any candidate that passes one index and changes its later increments, such as $2^n-1$.

More generally, for $1\le m\le n$, subtract the prefix through $m-1$:

$$\sum_{k=m}^{n}k2^{k-1}=(n-1)2^n-(m-2)2^{m-1}.$$

Both surviving boundaries have mathematical meaning. Equal differences do not identify a sequence without one initial value: adding an arbitrary constant to a candidate leaves every difference unchanged. A complete exact-sum proof therefore checks both the increment and the starting boundary, even if a requested numerical answer is at a large index.

## Q17

**Correct option: 3.** The exact square terms are $1,4,9,16,25$, whose sum is 55. A table makes their accumulation and the last term visible.

| Index | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| Square | 1 | 4 | 9 | 16 | 25 |
| Prefix | 1 | 5 | 14 | 30 | 55 |

For the general candidate $F(n)=n(n+1)(2n+1)/6$, the base is $F(1)=1$. Its successor satisfies

$$F(n)+(n+1)^2=\frac{(n+1)[n(2n+1)+6(n+1)]}{6}=\frac{(n+1)(n+2)(2n+3)}6.$$

The second equality uses $2n^2+7n+6=(n+2)(2n+3)$ and closes the inductive step. At five, $5\cdot6\cdot11/6=55$. Option 1,125, uses the cube of the upper index, not a sum of squares. Option 2,35, evaluates $n(n+1)(n+2)/6$, the wrong polynomial. Option 4,15, sums the unsquared indices. The direct enumeration checks this instance; the base and factored successor prove the identity for every eligible index.

## Q18

**Correct option: 2.** A second derivation uses the exact cube difference $(k+1)^3-k^3=3k^2+3k+1$. Sum this identity for $k=1,\ldots,n$. The left side telescopes to $(n+1)^3-1$, while the right side is $3S_n+3n(n+1)/2+n$. Solving for the square sum gives

$$S_n=\frac{(n+1)^3-1-3n(n+1)/2-n}{3}=\frac{n(n+1)(2n+1)}6.$$

At eight, the value is $8\cdot9\cdot17/6=204$. The individual squares $1,4,9,16,25,36,49,64$ add to the same total, so the closed-form substitution has an independent numerical check.

Option 1,120, substitutes into the wrong polynomial $n(n+1)(n+2)/6$. Option 3,36, sums the indices rather than their squares. Option 4,512, cubes the upper limit. Those are not alternative representations of the same sum. The cube-difference derivation requires the exact linear sum including its endpoints; replacing it by a leading asymptotic term would lose the quadratic and linear terms of this exact answer.

## Q19

**Correct option: 1.** Define $F(n)=n(n+1)(2n+1)/6$. Its initial value is $F(1)=1$. To verify every successor, subtract the neighboring values:

$$F(n+1)-F(n)=\frac{(n+1)[(n+2)(2n+3)-n(2n+1)]}{6}=(n+1)^2.$$

The bracket reduces to $6n+6$, so the result is exactly the new square summand. Induction now proves $\sum_{k=1}^{n}k^2=F(n)$ for all positive integers. The polynomial expands as $n^3/3+n^2/2+n/6$, displaying the lower-order terms that distinguish an exact answer from a growth estimate.

Option 2 is the linear-index sum; it already gives three instead of five at two. Option 3 gives eight there. Option 4 gives four there. Coincidence of all four candidates at $n=1$ is therefore insufficient to choose a universal formula. Under the empty-sum convention the correct formula also gives zero at zero, whereas its proof still requires only the stated positive starting case. The denominator six divides the numerator because the expression counts an integer sum, but integrality alone would not identify the correct polynomial.

## Q20

**Correct option: 4.** A proposed closed form is certified when it has the correct initial value and its consecutive difference equals the summand. For $F(n)=n(n+1)(2n+1)/6$, the factorization in the preceding answer gives $F(n+1)-F(n)=(n+1)^2$. Telescoping these differences from one to $n$ yields $F(n)=1+\sum_{k=2}^{n}k^2$, which is the required sum.

Option 1 drops $n^2/2+n/6$ from the exact expression. At $n=1$ the leading term $n^3/3$ is one third, not the sum one. Option 2 would permit unproved indices or undefined sums: integer induction does not establish the original finite sum at a negative or noninteger upper limit. Option 3 mistakes a bounded polynomial degree for evidence of equality; the zero polynomial has small degree but is not this sum.

The initial value must accompany the factored difference. $F(n)+7$ has the same successor difference as $F(n)$ but is wrong by seven at every index. Thus the correct option describes a method whose complete proof still includes its starting boundary. A low-degree conjecture can be discovered by fitting values, but proving the identity requires a justified uniqueness argument or the explicit difference-and-base proof above.

## Q21

**Correct option: 4.** The factor $k$ counts the choices of a distinguished member within a $k$-element subset. The weighted sum therefore counts pairs $(S,u)$ with $u\in S$ on a five-element universe.

| Subset size $k$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| Subsets $\binom5k$ | 1 | 5 | 10 | 10 | 5 | 1 |
| Marked pairs $k\binom5k$ | 0 | 5 | 20 | 30 | 20 | 5 |

The bottom row sums to 80. Alternatively, choose the distinguished element in five ways, then choose an arbitrary subset of the remaining four elements in $2^4$ ways; the chosen member is included automatically. Hence $5\cdot16=80$.

Option 1,32, counts subsets without a mark. Option 2,160, uses two choices for the marked element's membership even though it must be present. Option 3,120, counts permutations of all five elements, a different object. The empty subset contributes zero, not one, because it has no distinguished member. Distinct markings of the same nonempty subset are distinct counted pairs, exactly as the weight $k$ specifies.

## Q22

**Correct option: 3.** For each possible marked element of an eight-element universe, the other seven elements have independent membership choices. This gives $8\cdot2^7=1024$ pairs $(S,u)$ with $u\in S$. Counting instead by the size of $S$ gives the defining weighted binomial sum.

The factorial identity $k\binom8k=8\binom7{k-1}$, for $k\ge1$, verifies the correspondence algebraically. Thus

$$\sum_{k=0}^{8}k\binom8k=8\sum_{j=0}^{7}\binom7j=8(1+1)^7=1024.$$

The zero-index term vanishes before the index change. Option 1,2048, allows the marked element to be absent, doubling every valid construction. Option 2,40320, imposes an ordering of all eight elements that the subset-member object does not possess. Option 4,256, ignores the distinction among the marks within each subset.

For an optional analytic cross-check, differentiating $(1+x)^8=\sum_k\binom8k x^k$ and setting $x=1$ gives $8\cdot2^7$. This is a polynomial identity, so no infinite-series convergence is involved. The combinatorial proof establishes the result without requiring differentiation and explains why the marked membership is fixed rather than another independent binary choice.

## Q23

**Correct option: 2.** For $n\ge1$, choosing a marked element first gives $n$ choices; each other element may be included or excluded, giving $2^{n-1}$. This is a bijection onto the pairs counted by $\sum_{k=0}^{n}k\binom nk$, so the answer is $n2^{n-1}$.

An explicit induction uses Pascal's identity with out-of-range coefficients set to zero. If $T_n$ denotes the weighted sum, then

$$T_{n+1}=\sum_k k\binom nk+\sum_k k\binom n{k-1}=T_n+(T_n+2^n).$$

In the second sum, put $j=k-1$ and split $j+1$ into its two terms. The base $T_1=1$ and hypothesis $T_n=n2^{n-1}$ now yield $T_{n+1}=2n2^{n-1}+2^n=(n+1)2^n$, the required next formula.

Option 1 counts permutations; at $n=3$ it gives six instead of twelve. Option 3 counts unmarked subsets and fails at $n=1$, giving two instead of one. Option 4 doubles the required count by freeing the marked membership. This successor proof explains how the binomial coefficient family, not just the numerical expression, changes with the induction parameter.

## Q24

**Correct option: 1.** At $n=0$ there is one subset, the empty set, but no subset-member pair. The defining weighted sum is $0\binom00=0$. The selected-member construction used for $n\ge1$ cannot be performed on an empty universe, so this boundary should be evaluated directly. As a real numerical expression, $0\cdot2^{-1}$ also equals zero; that does not make $2^{-1}$ a count of subsets of a negative-size set.

Option 2 fails for a two-element subset, which has two possible distinguished members. Option 3 confuses the unweighted contribution $\binom00=1$ with the weighted contribution zero. Option 4 rejects a valid bijective double count; both orders determine exactly the same pair $(S,u)$ and give inverse constructions.

The distinction is between an algebraic formula's numerical extension and its combinatorial proof's domain. A proof relying on selecting an element needs a nonempty universe, whereas the empty weighted sum has its own exact evaluation. Checking this boundary also prevents incorrectly multiplying the unweighted subset total by one uniform number of marks: the number of marks varies with $|S|$, which is why the original sum has the weight $k$.

## Q25

**Correct option: 2.** In a finite full binary tree, every internal node has exactly two children. With $I=5$ internal nodes, there are $2I=10$ parent-child edges. Every nonroot vertex has exactly one parent, so the total number $N$ of vertices is one more than the edge count: $N=11$.

The number of leaves is $L=N-I=6$. Option 3 counts those leaves alone. Option 4 counts the edges and omits the root. Option 1,31, is the total size of a perfect tree with four edge levels; the parameter here counts internal nodes, not height. Fullness does not require all leaves to share a depth.

For a structural proof, the root-only tree has $(I,N)=(0,1)$. Joining two full subtrees beneath a new internal root gives $I=1+I_1+I_2$ and $N=1+N_1+N_2$. Substituting the two hypotheses $N_j=2I_j+1$ gives $N=2(1+I_1+I_2)+1=2I+1$. This closes the construction for every finite full shape, rather than assuming a particular balanced picture. The identities fail for a one-child chain, where internal nodes do not each create two edges.

## Q26

**Correct option: 1.** Eight internal nodes supply sixteen child edges. Since every nonroot node contributes exactly one edge from its parent, the total node count is $16+1=17$. There are then $17-8=9$ leaves.

One can build a full binary tree by repeatedly expanding a leaf into an internal node with two leaf children. Each expansion adds one internal node and two total nodes: it retains the old vertex and creates two children. Starting from one root vertex, eight expansions give $1+8\cdot2=17$, independently verifying the edge count. Any finite full tree has a deepest internal node whose leaf children can be collapsed, so reversing this operation reduces to the base and justifies the construction for all shapes.

Option 2,9, gives the leaf count rather than the requested total. Option 3,16, gives the edge count. Option 4,255, uses $2^8-1$, the total for a perfect tree with eight vertex levels, and has no basis in the given internal-node count. The tree may be balanced or elongated; both construction and edge accounting give the same total because they depend on fullness and finiteness, not on a height assumption.

## Q27

**Correct option: 4.** Let $I=n$ and let $L$ be the leaves. Counting the same edges by their parents and by their nonroot children gives $2n=n+L-1$. Hence $L=n+1$ and the requested total is $N=n+L=2n+1$.

Equivalently, induct on the tree constructor. A root leaf has $I=0,N=1$, satisfying the formula. For a new root with full subtrees $T_1,T_2$, their internal counts are smaller and the hypothesis gives $N_j=2I_j+1$. Then

$$N=1+N_1+N_2=2(I_1+I_2+1)+1=2I+1.$$

Both subtrees are needed; a hypothesis covering only one selected shape of size $I_j$ would not justify either arbitrary recursive child. Option 1 counts leaves. Option 2 counts edges. Option 3 confuses internal count with an exponential depth formula and already gives one at $n=1$ instead of the three nodes of a root with two leaf children.

At zero internal nodes, the valid base is one root leaf and the formula gives one. The original positive-parameter question uses $n\ge1$, but the structural proof must still include this smaller root-leaf object because it occurs as a child subtree.

## Q28

**Correct option: 3.** Fullness requires exactly two children at every internal node. Perfection also requires equal leaf depth, and balance imposes additional height conditions. These are different properties. A full comb is built by giving each continuing internal node one leaf child and one continuing child, until the final internal node has two leaf children. With $n$ internal nodes, it has height $n$ and total $2n+1$ nodes.

For $n=3$, the comb has leaf depths $1,2,3,3$, whereas the perfect tree with three internal nodes has four leaves at depth two. Both have seven total nodes, proving that equal node counts do not determine the shape or height. Option 2 is thereby refuted. Option 4 is refuted by the whole comb family: its height grows linearly with $n$, not logarithmically. Option 1 directly contradicts the full binary constructor, whose internal nodes have two children.

The height bound for arbitrary finite full binary trees with $n$ internal nodes is $\lceil\log_2(n+1)\rceil\le h\le n$. The lower bound comes from at most $2^h-1$ internal nodes in height $h$; the upper bound comes from distinct internal nodes along a longest root-leaf path. The comb attains the upper bound. Thus the node formula does not authorize a balanced-tree running-time bound without additional structural assumptions.

## Q29

**Correct option: 2.** Partial fractions give the exact identity $1/[k(k+1)]=1/k-1/(k+1)$ for every positive integer $k$. At five, write the finite cancellation explicitly:

$$\left(1-\frac12\right)+\left(\frac12-\frac13\right)+\left(\frac13-\frac14\right)+\left(\frac14-\frac15\right)+\left(\frac15-\frac16\right)=1-\frac16=\frac56.$$

Every interior fraction occurs once with each sign; the first positive term and last negative term have no partners. Option 1,5, replaces every summand by one. Option 3, $1/6$, retains only the final boundary magnitude and drops the initial one. Option 4, $5/7$, uses a denominator corresponding to the wrong terminal index.

For a successor check, assume the prefix through $n$ equals $n/(n+1)$. Adding the next term gives

$$\frac{n}{n+1}+\frac{1}{(n+1)(n+2)}=\frac{n(n+2)+1}{(n+1)(n+2)}=\frac{n+1}{n+2}.$$

The numerator is $(n+1)^2$; positive denominators justify the cancellation. The base at one is $1/2$, so both direct telescoping and induction prove the requested finite-sum value. Cancellation never means that each original positive term was zero.

## Q30

**Correct option: 1.** Sum the partial fractions through eight. The middle terms cancel and the surviving endpoints are $1$ and $-1/9$, giving $8/9$. The upper denominator is nine because the eighth summand contains $(8+1)$, not because another summand was added.

The exact prefixes illustrate the denominator pattern:

| Upper index | 1 | 2 | 3 | 4 | 8 |
|---|---|---|---|---|---|
| Partial sum | $1/2$ | $2/3$ | $3/4$ | $4/5$ | $8/9$ |

Option 2, $1/9$, is the remainder from the limiting total one, not the requested partial sum. Option 3, $4/5$, is the partial sum through four and omits the last four positive terms. Option 4,8, treats each reciprocal product as one. The answer lies strictly between zero and one, as the formula and term positivity require.

The infinite limit is one because $1/(n+1)$ tends to zero, and the exact tail after index eight is $1/9$. This conclusion follows *after* finite telescoping. Writing the sum as the difference of two separately divergent harmonic series is not a legitimate subtraction of finite real limits. Retaining the same finite upper endpoint until cancellation is complete avoids that ambiguity.

## Q31

**Correct option: 4.** For every $n\ge1$, partial fractions and finite cancellation give

$$\sum_{k=1}^{n}\frac{1}{k(k+1)}=\sum_{k=1}^{n}\left(\frac1k-\frac{1}{k+1}\right)=1-\frac{1}{n+1}=\frac{n}{n+1}.$$

For an induction proof, the base is $1/2$. The exact successor calculation $n/(n+1)+1/[(n+1)(n+2)]=(n+1)/(n+2)$ proves the same identity at the next index. Every denominator is nonzero because the indices are positive. The two methods establish the full domain, not only the numerical samples.

Option 1 keeps the tail instead of the partial sum; it accidentally agrees at $n=1$ but gives $1/3$ rather than $2/3$ at two. Option 2 shifts the last denominator one step too far and fails at one. Option 3 discards the reciprocals and gives one instead of one half at one. For a shifted interval $1\le m\le n$, the same finite cancellation yields $\sum_{k=m}^{n}1/[k(k+1)]=1/m-1/(n+1)$. Both starting and ending boundaries must be adjusted when the summation domain changes.

## Q32

**Correct option: 3.** The summands are positive and nonzero, but their partial-fraction *components* cancel across neighboring indices. For a finite upper limit, every cancellation occurs in a finite algebraic expression. The unmatched endpoints remain $1-1/(n+1)$, so the method is fully justified before a limit is taken.

Option 1 fails already at $k=1$, whose original summand is $1/2$. Option 2 predicts zero, contradicted by that same one-term sum. Option 4 would subtract two divergent harmonic series as though each had a finite value. With matched finite cutoffs their difference tends to one; with the first sum taken through $2n$ and the second through $n$, the difference is

$$\sum_{k=n+1}^{2n}\frac1k+1-\frac{1}{n+1},$$

which stays larger than $1-1/(n+1)+1/2$. Thus changing the cutoff convention changes the result and demonstrates why an unspecified difference of divergent series has no justified cancellation value.

For this particular nonnegative original series, the finite partial sums have the explicit increasing bound below one and their limit is one. The convergence conclusion comes from those partial sums, not from assigning values to the divergent component series. State the finite identity first, then the limiting operation and its assumptions.

## Q33

**Correct option: 4.** The recurrence has $H_0=0$ and $H_n=2H_{n-1}+1$ for $n\ge1$. Its first exact values are:

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| $H_n$ | 0 | 1 | 3 | 7 | 15 | 31 |

Set $B_n=H_n+1$. The recurrence becomes $B_n=2B_{n-1}$ with $B_0=1$. Induction gives $B_n=2^n$, hence $H_n=2^n-1$ and $H_5=31$. This change of variable accounts for the added central operation exactly instead of neglecting it.

Option 1,32, counts $B_5$ rather than $H_5$. Option 2,25, squares the disk count and violates the recurrence; for instance the proposed quadratic gives four at two instead of three. Option 3,15, is $H_4$ and omits one full recurrence level. In the standard three-peg Hanoi model, this recurrence comes from two transfers of four smaller disks and one move of the largest disk. Solving the supplied recurrence gives its exact value; proving that it describes a *minimum* additionally requires the construction and lower-bound argument developed in the boundary question.

## Q34

**Correct option: 3.** Expand the recurrence recursively without assuming its solution:

$$H_n=2(2H_{n-2}+1)+1=4H_{n-2}+3.$$

After $j$ expansions the expression is $2^jH_{n-j}+(2^j-1)$, proved by induction on $j$. Taking $j=n$ uses $H_0=0$ and gives $2^n-1$. At eight, $2^8-1=255$.

Option 1,64, uses $n^2$ and is incompatible with the exact successor rule. Option 2,127, is the preceding term $H_7$. Option 4,256, keeps the transformed doubling count but omits subtracting one. At the last step the actual arithmetic is $H_8=2H_7+1=2\cdot127+1=255$, independently checking the answer.

The expansion formula includes both the multiplied seed and the accumulated constant. If the initial value were $H_0=b$, the solution would instead be $H_n=(b+1)2^n-1$. Therefore the initial zero is an essential part of the result. A solution of the recurrence cannot be carried unchanged to an altered base simply because the successor expression looks identical.

## Q35

**Correct option: 2.** The base $H_0=0=2^0-1$ holds. Assuming $H_{n-1}=2^{n-1}-1$ at the predecessor gives

$$H_n=2(2^{n-1}-1)+1=2^n-1.$$

This establishes every positive successor and hence all nonnegative indices. Alternatively, $H_n+1=2(H_{n-1}+1)$ is pure doubling from the unit seed, providing the same formula.

Option 1 shifts the index and already gives zero at one rather than the actual one. Option 3 omits the constant correction and violates the zero base. Option 4, $n^2$, agrees at one but gives four at two, whereas the recurrence gives three. Those agreements are not universal solutions.

For the standard Hanoi construction, the predicate must state correctness for every distinct source-target peg pair, with the remaining peg auxiliary. Otherwise a hypothesis about transfer from the original source to the original target does not justify the first recursive transfer to the auxiliary peg. The algebra proves the move count once the recurrence is established. Correctness of the legal moves and optimality among all legal procedures are additional obligations, not consequences of a formula's appearance.

## Q36

**Correct option: 1.** A legal construction supplies an upper bound: move the $n-1$ smaller disks from source to auxiliary, move the largest from source to target, then move the smaller stack to target. With the generalized peg-pair hypothesis, these transfers are legal and use $2H_{n-1}+1$ moves.

For the standard three-peg puzzle, a lower bound can also be proved. Before the largest disk's **first** move, every smaller disk must have left its original peg and must be on the one peg other than that move's source and destination. That prefix requires at least the minimum $H_{n-1}$ moves to transfer the smaller stack. After the largest disk's **last** move to the final target, all smaller disks are again together on the remaining peg and must be moved onto that target, requiring at least another $H_{n-1}$ moves. These two disjoint stages plus at least one largest-disk move give a lower bound $2H_{n-1}+1$, even if a proposed solution moves the largest disk more than once. The construction attains it, so the recurrence genuinely represents the minimum.

Option 2 falsely treats a legal but wasteful recursive procedure as optimal; adding two reversible small-disk moves to a legal solution preserves legality but increases its cost. Option 3 omits the unavoidable largest-disk move and would incorrectly give zero for one disk. Option 4 is refuted by the proved inductive lower bound and by the earlier exponential-versus-square inequality. A recurrence solution alone establishes neither an unproved model nor optimality; the matched upper and lower bounds close those obligations for the declared three-peg rules.

## Q37

**Correct option: 1.** A full ternary tree with five internal nodes has $3\cdot5=15$ edges, because each internal node contributes three outgoing edges. Its total nodes are sixteen, since a finite tree has one more vertex than edges. Removing the five internal nodes leaves eleven leaves.

The structural construction checks the same arithmetic. Starting from a root leaf, replace a leaf by an internal node with three leaf children. Each expansion increases the internal count by one and the leaf count by two: one old leaf is removed from the leaf classification, then three are added. Five expansions give $L=1+5\cdot2=11$.

Option 2,16, counts all vertices. Option 3,6, uses the binary-tree leaf formula $I+1$ instead of the ternary branching rule. Option 4,10, omits the original root-leaf constant. Every finite full ternary shape can be reduced by collapsing a deepest internal node with its three leaf children, so the expansion argument is not confined to a balanced example. Missing children change the edge count and must not be admitted under the word “full.”

## Q38

**Correct option: 4.** With $I=8$, the edge count is 24 and total node count is 25. Therefore $L=25-8=17$. Directly, $3I=I+L-1$ gives $L=2I+1=17$.

For structural induction, if the three child subtrees have internal counts $I_1,I_2,I_3$, their leaf counts are $2I_j+1$. The new root is internal and adds no leaf, so

$$L=(2I_1+1)+(2I_2+1)+(2I_3+1)=2(1+I_1+I_2+I_3)+1=2I+1.$$

The root-only base has $I=0,L=1$ and is eligible as a child in the construction. At eight this gives the requested seventeen. Option 1,25, counts all nodes. Option 2,9, uses the binary leaf formula. Option 3,16, drops the base constant.

The induction hypotheses range over every finite full ternary subtree, including root leaves. Treating each subtree as necessarily nonempty in its *internal-node count* would exclude those base objects and break the first construction. Subtree shape and relative height need not agree: the count depends only on the three-child constructor and the combined internal counts.

## Q39

**Correct option: 3.** In any finite full ternary tree, parent counting gives $3n$ edges, and child counting gives $n+L-1$. Hence $L=2n+1$. This establishes the answer for every eligible internal-node count without assuming equal leaf depth.

The more general full $m$-ary identity is

$$mI=I+L-1,\qquad L=(m-1)I+1.$$

For a structural proof, the root-leaf base has one leaf. Combining $m$ subtrees adds one internal root and sums the $m$ leaf counts; inserting their hypotheses gives the displayed formula. When $m=3$ it becomes exactly the selected expression.

Option 1 uses $m=2$ and fails at one internal ternary node, whose three children are all leaves. Option 2 omits the constant and gives two instead of three there. Option 4 counts total nodes $3n+1$, not leaves. The zero-internal-node base also gives one, consistent with $2n+1$. The generic identity requires an exact child count at every internal node; replacing that by “at most $m$ children” supports a bound, not the same equality.

## Q40

**Correct option: 2.** The proof uses $E=3I$, so it requires exactly three child edges from each internal node. A one-child chain with $I$ internal nodes has only one leaf, not $2I+1$, explicitly refuting option 3's proposed extension. The root-only leaf is the zero-internal-node base and refutes option 4's exclusion.

Option 1 asserts that height alone fixes the leaf count. At height two, a full ternary tree with one expanded child of the root has $I=2,L=5$, whereas expanding all three root children gives $I=4,L=9$. Both have longest root-leaf path length two but different numbers of leaves. Thus height is not sufficient data for this formula.

There is an exact correction for variable child counts. If $d(v)$ is the number of children of internal vertex $v$, every edge is counted once in $\sum_v d(v)$, so

$$L=1+\sum_{v\ \mathrm{internal}}(d(v)-1).$$

For a ternary full tree every summand equals two; for a one-child chain every summand is zero. This derivation shows precisely which part of the original equality changes when the branching assumption changes. It does not replace the model by a vague claim that the formula “usually” depends on fullness.

## Q41

**Correct option: 1.** The exceptional first positive term is $a_1=2+a_0=3$. For $n\ge1$, subtract the equations for $a_{n+1}$ and $a_n$:

$$a_{n+1}-a_n=\left(2+\sum_{j=0}^{n}a_j\right)-\left(2+\sum_{j=0}^{n-1}a_j\right)=a_n.$$

Thus $a_{n+1}=2a_n$ after the seed three. The values at indices zero through five are $1,3,6,12,24,48$, so the answer is 48. The closed form $3\cdot2^{n-1}$ applies for $n\ge1$ and gives the same endpoint.

Option 2,32, uses a unit doubled seed and violates $a_1=3$. Option 3,243, changes the derived multiplier from two to three. Option 4,63, counts a different accumulated geometric family; it already gives three at one but seven at two, where the original recurrence gives $2+1+3=6$. One correct seed is insufficient if the successor is wrong. The prefix recurrence and the subtractive simplification both specify their initial ranges explicitly.

## Q42

**Correct option: 4.** Eight positive indices contain seven doublings after the established first term $a_1=3$. Hence $a_8=3\cdot2^7=384$. A prefix table independently confirms the recurrence through every required index.

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $a_n$ | 1 | 3 | 6 | 12 | 24 | 48 | 96 | 192 | 384 |

For an original-recurrence check, $2+\sum_{j=0}^{7}a_j=2+1+3(1+2+4+8+16+32+64)=3+3\cdot127=384$. This verifies the full prefix condition, not just the simplified doubling rule.

Option 1,256, discards the exceptional seed and gives $2^8$. Option 2,6561, uses $3^8$, the wrong multiplier. Option 3,511, uses $2^9-1$, which agrees at the first positive index but fails the second and every later original recurrence. The expression $3\cdot2^{n-1}$ must not be extended backward to the prescribed index zero, where it would give $3/2$ instead of one. Computing the original seed before simplifying prevents this systematic boundary error.

## Q43

**Correct option: 3.** First prove $a_1=3$. The subtractive recurrence gives $a_{n+1}=2a_n$ for $n\ge1$, so ordinary induction proves $a_n=3\cdot2^{n-1}$ throughout the positive domain.

A strong-induction verification uses the original prefix equation directly. Assume the formula at every earlier positive index. For $n\ge2$, with the separate initial term retained,

$$a_n=2+a_0+\sum_{j=1}^{n-1}3\cdot2^{j-1}=3+3(2^{n-1}-1)=3\cdot2^{n-1}.$$

The base $n=1$ is already established, and all sum indices are earlier and eligible. At zero the specified value remains one. Option 1 gives nine at two instead of six. Option 2 gives seven there. Option 4 gives two at one instead of three. Coincidence of option 2 with the first positive value does not make it a valid general solution.

More generally, replacing the added two by $b$ and the initial one by $c$ gives first positive term $b+c$ and later terms $(b+c)2^{n-1}$. That derivation still retains a separate $a_0=c$. The constant forcing term controls the seed rather than producing a new additive constant at every step of the simplified doubling relation.

## Q44

**Correct option: 2.** Neighboring prefix equations cancel their shared constant and shared earlier terms, leaving the final term $a_n$. However, this subtraction uses the original formula for $a_n$, which begins at $n=1$. Consequently the derived transition $a_{n+1}=2a_n$ is justified for $n\ge1$; it is not justified between zero and one. The original first equation gives three, whereas extending the doubling rule across that boundary would give two.

Option 1 misstates strong induction: only earlier eligible cases are assumed, never future ones. Option 3 ignores a formula's stated domain; the positive-index expression gives $3/2$ at zero, while the separate initial data correctly remains one. Option 4 is refuted by the exact exponential sequence just proved, so a prefix sum is not automatically polynomial.

The method changes the recurrence's apparent order without changing its mathematical boundary data. To recover the original prefix equation from the simplified transition, retain $a_0=1,a_1=3$ and sum the subsequent geometric values; the resulting prefix is $3\cdot2^{n-1}-2$, so adding two gives $a_n$. This converse verification establishes equivalence under the retained seeds rather than merely proposing a plausible simplified recurrence.

## Q45

**Correct option: 3.** Split $j^2=j(j-1)+j$. A subset with one marked member has $n2^{n-1}$ constructions. A subset with two **ordered distinct** marked members has $n(n-1)2^{n-2}$ constructions: choose the two different members in order, require both present, and choose any subset of the remaining elements.

For $n=6$, these contributions are $6\cdot32=192$ and $6\cdot5\cdot16=480$. Thus

$$\sum_{j=0}^{6}j^2\binom6j=480+192=672.$$

| Subset size $j$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| $j^2\binom6j$ | 0 | 6 | 60 | 180 | 240 | 150 | 36 |

The row independently totals 672. Option 1 counts only one mark. Option 2 counts two distinct ordered marks and excludes the repeated-mark case. Option 4,768, incorrectly uses $n^2 2^{n-1}$, applying the same free-membership count to distinct and repeated marked positions. In the repeated case only one member is forced present; in the distinct case two are forced present.

For $n\ge2$, the general expression simplifies to $n(n+1)2^{n-2}$. At zero the defining sum is zero; at one it is one. These boundaries can be evaluated directly instead of interpreting the negative-size optional subset in the distinct-two-member construction. The counting proof describes exactly why the ordinary square weight has two different structural contributions.

## Q46

**Correct option: 2.** The proof rule adds two to an established nonnegative index. Starting from zero, repeated applications reach $0,2,4,6,\ldots$. Formally, define $Q(m)=P(2m)$ for $m\ge0$. The given base proves $Q(0)$, and the transition at $k=2m$ proves $Q(m)\Rightarrow Q(m+1)$. Ordinary induction establishes all even-index assertions.

No such dependency path reaches an odd index. As a logical countermodel to the stronger claim, let $P(k)$ mean that $k$ is even. Then $P(0)$ and every given implication $P(k)\Rightarrow P(k+2)$ are true, while every odd-index assertion is false. Option 1 is therefore not justified. Option 3 reverses the reachable class, and option 4 ignores the valid transition from zero to two.

“Exactly” describes which indices this proof scheme establishes; it does **not** prove that the actual property is false at every odd index. The property might hold there for an independent reason. To establish the whole nonnegative range with this rule, supply the missing base $P(1)$ and induct separately on $P(2m+1)$. Strong induction cannot manufacture that base without a premise that reaches it. Distinguishing truth of a property from reachability in a proof prevents overstating what the given assumptions imply.
