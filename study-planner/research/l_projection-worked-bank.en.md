# Orthogonal projections: worked bank in progress

This is the first ten fully derived problems for the unfinished new projection chapter. It is not a completed chapter, a published bank, or an official examination key. Difficulty is an author assessment. The full chapter will integrate these derivations with figures, mechanism-specific simulations, further questions and complete final decisions after source and rendered audits. Exact real arithmetic is used unless complex arithmetic is explicitly stated.

## Problem 1. Build one plane projector by two independent routes

**Question.** Let S be spanned by (1,0,1) and (0,1,1). Find its orthogonal projection matrix, the projection of b=(2,1,0), and the squared distance from b to S. Explain why the closest point is unique.

**Solution.** Put the generators into the columns of

$$A=\begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix},\qquad A^TA=\begin{bmatrix}2&1\\1&2\end{bmatrix}.$$

The determinant of the Gram matrix is three, so the independent-column formula applies. Its inverse is one third of the matrix with diagonal two and off-diagonal negative one. Multiplication gives

$$P=A(A^TA)^{-1}A^T=\frac13\begin{bmatrix}2&-1&1\\-1&2&1\\1&1&2\end{bmatrix}.$$

A normal to S is n=(−1,−1,1), since its dot product with either generator is zero. Its squared length is three, so the complementary route gives $P=I-nn^T/3$, reproducing every entry above. This agreement checks both the subspace and the dimensions of the construction.

The projected point is p=(1,0,1), and the residual is r=b−p=(1,1,−1)=−n. The point p belongs to S; its coefficients in the displayed basis are (1,0). The residual is perpendicular to both generators. Thus $\Vert r\Vert^2=3$ is the squared distance. For any other s in S, the decomposition b−s=r+(p−s) has perpendicular terms, so its squared norm is three plus $\Vert p-s\Vert^2$. Equality occurs only at s=p, proving uniqueness. Checking only that p and r have zero dot product would be weaker: the residual must be perpendicular to the entire subspace.

## Problem 2. Dependent generators do not destroy a unique projection

**Question.** Let A have columns u=(1,2,0) and 2u. For b=(2,1,3), determine the projection, all coefficient vectors producing it, and the minimum-norm coefficient vector. Explain why directly inverting A transpose A is invalid.

**Solution.** Both columns describe the same line S. Its projector depends on u, not on how often u is listed:

$$P=\frac{uu^T}{u^Tu}=\frac15\begin{bmatrix}1&2&0\\2&4&0\\0&0&0\end{bmatrix}.$$

Here u transpose b is four. Hence $p=(4/5,8/5,0)^T$ and $r=(6/5,-3/5,3)^T$. The residual satisfies u transpose r=0, and its squared norm is $36/25+9/25+9=54/5$. The projection is unique by the closest-point theorem.

Coefficients c satisfy $Ac=u(c_1+2c_2)$, so the full coefficient family is $c_1+2c_2=4/5$. Writing c₂=t gives c₁=4/5−2t. The squared coefficient norm is $(4/5-2t)^2+t^2$. Completing the square, or differentiating this exact quadratic, gives t=8/25 and c₁=4/25. Thus the minimum-norm coefficient vector is (4/25,8/25), while infinitely many other coefficient vectors produce the same physical p.

The Gram matrix has proportional columns and determinant zero; it has no inverse. Selecting the single column basis u is sufficient to construct P. If a pseudoinverse is used, it must be derived correctly: $A^+=\frac1{25}\begin{bmatrix}1&2&0\\2&4&0\end{bmatrix}$ yields the same minimum-norm coefficients and satisfies $AA^+=P$. Unique physical projection and unique generator coordinates are different claims.

## Problem 3. Determine the scale instead of assuming symmetry is enough

**Question.** For a nonzero real scalar a, consider $M=a\begin{bmatrix}1&2\\2&4\end{bmatrix}$. For which a is M an orthogonal projection? Give its range and explain what fails at a=1/2.

**Solution.** Let B be the unscaled displayed matrix. Direct multiplication gives $B^2=5B$. Since M is symmetric for every real a, the missing condition is idempotence. The equation $M^2=M$ becomes $5a^2B=aB$. Because B is nonzero and a is nonzero, this reduces to 5a=1, so a=1/5. The excluded a=0 would give the zero-space projection, but it is outside the question's nonzero premise.

At a=1/5, M is $uu^T/(u^Tu)$ for u=(1,2), so its range is the line spanned by u and its kernel is the perpendicular line spanned by (−2,1). It fixes u and kills that normal. Those two actions give a direct decomposition certificate as well as the matrix identity test.

At a=1/2, the matrix remains symmetric and has the same range, but it multiplies u by 5/2 instead of fixing it. Applying it twice scales that component by 25/4, which differs from the first application. Thus range information and symmetry do not establish that the map is a projection. The error is an incorrect normalization, not a changed geometric line. A rank-one outer product requires division by the generator's squared length; rescaling the generator without preserving that normalization changes the operator.

## Problem 4. Weighted perpendicularity can look nonsymmetric

**Question.** Use the weighted inner product $\langle x,y\rangle_W=x^TWy$ with W=diag(1,4). Project b=(2,−1) onto the line spanned by u=(1,1). Find the matrix and verify a weighted energy split. Is the projector symmetric in ordinary coordinates?

**Solution.** The projection coefficient is $(u^TWb)/(u^TWu)$. Its numerator is 2−4=−2 and its denominator is 1+4=5. Therefore p=(−2/5,−2/5) and r=(12/5,−3/5). The matrix is

$$P_W=u(u^TWu)^{-1}u^TW=\frac15\begin{bmatrix}1&4\\1&4\end{bmatrix}.$$

It is not ordinarily symmetric because its off-diagonal entries differ. Nevertheless it is idempotent and satisfies the correct weighted self-adjoint relation $P_W^TW=WP_W$. Weighted perpendicularity is verified by $u^TWr=12/5+4(-3/5)=0$. Ordinary u transpose r is 9/5 rather than zero, so applying the ordinary Euclidean perpendicularity test would reject a valid weighted projection.

The original weighted squared norm is $2^2+4(-1)^2=8$. The projected energy is $5(2/5)^2=4/5$, and the residual energy is $(12/5)^2+4(3/5)^2=36/5$. Their sum is eight. This Pythagorean identity uses the same positive-definite W as the projection. Mixing an ordinary norm on one side with weighted energies on the other would compare different metrics. A nonsymmetric matrix can thus be an orthogonal projector in a declared weighted geometry while failing ordinary Euclidean orthogonality.

## Problem 5. An affine hyperplane is not a linear subspace

**Question.** Find the closest point to b=(3,1,0) on the affine plane $x+2y-z=3$, and its squared distance. State the affine projection map and explain why it is not linear.

**Solution.** The normal is n=(1,2,−1), with squared length six. Its dot product with b is five, exceeding the required plane value by two. Subtract the normal correction:

$$p=b-\frac{n^Tb-3}{n^Tn}n=(8/3,1/3,1/3)^T.$$

The plane equation checks directly: 8/3+2/3−1/3=3. The residual b−p=(1/3,2/3,−1/3) is a multiple of n and therefore perpendicular to every direction lying in the plane. Its squared norm is (1+4+1)/9=2/3. The direction-space certificate establishes unique closest-point optimality: subtracting any other point in the same plane creates a direction perpendicular to this residual.

For general input x, the closest-point map is $F(x)=(I-nn^T/6)x+n/2$. Its constant term is nonzero, so F(0)=n/2 rather than zero. Thus F is affine but not linear. It fixes every point on the plane and satisfies F(F(x))=F(x), yet those properties alone do not make it a linear projection matrix. Translating the plane to its parallel subspace, projecting the translated vector, and translating back provides another derivation. The distinction prevents replacing an affine constraint by a homogeneous one and returning the wrong closest point.

## Problem 6. A commuting product and a nonprojecting sum

**Question.** Let P=diag(1,1,0) and Q=diag(0,1,1). Determine projectors onto the intersection and sum of their ranges. Is P+Q itself a projection?

**Solution.** P selects the first two coordinate directions, and Q selects the last two. They commute because both are diagonal. Their common range is the second coordinate axis, and $PQ=\operatorname{diag}(0,1,0)$ is its projector. The sum of the ranges is the whole three-dimensional space, whose projector is $P+Q-PQ=I$. The subtraction removes the double count of the common coordinate.

The plain sum P+Q is diag(1,2,1). It sends e₂ to 2e₂, so it does not fix a vector in its alleged range; squaring gives diag(1,4,1), which differs. It is symmetric and positive semidefinite but not idempotent. A trace value four is also incompatible with an ordinary orthogonal projector in dimension three.

More generally, for commuting orthogonal projectors, PQ is symmetric and idempotent because transposition reverses the product and commutation restores it, while $(PQ)^2=P^2Q^2=PQ$. Its range lies in both ranges and it fixes their intersection. The complementary commuting product (I−P)(I−Q) projects onto the intersection of the complements. Taking its complement gives P+Q−PQ, the sum-space projector. Without commutation these algebraic simplifications are invalid. A formula verified on diagonal examples must still have its general hypothesis declared before use.

## Problem 7. A fractional trace refutes an intersection shortcut

**Question.** In the plane, let P project onto the first coordinate axis and Q onto the line spanned by (1,1). Compute PQ, decide whether it is a projection, and compare its trace with the dimension of the intersection.

**Solution.** The matrices and product are

$$P=\begin{bmatrix}1&0\\0&0\end{bmatrix},\quad Q=\frac12\begin{bmatrix}1&1\\1&1\end{bmatrix},\quad PQ=\frac12\begin{bmatrix}1&1\\0&0\end{bmatrix}.$$

The reverse product is one half of the matrix with rows (1,0) and (1,0), so the two products differ. Squaring PQ gives one quarter of its unscaled displayed matrix, or one half of PQ. Thus PQ is not idempotent and is not an orthogonal projector. It is also nonsymmetric.

The two distinct lines intersect only at zero, so their intersection dimension is zero. But trace(PQ)=1/2. The equality between trace and rank applies to an idempotent matrix; it cannot be applied to an arbitrary product of idempotent matrices. Here the product's nonzero eigenvalue is 1/2 rather than one, reflecting attenuation caused by the angle between the lines.

As an additional exact check, $\Vert P-Q\Vert_F^2=1$. The identity rank(P)+rank(Q)−2trace(PQ) gives 1+1−1=1, agreeing with direct entrywise squares. This geometric trace identity does not turn the fractional trace into an integer intersection dimension. The counterexample pinpoints the missing commutation premise rather than rejecting every useful relationship between two projection matrices.

## Problem 8. Conjugation is a substantive operation

**Question.** In complex Euclidean space, project b=(1,1) onto the line generated by u=(1,i), using the convention conjugate-linear in the first argument. Find p and r and diagnose the ordinary-transpose formula.

**Solution.** The squared norm is $u^*u=1+(-i)i=2$. The coefficient is $u^*b/2=(1-i)/2$, so

$$P=\frac12\begin{bmatrix}1&-i\\i&1\end{bmatrix},\quad p=\frac12\begin{bmatrix}1-i\\1+i\end{bmatrix},\quad r=\frac12\begin{bmatrix}1+i\\1-i\end{bmatrix}.$$

The projector is Hermitian: its off-diagonal entries are conjugates. The residual check is $u^*r=(1+i)/2-i(1-i)/2=0$. Each projected coordinate has squared magnitude 1/2, so the projected squared norm is one; the residual also has squared norm one. Their sum equals the original squared norm two, confirming the complex Pythagorean split.

Using u transpose instead would produce $u^Tu=1+i^2=0$ even though u is nonzero. That expression is not a positive-definite squared norm and cannot appear as the denominator of this Hermitian projection formula. The problem is not numerical roundoff; it is the wrong bilinear form. Other authors use a first-argument-linear convention, which changes the written coefficient orientation. Either convention can work if applied consistently, but a displayed conjugate must not be dropped during transcription or inferred solely from a real-valued example.

## Problem 9. Diagonal data reveals fixed and killed coordinates

**Question.** An ordinary orthogonal projector has diagonal (1,1/2,1/2). Determine its possible matrices in three dimensions. Explain why diagonal (1,0,1/2) cannot be the diagonal of another such projector.

**Solution.** For an orthogonal projector, $P_{jj}=\Vert Pe_j\Vert^2$ and $1-P_{jj}=\Vert(I-P)e_j\Vert^2$. A first diagonal entry one forces (I−P)e₁=0, hence Pe₁=e₁. Symmetry then fixes the first row and column as (1,0,0). The remaining symmetric block has the form $\begin{bmatrix}1/2&t\\t&1/2\end{bmatrix}$.

Its idempotence equation on a diagonal entry is 1/4+t²=1/2, giving t=±1/2. The off-diagonal equation is already t=t. Thus exactly two matrices fit: first coordinate fixed, with a rank-one projector onto either (0,1,1) or (0,1,−1) in the remaining coordinate plane. Both have total trace two and rank two.

By contrast, diagonal (1,0,1/2) would have trace 3/2. Over the declared real finite-dimensional model, every idempotent matrix has eigenvalues zero or one and is diagonalizable, so its trace is its integer rank. The fractional value rules out existence. Bounds placing every diagonal entry in [0,1] are necessary but not sufficient. A diagonal value zero also forces the corresponding row and column to vanish for an orthogonal projector, because the projected coordinate vector has zero norm. These structural constraints provide more information than a numerical trace check alone.

## Problem 10. Idempotence does not control Euclidean expansion

**Question.** Let $E=\begin{bmatrix}1&t\\0&0\end{bmatrix}$ with real t≠0. Determine its image, kernel and Euclidean operator norm. Is it an ordinary orthogonal projection despite E squared equaling E?

**Solution.** E maps (x,y) to (x+ty,0). Its image is the first coordinate axis and its kernel is the line x+ty=0, generated by (−t,1). Direct multiplication verifies E²=E, so it is an algebraic projector onto its image along that kernel. The kernel is not perpendicular to the image when t≠0.

The output length is $|x+ty|$. For a unit input, Cauchy–Schwarz bounds this by $\sqrt{1+t^2}$, and the input $(1,t)/\sqrt{1+t^2}$ attains that bound. Therefore $\Vert E\Vert_2=\sqrt{1+t^2}>1$. The matrix is nonsymmetric, and it expands some unit vectors. Both facts distinguish it from an ordinary orthogonal projection, which is contractive.

For example, E sends b=(0,1) to p=(t,0), with residual r=(−t,1). The residual dot e₁ is −t rather than zero, so the closest-point certificate fails; the actual orthogonal projection of b onto the image is zero. Eigenvalues zero and one, integer trace one, and idempotence establish an algebraic projection but do not establish orthogonality. The example explains why a spectral-radius bound of one is not an operator-norm bound of one for a nonnormal matrix. The geometry of the kernel and the declared inner product are essential.

## Current completion boundary

These ten derivations advance the new projection chapter's mathematical bank. They do not complete its required figures, simulations, source selection, full problem coverage, final summary or rendered review. The bank stays an authoring draft and is not included in the count of finished technical notes. The four working course selections and additional ETH support remain traceable in `l_projection-source-audit.md`; fresh MIT reading and Berkeley source-image inspection are recorded separately.
