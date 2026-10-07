1. **A minor is not a cofactor.** Delete the indicated row and column before computing a minor, then apply its cofactor sign separately. **Condition and worked check.** For the matrix in Question 1, deleting row two and column three gives minor $-14$ and cofactor $14$; the full determinant is $105$. Keep the deleted submatrix, its determinant, and its signed cofactor as three distinct objects.

2. **A swap ledger in a four-by-four determinant.** A triangular diagonal product belongs to the transformed matrix; correct it for every determinant-changing operation. **Condition and worked check.** For the four-by-four Berkeley matrix, one swap and determinant-preserving replacements give diagonal $(1,1,1,2)$. The original determinant is therefore $-2$, not the endpoint product $2$.

3. **Choosing a sparse expansion.** Choose an expansion by the cost of its surviving minors, not merely by its row number. **Condition and worked check.** For $\begin{bmatrix}2&4&2\\3&2&1\\2&0&1\end{bmatrix}$, expanding column two gives $-4-4=-8$. Expanding row three gives the same value with one zero minor and one zero entry.

4. **Two signs in a permutation term.** Calculate permutation parity and entry-product sign as two independent stages. **Condition and worked check.** For permutation $(3,2,1)$ in Question 4, three inversions give sign $-1$ while its entry product is $-70$. Their product is the positive contribution $70$.

5. **A four-by-four counterexample to Sarrus extension.** A diagonal mnemonic is valid only when it exhausts all required permutation terms. **Condition and worked check.** The four-by-four permutation matrix for $(2,1,3,4)$ has determinant $-1$ but is missed by the eight cyclic diagonal patterns. Sarrus cannot replace all 24 order-four permutations.

6. **Scaling the whole matrix and its inverse.** Count how many rows a scalar changes, and establish invertibility before using negative powers. **Condition and worked check.** For order-five invertible $A$ with $\det A=-3$, the three values are $\det(2A)=-96$, $\det(A^{-2})=1/9$, and $\det(-A^T)=3$. Whole-matrix scaling uses the order as its exponent.

7. **A mixed row-operation ledger.** State whether your ledger expresses the current determinant in terms of the original or the reverse. **Condition and worked check.** When a swap and a row scaling by three lead to a triangular determinant $-48$, the relation is $\det M=-3\det A$. Thus the original value is $16$; a row-addition coefficient contributes no scaling factor.

8. **Simultaneous row changes are not sequential replacements.** Encode simultaneous original-row combinations in a row-mixing matrix before applying operation laws. **Condition and worked check.** Simultaneously replacing three rows by $r_1+r_2,r_1-r_2,2r_3$ multiplies the determinant by $-4$. Use the determinant of the original-row mixing matrix, not sequential-operation intuition.

9. **Affine row replacement.** Row linearity is useful because retained duplicate rows eliminate the unwanted terms. **Condition and worked check.** For distinct retained rows $j,k$, replacing row $i$ by $\alpha r_i+\beta r_j+\gamma r_k$ gives $\alpha\det A$. At $\alpha=0$, the new determinant is zero because the new row is dependent on retained rows.

10. **A diagonal product with a zero first pivot.** Distinguish a zero pivot candidate from an exhausted pivot column. **Condition and worked check.** The matrix $\begin{bmatrix}0&2&1\\3&0&4\\1&5&0\end{bmatrix}$ has determinant $23$. A zero candidate pivot requires a row search; only failure of the complete remaining-column search establishes a missing pivot.

11. **Anti-diagonal matrices.** Reversal signs depend on the number of inverted pairs, not on the visual direction of a diagonal. **Condition and worked check.** For anti-diagonal entries $b_i$ in order $n$, the determinant is $(-1)^{n(n-1)/2}\prod_i b_i$. Entries $(2,3,5,7)$ at order four give $210$, because the reversal has six inversions.

12. **A cycle and a permutation power.** The determinant of a permutation power reveals parity, not its full permutation order. **Condition and worked check.** A six-coordinate permutation with cycle lengths three, two, and one has determinant $-1$ and its 2026th power has determinant $1$. This parity conclusion does not make the power matrix identity.

13. **Whole-matrix additivity fails even for invertible matrices.** Determinants multiply under matrix products but have no general two-term law under matrix addition. **Condition and worked check.** At order two, $I$ and $-I$ both have determinant one but their sum has determinant zero. Determinant additivity fails even when both summands are invertible with positive determinants.

14. **One-entry perturbation and an unchanged determinant.** A zero cofactor makes its own entry an exact determinant-insensitive direction. **Condition and worked check.** For the matrix in Question 14, $C_{31}=0$, so every change to entry $(3,1)$ leaves determinant $-8$ exactly unchanged. The cofactor excludes the changed entry and remains constant during that one-entry perturbation.

15. **Two-entry perturbations have a mixed term.** Simultaneous perturbations can create cross terms even though each individual entry enters affinely. **Condition and worked check.** Changing the two diagonal entries of $\begin{bmatrix}2&1\\3&4\end{bmatrix}$ by $h,k$ gives determinant $5+4h+2k+hk$. The mixed term prevents the multi-entry first-order expression from being exact in general.

16. **An untransposed cofactor matrix.** Form signed cofactors, transpose them, and only then divide by a nonzero determinant. **Condition and worked check.** For $\begin{bmatrix}2&1\\3&4\end{bmatrix}$, the adjugate is $\begin{bmatrix}4&-1\\-3&2\end{bmatrix}$ and the inverse is its one-fifth multiple. The transpose of the cofactor matrix is indispensable.

17. **Wrong-row cofactor sums.** An entry row paired with a different cofactor row gives an equal-row determinant and therefore zero. **Condition and worked check.** For every square matrix, $\sum_j a_{ij}C_{kj}=0$ when $i\ne k$, while it equals $\det A$ when $i=k$. The former sum expands a matrix with two equal rows, so no inverse assumption is needed.

18. **Rank and adjugate rank.** For order at least two, adjugate rank is full, one, or zero according to the original rank threshold. **Condition and worked check.** At order four, original ranks four, three, and at most two give adjugate ranks four, one, and zero respectively. A nonzero maximal minor and the one-dimensional nullspace together prove the middle case.

19. **The one-dimensional adjugate exception.** Verify the matrix order before applying adjugate formulas involving zeroth powers or empty minors. **Condition and worked check.** The adjugate of $[0]$ is $[1]$, whereas the adjugate of $0_{2\times2}$ is zero. The empty determinant convention makes order one an explicit exception to low-rank adjugate shorthand.

20. **A determinant of an adjugate expression.** Keep the matrix dimension exponent separate from the adjugate exponent one less than the dimension. **Condition and worked check.** For order-four $A$ with determinant two, $\det(3\operatorname{adj}A)=648$ and $\det(\operatorname{adj}(A^{-1}))=1/8$. Scaling has exponent four; the adjugate determinant law has exponent three.

21. **Cramer's rule with signed numerators.** Use signed column-replacement determinants, then substitute the resulting coordinates into the original system. **Condition and worked check.** For $A=\begin{bmatrix}2&1\\3&4\end{bmatrix}$ and $b=(5,6)^T$, column-replacement numerators are $14,-3$ and denominator is $5$. The signed solution is $(14/5,-3/5)^T$, which satisfies both original equations.

22. **Zero replacement determinants do not always imply consistency.** At a zero denominator, classify the augmented system rather than infer a solution from zero replacement determinants. **Condition and worked check.** For $A=0_{3\times3}$ and $b=(1,0,0)^T$, every replacement determinant is zero but the system is inconsistent. At a singular coefficient matrix, inspect augmented rank instead of forming undefined Cramer ratios.

23. **A parameter family with two different singular ranks.** Factor a parameter determinant to find singular values, then inspect the original map to determine rank at each value. **Condition and worked check.** For diagonal $x$ and off-diagonal one in order $n\ge3$, the determinant is $(x-1)^{n-1}(x+n-1)$. Rank is one at $x=1$ and $n-1$ at $x=1-n$.

24. **Elimination that divides away an exceptional case.** An exceptional denominator value requires substitution into the original matrix even if the final determinant polynomial extends to it. **Condition and worked check.** For $\begin{bmatrix}t&1\\t^2&t\end{bmatrix}$, determinant is always zero and rank is always one, including $t=0$. A derivation dividing by $t$ must separately inspect the original zero-parameter matrix.

25. **A rank-one perturbation of identity.** Reduce an identity rank-one determinant to one scalar inner product, retaining its sign. **Condition and worked check.** With $u=(1,2,-1)^T$ and $v=(2,-1,3)^T$, $\det(I+tuv^T)=1-3t$. The unique singular parameter is $1/3$, where the nonzero vector $u$ lies in the kernel.

26. **Rank-one updates of a singular matrix.** Use the adjugate update identity when the original matrix is singular. **Condition and worked check.** For $A=\operatorname{diag}(1,2,0)$ and update $12e_3e_3^T$, the new determinant is $24$. The inversion-free formula $\det(A+uv^T)=\det A+v^T\operatorname{adj}(A)u$ covers this singular starting matrix.

27. **How many updates can repair low rank?.** A rank-one update changes rank by at most one; it cannot repair two missing independent directions. **Condition and worked check.** A rank-one update of an order-five matrix of rank at most three still has rank at most four. Its determinant remains zero regardless of the update's numeric magnitude.

28. **A bordered matrix with a valid Schur complement.** A Schur determinant reduces dimension only after the chosen square pivot block is verified invertible. **Condition and worked check.** The bordered matrix in Question 28 has pivot-block determinant $6$ and Schur scalar $2/3$, giving determinant $4$. Verify the pivot block's invertibility and keep the order $EB^{-1}C$.

29. **An invertible matrix with a singular pivot block.** A singular diagonal block does not establish singularity of the complete block matrix. **Condition and worked check.** The block exchange $\begin{bmatrix}0&I_2\\I_2&0\end{bmatrix}$ has determinant one although its upper-left block is singular. An unavailable Schur pivot says nothing by itself about full-matrix invertibility.

30. **Block product order matters.** For matrix blocks, preserve the exact Schur order; a scalar-looking formula needs additional commutation assumptions. **Condition and worked check.** In the noncommuting block example of Question 30, the actual determinant is three while $\det(BD-EC)$ is two. A scalar-looking block formula is not valid without its necessary commutation assumptions.

31. **Vandermonde sign and reordered nodes.** A Vandermonde determinant is sensitive to node order; use signed differences in that order. **Condition and worked check.** Increasing-power Vandermonde nodes $(1,3,2)$ give $(3-1)(2-1)(2-3)=-2$. Swapping first and third rows changes this to two; sorting nodes without a sign ledger loses information.

32. **Interpolation loses uniqueness at repeated nodes.** Repeated interpolation nodes require consistency checks or independent derivative constraints, not an ordinary inverse. **Condition and worked check.** Repeated nodes $(0,1,1)$ give rank two: values $(2,5,5)$ admit infinitely many quadratic polynomials, but $(2,5,7)$ are inconsistent. Repeated ordinary values are not derivative conditions.

33. **A tridiagonal determinant with zero intermediate pivots.** Determinant recurrences remain valid through zero intermediate values when derived without division. **Condition and worked check.** For the all-one tridiagonal matrix, $D_0=D_1=1$ and $D_n=D_{n-1}-D_{n-2}$. The six-period sequence gives $D_{2026}=-1$ without dividing by any intermediate zero.

34. **A discrete Laplacian determinant.** Initialize both $D_0$ and $D_1$, and use the product of the two off-diagonal entries in a continuant recurrence. **Condition and worked check.** For diagonal two and adjacent diagonals minus one, $D_0=1,D_1=2$ and the recurrence gives $D_n=n+1$. In particular $D_{50}=51$; boundary conditions determine the correct closed form.

35. **A nonconstant tridiagonal recurrence.** In a variable-band recurrence, match each off-diagonal product to the edge just appended. **Condition and worked check.** For diagonal $(2,3,4,5)$ and adjacent products $(4,2,6)$, successive determinants are $2,2,4,8$. Match each recurrence's off-diagonal product to the newly appended edge.

36. **Signed area and unsigned triangle area.** Keep determinant sign for orientation, but use its absolute value for geometric area. **Condition and worked check.** Columns $(2,1)^T,(-1,3)^T$ give signed parallelogram area seven and triangle area $7/2$. Reversing their order negates orientation but preserves both physical areas.

37. **A triangle translated away from the origin.** Convert vertices into edge differences or use homogeneous-coordinate triangle determinants. **Condition and worked check.** Triangle vertices $(1,2),(4,3),(2,6)$ produce edge determinant eleven and area $11/2$. Subtract one base vertex before using a two-by-two area determinant.

38. **Gram volume for a rectangular matrix.** For rectangular columns, compute volume through the square Gram matrix and take a square root. **Condition and worked check.** For columns $(1,0,1)^T,(0,2,1)^T$, the Gram determinant is nine and embedded area is three. The original three-by-two matrix has no ordinary determinant.

39. **Cauchy–Binet with cancellation.** Match the same ordered intermediate index subset in both rectangular factors. **Condition and worked check.** For the rectangular factors in Question 39, matched maximal-minor products are $-1,6,6$, summing to eleven. Cauchy–Binet uses signed products; only the Gram specialization turns them into squares.

40. **The impossible tall product inverse.** Compare the product's output dimension with the intermediate dimension before attempting determinant arithmetic. **Condition and worked check.** A five-by-three factor followed by a three-by-five factor gives a singular five-by-five product. Its three-by-three reverse product can nevertheless be identity, because the output dimensions differ.

41. **Determinant one does not preserve lengths.** Volume preservation does not imply preservation of lengths or angles. **Condition and worked check.** The shear $\begin{bmatrix}1&3\\0&1\end{bmatrix}$ preserves area but sends a unit vector to length $\sqrt{10}$. Determinant one does not imply orthogonality or preservation of angles.

42. **A reflection from its normal vector.** A reflection flips one normal direction, preserving the perpendicular subspace and giving determinant minus one. **Condition and worked check.** For unit normal $(3/5,4/5)^T$, $I-2uu^T$ has determinant minus one, negates the normal, and preserves its perpendicular line. Normalization is required for the reflection formula.

43. **An odd skew-symmetric matrix.** Odd-dimensional skew-symmetry forces zero determinant; even-dimensional skew-symmetry does not. **Condition and worked check.** Odd-order real skew-symmetry forces zero determinant through $\det K=(-1)^n\det K$. Even-order skew-symmetry allows invertible examples; the proof also requires characteristic other than two.

44. **A proper projection and an involution.** Projection determinants detect missing directions, whereas involution determinants detect the parity of minus directions. **Condition and worked check.** A proper order-five projection of rank three has determinant zero. An order-five real involution with a two-dimensional minus subspace has determinant one, reflecting sign parity rather than lost rank.

45. **Positive determinant without positive definiteness.** For symmetric positivity, inspect directional signs or the complete relevant minor criterion, not only the determinant. **Condition and worked check.** The symmetric matrix $\operatorname{diag}(1,1,-1,-1)$ has determinant one but an indefinite quadratic form. An even number of negative directional factors can conceal failure of positivity in their product.

46. **A strict two-by-two positivity interval.** Strict and nonstrict positivity have different boundary cases; determine them from the original quadratic form. **Condition and worked check.** For $\begin{bmatrix}2&t\\t&3\end{bmatrix}$, strict positivity requires $|t|<\sqrt6$; equality gives rank-one positive semidefiniteness, and larger magnitude gives indefiniteness. Check the strict boundary separately.

47. **Determinant from a characteristic polynomial.** Read determinant and trace from coefficients only after fixing the characteristic-polynomial sign convention. **Condition and worked check.** With convention $p_A(t)=\det(tI-A)$, constant coefficient is $(-1)^n\det A$ and next-to-leading coefficient is $-\operatorname{tr}A$. The order-four polynomial in Question 47 gives determinant $-5$ and trace three.

48. **A defective matrix still has an eigenvalue product.** Multiply eigenvalues with algebraic multiplicity; diagonalizability is irrelevant to that determinant identity. **Condition and worked check.** A size-three Jordan block with diagonal two has determinant eight despite being defective. The eigenvalue product counts algebraic multiplicity and does not require an eigenbasis.

49. **A polynomial-space shift map.** For polynomial endomorphisms, degree behavior often reveals triangular structure before any full matrix is written. **Condition and worked check.** On polynomials of degree at most four, translation by three has triangular diagonal ones and determinant one; differentiation has determinant zero. Degree behavior can establish the result without writing every coefficient.

50. **Changing both bases independently.** Basis-independent endomorphism determinants use the same basis change in domain and codomain. **Condition and worked check.** Independent domain and codomain basis changes give matrix $Q^{-1}AP$ and determinant $\det A\det P/\det Q$. Only a common basis change automatically produces similarity and determinant invariance.

51. **A matrix derivative at a singular point.** At singular points, use the adjugate derivative identity rather than an undefined inverse. **Condition and worked check.** For $\begin{bmatrix}t&1\\0&t\end{bmatrix}$, the determinant derivative is $2t$, including zero at the singular point. The adjugate derivative formula works there; the inverse formula does not.

52. **A trace derivative for a structured family.** Log-determinant differentiation requires a nonzero determinant on the interval under discussion. **Condition and worked check.** For $I+tuv^T$, with $s=v^Tu$, the log-absolute-determinant derivative is $s/(1+ts)$ wherever $1+ts\ne0$. If $s=0$, the determinant stays one and the derivative is zero.

53. **A determinant lemma from rectangular blocks.** A two-way block elimination can prove identities without inverting the rectangular factors or final matrices. **Condition and worked check.** For rectangular $U,V$ of compatible sizes, $\det(I_m+UV)=\det(I_n+VU)$. Two Schur eliminations of the same identity-pivot block matrix prove this without inverting either rectangular factor.

54. **A low-dimensional determinant update.** Low-rank update identities can reduce determinant dimension, but the identity matrices must have the correct orders. **Condition and worked check.** The rectangular update in Question 54 reduces to $\det\begin{bmatrix}2&2\\3&5\end{bmatrix}=4$. Add the identity with the correct product order before using the lower-dimensional determinant.

55. **Equal row sums guarantee one factor, not a full formula.** A constant row sum supplies one known eigenvalue or factor; inspect the complementary subspace for the rest. **Condition and worked check.** Equal row sums $t-2$ guarantee singularity at two and, for polynomial entries, a factor $t-2$. They do not force all four determinant factors to equal that row sum.

56. **A repeated determinant root with small nullity.** Determine singular-parameter nullity from the matrix itself, not solely from determinant-root multiplicity. **Condition and worked check.** Both $\begin{bmatrix}t&1\\0&t\end{bmatrix}$ and $tI_2$ have determinant $t^2$, but their zero-parameter nullities are one and two. Root multiplicity does not determine singular-matrix nullity.

57. **A commutator has no determinant cancellation rule.** Equal product determinants do not license subtracting determinants through a matrix difference. **Condition and worked check.** The commutator in Question 57 is $\begin{bmatrix}0&1\\-1&0\end{bmatrix}$ of determinant one. Equal determinants of $AB$ and $BA$ cannot be subtracted through determinant nonadditivity.

58. **Determinant constraints from a similarity relation.** Combine similarity invariance with dimension-dependent scaling signs before attempting explicit basis changes. **Condition and worked check.** A real odd-order matrix similar to its negative is singular by dimension-dependent scaling and similarity invariance. At even order that determinant argument imposes no singularity condition.

59. **A product with transpose does not lose the determinant sign twice.** Distinguish negating both factors of a Gram product from negating the resulting matrix once. **Condition and worked check.** If order-three $A$ has determinant $-2$, then $\det(A^TA)=4$ and $\det(-A^TA)=-4$. Negating the final product differs from negating both of its factors.

60. **A complex Gram product needs conjugation.** Complex volume and length formulas use conjugate transpose, not merely transpose. **Condition and worked check.** For the complex column $(1,i)^T$, the transpose self-product is zero but the conjugate-transpose self-product is two. Complex Gram volume must use conjugation and squared absolute minors.

61. **The determinant of a diagonal-plus-constant matrix.** Expand an inverse-based rank-one formula into polynomial form before extending it to zero diagonal entries. **Condition and worked check.** For diagonal $D$, the polynomial update formula is $\prod_i d_i+\alpha\sum_i\prod_{j\ne i}d_j$. This remains valid when some entries vanish, unlike the version containing reciprocal diagonal entries.

62. **Two zero diagonal entries defeat one constant update.** In diagonal-plus-rank-one formulas, two missing diagonal directions already force the determinant to remain zero. **Condition and worked check.** For $D=\operatorname{diag}(0,0,3,4)$, every determinant term in $D+\alpha J$ still contains a zero diagonal factor. The determinant is identically zero because one update cannot repair two missing directions.

63. **One zero diagonal direction can be repaired.** One missing diagonal factor can contribute through its complementary maximal minor in a rank-one update. **Condition and worked check.** For $D=\operatorname{diag}(0,2,3,4)$, adding $5J$ gives determinant $5\cdot2\cdot3\cdot4=120$. One complementary maximal minor repairs the single missing direction.

64. **A homogeneous polynomial determinant has degree bounds.** A low-rank parameter coefficient bounds determinant polynomial degree through multilinear dependence. **Condition and worked check.** For $A_0+tA_1$ with $\operatorname{rank}A_1\le2$, the determinant polynomial has degree at most two. Every term selecting more than two parameter columns vanishes by dependence, even if $A_0$ is singular.

65. **A homogeneous scaling derivative.** A determinant is homogeneous of degree equal to its matrix order, including at singular matrices. **Condition and worked check.** For order $n$, $\sum_{i,j}a_{ij}C_{ij}=n\det A$. This is both the derivative of $\det(tA)$ at one and the sum of all $n$ row expansions.

66. **Recovering a cofactor from an inverse entry.** Inverse-entry and cofactor indices reverse because the adjugate is transposed. **Condition and worked check.** If $\det A=6$ and $(A^{-1})_{23}=-2$, then $C_{32}=-12$. The unsupplied cofactor $C_{23}$ cannot be inferred without further symmetry information.

67. **A nonzero cofactor at a singular matrix.** A nonzero maximal minor permits first-order departure from singularity even when the determinant itself is zero. **Condition and worked check.** The family $\begin{bmatrix}1&2\\2&t\end{bmatrix}$ is rank-one singular at four, with determinant derivative one. A nonzero cofactor allows a first-order departure from singularity.

68. **A determinant of products and adjugates.** Multiply scalar determinants without simplifying matrix factors through invalid commutation or transpose assumptions. **Condition and worked check.** For order-three factors with determinants two and minus three, $\det(A^{-1}\operatorname{adj}B\,A^T)=9$. Scalar determinant factors cancel even though the corresponding matrices do not.

69. **A diagonal polynomial of a triangular matrix.** A polynomial in a triangular matrix is triangular with that polynomial evaluated on each diagonal entry. **Condition and worked check.** A polynomial of an upper triangular matrix is upper triangular with that polynomial on its diagonal. For diagonal $(1,2,-1,0)$, $A^2+3A+2I$ is singular because the minus-one diagonal yields zero.

70. **A Schur complement at a parameter boundary.** A polynomial extension can validate a determinant at a singular pivot-block parameter while the inverse-based derivation remains restricted. **Condition and worked check.** The bordered family in Question 70 has determinant $6t-2$ for every real $t$. At zero its chosen Schur pivot fails, yet its full determinant is $-2$ and it remains invertible.

71. **Counting terms versus counting operations.** State whether a complexity claim counts arithmetic operations or operations on growing exact-number representations. **Condition and worked check.** Permutation and naive recursive cofactor methods have factorial growth, whereas dense elimination uses cubic arithmetic-operation count. Growing exact-number bit lengths require a separate complexity analysis.

72. **Exact singularity versus a small determinant.** Small determinant magnitude and exact singularity are different claims, especially after rescaling. **Condition and worked check.** The invertible matrix $\operatorname{diag}(10^{-8},10^{-8})$ has determinant $10^{-16}$. A fixed small-determinant threshold cannot universally distinguish scale from exact singularity.

73. **LU with a permutation factor.** Derive a factorization's determinant correction from its stated equation and triangular normalization. **Condition and worked check.** With $PA=LU$, one permutation swap, unit lower triangular $L$, and upper diagonal $(2,3,-4,5)$, the determinant is $120$. Read the factorization equation before choosing a correction sign.

74. **A nonsingular matrix with a zero leading minor.** Leading-principal-minor conditions depend on the property being tested; ordinary invertibility needs only a nonzero full determinant. **Condition and worked check.** The invertible matrix $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ has first leading minor zero and full determinant minus one. Positive-definiteness minor criteria are not general invertibility criteria.

75. **Matching an authentic positivity matrix through subspaces.** For a symmetric constant-off-diagonal matrix, inspect both invariant factors; a squared determinant factor can conceal negative directions. **Condition and worked check.** Diagonal one and off-diagonal $a$ in order three give factors $1+2a$ on the constant line and $1-a$ on the sum-zero plane. Strict positivity is exactly $-1/2<a<1$, excluding both collapses.

76. **A determinant can vanish after adding identity.** Identity updates of triangular matrices use one factor per diagonal entry, not an additive determinant shortcut. **Condition and worked check.** For triangular diagonal $(2,-1,3)$, $\det(I+tA)=(1+2t)(1-t)(1+3t)=1+4t+t^2-6t^3$. Its three singular parameters cannot be recovered by the false shortcut $1+t\det A$.

77. **A matrix whose determinant is invariant under every row shear.** Prove an operation law without division when you need it to cover singular inputs as well. **Condition and worked check.** Every finite sequence of row replacements preserves determinant without any invertibility assumption. Starting from a nonsingular matrix, these invertible shears cannot create a singular intermediate matrix.

78. **A finite-field parity caveat.** Check the field's characteristic before using parity signs or division by two in a proof. **Condition and worked check.** In characteristic two, minus one equals one and $D=-D$ does not imply $D=0$. Alternation still makes equal-row determinants vanish, but dividing by two is not a valid proof.

79. **Hadamard's volume bound with equality conditions.** Volume is bounded by the product of edge lengths, with nondegenerate equality exactly for mutually orthogonal edges. **Condition and worked check.** Hadamard's bound is $|\det[u_1\cdots u_n]|\le\prod_i\|u_i\|$. For nonzero independent columns equality requires mutual orthogonality; a zero column gives trivial equality and must be treated separately.

80. **A mixed examination workflow.** In mixed problems, derive the determinant first and then apply each downstream theorem with its own dimension and singular-case conditions. **Condition and worked check.** For diagonal $t$ and off-diagonal one at order three, determinant is $(t-1)^2(t+2)$ and adjugate determinant is $(t-1)^4(t+2)^2$. Singular ranks are one at $t=1$ and two at $t=-2$; consistency still depends on the right-hand side.
