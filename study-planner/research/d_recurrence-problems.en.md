# Worked recurrence problems

### 1. A valid formula with the wrong first transition

Let $a_0=7,a_1=2$, and $a_n=3a_{n-1}$ for $n\ge2$. Decide whether $a_n=7\cdot3^n$ is correct, and give the complete sequence formula.

#### Solution

The recurrence is not imposed at index one, so $a_1$ is independent of $a_0$. Starting from index one, repeated multiplication gives $a_n=2\cdot3^{n-1}$ for $n\ge1$. The full answer is this tail together with $a_0=7$. The proposed expression predicts twenty-one at index one, while the supplied value is two; satisfying the tail equation alone cannot correct that failure. A unified form is $a_n=(2/3)3^n+(19/3)\delta_{n,0}$. The impulse affects only the unconstrained first term. This problem illustrates why reducing effective order must preserve the original starting index.

### 2. One omitted base case invalidates an induction

For $a_n=4a_{n-1}-3a_{n-2}$, $a_0=a_1=1$, a proposed proof claims $a_n=3^n$ because the formula satisfies the recurrence and agrees at zero. Identify the flaw and solve the recurrence.

#### Solution

The induction step uses two earlier indices; to begin at two, both indices zero and one must satisfy the proposed statement. At one the claim predicts three, which is false. The characteristic polynomial factors as $(r-1)(r-3)$, so $a_n=A+B3^n$. The data yield $A+B=1$ and $A+3B=1$; subtracting gives $B=0$, hence $A=1$. Thus every term is one. Substituting one into the equation gives $4-3=1$, verifying the tail, and both bases agree. This is a reconstruction of the missing-base-case reasoning pattern in the Cornell reader; the independent solution shows how the erroneous growing mode is eliminated.

### 3. Recover an unknown initial value from a distant term

Let $a_n=2a_{n-1}+3$ for positive $n$, and suppose $a_4=109$. Determine $a_0$ and $a_7$.

#### Solution

Adding three to both sides gives $a_n+3=2(a_{n-1}+3)$. Therefore $a_n=(a_0+3)2^n-3$. At four, $112=16(a_0+3)$, so $a_0=4$. The seventh term is $7\cdot128-3=893$. A backward check gives the intermediate values $4,11,25,53,109$, confirming the recovered boundary. Backward recovery is possible because the coefficient two is nonzero. If it were zero, later terms would contain no information about the earlier value, and a distant observation could not determine $a_0$.

### 4. A well-founded recurrence with a floor

Let $a_0=0$ and $a_n=a_{\lfloor n/2\rfloor}+1$ for positive $n$. Find $a_{1000}$ and prove a formula for all positive indices.

#### Solution

Repeated integer halving reaches zero after the number of binary digits of $n$ steps. That count is $\lfloor\log_2 n\rfloor+1$, so $a_{1000}=10$ because $512\le1000<1024$. For a rigorous proof, if $2^j\le n<2^{j+1}$ with $j\ge1$, then $2^{j-1}\le\lfloor n/2\rfloor<2^j$. Induction on $j$ gives the predecessor value $j$, and the update gives $j+1$. The separate interval $n=1$ gives one directly. The expression is not defined by the same logarithm formula at zero; the specified zero value remains a separate boundary.

### 5. Diagnose insufficient information

Suppose $a_n=5a_{n-1}-6a_{n-2}$ for $n\ge2$ and only $a_0=1$ is specified. Is $a_{10}$ uniquely determined? Express the family in terms of $a_1=t$.

#### Solution

Roots two and three give $a_n=A2^n+B3^n$. The equations $A+B=1$ and $2A+3B=t$ imply $B=t-2$ and $A=3-t$. Consequently $a_{10}=(3-t)1024+(t-2)59049$, which changes with $t$. One boundary value cannot determine an order-two homogeneous equation. The valid answer is a parameterized family, not a guessed extra starting value. For example, $t=2$ gives $2^n$, whereas $t=3$ gives $3^n$, and both agree at zero. Distinguishing these two solutions proves nonuniqueness without any advanced algebra.

### 6. Classify three superficially similar equations

Classify $a_n=n a_{n-1}+1$, $b_n=2b_{n-1}+b_{n-2}^2$, and $T(n)=2T(n/2)+n$. Which supports a fixed consecutive-index characteristic polynomial directly?

#### Solution

The first is linear and nonhomogeneous, but its coefficient depends on the index; unrolling or an integrating factor is appropriate. The second is nonlinear because a previous unknown value is squared; superposition fails. The third is linear in the function $T$, but it refers to a halved argument rather than a fixed lag. None supports the constant-coefficient consecutive-index polynomial directly. If the third equation is restricted to powers of two, define $u_j=T(2^j)$; then $u_j=2u_{j-1}+2^j$, which does support a constant-lag forcing method. The change of variable must include the new boundary and index domain, not merely relabel the old polynomial.

### 7. Subtract prefix sums without losing the first value

Let $a_0=2$ and $a_n=3\sum_{j=0}^{n-1}a_j+1$ for $n\ge1$. Find $a_n$ and $a_5$.

#### Solution

The original first equation gives $a_1=3\cdot2+1=7$. For $n\ge2$, subtracting the equation at $n-1$ leaves $a_n-a_{n-1}=3a_{n-1}$, hence $a_n=4a_{n-1}$. Therefore $a_n=7\cdot4^{n-1}$ for positive $n$, with the exceptional $a_0=2$. At five the value is $7\cdot256=1792$. To verify the original relation, sum the geometric tail up to $n-1$: $2+7(4^{n-1}-1)/3$. Multiplying by three and adding one yields $7\cdot4^{n-1}$. Extending the simplified equation to index one would wrongly give eight instead of seven.

### 8. A symbolic parameter changes uniqueness

Let $p a_{n+1}=a_n$ for $n\ge0$ and $a_0=1$. Discuss the cases $p=0$ and $p\ne0$.

#### Solution

If $p\ne0$, normalization gives $a_{n+1}=a_n/p$, so induction yields $a_n=p^{-n}$. If $p=0$, the equation at zero demands $0=a_0=1$, making the data inconsistent. A formula obtained by dividing by $p$ cannot describe this case. If the boundary had instead been $a_0=0$ with $p=0$, all equations would demand every $a_n=0$, rather than leave the whole sequence arbitrary. The newest-term coefficient is therefore part of existence analysis, not just a convenient denominator. Normalization must be justified before the standard forward recurrence theorem is applied.

### 9. Constant forcing with a shifted fixed point

Solve $a_n=4a_{n-1}-6$ with $a_0=5$. Determine when the sequence would instead remain constant.

#### Solution

The fixed point solves $u=4u-6$, giving $u=2$. Define $b_n=a_n-2$; then $b_n=4b_{n-1}$ and $b_0=3$. Hence $a_n=2+3\cdot4^n$. Substitution gives $4(2+3\cdot4^{n-1})-6=2+3\cdot4^n$, and the zero-index value is five. The constant trajectory occurs exactly when $a_0=2$. The presence of root four in the homogeneous companion does not force every initial condition to grow: at the fixed point its homogeneous amplitude is zero. This same reasoning generalizes to $a_n=pa_{n-1}+q$ when $p\ne1$.

### 10. Resonant first-order forcing

Solve $a_n=3a_{n-1}+2\cdot3^n$ for $n\ge1$, $a_0=4$.

#### Solution

Divide by $3^n$ and set $u_n=a_n/3^n$. The recurrence becomes $u_n=u_{n-1}+2$, with $u_0=4$, hence $u_n=4+2n$. Therefore $a_n=(4+2n)3^n$. Equivalently, unrolling gives $3^n a_0+\sum_{j=1}^n3^{n-j}2\cdot3^j$; every summand is $2\cdot3^n$, so there are $n$ identical contributions. The forcing's exponential base equals the homogeneous root, which explains the extra factor $n$. A trial using only a constant multiple of $3^n$ has zero residual and cannot generate the required forcing.

### 11. Nonresonant first-order forcing

Solve $a_n=2a_{n-1}+5^n$ with $a_0=1$.

#### Solution

Try $p_n=K5^n$. Substitution yields $K=2K/5+1$, so $K=5/3$. Add the homogeneous term $A2^n$ and impose the boundary: $1=A+5/3$, so $A=-2/3$. Thus $a_n=(5^{n+1}-2^{n+1})/3$. At index one this gives seven, agreeing with $2+5$. The apparent fraction produces integers because $5\equiv2$ modulo three, so their equal powers have a difference divisible by three. An exact rational representation does not mean the count itself is fractional. This divisibility check independently supports the algebra and is often useful in a counting interpretation.

### 12. Polynomial forcing through a telescoping normalization

Let $a_n=a_{n-1}+n^2$, $a_0=0$. Derive $a_n$ without guessing a cubic coefficient from a few values.

#### Solution

Unrolling gives $a_n=\sum_{j=1}^n j^2$. To derive its polynomial, use $(j+1)^3-j^3=3j^2+3j+1$ and sum for $j=1,\ldots,n$. The left side telescopes to $(n+1)^3-1$. Substitute $\sum j=n(n+1)/2$ into the right side and solve for the square sum, obtaining $a_n=n(n+1)(2n+1)/6$. The expression vanishes at zero; subtracting its value at $n-1$ gives exactly $n^2$. These two facts, rather than a numerical fit, establish the result for every nonnegative index by uniqueness.

### 13. Alternating forcing and a negative root

Solve $a_n=-a_{n-1}+n$ for positive $n$, with $a_0=0$.

#### Solution

A linear particular term $Bn+C$ gives $Bn+C=-B(n-1)-C+n$, hence $2B=1$ and $2C=B$. Thus $B=1/2,C=1/4$. The homogeneous term is $A(-1)^n$, and the initial value gives $A=-1/4$. Therefore $a_n=n/2+(1-(-1)^n)/4$, equivalently $\lceil n/2\rceil$. For even $n$ the correction is zero; for odd $n$ it is one half, making the expression an integer in both cases. The first values $0,1,1,2,2$ agree with direct updates. Dropping the oscillating mode would miss the exact parity dependence even though the leading linear growth remained correct.

### 14. A factorial integrating factor

Solve $a_n=n a_{n-1}+n!$ with $a_0=2$.

#### Solution

For positive $n$, divide by $n!$ and use $n(n-1)!=n!$. The normalized value $u_n=a_n/n!$ satisfies $u_n=u_{n-1}+1$. Since $0!=1$, $u_0=2$, so $u_n=n+2$. The solution is $a_n=(n+2)n!$. Verify directly: $n(n+1)(n-1)!+n!=(n+2)n!$. A characteristic polynomial with coefficient $n$ would not be constant and would not justify an exponential answer. Here normalization works because every factorial denominator is nonzero, and it removes the changing coefficient exactly rather than approximating it.

### 15. A zero coefficient resets a variable-coefficient recurrence

Let $a_0=9$, $a_1=2a_0+1$, $a_2=0a_1+5$, and $a_n=3a_{n-1}+2$ for $n\ge3$. Find $a_{10}$ and determine whether it depends on $a_0$.

#### Solution

The first step gives nineteen, but the second gives five regardless of any preceding value. From index two, adding one produces $a_n+1=3(a_{n-1}+1)$. Thus $a_n=6\cdot3^{n-2}-1$ for $n\ge2$, and $a_{10}=6\cdot6561-1=39365$. The result does not depend on $a_0$. In the product formula, every contribution from before index two contains the coefficient zero and vanishes. Dividing by a product containing that zero would be invalid; the nondividing unrolled formula handles the reset naturally. The exceptional early values remain part of the sequence even though they no longer influence its tail.

### 16. Period-two variable coefficients

Let $a_0=1$, with $a_n=2a_{n-1}+1$ for odd $n$ and $a_n=3a_{n-1}+1$ for positive even $n$. Find formulas for the even and odd subsequences.

#### Solution

Compose two updates: $a_{2m}=3(2a_{2m-2}+1)+1=6a_{2m-2}+4$. Define $b_m=a_{2m}$ with $b_0=1$. The first-order formula gives $b_m=6^m+4(6^m-1)/5=(9\cdot6^m-4)/5$. Then $a_{2m+1}=2b_m+1=(18\cdot6^m-3)/5$. At $m=0$ these produce one and three, and at $m=1$ they produce ten and twenty-one. The original recurrence has variable coefficients, but grouping a complete coefficient period yields a constant-coefficient equation on each subsequence. Using an average multiplier would lose both exact values and phase information.

### 17. Distinct roots and explicit constants

Solve $a_n=5a_{n-1}-6a_{n-2}$ with $a_0=2,a_1=5$. Find $a_6$.

#### Solution

The characteristic equation is $r^2-5r+6=(r-2)(r-3)=0$. Write $a_n=A2^n+B3^n$. The initial equations $A+B=2$ and $2A+3B=5$ give $B=1,A=1$, so $a_n=2^n+3^n$. At six the answer is $64+729=793$. A substitution check uses $5r-6=r^2$ for each root, so each mode satisfies the equation and their sum does too. This is stronger than checking only index two. The starting equations must use exponents zero and one; substituting the supplied values at one and two would solve a different sequence.

### 18. Starting indices one and two

Let $a_1=1,a_2=3$, and $a_{n+2}=3a_{n+1}-2a_n$ for $n\ge1$. Find the exact formula.

#### Solution

The roots are one and two, so $a_n=A+B2^n$. Using the actual indices gives $A+2B=1$ and $A+4B=3$, hence $B=1,A=-1$. The answer is $a_n=2^n-1$ for positive $n$. Check the two supplied values and substitute the two modes. A formula $2^{n+1}-1$ would already give three at index one and is rejected before any large-index calculation. This is a reconstruction of the Oxford practice pattern; the written answer is fitted independently to the actual stated boundaries. Shifting to $b_m=a_{m+1}$ is also valid, but its formula must be shifted back at the end.

### 19. A dominant root can disappear

For $a_n=4a_{n-1}-3a_{n-2}$, $a_0=2$, determine which $a_1$ makes the sequence bounded and which makes $a_n=2\cdot3^n$.

#### Solution

The general solution is $A+B3^n$. Since $A+B=2$ and $A+3B=a_1$, one has $B=(a_1-2)/2$. Boundedness requires $B=0$, so $a_1=2$ and every term is two. For the pure growing mode, require $A=0,B=2$, giving $a_1=6$. All other real starting values leave a nonzero exponential amplitude; its sign determines whether the tail grows toward positive or negative infinity. Merely seeing the root three does not justify a growth claim until this amplitude is fitted. The bounded case is a one-dimensional set of initial data inside the two-dimensional solution space.

### 20. A stable averaging model

Let $L_n=(L_{n-1}+L_{n-2})/2$ for $n\ge3$, $L_1=100000,L_2=300000$. Find the limit and the exact alternating correction.

#### Solution

The roots are one and negative one half. Use $L_n=C+D(-1/2)^{n-1}$ so the first index is explicit. The equations $C+D=100000$ and $C-D/2=300000$ give $C=700000/3,D=-400000/3$. Therefore the limit is $700000/3$, and the error from that limit alternates while its magnitude halves at each step. The simple average two hundred thousand is not the invariant weighted limit. At three the formula gives two hundred thousand, matching the arithmetic update. This reconstructs Berkeley's averaging pattern with its original boundary indices; it is a deterministic mathematical model, not a forecast about real population dynamics.

### 21. Fibonacci approximation has a rigorous error bound

With $F_0=0,F_1=1$, prove that $F_n$ is the nearest integer to $\phi^n/\sqrt5$ for nonnegative $n$. Explain why this does not validate arbitrary large floating-point evaluation.

#### Solution

The exact root solution gives $F_n=(\phi^n-\psi^n)/\sqrt5$, where $\psi=(1-\sqrt5)/2$ has magnitude below one. Therefore the difference from $\phi^n/\sqrt5$ is $|\psi|^n/\sqrt5\le1/\sqrt5<1/2$. Because $F_n$ is an integer, it is the unique nearest integer. This bound concerns exact real arithmetic. A floating-point calculation introduces an additional error in the power and division, which can exceed one half as values grow. An exact integer recurrence or doubling algorithm avoids that unbounded rounding risk. Confusing a symbolic error bound with a machine arithmetic guarantee is a conceptual mistake.

### 22. Recover an earlier value from two later values

Let $a_n=5a_{n-1}-6a_{n-2}$ and suppose $a_3=35,a_4=97$. Recover $a_0,a_1$.

#### Solution

Backward rearrangement gives $a_{n-2}=(5a_{n-1}-a_n)/6$. Hence $a_2=(175-97)/6=13$, $a_1=(65-35)/6=5$, and $a_0=(25-13)/6=2$. These are the data of the sequence $2^n+3^n$. Backward uniqueness is available because the last coefficient negative six is nonzero over the rationals. It may fail over a modular ring where six is not invertible. The backward computations yield integers here, but integrality is a property to verify, not a general consequence of dividing by six. The fitted root form provides an independent forward check.

### 23. A sum of Fibonacci values from a recurrence identity

Show that $\sum_{j=0}^n F_j=F_{n+2}-1$. Then compute $\sum_{j=0}^{10}F_j$.

#### Solution

For $j\ge0$, the Fibonacci relation rearranges to $F_j=F_{j+2}-F_{j+1}$. Summing telescopes: all middle terms cancel, leaving $F_{n+2}-F_1=F_{n+2}-1$. At ten, $F_{12}=144$, so the sum is 143. The zero-index term is zero and does not change the result, but the subtraction of $F_1=1$ remains essential. Alternatively, the formula has the correct value at zero and its successive difference is $F_n$, proving it by induction. A frequent index error is $F_{n+1}-1$, which already fails for $n=1$.

### 24. Nonconsecutive boundary observations

Suppose $a_n=3a_{n-1}-2a_{n-2}$, $a_0=1,a_2=7$. Determine the sequence and explain why these observations suffice.

#### Solution

Roots one and two give $a_n=A+B2^n$. The observations produce $A+B=1$ and $A+4B=7$, so $B=2,A=-1$. Thus $a_n=2^{n+1}-1$ and $a_1=3$. The observation matrix has determinant $4-1=3$, so it is invertible even though the observations are not consecutive. Not every pair of nonconsecutive observations is sufficient: for roots one and negative one, two even-index observations cannot distinguish the amplitudes because both modes equal one at even indices. Independence of the complete modes does not imply every chosen measurement matrix is invertible.
