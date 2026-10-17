# Gaussian elimination: deeper instruction for the individual revision

## Column-space transport and original pivot columns

The exact statement for an invertible row transformation is $R=TA$, so $\operatorname{Col}(R)=T\operatorname{Col}(A)$. The dimension is unchanged because the restriction of the invertible map $T$ to that subspace is a bijection onto its image. Equality of dimensions does not assert equality of the two sets of vectors in the ambient equation space.

There are also important cases where the spaces are equal. If $A$ has full row rank, its columns already span the whole space $\mathbb F^m$, and applying $T$ leaves that entire space unchanged. More generally a proper subspace may happen to be invariant under the particular $T$. For example the first coordinate axis is unchanged by scaling the two coordinates separately. Therefore “row operations always change the column space” is false, just as “row operations always preserve the column space” is false.

Why, then, are reduced pivot indices useful for the original columns? Denote the original columns by $a_j$ and the reduced columns by $r_j=Ta_j$. For any coefficients $c_j$,

$$\sum_j c_ja_j=0\quad\Longleftrightarrow\quad\sum_j c_jr_j=0.$$

One direction follows by applying $T$; the other by applying $T^{-1}$. Thus the complete linear-dependence relations among corresponding columns are unchanged. In coefficient RREF the pivot columns are independent and span every reduced column. Independence transfers back to the corresponding original columns. If $r_k=\sum_i c_i r_{p_i}$, applying $T^{-1}$ gives $a_k=\sum_i c_i a_{p_i}$, so those original columns also span every original column. This proves the original-pivot-column basis procedure, not merely a rule to memorize.

For the three-row matrix with columns $(1,2,3)^T,(2,4,6)^T,(3,7,10)^T$, the original column space is the plane $z=x+y$. Its coefficient RREF has column space $z=0$. These are distinct rank-two planes. In contrast, the two-row matrix obtained by deleting the last row has full row rank two; both its original and reduced column spaces are the whole $\mathbb R^2$. The worked comparison at the end of the chapter proves both outcomes and shows the distinct planes explicitly.

## Why later pivot permutations move earlier multipliers

The equation $PA=LU$ is the invariant to preserve. At stage two, before collecting permutations, the actual elimination sequence is $G_2P_2G_1P_1A$. Insert $P_2^{-1}P_2$ between the first Gauss transform and the earlier permutation to obtain

$$G_2P_2G_1P_1A=G_2(P_2G_1P_2^{-1})(P_2P_1)A.$$

The earlier factor $P_1$ must remain in this equality. Omitting it would change which original equations the product represents. The collected permutation is chronological from right to left: applying $P_1$ and then $P_2$ gives $P_2P_1$.

For an earlier stage $k$, write $G_k=I-g_ke_k^T$, where $g_k$ is zero in coordinates one through $k$. A later active-row permutation $Q$ fixes those completed coordinates. In particular $e_k^TQ^{-1}=e_k^T$, and

$$QG_kQ^{-1}=I-(Qg_k)e_k^T.$$

The vector $Qg_k$ still vanishes in the first $k$ coordinates. Thus this conjugate is another lower Gauss transform at the same completed pivot coordinate; its stored multipliers have simply been permuted among later rows. This is the algebraic reason to exchange the already completed columns of $L$ when the active rows are swapped. The later unfilled entries and the prescribed unit diagonal are not exchanged wholesale.

The restriction to later active rows is essential. With $G=\begin{bmatrix}1&0\\2&1\end{bmatrix}$ and $Q=\begin{bmatrix}0&1\\1&0\end{bmatrix}$, direct multiplication gives $QGQ^{-1}=\begin{bmatrix}1&2\\0&1\end{bmatrix}$. This arbitrary swap moved the completed pivot coordinate and turned a lower transform into an upper one. Consequently an unrestricted assertion about all row swaps would not justify LU bookkeeping. The actual pivoting algorithm has the stronger support invariant needed by the proof.

## A complete examination decision sequence

**First decide what is being solved.** Record the coefficient field, the unknown count and whether the last column or columns are loads. A parameter is fixed during each individual solve; integer, nonnegative or minimum-norm requirements are additional restrictions, not alternative meanings of a coefficient pivot.

**Then establish compatibility.** A transformed row with zero coefficients and nonzero load ends the problem as inconsistent. A pivot in every coefficient column alone is not enough: the augmented RREF $\begin{bmatrix}1&0\\0&1\end{bmatrix}$ interpreted as one coefficient column and one load says $x=0$ and $0=1$. A unique loaded solution requires both consistency and coefficient rank equal to the number of unknowns.

**If compatible, describe every solution.** Derive $x_p$ and an independent basis of homogeneous directions. Verify $Ax_p=b$, verify each $Av_i=0$, and show every solution has the displayed free-coordinate values. One valid point proves existence but not uniqueness; several valid points do not establish a complete family.

**For parameters, track every division domain.** Identify all roots of every prospective pivot factor, classify the generic branch only where the factors are nonzero, and substitute each exceptional value into the last undivided system. A cancelled expression may select one point from an exceptional family or may fail a retained equation entirely.

**For factorizations, declare the convention and verify the product.** In $PA=LU$, use $Ly=Pb$ and then $Ux=y$. Preserve previously stored multipliers under later pivot swaps. A first-column proportionality argument is a necessary test for an unrestricted LU option; construct or verify factors to prove the selected option is attainable.

**Finally apply the model-specific checks.** For integer counts, eliminate shared sums and count actual allowed lattice points. For a finite field, use its legal inverses and count $q^{n-r}$ only after compatibility. For rounded computation, state the precision and operation policy, calculate the original-system residual, and distinguish it from forward error. These decisions lead into the eighty detailed rules below; each rule states its hypotheses and the inference it supports.
