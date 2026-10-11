# Orthogonal Projections and Projection Matrices

Authoring draft: the sections below have been written, but the complete problem bank, final examination rules, models, source comparison and independent review are still pending. This draft is not yet a library chapter. It follows Orthogonality and Orthogonal Decompositions and precedes Least Squares and Applications.

## 1. Written sources and the purpose of this chapter

The working synthesis uses MIT18.06SC Session2.3, Stanford EE263 Lecture5, Oxford M1 Linear Algebra I, and Berkeley Math54 Orthogonal Projections. ETH Zurich's Linear Algebra PartII supplies an additional precise QR argument. Exact reading ranges, conventions and the pending comparison are in the source audit. Four university names do not substitute for a documented chapter-specific selection.

The prerequisite chapter established inner products and the existence of perpendicular decompositions. Here the object of study is the projection operator itself: how to construct it from imperfectly presented generators, identify it from algebraic conditions, recognize its range and kernel, calculate distances, combine it with other projections, and distinguish physical vectors from their coordinates. An examination question may never mention geometry; it may give an idempotent matrix, a trace identity, an affine constraint or an unfamiliar weighted product. The same operator must be recognized through all these representations.

Unless otherwise declared, vectors are columns, the ambient space is finite dimensional, and real Euclidean geometry is used. Complex formulas use the conjugate transpose, written $A^*$. The residual convention is always data minus projected data:

$$p=Pb,\qquad r=b-p=(I-P)b.$$

Stanford Lecture5 instead writes the opposite residual. Its orthogonality conclusion is unchanged, but the sign of a displayed residual vector must be translated. Norm notation uses a complete grouped base before an exponent; a closing delimiter is not the base of the exponent.

## 2. A subspace and its generators are different objects

Let $A\in\mathbb R^{m\times n}$ and let $S=\operatorname{Col}(A)$. The subspace is a set of physical vectors in $\mathbb R^m$. A coefficient vector belongs to $\mathbb R^n$. Their dimensions and their roles differ:

$$c\in\mathbb R^n,\qquad Ac\in S\subseteq\mathbb R^m.$$

Repeating a generator, rescaling a nonzero generator, or adding a linear combination of earlier generators may change $A$ and its coefficient descriptions without changing $S$. Therefore a formula for the physical projection should depend on $S$, not on a particular generator list. This requirement is an immediate diagnostic: an alleged projection formula that changes when a column is doubled is suspect.

An independent column basis $C$ can be selected from $A$ by identifying pivot columns of the original matrix. Row reduction discovers the indices; the basis vectors must be taken from the original columns. Substituting the corresponding columns of the row-reduced matrix usually changes the physical subspace. If the rank is zero, the subspace is the zero subspace and its projection is the zero operator. No empty inverse is needed.

## 3. The closest-point theorem, with existence and uniqueness separated

Choose an orthonormal basis $q_1,\ldots,q_k$ of $S$. Define

$$p=\sum_{j=1}^{k}q_j(q_j^Tb),\qquad r=b-p.$$

For each basis vector, $q_i^Tr=q_i^Tb-q_i^Tb=0$. By linearity, $r$ is perpendicular to every vector in $S$. Thus a decomposition exists. For any candidate $s\in S$, the vector $p-s$ is also in $S$, so it is perpendicular to $r$. Consequently

$$b-s=r+(p-s),\qquad {\Vert b-s\Vert}^2={\Vert r\Vert}^2+{\Vert p-s\Vert}^2.$$

The second term is nonnegative and vanishes exactly when $s=p$. This proves both optimality and uniqueness. The proof uses positive definiteness. A bilinear form that admits a nonzero vector of zero self-product does not support this uniqueness argument.

The theorem gives a practical certificate without optimization or inversion: a candidate $p$ is the closest point exactly when $p\in S$ and $b-p\in S^\perp$. Checking only the dot product $p^T(b-p)=0$ is insufficient. It tests one vector in the subspace, rather than every generator direction.

## 4. Linearity follows from the decomposition certificate

Suppose $b_i=p_i+r_i$ with $p_i\in S$ and $r_i\in S^\perp$. For scalars $\alpha,\beta$, the decomposition of $\alpha b_1+\beta b_2$ is

$$\alpha b_1+\beta b_2=(\alpha p_1+\beta p_2)+(\alpha r_1+\beta r_2).$$

The first part belongs to $S$ and the second to $S^\perp$. Uniqueness therefore implies $P(\alpha b_1+\beta b_2)=\alpha Pb_1+\beta Pb_2$. This establishes linearity before a matrix formula is guessed.

The operator fixes every vector already in $S$ and kills every vector in $S^\perp$. Hence

$$P^2=P,\qquad \operatorname{Range}(P)=S,\qquad \operatorname{Ker}(P)=S^\perp.$$

The residual operator $I-P$ projects onto $S^\perp$. It is not an unrelated error-processing device: it is the complementary projection, and $P(I-P)=(I-P)P=0$.

## 5. Deriving the generator formula instead of memorizing it

Let $C\in\mathbb R^{m\times k}$ have independent columns and span $S$. Write $p=Cc$. Perpendicularity to every column gives

$$C^T(b-Cc)=0,\qquad C^TCc=C^Tb.$$

Why may the Gram matrix be inverted? For every nonzero $z\in\mathbb R^k$,

$$z^TC^TCz={\Vert Cz\Vert}^2>0.$$

The strict inequality follows from column independence. Thus $C^TC$ is positive definite, and

$$c=(C^TC)^{-1}C^Tb,\qquad P=C(C^TC)^{-1}C^T.$$

The dimensions are $m\times k$, $k\times k$, and $k\times m$; their product is an $m\times m$ ambient operator. Reversing a transpose can produce a dimensionally meaningless expression even when the source page appears authoritative.

If $C$ is replaced by $CR$, where $R$ is an invertible $k\times k$ matrix, the middle inverse becomes $R^{-1}(C^TC)^{-1}R^{-T}$. Multiplication cancels both changes, leaving exactly the same $P$. This is a constructive proof of basis invariance. Coefficients change to $R^{-1}c$; the physical vector does not.

## 6. Worked problem: a plane with a hidden normal

Let the plane be generated by $a_1=(1,0,1)^T$ and $a_2=(0,1,1)^T$, and project $b=(1,2,0)^T$. The generator matrix and its Gram system are

$$C=\begin{pmatrix}1&0\\0&1\\1&1\end{pmatrix},\qquad C^TC=\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad C^Tb=\begin{pmatrix}1\\2\end{pmatrix}.$$

The inverse Gram matrix is one third of $\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$. Therefore $c=(0,1)^T$, $p=(0,1,1)^T$, and $r=(1,1,-1)^T$. Both generator products with $r$ vanish. The squared distance is $3$; the norm decomposition reads $5=2+3$.

There is a second derivation. A normal is $n=(-1,-1,1)^T$, so $S=n^\perp$ and

$$P=I-\frac{nn^T}{n^Tn}=\frac13\begin{pmatrix}2&-1&1\\-1&2&1\\1&1&2\end{pmatrix}.$$

Applying this matrix yields the same $p$. The two derivations cross-check the signs of the normal and the distinction between projection onto the plane and projection onto its normal line. Changing $n$ to $-n$ leaves the outer product unchanged.

## 7. Dependent generators: unique vector, nonunique coefficients

Add $a_3=a_1+a_2$ to the preceding generator list. The new three-column matrix has rank two, so $A^TA$ is singular. Its column space and its orthogonal projector are unchanged. All coefficient descriptions of the projected vector satisfy

$$c_1+c_3=0,\qquad c_2+c_3=1.$$

Thus every coefficient vector has the form $c=(-t,1-t,t)^T$. Every such vector maps to the same $p$. A normal-equation solution alone does not guarantee a unique coefficient vector.

To select the minimum Euclidean coefficient norm, minimize $t^2+(1-t)^2+t^2=3t^2-2t+1$. Completing the square gives

$$3t^2-2t+1=3\left(t-\frac13\right)^2+\frac23.$$

The unique minimum-norm coefficient vector is $(-1/3,2/3,1/3)^T$. It is perpendicular to the coefficient nullspace generated by $(-1,-1,1)^T$. This is a statement in coefficient space; it must not be confused with the observation residual $r=(1,1,-1)^T$ in the ambient space, despite the coincident dimensions in this particular example.

A pseudoinverse may express this selection as $c=A^+b$. The operator $AA^+$ is the orthogonal projection onto the column space. Defining or deriving $A^+$ correctly is essential: the full-column-rank formula cannot simply be applied to a dependent matrix.

## 8. Rectangular orthonormal bases and the QR route

If $Q\in\mathbb R^{m\times k}$ has orthonormal columns, then $Q^TQ=I_k$ and the projector is $QQ^T$. Unless $k=m$, the reverse product is not the ambient identity. It is a rank-$k$ projection.

For a full-column-rank factorization $C=QR$ with invertible triangular $R$, substitute into the generator formula. The middle inverse is $R^{-1}R^{-T}$; cancellation gives

$$C(C^TC)^{-1}C^T=QQ^T.$$

To apply the projector, first measure the orthonormal coordinates $Q^Tb$ and then reconstruct $Q(Q^Tb)$. This uses neither an explicit Gram inverse nor an ambient dense matrix. If a full orthogonal matrix is partitioned as $[Q_1\ Q_2]$ with $Q_1$ spanning $S$, then $P=Q_1Q_1^T$, $I-P=Q_2Q_2^T$, and the squared distance is ${\Vert Q_2^Tb\Vert}^2$.

For computation, solving a triangular system is preferable to explicitly forming its inverse. The exact formulas establish mathematics; a numerically stable algorithm requires an additional conditioning discussion.

## 9. Algebraic recognition: symmetry and idempotence together

An orthogonal projector is symmetric and idempotent. Conversely, suppose a real square matrix satisfies $P^T=P$ and $P^2=P$. Every $x$ decomposes as $Px+(I-P)x$. The first component lies in the range. For any range vector $Py$,

$$ (Py)^T(I-P)x=y^TP(I-P)x=0.$$

The second component is perpendicular to the whole range. The closest-point theorem therefore identifies $P$ as its orthogonal projection. This proves the characterization without assuming a spectral theorem.

Idempotence alone only gives a direct-sum decomposition into range and kernel. For $E=\begin{pmatrix}1&2\\0&0\end{pmatrix}$, $E^2=E$, but the vertical unit vector maps to $(2,0)^T$. Length increases from one to two. Its residual follows the oblique kernel, not the Euclidean perpendicular direction.

Symmetry alone also fails. The diagonal matrix with entries $2$ and $0$ is symmetric but doubles the first coordinate. Checking only trace, rank or determinant never replaces both defining identities.

## 10. Contraction characterizes an idempotent projection

Every orthogonal projector satisfies ${\Vert Px\Vert}\le {\Vert x\Vert}$ by Pythagoras. Conversely, suppose $P^2=P$ and $P$ contracts every vector. Let $u$ lie in the range and $v$ in the kernel. Then $P(u+tv)=u$ for every real $t$, so

$$ {\Vert u\Vert}^2\le {\Vert u+tv\Vert}^2={\Vert u\Vert}^2+2t\,u^Tv+t^2{\Vert v\Vert}^2.$$

If $u^Tv$ were nonzero, choosing $t=-u^Tv/{\Vert v\Vert}^2$ would make the right-hand difference negative. Therefore range and kernel are perpendicular. The idempotent is orthogonal. The zero-kernel or zero-vector cases require no division and already satisfy the conclusion.

Testing contraction on a single vector is insufficient. The quantifier is every vector. This proof also explains how an oblique projector necessarily expands some input: a kernel component can partly cancel a range component before the oblique projection removes it.

## 11. Rank, trace, spectrum and the operator norm

If $Pv=\lambda v$ for a nonzero vector, idempotence implies $\lambda^2=\lambda$, so an eigenvalue is zero or one. More strongly, an idempotent is diagonalizable even when it is oblique: choose a basis of its range followed by a basis of its kernel. Their intersection is zero, and every vector splits into both parts. The matrix in that basis is $\operatorname{diag}(I_k,0)$.

It follows that the rank and trace equal $k$. The determinant is zero unless the rank is the full ambient dimension, in which case idempotence forces $P=I$. Trace equals rank for oblique idempotents as well; it does not certify symmetry.

For an orthogonal projector, $x^TPx={\Vert Px\Vert}^2\ge0$, and the same is true for $I-P$. Thus its quadratic form lies between zero and $x^Tx$. Its operator norm is one if the range is nonzero, since a nonzero range vector is fixed. The zero projector has norm zero. Its squared Frobenius norm equals $\operatorname{tr}(P^TP)=\operatorname{tr}(P)=k$.

## 12. Diagonal entries and hidden coordinate information

For the standard unit vector $e_i$, the diagonal entry is $p_{ii}=e_i^TPe_i={\Vert Pe_i\Vert}^2$. Consequently $0\le p_{ii}\le1$ and the diagonal sum equals the rank. Symmetry and idempotence also give

$$\sum_j p_{ij}^2=p_{ii}.$$

If $p_{ii}=0$, the whole corresponding row and column vanish. If $p_{ii}=1$, the diagonal square already exhausts the row's squared norm, so every off-diagonal entry in that row is zero; the coordinate direction belongs to the range.

Apply Cauchy–Schwarz to $Pe_i$ and $Pe_j$. Since their product is $p_{ij}$,

$$p_{ij}^2\le p_{ii}p_{jj}.$$

Applying the same argument to $I-P$ gives $p_{ij}^2\le(1-p_{ii})(1-p_{jj})$ when $i\ne j$. These inequalities are useful necessary tests, but a candidate matrix satisfying them need not be a projector. The identities $P^2=P$ and $P^T=P$ remain decisive.

## 13. Weighted geometry: the operator may look nonsymmetric

Let $G$ be real symmetric positive definite and define the product $x^TGy$. The projection onto an independent column basis $C$ is

$$P_G=C(C^TGC)^{-1}C^TG.$$

The proof repeats the membership and perpendicular-residual certificate, now with $C^TG(b-P_Gb)=0$. The Gram matrix remains positive definite because $Cz$ is nonzero for nonzero $z$. The operator is idempotent but generally not symmetric in ordinary coordinates. Its correct self-adjointness identity is $P_G^TG=GP_G$.

For $G=\operatorname{diag}(1,4)$ and $C=(1,1)^T$,

$$P_G=\frac15\begin{pmatrix}1&4\\1&4\end{pmatrix}.$$

For $b=(2,0)^T$, the projection is $(2/5,2/5)^T$ and the residual is $(8/5,-2/5)^T$. Their weighted product is zero. The squared input norm is $4$, the squared projected norm is $4/5$, and the squared residual norm is $16/5$. Ordinary symmetry is absent; weighted orthogonality is exact.

Writing $G=L^TL$ with invertible $L$ converts physical vectors to Euclidean coordinates $y=Lx$. The transformed projector $LP_GL^{-1}$ is Euclidean orthogonal. This is a change of metric representation, not permission to substitute ordinary transpose for the weighted adjoint.

## 14. Complex vectors require conjugation

For a complex column basis, replace each transpose in the Euclidean construction by conjugate transpose:

$$P=C(C^*C)^{-1}C^*.$$

For $c=(1,i)^T$, the squared norm is $c^*c=2$ and

$$P=\frac12\begin{pmatrix}1&-i\\i&1\end{pmatrix}.$$

Projecting $b=(1,0)^T$ gives $p=(1/2,i/2)^T$ and $r=(1/2,-i/2)^T$. The conjugate product $c^*r$ is zero and $P^*=P$. Using $c^Tc$ would give zero for a nonzero generator and falsely suggest that its Gram matrix is singular. This is a convention error, not a failure of the projection theorem.

## 15. Affine spaces: translate, project, and translate back

An affine space has the form $a+S$. To find its closest point to $b$, minimize the distance from $b-a$ to $S$. The result is

$$\Pi_{a+S}(b)=a+P(b-a)=Pb+(I-P)a.$$

Changing the representative $a$ by a vector in $S$ leaves the constant term unchanged. The mapping is affine and idempotent, but generally not linear. It is linear exactly when $(I-P)a=0$, which means the affine space contains the origin and is the same subspace $S$.

For a hyperplane $n^Tx=d$ with nonzero normal $n$, the closest point is

$$p=b-n\frac{n^Tb-d}{n^Tn}.$$

Take $n=(1,2,-1)^T$, $d=3$, and $b=(2,0,1)^T$. The violation is $-2$, so $p=b+n/3=(7/3,2/3,2/3)^T$. Direct substitution gives $n^Tp=3$. The correction has squared length $2/3$, which is also the squared distance to the hyperplane. This squared distance differs from the squared distance to the parallel subspace through the origin.

## 16. Several affine constraints and their qualifications

Let $D$ have independent rows and impose $Dx=d$. The kernel of $D$ is the direction subspace. A correction perpendicular to it belongs to the row space, so write $p=b-D^T\lambda$. The constraints imply $DD^T\lambda=Db-d$, giving

$$p=b-D^T(DD^T)^{-1}(Db-d).$$

For $D=\begin{pmatrix}1&1&0\\0&1&1\end{pmatrix}$, $d=(1,2)^T$ and $b=0$, the Gram inverse yields the closest feasible point $p=(0,1,1)^T$. Its squared norm is two. The direction kernel is generated by $(-1,1,-1)^T$, whose dot product with $p$ is zero. This checks both feasibility and minimal norm.

Dependent rows require two separate checks: consistency of the affine constraints and a valid inverse or pseudoinverse on the independent row space. A dependent but consistent system has a unique closest feasible vector. An inconsistent system has no point to project onto; solving a least-squares surrogate changes the question.

## 17. Combining projectors: commutation is a substantive hypothesis

Let $P,Q$ be orthogonal projectors. If they commute, then $PQ$ is symmetric and idempotent. Its range equals the intersection of their ranges: an output $PQx$ is fixed by both, while a vector fixed by both is fixed by $PQ$. Therefore $PQ$ projects onto that intersection.

Conversely, if $PQ$ is an orthogonal projector, symmetry gives $PQ=(PQ)^T=QP$. The condition is necessary as well as sufficient. A product of projections is not automatically a projection.

For projection onto the horizontal axis and onto the line generated by $(1,1)^T$,

$$P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad Q=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad PQ=\frac12\begin{pmatrix}1&1\\0&0\end{pmatrix}.$$

The product is neither symmetric nor idempotent. Repeated application multiplies its nonzero part by one half each time. The intersection is the zero subspace, so repeated products tend toward its zero projection, but a single product is not that limit. A simulation must show the actual finite iterates rather than label every intermediate result as an intersection projection.

## 18. Sums, differences and contained subspaces

If the ranges are perpendicular, then $PQ=QP=0$ and $P+Q$ is the projection onto their orthogonal direct sum. Conversely, idempotence of $P+Q$ gives $PQ+QP=0$. Taking trace yields $2\operatorname{tr}(PQ)=0$. For orthogonal projectors,

$$\operatorname{tr}(PQ)={\Vert PQ\Vert}_F^2\ge0.$$

Thus $PQ=0$, proving necessity. The argument uses symmetry; it must not be transplanted without qualification to arbitrary oblique idempotents.

If the range of $P$ is contained in the range of $Q$, then $QP=P$ and, by transpose, $PQ=P$. The difference $Q-P$ is an orthogonal projector onto the part of the larger range perpendicular to the smaller range. The sign matters: $P-Q$ then has eigenvalue minus one on that removed part, so it is generally not a projector.

## 19. Measuring how different two projections are

For ranks $r$ and $s$, expand the Frobenius square using symmetry and idempotence:

$$ {\Vert P-Q\Vert}_F^2=r+s-2\operatorname{tr}(PQ).$$

The trace is nonnegative by the preceding identity. It is at most both ranks: applying the contraction of $Q$ to an orthonormal basis of the range of $P$ shows that the sum of squared projected lengths is at most $r$, and the reverse argument gives $s$.

If the intersection has dimension $t$, extend an orthonormal basis of the intersection to a basis of the range of $P$. Each intersection vector contributes one to that same trace sum; every other contribution is nonnegative. Hence the trace is at least $t$, and $t\ge r+s-m$ when the ambient dimension is $m$. In particular

$$\max(0,r+s-m)\le\operatorname{tr}(PQ)\le\min(r,s).$$

The trace is usually not the dimension of the intersection. For two distinct nonperpendicular lines in a plane, the intersection has dimension zero while the trace equals the squared cosine of their angle and is positive. This gives an immediate conceptual counterexample to a tempting rank formula.

## 20. Rank changes and a discontinuous limiting projection

Let $A_\varepsilon=\begin{pmatrix}1&1\\0&\varepsilon\end{pmatrix}$. For every nonzero $\varepsilon$, its columns span the full plane and its orthogonal projector is the identity. At $\varepsilon=0$, they span only the horizontal line, whose projector is $\operatorname{diag}(1,0)$.

Thus the matrices of generators converge while their associated projection matrices do not converge to the projection of the limiting range. The rank changes at the limit. For the target $(0,1)^T$, exact coefficients at nonzero $\varepsilon$ are $(-1/\varepsilon,1/\varepsilon)^T$: the physical fitted vector remains fixed while the coefficient magnitude diverges.

This example separates three statements: the projection is well-defined at every parameter value, coefficient recovery can be ill-conditioned near dependent columns, and continuity of a projection as a function of its generators requires a fixed-rank qualification. Treating a very small nonzero parameter as exactly zero without declaring a numerical rank policy changes the subspace.

## Draft completion boundary

The remaining authoring work includes the full course-exercise reconstruction and original medium-to-hard solved bank, the complete final examination-rule section, conditional formulas for reflection and repeated projections, advanced coordinate and metric cases, and compact interactive models for angle-dependent projections, constraint corrections, coefficient nonuniqueness and finite iteration. The chapter will enter the library only after these parts and the independent mathematical/browser audit are complete.

## References

- MIT, Gilbert Strang,18.06SC Fall2011: Session2.3 lecture summary and exercise solutions, teaching pages1–3 and1–2 respectively.
- Stanford, Stephen Boyd, EE263 Autumn2007–08: Lecture5, Least-squares, especially projection and QR teaching pages1–10.
- Oxford, Andrew Wathen, M1 Linear Algebra I2022–23: native pages70–78, including the declared complex convention.
- Berkeley, Alexander Paulin, Math54 Spring2018: all four native pages of Orthogonal Projections and the preceding audited orthogonality texts.
- ETH Zurich, Afonso S. Bandeira and Robert Weismantel: Linear Algebra PartII, section6.3, native pages19–23.
