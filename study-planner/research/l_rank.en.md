# Rank, Invertibility, and Solution Sets

## Sources and the chapter boundary

This chapter synthesizes four primary written university courses: MIT 18.700 (David Vogan, Fall 2013), Oxford M1 Linear Algebra I (Andrew Wathen, 2022 course lecturer), Stanford EE263 (Stephen Boyd, Autumn 2007–08), and Berkeley Math 54 (Alexander Paulin, Spring 2018). CMU 21-241 (William Gunther, Summer I 2014) supplies a fifth reviewed comparison. The selection follows the documented accessible five-course pool, with actual page ranges and reasons in the [source audit](../reviews/l_rank-sources.html). A whole course is not counted as read merely because its homepage was visited.

The central problem is to determine how many independent restrictions a matrix imposes, which outputs it can attain, and how much ambiguity remains in each attainable output. Gaussian elimination is the prerequisite. Vector-space terminology needed here is explained locally; the later vector-space, linear-map, orthogonality and determinant chapters develop those subjects further. This chapter includes rank inequalities and carefully delimited advanced consequences because they often turn long examination calculations into short proofs.

Work through the lesson before the solved bank. A solution displayed immediately is a teaching example; the bank is not a request to take a diagnostic test. The two authentic items are explicit revisits of previously taught archive questions, now analyzed through rank and kernel arguments. All other entries state whether they are original or adapted from a reviewed written prompt.

## Spaces, coordinates, and rank

Let $A$ have $m$ rows and $n$ columns over a field $F$. Unless a problem says otherwise, use $F=\mathbb R$. The input vector has $n$ coordinates and the output vector has $m$ coordinates:

$$A:F^n\longrightarrow F^m.$$

Its action on an input is $x\longmapsto Ax$.

A **subspace** contains zero and is closed under addition and scalar multiplication. The span of vectors consists of all their finite linear combinations. A **basis** is an independent spanning list, and its size is the dimension. The zero space has the empty basis and dimension zero; a singleton list containing the zero vector is not a basis.

Why is basis size well defined? Suppose an independent list $u_1,\ldots,u_k$ lies in a space spanned by $v_1,\ldots,v_l$. Express $u_1$ in the spanning list. Some coefficient is nonzero, so solving for that corresponding $v_j$ replaces it by $u_1$ without changing the span. At the next step, independence ensures that $u_2$ cannot lie in the span of $u_1$ alone; a still-unreplaced vector has a nonzero coefficient and can be exchanged. Continue. Each independent vector consumes one slot, so $k\le l$. Apply this inequality in both directions to two bases to obtain equal sizes. It also proves that an independent list can be extended to a basis in a finite-dimensional space, and that dependent members can be removed from a spanning list until a basis remains.

Write the columns of $A$ as $a_j$. Matrix multiplication says

$$Ax=\sum_{j=1}^n x_j a_j.$$

Consequently its image, or column space, is $\operatorname{Col}(A)=\operatorname{span}(a_1,\ldots,a_n)\subseteq F^m$. Its kernel, or null space, is $\ker A=\{x\in F^n:Ax=0\}$. Linearity proves both are subspaces: a linear combination of two zero-output inputs still has zero output, and a linear combination of attained outputs is attained by the same combination of their inputs.

The row space $\operatorname{Row}(A)\subseteq F^n$ is the span of the rows. Initially define

$$\operatorname{rank}(A)=\dim\operatorname{Col}(A).$$

The theorem below will show that this is also the dimension of the row space. Always attach the correct ambient space to a basis: a column-space vector has $m$ entries, while a row-space or kernel vector has $n$ entries. Rank is a dimension, not the number of nonzero entries, nonzero rows in the original matrix, equations written, or diagonal entries visible.

<!-- FIGURE:spaces -->

## What reduction preserves and how bases are extracted

Let $R=EA$ be the reduced row echelon form, where $E$ is invertible and records row operations. Then $Rx=0$ if and only if $Ax=0$: multiplying by $E$ cannot create or destroy a zero output. Every row of $R$ is a combination of rows of $A$; reversing the operations gives the reverse containment, so their row spaces coincide.

Their column spaces need not coincide:

$$\operatorname{Col}(R)=E\operatorname{Col}(A).$$

The invertible output-coordinate map preserves dimension and every dependency coefficient among columns. If $a_j=\sum c_i a_i$, then $Ea_j=\sum c_i Ea_i$; conversely multiply by $E^{-1}$. This is the reason pivot indices found in $R$ select a basis from the **original** columns of $A$.

Suppose $R$ has $r$ pivots at indices $j_1,\ldots,j_r$. Its nonzero rows are independent: inspect each pivot column in a zero linear combination and force its corresponding row coefficient to vanish. They span the row space, so the row rank is $r$. The pivot columns of $R$ are the first $r$ standard coordinate vectors; all its other columns have zero entries below those rows and are combinations of the pivot columns. They form a column-space basis. Because $E$ is invertible, the same pivot indices in $A$ form an independent spanning list. Thus

$$\dim\operatorname{Row}(A)=\dim\operatorname{Col}(A)=r.$$

This proof also gives $\operatorname{rank}(A^T)=\operatorname{rank}(A)$ and $0\le r\le\min(m,n)$. A nonzero matrix has rank at least one. A diagonal matrix has rank equal to its nonzero diagonal count, but that shortcut does not apply to a general triangular matrix with zero diagonal entries: $\begin{bmatrix}0&1\\0&0\end{bmatrix}$ has rank one.

### A complete rectangular example

Consider the Berkeley written example, independently transcribed and checked:

$$A=\begin{bmatrix}1&2&0&1&0\\0&0&1&1&0\\1&2&0&1&1\\-1&-2&0&-1&0\end{bmatrix}.$$

Subtract row one from row three, add row one to row four, and retain the second row. The nonzero reduced rows are

$$R_*=\begin{bmatrix}1&2&0&1&0\\0&0&1&1&0\\0&0&0&0&1\end{bmatrix}.$$

The pivot columns are one, three and five. The rows of the displayed nonzero block form a row-space basis. The original column-space basis consists of the three columns of

$$C=\begin{bmatrix}1&0&0\\0&1&0\\1&0&1\\-1&0&0\end{bmatrix}.$$

The nonpivot relations are $a_2=2a_1$ and $a_4=a_1+a_3$. These are relations in the original output coordinates, not just relations in the reduced matrix.

For the kernel, choose $x_2=s$ and $x_4=t$. The equations give $x_1=-2s-t$, $x_3=-t$, and $x_5=0$. Hence

$$x=s(-2,1,0,0,0)^T+t(-1,0,-1,1,0)^T.$$

Each direction has a distinct free coordinate equal to one and the other free coordinate zero. This proves independence. The reduced equations prove spanning; direct multiplication by $A$ verifies that both directions are annihilated. All three steps matter when a problem asks for a **basis**, not merely some null vectors.

The following exact implementation makes the distinction between original pivot columns and reduced rows explicit. Use rational entries rather than floating-point inputs. Its assertions are substitution certificates; independence and completeness follow from the pivot construction just proved.

~~~python
from sympy import Matrix, Rational, zeros

def four_spaces(rows):
    A = Matrix([[Rational(v) for v in row]
                for row in rows])
    R, pivots = A.rref()
    r = len(pivots)
    columns = [A[:, j] for j in pivots]
    row_basis = [R[i, :] for i in range(r)]
    kernel = A.nullspace()
    left_kernel = A.T.nullspace()
    assert len(kernel) + r == A.cols
    assert len(left_kernel) + r == A.rows
    assert all(A * v == zeros(A.rows, 1)
               for v in kernel)
    assert all(A.T * v == zeros(A.cols, 1)
               for v in left_kernel)
    return columns, row_basis, kernel, left_kernel
~~~

<!-- FIGURE:pivots -->

## Rank–nullity and information lost by a map

For an $m\times n$ matrix with $r$ pivots, there are $n-r$ free coordinates. Assigning one free coordinate to one and the rest to zero produces an independent spanning kernel list. Therefore

$$\operatorname{rank}(A)+\dim\ker A=n.$$

The right side is the **domain** dimension. It is not $m$ unless $m=n$. Applying the theorem to $A^T$ separately gives $\dim\ker A^T=m-r$.

Here is a proof independent of a chosen matrix reduction. Take a kernel basis $k_1,\ldots,k_q$ and extend it to a domain basis by $v_1,\ldots,v_r$. Every output is a combination of the $Av_i$, since the $Ak_j$ vanish. If $\sum c_iAv_i=0$, then $\sum c_iv_i$ is in the kernel and therefore a combination of the $k_j$. Independence of the full domain basis forces every $c_i=0$. The images $Av_i$ are thus a basis of the image. Counting the domain basis gives $n=q+r$.

One should not interpret the theorem as saying that each original coordinate is separately either retained or deleted. The retained information can be a mixture of coordinates. For $A=(1,1)$, rank and nullity are both one, yet neither individual coordinate is ignored; their sum is measured while their difference is undetectable. A basis adapted to the kernel separates these roles.

More precisely, choose a complementary subspace $V$ with $F^n=\ker A+V$ and $\ker A\cap V=\{0\}$. The restriction $A:V\to\operatorname{Col}(A)$ is bijective. Existence follows because the kernel part contributes nothing; uniqueness follows from the trivial intersection. This is the rigorous version of “rank counts distinguishable information.”

<!-- FIGURE:fibers -->

## Solution sets, consistency, and all four fundamental spaces

If $Ax_p=b$, every vector $x_p+z$ with $z\in\ker A$ has output $b$. Conversely, another solution $x$ satisfies $A(x-x_p)=0$. Therefore a nonempty solution set is exactly

$$\{x:Ax=b\}=x_p+\ker A.$$

It is an affine translate with dimension $n-r$. It is a linear subspace precisely when $b=0$: containing zero would force $A0=b=0$. Two nonempty fibers for distinct outputs are disjoint, but they share the same direction space. Over an infinite field a positive-dimensional fiber has infinitely many elements. Over a finite field with $q$ elements it has exactly $q^{n-r}$ elements; a compatible full-column-rank system has one element over either type of field.

Appending $b$ to the column list increases its span dimension by zero if $b$ is already in the image, and by one otherwise. Thus

$$Ax=b\text{ is consistent}\quad\Leftrightarrow\quad\operatorname{rank}[A\mid b]=\operatorname{rank}A.$$

For multiple loads $B$, every column system is consistent if and only if $\operatorname{rank}[A\mid B]=\operatorname{rank}A$. The increase can now exceed one. In the compatible case, a matrix solution is $X=X_p+NC$, where the columns of $N$ form a kernel basis and each column of $C$ independently selects a null direction combination.

For real matrices with the standard Euclidean inner product,

$$\ker A=\operatorname{Row}(A)^\perp,\qquad \ker A^T=\operatorname{Col}(A)^\perp.$$

The first equality follows because the equation $Ax=0$ is exactly orthogonality to every row; the second applies the same reasoning to $A^T$. Dimensions give the orthogonal direct decompositions $\mathbb R^n=\operatorname{Row}(A)\oplus\ker A$ and $\mathbb R^m=\operatorname{Col}(A)\oplus\ker A^T$.

Consequently $b$ is compatible exactly when $y^Tb=0$ for every $y$ in the left null space. Necessity is $y^TAx=0$. For sufficiency, those conditions put $b$ in $(\ker A^T)^\perp=\operatorname{Col}(A)$. A basis of the left null space suffices because a linear condition that vanishes on a basis vanishes on every linear combination. A witness with $y^TA=0$ and $y^Tb\ne0$ proves inconsistency immediately.

Over $\mathbb C$, use conjugate transpose and the Hermitian inner product. Over arbitrary fields, keep the annihilator equations as algebraic statements; do not import positive Euclidean geometry without its hypotheses. In particular $\operatorname{rank}(A^TA)=\operatorname{rank}A$ is valid for real matrices because $x^TA^TAx=\Vert Ax\Vert^2$, but not for general complex matrices with plain transpose.

<!-- FIGURE:four -->

## Injectivity, surjectivity, and one-sided inverses

Injectivity means distinct inputs have distinct outputs. Since $Ax=Ay$ is equivalent to $A(x-y)=0$, it is equivalent to a trivial kernel, rank $n$, a pivot in each column, and independent columns. It requires $n\le m$. A tall matrix can be injective while failing to cover its output space.

Surjectivity means every output in $F^m$ is attainable. It is equivalent to rank $m$, a pivot in each row, and columns spanning $F^m$. It requires $m\le n$. A wide matrix can be onto while leaving many inputs for the same output. “There is a unique solution whenever one exists” is an injectivity assertion, whereas “there is a solution for every right side” is a surjectivity assertion.

If $LA=I_n$, then $Ax=0$ implies $x=LAx=0$; thus a left inverse implies injectivity. Conversely, if $A$ is injective, invert $A$ on its image and extend that linear map to a basis of the full output space. This gives a left inverse. If $AR=I_m$, any $b$ is reached by $Rb$, so a right inverse implies surjectivity. Conversely, choose one preimage of each output basis vector and extend linearly to obtain a right inverse.

For real full-column-rank matrices, $A^TA$ is invertible: if $(A^TA)x=0$, take the quadratic form to obtain $\Vert Ax\Vert^2=0$, whence $x=0$. Hence

$$L=(A^TA)^{-1}A^T,\qquad LA=I_n.$$

For real full-row-rank matrices, $R=A^T(AA^T)^{-1}$ is a right inverse. These are convenient constructions, not the only one-sided inverses. If $L_0$ is one left inverse, every other one is $L_0+D$ with $DA=0$. If $R_0$ is one right inverse, every other one is $R_0+Z$ with $AZ=0$. The respective affine families have dimensions $n(m-n)$ and $m(n-m)$, because each row of $D$ is in the left null space and each column of $Z$ is in the kernel.

For square $A$, injectivity and surjectivity coincide by rank–nullity, and either one-sided inverse is the unique two-sided inverse. If $BA=I$, injectivity gives invertibility, and multiplication by $A^{-1}$ gives $B=A^{-1}$. This argument requires finite equal dimensions. On the infinite sequence space, deleting the first coordinate and prepending zero compose to the identity in one order but not the other.

A quantitative lower bound $\Vert Ax\Vert\ge c\Vert x\Vert$ with $c>0$ implies injectivity. For square $A$, substituting $x=A^{-1}y$ gives $\Vert A^{-1}\Vert\le c^{-1}$. For a tall matrix it gives only an inverse on the image. It does not imply symmetry or positive definiteness: $-I$ preserves norm but has negative quadratic form.

<!-- FIGURE:inverse -->

## Rank factorization and changes of coordinates

Let $C$ contain the $r$ original pivot columns of $A$. Every original column has unique coordinates in that basis; put them into a matrix $F$ with $r$ rows. Then

$$A=CF,\quad \operatorname{rank}C=\operatorname{rank}F=r.$$

The pivot columns of $F$ form $I_r$. A rank factorization separates the output directions from the coordinates used to combine them. It also gives the minimal possible inner dimension in any exact factorization $A=UV$: every such product has rank at most that inner dimension, while $CF$ attains $r$.

For the smaller example

$$A=\begin{bmatrix}1&2&1\\2&4&0\\0&0&1\end{bmatrix},\quad C=\begin{bmatrix}1&1\\2&0\\0&1\end{bmatrix},\quad F=\begin{bmatrix}1&2&0\\0&0&1\end{bmatrix},$$

the second column is twice the first. Multiplication verifies $CF=A$; the first and third columns provide independent output directions. The only kernel direction is $(-2,1,0)^T$, which is also the kernel of $F$.

Invertible left and right factors preserve rank: $\operatorname{rank}(PAQ)=\operatorname{rank}A$. For the right factor, $\ker(AQ)=Q^{-1}\ker A$, not generally the same kernel. For the left factor, $\operatorname{Col}(PA)=P\operatorname{Col}(A)$, not generally the same column space. This distinction explains why column operations can change the coordinates of a solution while preserving the number of free directions.

Using bases adapted to kernel and image, any rank-$r$ linear map can be represented by a rectangular matrix with an $I_r$ block and zeros elsewhere. Equivalently invertible $P,Q$ exist with $PAQ=\operatorname{diag}(I_r,0)$ in rectangular block notation. Choose domain basis vectors whose images form an image basis, append a kernel basis, and extend the image basis in the codomain. This is equivalence under independently changing both bases; it is stronger freedom than similarity of a square matrix and must not be confused with an eigenvalue decomposition.

<!-- FIGURE:factor -->

## Compositions, sums, and sharp inequalities

Let $B:F^p\to F^n$ and $A:F^n\to F^m$. Restrict $A$ to $\operatorname{Col}(B)$. Its image is $\operatorname{Col}(AB)$ and its kernel is $\operatorname{Col}(B)\cap\ker A$. Rank–nullity on this restricted domain yields the exact formula

$$\operatorname{rank}(AB)=\operatorname{rank}B-\dim(\operatorname{Col}(B)\cap\ker A).$$

Thus a composition loses exactly the intermediate directions that the first map reaches and the second map kills. It follows that $\operatorname{rank}(AB)\le\min(\operatorname{rank}A,\operatorname{rank}B)$ and, since $\dim\ker A=n-\operatorname{rank}A$,

$$\operatorname{rank}(AB)\ge\operatorname{rank}A+\operatorname{rank}B-n.$$

Combine with zero when this lower bound is negative. Equality at the upper bound $\operatorname{rank}(AB)=\operatorname{rank}B$ occurs exactly when that intersection is zero. Equality at the lower Sylvester bound occurs exactly when $\ker A\subseteq\operatorname{Col}(B)$, provided the displayed nonnegative bound is the one under consideration. The separate sharp bound zero can occur without that containment when the formal bound is negative.

For $AB=0$, $\operatorname{Col}(B)\subseteq\ker A$, so $\operatorname{rank}A+\operatorname{rank}B\le n$. The converse dimension inequality is only necessary, not sufficient for the product to vanish; the spaces must actually align.

For equal-sized $A,B$, every $(A+B)x$ is in $\operatorname{Col}(A)+\operatorname{Col}(B)$, so

$$\operatorname{rank}(A+B)\le\operatorname{rank}A+\operatorname{rank}B.$$

Writing $A=(A+B)-B$ proves the reverse-triangle lower bound $\operatorname{rank}(A+B)\ge|\operatorname{rank}A-\operatorname{rank}B|$. Cancellation can be complete: $B=-A$. Disjoint column spaces alone do not guarantee equality in the upper bound, because the same input feeds both maps. For $A=(1,0)^T$ and $B=(0,1)^T$, the individual ranks sum to two while the single-column sum still has rank one. Both input and output independence matter.

For subspaces $U,W$, take a basis of $U\cap W$ and extend it separately in $U$ and $W$. The shared vectors together with both extension lists span $U+W$. A zero combination puts the $W$-extension combination in $U\cap W$, forcing its coefficients to vanish; then the $U$ coefficients vanish. Hence

$$\dim(U+W)+\dim(U\cap W)=\dim U+\dim W.$$

For matrices $C,D$ with column spaces $U,W$, $\operatorname{rank}[C\ D]=\dim(U+W)$, so the formula computes the intersection dimension. Stacking matrices instead describes simultaneous restrictions: the kernel of the vertical stack is $\ker C\cap\ker D$.

For three compatible maps, Frobenius' inequality is

$$\operatorname{rank}(ABC)+\operatorname{rank}B\ge\operatorname{rank}(AB)+\operatorname{rank}(BC).$$

To prove it, let $U=\operatorname{Col}(BC)\subseteq V=\operatorname{Col}(B)$ and $K=\ker A$. Restriction formulas give the two output ranks as $\dim U-\dim(U\cap K)$ and $\dim V-\dim(V\cap K)$. Since $U\cap K\subseteq V\cap K$, subtracting the first from the second gives at most $\dim V-\dim U$, which rearranges to the inequality. This proof states the common intermediate space and avoids memorizing incompatible dimensions.

<!-- FIGURE:composition -->

## Parameters, minors, and exceptional rank

Never divide by a parameter before separating its zero branch. A matrix's rank is the largest order of a nonzero minor: independent columns form a matrix with an equal number of independent rows, and those selected rows produce an invertible square submatrix; conversely an invertible minor forces its selected columns to be independent. The determinant chapter develops expansion rules, but the only fact used here is that a square matrix is invertible precisely when its determinant is nonzero.

For polynomial entries, a minor is a polynomial in the parameters. A nonzero $r$-minor gives rank at least $r$; vanishing of every $(r+1)$-minor gives rank at most $r$. One vanished minor does not prove the latter. A generic branch may have maximal rank while exceptional algebraic parameter values have lower rank.

For

$$A(t)=\begin{bmatrix}1&1&1\\1&t&1\\1&1&t\end{bmatrix},$$

subtract the first row from the other two to get diagonal restrictions $t-1$ in the second and third coordinates. Rank is three when $t\ne1$ and one when $t=1$. It never equals two. With load $b=(b_1,b_2,b_3)^T$, the exceptional system is compatible exactly when $b_2=b_1=b_3$; if compatible it has two free directions.

For the symmetric constant-off-diagonal family $M=(d-c)I_n+cJ_n$ over $\mathbb R$, decompose an input into a multiple of the all-ones vector plus a vector with coordinate sum zero. The corresponding scalar actions are $d+(n-1)c$ and $d-c$. Count which actions are nonzero, with respective multiplicities one and $n-1$. If both vanish, then $d=c=0$ and rank is zero. This direct decomposition supplies a parameter shortcut without silently importing a full spectral theorem.

Rank can also depend on the field. The real matrix $\begin{bmatrix}1&1\\1&-1\end{bmatrix}$ has rank two, but over characteristic two its rows coincide and rank is one. Plain-transpose Gram arguments fail over $\mathbb C$: for $A=(1,i)$, the nonzero rank-one matrix $A^TA$ has square zero, while for the column $C=(1,i)^T$, $C^TC=0$ although $C$ has rank one. Use $A^*A$ for complex Euclidean geometry.

Numerical rank requires a tolerance and a scale model; exact algebraic rank does not. For $\operatorname{diag}(1,\epsilon)$ with nonzero real $\epsilon$, exact rank is two, even if a numerical procedure regards the second direction as unresolved. Neither an animation nor a decimal threshold is proof that an exact pivot vanishes.

## Structured matrices and advanced examination transfers

A block diagonal matrix has rank equal to the sum of its diagonal block ranks, because the images lie in disjoint coordinate blocks. A block triangular matrix with singular diagonal blocks need not have rank equal to that sum; the off-diagonal block can add independent directions.

If the square block $P$ is invertible, reversible block row and column operations give

$$\operatorname{rank}\begin{bmatrix}P&Q\\R&S\end{bmatrix}=\operatorname{rank}P+\operatorname{rank}(S-RP^{-1}Q).$$

First subtract $RP^{-1}$ times the first block row from the second to clear $R$. Then subtract appropriate first block columns to clear $Q$. Both operations are invertible. The remaining diagonal blocks are $P$ and its Schur complement. This formula cannot be used merely because $P$ is square; invertibility is essential.

For an outer product $uv^T$, rank is one when both vectors are nonzero, and zero otherwise: every output is a multiple of $u$, and a nonzero coefficient of $v$ attains a nonzero multiple. Therefore adding a rank-one matrix can change rank by at most one, by the sum inequality in both directions.

If square $A$ is invertible, the update $A+uv^T=A(I+w v^T)$ with $w=A^{-1}u$ is singular exactly when $1+v^Tw=0$. Indeed, any kernel vector satisfies $x=-w(v^Tx)$; nonzero solutions must be multiples of $w$, and substituting $w$ yields the condition. In the singular case $w\ne0$ and the kernel is its one-dimensional span, so the new rank is exactly $n-1$. This is a kernel proof, not an unexplained determinant identity.

If $P^2=P$, each $x$ decomposes as $Px+(x-Px)$. The first part is in the image, the second is in the kernel, and their intersection is zero since $Py=y$ on the image. Thus a basis adapted to these spaces makes $P$ similar to $\operatorname{diag}(I_r,0)$; its rank and trace both equal $r$ over $\mathbb R$. The decomposition does not imply orthogonality unless $P$ is symmetric. Over positive characteristic trace is a field element, so interpreting it as an integer rank requires care.

If $A^2=0$, the image is contained in the kernel and $r\le n-r$, so $r\le\lfloor n/2\rfloor$. The bound is attainable by mapping one member of each independent pair to the other and then to zero. For an arbitrary square $A$, the sequence of kernels of powers increases, while ranks decrease. Equality of two consecutive kernels forces all later kernels to stabilize: if $A^{k+2}x=0$, then $Ax\in\ker A^{k+1}=\ker A^k$, so $x\in\ker A^{k+1}=\ker A^k$.

Finally, when a space has $d$ coordinates and a linear constraint map has rank $r$, its feasible homogeneous subspace has dimension $d-r$. Count the rank of constraints, not their written count. On symmetric real $4\times4$ matrices there are ten independent coordinates; trace is a nonzero scalar functional of rank one, leaving dimension nine. The solved bank develops this authentic examination item and harder redundant-constraint variants.

## Fully worked mathematical and conceptual problems

The entries below range from medium to hard. Computational tasks give exact bases and certificates; conceptual tasks explain both the theorem and why tempting shortcuts fail. Course-derived entries identify their written prompt. Authentic entries retain booklet, question, page and pinned repository provenance, with independently derived answers rather than a claimed official key.

<!-- INCLUDE:problems -->

## Complete summary and examination rules

<!-- INCLUDE:review -->

## Exact laboratory

Enter a coefficient matrix, not an augmented system. The laboratory distinguishes the four ambient spaces and returns original pivot columns, reduced nonzero rows, a kernel basis and a left-kernel basis. Every calculation uses rational arithmetic. It checks the annihilation products and rank–nullity identities; these checks certify the entered matrix only.

<!-- LAB:rank -->

## References and reading record

1. David Vogan, MIT, **18.700 Linear Algebra, Fall 2013**, *Gaussian Elimination*, PDF pp. 13–20, especially §5 and Proposition 6.5. [Written handout](https://ocw.mit.edu/courses/18-700-linear-algebra-fall-2013/b144082f6883d02faeec26d7f708c63e_MIT18_700F13_gauss.pdf).
2. University of Oxford, **M1 Linear Algebra I, 2022**, Andrew Wathen, course lecturer; the downloaded note does not separately credit an author. PDF pp. 42–51, 57–61 and 68–69, printed pp. 41–50, 56–60 and 67–68. [Written notes](https://courses.maths.ox.ac.uk/pluginfile.php/25471/mod_folder/content/0/lecture_notes22.pdf?forcedownload=1).
3. Stephen Boyd, Stanford University, **EE263, Autumn 2007–08**, Lecture 3, *Linear Algebra Review*, slides 3–1 through 3–19. [Written slides](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/lin-alg.pdf).
4. Alexander Paulin, UC Berkeley, **Math 54, Spring 2018**, *Rank and Nullity*, both handwritten pages visually read. [Written notes](https://math.berkeley.edu/~apaulin/Rank%20and%20Nullity.pdf).
5. William Gunther, Carnegie Mellon University, **21-241 Matrix Algebra, Summer I 2014**, Days 9 and 10, all six pages, and Day 24, all four pages, as an additional comparison. [Course and written links](https://www.math.cmu.edu/~wgunther/241/m14/index.html).
6. **Iranian MSc CS 1405, Q41, booklet PDF p. 9; Iranian PhD CS 1404, Q30, booklet PDF p. 8.** [Pinned examination archive](https://github.com/bheydari721rn24/Phd-Exam-CSE/tree/bdadf6e2c9cadc4772ae137a96a3da753c7cfd08/Exams). Source hashes and explicit revisit labels are retained with the bank.

The lesson, figures, simulations, proofs and independently authored problems are an original synthesis. Selection and scope are finite. Symbolic checks, complete derivations and visual inspection support the stated audit; they cannot guarantee a score on every unseen examination question.
