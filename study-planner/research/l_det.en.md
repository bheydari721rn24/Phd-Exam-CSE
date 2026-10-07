# Determinants, Orientation, and Structured Computation

## 1. Sources, scope, and prerequisites

This chapter assumes that you can multiply matrices, perform elementary row operations, solve a linear system, and interpret rank and nullity. It develops determinants from their defining structure rather than treating them as a collection of unrelated shortcuts. The central question is: how can a single scalar encode invertibility, signed volume, and the response of a square system to a change in its entries?

Four written university courses form the core: Richard Earl's **Oxford M1 Linear Algebra II, Hilary 2026**, Stephen J. Cowley's **Cambridge Mathematical Tripos IA Vectors and Matrices, Michaelmas 2010**, Gilbert Strang's **MIT 18.06SC Linear Algebra, Fall 2011**, and Alexander Paulin's **UC Berkeley Math 54, Spring 2018**. Their roles are different: Oxford supplies the axiomatic and basis-invariance structure; Cambridge supplies permutation and index proofs; MIT supplies geometric interpretation, cofactors, and determinant recurrences; Berkeley supplies an explicit row-operation ledger. References appear at the end, and the linked source audit gives the inspected page ranges, selection decisions, and corrections to source misprints.

The candidate review also considered Harvard Math 21b, a CMU course calendar, ETH-hosted notes, and Stanford SUMO notes. A university name alone was not a selection criterion. Incorrect printed formulas, mismatched calendar links, and uncertain course provenance were recorded rather than silently counted as four independent courses. This is a documented accessible candidate pool, not a claim to have inspected every course worldwide.

The scope includes ordinary determinants, structured determinants, adjugates, Cramer's rule, parameter cases, Gram determinants, and introductory determinant identities that support harder examination problems. Spectral decompositions, general positive-definite matrix theory, and numerical error analysis have their own later chapters; any necessary bridge here is proved or stated with its exact assumptions. The worked bank distinguishes authentic examination adaptations from independently written problems and reconstructed mathematical tasks. It does not reproduce complete copyrighted course exercise collections.

Read the [source-selection audit](../reviews/l_det-sources.html) and the [mathematical and visual quality audit](../reviews/l_det-quality.html) for the chapter's reading evidence, corrections, checks, and remaining limits.

## 2. What the determinant is and is not

For a square matrix $A\in\mathbb F^{n\times n}$, its determinant is a scalar in the same field. Here the default field is $\mathbb R$ or $\mathbb C$; finite-field exceptions are identified explicitly. A rectangular matrix has no ordinary determinant. Its square minors and Gram matrix may have determinants, but those are different objects with different dimensions.

The notation $\det A$ avoids confusing determinant bars with absolute value. The expression $|\det A|$ is the nonnegative magnitude when the field is real or complex. A determinant is not a matrix, is not a norm, and does not determine every feature of a linear transformation. For example, $I_2$ and $\begin{bmatrix}1&100\\0&1\end{bmatrix}$ both have determinant one although the second greatly distorts some lengths.

For a one-dimensional matrix, $\det[a]=a$. We define the determinant of the empty $0\times0$ matrix to be one. This convention makes cofactors of a $1\times1$ matrix and recurrence initial conditions consistent; it is not a statement that an empty matrix has a visible unit area.

## 3. Signed area before formulas

Let $u=(a,c)^T$ and $v=(b,d)^T$ be the columns of a real $2\times2$ matrix. The oriented parallelogram they span has signed area

$$\det[u\ v]=ad-bc.$$

One derivation fixes the first vector and measures the component of the second perpendicular to it. When $u\ne0$, a unit left normal is $(-c,a)^T/\sqrt{a^2+c^2}$. Base length times signed height is therefore $\sqrt{a^2+c^2}(-cb+ad)/\sqrt{a^2+c^2}=ad-bc$. If $u=0$, both the area and formula vanish. Positive sign means the ordered pair has the standard counterclockwise orientation; negative sign reverses it. Physical area is the absolute value.

Adding a multiple of $u$ to $v$ changes the slant but not the signed height. This explains geometrically why a shear preserves determinant. Exchanging the two columns reverses orientation while retaining physical area. Multiplying one column by a negative number changes both its length and orientation. Multiplying the entire matrix by $t$ changes two columns, so the area factor is $t^2$, not $t$.

<!-- SIM: geometry -->

## 4. Permutations and the Leibniz definition

A permutation $\pi$ is a bijection of $\{1,\ldots,n\}$. Its inversion count is the number of pairs $i<j$ with $\pi(i)>\pi(j)$. Define $\operatorname{sgn}(\pi)=(-1)^{\operatorname{inv}(\pi)}$. Adjacent exchanges change inversion parity, and sorting a permutation by adjacent exchanges connects this definition with the parity of transpositions. Equivalently, if its disjoint-cycle decomposition has $c$ cycles, counting fixed points as cycles, then its sign is $(-1)^{n-c}$. A cycle of length $r$ uses $r-1$ transpositions.

The determinant is defined by

$$\det A=\sum_{\pi\in S_n}\operatorname{sgn}(\pi)\prod_{i=1}^n a_{i,\pi(i)}.$$

Each product selects exactly one entry from each row and each column. Selecting two entries from the same column is not a determinant term. There are $n!$ potential terms; zeros can eliminate many. Their signs come from the permutation, not from whether their numeric factors happen to be positive. A negative entry and a negative permutation sign are separate contributions to the final sign.

For $I_n$, only the identity permutation survives and its product is one. For a triangular matrix, every nonidentity permutation selects at least one entry on the zero side of the diagonal. One way to see this for an upper triangular matrix is that a surviving permutation must satisfy $\pi(i)\ge i$ for every row; summing both sides forces equality for every row. Thus its determinant is the diagonal product, including zero diagonals.

<!-- SIM: permutations -->

## 5. Why the three determinant axioms characterize it

The Leibniz sum is linear in each row separately, vanishes when two rows are equal, and equals one on the identity. Linearity follows because each term contains exactly one factor from a specified row. For two equal rows, pair every permutation with the permutation that exchanges their chosen columns: products match and signs are opposite. This is a direct cancellation argument, including characteristic two, where opposite terms add to zero.

Conversely, suppose a scalar function of $n$ rows is multilinear, alternating, and normalized on the standard basis. Write each row as a linear combination of the standard row vectors. Expanding all rows produces $n^n$ choices. A repeated basis row kills its term by alternation. The remaining choices are permutations; exchanging basis rows gives precisely their signs, so the function equals the Leibniz sum. This proves uniqueness without dividing by any matrix entry.

In fields of characteristic other than two, a swap law implies equal rows give zero because $D=-D$ implies $2D=0$. In characteristic two that inference fails; alternation must be required directly. Our ordinary real and complex results do not have that exception, but recognizing it prevents an invalid proof from being presented as field independent.

## 6. Multilinearity is local, not whole-matrix additivity

When every other row is fixed,

$$\det(r_1,\ldots,\alpha u+\beta v,\ldots,r_n)=\alpha\det(r_1,\ldots,u,\ldots,r_n)+\beta\det(r_1,\ldots,v,\ldots,r_n).$$

Changing all rows of $A+B$ creates mixed choices. Therefore $\det(A+B)$ usually differs from $\det A+\det B$. With $A=B=I_2$, the two values are four and two. For two-by-two matrices, the omitted mixed contribution is $a_{11}b_{22}+b_{11}a_{22}-a_{12}b_{21}-b_{12}a_{21}$.

If $r_i$ becomes $\alpha r_i+\beta r_j$ with $j\ne i$ while row $j$ stays fixed, the determinant is multiplied by $\alpha$: the second term has equal rows. If several rows change simultaneously, do not apply that argument as though each still used an unchanged original row. Write the simultaneous transformation as multiplication by a row-mixing matrix and evaluate its determinant.

## 7. The row-operation ledger

For a single replacement $R_i\leftarrow R_i+tR_j$, $i\ne j$, the determinant is unchanged. For a row swap, it changes sign. For $R_i\leftarrow tR_i$, it is multiplied by $t$. Scaling by zero still has that determinant effect but is not an invertible elementary operation.

Maintain an explicit relation $\det M=k\det A$ between the current matrix $M$ and the original matrix $A$. Start with $k=1$. Each swap negates $k$; each nonzero row scaling multiplies $k$ by that scale; row replacement leaves it unchanged. At a triangular endpoint, divide the diagonal product by $k$. This convention avoids reversing a correction factor. Alternatively, accumulate a factor $f$ in $\det A=f\det M$, but then scaling a row by $t$ changes $f$ to $f/t$.

Every statement has a column analogue. It is valid to mix row and column operations as long as their factors are tracked. It is invalid to multiply the diagonal of an arbitrary matrix before it is triangular, or to read the determinant directly from its normalized reduced row echelon form without retaining the ledger.

<!-- SIM: elimination -->

## 8. Transpose, products, inverses, and basis invariance

Transposition preserves determinant. In the Leibniz formula for $A^T$, use $\pi^{-1}$ to reorder the factors, and use $\operatorname{sgn}(\pi^{-1})=\operatorname{sgn}(\pi)$. This proves the result without assuming that a zero pivot can be divided by.

For square matrices of the same order,

$$\det(AB)=\det A\det B.$$

To prove this, expand each column of $AB$ as $\sum_k b_{kj}A_k$. Multilinearity expands its determinant into choices of columns of $A$. Repeated choices vanish. A permutation of all columns contributes its sign times $\det A$, and the sum of the remaining coefficient products is $\det B$. This proof also covers singular factors.

Consequently, $\det(A^m)=(\det A)^m$ for nonnegative integers $m$, and for negative integers when $A$ is invertible. The inverse satisfies $\det(A^{-1})=1/\det A$. If $B=P^{-1}AP$ with $P$ invertible, the two determinants agree. A linear endomorphism therefore has a well-defined determinant independent of the basis used for both its domain and codomain. Using unrelated bases for domain and codomain produces an equivalence transformation, not necessarily similarity; its determinant may change.

## 9. Invertibility and the limits of a zero determinant

Gaussian elimination by swaps and replacements either reaches a nonzero diagonal at every stage or has fewer than $n$ pivots. The first case gives a nonzero determinant and an invertible matrix; the second gives a zero diagonal in echelon form and determinant zero. Thus, for square matrices, nonzero determinant, full rank, trivial nullspace, and unique solution for every right-hand side are equivalent.

The equation $\det A=0$ says only $\operatorname{rank}A<n$. It does not identify the exact rank. It also does not decide whether $Ax=b$ is inconsistent or has infinitely many solutions: compare the ranks of $A$ and its augmented matrix. A nearly zero floating-point determinant does not prove exact singularity; exact arithmetic or a numerical rank criterion is required.

## 10. Minors, cofactors, and choosing the best expansion

Let $A_{\widehat i,\widehat j}$ be the matrix formed by deleting row $i$ and column $j$. Its determinant is the minor $M_{ij}$, while its signed cofactor is $C_{ij}=(-1)^{i+j}M_{ij}$. In particular, a cofactor is a scalar, not the remaining matrix. The checkerboard starts with a plus sign at position $(1,1)$.

Grouping Leibniz terms by the selected entry of row $i$ gives

$$\det A=\sum_{j=1}^n a_{ij}C_{ij}.$$

Moving that row and column to the first position requires $(i-1)+(j-1)$ exchanges, which explains $(-1)^{i+j}$. Column expansion follows by transposition. Choose a row or column with many zeros; often first create zeros with determinant-preserving operations. Cofactors in the chosen row do not depend on that row's entries, but they can depend on entries in other rows. Summing $a_{ij}C_{kj}$ for $k\ne i$ gives zero: it expands a matrix with two equal rows.

<!-- SIM: cofactors -->

## 11. Adjugates and their singular cases

Let $C$ be the cofactor matrix. The adjugate is its transpose: $\operatorname{adj}A=C^T$. The product identities are

$$A\operatorname{adj}A=\operatorname{adj}A\,A=(\det A)I_n.$$

Indeed, product entry $(i,k)$ is $\sum_j a_{ij}C_{kj}$. When $i=k$, this is a row expansion of the determinant. When $i\ne k$, it is the equal-row expansion just proved and is zero. The reversed product follows with columns. If the determinant is nonzero, divide to obtain the inverse. If it is zero, the identity remains valid; division does not.

For $n\ge2$, rank at most $n-2$ forces every $(n-1)$-minor to vanish, so the adjugate is zero. At rank $n-1$, at least one such minor is nonzero. All columns of the adjugate lie in the one-dimensional right nullspace, so its rank is one. At full rank it is invertible. Also

$$\det(\operatorname{adj}A)=(\det A)^{n-1}.$$

For invertible $A$, apply the inverse formula and whole-matrix scaling. For singular $A$ and $n\ge2$, the rank cases give zero on both sides. For $n=1$, the adjugate is $[1]$, including when $A=[0]$; the identity is interpreted with the zeroth power equal to one. Distinguish adjugate from the conjugate transpose sometimes called an adjoint.

## 12. Cramer's rule and consistency traps

If $A_j(b)$ replaces column $j$ of $A$ with $b$, and $\det A\ne0$, then

$$x_j=\frac{\det A_j(b)}{\det A}.$$

For a direct proof, substitute $b=\sum_k x_k A_k$ into the replaced column. All terms with $k\ne j$ have a repeated column; only $x_j\det A$ remains. This explains why one replaces a column, not a row, when solving for a coordinate of a column-vector unknown.

If the denominator is zero, Cramer's rule is unavailable. A nonzero replacement determinant proves inconsistency, but all replacement determinants zero need not prove consistency when rank is below $n-1$. For example, a zero two-by-two coefficient matrix and nonzero right-hand side produce all replacement determinants zero although the equations cannot hold. At rank $n-1$, all column replacement determinants zero do imply that $b$ belongs to the column space, because some $n-1$ columns are independent and can be completed only by a vector outside that space.

<!-- SIM: cramer -->

## 13. Parameter matrices: evaluate exceptional cases separately

The determinant of a polynomial-entry matrix is itself a polynomial. Factor it before deciding where the matrix is singular. An elimination step dividing by $t-a$ proves a formula only away from $t=a$; substitute the exceptional value into the original matrix and assess rank or consistency there.

For $A=(x-1)I_n+J_n$, where every entry of $J_n$ is one,

$$\det A=(x-1)^{n-1}(x+n-1).$$

One proof uses the constant-vector direction, where $J_n$ multiplies by $n$, and the sum-zero subspace, where it vanishes. These subspaces form a direct sum over $\mathbb R$. In a basis adapted to them, $A$ is diagonal with one factor $x+n-1$ and $n-1$ factors $x-1$. This is a proved invariant-subspace calculation, not an assumption of arbitrary diagonalizability. For $n\ge2$, at $x=1$ rank is one, while at $x=1-n$ rank is $n-1$. The $n=1$ formula simply becomes $x$ and must be treated separately.

<!-- SIM: parameter -->

## 14. Triangular blocks and Schur complements

For square diagonal blocks $B,D$, the block triangular determinant is $\det B\det D$ regardless of the off-diagonal block. The Leibniz choices cannot move a lower-block row into the upper columns without also using a forbidden zero entry. No invertibility assumption is needed for this triangular-block identity.

For a general block matrix, if $B$ is invertible,

$$\det\begin{bmatrix}B&C\\E&D\end{bmatrix}=\det B\det(D-EB^{-1}C).$$

Left multiplication by $\begin{bmatrix}I&0\\-EB^{-1}&I\end{bmatrix}$ has determinant one and makes the lower-left block zero. The lower-right block is the Schur complement. Matrix multiplication order matters. One cannot replace this expression by $\det(BD-EC)$ for arbitrary matrix blocks, nor use $B^{-1}$ when $B$ is singular. If $D$ is invertible, eliminating the opposite block gives $\det D\det(B-CD^{-1}E)$.

<!-- SIM: blocks -->

## 15. Rank-one updates without unnecessary inversion

Multilinearity in columns gives, for every square $A$,

$$\det(A+uv^T)=\det A+v^T\operatorname{adj}(A)u.$$

Expand column $j$ as $A_j+v_j u$. Terms selecting two update columns vanish because they are proportional. The remaining single-update term is $v_j\sum_i C_{ij}u_i$, and summing over $j$ gives the identity. This proof covers singular $A$.

For invertible $A$, substitute the adjugate formula:

$$\det(A+uv^T)=\det A(1+v^TA^{-1}u).$$

Therefore a rank-one update becomes singular precisely when the scalar factor is zero. In particular, $\det(I+uv^T)=1+v^Tu$, and $\det(\alpha I+\beta J)=\alpha^{n-1}(\alpha+n\beta)$, with the $n=1$ convention handled directly. Applying the inverse-based version to a singular matrix is an avoidable error because the adjugate version already supplies the correct formula.

<!-- SIM: update -->

## 16. Vandermonde determinants and interpolation

For $V_{ij}=x_i^{j-1}$,

$$\det V=\prod_{1\le i<j\le n}(x_j-x_i).$$

Here is a complete polynomial proof. If two nodes coincide, two rows coincide, so the determinant polynomial is divisible by each difference $x_j-x_i$. Its total degree is $0+1+\cdots+(n-1)$, equal to the degree of their product. Hence it is a constant times that product. The coefficient of $x_2x_3^2\cdots x_n^{n-1}$ in both expressions is one: in the determinant it comes from the identity permutation, and in the product it comes from choosing the higher-index node in every factor. The constant is therefore one. Polynomial divisibility can be justified successively over the polynomial ring over a field; the distinct linear factors are nonassociate irreducibles.

The sign convention depends on the row order and increasing powers. Reversing the nodes changes the sign by $(-1)^{n(n-1)/2}$. Distinct nodes imply invertibility and uniqueness of polynomial interpolation of degree below $n$. Repeated nodes make the ordinary Vandermonde singular; derivative constraints require a different, confluent matrix.

<!-- SIM: vandermonde -->

## 17. Tridiagonal recurrences and boundary conditions

Let $T_n$ have diagonal entries $a_1,\ldots,a_n$, upper off-diagonal entries $b_1,\ldots,b_{n-1}$, and lower off-diagonal entries $c_1,\ldots,c_{n-1}$. Its leading principal determinants satisfy

$$D_0=1,\qquad D_1=a_1,\qquad D_n=a_nD_{n-1}-b_{n-1}c_{n-1}D_{n-2}.$$

Expand the last row. Its diagonal term leaves $T_{n-1}$. Its only other entry is at column $n-1$, with negative cofactor sign. In that minor, expansion of the last column yields $b_{n-1}D_{n-2}$. This derives the recurrence even when earlier determinants vanish; it does not divide by a pivot.

When all three bands are one, the sequence starting at $D_0$ is $1,1,0,-1,-1,0,1,\ldots$, with period six. When the diagonal is two and the off-diagonals are minus one, induction gives $D_n=n+1$. Verify $D_0,D_1$ before using a closed form. The determinant recurrence is a mathematical relation; computing it uses linear arithmetic-operation count, although exact integer bit lengths may still grow.

<!-- SIM: recurrence -->

## 18. Rectangular products, Cauchy–Binet, and Gram volume

If $X$ is $m\times n$, $Y$ is $n\times m$, and $m\le n$, then

$$\det(XY)=\sum_{S\subseteq\{1,\ldots,n\},\ |S|=m}\det(X_{:,S})\det(Y_{S,:}).$$

To derive Cauchy–Binet, expand the columns of $XY$ as combinations of columns of $X$. Repeated chosen columns kill their determinant. Group the surviving ordered choices by their underlying set $S$. Sorting their columns contributes a permutation sign, and summing the corresponding coefficients produces the determinant of $Y_{S,:}$. This is the rectangular version of the product proof. If $m>n$, rank is below $m$ and the product determinant is zero.

For a real $m\times k$ matrix $U$, with $k\le m$, apply the identity to $U^TU$:

$$\det(U^TU)=\sum_{|S|=k}\det(U_{S,:})^2.$$

This is nonnegative and is zero precisely when the columns are dependent, because full column rank is equivalent to a nonzero maximal minor. Its square root is the $k$-dimensional volume of the parallelotope spanned by the columns. For complex matrices, use $U^*U$ and squared absolute values, not an ordinary transpose. A rectangular matrix itself has no signed determinant even though this Gram volume exists.

## 19. Orthogonal, skew-symmetric, and special transformations

If $Q^TQ=I$, multiplicativity gives $(\det Q)^2=1$, so $\det Q=\pm1$. The converse is false: a shear has determinant one but is not orthogonal. A reflection with unit normal $u$ is $H=I-2uu^T$; the rank-one formula gives determinant minus one. A rotation in a coordinate plane has determinant one, and any product of $r$ reflections has determinant $(-1)^r$.

For a real skew-symmetric matrix $K^T=-K$, transposition and scaling give $\det K=(-1)^n\det K$. If $n$ is odd, this forces zero over the real or complex field. If $n$ is even, it gives no vanishing conclusion; $\begin{bmatrix}0&a\\-a&0\end{bmatrix}$ has determinant $a^2$. In characteristic two, dividing by two would again be invalid.

For a projection $P^2=P$, the space decomposes into its image, where it acts as identity, and its kernel, where it acts as zero. A proper projection therefore has determinant zero; a full-rank projection is identity and has determinant one. For an involution $S^2=I$ over $\mathbb R$, the plus and minus eigenspaces form a direct sum because $v=(v+Sv)/2+(v-Sv)/2$. Its determinant is $(-1)^r$ where $r$ is the dimension of the minus subspace.

## 20. Characteristic polynomials and determinant consequences

The characteristic polynomial convention here is $p_A(t)=\det(tI-A)$. Its leading coefficient is one, its coefficient of $t^{n-1}$ is $-\operatorname{tr}A$, and its constant coefficient is $(-1)^n\det A$. The trace coefficient follows because obtaining degree $n-1$ requires selecting $-a_{ii}$ in one diagonal slot and $t$ in every other one; off-diagonal selections require at least two non-$t$ factors.

Over $\mathbb C$, the polynomial factors into $\prod_i(t-\lambda_i)$ with algebraic multiplicities. Comparing constants yields $\det A=\prod_i\lambda_i$ without assuming diagonalizability. It is not legitimate to infer individual eigenvalues solely from the determinant, or to equate algebraic multiplicity with eigenspace dimension. A triangular map on polynomials can have its determinant read from the diagonal without solving any eigenvector equation.

## 21. Positivity requires more than a determinant

A positive determinant does not imply positive definiteness: $-I_2$ has determinant one but negative quadratic forms. For a real symmetric two-by-two matrix $\begin{bmatrix}a&b\\b&c\end{bmatrix}$, completing the square gives

$$ax^2+2bxy+cy^2=a(x+\frac ba y)^2+\frac{ac-b^2}{a}y^2.$$

It is positive definite exactly when $a>0$ and $ac-b^2>0$. The case $a=0$ is already incompatible with strict positivity on $(1,0)$. The higher-dimensional leading-principal-minor criterion is the corresponding repeated completion-of-squares result; one must inspect all leading minors in the given order, not only the full determinant. For the symmetric constant-off-diagonal matrix, use the constant and sum-zero decomposition from Section 13 to prove positivity directly, including both strict boundary exclusions.

## 22. Determinant derivatives and sensitivity

Because cofactor $C_{ij}$ excludes entry $a_{ij}$, the determinant is affine in that individual entry, with derivative $C_{ij}$. For a differentiable matrix path $A(t)$,

$$\frac{d}{dt}\det A(t)=\sum_{i,j}C_{ij}(A(t))a'_{ij}(t)=\operatorname{tr}(\operatorname{adj}(A(t))A'(t)).$$

This identity remains true at singular matrices. At invertible points it becomes $\det A(t)\operatorname{tr}(A(t)^{-1}A'(t))$. Replacing one entry by an increment $h$ gives an exact affine change $hC_{ij}$, not only a first-order approximation. Replacing many entries generally adds higher-order terms. Over real invertible intervals, the derivative of $\log|\det A(t)|$ is $\operatorname{tr}(A(t)^{-1}A'(t))$.

## 23. Computation, exact arithmetic, and a usable algorithm

Permutation expansion and naive recursive cofactors are factorial methods. Gaussian elimination needs cubic arithmetic operations for a dense matrix. Sparse expansion, tridiagonal recurrence, block elimination, or a rank-one identity can be cheaper when their assumptions actually hold.

The following exact-arithmetic pseudocode uses swaps and row replacements only. A zero candidate pivot triggers a row search, not an immediate declaration that the original determinant is zero. No row normalization is performed, so only swap parity corrects the final diagonal product.

```text
determinant(A):                 # A is square; copy before changing it
    M = exact_copy(A)
    sign = 1
    for k = 0, ..., n-1:
        p = first i >= k with M[i,k] != 0
        if no such p exists: return 0
        if p != k: swap rows p and k; sign = -sign
        for i = k+1, ..., n-1:
            multiplier = M[i,k] / M[k,k]
            row_i = row_i - multiplier * row_k
    return sign * product(M[k,k] for k = 0, ..., n-1)
```

For integer matrices, rational arithmetic preserves exactness but can enlarge numerators. Bareiss elimination replaces the update by $(p m_{ij}-m_{ik}m_{kj})/q$, with preceding pivot $q$ and initial $q=1$; when applied correctly to exact integer data, divisions are exact. Pivoting and singular cases still require care. Floating-point computation usually uses pivoted LU and a log magnitude $\sum_i\log|u_{ii}|$ plus sign, to avoid overflow. A tolerance in such computation is a numerical policy, not a theorem of exact algebra.

## 24. A decision procedure for examination problems

First confirm squareness and the quantity requested. Then inspect zero patterns, triangular structure, dependence, equal row sums, parameter factors, repeated nodes, block structure, and rank-one structure. Choose a method that reveals why the answer has its form. Keep factors, swap signs, dimension powers, and exceptional parameter values visible. Verify a symbolic expression at a simple nonexceptional input and, when practical, by an independent method.

For multiple-choice problems, derive the result before using the options. Diagnose likely distractors: a missing swap sign, a missing cofactor sign, a scalar power of one instead of $n$, omitted cross terms, an untransposed cofactor matrix, or division at a singular parameter. A correct numeric answer without its conditions is not a transferable solution.

## 25. Complete summary

The determinant is the unique normalized alternating multilinear scalar function of the rows or columns of a square matrix. Its permutation formula explains every ordinary operation law. Swaps change its sign, scaling one row changes it by that factor, and adding a multiple of another row preserves it. Transpose preserves determinant; products multiply determinants. Nonzero determinant is equivalent to invertibility for square matrices, while zero determinant alone does not determine exact rank or consistency.

Cofactors use deleted-row/deleted-column minors and the sign $(-1)^{i+j}$. Their transpose is the adjugate, whose product with the original matrix is $(\det A)I$. Cramer's rule requires a nonzero denominator and replaces a column. Structured problems should be recognized before expanded: triangular blocks, Schur complements with invertible pivot blocks, rank-one updates, Vandermonde products, and tridiagonal recurrences each have a precise efficient route.

Over the real field, determinant sign describes orientation and its magnitude describes full-dimensional volume scaling. Gram determinants provide squared lower-dimensional volume for rectangular column systems. Determinant one does not imply orthogonality, a positive determinant does not imply positive definiteness, and repeated roots of a determinant polynomial do not automatically identify nullity. The final rules below convert these conditions into retrieval cues and worked checks.

## 26. Mathematical and conceptual problems with complete solutions

The authentic questions preserve their original option order in checked English adaptations. Answers are independently derived, not presented as official answer keys. The additional problems include numerical calculation, formula derivation, counterexamples, conditional statements, parameter classification, and mixed-method synthesis. Visualizations attached to solutions use the stated data or an explicitly labelled numerical specialization. Read the solution as instruction, then attempt the corresponding reasoning independently after studying the chapter.

<!-- INCLUDE: problems -->

## 27. Final examination rules and worked retrieval checks

<!-- INCLUDE: review -->

## 28. Editable determinant laboratory

<!-- LAB: determinant -->

## 29. References and verification limits

1. **University of Oxford — Richard Earl. M1 Linear Algebra II, Hilary Term 2026.** Chapter 1, PDF pages 5–21, covering definitions, permutation matrices, adjugates, and determinants of linear maps. [Official lecture notes](https://courses.maths.ox.ac.uk/mod/resource/view.php?id=61510).
2. **University of Cambridge — Stephen J. Cowley. Mathematical Tripos IA Vectors and Matrices, Michaelmas 2010.** Sections 3.7, 4.1–4.2, the determinant paragraph of Section 4.3, and Appendix B; PDF pages 74–84, 89, and 148. [Official teaching notes](https://www.damtp.cam.ac.uk/user/sjc1/teaching/VandM/notes.pdf). These notes were inspected as references and are not redistributed here.
3. **Massachusetts Institute of Technology — Gilbert Strang. 18.06SC Linear Algebra, Fall 2011.** Sessions 2.5–2.7 written summaries, instructional PDF pages 1–3, 1–3, and 1–4 respectively. [Properties](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/5dd3f8ec0a398fd74264fef3fd591f81_MIT18_06SCF11_Ses2.5sum.pdf), [Cofactors](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/cc79f04d92ee282758780bac2ec5e403_MIT18_06SCF11_Ses2.6sum.pdf), [Cramer and volume](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/f6e46da0d783d8f9c0a25c407c76166a_MIT18_06SCF11_Ses2.7sum.pdf).
4. **University of California, Berkeley — Alexander Paulin. Math 54, Spring 2018.** Determinants lecture, all four handwritten pages. [Official notes](https://math.berkeley.edu/~apaulin/Determinants.pdf).

The synthesis, explanatory proofs, original problems, and diagrams are independently written. A source-audit link identifies printed mistakes corrected during review. The quality audit records exact computations, model-state checks, browser typography, delimiter checks, mobile layout, and retention of earlier chapters. Finite checks support the inspected claims; they do not establish a literal guarantee of perfection or performance on every unseen examination question. Optional extensions are clearly distinguished from the core determinant syllabus.
