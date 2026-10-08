1. **Closure through a homogeneous equation.** A nonzero homogeneous scalar constraint on $\mathbb R^n$ leaves dimension $n-1$. For $x+2y-z=0$, the basis $(-2,1,0),(1,0,1)$ proves dimension two; checking the free coordinates proves independence.

2. **An affine plane is not a subspace.** A consistent system $Ax=b\ne0$ is an affine translate of $N(A)$, not a subspace. The plane $x+2y-z=3$ has affine dimension two but fails the zero-vector test.

3. **Scaling closure does not give addition closure.** Containing zero and being scaling-closed are insufficient for a subspace. The union of the two axes fails addition, whereas its span is $\mathbb R^2$ of dimension two.

4. **Modified operations with a shifted zero.** For transported operations, identify the bijection before testing a basis. With $c=(1,2)$ and $\phi(u)=u-c$, the zero is $c$ and a basis is $(2,2),(1,3)$, whose translated vectors are $e_1,e_2$.

5. **A false scalar multiplication axiom.** When operations are changed, closure alone cannot replace all axioms. The rule $a\star(x,y)=(ax,0)$ fails $1v=v$ at $(0,1)$; only its horizontal-axis restriction has the expected behavior.

6. **Three parameters with only two freedoms.** Count independent parameter directions, not parameter names. The map $(a,b,c)\mapsto(a+b,2a+2b,c)$ has a one-dimensional kernel and a two-dimensional image.

7. **The logarithmic vector space.** The zero vector need not be the number zero. In the positive-real space with multiplication as addition, zero is one, basis $(2)$ gives $[8]_{(2)}=3$, and the additive inverse of eight is $1/8$.

8. **A homogeneous-looking nonlinear restriction.** A zero right side does not make a nonlinear constraint a subspace condition. For $p(0)p(1)=0$, $x$ and $1-x$ are admissible but their sum is not; the generated span still equals $P_2$.

9. **Dependent linear constraints.** Subtract the rank of constraints rather than their raw count. In $\mathbb R^4$, $x_1+x_2+x_3+x_4=0$, twice that same equation, and $x_1=x_2$ impose rank two, leaving dimension two.

10. **A field restriction changes subspace status.** Subspace status is relative to the scalar field. The real axis is a one-dimensional real subspace of $\mathbb C$, but is not a complex subspace because $i\cdot1$ leaves it.

11. **A dependency certificate from the original columns.** Redundant generators create coefficient ambiguity. For $(e_1,e_2,(2,3))$, all representations of $(5,7)$ have coefficients $(5-2t,7-3t,t)$; the basis $(e_1,e_2)$ restores uniqueness.

12. **Joint independence versus pairwise tests.** Pairwise independence does not imply joint independence. Three vectors in $\mathbb R^2$ are always dependent; $e_1+e_2-(e_1+e_2)=0$ gives an explicit pairwise-nonparallel example.

13. **Every vector need not be removable.** A dependence permits solving only for a vector with a nonzero coefficient in the witness. In $(e_1,e_2,2e_2)$, the vertical entries are redundant individually, but removing $e_1$ destroys the horizontal direction.

14. **Independence of parameterized columns.** Split parameter values before dividing by a potential pivot. The span of $(1,t),(t,1)$ has dimension two off $t=\pm1$ and dimension one at both exceptional values.

15. **A rank jump that a generic simplification hides.** Test a new generator against the old span. With fixed vectors $(1,0,1),(0,1,1)$, the column $(a,b,1)$ is redundant exactly when $a+b=1$; the dimension is then two, otherwise three.

16. **Transformed lists and a coefficient matrix.** An invertible coefficient transformation preserves independence over the stated field. If $u,v,w$ are independent, the list $(u+v,v+w,w+u)$ has coefficient determinant two: it remains independent over $\mathbb R$, but has rank two in characteristic two.

17. **A span equality with explicit recovery.** Prove span equality by recovering both old generators. The replacement $(u,v)\mapsto(u+v,u-v)$ preserves span when two is invertible; over $\mathbb F_2$ it can collapse a plane to a line.

18. **The exact relation space.** The dependence space lives in coefficient space. Four generators of rank two have two independent relations; for $v_3=v_1+v_2,v_4=2v_1+v_2$, the relation basis is $(-1,-1,1,0),(-2,-1,0,1)$.

19. **Function independence from evaluation.** Function independence concerns identities on the whole domain. Sampling $1,e^x,e^{2x}$ at $0,\log2,\log3$ yields an invertible Vandermonde matrix of determinant two, proving independence.

20. **A singular sample matrix is inconclusive.** An invertible evaluation matrix proves independence; a singular one may only reflect poor nodes. The independent polynomials $1,x^2$ have identical samples at $-1,1$ but are separated by nodes zero and one.

21. **Basis extraction from an echelon form.** Use original pivot columns for column space, reduced nonzero rows for row space, and special solutions for nullspace. For $A=\begin{bmatrix}1&2&0&3\\2&4&1&4\\3&6&2&5\end{bmatrix}$, the pivot columns are one and three, rank is two and nullity is two.

22. **Why reduced columns may answer the wrong question.** Row reduction preserves column dependency coefficients, not numerical column space. For $A$ with columns $(1,2),2(1,2)$, the reduced vector $(1,0)$ is outside the original column space.

23. **Extending a prescribed independent list.** To extend an independent list, add a vector outside its span. The plane generated by $(1,1,0),(0,1,1)$ satisfies $y=x+z$, so $e_1$ supplies a valid third basis direction.

24. **An allowed exchange and a forbidden exchange.** A basis member can be replaced by $w$ exactly when its coordinate in $w$ is nonzero. For $w=2e_1-e_2$ over $\mathbb R$, replace $e_1$ or $e_2$, but not $e_3$.

25. **A dimension bound is not a spanning certificate.** Exactly $d$ vectors in dimension $d$ form a basis only after independence or spanning is established. Four vectors $(e_1,e_2,e_3,e_1+e_2)$ in $\mathbb R^4$ fail both requirements despite the correct count.

26. **A maximal list relative to a candidate set.** State the universe of maximality. A maximal independent sublist of $e_1,e_2,e_1+e_2$ is a basis of their plane, not of the larger space $\mathbb R^3$.

27. **Nonunique representation count over a finite field.** Over $\mathbb F_q$, a consistent system with nullity $k$ has exactly $q^k$ solutions. A rank-three $4\times7$ matrix over $\mathbb F_3$ has 81 solutions per attainable right side and 27 attainable right sides.

28. **A nested dimension chain.** Proper finite-dimensional subspace inclusions force strict dimension inequalities. In a chain with endpoint dimensions five and seven and two proper inclusions, the middle dimension must be six.

29. **Equal dimensions without inclusion.** Equal finite dimensions imply subspace equality only with an inclusion premise. The $xy$ and $xz$ planes each have dimension two but are distinct; an inclusion between them would force equality.

30. **Coordinates in a nonstandard basis.** Always verify coordinates by reconstructing the original vector. The vector $(3,1)$ has coordinates $(2,1)$ in $((1,1),(1,-1))$ and $(1,1)$ in $((2,0),(1,1))$.

31. **Change-of-basis direction.** The columns of $P_{C\leftarrow B}$ are the $C$ coordinates of the $B$ vectors. For $B=((1,1),(1,-1))$ and $C=((2,0),(1,1))$, $P=\begin{bmatrix}0&1\\1&-1\end{bmatrix}$ sends $(2,1)^T$ to $(1,1)^T$; reversing the conversion requires $P^{-1}$.

32. **Coordinates in a proper subspace.** A basis of a proper subspace may give a rectangular basis matrix. The columns $(1,0,1),(0,1,1)$ recover coordinates $(2,3)$ for $(2,3,5)$, but their $3\times2$ matrix has no ordinary two-sided inverse.

33. **Dual coordinates as rows of the inverse.** Rows of a square basis matrix inverse read its coordinates. For $((1,1),(1,-1))$, the dual functionals are $(x+y)/2$ and $(x-y)/2$, giving coordinates $(1,4)$ for $(5,-3)$.

34. **A polynomial basis with a triangular coefficient matrix.** Coefficient comparison must use the selected basis. The polynomial $2+3x+4x^2$ has coordinates $(-1,-1,4)$ in $(1,1+x,1+x+x^2)$, whose coefficient matrix has determinant one.

35. **Distinct roots remove independent freedoms.** In $P_n$, $k$ distinct zero evaluations leave dimension $n+1-k$ when $k\le n+1$. In $P_4$ with roots zero, one, and two, a basis is $r,xr$ for $r=x(x-1)(x-2)$.

36. **Repeated roots and derivative conditions.** Over $\mathbb R$, $p(1)=p'(1)=0$ enforces a double root. Together with $p(-1)=0$ in $P_4$, it gives basis $r,xr$ with $r=(x-1)^2(x+1)$ and dimension two.

37. **Dependent evaluation equations.** Evaluation constraints must be ranked as functionals. In $P_3$, $p(0)=p(1)=0$ already implies $p(0)+2p(1)=0$; the dimension is two rather than one.

38. **A nonhomogeneous interpolation fiber.** Nonzero interpolation data produce affine solution sets. The constraints $p(0)=1,p(1)=2$ in $P_3$ give $1+x+(a+bx)x(x-1)$, with two free directions and no vector-subspace status.

39. **Integral and derivative constraints.** Linear functionals may involve integrals or derivatives. In $P_3$, zero integral on $[0,1]$ plus $p'(0)=0$ gives basis $x^2-1/3,x^3-1/4$ and dimension two.

40. **All polynomials versus finite-support sequences.** Algebraic span uses finite sums even for infinite generating sets. Monomials span all formal polynomials, while coordinate unit sequences span only finite-support sequences, excluding $(1,1,1,\ldots)$.

41. **Symmetric matrices with zero trace.** Symmetric trace-zero matrices have dimension $n(n+1)/2-1$ over $\mathbb R$. A basis uses off-diagonal symmetric pairs and $E_{ii}-E_{nn}$; the boundary $n=1$ has the empty basis.

42. **Symmetric and skew-symmetric decomposition.** The symmetric/skew decomposition requires two to be invertible. Over $\mathbb R$, the intersection is zero and dimensions sum to $n^2$; in characteristic two the transpose equations coincide and the intersection is nonzero.

43. **Two matrix constraints with a dependency.** Zero row and column sums on real $n\times n$ matrices leave dimension $(n-1)^2$. For $n=3$, four corner-adjusted $E_{ij}$ directions form a basis; the six sum constraints have one dependency.

44. **Symmetry plus row sums.** On symmetric matrices, zero row sums determine each diagonal independently. For order four, six off-diagonal freedoms remain, giving dimension six rather than nine or seven.

45. **Commuting with a diagonal matrix.** For diagonal $D$ with distinct-value multiplicities $m_j$, its commuting matrix space has dimension $\sum_jm_j^2$. The multiplicities $(2,1,1)$ give six allowed elementary-entry directions.

46. **A nonlinear matrix set and its linear span.** Singularity is not a linear constraint for matrix orders at least two. In order two, $E_{11}+E_{22}=I$ disproves closure, while the singular elementary matrices span all of $M_2$.

47. **Polynomial parity and a direct sum.** Real polynomials split uniquely into even and odd parts. In $P_5$ each part has dimension three; $2+3x-4x^2+x^5$ splits into $2-4x^2$ and $3x+x^5$.

48. **A sum and intersection from explicit planes.** Intersection directions measure ambiguity of decomposition. The $xy$ and $xz$ planes sum to $\mathbb R^3$, share the $x$ axis, and decompose $(a,b,c)$ as $(t,b,0)+(a-t,0,c)$.

49. **Intersecting two equation-defined spaces.** Solve simultaneous restrictions before applying the dimension formula. In $\mathbb R^4$, let $U$ satisfy $x_1+x_2+x_3+x_4=0$ and let $W=\{(a,a,b,b)\}$. Dimensions are $3,2,1,4$ for $U,W,U\cap W,U+W$; characteristic two changes the intersection.

50. **Intersection through generator coordinates.** Equating basis expansions computes an intersection without guessing common generators. The patterns $(a,b,a,b)$ and $(c,c,d,d)$ meet on $(t,t,t,t)$, so two planes have a three-dimensional sum.

51. **Redundant generators inflate a block nullspace.** The block-kernel dimension equals intersection dimension only when both generator matrices have independent columns. Duplicate $e_1$ columns produce block nullity two for an intersection of dimension one.

52. **Sharp intersection bounds.** Intersection bounds need not determine a unique value. Two dimension-six subspaces in dimension ten can intersect in any dimension two through six; coordinate-subspace constructions prove sharpness.

53. **Forced nonzero intersection.** In finite dimension $n$, $\dim U+\dim W>n$ forces a nonzero intersection. Replacing strictness by equality is invalid: two complementary coordinate planes in $\mathbb R^4$ give equality and zero intersection.

54. **Two-subspace union theorem.** For exactly two subspaces, union closure is equivalent to containment. The witnesses $u\in U\setminus W,w\in W\setminus U$ force $u+w$ outside both; no real-field assumption is needed.

55. **Three pairwise-trivial intersections are insufficient.** For three spaces, pairwise zero intersections do not prove a direct sum. The three distinct lines generated by $e_1,e_2,e_1+e_2$ have total component dimension three but sum dimension two.

56. **A nonorthogonal complement.** A complement need not be orthogonal. The lines generated by $(1,0)$ and $(1,2)$ form a direct sum, with $(5,6)=(2,0)+(3,6)$ despite a nonzero cross dot product.

57. **The dimension formula does not extend by naïve inclusion-exclusion.** Subspace dimensions do not obey naïve three-set inclusion-exclusion. Use the two-space formula iteratively; three distinct lines in a plane give predicted three by the naïve formula but actual dimension two.

58. **Polynomial intersections and least common multiples.** For divisibility subspaces, intersection uses the least common multiple. Factors $x(x-1)$ and $(x-1)(x-2)$ in $P_5$ give dimensions four, four, three, and five for the two spaces, intersection, and sum.

59. **A quotient basis from an adapted basis.** Extend a subspace basis and take cosets of the added vectors. For $U=\operatorname{span}(1,1,0)$, the quotient basis $e_2+U,e_3+U$ assigns coordinates $(y-x,z)$ to $(x,y,z)+U$.

60. **The quotient is not set subtraction.** Cosets are equal exactly when their representatives differ by a subspace vector. Modulo the horizontal axis, $(1,2)$ and $(7,2)$ represent the same vector, and the quotient zero is the whole axis.

61. **An annihilator with explicit equations.** To compute an annihilator, impose zero values on a subspace basis. The plane generated by $(1,1,0),(0,1,1)$ has annihilator spanned by $x-y+z$, of dimension one.

62. **Restriction of scalars.** Restricting complex scalars to reals doubles finite dimension. A complex basis $v_1,v_2,v_3$ yields real basis $v_1,iv_1,v_2,iv_2,v_3,iv_3$, with six independent real directions.

63. **Counting ordered bases.** Ordered basis counting excludes the entire span of previous choices. In $\mathbb F_2^3$, the counts are $7,6,4$, giving 168 ordered and 28 unordered bases.

64. **Three proper finite-field subspaces can cover.** The two-subspace union theorem must not be extended blindly to larger finite unions. Over $\mathbb F_2$, the three distinct lines in $\mathbb F_2^2$ cover all four ambient vectors.

65. **Formal polynomial versus polynomial function.** Over finite fields, formal polynomials and polynomial functions differ. On $\mathbb F_3$, $x^3-x$ is nonzero formally but vanishes everywhere, giving a one-dimensional kernel for evaluation on $P_3$.

66. **A proper subspace with equal infinite dimension.** The inclusion-plus-equal-dimension equality test requires finite dimension. Both $\mathbb R[x]$ and its proper subspace $x\mathbb R[x]$ have countably infinite monomial bases.

67. **A parameterized intersection.** Parameterized intersections may jump even when each component dimension stays fixed. For the planes $z=0$ and $z=t(x+y)$, intersection dimension is two at $t=0$ and one otherwise.

68. **Minimum constraints needed to specify a space.** The minimal number of independent homogeneous scalar equations defining a subspace is its codimension. A four-dimensional subspace in $\mathbb R^7$ requires exactly three, constructed from an adapted dual basis.

69. **A finite-function space and constrained values.** Functions on a finite set of size $m$ form an $m$-dimensional coordinate space. One nonzero total-value constraint leaves dimension $m-1$; use point indicators minus one reference indicator as a basis.

70. **Dimension of a recurrence solution space.** Count independent initial data for a homogeneous recurrence. The second-order rule $a_{n+2}=3a_{n+1}-2a_n$ has dimension two and basis sequences $1,2^n$, despite infinitely many coordinates.

71. **Connected difference vectors.** Connected edge differences span the sum-zero hyperplane. In $\mathbb R^n$ its dimension is $n-1$, with basis $e_i-e_n$; path telescoping explains why a spanning tree suffices.

72. **A plane, a constrained intersection, and a normal direction.** An equation-defined plane uses free-coordinate basis directions, while its coefficient row supplies a normal in Euclidean coordinates. For $2x-y+4z=0$, use $(1,2,0),(0,4,1)$ and normal $(2,-1,4)$.

73. **Measurement ambiguity and output dimension.** Sensor ambiguity is a kernel, not a count of repeated outputs. The measurements $x_1+x_2,x_2+x_3$ have rank two and invisible direction $(-1,1,-1)$, giving a one-parameter fiber for every output.

74. **Dimension of complementary projection components.** Every idempotent linear map splits its space into image and kernel. The decomposition $v=Pv+(v-Pv)$ proves existence, and $Pw=w$ on the image proves uniqueness; orthogonality is an additional property.

75. **Intersection dimension from ranks of stacked constraints.** For $U=\ker A,W=\ker B\subseteq F^n$, the stacked matrix $C=\begin{bmatrix}A\\B\end{bmatrix}$ defines their intersection. With ranks $r_A,r_B,r_C$, dimensions are $n-r_C$ for the intersection and $n-r_A-r_B+r_C$ for the sum. Taking $n=6,r_A=2,r_B=3,r_C=4$ gives two and five, respectively.

76. **A quotient of polynomial spaces.** Polynomial quotient coordinates can be read from remainders. Modulo multiples of $x^2-1$ in $P_4$, the basis cosets $1,x$ give coordinates $(c_0+c_2+c_4,c_1+c_3)$ and quotient dimension two.

77. **A hard counterexample to distributivity of subspaces.** Subspace sum and intersection are not generally distributive. The inclusion $(U\cap W)+(U\cap Z)\subseteq U\cap(W+Z)$ holds, but three distinct lines in a plane make it strict.

78. **A valid modular identity.** The modular identity requires $U\subseteq Z$. Under that premise, subtracting the $U$ component keeps a vector in $Z$ and proves $U+(W\cap Z)=(U+W)\cap Z$.

79. **Extending a prescribed basis using another supplied basis.** An independent subspace basis can be extended using a supplied spanning union. Two dimension-three spaces with one-dimensional intersection have a five-vector sum basis retaining any prescribed $U$ basis and two suitably chosen $W$ basis vectors.

80. **Independent constraints on a direct sum.** A scalar constraint can cancel across direct-sum components. For component dimensions four and three with nonzero restrictions, the full kernel has dimension six, while the sum of restricted kernels has only dimension five.
