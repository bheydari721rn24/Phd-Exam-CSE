### 25. A repeated root carries an independent polynomial mode

Solve $a_n=4a_{n-1}-4a_{n-2}$ with $a_0=1,a_1=6$. Determine $a_5$.

#### Solution

The polynomial is $(r-2)^2$, so the complete solution is $(A+Bn)2^n$. At zero, $A=1$; at one, $2(A+B)=6$, so $B=2$. Thus $a_n=(1+2n)2^n$, and $a_5=11\cdot32=352$. Substitution cancels the affine polynomial's second difference, confirming the recurrence identity. Using $A2^n+B2^n$ would collapse to one amplitude and predict $a_1=2a_0$, which is not the supplied six. A repeated polynomial root counts its multiplicity through independent index factors, not repeated labels on the same exponential mode.

### 26. A triple root and three boundary equations

Let $a_n=6a_{n-1}-12a_{n-2}+8a_{n-3}$ for $n\ge3$, with $a_0=1,a_1=8,a_2=36$. Find $a_6$.

#### Solution

The polynomial is $(r-2)^3$. Write $a_n=(A+Bn+Cn^2)2^n$. The boundary equations give $A=1$, $A+B+C=4$, and $A+2B+4C=9$. Hence $B+C=3$ and $B+2C=4$, so $C=1,B=2$. The formula is $(n+1)^2 2^n$, giving $a_6=49\cdot64=3136$. A degree-two polynomial has zero third finite difference, which independently verifies that the triple repeated shift factor annihilates the formula. Fitting only two starting values would leave one free parameter and could not establish this exact sequence.

### 27. A repeated root together with a distinct root

Solve $a_n=5a_{n-1}-7a_{n-2}+3a_{n-3}$, $a_0=4,a_1=12,a_2=32$.

#### Solution

Factor the polynomial as $(r-1)^2(r-3)$. The three independent modes give $a_n=A+Bn+C3^n$. At zero, $A+C=4$; at one, $A+B+3C=12$; at two, $A+2B+9C=32$. Subtracting the first equation gives $B+2C=8$ and $2B+8C=28$. Consequently $C=3,B=2,A=1$, so $a_n=1+2n+3^{n+1}$. Each term is annihilated by one factor of the polynomial with the required multiplicity. The linear mode associated with root one should not be confused with a particular solution: the recurrence here is homogeneous.

### 28. Zero roots require impulses rather than zero powers

Let $a_n=0$ for $n\ge2$, with $a_0=4,a_1=7$. Explain why the expressions $A0^n+Bn0^n$ cannot represent the sequence, and supply a valid representation.

#### Solution

Even if $0^0=1$ is assigned, the second proposed mode is zero at every index: at zero its factor $n$ is zero, and at positive indices its factor $0^n$ is zero. The first mode can only affect index zero, so no value of $B$ produces seven at index one. The correct representation is $a_n=4\delta_{n,0}+7\delta_{n,1}$. The two impulse sequences are independent and supply the two arbitrary prefix values, while the tail is zero. This is an order-two equation with polynomial $z^2$, but the familiar nonzero repeated-root formula has an assumption that cannot be removed by an informal power convention.

### 29. A zero-root prefix attached to an exponential tail

Let $a_0=4,a_1=5,a_2=6$, and $a_n=2a_{n-1}$ only for $n\ge3$. Describe the full solution and its formal order-three polynomial.

#### Solution

The tail beginning at two is $6\cdot2^{n-2}$, or $(3/2)2^n$. That extension would predict $3/2$ at zero and three at one. Correct those two values with impulses: $a_n=(3/2)2^n+(5/2)\delta_{n,0}+2\delta_{n,1}$. The normalized order-three polynomial is $z^3-2z^2=z^2(z-2)$. Its two zero factors represent prefix freedom; its nonzero factor controls the tail. The recurrence is not imposed at indices one or two, so arbitrary prefix data are consistent. This gives three independent parameters before the supplied values are fitted, matching the dimension of the initial triple.

### 30. Complex roots can produce a simple periodic sequence

Solve $a_n=-a_{n-2}$ with $a_0=1,a_1=0$, and compute $a_{2027}$.

#### Solution

The characteristic polynomial is $r^2+1$, with roots $i,-i$. A real representation is $a_n=A\cos(n\pi/2)+B\sin(n\pi/2)$. The data give $A=1,B=0$, so the sequence repeats $1,0,-1,0$. Since 2027 is congruent to three modulo four, the requested term is zero. Directly shifting by two negates each cosine value, verifying the recurrence. Complex roots do not mean complex final values when the coefficients and boundary data are real; conjugate modes combine into real trigonometric terms. Taking only their magnitudes would destroy the periodic signs and zeroes.

### 31. Growing oscillations and a conjugate pair

Solve $a_n=-2a_{n-1}-2a_{n-2}$ with $a_0=1,a_1=-1$. Is $|a_n|$ bounded below by a positive multiple of $(\sqrt2)^n$ for all large $n$?

#### Solution

The roots are $-1+i,-1-i$, of modulus $\sqrt2$ and angles plus or minus $3\pi/4$. The data select $a_n=(\sqrt2)^n\cos(3n\pi/4)$. At one this gives negative one, and the recurrence follows from the characteristic roots. For indices congruent to two modulo four, the cosine is zero. Hence no positive lower bound of the proposed kind holds at every sufficiently large index. An upper bound by $(\sqrt2)^n$ is valid. On some other subsequences the magnitude has that exponential order. An oscillatory leading mode needs a domain-aware statement rather than an unconditional positive Theta claim.

### 32. Recover a minimal recurrence from a proposed sequence

For $a_n=2^n+n3^n$, find a constant-coefficient homogeneous recurrence of minimal order.

#### Solution

The mode $2^n$ requires the factor $E-2$, and $n3^n$ requires $(E-3)^2$. The minimal polynomial is $(z-2)(z-3)^2=z^3-8z^2+21z-18$. Thus $a_n=8a_{n-1}-21a_{n-2}+18a_{n-3}$ for $n\ge3$, with $a_0=1,a_1=5,a_2=22$. Minimality follows from the independence of nonzero exponential-polynomial modes: a single factor at three cannot annihilate its degree-one coefficient, and removing the factor at two leaves the nonzero other mode. The sequence's visibly two summands therefore require order three, not order two.

### 33. Constant forcing resonant with a double root

Solve $a_n-2a_{n-1}+a_{n-2}=1$ with $a_0=0,a_1=1$.

#### Solution

The homogeneous polynomial is $(r-1)^2$, giving $A+Bn$. The constant forcing uses exponential base one, whose multiplicity is two; choose a particular $Kn^2$. Its backward second difference is $2K$, so $K=1/2$. Fit the complete expression $A+Bn+n^2/2$: index zero gives $A=0$, and index one gives $B=1/2$. Therefore $a_n=n(n+1)/2$. The first difference is $n$, whose difference is one, confirming the equation independently. A linear particular trial would be annihilated and cannot produce the forcing; it is the multiplicity, not the forcing's degree, that necessitates the quadratic term.

### 34. Exponential forcing at a double nonunit root

Let $a_n-4a_{n-1}+4a_{n-2}=2^n$, $a_0=a_1=0$. Find the exact solution.

#### Solution

Normalize by $2^n$ and let $u_n=a_n/2^n$. Then $u_n-2u_{n-1}+u_{n-2}=1$. Its zero bases give $u_n=n(n-1)/2$, because the backward second difference of that expression is one and it vanishes at zero and one. Therefore $a_n=n(n-1)2^{n-1}$. The same result follows from the general form $(A+Bn+Cn^2)2^n$: the residual is $2C2^n$, so $C=1/2$, and the bases determine $A=0,B=-1/2$. At two, the value is four, matching the first forced update. Forgetting either the normalization shift or the double resonance leads to a wrong coefficient.

### 35. Linear polynomial forcing with a resonant unit root

Solve $a_n=3a_{n-1}-2a_{n-2}+n$ for $n\ge2$, with $a_0=a_1=0$.

#### Solution

The roots are one and two. Since the polynomial forcing has base one and that root is simple, try $p_n=An^2+Bn$. Direct substitution into $p_n-3p_{n-1}+2p_{n-2}$ gives $-2An+5A-B$. Match it to $n$, obtaining $A=-1/2,B=-5/2$. Add $C+D2^n$. At zero, $C+D=0$; at one, $C+2D=3$, so $D=3,C=-3$. The answer is $a_n=3\cdot2^n-3-(n^2+5n)/2$. At two this is two, agreeing with the original equation. Fit the constants after adding the particular term; the zero boundary values do not imply a zero solution in a forced recurrence.

### 36. Polynomial times a nonresonant exponential

Solve $a_n=2a_{n-1}+n3^n$ with $a_0=0$.

#### Solution

Use $p_n=(An+B)3^n$. Substitution gives the normalized residual $(A/3)n+(B+2A)/3$, so matching $n$ yields $A=3,B=-6$. Add $C2^n$ and fit zero: $C=6$. Thus $a_n=(3n-6)3^n+6\cdot2^n$. At one the value is three, and at two it is twenty-four, agreeing with two successive updates. The trial must include both a linear and a constant coefficient even though the forcing has no constant term: shifting $n$ to $n-1$ generates a lower-degree term that must cancel. Trying only $An3^n$ misses that cancellation.

### 37. Mixed forcing and a separate boundary fit

Solve $a_n=2a_{n-1}+3^n+5n$, $a_0=0$.

#### Solution

The two forcing parts can be treated independently. For $3^n$, the particular term is $3^{n+1}$. For $5n$, try $Bn+C$: its residual is $-Bn+2B-C$, so $B=-5,C=-10$. The general answer is $D2^n+3^{n+1}-5n-10$. At zero, $D+3-10=0$, giving $D=7$. Thus $a_n=7\cdot2^n+3^{n+1}-5n-10$. Index one gives eight, which equals the direct forcing $3+5$. This reconstructs Oxford's mixed-forcing method with an independently verified boundary calculation. Adding particular terms is justified by linearity; the initial conditions belong to their full sum with the homogeneous term.

### 38. A third-order equation from a counting-course pattern

Find the general solution of $a_n=2a_{n-1}+5a_{n-2}-6a_{n-3}$. Then impose $a_0=0,a_1=7,a_2=-3$.

#### Solution

The polynomial $r^3-2r^2-5r+6$ factors as $(r-1)(r-3)(r+2)$. Hence $a_n=A+B3^n+C(-2)^n$. The boundaries give $A+B+C=0$, $A+3B-2C=7$, and $A+9B+4C=-3$. Subtracting the first equation yields $2B-3C=7$ and $8B+3C=-3$, so $B=2/5,C=-31/15,A=5/3$. The exact answer is $(25+6\cdot3^n-31(-2)^n)/15$. Integer bases and recurrence coefficients ensure integer later values even though the modal amplitudes are rational. This is a reconstructed Berkeley higher-order pattern with new boundary data and a complete independent fit.

### 39. A step forcing starts later than the sequence

Let $a_0=0$ and $a_n=2a_{n-1}+q_n$, where $q_n=0$ for $n<4$ and $q_n=1$ for $n\ge4$. Find $a_{10}$.

#### Solution

The first three updates are zero. At four the value becomes one. The unrolled formula includes contributions only from $j=4$ through ten: $a_{10}=\sum_{j=4}^{10}2^{10-j}=2^7-1=127$. In general, $a_n=0$ before four and $a_n=2^{n-3}-1$ from four onward. Treating the forcing as present since one would incorrectly produce $2^{10}-1$. A particular solution for a globally constant forcing cannot be extended across a step discontinuity without the correct piecewise boundary. The contribution interpretation automatically includes the actual activation time.

### 40. A correct bound can resist a weak induction

Let $H_n=2H_{n-1}+1$, $H_0=0$. The true bound $H_n\le2^n$ seems to fail under direct substitution. Repair the proof and obtain the exact answer.

#### Solution

The weak induction hypothesis yields $H_{n+1}\le2\cdot2^n+1$, which is too large to establish $2^{n+1}$. This does not disprove the bound; it shows the hypothesis lacks slack. Strengthen it to the exact formula $H_n=2^n-1$, or the upper bound $H_n\le2^n-1$. At zero the formula is correct. Substitution gives $2(2^n-1)+1=2^{n+1}-1$, closing the induction. Therefore the stronger statement holds and implies the original bound. This reconstructs the MIT verification pattern without copying its narrative; a failed proof step should be diagnosed separately from the truth of the target statement.

### 41. Binary strings avoiding consecutive ones

How many binary strings of length twelve have no adjacent ones? Derive the recurrence, bases, and exact count.

#### Solution

Let $B_n$ count such strings. A string ending in zero comes from any valid length-$n-1$ prefix. A string ending in one, for $n\ge2$, has a suffix zero-one; removing that pair leaves any valid length-$n-2$ prefix. The two endings are disjoint and the append operations are reversible, so $B_n=B_{n-1}+B_{n-2}$. The empty string contributes one, and both one-bit strings are allowed, giving $B_0=1,B_1=2$. Hence $B_n=F_{n+2}$ and $B_{12}=F_{14}=377$. A Fibonacci answer without specifying this two-index shift would not distinguish the string model from domino tilings.

### 42. No two identical restricted ternary symbols

For strings over $\{0,1,2\}$, forbid adjacent zeroes and adjacent ones, but allow adjacent twos. Find the number of valid length-six strings.

#### Solution

Let $u_n$ count strings ending in zero; symmetry gives the same count for endings in one. Let $v_n$ count endings in two. Then $u_n=u_{n-1}+v_{n-1}$, because zero can follow one or two, and $v_n=2u_{n-1}+v_{n-1}$, because two can follow any allowed ending. Start with $u_1=v_1=1$. The successive pairs are $(1,1),(2,3),(5,7),(12,17),(29,41),(70,99)$. Total length six is $2\cdot70+99=239$. The total recurrence is $T_n=2T_{n-1}+T_{n-2}$ with $T_0=1,T_1=3$. This reconstructs Berkeley's state-counting pattern; treating all identical adjacent symbols as forbidden would instead count a different language.

### 43. A generalized alphabet restriction

An alphabet has $q\ge2$ symbols and one distinguished symbol $X$. Count length-$n$ strings with no adjacent $X$ symbols by deriving a total recurrence and its first values.

#### Solution

Let $A_n$ end in $X$ and $B_n$ end in a non-$X$ symbol. Then $A_n=B_{n-1}$ and $B_n=(q-1)(A_{n-1}+B_{n-1})$. For $T_n=A_n+B_n$, this gives $T_n=(q-1)(T_{n-1}+T_{n-2})$ for $n\ge2$, with $T_0=1,T_1=q$. At two, it gives $(q-1)(q+1)=q^2-1$, which also follows by removing the one forbidden word $XX$ from all pairs. At three it gives $(q-1)(q^2+q-1)$. The multiplier $q-1$ counts available ordinary symbols; using $q$ would accidentally permit another $X$ in the forbidden transition.

### 44. Ordered colored payments

Let two distinct unit tokens and one five-unit token be available without limit, and let order matter. Find the number of token sequences totaling seven.

#### Solution

The recurrence is $W_n=2W_{n-1}+W_{n-5}$ for positive $n$, with $W_0=1$ and negative-index values zero. Thus $W_1=2,W_2=4,W_3=8,W_4=16,W_5=33,W_6=68,W_7=140$. Independently, either use seven unit tokens, giving $2^7=128$ colorings, or use one five-unit token plus two unit tokens. The latter has three possible positions for the five-unit token and four colorings of the two others, giving twelve. Their sum is 140. Two five-unit tokens are impossible at total seven. This reconstructed Berkeley pattern checks both the recurrence and the semantic assumption that token order is significant.

### 45. An exact domino count with a geometric split

How many domino tilings cover a $2\times8$ board? Explain why the two-horizontal case must consume two complete columns.

#### Solution

In the leftmost column, a vertical domino fills both cells and leaves a $2\times7$ board. If the top-left cell is covered horizontally, the bottom-left cell cannot be filled vertically because the top-left cell is occupied; it must also be covered horizontally. Together the two dominoes fill the first two columns and leave a $2\times6$ board. The cases are disjoint and reversible, giving $T_n=T_{n-1}+T_{n-2}$ with $T_0=T_1=1$. Therefore $T_8=F_9=34$. Removing only one horizontal domino would leave an irregular boundary and would not justify a simple width-one reduction.

### 46. A missing-cell board changes the state

Can the ordinary $2\times n$ domino recurrence count tilings of a board with its top-left cell removed? Explain and determine the count.

#### Solution

The altered board has $2n-1$ cells, an odd number, while every domino covers two. Therefore its tiling count is zero for every positive $n$. The ordinary recurrence assumes a complete rectangular boundary and cannot be applied after deleting a cell without redefining the state. This parity argument is stronger and faster than any recurrence calculation. If two cells were removed instead, area parity alone would no longer settle the problem; color balance or boundary-state analysis could be needed. The lesson is to check invariant feasibility before importing a recurrence from a visually similar model.

### 47. Compositions into odd parts

Let $C_n$ count ordered compositions of $n$ into positive odd parts, with the empty composition at zero. Find a rational generating function and the count at seven.

#### Solution

The allowed single-part series is $x+x^3+x^5+\cdots=x/(1-x^2)$. A sequence of such parts has generating function $1/(1-x/(1-x^2))=(1-x^2)/(1-x-x^2)$. Coefficient comparison gives $C_0=1,C_1=1,C_2=1$, and $C_n=C_{n-1}+C_{n-2}$ for $n\ge3$. Thus the positive-index sequence is $1,1,2,3,5,8,13$, giving $C_7=13$. The numerator changes the early correction: imposing the Fibonacci update at two with $C_0=C_1=1$ would wrongly give two. The formal-series construction is valid because every coefficient receives contributions from finitely many compositions.

### 48. A two-state transfer with weighted transitions

A counting model has states $U,V$ and update $(U_{n+1},V_{n+1})=(U_n+2V_n,3U_n)$, starting at $(U_0,V_0)=(1,0)$. Find a scalar recurrence for $U_n$ and compute $U_5$.

#### Solution

For positive $n$, substitute $V_n=3U_{n-1}$ into the first update to get $U_{n+1}=U_n+6U_{n-1}$. The starting values are $U_0=1,U_1=1$. The polynomial is $r^2-r-6=(r-3)(r+2)$. Solving $A+B=1$ and $3A-2B=1$ gives $A=3/5,B=2/5$. Hence $U_n=(3^{n+1}+2(-2)^n)/5$, and $U_5=(729-64)/5=133$. Direct state updates produce $1,1,7,13,55,133$ for $U$. The transition weight two or three means multiple labeled choices on an edge; it is not a probability unless normalized under a separately specified model.
