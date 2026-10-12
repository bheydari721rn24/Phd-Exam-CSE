## Mathematical constructions supporting the examination bank

The full vector lesson and its 34 derivation tutorials remain part of this chapter. The examination bank also uses kernel dimensions, structured matrices and operator norms. This section supplies those prerequisites explicitly rather than relying on later chapters to justify present answers. The arguments are independently derived extensions of the four reviewed courses.

### 1. Basis extension, kernels, and independent constraints

For a finite independent list, appending a vector outside its span preserves independence: a zero relation involving its new coefficient would express it in the previous span unless that coefficient were zero. Starting with a subspace basis, repeatedly append an ambient vector outside the current span. In a finite-dimensional space this terminates at an ambient basis. The standard finite-basis exchange fact ensures an independent list has at most as many members as any spanning list: replace one spanning vector with each new independent vector using a relation with a nonzero replaceable coefficient. At each replacement the spanning property is retained; if no original vectors remained to replace, the next independent vector would already lie in the previous independent span, a contradiction.

For a linear map $T:V\to W$, extend a kernel basis by vectors $b_1,\ldots,b_r$ to a basis of V. Their images span $\operatorname{im}T$ because the kernel terms vanish. A zero image combination puts $\sum c_ib_i$ in the kernel; independence of the full domain basis forces every $c_i$ to vanish. Therefore

$$\dim V=\dim\ker T+\dim\operatorname{im}T.$$

A constraint map collects equations into one linear map. Its rank, not its number of written equations, determines the lost dimension. Trace on symmetric real matrices has rank one, because it attains one on $E_{11}$. Conversely $\operatorname{tr}S=0$ and $2\operatorname{tr}S=0$ are redundant, not two independent restrictions. Parametrizing the diagonal and upper triangle gives the explicit basis and count in Questions 1 and 5–8. Affine equations with a nonzero right side, when consistent, form a translate of the kernel rather than the kernel itself.

### 2. Sum, intersection, union, and attainability

Take a basis of $U\cap V$ and extend it separately inside U and V. The combined list with the shared basis included once is a basis of $U+V$. Spanning is immediate; independence follows by moving U-only terms to the V side, placing that combination in the intersection and using both extended-basis independence statements. This proves

$$\dim(U+V)=\dim U+\dim V-\dim(U\cap V).$$

In an ambient space of dimension d, intersection dimension r necessarily satisfies $\max(0,p+q-d)\le r\le\min(p,q)$. Every integer in that range is attainable: take shared coordinate directions $e_1,\ldots,e_r$, U-only directions $e_{r+1},\ldots,e_p$, and V-only directions $e_{p+1},\ldots,e_{p+q-r}$. The bound ensures enough ambient coordinates. This construction turns an algebraic feasible interval into actual subspaces.

A union is a subspace precisely when one subspace contains the other. If neither contains the other, choose $u\in U\setminus V$ and $v\in V\setminus U$. If $u+v$ belonged to U, subtracting u would put v in U; if it belonged to V, subtracting v would put u in V. Both are contradictions. Thus the union fails addition. Every subspace contains zero, so “disjoint” must not be used in place of “intersection exactly zero.” An embedding preserving the actual two subspaces preserves their intersection; their individual dimensions alone still do not determine their relative positions.

### 3. Operator norms, lower bounds, and quadratic-form signs

For a real vector norm, its induced operator norm is

$$\Vert A\Vert=\operatorname{sup}_{x\ne0}\frac{\Vert Ax\Vert}{\Vert x\Vert}.$$

It immediately gives $\Vert Ax\Vert\le\Vert A\Vert\Vert x\Vert$. Applying this twice proves $\Vert AB\Vert\le\Vert A\Vert\Vert B\Vert$. The Euclidean induced norm is distinguished from the Frobenius norm $\Vert A\Vert_F=(\sum_{ij}|a_{ij}|^2)^{1/2}$. For $I_n$, the induced norm is one and the Frobenius norm is $\sqrt n$. Consequently the inverse bound in Question 2 must use the norm induced by the stated vector norm, not a sum of squared matrix entries.

The lower bound $\Vert Ax\Vert\ge\theta\Vert x\Vert$ with $\theta>0$ forces a trivial kernel. For a square finite-dimensional map it gives invertibility; substituting $x=A^{-1}y$ proves $\Vert A^{-1}\Vert\le1/\theta$. This does not imply $x^TAx>0$: the counterexample $A=-I$ preserves every norm but makes that quadratic form negative. The eigenvalue modulus statement uses absolute values, not eigenvalue positivity. Question 2 supplies the Euclidean complex extension and the finite-dimensional norm-equivalence argument for an arbitrary real norm. The selected Stanford/MIT pages do not define all operator-norm theory; these proofs are stated as independent prerequisite extensions.

For a real symmetric structured matrix $A=(1-a)I+a\mathbf1\mathbf1^T$, decompose $x=s\mathbf1+z$ with $\sum z_i=0$. Then

$$x^TAx=n(1+(n-1)a)s^2+(1-a)\Vert z\Vert_2^2.$$

For $n\ge2$, both directions exist and positive definiteness is equivalent to $-1/(n-1)<a<1$. The endpoints have null directions. At $n=1$ there is no sum-zero nontrivial component and the unused off-diagonal parameter imposes no restriction. The decomposition proves necessity and sufficiency without requiring a spectral theorem.

### 4. Orthogonal versus orthonormal formulas and source integrity

For a nonzero orthogonal basis $u_1,\ldots,u_n$, write the desired foot as $p=\sum c_ku_k$. Taking the residual's inner product with each basis vector isolates $c_j=\langle u_j,x\rangle/\langle u_j,u_j\rangle$. Only when the basis is orthonormal can the denominator be omitted. With first-argument conjugation this ordering also applies in complex geometry.

The original PhD CS 1404 Q31 calls its basis orthogonal and displays the formula without denominators. Its literal translation is preserved and marked ambiguous. For $u=(2,0)$, the displayed map is $\operatorname{diag}(4,0)$, which is not idempotent; a perpendicular vector also falsifies the reversed norm inequality. Under an explicitly added orthonormal interpretation, the familiar general-theorem answer is option 3. When the target is the full space, even that inequality holds with equality. These two boundaries are explained instead of presenting a manufactured unique official key.

For a true orthogonal projection, the foot lies in the target span and the residual is perpendicular to every generator. These two tests prove uniqueness and optimality: every alternative q in the span satisfies $\Vert x-q\Vert^2=\Vert x-p\Vert^2+\Vert p-q\Vert^2$. They also imply contraction and idempotence. Idempotence by itself does not imply contraction; an oblique idempotent map can increase vector lengths.

### 5. Gram geometry, coordinates, and conjugation

For independent real generators placed in columns of B, their Gram matrix is $G=B^TB$. If $x=Bc$, then $\Vert x\Vert^2=c^TGc$. The form is positive definite because $Bc\ne0$ for nonzero c. A dependent generating list instead gives a nonzero coefficient vector in the Gram kernel. Norms in coordinates therefore need G; the identity occurs only for an orthonormal basis.

For projection of w, require $B^T(w-Bc)=0$, yielding $Gc=B^Tw$. Question 37 has $G=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ and right side $(4,3)^T$. Eliminating one coefficient gives $(a,b)=(5/3,2/3)$. Both membership and residual orthogonality are checked in its answer. Question 45 uses the same Gram shape with a different right side and different vectors; its solution is independently calculated, not transferred by a visual template.

For complex geometry use $G=B^*B$ and right side $B^*w$, where $*$ is conjugate transpose. The norm is $c^*Gc$. Replacing conjugate transpose by ordinary transpose can make a nonzero vector appear to have zero length. For $b=(1,i)$ and $x=ib$, the correct coefficient is i; the reversed inner-product numerator produces $-i$. A residual orthogonality test catches this sign error directly.

### 6. Affine minima and complete-square certificates

For a nonempty affine set $x_0+W$, minimizing distance to a target y means projecting $y-x_0$ onto W and translating back. The minimizing residual must be perpendicular to the direction space, not necessarily to the base point. Completing squares supplies a direct global certificate when a parameterization is simple.

Question 46 has feasible vectors $(1-y,y,1-y)$. Its objective is $3(y-2/3)^2+2/3$, proving the unique minimum at $(1/3,2/3,1/3)$. The two normal vectors $(1,1,0)$ and $(0,1,1)$ also give a Gram system with right side $(1,1)$; the coefficients $1/3,1/3$ yield the same closest point to the origin. This provides an independent primal parameterization and a normal-direction construction.

For a single hyperplane $a\cdot x=d$, $a\ne0$, the minimum squared norm is $d^2/\Vert a\Vert^2$ at $d a/\Vert a\Vert^2$. For multiple constraints, first check consistency and independent rank. A redundant consistent equation changes no feasible point; a redundant equation with a conflicting right side makes the set empty. A stationary-point calculation without a feasibility check or a nonnegative-square certificate is an incomplete optimization solution.
