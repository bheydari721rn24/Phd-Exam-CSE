## Final review: formulas, complete decisions, and boundary tests

Each rule names its geometry and assumptions. Reconstruct the derivation from the full lesson before using this section as a recall sheet. A plotted example illustrates an exact statement; it does not replace its proof.

### 1. Points and displacements have different roles

The displacement from A to B is $B-A$; reversing the endpoints negates it. Translation of the origin changes both point-coordinate lists but not their difference. For $A=(2,-1,3)$ and $B=(-1,4,5)$, the displacement is $(-3,5,2)$ and distance $\sqrt{38}$. Projecting onto an affine line begins with a displacement from its base point, not the target's raw coordinates.

### 2. A field is part of an independence question

The vectors 1 and i are independent over the reals but dependent over the complex numbers, since $i\cdot1-1\cdot i=0$. Specify the scalar field before using a dimension count. Zero vectors, repeated vectors, and scalar multiples supply immediate nontrivial relations. Pairwise nonparallel vectors need not form an independent larger list.

### 3. Span and unique coordinates require separate tests

Write a general linear combination and compare coordinates to test membership. For $u=(1,0,1)$ and $v=(0,1,1)$, the span is $z=x+y$. Appending $u+v$ changes neither this span nor its dimension, but produces nonunique coefficients. A basis must both span the stated space and be independent.

### 4. A union is not generally a sum

The two coordinate axes have a union excluding $(1,1)$, while their sum is the plane. A union of subspaces is a subspace precisely when one contains the other. Intersections are always subspaces and contain zero. “Zero intersection” means intersection exactly $\{0\}$, not disjoint sets.

### 5. Sum dimensions subtract the shared basis once

Use $\dim(U+V)=\dim U+\dim V-\dim(U\cap V)$. Two ten-dimensional subspaces with fifteen-dimensional sum have five-dimensional intersection. Individual dimensions alone do not fix the overlap. In ambient dimension d, require $\max(0,p+q-d)\le r\le\min(p,q)$ and use a coordinate-basis construction to verify attainability.

### 6. Constraints remove independent rank

Symmetric real n-by-n matrices have $n(n+1)/2$ parameters. For $n\ge1$, trace zero removes one, giving $n(n+1)/2-1$. Five-by-five gives fourteen. Repeated equations add no rank, and trace zero does not force every diagonal entry to vanish. At size zero the trace constraint is already vacuous.

### 7. Nullity belongs to the domain

For an m-by-k matrix acting on column vectors, $\dim\ker A=k-\operatorname{rank}A$. An eight-by-six rank-four matrix has nullity two; its transpose has nullity four. Never subtract rank from the row count without changing which map is being discussed. The rank cannot be negative or exceed either dimension.

### 8. Coordinate norms use the basis Gram matrix

If $x=Bc$, its squared Euclidean norm is $c^TB^TBc$. In the basis $(1,1),(1,-1)$, coordinates $(2,1)$ represent $(3,1)$ and have physical squared norm ten, not five. Orthogonality removes cross terms; unit lengths remove the remaining diagonal weights. Only an orthonormal basis permits the ordinary coordinate-square sum.

### 9. Squared norms keep their cross term

For real inner-product geometry, $\Vert x+y\Vert^2=\Vert x\Vert^2+2\langle x,y\rangle+\Vert y\Vert^2$. Lengths three and four with dot product twelve give sum squared length 49. A result of 25 has assumed perpendicularity without evidence. In complex geometry replace the cross term by twice the real part.

### 10. Cauchy–Schwarz equality means dependence

The bound $|\langle x,y\rangle|\le\Vert x\Vert\Vert y\Vert$ has equality exactly for dependence over the stated field, including zero cases. With squared lengths nine and sixteen and dot product twelve, $v=(4/3)u$. A negative endpoint gives the opposite direction. A dot product outside the feasible interval cannot describe such vectors.

### 11. Triangle equality has a stricter sign condition

Nonzero vectors in inner-product geometry attain $\Vert x+y\Vert=\Vert x\Vert+\Vert y\Vert$ only for positive real proportionality. Taking $v=-3u$ gives Cauchy–Schwarz equality but strict triangle inequality. Zero inputs are handled separately. Do not transfer an absolute-value equality condition to a signed sum.

### 12. Reverse triangle rejects impossible distances

Use $|\Vert x\Vert-\Vert y\Vert|\le\Vert x-y\Vert\le\Vert x\Vert+\Vert y\Vert$. Lengths two and three permit distances between one and five in a real space of dimension at least two; in one dimension only the sign cases give one or five. Construct an equality case when an optimization asks for attainability.

### 13. Zero vectors are orthogonal but have no angle

For nonzero real vectors, $\cos\theta=\langle x,y\rangle/(\Vert x\Vert\Vert y\Vert)$ and $\theta\in[0,\pi]$. The zero vector has zero inner product with every vector, but the angle formula divides by zero. The unsigned right angle is $\pi/2$, not the negative right-angle value in the corrected Stanford slide.

### 14. Positive weights define a geometry

The product $\sum w_ix_iy_i$ is positive definite on the full real coordinate space when all weights are positive. Zero weights permit a nonzero zero-length vector; negative weights permit negative self-products. With weights $(4,1)$, projecting $(1,0)$ onto $(1,1)$ gives $(4/5,4/5)$ rather than $(1/2,1/2)$. Use the same metric for both coefficient and normalization.

### 15. Orthogonality is one scalar equation

For $(1,n)$ and $(a,2)$ in Euclidean geometry, the equation is $a+2n=0$. At n five, a is $-10$; the two coordinate products cancel. Requiring each product to be zero is stronger and wrong here. Changing the metric to weights $(4,1)$ changes the equation to $4a+2n=0$.

### 16. Complex inner products need a fixed convention

This chapter uses $\langle u,v\rangle=\sum\overline{u_i}v_i$, linear in v. For $(1,i)$ and $(i,1)$ the product is zero, and the first vector has squared norm two. A bilinear self-product gives zero for that nonzero vector and cannot define its norm. Oxford's opposite convention is translated explicitly.

### 17. Complex Pythagoras has a one-way converse

Orthogonality implies squared-norm additivity. The converse of a single such equality only gives zero real part of the inner product. The one-dimensional complex vectors 1 and i satisfy $|1+i|^2=1+1$ but have inner product i. Do not infer complex orthogonality from a real-valued expansion alone.

### 18. Projection coefficient, component, vector, and length differ

For nonzero real b, coefficient is $c=(b\cdot x)/\Vert b\Vert^2$, signed unit component is $(b\cdot x)/\Vert b\Vert$, and projected vector is cb. Projecting $(5,1,2)$ onto $(1,1,0)$ gives coefficient three, component $3\sqrt2$, vector $(3,3,0)$, and squared length eighteen. State which quantity is requested before computing.

### 19. Rescaling a nonzero generator preserves its span

Replacing b by tb with $t\ne0$ changes the coefficient to c/t and leaves the projected vector unchanged. At t zero the quotient is undefined, but projection onto the zero subspace is zero. The mathematical object can remain defined after one representation formula fails.

### 20. A projection answer needs two certificates

Check that p belongs to the target span and that $x-p$ is perpendicular to every generator. In Question 37, $(2,1,1)$ passes membership but fails one residual test. The correct $(7/3,2/3,5/3)$ passes both. These certificates prove unique nearest-point optimality through Pythagorean error decomposition.

### 21. Nonorthogonal directions require coupled coefficients

Solve $Gc=B^Tx$ for real independent generators, with $G=B^TB$. For $u=(1,0,1)$, $v=(1,1,0)$ and $x=(1,2,3)$, $G=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ and c is $(5/3,2/3)$. Summing separate line projections ignores the off-diagonal interaction. With dependent generators the vector can remain unique while its coefficients are nonunique.

### 22. Orthogonal does not mean orthonormal

An orthogonal nonzero basis needs each denominator $\Vert u_k\Vert^2$ in its projection sum. With $u=(2,0)$, the unnormalized source sum produces $\operatorname{diag}(4,0)$ rather than a projection. The authentic Q31 wording is therefore marked ambiguous; option three is explained only under an added normalization interpretation. Preserve the source condition rather than silently strengthening it.

### 23. Idempotence alone does not imply contraction

The oblique map $Q=\begin{pmatrix}1&2\\0&0\end{pmatrix}$ satisfies $Q^2=Q$ but increases the length of $(0,1)$ to two. True orthogonal projection satisfies $\Vert Px\Vert\le\Vert x\Vert$, with equality precisely for x in its image. For the full-space projection every vector has equality.

### 24. Residual energy and captured energy form a partition

For a true orthogonal projection, $\Vert x\Vert^2=\Vert Px\Vert^2+\Vert x-Px\Vert^2$. Question 22 gives $69=81/2+57/2$. A squared length cannot be replaced by a coefficient or a length without a square root. For perpendicular nonzero inputs the residual-length ratio is one; for image vectors it is zero.

### 25. Bessel and Parseval distinguish a list from a complete basis

For an orthonormal list, $\sum|\langle q_j,x\rangle|^2\le\Vert x\Vert^2$; the gap is residual squared norm. Two xy-plane directions applied to $(2,1,3)$ capture energy five of fourteen. Equality holds for x in their span; a basis of the entire space gives equality for every x. In complex cases use squared magnitudes.

### 26. Gram–Schmidt skips a zero residual

Subtract every retained direction's component before normalizing. Inputs $(1,1),(2,2),(0,0),(1,-1)$ produce two unit directions, with the middle two skipped. A zero residual does not force termination of the whole algorithm. A tiny nonzero residual is mathematically independent; numerical decisions need an explicit error scale and tolerance.

### 27. An affine foot requires translation

For $L=P+\operatorname{span}b$, project $X-P$ and add P back. For $X=(4,0)$ and $P=(1,2),b=(2,1)$, the foot is $(13/5,14/5)$. Directly projecting X finds a point on a different line through zero. Membership and residual perpendicularity must be checked after translating back.

### 28. Plane distance uses the normal length once

For $a\cdot X=d$, distance is $|a\cdot X-d|/\Vert a\Vert$, while the foot correction coefficient divides by $\Vert a\Vert^2$. Question 38 has residual two, normal length three, distance $2/3$, and coefficient $2/9$. Scaling the entire equation preserves the plane and distance. A zero normal means either the whole space or an inconsistent empty set.

### 29. Optimization needs feasibility and an attaining case

On $x+y+z=6$, the unique squared-norm minimum is twelve at $(2,2,2)$. On $x+y=1,y+z=1$, it is $2/3$ at $(1/3,2/3,1/3)$. A complete square proves global optimality, and substitution proves feasibility. A feasible larger value or an unachieved lower bound is not the answer.

### 30. Norm lower bounds do not imply positive definiteness

$A=-I$ satisfies $\Vert Ax\Vert\ge\Vert x\Vert$ in every norm but has a negative quadratic form. For a square map the lower bound does imply invertibility and an induced inverse norm bound. The Frobenius norm is different: $I_n$ has operator norm one and Frobenius norm $\sqrt n$. A magnitude statement is not a positivity statement about eigenvalues or quadratic forms.

### 31. Parameter endpoints need a null-direction witness

The real symmetric three-by-three matrix with diagonal one and off-diagonal a is positive definite precisely on $(-1/2,1)$. At the lower endpoint its all-equal direction is null; at the upper endpoint its sum-zero plane is null. Outside, one direction has negative quadratic form. For a Gram matrix, determinant zero signals dependence, not merely small vector lengths.

### 32. Products, polynomial geometry, and parity retain their domains

In oriented real three-space, $\Vert u\times v\Vert$ is parallelogram area, triangle area is half, and $|u\cdot(v\times w)|$ is parallelepiped volume. Use side differences from one vertex and retain cross-product parentheses. In polynomial integral geometry, odd functions integrate to zero over symmetric intervals: $t^3$ projects to zero on $\operatorname{span}(1,t^2)$, and $t^2-1/3$ has squared norm $8/45$. Negative cosine frequencies can represent the same function. None of these facts authorizes arbitrary-dimensional cross products or infinite Fourier convergence claims.

### Final verification sequence

State the field, ambient space and inner product; check feasibility and every denominator; derive the required vector or scalar; reconstruct coordinates or substitute constraints; check residual orthogonality with the actual metric; compare a second route or boundary. The recorded sources and finite tests support the stated scope. They do not establish a worldwide optimal course selection or a guarantee for every unseen examination question.
