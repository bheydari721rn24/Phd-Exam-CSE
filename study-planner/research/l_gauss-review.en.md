1. A linear equation is linear in its declared unknowns, with coefficients fixed during a solve. An external parameter may be classified separately, but a product of two unknowns is not an ordinary coefficient term.

2. Fix the unknown order before forming an augmented matrix. A missing variable contributes a zero coefficient rather than shifting the positions of later coefficients.

3. An $m$ by $n$ coefficient matrix acts on an $n$-coordinate variable vector and produces an $m$-coordinate load. The augmented matrix has $n+1$ columns, but still only $n$ unknowns.

4. The right-side column is data. It can contain a contradiction pivot in a full augmented RREF, but it is never a free variable or a solved coordinate.

5. A row exchange preserves the full solution set only when it exchanges the right sides along with the coefficient rows. Swapping coefficients alone generally changes the system.

6. Scaling a row is reversible only with a nonzero scalar in the coefficient field. Multiplication by zero can erase information and enlarge the solution set.

7. Adding a multiple of one row to a different row is reversible because the donor remains available. The inverse adds the negative multiple while leaving the donor unchanged.

8. Replacing two rows simultaneously by identical combinations is not an elementary addition. Its transformation can be singular, so verify invertibility rather than assuming every combination is harmless.

9. Row operations act by left multiplication. Column operations act by right multiplication and generally change the coordinates used for the unknown vector.

10. A composite row transform satisfies $M=TM_0$ with invertible $T$. Tracking this identity gives a stronger error check than merely observing an echelon-looking array.

11. Chronological operations $E_1$ then $E_2$ produce $E_2E_1M_0$. Undoing them requires $E_1^{-1}E_2^{-1}$, not the same factor order.

12. An atomic swap or temporary variable is required in code. Assigning one row over the other and then assigning back from the overwritten row duplicates data.

13. In REF, nonzero rows precede zero rows and leading positions move strictly rightward. Leading values need not be one unless normalization is imposed.

14. In RREF, every leading value is one and every other entry in its pivot column is zero. Nonpivot columns may still contain arbitrary entries.

15. A triangular square matrix with zero diagonal entries may fail REF conditions. Inspect actual leading positions rather than treating its diagonal as an automatic pivot list.

16. REF is generally nonunique. Different scaling choices and elimination routes can produce different REF arrays with the same solution set.

17. RREF is canonical within a fixed row-equivalence class. The row-operation trace and the intermediate fractions need not be canonical.

18. Pivot positions are determined from the current transformed array. Later-stage multipliers usually cannot be computed from original input entries.

19. A zero candidate pivot may be repaired by exchanging rows. It does not by itself prove singularity, inconsistency or a free coordinate.

20. If every eligible entry in a coefficient column is zero, skip that column without advancing the active row. A later column may still supply a pivot.

21. Pivot columns need not be consecutive and need not coincide with diagonal positions. This is especially important for rectangular systems and early zero columns.

22. The active pivot row has zeros in previously completed coefficient columns. This is the invariant that prevents later additions from destroying completed elimination.

23. Every column scan advances the column index and each accepted pivot advances the row index. These monotone indices prove termination of the finite elimination procedure.

24. Save the old elimination multiplier before overwriting its pivot-column entry. Recomputing it from a stored zero silently skips necessary trailing updates.

25. Transform every appended load column by the same row operation. Multiple loads share the coefficient reduction but can have different consistency outcomes.

26. A row $[0\;\cdots\;0\mid c]$ with $c\ne0$ proves inconsistency immediately. No free-variable choice can repair an equation that has no variable coefficients.

27. A fully zero augmented row is redundant information, not a contradiction. It represents the identity $0=0$.

28. If every coefficient-zero row has zero load, the system is consistent. Assigning free coordinates and solving pivot equations constructs a solution and proves sufficiency.

29. Count free coordinates only after consistency has been checked. An inconsistent system has no solution family, regardless of how many coefficient columns lack pivots.

30. For a consistent system with $n$ unknowns and $r$ coefficient pivots, the number of independent free coordinates is $n-r$. Redundant equation count is irrelevant to this dimension.

31. A consistent real system with a pivot in every coefficient column has a unique solution. A pivot in every equation row alone does not guarantee uniqueness when there are more unknowns than rows.

32. More equations than unknowns does not force inconsistency. Independent equations can determine a point while the remaining equations provide compatible redundant checks.

33. Fewer equations than real unknowns precludes a unique solution when the system is consistent. It does not guarantee consistency of the supplied loads.

34. A homogeneous system is always consistent because its zero vector is a solution. It has nonzero solutions exactly when at least one coefficient coordinate is free.

35. Generalized backward substitution uses the actual pivot column $p_i$, with nonzero denominator $u_{i,p_i}$. The square diagonal formula requires stronger triangular assumptions.

36. In ordinary nonsingular upper triangular substitution, process rows from bottom to top. In a lower triangular solve, process rows from top to bottom.

37. Setting free coordinates to zero gives one convenient particular solution, not necessarily a minimum-norm solution or the only solution satisfying additional restrictions.

38. A complete solution is a particular point plus a span of homogeneous directions. Verify both the point and each direction in the original coefficients.

39. The canonical free-coordinate directions are independent because their free-coordinate entries form an identity array. This also proves uniqueness of the parameter representation.

40. Every alleged complete family needs a converse argument. Showing that its displayed vectors solve the equations does not prove that no solutions were omitted.

41. Two distinct real solutions generate an entire affine line of solutions. Thus a real linear system cannot have exactly two, three or any other finite number greater than one.

42. Over a finite field with $q$ elements, a consistent system with $k$ free coordinates has $q^k$ solutions. The word “infinite” relies on an infinite coefficient field.

43. A coefficient-zero equation is the whole space when its load is zero and the empty set otherwise. It is not an ordinary line or plane.

44. Row additions preserve the common intersection of equations, not the geometric set defined by each individual equation. Draw the common solution point or family as the invariant.

45. Row operations preserve row space and kernel. They generally move the column space through the invertible left transformation while preserving its dimension.

46. Use pivot indices from reduction to select original columns when seeking an original column-space basis. Reduced pivot columns usually belong to a different geometric subspace.

47. A contradiction row supplies an original-coordinate certificate $y^TA=0$ and $y^Tb\ne0$. Multiplying any alleged solution by that row combination immediately refutes it.

48. Every dependence among coefficient rows requires the identical dependence among loads. All such compatibility conditions must hold, not just the first dependence noticed.

49. A single appended load increases rank by at most one. Several displayed contradiction rows do not create several independent last-column pivots.

50. RREF uniqueness follows from the common row space, its prefix-projection dimensions and its uniquely specified pivot-coordinate rows. It does not depend on one preferred elimination route.

51. Before dividing by a parameter expression, branch on every value where it vanishes. Return to the last undivided valid system for those exceptional values.

52. Cancelling a parameter factor gives a formula only on its nonzero branch. A continuous extension of one formula can miss an entire exceptional solution family.

53. A singular square coefficient branch may be inconsistent or have infinitely many real solutions. Reducing its right side distinguishes these cases.

54. A determinant polynomial identifies potential uniqueness failures for square systems. It is not a complete compatibility test and is unavailable as a direct determinant test for nonsquare arrays.

55. State the parameter domain before classifying roots. Real, complex and finite-field exceptional sets can differ.

56. If coefficient columns are transformed by $Q$, solve $AQy=b$ and recover $x=Qy$. Ignoring that final coordinate map usually returns the wrong original vector.

57. Complete pivoting includes column permutations and therefore requires variable permutation bookkeeping. Partial pivoting exchanges equations only.

58. Unpivoted Doolittle elimination assumes legal nonzero pivots in the chosen ordering. Nonsingularity alone does not ensure those particular pivots exist without exchanges.

59. For nonsingular square input, nonzero leading principal minors characterize nonzero-pivot elimination without exchanges. Singular triangular-factor cases require separate statements.

60. The unpivoted Doolittle pivot satisfies $u_{kk}=\Delta_k/\Delta_{k-1}$ with $\Delta_0=1$. Do not apply original-order minors after arbitrary permutations without checking the new ordering.

61. Doolittle uses unit diagonal in $L$, while Crout uses unit diagonal in $U$. An examination question that does not impose normalization permits diagonal rescaling of factors.

62. An unrestricted factorization $LU$ remains the same after replacing the factors by $LD$ and $D^{-1}U$. First-column proportionality can therefore be enough to identify a possible LU column.

63. The first column of an upper triangular $U$ has only its first entry potentially nonzero. Hence the first column of $LU$ is $u_{11}$ times the first column of $L$.

64. In $PA=LU$, solve $Ly=Pb$ before solving $Ux=y$. For the convention $A=P_0LU$, the load is instead $P_0^Tb$.

65. A later pivot row exchange must exchange the already stored earlier multiplier columns of $L$. Swapping only the current upper array can leave a visually triangular but false factorization.

66. The full matrix identity $PA=LU$ is the factorization certificate. Also check the unit-lower and upper-triangular structural conditions.

67. A Gauss transform $I-ge_k^T$ has inverse $I+ge_k^T$ because $g_k=0$ makes the rank-one square vanish. General lower triangular inverses need additional cross terms.

68. A block Schur complement is $E-DB^{-1}C$ with transformed load $g-DB^{-1}f$. Its derivation requires invertible $B$ and preserves the stated factor order.

69. Reducing $[A\mid I]$ to $[I\mid B]$ yields the square inverse $B$. If the left block is singular, the surviving right block is an invertible row transform, not an inverse of $A$.

70. A full-column-rank rectangular matrix may have a left inverse and unique compatible solutions without admitting every load. A left inverse is generally neither unique nor two-sided.

71. Reuse one factorization for multiple loads. Dense factorization is cubic in dimension, while each triangular solve is quadratic under the ordinary scalar-operation model.

72. Operation counts must specify whether divisions, comparisons, row swaps, loads and fused multiply-add instructions are included. Distinct valid conventions can give different exact formulas.

73. A field-operation count is not a bit-complexity bound for exact rationals. Intermediate numerators and denominators can grow even when the loop count is polynomial.

74. Partial pivoting bounds multiplier magnitudes by one in the current real or complex column. It does not bound every trailing entry by the largest original coefficient.

75. Exact zero and numerical near-zero are different concepts. Numerical rank estimates need a declared scale and precision; a universal fixed tolerance cannot certify every exact rank.

76. A rounding example must specify its arithmetic model. Three-significant-digit decimal rounding is not the same model as exact fractions or ordinary binary double precision.

77. A small residual bounds forward error only through inverse amplification. Check $\Vert e\Vert\le\Vert A^{-1}\Vert\Vert r\Vert$ rather than treating residual size as an unconditional accuracy guarantee.

78. Conditioning belongs to the system and stability to the method. Pivoting can improve the method while an ill-conditioned system remains sensitive to perturbations.

79. Integer and nonnegative restrictions are additional constraints on the field solution family. Real consistency and free-coordinate dimension do not determine integer solution counts.

80. Finish an examination calculation with original-system substitution, exceptional-case checks and a completeness argument. A correct-looking intermediate array or one valid point alone is insufficient evidence.
