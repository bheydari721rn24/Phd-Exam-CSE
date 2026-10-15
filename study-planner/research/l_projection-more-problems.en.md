## Problem 11. A perpendicular pair is not a complete certificate

**Question.** A candidate projection of $b=(1,1,1)^T$ onto $S=\operatorname{span}(e_1,e_2)$ is $p=e_1$. It satisfies $p^T(b-p)=0$. Is it the closest point? Give a necessary and sufficient certificate instead.

**Solution.** The proposed residual is $r=(0,1,1)^T$. Its dot product with $p=e_1$ is indeed zero, and the candidate belongs to the plane. But $e_2^Tr=1$, so the residual is not perpendicular to the entire plane. The candidate has squared error two. The point $(1,1,0)^T$ belongs to the plane and has squared error one, proving the proposed answer is wrong.

The complete certificate requires both $p\in S$ and $v^T(b-p)=0$ for every $v\in S$. It suffices to check every member of any spanning set. If those conditions hold, then for any $z\in S$, $b-z=(b-p)+(p-z)$ has perpendicular components. Consequently its squared length is ${\Vert b-p\Vert}^2+{\Vert p-z\Vert}^2$, minimized uniquely at $z=p$. A single vanishing scalar product cannot replace a whole-subspace condition when the subspace has more than one direction.

## Problem 12. Project onto a kernel without finding its basis

**Question.** Find the Euclidean projection onto $S=\{x:x_1+2x_2+2x_3=0\}$, then project $b=(3,0,0)^T$ and calculate the distance.

**Solution.** The constraint normal is $n=(1,2,2)^T$ and $n^Tn=9$. The normal-line projection is $nn^T/9$. Subtracting it from the identity gives

$$P=\frac19\begin{pmatrix}8&-2&-2\\-2&5&-4\\-2&-4&5\end{pmatrix}.$$

Thus $p=(8/3,-2/3,-2/3)^T$ and $r=(1/3,2/3,2/3)^T=n/3$. Substituting $p$ into the constraint gives $8/3-4/3-4/3=0$, so it is feasible. The residual is a normal multiple, providing the perpendicularity certificate. Its squared length is one, so the distance is one.

The matrix has trace two, consistent with one independent constraint in three dimensions. The normal-line projector has trace one. Confusing these complementary operators returns the residual instead of the closest point. The method avoids solving for two plane generators, but it relies on a nonzero normal: a zero constraint normal either imposes no homogeneous restriction or makes a nonzero affine right-hand side inconsistent.

## Problem 13. Orthogonal but unnormalized generators

**Question.** Project $b=(4,8,1)^T$ onto the span of $v_1=(2,1,2)^T$ and $v_2=(-2,2,1)^T$. Can their outer products simply be added?

**Solution.** Their dot product is $-4+2+2=0$, and both squared lengths are nine. Their products with the target are eighteen and nine. Therefore the correct projection is $p=2v_1+v_2=(2,4,5)^T$. The residual $(2,4,-4)^T$ has zero dot product with each generator, and its squared length is thirty-six.

The matrix is $(v_1v_1^T+v_2v_2^T)/9$. Adding the unscaled outer products produces $9P$, which acts by nine on every vector in the plane; it is not idempotent. If normalized generators $u_i=v_i/3$ are used, the formula becomes $u_1u_1^T+u_2u_2^T$ with no extra denominator.

The energy check is ${\Vert b\Vert}^2=81$, ${\Vert p\Vert}^2=45$, and ${\Vert r\Vert}^2=36$. This independently confirms the squared distance. The distinction between orthogonal and orthonormal is substantive: perpendicularity separates the coefficient equations, while unit normalization removes their denominators. This is an independently explained reconstruction of the numerical example in Berkeley's projection notes, pages three and four.

## Problem 14. Recover a projector from its action

**Question.** An orthogonal projector on $\mathbb R^3$ fixes $u=(1,1,0)^T$ and kills $v=(1,-1,0)^T$. Does this determine it uniquely? List all possibilities.

**Solution.** Normalize these perpendicular vectors to $q_1=u/\sqrt2$ and $q_2=v/\sqrt2$, and complete them with $q_3=e_3$. Symmetry implies $\langle Pq_3,q_1\rangle=\langle q_3,Pq_1\rangle=0$ and $\langle Pq_3,q_2\rangle=\langle q_3,Pq_2\rangle=0$. Thus $Pq_3$ is a scalar multiple $\lambda q_3$. Idempotence forces $\lambda^2=\lambda$, giving zero or one.

The two possibilities in standard coordinates are

$$P_0=\frac12\begin{pmatrix}1&1&0\\1&1&0\\0&0&0\end{pmatrix},\qquad P_1=P_0+e_3e_3^T.$$

Their ranks are one and two. Both satisfy every given action. The unspecified perpendicular direction creates a genuine ambiguity; counting the two supplied vectors does not establish that all three directions have been characterized. If the problem additionally states rank one, only the first remains. Without orthogonality, a third input could map obliquely into the fixed line and produce still more idempotent maps.

## Problem 15. A rank-one update when a new generator is added

**Question.** Suppose $P$ projects onto $S$ and a vector $v$ is added to its generators. Derive the new projector and handle $v\in S$ separately. Apply the result to $S=\operatorname{span}(e_1)$ and $v=(1,2,2)^T$.

**Solution.** Split $v=Pv+w$ with $w=(I-P)v$. If $w=0$, the new vector was already in $S$, so the subspace and projector are unchanged. If $w\ne0$, the enlarged space is the perpendicular direct sum of $S$ and the line spanned by $w$. Consequently

$$P_{\rm new}=P+\frac{ww^T}{w^Tw}.$$

The cross-products vanish because $Pw=0$, so the sum is symmetric and idempotent. Its range is the enlarged subspace, and its rank increases by exactly one. This derives the update and explains its denominator rather than guessing an outer product of the original $v$.

In the example $w=(0,2,2)^T$, giving $P_{\rm new}=\begin{pmatrix}1&0&0\\0&1/2&1/2\\0&1/2&1/2\end{pmatrix}$. For $b=(0,1,-1)^T$, both its projection and the update contribution are zero, so its squared distance remains two. Using $vv^T/(v^Tv)$ instead would double-count a component already present in $S$.

## Problem 16. A nonorthogonal change of basis

**Question.** The physical projector is $P=\operatorname{diag}(1,0)$, but coordinates use $B=\begin{pmatrix}1&1\\0&1\end{pmatrix}$. Compute the coordinate projector and its correct metric. Explain its nonsymmetry.

**Solution.** The inverse basis matrix is $B^{-1}=\begin{pmatrix}1&-1\\0&1\end{pmatrix}$. Direct multiplication gives $E=B^{-1}PB=\begin{pmatrix}1&1\\0&0\end{pmatrix}$. The coordinate metric is $G=B^TB=\begin{pmatrix}1&1\\1&2\end{pmatrix}$. We obtain $E^2=E$ and $E^TG=GE=\begin{pmatrix}1&1\\1&1\end{pmatrix}$.

For the physical vector $b=e_2$, its coordinates are $z=(-1,1)^T$. The coordinate projection is $Ez=0$, corresponding to the correct physical closest point zero. Its coordinate residual equals $z$, whose squared $G$-length is one, agreeing with the physical squared distance.

Ordinary coordinate symmetry is absent because the chosen basis vectors are not perpendicular. Testing $E^T=E$ would use the wrong metric. In contrast, treating that same numerical matrix as a map in a separately declared ordinary Euclidean coordinate system would make it oblique. A basis change preserves the geometric map only when its metric is transformed as well.

## Problem 17. Derive a Householder reflection

**Question.** Reflect $b=(3,0)^T$ across the line $x+y=0$. Find the reflection matrix, its determinant and the associated closest-point projection.

**Solution.** The normal is $n=(1,1)^T$. Projection onto the reflecting line is $P=I-nn^T/2=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$. Therefore $H=2P-I=\begin{pmatrix}0&-1\\-1&0\end{pmatrix}$ and $Hb=(0,-3)^T$. The projected point is $Pb=(3/2,-3/2)^T$, the midpoint of $b$ and its reflection.

The determinant of $H$ is minus one, so this is a reflection rather than a rotation of the plane. Directly, $H^TH=I$ and $H^2=I$; the input and reflected vectors have the same norm three. The direction $(1,-1)^T$ is fixed and the normal $(1,1)^T$ is negated.

The midpoint identity $P=(I+H)/2$ explains why averaging identity and reflection produces a closest-point map. The reflection itself is not idempotent: its second application returns the input. The projection is idempotent and discards the normal component. Confusing these two operations changes both the output and the spectrum.

## Problem 18. Quantify alternating projections

**Question.** Project alternately onto a line at sixty degrees and the horizontal axis, starting at $e_1$. Count a full cycle as the sloping projection followed by the horizontal one. How many cycles make the norm at most $1/1000$?

**Solution.** Here $c=1/2$ and $s=\sqrt3/2$. One cycle is $M=PQ=\begin{pmatrix}1/4&\sqrt3/4\\0&0\end{pmatrix}$. Since $Me_1=e_1/4$, induction gives $M^je_1=4^{-j}e_1$. The question asks for $4^j\ge1000$. Four cycles give denominator 256, which is insufficient; five give 1024, which is sufficient. Thus exactly five cycles are needed.

The intermediate sloping point in cycle $j$ is $4^{-(j-1)}(1/4,\sqrt3/4)^T$, and the next horizontal point is $(4^{-j},0)^T$. These are actual finite vectors, not the intersection projector. The two lines intersect only at zero, which is reached as a limit for this input, not after any finite cycle.

If a simulation counts each individual projection as a step, it requires ten individual steps rather than five. Stating what one iteration means prevents a factor-of-two error. A nearly parallel pair would have a contraction factor close to one and require many more cycles.

## Problem 19. A commutator and a quantitative angle

**Question.** For the horizontal projector $P$ and the projector $Q$ onto $(\cos\theta,\sin\theta)^T$, compute $PQ-QP$ and its squared Frobenius norm. When do they commute?

**Solution.** With $c=\cos\theta$ and $s=\sin\theta$, multiplication gives

$$PQ-QP=\begin{pmatrix}0&cs\\-cs&0\end{pmatrix},\qquad {\Vert PQ-QP\Vert}_F^2=2c^2s^2.$$

Thus the two maps commute exactly when $cs=0$. In the interval from zero to ninety degrees this means coincident lines or perpendicular lines. At forty-five degrees the squared norm is one half, the largest possible value for this family, since $c^2s^2\le1/4$.

The commutator is skew-symmetric, as transposition reverses its sign. It records an order effect: applying one projection before the other usually changes the result. It is not itself a projection merely because its factors are projections. A zero commutator is enough to construct the intersection projector by multiplication, but the numerical size of the commutator alone is not the intersection dimension or a count of violated constraints. The angle calculation makes the distinction explicit.

## Problem 20. Equal ranks do not imply equal ranges

**Question.** Two rank-two orthogonal projectors in $\mathbb R^3$ satisfy $\operatorname{tr}(PQ)=3/2$. Find ${\Vert P-Q\Vert}_F^2$ and the dimension of their intersection.

**Solution.** Expanding the squared Frobenius norm yields $\operatorname{tr}(P)+\operatorname{tr}(Q)-2\operatorname{tr}(PQ)=2+2-3=1$. The dimension formula implies that two planes in three dimensions intersect in dimension at least one.

If their intersection had dimension two, their ranges would coincide. The orthogonal projector onto a fixed subspace is unique, so $P=Q$, giving $\operatorname{tr}(PQ)=\operatorname{tr}(P)=2$, contrary to the data. The intersection therefore has dimension exactly one. The trace value $3/2$ itself is not a dimension.

To check realizability, let $P$ project onto the plane spanned by $e_1,e_2$, and let $Q$ project onto the plane spanned by $e_1,(e_2+e_3)/\sqrt2$. The common direction contributes one to the product trace and the remaining pair contributes one half. This constructs the stated overlap and confirms that the conditions are consistent, rather than merely extracting a formal number from them.

## Problem 21. A projector polynomial without multiplication

**Question.** Let $P$ be an idempotent matrix. Evaluate $P^7-3P^2+2I$ and determine when $aI+bP$ is invertible. Give its inverse when it exists.

**Solution.** Every positive power of $P$ equals $P$ by induction. The polynomial is therefore $2I-2P=2(I-P)$. More generally, on the range of $P$, the matrix $aI+bP$ acts by $a+b$; on its kernel it acts by $a$. These subspaces form a direct sum even for oblique idempotents.

If both subspaces are nonzero, invertibility requires $a\ne0$ and $a+b\ne0$, and the inverse is

$$\frac1a(I-P)+\frac1{a+b}P.$$

Multiplying and using $P(I-P)=0$ verifies the formula. Endpoint ranks need care: if $P=0$, only $a\ne0$ is required; if $P=I$, only $a+b\ne0$ is required. A formula containing a denominator for a nonexistent component can impose an unnecessary restriction. This method uses idempotence rather than orthogonality, so it applies to oblique projectors too. Positivity and norm conclusions, by contrast, would require more information.

## Problem 22. Rank from a shifted determinant

**Question.** An idempotent $5\times5$ real matrix satisfies $\det(I+2P)=27$. Determine its rank and $\det(2I-P)$. Must the matrix be symmetric?

**Solution.** A basis of the range followed by a basis of the kernel makes $P$ similar to $\operatorname{diag}(I_k,0)$. Thus $I+2P$ has $k$ eigenvalues three and $5-k$ eigenvalues one. Its determinant is $3^k=27$, giving $k=3$.

The second shifted matrix acts by one on the range and by two on the kernel. Therefore $\det(2I-P)=1^3 2^2=4$. The trace of $P$ is also three, but that fact does not imply symmetry. Similarity by an arbitrary invertible matrix preserves idempotence and these determinant values while generally destroying Euclidean symmetry.

For a concrete nonsymmetric construction, take a two-dimensional block $\begin{pmatrix}1&1\\0&0\end{pmatrix}$ and append diagonal entries $1,1,0$. The resulting five-dimensional matrix has rank three and both required determinants, yet is not symmetric. Spectral calculations answer the rank question; they do not certify that the decomposition uses perpendicular subspaces.

## Problem 23. All affine points from one constraint correction

**Question.** Minimize ${\Vert x-b\Vert}^2$ subject to $Dx=d$, where $D=\begin{pmatrix}1&1&0\\0&1&1\end{pmatrix}$, $d=(1,2)^T$ and $b=(1,0,0)^T$.

**Solution.** The violation is $Db-d=(0,-2)^T$. The row Gram matrix is $\begin{pmatrix}2&1\\1&2\end{pmatrix}$, whose inverse is $\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$. The multiplier is $(2/3,-4/3)^T$, so the correction $D^T\lambda$ is $(2/3,-2/3,-4/3)^T$. Therefore

$$p=(1/3,2/3,4/3)^T,\qquad {\Vert b-p\Vert}^2=8/3.$$

Both constraints check directly. Every feasible vector is $p+t(-1,1,-1)^T$, and the residual $(2/3,-2/3,-4/3)^T$ is perpendicular to that direction. Thus the squared error for a general feasible vector is $8/3+3t^2$, proving unique minimality at $t=0$ without relying only on stationary equations.

The residual lies in the row space, while the feasible directions lie in the kernel. These are subspaces of the three-dimensional physical space. The multiplier has only two entries because it belongs to constraint space; adding it directly to $b$ would be dimensionally invalid.

## Problem 24. Dependent constraints: consistency comes first

**Question.** Compare closest-point problems with constraints $x+y=1$, $2x+2y=2$ and with constraints $x+y=1$, $2x+2y=3$. Use the target zero.

**Solution.** In the first system the second equation is redundant. The feasible set is one line. Write $y=1-x$; the squared distance from zero is $x^2+(1-x)^2=2(x-1/2)^2+1/2$. The unique closest point is $(1/2,1/2)^T$ with squared distance one half. The two-row Gram matrix is singular, but the geometry remains well-defined after retaining one independent row.

In the second system, doubling the first equation forces $2x+2y=2$, contradicting the second equation. The feasible set is empty. There is no closest feasible point and no projection onto that empty set in the sense studied here.

An unconstrained least-squares fit to the inconsistent equations is a different optimization problem. With $s=x+y$, it minimizes $(s-1)^2+(2s-3)^2$, giving $s=7/5$. None of those minimizers satisfies either required pair exactly. A pseudoinverse cannot make incompatible constraints consistent; it can only solve a declared surrogate. Check the augmented rank before using an affine projection formula.

## Problem 25. A weighted affine correction

**Question.** Minimize $x^2+4y^2$ subject to $x+y=1$. Compare the answer with ordinary Euclidean projection of zero onto the same line.

**Solution.** Substitute $y=1-x$. The objective is $x^2+4(1-x)^2=5(x-4/5)^2+4/5$. Thus the unique weighted minimizer is $(4/5,1/5)^T$ with squared weighted distance $4/5$. Ordinary Euclidean minimization instead gives $(1/2,1/2)^T$.

The weighted correction formula explains the difference. With $G=\operatorname{diag}(1,4)$ and row constraint $D=(1,1)$, the shortest correction from target $b$ is

$$p=b-G^{-1}D^T(DG^{-1}D^T)^{-1}(Db-1).$$

At zero, $G^{-1}D^T=(1,1/4)^T$ and $DG^{-1}D^T=5/4$, producing the same answer. The correction follows the metric normal $G^{-1}D^T$, not the ordinary normal $D^T$.

The direction $(1,-1)^T$ lies in the line's direction space. Its weighted inner product with the minimizer is $4/5-4/5=0$. This verifies the correct orthogonality certificate and explains conceptually why changing the cost weights changes the closest point.

## Problem 26. A semidefinite cost can lose uniqueness

**Question.** Minimize $x^TGx$ over $x\in\mathbb R^2$ with $G=\operatorname{diag}(1,0)$. Then minimize the same cost subject to $x_1=1$. Why does the positive-definite projection theorem not apply?

**Solution.** The objective is simply $x_1^2$. Unconstrained minimizers are all vectors $(0,t)^T$, with arbitrary real $t$, and cost zero. Under $x_1=1$, every feasible vector $(1,t)^T$ has cost one, so again there are infinitely many minimizers.

The matrix is positive semidefinite, not positive definite. The nonzero vector $e_2$ has zero squared cost, violating the condition that zero length occurs only at the zero vector. Therefore $x^TGy$ is not an inner product on the full plane and its associated quantity is not a norm there.

The closest-point proof uses strict positivity of the extra squared difference to establish uniqueness. Here the extra term can vanish for different points separated in the unpenalized direction. A specific restricted feasible set might still have a unique minimizer, but uniqueness must then be proved from those restrictions. Substituting a singular weight into a formula derived for a positive-definite metric is not a valid general argument.

## Problem 27. Classify an idempotent family

**Question.** Let $P_a=\begin{pmatrix}1&a\\0&0\end{pmatrix}$ for real $a$. Find when it is Euclidean orthogonal, and find a positive-definite metric making it orthogonal for any fixed $a$.

**Solution.** Every member is idempotent. Euclidean symmetry requires $a=0$, which is also sufficient. For a general metric $G=\begin{pmatrix}g&h\\h&k\end{pmatrix}$, the self-adjoint condition $P_a^TG=GP_a$ requires $h=ag$. Positive definiteness then requires $g>0$ and $k>a^2g$.

One valid choice is $G=\begin{pmatrix}1&a\\a&a^2+1\end{pmatrix}$, whose determinant is one. Its quadratic form is $(x+ay)^2+y^2$, strictly positive for every nonzero vector. The range direction $e_1$ and kernel direction $(-a,1)^T$ have zero $G$-product.

Thus an oblique Euclidean projector can be orthogonal for another declared metric. The numerical matrix alone does not specify what perpendicularity means. Conversely, inventing a new metric after a question explicitly states the ordinary dot product would change the problem. The distinction helps diagnose apparent disagreements between coordinate formulas without erasing their hypotheses.

## Problem 28. Impossible diagonal and a sharp entry bound

**Question.** A real orthogonal projector has $p_{11}=1/4$ and $p_{22}=3/4$. Bound $|p_{12}|$. Can equality occur in two dimensions?

**Solution.** Cauchy–Schwarz for $Pe_1,Pe_2$ gives $p_{12}^2\le(1/4)(3/4)=3/16$. Applying it to the complementary projector gives the same bound, so $|p_{12}|\le\sqrt3/4$.

In two dimensions the symmetric candidate is $\begin{pmatrix}1/4&t\\t&3/4\end{pmatrix}$. Idempotence on the first diagonal gives $1/16+t^2=1/4$, requiring $t^2=3/16$. The other diagonal and off-diagonal equations then hold. Hence exactly the two signs $t=\pm\sqrt3/4$ are possible, and each attains equality.

These are line projectors generated by unit vectors $(1/2,\pm\sqrt3/2)^T$. A candidate with the same diagonal and $t=0$ satisfies the entry bound but is not idempotent. Necessary inequalities help reject matrices; they do not replace the defining identities. In higher dimensions extra entries can contribute to row squared norms, so the two-dimensional equality conclusion cannot be inferred from these two diagonal entries alone.

## Problem 29. Orthogonal decomposition of an observation vector

**Question.** Reconstruct MIT Session2.3 exercise16.1: fit the observations $(7,7,21)^T$ at times $(-1,1,2)$ with $C+Dt$. Derive the coefficients rather than quoting the answer.

**Solution.** The design columns are the all-ones vector and the time vector. Their Gram matrix is $\begin{pmatrix}3&2\\2&6\end{pmatrix}$, and their products with the observation vector give $(35,42)^T$. The normal equations are $3C+2D=35$ and $2C+6D=42$. Eliminate $C$: multiplying the first equation by two and the second by three gives $6C+4D=70$ and $6C+18D=126$. Thus $14D=56$, so $D=4$ and $C=9$.

The fitted observation vector is $(5,13,17)^T$, lying in the two-dimensional column space in $\mathbb R^3$. The coefficient vector $(9,4)^T$ instead lives in $\mathbb R^2$. They describe different objects. Since the two columns are independent, their Gram matrix has positive determinant fourteen and this coefficient solution is unique. The calculation is a projection in observation space, not an orthogonal-distance line fit in the time-height plot.

## Problem 30. Explain why projecting the error gives zero

**Question.** Continue the preceding MIT exercise family16.2–16.4. Find the residual, project that residual, and project the fitted vector again. Explain all three operations geometrically.

**Solution.** Subtracting fitted from observed values gives $r=(2,-6,4)^T$. Its products with the two design columns are $2-6+4=0$ and $-2-6+8=0$. Therefore it lies in the left nullspace and its orthogonal projection onto the column space is zero. Its squared norm is $4+36+16=56$.

The fitted vector $p=(5,13,17)^T$ already belongs to that column space, so $Pp=p$. Thus the operator kills the error and fixes the fit: $Pr=0$ and $Pp=p$. For a general input $b=p+r$, linearity then gives $Pb=p$.

If the residual is used as a new response vector with the same design columns, the unique fitted coefficients are zero. If the fitted response is used instead, its coefficients remain $(9,4)^T$ and its residual becomes zero. These statements depend on keeping the same design space; changing the time points or columns changes the projector. The operations demonstrate complementary subspaces and idempotence rather than requiring another matrix inverse.

## Problem 31. Locate each vector in its correct ambient space

**Question.** Revisit the four-subspace issue in MIT exercise16.5. For $A\in\mathbb R^{m\times n}$, where do the fitted vector, residual and least-squares coefficients belong? What changes if the columns are dependent?

**Solution.** The physical fit $p$ belongs to $\operatorname{Col}(A)\subseteq\mathbb R^m$. The residual belongs to $\operatorname{Ker}(A^T)\subseteq\mathbb R^m$. Any coefficient minimizer $c$ belongs to $\mathbb R^n$ and satisfies $Ac=p$. If the columns are independent, the row space of $A$ is all of $\mathbb R^n$, so that unique coefficient vector lies in it automatically.

With dependent columns, every minimizer has the form $c_0+z$, where $z\in\operatorname{Ker}(A)$. The unique minimum-norm minimizer is the one in $\operatorname{Col}(A^T)=\operatorname{Ker}(A)^\perp$. Other minimizers need not lie in the row space. For example, if $A=(1,1)$ and the target is one, $(1,0)^T$ is a minimizer but is not on the row-space line spanned by $(1,1)^T$; the minimum-norm choice is $(1/2,1/2)^T$.

Thus the source's full-column-rank example cannot be generalized to every minimizer of a deficient system. This is a hypothesis check, not a disagreement with its stated example.

## Problem 32. Symmetric times remove one coupling term

**Question.** Reconstruct MIT exercise16.6: fit values $(4,2,-1,0,0)^T$ at times $(-2,-1,0,1,2)$ with an intercept and slope. Compute the fit and squared residual norm.

**Solution.** The time sum is zero and the sum of squared times is ten. Thus the Gram matrix is $\operatorname{diag}(5,10)$. The observation sum is five, and the time-weighted sum is $-8-2=-10$. Therefore the coefficient equations give $C=1$ and $D=-1$.

The fitted values are $(3,2,1,0,-1)^T$, and the residual is $(1,0,-2,0,1)^T$. Its sum and time-weighted sum are zero, as required by perpendicularity to both design columns. The squared error is $1+4+1=6$. The input squared norm is twenty-one and the fitted squared norm is fifteen, giving the energy check $21=15+6$.

Centering time values makes the constant and time columns perpendicular; it does not necessarily make either a unit vector. Their squared lengths remain five and ten, explaining the two denominators. Symmetry of the times simplifies this example, but orthogonality follows from zero sum even for nonsymmetric time sets. The distinction separates a sufficient convenient pattern from the exact algebraic condition.

## Problem 33. QR from an explicit orthonormal pair

**Question.** Let $q_1=(1,1,0)^T/\sqrt2$, $q_2=(1,-1,2)^T/\sqrt6$, and $Q=[q_1\ q_2]$. Project $b=e_3$ and find the complementary rank-one projector.

**Solution.** The vectors have unit norm and dot product zero. The coordinate measurements are $Q^Tb=(0,2/\sqrt6)^T$. Reconstruction gives $p=(1/3,-1/3,2/3)^T$. The residual is $r=(-1/3,1/3,1/3)^T$, whose squared norm is one third.

A perpendicular unit vector is $q_3=(-1,1,1)^T/\sqrt3$. Hence $I-QQ^T=q_3q_3^T$, while $QQ^T=I-q_3q_3^T$. This provides a second calculation of the same residual. The fitted squared norm is two thirds, summing with the residual energy to the unit input energy.

Although $Q^TQ=I_2$, the product $QQ^T$ is a three-dimensional rank-two projector and cannot equal $I_3$. Its nullspace contains the nonzero vector $q_3$. Rectangular orthonormality is one-sided; substituting the wrong identity would make the computed residual vanish and falsely claim that every three-dimensional vector lies in a two-dimensional plane.

## Problem 34. Projection operators in a polynomial space

**Question.** In real polynomials of degree at most two, use $\langle f,g\rangle=\int_{-1}^1f(t)g(t)\,dt$. Project $f(t)=t^2$ onto the span of $1,t$. Find the squared error.

**Solution.** The generators are perpendicular because $\int_{-1}^1t\,dt=0$. Their squared norms are two and $2/3$. The target products are $\int_{-1}^1t^2dt=2/3$ and $\int_{-1}^1t^3dt=0$. Thus its projection is the constant polynomial $p(t)=1/3$.

The residual $t^2-1/3$ has zero product with both generators. Its squared norm is

$$\int_{-1}^1(t^2-1/3)^2dt=2/5-4/9+2/9=8/45.$$

The coefficient vector of $f$ in the monomial basis is $(0,0,1)^T$. Merely discarding the quadratic coordinate would give zero, which is wrong: the monomial basis is not orthonormal in this integral metric. Indeed the constant and quadratic monomials have nonzero product $2/3$. Projection acts on functions with their declared inner product, not on an arbitrary coefficient list with an assumed Euclidean metric. The same finite-dimensional theorem applies once the correct Gram matrix is used.

## Problem 35. Weighted complex projection

**Question.** In $\mathbb C^2$, use $G=\operatorname{diag}(2,1)$ and project $b=(1,1)^T$ onto the complex line generated by $u=(1,i)^T$.

**Solution.** The correct product is $u^*Gb=2-i$, and $u^*Gu=3$. Therefore the coefficient is $(2-i)/3$ and

$$p=\frac13\begin{pmatrix}2-i\\1+2i\end{pmatrix},\qquad r=\frac13\begin{pmatrix}1+i\\2-2i\end{pmatrix}.$$

The matrix is $P_G=\frac13\begin{pmatrix}2&-i\\2i&1\end{pmatrix}$. It is generally not Hermitian under the ordinary complex dot product, but satisfies $P_G^*G=GP_G$ and is idempotent. The weighted residual certificate is $u^*Gr=2(1+i)/3-i(2-2i)/3=0$.

The projected energy is $|2-i|^2/3=5/3$, while the input energy is three. The residual energy is therefore $4/3$; direct magnitude squares give the same value. Both conjugation and the metric are essential. Replacing $G$ by the identity solves a different closest-point problem, while replacing the conjugate transpose by an ordinary transpose destroys positive definiteness.

## Problem 36. Recover a subspace from a distance oracle

**Question.** An unknown orthogonal projector $P$ on $\mathbb R^3$ has squared residual distances zero for $e_1$ and $e_2$, and one for $e_3$. Determine $P$. Would knowledge of the three diagonal distances always determine a projector?

**Solution.** Zero distance for $e_1$ implies $(I-P)e_1=0$, hence $Pe_1=e_1$. The same reasoning fixes $e_2$. Distance one for the unit vector $e_3$ implies its projected energy is zero by Pythagoras, so $Pe_3=0$. The action on this basis determines $P=\operatorname{diag}(1,1,0)$.

The endpoint distance values are decisive because a nonnegative squared norm can vanish only at zero. Intermediate values do not usually identify the directions. In the plane, the two different line projectors $\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}$ and $\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$ give squared residual distance one half for both coordinate unit vectors.

Thus diagonal observations determine how much coordinate energy is retained, but can conceal sign and orientation information. A reconstruction problem should distinguish this special endpoint case from a general uniqueness claim. Additional mixed-vector distance measurements can recover off-diagonal entries by polarization.

## Problem 37. Recover an off-diagonal entry by polarization

**Question.** For an unknown real orthogonal projector, suppose the squared residual distances for $e_1,e_2,e_1+e_2$ are $1/2,1/2,0$. Determine $p_{11},p_{22},p_{12}$ and interpret the result in two dimensions.

**Solution.** The squared residual distance for $x$ is $x^T(I-P)x$. Applying it to the two unit vectors gives $1-p_{11}=1/2$ and $1-p_{22}=1/2$. Expanding for their sum gives $2-p_{11}-p_{22}-2p_{12}=0$, so $p_{12}=1/2$.

In two dimensions this fixes $P=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}$, the projector onto the line spanned by $(1,1)^T$. The zero residual distance for their sum says precisely that this direction belongs to the range.

The mixed measurement contains a cross term that separate coordinate measurements cannot reveal. The sign is easy to reverse if one uses projected energy instead of residual energy without changing the expansion. Checking the known range direction provides an immediate independent sign check. In a larger ambient dimension these entries specify only a principal block; other directions may still require measurements, although the fixed mixed vector imposes additional constraints.

## Problem 38. A quadratic minimum with a projector penalty

**Question.** For an orthogonal projector $P$ and real $\lambda>0$, minimize $F(x)={\Vert x-b\Vert}^2+\lambda{\Vert Px\Vert}^2$. Give the minimum value.

**Solution.** Decompose $b=b_S+b_N$ and $x=x_S+x_N$ using the range and perpendicular kernel of $P$. Perpendicularity separates the objective into ${\Vert x_N-b_N\Vert}^2+{\Vert x_S-b_S\Vert}^2+\lambda{\Vert x_S\Vert}^2$. Completing the square in the range component gives the unique minimizer

$$x_*=(I-P)b+\frac1{1+\lambda}Pb.$$

The minimum is $\lambda{\Vert Pb\Vert}^2/(1+\lambda)$. The kernel component is left unchanged because the penalty does not act there; the range component is shrunk rather than removed entirely.

For $P=\operatorname{diag}(1,0)$, $b=(3,4)^T$ and $\lambda=2$, the answer is $(1,4)^T$ and the minimum is six. At finite positive penalty this map is generally not a projector: its range eigenvalue is $1/(1+\lambda)$, strictly between zero and one. As the penalty tends to infinity, it approaches the complementary projection. A shrinkage operator and an idempotent projection have different spectra and repeated-application behavior.

## Problem 39. Closest-point projection can fail outside a subspace

**Question.** A proposed theorem claims every nonempty set has one unique closest point to every target. Refute it with a finite set, and explain the missing structure in the linear projection theorem.

**Solution.** Take the set $C=\{(-1,0)^T,(1,0)^T\}$ and target zero. Both candidates have squared distance one, so the minimizer exists but is not unique. There is no single-valued closest-point map without an arbitrary selection rule.

In the linear subspace theorem, differences of feasible points remain in the subspace. This lets the perpendicular residual split the squared error by Pythagoras, with a strictly positive extra term for every different point. The two-point set lacks the required feasible directions, and it is not convex.

The example does not say that only subspaces have unique closest points: nonempty closed convex subsets of finite-dimensional Euclidean space do too, by a broader theorem. Their projection maps, however, need not be linear. For instance projection onto the nonnegative real half-line sends a scalar to its maximum with zero. The present chapter's matrix identities characterize linear orthogonal projections, not every nearest-point operation on every possible set.

## Problem 40. A tempting but false complement formula

**Question.** Let $P,Q$ be orthogonal projectors. Is $I-PQ$ always an orthogonal projection? Is $P+Q-PQ$ always the projector onto the sum of their ranges?

**Solution.** Use the horizontal projector and the forty-five-degree line projector from Problem7. Their product is $M=\frac12\begin{pmatrix}1&1\\0&0\end{pmatrix}$ and satisfies $M^2=M/2$, not $M$. The complement $I-M$ would be idempotent only if $M^2=M$, as expanding $(I-M)^2=I-M$ shows. It therefore fails.

The proposed sum expression equals $\begin{pmatrix}1&0\\1/2&1/2\end{pmatrix}$. It is nonsymmetric and does not equal the identity, even though the two nonparallel lines span the whole plane. Its square also differs from itself.

If $P$ and $Q$ commute, both formulas become valid orthogonal projectors: the first onto the complement of the intersection, the second onto the sum. Expanding a product of complements in a specified order is always algebraically valid, but concluding that the product is itself a projector requires the commutation hypothesis. Set identities alone do not license replacing intersection by arbitrary matrix multiplication.

## Problem 41. A universal energy identity forces orthogonality

**Question.** A real square matrix $E$ satisfies $E^2=E$ and ${\Vert Ex\Vert}^2+{\Vert(I-E)x\Vert}^2={\Vert x\Vert}^2$ for every real vector $x$. Prove that $E$ is an orthogonal projector. Would one tested input suffice?

**Solution.** Expanding the identity gives $x^T(2E^TE-E-E^T)x=0$ for every $x$. The matrix in parentheses is symmetric, so polarization or evaluating on coordinate sums shows that it is zero. Hence $2E^TE=E+E^T$.

Alternatively, decompose arbitrary $x=u+v$ with $u$ in the range and $v$ in the kernel of the idempotent. The proposed identity becomes ${\Vert u\Vert}^2+{\Vert v\Vert}^2={\Vert u+v\Vert}^2$, forcing $u^Tv=0$ for every such pair. Thus the range and kernel are perpendicular, identifying $E$ as the orthogonal projector.

One tested input is insufficient. The oblique projector $\begin{pmatrix}1&1\\0&0\end{pmatrix}$ satisfies the energy identity for input $e_1$, since it fixes that vector. It fails for input $e_2$: the projected and residual squared lengths are one and two, summing to three instead of one. Universal quantifiers distinguish operator identities from accidental equality on a sample.

## Problem 42. Determine containment from one scalar

**Question.** Orthogonal projectors $P,Q$ satisfy $\operatorname{tr}(PQ)=\operatorname{rank}(P)$. Prove that the range of $P$ is contained in the range of $Q$. Is this valid for arbitrary idempotents?

**Solution.** Choose an orthonormal basis $u_1,\ldots,u_r$ of the range of $P$. The trace is $\sum_i u_i^TQu_i=\sum_i{\Vert Qu_i\Vert}^2$. Each summand is at most one by contraction. Since the sum equals $r$, every summand equals one. The perpendicular energy split then forces $(I-Q)u_i=0$ for each basis vector, establishing containment.

The claim fails for general oblique idempotents. Take $P=\begin{pmatrix}1&0\\0&0\end{pmatrix}$ and $Q=\begin{pmatrix}1&0\\1&0\end{pmatrix}$. Both are idempotent, and the product has trace one, equal to the rank of $P$. But their ranges are different lines, generated by $(1,0)^T$ and $(1,1)^T$.

The proof's crucial bounded summands came from orthogonal contraction. Integer eigenvalues of the individual idempotents do not recover that positivity argument for arbitrary products. Trace equalities must be interpreted with their structural hypotheses.

## Problem 43. The difference of nested projectors

**Question.** Let $S\subseteq U$ with dimensions two and four in $\mathbb R^6$, and let $P,Q$ be their orthogonal projectors. Describe $Q-P$, its rank, trace and kernel. Describe $P-Q$ too.

**Solution.** Containment gives $QP=PQ=P$. Thus $(Q-P)^2=Q-2P+P=Q-P$, and symmetry is immediate. Its range is $U\cap S^\perp$, which has dimension $4-2=2$. It therefore has rank and trace two. Its kernel is the perpendicular direct sum $S+U^\perp$, of dimension $2+(6-4)=4$.

One can verify this action directly: vectors in $S$ are fixed by both and cancel; vectors in $U\cap S^\perp$ are fixed only by $Q$; vectors in $U^\perp$ are killed by both. These three perpendicular pieces exhaust the space.

The reverse difference $P-Q$ acts by minus one on the two-dimensional middle piece and zero elsewhere. Its square is $Q-P$, so it is not idempotent here. Its trace is minus two and rank two. A difference formula needs both containment and the correct sign; symmetry alone does not determine which difference is a projection.

## Problem 44. Rank changes invalidate a limiting shortcut

**Question.** Let $A_\varepsilon=\begin{pmatrix}1&1\\0&\varepsilon\end{pmatrix}$. Find the projector onto its columns and the coefficients fitting $b=e_2$ for nonzero $\varepsilon$. Compare with $\varepsilon=0$.

**Solution.** For nonzero $\varepsilon$, the determinant is $\varepsilon$, so the columns span the whole plane. The orthogonal projector is $I$, independent of the parameter. Solving $A_\varepsilon c=e_2$ gives $\varepsilon c_2=1$ and $c_1+c_2=0$, hence $c=(-1/\varepsilon,1/\varepsilon)^T$. Coefficients diverge as the parameter tends to zero, although the fitted vector remains exactly $e_2$.

At zero the columns coincide and span the horizontal line. Its projector is $\operatorname{diag}(1,0)$, and the projected target is zero, with squared residual distance one. Thus the limit of the projectors at nonzero parameters is not the projector of the limiting matrix.

The discontinuity occurs at a rank change. It does not contradict uniqueness for any fixed subspace or imply that every small perturbation produces a discontinuity at fixed rank. A numerical procedure declaring a tiny parameter to be zero changes the modeled subspace and needs an explicit rank policy.

## Problem 45. Best approximation from orthogonal measurements

**Question.** A vector $b$ has squared norm twenty-five. Its inner products with three orthonormal vectors are $2,-3,1$. Find the closest vector in their span and the distance. Could the three reported measurements instead be $4,3,2$?

**Solution.** Orthogonality decouples the measurements, so the closest vector is $p=2q_1-3q_2+q_3$. Its squared norm is $4+9+1=14$. Pythagoras gives residual squared norm $25-14=11$, so the distance is $\sqrt{11}$. The formula identifies a physical vector in the declared basis even if its ambient coordinates are not supplied.

The alternate measurements would have squared sum $16+9+4=29$, exceeding the target's squared norm twenty-five. They are impossible for three orthonormal measurement vectors, by the same perpendicular energy identity or Bessel's inequality. The contradiction could indicate wrong data, nonunit vectors, or nonorthogonal directions, but the question's stated assumptions rule all three measurements out together.

An incomplete orthonormal set need not recover all the input energy; the remaining eleven can lie in its perpendicular complement. Equality of measured and total energy would certify membership in the measured span. These are exact feasibility conclusions, not statistical estimates.

## Problem 46. Distance from a rank-one projector to another

**Question.** Let $P=uu^T$ and $Q=vv^T$ for real unit vectors. Derive their squared Frobenius distance and find its possible range. Does replacing $v$ by $-v$ change it?

**Solution.** The product is $PQ=u(u^Tv)v^T$, whose trace is $(u^Tv)^2$. Both ranks are one, so

$$ {\Vert P-Q\Vert}_F^2=2\bigl(1-(u^Tv)^2\bigr).$$

Cauchy–Schwarz bounds the squared dot product between zero and one. The squared distance lies between zero and two. Zero occurs exactly when the two lines coincide, including the case $v=-u$. Two occurs for perpendicular lines. Intermediate angles produce intermediate values.

Replacing $v$ by its negative leaves the outer product unchanged, and the squared dot product also remains unchanged. The distance compares *unoriented subspaces*, not signed unit-vector representatives. In contrast, the ordinary vector distance ${\Vert u-v\Vert}$ distinguishes $v=u$ from $v=-u$. The formula uses a matrix Frobenius norm, so interpreting its maximum as the Euclidean distance between the original endpoints would mix two spaces and two geometric objects.

## Problem 47. Projection onto a diagonal line in arbitrary dimension

**Question.** Project $b=(1,2,\ldots,m)^T$ onto the all-ones line in $\mathbb R^m$, for positive integer $m$. Find the squared distance and handle $m=1$.

**Solution.** With generator $u=(1,\ldots,1)^T$, the denominator $u^Tu=m$. The coefficient is the coordinate mean $(m+1)/2$. Thus every projected coordinate equals that mean and $P=uu^T/m$.

Using the sum and sum-of-squares formulas, the residual energy is

$$\sum_{j=1}^{m}\left(j-\frac{m+1}{2}\right)^2=\frac{m(m^2-1)}{12}.$$

To derive it, expand the square into $\sum j^2-(m+1)\sum j+m(m+1)^2/4$, then substitute $\sum j=m(m+1)/2$ and $\sum j^2=m(m+1)(2m+1)/6$. A common denominator twelve yields the stated expression. The residual sum is zero, proving perpendicularity to the all-ones direction.

At $m=1$, the line is the full space, the projector is the identity, and the formula gives zero error. Dividing by $m$ is valid because $m$ is positive; a zero-dimensional empty-data version is not included. This example connects centering to a projection while keeping the exact finite-dimensional assumptions explicit.

## Problem 48. Centering is a complementary projection

**Question.** For $m\ge2$, let $J=uu^T/m$ with $u$ the all-ones vector. Show that $C=I-J$ centers data, find its rank, and prove that centering twice has no further effect.

**Solution.** Each coordinate of $Jb$ is the mean $\bar b=\sum_i b_i/m$, so $Cb$ has coordinates $b_i-\bar b$. Their sum is zero. The matrix $J$ is symmetric and satisfies $J^2=J$ because $u^Tu=m$. Hence $C$ is symmetric and $C^2=I-2J+J^2=C$.

The centered space is $u^\perp$, of dimension $m-1$, so $C$ has rank and trace $m-1$. Its kernel is the all-ones line. Centering a vector already of zero sum leaves it unchanged, explaining idempotence operationally.

The energy identity becomes $\sum_i b_i^2=m\bar b^2+\sum_i(b_i-\bar b)^2$. The first term is the squared norm of the mean vector, not merely the square of the scalar mean. Omitting the factor $m$ confuses those objects. This deterministic identity does not by itself justify any statistical unbiasedness correction; such a claim requires a sampling model and belongs to the probability/statistics chapters.

## Problem 49. A coordinate formula can be algebraically idempotent but wrong

**Question.** For $A=\begin{pmatrix}1&0\\1&1\\0&1\end{pmatrix}$, a solution replaces its pivot columns by those of its reduced row-echelon form and constructs a projector from them. Demonstrate the error with a target.

**Solution.** The original columns are independent. The reduced form has columns $e_1,e_2$ in the ambient three-space, so the incorrect construction gives $P_{\rm wrong}=\operatorname{diag}(1,1,0)$. That is a valid projector, but onto a different plane. Row operations preserve linear relations among columns, not the physical column space in the original coordinates.

The original plane has normal $n=(1,-1,1)^T$, so its correct projector is $I-nn^T/3$. For target $b=e_3$, this gives $p=(-1/3,1/3,2/3)^T$, with squared residual distance one third. The incorrect projector gives zero and squared distance one.

Membership checks expose the error: the original plane satisfies $x_1-x_2+x_3=0$, but the wrongly selected basis direction $e_1$ violates that equation. Checking symmetry and idempotence alone certifies a closest-point map onto *its own* range, not that its range matches the subspace asked about. Use original pivot columns after reduction identifies their indices.

## Problem 50. Synthesize weighted projection, coordinates and uniqueness

**Question.** In $\mathbb R^2$ with $G=\begin{pmatrix}2&1\\1&2\end{pmatrix}$, project $b=(2,0)^T$ onto the line generated by $u=(1,-1)^T$. Find the matrix, point, residual and weighted energies. Why is the answer unique?

**Solution.** The metric has positive leading principal minors two and three, so it is positive definite. Here $Gu=u$, $u^TGu=2$, and $u^TGb=2$. Therefore the coefficient is one and $p=(1,-1)^T$, with $r=(1,1)^T$.

The weighted projector is $P_G=u(u^TGu)^{-1}u^TG=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$. It happens to be ordinarily symmetric in this example because the chosen line and its ordinary perpendicular complement are metric eigendirections. Ordinary symmetry is not generally guaranteed for a weighted projector.

The input energy is eight, the projected energy two, and the residual energy six. Their weighted cross term is zero because $u^TGr=0$. For every competing point $tu$ on the line, the error energy is six plus $2(1-t)^2$, proving unique minimality at one. The existence of a matrix formula is not the uniqueness proof; strict positivity of the metric on every nonzero feasible direction is. This closes the chapter by combining a concrete calculation with the underlying certificate.
