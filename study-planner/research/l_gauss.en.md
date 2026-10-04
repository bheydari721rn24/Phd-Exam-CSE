# Gaussian Elimination and Linear Systems

## Written sources and learning scope

This chapter answers a precise family of questions: how to solve a finite linear system, how to prove that its entire solution set has been found, how to classify exceptional parameters without losing cases, and how to reuse or numerically improve elimination. You should already understand matrix multiplication and coordinate vectors from the preceding two chapters. All unqualified calculations use exact real arithmetic; rational examples can be computed exactly, and finite-field sections explicitly change the field.

The four primary courses are MIT 18.700, Oxford M1 Linear Algebra I, Stanford CME108/MATH114, and Berkeley Math 54. CMU 21-241 is an additional independent example and definition check. These were selected after reviewing the accessible written portions of all five course candidates, rather than selecting four names in advance. MIT supplies field-level structure and elementary-matrix arguments; Oxford supplies complete exceptional-parameter and rectangular-system examples; Stanford supplies LU, permutation bookkeeping and declared floating-point models; Berkeley supplies geometric meaning and nonconsecutive pivots. CMU provides a contrasting introductory route. The [source evaluation](../reviews/l_gauss-sources.html) records exact sections, corrections and limits. A five-course comparison cannot establish that every course offered worldwide has been inspected.

The question bank contains **71 fully worked tasks**: one newly checked doctoral item, one authentic master's revisit, and 69 original or course-derived tasks. The original tasks cover calculation, proof, parameter classification, counterexamples, exact code behavior and numerical interpretation. They are labeled separately from authentic examination questions. The [quality audit](../reviews/l_gauss-quality.html) records checks and remaining boundaries. This chapter does not replace later chapters on a full theory of rank, eigenvalues, least squares, QR or singular value decomposition.

## Equations, coordinates and geometry

### What is linear, and what is the coefficient field?

A linear system has fixed coefficients and fixed right sides. In row $i$, its equation is

$$\sum_{j=1}^{n} a_{ij}x_j=b_i.$$

The coefficients may depend on an external parameter, but when a particular parameter is classified they are constants with respect to the unknown vector. An expression such as $\lambda x+y=1$ is linear in $x,y$ for fixed $\lambda$. An equation involving $xy$, $x^2$ or $\sin x$ is generally not linear. Simplification can change that verdict only through a valid identity using the same arguments; $\sin^2 x+\cos^2 y$ is not identically one when $x$ and $y$ are independent.

Write the system as $Ax=b$, with $A\in\mathbb R^{m\times n}$, $x\in\mathbb R^n$ and $b\in\mathbb R^m$. Matrix multiplication matches each coefficient row with the variable column. The augmented matrix $[A\mid b]$ has $m$ rows and $n+1$ columns. The last column is data and is never a free variable. Fix the order of the unknowns before writing coefficients, inserting a zero when a variable is absent.

For instance, $x-y=-1$ and $4x+2y=8$ become

$$[A\mid b]=\begin{bmatrix}1&-1&-1\\4&2&8\end{bmatrix}.$$

Replace the second equation by itself minus four times the first. The new second equation is $6y=12$, giving $y=2$ and then $x=1$. Substitute into both original equations: $1-2=-1$ and $4+4=8$. This verifies existence; reversibility of the operation and the final two forced coordinates verify uniqueness.

### What the geometry does and does not show

A nonzero equation in two real unknowns describes a line; one in three unknowns describes a plane. The solution set is their common intersection. In the example, the two lines intersect at $(1,2)$. The elimination replaces one line by another passing through the same intersection; it does not preserve each individual line. Parallel distinct lines produce a contradiction. Coincident lines leave a free coordinate.

<!-- FIGURE:geometry -->

A coefficient-zero equation is different: $0=0$ describes the whole space, whereas $0=c$ with $c\ne0$ describes the empty set. Neither should be drawn as an ordinary line. In higher dimension, visual intuition must be supported by the algebraic pivot and compatibility tests. More equations than unknowns can be redundant and consistent; fewer equations than unknowns guarantee free coordinates only after consistency is established.

## Reversible row operations and certificates

### The three permitted operations

An elementary row operation acts on the **entire augmented row**. It exchanges two rows, scales one row by a nonzero scalar, or adds a scalar multiple of one row to a different row. Their inverses respectively repeat the exchange, scale by the reciprocal, and add the negative multiple. The donor row stays unchanged in the addition. A simultaneous exchange requires temporary storage or an atomic language operation; two sequential assignments can accidentally duplicate a row.

If the operation is applied to $I_m$, the resulting elementary matrix $E$ implements the operation by premultiplication. For an addition $R_i\leftarrow R_i+cR_j$ with $i\ne j$,

$$E=I_m+ce_ie_j^T.$$

Since $e_j^Te_i=0$, the square of $e_ie_j^T$ is zero. Thus the inverse is $I_m-ce_ie_j^T$. This proves invertibility without assuming that a row operation is harmless. A scaling by zero is forbidden because its inverse does not exist. Replacing two different rows by the same combination is also generally singular and can erase a constraint.

### Proof that the entire solution set is preserved

If $Ax=b$, premultiplication gives $EAx=Eb$. Conversely if $EAx=Eb$, premultiplication by $E^{-1}$ recovers $Ax=b$. Therefore the two systems have exactly the same solutions. Repeating the argument gives a composite invertible transformation $T=E_k\cdots E_1$, with

$$T[A\mid b]=[TA\mid Tb].$$

The operation performed first is the rightmost factor. Its inverse product reverses order. Associativity matters; matrix factors cannot generally be commuted.

This identity supplies a **checkable certificate** at every stage. Start a second array at $I_m$ and apply the same row operations to it. If the working augmented matrix is $M$ and the original one $M_0$, then $M=TM_0$. Our exact animations store both arrays, and the validation checks this equality for every elimination checkpoint. An unchanged solution set is then a consequence of an independently verified invertible transformation, not a caption alone.

<!-- FIGURE:certificate -->

### Row and column operations have different meanings

Row operations change equation combinations while keeping the variable vector fixed. An invertible column transformation $Q$ changes the coefficient matrix to $AQ$; the equivalent coordinate formulation is $AQy=b$ with **$x=Qy$**. A column permutation swaps variable names. A column addition makes new linear coordinates. Both can simplify computation, but returning $y$ as the original $x$ is incorrect unless the coordinate transformation is undone.

For $A=\begin{bmatrix}1&2\\0&1\end{bmatrix}$, replacing column two by column two minus twice column one gives $AQ=I$ with $Q=\begin{bmatrix}1&-2\\0&1\end{bmatrix}$. For load $(5,2)^T$, the transformed coordinate is $(5,2)^T$ but the original solution is $Q(5,2)^T=(1,2)^T$. This is why column operations must not be treated as unrestricted row reductions of the same unknown vector.

## Echelon form and a complete elimination algorithm

### Definitions that handle rectangular matrices

In row echelon form (REF), all zero rows come last; the first nonzero entry of each nonzero row is strictly to the right of the leading entry of the previous nonzero row; and every entry below a leading entry is zero. A leading entry is a **pivot**. It need not be one in REF. Reduced row echelon form (RREF) additionally requires every pivot to equal one and every other entry in its column to equal zero. Entries in nonpivot columns need not vanish.

For example,

$$R=\begin{bmatrix}1&2&0&-1\\0&0&1&3\\0&0&0&0\end{bmatrix}$$

is RREF with coefficient pivot columns one and three if all four columns are coefficients. Its second and fourth coefficient columns are free. If the fourth column is instead a right side, there are only three unknowns and only the second coefficient column is free. A matrix's interpretation and dimensions must be stated before counting parameters.

REF is not unique: scaling a pivot row preserves REF. RREF is unique for a given row-equivalence class, although the route to it is not unique. A triangular square array with a zero diagonal is not automatically REF; its actual row-leading positions must satisfy the echelon conditions.

<!-- FIGURE:pivots -->

### Forward elimination: search rows and skip empty columns

Maintain an active row $r$ and scan coefficient columns from left to right. In the current column $c$, search rows $r$ through $m$ for a nonzero entry. If none exists, mark the column as nonpivot and advance the column without advancing the active row. If one exists, exchange its row with row $r$, optionally normalize the pivot, and subtract multiples of row $r$ from all lower rows. Then advance $r$. Stop once all coefficient columns have been scanned or no active rows remain.

The relevant pivot is an entry of the **current matrix**, not the original matrix. In exact arithmetic, any nonzero eligible entry works. A top-left zero may require a row exchange; an entirely zero eligible column requires a skip. Neither condition alone proves inconsistency. Only the transformed right-side rows decide that.

```python
# Inputs are exact field elements; columns 0..n-1 are coefficients.
r = 0
for c in range(n):
    p = next((i for i in range(r, m) if M[i][c] != 0), None)
    if p is None:
        continue                 # Free coefficient column.
    M[r], M[p] = M[p], M[r]      # Exchange complete augmented rows.
    pivot = M[r][c]
    for i in range(r + 1, m):
        factor = M[i][c] / pivot
        for j in range(c + 1, n + 1):
            M[i][j] -= factor * M[r][j]
        M[i][c] = 0             # Store the known exact zero last.
    pivot_columns.append(c)
    r += 1
    if r == m:
        break
```

Do not overwrite the old pivot-column entry before saving the multiplier. Do not update the donor row during the same sweep. When tracking $T$, perform the corresponding full row operation on its complete row as well. The code above is forward elimination, not complete RREF, and returns a triangular/echelon system rather than a finished solution vector.

### Invariant and termination proof

Before scanning a new coefficient column, all previously chosen pivot columns are zero below their pivot rows. Every active row has zeros in all earlier scanned columns that were skipped or cleared. Swapping two active rows preserves these zeros. Adding a multiple of the new active pivot row to a later active row also preserves them because the donor row has those earlier zeros. The operation clears the new column below the pivot. This proves the invariant by induction.

The coefficient column increases on every iteration and a chosen pivot also increases the active row. Thus there are at most $n$ column scans and at most $\min(m,n)$ coefficient pivots. The process terminates. Each step is reversible, so the final system is equivalent. This is a full algorithmic proof: the invariant preserves already completed work, progress rules out an infinite loop, and the final conditions are precisely echelon conditions.

### Gauss–Jordan completion

Starting from REF, process pivot rows from bottom to top. Normalize each nonzero pivot to one and clear its column above it. Lower processed pivot rows have zeros in earlier pivot columns, so these upward additions preserve the earlier leading positions. The resulting coefficient block is RREF.

Our solver deliberately searches only coefficient columns. If a coefficient-zero row has a nonzero right side, it stops classification as inconsistent. Such a displayed augmented matrix need not be the RREF of **all $n+1$ columns**: a full augmented RREF would also normalize and clear the last-column pivot. Both conventions are valid when labeled. A right-side pivot signifies a contradiction and is never counted as a solved unknown.

## Reading and proving the complete solution

### Consistency first

After elimination, any row of the form $[0\;\cdots\;0\mid c]$ with $c\ne0$ requires $0=c$ and makes the system inconsistent. If every coefficient-zero row also has zero right side, choose values for every free coefficient coordinate and solve the pivot equations; this constructs a solution. Therefore this test is both necessary and sufficient.

Equivalently, if $r$ is the coefficient pivot count, the augmented rank is $r$ when the system is consistent and $r+1$ when it is inconsistent. Appending one right-side column cannot increase rank by more than one, even when several displayed rows contain contradictions.

For a consistent system, every coefficient column having a pivot means exactly one solution. Otherwise over the reals there are infinitely many. The number of free coordinates is $n-r$, independent of the number of redundant equations. These are statements about the **declared field**: a finite field with $q$ elements gives $q^{n-r}$ solutions instead of infinitely many.

### Generalized backward substitution

Let the nonzero coefficient rows of REF have pivot columns $p_1<\cdots<p_r$. Assign arbitrary values to the other coefficient coordinates. Descending through pivot rows gives

$$x_{p_i}=\frac{c_i-\sum_{j=p_i+1}^{n}u_{ij}x_j}{u_{i,p_i}}.$$

The denominator is a chosen nonzero pivot. This formula remains valid when pivot columns are not diagonal columns. The square triangular shortcut

$$x_i=\frac{b_i-\sum_{j=i+1}^{n}u_{ij}x_j}{u_{ii}}$$

requires a nonsingular upper triangular square matrix. Applying it without checking those assumptions can divide by zero or miss free variables.

### Particular solution plus homogeneous directions

In coefficient RREF, let free indices be $f_1,\ldots,f_k$. Set them all to zero to obtain one particular solution $x_p$. For each free index $f_j$, solve the homogeneous system with that free coordinate one and all other free coordinates zero; call the result $v_j$. Then

$$x=x_p+\sum_{j=1}^{k}t_jv_j,\qquad t_j\in\mathbb R.$$

Each displayed vector is a solution because $Ax_p=b$ and $Av_j=0$. Conversely every solution has a unique set of free coordinate values; its pivot equations force the same remaining values as the displayed construction. The directions are independent because their free-coordinate submatrix is an identity. Thus the representation is complete and has no redundant parameters.

For

$$[R\mid c]=\begin{bmatrix}1&0&2&-1&3\\0&1&-1&4&-1\\0&0&0&0&0\end{bmatrix},$$

take $x_3=s$, $x_4=t$. Then $x_1=3-2s+t$ and $x_2=-1+s-4t$. The full family is $(3,-1,0,0)^T+s(-2,1,1,0)^T+t(1,-4,0,1)^T$. Verifying the particular point alone is insufficient: each direction must satisfy the original homogeneous equations.

<!-- FIGURE:affine -->

### Additional restrictions and boundaries

Nonnegative coordinates, integer coordinates or a minimum-norm objective are extra requirements. They restrict an already derived affine family and may change its cardinality. A unique rational solution need not be integral. A real affine line may intersect the nonnegative orthant in a bounded segment. The master's archive revisit illustrates why a continuous free-variable count is not an integer lattice count.

With no equations and $n$ unknowns, every vector satisfies the empty system. With no unknowns, the sole candidate is the empty vector, which satisfies the system exactly when every load is zero. These boundaries sharpen the theorem even though the interactive laboratory accepts only ordinary positive dimensions.

## Canonical form and impossibility certificates

### Why RREF is unique

Row operations preserve the row space: a new row is a combination of old rows, and invertibility supplies the reverse containment. Let two RREF matrices have this common row space $W$. For each prefix of $j$ coordinates, project $W$ onto those coordinates. In RREF, a row with pivot after $j$ projects to zero, while rows with earlier pivots remain independent because their pivot-coordinate columns form an identity array. Hence the projected dimension equals the number of pivots at or before $j$. The same row space gives the same dimension for every prefix, so both RREF matrices have identical pivot positions.

Now use the common pivot-coordinate set. Evaluation on these coordinates maps the row space bijectively onto $\mathbb R^r$: the nonzero RREF rows map to the standard coordinate basis. Consequently there is exactly one vector in $W$ taking value one at a particular pivot coordinate and zero at the others. The corresponding rows of both RREF matrices must agree. Their nonzero rows, followed by their zero rows, are identical. This proof establishes uniqueness and explains why differing elimination traces can still agree at completion.

### A contradiction can be certified in the original coordinates

Suppose a tracked elimination row has coefficient entries zero and right side $c\ne0$. If that row of $T$ is $y^T$, then

$$y^TA=0,\qquad y^Tb=c\ne0.$$

Any alleged solution would give $y^TAx=y^Tb$, namely $0=c$. This is a short original-system impossibility certificate. Conversely, any such $y$ proves inconsistency before reduction is completed. For example, if the second coefficient row is twice the first but $b_2\ne2b_1$, choose $y=(-2,1)^T$.

<!-- FIGURE:contradiction -->

These certificates also characterize compatibility conditions: every linear dependence among coefficient equations must be mirrored by their loads. Row operations preserve the kernel and row space, and preserve column rank; they generally **move the column space** by the invertible left transformation. Selecting pivot indices from the reduced array and selecting those columns from the original array is therefore the correct way to recover an original column-space basis.

## Parameter systems and exceptional branches

### Never divide by an unchecked expression

A system depending on a parameter is a family of systems. An operation dividing by $p(\lambda)$ is legal only on the branch where that expression is nonzero. First branch on its zeros, then perform the division in the generic branch, and return to the last valid undivided equations for every exceptional value. Simplifying a rational expression does not restore the constraints lost at the cancelled root.

Consider $x+y=1$ and $x+\lambda y=\lambda$. Subtraction gives $(\lambda-1)y=\lambda-1$. For $\lambda\ne1$ this forces $(x,y)=(0,1)$. At $\lambda=1$ it gives $0=0$ and all $(1-t,t)$ solve the system. The generic point remains a valid exceptional point, but it is not the whole exceptional family.

### A family displaying all three solution types

The Oxford comparison example is $x+z=-5$, $2x+\alpha y+3z=-9$, $-x-\alpha y+\alpha z=\alpha^2$. Operations not requiring division yield

$$[U\mid c]=\begin{bmatrix}1&0&1&-5\\0&\alpha&1&1\\0&0&\alpha+2&\alpha^2-4\end{bmatrix}.$$

For $\alpha\ne0,-2$, the three pivots are nonzero and

$$z=\alpha-2,\qquad y=\frac3\alpha-1,\qquad x=-\alpha-3.$$

At $\alpha=0$, the second equation says $z=1$ while the third says $2z=-4$, so no solution exists. At $\alpha=-2$, the last row is an identity and the complete family is $z=t$, $y=(t-1)/2$, $x=-5-t$. This is a different result from inserting the exceptional value into a generic simplified formula.

<!-- FIGURE:branches -->

For a square family, a determinant polynomial can identify values where uniqueness may fail. It cannot decide whether those branches are inconsistent or have free variables. The right side must be reduced at each exceptional value. For rectangular families, the entire pivot pattern can change, and determinant-only reasoning may not even be available. State the domain of the parameter as well: a real root, complex root and finite-field root need not coincide.

## LU, permutations and repeated solves

### Elimination records a factorization

For a square matrix with legal nonzero pivots and no row exchanges, at stage $k$ form multipliers $l_{ik}=a_{ik}^{(k)}/a_{kk}^{(k)}$ for $i>k$. Subtract their multiples of the pivot row. The superscript denotes the **current stage**; entries from the original input usually give wrong later multipliers.

Let $g_k$ contain these multipliers below position $k$ and zeros elsewhere. The Gauss transform is $G_k=I-g_ke_k^T$. Since $e_k^Tg_k=0$, its inverse is $I+g_ke_k^T$. After elimination,

$$G_{n-1}\cdots G_1A=U,$$

and thus $A=LU$ with $L=G_1^{-1}\cdots G_{n-1}^{-1}$. This ordered product is unit lower triangular. For stages $i<j$, the relevant cross product vanishes because the $i$th coordinate of the later multiplier vector is zero, so its subdiagonal entries are exactly the stored elimination multipliers. This argument concerns these ordered Gauss transforms; the inverse of a general unit lower triangular matrix does not merely negate all subdiagonal entries.

For the Stanford comparison matrix,

$$A=\begin{bmatrix}2&1&1\\4&-6&0\\-2&7&2\end{bmatrix},$$

the multipliers are $l_{21}=2$, $l_{31}=-1$, $l_{32}=-1$, giving

$$L=\begin{bmatrix}1&0&0\\2&1&0\\-1&-1&1\end{bmatrix},$$

$$U=\begin{bmatrix}2&1&1\\0&-8&-2\\0&0&1\end{bmatrix}.$$

Their product is exactly $A$. For load $(5,-2,9)^T$, first solve $Ly=b$, obtaining $(5,-12,2)^T$, then $Ux=y$, obtaining $(1,1,2)^T$. This two-stage solve reuses the same factors for every new load.

### Existence and normalization conditions

For a nonsingular square matrix in a fixed ordering, elimination without row exchanges and with nonzero pivots is possible exactly when every leading principal determinant is nonzero. If $A=LU$ with unit lower $L$, the leading $k$ block factors as $L_kU_k$, so its determinant is the product of the first $k$ pivots. Conversely, a nonzero first leading determinant gives a legal first pivot; eliminating it produces a Schur complement whose leading determinants are ratios of successive original leading determinants. Induction supplies every later pivot.

In particular, with $\Delta_0=1$,

$$u_{kk}=\frac{\Delta_k}{\Delta_{k-1}}.$$

This is a theorem about nonsingular matrices and the declared ordering. A nonsingular matrix such as $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ still requires a row exchange. Singular matrices can have some triangular factorizations, but the nonzero-pivot theorem does not apply. Unrestricted triangular factorizations are not unique: $LU=(LD)(D^{-1}U)$ for any invertible diagonal $D$. Doolittle normalization imposes unit diagonal on $L$; Crout imposes it on $U$. Always check which normalization a question actually states.

### Partial pivoting and the convention $PA=LU$

At each stage, choose a row with largest magnitude in the active coefficient column and exchange it with the active row. For nonsingular square input this supplies a nonzero pivot. Record the row permutation $P$, keep $L$ unit lower triangular, and obtain

$$PA=LU.$$

To solve $Ax=b$, compute $Pb$, solve $Ly=Pb$, then solve $Ux=y$. The permutation convention is part of the formula. If another source writes $A=P_0LU$, then $P=P_0^T$ and the correct transformed load is $P_0^Tb$.

At a later swap, move the already stored columns of $L$ **before the current stage** along with the swapped rows. Do not exchange its unit diagonal or unused future columns. For $A=\begin{bmatrix}4&2&0\\2&1&1\\1&3&1\end{bmatrix}$, the first multipliers are $1/2$ and $1/4$. After stage one, the second pivot candidate is zero and the third-row candidate is $5/2$. Swapping rows two and three must also swap those earlier multipliers. The resulting $L$ has first-column entries $(1,1/4,1/2)^T$, not $(1,1/2,1/4)^T$.

<!-- FIGURE:plu -->

```python
# Nonsingular square input; all arithmetic and comparisons declared.
U = copy_matrix(A)
L = identity(n)
P = identity(n)
for k in range(n):
    p = max(range(k, n), key=lambda i: abs(U[i][k]))
    if U[p][k] == 0:
        raise SingularMatrix()   # Numerical code needs a scaled policy.
    U[k], U[p] = U[p], U[k]
    P[k], P[p] = P[p], P[k]
    L[k][:k], L[p][:k] = L[p][:k], L[k][:k]
    for i in range(k + 1, n):
        L[i][k] = U[i][k] / U[k][k]
        for j in range(k + 1, n):
            U[i][j] -= L[i][k] * U[k][j]
        U[i][k] = 0
# Verify P @ A == L @ U in the exact model.
```

For a blocked system with invertible upper-left block $B$, eliminating the first variable block gives the Schur complement $S=E-DB^{-1}C$ and transformed load $g-DB^{-1}f$. Both must be changed. In numerical implementation, solve with $B$ rather than forming its explicit inverse. Singular $B$ prevents this particular derivation even if the complete block matrix is invertible.

## Inverses and multiple right sides

For a nonsingular square $A$, reduce $[A\mid I_n]$ while searching pivots in $A$. If the composite transform is $T$, the final array is $[TA\mid T]$. Achieving $TA=I_n$ shows that $T=A^{-1}$. The square inverse is two-sided; direct multiplication can verify both $TA=I_n$ and $AT=I_n$. The same process solves all standard basis loads at once.

For $A=\begin{bmatrix}2&1\\1&1\end{bmatrix}$, the inverse is $\begin{bmatrix}1&-1\\-1&2\end{bmatrix}$. Its first column solves load $(1,0)^T$ and its second solves load $(0,1)^T$. If the coefficient block reduces to a nonidentity singular form, the right block is still an invertible row transform, but it is **not** an inverse of $A$.

For an $m$ by $n$ full-column-rank matrix with $m\ge n$, the reduced coefficient block is $[I_n;0]$. In reducing $[A\mid I_m]$, the first $n$ rows of the transform give a left inverse $B$ with $BA=I_n$. There may be additional zero coefficient rows, so a pivot in every coefficient **column** does not mean a pivot in every row. A left inverse gives uniqueness for compatible loads but does not guarantee existence for all loads. In the rectangular case it need not be unique and generally does not satisfy $AB=I_m$.

Multiple supplied loads can also be appended as a block $[A\mid B]$. Perform the same coefficient operations on every load column, then classify each load separately. One column can be consistent while another is inconsistent. An inverse is unnecessary when only a few loads are required; reuse a factorization and triangular solves.

## Cost, rounding and numerical interpretation

### Deriving a cost rather than memorizing a slogan

For dense square unpivoted factorization, store each multiplier with one division and update only the trailing $(n-k)$ by $(n-k)$ block. Known eliminated zeros are assigned directly. At stage $k$, there are $n-k$ divisions and $(n-k)^2$ multiplications and subtractions each. Therefore

$$D=\sum_{k=1}^{n-1}(n-k)=\frac{n(n-1)}2,$$

$$M=S=\sum_{k=1}^{n-1}(n-k)^2=\frac{(n-1)n(2n-1)}6.$$

If every multiplication, subtraction and division counts once, the factorization total is $2n^3/3-n^2/2-n/6$. This excludes pivot comparisons, exchanges, loads and indexing. One forward and one backward solve each require quadratic work. For straightforward backward substitution, there are $n(n-1)/2$ multiplications, the same number of subtractions, and $n$ divisions, totaling $n^2$ under that convention.

For $q$ loads, reuse yields cubic factorization work plus quadratic work per load. Repeating factorization for every load instead repeats the cubic term. Sparse matrices, band structure, fused multiply-add conventions and exact rational bit growth require different cost models. A field-operation count does not bound bit complexity when rational numerators and denominators grow.

### Exact zero and numerical smallness are different tests

In exact arithmetic zero is unambiguous. In floating-point arithmetic, stored coefficients approximate an underlying input and operations introduce rounding. A universal decimal threshold cannot certify exact rank for every scale. A numerical code needs a declared precision, scaling convention, tolerance policy and error analysis. The laboratory uses exact rational input so its algebraic classification has no tolerance ambiguity.

Partial pivoting makes the multiplier magnitude at most one because the selected current pivot is the largest available magnitude in its column. It often improves stability but cannot guarantee small error for every matrix: intermediate entries can grow, and an ill-conditioned system amplifies even small perturbations.

Consider $10^{-4}x+y=1$ and $x+y=2$. The exact solution is $(10000/9999,9998/9999)$. With three significant decimal digits and rounding after each scalar operation, unpivoted elimination uses multiplier $10000$. Both lower coefficient $-9999$ and load $-9998$ round to $-10000$, producing $\widehat y=1$ and $\widehat x=0$. Exchanging equations first produces multiplier $10^{-4}$ and a rounded solution $(1,1)$, much closer to the exact one. The simulation explicitly names this rounding model; it does not claim the same numbers for every computer precision.

### Residual, forward error and conditioning

For a nonsingular system, define residual $r=b-A\widehat x$ and error $e=\widehat x-x$. Then $Ae=-r$, so

$$\Vert e\Vert\le\Vert A^{-1}\Vert\Vert r\Vert.$$

For nonzero $b$ and a compatible induced norm,

$$\frac{\Vert e\Vert}{\Vert x\Vert}\le\kappa(A)\frac{\Vert r\Vert}{\Vert b\Vert},\qquad \kappa(A)=\Vert A\Vert\Vert A^{-1}\Vert.$$

The second inequality follows because $\Vert b\Vert\le\Vert A\Vert\Vert x\Vert$. A small residual alone says little about forward error when the inverse norm is large. For $A=\begin{bmatrix}1&1\\1&1+\varepsilon\end{bmatrix}$, exact $x=(1,1)^T$ and approximate $\widehat x=(2,0)^T$ differ by infinity norm one, yet the residual infinity norm is only $\varepsilon$. Conditioning belongs to the mathematical system; stability belongs to the computational procedure. Pivoting can improve a procedure without changing the system's condition number under the original coordinates.

## Changing the field

Elementary row arguments require division by nonzero elements in a field. They apply to the real, complex and rational fields and to finite fields. They do not justify treating integers as a field. Over $\mathbb F_2$, arithmetic is modulo two, addition equals subtraction, and the only nonzero scalar is one.

The equations $x+y=1$, $y+z=0$, $x+z=1$ have two binary solutions: $(1,0,0)$ and $(0,1,1)$. Over the reals, the same printed coefficient pattern has only $(1,0,0)$. In the binary field a row dependence appears because twice any entry is zero. The field changes rank and compatibility, not merely how the final solution is displayed.

For a finite field with $q$ elements, a consistent system with $n-r$ independent free coordinates has exactly $q^{n-r}$ solutions, because each free coordinate has $q$ choices and the pivot coordinates are forced. This counting proof is constructive. Modular arithmetic with composite modulus is generally not a field; a nonzero residue need not be invertible, so the field algorithm cannot be applied without checking units.

## Worked mathematical and conceptual problems

Read each solution as a sequence of justified transformations. Authentic archive questions retain their source identifiers, pages, options and independently derived answer provenance. The master's item is an intentional revisit linking linear constraint elimination to integer counting. Course-derived tasks identify their source structure; original tasks do not claim to be past examination questions. The bank is finite and does not claim to reproduce every exercise in entire university courses.

<!-- INCLUDE:problems -->

## Complete summary and examination rules

The central chain is: write the correct augmented matrix; apply reversible synchronized operations; identify coefficient pivots; test coefficient-zero rows against their right sides; then derive the complete affine family. Verify a particular solution, every homogeneous direction and completeness of the free-coordinate parametrization. Parameters require explicit branches before division. Repeated square solves benefit from LU or $PA=LU$ with a declared normalization and permutation convention. Numerical smallness, finite-field arithmetic and extra integer restrictions require their own stated models.

The following rules are complete statements, not abbreviated slogans. They distinguish computational shortcuts from hypotheses and give specific ways to detect distractors.

<!-- INCLUDE:review -->

## Exact elimination laboratory

Enter an augmented matrix using integer or rational coefficients. Each row ends with its load. The laboratory searches coefficient columns only, records every reversible operation and displays the complete exact solution or an original-system contradiction certificate. Backward and forward controls let you inspect the actual changing array; the matrices and indices use the chapter's dedicated mathematical font.

<!-- LAB:gauss -->

## References

1. **MIT — 18.700 Linear Algebra, Fall 2013. David Vogan.** [Gaussian Elimination](https://ocw.mit.edu/courses/18-700-linear-algebra-fall-2013/b144082f6883d02faeec26d7f708c63e_MIT18_700F13_gauss.pdf), instructional pp. 2–20, especially Sections 2–6. The course identifies its instructor; the handout is cited as course material. Canonical-form uniqueness and some omitted details are proved independently here.
2. **University of Oxford — M1 Linear Algebra I, Michaelmas 2022. Andrew Wathen, course lecturer.** [Lecture notes](https://courses.maths.ox.ac.uk/pluginfile.php/25471/mod_folder/content/0/lecture_notes22.pdf?forcedownload=1), printed pp. 3–7 and 16–20. The separately uncredited note author is not inferred from the lecturer's name.
3. **Stanford University — CME108/MATH114, Introduction to Scientific Computing.** [Written module index](https://web.stanford.edu/class/math114/pages/modules.html): Gaussian elimination, all three linked parts; LU factorization, all three linked parts; Permuted LU, all five linked parts. The retrieved public pages do not separately identify a lecturer, so no instructor name is invented. Exact module URLs and content fingerprints appear in the source audit.
4. **University of California, Berkeley — Math 54, Spring 2018. Alexander Paulin.** [Systems of Linear Equations and Row Reduction](https://math.berkeley.edu/~apaulin/Systems%20of%20Linear%20Equations.pdf), all seven handwritten pages, rendered and visually read; [official course](https://math.berkeley.edu/~apaulin/54_001(Spring2018).html).
5. **Carnegie Mellon University — 21-241 Matrix Algebra, Summer I 2014. William Gunther.** [Day 1](https://www.math.cmu.edu/~wgunther/241/m14/notes/week1/1.pdf), [Day 2](https://www.math.cmu.edu/~wgunther/241/m14/notes/week1/2.pdf), and [Day 8](https://www.math.cmu.edu/~wgunther/241/m14/notes/week2/8.pdf), all nine pages. Definition, sign and transcription slips are corrected rather than reproduced.
6. **Iranian examination archive.** [Phd-Exam-CSE repository](https://github.com/bheydari721rn24/Phd-Exam-CSE/tree/bdadf6e2c9cadc4772ae137a96a3da753c7cfd08/Exams). Doctoral CS 1404, Q33, booklet PDF p. 8; master's CS 1405, Q113, booklet PDF p. 25. English translations were checked against rendered originals. Answers are independently derived and are not represented as official answer keys.

The explanations, proofs, figures, simulations and solutions in this chapter are an independently organized synthesis. Course prompts are transformed into teaching tasks with explicit attribution. The documented scope is finite; a comprehensive preparation resource cannot honestly guarantee performance on every unseen question.
