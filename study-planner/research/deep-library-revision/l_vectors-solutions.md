## Q1

**Correct option: 2.**

### Model the independent coordinates explicitly

A real symmetric four-by-four matrix has the form

$$S=\begin{pmatrix}d_1&a&b&c\\a&d_2&e&f\\b&e&d_3&g\\c&f&g&d_4\end{pmatrix}.$$

The six off-diagonal coordinates $a,b,c,e,f,g$ are unconstrained; symmetry means each is copied into a second entry, not independently chosen twice. Trace zero means $d_1+d_2+d_3+d_4=0$, so $d_4=-d_1-d_2-d_3$. Thus all admissible matrices are uniquely described by nine real parameters: six off-diagonal entries and three diagonal entries. This unique parameterization proves dimension nine.

A concrete basis is $E_{ij}+E_{ji}$ for $1\le i<j\le4$, together with $E_{11}-E_{44},E_{22}-E_{44},E_{33}-E_{44}$. Every element is symmetric and trace zero. A zero linear combination forces the six off-diagonal coefficients to vanish by inspecting their entries, and then forces the three remaining coefficients to vanish by inspecting the first three diagonal entries. The nine matrices are therefore independent and span the space.

Option 1's ten ignores the trace restriction. Options 3 and 4 remove two or three dimensions instead of the rank-one constraint. Trace zero does not mean zero diagonal: $\operatorname{diag}(1,-1,0,0)$ is a valid nonzero diagonal element. The trace functional has rank one because it takes value one on $E_{11}$; writing equivalent copies of its equation does not create extra rank.

For positive size $n$, the corresponding real dimension is $n(n+1)/2-1$. At $n=1$ the space contains only zero and has dimension zero. At $n=0$, trace is already zero on the zero-dimensional space, so a separate dimension-zero answer is required; subtracting one would be invalid.

### Exact verification ledger


| Parameter family | Independent count | Why |
|---|---|---|
| Off-diagonal symmetric pairs | 6 | Upper and lower entries are linked. |
| Trace-zero diagonal entries | 3 | The fourth cancels the other three. |
| Total | 9 | The two families form an independent basis. |


## Q2

**Correct option: 2.**

The hypothesis controls magnitude, not the sign of a quadratic form. Take $A=-I$ and $\theta=1$. For every vector and every norm, $\Vert Ax\Vert=\Vert-x\Vert=\Vert x\Vert$. Yet for every nonzero real $x$, $x^TAx=-\Vert x\Vert_2^2<0$. Thus positive definiteness does not follow, and option 2 is the false general assertion.

To check option 3, suppose $Ax=0$. The bound gives $0\ge\theta\Vert x\Vert$, and $\theta>0$ forces $x=0$. A square real matrix with a trivial kernel is invertible. This uses squareness: a tall injective rectangular map need not have a two-sided inverse.

For option 1, put $x=A^{-1}y$ in the original inequality. Then $\Vert y\Vert\ge\theta\Vert A^{-1}y\Vert$. Dividing by $\theta\Vert y\Vert$ for $y\ne0$ and taking the supremum yields the corresponding induced operator norm bound

$$\Vert A^{-1}\Vert\le\theta^{-1}.$$

For a real eigenvalue with real eigenvector $v\ne0$, substituting $Av=\lambda v$ directly gives $|\lambda|\ge\theta$. Nonreal eigenvalues need an additional argument because the original vectors are real. With the Euclidean norm, write a complex eigenvector $v=u+iw$ and apply the squared real bound to $u$ and $w$ separately. Adding gives $\Vert Av\Vert_2^2\ge\theta^2\Vert v\Vert_2^2$, hence the same modulus bound.

The conclusion also holds for any finite-dimensional real norm with its induced matrix norm. Set $B=A^{-1}$; then $\Vert B^k\Vert\le\theta^{-k}$. Norm equivalence gives constants $c,C>0$ with $c\Vert x\Vert_2\le\Vert x\Vert\le C\Vert x\Vert_2$ on real vectors. Therefore $\Vert B^k x\Vert_2\le(C/c)\theta^{-k}\Vert x\Vert_2$. Extend this upper Euclidean bound to complex vectors by summing the bounds for real and imaginary parts. For an eigenvalue $\mu$ of $B$, it gives $|\mu|^k\le(C/c)\theta^{-k}$. Taking $k$th roots and letting $k$ grow gives $|\mu|\le\theta^{-1}$, so the eigenvalue $\lambda=1/\mu$ of $A$ has $|\lambda|\ge\theta$. This justifies option 4 without silently imposing a Euclidean norm on the source's unqualified notation.

Finite-dimensional norm equivalence here follows by bounding a norm on the Euclidean unit sphere: continuity follows from the triangle inequality and coordinate expansion, the compact sphere has a finite maximum, and its minimum is positive because a norm vanishes only at zero. The complex argument is an extension of a real norm bound, not an assertion that the original real norm is automatically a complex inner product.

## Q3

**Source ambiguity; intended normalized interpretation: option 3.**

### Read the source hypothesis literally

The original Persian page says “orthogonal basis” and does not explicitly state unit lengths. Orthogonal and orthonormal are different hypotheses. For a nonunit orthogonal basis, the correct orthogonal projection formula is

$$P_Ux=\sum_{k=1}^{n}\frac{\langle u_k,x\rangle}{\langle u_k,u_k\rangle}u_k.$$

The source omits these denominators. To see why this matters, take $U=\operatorname{span}(2,0)$ in $\mathbb R^2$. Its displayed operator is $P_s=\operatorname{diag}(4,0)$, whereas the actual orthogonal projection is $\operatorname{diag}(1,0)$. Applying $P_s$ twice gives $\operatorname{diag}(16,0)$, so option 1's idempotence assertion fails. For $x=(0,1)$, $P_sx=0$ and option 3's inequality is also false. Thus the literal hypothesis does not supply one uniquely false general assertion. No official answer key is asserted here.

If “orthogonal” was intended to include normalization in the source convention, the extra orthonormal hypothesis gives the usual educational answer, option 3. The following proof states that interpretation explicitly rather than silently changing the authentic wording.

### Under the orthonormal interpretation

Let $p=Px$ and $r=x-p$. For each basis vector $u_j$, orthonormality gives

$$\langle r,u_j\rangle=\langle x,u_j\rangle-\sum_{k=1}^{n}\langle x,u_k\rangle\langle u_k,u_j\rangle=0.$$

Thus $p\in U$ and $r\perp U$. Pythagoras proves $\Vert x\Vert_2^2=\Vert Px\Vert_2^2+\Vert x-Px\Vert_2^2$. The universally valid direction is $\Vert Px\Vert_2\le\Vert x\Vert_2$, with equality precisely when $x\in U$. The reverse inequality fails on a proper subspace: for $U=\operatorname{span}(1,0)$ and $x=(0,1)$, it reads $1\le0$.

Linearity of the coefficient functionals gives option 4, and outputs lie in $U$ by construction. For $x\in U$, the orthonormal expansion recovers $x$, proving option 2 and the stronger $Px=x$. Applying this fact to $Px\in U$ proves $P^2=P$, option 1.

**Full-space boundary.** The source allows $n=m$. With an orthonormal basis of the entire space, $P=I$, so option 3 holds with equality and all four assertions hold for that particular configuration. It is false as a general projection theorem, not false for every possible subspace or vector.

Finally, idempotence alone does not imply contraction: $Q=\begin{pmatrix}1&2\\0&0\end{pmatrix}$ has $Q^2=Q$ but sends $(0,1)$ to $(2,0)$. Orthogonality supplies the norm decomposition; a projection must be identified by its actual geometry and formula.


### Exact verification ledger


| Hypothesis | Displayed sum idempotent? | Reverse norm inequality |
|---|---|---|
| Literal nonunit orthogonal basis | Not generally; $u=(2,0)$ disproves it. | Not generally; a perpendicular input disproves it. |
| Orthonormal basis of a proper subspace | Yes | Fails on a nonzero perpendicular vector. |
| Orthonormal basis of the full space | Yes; $P=I$ | Equality for every vector. |


## Q4

**Correct option: 2.**

The source matrix is $A=(1-a)I+a\mathbf1\mathbf1^T$ in three dimensions. Every real vector can be written uniquely as $x=s\mathbf1+z$, with $s=(x_1+x_2+x_3)/3$ and $z_1+z_2+z_3=0$. The two terms are orthogonal. Expanding the quadratic form gives

$$x^TAx=3(1+2a)s^2+(1-a)\Vert z\Vert_2^2.$$

If $a\ge1$, choose nonzero $z=(1,-1,0)$ and $s=0$; the form is nonpositive. If $a\le-1/2$, choose $s=1,z=0$; again the form is nonpositive. Thus strict positive definiteness requires $1-a>0$ and $1+2a>0$.

Conversely, if both coefficients are positive, every nonzero $x$ has either $s\ne0$ or $z\ne0$, and the displayed sum is strictly positive. This proves sufficiency directly, without importing an unexplained eigenvalue criterion. The exact interval is $-1/2<a<1$, option 2.

Option 1 permits, for example, $a=-3/4$, where the all-equal direction gives $3(1+2a)=-3/2$. Option 3 unnecessarily rejects $a=3/4$, where both coefficients are positive. Option 4 unnecessarily rejects $a=-1/4$, also valid, and excludes $a=0$, the identity matrix. At $a=-1/2$, the all-equal line is null; at $a=1$, the sum-zero plane is null. Both endpoints are positive semidefinite but not positive definite. Outside the closed interval, a direction of negative quadratic form exists.

For $n\ge2$ with the analogous real symmetric matrix, the decomposition yields coefficients $1+(n-1)a$ and $1-a$, hence strict range $-1/(n-1)<a<1$. At $n=1$, there are no off-diagonal entries: the matrix is simply $(1)$ and places no restriction on the unused parameter. The special dimension-one case must not be inferred by dividing by zero in the general endpoint.

## Q5

**Correct option: 2.**

For $n=5$, symmetry leaves five diagonal plus ten upper-triangular parameters. Trace removes one diagonal freedom, leaving $10+4=14$, option 2. The alternatives 24, 15, and 10 respectively impose trace on all matrices without symmetry, omit trace, or impose a zero diagonal instead of a zero trace. A diagonal matrix with entries $(1,-1,0,0,0)$ witnesses the last distinction.

### Derivation and transfer


A symmetric real $n$-by-$n$ matrix is specified by $n$ diagonal entries and $\binom n2$ upper-triangular entries. The lower-triangular entries are copies, not extra degrees of freedom. Therefore its unconstrained dimension is $n(n+1)/2$. Trace zero gives one independent homogeneous equation, because the trace functional is nonzero: it takes value one on $E_{11}$. Choose the first $n-1$ diagonal entries freely and set the last to their negative sum.

An explicit basis consists of $E_{ij}+E_{ji}$ for $i<j$ and $E_{ii}-E_{nn}$ for $i<n$. Off-diagonal entries show independence of the first family; the first $n-1$ diagonal entries then show independence of the second. Every symmetric trace-zero matrix is their unique linear combination. This proves

$$\dim W=\binom n2+(n-1)=\frac{n(n+1)}2-1\quad(n\ge1).$$

At $n=1$, only the zero matrix remains and the basis is empty. At size zero, there is already a zero-dimensional space and no rank-one trace restriction, so the displayed subtraction is not used. Repeating the trace equation or multiplying it by a nonzero scalar does not add constraints. Requiring every diagonal entry to vanish is stronger than trace zero: the diagonal entries 1 and $-1$ can cancel.

## Q6

**Correct option: 1.**

For $n=8$, there are $\binom82=28$ free off-diagonal entries and seven free diagonal entries after trace zero. Their sum is 35, option 1. The distractor 63 counts all trace-zero matrices, 36 omits trace, and 28 removes every diagonal entry. The seven diagonal basis matrices $E_{ii}-E_{88}$ show concretely which freedoms the answer 28 loses.

### Derivation and transfer


A symmetric real $n$-by-$n$ matrix is specified by $n$ diagonal entries and $\binom n2$ upper-triangular entries. The lower-triangular entries are copies, not extra degrees of freedom. Therefore its unconstrained dimension is $n(n+1)/2$. Trace zero gives one independent homogeneous equation, because the trace functional is nonzero: it takes value one on $E_{11}$. Choose the first $n-1$ diagonal entries freely and set the last to their negative sum.

An explicit basis consists of $E_{ij}+E_{ji}$ for $i<j$ and $E_{ii}-E_{nn}$ for $i<n$. Off-diagonal entries show independence of the first family; the first $n-1$ diagonal entries then show independence of the second. Every symmetric trace-zero matrix is their unique linear combination. This proves

$$\dim W=\binom n2+(n-1)=\frac{n(n+1)}2-1\quad(n\ge1).$$

At $n=1$, only the zero matrix remains and the basis is empty. At size zero, there is already a zero-dimensional space and no rank-one trace restriction, so the displayed subtraction is not used. Repeating the trace equation or multiplying it by a nonzero scalar does not add constraints. Requiring every diagonal entry to vanish is stronger than trace zero: the diagonal entries 1 and $-1$ can cancel.

## Q7

**Correct option: 4.**

Option 4 is $n(n+1)/2-1$ throughout the positive-integer domain. The alternatives $n^2-1$, $n(n+1)/2$, and $n(n-1)/2$ respectively discard symmetry, discard trace zero, and replace it by zero diagonal. At $n=2$, the true space consists of $\begin{pmatrix}a&b\\b&-a\end{pmatrix}$ and has two parameters, making the difference visible without a counting slogan.

### Derivation and transfer


A symmetric real $n$-by-$n$ matrix is specified by $n$ diagonal entries and $\binom n2$ upper-triangular entries. The lower-triangular entries are copies, not extra degrees of freedom. Therefore its unconstrained dimension is $n(n+1)/2$. Trace zero gives one independent homogeneous equation, because the trace functional is nonzero: it takes value one on $E_{11}$. Choose the first $n-1$ diagonal entries freely and set the last to their negative sum.

An explicit basis consists of $E_{ij}+E_{ji}$ for $i<j$ and $E_{ii}-E_{nn}$ for $i<n$. Off-diagonal entries show independence of the first family; the first $n-1$ diagonal entries then show independence of the second. Every symmetric trace-zero matrix is their unique linear combination. This proves

$$\dim W=\binom n2+(n-1)=\frac{n(n+1)}2-1\quad(n\ge1).$$

At $n=1$, only the zero matrix remains and the basis is empty. At size zero, there is already a zero-dimensional space and no rank-one trace restriction, so the displayed subtraction is not used. Repeating the trace equation or multiplying it by a nonzero scalar does not add constraints. Requiring every diagonal entry to vanish is stronger than trace zero: the diagonal entries 1 and $-1$ can cancel.

## Q8

**Correct option: 3.**

Option 3 correctly gives rank one for the real trace equation. Symmetry prevents all entries from being independent, and redundant equations do not each lower dimension. Trace zero permits nonzero diagonal cancellation. For example the constraints $\operatorname{tr}S=0$ and $2\operatorname{tr}S=0$ together still have rank one; their written number two is not their independent rank.

### Derivation and transfer


A symmetric real $n$-by-$n$ matrix is specified by $n$ diagonal entries and $\binom n2$ upper-triangular entries. The lower-triangular entries are copies, not extra degrees of freedom. Therefore its unconstrained dimension is $n(n+1)/2$. Trace zero gives one independent homogeneous equation, because the trace functional is nonzero: it takes value one on $E_{11}$. Choose the first $n-1$ diagonal entries freely and set the last to their negative sum.

An explicit basis consists of $E_{ij}+E_{ji}$ for $i<j$ and $E_{ii}-E_{nn}$ for $i<n$. Off-diagonal entries show independence of the first family; the first $n-1$ diagonal entries then show independence of the second. Every symmetric trace-zero matrix is their unique linear combination. This proves

$$\dim W=\binom n2+(n-1)=\frac{n(n+1)}2-1\quad(n\ge1).$$

At $n=1$, only the zero matrix remains and the basis is empty. At size zero, there is already a zero-dimensional space and no rank-one trace restriction, so the displayed subtraction is not used. Repeating the trace equation or multiplying it by a nonzero scalar does not add constraints. Requiring every diagonal entry to vanish is stronger than trace zero: the diagonal entries 1 and $-1$ can cancel.

## Q9

**Correct option: 4.**

At $n=5$, both subspaces have dimension ten and their sum has dimension fifteen. The identity gives $\dim(U\cap V)=10+10-15=5$, option 4. A zero intersection would make the sum dimension twenty; intersection dimension ten would make U and V equal with sum ten; fifteen exceeds either subspace dimension. Thus each distractor contradicts a different supplied constraint.

### Derivation and transfer


To justify the sum formula, start with a basis of $U\cap V$ of size $r$. Extend it separately to bases of $U$ and $V$, of sizes $p$ and $q$. The union of the shared basis and the two added lists spans $U+V$. It is independent: a zero relation puts the combination of U-only added vectors in both $U$ and $V$; expressing it in the shared basis and using independence in $U$ forces its added coefficients to vanish. Independence in $V$ then forces the other coefficients to vanish. Hence

$$\dim(U+V)=p+q-r.$$

With $p=q=2n$ and sum dimension $3n$, $r=4n-3n=n$. Attainability is constructive: in $\mathbb R^{3n}$, let $U=\operatorname{span}(e_1,\ldots,e_{2n})$ and $V=\operatorname{span}(e_{n+1},\ldots,e_{3n})$. Their intersection has basis $e_{n+1},\ldots,e_{2n}$.

If the sum dimension is unspecified, equal individual dimensions do not determine overlap. They can coincide, or have smaller intersection when the ambient dimension permits. In an ambient space of dimension $d$, necessarily $\max(0,p+q-d)\le r\le\min(p,q)$. An embedding that preserves the actual U and V does not change their intersection; relative position and the feasible ambient dimension are separate issues.

## Q10

**Correct option: 3.**

At $n=8$, the dimensions are sixteen, sixteen, and twenty-four. Therefore the intersection has dimension eight, option 3. Zero would force sum dimension thirty-two; sixteen would force the subspaces to coincide; twenty-four exceeds each subspace's dimension. In the constructive coordinate example the shared directions are exactly $e_9,\ldots,e_{16}$, eight vectors.

### Derivation and transfer


To justify the sum formula, start with a basis of $U\cap V$ of size $r$. Extend it separately to bases of $U$ and $V$, of sizes $p$ and $q$. The union of the shared basis and the two added lists spans $U+V$. It is independent: a zero relation puts the combination of U-only added vectors in both $U$ and $V$; expressing it in the shared basis and using independence in $U$ forces its added coefficients to vanish. Independence in $V$ then forces the other coefficients to vanish. Hence

$$\dim(U+V)=p+q-r.$$

With $p=q=2n$ and sum dimension $3n$, $r=4n-3n=n$. Attainability is constructive: in $\mathbb R^{3n}$, let $U=\operatorname{span}(e_1,\ldots,e_{2n})$ and $V=\operatorname{span}(e_{n+1},\ldots,e_{3n})$. Their intersection has basis $e_{n+1},\ldots,e_{2n}$.

If the sum dimension is unspecified, equal individual dimensions do not determine overlap. They can coincide, or have smaller intersection when the ambient dimension permits. In an ambient space of dimension $d$, necessarily $\max(0,p+q-d)\le r\le\min(p,q)$. An embedding that preserves the actual U and V does not change their intersection; relative position and the feasible ambient dimension are separate issues.

## Q11

**Correct option: 2.**

Option 2's $n$ follows by rearranging the proved dimension identity. The proposals zero, $2n$, and $3n$ respectively impose a direct sum, impose coincident subspaces, or exceed their individual dimensions. It is the dimension of the actual sum, rather than a sum of unrelated labels, that fixes the intersection.

### Derivation and transfer


To justify the sum formula, start with a basis of $U\cap V$ of size $r$. Extend it separately to bases of $U$ and $V$, of sizes $p$ and $q$. The union of the shared basis and the two added lists spans $U+V$. It is independent: a zero relation puts the combination of U-only added vectors in both $U$ and $V$; expressing it in the shared basis and using independence in $U$ forces its added coefficients to vanish. Independence in $V$ then forces the other coefficients to vanish. Hence

$$\dim(U+V)=p+q-r.$$

With $p=q=2n$ and sum dimension $3n$, $r=4n-3n=n$. Attainability is constructive: in $\mathbb R^{3n}$, let $U=\operatorname{span}(e_1,\ldots,e_{2n})$ and $V=\operatorname{span}(e_{n+1},\ldots,e_{3n})$. Their intersection has basis $e_{n+1},\ldots,e_{2n}$.

If the sum dimension is unspecified, equal individual dimensions do not determine overlap. They can coincide, or have smaller intersection when the ambient dimension permits. In an ambient space of dimension $d$, necessarily $\max(0,p+q-d)\le r\le\min(p,q)$. An embedding that preserves the actual U and V does not change their intersection; relative position and the feasible ambient dimension are separate issues.

## Q12

**Correct option: 1.**

Option 1 correctly distinguishes union from sum. The coordinate axes in $\mathbb R^2$ have a union that omits $(1,1)$, but their sum is the whole plane. All subspaces contain zero, so they are never disjoint as sets. The revised fourth alternative, claiming individual dimensions determine intersection regardless of relative positions, is false: two lines in the plane can coincide or be distinct, giving intersection dimensions one or zero. The former phrase about independence of the ambient space was ambiguous and is replaced rather than defended.

### Derivation and transfer


To justify the sum formula, start with a basis of $U\cap V$ of size $r$. Extend it separately to bases of $U$ and $V$, of sizes $p$ and $q$. The union of the shared basis and the two added lists spans $U+V$. It is independent: a zero relation puts the combination of U-only added vectors in both $U$ and $V$; expressing it in the shared basis and using independence in $U$ forces its added coefficients to vanish. Independence in $V$ then forces the other coefficients to vanish. Hence

$$\dim(U+V)=p+q-r.$$

With $p=q=2n$ and sum dimension $3n$, $r=4n-3n=n$. Attainability is constructive: in $\mathbb R^{3n}$, let $U=\operatorname{span}(e_1,\ldots,e_{2n})$ and $V=\operatorname{span}(e_{n+1},\ldots,e_{3n})$. Their intersection has basis $e_{n+1},\ldots,e_{2n}$.

If the sum dimension is unspecified, equal individual dimensions do not determine overlap. They can coincide, or have smaller intersection when the ambient dimension permits. In an ambient space of dimension $d$, necessarily $\max(0,p+q-d)\le r\le\min(p,q)$. An embedding that preserves the actual U and V does not change their intersection; relative position and the feasible ambient dimension are separate issues.

## Q13

**Correct option: 1.**

For $n=5$, $A$ is eight-by-six with rank four. The kernel dimension is $6-4=2$, option 1. The alternatives five, six, and eight are respectively the parameter itself, the domain size before subtracting rank, and the codomain size. The explicit witness retains coordinates 1–4 and kills coordinates 5–6; it does not lose all six coordinates.

### Derivation and transfer


The matrix acts on column vectors in $\mathbb R^{n+1}$ and takes values in $\mathbb R^{n+3}$. Nullity concerns the kernel in the domain, whose dimension is the column count. To prove rank–nullity, take a basis of the kernel and extend it to a basis of the domain. The images of the added vectors span the image because every domain vector has this expansion and kernel terms disappear. Those images are independent: a zero image of an added-vector combination would put it in the kernel, contradicting independence of the extended basis. The number added equals the rank, proving domain dimension equals nullity plus rank.

Consequently

$$\operatorname{nullity}A=(n+1)-(n-1)=2.$$

The shape is feasible for every $n\ge1$. A concrete witness sends $(x_1,\ldots,x_{n+1})$ to $(x_1,\ldots,x_{n-1},0,0,0,0)$, a vector with $n+3$ coordinates. Its kernel is spanned by $e_n,e_{n+1}$. At $n=1$, this is the zero map from dimension two to dimension four and still has nullity two. The parameter $n=0$ would require negative rank and is not a valid instance. The transpose has domain dimension $n+3$ and the same rank, hence nullity four, not two.

## Q14

**Correct option: 4.**

For $n=8$, the shape is eleven-by-nine and rank is seven. Therefore nullity is $9-7=2$, option 4. Values eight, nine, and eleven mistake the parameter, domain, or codomain for kernel dimension. The corresponding transpose has nullity $11-7=4$, explaining why row count belongs to a different map.

### Derivation and transfer


The matrix acts on column vectors in $\mathbb R^{n+1}$ and takes values in $\mathbb R^{n+3}$. Nullity concerns the kernel in the domain, whose dimension is the column count. To prove rank–nullity, take a basis of the kernel and extend it to a basis of the domain. The images of the added vectors span the image because every domain vector has this expansion and kernel terms disappear. Those images are independent: a zero image of an added-vector combination would put it in the kernel, contradicting independence of the extended basis. The number added equals the rank, proving domain dimension equals nullity plus rank.

Consequently

$$\operatorname{nullity}A=(n+1)-(n-1)=2.$$

The shape is feasible for every $n\ge1$. A concrete witness sends $(x_1,\ldots,x_{n+1})$ to $(x_1,\ldots,x_{n-1},0,0,0,0)$, a vector with $n+3$ coordinates. Its kernel is spanned by $e_n,e_{n+1}$. At $n=1$, this is the zero map from dimension two to dimension four and still has nullity two. The parameter $n=0$ would require negative rank and is not a valid instance. The transpose has domain dimension $n+3$ and the same rank, hence nullity four, not two.

## Q15

**Correct option: 3.**

Option 3's constant two is correct throughout the feasible positive domain. The choices $n$, $n+1$, and $n+3$ cannot replace domain-minus-rank. A rank value alone is insufficient: the same rank-seven map can have domain dimension seven with trivial kernel or domain dimension nine with two kernel freedoms.

### Derivation and transfer


The matrix acts on column vectors in $\mathbb R^{n+1}$ and takes values in $\mathbb R^{n+3}$. Nullity concerns the kernel in the domain, whose dimension is the column count. To prove rank–nullity, take a basis of the kernel and extend it to a basis of the domain. The images of the added vectors span the image because every domain vector has this expansion and kernel terms disappear. Those images are independent: a zero image of an added-vector combination would put it in the kernel, contradicting independence of the extended basis. The number added equals the rank, proving domain dimension equals nullity plus rank.

Consequently

$$\operatorname{nullity}A=(n+1)-(n-1)=2.$$

The shape is feasible for every $n\ge1$. A concrete witness sends $(x_1,\ldots,x_{n+1})$ to $(x_1,\ldots,x_{n-1},0,0,0,0)$, a vector with $n+3$ coordinates. Its kernel is spanned by $e_n,e_{n+1}$. At $n=1$, this is the zero map from dimension two to dimension four and still has nullity two. The parameter $n=0$ would require negative rank and is not a valid instance. The transpose has domain dimension $n+3$ and the same rank, hence nullity four, not two.

## Q16

**Correct option: 2.**

Option 2 correctly uses the column dimension for action on column vectors. A rectangular matrix can have a large kernel, and transposing changes the domain. For $A=\begin{pmatrix}1&0&0\end{pmatrix}$, rank is one and nullity two, whereas its transpose has domain dimension one and nullity zero. Equal rank does not imply equal nullity when the domain changes.

### Derivation and transfer


The matrix acts on column vectors in $\mathbb R^{n+1}$ and takes values in $\mathbb R^{n+3}$. Nullity concerns the kernel in the domain, whose dimension is the column count. To prove rank–nullity, take a basis of the kernel and extend it to a basis of the domain. The images of the added vectors span the image because every domain vector has this expansion and kernel terms disappear. Those images are independent: a zero image of an added-vector combination would put it in the kernel, contradicting independence of the extended basis. The number added equals the rank, proving domain dimension equals nullity plus rank.

Consequently

$$\operatorname{nullity}A=(n+1)-(n-1)=2.$$

The shape is feasible for every $n\ge1$. A concrete witness sends $(x_1,\ldots,x_{n+1})$ to $(x_1,\ldots,x_{n-1},0,0,0,0)$, a vector with $n+3$ coordinates. Its kernel is spanned by $e_n,e_{n+1}$. At $n=1$, this is the zero map from dimension two to dimension four and still has nullity two. The parameter $n=0$ would require negative rank and is not a valid instance. The transpose has domain dimension $n+3$ and the same rank, hence nullity four, not two.

## Q17

**Correct option: 2.**

For $n=5$, $w=(5,1,2)$, $c=6/2=3$, and $p=(3,3,0)$. Its squared norm is $9+9=18$, option 2. The alternatives 30, 3, and 8 count the original squared norm, the coefficient, and the squared projection onto the different line $(1,-1,0)$. Residual $(2,-2,2)$ has squared norm twelve; $30=18+12$ checks the orthogonal decomposition.

### Derivation and transfer


Let $p=cu$ with $u=(1,1,0)$. Residual orthogonality gives $0=u\cdot(w-cu)=n+1-2c$, so $c=(n+1)/2$ and $p=((n+1)/2,(n+1)/2,0)$. Taking its squared Euclidean norm gives

$$\Vert p\Vert_2^2=2\left(\frac{n+1}{2}\right)^2=\frac{(n+1)^2}{2}.$$

The four related quantities are coefficient $c=(n+1)/2$, signed component $s=(n+1)/\sqrt2$ along the unit direction $u/\sqrt2$, vector $p=cu$, and squared length $s^2$. They are not interchangeable. The residual is $((n-1)/2,(1-n)/2,2)$, whose dot product with $u$ is zero, so the proposed vector is the actual nearest point on the line.

For any nonzero real scaling $v=tu$, the coefficient becomes $(n+1)/(2t)$ but multiplying it by $tu$ gives the same $p$. At scaling zero the formula divides by zero, while projection onto the resulting zero subspace is defined as zero. The expression remains valid for every real $n$, although the question uses positive integers; at $n=-1$ the vector is perpendicular to the line and the projection vanishes.

### Exact verification ledger


| Requested object | Exact value at $n=5$ |
|---|---|
| Coefficient along nonunit $u$ | $3$ |
| Signed component along unit direction | $3\sqrt2$ |
| Projected vector | $(3,3,0)$ |
| Squared projection norm | $18$ |


## Q18

**Correct option: 1.**

For $n=8$, the coefficient is $9/2$ and the projected vector is $(9/2,9/2,0)$. Its squared norm is $81/2$, option 1. The alternatives 69, $9/2$, and $49/2$ represent the full vector's squared norm, its coefficient, and projection onto the opposite diagonal. Residual $(7/2,-7/2,2)$ has squared norm $57/2$, and $81/2+57/2=69$.

### Derivation and transfer


Let $p=cu$ with $u=(1,1,0)$. Residual orthogonality gives $0=u\cdot(w-cu)=n+1-2c$, so $c=(n+1)/2$ and $p=((n+1)/2,(n+1)/2,0)$. Taking its squared Euclidean norm gives

$$\Vert p\Vert_2^2=2\left(\frac{n+1}{2}\right)^2=\frac{(n+1)^2}{2}.$$

The four related quantities are coefficient $c=(n+1)/2$, signed component $s=(n+1)/\sqrt2$ along the unit direction $u/\sqrt2$, vector $p=cu$, and squared length $s^2$. They are not interchangeable. The residual is $((n-1)/2,(1-n)/2,2)$, whose dot product with $u$ is zero, so the proposed vector is the actual nearest point on the line.

For any nonzero real scaling $v=tu$, the coefficient becomes $(n+1)/(2t)$ but multiplying it by $tu$ gives the same $p$. At scaling zero the formula divides by zero, while projection onto the resulting zero subspace is defined as zero. The expression remains valid for every real $n$, although the question uses positive integers; at $n=-1$ the vector is perpendicular to the line and the projection vanishes.

## Q19

**Correct option: 4.**

Option 4 is $(n+1)^2/2$. The alternatives $n^2+5$, $(n+1)/2$, and $(n-1)^2/2$ use the unprojected squared norm, the coefficient, and the other diagonal's component. At $n=1$, the answer is two and the entire third coordinate remains residual; the original squared norm six cannot be the projected squared norm.

### Derivation and transfer


Let $p=cu$ with $u=(1,1,0)$. Residual orthogonality gives $0=u\cdot(w-cu)=n+1-2c$, so $c=(n+1)/2$ and $p=((n+1)/2,(n+1)/2,0)$. Taking its squared Euclidean norm gives

$$\Vert p\Vert_2^2=2\left(\frac{n+1}{2}\right)^2=\frac{(n+1)^2}{2}.$$

The four related quantities are coefficient $c=(n+1)/2$, signed component $s=(n+1)/\sqrt2$ along the unit direction $u/\sqrt2$, vector $p=cu$, and squared length $s^2$. They are not interchangeable. The residual is $((n-1)/2,(1-n)/2,2)$, whose dot product with $u$ is zero, so the proposed vector is the actual nearest point on the line.

For any nonzero real scaling $v=tu$, the coefficient becomes $(n+1)/(2t)$ but multiplying it by $tu$ gives the same $p$. At scaling zero the formula divides by zero, while projection onto the resulting zero subspace is defined as zero. The expression remains valid for every real $n$, although the question uses positive integers; at $n=-1$ the vector is perpendicular to the line and the projection vanishes.

## Q20

**Correct option: 3.**

Option 3 correctly requires division by the squared direction norm. Here $u\cdot u=2$. Using the dot product $n+1$ as the coefficient gives twice the correct projected vector. Rescaling a nonzero generator leaves its line unchanged: replacing u by $2u$ halves the coefficient and leaves $p$ intact. A generator of a line need not be unit length.

### Derivation and transfer


Let $p=cu$ with $u=(1,1,0)$. Residual orthogonality gives $0=u\cdot(w-cu)=n+1-2c$, so $c=(n+1)/2$ and $p=((n+1)/2,(n+1)/2,0)$. Taking its squared Euclidean norm gives

$$\Vert p\Vert_2^2=2\left(\frac{n+1}{2}\right)^2=\frac{(n+1)^2}{2}.$$

The four related quantities are coefficient $c=(n+1)/2$, signed component $s=(n+1)/\sqrt2$ along the unit direction $u/\sqrt2$, vector $p=cu$, and squared length $s^2$. They are not interchangeable. The residual is $((n-1)/2,(1-n)/2,2)$, whose dot product with $u$ is zero, so the proposed vector is the actual nearest point on the line.

For any nonzero real scaling $v=tu$, the coefficient becomes $(n+1)/(2t)$ but multiplying it by $tu$ gives the same $p$. At scaling zero the formula divides by zero, while projection onto the resulting zero subspace is defined as zero. The expression remains valid for every real $n$, although the question uses positive integers; at $n=-1$ the vector is perpendicular to the line and the projection vanishes.

## Q21

**Correct option: 2.**

At $n=5$, $r=(2,-2,2)$, so its squared norm is $4+4+4=12$, option 2. The choices 18 and 30 count projected and total squared norms; four counts only the third-coordinate contribution and misses the first two residual coordinates. The check $18+12=30$ verifies both the arithmetic and the type of quantity.

### Derivation and transfer


Compute the residual itself before invoking any subtraction rule. The projection onto $(1,1,0)$ is $((n+1)/2,(n+1)/2,0)$. Hence

$$r=w-p=\left(\frac{n-1}{2},\frac{1-n}{2},2\right),\qquad \Vert r\Vert_2^2=\frac{(n-1)^2}{2}+4.$$

The dot product with the line direction is $(n-1)/2+(1-n)/2=0$. Therefore the two components are orthogonal and Pythagoras permits the second route

$$\Vert r\Vert_2^2=n^2+5-\frac{(n+1)^2}{2}=\frac{(n-1)^2}{2}+4.$$

The third coordinate contributes an unavoidable four because the target line has third coordinate zero. The first two coordinates contribute another nonnegative term, vanishing only at $n=1$. Thus the residual is never zero in this family, although its projection can be nonzero. For arbitrary decompositions $w=p+r$, the exact expansion includes $2p\cdot r$; discarding that term is permitted here only after orthogonality is checked. For complex geometry use $2\operatorname{Re}\langle p,r\rangle$ and actual complex orthogonality, not merely a real-looking coordinate picture.

## Q22

**Correct option: 1.**

At $n=8$, the residual is $(7/2,-7/2,2)$ and its squared norm is $49/4+49/4+4=57/2$, option 1. The proposed $81/2$ is projected energy, 69 is total energy, and four omits the nonzero diagonal imbalance. A length would be $\sqrt{57/2}$, but the requested quantity is its square.

### Derivation and transfer


Compute the residual itself before invoking any subtraction rule. The projection onto $(1,1,0)$ is $((n+1)/2,(n+1)/2,0)$. Hence

$$r=w-p=\left(\frac{n-1}{2},\frac{1-n}{2},2\right),\qquad \Vert r\Vert_2^2=\frac{(n-1)^2}{2}+4.$$

The dot product with the line direction is $(n-1)/2+(1-n)/2=0$. Therefore the two components are orthogonal and Pythagoras permits the second route

$$\Vert r\Vert_2^2=n^2+5-\frac{(n+1)^2}{2}=\frac{(n-1)^2}{2}+4.$$

The third coordinate contributes an unavoidable four because the target line has third coordinate zero. The first two coordinates contribute another nonnegative term, vanishing only at $n=1$. Thus the residual is never zero in this family, although its projection can be nonzero. For arbitrary decompositions $w=p+r$, the exact expansion includes $2p\cdot r$; discarding that term is permitted here only after orthogonality is checked. For complex geometry use $2\operatorname{Re}\langle p,r\rangle$ and actual complex orthogonality, not merely a real-looking coordinate picture.

## Q23

**Correct option: 4.**

Option 4 is $(n-1)^2/2+4$. The projected expression $(n+1)^2/2$ uses the wrong component; $n^2+5$ includes both components; the constant four is correct only at the exceptional value $n=1$. Agreement at that one point does not establish a formula for all n.

### Derivation and transfer


Compute the residual itself before invoking any subtraction rule. The projection onto $(1,1,0)$ is $((n+1)/2,(n+1)/2,0)$. Hence

$$r=w-p=\left(\frac{n-1}{2},\frac{1-n}{2},2\right),\qquad \Vert r\Vert_2^2=\frac{(n-1)^2}{2}+4.$$

The dot product with the line direction is $(n-1)/2+(1-n)/2=0$. Therefore the two components are orthogonal and Pythagoras permits the second route

$$\Vert r\Vert_2^2=n^2+5-\frac{(n+1)^2}{2}=\frac{(n-1)^2}{2}+4.$$

The third coordinate contributes an unavoidable four because the target line has third coordinate zero. The first two coordinates contribute another nonnegative term, vanishing only at $n=1$. Thus the residual is never zero in this family, although its projection can be nonzero. For arbitrary decompositions $w=p+r$, the exact expansion includes $2p\cdot r$; discarding that term is permitted here only after orthogonality is checked. For complex geometry use $2\operatorname{Re}\langle p,r\rangle$ and actual complex orthogonality, not merely a real-looking coordinate picture.

## Q24

**Correct option: 3.**

Option 3 correctly conditions squared-norm subtraction on orthogonality. Take the oblique decomposition $(1,1)=(2,0)+(-1,1)$. The total squared norm is two, while the component squares sum to six; their cross term is $2(2,0)\cdot(-1,1)=-4$. In the present family p and r are perpendicular, so the cross term vanishes. A nonzero residual neither belongs to the projection line nor forces the projection to vanish.

### Derivation and transfer


Compute the residual itself before invoking any subtraction rule. The projection onto $(1,1,0)$ is $((n+1)/2,(n+1)/2,0)$. Hence

$$r=w-p=\left(\frac{n-1}{2},\frac{1-n}{2},2\right),\qquad \Vert r\Vert_2^2=\frac{(n-1)^2}{2}+4.$$

The dot product with the line direction is $(n-1)/2+(1-n)/2=0$. Therefore the two components are orthogonal and Pythagoras permits the second route

$$\Vert r\Vert_2^2=n^2+5-\frac{(n+1)^2}{2}=\frac{(n-1)^2}{2}+4.$$

The third coordinate contributes an unavoidable four because the target line has third coordinate zero. The first two coordinates contribute another nonnegative term, vanishing only at $n=1$. Thus the residual is never zero in this family, although its projection can be nonzero. For arbitrary decompositions $w=p+r$, the exact expansion includes $2p\cdot r$; discarding that term is permitted here only after orthogonality is checked. For complex geometry use $2\operatorname{Re}\langle p,r\rangle$ and actual complex orthogonality, not merely a real-looking coordinate picture.

## Q25

**Correct option: 4.**

For $n=5$, cancellation requires $a+10=0$, so $a=-10$, option 4. Substitution gives products $-10$ and $10$, summing to zero. The choices 10, $-5$, and 5 give dot products 20, 5, and 15 respectively, so none is perpendicular. The sign is determined by the equation rather than by a length formula.

### Derivation and transfer


Under the standard real Euclidean inner product, orthogonality means the sum of coordinate products is zero. For $u=(1,n)$ and $v=(a,2)$,

$$u\cdot v=a+2n=0\quad\Longleftrightarrow\quad a=-2n.$$

The products in the two coordinates need not vanish separately: they cancel. Both vectors are nonzero because their first and second fixed entries are nonzero, so their angle is indeed a right angle after the dot-product condition is met. A negative dot product would indicate an obtuse angle, not perpendicularity.

The conclusion depends on the metric. Under the positive-definite weighted product $\langle x,y\rangle_D=4x_1y_1+x_2y_2$, the equation is $4a+2n=0$, giving $a=-n/2$. For the Euclidean answer $a=-2n$, this weighted product is $-6n$, not zero unless $n=0$. Positivity of the weights gives a valid geometry, but does not preserve every perpendicular pair. In a general linear parameter equation $ca+d=0$, first check $c\ne0$ before division; if $c=0$, the constraint is either impossible or satisfied by every a.

## Q26

**Correct option: 3.**

For $n=8$, $a+16=0$ gives $a=-16$, option 3. The other candidates $-8$, 8, and 16 yield dot products 8, 24, and 32. All are positive and therefore not zero. Computing the signed scalar dot product directly distinguishes the valid negative parameter from distractors of the same magnitude class.

### Derivation and transfer


Under the standard real Euclidean inner product, orthogonality means the sum of coordinate products is zero. For $u=(1,n)$ and $v=(a,2)$,

$$u\cdot v=a+2n=0\quad\Longleftrightarrow\quad a=-2n.$$

The products in the two coordinates need not vanish separately: they cancel. Both vectors are nonzero because their first and second fixed entries are nonzero, so their angle is indeed a right angle after the dot-product condition is met. A negative dot product would indicate an obtuse angle, not perpendicularity.

The conclusion depends on the metric. Under the positive-definite weighted product $\langle x,y\rangle_D=4x_1y_1+x_2y_2$, the equation is $4a+2n=0$, giving $a=-n/2$. For the Euclidean answer $a=-2n$, this weighted product is $-6n$, not zero unless $n=0$. Positivity of the weights gives a valid geometry, but does not preserve every perpendicular pair. In a general linear parameter equation $ca+d=0$, first check $c\ne0$ before division; if $c=0$, the constraint is either impossible or satisfied by every a.

## Q27

**Correct option: 2.**

Option 2 is $-2n$. Substituting $2n$, $-n$, and $n$ leaves dot products $4n$, $n$, and $3n$, positive for every n in the stated domain. At $n=0$, some formulas coincide, which is why checking a single degenerate value cannot prove the symbolic result.

### Derivation and transfer


Under the standard real Euclidean inner product, orthogonality means the sum of coordinate products is zero. For $u=(1,n)$ and $v=(a,2)$,

$$u\cdot v=a+2n=0\quad\Longleftrightarrow\quad a=-2n.$$

The products in the two coordinates need not vanish separately: they cancel. Both vectors are nonzero because their first and second fixed entries are nonzero, so their angle is indeed a right angle after the dot-product condition is met. A negative dot product would indicate an obtuse angle, not perpendicularity.

The conclusion depends on the metric. Under the positive-definite weighted product $\langle x,y\rangle_D=4x_1y_1+x_2y_2$, the equation is $4a+2n=0$, giving $a=-n/2$. For the Euclidean answer $a=-2n$, this weighted product is $-6n$, not zero unless $n=0$. Positivity of the weights gives a valid geometry, but does not preserve every perpendicular pair. In a general linear parameter equation $ca+d=0$, first check $c\ne0$ before division; if $c=0$, the constraint is either impossible or satisfied by every a.

## Q28

**Correct option: 1.**

Option 1 correctly requires specifying the inner product. Euclidean orthogonality uses $a=-2n$; weights $(4,1)$ require $a=-n/2$. Individual coordinate products may be nonzero, and a negative dot product is not zero. The vector space operations and the algebraic span stay the same when the inner product changes, but perpendicularity and nearest-point geometry can change.

### Derivation and transfer


Under the standard real Euclidean inner product, orthogonality means the sum of coordinate products is zero. For $u=(1,n)$ and $v=(a,2)$,

$$u\cdot v=a+2n=0\quad\Longleftrightarrow\quad a=-2n.$$

The products in the two coordinates need not vanish separately: they cancel. Both vectors are nonzero because their first and second fixed entries are nonzero, so their angle is indeed a right angle after the dot-product condition is met. A negative dot product would indicate an obtuse angle, not perpendicularity.

The conclusion depends on the metric. Under the positive-definite weighted product $\langle x,y\rangle_D=4x_1y_1+x_2y_2$, the equation is $4a+2n=0$, giving $a=-n/2$. For the Euclidean answer $a=-2n$, this weighted product is $-6n$, not zero unless $n=0$. Positivity of the weights gives a valid geometry, but does not preserve every perpendicular pair. In a general linear parameter equation $ca+d=0$, first check $c\ne0$ before division; if $c=0$, the constraint is either impossible or satisfied by every a.

## Q29

**Correct option: 4.**

At $n=5$, the equations are $c_1+c_2=5$ and $c_1-c_2=2$. Their solution is $(7/2,3/2)$, so the first coordinate is $7/2$, option 4. The distractor $3/2$ is the second coordinate; 5 is the first standard coordinate; 10 doubles that coordinate without solving the basis equations. Reconstruction gives $(5,2)$ exactly.

### Derivation and transfer


Write $v=c_1b_1+c_2b_2$ in the stated ordered basis. Comparing ordinary coordinates gives $c_1+c_2=n$ and $c_1-c_2=2$. Add the equations to obtain $c_1=(n+2)/2$ and subtract them to obtain $c_2=(n-2)/2$. Reconstruction verifies both entries:

$$\frac{n+2}{2}(1,1)+\frac{n-2}{2}(1,-1)=(n,2).$$

The coefficient list is unique because a zero combination has both coefficient sum and difference zero, forcing both coefficients to vanish. The basis is orthogonal, but each squared length is two, not one. Thus dot-product extraction must divide by two. A coordinate vector and the represented geometric vector are different objects: their norms satisfy $\Vert v\Vert_2^2=2(c_1^2+c_2^2)=n^2+4$, not simply $c_1^2+c_2^2$.

Swapping the basis order swaps the two coefficients. Introducing a dependent generator creates multiple representations, whereas changing from one actual basis to another retains uniqueness in each chosen coordinate system. For real $n=2$ the second coefficient vanishes; this means the vector lies along $b_1$, not that the basis loses independence.

## Q30

**Correct option: 3.**

At $n=8$, the equations give $(c_1,c_2)=(5,3)$, so option 3 is correct. The alternative 3 is the second coefficient, 8 the standard x-coordinate, and 16 an unjustified doubling. The metric check is $2(25+9)=68=8^2+2^2$, confirming that this nonunit basis changes the coordinate norm formula.

### Derivation and transfer


Write $v=c_1b_1+c_2b_2$ in the stated ordered basis. Comparing ordinary coordinates gives $c_1+c_2=n$ and $c_1-c_2=2$. Add the equations to obtain $c_1=(n+2)/2$ and subtract them to obtain $c_2=(n-2)/2$. Reconstruction verifies both entries:

$$\frac{n+2}{2}(1,1)+\frac{n-2}{2}(1,-1)=(n,2).$$

The coefficient list is unique because a zero combination has both coefficient sum and difference zero, forcing both coefficients to vanish. The basis is orthogonal, but each squared length is two, not one. Thus dot-product extraction must divide by two. A coordinate vector and the represented geometric vector are different objects: their norms satisfy $\Vert v\Vert_2^2=2(c_1^2+c_2^2)=n^2+4$, not simply $c_1^2+c_2^2$.

Swapping the basis order swaps the two coefficients. Introducing a dependent generator creates multiple representations, whereas changing from one actual basis to another retains uniqueness in each chosen coordinate system. For real $n=2$ the second coefficient vanishes; this means the vector lies along $b_1$, not that the basis loses independence.

## Q31

**Correct option: 2.**

Option 2's $(n+2)/2$ is the first coefficient. The alternatives $(n-2)/2$, n, and $2n$ refer to the second coefficient, the first standard coordinate, or an unproved scaling. The first coefficient is determined by two component equations, not by copying the supplied tuple into a new basis.

### Derivation and transfer


Write $v=c_1b_1+c_2b_2$ in the stated ordered basis. Comparing ordinary coordinates gives $c_1+c_2=n$ and $c_1-c_2=2$. Add the equations to obtain $c_1=(n+2)/2$ and subtract them to obtain $c_2=(n-2)/2$. Reconstruction verifies both entries:

$$\frac{n+2}{2}(1,1)+\frac{n-2}{2}(1,-1)=(n,2).$$

The coefficient list is unique because a zero combination has both coefficient sum and difference zero, forcing both coefficients to vanish. The basis is orthogonal, but each squared length is two, not one. Thus dot-product extraction must divide by two. A coordinate vector and the represented geometric vector are different objects: their norms satisfy $\Vert v\Vert_2^2=2(c_1^2+c_2^2)=n^2+4$, not simply $c_1^2+c_2^2$.

Swapping the basis order swaps the two coefficients. Introducing a dependent generator creates multiple representations, whereas changing from one actual basis to another retains uniqueness in each chosen coordinate system. For real $n=2$ the second coefficient vanishes; this means the vector lies along $b_1$, not that the basis loses independence.

## Q32

**Correct option: 1.**

Option 1 correctly links coordinate order to basis order. The vector $(5,2)$ has coordinates $(7/2,3/2)$ in $(b_1,b_2)$ and $(3/2,7/2)$ in $(b_2,b_1)$. A dependent spanning list does not have unique coefficients: appending $b_1+b_2$ allows one to add t to its coefficient while subtracting t from each old coefficient. This changes descriptions without changing the vector.

### Derivation and transfer


Write $v=c_1b_1+c_2b_2$ in the stated ordered basis. Comparing ordinary coordinates gives $c_1+c_2=n$ and $c_1-c_2=2$. Add the equations to obtain $c_1=(n+2)/2$ and subtract them to obtain $c_2=(n-2)/2$. Reconstruction verifies both entries:

$$\frac{n+2}{2}(1,1)+\frac{n-2}{2}(1,-1)=(n,2).$$

The coefficient list is unique because a zero combination has both coefficient sum and difference zero, forcing both coefficients to vanish. The basis is orthogonal, but each squared length is two, not one. Thus dot-product extraction must divide by two. A coordinate vector and the represented geometric vector are different objects: their norms satisfy $\Vert v\Vert_2^2=2(c_1^2+c_2^2)=n^2+4$, not simply $c_1^2+c_2^2$.

Swapping the basis order swaps the two coefficients. Introducing a dependent generator creates multiple representations, whereas changing from one actual basis to another retains uniqueness in each chosen coordinate system. For real $n=2$ the second coefficient vanishes; this means the vector lies along $b_1$, not that the basis loses independence.

## Q33

**Correct option: 1.**

For six ambient coordinates, freely choose the first five and use the sixth to cancel their sum. The dimension is five, option 1. The alternatives six, one, and four are the ambient dimension, the rank of the sum functional, and subtraction of an extra nonexistent independent equation. For instance $(1,-1,0,0,0,0)$ belongs and shows that coordinates need not vanish individually.

### Derivation and transfer


The homogeneous coordinate-sum equation in $\mathbb R^{n+1}$ can be solved without elimination machinery: choose $x_1,\ldots,x_n$ freely and put $x_{n+1}=-(x_1+\cdots+x_n)$. The parameterization is linear, injective, and reaches every vector with sum zero. Consequently the dimension is n.

The explicit basis is $e_i-e_{n+1}$ for $1\le i\le n$. Each has sum zero, every solution is their combination with coefficients $x_i$, and inspecting its first n coordinates proves independence. The equation is a nonzero real linear functional of rank one; its kernel dimension therefore agrees with $(n+1)-1$.

Replacing the right side by a nonzero constant c gives $ce_{n+1}+W$, an affine translate of the homogeneous kernel W. It still has n free parameters but does not contain zero and is not a vector subspace. At $n=0$, the homogeneous condition on $\mathbb R^1$ forces its only coordinate to zero; dimension is zero and the basis is empty. Cancellation, rather than individual coordinate vanishing, is the defining restriction.

## Q34

**Correct option: 4.**

For nine ambient coordinates, the eight independent basis vectors $e_i-e_9$ span the kernel. Hence dimension is eight, option 4. Nine ignores the restriction, one mistakes the functional's image dimension for its kernel dimension, and seven subtracts a second restriction not present in the statement.

### Derivation and transfer


The homogeneous coordinate-sum equation in $\mathbb R^{n+1}$ can be solved without elimination machinery: choose $x_1,\ldots,x_n$ freely and put $x_{n+1}=-(x_1+\cdots+x_n)$. The parameterization is linear, injective, and reaches every vector with sum zero. Consequently the dimension is n.

The explicit basis is $e_i-e_{n+1}$ for $1\le i\le n$. Each has sum zero, every solution is their combination with coefficients $x_i$, and inspecting its first n coordinates proves independence. The equation is a nonzero real linear functional of rank one; its kernel dimension therefore agrees with $(n+1)-1$.

Replacing the right side by a nonzero constant c gives $ce_{n+1}+W$, an affine translate of the homogeneous kernel W. It still has n free parameters but does not contain zero and is not a vector subspace. At $n=0$, the homogeneous condition on $\mathbb R^1$ forces its only coordinate to zero; dimension is zero and the basis is empty. Cancellation, rather than individual coordinate vanishing, is the defining restriction.

## Q35

**Correct option: 3.**

Option 3 is n. The choices $n+1$, one, and $n-1$ confuse the ambient dimension, rank, or an extra constraint with nullity. A rank-one equation eliminates exactly one degree of freedom because it is genuinely nonzero; an identically zero equation would eliminate none.

### Derivation and transfer


The homogeneous coordinate-sum equation in $\mathbb R^{n+1}$ can be solved without elimination machinery: choose $x_1,\ldots,x_n$ freely and put $x_{n+1}=-(x_1+\cdots+x_n)$. The parameterization is linear, injective, and reaches every vector with sum zero. Consequently the dimension is n.

The explicit basis is $e_i-e_{n+1}$ for $1\le i\le n$. Each has sum zero, every solution is their combination with coefficients $x_i$, and inspecting its first n coordinates proves independence. The equation is a nonzero real linear functional of rank one; its kernel dimension therefore agrees with $(n+1)-1$.

Replacing the right side by a nonzero constant c gives $ce_{n+1}+W$, an affine translate of the homogeneous kernel W. It still has n free parameters but does not contain zero and is not a vector subspace. At $n=0$, the homogeneous condition on $\mathbb R^1$ forces its only coordinate to zero; dimension is zero and the basis is empty. Cancellation, rather than individual coordinate vanishing, is the defining restriction.

## Q36

**Correct option: 2.**

Option 2 correctly classifies a nonzero constant-sum set as affine. If its right side is six, $(6,0,\ldots,0)$ is feasible but its double has sum twelve and lies outside. Zero is also infeasible. The homogeneous set permits nonzero cancellation vectors and is a subspace. Having the same number of parameters as a subspace does not make an affine translate a vector space under the original operations.

### Derivation and transfer


The homogeneous coordinate-sum equation in $\mathbb R^{n+1}$ can be solved without elimination machinery: choose $x_1,\ldots,x_n$ freely and put $x_{n+1}=-(x_1+\cdots+x_n)$. The parameterization is linear, injective, and reaches every vector with sum zero. Consequently the dimension is n.

The explicit basis is $e_i-e_{n+1}$ for $1\le i\le n$. Each has sum zero, every solution is their combination with coefficients $x_i$, and inspecting its first n coordinates proves independence. The equation is a nonzero real linear functional of rank one; its kernel dimension therefore agrees with $(n+1)-1$.

Replacing the right side by a nonzero constant c gives $ce_{n+1}+W$, an affine translate of the homogeneous kernel W. It still has n free parameters but does not contain zero and is not a vector subspace. At $n=0$, the homogeneous condition on $\mathbb R^1$ forces its only coordinate to zero; dimension is zero and the basis is empty. Cancellation, rather than individual coordinate vanishing, is the defining restriction.

## Q37

**Correct option: 1.**

### Solve the Gram equations, not separate projections

Set $p=au+bv=(a+b,b,a)$ with $u=(1,0,1)$ and $v=(1,1,0)$. The dot products are $u\cdot u=v\cdot v=2$, $u\cdot v=1$, $u\cdot w=4$, and $v\cdot w=3$. Residual orthogonality to both generators gives

$$\begin{pmatrix}2&1\\1&2\end{pmatrix}\begin{pmatrix}a\\b\end{pmatrix}=\begin{pmatrix}4\\3\end{pmatrix}.$$

Twice the first equation minus the second gives $3a=5$, hence $a=5/3$. Substitute back to get $b=2/3$. Therefore $p=(7/3,2/3,5/3)$, option 1, and $r=w-p=(-4/3,4/3,4/3)$. Dotting r with either generator gives zero. Moreover $\Vert r\Vert^2=16/3$, $\Vert p\Vert^2=26/3$, and their sum 14 equals $\Vert w\Vert^2$.

The span satisfies $x_1=x_2+x_3$. Option 2's w violates this equation. Option 3's $(4,3,4)$ violates it and also fails residual orthogonality. Option 4's $(2,1,1)$ lies in the span, but its residual $(-1,1,2)$ has dot products 1 and 0 with u and v; one zero test is insufficient. The naive sum of separate projections is $2u+(3/2)v=(7/2,3/2,2)$, which also fails the two residual tests.

The Gram matrix is positive definite: $2a^2+2ab+2b^2=(a+b)^2+a^2+b^2>0$ for nonzero coefficients. This proves uniqueness. For any alternative q in the span, $\Vert w-q\Vert^2=\Vert r\Vert^2+\Vert p-q\Vert^2$, proving nearest-point optimality without assuming it from the drawing.

### Exact verification ledger


| Check | Exact result |
|---|---|
| Foot membership | $7/3=2/3+5/3$ |
| Residual dot $u$ | $-4/3+4/3=0$ |
| Residual dot $v$ | $-4/3+4/3=0$ |
| Energy split | $14=26/3+16/3$ |


## Q38

**Correct option: 1.**

The normal is $n=(2,-1,2)$, with squared length nine. For target $X=(1,2,3)$ the signed plane-equation residual is $n\cdot X-4=2-2+6-4=2$. Seek the foot as $Q=X-tn$. Substitution into the plane equation gives $6-9t=4$, so $t=2/9$ and

$$Q=\left(\frac59,\frac{20}9,\frac{23}9\right),\qquad X-Q=\frac29(2,-1,2).$$

The correction has length $(2/9)\cdot3=2/3$, option 1. Check membership: $2(5/9)-20/9+2(23/9)=36/9=4$. Every other plane point differs from Q by a vector perpendicular to n, so Pythagoras proves that no other point is closer.

Option 2's two is the unnormalized equation residual. Option 3's three is the normal length itself. Option 4's $1/3$ misses the numerator factor two. Distinguish the coefficient $2/9$, distance $2/3$, and squared distance $4/9$. Scaling the entire equation to $4x-2y+4z=8$ doubles both residual and normal length and leaves the distance unchanged. A zero normal requires handling the whole-space or inconsistent-empty-set case separately; the quotient assumes a nonzero normal.

## Q39

**Correct option: 2.**

Let the coefficients be r,s,t. A zero combination gives $r+s=0$, $r+t=0$, and $s+at=0$. The first two force $s=t=-r$; the third is $-(1+a)r=0$. For $a\ne-1$, this forces all coefficients zero and proves independence, option 2. At $a=-1$, coefficients $(1,-1,-1)$ give a concrete nontrivial relation.

Option 1 excludes a valid value 1 but includes the invalid value $-1$. Option 3 unnecessarily requires positivity: zero and $-2$ are both valid. Option 4 excludes the valid value zero while retaining the invalid value $-1$. The exceptional parameter is determined by the coefficient equation, not by a sign intuition about coordinates.

The generator matrix has determinant $-(a+1)$, a second calculation consistent with the direct proof. At $a=-1$, the first two vectors remain independent and the third is their difference, so the rank is exactly two rather than zero or one. Their cross product is $(1,-1,-1)$ and its dot product with the third vector is $-(1+a)$; this is the signed volume whose vanishing detects the same degeneracy. A zero volume need not mean every pair is parallel.

## Q40

**Correct option: 1.**

The affine constraint is $x+y+z=6$. Cauchy–Schwarz with normal $(1,1,1)$ gives $36\le3(x^2+y^2+z^2)$, hence squared norm at least twelve. Equality requires the vector to be a scalar multiple of the normal; its coordinate sum makes that multiple two. The feasible attaining vector is $(2,2,2)$, so option 1 gives the exact minimum and optimizer.

An explicit complete-square certificate is

$$x^2+y^2+z^2=12+(x-2)^2+(y-2)^2+(z-2)^2$$

on the constrained plane, because expanding the right side uses $x+y+z=6$. The extra squares vanish simultaneously only at $(2,2,2)$, proving uniqueness. Option 2's $(6,0,0)$ is feasible but has squared norm 36, not the minimum. Option 3's $(1,2,3)$ has squared norm fourteen rather than six. Option 4's zero vector is not feasible.

For a nonzero real normal a and plane $a\cdot x=d$, the same argument gives minimum squared norm $d^2/\Vert a\Vert^2$, attained at $d a/\Vert a\Vert^2$. If $d=0$, the minimum is zero at zero. If a is zero, first decide whether the equation is vacuous or inconsistent. A lower bound without a feasible equality case would not complete the optimization.

## Q41

**Correct option: 1.**

The coefficient equations are $c_1+c_2=3$ and $c_1-c_2=1$, giving $(c_1,c_2)=(2,1)$. Reconstruction gives $2(1,1)+(1,-1)=(3,1)$. The physical squared norm is $3^2+1^2=10$, option 1.

The basis Gram matrix is $G=\begin{pmatrix}2&0\\0&2\end{pmatrix}$, since the two basis vectors are perpendicular but each has norm $\sqrt2$. Thus a coordinate column c has squared norm $c^TGc=2(2^2+1^2)=10$. Option 3 correctly finds the coordinates but computes their unweighted squared norm five, assuming a normalized basis. Option 2 uses the raw dot products 4 and 2 as coordinates and would reconstruct $(6,2)$; its reported twenty is not the target's norm. Option 4 retains the standard coordinate tuple instead of converting it to the stated basis.

For a general real basis matrix B, $x=Bc$ implies $\Vert x\Vert^2=c^TB^TBc$. A nonorthogonal basis produces cross terms in its Gram matrix; an orthogonal nonunit basis produces diagonal weights; only an orthonormal basis produces the identity. Coordinates describe a vector, while the Gram matrix describes its geometry in those coordinates.

### Exact verification ledger


| Description | Value |
|---|---|
| Standard coordinate tuple | $(3,1)$ |
| Ordered basis coordinate tuple | $(2,1)$ |
| Basis Gram matrix | $2I$ |
| Physical squared norm | $2(2^2+1^2)=10$ |


## Q42

**Correct option: 1.**

The definition conjugates the first argument. Since $\overline1=1$ and $\overline i=-i$,

$$\langle u,v\rangle=1\cdot i+(-i)\cdot1=0,\qquad \Vert u\Vert^2=1\cdot1+(-i)i=2.$$

This is option 1. Option 2 omits conjugation in both calculations, producing $2i$ and $1+i^2=0$. Option 3 uses the wrong un-conjugated cross product but the correct norm. Option 4 uses the correct cross product but a bilinear self-product that vanishes for a nonzero vector. Positive definiteness rules out that last purported norm.

Conjugate symmetry gives $\langle v,u\rangle=\overline{\langle u,v\rangle}=0$ here; it does not say the two ordered products always agree. For one-dimensional vectors 1 and i, the products are i and $-i$. Under the stated convention, the coefficient of projection along a nonzero b is $\langle b,x\rangle/\langle b,b\rangle$. As a diagnostic, projecting $x=ib$ must give coefficient i, whereas using the reversed numerator gives $-i$ and the wrong vector. Every scalar movement and formula must follow the same convention.

## Q43

**Correct option: 3.**

Choose an orthonormal basis of the target plane. The assumed nonzero x is perpendicular to each basis vector, so every projection coefficient vanishes and $Px=0$. Therefore $x-Px=x$ and the requested ratio is one, option 3.

Option 1's zero would describe x lying in the plane. Option 2's one half imposes an unexplained split of its length. Option 4 ignores that the perpendicularity condition fixes the result for every plane. The nonzero assumption ensures the denominator is positive; at x zero the written ratio would be $0/0$ and undefined, despite the projection being well-defined.

For arbitrary nonzero x, the orthogonal decomposition gives $0\le\Vert x-Px\Vert/\Vert x\Vert\le1$. The ratio equals zero exactly for vectors in the plane and one exactly for perpendicular vectors, since those cases force one squared component to vanish. Intermediate ratios correspond to a mixture of plane and normal components. For example $x=(1,0,1)$ with the xy-plane gives ratio $1/\sqrt2$, showing why neither a fixed half nor a norm-squared fraction may be substituted for the actual length ratio.

## Q44

**Correct option: 3.**

The lengths are three and four, and the dot product is twelve. Hence $u\cdot v=\Vert u\Vert\Vert v\Vert>0$, equality in Cauchy–Schwarz. A direct residual calculation proves the dependence and its sign:

$$\left\Vert v-\frac43u\right\Vert^2=16-2\frac43\cdot12+\frac{16}9\cdot9=0.$$

Positive definiteness forces $v=(4/3)u$, a positive multiple, so they point in the same direction: option 3. Option 1 is contradicted by this nontrivial relation; option 2 would require dot product zero. The squared sum norm is $9+16+24=49$, not 25, rejecting option 4. The squared difference norm is $9+16-24=1$, an additional check.

The Gram matrix $\begin{pmatrix}9&12\\12&16\end{pmatrix}$ has determinant zero and kernel coefficient vector $(-4/3,1)$. If the dot product were $-12$, dependence would still hold but the scalar would be $-4/3$ and the directions opposite. A feasible dot product lies in $[-12,12]$; values beyond these endpoints cannot describe vectors in positive-definite inner-product geometry. Positive individual lengths do not guarantee an independent pair.

## Q45

**Correct option: 2.**

Let $p=cu+dw=(c+d,c,d)$ for the two stated generators. Their squared norms are two, their dot product is one, and their dot products with v are each one. Enforcing both residual orthogonality equations gives $2c+d=1$ and $c+2d=1$. Subtract them to get c=d; then $3c=1$. Thus $p=(2/3,1/3,1/3)$, option 2.

The residual is $(-2/3,2/3,2/3)$ and is perpendicular to both generators. Its squared norm is $4/3$ while the projection squared norm is $2/3$; their sum two equals $\Vert v\Vert^2$. The plane is characterized by first coordinate equal to the sum of the other two. Option 1's $(1,1,1)$ violates this. Option 3's $(0,1/2,1/2)$ and option 4's $(1/2,1/2,1/2)$ also fail membership. The naive sum of separate line projections is $(1,1/2,1/2)$: it lies in the plane, but its residual has dot product $-1/2$ with each generator, so membership alone does not verify projection.

For any other plane point q, the error separates as $\Vert v-q\Vert^2=4/3+\Vert p-q\Vert^2$. This proves both optimality and uniqueness. Gram equations keep the nonzero cross inner product that the separate-projection shortcut loses.

## Q46

**Correct option: 2.**

Both constraints imply $x=z=1-y$. Conversely every real y produces a feasible vector, so the entire feasible set is the affine line $(1,0,1)+y(-1,1,-1)$. Its squared norm is

$$F(y)=2(1-y)^2+y^2=3\left(y-\frac23\right)^2+\frac23.$$

The nonnegative square proves a global lower bound $2/3$, attained uniquely at $y=2/3$, hence $x=z=1/3$. This is option 2. Option 1's $1/3$ omits two coordinate squares at the attaining point. The values one and two can occur elsewhere but are not minimal: $y=1$ gives one and $y=0$ gives two. The requested squared norm differs from the actual minimum norm $\sqrt{2/3}$.

At the minimizing point, the dot product with the line direction is $(1/3)(-1)+(2/3)(1)+(1/3)(-1)=0$. Thus it is the projection of the origin onto this affine line, providing a geometric proof consistent with completing the square. For a feasible displacement $t(-1,1,-1)$ from it, the squared norm becomes $2/3+3t^2$, which certifies unique optimality. Solving the constraints first avoids searching over infeasible vectors or treating a nonhomogeneous solution set as a subspace.

### Exact verification ledger


| Feasible parameter $y$ | Feasible vector | Squared norm |
|---|---|---|
| $0$ | $(1,0,1)$ | $2$ |
| $2/3$ | $(1/3,2/3,1/3)$ | $2/3$ |
| $1$ | $(0,1,0)$ | $1$ |

