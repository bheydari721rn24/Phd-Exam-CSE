# Final reasoning rules

1. A recurrence does not define a unique sequence until its valid index range and enough starting values are stated; the same update can generate different sequences from different boundaries.

2. Every value used in a forward update must already be defined, or a separate existence argument is required. A self-reference at the boundary cannot replace an initial value.

3. When a recurrence begins later than its effective order suggests, keep the unconstrained initial prefix. Reducing its order does not authorize extending its domain backward.

4. Normalize the coefficient of the newest term only after verifying it is nonzero. A zero coefficient can change consistency or eliminate forward uniqueness.

5. An order-$k$ normalized recurrence beginning at $k$ needs an initial tuple of length $k$ for forward uniqueness, even when some last coefficients vanish.

6. A fixed-order homogeneous solution space has dimension $k$ because its initial tuple determines the sequence linearly and uniquely. Proposed modes must be independent as well as numerous enough.

7. A formula must satisfy every boundary value and the recurrence identity. Agreement at a few sampled indices is useful error detection, not a complete proof.

8. A missing base case can invalidate induction while every symbolic induction step remains correct. Check which predecessor indices the first step actually uses.

9. Linear means that unknown sequence values are not multiplied or raised to nonlinear powers; coefficients may still depend on the index.

10. A halving-argument cost equation can be linear in its unknown function without being a constant-lag sequence equation. Its characteristic method requires a justified representation change.

11. Homogeneous equations have zero forcing. A fixed nonzero forcing produces an affine solution family, not a vector space closed under arbitrary addition.

12. The difference of two solutions with the same forcing is homogeneous. Their sum generally solves an equation with twice that forcing.

13. For $a_n=pa_{n-1}+q_n$, the contribution introduced at index $j$ is multiplied by $p^{n-j}$, not $p^{n-j+1}$.

14. Unrolling stops at the starting value actually supplied. If the boundary is at one, stop there rather than invent a value at zero.

15. For constant forcing and $p\ne1$, evaluate the finite geometric sum. The separate case $p=1$ gives a linear accumulated contribution and must not be obtained by dividing by zero.

16. A zero first-order multiplier erases earlier information. The product-form expansion remains valid, whereas dividing by a product containing zero is invalid.

17. An integrating factor works only when its normalizing product is nonzero. Verify this condition before telescoping a variable-coefficient equation.

18. A factorial multiplier can often be removed by dividing by $n!$; prove the transformed update and carry the original starting value through the normalization.

19. Periodic variable coefficients can be composed over a full period. The resulting constant update acts on a subsequence and must preserve its phase.

20. For multiplicative positive recurrences, taking logarithms or summing exponents can linearize the calculation. A constant characteristic root is not appropriate when the multiplier depends on the index.

21. Moving all homogeneous terms to the left fixes the signs of the characteristic polynomial. A negative recurrence coefficient becomes a positive polynomial coefficient at the corresponding position.

22. Deriving the polynomial by dividing by a root power assumes the root is nonzero. A nonzero last coefficient guarantees this for the standard characteristic polynomial.

23. Distinct roots contribute one exponential mode each. The Vandermonde initial system is invertible because the roots are distinct.

24. Boundary values at indices one and two must be inserted with those exponents. Relabeling them as zero and one solves a shifted sequence unless the shift is reversed.

25. Nonconsecutive observations can determine a solution only when their measurement matrix is invertible. Two even-index observations may fail to distinguish modes one and negative one.

26. Repeated copies of the same exponential are proportional and provide only one degree of freedom. Root multiplicity requires additional index powers.

27. A nonzero root of multiplicity $m$ contributes $n^j r^n$ for $j=0,\ldots,m-1$. The maximum polynomial degree is one less than the multiplicity.

28. Finite differences lower a nonconstant polynomial's degree by one. This fact explains why repeated shift factors annihilate polynomial-exponential modes.

29. To prove completeness, show that the modes satisfy the equation, are independent, and number $k$. A list of plausible trial solutions alone is insufficient.

30. Zero repeated roots cannot generally be represented by $n^j0^n$. Retain independent finite-prefix impulses and solve the nonzero-root tail.

31. A negative root produces alternating signs. Discarding its sign while retaining its magnitude changes the exact sequence.

32. Conjugate complex roots combine into real sine and cosine modes for real data. Complex intermediate roots do not imply a complex final sequence.

33. A largest root can have zero amplitude after the boundaries are fitted. Determine actual coefficients before asserting the sequence's growth.

34. Equal-magnitude oscillating modes can cancel on infinitely many indices. An upper bound on absolute values does not automatically provide a positive lower bound.

35. The Fibonacci convention here is $F_0=0,F_1=1$. Domino tilings use $T_0=T_1=1$ and therefore equal $F_{n+1}$, not $F_n$.

36. The error in the exact Binet approximation is below one half, but floating-point power evaluation adds its own error. Use integer methods when exact large terms are required.

37. For a nonhomogeneous equation, find the homogeneous family and one particular term before fitting the complete expression to the boundary data.

38. A particular solution need not satisfy the initial values. Its job is to produce the forcing under the recurrence operator.

39. Exponential forcing uses its base for the resonance test. Polynomial forcing uses base one, because a polynomial is multiplied by $1^n$.

40. If the forcing base is a root of multiplicity $m$, multiply the polynomial-exponential trial by $n^m$. The forcing's degree does not determine that multiplier.

41. An impossible coefficient equation can mean that the trial lies in the homogeneous null space. Diagnose resonance before concluding the recurrence is inconsistent.

42. Include all lower-degree coefficients in a polynomial trial. Index shifts generate lower-degree terms even when the forcing lacks them.

43. Mixed forcing components can have different resonance multipliers. Construct and verify each particular contribution separately before adding them.

44. Step forcing must be summed only after its activation index. Extending a later constant forcing backward changes the boundary correction.

45. A failed induction with a weak upper bound does not disprove the bound. A stronger claim with the right slack can close the update.

46. A counting recurrence needs cases that are disjoint, exhaustive, and reversibly reduced. A plausible numeric pattern does not establish a counting proof.

47. The empty object often contributes one because there is one valid empty completion. Check the definition rather than assigning every zero-size count zero.

48. Ordered compositions and unordered partitions are different objects. A last-part recurrence is valid only when a last position is actually distinguished.

49. Distinguishable token types multiply the number of choices even when they have the same numeric value. Losing their labels changes the recurrence coefficient.

50. A domino tiling's first horizontal placement forces a second horizontal placement across the same two columns. Removing only one produces a different boundary state.

51. Feasibility invariants such as area parity should be checked before recurrence calculations. A familiar shape with missing cells may not use the rectangle recurrence.

52. For forbidden patterns, store enough suffix information to determine legal next symbols. A total count alone may not be an autonomous state.

53. Symmetry can reduce several ending states to one count, but the total must include the correct multiplicity of that state.

54. An empty string has no last symbol. Initialize a last-symbol model at length one or introduce a separate empty-start state.

55. Transition weights count labeled choices when the model is combinatorial. They are not probabilities unless a separate normalized probability contract is provided.

56. In the derangement recurrence, the image choice contributes $n-1$ to both cycle cases. Both deletion operations must have a unique inverse.

57. Derangements and factorials can satisfy the same variable-coefficient relation with different boundaries. Sharing an update does not make their counts equal.

58. The recurrence $D_n=nD_{n-1}+(-1)^n$ follows from an alternating residual. Its sign is fixed by the initial values, not guessed independently.

59. Unlabeled blocks in a particular set partition remain distinct subsets. Inserting an element into one of $k$ existing blocks gives $k$ choices, not $k!$.

60. Stirling boundary values include $S(0,0)=1$ and zero outside the feasible range. These edges are part of the recurrence's correctness.

61. Bell numbers count all block counts, whereas marked-block counts weight each partition by its number of blocks. The distinguished object changes the answer.

62. In the Bell recurrence, choosing elements outside the new element's block makes the reconstruction unique. Marking an arbitrary block without tracking the mark overcounts.

63. A positive-index inclusion-exclusion formula can fail at zero. Check the empty-domain intersections before extending its domain.

64. Integer partitions into exactly $k$ parts and partitions with largest part at most $k$ use different state definitions and different recurrences.

65. Subtracting one from every part removes a full Ferrers column. Its total reduction is $k$, not one.

66. Ferrers transposition equates at most $k$ parts with largest part at most $k$. Exactly $k$ parts instead correspond to largest part exactly $k$.

67. Catalan decomposition uses the first matching close or first return, giving a unique split. Arbitrary splits would count an object multiple times.

68. A product of two sequence values makes the Catalan recurrence nonlinear. A closed form does not imply a linear characteristic method applies.

69. Full binary trees indexed by internal nodes have $2n+1$ total nodes. Changing the size convention changes valid indices and boundary values.

70. Prefix subtraction begins only where both original prefix equations exist. Obtain the first simplified boundary from the original definition.

71. Verify the converse after differencing a recurrence. A simplified update plus the correct earliest values should reconstruct the original equation.

72. A rational generating denominator records the recurrence, while its numerator records starting corrections and forcing. Identical denominators need not imply identical sequences.

73. Formal power-series coefficient arguments do not require analytic convergence when each coefficient uses finitely many products. Infinite numerical sums require separate justification.

74. A companion matrix must store enough recent terms in the declared order. Swapping its coordinates without swapping its rows changes the update.

75. Augmenting a constant-forcing equation with a coordinate equal to one yields a homogeneous matrix equation. That extra coordinate is constrained, not a new arbitrary boundary.

76. A logarithmic count of arithmetic stages does not mean logarithmic bit complexity. Exact output size and growing multiplication cost remain relevant.

77. A deterministic finite-state recurrence is eventually periodic, but it may have a transient. A bijective state map is periodic from the start.

78. Modular invertibility is different from nonzero real coefficients. The last coefficient must be a unit modulo the modulus to guarantee a reversible companion update.

79. Periodic forcing requires a phase coordinate for an autonomous residue model. A repeated scalar residue alone does not prove a complete state cycle.

80. Match the requested output before calculating: an exact value, a residue, an asymptotic bound, and a counting formula may need different representations. Preserve all assumptions while changing methods.
