# Linear Transformations, Coordinate Representations, and Changes of Basis

## 1. Sources, prerequisites, and the chapter contract

The four core courses are Oxford M1 Linear Algebra I (Andrew Wathen, 2022–23, native PDF pages 53–67), MIT 18.06SC (Gilbert Strang, Fall 2011, Sessions 3.6 and 3.7), Stanford EE263 (Stephen Boyd, Autumn 2007–08, Lecture 3, native pages 5–13), and Berkeley Math 54 (Alexander Paulin, Spring 2018, both four-page handouts on linear transformations and coordinate systems). Their contributions are complementary: Oxford supplies abstract proofs, MIT connects basis images to geometry, Stanford treats attainable outputs and coordinate ambiguity, and Berkeley derives directional coordinate matrices explicitly. CMU's written notes were also read and evaluated; specific errors make them an additional comparison rather than a core authority.

You should already be able to solve a linear system, recognize a basis, compute rank, and distinguish a vector space from an affine set. This chapter derives every new transformation theorem. The underlying field is denoted by $F$; unless another field is explicitly stated, numerical examples use real numbers. Matrices act on **column** coordinate vectors. $P_n(F)$ means polynomials of degree at most $n$, including zero.

The target is reliable reasoning about linear maps, not memorization of a matrix identity without its input and output types. Every occurrence of a change-of-basis matrix below states its direction. Eigenvector bases and inner products appear only where they clarify this chapter; spectral theory and orthogonality have their own subsequent chapters. The selection is a documented comparison of accessible written courses, not a claim to have exhausted every course ever offered.

## 2. What linearity asserts

A map $T:V\to W$ between vector spaces over the same field is linear when

$$T(au+bv)=aT(u)+bT(v)$$

for every $u,v\in V$ and every $a,b\in F$. This single statement is equivalent to additivity and scalar homogeneity separately. Set $a=b=1$ to obtain additivity; set $b=0$ to obtain homogeneity. Conversely apply additivity first and then homogeneity to each summand. Repeated application proves preservation of any finite linear combination:

$$T\left(\sum_{j=1}^{k}a_jv_j\right)=\sum_{j=1}^{k}a_jT(v_j).$$

Since $T(0)=T(0+0)=T(0)+T(0)$, subtracting gives $T(0)=0$. Also $T(-v)=-T(v)$. These are consequences, not substitute definitions. The map $T(x,y)=(x,y^2)$ fixes zero but violates homogeneity at $(0,1)$ with scalar two. To disprove linearity it is enough to exhibit one valid failed combination. To prove it, checking only several sample vectors is insufficient.

The field matters. Complex conjugation satisfies addition and real scalar multiplication, so it is a linear map on the two-dimensional real space $\mathbb C$. It is not complex-linear: $T(i)= -i$, whereas $iT(1)=i$. Over a finite field even familiar polynomial formulas may behave differently; on $\mathbb F_2$, the scalar function $x^2$ equals $x$. State the domain and field before declaring a formula nonlinear.

## 3. Linear, affine, and nonlinear geometry

A map $x\mapsto Ax+b$ is affine. It is linear precisely when $b=0$, because its value at zero is $b$. Affine maps preserve combinations whose coefficients sum to one. For example

$$T((1-t)x+ty)=(1-t)T(x)+tT(y).$$

A linear map preserves every linear combination; an affine translation preserves this restricted family. This explains why both can send lines to lines even though only the linear map must fix the origin. A singular linear map may collapse a line to a point. Thus “lines stay lines” needs a degeneracy qualification and does not characterize linearity.

Radially doubling every vector without changing its direction is $T(v)=2v$, despite the description $T(r,\theta)=(2r,\theta)$ in polar coordinates. Polar pairs do not use componentwise vector addition. Testing linearity in that nonlinear coordinate chart would test the wrong operations. In contrast, replacing $y$ by $|y|$ folds the plane and fails additivity across the horizontal axis.

<!-- SIM: geometry -->

## 4. Basis images determine exactly one map

Let $B=(b_1,\ldots,b_n)$ be an ordered basis of $V$, and choose arbitrary $w_1,\ldots,w_n\in W$. Define

$$T\left(\sum_{j=1}^{n}a_jb_j\right)=\sum_{j=1}^{n}a_jw_j.$$

This is well defined because the basis coefficients are unique. To prove linearity, write two inputs in that basis; the coefficients of $au+bv$ are the corresponding linear combinations of their coefficients, so the displayed definition gives the required output combination. Any linear map sending each $b_j$ to $w_j$ must satisfy this formula, proving uniqueness. No independence of the output vectors is required. Dependence among the $w_j$ creates a kernel; it does not prevent existence.

For $b_1=(1,1)$ and $b_2=(2,1)$, suppose $T(b_1)=(1,0)$ and $T(b_2)=(0,1)$. The vector $(5,3)=b_1+2b_2$ has image $(1,2)$. This is not obtained by treating $(5,3)$ as the basis coefficients. In standard coordinates the input basis matrix is

$$P=\begin{pmatrix}1&2\\1&1\end{pmatrix},\qquad A=P^{-1}=\begin{pmatrix}-1&2\\1&-1\end{pmatrix}.$$

Indeed $A(5,3)^T=(1,2)^T$. Basis-image questions should begin by solving for coefficients, not by reading physical components as coefficients.

## 5. Prescribed dependent inputs and extension freedom

Suppose specified input vectors are the columns of $X\in F^{n\times k}$, and their desired outputs are the columns of $Y\in F^{m\times k}$. A matrix $A$ satisfying $AX=Y$ exists if and only if

$$\ker X\subseteq\ker Y.$$

Necessity follows from $Xc=0\Rightarrow Yc=AXc=0$. For sufficiency define $T(Xc)=Yc$ on the input span. If $Xc=Xd$, then $c-d\in\ker X$, hence $Yc=Yd$; the definition is unambiguous and linear. Extend a basis of this span to a basis of the full domain and assign arbitrary images to the additional basis vectors.

If $\operatorname{rank}X=r$, there are $n-r$ independent unused input directions. Each can have any vector in an $m$-dimensional output space, so the solution set, when nonempty, is an affine space of dimension $m(n-r)$. Over a finite field with $q$ elements it has $q^{m(n-r)}$ members. If the specified inputs span the domain, existence implies uniqueness even if the list contains redundancy.

For inputs $(1,0),(0,1),(1,1)$, the third output must equal the sum of the first two. Declaring three arbitrary outputs silently assumes independence that these inputs do not have.

## 6. Kernel, image, and fibers

The kernel and image are

$$\ker T=\{v\in V:T(v)=0\},\qquad \operatorname{im}T=\{T(v):v\in V\}.$$

They are subspaces: a combination of kernel vectors maps to zero; a combination of two attained outputs is attained by the corresponding input combination. For a specified $y\in W$, the fiber $T^{-1}(\{y\})$ is empty if $y$ is not attained. If $T(x_0)=y$, then

$$T^{-1}(\{y\})=x_0+\ker T.$$

Proof: $T(x)=T(x_0)$ is equivalent to $T(x-x_0)=0$. Consequently all nonempty fibers have the same direction space and dimension, although a nonzero fiber is generally affine rather than a subspace. The zero fiber is the kernel.

The map $T(x,y)=(x+y,0)$ has image the horizontal axis and kernel $\operatorname{span}\{(1,-1)\}$. For output $(3,0)$ every input is $(3,0)+t(1,-1)$. Output $(3,1)$ has no preimage. “Not injective” means multiple inputs produce the same attainable output; it does not mean every output is attainable.

<!-- SIM: fibers -->

## 7. Rank–nullity with its proof

Assume $\dim V=n<\infty$. Start with a basis $k_1,\ldots,k_s$ of $\ker T$ and extend it by $u_1,\ldots,u_r$ to a basis of $V$. Every image is a combination of the $T(u_j)$ because the kernel basis images vanish. If $\sum a_jT(u_j)=0$, then $\sum a_ju_j$ is in the kernel. Express it in the $k_i$ and use independence of the extended basis to force all $a_j=0$. Thus the $T(u_j)$ form an image basis. Counting gives

$$\dim V=\dim\ker T+\dim\operatorname{im}T.$$

This argument produces adapted bases rather than merely a number. In the domain order $(u_1,\ldots,u_r,k_1,\ldots,k_s)$ and an output basis beginning with $(T(u_1),\ldots,T(u_r))$, the matrix is the rectangular block containing $I_r$ and zeros elsewhere. The kernel need not coincide with any standard coordinate axes; the normal form uses chosen bases.

For $V$ of dimension $n$ and $W$ of dimension $m$, injectivity requires rank $n$ and therefore $n\le m$. Surjectivity requires rank $m$ and therefore $m\le n$. These inequalities are necessary, not sufficient for a particular map. When $n=m<\infty$, either property forces the other.

<!-- SIM: rank-nullity -->

## 8. Coordinate maps and typed representations

An ordered basis $B$ gives a linear isomorphism $\kappa_B:V\to F^n$, defined by $\kappa_B(v)=[v]_B$, the unique coefficient column. Its inverse synthesizes the vector from those coefficients. If $C=(c_1,\ldots,c_m)$ is an output basis, the coordinate representation of $T$ is

$$A_{C\leftarrow B}=\kappa_C T\kappa_B^{-1},\qquad [T(v)]_C=A_{C\leftarrow B}[v]_B.$$

Its $j$th column is $[T(b_j)]_C$, because $[b_j]_B=e_j$. This derivation prevents two common errors: placing basis images in rows, and placing their standard coordinates in a matrix that promises $C$-coordinates.

If the spaces are ordinary coordinate spaces with basis matrices $P=(b_1\ \cdots\ b_n)$ and $Q=(c_1\ \cdots\ c_m)$, and $A$ is the standard matrix, then

$$A_{C\leftarrow B}=Q^{-1}AP.$$

The pipeline is input coefficients, physical input, physical output, output coefficients. Its operations are $P$, then $A$, then $Q^{-1}$. Matrix composition is read from right to left. This formula requires both basis matrices to be square invertible; a redundant generating list is not a basis.

<!-- SIM: coordinates -->

## 9. Full example with independent input and output bases

Let $A=\begin{pmatrix}1&2\\0&1\end{pmatrix}$, let $B=((1,1),(0,1))$, and let $C=((1,0),(1,1))$. Thus

$$P=\begin{pmatrix}1&0\\1&1\end{pmatrix},\quad Q=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad AP=\begin{pmatrix}3&2\\1&1\end{pmatrix}.$$

Multiplying by $Q^{-1}$ gives

$$A_{C\leftarrow B}=\begin{pmatrix}2&1\\1&1\end{pmatrix}.$$

For input coefficients $(2,-1)^T$, synthesis gives physical input $(2,1)^T$, the physical output is $(4,1)^T$, and output coefficients are $(3,1)^T$. Applying the representation matrix directly to $(2,-1)^T$ gives the same $(3,1)^T$. Checking both paths is a useful independent verification.

Neither $AP$ alone nor $Q^{-1}A$ is the requested representation. The first retains standard output coordinates; the second retains standard input coordinates. The matrix $Q^{-1}AP$ is generally not similar to $A$, because two bases were independently chosen.

## 10. Directional change-of-coordinate matrices

For two bases $B$ and $D$ of the same space, define $P_{B\leftarrow D}$ by

$$[v]_B=P_{B\leftarrow D}[v]_D.$$

Its columns are the vectors $[d_j]_B$. The inverse is $P_{D\leftarrow B}$, since converting in both directions recovers each coordinate column. For a third basis $E$,

$$P_{B\leftarrow E}=P_{B\leftarrow D}P_{D\leftarrow E}.$$

The middle labels must match. It is safer to derive this by substituting the two coordinate equations than to recall a word such as “transition matrix,” whose direction varies between textbooks.

With standard-basis matrices $B_0,D_0$, solve $B_0P=D_0$; equivalently $P=B_0^{-1}D_0$. Augmenting $[B_0\mid D_0]$ and reducing the left block to identity computes the entire transition at once. Row reduction is a computational tool here; the pivot operations do not change the physical basis vectors being represented.

## 11. Composition and mismatched intermediate coordinates

Suppose $T:U\to V$ and $S:V\to W$. If $T$ uses output basis $C$ and $S$ uses that same basis as its input, then

$$[ST]_{D\leftarrow B}=[S]_{D\leftarrow C}[T]_{C\leftarrow B}.$$

If $T$ outputs $C$-coordinates but $S$ expects $E$-coordinates, insert the bridge:

$$[ST]_{D\leftarrow B}=[S]_{D\leftarrow E}P_{E\leftarrow C}[T]_{C\leftarrow B}.$$

Equal numerical dimensions do not make incompatible coordinate labels compatible. Associativity follows from substitution of functions; it does not permit reversing order. A horizontal shear $H=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ and vertical shear $K=\begin{pmatrix}1&0\\1&1\end{pmatrix}$ satisfy

$$KH=\begin{pmatrix}1&1\\1&2\end{pmatrix},\qquad HK=\begin{pmatrix}2&1\\1&1\end{pmatrix}.$$

Their images of $e_1$ already differ: $(1,1)^T$ versus $(2,1)^T$. A diagram should show the intermediate vector and named operation, not just two unrelated final shapes.

<!-- SIM: composition -->

## 12. Inverses and one-sided recovery

A bijective linear map has a linear inverse. For $y_i=T(x_i)$, linearity gives $T(ax_1+bx_2)=ay_1+by_2$. Apply the inverse to get $T^{-1}(ay_1+by_2)=aT^{-1}(y_1)+bT^{-1}(y_2)$. Its coordinate matrix reverses both the direction and bases:

$$[T^{-1}]_{B\leftarrow C}=([T]_{C\leftarrow B})^{-1}.$$

A left inverse $L$ with $LT=I_V$ exists in finite dimensions exactly when $T$ is injective: necessity follows by applying $L$ to $T(v)=0$; sufficiency defines $L$ on an image basis and extends it to the codomain. A right inverse $R$ with $TR=I_W$ exists exactly when $T$ is surjective: choose a preimage for each output basis vector and extend linearly.

For a real full-column-rank matrix $A$, $(A^TA)^{-1}A^T$ is a left inverse. For real full-row-rank $A$, $A^T(AA^T)^{-1}$ is a right inverse. Their existence does not make a rectangular matrix square invertible. Over $\mathbb C$, replace transpose by conjugate transpose in these Gram formulas. Over an arbitrary field, the stated Gram construction may fail even for independent columns; use the basis-extension proof instead.

## 13. Changing both bases and changing one operator basis

Let old input/output representations be $A$. Let $P$ convert new input coordinates to old input coordinates and $Q$ convert new output coordinates to old output coordinates. Substitution yields

$$A_{\mathrm{new}}=Q^{-1}AP.$$

This is matrix equivalence and preserves rank. When the map is an endomorphism and the **same** basis change is used at both ends, $Q=P$, giving similarity:

$$A_{\mathrm{new}}=P^{-1}AP.$$

Similarity preserves determinant, trace, characteristic polynomial, and the ranks of all polynomial expressions in the operator. Proofs: determinants multiply and cancel $\det P$; cyclicity $\operatorname{tr}(XY)=\operatorname{tr}(YX)$ follows by exchanging the two finite summation indices; and

$$tI-P^{-1}AP=P^{-1}(tI-A)P.$$

Taking determinants proves equality of characteristic polynomials. Multiplication repeatedly cancels adjacent $PP^{-1}$, so $f(P^{-1}AP)=P^{-1}f(A)P$ for every polynomial $f$. Independent input/output changes need not preserve trace, determinant, or eigenvalues, even for square matrices.

## 14. A passive coordinate change is not an active motion

An active transformation changes a physical vector while the axes remain fixed. A passive coordinate change keeps the physical vector fixed but changes its coefficient description. If $v=P[v]_B$, changing the basis changes $[v]_B=P^{-1}v$ rather than moving $v$.

Consider $A=\begin{pmatrix}2&1\\3&-2\end{pmatrix}$ and $P=\begin{pmatrix}1&-2\\-2&5\end{pmatrix}$. Since $\det P=1$,

$$P^{-1}=\begin{pmatrix}5&2\\2&1\end{pmatrix},\qquad P^{-1}AP=\begin{pmatrix}14&-27\\7&-14\end{pmatrix}.$$

The larger entries describe the same operator in a more skewed basis. The trace remains zero and the determinant remains $-7$. Equal trace and determinant in dimension two imply equal characteristic polynomials, but they do **not** generally prove similarity; scalar and nonzero nilpotent matrices can share characteristic polynomials without being similar.

<!-- SIM: passive -->

## 15. Rotation, reflection, shear, and projection

A planar rotation through $\theta$ has matrix

$$R_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}.$$

Derive its columns by rotating $e_1,e_2$. Angles add under composition. An animation of rotation must use $R_{t\theta}$, not $(1-t)I+tR_\theta$: the latter usually changes lengths and can collapse the plane at a half-turn midpoint. A reflection across the line at angle $\theta$ has matrix

$$F_\theta=\begin{pmatrix}\cos(2\theta)&\sin(2\theta)\\\sin(2\theta)&-\cos(2\theta)\end{pmatrix}.$$

It fixes the line direction, negates a perpendicular direction, and squares to identity. Its determinant is negative; no continuous path consisting solely of invertible real matrices connects identity to this reflection, because determinant would have to cross zero. A discrete reflection animation therefore explains the switch rather than pretending every intervening matrix is itself a reflection.

The shear $(x,y)\mapsto(x+sy,y)$ preserves area and horizontal lines but not angles. Orthogonal projection onto a unit direction $u$ is $uu^T$. A general projection is any operator $P$ with $P^2=P$; it need not be symmetric.

<!-- SIM: transforms -->

## 16. Oblique projections and complementary subspaces

If $V=U\oplus K$, each vector has a unique expression $u+k$. Define $P(u+k)=u$. This is linear, has image $U$, kernel $K$, and satisfies $P^2=P$. Conversely, if $P^2=P$, then

$$v=Pv+(v-Pv),\quad Pv\in\operatorname{im}P,\quad v-Pv\in\ker P.$$

Their intersection is zero: if $w=Px$ and $Pw=0$, idempotence also gives $Pw=P^2x=Px=w$. Therefore every projection determines a direct sum. In an adapted basis its matrix is $\operatorname{diag}(I_r,0)$.

For projection onto the horizontal axis along $\operatorname{span}\{(1,1)\}$, write $(x,y)=(x-y,0)+(y,y)$, so

$$P=\begin{pmatrix}1&-1\\0&0\end{pmatrix}.$$

The discarded displacement is parallel to $(1,1)$, not perpendicular to the horizontal axis. Its matrix is not symmetric, but its square equals itself. The complementary projection $I-P$ has image $\ker P$ and kernel $\operatorname{im}P$. For a real idempotent, trace equals rank, since an adapted basis has only zero and one diagonal entries.

<!-- SIM: projection -->

## 17. Polynomial operators, characteristic, and evaluation

Differentiation $D:P_n(F)\to P_{n-1}(F)$ is linear. In monomial bases its $j$th degree column has the coefficient $j$ one degree lower. Over characteristic zero, its kernel consists of constants and its image is all of $P_{n-1}$. For $P_2\to P_1$,

$$[D]=\begin{pmatrix}0&1&0\\0&0&2\end{pmatrix}.$$

For a polynomial $p=2-3x+4x^2$, multiplication by this matrix gives the coefficient column $(-3,8)^T$, representing $-3+8x$. Inputs and outputs have different dimensions; treating this derivative matrix as a square operator changes the stated spaces.

In characteristic $p$, $D(x^p)=0$. Thus the characteristic-zero kernel claim fails whenever that monomial lies in the domain. For $P_4(\mathbb F_2)$, the kernel is spanned by $1,x^2,x^4$, and the image by $1,x^2$.

Evaluation at fixed nodes $t_0,\ldots,t_n$ maps a polynomial to its value column. In monomial coordinates its matrix has row $i$ equal to $(1,t_i,\ldots,t_i^n)$. Distinct nodes give invertibility: a degree-at-most-$n$ polynomial with $n+1$ roots is zero, so the kernel vanishes. Repeated nodes remove independent information unless derivative data are explicitly supplied.

<!-- SIM: polynomials -->

## 18. Interpolation, dual measurements, and compression

For distinct nodes, Lagrange polynomials

$$\ell_j(x)=\prod_{i\ne j}\frac{x-t_i}{t_j-t_i}$$

satisfy $\ell_j(t_i)=\delta_{ij}$. They form a basis because evaluating a zero combination at node $i$ extracts its coefficient. The evaluation matrix in this basis is identity, illustrating that a basis can be adapted to the measurement rather than to monomials.

An invertible synthesis matrix $W$ gives coefficients $c=W^{-1}x$. This conversion itself loses no information. Setting some coefficients to zero is a separate approximation step. With $M$ a diagonal zero/one mask, reconstruction is

$$\widehat x=WMW^{-1}x.$$

This is a projection onto the retained basis span along the discarded basis span. It is orthogonal only for an orthogonal decomposition; arbitrary skewed bases produce oblique projections. The reconstruction error is $x-\widehat x=W(I-M)c$. A nonlinear threshold rule that chooses a mask from the input is generally not a fixed linear operator, even though reconstruction for a fixed mask is linear.

<!-- SIM: compression -->

## 19. Matrix spaces are legitimate vector domains

In $M_{m\times n}(F)$, fixing a matrix $L$ makes $X\mapsto LX$ linear; fixing $R$ makes $X\mapsto XR$ linear. The map $X\mapsto LXR$ is also linear in $X$. Allowing both factors to vary creates a bilinear operation, not a linear map on the joint pair.

Transpose is a linear map $M_{m\times n}\to M_{n\times m}$. In the matrix-unit basis it permutes $E_{ij}$ into $E_{ji}$. On square matrices over a field of characteristic not two, symmetric and skew-symmetric subspaces are complementary:

$$X=\frac{X+X^T}{2}+\frac{X-X^T}{2}.$$

The projection onto symmetric matrices has kernel the skew-symmetric matrices and rank $n(n+1)/2$. In characteristic two division by two is unavailable, and the displayed decomposition must not be imported.

Trace $X\mapsto\operatorname{tr}X$ is a linear functional. Its kernel has dimension $n^2-1$ because it is surjective: $\operatorname{tr}(aE_{11})=a$. Determinant is not linear for $n\ge2$. The counterexample $\det(I+I)$ versus $\det I+\det I$ works over the reals for most dimensions, but a field-independent disproof should use two diagonal rank-deficient matrices whose sum is identity for $n=2$.

## 20. Commutators and the Sylvester equation

For fixed $A,B$, the map $\mathcal L(X)=AX-XB$ is linear on matrix space. If $A=\operatorname{diag}(a_1,\ldots,a_m)$ and $B=\operatorname{diag}(b_1,\ldots,b_n)$, then

$$\mathcal L(E_{ij})=(a_i-b_j)E_{ij}.$$

Thus its kernel dimension is the number of ordered pairs with $a_i=b_j$. The equation $AX-XB=C$ is uniquely solvable precisely when no such pair exists; then $x_{ij}=c_{ij}/(a_i-b_j)$. If a coefficient difference vanishes, the corresponding equation requires $c_{ij}=0$ and leaves $x_{ij}$ free.

For a commutator $AX-XA$, every polynomial in $A$ commutes with $A$, but that does not imply every commuting matrix is such a polynomial. When $A$ is scalar, all matrices commute; polynomials in $A$ span only scalar matrices. If $A$ is diagonal with distinct diagonal entries, its commuting matrices are precisely diagonal matrices, and interpolation does express each as a polynomial in $A$.

<!-- SIM: matrix-operators -->

## 21. Composition rank and precise preimage formulas

For $T:U\to V$ and $S:V\to W$,

$$\ker(ST)=T^{-1}(\ker S),\qquad \operatorname{im}(ST)=S(\operatorname{im}T).$$

Restrict $S$ to $\operatorname{im}T$. Its kernel is $\operatorname{im}T\cap\ker S$. Applying rank–nullity on that restricted domain gives the exact formula

$$\operatorname{rank}(ST)=\operatorname{rank}T-\dim(\operatorname{im}T\cap\ker S).$$

Therefore rank cannot exceed either factor rank. Since $\dim(\operatorname{im}T\cap\ker S)\le\dim\ker S=\dim V-\operatorname{rank}S$, the Sylvester lower bound is

$$\operatorname{rank}(ST)\ge\operatorname{rank}T+\operatorname{rank}S-\dim V.$$

Equality at the upper bound $\operatorname{rank}(ST)=\operatorname{rank}T$ means $S$ is injective on the attained output subspace of $T$, not necessarily on all of $V$. Full ranks alone are insufficient to identify a product rank without dimension and intersection data.

For maps $S,T$ with a common domain and codomain, $\ker S\cap\ker T\subseteq\ker(S+T)$ and $\operatorname{im}(S+T)\subseteq\operatorname{im}S+\operatorname{im}T$. Equalities need not hold: $T=-S$ makes the sum zero. In particular, ranks do not add mechanically.

## 22. Dual maps, transpose, and the adjoint boundary

A linear functional is a linear map to the scalar field. The dual map of $T:V\to W$ is $T^*:W^*\to V^*$, defined by $T^*(f)=f\circ T$. If $A$ represents $T$ in bases $B,C$, then $A^T$ represents the dual map in the corresponding **dual bases**. Indeed a coordinate functional row acts on $A[v]_B$, so its coefficient column becomes $A^T[f]_{C^*}$.

This is not permission to interpret $A^T$ as the original map on the original space. The direction changes and the objects are functionals. With real inner products, an adjoint $T^\dagger$ can instead be represented on the vector spaces. If the Gram matrices of the input and output bases are $G_B,G_C$, then

$$[T^\dagger]_{B\leftarrow C}=G_B^{-1}A^TG_C.$$

Derivation: $\langle Ax,y\rangle_C=x^TA^TG_Cy$ and $\langle x,By\rangle_B=x^TG_BBy$. Equality for all columns forces $G_BB=A^TG_C$. The simple transpose formula holds in orthonormal bases; complex inner products use conjugate transpose. This section establishes the boundary; full Gram–Schmidt and least-squares derivations belong to the orthogonality chapter.

## 23. Nilpotence, idempotence, and powers under coordinates

For an endomorphism, $T^2$ means applying $T$ twice with the same physical intermediate space. A nilpotent shift on $P_n$ under differentiation has sufficiently high power zero in characteristic zero. On $F^3$, the map $(x,y,z)\mapsto(0,x,y)$ has $T^3=0$ but $T^2\ne0$. Its rank sequence is $3,2,1,0$ for powers starting at zero.

Under similarity all powers are conjugated, so these ranks and the least positive zero power are invariant. Under independent domain/output basis changes, multiplying the displayed matrix by itself is usually invalid because its output coordinates differ from its input coordinates. To square such an endomorphism representation, insert the bridge from its output basis to its input basis.

An involution satisfies $T^2=I$. Over characteristic not two,

$$v=\frac{v+Tv}{2}+\frac{v-Tv}{2}$$

decomposes the domain into the fixed and negated subspaces. This is why a reflection has a natural adapted basis. In characteristic two the two eigenvalue labels coincide, and a nonidentity involution can fail this direct-sum decomposition.

<!-- SIM: powers -->

## 24. Infinite-dimensional counterexamples

Finite dimensionality is essential to the injective/surjective equivalence for endomorphisms. On all polynomials $F[x]$, multiplication by $x$ is injective but misses the constant polynomial one. On real polynomials differentiation is surjective because every polynomial has a polynomial antiderivative, but its kernel contains constants.

Represent polynomials by finite sequences of coefficients. The right shift $R(a_0,a_1,\ldots)=(0,a_0,a_1,\ldots)$ and left shift $L(a_0,a_1,\ldots)=(a_1,a_2,\ldots)$ satisfy $LR=I$ but $RL\ne I$: the latter erases the constant coefficient. This gives a concrete one-sided inverse counterexample outside finite dimensions.

Do not infer finite-dimensional identities from a formal infinite matrix without specifying its domain. Finite-support sequences, all sequences, convergent sequences, and square-summable sequences have different operator domains and additional analytic conditions.

## 25. A reliable solution procedure

First write the domain, codomain, field, and ordered bases. Second decide whether the problem asks about a physical map, coordinates of a vector, or a matrix representing a map. Third reconstruct missing basis images or identify their dependency constraints. Fourth compute kernel and image in one well-defined representation, translating a requested physical basis back through the synthesis matrix.

For a coordinate problem, draw the pipeline before multiplying. For a composition, match the middle basis labels. For a power, check that input and output coordinates agree. For a claim about uniqueness, check both attainability and kernel dimension. For a projection, verify the square identity and identify the two complementary subspaces.

Finally verify the result independently: test every basis vector, substitute a general parameterization into the original map, multiply claimed inverse matrices, or compute trace and determinant when similarity is asserted. A single numerical check is useful for catching errors but does not replace a universal proof.

## 26. Complete summary

A linear map preserves all scalar combinations over its stated field and is uniquely determined by images of a domain basis. Arbitrary prescriptions on a dependent list are feasible exactly when every input dependency is also an output dependency. A kernel records lost information; an image records attainable information; every nonempty output fiber is a translate of the kernel.

The rank–nullity proof builds a kernel basis, extends it to a domain basis, and maps the added vectors to an image basis. The coordinate equation is $[T(v)]_C=A_{C\leftarrow B}[v]_B$. Columns are output coordinates of domain basis images. General representation changes use $Q^{-1}AP$; an endomorphism with the same basis at both ends uses $P^{-1}AP$ and preserves operator invariants.

Composition acts right to left and needs matching intermediate coordinates. Projections correspond exactly to complementary image/kernel decompositions. Polynomial and matrix-space operators obey the same theory once the spaces and bases are stated. The dual transpose acts on functionals in dual bases; an adjoint in nonorthonormal vector bases additionally contains Gram matrices. Finite-dimensional qualifications and field characteristic are part of the theorem, not optional footnotes.

## 27. Formula and concept problems with complete solutions

The following problems combine calculation, symbolic conditions, proofs, and counterexamples. Course reconstructions explicitly name their origin. Authentic archive items are marked as revisited when they appeared earlier; they are not counted as new unique examination questions.

<!-- INCLUDE: problems -->

## 28. Final examination rules and failure modes

Every rule below includes its hypotheses or an explicit boundary. Use this section after learning the proofs; it is not a replacement for the instruction above.

<!-- INCLUDE: review -->

## 29. Interactive coordinate laboratory

The stored walkthroughs above use distinct geometric, coefficient-flow, matrix-space, and coordinate-pipeline models. All start paused. Controls expose individual exact checkpoints and comparisons; a moving shape is never treated as a proof. The laboratory below lets you change an operator and two bases, independently checks both computational paths, and displays the physical input and output separately from their coordinates.

<!-- LAB: linear -->

## 30. References and reading boundaries

- **Oxford University — M1 Linear Algebra I, Andrew Wathen, 2022–23.** [Written lecture notes](https://courses.maths.ox.ac.uk/pluginfile.php/25471/mod_folder/content/0/lecture_notes22.pdf?forcedownload=1), native PDF pages 53–67. Definitions, basis extension, rank–nullity, matrix representations, composition, coordinate changes, and similarity. The lecturer attribution is a course attribution, not a claim of credited PDF authorship.
- **MIT — 18.06SC Linear Algebra, Gilbert Strang, Fall 2011.** [Linear transformations and their matrices](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/positive-definite-matrices-and-applications/linear-transformations-and-their-matrices/), all four teaching pages plus both exercises and their two teaching solution pages. [Change of basis and image compression](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/positive-definite-matrices-and-applications/change-of-basis-image-compression/), all three teaching pages. License pages were separately identified.
- **Stanford University — EE263, Stephen Boyd, Autumn 2007–08, Lecture 3.** [Linear algebra review](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/lin-alg2.pdf), native PDF pages 5–13. Kernel, attainable outputs, inverses, rank, and change of coordinates.
- **University of California, Berkeley — Math 54, Alexander Paulin, Spring 2018.** [Vector Spaces and Linear Transformations](https://math.berkeley.edu/~apaulin/Vector%20Spaces%20and%20Linear%20Transformations.pdf) and [Bases and Coordinate Systems](https://math.berkeley.edu/~apaulin/Bases%20and%20Coordinate%20Systems.pdf). All eight scanned pages were read visually; native scans distinguish ambiguous subscripts and a repeated coordinate label.
- **Carnegie Mellon University — 21-241, William Gunther, Summer I 2014, Day 24.** [Written notes](https://www.math.cmu.edu/~wgunther/241/m14/notes/week6/24.pdf), all four pages. Additional comparison only; the source audit identifies incorrect independence, polynomial-space, and nonlinearity statements.
- **Iranian examination archive.** [Phd-Exam-CSE examination repository](https://github.com/bheydari721rn24/Phd-Exam-CSE/tree/main/Exams). Included items carry immutable source commits, native page numbers, and independently derived answers.

No claim of guaranteed performance on all unseen questions is made. The audit records the selected scope, exact reading, independently checked cases, source corrections, and remaining boundaries.
