# Final examination rules

1. Declare the field and inner product before using perpendicularity. A weighted Gram product can make ordinarily nonperpendicular vectors perpendicular.

2. A real Gram matrix defines an inner product exactly when it is symmetric positive definite. Symmetry and nonnegative diagonal entries alone do not suffice.

3. A complex Gram matrix must be Hermitian positive definite. Ordinary transpose cannot replace conjugate transpose.

4. In this chapter the first argument is conjugate linear and the second is linear. A source using the other convention requires translated coefficients.

5. Length is the square root of the self-product. Squared length scales by $|\alpha|^2$, while length scales by $|\alpha|$.

6. Strict positivity is the reason a vector perpendicular to itself must be zero. The conclusion fails for indefinite bilinear forms.

7. For a symmetric matrix $\begin{pmatrix}a&b\\b&c\end{pmatrix}$, positive definiteness is equivalent to $a>0$ and $ac-b^2>0$.

8. A Gram matrix $A^*A$ is positive semidefinite for every matrix $A$, and positive definite exactly for independent columns.

9. The identity $\ker(A^*A)=\ker A$ holds over real and complex Euclidean spaces. Its proof uses $\|Ax\|^2$, not cancellation of a potentially singular factor.

10. Consequently $\operatorname{rank}(A^*A)=\operatorname{rank}A$. The ambient dimension of the Gram matrix remains the number of columns.

11. Cauchy–Schwarz equality holds exactly for linearly dependent input vectors, including cases involving zero.

12. A real unsigned angle is defined only for nonzero vectors and lies in $[0,\pi]$. A negative right angle is not part of that convention.

13. A negative real product corresponds to an obtuse angle. A complex product does not generally define the same arccosine expression.

14. For real vectors, Pythagorean equality is equivalent to perpendicularity. For complex vectors it only forces the real part of the product to vanish.

15. Equality in the real triangle inequality requires the same nonnegative direction, or a zero input. Opposite dependent vectors do not generally give equality.

16. Polarization reconstructs real products from norms. A linear norm-preserving map therefore preserves real products.

17. A translation preserves distances but generally changes norms from the origin. Distance preservation does not by itself establish linearity.

18. Pairwise orthogonality gives independence only when every listed vector is nonzero.

19. Normalize a nonzero orthogonal vector by its own norm. A zero residual cannot be normalized.

20. Coefficients in an orthogonal basis are $\langle u_j,x\rangle/\|u_j\|^2$ under the chapter convention. Unit-length denominators disappear only after normalization.

21. In an orthonormal complex basis the analysis coefficient is $\langle q_j,x\rangle$. Reversing the arguments conjugates it.

22. A nonorthogonal basis couples coefficients through its Gram matrix. Independent scalar projection coefficients cannot replace that system.

23. The Gram matrix in an orthogonal but unnormalized basis is diagonal with the basis squared norms. Summing coefficient squares without those weights is wrong.

24. Testing a spanning list suffices to characterize its perpendicular complement. Testing only one generator of a larger span does not.

25. Every perpendicular complement is a subspace. The intersection with the original subspace contains zero and, for an inner product, contains no other vector.

26. In finite dimension $\dim W+\dim W^\perp=\dim V$. The dimension refers to the same stated ambient space.

27. In finite dimension $(W^\perp)^\perp=W$. Infinite-dimensional versions can require closure and completeness hypotheses.

28. An algebraic complement need not be perpendicular. A direct-sum decomposition alone does not prove a minimum-distance property.

29. Row space and nullspace belong to the domain coordinate space. Column space and left nullspace belong to the codomain coordinate space.

30. For a real $m$-by-$n$ matrix of rank $r$, the four dimensions are $r,n-r,r,m-r$. They are not generally all equal.

31. The row-side perpendicular complement is $\ker A$, and the column-side perpendicular complement is $\ker A^*$. In complex coordinates the row-side space is identified through conjugation.

32. A system $Ax=b$ is consistent exactly when every left-null vector is perpendicular to $b$.

33. One left-null vector with nonzero product against $b$ is a certificate of inconsistency.

34. Perpendicular complements reverse inclusions: if $U\subseteq W$, then $W^\perp\subseteq U^\perp$.

35. The identity $(U+W)^\perp=U^\perp\cap W^\perp$ follows directly from the definition.

36. In finite dimension $(U\cap W)^\perp=U^\perp+W^\perp$. Do not silently transfer the statement to unrestricted infinite-dimensional subspaces.

37. A nonzero line generator gives $P_u=uu^*/(u^*u)$. Nonzero scalar rescaling does not alter this projector.

38. A zero generator defines the zero subspace, whose projector is zero. The line division formula itself remains undefined.

39. A projected vector is certified by membership in the target subspace and a perpendicular residual. Either condition alone is insufficient.

40. A perpendicular residual belongs to the perpendicular complement; it is a vector and is not equal to that entire subspace.

41. Projection onto an orthonormal column basis is $QQ^*$, with physical dimension equal to the ambient space.

42. For rectangular orthonormal $Q$, $Q^*Q=I$ but $QQ^*$ generally is a proper projector. A two-sided inverse is available only in the square case.

43. The perpendicular projector is independent of which orthonormal basis spans its subspace.

44. The closest-point proof compares squared distance with a sum of two nonnegative squared lengths. Equality identifies a unique minimizer.

45. Perpendicular projection contracts the norm: $\|Px\|\le\|x\|$. Equality holds exactly for vectors already in the target subspace.

46. A Euclidean projector is orthogonal exactly when it is self-adjoint and idempotent. Neither property alone is enough.

47. Every idempotent splits its space into image plus kernel, even when the splitting is oblique.

48. An oblique projector can increase Euclidean length and need not produce the Euclidean closest point.

49. For an idempotent, all positive powers equal the matrix and trace equals rank. Symmetry is unnecessary for those algebraic facts.

50. The complementary projector is $I-P$. Its image and kernel are the original kernel and image.

51. A full-column-rank basis gives $P=A(A^*A)^{-1}A^*$. Invertibility of the Gram matrix is a hypothesis, not an automatic property of generators.

52. For dependent generators, select an independent column basis or use an appropriate pseudoinverse. Never invert their singular Gram matrix.

53. A physical projection remains unique even when generator coefficient representations are not unique.

54. For a hyperplane through zero with real normal $n\ne0$, subtract $n(n^Tx)/(n^Tn)$. The distance is $|n^Tx|/\|n\|$.

55. Projection onto a shifted affine plane includes a constant term. It need not be a linear operator.

56. Bessel uses an orthonormal list and leaves a nonnegative residual term. Equality means membership in that list's span.

57. Parseval holds for a complete orthonormal expansion. A partial list does not automatically give norm equality.

58. Squared distance to an orthonormal span is the original squared norm minus the sum of captured coefficient magnitudes squared.

59. Gram–Schmidt preserves every ordered input prefix span, not merely the final span.

60. At each orthogonalization step remove all preceding accepted components. Removing only the immediately previous vector is generally insufficient.

61. Independent inputs produce nonzero exact Gram–Schmidt residuals. A zero residual diagnoses membership in the preceding span.

62. A dependent column can be skipped while later columns are still processed. Permanent termination can miss later independent directions.

63. Changing input order generally changes orthonormal outputs and intermediate spans. The final projector is unchanged if the final span is unchanged.

64. Unnormalized orthogonalization often preserves rational arithmetic. Normalize only when an orthonormal output or QR factor is required.

65. Reduced QR for an $m$-by-$r$ full-column-rank matrix has $Q$ of size $m$ by $r$ and $R$ of size $r$ by $r$.

66. The reduced QR factor $R=Q^*A$ is upper triangular because later orthonormal vectors are perpendicular to earlier input prefixes.

67. With standard Gram–Schmidt normalization, $R$ has strictly positive real diagonal. This fixes sign or phase ambiguity.

68. Without the diagonal convention, valid QR factors can change column signs or phases while preserving their product.

69. Gram–Schmidt on an invertible real upper triangular matrix produces signed standard coordinate vectors. Positive input diagonal gives the unsigned canonical basis.

70. For independent columns, least squares reduces to $Rc=Q^*b$ and triangular back substitution.

71. For dependent columns, a least-squares fitted physical vector is unique but its coefficients may form an affine family.

72. The least-squares residual lies in $\ker A^*$. Its norm can be checked using perpendicular decomposition without reconstructing every coefficient.

73. In weighted geometry use $A^*GA$ and $A^*Gb$. The resulting projection minimizes the weighted norm, not an unstated Euclidean norm.

74. Weighted perpendicular projection obeys $P^*G=GP$ and $P^2=P$. Its coordinate matrix can be ordinarily nonsymmetric.

75. A basis change transports the metric by congruence $S^*GS$, while an operator matrix changes by similarity $S^{-1}PS$.

76. Integral products are strictly positive on continuous nonzero functions on a nondegenerate interval. Arbitrary pointwise function spaces require care about almost-everywhere equivalence.

77. On a symmetric interval odd functions are perpendicular to even functions. This can eliminate all coefficients before doing lengthy integrals.

78. Sampled products on degree-at-most-$d$ polynomials need at least $d+1$ distinct nodes with positive weights for strict positivity.

79. Trigonometric cosine indices with opposite signs duplicate the same function. Distinct absolute frequencies, not merely distinct integers, determine distinct cosine directions.

80. The constant Fourier function has a different squared normalization from nonzero sine/cosine frequencies. The zero sine cannot be normalized into a basis vector.

81. Householder reflection fixes a perpendicular hyperplane and reverses its normal. Projection deletes the normal instead; the two operators are different.

82. A product of two orthogonal projectors is an orthogonal projector exactly when the factors commute. Its image is then their image-space intersection.

83. Nested projector differences and perpendicular-space projector sums have valid projection interpretations. General sums and differences require separate checks.

84. Exact algebra, a numerical tolerance and an illustrative animation serve different purposes. Use exact membership, residual, metric and identity checks to certify an examination answer.
