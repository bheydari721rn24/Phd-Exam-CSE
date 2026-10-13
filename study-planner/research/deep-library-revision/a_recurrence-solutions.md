# Algorithmic recurrence solutions — individual revision draft

### Solution 1

**Subtract two consecutive prefix equations before introducing a generating function.** The first term is $c_1=c_0=1$. For $n\ge1$, the two defining equations give
$$c_{n+1}-c_n=\sum_{i=0}^{n}c_i-\sum_{i=0}^{n-1}c_i=c_n.$$
Thus $c_{n+1}=2c_n$ for $n\ge1$, and $c_n=2^{n-1}$ for every $n\ge1$. The qualification is essential: applying $c_1=2c_0$ would contradict the original seed. The first six values are $1,1,2,4,8,16$.

Treat the generating function as a formal power series, so convergence is unnecessary for coefficient identities. Its constant coefficient is one; the remaining coefficients sum to
$$C(x)=1+\sum_{n=1}^{\infty}2^{n-1}x^n=1+\frac{x}{1-2x}=\frac{1-x}{1-2x}.$$
Comparison with the given denominator gives $\alpha=2$, option 1. If an analytic interpretation is desired, the geometric-series equality holds for $|x|<1/2$.

There is an independent coefficient check that diagnoses every wrong option. Expanding the proposed expression for any candidate $\alpha$ gives a coefficient of $x$ equal to $\alpha-1$. The recurrence requires that coefficient to be $c_1=1$. Options 2, 3 and 4, with $\alpha=3,4,5$, would instead give $2,3,4$. They already fail at the first nonconstant coefficient. Do not solve an altered recurrence with the seed doubled, and do not confuse the denominator growth factor with the exceptional initial term.

### Solution 2

**Use mass conservation to prove both bounds for the unequal tree.** Let $B>0$ be the fixed stopping size, $\delta=\min(\alpha,\beta)$ and $q=\max(\alpha,\beta)$. Because both constants are positive and sum to one, $0<\delta\le q<1$. First analyze the stated real-size recurrence, which keeps the exact identities visible.

At depth $j$, every node has size between $n\delta^j$ and $nq^j$. While the smaller bound exceeds $B$, the entire level remains internal. Its sizes sum to $n$: each split replaces size $s$ by $\alpha s+\beta s=s$. Therefore each of $\Theta(\log n)$ complete levels contributes exactly $n$ toll, proving $\Omega(n\log n)$.

Every branch stops after at most $\log_{1/q}(n/B)+O(1)$ levels. On any incomplete level, internal-node sizes total at most $n$, because terminated subtrees contribute no further internal work. All internal tolls are consequently $O(n\log n)$. Every nonroot leaf has size in $(\delta B,B]$; leaf sizes sum to $n$. There are $O(n)$ leaves, whose bounded base costs add only $O(n)$. This proves the matching upper bound and $T(n)\in\Theta(n\log n)$.

Option 2 is the stated valid upper bound. Options 1 and 4 have only linear order for fixed $\alpha,\beta$, which is too small. The ratio of option 3 to the derived order is $\beta n^{\alpha-1}\to0$, so that upper bound also fails. Fixed ratios matter: permitting $\alpha$ to approach zero with the input changes the constants and can invalidate this uniform argument. For an implementation with integer children, declare the rounding and verify progress; the exact real-size identities are not automatically exact integer identities.

### Solution 3

**Count a single chain of decreasing logarithms.** Choose natural logarithms for the derivation; another fixed base changes only positive constants. Put $L=\ln n$ and $d=\ln(3/2)>0$. After $j$ recursive steps, the argument is $(2/3)^jn$, so its toll is $(L-jd)^2$. A fixed stopping threshold gives $h=L/d+O(1)$ nonbase calls. Unrolling yields
$$T(n)=O(1)+\sum_{j=0}^{h-1}(L-jd)^2.$$
There are $O(L)$ summands, each at most $L^2$, giving $O(L^3)$. To prove the lower bound, keep the first $\lfloor L/(2d)\rfloor$ calls. Each has logarithm at least $L/2$, so these $\Theta(L)$ calls contribute $\Omega(L^3)$. Both bounds establish $\Theta(\log^3 n)$, option 3.

The exact subsequence $n=(3/2)^h$, with a base at one, provides a check: the nonrecursive sum is
$$d^2\sum_{r=1}^{h}r^2=d^2\frac{h(h+1)(2h+1)}6.$$
The cubic power comes from accumulating squared logarithms along one branch; there are no exponentially many nodes to count.

Option 2 retains just the largest toll and loses a factor of $\log n$. Option 1 asserts a tight linear order, but $\log^3 n/n\to0$. Option 4 is also a false tight order, since $(n\log^2 n)/\log^3 n=n/\log n\to\infty$. These two larger expressions would be valid loose upper bounds if they used $O$; here they use $\Theta$. Fixed bounded integer rounding changes only the final endpoint and constants when the child eventually enters the declared base region.

### Solution 4

**Use the four options actually printed on the enlarged original page.** They are $O(\log n\log\log n)$, $O(n\log n\log\log n)$, $O(n\log\log n)$ and $O(\log\log n)$, respectively. The original literal wording admits three true upper bounds. Option 1 is the intended answer under the smallest-listed-upper-bound convention; options 2 and 3 must not be called false upper bounds.

Put $m=\log_2 n$. Without rounding, the transformed recurrence is $S(m)=2S(m/2)+m$, whose level toll is $2^j(m/2^j)=m$. There are $\Theta(\log m)$ nonbase levels and $O(m)$ leaves. Thus $S(m)\in\Theta(m\log m)$.

The floor needs an actual bound. For $x\ge4$, $\sqrt x/2\le\lfloor\sqrt x\rfloor\le\sqrt x$. Taking logarithms gives a transformed child between $m/2-1$ and $m/2$. Iterating bounds the common size at depth $j$ between $m/2^j-2$ and $m/2^j$. Total toll is at most $m$ and, while $2^j\le m/4$, at least $m-2^{j+1}\ge m/2$. There are $\Theta(\log m)$ such early levels. The complete tree stops by $O(\log m)$ depth and has $O(m)$ leaves. These independent lower and upper estimates retain the same tight order despite rounding.

Return to the original variable: $m\log m=\Theta(\log n\log\log n)$. Relative to this expression, option 2 has factor $n$ and option 3 has factor $n/\log n$, both unbounded. Option 4 is too small by a factor of $\log n$. A fixed base region must contain the fixed point one and all other terminal inputs; recursing at one would otherwise fail to terminate. The displayed tree uses an exact double-exponential size to illustrate the derivation, and explicitly identifies that illustrative input rather than pretending to animate every integer.

### Solution 5

**Derive the branch sizes from the pivot guarantee, not from a preferred theorem.** For sufficiently large $n$, the sample size $m=2\sqrt n+1$ is at most $n$ after ordinary rounding. Insertion sort of these $\Theta(\sqrt n)$ sampled elements costs $O(m^2)=O(n)$, and the ordinary partition scan performs $\Theta(n)$ work. The combined toll is therefore $\Theta(n)$ even when the sample happened to be already sorted.

Assume distinct keys. The sample median has at least $\sqrt n$ sampled keys below it and at least that many above it, suppressing the integer corrections. The global pivot rank cannot be closer than roughly $\sqrt n$ to either endpoint. Nevertheless all unsampled keys can lie on one side, so the guarantee allows a small side of that order and a large side of order $n-\sqrt n$.

The faithful integer worst-case model is a maximization over the allowed ranks:
$$W(n)=\max_{r\in R_n}\bigl(W(r)+W(n-1-r)+\Theta(n)\bigr),$$
where $R_n$ excludes the forbidden endpoint ranks. The listed extreme-split abstraction suppresses the pivot, rounding and bounded corrections, yielding $T(n-\sqrt n)+T(\sqrt n)+n$, option 4. It describes the worst permitted imbalance, not the split of every input. A proof that the same extreme choices can be realized recursively needs an adversarial-input argument; the recurrence choice alone is not that proof.

Option 1 creates two almost full-size children and violates disjoint partition sizes. Option 2 accounts for only about $2\sqrt n$ elements and omits the large partition. Option 3 again counts two large children whose total size exceeds the parent's available keys. With duplicate keys, an equal-key partition policy must be specified; the distinct-rank guarantee cannot be imported unchanged. This is a modeling question, so applying the equal-ratio Master theorem would miss its central point.

### Solution 6

**Expand a product, not a sum.** The recurrence multiplies by $2^n$ at the current step. Repeated substitution gives
$$T(n)=2^n2^{n-1}\cdots2^1T(0)=2^{\sum_{j=1}^{n}j}=2^{n(n+1)/2}.$$
The empty product at $n=0$ is one, matching the specified seed. An independent logarithmic derivation puts $L_n=\log_2T(n)$, so $L_n=L_{n-1}+n$ and $L_0=0$. Summing this additive recurrence gives exactly the same triangular exponent. The first values are $1,2,8,64,1024$.

Option 4 is exact, not merely asymptotically equivalent:
$$2^{n(n+1)/2}=(\sqrt2)^{n^2+n}.$$
Option 3 fails as a tight class because its ratio to the exact value is $2^{(n^2-n)/2}\to\infty$. Although both exponents have quadratic order, a constant factor inside an exponent cannot be discarded when asserting a $\Theta$ relation between the exponentials.

Option 1 has base-two logarithm $2n\log_2 n$, which is smaller than $n(n+1)/2$ by an unbounded asymptotic factor. Its ratio to the exact value tends to zero. Option 2 likewise has logarithm $n+\log_2\log n$, only roughly linear. Thus neither can provide a matching lower bound for $T$.

The broad description $2^{\Theta(n^2)}$ is valid, but it encompasses many inequivalent tight exponential classes and would not distinguish options 3 and 4. The base seed also matters: replacing it by zero would make every value zero. The logarithmic animation displays the exponent and actual multipliers so its numerical labels stay readable while the mathematical product remains exact.

### Solution 7

**Project the recurrence onto the two parity states.** Let $p_n$ be the residue of $a_n$ modulo two. Both odd multipliers reduce to one, while four reduces to zero. Therefore
$$p_n\equiv p_{n-1}+p_{n-2}\pmod2.$$
The given values at indices sixteen and seventeen are both odd, so the initial pair is $(1,1)$. Its next state is $(1,0)$, then $(0,1)$, then $(1,1)$ again. The three-state cycle repeats deterministically: the recurrence on pairs maps each current pair to exactly one next pair.

From the anchored indices we obtain $p_{18}=0$, $p_{19}=1$, $p_{20}=1$ and $p_{21}=0$. Thus the even terms are precisely those indices congruent to zero modulo three along this forward recurrence. We do not need the huge actual values of the sequence.

The closed requested interval contains the multiples $102,105,108,111$. Equivalently, their count is
$$\left\lfloor\frac{113}{3}\right\rfloor-\left\lfloor\frac{99}{3}\right\rfloor=37-33=4.$$
Option 1 is correct. Option 2 would come from including the next multiple, 114, which is outside the interval, or misaligning the initial cycle. Options 3 and 4 do not follow from the actual three-state orbit; the interval has fourteen terms but parity is not evenly alternating.

A bare statement that the cycle has length three is insufficient: its phase must be fixed from the supplied indices. Also, taking parity after numerically generating large integers is unnecessary and obscures the proof. The diagram shows both the initial transition cycle and the actual requested indices, with the skipped middle interval clearly declared. The argument is a finite-state recurrence calculation, not an assumption that all second-order sequences have this period.

### Solution 8

**Keep the base contribution when asking for an exact value.** Write $n=2^h$ and normalize $V_h=T(2^h)/2^h$. The defining recurrence becomes $V_h=V_{h-1}+1$, while $V_0=T(1)=3$. Consequently $V_h=3+h$, and
$$T(n)=n(3+\log_2 n).$$
For $n=32=2^5$, this is $32(3+5)=256$, option 3. The recurrence itself supplies a second exact check: its values at inputs $1,2,4,8,16,32$ are $3,8,20,48,112,256$.

The tree explains every term. At each of the five internal depths, there are $2^j$ nodes of size $32/2^j$, so the total toll is 32. Those levels cost $5\cdot32=160$. There are 32 leaves and each costs three, adding 96. The total is $160+96=256$.

Option 1, 160, drops all leaf work. Option 4, 96, drops all internal work. Option 2, 192, is the answer to a different recurrence with unit leaf cost: its six equal 32-unit contributions would total 192. Exact seed changes can matter even though all these positive fixed seeds preserve the same $\Theta(n\log n)$ class.

This derivation uses powers of two, as the question specifies. It is not an exact formula for a rounded implementation at arbitrary sizes. If the input were 33, one would first need the floor/ceiling split and the terminal conditions. The animation accounts for a complete level by node multiplicity rather than drawing dozens of overlapping leaf boxes, and separately includes the base level.

### Solution 9

**Transform the input into its logarithmic index and sum the actual tolls.** At $n=2^h$, let $U_h=T(2^h)$. One recursive halving decrements $h$ by one, so $U_h=U_{h-1}+h^3$, with $U_0=1$. Unrolling gives
$$U_h=1+\sum_{r=1}^{h}r^3=1+\left(\frac{h(h+1)}2\right)^2.$$
For $n=16$, $h=4$. The tolls along the chain are $4^3,3^3,2^3,1^3$, not four copies of the root toll. Hence
$$T(16)=1+64+27+8+1=101,$$
and option 3 is correct. The seed one and the last toll one are separate contributions.

Option 1, 65, retains only the root toll and the base. Option 2, 81, misses contributions and is not the recurrence total: the correct sum of nonbase tolls is 100. Option 4, 257, treats the four nonbase calls as if all retained toll $4^3$, then adds the seed. That overcounts the three smaller tolls.

The sum-of-cubes identity can be established by induction: adding $(h+1)^3$ to $[h(h+1)/2]^2$ gives $[(h+1)(h+2)/2]^2$. Thus both the closed form and its initial value are verified. Returning to general powers of two gives $\Theta((\log n)^4)$; the input's logarithmic chain length cannot be mistaken for $n$ recursive calls. Keeping the specified log base is required for the exact value 101, although any fixed log base gives the same asymptotic class.

### Solution 10

**A square root halves the logarithm, not the input by a fixed ratio.** Put $m=\log_2 n$ and $S(m)=T(2^m)$. The recurrence becomes $S(m)=4S(m/2)+m$, with a fixed base region $m\le2$. Its branching exponent is $\log_2 4=2$, and its toll $m$ is polynomially below $m^2$. The leaf-dominated case therefore yields $S(m)\in\Theta(m^2)$, which returns to $\Theta(\log^2 n)$, option 3.

A complete tree independently verifies the classification. At depth $j$, there are $4^j$ nodes with logarithmic size $m/2^j$. Their combined toll is $m2^j$. The depth is $h=\log_2(m/2)+O(1)$. Summing the geometric level tolls gives $\Theta(m2^h)=\Theta(m^2)$. The leaves number $4^h=\Theta(m^2)$, and positive bounded base costs supply a matching lower bound.

For the exact grid $n=2^{2^k}$ and a unit base at $n=4$, $k\ge1$, the cost sequence satisfies $U_1=1$ and $U_k=4U_{k-1}+2^k$. Direct substitution gives $U_k=3\cdot4^{k-1}-2^k$. The first values $1,8,40,176$ confirm the quadratic order in $m=2^k$, without claiming this particular seed in the original asymptotic question.

Option 1 is too small by a logarithmic factor. Option 2 is the critical order for two children, not four; its ratio to $\log^2 n$ tends to zero. Option 4 is much too large as a tight class because $\log^2 n/n\to0$. The fixed base region avoids the square-root fixed point at one. It also makes the theorem application well defined in the transformed variable.

### Solution 11

**Subtract adjacent prefix equations while retaining the exceptional first step.** The definition gives $a_1=3a_0=3$. For $n\ge1$,
$$a_{n+1}-a_n=3\sum_{i=0}^{n}a_i-3\sum_{i=0}^{n-1}a_i=3a_n.$$
Thus $a_{n+1}=4a_n$ for $n\ge1$, and $a_n=3\cdot4^{n-1}$ for $n\ge1$. At $n=5$, $a_5=3\cdot4^4=768$, option 2. The direct sequence is $1,3,12,48,192,768$.

The subtraction is valid only after the earlier defining equation exists. Imposing $a_1=4a_0$ would turn the sequence into $4^n$ and fail at its first nonbase index. This explains option 3, 1024, which improperly extends the factor four across the initial step.

Options 1 and 4, 243 and 729, are powers of three and correspond to treating the prefix multiplier as the one-step growth factor. The multiplier applies to the entire previous prefix, not just the previous term. The prefix itself doubles only in the multiplier-one version; here its new term is three times the previous prefix, so the updated prefix is four times as large.

A second derivation defines $P_n=\sum_{i=0}^{n}a_i$. Then $P_0=1$ and $P_{n+1}=P_n+a_{n+1}=4P_n$, giving $P_n=4^n$. Therefore $a_5=3P_4=768$. This calculation validates the index and distinguishes term growth from prefix growth. The animation lists both quantities on each step, rather than using an unlabeled generic exponential chart.

### Solution 12

**A repeated root requires two linearly independent solutions.** Moving all terms to one side yields characteristic polynomial $r^2-4r+4=(r-2)^2$. Its repeated root gives the form $a_n=(A+Bn)2^n$. The first seed gives $A=a_0=1$; the second gives $2(A+B)=6$, so $B=2$. Therefore
$$a_n=(1+2n)2^n,\qquad a_4=9\cdot16=144,$$
which is option 3.

There is a derivation that does not depend on memorizing the repeated-root rule. Normalize $b_n=a_n/2^n$. Dividing the recurrence by $2^n$ gives $b_n=2b_{n-1}-b_{n-2}$. Hence consecutive differences satisfy $b_n-b_{n-1}=b_{n-1}-b_{n-2}$. Since $b_0=1$ and $b_1=3$, all these differences equal two, giving $b_n=1+2n$. This proves both the form and the required linear factor.

Direct evaluation supplies the finite check $a_0,a_1,a_2,a_3,a_4=1,6,20,56,144$. Option 1, 64, drops the constant contribution and uses a different slope. Option 2, 80, results from slope one instead of two. Option 4, 160, would require a different initial constant or slope. Each is refuted by the normalized seeds or the final exact evaluation; none becomes acceptable just because it looks like a polynomial times $2^n$.

Uniqueness follows because each next term is determined by the previous two terms. A purported closed form that satisfies only the characteristic equation but not both seeds solves a different initial-value problem. Negative recurrence coefficients also mean an interpretation as a tree with positive child counts would be inappropriate.

### Solution 13

**Unroll the subtract-one chain and include its entire endpoint range.** Since the terminal input is zero, the nonbase calls use $n,n-1,\ldots,1$. Their tolls are the first $n$ positive odd integers in descending order. Thus
$$T(n)=T(0)+\sum_{j=1}^{n}(2j-1)=2\frac{n(n+1)}2-n=n^2.$$
Option 2 is correct, including at $n=0$, where the sum is empty.

Induction provides a separate check. Assume $T(n-1)=(n-1)^2$. Adding the current toll gives $(n-1)^2+2n-1=n^2$, and the zero base satisfies the proposed form. At inputs zero through four, the values are $0,1,4,9,16$.

Option 1, $n$, counts calls while assuming unit toll; it ignores the increasing local cost. Option 3, $n(n+1)$, sums the even tolls $2j$ and omits the subtract-one in every call. Its overestimate is exactly $n$. Option 4, $2^n-1$, is a geometric total associated with repeated doubling, whereas this recurrence has one child and no multiplicative amplification.

The geometric interpretation of the odd tolls is exact: enlarging a square of side $n-1$ to a square of side $n$ adds $2n-1$ unit cells. That visual provides a constructive reason for the squared answer and a useful check of the endpoint. The standard Master theorem does not apply because the child is $n-1$, not $n/b$ for a fixed $b>1$. Changing the seed to a constant $c$ would give $n^2+c$, which preserves order but changes exact values.

### Solution 14

**Quadratic work contracts across the unequal children.** The root alone contributes $n^2$, proving $\Omega(n^2)$. At the next complete level, the sum of squared child sizes is
$$\left(\frac n4\right)^2+\left(\frac{3n}4\right)^2=\frac58n^2.$$
Repeating gives total squared toll at depth $j$ no greater than $(5/8)^jn^2$; stopping a small node removes its future positive tolls and can only decrease this level sum. The internal work is at most $n^2\sum_{j\ge0}(5/8)^j=(8/3)n^2$. Leaf sizes remain bounded below by a fixed positive fraction of the base threshold, so there are $O(n)$ leaves and only $O(n)$ base work. This establishes $O(n^2)$ and hence the tight class $\Theta(n^2)$, option 3.

An induction envelope supplies the same constant. If each child is bounded by $Cs^2$, the recurrence gives $T(n)\le(5C/8+1)n^2$. Choosing $C\ge8/3$ makes this at most $Cn^2$, and increasing $C$ further covers the finitely many base inputs. That base adjustment must not be omitted.

Option 1 is smaller than the compulsory root toll. Option 2 is also too small because $n\log n/n^2\to0$. Option 4 incorrectly adds a depth factor: the per-level quadratic work decreases geometrically, so its total is bounded by a constant multiple of the root cost. Linear mass conservation would yield constant linear level work, but conservation of size does not imply conservation of squared size.

The displayed model uses exact real-size splits and labels each squared contribution. An integer implementation needs a specified partition and bounded-rounding analysis, rather than claiming the exact fraction $5/8$ at every rounded node.

### Solution 15

**Distinguish executed calls from distinct subproblems.** Let $C_n$ be the number of calls in naive recursion, including the initial call. With the ordinary bases zero and one, $C_0=C_1=1$, and for $n\ge2$,
$$C_n=C_{n-1}+C_{n-2}+1.$$
Set $D_n=C_n+1$. Then $D_n=D_{n-1}+D_{n-2}$ with $D_0=D_1=2$. It follows that $C_n=2F_{n+1}-1$. The characteristic roots of the Fibonacci recurrence are $\phi=(1+\sqrt5)/2$ and $\psi=(1-\sqrt5)/2$, with $|\psi|<1$. Thus $F_{n+1}\in\Theta(\phi^n)$ and naive work has that tight order.

Memoization changes the executed graph. Each state zero through $n$ is stored once; each new nonbase state needs one addition and a fixed number of lookups. There are $n-1$ such additions and $O(n)$ state/edge operations. Therefore both the required lower work and an explicit evaluation strategy establish $\Theta(n)$ under the stated unit-cost arithmetic assumption. Option 2 is correct.

Option 1 understates naive growth as quadratic. Option 3 uses a loose exponential upper bound $2^n$ as if it were tight, and its logarithmic memoized claim cannot even cover the $n-1$ distinct additions. Option 4 assumes naive recursion already reuses overlapping states. A call tree and a dependency DAG can compute the same mathematical sequence with different work.

The arithmetic model is part of the answer. Fibonacci integers have $\Theta(n)$ bits. With linear-time bit additions, straightforward memoized arithmetic sums bit costs of orders $1,2,\ldots,n$ and takes $\Theta(n^2)$ bit operations, rather than the stipulated $\Theta(n)$ unit operations. Stack depth is another quantity and must not be substituted for total calls.

### Solution 16

**Derive the exact expression and its domain.** Introduce the shifted sequence $V_n=T_n+3$. Then $V_n=2V_{n-1}$ and $V_0=3$, so $V_n=3\cdot2^n$. Returning to $T$ yields $T_n=3(2^n-1)$. Unrolling gives the independent geometric sum $3\sum_{j=0}^{n-1}2^j$, since each earlier toll is doubled at every later step. The values at indices zero through three are $0,3,9,21$. The proposed form has the correct seed and, on substitution, $2\cdot3(2^{n-1}-1)+3=3(2^n-1)$. Uniqueness follows from the one-step recurrence. Its growth is $\Theta(2^n)$, but replacing its exact value by $3\cdot2^n$ loses the constant correction. The shift is chosen from the fixed-point equation $c=2c+3$, whose fixed point is negative three.

$$T_n=3(2^n-1).$$

**Evaluate the requested index, rather than just its order.** Substituting $n=5$ yields $93$, so option 2 is correct. Direct step-by-step iteration from the declared seed provides the same number; the accompanying ledger includes each multiplication, local toll and accumulated total.

Option 1 gives $15$, which differs from the independently evaluated exact value $93$. Option 3 gives $96$, which differs from the independently evaluated exact value $93$. Option 4 gives $31$, which differs from the independently evaluated exact value $93$. The precise finite correction and the initial value decide this numerical question; selecting merely the right asymptotic class would not distinguish the listed integers.

### Solution 17

**Derive the exact expression and its domain.** Introduce the shifted sequence $V_n=T_n+3$. Then $V_n=2V_{n-1}$ and $V_0=3$, so $V_n=3\cdot2^n$. Returning to $T$ yields $T_n=3(2^n-1)$. Unrolling gives the independent geometric sum $3\sum_{j=0}^{n-1}2^j$, since each earlier toll is doubled at every later step. The values at indices zero through three are $0,3,9,21$. The proposed form has the correct seed and, on substitution, $2\cdot3(2^{n-1}-1)+3=3(2^n-1)$. Uniqueness follows from the one-step recurrence. Its growth is $\Theta(2^n)$, but replacing its exact value by $3\cdot2^n$ loses the constant correction. The shift is chosen from the fixed-point equation $c=2c+3$, whose fixed point is negative three.

$$T_n=3(2^n-1).$$

**Evaluate the requested index, rather than just its order.** Substituting $n=8$ yields $765$, so option 1 is correct. Direct step-by-step iteration from the declared seed provides the same number; the accompanying ledger includes each multiplication, local toll and accumulated total.

Option 2 gives $768$, which differs from the independently evaluated exact value $765$. Option 3 gives $255$, which differs from the independently evaluated exact value $765$. Option 4 gives $24$, which differs from the independently evaluated exact value $765$. The precise finite correction and the initial value decide this numerical question; selecting merely the right asymptotic class would not distinguish the listed integers.

### Solution 18

**Derive the exact expression and its domain.** Introduce the shifted sequence $V_n=T_n+3$. Then $V_n=2V_{n-1}$ and $V_0=3$, so $V_n=3\cdot2^n$. Returning to $T$ yields $T_n=3(2^n-1)$. Unrolling gives the independent geometric sum $3\sum_{j=0}^{n-1}2^j$, since each earlier toll is doubled at every later step. The values at indices zero through three are $0,3,9,21$. The proposed form has the correct seed and, on substitution, $2\cdot3(2^{n-1}-1)+3=3(2^n-1)$. Uniqueness follows from the one-step recurrence. Its growth is $\Theta(2^n)$, but replacing its exact value by $3\cdot2^n$ loses the constant correction. The shift is chosen from the fixed-point equation $c=2c+3$, whose fixed point is negative three.

$$T_n=3(2^n-1).$$

**Diagnose the symbolic alternatives.** Option 4 is the exact expression. $3\cdot2^n$ omits the subtract-three correction; $2^n-1$ omits the toll multiplier three; $3n$ adds tolls without their repeated doubling. Each invalid expression either fails the stated seed, fails the step equation, or drops a nonzero exact contribution. Checking a proposed formula against both conditions is a complete test for this one-step initial-value problem. The animation gives two independently evaluated indices, five and eight; those illustrations supplement the algebraic proof rather than replace it.

### Solution 19

**Derive the exact expression and its domain.** Introduce the shifted sequence $V_n=T_n+3$. Then $V_n=2V_{n-1}$ and $V_0=3$, so $V_n=3\cdot2^n$. Returning to $T$ yields $T_n=3(2^n-1)$. Unrolling gives the independent geometric sum $3\sum_{j=0}^{n-1}2^j$, since each earlier toll is doubled at every later step. The values at indices zero through three are $0,3,9,21$. The proposed form has the correct seed and, on substitution, $2\cdot3(2^{n-1}-1)+3=3(2^n-1)$. Uniqueness follows from the one-step recurrence. Its growth is $\Theta(2^n)$, but replacing its exact value by $3\cdot2^n$ loses the constant correction. The shift is chosen from the fixed-point equation $c=2c+3$, whose fixed point is negative three.

$$T_n=3(2^n-1).$$

**Check the statement about applicability.** The correct statement is that the shifted seed is required. The new sequence has seed three, not zero. If it were incorrectly started at zero, every homogeneous value would be zero and the reconstructed sequence would be negative three, immediately violating $T_0=0$. A positive constant toll under two-child amplification yields exponential growth, so the linear-growth claim also fails. Omitting the toll changes the actual recurrence to the identically zero sequence. The correct option is 3. The two finite illustrations are checks of this proof; their agreement is not used to infer a formula for all positive indices. The same mathematical recurrence must always be accompanied by its seed and by the relationship, if any, between its index and the original input size.

### Solution 20

**Derive the exact expression and its domain.** Normalize by the input size: $V_n=U_n/2^n$. Dividing the equation by $2^n$ gives $V_n=V_{n-1}+1$, with $V_0=1$. Therefore $V_n=n+1$ and $U_n=(n+1)2^n$. At original size $N=2^n$, the recursion depth is $n=\log_2N$. Its $n$ internal levels each have aggregate toll $N$; its $N$ unit leaves add one more aggregate $N$. The indices zero through three have values $1,4,12,32$. Substitution verifies $2[n2^{n-1}]+2^n=(n+1)2^n$, and the seed matches. In the original input variable, the tight class is $\Theta(N\log N)$; in the depth index it is $\Theta(n2^n)$. The variables must be distinguished before a theorem is applied.

$$U_n=(n+1)2^n.$$

**Evaluate the requested index, rather than just its order.** Substituting $n=5$ yields $192$, so option 1 is correct. Direct step-by-step iteration from the declared seed provides the same number; the accompanying ledger includes each multiplication, local toll and accumulated total.

Option 2 gives $160$, which differs from the independently evaluated exact value $192$. Option 3 gives $63$, which differs from the independently evaluated exact value $192$. Option 4 gives $1024$, which differs from the independently evaluated exact value $192$. The precise finite correction and the initial value decide this numerical question; selecting merely the right asymptotic class would not distinguish the listed integers.

### Solution 21

**Derive the exact expression and its domain.** Normalize by the input size: $V_n=U_n/2^n$. Dividing the equation by $2^n$ gives $V_n=V_{n-1}+1$, with $V_0=1$. Therefore $V_n=n+1$ and $U_n=(n+1)2^n$. At original size $N=2^n$, the recursion depth is $n=\log_2N$. Its $n$ internal levels each have aggregate toll $N$; its $N$ unit leaves add one more aggregate $N$. The indices zero through three have values $1,4,12,32$. Substitution verifies $2[n2^{n-1}]+2^n=(n+1)2^n$, and the seed matches. In the original input variable, the tight class is $\Theta(N\log N)$; in the depth index it is $\Theta(n2^n)$. The variables must be distinguished before a theorem is applied.

$$U_n=(n+1)2^n.$$

**Evaluate the requested index, rather than just its order.** Substituting $n=8$ yields $2304$, so option 4 is correct. Direct step-by-step iteration from the declared seed provides the same number; the accompanying ledger includes each multiplication, local toll and accumulated total.

Option 1 gives $2048$, which differs from the independently evaluated exact value $2304$. Option 2 gives $511$, which differs from the independently evaluated exact value $2304$. Option 3 gives $65536$, which differs from the independently evaluated exact value $2304$. The precise finite correction and the initial value decide this numerical question; selecting merely the right asymptotic class would not distinguish the listed integers.

### Solution 22

**Derive the exact expression and its domain.** Normalize by the input size: $V_n=U_n/2^n$. Dividing the equation by $2^n$ gives $V_n=V_{n-1}+1$, with $V_0=1$. Therefore $V_n=n+1$ and $U_n=(n+1)2^n$. At original size $N=2^n$, the recursion depth is $n=\log_2N$. Its $n$ internal levels each have aggregate toll $N$; its $N$ unit leaves add one more aggregate $N$. The indices zero through three have values $1,4,12,32$. Substitution verifies $2[n2^{n-1}]+2^n=(n+1)2^n$, and the seed matches. In the original input variable, the tight class is $\Theta(N\log N)$; in the depth index it is $\Theta(n2^n)$. The variables must be distinguished before a theorem is applied.

$$U_n=(n+1)2^n.$$

**Diagnose the symbolic alternatives.** Option 3 is the exact expression. $2^{n+1}-1$ counts a single decreasing-cost chain instead of the two-child tree; $4^n$ uses a leaf exponent for four rather than two children; $n2^n$ drops the unit cost of every base leaf. Each invalid expression either fails the stated seed, fails the step equation, or drops a nonzero exact contribution. Checking a proposed formula against both conditions is a complete test for this one-step initial-value problem. The animation gives two independently evaluated indices, five and eight; those illustrations supplement the algebraic proof rather than replace it.

### Solution 23

**Derive the exact expression and its domain.** Normalize by the input size: $V_n=U_n/2^n$. Dividing the equation by $2^n$ gives $V_n=V_{n-1}+1$, with $V_0=1$. Therefore $V_n=n+1$ and $U_n=(n+1)2^n$. At original size $N=2^n$, the recursion depth is $n=\log_2N$. Its $n$ internal levels each have aggregate toll $N$; its $N$ unit leaves add one more aggregate $N$. The indices zero through three have values $1,4,12,32$. Substitution verifies $2[n2^{n-1}]+2^n=(n+1)2^n$, and the seed matches. In the original input variable, the tight class is $\Theta(N\log N)$; in the depth index it is $\Theta(n2^n)$. The variables must be distinguished before a theorem is applied.

$$U_n=(n+1)2^n.$$

**Check the statement about applicability.** The correct scope statement identifies the level index as the logarithm of the original size. The index $n$ is not $N=2^n$. Unit leaves contribute exactly $2^n$, so they cannot be dropped from an exact total. A linear toll under two half-size children accumulates on every level; it is not automatically linear overall. On the concrete depth five input, internal work is 160 and leaf work is 32. The correct option is 2. The two finite illustrations are checks of this proof; their agreement is not used to infer a formula for all positive indices. The same mathematical recurrence must always be accompanied by its seed and by the relationship, if any, between its index and the original input size.

### Solution 24

**Derive the exact expression and its domain.** Divide by $4^n$ and write $V_n=U_n/4^n$. The equation becomes $V_n=V_{n-1}+2^{-n}$ with $V_0=1$. Its finite geometric sum is $V_n=1+\sum_{j=1}^n2^{-j}=2-2^{-n}$. Hence $U_n=2\cdot4^n-2^n$. The base value is $2-1=1$. Substitution verifies $4(2\cdot4^{n-1}-2^{n-1})+2^n=2\cdot4^n-2^n$. Values at indices zero through three are $1,6,28,120$. At original input size $N=2^n$, each level $j$ has toll $N2^j$ and the base level contains $4^n=N^2$ unit leaves. The sum is leaf dominated, giving $\Theta(N^2)$, but the finite correction remains necessary for exact questions.

$$U_n=2\cdot4^n-2^n.$$

**Evaluate the requested index, rather than just its order.** Substituting $n=5$ yields $2016$, so option 4 is correct. Direct step-by-step iteration from the declared seed provides the same number; the accompanying ledger includes each multiplication, local toll and accumulated total.

Option 1 gives $1024$, which differs from the independently evaluated exact value $2016$. Option 2 gives $192$, which differs from the independently evaluated exact value $2016$. Option 3 gives $2048$, which differs from the independently evaluated exact value $2016$. The precise finite correction and the initial value decide this numerical question; selecting merely the right asymptotic class would not distinguish the listed integers.

### Solution 25

**Derive the exact expression and its domain.** Divide by $4^n$ and write $V_n=U_n/4^n$. The equation becomes $V_n=V_{n-1}+2^{-n}$ with $V_0=1$. Its finite geometric sum is $V_n=1+\sum_{j=1}^n2^{-j}=2-2^{-n}$. Hence $U_n=2\cdot4^n-2^n$. The base value is $2-1=1$. Substitution verifies $4(2\cdot4^{n-1}-2^{n-1})+2^n=2\cdot4^n-2^n$. Values at indices zero through three are $1,6,28,120$. At original input size $N=2^n$, each level $j$ has toll $N2^j$ and the base level contains $4^n=N^2$ unit leaves. The sum is leaf dominated, giving $\Theta(N^2)$, but the finite correction remains necessary for exact questions.

$$U_n=2\cdot4^n-2^n.$$

**Evaluate the requested index, rather than just its order.** Substituting $n=8$ yields $130816$, so option 3 is correct. Direct step-by-step iteration from the declared seed provides the same number; the accompanying ledger includes each multiplication, local toll and accumulated total.

Option 1 gives $2304$, which differs from the independently evaluated exact value $130816$. Option 2 gives $131072$, which differs from the independently evaluated exact value $130816$. Option 4 gives $65536$, which differs from the independently evaluated exact value $130816$. The precise finite correction and the initial value decide this numerical question; selecting merely the right asymptotic class would not distinguish the listed integers.

### Solution 26

**Derive the exact expression and its domain.** Divide by $4^n$ and write $V_n=U_n/4^n$. The equation becomes $V_n=V_{n-1}+2^{-n}$ with $V_0=1$. Its finite geometric sum is $V_n=1+\sum_{j=1}^n2^{-j}=2-2^{-n}$. Hence $U_n=2\cdot4^n-2^n$. The base value is $2-1=1$. Substitution verifies $4(2\cdot4^{n-1}-2^{n-1})+2^n=2\cdot4^n-2^n$. Values at indices zero through three are $1,6,28,120$. At original input size $N=2^n$, each level $j$ has toll $N2^j$ and the base level contains $4^n=N^2$ unit leaves. The sum is leaf dominated, giving $\Theta(N^2)$, but the finite correction remains necessary for exact questions.

$$U_n=2\cdot4^n-2^n.$$

**Diagnose the symbolic alternatives.** Option 2 is the exact expression. $2\cdot4^n$ replaces a finite sum by its limiting normalized value and omits $2^n$; $4^n$ counts only unit leaf work; $(n+1)2^n$ belongs to two rather than four children. Each invalid expression either fails the stated seed, fails the step equation, or drops a nonzero exact contribution. Checking a proposed formula against both conditions is a complete test for this one-step initial-value problem. The animation gives two independently evaluated indices, five and eight; those illustrations supplement the algebraic proof rather than replace it.

### Solution 27

**Derive the exact expression and its domain.** Divide by $4^n$ and write $V_n=U_n/4^n$. The equation becomes $V_n=V_{n-1}+2^{-n}$ with $V_0=1$. Its finite geometric sum is $V_n=1+\sum_{j=1}^n2^{-j}=2-2^{-n}$. Hence $U_n=2\cdot4^n-2^n$. The base value is $2-1=1$. Substitution verifies $4(2\cdot4^{n-1}-2^{n-1})+2^n=2\cdot4^n-2^n$. Values at indices zero through three are $1,6,28,120$. At original input size $N=2^n$, each level $j$ has toll $N2^j$ and the base level contains $4^n=N^2$ unit leaves. The sum is leaf dominated, giving $\Theta(N^2)$, but the finite correction remains necessary for exact questions.

$$U_n=2\cdot4^n-2^n.$$

**Check the statement about applicability.** The correct statement separates an asymptotically dominant term from the exact lower-order correction. The smaller toll is positive at every internal call and contributes $4^n-2^n$ in total, not zero. The exact answer differs from $2\cdot4^n$ by $2^n$ at every finite index. Changing the child count from four to two changes the growth mechanism, so the number of children cannot be ignored. The correct option is 1. The two finite illustrations are checks of this proof; their agreement is not used to infer a formula for all positive indices. The same mathematical recurrence must always be accompanied by its seed and by the relationship, if any, between its index and the original input size.

### Solution 28

**Derive the exact expression and its domain.** Unroll the one-child recurrence without a multiplicity factor: $U_n=1+\sum_{j=1}^n2^j$. The finite geometric sum equals $2^{n+1}-2$, giving $U_n=2^{n+1}-1$. The sequence begins $1,3,7,15$. Substitution verifies $(2^n-1)+2^n=2^{n+1}-1$ and the zero-index seed is one. If these indices represent input sizes $N=2^n$, the chain contains tolls $N,N/2,\ldots,2$ plus the unit base, totaling $2N-1$. Its work is $\Theta(N)$ despite having logarithmic depth. A depth factor cannot simply multiply the top toll when later tolls shrink geometrically. For exact values, both the lower limit of the sum and the initial seed are retained.

$$U_n=2^{n+1}-1.$$

**Evaluate the requested index, rather than just its order.** Substituting $n=5$ yields $63$, so option 4 is correct. Direct step-by-step iteration from the declared seed provides the same number; the accompanying ledger includes each multiplication, local toll and accumulated total.

Option 1 gives $32$, which differs from the independently evaluated exact value $63$. Option 2 gives $160$, which differs from the independently evaluated exact value $63$. Option 3 gives $6$, which differs from the independently evaluated exact value $63$. The precise finite correction and the initial value decide this numerical question; selecting merely the right asymptotic class would not distinguish the listed integers.

### Solution 29

**Derive the exact expression and its domain.** Unroll the one-child recurrence without a multiplicity factor: $U_n=1+\sum_{j=1}^n2^j$. The finite geometric sum equals $2^{n+1}-2$, giving $U_n=2^{n+1}-1$. The sequence begins $1,3,7,15$. Substitution verifies $(2^n-1)+2^n=2^{n+1}-1$ and the zero-index seed is one. If these indices represent input sizes $N=2^n$, the chain contains tolls $N,N/2,\ldots,2$ plus the unit base, totaling $2N-1$. Its work is $\Theta(N)$ despite having logarithmic depth. A depth factor cannot simply multiply the top toll when later tolls shrink geometrically. For exact values, both the lower limit of the sum and the initial seed are retained.

$$U_n=2^{n+1}-1.$$

**Evaluate the requested index, rather than just its order.** Substituting $n=8$ yields $511$, so option 3 is correct. Direct step-by-step iteration from the declared seed provides the same number; the accompanying ledger includes each multiplication, local toll and accumulated total.

Option 1 gives $2048$, which differs from the independently evaluated exact value $511$. Option 2 gives $9$, which differs from the independently evaluated exact value $511$. Option 4 gives $256$, which differs from the independently evaluated exact value $511$. The precise finite correction and the initial value decide this numerical question; selecting merely the right asymptotic class would not distinguish the listed integers.

### Solution 30

**Derive the exact expression and its domain.** Unroll the one-child recurrence without a multiplicity factor: $U_n=1+\sum_{j=1}^n2^j$. The finite geometric sum equals $2^{n+1}-2$, giving $U_n=2^{n+1}-1$. The sequence begins $1,3,7,15$. Substitution verifies $(2^n-1)+2^n=2^{n+1}-1$ and the zero-index seed is one. If these indices represent input sizes $N=2^n$, the chain contains tolls $N,N/2,\ldots,2$ plus the unit base, totaling $2N-1$. Its work is $\Theta(N)$ despite having logarithmic depth. A depth factor cannot simply multiply the top toll when later tolls shrink geometrically. For exact values, both the lower limit of the sum and the initial seed are retained.

$$U_n=2^{n+1}-1.$$

**Diagnose the symbolic alternatives.** Option 2 is the exact expression. $n+1$ assumes unit cost at every call; $2^n$ counts only the largest toll; $n2^n$ treats every toll as equal to the largest. Each invalid expression either fails the stated seed, fails the step equation, or drops a nonzero exact contribution. Checking a proposed formula against both conditions is a complete test for this one-step initial-value problem. The animation gives two independently evaluated indices, five and eight; those illustrations supplement the algebraic proof rather than replace it.

### Solution 31

**Derive the exact expression and its domain.** Unroll the one-child recurrence without a multiplicity factor: $U_n=1+\sum_{j=1}^n2^j$. The finite geometric sum equals $2^{n+1}-2$, giving $U_n=2^{n+1}-1$. The sequence begins $1,3,7,15$. Substitution verifies $(2^n-1)+2^n=2^{n+1}-1$ and the zero-index seed is one. If these indices represent input sizes $N=2^n$, the chain contains tolls $N,N/2,\ldots,2$ plus the unit base, totaling $2N-1$. Its work is $\Theta(N)$ despite having logarithmic depth. A depth factor cannot simply multiply the top toll when later tolls shrink geometrically. For exact values, both the lower limit of the sum and the initial seed are retained.

$$U_n=2^{n+1}-1.$$

**Check the statement about applicability.** The correct statement distinguishes one-child accounting from two-child accounting. A chain has one node at depth $j$, whereas a full binary tree has $2^j$ nodes. The same decreasing per-node linear toll therefore gives decreasing aggregate cost in the chain but constant aggregate cost in the tree. The unit base affects the exact total by one; discarding it would produce $2^{n+1}-2$. Halving the argument alone does not determine the answer without the child multiplicity. The correct option is 1. The two finite illustrations are checks of this proof; their agreement is not used to infer a formula for all positive indices. The same mathematical recurrence must always be accompanied by its seed and by the relationship, if any, between its index and the original input size.

### Solution 32

**Derive the exact expression and its domain.** Unroll the exact chain to obtain $U_n=1+\sum_{j=1}^n j^2$. The sum-of-squares identity gives $U_n=1+n(n+1)(2n+1)/6$. A direct proof adds $(n+1)^2$ to the polynomial at index $n$ and obtains the polynomial at index $n+1$; the zero seed is one. Values at indices zero through three are $1,2,6,15$. The leading term is $n^3/3$, so accumulation raises the squared index toll to cubic order. If this sequence comes from $N=2^n$ and toll $(\log_2N)^2$ along a halving chain, its original-size order is $\Theta(\log^3N)$. Without that change of variable, its order in the stated index is $\Theta(n^3)$. Both interpretations have the same exact index values but different input labels.

$$U_n=1+\frac{n(n+1)(2n+1)}6.$$

**Evaluate the requested index, rather than just its order.** Substituting $n=5$ yields $56$, so option 3 is correct. Direct step-by-step iteration from the declared seed provides the same number; the accompanying ledger includes each multiplication, local toll and accumulated total.

Option 1 gives $125$, which differs from the independently evaluated exact value $56$. Option 2 gives $26$, which differs from the independently evaluated exact value $56$. Option 4 gives $55$, which differs from the independently evaluated exact value $56$. The precise finite correction and the initial value decide this numerical question; selecting merely the right asymptotic class would not distinguish the listed integers.

### Solution 33

**Derive the exact expression and its domain.** Unroll the exact chain to obtain $U_n=1+\sum_{j=1}^n j^2$. The sum-of-squares identity gives $U_n=1+n(n+1)(2n+1)/6$. A direct proof adds $(n+1)^2$ to the polynomial at index $n$ and obtains the polynomial at index $n+1$; the zero seed is one. Values at indices zero through three are $1,2,6,15$. The leading term is $n^3/3$, so accumulation raises the squared index toll to cubic order. If this sequence comes from $N=2^n$ and toll $(\log_2N)^2$ along a halving chain, its original-size order is $\Theta(\log^3N)$. Without that change of variable, its order in the stated index is $\Theta(n^3)$. Both interpretations have the same exact index values but different input labels.

$$U_n=1+\frac{n(n+1)(2n+1)}6.$$

**Evaluate the requested index, rather than just its order.** Substituting $n=8$ yields $205$, so option 2 is correct. Direct step-by-step iteration from the declared seed provides the same number; the accompanying ledger includes each multiplication, local toll and accumulated total.

Option 1 gives $65$, which differs from the independently evaluated exact value $205$. Option 3 gives $204$, which differs from the independently evaluated exact value $205$. Option 4 gives $512$, which differs from the independently evaluated exact value $205$. The precise finite correction and the initial value decide this numerical question; selecting merely the right asymptotic class would not distinguish the listed integers.

### Solution 34

**Derive the exact expression and its domain.** Unroll the exact chain to obtain $U_n=1+\sum_{j=1}^n j^2$. The sum-of-squares identity gives $U_n=1+n(n+1)(2n+1)/6$. A direct proof adds $(n+1)^2$ to the polynomial at index $n$ and obtains the polynomial at index $n+1$; the zero seed is one. Values at indices zero through three are $1,2,6,15$. The leading term is $n^3/3$, so accumulation raises the squared index toll to cubic order. If this sequence comes from $N=2^n$ and toll $(\log_2N)^2$ along a halving chain, its original-size order is $\Theta(\log^3N)$. Without that change of variable, its order in the stated index is $\Theta(n^3)$. Both interpretations have the same exact index values but different input labels.

$$U_n=1+\frac{n(n+1)(2n+1)}6.$$

**Diagnose the symbolic alternatives.** Option 1 is the exact expression. $n(n+1)(2n+1)/6$ drops the seed one; $n^3$ has the wrong exact leading coefficient and lower terms; $n^2+1$ counts only the current squared toll and the base. Each invalid expression either fails the stated seed, fails the step equation, or drops a nonzero exact contribution. Checking a proposed formula against both conditions is a complete test for this one-step initial-value problem. The animation gives two independently evaluated indices, five and eight; those illustrations supplement the algebraic proof rather than replace it.

### Solution 35

**Derive the exact expression and its domain.** Unroll the exact chain to obtain $U_n=1+\sum_{j=1}^n j^2$. The sum-of-squares identity gives $U_n=1+n(n+1)(2n+1)/6$. A direct proof adds $(n+1)^2$ to the polynomial at index $n$ and obtains the polynomial at index $n+1$; the zero seed is one. Values at indices zero through three are $1,2,6,15$. The leading term is $n^3/3$, so accumulation raises the squared index toll to cubic order. If this sequence comes from $N=2^n$ and toll $(\log_2N)^2$ along a halving chain, its original-size order is $\Theta(\log^3N)$. Without that change of variable, its order in the stated index is $\Theta(n^3)$. Both interpretations have the same exact index values but different input labels.

$$U_n=1+\frac{n(n+1)(2n+1)}6.$$

**Check the statement about applicability.** The correct statement requires transforming the interpretation of the solution back to the original variable. A cubic polynomial in $n=\log_2N$ becomes a cubic logarithm in $N$, not a cubic polynomial in $N$. The sum of $n$ squared-index tolls has cubic order, so preserving quadratic order is false. Changing variables never permits removal of the base value; here it remains one and distinguishes this family from the otherwise identical zero-seed family. The correct option is 4. The two finite illustrations are checks of this proof; their agreement is not used to infer a formula for all positive indices. The same mathematical recurrence must always be accompanied by its seed and by the relationship, if any, between its index and the original input size.

### Solution 36

**Derive the exact expression and its domain.** The decrementing argument visits every integer from $n$ through one, so $T_n=\sum_{j=1}^n j^2$. Expanding the known finite sum gives $T_n=n^3/3+n^2/2+n/6$. Its successive difference is exactly $n^2$, and its zero value is zero, proving that it solves the specified initial-value problem. The first four values are $0,1,5,14$. The leading term gives $\Theta(n^3)$ in the original input size; no logarithmic transformation was specified. A second lower bound keeps the final half of the squared-index summands: at least a positive multiple of $n$ terms are each a positive multiple of $n^2$. The upper bound uses $n$ summands each at most $n^2$. These matching bounds independently confirm the cubic order.

$$T_n=\frac{n(n+1)(2n+1)}6.$$

**Evaluate the requested index, rather than just its order.** Substituting $n=5$ yields $55$, so option 4 is correct. Direct step-by-step iteration from the declared seed provides the same number; the accompanying ledger includes each multiplication, local toll and accumulated total.

Option 1 gives $125$, which differs from the independently evaluated exact value $55$. Option 2 gives $25$, which differs from the independently evaluated exact value $55$. Option 3 gives $15$, which differs from the independently evaluated exact value $55$. The precise finite correction and the initial value decide this numerical question; selecting merely the right asymptotic class would not distinguish the listed integers.

### Solution 37

**Derive the exact expression and its domain.** The decrementing argument visits every integer from $n$ through one, so $T_n=\sum_{j=1}^n j^2$. Expanding the known finite sum gives $T_n=n^3/3+n^2/2+n/6$. Its successive difference is exactly $n^2$, and its zero value is zero, proving that it solves the specified initial-value problem. The first four values are $0,1,5,14$. The leading term gives $\Theta(n^3)$ in the original input size; no logarithmic transformation was specified. A second lower bound keeps the final half of the squared-index summands: at least a positive multiple of $n$ terms are each a positive multiple of $n^2$. The upper bound uses $n$ summands each at most $n^2$. These matching bounds independently confirm the cubic order.

$$T_n=\frac{n(n+1)(2n+1)}6.$$

**Evaluate the requested index, rather than just its order.** Substituting $n=8$ yields $204$, so option 3 is correct. Direct step-by-step iteration from the declared seed provides the same number; the accompanying ledger includes each multiplication, local toll and accumulated total.

Option 1 gives $64$, which differs from the independently evaluated exact value $204$. Option 2 gives $36$, which differs from the independently evaluated exact value $204$. Option 4 gives $512$, which differs from the independently evaluated exact value $204$. The precise finite correction and the initial value decide this numerical question; selecting merely the right asymptotic class would not distinguish the listed integers.

### Solution 38

**Derive the exact expression and its domain.** The decrementing argument visits every integer from $n$ through one, so $T_n=\sum_{j=1}^n j^2$. Expanding the known finite sum gives $T_n=n^3/3+n^2/2+n/6$. Its successive difference is exactly $n^2$, and its zero value is zero, proving that it solves the specified initial-value problem. The first four values are $0,1,5,14$. The leading term gives $\Theta(n^3)$ in the original input size; no logarithmic transformation was specified. A second lower bound keeps the final half of the squared-index summands: at least a positive multiple of $n$ terms are each a positive multiple of $n^2$. The upper bound uses $n$ summands each at most $n^2$. These matching bounds independently confirm the cubic order.

$$T_n=\frac{n(n+1)(2n+1)}6.$$

**Diagnose the symbolic alternatives.** Option 2 is the exact expression. $n(n+1)/2$ sums linear rather than squared tolls; $n^3$ is the root toll times depth and is not the finite exact sum; $n^2$ counts only the root toll. Each invalid expression either fails the stated seed, fails the step equation, or drops a nonzero exact contribution. Checking a proposed formula against both conditions is a complete test for this one-step initial-value problem. The animation gives two independently evaluated indices, five and eight; those illustrations supplement the algebraic proof rather than replace it.

### Solution 39

**Derive the exact expression and its domain.** The decrementing argument visits every integer from $n$ through one, so $T_n=\sum_{j=1}^n j^2$. Expanding the known finite sum gives $T_n=n^3/3+n^2/2+n/6$. Its successive difference is exactly $n^2$, and its zero value is zero, proving that it solves the specified initial-value problem. The first four values are $0,1,5,14$. The leading term gives $\Theta(n^3)$ in the original input size; no logarithmic transformation was specified. A second lower bound keeps the final half of the squared-index summands: at least a positive multiple of $n$ terms are each a positive multiple of $n^2$. The upper bound uses $n$ summands each at most $n^2$. These matching bounds independently confirm the cubic order.

$$T_n=\frac{n(n+1)(2n+1)}6.$$

**Check the statement about applicability.** The correct scope statement rejects the standard Master theorem for the subtract-one argument. Its fixed-ratio assumption $n/b$ with constant $b>1$ is absent. The recursion depth is exactly $n$ nonbase steps, rather than logarithmic depth. The root contributes $n^2$ but is only one term of the required finite sum. Unrolling or a difference equation supplies both exactness and a valid proof. The correct option is 1. The two finite illustrations are checks of this proof; their agreement is not used to infer a formula for all positive indices. The same mathematical recurrence must always be accompanied by its seed and by the relationship, if any, between its index and the original input size.

### Solution 40

**Derive the exact expression and its domain.** After dividing by $2^n$, put $V_n=U_n/2^n$. Then $V_n=V_{n-1}+n/2^n$ and $V_0=0$. Therefore $V_n=\sum_{j=1}^n j/2^j=2-(n+2)/2^n$, giving $U_n=2^{n+1}-n-2$. The finite identity follows either by subtracting its half-shifted sum or by induction. The sequence starts $0,1,4,11$, and substitution gives $2(2^n-n-1)+n=2^{n+1}-n-2$. The infinite normalized sum tends to two, but the finite tail is $(n+2)/2^n$ and cannot be discarded in an exact calculation. If the original input is $N=2^n$, the final order is $\Theta(N)$ even though the per-node toll is logarithmic. Branch multiplicity weights the tolls by their depths; it does not create an extra logarithmic factor in every case.

$$U_n=2^{n+1}-n-2.$$

**Evaluate the requested index, rather than just its order.** Substituting $n=5$ yields $57$, so option 2 is correct. Direct step-by-step iteration from the declared seed provides the same number; the accompanying ledger includes each multiplication, local toll and accumulated total.

Option 1 gives $63$, which differs from the independently evaluated exact value $57$. Option 3 gives $64$, which differs from the independently evaluated exact value $57$. Option 4 gives $32$, which differs from the independently evaluated exact value $57$. The precise finite correction and the initial value decide this numerical question; selecting merely the right asymptotic class would not distinguish the listed integers.

### Solution 41

**Derive the exact expression and its domain.** After dividing by $2^n$, put $V_n=U_n/2^n$. Then $V_n=V_{n-1}+n/2^n$ and $V_0=0$. Therefore $V_n=\sum_{j=1}^n j/2^j=2-(n+2)/2^n$, giving $U_n=2^{n+1}-n-2$. The finite identity follows either by subtracting its half-shifted sum or by induction. The sequence starts $0,1,4,11$, and substitution gives $2(2^n-n-1)+n=2^{n+1}-n-2$. The infinite normalized sum tends to two, but the finite tail is $(n+2)/2^n$ and cannot be discarded in an exact calculation. If the original input is $N=2^n$, the final order is $\Theta(N)$ even though the per-node toll is logarithmic. Branch multiplicity weights the tolls by their depths; it does not create an extra logarithmic factor in every case.

$$U_n=2^{n+1}-n-2.$$

**Evaluate the requested index, rather than just its order.** Substituting $n=8$ yields $502$, so option 1 is correct. Direct step-by-step iteration from the declared seed provides the same number; the accompanying ledger includes each multiplication, local toll and accumulated total.

Option 2 gives $512$, which differs from the independently evaluated exact value $502$. Option 3 gives $256$, which differs from the independently evaluated exact value $502$. Option 4 gives $511$, which differs from the independently evaluated exact value $502$. The precise finite correction and the initial value decide this numerical question; selecting merely the right asymptotic class would not distinguish the listed integers.

### Solution 42

**Derive the exact expression and its domain.** After dividing by $2^n$, put $V_n=U_n/2^n$. Then $V_n=V_{n-1}+n/2^n$ and $V_0=0$. Therefore $V_n=\sum_{j=1}^n j/2^j=2-(n+2)/2^n$, giving $U_n=2^{n+1}-n-2$. The finite identity follows either by subtracting its half-shifted sum or by induction. The sequence starts $0,1,4,11$, and substitution gives $2(2^n-n-1)+n=2^{n+1}-n-2$. The infinite normalized sum tends to two, but the finite tail is $(n+2)/2^n$ and cannot be discarded in an exact calculation. If the original input is $N=2^n$, the final order is $\Theta(N)$ even though the per-node toll is logarithmic. Branch multiplicity weights the tolls by their depths; it does not create an extra logarithmic factor in every case.

$$U_n=2^{n+1}-n-2.$$

**Diagnose the symbolic alternatives.** Option 4 is the exact expression. $2^{n+1}$ drops the entire finite-tail correction; $2^n$ is an incorrect normalized limit and does not satisfy the recurrence; $2^{n+1}-1$ uses a constant toll in the index instead of toll $n$. Each invalid expression either fails the stated seed, fails the step equation, or drops a nonzero exact contribution. Checking a proposed formula against both conditions is a complete test for this one-step initial-value problem. The animation gives two independently evaluated indices, five and eight; those illustrations supplement the algebraic proof rather than replace it.

### Solution 43

**Derive the exact expression and its domain.** After dividing by $2^n$, put $V_n=U_n/2^n$. Then $V_n=V_{n-1}+n/2^n$ and $V_0=0$. Therefore $V_n=\sum_{j=1}^n j/2^j=2-(n+2)/2^n$, giving $U_n=2^{n+1}-n-2$. The finite identity follows either by subtracting its half-shifted sum or by induction. The sequence starts $0,1,4,11$, and substitution gives $2(2^n-n-1)+n=2^{n+1}-n-2$. The infinite normalized sum tends to two, but the finite tail is $(n+2)/2^n$ and cannot be discarded in an exact calculation. If the original input is $N=2^n$, the final order is $\Theta(N)$ even though the per-node toll is logarithmic. Branch multiplicity weights the tolls by their depths; it does not create an extra logarithmic factor in every case.

$$U_n=2^{n+1}-n-2.$$

**Check the statement about applicability.** The correct statement retains finite-sum corrections. Replacing the sum by its infinite limit yields $2^{n+1}$ instead of the exact $2^{n+1}-n-2$. The zero seed fixes the homogeneous contribution and is essential. A logarithmic local toll with two half-size children does not automatically create $N\log N$ work; the weighted finite sum here is of linear order in $N$. At index five, the correction is seven, producing 57 rather than 64. The correct option is 3. The two finite illustrations are checks of this proof; their agreement is not used to infer a formula for all positive indices. The same mathematical recurrence must always be accompanied by its seed and by the relationship, if any, between its index and the original input size.

### Solution 44

**Derive the exact expression and its domain.** Shift by one: $V_n=U_n+1$ satisfies $V_n=2V_{n-1}$ with $V_0=1$. Thus $V_n=2^n$ and $U_n=2^n-1$. Alternatively, a full two-child tree of depth $n$ has $2^j$ unit-toll internal nodes at depth $j<n$, so its internal work is $\sum_{j=0}^{n-1}2^j=2^n-1$. Its leaf seed is zero, so it adds no leaf work in this stated abstract model. The first four values are $0,1,3,7$. At original input size $N=3^n$, the exponent is not one: $2^n=N^{\log_3 2}$. Consequently the original-size tight class is $\Theta(N^{\log_3 2})$. The two children and the shrink factor three are independent parameters. Substitution of the exact expression verifies both the step equation and the base.

$$U_n=2^n-1.$$

**Evaluate the requested index, rather than just its order.** Substituting $n=5$ yields $31$, so option 3 is correct. Direct step-by-step iteration from the declared seed provides the same number; the accompanying ledger includes each multiplication, local toll and accumulated total.

Option 1 gives $5$, which differs from the independently evaluated exact value $31$. Option 2 gives $32$, which differs from the independently evaluated exact value $31$. Option 4 gives $242$, which differs from the independently evaluated exact value $31$. The precise finite correction and the initial value decide this numerical question; selecting merely the right asymptotic class would not distinguish the listed integers.

### Solution 45

**Derive the exact expression and its domain.** Shift by one: $V_n=U_n+1$ satisfies $V_n=2V_{n-1}$ with $V_0=1$. Thus $V_n=2^n$ and $U_n=2^n-1$. Alternatively, a full two-child tree of depth $n$ has $2^j$ unit-toll internal nodes at depth $j<n$, so its internal work is $\sum_{j=0}^{n-1}2^j=2^n-1$. Its leaf seed is zero, so it adds no leaf work in this stated abstract model. The first four values are $0,1,3,7$. At original input size $N=3^n$, the exponent is not one: $2^n=N^{\log_3 2}$. Consequently the original-size tight class is $\Theta(N^{\log_3 2})$. The two children and the shrink factor three are independent parameters. Substitution of the exact expression verifies both the step equation and the base.

$$U_n=2^n-1.$$

**Evaluate the requested index, rather than just its order.** Substituting $n=8$ yields $255$, so option 2 is correct. Direct step-by-step iteration from the declared seed provides the same number; the accompanying ledger includes each multiplication, local toll and accumulated total.

Option 1 gives $256$, which differs from the independently evaluated exact value $255$. Option 3 gives $6560$, which differs from the independently evaluated exact value $255$. Option 4 gives $8$, which differs from the independently evaluated exact value $255$. The precise finite correction and the initial value decide this numerical question; selecting merely the right asymptotic class would not distinguish the listed integers.

### Solution 46

**Derive the exact expression and its domain.** Shift by one: $V_n=U_n+1$ satisfies $V_n=2V_{n-1}$ with $V_0=1$. Thus $V_n=2^n$ and $U_n=2^n-1$. Alternatively, a full two-child tree of depth $n$ has $2^j$ unit-toll internal nodes at depth $j<n$, so its internal work is $\sum_{j=0}^{n-1}2^j=2^n-1$. Its leaf seed is zero, so it adds no leaf work in this stated abstract model. The first four values are $0,1,3,7$. At original input size $N=3^n$, the exponent is not one: $2^n=N^{\log_3 2}$. Consequently the original-size tight class is $\Theta(N^{\log_3 2})$. The two children and the shrink factor three are independent parameters. Substitution of the exact expression verifies both the step equation and the base.

$$U_n=2^n-1.$$

**Diagnose the symbolic alternatives.** Option 1 is the exact expression. $3^n-1$ confuses shrink factor three with child count two; $n$ counts only one internal node per depth; $2^n$ adds an unrequested unit to the exact zero-seed total. Each invalid expression either fails the stated seed, fails the step equation, or drops a nonzero exact contribution. Checking a proposed formula against both conditions is a complete test for this one-step initial-value problem. The animation gives two independently evaluated indices, five and eight; those illustrations supplement the algebraic proof rather than replace it.

### Solution 47

**Derive the exact expression and its domain.** Shift by one: $V_n=U_n+1$ satisfies $V_n=2V_{n-1}$ with $V_0=1$. Thus $V_n=2^n$ and $U_n=2^n-1$. Alternatively, a full two-child tree of depth $n$ has $2^j$ unit-toll internal nodes at depth $j<n$, so its internal work is $\sum_{j=0}^{n-1}2^j=2^n-1$. Its leaf seed is zero, so it adds no leaf work in this stated abstract model. The first four values are $0,1,3,7$. At original input size $N=3^n$, the exponent is not one: $2^n=N^{\log_3 2}$. Consequently the original-size tight class is $\Theta(N^{\log_3 2})$. The two children and the shrink factor three are independent parameters. Substitution of the exact expression verifies both the step equation and the base.

$$U_n=2^n-1.$$

**Check the statement about applicability.** The correct statement separates branch count from shrink factor. There are two children per node even though each child input is divided by three. The exponent $\log_3 2$ is a positive noninteger, which is perfectly valid in asymptotic notation. The index growth is a base-two exponential, while the original input itself is a base-three exponential in that index. Swapping these two quantities gives the wrong answer and the wrong growth exponent. The correct option is 4. The two finite illustrations are checks of this proof; their agreement is not used to infer a formula for all positive indices. The same mathematical recurrence must always be accompanied by its seed and by the relationship, if any, between its index and the original input size.

### Solution 48

**Derive the exact expression and its domain.** The original sizes are $N=2^{2^n}$. Taking a square root changes $2^n$ to $2^{n-1}$, so it decreases the index $n$ by one. The original base-two logarithmic toll is $\log_2N=2^n$. Normalize the given cost by that toll: $V_n=U_n/2^n$ gives $V_n=V_{n-1}+1$ with $V_0=1$. Hence $U_n=(n+1)2^n$. Its values at indices zero through three are $1,4,12,32$. Here index zero means original input two, not input one or zero. Returning to the original variable gives $2^n=\log_2N$ and $n=\log_2\log_2N$, so the exact grid expression is $(1+\log_2\log_2N)\log_2N$. The tight class is $\Theta(\log N\log\log N)$, and the grid avoids rounding issues because every recursive square root is exact until its declared base.

$$U_n=(n+1)2^n.$$

**Evaluate the requested index, rather than just its order.** Substituting $n=5$ yields $192$, so option 4 is correct. Direct step-by-step iteration from the declared seed provides the same number; the accompanying ledger includes each multiplication, local toll and accumulated total.

Option 1 gives $160$, which differs from the independently evaluated exact value $192$. Option 2 gives $1024$, which differs from the independently evaluated exact value $192$. Option 3 gives $63$, which differs from the independently evaluated exact value $192$. The precise finite correction and the initial value decide this numerical question; selecting merely the right asymptotic class would not distinguish the listed integers.

### Solution 49

**Derive the exact expression and its domain.** The original sizes are $N=2^{2^n}$. Taking a square root changes $2^n$ to $2^{n-1}$, so it decreases the index $n$ by one. The original base-two logarithmic toll is $\log_2N=2^n$. Normalize the given cost by that toll: $V_n=U_n/2^n$ gives $V_n=V_{n-1}+1$ with $V_0=1$. Hence $U_n=(n+1)2^n$. Its values at indices zero through three are $1,4,12,32$. Here index zero means original input two, not input one or zero. Returning to the original variable gives $2^n=\log_2N$ and $n=\log_2\log_2N$, so the exact grid expression is $(1+\log_2\log_2N)\log_2N$. The tight class is $\Theta(\log N\log\log N)$, and the grid avoids rounding issues because every recursive square root is exact until its declared base.

$$U_n=(n+1)2^n.$$

**Evaluate the requested index, rather than just its order.** Substituting $n=8$ yields $2304$, so option 3 is correct. Direct step-by-step iteration from the declared seed provides the same number; the accompanying ledger includes each multiplication, local toll and accumulated total.

Option 1 gives $65536$, which differs from the independently evaluated exact value $2304$. Option 2 gives $511$, which differs from the independently evaluated exact value $2304$. Option 4 gives $2048$, which differs from the independently evaluated exact value $2304$. The precise finite correction and the initial value decide this numerical question; selecting merely the right asymptotic class would not distinguish the listed integers.

### Solution 50

**Derive the exact expression and its domain.** The original sizes are $N=2^{2^n}$. Taking a square root changes $2^n$ to $2^{n-1}$, so it decreases the index $n$ by one. The original base-two logarithmic toll is $\log_2N=2^n$. Normalize the given cost by that toll: $V_n=U_n/2^n$ gives $V_n=V_{n-1}+1$ with $V_0=1$. Hence $U_n=(n+1)2^n$. Its values at indices zero through three are $1,4,12,32$. Here index zero means original input two, not input one or zero. Returning to the original variable gives $2^n=\log_2N$ and $n=\log_2\log_2N$, so the exact grid expression is $(1+\log_2\log_2N)\log_2N$. The tight class is $\Theta(\log N\log\log N)$, and the grid avoids rounding issues because every recursive square root is exact until its declared base.

$$U_n=(n+1)2^n.$$

**Diagnose the symbolic alternatives.** Option 2 is the exact expression. $2^{n+1}-1$ counts a single child rather than two; $n2^n$ drops all unit base leaves; $4^n$ assigns the transformed recurrence four children instead of two. Each invalid expression either fails the stated seed, fails the step equation, or drops a nonzero exact contribution. Checking a proposed formula against both conditions is a complete test for this one-step initial-value problem. The animation gives two independently evaluated indices, five and eight; those illustrations supplement the algebraic proof rather than replace it.

### Solution 51

**Derive the exact expression and its domain.** The original sizes are $N=2^{2^n}$. Taking a square root changes $2^n$ to $2^{n-1}$, so it decreases the index $n$ by one. The original base-two logarithmic toll is $\log_2N=2^n$. Normalize the given cost by that toll: $V_n=U_n/2^n$ gives $V_n=V_{n-1}+1$ with $V_0=1$. Hence $U_n=(n+1)2^n$. Its values at indices zero through three are $1,4,12,32$. Here index zero means original input two, not input one or zero. Returning to the original variable gives $2^n=\log_2N$ and $n=\log_2\log_2N$, so the exact grid expression is $(1+\log_2\log_2N)\log_2N$. The tight class is $\Theta(\log N\log\log N)$, and the grid avoids rounding issues because every recursive square root is exact until its declared base.

$$U_n=(n+1)2^n.$$

**Check the statement about applicability.** The correct statement rejects a fixed input shrink ratio for a square root. Its ratio to the current input is $1/\sqrt N$, which varies with that input. The useful fixed halving occurs in $m=\log_2N$, and the useful decrement occurs in $n=\log_2m$. A logarithm of the transformed variable is therefore a double logarithm of the original variable. Confusing these steps would replace the correct logarithmic complexity by an unrelated polynomial or exponential class. The correct option is 1. The two finite illustrations are checks of this proof; their agreement is not used to infer a formula for all positive indices. The same mathematical recurrence must always be accompanied by its seed and by the relationship, if any, between its index and the original input size.

### Solution 52

**Use a potential that measures the actual amount of shrinking.** Let $n_{j+1}=n_j-\lceil\sqrt{n_j}\rceil$ for integer $n_j>1$, and stop at zero or one. The child is nonnegative and strictly smaller, so this process is well defined. Define potential $P(n)=\sqrt n$. One step decreases it by
$$P(n)-P(n-d)=\frac{d}{\sqrt n+\sqrt{n-d}},\qquad d=\lceil\sqrt n\rceil.$$
Because $\sqrt n\le d<\sqrt n+1$, the decrement is at least $1/2$ and at most $1+1/\sqrt n<2$ for every integer $n>1$. If there are $h$ nonbase steps, their potential decrements telescope. The final potential is at most one, so
$$\frac{\sqrt n-1}{2}<h\le2\sqrt n.$$
These constants establish $h\in\Theta(\sqrt n)$. Each step has unit toll and the terminal cost is bounded, giving $T(n)\in\Theta(\sqrt n)$, option 2.

The actual chain starting at 100 is $100,90,80,71,62,54,46,39,32,26,20,15,11,7,4,2,0$, with sixteen nonbase steps. It is a numerical witness, not the proof of the asymptotic order. The ceiling matters for exact checkpoints and is retained in the animation.

Option 1 assumes geometric shrinking and logarithmic depth, which the potential calculation refutes. Option 3 assumes only a constant amount is removed per step and overstates the depth. Option 4 additionally multiplies that overestimate by a nonexistent logarithmic toll. The equal-ratio Master theorem is unavailable because the shrink ratio depends on the input. The potential proof handles the rounding directly rather than discarding it as harmless without justification.

### Solution 53

**Count the work actually executed after reuse.** The two calls refer to the identical subproblem, including its state and required output; size equality alone would not suffice. Once the first result is stored, the second use performs only a bounded lookup rather than another recursive computation. For exact powers of two, let the base cost be $c>0$ and the local cost be exactly $n$. The executed recurrence is therefore
$$T(n)=T(n/2)+n.$$
Unrolling its single chain gives
$$T(n)=c+n+\frac n2+\cdots+2=c+2n-2.$$
For a unit seed and input 32, the total is 63. Positive root work supplies $\Omega(n)$, and the geometric sum supplies $O(n)$, proving $\Theta(n)$, option 2. A bounded lookup per level adds only $O(\log n)$ and does not change the class.

If both calls were executed afresh, the recurrence would instead be $2T(n/2)+n$, with constant aggregate toll per depth and $\Theta(n\log n)$ work. Option 3 describes that unreused implementation. Option 1 counts just the number of depth levels and ignores the root's compulsory linear work. Option 4 is also too large: the actual geometric toll sum is bounded by twice the input, plus the base contribution.

The distinction concerns total work, not just stack depth. A reused dependency graph can preserve logarithmic depth while greatly reducing executed nodes. The solution assumes result storage and lookup fit the stated cost model; if copying a large result costs linear time, add that cost explicitly. Most importantly, two different subproblems of equal size cannot automatically share an answer. The animation marks the reused dependency as a reference, distinguishes it from an executed edge, and displays the actual single-chain cost ledger.
