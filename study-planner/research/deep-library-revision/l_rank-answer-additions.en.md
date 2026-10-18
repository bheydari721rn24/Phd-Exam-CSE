# Individually checked teaching extensions for the rank problem bank

Each numbered addition belongs to that exact question. Existing correct derivations remain; these additions supply missing coordinate calculations, proof steps, hypotheses and examination decisions. They are not additional questions.

## LR01

**Write the compatibility test as an equation.** The left-kernel vector gives $-b_1+b_2/2+b_3=0$, equivalently $b_2=2b_1-2b_3$. When this holds, choose $x_2=t$. The original third equation gives $x_3=b_3$, and the first gives $x_1=b_1-b_3-2t$. Therefore the entire fiber is $(b_1-b_3,0,b_3)^T+t(-2,1,0)^T$. Substitution into row two produces $2b_1-2b_3=b_2$, so the condition is sufficient as well as necessary. The column space and left kernel are subspaces of $\mathbb R^3$ in output coordinates; the row space and kernel also have three coordinates here, but describe input restrictions and input ambiguities instead. Equal ambient sizes do not identify their roles.

## LR02

**Recover every compatible input.** The only load restriction is $b_1+b_4=0$. Put $x_2=s$ and $x_4=t$; row two gives $x_3=b_2-t$, row one gives $x_1=b_1-2s-t$, and row three then gives $x_5=b_3-b_1$. Thus $x=(b_1-2s-t,s,b_2-t,t,b_3-b_1)^T$. The independent free patterns are exactly the two displayed kernel vectors. Column and left-kernel vectors have four entries; row and right-kernel vectors have five. The independent fifth column affects the third output even though it appears after two free columns. This is why counting only diagonal pivots or assuming a terminal block of free variables fails.

## LR03

**Separate a source typo from the compatibility calculation.** From $Y=(-1,-6,-3,1)^T$, the load restriction is $b_4=b_1+6b_2+3b_3$. This is the original row identity, so it can be checked before elimination. To recover inputs, let $\rho_1,\rho_2,\rho_3$ be the transformed load entries under the same listed row operations. The reduced equations are $x_1+x_3-x_5=\rho_1$, $x_2+2x_3+3x_5=\rho_2$, and $x_4+4x_5=\rho_3$. Taking $x_3=s,x_5=t$ yields $(\rho_1-s+t,\rho_2-2s-3t,s,\rho_3-4t,t)^T$. The two free-coordinate coefficient vectors agree with $N$. Column/left-kernel coordinates lie in $\mathbb R^4$; row/kernel coordinates lie in $\mathbb R^5$. Never reduce $A$ and then attach an untransformed $b$ to its RREF.

## LR04

**Interpret the row relation.** Original row one minus twice row two plus row three is zero; hence $b_1-2b_2+b_3=0$. Choose $x_3=s,x_4=t$. From the original first equation, $x_2=b_1-2s-3t$. From the second, $x_1=b_2-2b_1+s+2t$. These inputs satisfy the third precisely under the stated compatibility condition. The fiber has two free directions even though there is only one zero row: nullity is the number of columns minus rank, not the number of zero rows. The column space/left kernel lie in $\mathbb R^3$; row space/kernel lie in $\mathbb R^4$.

## LR05

**Existence and uniqueness require different checks.** The output of $(x_1,x_2)$ is $(x_1,x_2,x_1+x_2)$. Thus $b_3=b_1+b_2$ is necessary. Under that condition the unique input is $(b_1,b_2)^T$, proving sufficiency directly. The two column vectors span a plane in $\mathbb R^3$; their single independent orthogonal restriction is the left-kernel vector $(-1,-1,1)^T$. The row space is all of $\mathbb R^2$ and the kernel is zero. Being injective does not turn this plane into the entire three-dimensional output space.

## LR06

**Make the free coordinate visible.** For any $b\in\mathbb R^2$, set $x_3=t$, then $x_1=b_1-t$ and $x_2=b_2-t$. Therefore $x=(b_1,b_2,0)^T+t(-1,-1,1)^T$, and multiplication verifies every value of $t$. The image is $\mathbb R^2$ and its left kernel is the zero space. The row space is a two-dimensional subspace of $\mathbb R^3$, perpendicular to the one-dimensional kernel. An empty left-kernel basis imposes no load equations; it does not assert that the input is unique.

## LR07

**Treat the zero matrix without inventing pivots.** For every $x\in\mathbb R^3$, $Ax=(0,0)^T$. Thus $b\ne0$ has no preimage, while $b=0$ has every three-coordinate input as a solution. The image is the zero subspace of $\mathbb R^2$ and the row space is the zero subspace of $\mathbb R^3$. Their bases are empty lists, not lists containing a zero vector. The two left-kernel standard vectors give the explicit conditions $b_1=0$ and $b_2=0$; the three right-kernel standard vectors give three independent input parameters.

## LR08

**Calculate the two independent load restrictions.** They are $-2b_1+b_2=0$ and $b_1+b_3=0$. When both hold, the first equation alone determines $x_1=b_1+2s-3t$ after choosing $x_2=s,x_3=t$. Its substitution into rows two and three gives exactly $b_2=2b_1$ and $b_3=-b_1$. Hence the solution set is $(b_1,0,0)^T+s(2,1,0)^T+t(-3,0,1)^T$. Every listed space is ambiently three-dimensional here, but their actual dimensions are respectively one, one, two and two. Three nonzero equations carry only one independent restriction.

## LR09

**Handle the early free column correctly.** The left-kernel equation is $-b_1/2+b_2=0$, so $b_1=2b_2$. Choose $x_1=s,x_3=t$. The original third row gives $x_4=b_3/3$, and the second gives $x_2=b_2-2t+b_3/3$. The first equation is then twice the second, as required. The two independent directions are $(1,0,0,0)^T$ and $(0,-2,1,0)^T$. Column/left-kernel vectors have three entries; row/kernel vectors have four. Column four is a pivot column despite appearing after free columns one and three.

## LR10

**Convert the left kernel into a complete existence criterion.** Its two columns impose $b_2=2b_1$ and $b_4=b_1+b_3$. Choose $x_3=s,x_4=t$. The original third row gives $x_2=b_3-s$, and the first gives $x_1=b_1-2b_3-s-4t$. The second and fourth rows then hold precisely under those two load equations. Thus a compatible load has a two-dimensional affine fiber, not a unique solution. All four spaces use four coordinates, but the row/column spaces and both kernels each have dimension two. A square singular matrix can have many consistent nonzero loads.

## LR11

**Write the output hyperplane explicitly.** The left-kernel equation is $-b_1-2b_2-3b_3-4b_4+b_5=0$. If it holds, the first four original equations determine the unique input $(b_1,b_2,b_3,b_4)^T$; the last equation is exactly the displayed restriction. Therefore the column space is a four-dimensional hyperplane in $\mathbb R^5$, its left kernel is a line in $\mathbb R^5$, its row space is all of $\mathbb R^4$, and its right kernel is zero. The extra output coordinate creates a consistency test, not an extra independent input coordinate.

## LR12

**Parameterize the entire fiber instead of only counting it.** Set $x_2=s,x_4=t,x_5=u$. The two pivot equations give $x_1=b_1-2s-t-3u$ and $x_3=b_2-t+u$. Thus every solution is $(b_1,0,b_2,0,0)^T+s(-2,1,0,0,0)^T+t(-1,0,-1,1,0)^T+u(-3,0,1,0,1)^T$. The three free-coordinate patterns are independent, so there are exactly three parameters. The image is $\mathbb R^2$ with zero left kernel; row space and kernel are complementary orthogonal subspaces of dimensions two and three in $\mathbb R^5$. There is no load restriction.

## LR13

**Locate the exact independence implication.** Write a kernel basis as $k_1,\ldots,k_q$. A relation among the proposed image vectors means $\sum_i c_i v_i=\sum_j d_j k_j$ for some $d_j$. Rearranging produces a zero relation in the full domain basis, so every coefficient vanishes. In particular, a nonzero added basis vector cannot map to zero. Spanning alone would provide only an upper bound on rank; independence supplies the matching lower bound. The construction includes the endpoints $q=0$ and $r=0$, using an empty kernel basis or an empty image basis when appropriate.

## LR14

**Translate the counts into what a solver observes.** Every compatible load has four independent input parameters, because its fiber is a translate of the four-dimensional kernel. The five output coordinates satisfy one independent homogeneous compatibility equation $y^Tb=0$, where any nonzero $y\in\ker A^T$ suffices. These numbers obey two different conservation equations: $4+4=8$ in the input space and $4+1=5$ in the output space. Without the actual coefficients one cannot name the vector $y$ or a particular preimage, although the dimensions and failure of surjectivity are already determined.

## LR15

**Check feasibility before any arithmetic.** For an $m\times n$ matrix, $0\le r\le\min(m,n)$ implies $\max(0,n-m)\le\operatorname{nullity}A\le n$. Here this interval is $4\le\operatorname{nullity}A\le7$. The proposed value three is outside it. No special choice of zero entries, dependent rows or scalar field can evade this finite-dimensional bound. The smallest possible nullity four is attainable, for example by the matrix $[I_3\;0_{3\times4}]$, so the contradiction is sharp rather than an artifact of an unnecessarily weak estimate.

## LR16

**Prove the uniqueness statement in both directions.** If $x_p$ solves the compatible system and $z\ne0$ lies in the kernel, then $x_p+z$ is a different solution. Conversely, if the kernel is zero and two inputs have the same output, subtracting them gives a zero kernel vector, so the inputs coincide. Thus uniqueness for the one stated load and global injectivity are equivalent here. Rank four leaves left nullity $6-4=2$: two independent restrictions still exclude many loads. The word “compatible” is essential; a system with no solutions is not a uniquely solvable system.

## LR17

**Distinguish an affine direction from its translated set.** If $x_p\ne0$ is a solution for $b\ne0$, then $A(2x_p)=2b\ne b$ over the reals, so even scalar closure fails. The zero-vector argument works over every field without needing this real example. For compatible loads, subtracting $x_p$ converts the entire fiber bijectively into $\ker A$: $A(x-x_p)=0$. Thus the fiber has a well-defined affine dimension $n-r$ even though it has no subspace basis in the usual sense. A particular solution together with a basis of directions is the correct description.

## LR18

**Verify the geometry algebraically.** For load three, $(x_1,x_2)=(3+t,-t)$ has sum three for every real $t$; for load five, $(5+s,-s)$ has sum five. The kernel direction has sum zero, so moving along it cannot change a load. Distinct parameter values within either line give distinct points because $(1,-1)\ne0$. Each fiber therefore has affine dimension one, while the image is the one-dimensional scalar output space. Parallelism concerns the common direction; it does not mean the two translated lines coincide or share a point.

## LR19

**Justify multiplication of the choices.** Fix one particular solution $x_p$ and an independent kernel basis $v_1,v_2$. The map $(s,t)\mapsto x_p+sv_1+tv_2$ is onto the solution set by the affine-fiber theorem and is one-to-one by independence. Its domain has $9\cdot9=81$ elements, proving the count without double counting. A field with nine elements is not the ring of integers modulo nine: the latter has zero divisors and does not support ordinary field row reduction. The formula assumes an actual field of order nine and a compatible load; an incompatible load has zero solutions.

## LR20

**Explain why the condition is sufficient.** The set $H=\{b\in\mathbb R^3:-b_1-2b_2+b_3=0\}$ has dimension two: its first two coordinates are free and its third is fixed by them. Every output $Ax$ lies in $H$, by the original row relation. Since the image also has dimension two, this containment is equality. Thus every point of $H$ is attained. If rank were one instead, the image could be a line properly inside this plane, and another independent left-kernel relation would be needed. Necessity alone would not justify accepting all loads in the plane.

## LR21

**Do not mix existence with uniqueness.** Rank equality $\operatorname{rank}[A\mid b]=\operatorname{rank}A$ proves that some solution exists. It leaves the kernel unchanged, so it gives uniqueness only if the coefficient rank also equals the number of unknowns. If augmentation raises rank, a reduced row of the form $[0\;\cdots\;0\mid c]$ with $c\ne0$ certifies the contradiction. This geometric argument works over every field: one appended vector either belongs to the old span or extends a basis by exactly one vector. The load column is not an extra unknown.

## LR22

**Read the matrix equation column by column.** Writing $X=[x^{(1)}\;x^{(2)}]$ gives the separate demands $Ax^{(1)}=e_2$ and $Ax^{(2)}=e_3$. For $x=(u,v)^T$, however, $Ax=(u,0,0)^T$, so neither demand can hold. The concatenation contains the three independent vectors $e_1,e_2,e_3$ and one redundant zero column, hence has rank three. Notice that $B$ itself has rank two; the rank comparison relevant to compatibility is between $A$ and $[A\;B]$, not between $A$ and $B$ alone.

## LR23

**Give the dimension proof, including uniqueness of coordinates.** If $NC_1=NC_2$, each column of $C_1-C_2$ is annihilated by the injective map $N:F^{n-r}\to F^n$. Therefore $C_1=C_2$, so the $k(n-r)$ scalar entries are genuinely independent coordinates. In the full-column-rank case $n-r=0$, the correction matrix has no rows and the compatible solution is unique. Over a finite field with $q$ elements the same bijection gives $q^{k(n-r)}$ solution matrices. If even one load column is incompatible, there are none; counting parameters must follow, not precede, the compatibility test.

## LR24

**Expand the full family and its meaning.** Every left inverse has the form $L=\begin{bmatrix}1-s&-s&s\\-t&1-t&t\end{bmatrix}$. Multiplying its first row by the two columns of $A$ gives $(1-s+s,-s+s)=(1,0)$; the second gives $(-t+t,1-t+t)=(0,1)$. Conversely, $LA=I_2$ implies $(L-L_0)A=0$, forcing each difference row into the one-dimensional left kernel. Thus no other left inverses are missed. These maps agree on attainable outputs $\operatorname{Col}A$, where input recovery is unique, but may act differently on outputs outside that plane. Nonuniqueness therefore does not contradict injectivity of $A$.

## LR25

**Write the two columns and verify them.** The full family is $R=\begin{bmatrix}1-s&-t\\-s&1-t\\s&t\end{bmatrix}$. Its first column maps to $(1,0)^T$ and its second to $(0,1)^T$, so $AR=I_2$. Conversely, subtract any such $R_0$ from another right inverse: both difference columns must map to zero, and the kernel line supplies exactly the two independent coefficients $s,t$. Each choice selects one preimage for every output in a linear way. No choice can satisfy $RA=I_3$, since a nonzero kernel vector $v$ would then give $v=RAv=0$, a contradiction.

## LR26

**Check shapes and the remaining limitation.** If $A$ is $m\times n$, then $A^TA$ is $n\times n$ and the resulting left inverse is $n\times m$. Its product in the other order is $A(A^TA)^{-1}A^T$, an $m\times m$ projection onto the image, generally not $I_m$. For example, with $A=(1,0)^T$ the two products are $1$ and $\operatorname{diag}(1,0)$. Over complex scalars replace every transpose in this construction by the conjugate transpose. This is an algebraic existence formula; numerically forming normal equations can worsen conditioning, so existence is not a recommendation to implement every solver this way.

## LR27

**Exhibit the missing output rather than relying only on shape.** If a right inverse $R$ existed, applying $AR=I_3$ to $e_3$ would give $A(Re_3)=e_3$. But every vector in the image has third coordinate zero. This is impossible. The matrix $L=\begin{bmatrix}1&0&0\\0&1&0\end{bmatrix}$ does satisfy $LA=I_2$. The lower bound proves that distinct inputs remain distinct and that small output differences cannot hide a large input difference on this image. It cannot supply the nonexistent preimage of $e_3$. The Euclidean norm equality is verified directly by $\Vert Ax\Vert ^2=x_1^2+x_2^2$.

## LR28

**An alternative proof avoids introducing an inverse early.** From $AB=I_n$, the product rank is $n$, so both factors have rank $n$. In particular $\ker A=\{0\}$. Now $A(BA-I_n)=(AB)A-A=A-A=0$. Every column of $BA-I_n$ is therefore in the zero kernel of $A$, forcing that matrix to be zero. This proof states exactly where finite square dimensions are used: product rank $n$ exhausts all input dimensions of $A$. With rectangular factors the two identity sizes differ, and the same inference is unavailable.

## LR29

**Check the ordering on a witness.** For $e_1=(1,0,0,\ldots)$, $De_1=0$ and hence $SDe_1=0\ne e_1$, whereas $DSe_1=e_1$. The shift $S$ is injective but not onto because its first output entry is always zero; $D$ is onto but not injective because it deletes that entry. Both maps are linear on the space of all real sequences. There is no contradiction with the finite theorem: this space is infinite-dimensional, and equality of domain and codomain as sets of sequences does not permit subtraction of finite dimensions as in $n-r$.

## LR30

**Follow one arbitrary input through the bottleneck.** For $x=(x_1,x_2,x_3)^T$, the intermediate vector is $Fx=(x_1+2x_2,x_3)^T$. Multiplying by $C$ gives $(x_1+2x_2+x_3,2x_1+4x_2,x_3)^T$, exactly $Ax$. The two coordinates record the independent combinations that survive; changing $x$ along $(-2,1,0)^T$ leaves them unchanged. Conversely, every two-coordinate intermediate vector is reachable by choosing $x_2=0$. Thus $F$ is onto and $C$ is injective. This explains the factorization structurally, rather than only displaying two arrays whose product happens to agree.

## LR31

**Prove the common-image premise as well.** Because $F$ has row rank $r$, it maps onto $F^r$. Hence every column combination $Cz$ can be written as $CFx=Ax$ for some $x$, so $\operatorname{Col}C=\operatorname{Col}A$. The same argument applies to $D$. To see why $H$ is nonsingular, $Hz=0$ would imply $Dz=CHz=0$; independence of the columns of $D$ forces $z=0$. The square matrix $H$ is therefore invertible. This argument requires both factors to have the full intermediate rank; inserting redundant intermediate coordinates would destroy the uniqueness of that basis change.

## LR32

**Verify the coordinate transformation explicitly.** Here $Q=\begin{bmatrix}0&1\\1&0\end{bmatrix}=Q^{-1}$. Applying it to the old null direction gives $Q^{-1}(-2,1)^T=(1,-2)^T$, the new direction. The image remains the whole scalar output space, since right multiplication by an invertible matrix merely reparameterizes every possible input. Thus column operations preserve image and rank, but transport kernel and row-space coordinates. Row operations have the complementary behavior: they preserve the right kernel exactly and transport the image. State the side of the invertible multiplication before asserting that a particular subspace is unchanged.

## LR33

**Distinguish an input equation from an output axis.** The original scalar input $t$ produces $(t,0)^T$; after the row swap it produces $(0,t)^T$. Both outputs vanish exactly when $t=0$, so the kernel remains zero. But $(1,0)^T$ belongs only to the original image and $(0,1)^T$ only to the transformed image. The row-space basis in each case is the one-entry row $(1)$, so the row space is unchanged too. An invertible output transformation preserves dependence coefficients among columns without preserving their literal positions in the output plane.

## LR34

**Account for all intermediate directions.** The image of $B$ is a three-dimensional subspace of $F^4$. Exactly one of its dimensions lies in $\ker A$ and is killed. The remaining two independent directions give the two-dimensional image of the product. Global nullity of $A$ is $4-2=2$, but only one of those two directions is actually reached by $B$; subtracting the entire nullity would incorrectly give rank one. Rank–nullity is being applied to $A|_{\operatorname{Col}B}$, whose domain is the image of $B$, rather than to the full four-dimensional domain of $A$.

## LR35

**Specify actual matrices, not only dimensions.** Use $A=\begin{bmatrix}1&0&0&0&0\\0&1&0&0&0\\0&0&1&0&0\\0&0&0&0&0\end{bmatrix}$. For the rank-two product choose the six columns of $B$ as $e_1,e_2,e_4,e_5,0,0$ in $\mathbb R^5$; its product columns are the first two standard output vectors and four zeros. For the rank-three product use $e_1,e_2,e_3,e_4,0,0$ instead. Both $B$ matrices have rank four. Their intersections with $\ker A=\operatorname{span}(e_4,e_5)$ have dimensions two and one, respectively, explaining both outcomes by the exact formula.

## LR36

**Compare with an actually zero product having the same ranks.** Retain $A=\operatorname{diag}(1,0)$ but replace $B$ by $\operatorname{diag}(0,1)$. Now both factor ranks are still one while $AB=0$, because the reached second axis is precisely the kernel of $A$. Thus identical sizes and identical individual ranks admit either product rank zero or one. Sylvester only guarantees $\max(0,1+1-2)=0$ as a lower bound; it does not force equality. This pair of constructions isolates alignment as the missing information and refutes any rule that tries to determine product rank solely from factor ranks.

## LR37

**Check both powers on every basis vector.** The three nonzero images are $e_1,e_3,e_5$, which are independent. Those vectors and $e_7$ themselves map to zero, so the kernel is $\operatorname{span}(e_1,e_3,e_5,e_7)$ of dimension four. Every image is inside this kernel, hence the square vanishes on every basis vector and therefore on the whole space. Rank three and nullity four sum to seven. The estimate generalizes to $r\le\lfloor n/2\rfloor$; direct sums of two-vector chains plus, if needed, one killed vector attain it. Merely exhibiting one matrix would prove attainability but not maximality.

## LR38

**Keep both bounds in view.** For $m\times n$ matrices the full statement is $|r_A-r_B|\le r_{A+B}\le\min(m,n,r_A+r_B)$. The lower inequality follows from two separate rearrangements, so taking only $r_A-r_B$ would miss the case $r_B>r_A$. With $B=-A$, both factor ranks are equal and the lower bound becomes zero, attained by the zero sum. To attain the upper bound in a simple case, use $A=\operatorname{diag}(1,0)$ and $B=\operatorname{diag}(0,1)$. Thus the individual rank data permit both cancellation and addition; the matrices themselves determine which occurs.

## LR39

**Find the joint-coordinate obstruction.** The sum map is $t\mapsto(t,t)$, so its image is the diagonal line, not the whole output plane. Horizontal concatenation $[A\;B]=I_2$ instead allows independent inputs $(s,t)$ and has rank two. Therefore $\operatorname{Col}(A+B)$ is contained in $\operatorname{Col}A+\operatorname{Col}B$ but may be a proper subspace. Disjoint images ensure a unique decomposition of a vector already in that sum; they do not ensure that one shared input can realize every pair of components. The distinction concerns independent controllability as well as independent output directions.

## LR40

**A constructive way to locate the shared direction.** Solve $Cu=Dv$, equivalently $[C\;-D](u,v)^T=0$. Because both $C,D$ have independent columns, a nonzero solution cannot have just one of $u,v$ zero. Mapping such solutions to $Cu$ gives a bijection onto the intersection. In this case the six-column constraint matrix has rank five and nullity one, so there is exactly one independent shared direction. Its coordinates in the two chosen bases may differ completely. The dimension formula supplies the count; solving the block equation would supply the actual basis vector if the entries were provided.

## LR41

**Use the correct dimension formula for each construction.** If $S=\begin{bmatrix}A\\B\end{bmatrix}$ has three input columns, then $\dim(\ker A\cap\ker B)=3-\operatorname{rank}S$. If $H=[A\;B]$ has three output rows, then $\dim(\operatorname{Col}A+\operatorname{Col}B)=\operatorname{rank}H$. When both individual ranks are known, their image-intersection dimension is $r_A+r_B-\operatorname{rank}H$. The stack tests two sets of equations on one input, while concatenation permits two independently chosen inputs. Counting rows in the first or columns in the second without testing independence confuses constraints with generators.

## LR42

**Prove that the displayed intersection basis is complete.** A vector satisfying both membership conditions must have the form $(0,a,b,0)^T$, so every such vector is a combination of $e_2,e_3$. Conversely both basis vectors are visibly in each original span, proving equality in both directions. The sum contains $e_1$ from $U$, $e_4$ from $W$, and $e_2,e_3$ from either; hence it is all of $\mathbb R^4$. The two shared directions were counted twice in $3+3$, and subtracting their dimension once leaves four. A set intersection and a vector-space sum are different operations; neither is obtained by merely appending all original vectors.

## LR43

**Derive the bound as a restricted-kernel count.** Put $U=\operatorname{Col}B$ and $W=\operatorname{Col}(BC)\subseteq U$. The kernel of $A|_U$ has dimension $5-4=1$. The restriction to $W$, a three-dimensional domain, can lose at most that one dimension because $W\cap\ker A\subseteq U\cap\ker A$. Therefore $\operatorname{rank}(ABC)=3-\dim(W\cap\ker A)$ is either two or three. Both are attainable: let $B=I_5$, $A=\operatorname{diag}(1,1,1,1,0)$, and let the three columns of $C$ be either $e_1,e_2,e_5$ or $e_1,e_2,e_3$. These choices realize losses one and zero.

## LR44

**Give a certificate on each stratum.** The row-subtraction matrix $E=\begin{bmatrix}1&0&0\\-1&1&0\\-1&0&1\end{bmatrix}$ is invertible with determinant one, and $EA=\begin{bmatrix}1&1&1\\0&s&0\\0&0&t\end{bmatrix}$. This proves the branches without dividing by a possibly zero parameter. When both vanish, a nonzero first row proves rank one; when exactly one survives, its zero first coordinate proves independence from the first row; when both survive, the determinant $st$ is nonzero. Merely computing $\det A=st$ would separate invertible from singular cases but would not distinguish ranks one and two on the singular axes.

## LR45

**Verify the parameterization in the original equations.** The first row gives $x_1+x_2+x_3=b_1$. With $s=0$ the second row is identical, so it demands $b_2=b_1$. The third row adds $t x_3$ to the first, giving $b_3-b_1$ and fixing $x_3$. Substitution of the proposed $x$ therefore verifies all three equations. The free direction is $(-1,1,0)^T$ and is nonzero; changing its coefficient gives distinct inputs. If the load condition fails there are no inputs at all, despite the coefficient rank and nullity remaining two and one. Nullity counts a compatible fiber, not a guarantee of compatibility.

## LR46

**Explain why a continuous matrix can skip an integer rank.** The determinant is $(t-1)^2$, so every $t\ne1$ has rank three. At $t=1$ the matrix is the all-ones matrix, whose image is the line spanned by $(1,1,1)^T$. Both additional pivot directions disappear at the same parameter. The real-valued entries vary continuously, but rank is an integer-valued count and is not a continuous function. Near $t=1$, a numerical tolerance may report an effective smaller rank; that does not create an exact rank-two value in this family.

## LR47

**State a complete rank certificate.** A rank-$r$ claim requires both a lower and an upper bound. Here the $2\times2$ identity minor proves rank at least two, while the zero third column bounds the column span by the first two columns and proves rank at most two. In a general $3\times3$ singular matrix, determinant zero gives only the upper bound two. A nonzero entry would prove merely rank at least one and would still leave two possibilities. This “nonzero smaller minor plus vanishing larger structure” pattern is especially useful when parameters make the full determinant vanish.

## LR48

**Compute the relevant minors.** For column pairs $(1,2),(1,3),(2,3)$ the determinants are respectively $0,1,2$. At least one nonzero two-column minor proves rank two, already the maximum allowed by two rows. Over characteristic two the last determinant vanishes, but the middle remains one, so rank is still two. Thus even field changes do not rescue the proposed shortcut in this example. To prove rank at most one, every two-column minor must vanish; checking one convenient pair can miss a pivot located in a later column.

## LR49

**Justify the decomposition and count multiplicities.** Any real $x\in\mathbb R^4$ has the unique decomposition $x=a\mathbf1+z$, where $a=(x_1+x_2+x_3+x_4)/4$ and $z$ has coordinate sum zero. Since $J\mathbf1=4\mathbf1$ and $Jz=0$, the two scalar actions follow directly. A nonzero scalar on the zero-sum space contributes three image dimensions, not one. For $d=c\ne0$ the rank is one; for $d=-3c$ with $c\ne0$ it is three; the common zero case gives the zero matrix. Division by four explains why this real argument must be reconsidered in characteristic two.

## LR50

**Compare kernels as well as ranks.** Over the reals, adding and subtracting the two equations in $Ax=0$ forces $x_1=x_2=0$. Over $\mathbb F_2$, the single remaining equation is $x_1+x_2=0$, and its kernel is $\{(0,0),(1,1)\}$, a one-dimensional space. The output is either $(0,0)$ or $(1,1)$, so image size two also confirms rank one. Integer determinant $-2$ is nonzero in $\mathbb R$ but equals zero after reduction modulo two. Rank must be computed after interpreting coefficients in the specified field.

## LR51

**Identify the invalid positivity step.** Plain transpose would produce $z^Tz$, which may vanish for a nonzero complex vector: $(1,i)$ is isotropic for that bilinear form. The Hermitian expression is $z^*z=|z_1|^2+|z_2|^2$, which is positive for every nonzero vector. Consequently $\ker(C^*C)=\ker C$ is justified by $x^*C^*Cx=\Vert Cx\Vert ^2$, whereas the analogous plain-transpose reasoning is false. The example uses a column of length two, so both Gram products are one-by-one matrices: their ranks are decided by whether the resulting scalar is zero, not by their displayed size.

## LR52

**Make a numerical convention explicit.** The singular values are $1$ and $|\epsilon|$, in decreasing order when $|\epsilon|\le1$. If numerical rank counts singular values strictly above $\tau\sigma_{\max}$ with $0<\tau<1$, then $0<|\epsilon|\le\tau$ gives numerical rank one but exact rank two. At $|\epsilon|=\tau$, the strict convention excludes the second value; an inclusive convention would differ. Scaling the entire matrix changes an absolute threshold comparison but leaves a relative comparison unchanged. These are declared resolution decisions, not contradictory algebraic answers about the same exact nonzero parameter.

## LR53

**Show the reversible operation behind the Schur complement.** Solving $(a,b)P=(2,2)$ gives $(a,b)=(1,1)$, so the row operation $R_3\leftarrow R_3-R_1-R_2$ produces bottom row $(0,0,t-4)$. The first two rows have pivots in columns one and two because their leading block is invertible. At $t=4$, the bottom row vanishes, giving rank two; elsewhere it supplies the third pivot. At the exceptional value a kernel vector is $(-1,-1,1)^T$, since the original third column equals the sum of the first two. The formula and direct row calculation therefore certify the same branch.

## LR54

**Explain exactly why the Schur shortcut is illegal.** A formula involving $P^{-1}$ cannot be used when the leading scalar block is zero. The actual linear map sends $(x_1,x_2)^T$ to $(x_2,0)^T$, so its image is the first axis and its kernel is the same first axis in input coordinates. Rank one follows immediately. The two diagonal blocks separately miss the transfer from the second input block to the first output block. In a block-diagonal matrix this cross transfer is absent, which is the additional structural fact that makes rank addition valid there.

## LR55

**Use the direct-product description.** The map sends $(u,v)\in F^4\times F^3$ to $(Cu,Dv)\in F^3\times F^2$. Its kernel is $\ker C\times\ker D$, of dimension two plus two; its image is $\operatorname{Col}C\times\operatorname{Col}D$, of dimension two plus one. Its left kernel similarly splits into the one-dimensional left kernel of each block. These constructions prove the rank and both nullities without assuming any particular entries or a common basis across blocks. The two conservation equations are $3+4=7$ for inputs and $3+2=5$ for outputs.

## LR56

**Check the kernel by the displayed equations.** The updated system is $-2x_1+x_2=0$ and $x_3=0$, with an identically zero first row. Hence $x=(t,2t,0)^T=t u$, agreeing with the rank-one argument. This example loses exactly one rank because $I_3$ originally has trivial kernel and the update creates precisely that one line. The equality $(I+uv^T)u=0$ alone establishes only that $u$ is a kernel vector; proving that every kernel vector is proportional to $u$ is the step that rules out a larger rank drop.

## LR57

**An explicit inverse checks the nonexceptional branch.** Here the update is $M=\begin{bmatrix}2&0&0\\2&1&0\\0&0&1\end{bmatrix}$. Solving $Mx=b$ gives $x_1=b_1/2$, $x_2=b_2-b_1$, $x_3=b_3$, hence $M^{-1}=\begin{bmatrix}1/2&0&0\\-1&1&0\\0&0&1\end{bmatrix}$. Multiplication in either order gives $I_3$. More generally the inverse is $I-uv^T/(1+v^Tu)$ when the denominator is nonzero. That denominator must be tested before division; the preceding problem is precisely the exceptional branch where the same expression is undefined and a one-dimensional kernel appears.

## LR58

**Show that all three outcomes can occur.** Rank increases by one if $A=\operatorname{diag}(1,0)$ and the update is $e_2e_2^T$, giving $I_2$. It decreases by one if $A=I_2$ and the update is $-e_2e_2^T$, giving $\operatorname{diag}(1,0)$. It stays unchanged if $A=I_2$ and the update is $e_1e_1^T$, giving $\operatorname{diag}(2,1)$ over the reals. Thus “rank-one update” names the rank of the added matrix, not a guaranteed increase in the resulting rank. The two-sided estimate follows from two sum inequalities and requires no determinant or square shape.

## LR59

**Decompose an arbitrary vector.** For $x=(a,b)^T$, $Px=(a+2b,0)^T$ and $(I-P)x=(-2b,b)^T=b(-2,1)^T$. Their sum is exactly $x$. Applying $P$ fixes the first term and kills the second, so every vector has a unique image-plus-kernel decomposition. The projection moves along the slanted kernel direction rather than perpendicular to the horizontal image. This explains the word “oblique.” The matrix is not symmetric, and the two summands have dot product $-2b(a+2b)$, generally nonzero. Idempotence describes repeated action, while orthogonality describes the angle between the component spaces.

## LR60

**Supply the trace-invariance step.** If $Q$ is the change-of-basis matrix, the adapted matrix is $Q^{-1}PQ=\operatorname{diag}(I_r,0)$. For compatible square products, $\operatorname{tr}(XY)=\sum_{i,j}x_{ij}y_{ji}=\sum_{j,i}y_{ji}x_{ij}=\operatorname{tr}(YX)$. Therefore $\operatorname{tr}(Q^{-1}PQ)=\operatorname{tr}(PQQ^{-1})=\operatorname{tr}P=r$. No orthogonality of $Q$ is needed. The real-field qualification makes $r$ an ordinary integer scalar; in positive characteristic the trace records that integer modulo the characteristic and may be zero even for a nonzero-rank identity matrix.

## LR61

**Separate nesting from equality.** For every $j$, $\ker A^j\subseteq\ker A^{j+1}$ because applying one further $A$ to zero still gives zero. Hence equal dimensions of two consecutive kernels force equality of the spaces, but equal dimensions of arbitrary unrelated subspaces would not. Once equality occurs, the proof in the solution propagates it one step and induction handles all later steps. In an $n$-dimensional space at most $n$ strict dimension increases can occur, so eventual stabilization is guaranteed. A plateau cannot be followed by a later increase. The ranks of powers therefore form a nonincreasing sequence that stays constant after its first repeated consecutive value.

## LR62

**Check the endpoint and the first nonzero chain.** For $k=2$, the images of $e_3,e_4,e_5$ are $e_1,e_2,e_3$, while $e_1,e_2$ are killed. Thus rank three and nullity two are concrete, not merely inferred from a pattern. At $k=5$ every chain has reached zero, so the entire matrix power vanishes. At $k=0$ the identity has rank five and nullity zero; for every $k\ge5$ rank remains zero by stabilization. The chain length controls when each input direction disappears, which is more informative than knowing only the rank four of $A$ itself.

## LR63

**Show that the bound is sharp for each remainder of n.** Write $n=3q+s$ with $s\in\{0,1,2\}$. Use $q$ disjoint three-vector chains, each contributing dimension three and rank two. If $s=1$, add one killed vector; if $s=2$, add a two-vector chain of rank one. The resulting cube is zero and its rank is $2q+\lfloor2s/3\rfloor=\lfloor2n/3\rfloor$. This construction is compatible with the two Sylvester inequalities and proves the maximum, rather than only an upper bound. Each chain contribution can be checked by mapping its last vector down one position and killing its first.

## LR64

**Exhibit a complete basis, not only a count.** Let $E_{ij}$ have a single one in position $(i,j)$. Six matrices $E_{ij}+E_{ji}$ for $i<j$ independently choose the symmetric off-diagonal entries. Three further matrices $E_{11}-E_{44}$, $E_{22}-E_{44}$, $E_{33}-E_{44}$ independently choose the first three diagonal entries with the fourth fixed by trace zero. These nine matrices are independent by entry comparison and span every admissible matrix. The twice-trace equation adds no restriction because it is a scalar multiple of the first; over the reals multiplying a functional by two does not change its kernel.

## LR65

**A basis confirms the dimension eight.** Use the same three trace-zero diagonal directions as in the preceding solution and the five off-diagonal symmetric pairs other than $E_{12}+E_{21}$. Entry comparison proves independence and shows that every allowed matrix is generated. The omitted pair is exactly the coordinate suppressed by $a_{12}=0$; symmetry already makes $a_{21}=0$, so it is not a third independent restriction. The two witness matrices in the original proof establish surjectivity of the constraint map before subtracting its rank. Counting both mirrored entries as separate unknowns would overstate the ambient dimension.

## LR66

**Construct the free-coordinate basis.** For each pair $i<j$, choose $F_{ij}=E_{ij}+E_{ji}-E_{ii}-E_{jj}$. Its two affected row sums vanish, and all other row sums are zero. The $n(n-1)/2$ matrices are independent because each has a unique off-diagonal pair. Conversely, choosing the off-diagonal entries of a symmetric row-sum-zero matrix determines the diagonal entries uniquely, so these vectors span the whole kernel. For $n=1$ the basis is empty and the only matrix is zero, consistent with the formula. Row-sum constraints are independent because diagonal input matrices can produce any prescribed row-sum vector.

## LR67

**Write the interpolation witnesses.** The polynomials $\ell_0=(x-1)(x-2)/2$, $\ell_1=-x(x-2)$ and $\ell_2=x(x-1)/2$ give evaluation outputs $(1,0,0)$, $(0,1,0)$ and $(0,0,1)$, respectively. Thus the map onto three outputs is surjective. The factor theorem successively divides a kernel polynomial by $x$, $x-1$ and $x-2$ because the roots are distinct. The remaining factor has degree at most one, so precisely two coefficients remain. These witnesses prove both independent constraints and the complete kernel description; merely seeing three written equations would not prove their independence.

## LR68

**Identify the attainable output subspace.** Every output has the form $(a,a,b)^T$, and the linear polynomial $p(x)=a+(b-a)x$ realizes any such pair. Hence the image is a plane in $\mathbb R^3$ and its left kernel is spanned by $(1,-1,0)^T$. The zero-output condition still imposes only $p(0)=p(1)=0$; repeated evaluation at zero does not impose $p'(0)=0$. The latter would be a different functional and would enforce a repeated root. The three-dimensional kernel consists of $x(x-1)(c_0+c_1x+c_2x^2)$ with independently chosen coefficients.

## LR69

**Represent the operator with its two bases stated.** In domain basis $(1,x,x^2,x^3,x^4)$ and codomain basis $(1,x,x^2,x^3)$, the derivative matrix is $\begin{bmatrix}0&1&0&0&0\\0&0&2&0&0\\0&0&0&3&0\\0&0&0&0&4\end{bmatrix}$. Its four pivot columns are the nonconstant monomials. For an output $a_0+a_1x+a_2x^2+a_3x^3$, a preimage is $a_0x+(a_1/2)x^2+(a_2/3)x^3+(a_3/4)x^4$, plus any constant. This makes both surjectivity and one-dimensional input ambiguity explicit and shows exactly which divisions rely on characteristic zero.

## LR70

**Compute coefficients before counting pivots.** For $p=a_0+a_1x+a_2x^2+a_3x^3+a_4x^4$, formal differentiation in characteristic two gives $Dp=a_1+a_3x^2$. Thus output coordinates one and $x^2$ vary independently, while the other two codomain coordinates are always zero. The kernel equations are $a_1=a_3=0$; coefficients $a_0,a_2,a_4$ remain free. This concerns formal polynomials as vectors, not polynomial functions identified by their values on a finite field. Distinct formal polynomials may induce the same function on that field, and quotienting by that relation would change the vector space being studied.

## LR71

**Verify independence of the path-generated vectors.** Choose root vertex $n$. In a relation $\sum_{i=1}^{n-1}c_i(e_i-e_n)=0$, coordinate $i$ is $c_i$, so all coefficients vanish. Every zero-sum vector $z$ equals $\sum_{i=1}^{n-1}z_i(e_i-e_n)$, proving spanning. Orientation only changes signs of the selected incidence columns and cannot change rank. For a graph with $c$ connected components, apply the same argument separately in each component to obtain rank $n-c$, with one independent constant left-kernel vector per component. Connectivity is exactly the hypothesis that reduces this count to one.

## LR72

**Quantify the kernel change.** The new kernel is $K\cap\ker c^T$ where $K=\ker A$. If $c^T|_K$ is zero, no old ambiguity is removed. Otherwise it is a nonzero functional onto the one-dimensional scalar field, so rank–nullity on $K$ gives a kernel of dimension $\dim K-1$. The new matrix rank consequently rises from $r$ to $r+1$. For example, $A=(1,1)$ has null direction $(1,-1)^T$. Appending $(2,2)$ adds no information, while appending $(1,0)$ distinguishes that direction and makes the two-input system injective. The numerical scale of a redundant sensor row cannot make it independent.

## LR73

**Give the dimension argument behind the orthogonal-complement identity.** Every row annihilates the kernel, so $\operatorname{Row}A\subseteq(\ker A)^\perp$. Both spaces have dimension $r$, since the orthogonal complement has dimension $n-(n-r)=r$. Hence containment is equality. Apply the same argument to $B$ to establish the claim. With unequal row counts, even identical row spaces cannot be connected by one invertible matrix of a common row size; extra redundant or zero equations may be present. Over a general field the corresponding statement uses annihilators in the dual space, avoiding an unjustified Euclidean positivity assumption.

## LR74

**Check the converse and a counterexample to global injectivity.** If $A$ is injective on $\operatorname{Col}B$, its restriction has zero kernel, so the product retains all $r_B$ independent attained directions and has rank $r_B$. For a proper restriction example take $A=\operatorname{diag}(1,0)$ and $B=(1,0)^T$. Then $AB=B$ has rank one, although $A$ kills $e_2$ and is not globally injective. Only the reached first-axis subspace matters. This equivalence also includes $B=0$, whose image is the zero space and on which every linear map is injective in the vacuous sense.

## LR75

**Distinguish equality with the formal and truncated bounds.** Put $r=\operatorname{rank}A$, $s=\operatorname{rank}B$, and $K=\ker A$ of dimension $n-r$. Equality $\operatorname{rank}(AB)=r+s-n$ requires $\dim(\operatorname{Col}B\cap K)=\dim K$, hence $K\subseteq\operatorname{Col}B$. If $r+s<n$, that formal expression is negative and cannot equal a rank. Equality with the usable lower bound zero instead means $\operatorname{Col}B\subseteq K$, the reverse containment. At $r+s=n$, equality zero and the matching dimensions force the two spaces to be equal. This boundary explains why reversing the containment gives a wrong equality test.

## LR76

**Compute the sum on an arbitrary input.** For $x=(s,t)^T$, $Ax=(s,0)^T$, $Bx=(0,t)^T$, and $(A+B)x=(s,t)^T$. Both output directions can be chosen independently because different input coordinates control them. By contrast, two one-column maps can only receive one shared scalar, so their sum has rank at most one regardless of the angle between output columns. This example proves attainability of additive rank in a separated case; it is not a general theorem that visually distinct columns automatically add ranks. Product, sum and concatenation have different input-sharing structures.

## LR77

**Show the directness explicitly.** If $y$ is in both $\operatorname{Col}P$ and $\operatorname{Col}(I-P)$, then the first membership gives $Py=y$ and the second gives $Py=0$, so $y=0$. Also $x=Px+(I-P)x$ for every $x$, so the two images span the entire space. Their dimensions therefore add to $n$. The identities $P(I-P)=(I-P)P=0$ express the same separation algebraically. Neither a symmetric matrix nor an orthonormal basis was needed. For the earlier oblique projection, the two images are the horizontal line and the slanted line spanned by $(-2,1)^T$.

## LR78

**Use the general outer-product trace formula.** If $A=uv^T$, then $\operatorname{tr}A=\sum_i u_iv_i=v^Tu$ and $A^2=u(v^Tu)v^T$. Taking nonzero orthogonal $u=e_1,v=e_2$ makes both the trace and square zero while preserving rank one. A nonzero rank-one idempotent instead requires $v^Tu=1$, so its trace is one. Thus the projection theorem relies on the multiplication identity $A^2=A$, not merely on low rank or a particular diagonal pattern. This also explains why a matrix can carry a nontrivial image direction while every diagonal entry vanishes.

## LR79

**Construct an attaining product with all shapes explicit.** Let $W=[I_2\;0_{2\times5}]$, let $V$ embed $(a,b)$ as $(a,b,0)$, and let $U$ embed three coordinates as the first three of eight outputs. Then $UVW$ has ones in positions $(1,1),(2,2)$ and zeros elsewhere, so its rank is two. The bound is the minimum of all intermediate dimensions and the final ambient sizes, here $\min(8,3,2,7)=2$. Zero or dependent factors can make the actual rank smaller; the construction shows the best attainable value using dimensions alone.

## LR80

**Check whether the shift lies along the direction.** A translated set $a+\operatorname{span}v$ is a subspace exactly when $a\in\operatorname{span}v$, because then the translation leaves the line unchanged. Here $(1,1)$ is not a multiple of $(1,2)$: the first coordinate would require multiplier one and the second one-half. Thus the shift is genuinely transverse to the original line. A translated line is not automatically non-linear; for example $(1,2)+t(1,2)$ is the original span. The zero test detects the relevant membership condition directly and avoids that overgeneralization.

## LR81

**Identify precisely which axiom fails.** The set contains zero and is closed under every real scalar because $(\lambda x)(\lambda y)=\lambda^2xy\ge0$ whenever $xy\ge0$. Those two properties alone do not suffice: closure under addition is also required and the stated pair violates it. The admissible points occupy the first and third closed quadrants, rather than a line or plane subspace. Consequently one cannot assign a nullity by subtracting the number of written inequalities from two. Rank–nullity concerns kernels of linear maps, which satisfy all linear-combination closure properties simultaneously.

## LR82

**Supply a matrix certificate and the dimension count.** The restriction matrix is $C=\begin{bmatrix}-2&1&0\\0&-1&1\end{bmatrix}$. Its two rows are independent because the first has a nonzero first entry and the second does not. Thus rank is two and nullity is $3-2=1$. Multiplication gives $C(1,2,2)^T=0$, so the nonzero displayed vector is a complete kernel basis by the dimension count. The second proposed direction $(1/2,1,1)^T$ is exactly half of it, not another independent direction. A basis may be rescaled without creating another degree of freedom.

## LR83

**Verify the coefficients in the original rows.** The combination is $(1/2)(3,4)-(1/2)(1,2)=(1,1)$. The row matrix has determinant $3\cdot2-4\cdot1=2\ne0$, so its row space is the whole plane; every two-coordinate target has a unique row-coefficient pair. The membership equations can be expressed as $A^T(s,t)^T=(1,1)^T$, emphasizing that row coefficients solve a transposed system. Solving $Ax=(1,1)^T$ instead would find coefficients of columns and would be a different calculation, even though invertibility would also make that different system solvable.

## LR84

**Separate redundancy from the zero vector issue.** A nontrivial relation is $2(1,1)^T-(2,2)^T=0$, with coefficients not both zero. Both vectors are individually nonzero, so dependence does not require that a list contain zero. A vector $(a,b)^T$ belongs to the span exactly when $a=b$; the single parameter is their common coordinate. Either singleton basis gives unique coordinates, while the original two-vector generating list gives many coefficient pairs for the same vector. This coefficient ambiguity is the linear-algebra reason that a spanning list must be reduced before it is called a basis.

## LR85

**Write the coordinate matrix and an arbitrary expansion.** In basis $(1,x,x^2)$ the proposed polynomial columns are $\begin{bmatrix}1&10&3\\-1&1&0\\1&0&0\end{bmatrix}$, whose determinant is $-3\ne0$. To express $a+bx+cx^2$, choose coefficients $\alpha=c$, $\beta=b+c$, and $γ=(a-10b-11c)/3$. Direct coefficient comparison verifies the expansion. There is no cubic component in any generator, so $x^3$ is a concrete witness outside their span in $P_3$. Independence of three vectors does not imply they span every larger ambient space containing them.

## LR86

**Find the coordinates of a general polynomial.** Write $a+bx+cx^2=\alpha(1+x)+\beta(1-x)+γ x^2$. Comparing coefficients gives $\alpha+\beta=a$, $\alpha-\beta=b$, and $γ=c$, hence $\alpha=(a+b)/2$, $\beta=(a-b)/2$, $γ=c$. These unique coordinates prove both spanning and independence at once. In characteristic two, $1-x=1+x$, so the first pair is dependent; adding one vector cannot remove an existing dependence. The real-field qualification justifies the divisions by two and the original basis-extension argument.

## LR87

**Use a complete linearity check when the zero test passes.** Scaling satisfies $2(\alpha x+\beta y)=\alpha(2x)+\beta(2y)$ for all scalars, so it is linear. The determinant map sends zero to zero, but that necessary condition is insufficient: homogeneity fails on $2I_2$ as shown. Additivity also fails because $\det I_2+\det I_2=2$ while $\det(2I_2)=4$. Its multiplicativity under matrix products is a different property. A rank–nullity calculation for the determinant as a linear functional would therefore be invalid; its zero set of singular matrices is not a vector subspace.

## LR88

**Use the right kernel for this row-space test.** Let $A$ be the three-by-four matrix of the stated rows and put $z=(-8,1,-6,5)^T$. Direct multiplication gives $Az=0$. Its rank is three, so its right kernel is exactly the line spanned by $z$. Every row-space vector $x$ satisfies $xz=0$, giving $-8x_1+x_2-6x_3+5x_4=0$. Conversely that hyperplane has dimension three and contains the three-dimensional row space, so they coincide. This is a right-kernel annihilator of rows, not the left kernel of $A$; the left kernel is zero because all three rows are independent. Confusing the two spaces would predict the wrong ambient coordinate count.
