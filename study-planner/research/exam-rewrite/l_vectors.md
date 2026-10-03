## Teaching through formulas and conceptual decisions

### Turn geometric language into an optimization equation

For a nonzero direction$u$, minimize $\|v-tu\|^2$. Expanding gives $\|v\|^2-2t\langle u,v\rangle+t^2\|u\|^2$ over the reals. Completing the square yields the unique minimizing coefficient $t=\langle u,v\rangle/\langle u,u\rangle$. The projection vector is$tu$, its length is$|t|\|u\|$, and the distance is the norm of$v-tu$. These are three different requested quantities. The residual is orthogonal to$u$, supplying an independent computational check.

For a line$p+tu$, first replace$v$ by$v-p$, project that displacement, and add$p$ back. For a plane $a\cdot x=b$ with nonzero normal$a$, the distance from$p$ is $|a\cdot p-b|/\|a\|$. Normalizing an offset plane equation incorrectly can move the plane: scale both sides together.

### Independence and coordinates are linear systems

To decide whether$v_1,\ldots,v_k$ are independent, solve $c_1v_1+\cdots+c_kv_k=0$. One nonzero coefficient solution proves dependence. A zero vector always creates dependence, but nonzero vectors can also be dependent. If a family is a basis, expressing a target vector in that family is solving the corresponding system for its coordinate coefficients; these coefficients need not equal the standard coordinates.

### Change the inner product before applying a Euclidean shortcut

With positive definite diagonal weights$w_i$, use $\langle u,v\rangle_W=\sum_iw_iu_iv_i$ in both projection numerator and denominator. Complex inner products require conjugation; here $\langle u,v\rangle=\sum\overline{u_i}v_i$ is linear in the second argument. The sum of complex squares without conjugates can vanish for a nonzero vector and is not a norm.

In Gram–Schmidt, subtract projections onto previous orthogonal directions and only then normalize the residual. A zero residual records dependence and cannot be divided by its norm. The cross product measures oriented area only in three-dimensional real coordinates; its norm gives parallelogram area and half that gives triangle area.

## Formula and conceptual problem bank

### Question 1. Projection coefficient and vector

For $v=(3,1)$ and $u=(1,2)$, what is the orthogonal projection of$v$ onto the line spanned by$u$?

**A.** $(1,2)$

**B.** $(5,10)$

**C.** $(2,-1)$

**D.** $(3,1)$

**Answer: A.**

The dot product is5 and $u\cdot u=5$, so the coefficient is1. Multiplying by$u$ yields$(1,2)$. The residual$(2,-1)$ has dot product0 with$u$, verifying the calculation. ChoiceB omits division by the squared norm; C is the residual rather than the projection; D would require$v$ already to be parallel to$u$.

### Question 2. Projection distance

Use the vectors in Question 1. What is the distance from$v$ to the line?

**A.** $1$

**B.** $\sqrt5$

**C.** $5$

**D.** $\sqrt{10}$

**Answer: B.**

The residual is$(2,-1)$, whose squared norm is$4+1=5$. The distance is therefore$\sqrt5$. The coefficient1 is not the distance. The scalar5 is the squared distance, and$\sqrt{10}$ is the norm of$v$ rather than its perpendicular component.

### Question 3. Affine line

Find the closest point to$q=(4,3)$ on the line$p+t u$, where$p=(1,1)$ and$u=(1,0)$.

**A.** $(4,0)$

**B.** $(3,1)$

**C.** $(4,1)$

**D.** $(1,3)$

**Answer: C.**

Translate to$q-p=(3,2)$, whose projection on$u$ is$(3,0)$. Add the base point to get$(4,1)$. The displacement from that point to$q$ is vertical and orthogonal to$u$. Projecting$q$ directly onto the direction space gives$(4,0)$, which lies on a different line.

### Question 4. Plane distance

What is the distance from$p=(1,2,3)$ to the plane$x+2y+2z=5$?

**A.** 1

**B.** 2

**C.** 3

**D.** 6

**Answer: B.**

The normal is$(1,2,2)$ with norm3. The plane expression at$p$ is$1+4+6=11$, so the signed discrepancy is6. Divide its absolute value by3 to obtain2. Six is not a distance unless the normal has unit norm. Scaling the entire plane equation leaves the quotient unchanged.

### Question 5. Parameter-dependent independence

The vectors $(1,t)$ and$(2,4)$ in$\mathbb R^2$ are dependent for which real$t$?

**A.** 0

**B.** 1

**C.** 2

**D.** 4

**Answer: C.**

If the second vector is twice the first, its second coordinate must satisfy$4=2t$, giving$t=2$. Conversely at2 that exact multiple relation proves dependence. The determinant$4-2t$ is a second check. Neither zero$t$ nor equal displayed coordinates by themselves establish dependence.

### Question 6. Coordinates in a chosen basis

Let$b_1=(1,1)$ and$b_2=(1,-1)$. What are the coordinates of$v=(4,2)$ in this ordered basis?

**A.** $(4,2)$

**B.** $(3,1)$

**C.** $(1,3)$

**D.** $(2,4)$

**Answer: B.**

Solve$c_1+c_2=4$ and$c_1-c_2=2$. Adding gives$c_1=3$, and then$c_2=1$. Indeed $3(1,1)+(1,-1)=(4,2)$. Reversing the basis order would reverse these coordinates, but that is not the stated ordered basis. The standard components are not automatically basis coefficients.

### Question 7. Weighted geometry

Use inner product $\langle x,y\rangle=x_1y_1+4x_2y_2$. For$v=(2,1)$ and$u=(1,1)$, what is the projection coefficient$t$?

**A.** 3/2

**B.** 6/5

**C.** 3/5

**D.** 1

**Answer: B.**

The weighted numerator is$2+4=6$ and the weighted denominator is$1+4=5$. Thus$t=6/5$. The Euclidean coefficient3/2 uses the wrong geometry. With this coefficient, the weighted inner product of$u$ with$v-tu$ is zero, checking the minimizer. The same metric must be used in numerator and denominator.

### Question 8. Complex norm

Under the standard Hermitian inner product, what is $\|(1,i)\|^2$?

**A.** 0

**B.** 1

**C.** 2

**D.** $1+i$

**Answer: C.**

Conjugation gives $|1|^2+|i|^2=1+1=2$. Adding ordinary squares would give$1+i^2=0$, incorrectly assigning zero squared norm to a nonzero vector. A squared norm is real and nonnegative. The conjugate factor is necessary, not a stylistic convention.

### Question 9. Gram–Schmidt residual

With$v_1=(1,1,0)$ and$v_2=(1,0,1)$, what residual results after removing the projection of$v_2$ on$v_1$?

**A.** $(0,-1,1)$

**B.** $(1/2,-1/2,1)$

**C.** $(1,1,0)$

**D.** $(1/2,1/2,0)$

**Answer: B.**

The projection coefficient is $(v_1\cdot v_2)/(v_1\cdot v_1)=1/2$. Subtract$(1/2,1/2,0)$ from$v_2$ to obtain$(1/2,-1/2,1)$. Its dot product with$v_1$ is zero. OptionD is the removed projection. Normalizing this residual is a subsequent step, not part of merely computing it.

### Question 10. Cauchy–Schwarz equality

For nonzero real vectors$u,v$, when does $|u\cdot v|=\|u\|\|v\|$ hold?

**A.** Exactly when they are perpendicular.

**B.** Exactly when one is a scalar multiple of the other.

**C.** Exactly when their lengths are equal.

**D.** Always in two dimensions.

**Answer: B.**

Equality occurs precisely when the perpendicular residual in the projection proof has zero norm. That means$v$ lies in the span of$u$, so$v=tu$ for some real$t$. Negative$t$ is allowed because the dot product is inside an absolute value. Equal lengths alone do not force parallel directions.

### Question 11. Triangle area

What is the area of the triangle generated from the origin by$u=(1,0,0)$ and$v=(0,3,0)$?

**A.** 1

**B.** 3/2

**C.** 3

**D.** 6

**Answer: B.**

The cross product is$(0,0,3)$, whose norm3 is the parallelogram area. A triangle is half that region, so its area is3/2. OptionC omits the half factor. The norm-product shortcut works here because the directions are perpendicular, but in general a sine factor is required.

### Question 12. Scalar triple product

For$u=(1,0,0)$,$v=(0,2,0)$,$w=(0,0,-3)$, what is the volume of the parallelepiped?

**A.** -6

**B.** 3

**C.** 6

**D.** 12

**Answer: C.**

$v\times w=(-6,0,0)$ and $u\cdot(v\times w)=-6$. The signed triple product records orientation; volume is its absolute value6. A negative signed value is not a negative geometric volume. Reversing two vectors changes the sign but leaves the requested volume unchanged.

<!-- CHALLENGE-BANK -->

### Question 13. Challenge: Projection onto a nonorthogonal span

Let$u=(1,1,0)$,$w=(1,0,1)$ and$v=(0,1,1)$. What is the Euclidean projection of$v$ onto$\operatorname{span}(u,w)$?

**A.** $(1,1,1)$

**B.** $(2/3,1/3,1/3)$

**C.** $(0,1/2,1/2)$

**D.** $(1/2,1/2,1/2)$

**Answer: B.**

Write the projection$cu+dw$ and impose residual orthogonality to both directions. Dot products give$2c+d=1$ and$c+2d=1$, hence$c=d=1/3$. The projection is$(2/3,1/3,1/3)$. Its residual$(-2/3,2/3,2/3)$ is orthogonal to both$u,w$. Adding separate one-direction projections fails because the directions are not orthogonal; the Gram system accounts for their interaction.

### Question 14. Challenge: Minimum norm on an affine intersection

Among real$(x,y,z)$ satisfying$x+y=1$ and$y+z=1$, what is the minimum squared Euclidean norm?

**A.** 1/3

**B.** 2/3

**C.** 1

**D.** 2

**Answer: B.**

The constraints give$x=z=1-y$. Squared norm is$2(1-y)^2+y^2=3(y-2/3)^2+2/3$. It is minimized uniquely at$y=2/3$, giving$x=z=1/3$ and squared norm2/3. Completing the square proves global optimality without an unproved critical-point argument. The requested quantity is squared norm, so taking an additional square root would answer a different question.

## Applicable formulas and examination notes

### 1. Projection versus residual

$\operatorname{proj}_u v=(\langle u,v\rangle/\langle u,u\rangle)u$ for nonzero$u$. For$(3,1)$ onto$(1,2)$, projection is$(1,2)$ and residual is$(2,-1)$. Check their orthogonality; do not return the scalar coefficient when the vector is requested.

### 2. Distance formula

Distance to the span of$u$ is $\sqrt{\|v\|^2-|\langle u,v\rangle|^2/\|u\|^2}$. The root is required for distance, not squared distance. A slightly negative value from rounding needs a numerical error analysis, not a new geometric interpretation.

### 3. Affine translation

For line$p+tu$, project$q-p$ and add$p$. Projecting$q$ directly solves the origin-line problem. For a plane normal$a$, use $|a\cdot q-b|/\|a\|$ and require$a\ne0$.

### 4. Independence

Solve the homogeneous coefficient equation; dependence means some nonzero coefficient tuple yields zero. With$(1,t),(2,4)$, the condition is$t=2$. More than$d$ vectors in a$d$-dimensional space cannot be independent.

### 5. Basis coordinates

Coordinates are coefficients relative to an ordered basis. Solve the column system rather than reusing standard entries. In basis$(1,1),(1,-1)$, vector$(4,2)$ has coefficients$(3,1)$. Reordering the basis reorders the coefficients.

### 6. Span versus affine combinations

A linear span allows arbitrary coefficients; an affine combination requires their sum to be1. An affine line need not contain zero. A subset closed under differences need not be a subspace unless it also has the required scalar and origin properties.

### 7. Metric consistency

Weighted projection uses the same positive definite inner product in numerator and denominator. For weights1,4, vectors$(2,1),(1,1)$ give coefficient6/5. Zero or negative weights can destroy the norm properties used by the projection proof.

### 8. Complex conjugation

With the convention conjugate-linear in the first argument, use $\langle u,v\rangle=\sum\overline{u_i}v_i$. Vector$(1,i)$ has squared norm2, not0. State the convention before computing coefficients or adjoints.

### 9. Gram–Schmidt order

Subtract all earlier orthogonal components before normalization. A zero residual detects dependence and cannot be normalized. Orthogonality alone implies independence only when every listed vector is nonzero.

### 10. Angle conditions

For nonzero real vectors, $\cos\theta=(u\cdot v)/(\|u\|\|v\|)$. A zero vector has no direction angle under this formula. The absolute-value equality in Cauchy–Schwarz permits both parallel and antiparallel vectors.

### 11. Area and orientation

In$\mathbb R^3$, parallelogram area is$\|u\times v\|$ and triangle area is half that. Reversing factors negates the cross product but preserves area. The cross product is not the general inner-product projection operator.

### 12. Volume and coplanarity

Volume is $|u\cdot(v\times w)|$. A zero triple product detects linear dependence of three real3D vectors, including degenerate zero-vector cases. The signed value distinguishes orientation and must not be reported as a negative volume.

<!-- BOUNDARY-NOTES -->

### 13. Orthogonal complement dimensions

In a finite-dimensional inner-product space of dimension $d$, a $k$-dimensional subspace has orthogonal complement dimension $d-k$. Only the zero vector lies in both. This formula applies to the span's dimension, not automatically to the number of possibly dependent listed vectors.

### 14. Pythagorean scope

For orthogonal vectors, squared norms add. Triangle and reverse-triangle inequalities hold in any normed space, but the dot-product projection and Pythagorean identities require inner-product geometry. Do not treat every norm as Euclidean without a stated metric.

### 15. Polynomial vector geometry

Polynomials form a vector space under coefficient-wise addition, and an integral inner product can supply different geometry from their coefficient dot product. Compute the specified integral or weighted rule before deciding orthogonality. Sampling at too few points can give a zero measurement to a nonzero polynomial and fail positive definiteness.
