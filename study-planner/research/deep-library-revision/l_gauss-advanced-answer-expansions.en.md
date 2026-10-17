# Gaussian elimination: advanced worked-answer revision

This bounded manuscript replaces the teaching solutions for LG26–LG69. It preserves the bank's exact question statements, identifiers, titles, difficulty labels and provenance. The derivations below are independent explanatory expansions; they do not assert a fresh review of the cited university course materials. Mathematical checks and their limits are recorded separately. These are author-review drafts, not a declaration that the whole chapter has completed its final review.

## LG26

**Title.** Invalid replacement that silently removes information

**Question.** A student replaces the pair $x+y=1$, $x-y=3$ by two copies of their sum $2x=4$. Explain the error and compute the extra solutions introduced.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Establish the original solution.** Adding the equations gives $2x=4$, hence $x=2$. Subtracting the second equation from the first gives $2y=-2$, hence $y=-1$. Substitution verifies $2+(-1)=1$ and $2-(-1)=3$. Since both coordinates were forced, the original solution set is the singleton $\{(2,-1)\}$.

**2. Identify exactly what the proposed operation preserves.** Writing the original system as $Au=b$, the replacement applies

$$E=\begin{bmatrix}1&1\\1&1\end{bmatrix},\qquad EA=\begin{bmatrix}2&0\\2&0\end{bmatrix},\qquad Eb=\begin{bmatrix}4\\4\end{bmatrix}.$$

Every old solution still satisfies the new equations, because multiplying an equality by any matrix preserves equality. The converse fails: $E(1,-1)^T=0$, so $E$ has a nonzero kernel and no inverse. Information in the difference of the old equations has disappeared.

**3. Determine all extra points.** The replacement requires only $x=2$, with unrestricted real $y$. Its solution set is $\{(2,t):t\in\mathbb R\}$. The extra points are exactly those with $t\ne-1$. For example, $(2,0)$ satisfies both replacement equations but violates both original equations. A valid addition would replace only one row and retain the other; its triangular transformation has determinant one. The examination decision is therefore about reversibility of the entire operation, not whether each new equation is a legitimate consequence of the old ones.

## LG27

**Title.** Right-side synchronization is mandatory

**Question.** A student reduces $A=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$ to $\begin{bmatrix}1&1\\0&-2\end{bmatrix}$ but leaves $b=(3,1)^T$ unchanged. Compare the resulting answer with the true solution.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Apply the operation to the complete row.** The lower coefficient row changes from $(1,-1)$ to $(1,-1)-(1,1)=(0,-2)$. Consequently its load must change from $1$ to $1-3=-2$:

$$\begin{bmatrix}1&1&3\\1&-1&1\end{bmatrix}\longrightarrow\begin{bmatrix}1&1&3\\0&-2&-2\end{bmatrix}.$$

The second row gives $y=1$, and the first then gives $x=2$. These satisfy $x+y=3$ and $x-y=1$ exactly. The nonzero pivots $1,-2$ also prove uniqueness.

**2. Follow the student's actual corrupted system.** If the unchanged load is retained, the lower equation is $-2y=1$, so $y=-1/2$. The first equation gives $x=3+1/2=7/2$. In the original equations this point produces $3$ and $4$, rather than the required $3$ and $1$.

**3. Locate the structural failure.** The elementary matrix is $E=\begin{bmatrix}1&0\\-1&1\end{bmatrix}$. Correct equivalence is $EAu=Eb$, whereas the student solves $EAu=b$. Multiplying the latter by $E^{-1}$ yields $Au=E^{-1}b=(3,4)^T$, a different load. The residual of the wrong point in the original system is $(0,-3)^T$. An original-system residual therefore detects the fault even though the altered triangular system is solved perfectly.

## LG28

**Title.** Elementary matrices and composition order

**Question.** First swap the two rows of $A$, then add three times its new first row to its second. Find the left transformation and its inverse.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Encode each chronological operation.** Swapping the rows is left multiplication by $S=\begin{bmatrix}0&1\\1&0\end{bmatrix}$. Adding three times the new first row to the new second is left multiplication by $T=\begin{bmatrix}1&0\\3&1\end{bmatrix}$. After both actions the array is $T(SA)$, so

$$E=TS=\begin{bmatrix}0&1\\1&3\end{bmatrix}.$$

On a generic pair of old rows $(r_1,r_2)$ this produces $(r_2,r_1+3r_2)$, which independently checks the product order.

**2. Undo the actions.** First subtract three times the current first row from its second; then swap the rows. Therefore

$$E^{-1}=S^{-1}T^{-1}=\begin{bmatrix}0&1\\1&0\end{bmatrix}\begin{bmatrix}1&0\\-3&1\end{bmatrix}=\begin{bmatrix}-3&1\\1&0\end{bmatrix}.$$

Direct multiplication gives $EE^{-1}=\begin{bmatrix}1&0\\0&1\end{bmatrix}$: its second row is $(-3+3,1)=(0,1)$. The reverse product gives the same identity. Also $\det E=-1$, consistent with one swap and a determinant-preserving row addition. The matrix acting first stands closest to $A$; inverse operations reverse chronological order. Keeping the old product order when inverting generally fails because $S$ and $T$ do not commute.

## LG29

**Title.** Row operation versus column operation

**Question.** Let $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$ and $b=(5,11)^T$. Swap coefficient columns, solve for a vector $y$, and recover the original vector $x$.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Name the changed coordinates.** Swapping the coefficient columns is right multiplication by $Q=\begin{bmatrix}0&1\\1&0\end{bmatrix}$. The transformed equation is $AQy=b$, with

$$AQ=\begin{bmatrix}2&1\\4&3\end{bmatrix}.$$

Thus $2y_1+y_2=5$ and $4y_1+3y_2=11$. Subtract twice the first equation from the second to obtain $y_2=1$; then $y_1=2$. Both transformed equations are verified by $(2,1)^T$.

**2. Recover the requested variables.** The substitution that makes the new system equivalent is $x=Qy$. Consequently $x=(1,2)^T$, not $(2,1)^T$. Indeed $Ax=(1+4,3+8)^T=(5,11)^T$. Returning $y$ without recovery would give $Ay=(4,10)^T$, which fails both loads.

**3. Distinguish left and right actions.** An invertible row operation changes equation combinations and acts on both $A$ and $b$, leaving $x$ fixed. A coefficient-column permutation changes the coordinate labels and acts on $A$ on the right, leaving $b$ fixed but requiring $x=Qy$. Here $Q^{-1}=Q$, which makes recovery especially simple; for a general permutation the defining substitution, rather than an assumption of symmetry, determines the correct direction.

## LG30

**Title.** Column addition needs a coordinate map

**Question.** For $A=\begin{bmatrix}1&2\\0&1\end{bmatrix}$, replace column two by column two minus twice column one. If the load is $(5,2)^T$, solve correctly.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Derive the right transformation from its columns.** Keeping column one and replacing column two by column two minus twice column one means

$$Q=\begin{bmatrix}1&-2\\0&1\end{bmatrix},\qquad AQ=\begin{bmatrix}1&0\\0&1\end{bmatrix}.$$

The second column of $Q$ contains the coefficients $(-2,1)$ of the new column, which is a direct way to avoid putting the minus two in the wrong position.

**2. Solve in the new coordinates and recover.** The transformed system is $Iy=b$, so $y=(5,2)^T$. The original vector is

$$x=Qy=\begin{bmatrix}5-2(2)\\2\end{bmatrix}=\begin{bmatrix}1\\2\end{bmatrix}.$$

Substitution gives $x_1+2x_2=1+4=5$ and $x_2=2$. Since $Q$ is invertible and the new coefficient matrix is the identity, this is the unique original solution.

**3. Verify the meaning of the map.** Here $x_1=y_1-2y_2$ and $x_2=y_2$, or conversely $y_1=x_1+2x_2$ and $y_2=x_2$. Thus $(5,2)$ is an equation-adapted coordinate vector, not the original answer. Although $Q=A^{-1}$ happens to hold in this example, the general column-operation principle is the substitution $x=Qy$. A coefficient-column operation must not silently include the augmented load as though it were another unknown coordinate.

## LG31

**Title.** An exact inverse from synchronized right sides

**Question.** Compute the inverse of $A=\begin{bmatrix}2&1\\1&1\end{bmatrix}$ using row reduction and certify it.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Keep a full operation trace.** Reduce the two identity loads simultaneously:

$$\begin{bmatrix}2&1&1&0\\1&1&0&1\end{bmatrix}\longrightarrow\begin{bmatrix}1&1&0&1\\2&1&1&0\end{bmatrix}\longrightarrow\begin{bmatrix}1&1&0&1\\0&-1&1&-2\end{bmatrix}.$$

The actions are a swap followed by $R_2\leftarrow R_2-2R_1$. Next multiply row two by $-1$ and subtract the resulting row two from row one:

$$\begin{bmatrix}1&1&0&1\\0&1&-1&2\end{bmatrix}\longrightarrow\begin{bmatrix}1&0&1&-1\\0&1&-1&2\end{bmatrix}.$$

Thus the right block is $B=\begin{bmatrix}1&-1\\-1&2\end{bmatrix}$.

**2. Certify both multiplication directions.** The rows of $AB$ are $(2-1,-2+2)=(1,0)$ and $(1-1,-1+2)=(0,1)$. The rows of $BA$ are $(2-1,1-1)=(1,0)$ and $(-2+2,-1+2)=(0,1)$. Therefore $AB=BA=I_2$.

**3. Explain why the method works.** If $T$ is the composite row transformation, reducing $[A\mid I]$ produces $[TA\mid T]$. The final left identity says $TA=I$, so in the square case $T=A^{-1}$. Each column of $B$ is the solution of one standard-basis load, and $\det A=1\ne0$ independently confirms that such a universal inverse exists.

## LG32

**Title.** A singular inverse attempt is informative

**Question.** Explain the result of reducing $[A\mid I]$ for $A=\begin{bmatrix}1&2\\2&4\end{bmatrix}$.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Perform a legal reduction without pretending to obtain an inverse.** The operation $R_2\leftarrow R_2-2R_1$ gives

$$\begin{bmatrix}1&2&1&0\\2&4&0&1\end{bmatrix}\longrightarrow\begin{bmatrix}1&2&1&0\\0&0&-2&1\end{bmatrix}.$$

The coefficient block has only one pivot. Its rank cannot increase under further invertible row operations, so it cannot become $I_2$.

**2. Interpret the surviving right block correctly.** It is $T=\begin{bmatrix}1&0\\-2&1\end{bmatrix}$, an invertible operation matrix with determinant one. Its product with $A$ is $\begin{bmatrix}1&2\\0&0\end{bmatrix}$, not the identity. Being invertible itself does not make $T$ an inverse of a different matrix.

**3. Extract useful information for any load.** Applying the same operation to $(b_1,b_2)^T$ gives $(b_1,b_2-2b_1)^T$. Compatibility is exactly $b_2=2b_1$. If this holds, all solutions are $(b_1-2t,t)^T$; if it fails, the last equation is $0=b_2-2b_1\ne0$ and no solution exists. The row $(-2,1)$ is a left-null certificate: it annihilates $A$ but not an incompatible $b$. For example, the load $e_1$ is impossible because its second compatibility expression equals $-2$. This explains why no matrix could solve every load by multiplying it by a universal inverse.

## LG33

**Title.** A rectangular left inverse without an identity on every row

**Question.** Find a left inverse for $A=\begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix}$. Explain why it is not a two-sided inverse.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Construct a left inverse and multiply it out.** Let

$$B=\begin{bmatrix}1&0&0\\0&1&0\end{bmatrix}.$$

It selects the first two rows of $A$, so $BA=I_2$. However,

$$AB=\begin{bmatrix}1&0&0\\0&1&0\\1&1&0\end{bmatrix}\ne I_3.$$

The obstruction is structural: a $3$ by $2$ matrix has rank at most two, so its product with a $2$ by $3$ matrix cannot have rank three.

**2. State exactly what a compatible solve requires.** For a load $c=(c_1,c_2,c_3)^T$, the first two equations force $x=(c_1,c_2)^T$. The third equation then holds exactly when $c_3=c_1+c_2$. On that compatible plane, $Bc$ recovers the unique solution. Outside that plane $Bc$ is merely a candidate and fails the third equation.

**3. Exhibit nonuniqueness explicitly.** Let $w^T=(-1,-1,1)$, so $w^TA=0$. For arbitrary real $s,t$, define $B_{s,t}=B+(s,t)^T w^T$. Then $B_{s,t}A=BA+(s,t)^T0=I_2$. These are all left inverses: the difference of any two must have rows in the one-dimensional left kernel spanned by $w^T$. They agree on compatible loads because $w^Tc=0$, but need not agree elsewhere. A rectangular left inverse therefore means injectivity of the coefficient map, not surjectivity onto every possible load.

## LG34

**Title.** Doolittle factors from elimination multipliers

**Question.** Compute $A=LU$ with unit diagonal $L$ for $A=\begin{bmatrix}2&1&1\\4&-6&0\\-2&7&2\end{bmatrix}$, then solve $Ax=(5,-2,9)^T$.

**Provenance.** Course-derived task: Stanford CME108/MATH114, Gaussian elimination and LU examples

**Difficulty.** Hard

### Teaching solution

**1. Calculate the multipliers from the current array.** The first pivot is two. Thus $l_{21}=4/2=2$ and $l_{31}=-2/2=-1$. Updating the lower rows gives $(0,-8,-2)$ and $(0,8,3)$. The second multiplier is therefore $l_{32}=8/(-8)=-1$, not a ratio taken from the original second column. Subtracting this multiple of row two gives the last row $(0,0,1)$.

Consequently

$$L=\begin{bmatrix}1&0&0\\2&1&0\\-1&-1&1\end{bmatrix},\qquad U=\begin{bmatrix}2&1&1\\0&-8&-2\\0&0&1\end{bmatrix}.$$

**2. Verify the factorization row by row.** Row two of $LU$ is twice row one of $U$ plus row two of $U$, namely $(4,-6,0)$. Row three is minus row one minus row two plus row three, namely $(-2,7,2)$. The first row is already correct, so $LU=A$.

**3. Solve the two triangular systems.** From $Ly=b$, obtain $y_1=5$, $2(5)+y_2=-2$, and $-5-(-12)+y_3=9$. Thus $y=(5,-12,2)^T$. Backward substitution gives $x_3=2$, $-8x_2-4=-12$, and $2x_1+1+2=5$, so $x=(1,1,2)^T$. Original substitution yields $(5,-2,9)^T$. The nonzero pivots $2,-8,1$ prove uniqueness; the reusable factors depend only on $A$, whereas these intermediate and final vectors depend on the load.

## LG35

**Title.** Invertibility does not guarantee unpivoted LU

**Question.** Prove that $A=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ has no factorization $A=LU$ with lower triangular $L$ and upper triangular $U$, and give a pivoted factorization.

**Provenance.** Course-derived task: Stanford CME108/MATH114, Permuted LU, initial example

**Difficulty.** Hard

### Teaching solution

**1. Show that the matrix itself is nonsingular.** Its determinant is $-1$, and $A^2=I_2$. A zero first pivot in this ordering is therefore not evidence of singularity.

**2. Prove impossibility of the requested unpivoted form.** Suppose $A=LU$ with both factors triangular. Since $A$ is nonsingular, neither factor can be singular: $\det A=(\det L)(\det U)\ne0$. Hence their diagonal entries are nonzero. In particular,

$$L=\begin{bmatrix}l_{11}&0\\l_{21}&l_{22}\end{bmatrix},\qquad U=\begin{bmatrix}u_{11}&u_{12}\\0&u_{22}\end{bmatrix}$$

would give $(LU)_{11}=l_{11}u_{11}\ne0$, contradicting $a_{11}=0$. This rules out even unrestricted nonsingular triangular factors, not just unit-diagonal Doolittle factors.

**3. Repair the ordering.** Choose $P=\begin{bmatrix}0&1\\1&0\end{bmatrix}=A$. Then $PA=I_2$, so the pivoted factorization is $PA=LU$ with $L=U=I_2$. For a load $b$, the solve is simply $x=Pb$, which also follows from $A^{-1}=A$. The key examination distinction is between an invertible linear map and the legality of one particular elimination order. Row pivoting changes the order of equations and removes this obstruction without changing the original unknown vector.

## LG36

**Title.** A later row swap must move earlier multipliers

**Question.** Compute partial-pivot factors of $A=\begin{bmatrix}4&2&0\\2&1&1\\1&3&1\end{bmatrix}$. Explain the second-stage swap.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Carry out stage one.** The largest first-column magnitude is four. The multipliers are $1/2$ and $1/4$, so the working upper array becomes

$$\begin{bmatrix}4&2&0\\0&0&1\\0&5/2&1\end{bmatrix}.$$

The second pivot candidate is zero; partial pivoting exchanges its row with the last row, whose active entry is $5/2$.

**2. Carry old multiplier information with its equation.** Before the swap, the second row originated from original row two minus $1/2$ of original row one. After the swap that row occupies position three. Therefore the old multiplier $1/2$ must move to $l_{31}$, and $1/4$ must move to $l_{21}$. The second-stage multiplier is now zero. This yields

$$P=\begin{bmatrix}1&0&0\\0&0&1\\0&1&0\end{bmatrix},\quad L=\begin{bmatrix}1&0&0\\1/4&1&0\\1/2&0&1\end{bmatrix},\quad U=\begin{bmatrix}4&2&0\\0&5/2&1\\0&0&1\end{bmatrix}.$$

**3. Certify the complete result.** Row two of $LU$ is $(1,1/2,0)+(0,5/2,1)=(1,3,1)$, which is original row three. Row three is $(2,1,0)+(0,0,1)=(2,1,1)$, which is original row two. Thus $LU=PA$. Keeping the old multipliers would instead produce row two $(2,7/2,1)$ and row three $(1,1/2,1)$, immediately falsifying the identity. At stage $k$, exchange only the already stored columns $1$ through $k-1$ of $L$; exchanging complete rows of $L$ would also move its structural unit diagonal incorrectly.

## LG37

**Title.** Permutation orientation matters

**Question.** If software returns $A=P_0LU$, explain the load transformation required to solve $Ax=b$ and compare with the convention $PA=LU$.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Derive the load transformation from the supplied identity.** If $A=P_0LU$, then $Ax=b$ means $P_0LUx=b$. A permutation matrix satisfies $P_0^{-1}=P_0^T$, so premultiplication gives

$$LUx=P_0^Tb.$$

The correct two-stage solve is $Ly=P_0^Tb$, followed by $Ux=y$. In the alternative convention $PA=LU$, premultiplication of $Ax=b$ by $P$ gives $LUx=Pb$. These statements coincide when $P=P_0^T$.

**2. Use a nonsymmetric example to expose the direction.** Take

$$P_0=\begin{bmatrix}0&1&0\\0&0&1\\1&0&0\end{bmatrix},\qquad L=U=I_3,\qquad b=(1,2,3)^T.$$

Then $P_0^Tb=(3,1,2)^T$, and $A(3,1,2)^T=(1,2,3)^T$ as required. Using $P_0b=(2,3,1)^T$ instead gives $A(2,3,1)^T=(3,1,2)^T$, the wrong load.

**3. Explain the common misleading test.** A single row exchange has $P_0=P_0^T$, so either formula appears to work in a two-row demonstration. A three-cycle has distinct inverse and forward permutations and therefore detects the mistake. Before substituting a software permutation into a remembered solve formula, verify whether its documented identity places the permutation on the left of $A$ or on the right side of the equality.

## LG38

**Title.** Scaling makes an unrestricted LU nonunique

**Question.** If $A=LU$ and $D$ is any invertible diagonal matrix, construct another triangular factorization. Why does unit diagonal resolve the ambiguity for nonsingular factors?

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Produce an entire family of factorizations.** For invertible diagonal $D$, insert $DD^{-1}$ between the factors:

$$A=LU=(LD)(D^{-1}U).$$

Multiplying $L$ on the right scales its columns and keeps it lower triangular. Multiplying $U$ on the left scales its rows and keeps it upper triangular. The column scaling and reciprocal row scaling cancel in their product. For example, a diagonal entry $d_i=2$ doubles column $i$ of $L$ and halves row $i$ of $U$.

**2. Prove uniqueness under the stated nonsingular normalization.** Suppose $L_1U_1=L_2U_2$, with both lower factors unit diagonal and all factors nonsingular. Rearrangement gives

$$L_2^{-1}L_1=U_2U_1^{-1}.$$

The left side is unit lower triangular; the right side is upper triangular. A matrix simultaneously lower and upper triangular is diagonal. Its diagonal must also be all ones, so both sides equal the identity. Hence $L_1=L_2$ and then $U_1=U_2$.

**3. Retain the hypotheses.** Under the diagonal-rescaling construction, $LD$ has diagonal $d_i$ because $L$ is unit diagonal, so it remains unit diagonal only when $D=I$. The uniqueness proof additionally uses inverse factors; it must not be copied unchanged to a singular factorization. Existence in a fixed ordering is also a separate issue: normalization cannot create a nonzero pivot where the chosen elimination order has none.

## LG39

**Title.** Leading principal minors and pivot existence

**Question.** For a nonsingular square $A$, prove that nonzero leading principal minors are equivalent to existence of Doolittle elimination without row swaps and nonzero pivots.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Prove necessity using leading blocks.** Let $A=LU$ with unit lower $L$ and nonzero diagonal of $U$. For each leading $k$ by $k$ block, triangular zero patterns ensure $A_k=L_kU_k$. No contributions from indices larger than $k$ enter these entries. Therefore

$$\Delta_k=\det A_k=\det L_k\det U_k=\prod_{i=1}^{k}u_{ii}\ne0.$$

**2. Prove sufficiency by induction, retaining the updated problem.** The first determinant gives $a_{11}\ne0$. Partition $A=\begin{bmatrix}a&r\\c&D\end{bmatrix}$ and eliminate the first column. The lower block is $S=D-ca^{-1}r$. For every leading $j$ by $j$ block of $S$, the corresponding block determinant identity is

$$\Delta_{j+1}=a\det S_j.$$

Because $a\ne0$ and all $\Delta_{j+1}$ are nonzero, every leading principal determinant of $S$ is nonzero. The induction hypothesis supplies a legal nonzero-pivot Doolittle factorization of $S$. Combining those elimination steps with the first-column multipliers supplies the factors for $A$.

**3. Identify the exact scope.** The criterion concerns nonsingular square matrices in a fixed row and column order. It implies $u_{kk}=\Delta_k/\Delta_{k-1}$ with $\Delta_0=1$. It is not a claim that every nonsingular matrix admits this unpivoted ordering: the row-exchange matrix has $\Delta_1=0$. Nor does failure of the criterion rule out every singular LU factorization; a diagonal matrix with a zero final entry already provides a singular triangular factorization with a zero pivot.

## LG40

**Title.** The final pivot is a determinant ratio

**Question.** A nonsingular three by three matrix has leading principal determinants $\Delta_1=2$, $\Delta_2=-6$, $\Delta_3=24$. Find the unpivoted Doolittle pivots.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Convert determinant products into individual pivots.** For unit-lower Doolittle factors in the original unpermuted ordering,

$$\Delta_1=u_{11},\qquad \Delta_2=u_{11}u_{22},\qquad \Delta_3=u_{11}u_{22}u_{33}.$$

Thus $u_{11}=2$, $u_{22}=(-6)/2=-3$, and $u_{33}=24/(-6)=-4$. Each divisor is nonzero, as required by the nonzero-pivot criterion.

**2. Verify every available invariant.** The first pivot reproduces $\Delta_1=2$. The first two reproduce $2(-3)=-6$. All three reproduce $2(-3)(-4)=24$. This is stronger than checking the final determinant alone: many incorrect triples have the same total product but the wrong intermediate leading-block determinant.

**3. Explain what the data do not determine.** These minors determine the diagonal pivots but not the off-diagonal entries of $L$ or $U$, so they do not determine the complete matrix. The diagonal example $\operatorname{diag}(2,-3,-4)$ is one realization. The ratio rule applies to the declared original ordering with no row swaps. If a question inserts row permutations, the appropriate leading minors are those of the permuted coefficient matrix; a final determinant sign correction does not repair every intermediate original-minor ratio. A zero denominator would require a new branch or a different order rather than division by zero.

## LG41

**Title.** Schur complement as the lower subsystem

**Question.** Eliminate $x$ from $2x+y+z=1$, $4x+3y-z=2$, $-2x+y+2z=0$ and solve the resulting two by two system.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Eliminate the first unknown without changing the equation set.** The pivot two is nonzero. Apply $R_2\leftarrow R_2-2R_1$ and $R_3\leftarrow R_3+R_1$ to obtain

$$y-3z=0,\qquad 2y+3z=1.$$

The coefficient and load updates are equally necessary: the lower loads become $2-2(1)=0$ and $0+1=1$.

**2. Solve the lower subsystem and recover.** The first lower equation gives $y=3z$. Substitution in the second gives $6z+3z=1$, so $z=1/9$ and $y=1/3$. The original first equation then yields

$$x=\frac{1-y-z}{2}=\frac{1-1/3-1/9}{2}=\frac5{18}.$$

All original equations check: $2x+y+z=5/9+3/9+1/9=1$, $4x+3y-z=10/9+1-1/9=2$, and $-2x+y+2z=-5/9+3/9+2/9=0$.

**3. Read the Schur complement explicitly.** With first scalar pivot $a=2$, row $r=(1,1)$, column $c=(4,-2)^T$, lower block $D=\begin{bmatrix}3&-1\\1&2\end{bmatrix}$, and lower load $d=(2,0)^T$, the new block is $D-ca^{-1}r=\begin{bmatrix}1&-3\\2&3\end{bmatrix}$ and the new load is $d-ca^{-1}(1)=(0,1)^T$. Its determinant is nine, so this subsystem and hence the whole system have unique solutions.

## LG42

**Title.** Reusable factors for two loads

**Question.** Use $L=\begin{bmatrix}1&0\\2&1\end{bmatrix}$ and $U=\begin{bmatrix}3&1\\0&2\end{bmatrix}$ to solve loads $b^{(1)}=(4,10)^T$ and $b^{(2)}=(1,0)^T$.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Recover the common coefficient matrix.** Multiplication gives

$$A=LU=\begin{bmatrix}3&1\\6&4\end{bmatrix}.$$

For any load $(b_1,b_2)^T$, forward substitution through unit-lower $L$ gives $y_1=b_1$ and $y_2=b_2-2b_1$. Backward substitution through $U$ then gives $x_2=y_2/2$ and $x_1=(y_1-x_2)/3$. The nonzero upper diagonal $3,2$ guarantees a unique result for each load.

**2. Apply the same formulas to both loads.** For $(4,10)^T$, $y=(4,2)^T$, so $x_2=1$ and $x_1=(4-1)/3=1$. For $(1,0)^T$, $y=(1,-2)^T$, so $x_2=-1$ and $x_1=(1+1)/3=2/3$.

**3. Verify independently in the original matrix.** The first vector gives $(3+1,6+4)^T=(4,10)^T$. The second gives $(2-1,4-4)^T=(1,0)^T$. Equivalently, the two intermediate vectors can be solved as the columns of a load block, but each column must receive all the same coefficient-row operations. The factors are reused because only the loads changed; the intermediate vector $y$ is not reusable across different loads. Constructing an inverse would solve every standard-basis load even though only these two particular solves were requested.

## LG43

**Title.** Exact backward-substitution work

**Question.** Count scalar multiplications, subtractions and divisions in straightforward backward substitution for a dense nonsingular upper triangular $n$ by $n$ matrix.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Specify the loop being counted.** In row $i$, initialize a running value at $b_i$ and for $j=i+1,\ldots,n$ perform $s\leftarrow s-u_{ij}x_j$. Then compute $x_i=s/u_{ii}$. Each visited off-diagonal entry therefore contributes one multiplication and one subtraction, including the first subtraction from $b_i$. Each row contributes one division because its diagonal is nonzero.

**2. Sum the operations.** Row $i$ has $n-i$ visited entries, so

$$M=S=\sum_{i=1}^{n}(n-i)=\frac{n(n-1)}2,\qquad D=n.$$

Counting each scalar operation once gives $M+S+D=n(n-1)+n=n^2$. For $n=3$, the rows use respectively two, one and zero products and subtractions, hence three of each and three divisions: nine operations. For $n=1$, only one division remains, agreeing with the formula.

**3. State the boundaries of the count.** This is arithmetic work for a dense straightforward solve, excluding indexing, comparisons and memory operations. It assumes the implementation does not exploit accidental zeros or unit diagonal entries. A fused multiply-add instruction could combine a product and subtraction under a different convention; precomputed reciprocal multiplication also changes the classification. The asymptotic cost remains quadratic, but exact formulas are meaningful only after naming the operations that count and the loop actually executed.

## LG44

**Title.** Factorization operation count from the loops

**Question.** For unpivoted dense elimination, count divisions, multiplications and subtractions needed to factor a square coefficient matrix when known pivot-column zeros are assigned directly.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Count a single stage from the executed updates.** At pivot stage $k$, there are $n-k$ rows below the pivot. Each multiplier requires one division. For each such row the trailing columns $k+1,\ldots,n$ contribute $n-k$ updates, each consisting of one multiplication and one subtraction. The known pivot-column zero is assigned directly rather than recomputed arithmetically.

**2. Sum over all stages.** Setting $j=n-k$ gives

$$D=\sum_{j=1}^{n-1}j=\frac{n(n-1)}2,\qquad M=S=\sum_{j=1}^{n-1}j^2=\frac{(n-1)n(2n-1)}6.$$

Thus

$$D+M+S=\frac{n(n-1)}2+\frac{(n-1)n(2n-1)}3=\frac23n^3-\frac12n^2-\frac16n.$$

For $n=3$, the multiplier counts are two and one, while the trailing-update counts are four and one. The total is $3+5+5=13$, agreeing with the formula.

**3. Separate factorization from solves and input models.** Updating one appended load would add $\sum_{j=1}^{n-1}j$ products and the same number of subtractions, but these are excluded from the stated coefficient-only count. Pivot searches, swaps, loop overhead and storage are also excluded. For $n=1$ the formula gives zero factorization operations, correctly reflecting that no elimination stage is needed; solving a load still requires a division. Exact rational arithmetic obeys the same loop count, but growing numerator and denominator lengths prevent this scalar-operation formula from being a bit-complexity bound.

## LG45

**Title.** A tiny pivot under declared rounding

**Question.** Solve $10^{-4}x+y=1$, $x+y=2$ exactly. Then show unpivoted elimination with rounding to three significant decimal digits after every scalar operation can fail.

**Provenance.** Course-derived task: Stanford CME108/MATH114, Permuted LU, rounding example

**Difficulty.** Hard

### Teaching solution

**1. Obtain a reference answer in exact arithmetic.** Subtract the first equation from the second to get $(1-10^{-4})x=1$. Therefore $x=10000/9999$ and $y=2-x=9998/9999$. These values satisfy both original equations exactly.

**2. Follow the declared unpivoted arithmetic operation by operation.** Let each scalar result be rounded to three significant decimal digits. The multiplier is $1/(10^{-4})=10000$. The lower coefficient is rounded from $1-10000=-9999$ to $-10000$, and its load from $2-10000=-9998$ to $-10000$. Division gives $\widehat y=1$. In the first equation, the product $1\widehat y=1$, subtraction $1-1=0$, and division by $10^{-4}$ give $\widehat x=0$. The resulting vector $(0,1)$ has original residual $(0,1)^T$, so the second equation is badly violated.

**3. Repeat after the row exchange.** The first pivot is now one and the multiplier is $10^{-4}$. The lower coefficient $1-10^{-4}=0.9999$ rounds to $1.00$ and the lower load $1-2(10^{-4})=0.9998$ also rounds to $1.00$. Hence $\widehat y=1$ and the first equation $x+y=2$ gives $\widehat x=1$. The residual is now $(-10^{-4},0)^T$, and the infinity-norm forward error is only $1/9999$. The unpivoted error is $10000/9999$. This example distinguishes an exact answer from a particular rounded computation; it does not claim these rounded outputs for unrestricted binary double precision.

## LG46

**Title.** Small residual does not imply small forward error

**Question.** For $A=\begin{bmatrix}1&1\\1&1+\varepsilon\end{bmatrix}$, $b=(2,2+\varepsilon)^T$, compare the exact solution with $\widehat x=(2,0)^T$, where $\varepsilon>0$ is small.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Determine the exact solution and uniqueness.** Subtract row one from row two to get $\varepsilon x_2=\varepsilon$. Since $\varepsilon>0$, $x_2=1$, and the first equation gives $x_1=1$. The determinant is $\varepsilon\ne0$, so this solution is unique.

**2. Compare forward error and residual.** For $\widehat x=(2,0)^T$,

$$e=\widehat x-x=(1,-1)^T,\qquad A\widehat x=(2,2)^T,\qquad r=b-A\widehat x=(0,\varepsilon)^T.$$

Thus ${\Vert e\Vert}_\infty=1$ while ${\Vert r\Vert}_\infty=\varepsilon$, which can be arbitrarily small. The direction $(1,-1)^T$ is mapped to $(0,-\varepsilon)^T$, explaining the compression directly.

**3. Compute the missing amplification factor.** The inverse is

$$A^{-1}=\frac1\varepsilon\begin{bmatrix}1+\varepsilon&-1\\-1&1\end{bmatrix}.$$

Its maximum absolute row sum is $(2+\varepsilon)/\varepsilon$. Also ${\Vert A\Vert}_\infty=2+\varepsilon$, so $\kappa_\infty(A)=(2+\varepsilon)^2/\varepsilon$. The identity $e=-A^{-1}r$ yields the valid bound ${\Vert e\Vert}_\infty\le{\Vert A^{-1}\Vert}_\infty{\Vert r\Vert}_\infty=2+\varepsilon$; it never promised a tiny error. Relative residual is $\varepsilon/(2+\varepsilon)$, whereas relative forward error is one. At $\varepsilon=0$, excluded by the question, the system is singular and $(2,0)^T$ is itself a valid solution; this boundary further shows why nonsingularity must be stated before using inverse-based bounds.

## LG47

**Title.** Pivoting is a stability strategy, not a rank theorem

**Question.** Does choosing the largest available coefficient pivot prove that every numerical rank decision is exact or that every computed solution is accurate? Give precise limits.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Separate the exact and numerical questions.** In exact arithmetic, a nonzero pivot permits reversible division regardless of its magnitude. For example, $\operatorname{diag}(1,10^{-12})$ has exact rank two. A rule declaring every magnitude below $10^{-10}$ to be zero would falsely report rank one. Conversely $10^{12}\operatorname{diag}(1,10^{-12})=\operatorname{diag}(10^{12},1)$ has the same exact rank and condition number but passes that absolute threshold. Therefore a universal absolute cutoff is not invariant even under uniform rescaling.

**2. Identify what partial pivoting actually proves.** Selecting a maximum-magnitude nonzero entry from the current active column gives $|l_{ik}|\le1$. It avoids dividing by an entry smaller than another available entry in that column. It neither gives a lower bound on the final pivot relative to data uncertainty nor bounds the system's inverse norm. The nearly dependent two-row matrix in LG46 remains ill-conditioned under a sensible pivot choice.

**3. Give an explicit growth counterexample.** For $A=\begin{bmatrix}1&-1\\1&1\end{bmatrix}$, a valid partial-pivot tie choice keeps the first row. The multiplier is one, but the trailing update is $1-1(-1)=2$, larger than every original entry in magnitude. Thus bounded multipliers are not bounded upper-array growth.

The practical decision requires declared precision, scaling, tolerance and data uncertainty, together with a residual and conditioning assessment. These can support a numerical rank estimate and an error bound under stated assumptions; the pivot-selection slogan alone cannot certify exact rank or universal accuracy.

## LG48

**Title.** Magnitude of multipliers under partial pivoting

**Question.** Prove $|l_{ik}|\le1$ after partial pivot selection, and explain why this does not bound every entry of $U$ by the largest original entry.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Prove the multiplier bound at the current stage.** After a partial-pivot exchange, let the active nonzero pivot be $a_{kk}^{(k)}$. Its selection means $|a_{ik}^{(k)}|\le|a_{kk}^{(k)}|$ for every $i>k$. Therefore

$$|l_{ik}|=\left|\frac{a_{ik}^{(k)}}{a_{kk}^{(k)}}\right|\le1.$$

The proof works with ordinary absolute value over the reals and modulus over the complex numbers. If every eligible entry is zero, no nonzero pivot exists in that column, so division is not performed.

**2. Analyze the different update quantity.** A trailing entry changes by

$$a_{ij}^{(k+1)}=a_{ij}^{(k)}-l_{ik}a_{kj}^{(k)}.$$

The triangle inequality only gives $|a_{ij}^{(k+1)}|\le|a_{ij}^{(k)}|+|a_{kj}^{(k)}|$, not a bound by the larger of those two magnitudes. Cancellation of signs can therefore become addition of magnitudes.

**3. Verify a concrete counterexample.** In $A=\begin{bmatrix}1&-1\\1&1\end{bmatrix}$, retain the first row in the tied pivot search. Then $l_{21}=1$ and $U=\begin{bmatrix}1&-1\\0&2\end{bmatrix}$. The multiplier obeys the theorem, but $\max|U_{ij}|/\max|A_{ij}|=2$. If the tied rows are exchanged instead, the final pivot is $-2$, with the same magnitude growth. All comparisons and quotients in the proof concern the transformed active column, not original entries. The examination conclusion is that the multiplier bound and an upper-entry growth bound are different propositions, and the latter does not follow from the former with constant one.

## LG49

**Title.** Binary-field elimination changes the arithmetic

**Question.** Over $\mathbb F_2$, solve $x+y=1$, $y+z=0$, $x+z=1$. Compare with the same equations over the reals.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Solve in the declared binary field.** In $\mathbb F_2$, $-1=1$ and $1+1=0$. The third equation is the sum of the first two: adding their left sides gives $x+2y+z=x+z$, and adding their loads gives one. Thus it contributes no independent restriction. Set $z=t\in\{0,1\}$. The second equation gives $y=t$, and the first gives $x=1+t$.

The two choices yield $(1,0,0)$ and $(0,1,1)$. For the latter, the first equation reads $0+1=1$, the second $1+1=0$, and the third $0+1=1$, all modulo two. Two independent pivots and one free binary coordinate prove these are all the solutions.

**2. Solve the same printed equations over the reals.** Now $y=-z$ and $x=1+z$. Substituting into the third equation gives $1+2z=1$, so $z=0$, $y=0$ and $x=1$. The coefficient determinant is two, nonzero over the reals but zero in characteristic two.

**3. Locate the field-dependent step.** Over the reals, division by two forces $z=0$; over $\mathbb F_2$, the equation $2z=0$ is the identity $0=0$ and supplies no restriction. The field changes the row dependence and rank, not just the notation of the final answer. A real-valued rational elimination simulator cannot establish the binary classification unless its arithmetic operations are actually replaced by modular ones.

## LG50

**Title.** A parameter family over a finite field

**Question.** Over $\mathbb F_5$, solve $x+2y=1$ and $2x+4y=2$. List all solutions.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Remove the dependent equation legally.** Over $\mathbb F_5$, subtract twice the first row from the second. Both its coefficient entries and its load become zero. Hence only $x+2y=1$ remains, with one pivot and one free coordinate.

**2. Enumerate the parameter with field arithmetic.** For $y=t$, $x=1-2t$ modulo five. The five choices are shown with the free coordinate in the first row and its corresponding first coordinate in the second row:

$$\begin{bmatrix}0&1&2&3&4\\1&4&2&0&3\end{bmatrix}.$$

Thus the complete list is $(1,0),(4,1),(2,2),(0,3),(3,4)$. Checking the first equation produces integer sums $1,6,6,6,11$, each congruent to one modulo five. The second equation is automatically twice the first and therefore has load two modulo five.

**3. Prove completeness and state the domain limit.** Every solution has some second coordinate $t$ among the five residues. Its first coordinate is then uniquely forced by the first equation, so no sixth solution is possible. The map from $t$ to the pair is injective because it retains $t$ as its second coordinate. This is the constructive reason for the count $5^{2-1}=5$. Although a free coordinate over the reals would produce infinitely many solutions, a free coordinate over a finite field has only finitely many choices. All nonzero residues in $\mathbb F_5$ are invertible; for example $2\cdot3=1$ modulo five. The corresponding field-division reasoning is not automatically valid for a composite modulus.

## LG51

**Title.** A rank change caused by field characteristic

**Question.** Compare the solutions of $x+y=0$, $x-y=0$ over $\mathbb R$ and over $\mathbb F_2$.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Work over the reals first.** Subtract the second equation from the first to get $2y=0$. Hence $y=0$ and then $x=0$. Equivalently the determinant of $\begin{bmatrix}1&1\\1&-1\end{bmatrix}$ is $-2$, nonzero in $\mathbb R$, so the unique solution is $(0,0)$.

**2. Reduce the coefficients in the binary field.** In $\mathbb F_2$, the coefficient $-1$ equals $1$. Thus both equations become $x+y=0$. One row subtracts to zero, leaving one pivot and one free coordinate. Setting $y=t$ gives $x=t$, and the complete solution list is $(0,0)$ and $(1,1)$.

**3. Verify the structural change.** The real full-rank matrix has rank two; its binary reduction has rank one. The determinant formula itself has not failed: $-2$ reduces to zero modulo two. What changes is whether that determinant is a nonzero field element. Likewise the real equation $2y=0$ forces $y=0$, whereas the binary version is $0=0$ for every $y$.

The examination decision must therefore identify the coefficient field before invoking a determinant, pivot division or free-coordinate count. The same integer symbols can represent different linear maps after changing fields. Over any field of characteristic other than two the determinant remains nonzero; characteristic two is precisely the exceptional case for this example.

## LG52

**Title.** An invariant for a correct in-place implementation

**Question.** Explain why an elimination implementation must save the old multiplier before overwriting its pivot-column entry with zero. Give a failing two by two example.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Preserve the pre-update multiplier.** In the given augmented array, the first pivot is two and the lower pivot-column entry is four. Store $f=4/2=2$ before changing either of those values. Updating the whole lower row gives

$$[4,3,7]-2[2,1,3]=[0,1,1].$$

Backward substitution then yields $y=1$ and $x=(3-1)/2=1$. Original substitution gives loads three and seven as required.

**2. Trace the faulty in-place ordering.** If the code first stores zero in the lower pivot-column entry and then reads it to compute the multiplier, it obtains $f=0/2=0$. Its trailing update subtracts nothing, leaving the corrupted lower row $[0,3,7]$. Solving this wrong array gives $y=7/3$ and $x=(3-7/3)/2=1/3$.

The resulting point satisfies the first original equation but gives $4(1/3)+3(7/3)=25/3$, not seven, in the second. Its original residual is $(0,-4/3)^T$.

**3. State an implementable invariant.** Save $f$ once, use the unchanged pivot row for every trailing coefficient and appended load update, and then assign the known pivot-column zero. An alternative may assign that zero earlier only after $f$ is already saved. At each completed update the array must equal an invertible row transform of the original augmented input. A triangular-looking output alone does not establish that invariant; this failure produces an apparently valid triangular array that represents a different problem.

## LG53

**Title.** A linear dependence among equations is a load test

**Question.** Rows satisfy $r_3=2r_1-r_2$. What condition on loads is necessary for consistency, and is it sufficient if the first two rows are independent?

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Derive necessity directly from a hypothetical solution.** If $x$ solves all three equations, then

$$b_3=r_3x=(2r_1-r_2)x=2b_1-b_2.$$

Thus $b_3-2b_1+b_2=0$ is a compatibility condition. The vector $(-2,1,1)^T$ is a left-null certificate: its transpose annihilates the three-row coefficient matrix. A nonzero product with the load disproves consistency immediately.

**2. Prove sufficiency under the independence hypothesis.** Put $R=\begin{bmatrix}r_1\\r_2\end{bmatrix}$. Independence of the two real rows means $\operatorname{rank}R=2$, so the map $x\mapsto Rx$ is onto $\mathbb R^2$. Consequently there exists an $x$ with $r_1x=b_1$ and $r_2x=b_2$ for every prescribed load pair. More constructively, $RR^T$ is invertible because $v^TRR^Tv={\Vert R^Tv\Vert}^2>0$ for nonzero $v\in\mathbb R^2$. Thus $x=R^T(RR^T)^{-1}(b_1,b_2)^T$ is one such vector. The compatibility equality then makes $r_3x=b_3$ automatic.

**3. Explain why independence matters.** If $r_1=r_2=[1]$, then $r_3=2r_1-r_2=[1]$. Loads $(0,1,-1)$ obey $b_3=2b_1-b_2$, yet the first two equations demand both $x=0$ and $x=1$. Additional row dependences create additional load tests. The stated equality is necessary in every case, but sufficient here only because the first two independent rows account for all remaining constraints.

## LG54

**Title.** A linear constraint after elimination

**Question.** The general solution is $x=(1,0,2)^T+s(1,1,0)^T+t(0,1,-1)^T$. Add the conditions $x_1-x_2=0$ and $x_2+x_3=4$ and solve.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Write the actual coordinates before substituting.** The given family is

$$x_1=1+s,\qquad x_2=s+t,\qquad x_3=2-t.$$

The first added condition becomes $1+s-(s+t)=0$, so $t=1$. The second becomes $(s+t)+(2-t)=4$, so $s=2$. Consequently the unique candidate is $x=(3,3,1)^T$.

**2. Verify membership and both restrictions.** Substituting $s=2,t=1$ into the original family gives $(1,0,2)+2(1,1,0)+(0,1,-1)=(3,3,1)$. The added loads are $3-3=0$ and $3+1=4$. Hence the point belongs to the original solution family and satisfies both new conditions.

**3. Prove uniqueness within the family.** In parameter order $(s,t)$, the restriction equations have coefficient matrix $\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ and right side $(-1,2)^T$. Its determinant is one, so the parameter pair is uniquely determined. The original two directions are also independent: their first coordinates force the first coefficient to zero in a zero combination, and their third coordinates force the second coefficient to zero. Therefore distinct parameter pairs would represent distinct points. Combining these facts proves the intersection contains exactly one point. Additional constraints can be solved in the lower-dimensional parameter space; there is no need to reconstruct and eliminate every original equation.

## LG55

**Title.** Row space is preserved; column space generally moves

**Question.** For $A=\begin{bmatrix}1&0\\1&0\end{bmatrix}$, apply $R_2\leftarrow R_2-R_1$. Compare row spaces, column spaces and kernels.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Compute the transformed matrix and operation.** With $E=\begin{bmatrix}1&0\\-1&1\end{bmatrix}$,

$$R=EA=\begin{bmatrix}1&0\\0&0\end{bmatrix}.$$

Since $E$ is invertible, each row of $R$ is a combination of rows of $A$ and the inverse relation gives the converse. Here both row spaces are explicitly $\operatorname{span}\{(1,0)\}$.

**2. Solve the two homogeneous systems.** Both $Au=0$ and $Ru=0$ require $u_1=0$ and leave $u_2$ arbitrary. Their common kernel is $\operatorname{span}\{(0,1)^T\}$. In general $EAu=0$ is equivalent to $Au=0$ by multiplication by $E^{-1}$.

**3. Compare column spaces as actual geometric sets.** The only nonzero original column is $(1,1)^T$, so $\operatorname{col}(A)=\{(t,t)^T:t\in\mathbb R\}$. The transformed column is $(1,0)^T$, so $\operatorname{col}(R)=\{(t,0)^T:t\in\mathbb R\}$. Both have dimension one but are distinct lines. Precisely, $\operatorname{col}(R)=E\operatorname{col}(A)$; invertibility preserves dimension, not pointwise location.

For example, the original load $(1,1)^T$ is compatible, but it must transform to $(1,0)^T$ when solving with $R$. Testing that unchanged load against $\operatorname{col}(R)$ would incorrectly reject it. This is the practical difference between preserving column rank and preserving the original column space.

## LG56

**Title.** Original pivot columns versus reduced pivot columns

**Question.** Reduce $A=\begin{bmatrix}1&2&3\\2&4&7\end{bmatrix}$ and identify a basis of its original column space.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Reduce the stated matrix and select original columns.** Subtracting twice row one from row two gives $R=\begin{bmatrix}1&2&3\\0&0&1\end{bmatrix}$. The pivot indices are one and three. Their original columns are $c_1=(1,2)^T$ and $c_3=(3,7)^T$, and $\det[c_1\ c_3]=7-6=1\ne0$. They are independent and span $\mathbb R^2$, so they are a basis of the original column space. Also $c_2=2c_1$, which identifies the redundant column directly.

**2. Avoid an incorrect general warning in this particular example.** Here both original and reduced matrices have full row rank, so both column spaces are the whole ambient $\mathbb R^2$. The reduced pivot columns $(1,0)^T$ and $(3,1)^T$ therefore also span that space. Claiming that the spaces differ in this example would be false.

**3. Show when selecting reduced columns would really be wrong.** For the illustrative extension $B=\begin{bmatrix}1&2&3\\2&4&7\\3&6&10\end{bmatrix}$, operations $R_2-2R_1$, $R_3-3R_1$, then $R_3-R_2$ give $S=\begin{bmatrix}1&2&3\\0&0&1\\0&0&0\end{bmatrix}$. Original columns satisfy $z=x+y$ and span that plane. Reduced columns span $z=0$. The witness $(1,0,0)^T$ belongs only to the latter; their intersection is $\{(t,-t,0)^T\}$. The pivot indices still select independent original columns because an invertible row transform preserves every column-dependence relation. Therefore transfer the indices, rather than assuming the transformed vectors always lie in the original space.

## LG57

**Title.** No equations and no variables are distinct boundaries

**Question.** Classify a system with zero equations and $n$ real unknowns. Then classify one with $m$ equations and zero unknowns.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Treat no equations as an empty set of restrictions.** When $m=0$, the coefficient map goes from $\mathbb R^n$ to the zero-dimensional space. Every vector satisfies all zero equations, so the solution set is $\mathbb R^n$. For $n\ge1$ it is infinite and has $n$ free real coordinates.

**2. Treat no unknowns as a different domain.** When $n=0$, the domain $\mathbb R^0$ contains exactly one vector, the empty tuple. There are no choices of coordinates to make. Every coefficient row has length zero, so its dot product with that tuple is the empty sum, equal to zero. The system is therefore consistent exactly when every supplied $b_i$ is zero. If so the unique solution is the empty tuple; otherwise there are no solutions.

**3. Reconcile the simultaneous boundary.** If $m=n=0$, there are no equations to fail and one possible variable vector, so there is exactly one solution. This is consistent with $\mathbb R^0$ having one element, not zero elements. It is also consistent with the parameter count $n-r=0$ and, over a finite field, the count $q^0=1$.

The common shortcut “no pivots means infinitely many solutions” is thus false without a positive number of real unknowns and a consistency check. These are mathematical boundary classifications; a particular software input interface may reject empty arrays even though the underlying linear-map statements remain well-defined.

## LG58

**Title.** An integer restriction requires more than real consistency

**Question.** The real system is $2x+y=1$ and $x-2y=0$. Does its unique real solution give an integer solution?

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Solve over a field before applying the integer restriction.** From the second equation, $x=2y$. Substituting in the first gives $2(2y)+y=1$, hence $5y=1$. Over $\mathbb Q$ or $\mathbb R$, this yields $(x,y)=(2/5,1/5)$.

**2. Establish that no other real point was missed.** The coefficient determinant is $2(-2)-1(1)=-5\ne0$, so the field solution is unique. Direct substitution gives $4/5+1/5=1$ and $2/5-2/5=0$.

**3. Decide the integer problem without rounding.** If $x,y$ were integers, the substitution $x=2y$ would still be valid and would require $5y=1$. Its left side is divisible by five and its right side is not, a contradiction. Equivalently, reducing this necessary equality modulo five gives $0=1$. Thus there is no integer solution. Rounding the real coordinates cannot repair this divisibility obstruction.

Elementary row additions and swaps with integer coefficients remain reversible over the integers, but division by an arbitrary nonzero integer is not an internal integer operation: five has no multiplicative inverse in $\mathbb Z$. Field rank and pivot information classify the real or rational system, while integrality imposes an additional arithmetic condition. The unique field solution makes this example particularly simple: any integer solution would have to equal that noninteger point, so none can exist.

## LG59

**Title.** Nonnegative real solutions in an affine family

**Question.** Find all nonnegative real solutions of $x+y+z=4$, $x-y=0$, and the extreme points of their solution set.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Find the full real affine family first.** The equation $x-y=0$ gives $x=y=t$. Substitution in the sum equation gives $z=4-2t$. Every real solution is therefore $(t,t,4-2t)$; conversely every such point satisfies both equalities.

**2. Impose each inequality on the same parameter.** Nonnegativity of $x$ and $y$ requires $t\ge0$. Nonnegativity of $z$ requires $4-2t\ge0$, or $t\le2$. Hence the feasible parameter interval is exactly $[0,2]$.

For $0\le t\le2$,

$$ (t,t,4-2t)=\left(1-\frac t2\right)(0,0,4)+\frac t2(2,2,0).$$

The coefficients are nonnegative and sum to one, so the feasible set is precisely the line segment joining these two endpoints.

**3. Prove the extreme-point claim.** Every point with $0<t<2$ is a nontrivial convex combination of the distinct endpoints and is therefore not extreme. To represent the $t=0$ endpoint as a convex combination of feasible points, the nonnegative first coordinates of both points must be zero, forcing both to be that endpoint. The same argument with the nonnegative coordinate $z$ proves the $t=2$ endpoint extreme. Thus exactly $(0,0,4)$ and $(2,2,0)$ are extreme points. The unrestricted affine line has no endpoint; it is the added inequalities, not elimination itself, that create this bounded feasible segment.

## LG60

**Title.** A determinant sign from row swaps and pivots

**Question.** Elimination makes a three by three matrix upper triangular with pivots $2,-3,5$ after two row swaps and no row scaling. Find its determinant.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Relate the final triangular determinant to the original one.** Let $U$ be the final triangular matrix. Row additions do not change determinant, and each of the two exchanges changes its sign. Since there is no row scaling,

$$\det U=(-1)^2\det A=\det A.$$

**2. Use triangularity for the product.** The final diagonal pivots are $2,-3,5$, so $\det U=2(-3)5=-30$. Therefore $\det A=-30$. The nonzero product also confirms nonsingularity.

**3. Explain why the operation history matters.** With one exchange instead, the same diagonal product would imply $\det A=30$. If rows had additionally been scaled by nonzero factors $s_1,\ldots,s_k$, the relation would be $\det U=(-1)^p(s_1\cdots s_k)\det A$. One would need to divide by the product of scale factors after correcting the swap sign. In particular, reducing an invertible matrix all the way to RREF yields determinant one for the final identity, which by itself loses the original determinant magnitude. The present answer is unambiguous precisely because the stem supplies two exchanges and explicitly excludes scaling. Multiplying pivots is a determinant method only when the effects of all determinant-changing operations are accounted for.

## LG61

**Title.** A zero determinant is not a consistency verdict

**Question.** Provide singular two by two systems with the same coefficient matrix but respectively no solution and infinitely many solutions.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Fix one singular coefficient matrix.** Choose $A=\begin{bmatrix}1&1\\2&2\end{bmatrix}$. Its determinant is zero, and its second row is twice the first. On a general augmented load $(b_1,b_2)^T$, the operation $R_2\leftarrow R_2-2R_1$ gives the lower equation $0=b_2-2b_1$.

**2. Construct the consistent case.** For $b=(1,2)^T$, the lower equation is $0=0$ and the remaining restriction is $x+y=1$. Set $y=t$ to obtain every solution $(1-t,t)$, with arbitrary real $t$. Each such point satisfies both original equations. The free parameter is genuinely unrestricted, so the set is infinite.

**3. Construct the inconsistent case.** For $b=(1,3)^T$, the lower equation becomes $0=1$. No point can satisfy it, so there is no solution. Equivalently the row combination $(-2,1)$ annihilates $A$ but gives $(-2,1)b=1\ne0$.

Both cases have the same determinant zero and coefficient rank one. Their augmented ranks differ: one in the consistent case and two in the inconsistent case. Thus a zero coefficient determinant rules out a unique solution for a square real system but does not choose between no solutions and infinitely many. The right side must enter the compatibility test. Over a finite field, the compatible rank-one case would have finitely many solutions rather than infinitely many, so the real-domain hypothesis also matters to the wording.

## LG62

**Title.** Block elimination with a matrix pivot

**Question.** Let $A=\begin{bmatrix}B&C\\D&E\end{bmatrix}$ with square invertible $B$. Derive the lower subsystem for $A(x,y)^T=(f,g)^T$ and its load.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Make the block dimensions explicit.** Let $B$ be $p$ by $p$, $C$ be $p$ by $q$, $D$ be $r$ by $p$, and $E$ be $r$ by $q$. Then $x\in\mathbb R^p$, $y\in\mathbb R^q$, $f\in\mathbb R^p$, and $g\in\mathbb R^r$. Only $B$ is assumed square and invertible; the lower subsystem can be rectangular.

**2. Eliminate and transform the load together.** The upper equation gives $x=B^{-1}f-B^{-1}Cy$. Substitution into $Dx+Ey=g$ yields

$$Sy=h,\qquad S=E-DB^{-1}C,\qquad h=g-DB^{-1}f.$$

Equivalently, left multiplication by the invertible block operation $T=\begin{bmatrix}I&0\\-DB^{-1}&I\end{bmatrix}$ changes the coefficient matrix to $\begin{bmatrix}B&C\\0&S\end{bmatrix}$ and the load to $(f,h)^T$.

**3. Prove equivalence, not just necessity.** Every original solution gives a solution of $Sy=h$. Conversely, if $y$ solves that lower equation and $x=B^{-1}(f-Cy)$, the upper equation holds by construction and the lower equation follows after substitution. Thus the solution correspondence is complete. If the lower equation is incompatible, so is the original system; if it has free coordinates, each permitted $y$ determines one $x$.

The factor order is forced by dimensions and matrix multiplication is not commutative. Computationally, solve $Bv=f$ and $BW=C$ and form $g-Dv$, $E-DW$, rather than explicitly forming $B^{-1}$. A singular $B$ prevents this particular derivation, even though a full matrix such as $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ can still be invertible after a block reorder.

## LG63

**Title.** A lower-triangular inverse by a finite series

**Question.** For $L=\begin{bmatrix}1&0&0\\2&1&0\\-1&3&1\end{bmatrix}$, compute its inverse and distinguish it from negating all subdiagonal entries.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Separate the identity and strictly lower part.** Write

$$N=L-I=\begin{bmatrix}0&0&0\\2&0&0\\-1&3&0\end{bmatrix}.$$

Multiplication gives $N^2=\begin{bmatrix}0&0&0\\0&0&0\\6&0&0\end{bmatrix}$ and $N^3=0$. The entry six comes from the indirect product $n_{32}n_{21}=3(2)$.

**2. Use the terminating geometric identity.** Since $N^3=0$,

$$ (I+N)(I-N+N^2)=I+N^3=I,$$

and the reversed product is also the identity because these are polynomials in the same matrix. Therefore

$$L^{-1}=I-N+N^2=\begin{bmatrix}1&0&0\\-2&1&0\\7&-3&1\end{bmatrix}.$$

**3. Verify the entry most vulnerable to error.** The third-row first-column entry of $LL^{-1}$ is $-1+3(-2)+7=0$. In the reverse product it is $7+(-3)2-1=0$. Simply negating every strictly lower entry would instead use one at position $(3,1)$ and produce $-6$ in that off-diagonal product entry, not zero.

The shortcut $I-N$ is an inverse only when $N^2=0$. Here the two-step dependency through row two makes $N^2\ne0$ and forces the extra six. More generally, for a strictly lower $n$ by $n$ matrix, $N^n=0$ and the inverse of $I+N$ is the finite alternating series through $(-N)^{n-1}$; no convergence or smallness assumption is needed.

## LG64

**Title.** A Gauss transform has a simple inverse for a reason

**Question.** Let $G=I-ge_k^T$ with $g_i=0$ for every $i\le k$. Prove $G^{-1}=I+ge_k^T$ and identify the assumption that makes this true.

**Provenance.** Course-derived proof task: Stanford CME108/MATH114, LU, Gauss-transform prompt

**Difficulty.** Hard

### Teaching solution

**1. Multiply the rank-one part before guessing an inverse.** Set $N=ge_k^T$. Its square is

$$N^2=(ge_k^T)(ge_k^T)=g(e_k^Tg)e_k^T=g_kN.$$

The hypothesis $g_i=0$ for $i\le k$ implies $g_k=0$, so $N^2=0$. Hence $(I-N)(I+N)=I-N^2=I$, and the same computation in reverse order gives the other inverse identity. Therefore $G^{-1}=I+ge_k^T$.

**2. Identify the minimal algebraic hypothesis.** It is the single condition $e_k^Tg=g_k=0$ that makes the square vanish. Having support strictly below the pivot supplies this condition and also makes $G$ a unit lower triangular elimination matrix. The additional zeros above the pivot enforce that elimination structure; they are not separately needed for the inverse identity once $g_k=0$ is known.

**3. Examine the excluded case.** If $g_k\ne0$ and $g\ne0$, then $N^2=g_kN\ne0$, and the claimed opposite-sign inverse fails. More precisely, if $g_k\ne1$, direct multiplication gives

$$ (I-N)^{-1}=I+\frac{N}{1-g_k}.$$

If $g_k=1$, then $(I-N)g=(1-g_k)g=0$ with $g\ne0$, so the matrix is singular. Thus rank-one appearance alone is insufficient; the special support of elimination multipliers is exactly what justifies the particularly simple inverse used in LU derivations.

## LG65

**Title.** Why multiple contradictions add only one augmented rank

**Question.** An eliminated single-load system has several coefficient-zero rows with nonzero right sides. Can the augmented rank exceed the coefficient rank by more than one?

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Use the one-column rank bound.** The column space of $[A\mid b]$ is generated by the columns of $A$ plus the single extra vector $b$. Adding one vector can increase dimension by at most one. Therefore

$$\operatorname{rank}A\le\operatorname{rank}[A\mid b]\le\operatorname{rank}A+1.$$

**2. Read the same fact from contradiction rows.** After coefficient elimination, every coefficient-zero augmented row has the form $(0,\ldots,0,c_i)$. All rows with $c_i\ne0$ are scalar multiples of the last-coordinate row. Several such rows can give several visible contradictions, but they span only one new row direction. For instance, the lower rows $[0\ 0\mid2]$ and $[0\ 0\mid5]$ reduce to $[0\ 0\mid1]$ and a zero row, not two independent pivots.

**3. Connect rank with compatibility.** If any contradiction appears, $b$ is outside the original column space, so the rank increases by exactly one. If no contradiction appears, $b$ is in that space and the rank does not increase. In a full augmented RREF the single right-side column can have only one pivot.

For several load columns the bound changes: appending $q$ columns can increase rank by as much as $q$. As a simple example, take a zero $2$ by $1$ coefficient matrix and append the two columns of $I_2$; coefficient rank zero becomes augmented rank two. That block statement must not be confused with the rank increment for one individual load.

## LG66

**Title.** Same kernel need not mean the same nonhomogeneous solutions

**Question.** Let $A=[1\;0]$ and $C=[2\;0]$. Compare the systems $Ax=1$ and $Cx=1$, and their homogeneous kernels.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Compare the homogeneous maps.** With a two-coordinate unknown $u=(u_1,u_2)^T$, $Au=0$ means $u_1=0$, whereas $Cu=0$ means $2u_1=0$. Over the reals these conditions are equivalent, so both kernels are $\{(0,t)^T:t\in\mathbb R\}$.

**2. Solve the nonhomogeneous equations as stated.** The first load-one system has solution set $\{(1,t)^T:t\in\mathbb R\}$. The second has solution set $\{(1/2,t)^T:t\in\mathbb R\}$. These parallel affine lines are disjoint. They have identical allowable difference directions but different offsets.

**3. Explain the missing load operation.** Since $C=2A$, scaling the entire first equation by two would produce $Cu=2$, not $Cu=1$. The equivalent solution line would then still be $u_1=1$. Coefficient row equivalence by itself preserves homogeneous kernels; nonhomogeneous equivalence requires the same invertible transformation of the load.

In affine form, the kernel supplies the direction space in $u=u_p+z$, but it does not supply the particular point $u_p$. Even multiplying a scalar equation by a nonzero constant can change the nonhomogeneous set if its right side is held fixed. This is a minimal counterexample to the claim that knowing the same kernel is enough to identify every load-dependent solution set.

## LG67

**Title.** A complete elimination certificate for an asserted solution family

**Question.** A proposed family for $x+y+z=2$, $2x-y+z=1$ is $(1,1,0)+t(1,1,-2)$. Accept or reject it and repair the result.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Test the proposed base point and direction separately.** The point $(1,1,0)$ gives $1+1+0=2$ and $2-1+0=1$, so it is a valid particular solution. The proposed direction $v=(1,1,-2)$ gives $1+1-2=0$ in the first homogeneous equation but $2-1-2=-1$ in the second. Therefore the proposed family has second load $1-t$ rather than one; it is valid only at $t=0$, not for arbitrary $t$.

**2. Derive the complete family from the original equations.** Subtract the first equation from the second to obtain $x-2y=-1$. Thus $x=2y-1$. Substituting into the first gives $z=3-3y$. Since no condition remains on $y$, let $y=1+t$. Then

$$ (x,y,z)=(1,1,0)+t(2,1,-3),\qquad t\in\mathbb R.$$

**3. Verify both validity and completeness.** The repaired direction gives $2+1-3=0$ and $4-1-3=0$, so every displayed point satisfies both loads. Conversely, any original solution has some real coordinate $y$; choosing $t=y-1$ reproduces its forced values of $x$ and $z$. This converse proves no solutions were omitted. Checking a particular point alone certifies existence; checking all null directions certifies validity of the family; the converse parametrization or pivot count certifies completeness. All three roles matter when judging an asserted general solution.

## LG68

**Title.** Minimum-length member of an affine line

**Question.** The solutions are $x=(1,2)^T+t(1,-1)^T$. Find the unique solution of minimum Euclidean norm using the parametrization.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Optimize on the already complete affine line.** The coordinates are $x_1=1+t$ and $x_2=2-t$, so the squared Euclidean norm is

$$f(t)=(1+t)^2+(2-t)^2=2t^2-2t+5=2\left(t-\frac12\right)^2+\frac92.$$

Because the squared term is nonnegative and its coefficient is strictly positive, the unique global minimum occurs at $t=1/2$. The minimum-norm point is $(3/2,3/2)^T$, and its norm is $3/\sqrt2$. Minimizing the squared norm also minimizes the norm because the square-root function is increasing on nonnegative numbers.

**2. Verify the geometric criterion without calculus.** With direction $v=(1,-1)^T$, the chosen point $x_*$ obeys $x_*^Tv=3/2-3/2=0$. Every other point is $x_*+sv$, and

$${\Vert x_*+sv\Vert}^2={\Vert x_*\Vert}^2+2s x_*^Tv+s^2{\Vert v\Vert}^2=\frac92+2s^2.$$

This proves strict minimality for every $s\ne0$ and explains why orthogonality to the null direction is the relevant condition.

**3. Distinguish selection from solving the original constraints.** Taking the free parameter to be zero produces the perfectly valid point $(1,2)^T$, but its squared norm is five, larger than $9/2$. Free-parameter zero is a convenient particular solution, not a minimum-norm theorem. Here all points satisfy $x_1+x_2=3$; the optimization selects the point on that line closest to the origin while leaving the full equation solution set unchanged.

## LG69

**Title.** Deterministic pivot search versus maximum-magnitude search

**Question.** In exact rational arithmetic, must one select the largest available pivot to obtain the correct RREF? Discuss work and the canonical result.

**Provenance.** Original problem

**Difficulty.** Hard

### Teaching solution

**1. Separate algebraic legality from numerical preference.** In exact rational arithmetic, every nonzero pivot has an exact reciprocal. Scaling its row and adding multiples to other rows are reversible, so no maximum-magnitude condition is required for preserving the system. For example, in $\begin{bmatrix}1&1\\2&3\end{bmatrix}$ one may keep the first pivot one or exchange rows and use two; both are legal and both yield the same final identity RREF of the coefficient matrix.

**2. State the actual correctness requirements.** Search the current active column, choose an eligible nonzero entry, exchange the whole augmented row when necessary, retain the multiplier before overwriting it, and update every trailing coefficient and load. Skip a column only if all eligible entries in it are zero. Continue monotonically through columns and normalize and clear pivot columns to reach RREF. These conditions, rather than pivot magnitude, give termination and equivalence.

**3. Explain canonical output versus noncanonical work.** Different legal choices can create different intermediate fractions and different echelon arrays. The unique RREF of the same augmented row-equivalence class is nevertheless the same, so the final classification and affine family agree. Exact implementation work is affected by numerator and denominator growth: a small rational pivot can introduce large denominators, while another choice may reduce them. Maximizing real magnitude is primarily motivated by floating-point multiplier control and is not automatically a minimum-bit-cost strategy. Over an arbitrary field there may be no compatible notion of magnitude at all. A deterministic “first eligible nonzero” rule can therefore be mathematically correct even though it is not the preferred floating-point strategy.
