# Summary: rank counts independent restrictions and attainable directions

A matrix with $m$ rows, $n$ columns and $r$ pivots has an image of dimension $r$, a row space of dimension $r$, a kernel of dimension $n-r$ and a left kernel of dimension $m-r$. A compatible load has a complete affine family of solutions with direction space equal to the kernel. Full column rank gives uniqueness on the image; full row rank gives existence for every load; both coincide with invertibility only for square matrices.

1. State the field before reducing a matrix. A coefficient that is nonzero over the reals may vanish in positive characteristic, changing both rank and nullity.

2. Record the input and output dimensions before applying rank–nullity. For an $m\times n$ matrix, input vectors have $n$ entries and outputs have $m$ entries.

3. Define rank as image dimension or independent pivot count. Nonzero entries and nonzero original rows are not independent restrictions.

4. A rank-zero matrix is the zero matrix. Its image and row space have empty bases, while its kernel and left kernel are full coordinate spaces.

5. The zero vector cannot occur in an independent basis list. The zero space nevertheless has dimension zero because its correct basis is the empty list.

6. A column-space basis contains $m$-entry vectors. A row-space basis and kernel basis contain $n$-entry vectors; mixing these shapes is an immediate error.

7. Row reduction preserves the kernel exactly because the left transformation is invertible. Every old zero-output input remains a zero-output input and conversely.

8. Row reduction preserves the row space exactly. Both the forward operations and their inverses express new rows in terms of old rows.

9. Row reduction generally moves the column space by an invertible output-coordinate map. Its dimension is preserved even when its position changes.

10. Find pivot indices in the reduced matrix, then select those columns from the original matrix for an original column-space basis.

11. The nonzero rows of an echelon matrix form a row-space basis. Their leading positions prove independence and their row equivalence proves spanning.

12. A zero early column can be free even when later columns contain pivots. Free coordinates are not necessarily the last consecutive coordinates.

13. A kernel basis obtained from free variables must have one independent free-coordinate pattern per direction. Verify annihilation, independence and spanning.

14. The number of kernel basis vectors equals $n-r$. This counts independent parameters, not the number of visible zero rows.

15. The number of left-kernel basis vectors equals $m-r$. Reduce the transpose or track exact row combinations to find them.

16. Row rank equals column rank over every field. The proof uses invertible reduction and standard pivot columns, not Euclidean geometry.

17. Rank is unchanged by transposition. Kernel dimensions of a rectangular matrix and its transpose can nevertheless differ.

18. Rank never exceeds the smaller matrix dimension. Any proposed dimension data must satisfy this bound before computation proceeds.

19. Full column rank means all columns are independent. It requires at least as many output coordinates as input coordinates.

20. Full row rank means all rows are independent and every output is attainable. It requires at least as many input coordinates as output coordinates.

21. A diagonal matrix's rank is its nonzero diagonal count. A general triangular matrix with zero diagonal entries can still have off-diagonal pivots.

22. Independent vectors cannot outnumber the dimension of their ambient space. A spanning list cannot contain fewer vectors than that dimension.

23. A finite independent list can be extended to a basis. A finite spanning list can be shortened to a basis by removing dependencies.

24. A singleton nonzero vector spans a one-dimensional space. Two nonzero proportional vectors still span only one dimension.

25. A homogeneous system always has the zero solution. Positive nullity describes additional directions, not inconsistency.

26. A nonhomogeneous system is compatible exactly when its load lies in the column space. Equation count alone cannot determine compatibility.

27. Appending one load column increases rank by zero or one. An increase of one proves incompatibility for that load.

28. Appending several load columns may increase rank by more than one. Equality of augmented and coefficient ranks is required for every load column to be compatible.

29. One particular solution plus every kernel direction gives all solutions. Conversely subtracting any two solutions gives a kernel vector.

30. A nonempty fiber has affine dimension $n-r$. It is a linear subspace only when the load is zero.

31. Fibers for different outputs are disjoint. Their common kernel direction space can make them parallel affine sets.

32. Uniqueness for one compatible load implies a zero kernel. It then implies uniqueness for every compatible load, but does not establish surjectivity.

33. Existence for one load says little about other loads. Existence for every load is the full-row-rank assertion.

34. Over an infinite field, positive nullity gives infinitely many compatible solutions. Over a field of $q$ elements, the count is exactly $q^{n-r}$.

35. A real load is compatible exactly when it is orthogonal to every left-kernel vector. Testing a left-kernel basis is sufficient.

36. A nonzero left-kernel load pairing is an inconsistency certificate. It refutes every possible input without guessing an input.

37. For real matrices, the row space and kernel are orthogonal complements. The column space and left kernel are orthogonal complements in the output space.

38. For complex Euclidean geometry, use conjugate transpose. Plain transpose can produce a zero Gram product from a nonzero matrix.

39. Gram rank equality over the reals follows from positivity of the squared norm. Do not apply that proof over an arbitrary field.

40. Injectivity is equivalent to a zero kernel and full column rank. It means distinguishable inputs, rather than coverage of every output.

41. Surjectivity is equivalent to full row rank. It means coverage of every output, rather than uniqueness of the producing input.

42. A left inverse exists exactly for an injective finite-dimensional matrix map. Its product with the matrix is an identity on the input coordinates.

43. A right inverse exists exactly for a surjective matrix map. Its product in the opposite order is an identity on the output coordinates.

44. A tall full-column-rank real matrix has left inverse $(A^TA)^{-1}A^T$. This construction is legal because its Gram matrix is positive definite.

45. A wide full-row-rank real matrix has right inverse $A^T(AA^T)^{-1}$. This gives one choice among an affine family of preimages.

46. Correcting a left inverse requires correction rows in the left kernel. Correcting a right inverse requires correction columns in the kernel.

47. One-sided inverses are generally nonunique for genuinely rectangular maps. Their affine family dimensions follow by counting independent correction coordinates.

48. Square finite-dimensional injectivity and surjectivity are equivalent. This equivalence, rather than matrix shape alone, makes a one-sided inverse two-sided.

49. Infinite-dimensional shifts demonstrate that the square finite-dimensional theorem has genuine hypotheses. An onto map there can have a nonzero kernel.

50. A positive lower norm bound forces injectivity. For a square map it also bounds the inverse norm, but it does not imply positive definiteness.

51. A rank factorization uses original independent columns and their coordinate rows. Multiplication should reproduce every original column.

52. Rank is the smallest possible exact factorization bottleneck dimension. A product through fewer than r coordinates cannot have rank r.

53. Different full-rank factorizations differ by an invertible internal basis change. This changes intermediate coordinates while preserving the product.

54. Invertible factors on either side preserve rank. They need not preserve the literal image or kernel subspace in the original coordinates.

55. Independent domain and codomain basis changes can produce an identity-and-zero rank form. This matrix equivalence is not the same as similarity.

56. Composition rank equals the first attained image dimension minus the directions killed by the next map. Identify the actual intermediate intersection.

57. The rank of a product cannot exceed either factor's rank. A small intermediate dimension is an additional bottleneck.

58. Sylvester's lower bound uses the shared intermediate dimension n: $\operatorname{rank}(AB)\ge\operatorname{rank}A+\operatorname{rank}B-n$.

59. Combine a negative Sylvester expression with the independent lower bound zero. Equality with zero and equality with the formal expression need different interpretations.

60. If $AB=0$, the image of B lies in the kernel of A. A compatible dimension inequality alone does not prove that containment.

61. Product rank equals the rank of B exactly when A is injective on the image of B. This is a restriction, not necessarily global injectivity.

62. Sum rank has an upper bound by the sum of ranks and a lower bound by their absolute difference. Complete cancellation can attain zero.

63. Disjoint images alone do not force additive rank of a sum. Shared input coordinates can still restrict the number of independently controllable directions.

64. Concatenation images are sums of images. Vertical-stack kernels are intersections of kernels; the two constructions have different meanings.

65. Use the dimension formula to subtract shared directions once. Repeatedly counting an intersection overstates the size of a subspace sum.

66. Frobenius' inequality compares restrictions on nested intermediate images. Confirm all product shapes before inserting rank numbers.

67. A nonzero minor proves a lower bound on rank. One vanished minor does not prove an upper bound.

68. Rank at most r requires every minor of order r plus one to vanish. Structural column dependencies can establish the same upper bound more efficiently.

69. Separate parameter-zero branches before division. A generic RREF formula can lose exactly the exceptional cases an examination asks about.

70. At an exceptional parameter, recheck load compatibility as well as coefficient rank. A lower rank can mean either a larger fiber or no fiber.

71. Exact rank can jump from three to one at a single parameter value. Continuous entries do not force intermediate rank two to occur.

72. Constant-off-diagonal matrices can be analyzed on the all-ones line and the zero-sum space. Count the nonzero scalar actions with their correct multiplicities.

73. Exact and numerical rank answer different questions. A numerical tolerance must be stated with its scale assumptions.

74. Block diagonal ranks add because their images occupy disjoint coordinate blocks. Block triangular matrices with singular diagonal blocks need not obey that formula.

75. A Schur-complement rank formula requires an invertible leading block. Reversible block operations justify the formula and its branch conditions.

76. A nonzero outer product has rank one. Adding it changes rank by at most one, by applying the sum bound in both directions.

77. For invertible A, a rank-one update is singular exactly when $1+v^TA^{-1}u=0$. In that case its kernel is one-dimensional and its rank falls by exactly one.

78. An idempotent map splits its space into image and kernel. Rank equals trace over the reals, but orthogonality requires an additional symmetry condition.

79. A square-zero map has image contained in kernel, so rank is at most half the dimension rounded down. Nested kernels of powers stabilize permanently after their first equality.

80. Subtract the rank of independent linear constraints from the number of ambient coordinates. Repeated constraints, nonlinear conditions and field-dependent coefficients require separate checks before this rule applies.
