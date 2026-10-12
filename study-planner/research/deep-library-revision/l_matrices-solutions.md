## Q1

**Correct option: 2.**

### Model the independent coordinates explicitly

A real symmetric four-by-four matrix has the form

$$S=\begin{pmatrix}d_1&a&b&c\\a&d_2&e&f\\b&e&d_3&g\\c&f&g&d_4\end{pmatrix}.$$

The six off-diagonal coordinates $a,b,c,e,f,g$ are unconstrained; symmetry means each is copied into a second entry, not independently chosen twice. Trace zero means $d_1+d_2+d_3+d_4=0$, so $d_4=-d_1-d_2-d_3$. Thus all admissible matrices are uniquely described by nine real parameters: six off-diagonal entries and three diagonal entries. This unique parameterization proves dimension nine.

A concrete basis is $E_{ij}+E_{ji}$ for $1\le i<j\le4$, together with $E_{11}-E_{44},E_{22}-E_{44},E_{33}-E_{44}$. Every element is symmetric and trace zero. A zero linear combination forces the six off-diagonal coefficients to vanish by inspecting their entries, and then forces the three remaining coefficients to vanish by inspecting the first three diagonal entries. The nine matrices are therefore independent and span the space.

Option 1's ten ignores the trace restriction. Options 3 and 4 remove two or three dimensions instead of the rank-one constraint. Trace zero does not mean zero diagonal: $\operatorname{diag}(1,-1,0,0)$ is a valid nonzero diagonal element. The trace functional has rank one because it takes value one on $E_{11}$; writing equivalent copies of its equation does not create extra rank.

For positive size $n$, the corresponding real dimension is $n(n+1)/2-1$. At $n=1$ the space contains only zero and has dimension zero. At $n=0$, trace is already zero on the zero-dimensional space, so a separate dimension-zero answer is required; subtracting one would be invalid.

### Exact verification ledger


| Parameter family | Independent count | Why |
|---|---|---|
| Off-diagonal symmetric pairs | 6 | Upper and lower entries are linked. |
| Trace-zero diagonal entries | 3 | The fourth cancels the other three. |
| Total | 9 | The two families form an independent basis. |

## Q2

**Correct option: 4.** The number is $336$. The original PDF's first alternative is **37**, correcting an earlier transcription as 32.

### Remove the coupled sum before counting

Subtract the first equation from the second. This is a reversible operation on the two constraints and gives
$$x_1+x_2+x_3=5,\qquad x_4+x_5=15.$$
The variable groups are now disjoint. For a fixed $x_1=t$, the pairs $(x_2,x_3)$ are $(0,5-t),(1,4-t),\ldots,(5-t,0)$, exactly $6-t$ choices. Sum over $t=0,\ldots,5$:
$$6+5+4+3+2+1=21=\binom72.$$
For the second group choose $x_4=s$ with $s=0,\ldots,15$; then $x_5=15-s$ is forced. These are sixteen choices, including both zero endpoints. Every first-group triple can be paired with every second-group pair, and every admissible five-tuple has exactly one such decomposition. This bijection proves the product, rather than an unsupported assumption of independent equations:
$$21\cdot16=336.$$

| Alternative | Exact value | Why it fails |
|---|---:|---|
| Add the two group counts | $21+16=37$ | This counts choosing one group or the other, instead of supplying both. |
| Add unrestricted five-variable count | $\binom{24}{4}+21=10647$ | The unrestricted total-sum equation does not enforce the first-group sum. |
| Multiply that unrestricted count | $\binom{24}{4}\cdot21=223146$ | Each counted object carries an extra choice; it is not one uniquely admissible tuple. |
| Product of the two disjoint-group counts | $336$ | Every allowed tuple is counted once. |

### Why matrix rank does not answer this question

Over the reals, the coefficient rows are independent and the affine solution set has dimension $5-2=3$. That describes continuous degrees of freedom; it is not the cardinality of its nonnegative integer points. The nonnegative boundaries make a finite lattice problem. For totals $r$ and $t$, the same decomposition gives $\binom{r+2}{2}(t-r+1)$ when $0\le r\le t$ are integers, and zero if $t<r$. These domain tests must precede the counting formula. No official answer key is invented: option 4 is independently derived from the original statement.

## Q3

**Correct option: 2.**

The hypothesis controls magnitude, not the sign of a quadratic form. Take $A=-I$ and $\theta=1$. For every vector and every norm, $\Vert Ax\Vert=\Vert-x\Vert=\Vert x\Vert$. Yet for every nonzero real $x$, $x^TAx=-\Vert x\Vert_2^2<0$. Thus positive definiteness does not follow, and option 2 is the false general assertion.

To check option 3, suppose $Ax=0$. The bound gives $0\ge\theta\Vert x\Vert$, and $\theta>0$ forces $x=0$. A square real matrix with a trivial kernel is invertible. This uses squareness: a tall injective rectangular map need not have a two-sided inverse.

For option 1, put $x=A^{-1}y$ in the original inequality. Then $\Vert y\Vert\ge\theta\Vert A^{-1}y\Vert$. Dividing by $\theta\Vert y\Vert$ for $y\ne0$ and taking the supremum yields the corresponding induced operator norm bound

$$\Vert A^{-1}\Vert\le\theta^{-1}.$$

For a real eigenvalue with real eigenvector $v\ne0$, substituting $Av=\lambda v$ directly gives $|\lambda|\ge\theta$. Nonreal eigenvalues need an additional argument because the original vectors are real. With the Euclidean norm, write a complex eigenvector $v=u+iw$ and apply the squared real bound to $u$ and $w$ separately. Adding gives $\Vert Av\Vert_2^2\ge\theta^2\Vert v\Vert_2^2$, hence the same modulus bound.

The conclusion also holds for any finite-dimensional real norm with its induced matrix norm. Set $B=A^{-1}$; then $\Vert B^k\Vert\le\theta^{-k}$. Norm equivalence gives constants $c,C>0$ with $c\Vert x\Vert_2\le\Vert x\Vert\le C\Vert x\Vert_2$ on real vectors. Therefore $\Vert B^k x\Vert_2\le(C/c)\theta^{-k}\Vert x\Vert_2$. Extend this upper Euclidean bound to complex vectors by summing the bounds for real and imaginary parts. For an eigenvalue $\mu$ of $B$, it gives $|\mu|^k\le(C/c)\theta^{-k}$. Taking $k$th roots and letting $k$ grow gives $|\mu|\le\theta^{-1}$, so the eigenvalue $\lambda=1/\mu$ of $A$ has $|\lambda|\ge\theta$. This justifies option 4 without silently imposing a Euclidean norm on the source's unqualified notation.

Finite-dimensional norm equivalence here follows by bounding a norm on the Euclidean unit sphere: continuity follows from the triangle inequality and coordinate expansion, the compact sphere has a finite maximum, and its minimum is positive because a norm vanishes only at zero. The complex argument is an extension of a real norm bound, not an assertion that the original real norm is automatically a complex inner product.

## Q4

**Source ambiguity; intended normalized interpretation: option 3.**

### Read the source hypothesis literally

The original Persian page says “orthogonal basis” and does not explicitly state unit lengths. Orthogonal and orthonormal are different hypotheses. For a nonunit orthogonal basis, the correct orthogonal projection formula is

$$P_Ux=\sum_{k=1}^{n}\frac{\langle u_k,x\rangle}{\langle u_k,u_k\rangle}u_k.$$

The source omits these denominators. To see why this matters, take $U=\operatorname{span}(2,0)$ in $\mathbb R^2$. Its displayed operator is $P_s=\operatorname{diag}(4,0)$, whereas the actual orthogonal projection is $\operatorname{diag}(1,0)$. Applying $P_s$ twice gives $\operatorname{diag}(16,0)$, so option 1's idempotence assertion fails. For $x=(0,1)$, $P_sx=0$ and option 3's inequality is also false. Thus the literal hypothesis does not supply one uniquely false general assertion. No official answer key is asserted here.

If “orthogonal” was intended to include normalization in the source convention, the extra orthonormal hypothesis gives the usual educational answer, option 3. The following proof states that interpretation explicitly rather than silently changing the authentic wording.

### Under the orthonormal interpretation

Let $p=Px$ and $r=x-p$. For each basis vector $u_j$, orthonormality gives

$$\langle r,u_j\rangle=\langle x,u_j\rangle-\sum_{k=1}^{n}\langle x,u_k\rangle\langle u_k,u_j\rangle=0.$$

Thus $p\in U$ and $r\perp U$. Pythagoras proves $\Vert x\Vert_2^2=\Vert Px\Vert_2^2+\Vert x-Px\Vert_2^2$. The universally valid direction is $\Vert Px\Vert_2\le\Vert x\Vert_2$, with equality precisely when $x\in U$. The reverse inequality fails on a proper subspace: for $U=\operatorname{span}(1,0)$ and $x=(0,1)$, it reads $1\le0$.

Linearity of the coefficient functionals gives option 4, and outputs lie in $U$ by construction. For $x\in U$, the orthonormal expansion recovers $x$, proving option 2 and the stronger $Px=x$. Applying this fact to $Px\in U$ proves $P^2=P$, option 1.

**Full-space boundary.** The source allows $n=m$. With an orthonormal basis of the entire space, $P=I$, so option 3 holds with equality and all four assertions hold for that particular configuration. It is false as a general projection theorem, not false for every possible subspace or vector.

Finally, idempotence alone does not imply contraction: $Q=\begin{pmatrix}1&2\\0&0\end{pmatrix}$ has $Q^2=Q$ but sends $(0,1)$ to $(2,0)$. Orthogonality supplies the norm decomposition; a projection must be identified by its actual geometry and formula.


### Exact verification ledger


| Hypothesis | Displayed sum idempotent? | Reverse norm inequality |
|---|---|---|
| Literal nonunit orthogonal basis | Not generally; $u=(2,0)$ disproves it. | Not generally; a perpendicular input disproves it. |
| Orthonormal basis of a proper subspace | Yes | Fails on a nonzero perpendicular vector. |
| Orthonormal basis of the full space | Yes; $P=I$ | Equality for every vector. |

## Q5

**Correct option: 2.**

The source matrix is $A=(1-a)I+a\mathbf1\mathbf1^T$ in three dimensions. Every real vector can be written uniquely as $x=s\mathbf1+z$, with $s=(x_1+x_2+x_3)/3$ and $z_1+z_2+z_3=0$. The two terms are orthogonal. Expanding the quadratic form gives

$$x^TAx=3(1+2a)s^2+(1-a)\Vert z\Vert_2^2.$$

If $a\ge1$, choose nonzero $z=(1,-1,0)$ and $s=0$; the form is nonpositive. If $a\le-1/2$, choose $s=1,z=0$; again the form is nonpositive. Thus strict positive definiteness requires $1-a>0$ and $1+2a>0$.

Conversely, if both coefficients are positive, every nonzero $x$ has either $s\ne0$ or $z\ne0$, and the displayed sum is strictly positive. This proves sufficiency directly, without importing an unexplained eigenvalue criterion. The exact interval is $-1/2<a<1$, option 2.

Option 1 permits, for example, $a=-3/4$, where the all-equal direction gives $3(1+2a)=-3/2$. Option 3 unnecessarily rejects $a=3/4$, where both coefficients are positive. Option 4 unnecessarily rejects $a=-1/4$, also valid, and excludes $a=0$, the identity matrix. At $a=-1/2$, the all-equal line is null; at $a=1$, the sum-zero plane is null. Both endpoints are positive semidefinite but not positive definite. Outside the closed interval, a direction of negative quadratic form exists.

For $n\ge2$ with the analogous real symmetric matrix, the decomposition yields coefficients $1+(n-1)a$ and $1-a$, hence strict range $-1/(n-1)<a<1$. At $n=1$, there are no off-diagonal entries: the matrix is simply $(1)$ and places no restriction on the unused parameter. The special dimension-one case must not be inferred by dividing by zero in the general endpoint.

## Q6

**Correct option: 4.**

### Construct the result from the defining map

Let $q=(1,\ldots,1)^T$ and $J=qq^T$. For every vector $x$,
$$Jx=\left(\sum_{i=1}^n x_i\right)q,\qquad Jq=nq.$$
Write $x=sq+z$ with $s=(\sum_i x_i)/n$ and $\sum_i z_i=0$. This decomposition is unique because the all-equal line intersects the sum-zero subspace only at zero over the real field. The vectors $e_i-e_n$, $1\le i<n$, form a basis of the latter: their first $n-1$ coordinates prove independence and reconstruct every sum-zero vector. In this adapted basis, $I+J$ is diagonal with entries $n+1,1,\ldots,1$. Consequently
$$\det(I+J)=(n+1)\cdot1^{n-1}=n+1.$$
The determinant's invariance under an invertible basis change follows from multiplicativity: $\det(S^{-1}MS)=\det(S)^{-1}\det(M)\det(S)$. We are not multiplying the diagonal of the original dense matrix. All of its diagonal entries are two, whose product $2^n$ is generally wrong.

A direct inverse provides an independent structural check. Since $J^2=nJ$,
$$\left(I+J\right)\left(I-\frac{J}{n+1}\right)=I+J-\frac{J}{n+1}-\frac{nJ}{n+1}=I.$$
The reverse product agrees because these factors are polynomials in $J$. Thus singularity of the addend $J$ for $n>1$ does not make $I+J$ singular.

### Exact answer, competing options, and boundary

At $n=5$, the adapted-basis entries are $6,1,1,1,1$, so the determinant is 6, option 4. The alternatives 32, 5 and 1 respectively multiply the original diagonal, omit the added identity on the all-equal line, or ignore that line's changed scale. A matrix can have every displayed diagonal entry equal to two yet determinant six; the other entries participate in its volume transformation.

## Q7

**Correct option: 3.**

### Construct the result from the defining map

Let $q=(1,\ldots,1)^T$ and $J=qq^T$. For every vector $x$,
$$Jx=\left(\sum_{i=1}^n x_i\right)q,\qquad Jq=nq.$$
Write $x=sq+z$ with $s=(\sum_i x_i)/n$ and $\sum_i z_i=0$. This decomposition is unique because the all-equal line intersects the sum-zero subspace only at zero over the real field. The vectors $e_i-e_n$, $1\le i<n$, form a basis of the latter: their first $n-1$ coordinates prove independence and reconstruct every sum-zero vector. In this adapted basis, $I+J$ is diagonal with entries $n+1,1,\ldots,1$. Consequently
$$\det(I+J)=(n+1)\cdot1^{n-1}=n+1.$$
The determinant's invariance under an invertible basis change follows from multiplicativity: $\det(S^{-1}MS)=\det(S)^{-1}\det(M)\det(S)$. We are not multiplying the diagonal of the original dense matrix. All of its diagonal entries are two, whose product $2^n$ is generally wrong.

A direct inverse provides an independent structural check. Since $J^2=nJ$,
$$\left(I+J\right)\left(I-\frac{J}{n+1}\right)=I+J-\frac{J}{n+1}-\frac{nJ}{n+1}=I.$$
The reverse product agrees because these factors are polynomials in $J$. Thus singularity of the addend $J$ for $n>1$ does not make $I+J$ singular.

### Exact answer, competing options, and boundary

At $n=8$, the adapted-basis entries are $9$ and seven ones. Their product is 9, option 3. The distractors 8, 1 and 256 are the all-ones eigenvalue without the identity shift, the unchanged complementary scale alone, and $2^8$ from an unjustified original-diagonal rule. Checking the action on $q$ distinguishes the first two errors without any eight-by-eight expansion.

## Q8

**Correct option: 2.**

### Construct the result from the defining map

Let $q=(1,\ldots,1)^T$ and $J=qq^T$. For every vector $x$,
$$Jx=\left(\sum_{i=1}^n x_i\right)q,\qquad Jq=nq.$$
Write $x=sq+z$ with $s=(\sum_i x_i)/n$ and $\sum_i z_i=0$. This decomposition is unique because the all-equal line intersects the sum-zero subspace only at zero over the real field. The vectors $e_i-e_n$, $1\le i<n$, form a basis of the latter: their first $n-1$ coordinates prove independence and reconstruct every sum-zero vector. In this adapted basis, $I+J$ is diagonal with entries $n+1,1,\ldots,1$. Consequently
$$\det(I+J)=(n+1)\cdot1^{n-1}=n+1.$$
The determinant's invariance under an invertible basis change follows from multiplicativity: $\det(S^{-1}MS)=\det(S)^{-1}\det(M)\det(S)$. We are not multiplying the diagonal of the original dense matrix. All of its diagonal entries are two, whose product $2^n$ is generally wrong.

A direct inverse provides an independent structural check. Since $J^2=nJ$,
$$\left(I+J\right)\left(I-\frac{J}{n+1}\right)=I+J-\frac{J}{n+1}-\frac{nJ}{n+1}=I.$$
The reverse product agrees because these factors are polynomials in $J$. Thus singularity of the addend $J$ for $n>1$ does not make $I+J$ singular.

### Exact answer, competing options, and boundary

The expression is $n+1$, option 2, for every positive integer $n$. At $n=1$, $I+J=[2]$, so the formula gives two; the empty sum-zero component causes no problem. For the more general $\alpha I+\beta J$ with $n\ge2$, the determinant is $\alpha^{n-1}(\alpha+n\beta)$. If either factor vanishes, an actual invariant subspace is killed. At $n=1$, only the scalar $\alpha+\beta$ matters, so requiring $\alpha\ne0$ separately would be unnecessarily restrictive.

## Q9

**Correct option: 1.**

### Construct the result from the defining map

Let $q=(1,\ldots,1)^T$ and $J=qq^T$. For every vector $x$,
$$Jx=\left(\sum_{i=1}^n x_i\right)q,\qquad Jq=nq.$$
Write $x=sq+z$ with $s=(\sum_i x_i)/n$ and $\sum_i z_i=0$. This decomposition is unique because the all-equal line intersects the sum-zero subspace only at zero over the real field. The vectors $e_i-e_n$, $1\le i<n$, form a basis of the latter: their first $n-1$ coordinates prove independence and reconstruct every sum-zero vector. In this adapted basis, $I+J$ is diagonal with entries $n+1,1,\ldots,1$. Consequently
$$\det(I+J)=(n+1)\cdot1^{n-1}=n+1.$$
The determinant's invariance under an invertible basis change follows from multiplicativity: $\det(S^{-1}MS)=\det(S)^{-1}\det(M)\det(S)$. We are not multiplying the diagonal of the original dense matrix. All of its diagonal entries are two, whose product $2^n$ is generally wrong.

A direct inverse provides an independent structural check. Since $J^2=nJ$,
$$\left(I+J\right)\left(I-\frac{J}{n+1}\right)=I+J-\frac{J}{n+1}-\frac{nJ}{n+1}=I.$$
The reverse product agrees because these factors are polynomials in $J$. Thus singularity of the addend $J$ for $n>1$ does not make $I+J$ singular.

### Exact answer, competing options, and boundary

The corrected option 1 states a guarantee: triangular structure makes the diagonal-product determinant valid, while arbitrary matrices have no such guarantee. It must not say triangularity is necessary. The nontriangular matrix $\begin{pmatrix}1&1&1\\0&1&1\\1&0&2\end{pmatrix}$ has determinant $2$ and diagonal product $2$. This coincidence does not prove a general rule. A rank-one update leaves the $n-1$ sum-zero directions unchanged here, refuting option 3. Taking $n=2$ gives $I+J=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ with determinant three, refuting the original-diagonal assertion and the claim of unavoidable singularity.

## Q10

**Correct option: 1.**

### Construct the result from the defining map

Write the shear as $S=I+N$, where
$$S=\begin{pmatrix}1&n\\0&1\end{pmatrix},\qquad N=\begin{pmatrix}0&n\\0&0\end{pmatrix},\qquad N^2=0.$$
Both ordered products satisfy $(I+N)(I-N)=(I-N)(I+N)=I-N^2=I$, proving
$$S^{-1}=\begin{pmatrix}1&-n\\0&1\end{pmatrix}.$$
On a vector $(x,y)^T$, the first map outputs $(x+ny,y)^T$; the inverse must subtract precisely the same multiple of the unchanged second coordinate. This explains the negative upper-right entry geometrically. Entrywise reciprocation is unrelated to undoing a map and is already undefined at the zero entries of this invertible matrix.

More generally, a nilpotent matrix $N$ with $N^r=0$ gives a finite inverse polynomial
$$ (I+N)^{-1}=\sum_{j=0}^{r-1}(-1)^jN^j.$$
Multiplication cancels adjacent terms and leaves $I+(-1)^{r-1}N^r=I$ in either order. No infinite geometric-series convergence assumption is used. If $N^3=0$ rather than $N^2=0$, the extra $N^2$ term is necessary; simply negating all off-diagonal entries can fail.

### Exact answer, competing options, and boundary

At $n=5$, the answer is $-5$, option 1. Substituting the candidates into an alleged inverse $X=\begin{pmatrix}1&t\\0&1\end{pmatrix}$ gives $(SX)_{12}=5+t$. Values $5,1/5,0$ leave $10,26/5,5$, respectively; only $t=-5$ makes this entry zero. The reverse product has the same scalar sum, so both sides are certified.

## Q11

**Correct option: 4.**

### Construct the result from the defining map

Write the shear as $S=I+N$, where
$$S=\begin{pmatrix}1&n\\0&1\end{pmatrix},\qquad N=\begin{pmatrix}0&n\\0&0\end{pmatrix},\qquad N^2=0.$$
Both ordered products satisfy $(I+N)(I-N)=(I-N)(I+N)=I-N^2=I$, proving
$$S^{-1}=\begin{pmatrix}1&-n\\0&1\end{pmatrix}.$$
On a vector $(x,y)^T$, the first map outputs $(x+ny,y)^T$; the inverse must subtract precisely the same multiple of the unchanged second coordinate. This explains the negative upper-right entry geometrically. Entrywise reciprocation is unrelated to undoing a map and is already undefined at the zero entries of this invertible matrix.

More generally, a nilpotent matrix $N$ with $N^r=0$ gives a finite inverse polynomial
$$ (I+N)^{-1}=\sum_{j=0}^{r-1}(-1)^jN^j.$$
Multiplication cancels adjacent terms and leaves $I+(-1)^{r-1}N^r=I$ in either order. No infinite geometric-series convergence assumption is used. If $N^3=0$ rather than $N^2=0$, the extra $N^2$ term is necessary; simply negating all off-diagonal entries can fail.

### Exact answer, competing options, and boundary

At $n=8$, the answer is $-8$, option 4. The defining inverse equation requires $8+t=0$. The other upper-right candidates $8,1/8,0$ produce $16,65/8,8$. Their signs or reciprocal values have no cancellation interpretation. Check the zero off-diagonal of the product, rather than choosing a visually similar number.

## Q12

**Correct option: 3.**

### Construct the result from the defining map

Write the shear as $S=I+N$, where
$$S=\begin{pmatrix}1&n\\0&1\end{pmatrix},\qquad N=\begin{pmatrix}0&n\\0&0\end{pmatrix},\qquad N^2=0.$$
Both ordered products satisfy $(I+N)(I-N)=(I-N)(I+N)=I-N^2=I$, proving
$$S^{-1}=\begin{pmatrix}1&-n\\0&1\end{pmatrix}.$$
On a vector $(x,y)^T$, the first map outputs $(x+ny,y)^T$; the inverse must subtract precisely the same multiple of the unchanged second coordinate. This explains the negative upper-right entry geometrically. Entrywise reciprocation is unrelated to undoing a map and is already undefined at the zero entries of this invertible matrix.

More generally, a nilpotent matrix $N$ with $N^r=0$ gives a finite inverse polynomial
$$ (I+N)^{-1}=\sum_{j=0}^{r-1}(-1)^jN^j.$$
Multiplication cancels adjacent terms and leaves $I+(-1)^{r-1}N^r=I$ in either order. No infinite geometric-series convergence assumption is used. If $N^3=0$ rather than $N^2=0$, the extra $N^2$ term is necessary; simply negating all off-diagonal entries can fail.

### Exact answer, competing options, and boundary

For every positive integer $n$, the upper-right entry is $-n$, option 3. The exact expression also extends to every real or complex shear parameter: the determinant remains one. At $n=0$, the original matrix and its inverse are identity, while the reciprocal distractor is undefined. Thus that distractor's singularity is a defect of the proposed formula, not a singularity of the matrix.

## Q13

**Correct option: 2.**

### Construct the result from the defining map

Write the shear as $S=I+N$, where
$$S=\begin{pmatrix}1&n\\0&1\end{pmatrix},\qquad N=\begin{pmatrix}0&n\\0&0\end{pmatrix},\qquad N^2=0.$$
Both ordered products satisfy $(I+N)(I-N)=(I-N)(I+N)=I-N^2=I$, proving
$$S^{-1}=\begin{pmatrix}1&-n\\0&1\end{pmatrix}.$$
On a vector $(x,y)^T$, the first map outputs $(x+ny,y)^T$; the inverse must subtract precisely the same multiple of the unchanged second coordinate. This explains the negative upper-right entry geometrically. Entrywise reciprocation is unrelated to undoing a map and is already undefined at the zero entries of this invertible matrix.

More generally, a nilpotent matrix $N$ with $N^r=0$ gives a finite inverse polynomial
$$ (I+N)^{-1}=\sum_{j=0}^{r-1}(-1)^jN^j.$$
Multiplication cancels adjacent terms and leaves $I+(-1)^{r-1}N^r=I$ in either order. No infinite geometric-series convergence assumption is used. If $N^3=0$ rather than $N^2=0$, the extra $N^2$ term is necessary; simply negating all off-diagonal entries can fail.

### Exact answer, competing options, and boundary

Option 2 correctly rejects entrywise inversion. At zero shear, the off-diagonal entry is zero but the matrix is identity; this refutes both a supposed need to invert the off-diagonal and the assertion that any zero entry prevents invertibility. At nonzero shear, the product test above refutes reciprocation. The compatible block version $\begin{pmatrix}I_p&C\\0&I_q\end{pmatrix}^{-1}=\begin{pmatrix}I_p&-C\\0&I_q\end{pmatrix}$ permits rectangular $C$; an ordinary inverse of that block may not even be defined.

## Q14

**Correct option: 3.**

### Construct the result from the defining map

Use $D=\operatorname{diag}(1,2,\ldots,n)$ with $n\ge2$ and a permutation matrix $P$ having no fixed coordinate. The entry formula, not a rule about trace multiplicativity, gives
$$ (DP)_{ii}=\sum_kD_{ik}P_{ki}=iP_{ii}.$$
Only $k=i$ survives because $D$ is diagonal. A permutation diagonal entry $P_{ii}$ equals one exactly when the permutation fixes coordinate $i$. Therefore
$$\operatorname{tr}(DP)=\sum_{i:\,P_{ii}=1}i=0.$$
For an arbitrary diagonal weight matrix and arbitrary permutation, the same derivation gives the sum of weights on the fixed coordinates. The no-fixed-coordinate hypothesis is doing real work. Multiplying on the left rescales rows but cannot change a zero diagonal entry into a nonzero one.

Cyclic trace invariance is a different theorem. For compatible rectangular matrices $A,B$,
$$\operatorname{tr}(AB)=\sum_i\sum_j a_{ij}b_{ji}=\sum_j\sum_i b_{ji}a_{ij}=\operatorname{tr}(BA).$$
The scalar terms commute inside the sums; the matrices need not commute. For three factors the allowed operation rotates the entire sequence. It does not allow arbitrary factor swapping or removal.

### Exact answer, competing options, and boundary

At $n=5$, all five diagonal entries of $DP$ are zero, giving option 3. The alternatives $5,25,15$ respectively suggest a coordinate count, a squared size, or $\operatorname{tr}(D)=1+2+3+4+5$. None computes $iP_{ii}$. To audit the premise, write the actual cycle $e_1\mapsto e_2\mapsto\cdots\mapsto e_5\mapsto e_1$; no diagonal entry receives a one.

## Q15

**Correct option: 2.**

### Construct the result from the defining map

Use $D=\operatorname{diag}(1,2,\ldots,n)$ with $n\ge2$ and a permutation matrix $P$ having no fixed coordinate. The entry formula, not a rule about trace multiplicativity, gives
$$ (DP)_{ii}=\sum_kD_{ik}P_{ki}=iP_{ii}.$$
Only $k=i$ survives because $D$ is diagonal. A permutation diagonal entry $P_{ii}$ equals one exactly when the permutation fixes coordinate $i$. Therefore
$$\operatorname{tr}(DP)=\sum_{i:\,P_{ii}=1}i=0.$$
For an arbitrary diagonal weight matrix and arbitrary permutation, the same derivation gives the sum of weights on the fixed coordinates. The no-fixed-coordinate hypothesis is doing real work. Multiplying on the left rescales rows but cannot change a zero diagonal entry into a nonzero one.

Cyclic trace invariance is a different theorem. For compatible rectangular matrices $A,B$,
$$\operatorname{tr}(AB)=\sum_i\sum_j a_{ij}b_{ji}=\sum_j\sum_i b_{ji}a_{ij}=\operatorname{tr}(BA).$$
The scalar terms commute inside the sums; the matrices need not commute. For three factors the allowed operation rotates the entire sequence. It does not allow arbitrary factor swapping or removal.

### Exact answer, competing options, and boundary

At $n=8$, all eight diagonal entries remain zero, so option 2 is correct. The alternatives $64,36,8$ are $n^2$, $\operatorname{tr}(D)$, and $n$. They contain no fixed-coordinate test. If the first coordinate were fixed while the other seven formed a cycle, the trace would instead be one; this nearby construction shows exactly why the hypothesis cannot be omitted.

## Q16

**Correct option: 1.**

### Construct the result from the defining map

Use $D=\operatorname{diag}(1,2,\ldots,n)$ with $n\ge2$ and a permutation matrix $P$ having no fixed coordinate. The entry formula, not a rule about trace multiplicativity, gives
$$ (DP)_{ii}=\sum_kD_{ik}P_{ki}=iP_{ii}.$$
Only $k=i$ survives because $D$ is diagonal. A permutation diagonal entry $P_{ii}$ equals one exactly when the permutation fixes coordinate $i$. Therefore
$$\operatorname{tr}(DP)=\sum_{i:\,P_{ii}=1}i=0.$$
For an arbitrary diagonal weight matrix and arbitrary permutation, the same derivation gives the sum of weights on the fixed coordinates. The no-fixed-coordinate hypothesis is doing real work. Multiplying on the left rescales rows but cannot change a zero diagonal entry into a nonzero one.

Cyclic trace invariance is a different theorem. For compatible rectangular matrices $A,B$,
$$\operatorname{tr}(AB)=\sum_i\sum_j a_{ij}b_{ji}=\sum_j\sum_i b_{ji}a_{ij}=\operatorname{tr}(BA).$$
The scalar terms commute inside the sums; the matrices need not commute. For three factors the allowed operation rotates the entire sequence. It does not allow arbitrary factor swapping or removal.

### Exact answer, competing options, and boundary

The correct symbolic expression is zero, option 1, on the stated $n\ge2$ no-fixed-coordinate domain. At $n=1$, the only permutation is identity and the trace is one, so that parameter does not satisfy the premise. The alternatives $n(n+1)/2,n,n^2$ are not zero for any positive allowed dimension. A generic permutation need not be a derangement; for example, identity gives the full weight sum.

## Q17

**Correct option: 4.**

### Construct the result from the defining map

Use $D=\operatorname{diag}(1,2,\ldots,n)$ with $n\ge2$ and a permutation matrix $P$ having no fixed coordinate. The entry formula, not a rule about trace multiplicativity, gives
$$ (DP)_{ii}=\sum_kD_{ik}P_{ki}=iP_{ii}.$$
Only $k=i$ survives because $D$ is diagonal. A permutation diagonal entry $P_{ii}$ equals one exactly when the permutation fixes coordinate $i$. Therefore
$$\operatorname{tr}(DP)=\sum_{i:\,P_{ii}=1}i=0.$$
For an arbitrary diagonal weight matrix and arbitrary permutation, the same derivation gives the sum of weights on the fixed coordinates. The no-fixed-coordinate hypothesis is doing real work. Multiplying on the left rescales rows but cannot change a zero diagonal entry into a nonzero one.

Cyclic trace invariance is a different theorem. For compatible rectangular matrices $A,B$,
$$\operatorname{tr}(AB)=\sum_i\sum_j a_{ij}b_{ji}=\sum_j\sum_i b_{ji}a_{ij}=\operatorname{tr}(BA).$$
The scalar terms commute inside the sums; the matrices need not commute. For three factors the allowed operation rotates the entire sequence. It does not allow arbitrary factor swapping or removal.

### Exact answer, competing options, and boundary

Option 4 separates cyclic invariance from a false multiplication law. Taking $A=B=I_2$ gives $\operatorname{tr}(AB)=2$ but $\operatorname{tr}(A)\operatorname{tr}(B)=4$, refuting option 1. Replacing identity $P$ by a nontrivial cycle changes $\operatorname{tr}(DP)$ from the positive weight sum to zero, refuting option 2. A two-coordinate swap has no fixed coordinate, refuting option 3. Each counterexample is dimension-compatible and isolates one proposed rule.

## Q18

**Correct option: 2.**

### Construct the result from the defining map

The two factors are $2I_n$ and $3I_n$, so their product is $6I_n$. Every diagonal entry is six and all off-diagonal entries are zero. Thus
$$\det((2I_n)(3I_n))=\det(6I_n)=6^n.$$
This is a legitimate diagonal-product computation because the matrix is diagonal. It can also be derived by determinant multiplicativity: $\det(2I_n)\det(3I_n)=2^n3^n$. No commutation hypothesis is required by determinant multiplicativity, although these particular diagonal factors do commute.

The dimension exponent has a geometric and algebraic meaning. Scaling the whole matrix by $c$ scales each of its $n$ rows. Multilinearity of determinant extracts one scalar from each row:
$$\det(cA)=c^n\det(A).$$
The determinant measures oriented $n$-dimensional volume, while trace adds $n$ diagonal values. Their scaling laws are different: $\operatorname{tr}(cA)=c\operatorname{tr}(A)$. Applying a trace-like factor to determinant discards the independent scaling of all dimensions. When $c=0$ and $n>0$, the zero matrix has determinant zero; when $c<0$, parity of $n$ determines the determinant sign.

### Exact answer, competing options, and boundary

For $n=5$, $6^5=7776$, option 2. The three wrong values are $3^5=243$, $2^5+3^5=32+243=275$, and $6n=30$. They respectively omit the first factor, replace multiplication of determinants by addition, and calculate the trace of $6I_5$. Distinguishing a product from a sum and a determinant from a trace explains each distractor quantitatively.

## Q19

**Correct option: 1.**

### Construct the result from the defining map

The two factors are $2I_n$ and $3I_n$, so their product is $6I_n$. Every diagonal entry is six and all off-diagonal entries are zero. Thus
$$\det((2I_n)(3I_n))=\det(6I_n)=6^n.$$
This is a legitimate diagonal-product computation because the matrix is diagonal. It can also be derived by determinant multiplicativity: $\det(2I_n)\det(3I_n)=2^n3^n$. No commutation hypothesis is required by determinant multiplicativity, although these particular diagonal factors do commute.

The dimension exponent has a geometric and algebraic meaning. Scaling the whole matrix by $c$ scales each of its $n$ rows. Multilinearity of determinant extracts one scalar from each row:
$$\det(cA)=c^n\det(A).$$
The determinant measures oriented $n$-dimensional volume, while trace adds $n$ diagonal values. Their scaling laws are different: $\operatorname{tr}(cA)=c\operatorname{tr}(A)$. Applying a trace-like factor to determinant discards the independent scaling of all dimensions. When $c=0$ and $n>0$, the zero matrix has determinant zero; when $c<0$, parity of $n$ determines the determinant sign.

### Exact answer, competing options, and boundary

For $n=8$, $6^8=1679616$, option 1. The alternatives are $2^8+3^8=256+6561=6817$, $6n=48$, and $3^8=6561$. They make the same three structural errors in different numerical order. The large magnitude is expected: each of eight independent coordinate directions is stretched by six.

## Q20

**Correct option: 4.**

### Construct the result from the defining map

The two factors are $2I_n$ and $3I_n$, so their product is $6I_n$. Every diagonal entry is six and all off-diagonal entries are zero. Thus
$$\det((2I_n)(3I_n))=\det(6I_n)=6^n.$$
This is a legitimate diagonal-product computation because the matrix is diagonal. It can also be derived by determinant multiplicativity: $\det(2I_n)\det(3I_n)=2^n3^n$. No commutation hypothesis is required by determinant multiplicativity, although these particular diagonal factors do commute.

The dimension exponent has a geometric and algebraic meaning. Scaling the whole matrix by $c$ scales each of its $n$ rows. Multilinearity of determinant extracts one scalar from each row:
$$\det(cA)=c^n\det(A).$$
The determinant measures oriented $n$-dimensional volume, while trace adds $n$ diagonal values. Their scaling laws are different: $\operatorname{tr}(cA)=c\operatorname{tr}(A)$. Applying a trace-like factor to determinant discards the independent scaling of all dimensions. When $c=0$ and $n>0$, the zero matrix has determinant zero; when $c<0$, parity of $n$ determines the determinant sign.

### Exact answer, competing options, and boundary

The symbolic answer is $6^n$, option 4. The alternatives $2^n+3^n$, $6n$ and $3^n$ do not follow from determinant multiplication or row multilinearity. At $n=1$, some scalar formulas can coincide accidentally; the theorem must hold for every specified positive dimension. At $n=2$, the determinant is 36 while those three alternatives are 13, 12 and 9, separating all choices.

## Q21

**Correct option: 3.**

### Construct the result from the defining map

The two factors are $2I_n$ and $3I_n$, so their product is $6I_n$. Every diagonal entry is six and all off-diagonal entries are zero. Thus
$$\det((2I_n)(3I_n))=\det(6I_n)=6^n.$$
This is a legitimate diagonal-product computation because the matrix is diagonal. It can also be derived by determinant multiplicativity: $\det(2I_n)\det(3I_n)=2^n3^n$. No commutation hypothesis is required by determinant multiplicativity, although these particular diagonal factors do commute.

The dimension exponent has a geometric and algebraic meaning. Scaling the whole matrix by $c$ scales each of its $n$ rows. Multilinearity of determinant extracts one scalar from each row:
$$\det(cA)=c^n\det(A).$$
The determinant measures oriented $n$-dimensional volume, while trace adds $n$ diagonal values. Their scaling laws are different: $\operatorname{tr}(cA)=c\operatorname{tr}(A)$. Applying a trace-like factor to determinant discards the independent scaling of all dimensions. When $c=0$ and $n>0$, the zero matrix has determinant zero; when $c<0$, parity of $n$ determines the determinant sign.

### Exact answer, competing options, and boundary

Option 3 names the correct dimensional scaling mechanism. Determinants do not distribute over arbitrary sums: $\det(I_2+I_2)=4$ but $\det(I_2)+\det(I_2)=2$. Multiplicativity does not require commuting factors; for $S=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ and $D=\operatorname{diag}(2,3)$, $SD\ne DS$ but both determinants multiply to six. Finally, $\det(2I_2)=4$, not two, refuting the single-scalar scaling assertion.

## Q22

**Correct option: 3.**

### Construct the result from the defining map

Let $N$ have $N_{12}=N_{23}=1$ and all other entries zero. Acting on the coordinate basis gives $Ne_3=e_2$, $Ne_2=e_1$ and $Ne_1=0$. Thus $N^2=E_{13}$ and $N^3=0$. Since identity commutes with $N$, the binomial expansion terminates:
$$ (I+N)^k=I+kN+\binom{k}{2}N^2=\begin{pmatrix}1&k&\binom{k}{2}\\0&1&k\\0&0&1\end{pmatrix},\quad k\ge0.$$
The $(1,3)$ coefficient uses two distinct time slots. At one slot the action moves $e_3$ to $e_2$; at a later slot it moves $e_2$ to $e_1$. The remaining slots apply identity. There are $\binom{k}{2}$ choices of the ordered pair of distinct slots once their chronological order is fixed. Allowing a double move inside one factor would count an operation that $I+N$ does not perform.

An independent recurrence verifies the same result. If $t_k$ denotes the upper-right coefficient, multiplying the displayed power by $I+N$ gives
$$t_{k+1}=t_k+k,\qquad t_0=0,$$
so $t_k=0+1+\cdots+(k-1)=k(k-1)/2$. This recurrence explains every checkpoint of the associated path simulation.

### Exact answer, competing options, and boundary

For exponent five, the answer is $5\cdot4/2=10$, option 3. The incorrect 25 counts two slots independently with replacement and order; 15 uses $1+\cdots+5$ instead of $0+\cdots+4$; five is the first-superdiagonal coefficient, which needs only one move. A state ledger at powers $0,1,2,3,4,5$ gives upper-right values $0,0,1,3,6,10$, with increments $0,1,2,3,4$.

## Q23

**Correct option: 2.**

### Construct the result from the defining map

Let $N$ have $N_{12}=N_{23}=1$ and all other entries zero. Acting on the coordinate basis gives $Ne_3=e_2$, $Ne_2=e_1$ and $Ne_1=0$. Thus $N^2=E_{13}$ and $N^3=0$. Since identity commutes with $N$, the binomial expansion terminates:
$$ (I+N)^k=I+kN+\binom{k}{2}N^2=\begin{pmatrix}1&k&\binom{k}{2}\\0&1&k\\0&0&1\end{pmatrix},\quad k\ge0.$$
The $(1,3)$ coefficient uses two distinct time slots. At one slot the action moves $e_3$ to $e_2$; at a later slot it moves $e_2$ to $e_1$. The remaining slots apply identity. There are $\binom{k}{2}$ choices of the ordered pair of distinct slots once their chronological order is fixed. Allowing a double move inside one factor would count an operation that $I+N$ does not perform.

An independent recurrence verifies the same result. If $t_k$ denotes the upper-right coefficient, multiplying the displayed power by $I+N$ gives
$$t_{k+1}=t_k+k,\qquad t_0=0,$$
so $t_k=0+1+\cdots+(k-1)=k(k-1)/2$. This recurrence explains every checkpoint of the associated path simulation.

### Exact answer, competing options, and boundary

For exponent eight, $8\cdot7/2=28$, option 2. The alternatives 36, eight and 64 are $\binom92$, the one-move coefficient, and $8^2$. Counting two distinct chronological slots excludes eight equal-slot cases and then divides the remaining $8\cdot7$ ordered choices by two. The entry is a coefficient of $N^2$, not a square of the coefficient of $N$.

## Q24

**Correct option: 1.**

### Construct the result from the defining map

Let $N$ have $N_{12}=N_{23}=1$ and all other entries zero. Acting on the coordinate basis gives $Ne_3=e_2$, $Ne_2=e_1$ and $Ne_1=0$. Thus $N^2=E_{13}$ and $N^3=0$. Since identity commutes with $N$, the binomial expansion terminates:
$$ (I+N)^k=I+kN+\binom{k}{2}N^2=\begin{pmatrix}1&k&\binom{k}{2}\\0&1&k\\0&0&1\end{pmatrix},\quad k\ge0.$$
The $(1,3)$ coefficient uses two distinct time slots. At one slot the action moves $e_3$ to $e_2$; at a later slot it moves $e_2$ to $e_1$. The remaining slots apply identity. There are $\binom{k}{2}$ choices of the ordered pair of distinct slots once their chronological order is fixed. Allowing a double move inside one factor would count an operation that $I+N$ does not perform.

An independent recurrence verifies the same result. If $t_k$ denotes the upper-right coefficient, multiplying the displayed power by $I+N$ gives
$$t_{k+1}=t_k+k,\qquad t_0=0,$$
so $t_k=0+1+\cdots+(k-1)=k(k-1)/2$. This recurrence explains every checkpoint of the associated path simulation.

### Exact answer, competing options, and boundary

The correct expression is $\binom n2$, option 1. It is zero at powers zero and one and equals one at power two, matching $N^2=E_{13}$. The alternatives $n,n^2,\binom{n+1}{2}$ fail these boundary checks. For a weighted upper nilpotent with $N_{12}=a$, $N_{23}=c$ and $N_{13}=b$, the same proof gives $(I+N)^k_{13}=kb+\binom{k}{2}ac$; direct one-step and indirect two-step contributions must both be retained.

## Q25

**Correct option: 4.**

### Construct the result from the defining map

Let $N$ have $N_{12}=N_{23}=1$ and all other entries zero. Acting on the coordinate basis gives $Ne_3=e_2$, $Ne_2=e_1$ and $Ne_1=0$. Thus $N^2=E_{13}$ and $N^3=0$. Since identity commutes with $N$, the binomial expansion terminates:
$$ (I+N)^k=I+kN+\binom{k}{2}N^2=\begin{pmatrix}1&k&\binom{k}{2}\\0&1&k\\0&0&1\end{pmatrix},\quad k\ge0.$$
The $(1,3)$ coefficient uses two distinct time slots. At one slot the action moves $e_3$ to $e_2$; at a later slot it moves $e_2$ to $e_1$. The remaining slots apply identity. There are $\binom{k}{2}$ choices of the ordered pair of distinct slots once their chronological order is fixed. Allowing a double move inside one factor would count an operation that $I+N$ does not perform.

An independent recurrence verifies the same result. If $t_k$ denotes the upper-right coefficient, multiplying the displayed power by $I+N$ gives
$$t_{k+1}=t_k+k,\qquad t_0=0,$$
so $t_k=0+1+\cdots+(k-1)=k(k-1)/2$. This recurrence explains every checkpoint of the associated path simulation.

### Exact answer, competing options, and boundary

Option 4 identifies why the standard binomial grouping is justified here: the summands $I$ and $N$ commute. For arbitrary square matrices, $(A+B)^2=A^2+AB+BA+B^2$, and replacing the middle terms by $2AB$ requires $AB=BA$. Choose $A=\operatorname{diag}(1,0)$, $B=E_{12}$: $AB=B$ but $BA=0$, so the ordinary scalar square formula is false. Nilpotence does not mean the matrix itself is zero; our $N$ is a direct counterexample. The first- and second-power coefficients differ, as exponent five gives five versus ten. Coincidences at an isolated exponent do not establish a universal expansion.

## Q26

**Correct option: 1.**

### Construct the result from the defining map

Let $U$ have shape $n\times2$ and rank two, and $V$ shape $2\times n$ and rank two, with $n\ge2$. The map $V:\mathbb R^n\to\mathbb R^2$ is onto because its image has the full codomain dimension two. The map $U:\mathbb R^2\to\mathbb R^n$ is injective because its kernel has dimension $2-2=0$. Therefore
$$\operatorname{im}(UV)=U(\operatorname{im}V)=U(\mathbb R^2)=\operatorname{im}U,\qquad\operatorname{rank}(UV)=2.$$
This proves equality, not merely an upper bound. Equivalently, $UVx=0$ implies $Vx=0$ by injectivity of $U$, so $\ker(UV)=\ker V$ and the nullity is $n-2$.

For a general product $AB$, one only has $\operatorname{rank}(AB)\le\min(\operatorname{rank}A,\operatorname{rank}B)$ without additional hypotheses. If $A=\operatorname{diag}(1,0)$ and $B=\operatorname{diag}(0,1)$, both factors have rank one but $AB=0$. The first factor kills the entire image of the second. The original problem avoids that loss because the left factor is injective on its whole two-dimensional domain.

### Exact answer, competing options, and boundary

At $n=5$, the square product has rank two, option 1, and kernel dimension three. Its being five-by-five does not imply rank five; there are only two intermediate coordinates. Rank four wrongly adds factor ranks; rank zero contradicts the injective-left/onto-right composition argument. A concrete witness is $U=[e_1\ e_2]$ and $V=U^T$, giving $UV=\operatorname{diag}(1,1,0,0,0)$.

## Q27

**Correct option: 4.**

### Construct the result from the defining map

Let $U$ have shape $n\times2$ and rank two, and $V$ shape $2\times n$ and rank two, with $n\ge2$. The map $V:\mathbb R^n\to\mathbb R^2$ is onto because its image has the full codomain dimension two. The map $U:\mathbb R^2\to\mathbb R^n$ is injective because its kernel has dimension $2-2=0$. Therefore
$$\operatorname{im}(UV)=U(\operatorname{im}V)=U(\mathbb R^2)=\operatorname{im}U,\qquad\operatorname{rank}(UV)=2.$$
This proves equality, not merely an upper bound. Equivalently, $UVx=0$ implies $Vx=0$ by injectivity of $U$, so $\ker(UV)=\ker V$ and the nullity is $n-2$.

For a general product $AB$, one only has $\operatorname{rank}(AB)\le\min(\operatorname{rank}A,\operatorname{rank}B)$ without additional hypotheses. If $A=\operatorname{diag}(1,0)$ and $B=\operatorname{diag}(0,1)$, both factors have rank one but $AB=0$. The first factor kills the entire image of the second. The original problem avoids that loss because the left factor is injective on its whole two-dimensional domain.

### Exact answer, competing options, and boundary

At $n=8$, the answer is two, option 4, and the kernel has dimension six. The alternatives eight, seven and zero respectively assume a full-rank square map, a single lost direction, or total annihilation. None respects the two-dimensional intermediate space together with the two stated full-rank conditions. Choosing the standard embedding and coordinate reader gives $UV=\operatorname{diag}(1,1,0,0,0,0,0,0)$ and verifies both factor ranks.

## Q28

**Correct option: 3.**

### Construct the result from the defining map

Let $U$ have shape $n\times2$ and rank two, and $V$ shape $2\times n$ and rank two, with $n\ge2$. The map $V:\mathbb R^n\to\mathbb R^2$ is onto because its image has the full codomain dimension two. The map $U:\mathbb R^2\to\mathbb R^n$ is injective because its kernel has dimension $2-2=0$. Therefore
$$\operatorname{im}(UV)=U(\operatorname{im}V)=U(\mathbb R^2)=\operatorname{im}U,\qquad\operatorname{rank}(UV)=2.$$
This proves equality, not merely an upper bound. Equivalently, $UVx=0$ implies $Vx=0$ by injectivity of $U$, so $\ker(UV)=\ker V$ and the nullity is $n-2$.

For a general product $AB$, one only has $\operatorname{rank}(AB)\le\min(\operatorname{rank}A,\operatorname{rank}B)$ without additional hypotheses. If $A=\operatorname{diag}(1,0)$ and $B=\operatorname{diag}(0,1)$, both factors have rank one but $AB=0$. The first factor kills the entire image of the second. The original problem avoids that loss because the left factor is injective on its whole two-dimensional domain.

### Exact answer, competing options, and boundary

The expression is two, option 3, for every allowed $n\ge2$. At $n=2$, both maps are square and invertible; their product is invertible. At $n>2$, the same rank two makes the larger product singular. Thus it would be wrong to call the product singular for all parameters. The full-rank premises are impossible at $n=1$, because an $n\times2$ or $2\times n$ matrix cannot have rank two there.

## Q29

**Correct option: 2.**

### Construct the result from the defining map

Let $U$ have shape $n\times2$ and rank two, and $V$ shape $2\times n$ and rank two, with $n\ge2$. The map $V:\mathbb R^n\to\mathbb R^2$ is onto because its image has the full codomain dimension two. The map $U:\mathbb R^2\to\mathbb R^n$ is injective because its kernel has dimension $2-2=0$. Therefore
$$\operatorname{im}(UV)=U(\operatorname{im}V)=U(\mathbb R^2)=\operatorname{im}U,\qquad\operatorname{rank}(UV)=2.$$
This proves equality, not merely an upper bound. Equivalently, $UVx=0$ implies $Vx=0$ by injectivity of $U$, so $\ker(UV)=\ker V$ and the nullity is $n-2$.

For a general product $AB$, one only has $\operatorname{rank}(AB)\le\min(\operatorname{rank}A,\operatorname{rank}B)$ without additional hypotheses. If $A=\operatorname{diag}(1,0)$ and $B=\operatorname{diag}(0,1)$, both factors have rank one but $AB=0$. The first factor kills the entire image of the second. The original problem avoids that loss because the left factor is injective on its whole two-dimensional domain.

### Exact answer, competing options, and boundary

Option 2 correctly requires more than the generic rank bound to conclude equality. A tall full-column-rank matrix maps onto its own image, not every vector of a larger codomain. For $n\ge4$, let $U=[e_1\ e_2]$ and let $V$ read coordinates three and four. Both ranks are two; $UV$ sends those coordinates into the first two axes, so it has rank two but $(UV)^2=0$, while $VU=0$. The reverse product need not have rank two. This exact example separates factor rank, square-product invertibility and action order.

## Q30

**Correct option: 3.**

### Construct the result from the defining map

Use the ordered basis $\mathcal B=(b_1,b_2)$ with $b_1=(1,1)^T$, $b_2=(1,-1)^T$, and the standard-coordinate map $T=\operatorname{diag}(2,n)$. The basis matrix and its inverse are
$$B=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad B^{-1}=\frac12B.$$
For a basis-coordinate input $c$, the conversion sequence is $c\mapsto Bc\mapsto TBc\mapsto B^{-1}TBc$. Hence
$$[T]_{\mathcal B}=B^{-1}TB=\frac12\begin{pmatrix}n+2&2-n\\2-n&n+2\end{pmatrix}.$$
The first-row second-column entry is the first basis coefficient of $T(b_2)=(2,-n)^T$. Solve $c_1+c_2=2$ and $c_1-c_2=-n$; adding yields $c_1=(2-n)/2$, and subtracting yields $c_2=(2+n)/2$. This column construction independently verifies the conjugation calculation.

The same ordered basis is used on input and output because $T$ is an endomorphism. Independent basis choices would instead give $C^{-1}TB$, not necessarily a similarity. Under similarity, trace and determinant remain $n+2$ and $2n$, while individual entries generally change. These invariants are useful checks, not replacements for converting the actual columns.

### Exact answer, competing options, and boundary

At $n=5$, the transformed matrix is $\begin{pmatrix}7/2&-3/2\\-3/2&7/2\end{pmatrix}$. The answer is $-3/2$, option 3. Values $-3$, three and $7/2$ omit the half factor, reverse the sign while omitting it, or give the diagonal coefficient instead. Reconstructing the second image gives $(-3/2)b_1+(7/2)b_2=(2,-5)^T$, exactly $T(b_2)$.

## Q31

**Correct option: 2.**

### Construct the result from the defining map

Use the ordered basis $\mathcal B=(b_1,b_2)$ with $b_1=(1,1)^T$, $b_2=(1,-1)^T$, and the standard-coordinate map $T=\operatorname{diag}(2,n)$. The basis matrix and its inverse are
$$B=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad B^{-1}=\frac12B.$$
For a basis-coordinate input $c$, the conversion sequence is $c\mapsto Bc\mapsto TBc\mapsto B^{-1}TBc$. Hence
$$[T]_{\mathcal B}=B^{-1}TB=\frac12\begin{pmatrix}n+2&2-n\\2-n&n+2\end{pmatrix}.$$
The first-row second-column entry is the first basis coefficient of $T(b_2)=(2,-n)^T$. Solve $c_1+c_2=2$ and $c_1-c_2=-n$; adding yields $c_1=(2-n)/2$, and subtracting yields $c_2=(2+n)/2$. This column construction independently verifies the conjugation calculation.

The same ordered basis is used on input and output because $T$ is an endomorphism. Independent basis choices would instead give $C^{-1}TB$, not necessarily a similarity. Under similarity, trace and determinant remain $n+2$ and $2n$, while individual entries generally change. These invariants are useful checks, not replacements for converting the actual columns.

### Exact answer, competing options, and boundary

At $n=8$, the transformed matrix is $\begin{pmatrix}5&-3\\-3&5\end{pmatrix}$, so option 2 is correct. The alternatives six, five and negative six correspond to a reversed unhalved difference, the diagonal entry and the unhalved difference. The trace ten equals $2+8$, and determinant $25-9=16$ equals $2\cdot8$, providing two independent structural checks.

## Q32

**Correct option: 1.**

### Construct the result from the defining map

Use the ordered basis $\mathcal B=(b_1,b_2)$ with $b_1=(1,1)^T$, $b_2=(1,-1)^T$, and the standard-coordinate map $T=\operatorname{diag}(2,n)$. The basis matrix and its inverse are
$$B=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad B^{-1}=\frac12B.$$
For a basis-coordinate input $c$, the conversion sequence is $c\mapsto Bc\mapsto TBc\mapsto B^{-1}TBc$. Hence
$$[T]_{\mathcal B}=B^{-1}TB=\frac12\begin{pmatrix}n+2&2-n\\2-n&n+2\end{pmatrix}.$$
The first-row second-column entry is the first basis coefficient of $T(b_2)=(2,-n)^T$. Solve $c_1+c_2=2$ and $c_1-c_2=-n$; adding yields $c_1=(2-n)/2$, and subtracting yields $c_2=(2+n)/2$. This column construction independently verifies the conjugation calculation.

The same ordered basis is used on input and output because $T$ is an endomorphism. Independent basis choices would instead give $C^{-1}TB$, not necessarily a similarity. Under similarity, trace and determinant remain $n+2$ and $2n$, while individual entries generally change. These invariants are useful checks, not replacements for converting the actual columns.

### Exact answer, competing options, and boundary

The answer is $(2-n)/2$, option 1. The plus expression gives the other coefficient of the same image; the remaining differences omit basis normalization and sometimes change sign. At $n=2$, $T=2I$, so every basis yields the same matrix and the off-diagonal entry is zero. At $n\ne2$, the displayed two eigenvectors mix the original coordinate axes, which generally creates off-diagonal entries.

## Q33

**Correct option: 4.**

### Construct the result from the defining map

Use the ordered basis $\mathcal B=(b_1,b_2)$ with $b_1=(1,1)^T$, $b_2=(1,-1)^T$, and the standard-coordinate map $T=\operatorname{diag}(2,n)$. The basis matrix and its inverse are
$$B=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad B^{-1}=\frac12B.$$
For a basis-coordinate input $c$, the conversion sequence is $c\mapsto Bc\mapsto TBc\mapsto B^{-1}TBc$. Hence
$$[T]_{\mathcal B}=B^{-1}TB=\frac12\begin{pmatrix}n+2&2-n\\2-n&n+2\end{pmatrix}.$$
The first-row second-column entry is the first basis coefficient of $T(b_2)=(2,-n)^T$. Solve $c_1+c_2=2$ and $c_1-c_2=-n$; adding yields $c_1=(2-n)/2$, and subtracting yields $c_2=(2+n)/2$. This column construction independently verifies the conjugation calculation.

The same ordered basis is used on input and output because $T$ is an endomorphism. Independent basis choices would instead give $C^{-1}TB$, not necessarily a similarity. Under similarity, trace and determinant remain $n+2$ and $2n$, while individual entries generally change. These invariants are useful checks, not replacements for converting the actual columns.

### Exact answer, competing options, and boundary

Corrected option 4 specifies the same new ordered basis for both domain and codomain. Multiplication on only one side converts only inputs or outputs, so option 1 is incomplete. The $n=5$ example changes a zero standard off-diagonal to $-3/2$, refuting entry invariance. The column $T(b_2)=(2,-n)$ is a standard-coordinate image; it must be multiplied by $B^{-1}$ to become the new column. This distinction refutes option 3 and explains both factors in the similarity formula.

## Q34

**Correct option: 1.**

### Construct the result from the defining map

Let $M=\begin{pmatrix}I_n&C\\0&2I_n\end{pmatrix}$ with arbitrary $n\times n$ block $C$. The full $2n\times2n$ matrix is upper triangular: its diagonal blocks are diagonal and its entire lower-left block is zero. Its first $n$ diagonal entries are one and its last $n$ are two. Therefore
$$\det M=1^n2^n=2^n.$$
No invertibility hypothesis on $C$ is needed. Its entries change the coupling from the second block of coordinates to the first, but not the triangular diagonal product. A direct inverse proves invertibility independently:
$$M^{-1}=\begin{pmatrix}I_n&-C/2\\0&I_n/2\end{pmatrix}.$$
In $MM^{-1}$ the upper-right block is $-C/2+C/2=0$; in $M^{-1}M$ it is $C-C=0$. The diagonal blocks are identity in both orders. Thus a singular, zero or even noninvertible off-diagonal block does not obstruct the whole inverse.

More generally, with invertible diagonal blocks $A,D$ and compatible rectangular $C$,
$$\begin{pmatrix}A&C\\0&D\end{pmatrix}^{-1}=\begin{pmatrix}A^{-1}&-A^{-1}CD^{-1}\\0&D^{-1}\end{pmatrix}.$$
Both block products verify this ordered formula. The coupling block need not be square; what matters is the inverses of the diagonal actions and the factor order.

### Exact answer, competing options, and boundary

At $n=5$, the determinant is $2^5=32$, option 1. Values one, ten and 1024 ignore the second diagonal block, confuse the dimension-dependent product with $2n$, or compute $4^5$ as if all ten diagonal coordinates were scaled by two. Exactly five coordinates contribute a factor two; the first five contribute one.

## Q35

**Correct option: 4.**

### Construct the result from the defining map

Let $M=\begin{pmatrix}I_n&C\\0&2I_n\end{pmatrix}$ with arbitrary $n\times n$ block $C$. The full $2n\times2n$ matrix is upper triangular: its diagonal blocks are diagonal and its entire lower-left block is zero. Its first $n$ diagonal entries are one and its last $n$ are two. Therefore
$$\det M=1^n2^n=2^n.$$
No invertibility hypothesis on $C$ is needed. Its entries change the coupling from the second block of coordinates to the first, but not the triangular diagonal product. A direct inverse proves invertibility independently:
$$M^{-1}=\begin{pmatrix}I_n&-C/2\\0&I_n/2\end{pmatrix}.$$
In $MM^{-1}$ the upper-right block is $-C/2+C/2=0$; in $M^{-1}M$ it is $C-C=0$. The diagonal blocks are identity in both orders. Thus a singular, zero or even noninvertible off-diagonal block does not obstruct the whole inverse.

More generally, with invertible diagonal blocks $A,D$ and compatible rectangular $C$,
$$\begin{pmatrix}A&C\\0&D\end{pmatrix}^{-1}=\begin{pmatrix}A^{-1}&-A^{-1}CD^{-1}\\0&D^{-1}\end{pmatrix}.$$
Both block products verify this ordered formula. The coupling block need not be square; what matters is the inverses of the diagonal actions and the factor order.

### Exact answer, competing options, and boundary

At $n=8$, the determinant is $2^8=256$, option 4. The other values one, sixteen and 65536 are $1$, $2n$ and $4^n$. They are inconsistent with the eight entries equal to one and eight equal to two. The result is unchanged as $C$ varies, including $C=0$ and any singular block, because its position is strictly above the full diagonal.

## Q36

**Correct option: 3.**

### Construct the result from the defining map

Let $M=\begin{pmatrix}I_n&C\\0&2I_n\end{pmatrix}$ with arbitrary $n\times n$ block $C$. The full $2n\times2n$ matrix is upper triangular: its diagonal blocks are diagonal and its entire lower-left block is zero. Its first $n$ diagonal entries are one and its last $n$ are two. Therefore
$$\det M=1^n2^n=2^n.$$
No invertibility hypothesis on $C$ is needed. Its entries change the coupling from the second block of coordinates to the first, but not the triangular diagonal product. A direct inverse proves invertibility independently:
$$M^{-1}=\begin{pmatrix}I_n&-C/2\\0&I_n/2\end{pmatrix}.$$
In $MM^{-1}$ the upper-right block is $-C/2+C/2=0$; in $M^{-1}M$ it is $C-C=0$. The diagonal blocks are identity in both orders. Thus a singular, zero or even noninvertible off-diagonal block does not obstruct the whole inverse.

More generally, with invertible diagonal blocks $A,D$ and compatible rectangular $C$,
$$\begin{pmatrix}A&C\\0&D\end{pmatrix}^{-1}=\begin{pmatrix}A^{-1}&-A^{-1}CD^{-1}\\0&D^{-1}\end{pmatrix}.$$
Both block products verify this ordered formula. The coupling block need not be square; what matters is the inverses of the diagonal actions and the factor order.

### Exact answer, competing options, and boundary

The expression is $2^n$, option 3, for every positive dimension. At $n=1$, $M=\begin{pmatrix}1&c\\0&2\end{pmatrix}$ has determinant two for every real $c$. Some distractors coincide at a special dimension, so that boundary alone cannot establish a symbolic law. At $n=2$, the alternatives $2n$ and $2^n$ happen to coincide at four; the diagonal argument is needed to decide validity for all $n$.

## Q37

**Correct option: 2.**

### Construct the result from the defining map

Let $M=\begin{pmatrix}I_n&C\\0&2I_n\end{pmatrix}$ with arbitrary $n\times n$ block $C$. The full $2n\times2n$ matrix is upper triangular: its diagonal blocks are diagonal and its entire lower-left block is zero. Its first $n$ diagonal entries are one and its last $n$ are two. Therefore
$$\det M=1^n2^n=2^n.$$
No invertibility hypothesis on $C$ is needed. Its entries change the coupling from the second block of coordinates to the first, but not the triangular diagonal product. A direct inverse proves invertibility independently:
$$M^{-1}=\begin{pmatrix}I_n&-C/2\\0&I_n/2\end{pmatrix}.$$
In $MM^{-1}$ the upper-right block is $-C/2+C/2=0$; in $M^{-1}M$ it is $C-C=0$. The diagonal blocks are identity in both orders. Thus a singular, zero or even noninvertible off-diagonal block does not obstruct the whole inverse.

More generally, with invertible diagonal blocks $A,D$ and compatible rectangular $C$,
$$\begin{pmatrix}A&C\\0&D\end{pmatrix}^{-1}=\begin{pmatrix}A^{-1}&-A^{-1}CD^{-1}\\0&D^{-1}\end{pmatrix}.$$
Both block products verify this ordered formula. The coupling block need not be square; what matters is the inverses of the diagonal actions and the factor order.

### Exact answer, competing options, and boundary

Option 2 correctly states that an off-diagonal block need not be invertible. Taking $C=0$ supplies an invertible block diagonal matrix and refutes option 3 directly. The determinant certainly does not ignore its diagonal blocks, which provide $2^n$, refuting option 4. Adding a lower-left coupling destroys automatic triangularity: the scalar-block matrix $\begin{pmatrix}1&1\\1&2\end{pmatrix}$ has determinant one, not two. Thus option 1 cannot retain the same formula without further conditions.

## Q38

**Correct option: 3.** The dimension is $13$.

A real symmetric $5\times5$ matrix has five independently chosen diagonal entries and ten independently chosen upper off-diagonal entries. Symmetry copies each upper entry into the reflected lower cell; it does not create a new parameter there. The starting dimension is $5+\binom52=15$.

The trace-zero condition determines the fifth diagonal entry from the first four. The condition $a_{12}=0$ removes one off-diagonal parameter. These constraints act on different independent coordinates, so two dimensions are removed. To prove their independence formally, apply a proposed relation $c\operatorname{tr}(A)+d a_{12}=0$ to $E_{11}$; this gives $c=0$. Apply it next to $E_{12}+E_{21}$; this gives $d=0$. Thus the constraint map has rank two, not merely two written equations.

An explicit basis certifies the count:
$$\{E_{ii}-E_{55}:1\le i\le4\}\ \cup\ \{E_{ij}+E_{ji}:1\le i<j\le5,\ (i,j)\ne(1,2)\}.$$
There are four diagonal-difference vectors and nine off-diagonal pair vectors. Inspecting the first four diagonal entries and each permitted upper entry proves their independence. Any allowed matrix is reconstructed with those entries as coefficients, proving spanning. Therefore $4+9=13$.

Fifteen ignores both constraints. Fourteen removes only one. Twelve wrongly counts the mirrored requirements $a_{12}=a_{21}=0$ as two separate restrictions after symmetry has already identified their parameter. More generally, on symmetric $n\times n$ matrices with $n\ge2$, trace zero and one specified off-diagonal zero give dimension $n(n+1)/2-2$. The off-diagonal condition has no meaning at $n=1$, so this formula must not be used there.

## Q39

**Correct option: 4.** The columns are $(2,1)^T$ and $(1,0)^T$ in the stated ordered basis.

The standard-coordinate images are $T(b_1)=(3,1)^T$ and $T(b_2)=(1,1)^T$. New matrix columns must contain their **basis coordinates**, not their standard coordinates. With $b_1=(1,1)^T$ and $b_2=(1,-1)^T$, the coordinate equation is
$$c_1b_1+c_2b_2=(c_1+c_2,c_1-c_2)^T=(x,y)^T.$$
Adding and subtracting the two scalar equations gives $c_1=(x+y)/2$, $c_2=(x-y)/2$. For the first image these are $(2,1)$; for the second they are $(1,0)$. Hence
$$[T]_{\mathcal B}=\begin{pmatrix}2&1\\1&0\end{pmatrix}.$$
Reconstruction verifies both columns: $2b_1+b_2=(3,1)^T$ and $b_1=(1,1)^T$. This is a direct action check independent of matrix conjugation.

Option 2 copies the unconverted standard images into columns. Option 1's second column $(0,1)$ reconstructs $b_2=(1,-1)$, the wrong second image. Option 3's first column $(2,0)$ reconstructs $(2,2)$ rather than $(3,1)$. These exact reconstructions diagnose each alternative.

For an additional verification, the old standard matrix is also $\begin{pmatrix}2&1\\1&0\end{pmatrix}$, since the two images and invertible basis matrix determine it. Conjugating with $B=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ gives this same array in the new basis. That equality is a specific coincidence, not a theorem that basis changes preserve entries. A map is basis-independent as an abstract transformation, while its array generally depends on the selected ordered basis.

## Q40

**Correct option: 3.** The upper-right entry is $21$.

Let $N$ have $N_{12}=N_{23}=1$ and all other entries zero. Acting on the coordinate basis gives $Ne_3=e_2$, $Ne_2=e_1$ and $Ne_1=0$. Thus $N^2=E_{13}$ and $N^3=0$. Since identity commutes with $N$, the binomial expansion terminates:
$$ (I+N)^k=I+kN+\binom{k}{2}N^2=\begin{pmatrix}1&k&\binom{k}{2}\\0&1&k\\0&0&1\end{pmatrix},\quad k\ge0.$$
The $(1,3)$ coefficient uses two distinct time slots. At one slot the action moves $e_3$ to $e_2$; at a later slot it moves $e_2$ to $e_1$. The remaining slots apply identity. There are $\binom{k}{2}$ choices of the ordered pair of distinct slots once their chronological order is fixed. Allowing a double move inside one factor would count an operation that $I+N$ does not perform.

An independent recurrence verifies the same result. If $t_k$ denotes the upper-right coefficient, multiplying the displayed power by $I+N$ gives
$$t_{k+1}=t_k+k,\qquad t_0=0,$$
so $t_k=0+1+\cdots+(k-1)=k(k-1)/2$. This recurrence explains every checkpoint of the associated path simulation.

For the requested exponent $7$, two distinct chronological slots can be chosen in $7(7-1)/2=21$ ways. This supplies the second-superdiagonal coefficient, not the one-step coefficient $7$ or the unrestricted ordered-pair count $49$.

The candidates seven, fourteen and forty-nine count one move, twice one move, or two independent unrestricted slots. None respects two ordered distinct slots. The exact recurrence ledger is

| Power $k$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ |
|---|---|---|---|---|---|---|---|---|
| $(1,3)$ entry | $0$ | $0$ | $1$ | $3$ | $6$ | $10$ | $15$ | $21$ |

Each increment equals the previous first-superdiagonal coefficient. The lemma concerns the actual three-coordinate chain; for a longer chain, farther superdiagonals have higher binomial coefficients and cannot all use this two-step count.

## Q41

**Correct option: 1.** For arbitrary invertible square factors,
$$ (ABA^{-1})^{-1}=AB^{-1}A^{-1}.$$
The inverse of a product reverses its factors. Applying this to all three factors gives $(A^{-1})^{-1}B^{-1}A^{-1}$, which simplifies to the stated candidate. Both products verify it:
$$ (ABA^{-1})(AB^{-1}A^{-1})=AB(A^{-1}A)B^{-1}A^{-1}=I,$$
$$ (AB^{-1}A^{-1})(ABA^{-1})=AB^{-1}(A^{-1}A)BA^{-1}=I.$$
Associativity brings adjacent inverse pairs together without moving them across other factors.

To reject the other expressions concretely, choose $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ and $B=\operatorname{diag}(2,3)$. Then $M=ABA^{-1}=\begin{pmatrix}2&1\\0&3\end{pmatrix}$ and
$$M^{-1}=\begin{pmatrix}1/2&-1/6\\0&1/3\end{pmatrix}.$$
Every listed candidate has the same diagonal entries in this example, so the upper-right entry isolates the error:

| Option | Candidate upper-right entry | $(M X)_{12}$ |
|---|---|---|
| 1 | $-1/6$ | $0$ |
| 2 | $1/6$ | $2/3$ |
| 3 | $-5/6$ | $-4/3$ |
| 4 | $5/6$ | $2$ |

The last column uses $2X_{12}+1/3$. Only option 1 gives an identity product. Wrong symbolic expressions may coincide when factors commute or when one factor is identity; such accidental agreement does not prove a rule for arbitrary invertible matrices. Conceptually, conjugation changes the coordinates of a map, and the inverse is the same coordinate conversion around the inverse action $B^{-1}$.

## Q42

**Correct option: 1.** For a real $m\times n$ matrix,
$$\ker(A^TA)=\ker A.$$
First, $Ax=0$ immediately gives $A^TAx=0$. Conversely, if $A^TAx=0$, premultiply by $x^T$:
$$0=x^TA^TAx=(Ax)^T(Ax)=\sum_{i=1}^{m}(Ax)_i^2.$$
Every real square is nonnegative. Their sum is zero only if every output coordinate is zero, proving $Ax=0$. This is the indispensable positivity step; mere associativity alone cannot prove the reverse inclusion.

Both kernels are subspaces of the same $n$-dimensional domain, so rank–nullity yields $\operatorname{rank}(A^TA)=\operatorname{rank}A$. It need not equal $m$. The Gram matrix is invertible exactly when all $n$ columns are independent, because its kernel is then zero. Taking $A=0$ refutes unconditional invertibility and unconditional row-dimension rank. Taking $A=\begin{pmatrix}1&1\\0&0\end{pmatrix}$ gives
$$A^TA=\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad AA^T=\begin{pmatrix}2&0\\0&0\end{pmatrix},$$
refuting equality of the two Gram matrices even when their shapes agree. With a rectangular $A$, their shapes differ as well.

The real hypothesis matters. For the complex column $A=(1,i)^T$, ordinary transpose gives $A^TA=1+i^2=0$, although $A$ has trivial one-dimensional kernel. Over the complex field use the adjoint $A^*$, giving $A^*A=2$ and recovering the kernel theorem through squared absolute values. The same argument works for a positive-definite weight $H$ in $A^*HA$; a merely semidefinite weight can kill a nonzero output, so the reverse implication may fail.

## Q43

**Correct option: 2.** The interval is $-1/3<a<1$.

Write the four-dimensional symmetric matrix as $M=(1-a)I_4+aJ_4$. For $q=(1,1,1,1)^T$, decompose every real vector uniquely as $x=sq+z$ with $\sum z_i=0$. The two components are perpendicular. As $Jq=4q$ and $Jz=0$,
$$x^TMx=4(1+3a)s^2+(1-a)\|z\|_2^2.$$
Necessity follows by testing each component separately. Take $z=0,s=1$ to require $1+3a>0$; take $s=0,z=(1,-1,0,0)$ to require $1-a>0$. Sufficiency follows because any nonzero $x$ has at least one nonzero component, so positive coefficients make its quadratic value strictly positive. Combining the inequalities gives the open interval.

At $a=-1/3$, the all-equal vector is nonzero and has quadratic value zero. At $a=1$, every sum-zero vector is a nonzero null direction. These endpoints give semidefinite matrices, not positive-definite ones. Outside the interval one of the displayed test vectors has negative quadratic value.

| Proposed interval | Concrete test | Failure |
|---|---|---|
| $(-1,1)$ | $a=-1/2$, $x=q$ | $1+3a=-1/2<0$. |
| $(-1/3,1)$ | Both coefficients positive | Necessary and sufficient. |
| $(0,1)$ | $a=-1/4$ | Excludes a valid positive-definite matrix. |
| $(-1/4,1/4)$ | $a=1/2$ | Excludes another valid matrix. |

In dimension $d\ge2$ the same proof gives $-1/(d-1)<a<1$. At $d=1$ the off-diagonal parameter does not occur. This geometric decomposition is stronger than checking a few test vectors: it exhausts the entire space and proves sufficiency.

## Q44

**Correct option: 2.** The traces agree although the two products have different sizes.

For $A\in\mathbb R^{2\times3}$ and $B\in\mathbb R^{3\times2}$, $AB$ is two-by-two and $BA$ three-by-three. Expand only their diagonal entries:
$$\operatorname{tr}(AB)=\sum_{i=1}^{2}\sum_{j=1}^{3}a_{ij}b_{ji},\qquad\operatorname{tr}(BA)=\sum_{j=1}^{3}\sum_{i=1}^{2}b_{ji}a_{ij}.$$
Both sums contain exactly the same six scalar products. Finite summation order and scalar multiplication order can be interchanged, proving the equality. No claim that $AB=BA$ has entered the proof.

Use the embedding/reader pair
$$A=\begin{pmatrix}1&0&0\\0&1&0\end{pmatrix},\quad B=\begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix}.$$
Then $AB=I_2$ and $BA=\operatorname{diag}(1,1,0)$. Their traces are both two, but their determinants are one and zero. This rejects determinant equality, and their two distinct shapes reject both matrix equality and identical-dimension assertions. The larger product kills $e_3$ while fixing $e_1,e_2$, explaining its zero determinant geometrically.

The general trace theorem allows $m\times n$ and $n\times m$ factors of any compatible positive sizes. For longer cyclic products, rotate the entire sequence only when every resulting multiplication is defined. Cyclic equality is not arbitrary permutation: for two-dimensional matrix units, $\operatorname{tr}(E_{12}E_{21}E_{11})=1$ whereas $\operatorname{tr}(E_{12}E_{11}E_{21})=0$. Thus a single scalar invariant neither erases action order nor makes differently sized transformations equal.

## Q45

**Correct option: 2.** The upper-right inverse block is $-C$.

Let the identity block sizes be $p$ and $q$, with $C$ of compatible shape $p\times q$. Write
$$M=\begin{pmatrix}I_p&C\\0&I_q\end{pmatrix},\qquad X=\begin{pmatrix}I_p&-C\\0&I_q\end{pmatrix}.$$
In the forward product, the upper-right block is $I_p(-C)+CI_q=0$; the lower-left block remains zero, and each diagonal block is identity. In the reverse product, it is $I_pC+(-C)I_q=0$. Thus $MX=XM=I_{p+q}$, proving the full two-sided inverse. Negating the coupling subtracts the same contribution that the forward map adds from the second coordinate group to the first.

The candidate $C$ would double that block instead of canceling it, unless the particular coupling happened to vanish. Zero would leave the original coupling. The expression $C^{-1}$ is not even defined for a rectangular or singular coupling, despite the full block matrix remaining invertible. For the scalar block $C=2$, those wrong choices leave upper-right product entries four, two and $5/2$, respectively; only negative two gives zero. Accidental agreement for a special block is not a general inverse law.

### Rectangular extension

Choose $p=1,q=2$ and $C=(2,-1)$. On input $(x,y_1,y_2)$, the forward map gives $(x+2y_1-y_2,y_1,y_2)$. The inverse gives $(z-2y_1+y_2,y_1,y_2)$, restoring the original first coordinate. The coupling row has no square inverse, yet the full three-by-three matrix has determinant one and the displayed inverse. This example exposes why block shapes must be specified before applying a formula.

## Q46

**Correct option: 3.** The upper-right entry is $45$.

Let $N$ have $N_{12}=N_{23}=1$ and all other entries zero. Acting on the coordinate basis gives $Ne_3=e_2$, $Ne_2=e_1$ and $Ne_1=0$. Thus $N^2=E_{13}$ and $N^3=0$. Since identity commutes with $N$, the binomial expansion terminates:
$$ (I+N)^k=I+kN+\binom{k}{2}N^2=\begin{pmatrix}1&k&\binom{k}{2}\\0&1&k\\0&0&1\end{pmatrix},\quad k\ge0.$$
The $(1,3)$ coefficient uses two distinct time slots. At one slot the action moves $e_3$ to $e_2$; at a later slot it moves $e_2$ to $e_1$. The remaining slots apply identity. There are $\binom{k}{2}$ choices of the ordered pair of distinct slots once their chronological order is fixed. Allowing a double move inside one factor would count an operation that $I+N$ does not perform.

An independent recurrence verifies the same result. If $t_k$ denotes the upper-right coefficient, multiplying the displayed power by $I+N$ gives
$$t_{k+1}=t_k+k,\qquad t_0=0,$$
so $t_k=0+1+\cdots+(k-1)=k(k-1)/2$. This recurrence explains every checkpoint of the associated path simulation.

For the requested exponent $10$, two distinct chronological slots can be chosen in $10(10-1)/2=45$ ways. This supplies the second-superdiagonal coefficient, not the one-step coefficient $10$ or the unrestricted ordered-pair count $100$.

The alternatives ten, twenty and one hundred are the one-step coefficient, twice the one-step coefficient and a square count with replacement. The exponent-ten calculation is $\sum_{j=0}^{9}j=45$, and the full power is $\begin{pmatrix}1&10&45\\0&1&10\\0&0&1\end{pmatrix}$. Multiplying the exponent-nine matrix, whose upper-right entry is 36, by $I+N$ adds nine and gives 45. This independent last-step verification prevents an off-by-one triangular-number error. If the chain weights are $a,c$, the two-step term is $45ac$; a direct $(1,3)$ weight $b$ adds $10b$, so changing the generator requires changing both contributions.

## Q47

**Correct option: 2.** The upper-right inverse block is $-B$.

Let the identity block sizes be $p$ and $q$, with $B$ of compatible shape $p\times q$. Write
$$M=\begin{pmatrix}I_p&B\\0&I_q\end{pmatrix},\qquad X=\begin{pmatrix}I_p&-B\\0&I_q\end{pmatrix}.$$
In the forward product, the upper-right block is $I_p(-B)+BI_q=0$; the lower-left block remains zero, and each diagonal block is identity. In the reverse product, it is $I_pB+(-B)I_q=0$. Thus $MX=XM=I_{p+q}$, proving the full two-sided inverse. Negating the coupling subtracts the same contribution that the forward map adds from the second coordinate group to the first.

The candidate $B$ would double that block instead of canceling it, unless the particular coupling happened to vanish. Zero would leave the original coupling. The expression $B^{-1}$ is not even defined for a rectangular or singular coupling, despite the full block matrix remaining invertible. For the scalar block $B=2$, those wrong choices leave upper-right product entries four, two and $5/2$, respectively; only negative two gives zero. Accidental agreement for a special block is not a general inverse law.

### Nonidentity diagonal extension

For invertible diagonal blocks $A,D$, the upper-right inverse block becomes $-A^{-1}BD^{-1}$, with the order fixed by solving $AX_{12}+BD^{-1}=0$. For the scalar blocks $A=2,D=3,B=6$, the correct upper-right is negative one, and the inverse is $\begin{pmatrix}1/2&-1\\0&1/3\end{pmatrix}$. Merely negating $B$ would fail because the surrounding diagonal scalings also need undoing. With matrix blocks these factors generally cannot commute; both product checks remain necessary to certify the ordered construction.
