# Vector Spaces, Subspaces, Bases, and Dimension

## 1. Sources, scope, and how to study this chapter

This chapter develops the algebra that makes a collection of numbers, polynomials, matrices, functions, or signals into a vector space. The goal is to recognize the structure of a question before doing arithmetic: identify the scalar field, identify the actual operations, distinguish a generating list from a basis, and count independent freedoms rather than symbols. Gaussian elimination and determinants are prerequisites. No knowledge of eigenvectors, orthogonal projection algorithms, or abstract algebra beyond the field definition is assumed.

Four written university courses form the core synthesis: Oxford M1 Linear Algebra I, Michaelmas 2022, taught by Andrew Wathen; ETH Zürich Linear Algebra, HS2024, with notes by Bernd Gärtner; MIT 18.06SC, Fall 2011, Gilbert Strang; and Stanford EE263, Autumn 2007–08, Stephen Boyd. The source audit records exact documents, reading locations, candidate comparisons, and corrections. Oxford and ETH supply the proof structure; MIT supplies the computational distinction between column generators and coefficient dependencies; Stanford supplies coordinate recovery and measurement interpretations. CMU and Harvard candidates were also checked, but their relevant notes require qualifications and do not replace the four core courses.

The assessed scope includes vector-space axioms, subspace tests, span, independence, basis construction, exchange, dimension, coordinate systems, sums and intersections, direct sums, polynomial and matrix spaces, field dependence, elementary quotient and dual-space connections, and the pitfalls of infinite-dimensional examples. Linear maps receive the definitions needed here; their full operator theory belongs to the following linear-algebra chapter. The worked bank contains authentic examination adaptations, course-calibrated reconstructions, and original problems. Source exercises are attributed where reconstructed. This is a finite, documented source comparison, not a claim that every course ever offered has been inspected. Coverage is audited against the stated scope; no finite text can prove success on every unseen examination question.

Read the teaching sections before using the solved bank. In each proof, mark the exact point where nonemptiness, a nonzero coefficient, or finite dimension is used. Then work through the solved problems by reconstructing the argument, including the counterexample or boundary case. The final rules are a retrieval companion; they do not replace the proofs.

## 2. A vector space includes its field and operations

A field $F$ is a set with addition and multiplication in which addition and multiplication are associative and commutative, multiplication distributes over addition, the identities $0$ and $1$ are distinct, every element has an additive inverse, and every nonzero element has a multiplicative inverse. Familiar examples are $\mathbb Q$, $\mathbb R$, $\mathbb C$, and the residues $\mathbb F_p$ for a prime $p$. The integers are not a field: two has no integer reciprocal. Residues modulo a composite number are not a field: modulo six, two times three is zero although neither factor is zero.

A vector space over $F$ consists of a nonempty set $V$, an addition $V\times V\to V$, and scalar multiplication $F\times V\to V$. For all vectors $u,v,w$ and scalars $a,b$, the following laws hold:

$$u+v=v+u,\qquad (u+v)+w=u+(v+w),\qquad v+0_V=v,\qquad v+(-v)=0_V.$$

$$a(u+v)=au+av,\qquad (a+b)v=av+bv,\qquad a(bv)=(ab)v,\qquad 1v=v.$$

The functions defining the operations already impose closure. A list of eight algebraic laws is meaningful only after the operations are well-defined on their stated domains. The scalar zero and vector zero are different objects even when both are written as zero. A vector need not be an arrow or a tuple. A continuous function, a matrix, and a polynomial can each be one vector.

The field matters. The complex numbers have basis $(1)$ over $\mathbb C$, but basis $(1,i)$ over $\mathbb R$. The equation $a+bi=0$ forces both coefficients to vanish when $a,b$ are real. With complex coefficients, the nontrivial relation $i\cdot1-1\cdot i=0$ proves dependence. Therefore a dimension without its scalar field can be ambiguous.

## 3. Consequences of the axioms and unusual operations

The zero vector is unique: if $z$ and $z'$ are both additive identities, then $z=z+z'=z'$. An additive inverse is unique by cancellation: if $u+v=0=u+w$, add the inverse of $u$ to obtain $v=w$. The identities $0v=0_V$ and $a0_V=0_V$ follow by distributing over $0+0$ and $0_V+0_V$, respectively, then cancelling the repeated term. Since $v+(-1)v=(1-1)v=0_V$, the additive inverse is $(-1)v$. If $av=0_V$ and $a\ne0$, multiplication by $a^{-1}$ gives $v=0_V$. This last inference uses the field property; it can fail for modules over rings with zero divisors.

One cannot check a new scalar multiplication by closure alone. On $\mathbb R^2$, define $a\star(x,y)=(ax,0)$ while keeping ordinary addition. The result always lies in $\mathbb R^2$, but $1\star(0,1)=(0,0)\ne(0,1)$. The identity law fails.

Some unusual operations really do produce vector spaces. On $V=(0,\infty)$, let $u\oplus v=uv$ and $a\odot u=u^a$, for real $a$. The bijection $\phi(u)=\log u$ converts these into ordinary addition and scaling: $\phi(u\oplus v)=\phi(u)+\phi(v)$ and $\phi(a\odot u)=a\phi(u)$. Thus every axiom transfers from $\mathbb R$. The zero vector is the positive number one, the additive inverse of $u$ is $1/u$, and the single vector $e$ is a basis because $u=e^{\log u}$. The number zero is not even an element of this space. Always read the specified operations before importing familiar notation.

## 4. The subspace test and its precise hypotheses

Let $W$ be a subset of an already established vector space $V$ over the same field, with inherited operations. Then $W$ is a subspace exactly when it is nonempty and closed under all combinations $au+bv$ with $u,v\in W$ and $a,b\in F$. Equivalently, verify $0_V\in W$, closure under addition, and closure under scalar multiplication.

For the forward direction, every subspace satisfies these properties. For the reverse direction, closure restricts the two operations to $W$; the ambient associativity, commutativity, and distributive laws still hold. The zero vector belongs to $W$, and $-w=(-1)w\in W$ supplies every additive inverse. This proves all axioms without checking them independently again.

Nonemptiness cannot be omitted: the empty set satisfies every universally quantified closure implication vacuously, but has no additive identity. Containing zero is necessary, not sufficient. The set $\{(x,y):xy=0\}$ contains both coordinate axes and zero. Yet $(1,0)+(0,1)=(1,1)$ lies outside it. The quadrant $x,y\ge0$ is addition-closed, but multiplying $(1,0)$ by minus one leaves it. Conversely, a union of lines through zero may be scaling-closed while failing addition.

To disprove a subspace, one explicit failed test is sufficient. To prove one, a few successful numerical examples are never sufficient: use arbitrary admissible vectors and arbitrary field scalars. Conditions such as “positive,” “norm one,” “determinant nonzero,” and “degree exactly two” usually fail the zero test or closure, but the failed step should be exhibited.

The geometric models show finite visible patches of unbounded planes and finite visible segments of lines. Their fixed oblique projection is a drawing convention, not a coordinate transformation used in the proofs. Read the printed vector coordinates and constraint checks: two distinct three-dimensional points can project to the same screen location, so screen overlap alone never establishes vector equality or membership.

<!-- SIM: closure -->

## 5. Homogeneous constraints, affine sets, and parameter counting

For a matrix $A\in F^{m\times n}$, the solution set $N(A)=\{x:Ax=0\}$ is a subspace of $F^n$: $A(au+bv)=aAu+bAv=0$. For $Ax=b$ with $b\ne0$, zero is not a solution. If $x_0$ is one solution, every solution is of the form $x_0+z$ with $z\in N(A)$, because $A(x-x_0)=0$. Conversely every such translate solves the system. Thus a consistent nonhomogeneous system is an affine translate of a subspace. Its affine dimension is $n-\operatorname{rank}A$, but it is not a vector subspace under inherited operations.

A parameterization is a description, not automatically an independent coordinate system. For example,

$$W=\{(a+b,2a+2b,c):a,b,c\in\mathbb R\}=\operatorname{span}\{(1,2,0),(0,0,1)\}.$$

There are three written parameters but only two independent directions: $a$ and $b$ appear only through their sum. On the other hand, the homogeneous constraint $x+2y-z=0$ has the unique free-coordinate representation $(x,y,z)=y(-2,1,0)+z(1,0,1)$. Since the displayed coefficients occupy distinct free coordinates, those two generators are independent.

The same logic applies to function constraints. The polynomials with $p(1)=0$ form a subspace; those with $p(1)=1$ form an affine set. Homogeneity refers to the unknown vector or function, not to how complicated the coefficient expression looks. An equation involving $x^2$ as a known function of the independent variable can still be linear in unknown coefficients; multiplying two unknown coefficients is nonlinear.

## 6. Span is the smallest containing subspace

For a subset $S\subseteq V$, its span is the set of all finite linear combinations of elements of $S$. The empty combination is zero, so $\operatorname{span}\varnothing=\{0_V\}$. Even when $S$ is infinite, each individual combination uses only finitely many vectors. Convergence of an infinite series is additional structure, not part of the algebraic definition of span.

The span is a subspace because adding finite combinations or multiplying one by a scalar gives another finite combination. It contains every vector of $S$. Any subspace containing $S$ must contain all these combinations by repeated closure. Hence the span is the smallest subspace containing $S$, equivalently the intersection of all subspaces containing $S$.

For a finite generating list $v_1,\ldots,v_k$, form the column matrix $B=[v_1\ \cdots\ v_k]$. A target $v$ belongs to the span exactly when $Bc=v$ is consistent. Adding a vector already in the span changes the list, not the space. Adding a vector outside the span enlarges the space by exactly one dimension when the original span is finite-dimensional. This is the algebra behind incremental basis extraction.

To establish equality of spans, prove both inclusions, usually by expressing each generating list through the other. Identical cardinalities or identical dimensions alone do not prove equality of subspaces. Once an inclusion is known and both dimensions are finite, equal dimension does prove equality; the inclusion is the essential missing premise.

<!-- SIM: span -->

## 7. Linear independence, dependencies, and representation ambiguity

A list $v_1,\ldots,v_k$ is linearly independent when the only coefficients satisfying $\sum_{j=1}^k c_jv_j=0_V$ are all zero. A dependence witness is a nonzero coefficient vector $c$ giving zero; “nonzero” means at least one coefficient is nonzero. The empty list is independent. A list containing the zero vector is dependent. Repeating a nonzero vector also creates a dependence. Treat a list with duplicates as a list; silently converting it to a set changes the question.

A finite list is dependent exactly when some vector can be written using the others. Given a dependence and an index with $c_j\ne0$, solve for $v_j$ by dividing by that coefficient. Conversely, moving such a representation to one side gives a nontrivial zero combination. This does not say that every vector in a dependent list is redundant: the list $(e_1,e_2,2e_2)$ is dependent, but $e_1$ cannot be removed without changing its span.

Independence is equivalent to uniqueness of representation within the span. If $Bc=Bd$, then $B(c-d)=0$; independent columns force $c=d$. If a dependence $Bz=0$ exists with $z\ne0$, then every representation $Bc=v$ yields others $B(c+tz)=v$. Over an infinite field there are infinitely many; over a finite field their number is finite and controlled by the nullity.

Every sublist of an independent list is independent. Every list containing a dependent sublist is dependent. Pairwise nonparallel vectors need not be jointly independent: $(1,0)$, $(0,1)$, and $(1,1)$ give a counterexample. Independence is a collective property, not merely a pairwise comparison.

## 8. A basis supplies both existence and uniqueness

A basis of $V$ is an independent spanning list. Spanning guarantees a representation for every vector; independence guarantees uniqueness. Neither property alone is sufficient. The standard basis of $F^n$ consists of the coordinate unit vectors. The zero space has the empty basis, not the singleton list containing zero.

If $B=(b_1,\ldots,b_d)$ is an ordered basis, write $[v]_B=(c_1,\ldots,c_d)^T$ when $v=\sum c_jb_j$. The order matters: reversing two basis vectors reverses the corresponding coordinate positions. Coordinates are not the vector itself. The same coordinate tuple can represent different vectors in two bases, and one vector generally has different tuples in two bases.

The coordinate map is linear and bijective from $V$ to $F^d$. It is linear because adding vector expansions adds coefficients, and scaling multiplies every coefficient. It is injective by independence and surjective because every coefficient tuple defines a combination. Thus an abstract finite-dimensional space can be studied using an ordinary coordinate matrix once a basis is fixed. Choosing coordinates preserves addition and scalar multiplication; it need not preserve lengths unless the basis has extra metric properties.

For $b_1=(1,1)$ and $b_2=(1,-1)$, solving $(x,y)=c_1b_1+c_2b_2$ gives $c_1=(x+y)/2$, $c_2=(x-y)/2$. The vector $(3,1)$ has coordinates $(2,1)$ in this basis. It does not mean that the vector has changed to the point $(2,1)$ in the original plane.

<!-- SIM: coordinates -->

## 9. Exchange and why every finite basis has the same size

The key exchange step is algebraic. Suppose $w=\sum_{j=1}^k a_jv_j$ and $a_r\ne0$. Then

$$v_r=a_r^{-1}\left(w-\sum_{j\ne r}a_jv_j\right).$$

Replacing $v_r$ by $w$ preserves the span. One inclusion follows because $w$ was in the original span; the other follows from the displayed recovery formula. If the original list is a basis, the replacement is a basis as well: spanning is preserved and a zero relation in the new list can be substituted into the old independent list. If $a_r=0$, replacement at that position need not preserve the span.

Now let $u_1,\ldots,u_r$ be independent and $v_1,\ldots,v_s$ span $V$. Express $u_1$ through the spanning list. At least one coefficient is nonzero, because $u_1\ne0$; exchange the corresponding $v$. At step $j$, the current spanning list includes the previously inserted $u_1,\ldots,u_{j-1}$. When $u_j$ is expressed through that list, some still-unexchanged vector must have nonzero coefficient. Otherwise $u_j$ lies in the span of earlier $u$ vectors, contradicting independence. Continue. There must be at least $r$ available positions, so $r\le s$.

Apply this inequality in both directions to two finite bases. Each is independent and the other spans, so neither can contain more vectors than the other. Their sizes are equal. This common number defines the dimension. The argument is not merely an observation about a few examples, and it does not assume the conclusion when proving it.

<!-- SIM: exchange -->

## 10. Dimension theorems and construction of bases

Suppose $V$ has finite dimension $d$. Every independent list has at most $d$ members; every spanning list has at least $d$ members. An independent list of exactly $d$ vectors is a basis. A spanning list of exactly $d$ vectors is also a basis. A list of $d$ arbitrary vectors need not be either. A list with more than $d$ vectors is dependent, while fewer than $d$ cannot span.

To extract a basis from a finite spanning list, repeatedly remove a vector that is a combination of the others. Each removal preserves the span and decreases the finite length, so the procedure stops at an independent spanning list. To extend an independent list to a basis, choose a vector outside its current span whenever that span is proper. The enlarged list is independent: a relation with a nonzero coefficient on the new vector would express it through the previous list. The process stops after at most $d$ vectors.

“Maximal independent” means that no vector from the specified ambient space can be added while preserving independence. “Minimal spanning” means that removing any member destroys spanning. Both characterize bases. A list may be maximal among a supplied candidate collection without being a basis of a larger ambient space; always state the universe over which maximality is asserted.

For $U\subseteq V$ a subspace, the same extension argument gives $\dim U\le d$. If equality holds, a basis of $U$ already has $d$ independent vectors in $V$, hence spans $V$ and $U=V$. This proof requires finite dimension. In $F[x]$, the proper subspace $xF[x]$ has the same countably infinite basis size as $F[x]$; equal infinite dimensions do not turn a proper inclusion into equality.

## 11. Computing a basis without changing the requested space

Let $A$ have the generating vectors as columns. Row-reduce to $R=EA$, with $E$ invertible. Then $Ac=0$ exactly when $Rc=0$, so all coefficient dependencies are preserved. Pivot column indices in $R$ identify independent columns of the original $A$. The corresponding original columns form a basis of $\operatorname{Col}A$. The reduced columns generally live in the transformed space $E(\operatorname{Col}A)$, so copying their numerical entries answers a different question.

For row space, row operations do preserve the space. Every new row is a combination of old rows, and the inverse operations give the reverse inclusion. Therefore the nonzero rows of an echelon form are a row-space basis. Their independence follows by inspecting successive pivot positions in a zero combination. Row and column rank are equal, but row space and column space are different objects, sometimes even in different ambient dimensions.

For the nullspace, solve $Rx=0$ by assigning one free coordinate at a time to one and the other free coordinates to zero. These special solutions span every solution. They are independent because their free-coordinate portions are distinct unit vectors. Thus a matrix with $n$ columns and rank $r$ has nullity $n-r$.

Consider $A=\begin{bmatrix}1&2&0&3\\2&4&1&4\\3&6&2&5\end{bmatrix}$. Its reduced form is $\begin{bmatrix}1&2&0&3\\0&0&1&-2\\0&0&0&0\end{bmatrix}$. Columns one and three of $A$ give a column-space basis; the two nonzero reduced rows give a row-space basis. The nullspace basis is $(-2,1,0,0)^T$ and $(-3,0,2,1)^T$. Verify both by multiplication against the original matrix, not only the reduced one.

<!-- SIM: computation -->

## 12. Polynomial and function spaces

Let $P_n(F)$ denote the formal polynomials of degree at most $n$, including zero. Its basis is $(1,x,\ldots,x^n)$ and dimension $n+1$. Comparing polynomial coefficients proves independence; expanding an arbitrary polynomial proves spanning. The zero polynomial has no ordinary finite degree, but it belongs to $P_n$. Polynomials of degree exactly $n$ are not a subspace: zero is absent and leading terms can cancel.

Convert a polynomial list into columns of coefficients relative to the same monomial basis. For $p_1=1+x$, $p_2=x+x^2$, and $p_3=1+2x+x^2$, the identity $p_3=p_1+p_2$ gives dependence. The first two are independent because the constant coefficient forces the coefficient on $p_1$ to vanish and the quadratic coefficient forces the coefficient on $p_2$ to vanish. Their span is a two-dimensional subspace of $P_2$, not all of $P_2$.

For function spaces, equality means equality at every point of the specified domain. To prove dependence, exhibit an identity, such as $\sin^2x+\cos^2x-1=0$. To prove independence, evaluate a proposed zero identity at enough points, differentiate when justified, or use known distinct structural features. The functions $\sin x$ and $\cos x$ are independent over $\mathbb R$ on $\mathbb R$: evaluation at zero and $\pi/2$ forces both coefficients to vanish. Agreement or cancellation at one point says little about equality of functions.

Evaluation can establish independence when the resulting square evaluation matrix is invertible. A singular evaluation matrix only shows that the selected samples are insufficient; it need not show that the functions are dependent. For example, $1$ and $x^2$ have identical values at $-1$ and $1$, yet are independent polynomials.

<!-- SIM: polynomial -->

## 13. Linear constraints on polynomials and interpolation

In $P_n(\mathbb R)$, a condition such as $p(a)=0$ is homogeneous and linear in the polynomial. For distinct $a_1,\ldots,a_k$ with $k\le n+1$, the conditions $p(a_j)=0$ are independent. One proof constructs Lagrange polynomials $L_j(x)=\prod_{i\ne j}(x-a_i)/(a_j-a_i)$, whose values at the nodes are unit vectors. Hence the evaluation map onto $\mathbb R^k$ is surjective and its kernel has dimension $n+1-k$.

Equivalently, $p$ vanishes at all nodes exactly when it is divisible by $\prod_j(x-a_j)$. For $k\le n$, a basis of the constrained space consists of that product times $1,x,\ldots,x^{n-k}$. If $k=n+1$, only zero remains. If there are more than $n$ distinct roots, a nonzero polynomial of degree at most $n$ is impossible.

Repeated conditions require actual rank analysis. The constraints $p(1)=0$ and $2p(1)=0$ are the same restriction. In characteristic zero, $p(1)=0$ and $p'(1)=0$ impose a repeated root and are independent on $P_n$ when $n\ge1$. In positive characteristic, differentiation can behave differently: the derivative of $x^p$ over $\mathbb F_p$ is zero. Do not transfer a real-variable derivative proof to every field unchanged.

Interpolation data $p(a_j)=y_j$ describe an affine fiber. With $n+1$ distinct real nodes, there is exactly one polynomial in $P_n$ for each data tuple. With fewer nodes, there are free directions; with repeated inconsistent data at one node, no solution exists. The number of equations written is not necessarily the number of independent constraints.

## 14. Matrix spaces and structured degrees of freedom

The vector space $M_{m\times n}(F)$ has basis $E_{ij}$, the matrices with one unit entry, and dimension $mn$. Matrix multiplication is not the vector-space operation: addition and scalar multiplication are. Noncommutativity of matrix multiplication does not prevent matrices from forming a vector space.

Over a field of characteristic other than two, symmetric $n\times n$ matrices have dimension $n(n+1)/2$: choose $n$ diagonal and $n(n-1)/2$ upper-triangular entries. A basis consists of $E_{ii}$ and $E_{ij}+E_{ji}$ for $i<j$. Skew-symmetric matrices have zero diagonal and basis $E_{ij}-E_{ji}$ for $i<j$, so dimension $n(n-1)/2$.

The trace-zero condition is one nonzero linear equation, even when the characteristic divides $n$: the trace of $E_{11}$ is still one. In symmetric matrices it removes one independent diagonal freedom. A useful trace-zero symmetric basis is $E_{ii}-E_{nn}$ for $i<n$, together with the off-diagonal symmetric pairs. For real $4\times4$ matrices this gives three diagonal directions and six off-diagonal directions, total nine.

Every real square matrix has the unique decomposition

$$A=\frac{A+A^T}{2}+\frac{A-A^T}{2}.$$

The first term is symmetric and the second skew-symmetric. Their intersection is zero because $A^T=A=-A$ implies $2A=0$. The division by two is essential; in characteristic two the two transpose equations coincide, and the direct-sum theorem in this form fails. A determinant-zero condition is nonlinear: two singular matrices can add to an invertible matrix, so singular matrices do not form a subspace in orders at least two.

<!-- SIM: matrix -->

## 15. Sums, intersections, and the union trap

For subspaces $U,W\subseteq V$, define $U+W=\{u+w:u\in U,w\in W\}$. This is the smallest subspace containing both. The intersection is also a subspace: each closure operation remains valid in both spaces. More generally, any intersection of subspaces is a subspace; the empty intersection is the ambient space when that convention is used.

The union is different. Two subspaces have a subspace union exactly when one contains the other. If neither contains the other, select $u\in U\setminus W$ and $w\in W\setminus U$. If $u+w$ belonged to $U$, subtraction of $u$ would put $w$ in $U$; if it belonged to $W$, subtraction of $w$ would put $u$ in $W$. Both are contradictions. Thus addition fails in the union.

To compute a sum from basis matrices $B_U,B_W$, concatenate the columns and extract a basis. To compute an intersection, solve

$$B_Ua=B_Wb,\qquad [B_U\ -B_W]\begin{bmatrix}a\\b\end{bmatrix}=0.$$

Map each coefficient-pair solution to the actual vector $B_Ua$. If the two supplied lists are genuine bases, this map from the block nullspace to the intersection is bijective: a vector in the intersection has unique coordinates in each basis. If either list is redundant, the coefficient-pair nullspace also contains representation ambiguities that map to zero. Then its dimension can exceed the intersection dimension, and mapped vectors must be filtered for independence.

<!-- SIM: intersection -->

## 16. The dimension formula, with a proof

For finite-dimensional subspaces,

$$\dim(U+W)=\dim U+\dim W-\dim(U\cap W).$$

Choose a basis $c_1,\ldots,c_r$ of the intersection. Extend it separately to $(c_1,\ldots,c_r,u_1,\ldots,u_p)$ for $U$ and $(c_1,\ldots,c_r,w_1,\ldots,w_q)$ for $W$. The joined list $(c,u,w)$ spans the sum because an arbitrary $u+w$ expands in those vectors and common coefficients can be combined.

For independence, suppose a zero combination of this joined list exists. Move the $w$ terms to the other side. The remaining vector lies in both $U$ and $W$, so it is a combination of the $c$ vectors. Substituting that representation into the basis of $W$ forces every $w$ coefficient to vanish. The remaining relation in the basis of $U$ forces all $u$ and $c$ coefficients to vanish. Therefore the joined list is a basis. Counting its members gives $(r+p)+(r+q)-r$.

If the ambient space has dimension $n$, the intersection dimension satisfies

$$\max(0,\dim U+\dim W-n)\le\dim(U\cap W)\le\min(\dim U,\dim W).$$

All integer values in this range are attainable by coordinate subspaces: choose the desired common coordinate directions and then separate remaining directions. This gives both a bound and a construction showing sharpness. For two six-dimensional subspaces in a ten-dimensional space, the intersection has dimension between two and six, inclusive. It is not necessarily exactly two.

## 17. Direct sums and uniqueness of decomposition

The sum $U+W$ is direct when $U\cap W=\{0\}$. Write $U\oplus W$ for that sum. To claim $V=U\oplus W$, also verify $U+W=V$. Trivial intersection alone does not ensure that the subspaces cover an arbitrarily larger ambient space.

Directness is equivalent to uniqueness of the decomposition of each vector in the sum. If $u+w=u'+w'$, then $u-u'=w'-w$ lies in the intersection. A zero intersection forces equality of both components. Conversely, a nonzero $z\in U\cap W$ gives two decompositions of zero, $0+0$ and $z+(-z)$.

In finite dimension, bases of two subspaces concatenate to an independent list exactly when their intersection is zero. They form an ambient basis exactly when the sum is the whole space as well. Dimension addition is a useful check once the containment and spanning premises are established.

For three or more subspaces, pairwise trivial intersections are insufficient. In $\mathbb R^2$, the lines generated by $e_1$, $e_2$, and $e_1+e_2$ intersect pairwise only at zero, but $e_1+e_2-(e_1+e_2)=0$ is a nontrivial relation across the three components. The correct condition is that $u_1+\cdots+u_k=0$, with $u_j\in U_j$, implies every $u_j=0$. Equivalently, each newly added subspace must intersect the sum of its predecessors trivially.

<!-- SIM: direct -->

## 18. Complements and adapted bases

Every subspace $U$ of a finite-dimensional $V$ has a complement. Extend a basis of $U$ to a basis of $V$, and let $W$ be the span of the added vectors. The full basis proves $U+W=V$ and $U\cap W=\{0\}$. The complement is generally not unique: in $\mathbb R^2$, any line other than the horizontal axis complements the horizontal axis. A complement is not automatically perpendicular; orthogonal complements require an inner product.

For nested subspaces $U\subseteq W\subseteq V$, first choose a basis of $U$, extend it to $W$, then extend to $V$. This adapted basis makes all containments visible as initial coordinate blocks. For two arbitrary subspaces, begin with the intersection and extend separately as in the dimension-formula proof. Choosing unrelated bases first can hide common directions even when the spaces intersect substantially.

An internal direct sum consists of actual subspaces in one ambient space. The external direct sum of two abstract finite-dimensional spaces is the set of ordered pairs $(u,w)$ with componentwise operations. Its dimension is the sum of dimensions, and its coordinate blocks are always independent by construction. The map $(u,w)\mapsto u+w$ identifies an external sum with an internal one only when the internal decomposition is unique.

## 19. Coordinate change and coordinate-reading functionals

Let $B$ and $C$ be ordered bases of the same $d$-dimensional space. The matrix $P_{C\leftarrow B}$ has as its $j$th column $[b_j]_C$. Expanding $v=\sum_j [v]_{B,j}b_j$ in the $C$ basis yields

$$[v]_C=P_{C\leftarrow B}[v]_B.$$

The reverse matrix is its inverse, and changes compose in the direction of the arrows. In a coordinate realization with basis matrices $S_B,S_C$, this is $P_{C\leftarrow B}=S_C^{-1}S_B$. For a proper subspace of $F^m$, the rectangular basis matrix has no ordinary square inverse; solve the full-column-rank coordinate system instead. Do not write an inverse for a rectangular matrix merely because its columns form a basis of their own span.

Each coordinate position defines a linear functional $\ell_j:V\to F$ by $\ell_j(v)=[v]_{B,j}$. These satisfy $\ell_i(b_j)=\delta_{ij}$. They form the dual basis: a linear functional is determined by its values on the basis vectors, and $\ell(v)=\sum_j\ell(b_j)\ell_j(v)$. For a square real basis matrix, the rows of its inverse are these coordinate-reading functionals. They are covectors, not an extra list of physical vectors unless an inner product is explicitly used to identify them.

## 20. Quotients and what remains after ignoring a subspace

For a subspace $U\subseteq V$, the coset $v+U$ consists of vectors differing from $v$ by an element of $U$. Two cosets are equal exactly when $v-w\in U$; otherwise they are disjoint. Define $(v+U)+(w+U)=(v+w)+U$ and $a(v+U)=av+U$. These operations are well-defined: changing representatives adds elements of $U$, and closure keeps that change in $U$. The cosets form the quotient vector space $V/U$, whose zero vector is the whole coset $U$.

Extend a basis of $U$ by $w_1,\ldots,w_r$ to a basis of $V$. Then the cosets $w_1+U,\ldots,w_r+U$ form a basis of the quotient. Spanning follows by discarding the $U$ component of every expansion. Independence follows because a combination of the added vectors lies in $U$ only when all its coefficients are zero. Consequently $\dim(V/U)=\dim V-\dim U$ in finite dimension.

The quotient is not the set difference $V\setminus U$, and its vectors are cosets rather than chosen representatives. For the horizontal axis in $\mathbb R^2$, a coset is an entire horizontal line; only its vertical displacement remains. A chosen complement can provide representatives, but the quotient construction itself does not pick a unique complement.

<!-- SIM: quotient -->

## 21. Fields, finite counts, and characteristic-dependent traps

An $n$-dimensional vector space over a field with $q$ elements has exactly $q^n$ vectors, because a basis gives a bijection with $F^n$. A $d$-dimensional subspace contains $q^d$ vectors. The number of ordered bases of $F_q^n$ is

$$\prod_{j=0}^{n-1}(q^n-q^j).$$

After $j$ independent vectors have been chosen, their span contains $q^j$ vectors, which are precisely the forbidden choices for the next basis member. Over $\mathbb F_2$, each line has only one nonzero vector, and the three lines in $\mathbb F_2^2$ together cover the whole space. Thus statements about finite unions of proper real subspaces need field qualifications. The theorem about a union of exactly two subspaces remains valid over every field.

If $K$ is a finite-dimensional field extension of $F$, and $V$ has finite dimension over $K$, then $\dim_FV=(\dim_FK)(\dim_KV)$. Multiply a basis of $V$ over $K$ by each member of a basis of $K$ over $F$; expanding scalar coefficients proves spanning and comparing the two sets of coefficients proves independence. This gives $\dim_{\mathbb R}\mathbb C^n=2n$.

Formal polynomials and polynomial functions must also be distinguished over finite fields. The nonzero formal polynomial $x^q-x$ vanishes at every element of $\mathbb F_q$. Therefore evaluations on all field elements need not distinguish arbitrary formal polynomials, although distinct-node interpolation remains valid for degree less than the number of nodes.

<!-- SIM: field -->

## 22. Parameter-dependent spans and safe case splitting

For a parameterized matrix, first find values where pivots or a determinant may vanish, then analyze each exceptional case in the original matrix. Dividing by a symbolic expression assumes it is nonzero. A generic rank calculation can miss a dimension drop precisely at the values most likely to be tested.

For $v_1=(1,t)$ and $v_2=(t,1)$ over $\mathbb R$, the column determinant is $1-t^2$. The span is the plane for $t\ne\pm1$. At $t=1$ it is the line through $(1,1)$, and at $t=-1$ it is the line through $(1,-1)$. Neither exceptional span is zero. The geometric scale and axes in the model stay fixed so a dimension change is not confused with camera rescaling.

For more than two vectors, inspect appropriate minors or perform elimination with explicit branches. A zero determinant of one selected square submatrix only proves that particular subset is dependent; another subset can still supply full rank. After finding a candidate basis, verify spanning of every supplied generator and independence of the chosen ones.

<!-- SIM: parameter -->

## 23. Infinite-dimensional boundaries and annihilating constraints

The formal monomials $(1,x,x^2,\ldots)$ are a basis of $F[x]$: each polynomial has a finite coefficient expansion. No finite list spans the space, because the degrees of finitely many polynomials are bounded while higher monomials exist. In contrast, the coordinate unit sequences span only the finite-support sequences, not every infinite sequence. The constant sequence $(1,1,\ldots)$ cannot be a finite combination of them. A convergent series representation requires a topology and is not automatically a Hamel-basis expansion.

For finite-dimensional $V$, the annihilator $U^0$ is the subspace of linear functionals that vanish on $U$. In an adapted basis extending a basis of $U$, such a functional must have zero coefficients on the $U$ basis vectors and can be arbitrary on the remaining vectors. Hence $\dim U^0=\dim V-\dim U$. Independent homogeneous constraints can therefore be viewed as independent functionals. A list of equations cuts the dimension by the rank of these functionals, not by its raw length.

If $U=\ker A$ in coordinate space, the row functionals of $A$ supply the constraints. Redundant rows are redundant restrictions. The identity $\dim U=n-\operatorname{rank}A$ is the same principle expressed computationally. Orthogonal complements are a Euclidean realization of related ideas; they should not be silently assumed in an abstract vector space without an inner product.

## 24. A reliable examination workflow

Begin by naming the ambient space, scalar field, and inherited or modified operations. If asked whether a set is a subspace, test zero and closure symbolically; for rejection, provide a minimal witness. If asked for a basis, specify whether the vectors are generators or solutions of equations. Use original pivot columns for a generated space and special solutions for a constrained space. Check the ambient coordinate length of every proposed basis vector.

For dimensions, identify independent parameters or independent constraints, then verify the resulting count against the ambient dimension. For sums and intersections, draw the containment structure and apply the two-subspace formula with its actual premises. For direct sums, verify both coverage and uniqueness. For polynomial and matrix spaces, choose a common coefficient system before eliminating. For parameterized questions, separate exceptional values before division.

Finish with a certificate. A basis certificate contains membership, independence, and spanning. An impossibility answer contains a violated bound or an explicit counterexample. A dimension answer should be accompanied by a basis construction or a rank argument, not an unexplained integer. A coordinate answer should include a reconstruction of the original vector. These checks expose reversed change matrices, lost exceptional cases, and redundant parameters immediately.

## 25. Summary with complete mathematical statements

A vector space is defined by its set, field, addition, and scalar multiplication. A subspace inherits those operations, contains zero, and is closed under arbitrary field-linear combinations. Span is the smallest containing subspace and uses finite combinations. Independence is absence of a nontrivial zero relation; it gives unique coefficients within a span. A basis gives both existence and uniqueness of coordinates, and exchange proves that all finite bases have the same size.

In dimension $d$, at most $d$ vectors can be independent and at least $d$ are needed to span. Equality of subspace dimensions implies equality of spaces only when inclusion and finite dimension are also known. Row operations preserve row space and coefficient dependencies, while original pivot columns preserve the requested column space. A homogeneous system with $n$ unknowns and rank $r$ has a nullspace of dimension $n-r$.

For finite-dimensional subspaces, the dimension of the sum equals the sum of dimensions minus the intersection dimension. A direct sum is characterized by unique components. Pairwise trivial intersections of three spaces do not ensure a direct sum. Polynomial, matrix, and function examples obey the same principles after their operations and fields are fixed. Quotients remove a subspace by identifying cosets; their dimension is the missing number of basis directions. The following bank and final rules develop these statements through explicit medium and hard applications and foundational boundary checks.

## 26. Fully worked mathematical and conceptual problems

<!-- INCLUDE: problems -->

## 27. Final examination rules, conditions, and worked checks

<!-- INCLUDE: review -->

## 28. Editable exact-arithmetic laboratory

Enter generators as the columns of a small matrix and a target vector. The laboratory keeps the supplied generators unchanged, row-reduces a copy with exact rational arithmetic, identifies a basis from original pivot columns, constructs every nullspace basis direction, and decides target membership. Every row operation is shown. A dependent generator list has coefficient ambiguity, which must not be confused with ambiguity in the target vector itself.

<!-- LAB: spaces -->

## 29. References and provenance

1. Andrew Wathen. **M1: Linear Algebra I**, University of Oxford, Michaelmas 2022. Lecture notes, PDF pages 26–44 and 47–52, corresponding to printed pages 25–43 and 46–51: vector spaces, subspaces, spans, independence, bases, exchange, dimensions, sums, and direct sums. [Course and instructor](https://courses.maths.ox.ac.uk/course/view.php?id=609). [Written notes](https://courses.maths.ox.ac.uk/pluginfile.php/25471/mod_folder/content/0/lecture_notes22.pdf?forcedownload=1). Document typos relevant to the synthesis are recorded in the source audit; this chapter supplies independently checked statements and examples.
2. Bernd Gärtner. **Linear Algebra, First Part**, ETH Zürich, HS2024, course 401-0131-00L, taught by Bernd Gärtner and Robert Weismantel. Sections 4.1–4.2, PDF pages 114–129, and the computational bridge in 4.3.1–4.3.2, PDF pages 130–132. [Course](https://ti.inf.ethz.ch/ew/courses/LA24/index.html). [Lecture notes](https://ti.inf.ethz.ch/ew/courses/LA24/notes_part_I.pdf). The chapter uses the finite-combination convention, exchange proof, and basis construction, with independent examples and explicit field qualifications.
3. Gilbert Strang. **18.06SC Linear Algebra**, MIT, Fall 2011. Session 1.9, *Independence, Basis and Dimension*: lecture summary, PDF pages 1–3; problems 9.1–9.2, PDF page 1; solutions, PDF pages 1–2. [Session and written resources](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/ax-b-and-the-four-subspaces/independence-basis-and-dimension/). The bank contains attributed, independently reconstructed variations rather than reproducing an entire assignment.
4. Stephen Boyd. **EE263: Introduction to Linear Dynamical Systems**, Stanford University, Autumn 2007–08. Lecture 3, *Linear Algebra Review*, PDF pages 1–11, slides 3–1 through 3–22. [Course](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/). [Written slides](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/lin-alg2.pdf). Coordinate recovery, dual-basis interpretation, and measurement ambiguity are used with finite-dimensional qualifications.
5. William Gunther. **21-241 Matrix Algebra**, Carnegie Mellon University, Summer I 2014. *Summary of Day 22*, PDF pages 1–4, and *Summary of Day 23*, PDF pages 1–4. [Course calendar](https://www.math.cmu.edu/~wgunther/241/m14/index.html). [Abstract spaces](https://www.math.cmu.edu/~wgunther/241/m14/notes/week5/22.pdf). [Bases](https://www.math.cmu.edu/~wgunther/241/m14/notes/week6/23.pdf). Evaluated as a supplementary candidate; incorrect independence statements and missing qualifications are documented and corrected rather than adopted.
6. Oliver Knill. **Math 21b**, Harvard College, Spring 2023, Lecture 4. [Written handout](https://people.math.harvard.edu/~knill/teaching/math21b2023/handouts/lecture04.pdf). Screened as a compact review candidate; not counted among the four core courses. UC Berkeley Math 54, Alexander Paulin, Spring 2018, was also screened for relevant written documents; its scanned materials were not counted as fully read in this chapter audit.
7. Original Iranian examination booklets are pinned to repository commit `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`. Each authentic item supplies its booklet, question number, original PDF page, document hash in the research record, and original option order. Answers are independently derived and are not represented as official answer keys. Original and reconstructed questions are explicitly labelled.
