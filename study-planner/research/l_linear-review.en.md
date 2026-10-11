### Linearity and specification

1. State the field before testing linearity. Complex conjugation preserves real combinations but fails complex homogeneity.

2. A linear map must send zero to zero. Passing that necessary check does not prove linearity; a square or absolute-value component can still fail.

3. Prove linearity for arbitrary inputs and scalars. Several successful numerical examples cannot establish the universal identity.

4. Disprove linearity with one valid counterexample. State both sides of the failed identity and verify that the chosen inputs lie in the domain.

5. An affine map $Ax+b$ is linear precisely when $b=0$. Its preservation of weighted combinations with coefficient sum one is a different property.

6. Use the vector operations of the actual space. Componentwise addition of polar coordinates does not implement physical vector addition.

7. Radial multiplication by a fixed scalar is linear. A formula described using distances or angles can still be a matrix map after conversion to Cartesian coordinates.

8. Images of a domain basis can be chosen arbitrarily. Output dependence creates a kernel but does not prevent a well-defined extension.

9. Basis coefficients are unique, which proves that the extension definition is unambiguous. A spanning list without independence does not have this uniqueness.

10. A linear map agreeing with another on a spanning set agrees everywhere. The spanning set need not be independent for this uniqueness implication.

11. Prescriptions on a dependent input list must preserve every input relation. Test $\ker X\subseteq\ker Y$ for input and output column matrices.

12. If a dependent prescription violates one relation, no linear extension exists. Extra codomain dimensions cannot repair a specified contradictory relation.

13. If prescribed inputs have rank $r$ in an $n$-dimensional domain, there are $n-r$ unused basis directions. Each carries an arbitrary output vector.

14. A nonempty extension set into an $m$-dimensional codomain has affine dimension $m(n-r)$. It is a vector space only when the prescribed outputs permit zero as an extension.

15. Over a field of $q$ elements, that affine extension set has $q^{m(n-r)}$ maps. Counting formulas require finite field size as well as consistency.

16. $\operatorname{Hom}(F^n,F^m)$ has dimension $mn$. Matrix units and freely chosen basis images describe the same scalar freedoms.

### Kernel, image, and dimension

17. The kernel is a subspace of the domain and the image is a subspace of the codomain. Keeping their ambient spaces separate prevents a dimension-type mistake.

18. A fiber outside the image is empty. A nonempty fiber is $x_0+\ker T$, not generally the kernel itself.

19. The fiber of a nonzero attainable output is never a vector subspace, because it cannot contain the zero input. Describe it as a translate of the kernel.

20. Every nonempty fiber has the same direction space and dimension. The position depends on the selected output and particular preimage.

21. Injectivity is equivalent to a zero kernel. Apply linearity to $T(u)=T(v)$ to reduce it to $u-v\in\ker T$.

22. Surjectivity is equivalent to image equal to the codomain. It concerns attainable outputs, not the uniqueness of inputs.

23. Rank–nullity uses the dimension of the domain. Subtracting rank from codomain dimension gives a cokernel count, not nullity.

24. The rank–nullity proof extends a kernel basis. Images of the added basis vectors are independent and span the image.

25. A map from dimension $n$ to dimension $m$ can be injective only if $n\le m$. This inequality is necessary and does not force a particular map to be injective.

26. Such a map can be onto only if $m\le n$. Equal dimensions make injectivity and surjectivity equivalent only in finite dimensions.

27. An adapted input/output basis puts a rank-$r$ map into rectangular identity/zero form. This generally requires independent changes at the two ends.

28. Standard-coordinate kernel directions need not align with coordinate axes. Do not draw a rank collapse as deleting specific original coordinates without justification.

### Coordinates, composition, and inverses

29. An ordered basis gives a coefficient isomorphism. The physical vector and its coefficient column are different typed objects, even when both are written as tuples.

30. A representation matrix maps input-basis coefficients to output-basis coefficients. Write $[T(v)]_C=A_{C\leftarrow B}[v]_B$ before computing.

31. Column $j$ contains $[T(b_j)]_C$. Rows contain output-component functionals; they are not the basis images themselves.

32. With physical standard matrix $A$ and synthesis matrices $P,Q$, the representation is $Q^{-1}AP$. Read the operations from right to left.

33. $AP$ retains standard output coordinates. $Q^{-1}A$ retains standard input coordinates; neither is the two-basis representation by itself.

34. A basis matrix is square invertible. A rectangular or dependent generator matrix cannot be inverted as a coordinate isomorphism.

35. $P_{B\leftarrow D}$ converts $D$-coefficients to $B$-coefficients. Its columns are $D$ basis vectors expressed in $B$.

36. The inverse transition reverses direction. A phrase such as “from the old basis to the new basis” is ambiguous until its coordinate equation is stated.

37. Coordinate transitions compose with matching middle labels. Derive $P_{B\leftarrow E}=P_{B\leftarrow D}P_{D\leftarrow E}$ by substitution.

38. For a transition computed from standard synthesis matrices, solve $B_0P=D_0$. Reducing $[B_0\mid D_0]$ computes all columns together.

39. Passive coordinate conversion keeps the physical vector fixed. Active transformation changes the physical vector under a fixed coordinate system.

40. A composite $ST$ applies $T$ first. The representation order is $[S][T]$ when intermediate bases agree.

41. If the intermediate bases differ, insert their directional transition between the two matrices. Numeric dimension compatibility cannot detect this omission.

42. Associativity allows regrouping but never reverses factors. A two-vector shear example can expose a mistaken order immediately.

43. A bijective linear map has a linear inverse. Its inverse representation reverses both physical direction and input/output basis labels.

44. A left inverse implies injectivity. A right inverse implies surjectivity; they are different claims for rectangular maps.

45. In finite dimensions an injection admits a left inverse by extending an image basis. A surjection admits a right inverse by choosing basis-vector preimages.

46. A real full-column-rank matrix has Gram left inverse $(A^TA)^{-1}A^T$. Over complex scalars use conjugate transpose.

47. A real full-row-rank matrix has Gram right inverse $A^T(AA^T)^{-1}$. Over a general field the Gram construction may fail, so use basis arguments.

48. A one-sided inverse becomes two-sided for square finite-dimensional maps. Infinite-dimensional shifts provide a counterexample to dropping the finiteness condition.

### Equivalence, similarity, and geometry

49. Independent changes at the two ends give $Q^{-1}AP$ and preserve rank. They do not generally preserve trace, determinant, or eigenvalues.

50. The same basis change for an endomorphism gives $P^{-1}AP$. This is similarity and preserves operator structure.

51. Similarity preserves determinant by multiplicative cancellation. Verify the determinant of the basis matrix is nonzero before invoking it.

52. Similarity preserves trace by cyclicity. Equal trace and determinant alone are not a general similarity test.

53. Similarity preserves characteristic polynomial. A zero matrix and a nonzero nilpotent matrix can share that polynomial and still have different ranks.

54. Polynomial identities and ranks of powers survive similarity. Repeated cancellation gives $f(P^{-1}AP)=P^{-1}f(A)P$.

55. Powers require a common input/output basis. A mixed-basis endomorphism representation needs a coordinate bridge before another application.

56. A rotation matrix is derived from the rotated coordinate units. To animate rotation, vary the angle rather than interpolate arbitrary matrix entries.

57. Interpolating identity and a half-turn linearly collapses the plane at the midpoint. That family is not a sequence of rotations.

58. A reflection squares to identity and reverses orientation. An invertible continuous real path from identity to a reflection cannot avoid a zero determinant.

59. A shear can preserve area without preserving angles or lengths. Determinant one is not an orthogonality condition.

60. A projection is characterized by $P^2=P$. Symmetry is an additional requirement for Euclidean orthogonal projection.

61. Every projection splits the domain into image and kernel. The retained and discarded directions need not be perpendicular.

62. $I-P$ is the complementary projection. Its image is $\ker P$ and its kernel is $\operatorname{im}P$.

63. Commuting projections have an idempotent product. Without commutation their product can fail the projection identity.

64. Over the reals an idempotent has trace equal to rank. In positive characteristic the trace scalar records that integer only modulo the characteristic.

### Function and matrix-space operators

65. Differentiation is linear once its polynomial spaces are stated. $P_n\to P_{n-1}$ has different input and output dimensions.

66. In characteristic zero the derivative kernel on $P_n$ is the constants. Positive characteristic can create additional zero derivatives such as $x^p$.

67. Evaluation at fixed nodes is a linear measurement. Distinct nodes and a degree bound determine when enough measurements give uniqueness.

68. Repeated evaluation at the same node is redundant. Derivative measurements at that node are different information and must be explicitly specified.

69. Lagrange polynomials form an evaluation-adapted basis. In that basis the full distinct-node evaluation matrix is identity.

70. Invertible basis conversion loses no information. Discarding coefficients is a separate approximation step.

71. A fixed zero/one coefficient mask reconstructs a projection. An input-dependent threshold generally makes the overall rule nonlinear.

72. Fixed left/right matrix multiplication is linear in the variable matrix. Jointly varying both factors gives a bilinear operation rather than a joint linear map.

73. The rank of $X\mapsto AX$ is $n\operatorname{rank}A$ when $X$ has $n$ columns. Count independent column copies.

74. The rank of $X\mapsto AXB$ is $\operatorname{rank}A\,\operatorname{rank}B$. Use rank-form coordinate changes to justify the entry count.

75. Transpose is linear on matrix space and permutes matrix units. It is not automatically the coordinate-free adjoint of an unrelated operator.

76. Trace is a linear functional and remains nonzero in every field. The trace of identity can vanish in positive characteristic without making the whole functional zero.

77. Determinant is not a linear functional in dimension at least two. Two singular diagonal summands whose sum is identity provide a clean counterexample in dimension two.

78. For diagonal Sylvester factors, each matrix unit has multiplier $a_i-b_j$. Zero multipliers create both output consistency conditions and free input entries.

79. The commutant contains all polynomials in the fixed matrix. Equality fails for a scalar matrix, where every matrix commutes.

80. Composite rank equals $\operatorname{rank}T-\dim(\operatorname{im}T\cap\ker S)$. The intersection is taken in the intermediate space.

81. The Sylvester product lower bound subtracts intermediate dimension. Factor ranks alone may leave several possible product ranks.

82. Kernel intersections are contained in the kernel of a sum, but cancellation prevents equality in general. Likewise images of sums need not equal sums of images.

83. A dual map acts on functionals in the reverse direction and has transpose matrix in dual bases. A vector-space adjoint instead uses Gram corrections outside orthonormal bases.

84. Finite-dimensional hypotheses are essential to bijection implications and inverse theorems. State the sequence or function domain before using an infinite-dimensional counterexample.
