# Orthogonality and Orthogonal Decompositions

## 1. Sources, prerequisites, notation and learning route

The core synthesis uses **Oxford M1 Linear Algebra I** (lecturer Andrew Wathen), **MIT18.06SC** (Gilbert Strang), **Berkeley Math54** (Alexander Paulin), and **ETH Zurich Linear Algebra for Computer Scientists PartII** (Afonso S. Bandeira and Robert Weismantel). Stanford EE263, CMU21-241 and Harvard Math55a were compared as additional written sources. Exact documents, page ranges, selection reasons and corrections are in the [source audit](../reviews/l_orthogonality-sources.html). Exercises are reconstructed with independent solutions; no complete copyrighted assignment collection is reproduced.

You need span, independence, rank–nullity, basis coordinates and matrix multiplication. Declare the field and inner product before computing. We mainly work in finite-dimensional real spaces. The complex extension uses **conjugate linearity in the first argument** and linearity in the second:

$$
\langle x,y\rangle_G=x^*Gy,\qquad x^*=\overline{x}^{\,T}.
$$

Here $G$ is Hermitian positive definite; the standard case is $G=I$. On real spaces conjugations disappear. A generator matrix has generators as **columns**. An orthonormal column matrix $Q\in\mathbb F^{m\times r}$ need not be square. We distinguish $P$ (a projector), $G$ (a metric), and $R$ (an upper triangular factor). Animations distinguish exact algebraic checkpoints from illustrative movement. A planar drawing does not replace a proof in arbitrary dimension.

## 2. What an inner product adds to a vector space

Vector-space axioms alone define neither length nor perpendicularity. An inner product adds these through additivity, the declared scalar convention, conjugate symmetry and strict positivity:

$$
\langle x,y\rangle=\overline{\langle y,x\rangle},
\qquad \langle x,x\rangle>0\quad(x\ne0).
$$

The induced norm and distance are

$$
\|x\|=\sqrt{\langle x,x\rangle},\qquad d(x,y)=\|x-y\|.
$$

The square root is essential: the self-product scales by $|\alpha|^2$, whereas length scales by $|\alpha|$. Positivity means that a vector orthogonal to itself is zero. With the indefinite form $G=\operatorname{diag}(1,-1)$, the nonzero vector $(1,1)^T$ has self-product zero. Such a form is not an inner product; our norm and minimization proofs cannot be transferred to it.

For $G=\operatorname{diag}(1,4)$, vectors $(1,1)^T$ and $(4,-1)^T$ are perpendicular in the weighted metric, although their ordinary dot product is three. Orthogonality belongs to the chosen metric, not merely to the coordinate labels.

<!-- SIM: metric -->

## 3. Gram matrices and positive definiteness

For a basis $(b_1,\ldots,b_n)$ define $G_{ij}=\langle b_i,b_j\rangle$. Expanding both arguments gives

$$
\left\langle\sum_i x_i b_i,\sum_j y_j b_j\right\rangle=x^*Gy.
$$

A real inner product has a symmetric positive definite Gram matrix; a complex one has a Hermitian positive definite Gram matrix. Conversely such a matrix defines an inner product. Symmetry alone is insufficient: $\operatorname{diag}(1,0)$ gives zero length to a nonzero vector. In dimension two, completing the square gives

$$
G=\begin{pmatrix}a&b\\b&c\end{pmatrix},
\quad x^TGx=a\left(x_1+\frac ba x_2\right)^2+
\left(c-\frac{b^2}{a}\right)x_2^2.
$$

Thus $G$ is positive definite exactly when $a>0$ and $ac-b^2>0$. For any generator matrix $A$,

$$
z^*A^*Az=\|Az\|^2,\qquad \ker(A^*A)=\ker A.
$$

The kernel equality follows in both directions by multiplying or by strict positivity. Therefore $\operatorname{rank}(A^*A)=\operatorname{rank}A$, and $A^*A$ is invertible exactly when the columns are independent.

## 4. Cauchy–Schwarz, equality and angles

For $y\ne0$, subtract the component along $y$:

$$
r=x-y\frac{\langle y,x\rangle}{\langle y,y\rangle}.
$$

The residual satisfies $\langle y,r\rangle=0$. Expansion yields

$$
0\le\|r\|^2=\|x\|^2-\frac{|\langle y,x\rangle|^2}{\|y\|^2}.
$$

Hence $|\langle y,x\rangle|\le\|y\|\|x\|$, with equality precisely when $r=0$, meaning linear dependence. If $y=0$, the inequality is immediate and equality holds. In real space the unsigned angle between **nonzero** vectors is

$$
\theta=\arccos\!\left(\frac{\langle x,y\rangle}{\|x\|\|y\|}\right),
\qquad 0\le\theta\le\pi.
$$

Cauchy–Schwarz makes the arccosine input admissible. Orthogonality gives $\theta=\pi/2$, never a negative unsigned angle. A zero vector has no defined angle. A complex product may be nonreal, so this real arccosine formula cannot be used unchanged.

## 5. Pythagoras, triangle inequality and polarization

For real vectors,

$$
\|x+y\|^2=\|x\|^2+2\langle x,y\rangle+\|y\|^2.
$$

Perpendicularity removes the middle term. Bounding it by $2\|x\|\|y\|$ and taking nonnegative square roots proves the triangle inequality. Equality requires vectors in the same nonnegative direction, including zero; arbitrary dependence is insufficient because opposite vectors cancel.

In real space the Pythagorean equality also implies perpendicularity. In complex space it forces only $\operatorname{Re}\langle x,y\rangle=0$. The imaginary part can remain nonzero. Real products can be reconstructed from lengths:

$$
\langle x,y\rangle=\frac{\|x+y\|^2-\|x-y\|^2}{4}.
$$

Consequently a real **linear** norm-preserving map preserves products. A translation preserves distances but need not preserve norms measured from the origin.

## 6. Orthogonal sets and coefficient extraction

A pairwise orthogonal list is independent if every vector is nonzero. Indeed, from $\sum c_i u_i=0$ one gets

$$
0=\left\langle u_j,\sum_i c_i u_i\right\rangle=c_j\|u_j\|^2.
$$

Strict positivity forces every coefficient to vanish. Dividing each nonzero vector by its norm produces an orthonormal list. For a vector in its span,

$$
x=\sum_j c_j u_j,\qquad
c_j=\frac{\langle u_j,x\rangle}{\|u_j\|^2}.
$$

The denominator disappears only for unit vectors. Under the opposite complex convention, argument order must be changed consistently. For a nonorthogonal basis, coefficients are coupled by a Gram system rather than obtained by independent division.

For example, $(3,-1)^T$ and $(1,3)^T$ are perpendicular and have squared norm ten. The coefficients of $(1,2)^T$ are $1/10$ and $7/10$. Multiplying by the corresponding basis vectors reconstructs $(1,2)^T$. These are coefficients in an unnormalized basis, not coefficients in its normalized version.

## 7. Orthogonal complements and a unique decomposition

Define

$$
W^\perp=\{x\in V:\langle w,x\rangle=0\text{ for every }w\in W\}.
$$

Linearity in the second argument proves that this is a subspace. Testing a spanning list suffices because perpendicularity extends to every linear combination. Also $W\cap W^\perp=\{0\}$, because a common vector is perpendicular to itself.

In finite dimension extend an orthonormal basis of $W$ to one of $V$, then split each vector's expansion into the two basis groups. This proves

$$
V=W\oplus W^\perp,\quad
\dim W^\perp=\dim V-\dim W,\quad
(W^\perp)^\perp=W.
$$

Uniqueness follows from the zero intersection. A chosen algebraic complement need not be perpendicular. Empty intersections are impossible: every subspace contains zero. For arbitrary infinite-dimensional subspaces, the decomposition theorem needs additional completeness/closedness hypotheses and is not inferred from the finite proof.

## 8. Four fundamental subspaces and consistency

For $A\in\mathbb R^{m\times n}$, row space and nullspace live in $\mathbb R^n$; column space and left nullspace live in $\mathbb R^m$. The equation $Ax=0$ tests perpendicularity to every row, so

$$
\operatorname{Row}(A)^\perp=\ker A,\qquad
\operatorname{Col}(A)^\perp=\ker A^T.
$$

Their dimensions are $r,n-r,r,m-r$, where $r=\operatorname{rank}A$. Equal row and column ranks do not give equality of all four dimensions. In complex space use conjugate transpose and identify the row-side subspace with $\operatorname{Col}(A^*)$.

The system $Ax=b$ is consistent exactly when $b$ is perpendicular to every vector in $\ker A^*$. A left-null vector with nonzero product against $b$ certifies inconsistency. This explains why the least-squares residual belongs to the left nullspace.

## 9. Projection onto a line

For $u\ne0$, seek $p=cu$ whose residual is perpendicular to the line. The equation $\langle u,x-cu\rangle=0$ gives

$$
p=u\frac{\langle u,x\rangle}{\langle u,u\rangle},
\qquad r=x-p,\qquad\langle u,r\rangle=0.
$$

In Euclidean real coordinates, $P_u=uu^T/(u^Tu)$. Rescaling $u$ by any nonzero scalar leaves the projector unchanged. A zero generator describes the zero subspace, whose projector is zero; the division formula itself is undefined.

With $u=(2,1)^T$ and $x=(1,3)^T$, the coefficient is one, $p=(2,1)^T$, $r=(-1,2)^T$ and the squared distance is five. The product $u^Tr=0$ is a separate check rather than a visual guess.

<!-- SIM: line -->

## 10. Projection onto a subspace and the closest-point proof

For an orthonormal basis $q_1,\ldots,q_r$ of $W$, set

$$
P_Wx=\sum_{j=1}^r q_j\langle q_j,x\rangle.
$$

The result belongs to $W$, and its residual is perpendicular to each basis vector. It therefore realizes the unique perpendicular decomposition, proving independence of the selected orthonormal basis.

For any $w\in W$,

$$
\|x-w\|^2=\|x-P_Wx\|^2+\|P_Wx-w\|^2.
$$

The two difference vectors are perpendicular. The unique closest point is consequently $P_Wx$, and equality in the minimum occurs only for that point. The same proof establishes $\|P_Wx\|\le\|x\|$, with equality precisely for $x\in W$.

## 11. Projector matrices and the oblique distinction

Let $Q$ contain an orthonormal column basis. Then $P=QQ^*$ and

$$
P^2=P,\quad P^*=P,\quad
\operatorname{im}P=W,\quad\ker P=W^\perp.
$$

All positive powers equal $P$. The complement $I-P$ swaps image and kernel, and $P(I-P)=0$. A Euclidean real matrix is an orthogonal projector **if and only if** it is symmetric and idempotent. For the converse, idempotence splits $x=Px+(I-P)x$, while symmetry makes the terms perpendicular.

Idempotence alone gives an oblique projection. For

$$
P=\begin{pmatrix}1&2\\0&0\end{pmatrix},
$$

the vertical unit vector maps to $(2,0)^T$, increasing length. The kernel is $\operatorname{span}\{(-2,1)^T\}$, which is not perpendicular to the horizontal image. The geometric distinction changes norm and minimum-distance conclusions.

<!-- SIM: oblique -->

## 12. General basis formula and dependent generators

For independent columns of $A\in\mathbb F^{m\times r}$, write $p=Ac$. Perpendicularity gives

$$
A^*(x-Ac)=0,\quad
c=(A^*A)^{-1}A^*x,\quad
P=A(A^*A)^{-1}A^*.
$$

The inverse is valid by the Gram-kernel theorem. The final matrix is $m$ by $m$. Dependent columns make the Gram matrix singular; choose a column basis $B$ instead. This changes coefficient bookkeeping but leaves the physical subspace and projector unchanged.

Coefficients may be nonunique even though the projected vector is unique. For $A=(u,2u)$, every pair satisfying $c_1+2c_2=\alpha$ gives $p=\alpha u$. A pseudoinverse selects a particular coefficient representative; it is not needed to define the unique projection.

## 13. A complete plane projection with two checks

Let $W$ be the plane normal to $n=(1,1,-1)^T$. The vector $(1,2,3)^T$ already belongs to it. For $y=(1,2,4)^T$, one has $n^Ty=-1$, hence

$$
P_Wy=y-\frac{n^Ty}{n^Tn}n
=\begin{pmatrix}4/3\\7/3\\11/3\end{pmatrix}.
$$

First check: $n^TP_Wy=0$. Second check: the residual is $-n/3$ and is normal to the plane. Its squared norm is $1/3$. The independent matrix expression $P_W=I-nn^T/3$ gives the same result. These checks catch sign errors and confusion between arbitrary complements and perpendicular ones.

## 14. Bessel, Parseval and partial expansions

For an orthonormal list spanning $W$,

$$
\|x\|^2=\sum_{j=1}^r|\langle q_j,x\rangle|^2+\|x-P_Wx\|^2.
$$

Dropping the nonnegative residual proves Bessel's inequality, with equality exactly for $x\in W$. A basis of the entire space makes the residual always zero and gives Parseval's identity. A partial list therefore gives an inequality, not an automatic identity.

If $\|x\|^2=14$ and two orthonormal coefficients are two and minus one, the squared distance to their span is $14-4-1=9$. The projected vector has squared norm five; the original vector need not have that norm.

## 15. Gram–Schmidt and its ordered-span invariant

For independent ordered inputs, set $v_1=a_1$ and recursively compute

$$
v_k=a_k-\sum_{j<k}v_j\frac{\langle v_j,a_k\rangle}{\|v_j\|^2},
\qquad q_k=\frac{v_k}{\|v_k\|}.
$$

Assume earlier outputs are mutually perpendicular and span the same input prefixes. Taking the product with $v_i$ cancels exactly the $i$th projection term. A zero residual would place $a_k$ in the preceding input span, contradicting independence. The difference $a_k-v_k$ lies in that span, so both enlarged prefixes agree. This completes the induction; normalization preserves both span and perpendicularity.

The result depends on input order and sign/phase choices, whereas the final subspace projector does not. A dependent list can be processed by skipping exact zero residuals; dividing by them is invalid. A floating-point zero test needs a scale-aware tolerance and is a numerical judgment.

<!-- SIM: gram -->

## 16. A full three-column orthogonalization

Take $a_1=(1,1,0)^T$, $a_2=(1,0,1)^T$ and $a_3=(0,1,1)^T$. The first squared norm is two. The second projection coefficient is $1/2$, giving $v_2=(1/2,-1/2,1)^T$ with squared norm $3/2$. The third coefficients against $v_1$ and $v_2$ are $1/2$ and $1/3$, so

$$
v_3=(-2/3,2/3,2/3)^T,\qquad \|v_3\|^2=4/3.
$$

Normalize to obtain

$$
q_1=\frac{(1,1,0)^T}{\sqrt2},\quad
q_2=\frac{(1,-1,2)^T}{\sqrt6},\quad
q_3=\frac{(-1,1,1)^T}{\sqrt3}.
$$

Check all three cross-products and all three lengths. Unit lengths alone do not give orthonormality, and neither does independence alone.

## 17. Reduced QR, rectangular dimensions and uniqueness

Set $Q=(q_1,\ldots,q_r)$ and $R=Q^*A$. Prefix-span preservation gives $R_{ij}=0$ for $i>j$, and normalization gives $R_{jj}=\|v_j\|>0$. Therefore

$$
A=QR,\quad Q^*Q=I_r,\quad
Q\in\mathbb F^{m\times r},\quad R\in\mathbb F^{r\times r}.
$$

This reduced QR does not make rectangular $Q$ invertible. For uniqueness with positive real diagonal, suppose $QR=\widetilde Q\widetilde R$. The matrix $U=Q^*\widetilde Q=R\widetilde R^{-1}$ is unitary and upper triangular. Column orthogonality successively forces it to be diagonal; its positive diagonal entries must all be one. Both factors consequently agree. Without the sign condition, signs or complex phases can move between factors.

Dependent input produces a singular triangular factor. A rank-revealing decomposition then requires separate choices.

<!-- SIM: qr -->

## 18. Least squares is projection plus coefficient recovery

Minimizing $\|b-Ac\|$ finds the closest point in $\operatorname{Col}(A)$. Independent columns give a unique coefficient vector; dependent columns give a unique physical minimizer but potentially many coefficients. The residual always satisfies $A^*(b-Ac)=0$.

For independent columns and $A=QR$, the normal equations simplify to

$$
Rc=Q^*b,\qquad
\|b-Ac\|^2=\|b\|^2-\|Q^*b\|^2.
$$

Use back substitution rather than an explicit inverse. The norm identity independently checks an exact examination calculation. In floating-point work forming $A^*A$ worsens conditioning; QR avoids that formation. Detailed numerical stability and SVD theory belong to later chapters.

## 19. Weighted projection

With $\langle x,y\rangle_G=x^*Gy$, residual perpendicularity is $A^*G(x-Ac)=0$. Hence

$$
P_G=A(A^*GA)^{-1}A^*G,\qquad
P_G^2=P_G,\qquad P_G^*G=GP_G.
$$

The projector need not be ordinarily symmetric. For $G=\operatorname{diag}(1,4)$ and line generator $(1,1)^T$,

$$
P_G=\frac15\begin{pmatrix}1&4\\1&4\end{pmatrix}.
$$

Applied to $(2,0)^T$ it gives $(2/5,2/5)^T$. The residual $(8/5,-2/5)^T$ has zero weighted product with the generator. Euclidean perpendicularity and Euclidean minimum distance do not follow; the minimization is in the weighted norm.

<!-- SIM: weighted -->

## 20. A skewed basis transports the metric

Under physical synthesis $x=Sc$, coefficient products use $G_{\rm new}=S^*GS$. This is congruence, while an operator representation changes by similarity $P_{\rm new}=S^{-1}PS$. Self-adjointness becomes

$$
P_{\rm new}^*G_{\rm new}=G_{\rm new}P_{\rm new}.
$$

For $S=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ and physical horizontal projection, the coefficient projector is $\begin{pmatrix}1&1\\0&0\end{pmatrix}$, while the Gram matrix is $\begin{pmatrix}1&1\\1&2\end{pmatrix}$. The representation remains orthogonal in the transported metric despite its ordinary nonsymmetry. A coordinate matrix cannot be classified geometrically without its basis metric.

## 21. Function products and polynomial parity

On continuous real functions on $[a,b]$, $a<b$, define $\langle f,g\rangle=\int_a^b fg$. A continuous nonzero function is bounded away from zero on a small interval, so its squared integral is positive. Arbitrary pointwise functions lack that property: changing one point leaves an integral unchanged. In $L^2$, functions equal almost everywhere are identified.

On $[-1,1]$, odd functions are perpendicular to even ones. In basis $(1,t,t^2)$ the Gram matrix is

$$
G=\begin{pmatrix}2&0&2/3\\0&2/3&0\\2/3&0&2/5\end{pmatrix}.
$$

Monomials are independent but not orthogonal. Orthogonalization gives $1,t,t^2-1/3$ with squared norms $2,2/3,8/45$. The odd polynomial $t^3$ projects to zero onto the even span of $1,t^2$: both numerator integrals vanish. Onto the different span of $1,t$, its projection is $(3/5)t$ and its squared error is $8/175$. The choice of subspace is decisive.

<!-- SIM: polynomial -->

## 22. Finite Fourier expansions and sampled products

On $[-\pi,\pi]$, $\|1\|^2=2\pi$ and $\|\cos kt\|^2=\|\sin kt\|^2=\pi$ for positive integer $k$. Distinct positive frequencies are perpendicular. Negative cosine frequencies repeat positive ones, and the zero sine is not a nonzero basis vector.

A finite trigonometric projection uses a finite coefficient sum. No exchange of an infinite sum and integral is required. Infinite Fourier convergence needs additional hypotheses and does not follow from finite orthogonality.

A sampled product $\sum_j w_jp(t_j)q(t_j)$ is positive definite on degree-at-most-$d$ polynomials when there are at least $d+1$ distinct real nodes with strictly positive weights. A nonzero polynomial cannot vanish at that many distinct points. Too few distinct nodes permit a nonzero vanishing polynomial and produce a semidefinite form.

## 23. Orthogonal matrices and Householder reflection

A square real matrix is orthogonal if $Q^TQ=I$, so $Q^{-1}=Q^T$. Complex unitary matrices use conjugate transpose. A rectangular orthonormal-column matrix is an isometric embedding but lacks a two-sided inverse.

For nonzero real $v$,

$$
H=I-2\frac{vv^T}{v^Tv}
$$

fixes $v^\perp$ and sends $v$ to $-v$. It is symmetric and satisfies $H^2=I$, hence is orthogonal with determinant minus one. The complementary projector $I-vv^T/(v^Tv)$ has normal eigenvalue zero rather than minus one; it is not reflection.

To reflect $x$ onto a different equal-length target $y$, take $v=x-y$. Equal squared lengths imply $2v^Tx=v^Tv$, so $Hx=x-v=y$. For $x=y$ the generator is zero; use identity rather than divide by zero.

<!-- SIM: reflection -->

## 24. Products, nested subspaces and alternating projections

Two orthogonal projectors have an orthogonal-projector product exactly when they commute. If $PQ=QP$, then $(PQ)^2=PQ$ and $(PQ)^*=PQ$, with image equal to the intersection. Conversely symmetry of $PQ$ implies $PQ=QP$.

For $U\subseteq W$, $P_UP_W=P_WP_U=P_U$, and $P_W-P_U$ projects onto $W\cap U^\perp$. For perpendicular subspaces, $P_UP_W=0$ and their projector sum gives projection onto the direct sum. General products and sums do not satisfy these conclusions.

For two real lines at angle $\theta$, $\operatorname{tr}(P_UP_W)=\cos^2\theta$. Repeated alternating projection can converge toward the intersection while a single product is not its orthogonal projector. The bank derives the exact planar contraction rather than extrapolating a drawing.

Matrix spaces also have perpendicular decompositions. For real matrices use the Frobenius product $\langle X,Y\rangle_F=\operatorname{tr}(X^TY)$. Symmetric and skew-symmetric parts are perpendicular: pairing a diagonal term with a skew part gives zero, while off-diagonal terms cancel in pairs. Thus $X=(X+X^T)/2+(X-X^T)/2$ is an orthogonal splitting. Inside symmetric $n$-by-$n$ matrices, trace is the product with $I$; the perpendicular projection onto trace-zero matrices is $X-\operatorname{tr}(X)I/n$. One scalar normal direction is removed from dimension $n(n+1)/2$. This supplies the orthogonal interpretation of the authentic dimension revisit.

## 25. Implementation, numerical boundaries and a verification workflow

Hand calculations often stay simpler with unnormalized perpendicular vectors until the last step. The editable laboratory uses exact rational Gram systems and checks perpendicular residuals, projector identities and squared distances.

Modified Gram–Schmidt updates the current residual after each subtraction:

~~~text
Q = empty list
for each input column a:
    v = a
    for each accepted unit column q:
        v = v - q * inner(q, v)
    if v has exact norm zero:
        record a dependency and continue
    append v / norm(v) to Q
~~~

Classical Gram–Schmidt computes the projection coefficients against the original current input column. In exact arithmetic both agree; rounding can make them differ. Reorthogonalization can help. Householder QR uses norm-preserving transformations. A stable algorithm does not make an ill-conditioned problem well-conditioned.

Verify the field, conjugations, metric, nonzero denominators, independence before inversion, dimensions and original basis. For projection the strongest economical checks are **membership plus perpendicular residual**. These verify the answer independently of how it was obtained.

## 26. Complete chapter summary

Positive definiteness provides length, perpendicularity and the independence of nonzero orthogonal vectors. In finite dimension every subspace has a unique perpendicular complement, and every vector splits uniquely into its subspace part and perpendicular residual.

Projection gives the unique closest point. Use $QQ^*$ for orthonormal columns, a Gram inverse for independent general columns, and a weighted Gram expression for a different metric. Idempotence alone may describe an oblique projector. Ordinary matrix symmetry depends on whether the basis is orthonormal.

Gram–Schmidt removes earlier components while preserving ordered spans. Its normalized output forms reduced QR, which turns full-column-rank least squares into triangular solution. Bessel measures omitted components; Parseval requires a complete expansion. Function and sampled-polynomial spaces obey the same finite-dimensional principles once their product conventions are specified.

## 27. Worked mathematical, conceptual and authentic problems

The bank combines original synthesis, identified reconstructed university exercises, exact computations, and authentic archive revisits. Solutions expose the hypotheses, calculations and failed shortcuts. Revisits are not counted as new unique examination questions. Geometry and stateful computations receive appropriate visuals; purely algebraic certificates are written explicitly.

<!-- INCLUDE: problems -->

## 28. Final examination rules and difficult-case checks

Every rule is a complete statement with its admissibility conditions. The bank supplies the proofs and counterexamples behind them.

<!-- INCLUDE: review -->

## 29. Editable exact projection laboratory

<!-- LAB: orthogonality -->

## 30. References and remaining scope

- **Oxford University — M1 Linear Algebra I 2022–23**, lecturer Andrew Wathen, [notes, native pages70–78](https://courses.maths.ox.ac.uk/pluginfile.php/25471/mod_folder/content/0/lecture_notes22.pdf?forcedownload=1).
- **MIT — 18.06SC Linear Algebra, Fall2011**, Gilbert Strang, [Session2.1](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/fdce42d9c8d8dc4eac7a9db3c1978e18_MIT18_06SCF11_Ses2.1sum.pdf), [Session2.4](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/7ac32be444c25e48590f47573833ccc6_MIT18_06SCF11_Ses2.4sum.pdf), [exercises17.1–17.2](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/b0aca3af754666dff0ab394cf36afaec_MIT18_06SCF11_Ses2.4prob.pdf).
- **Berkeley — Math54 Spring2018**, Alexander Paulin, [written course collection](https://math.berkeley.edu/~apaulin/54_001(Spring2018).html): Inner Products, Orthogonal Sets, Orthogonal Projections, Inner Product Spaces and Gram-Schmidt.
- **ETH Zurich — Linear Algebra for Computer Scientists PartII**, Afonso S. Bandeira and Robert Weismantel, [section6.3, native pages19–23](https://ti.inf.ethz.ch/ew/courses/LA25/notes_part_II.pdf).
- **Stanford — EE263 Autumn2007–08**, Stephen Boyd, [Lecture3, native pages14–16](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/lin-alg2.pdf).
- **CMU — 21-241 Matrix Algebra SummerI2014**, William Gunther, [written-course calendar](https://www.math.cmu.edu/~wgunther/241/m14/index.html), Days18–20.
- **Harvard — Math55a Honors Abstract Algebra**, [official notes, native pages12–13](https://abel.math.harvard.edu/~ctm/home/text/class/harvard/55a/08/html/home/course/course.pdf).

The [source audit](../reviews/l_orthogonality-sources.html) records comparisons and corrections. The [quality audit](../reviews/l_orthogonality-quality.html) records exact checks and browser inspection. Full floating-point stability proofs, infinite-dimensional Hilbert-space theory and full SVD theory lie outside this chapter. Exhaustive worldwide-course review and guaranteed performance on unseen questions are not claimed.
