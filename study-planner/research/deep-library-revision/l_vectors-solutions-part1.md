# Partial working manuscript: vectors examination answers

This manuscript is incomplete. It is not a delivered revised chapter. Original PDF pages for Questions 1–4 were inspected on 12 October 2026; the remaining answer bank, source reconciliation, diagrams and browser checks must be completed before the chapter can be marked revised.

## Q1

**Correct option: 2.**

### Model the independent coordinates explicitly

A real symmetric four-by-four matrix has the form

$$S=\begin{pmatrix}d_1&a&b&c\\a&d_2&e&f\\b&e&d_3&g\\c&f&g&d_4\end{pmatrix}.$$

The six off-diagonal coordinates $a,b,c,e,f,g$ are unconstrained; symmetry means each is copied into a second entry, not independently chosen twice. Trace zero means $d_1+d_2+d_3+d_4=0$, so $d_4=-d_1-d_2-d_3$. Thus all admissible matrices are uniquely described by nine real parameters: six off-diagonal entries and three diagonal entries. This unique parameterization proves dimension nine.

A concrete basis is $E_{ij}+E_{ji}$ for $1\le i<j\le4$, together with $E_{11}-E_{44},E_{22}-E_{44},E_{33}-E_{44}$. Every element is symmetric and trace zero. A zero linear combination forces the six off-diagonal coefficients to vanish by inspecting their entries, and then forces the three remaining coefficients to vanish by inspecting the first three diagonal entries. The nine matrices are therefore independent and span the space.

Option 1's ten ignores the trace restriction. Options 3 and 4 remove two or three dimensions instead of the rank-one constraint. Trace zero does not mean zero diagonal: $\operatorname{diag}(1,-1,0,0)$ is a valid nonzero diagonal element. The trace functional has rank one because it takes value one on $E_{11}$; writing equivalent copies of its equation does not create extra rank.

For positive size $n$, the corresponding real dimension is $n(n+1)/2-1$. At $n=1$ the space contains only zero and has dimension zero. At $n=0$, trace is already zero on the zero-dimensional space, so a separate dimension-zero answer is required; subtracting one would be invalid.

## Q2

**Correct option: 2.**

The hypothesis controls magnitude, not the sign of a quadratic form. Take $A=-I$ and $\theta=1$. For every vector and every norm, $\Vert Ax\Vert=\Vert-x\Vert=\Vert x\Vert$. Yet for every nonzero real $x$, $x^TAx=-\Vert x\Vert_2^2<0$. Thus positive definiteness does not follow, and option 2 is the false general assertion.

To check option 3, suppose $Ax=0$. The bound gives $0\ge\theta\Vert x\Vert$, and $\theta>0$ forces $x=0$. A square real matrix with a trivial kernel is invertible. This uses squareness: a tall injective rectangular map need not have a two-sided inverse.

For option 1, put $x=A^{-1}y$ in the original inequality. Then $\Vert y\Vert\ge\theta\Vert A^{-1}y\Vert$. Dividing by $\theta\Vert y\Vert$ for $y\ne0$ and taking the supremum yields the corresponding induced operator norm bound

$$\Vert A^{-1}\Vert\le\theta^{-1}.$$

For a real eigenvalue with real eigenvector $v\ne0$, substituting $Av=\lambda v$ directly gives $|\lambda|\ge\theta$. Nonreal eigenvalues need an additional argument because the original vectors are real. With the Euclidean norm, write a complex eigenvector $v=u+iw$ and apply the squared real bound to $u$ and $w$ separately. Adding gives $\Vert Av\Vert_2^2\ge\theta^2\Vert v\Vert_2^2$, hence the same modulus bound.

The conclusion also holds for any finite-dimensional real norm with its induced matrix norm. Set $B=A^{-1}$; then $\Vert B^k\Vert\le\theta^{-k}$. Norm equivalence gives constants $c,C>0$ with $c\Vert x\Vert_2\le\Vert x\Vert\le C\Vert x\Vert_2$ on real vectors. Therefore $\Vert B^k x\Vert_2\le(C/c)\theta^{-k}\Vert x\Vert_2$. Extend this upper Euclidean bound to complex vectors by summing the bounds for real and imaginary parts. For an eigenvalue $\mu$ of $B$, it gives $|\mu|^k\le(C/c)\theta^{-k}$. Taking $k$th roots and letting $k$ grow gives $|\mu|\le\theta^{-1}$, so the eigenvalue $\lambda=1/\mu$ of $A$ has $|\lambda|\ge\theta$. This justifies option 4 without silently imposing a Euclidean norm on the source's unqualified notation.

Finite-dimensional norm equivalence here follows by bounding a norm on the Euclidean unit sphere: continuity follows from the triangle inequality and coordinate expansion, the compact sphere has a finite maximum, and its minimum is positive because a norm vanishes only at zero. The complex argument is an extension of a real norm bound, not an assertion that the original real norm is automatically a complex inner product.

## Q3

**Correct option: 3 as a purported general projection theorem.**

Let $p=Px$ and $r=x-p$. For each basis vector $u_j$, orthonormality gives

$$\langle r,u_j\rangle=\langle x,u_j\rangle-\sum_{k=1}^{n}\langle x,u_k\rangle\langle u_k,u_j\rangle=0.$$

Thus $p\in U$ and $r\perp U$. The decomposition $x=p+r$ is orthogonal, so

$$\Vert x\Vert_2^2=\Vert Px\Vert_2^2+\Vert x-Px\Vert_2^2.$$

The correct universal direction is $\Vert Px\Vert_2\le\Vert x\Vert_2$. Equality holds precisely when $r=0$, equivalently $x\in U$. The reversed inequality in option 3 fails for a proper subspace: in $\mathbb R^2$, choose $U=\operatorname{span}(1,0)$ and $x=(0,1)$. Then $Px=0$, and the proposed inequality reads $1\le0$.

The remaining statements hold. Linearity follows by distributing each coefficient functional over vector sums and scalar multiples; every resulting output is a combination of the $u_k$, establishing option 4. If $x\in U$, its orthonormal expansion is exactly $x$, proving option 2 and the stronger identity $Px=x$. Applying this identity to $Px\in U$ gives $P^2x=Px$, establishing option 1.

**Source quantifier boundary.** The original allows $n=m$. If $U=\mathbb R^m$, then $P=I$ and the inequality in option 3 holds with equality; for that particular full-space configuration all four assertions are true. Option 3 is therefore false as a general theorem over the allowed subspaces, not a claim that its inequality fails for every allowed $U$ or every $x$. Preserve the authentic statement and explain this endpoint instead of silently changing its hypothesis to $n<m$.

An idempotent map alone need not shorten vectors. For example $Q=\begin{pmatrix}1&2\\0&0\end{pmatrix}$ has $Q^2=Q$, but maps $(0,1)$ to $(2,0)$. Orthogonality, not just idempotence, supplies the norm decomposition above.

## Q4

**Correct option: 2.**

The source matrix is $A=(1-a)I+a\mathbf1\mathbf1^T$ in three dimensions. Every real vector can be written uniquely as $x=s\mathbf1+z$, with $s=(x_1+x_2+x_3)/3$ and $z_1+z_2+z_3=0$. The two terms are orthogonal. Expanding the quadratic form gives

$$x^TAx=3(1+2a)s^2+(1-a)\Vert z\Vert_2^2.$$

If $a\ge1$, choose nonzero $z=(1,-1,0)$ and $s=0$; the form is nonpositive. If $a\le-1/2$, choose $s=1,z=0$; again the form is nonpositive. Thus strict positive definiteness requires $1-a>0$ and $1+2a>0$.

Conversely, if both coefficients are positive, every nonzero $x$ has either $s\ne0$ or $z\ne0$, and the displayed sum is strictly positive. This proves sufficiency directly, without importing an unexplained eigenvalue criterion. The exact interval is $-1/2<a<1$, option 2.

Option 1 permits, for example, $a=-3/4$, where the all-equal direction gives $3(1+2a)=-3/2$. Option 3 unnecessarily rejects $a=3/4$, where both coefficients are positive. Option 4 unnecessarily rejects $a=-1/4$, also valid, and excludes $a=0$, the identity matrix. At $a=-1/2$, the all-equal line is null; at $a=1$, the sum-zero plane is null. Both endpoints are positive semidefinite but not positive definite. Outside the closed interval, a direction of negative quadratic form exists.

For $n\ge2$ with the analogous real symmetric matrix, the decomposition yields coefficients $1+(n-1)a$ and $1-a$, hence strict range $-1/(n-1)<a<1$. At $n=1$, there are no off-diagonal entries: the matrix is simply $(1)$ and places no restriction on the unused parameter. The special dimension-one case must not be inferred by dividing by zero in the general endpoint.
