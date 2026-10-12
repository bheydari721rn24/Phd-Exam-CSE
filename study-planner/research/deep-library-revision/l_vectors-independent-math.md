# Independent mathematical audit: l_vectors

Audit date: 12 October 2026. Scope: all 46 existing question stems, options and previous answers were individually read using `read_deep_revision.py` in ranges 1–16, 17–32 and 33–46. The four new draft solutions in `l_vectors-solutions-part1.md` were also read. This report does not mark the chapter delivered, scientifically infallible, or student-approved. No lesson, question bank, publication state, or shared manuscript was edited during this audit.

## 1. Original source inspection and two necessary corrections

The two full-page PNGs in `Temp/deep-vector-sources` were actually viewed. The first contains MSc CS 1405 Q41 on PDF page 9. The second contains PhD CS 1404 Q30, Q31 and Q32 on PDF page 8. The original PDF hashes were independently recomputed and match the canonical records:

- MSc CS 1405: `198f75f9f9d195adc5c09ab14d17029e63a3cd11030d62cffcdfcb5df7627527`.
- PhD CS 1404: `928e51b55059b3094583f9c190e260b405ec775da05f6c7679675e332a8a6f40`.

### Authentic Q3: orthogonal is not automatically orthonormal

The Persian source says an **orthogonal basis**; it does not visibly supply the word meaning unit or normalized. The English canonical question currently says **orthonormal basis**, which adds a substantive assumption. With a merely orthogonal nonzero basis, the displayed map

\[
Px=\sum_k\langle x,u_k\rangle u_k
\]

need not be idempotent. For one basis vector \(u=(2,0)\), the map is \(P=\operatorname{diag}(4,0)\), so \(P^2=\operatorname{diag}(16,0)\ne P\). Therefore option 1 as well as the reversed universal inequality in option 3 fails as a general theorem under the literal orthogonal-basis wording. To obtain the true orthogonal projection with a nonunit orthogonal basis, use

\[
P_Ux=\sum_k\frac{\langle x,u_k\rangle}{\langle u_k,u_k\rangle}u_k
\]

in the real inner-product convention used by the authentic question.

**Required handling:** preserve the literal source and explain the intended normalized interpretation. Record `answer=null`, `intendedAnswer=3`, and an explicit source-ambiguity status in the canonical item; this change is to be performed by the integrating agent. Do not present option 3 as an unqualified unique literal answer or call a derived key official. The existing part1 proof is correct for an orthonormal basis, but its source-boundary note needs this additional ambiguity.

There is a second independent boundary even with orthonormal vectors: the source permits \(n=m\). Then \(U=\mathbb R^m\), \(P=I\), and all four displayed assertions hold. Option 3 is false as a universal proposed theorem over the permitted choices of subspace; it is not false for every permitted fixed configuration. For a proper subspace, a nonzero perpendicular vector supplies a counterexample.

### Authored Q12: the ambient-space distractor is ambiguous

Option 4 currently says the overlap dimension is independent of the ambient space. If fixed subspaces are embedded in a larger ambient space, their intersection dimension indeed remains unchanged. What does change with relative positioning, and with the feasible range imposed by the ambient dimension, is the intersection dimension among different pairs of subspaces. A precise false distractor is:

> The individual dimensions determine the intersection dimension regardless of the relative positions of the two subspaces.

Option 1 remains the intended true answer. This is an authored question, so correcting that distractor does not modify an authentic examination.

## 2. Exact answer ledger for all placements

The table uses existing option order. Q3 requires the qualifications above. Remaining entries agree with independent algebra; no official answer key was assumed.

| Q | Correct option | Exact requested result or assertion |
|---|---:|---|
| 1 | 2 | Dimension 9 |
| 2 | 2 | Positive definiteness does not follow |
| 3 | Qualified | Intended normalized general-theorem answer 3; literal source ambiguity affects 1 too |
| 4 | 2 | \(-1/2<a<1\) |
| 5 | 2 | 14 |
| 6 | 1 | 35 |
| 7 | 4 | \(n(n+1)/2-1\), positive integer \(n\) |
| 8 | 3 | The trace restriction has rank one over the real field |
| 9 | 4 | 5 |
| 10 | 3 | 8 |
| 11 | 2 | Intersection dimension \(n\) |
| 12 | 1 | A union is not generally the sum; correct ambiguous distractor 4 |
| 13 | 1 | Nullity 2 |
| 14 | 4 | Nullity 2 |
| 15 | 3 | Nullity 2 |
| 16 | 2 | Use the column dimension of the map acting on column vectors |
| 17 | 2 | Squared projection norm 18 |
| 18 | 1 | Squared projection norm \(81/2\) |
| 19 | 4 | \((n+1)^2/2\) |
| 20 | 3 | A nonunit direction needs the squared-norm denominator |
| 21 | 2 | Squared residual norm 12 |
| 22 | 1 | Squared residual norm \(57/2\) |
| 23 | 4 | \((n-1)^2/2+4\) |
| 24 | 3 | Orthogonality justifies the Pythagorean subtraction as a general rule |
| 25 | 4 | \(a=-10\) |
| 26 | 3 | \(a=-16\) |
| 27 | 2 | \(a=-2n\) |
| 28 | 1 | Orthogonality depends on the specified inner product |
| 29 | 4 | First coordinate \(7/2\) |
| 30 | 3 | First coordinate 5 |
| 31 | 2 | First coordinate \((n+2)/2\) |
| 32 | 1 | Basis order determines coordinate order |
| 33 | 1 | Dimension 5 |
| 34 | 4 | Dimension 8 |
| 35 | 3 | Dimension \(n\) |
| 36 | 2 | A nonzero constant sum defines an affine set, not a vector subspace |
| 37 | 1 | Projection \((7/3,2/3,5/3)\) |
| 38 | 1 | Distance \(2/3\) |
| 39 | 2 | Independence exactly when \(a\ne-1\) |
| 40 | 1 | Minimum squared norm 12, uniquely at \((2,2,2)\) |
| 41 | 1 | Coordinates \((2,1)\), squared norm 10 |
| 42 | 1 | Hermitian inner product 0, squared norm 2 |
| 43 | 3 | Residual-to-original norm ratio 1 |
| 44 | 3 | Dependent, same direction |
| 45 | 2 | Projection \((2/3,1/3,1/3)\) |
| 46 | 2 | Minimum squared norm \(2/3\) |

## 3. Family-level independent derivations, option failures and boundaries

### Q1 and Q5–8: symmetric matrices subject to trace zero

The independent entries comprise \(n\) diagonal entries and \(n(n-1)/2\) upper off-diagonal entries. The trace functional is nonzero: it maps \(E_{11}\) to 1. Its kernel therefore has dimension

\[
\frac{n(n+1)}2-1=\frac{n(n-1)}2+(n-1).
\]

A basis is \(E_{ij}+E_{ji}\) for \(i<j\), and \(E_{ii}-E_{nn}\) for \(1\le i<n\). Inspecting the off-diagonal entries and then the first \(n-1\) diagonal entries proves independence. Every matrix expands uniquely in this list. At sizes 5 and 8 the results are respectively \(10+4=14\) and \(28+7=35\).

The distractor \(n^2-1\) incorrectly treats asymmetric entries as independent. The distractor \(n(n+1)/2\) omits trace. The distractor \(n(n-1)/2\) incorrectly sets each diagonal entry to zero. Trace zero allows cancellation, such as diagonal entries 1 and -1. Repeated copies of an equation do not change its rank. At \(n=1\) the dimension is zero; at \(n=0\) the trace rank is zero and the displayed subtract-one formula is inapplicable. This is a real vector-space question; do not use complex symmetric and Hermitian dimensions interchangeably.

### Q2: arbitrary real norm, inverse bound and complex eigenvalues

The bound with positive \(\theta\) makes the kernel trivial. Squareness then yields invertibility. Substituting \(x=A^{-1}y\) proves the inverse induced-norm bound. The counterexample \(A=-I\), \(\theta=1\), works for every vector norm and gives a strictly negative Euclidean quadratic form on nonzero vectors. The existing part1 argument proving the modulus bound for nonreal eigenvalues under an arbitrary finite-dimensional real norm is sound: use inverse powers, norm equivalence and a real-to-complex Euclidean extension, then take kth roots. The constant \(C/c\) must stay outside the kth power, otherwise the final sharp lower bound is lost. The result is not a positivity criterion or a claim that each eigenvalue itself is positive. A rectangular injective map lacks the stated two-sided inverse.

### Q3: projection

Under normalized basis vectors, residual orthogonality gives

\[
\|x\|_2^2=\|Px\|_2^2+\|x-Px\|_2^2.
\]

Equality in contraction holds exactly on the range. For a proper range, a nonzero vector in its orthogonal complement contradicts the reversed inequality. An idempotent oblique map is not necessarily contractive: \(Q=\begin{pmatrix}1&2\\0&0\end{pmatrix}\) maps \((0,1)\) to \((2,0)\). Add both literal-source ambiguities from Section 1 to the present proof.

### Q4: structured positive definiteness

Write \(A=(1-a)I+a\mathbf1\mathbf1^T\). For \(x=s\mathbf1+z\), \(\sum z_i=0\), the components are perpendicular and

\[
x^TAx=3(1+2a)s^2+(1-a)\|z\|_2^2.
\]

Both coefficients must be positive, and this is sufficient. At \(-1/2\), the all-equal line is null; at 1, the sum-zero plane is null. The endpoints are semidefinite, not definite. Option 1 admits \(a=-3/4\), which gives a negative all-equal direction. Options 3 and 4 omit valid parameters such as \(3/4\) and \(-1/4\). For analogous dimension \(n\ge2\), the eigenvalues are \(1+(n-1)a\) once and \(1-a\) with multiplicity \(n-1\), giving \(-1/(n-1)<a<1\). At \(n=1\), the matrix is (1) and the off-diagonal parameter is unused. Determinant positivity alone is not a general definiteness test: here \(\det A=(1-a)^2(1+2a)\) is positive for \(a>1\), yet the sum-zero directions are negative.

### Q9–12: sum and intersection

The linear map \(U\times V\to U+V\), \((u,v)\mapsto u+v\), is onto, and its kernel is \(\{(w,-w):w\in U\cap V\}\). Rank-nullity gives

\[
\dim(U\cap V)=2n+2n-3n=n.
\]

Results 5 and 8 are exact. Zero incorrectly assumes a direct sum, \(2n\) incorrectly assumes coincidence, and \(3n\) exceeds each intersection's individual dimension bound. An explicit realization is \(U=\operatorname{span}(e_1,\ldots,e_{2n})\) and \(V=\operatorname{span}(e_{n+1},\ldots,e_{3n})\); the overlap has basis \(e_{n+1},\ldots,e_{2n}\). The union of two subspaces is a subspace iff one contains the other: if neither does, \(u\in U\setminus V\), \(v\in V\setminus U\) have sum in neither. Correct Q12 option 4 as above.

### Q13–16: shape, rank and nullity

The matrix represents a map from \(\mathbb R^{n+1}\) to \(\mathbb R^{n+3}\); nullity is \((n+1)-(n-1)=2\). At \(n=5\), the shape is \(8\times6\), rank 4, kernel dimension 2. At \(n=8\), it is \(11\times9\), rank 7, again kernel dimension 2. Its transpose has nullity \((n+3)-(n-1)=4\). Therefore rows-minus-rank answers a different question. Positive integer \(n\) makes the stated rank feasible, including \(n=1\) and rank zero. \(n=0\) would impose impossible rank -1. A rectangular map may have a kernel; injectivity does not depend on squareness alone.

### Q17–24: projection and orthogonal residual

For \(w=(n,1,2)\), \(u=(1,1,0)\),

\[
p=\frac{n+1}{2}(1,1,0),\qquad r=\left(\frac{n-1}{2},-\frac{n-1}{2},2\right),\qquad r\cdot u=0.
\]

Thus \(\|p\|^2=(n+1)^2/2\) and \(\|r\|^2=(n-1)^2/2+4\); their sum is \(n^2+5\). At 5 these are 18 and 12; at 8, \(81/2\) and \(57/2\). The coefficient \((n+1)/2\), squared length and vector are different objects. The distractor \((n-1)^2/2\) in the projection family computes only the horizontal part of the residual. The residual-family distractor 4 retains only the third coordinate; it coincides with the correct expression at \(n=1\), not at the tested values. Neither a nonzero projection nor a nonzero residual precludes the other.

Rescale a nonzero direction by \(t\ne0\): its coefficient becomes \((n+1)/(2t)\), and the vector is unchanged. Scaling by zero destroys a spanning direction and must be excluded. General decompositions have a cross term \(2p\cdot r\); orthogonality supplies its vanishing. In this family the formula extends to every real \(n\), including \(n=-1\) giving zero projection, and \(n=1\) giving a purely vertical residual. Avoid claiming that accidental cancellation is impossible for a particular nonorthogonal decomposition; the criterion concerns a universally justified rule.

### Q25–28: perpendicularity depends on the metric

For the specified Euclidean product, \((1,n)\cdot(a,2)=a+2n\), giving \(a=-2n\): -10 and -16. Positive choices reverse the cancellation sign, while \(-n\) omits the factor 2. Individual coordinate products need not vanish: here they are \(-2n\) and \(2n\). Under the valid weighted inner product with matrix \(\operatorname{diag}(1,2)\), the equation is \(a+4n=0\), giving \(a=-4n\). This counterexample proves that arbitrary metric changes need not preserve the same perpendicular pairs. A positive scalar multiple of the Euclidean inner product does preserve all orthogonality, so do not claim every metric change changes every pair.

### Q29–32: ordered basis coordinates

With columns \(B=\begin{pmatrix}1&1\\1&-1\end{pmatrix}\), \(\det B=-2\), so \(B^{-1}=B/2\). Hence

\[
[v]_B=\left(\frac{n+2}{2},\frac{n-2}{2}\right).
\]

The first coordinates at 5 and 8 are \(7/2\) and 5. \((n-2)/2\) is the second coordinate; \(n\) is the first standard coordinate, while \(2n\) is neither. Basis order matters: swapping basis columns swaps coordinate positions. A dependent spanning list cannot give unique coefficients; for example the list \((e_1,e_1)\) represents \(e_1\) by both (1,0) and (0,1). Orthogonality alone is not orthonormality: \(B^TB=2I\), so \(\|v\|^2=2(c_1^2+c_2^2)=n^2+4\), not \(c_1^2+c_2^2\).

### Q33–36: homogeneous versus affine hyperplanes

The coordinate-sum map on \(\mathbb R^{n+1}\) has rank one because it takes value 1 on any standard basis vector. Its kernel has basis \(e_i-e_{n+1}\), \(1\le i\le n\), and dimension \(n\), giving 5 and 8. The ambient dimension \(n+1\) ignores the constraint, 1 confuses functional rank with kernel dimension, and \(n-1\) subtracts too many independent conditions. A fixed nonzero sum \(c\) gives the translate \((c,0,\ldots,0)+\ker f\), with affine dimension \(n\) but no zero vector and no vector-subspace structure. Inconsistent systems, unlike this onto single functional, can have empty affine solution sets. At \(n=0\), the homogeneous kernel is the zero subspace of \(\mathbb R\), dimension zero.

## 4. Independent checks of all integrated questions

### Q37

\(G=\begin{pmatrix}2&1\\1&2\end{pmatrix}\), right-hand side (4,3). Its determinant is 3 and inverse is \(\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\), giving coefficients \((5/3,2/3)\). Projection is \((7/3,2/3,5/3)\); residual is \((-4/3,4/3,4/3)\), perpendicular to both directions. Squared norms are \(26/3\) and \(16/3\), totaling 14. A normal is \((-1,1,1)\), and removing \((4/3)(-1,1,1)\) gives the same result. Among the other three candidates, the original w is not in the span; (4,3,4) is not in the span either; (2,1,1) is in the span but its residual is not orthogonal. Adding the separate projections actually gives \((7/2,3/2,2)\), not one of those options, so do not attribute that specific wrong method to a listed value without calculation.

### Q38

Normal \(h=(2,-1,2)\) has squared length 9. Signed equation residual is 2, so distance is \(2/3\); the nearest point is \((5/9,20/9,23/9)\). Its plane expression is exactly 4. The removed vector \((4/9,-2/9,4/9)\) has squared length \(4/9\). Divide the absolute residual by \(\|h\|\), not \(\|h\|^2\), when requesting distance; the squared denominator belongs to the correction coefficient. A nonzero scaling of the entire plane equation changes numerator and denominator by the same absolute factor.

### Q39

The column determinant is \(-(a+1)\). At \(a=-1\), coefficients (1,-1,-1) give a nontrivial relation. At \(a=0\) and \(a=1\) the determinant is nonzero, contradicting options excluding those values; any negative \(a\ne-1\) contradicts positivity as a necessary condition. At the exceptional value the first two columns remain independent, so rank is exactly 2, not zero or one.

### Q40

\(x^2+y^2+z^2\ge(x+y+z)^2/3=12\), with equality iff all three coordinates coincide. The constraint then forces (2,2,2), proving uniqueness. (6,0,0) is feasible but has squared norm 36. (1,2,3) is feasible but has squared norm 14, not 6. Zero is infeasible. More generally, sum \(c\) in \(d\) coordinates gives minimum \(c^2/d\), attained at \((c/d)\mathbf1\), with positive \(d\).

### Q41

Coordinates are (2,1), reconstruction \(2(1,1)+(1,-1)=(3,1)\). Gram matrix \(2I\) gives squared norm 10. The raw dot products (4,2) must be divided by squared basis lengths 2. The number 5 is the unweighted coefficient-square sum; (3,1) is the standard-basis tuple, not the requested tuple.

### Q42

For first-argument conjugation, \(\langle u,v\rangle=i-i=0\) and \(\langle u,u\rangle=1+(-i)i=2\). Omitting conjugation gives the nonpositive-definite bilinear self-product \(1+i^2=0\), while the cross bilinear product is \(2i\). This distinguishes all four options. The first-argument-conjugate convention makes the second argument linear. Therefore the complex projection coefficient onto u is \(\langle u,w\rangle/\langle u,u\rangle\), not \(\langle w,u\rangle/\langle u,u\rangle\). The latter fails when \(w=iu\). Audit all general complex projection formulas in the lesson against the explicitly chosen convention.

### Q43

For nonzero \(x\in U^\perp\), \(Px=0\), so numerator and denominator are equal and the ratio is 1. For \(x=0\) the ratio is undefined. For general nonzero x the ratio lies in [0,1], is 0 on U, and is 1 on \(U^\perp\). A right-angle decomposition supports these endpoints without inventing a dependence on the plane's orientation.

### Q44

\(\det G=9\cdot16-12^2=0\). With \(\|u\|=3\), \(\|v\|=4\), Cauchy–Schwarz equality implies linear dependence; positive dot product means \(v=(4/3)u\). Sum squared norm is 49, while difference squared norm is 1. Had the dot product been -12, the vectors would point oppositely; had its absolute value exceeded 12, no such real Euclidean vectors would exist. Gram positivity is a feasibility test before any angle calculation.

### Q45

The same Gram matrix as Q37 has right-hand side (1,1), giving coefficients (1/3,1/3). Projection is (2/3,1/3,1/3), residual (-2/3,2/3,2/3). Squared norms are 2/3 and 4/3, summing to the original squared norm 2. The proposed (1,1,1) is not in the span; (0,1/2,1/2) and (1/2,1/2,1/2) are also not in the span because the span equation is first coordinate = second + third. This supplies direct option rejections instead of vague remarks.

### Q46

The feasible line is \((1-t,t,1-t)\). Completing the square gives \(3(t-2/3)^2+2/3\), hence the unique minimizing vector (1/3,2/3,1/3), squared norm 2/3. Its inner product with line direction (-1,1,-1) is zero; every feasible vector equals the minimizer plus a multiple of that direction, proving the same lower bound by Pythagoras. The row-space method \(C^T(CC^T)^{-1}(1,1)^T\), with \(C=\begin{pmatrix}1&1&0\\0&1&1\end{pmatrix}\), gives the identical point. Do not take a square root when the question asks squared norm.

## 5. Exact computational corroboration actually executed

SymPy independently computed the parameter projection/residual, basis coordinates, Q39 determinant, Q37 and Q45 Gram projections, Q46 constrained minimizer, and Q4 determinant/eigenvalue multiplicities. Results agree with the derivations above. Explicit trace-zero symmetric basis ranks were computed for sizes 1 through 8, giving 0, 2, 5, 9, 14, 20, 27 and 35. Coordinate-block subspace constructions at n=5 and n=8 gave intersection dimensions 5 and 8. Rectangular canonical maps at both values gave nullity 2 and transpose nullity 4. For the complex convention check with u=(1,i) and w=iu, SymPy returned the correct coefficient i and the wrong reversed coefficient -i. These symbolic checks cover the specified models; they do not establish universal chapter coverage or validate every conceivable future question. No browser, font, diagram layout, or course-content comparison was conducted by this independent subtask.

## 6. Question-specific visual recommendations

1. **Trace degrees of freedom (Q1, Q5–8):** draw the actual symmetric matrix; linked reflected off-diagonal cells share one parameter. Reveal the trace equation, then derive the last diagonal cell from the first ones. Show separate counters for off-diagonal coordinates, free diagonal coordinates, and rank-one restriction. This is not a three-dimensional geometric space despite the matrix's convenient grid representation.
2. **Sum/intersection (Q9–12):** for n=1 show two distinct planes in R3 with a shared line; for n=5,8 use dimension blocks showing common n, U-only n and V-only n. Mark that the higher-dimensional block drawing is a dimension ledger, not a literal R3 embedding.
3. **Rectangular map (Q13–16):** pair a concrete canonical block matrix with domain-column/range-row ledgers. Animate one free kernel coordinate without moving the image, then a pivot coordinate moving the image; switch to transpose and display why the nullity changes from 2 to 4. Preserve dimension labels.
4. **Projection/residual (Q17–24, Q43):** use 3D geometry or a clearly labeled orthogonal coordinate view with original vector, its foot on the line, residual, and right-angle marker. Parameter changes must update all actual coordinates and squared-norm values. A parallel translated line is not the projection subspace. Scale the direction vector separately to show its coefficient changes while the foot stays fixed.
5. **Metric orthogonality (Q25–28):** show cancellation of the two coordinate products alongside the actual planar vector pair. Switch to the weighted metric and update the required a, accompanied by a metric ellipse and an explicit warning that Euclidean visual right angles need not represent weighted orthogonality.
6. **Basis coordinates (Q29–32, Q41):** construct the vector head-to-tail using c1*b1 and c2*b2; display both standard and basis coordinates. Swap basis order without moving the endpoint. Show squared basis lengths 2 and the Gram-weighted norm rather than falsely treating the coefficient plane as an isometric copy.
7. **Homogeneous/affine hyperplanes (Q33–36, Q40):** for a three-coordinate representative move a sum-zero plane to a nonzero parallel plane. Mark the origin, the closest point and normal segment. In higher dimension, use an explicitly schematic dimension ledger rather than claim literal 3D geometry.
8. **Nonorthogonal span (Q37,Q45):** show both spanning arrows, their plane, w, foot and residual normal. Each checkpoint should calculate a Gram equation or its solution, then verify both zero residual dot products. Do not add two independent one-dimensional projections. View scale must retain the vector endpoint and the plane foot.
9. **Scaled plane normal (Q38):** show w, nearest point and shortest perpendicular segment. Scale the displayed normal arrow while keeping the plane and distance fixed. Label the coefficient and length separately.
10. **Parameter-dependent independence (Q39):** move the third vector to a coplanar position at a=-1 while plotting exact determinant -(a+1). At that checkpoint display the nonzero coefficient relation, not just a color change.
11. **Structured definiteness (Q4):** split the all-equal line and sum-zero plane into labeled invariant directions; plot their two quadratic coefficients as a varies. At the endpoints show which direction becomes null. For a>1, demonstrate why a positive determinant can coexist with negative directions.
12. **Complex conjugation (Q42):** use a real/imaginary component ledger and explicit conjugation, i→-i, so the i and -i cross terms cancel and (-i)i becomes +1. A generic real vector projection picture would be misleading.
13. **Gram degeneracy (Q44):** draw collinear arrows of lengths 3 and 4 in the same direction, then the sum length 7. Show the Gram determinant zero and the ratio 4/3. A feasible dot-product control must stay within [-12,12] or explicitly enter an impossible-data state.
14. **Affine minimum norm (Q46):** draw the feasible line and shortest origin-to-line segment ending at the minimizer; show the exact convex parabola in t alongside it. Stepping t changes both the feasible point and the excess squared norm, with the minimum checkpoint fixed at t=2/3.

## 7. Limits and handoff

All existing 46 placements were read and their stated calculations independently checked. The identified source ambiguity in Q3 and authored wording ambiguity in Q12 require action before clean delivery. Complex projection convention must be reconciled across the full lesson. This subtask does not constitute full course synthesis, final lesson review, simulation verification, source publication, or a guarantee of performance on unseen examinations.
