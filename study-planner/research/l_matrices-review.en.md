## 13. Consolidation: essential results and examination reasoning

This section condenses results **after** the full teaching and worked solutions. Read it as a retrieval map: each statement includes the condition under which it is valid and a way to recognize when it is useful. It does not replace the derivations. “Examination reasoning” here means general mathematical problem-solving patterns; archived Iranian MSc and PhD papers remain reserved for the final month as requested.

### 13.1 The essential-result map

| Result | Necessary context | Meaning and use |
|---|---|---|
| (AB)<sub>ij</sub> = ∑<sub>k=1</sub><sup>n</sup> a<sub>ik</sub>b<sub>kj</sub> | A is m-by-n and B is n-by-p. | The output is m-by-p. Keep the free indices and sum the shared index. |
| (AB)x = A(Bx) | Every intermediate product is compatible. | The rightmost transformation acts first on a column vector. |
| Column j of AB is A times column j of B. | B's column has A's input dimension. | Use this view for multiple inputs, sparse coefficients, and column-span reasoning. |
| Row i of AB is row i of A times B. | A's row length matches B's number of rows. | Use this view for row combinations and left multiplication. |
| AB is a sum of paired column-row outer products. | Column k of A is paired with row k of B. | Each term has the output shape and exposes simple constituent maps. |
| (AB)C = A(BC) | The ordered chain is compatible. | Change grouping to reduce work; do not change factor order. |
| (AB)<sup>T</sup> = B<sup>T</sup>A<sup>T</sup> | Ordinary transpose over ℝ or ℂ. | Reverse the complete factor sequence. |
| (AB)<sup>*</sup> = B<sup>*</sup>A<sup>*</sup> | The star means conjugate transpose. | Complex scalar factors must also be conjugated. |
| (AB)<sup>−1</sup> = B<sup>−1</sup>A<sup>−1</sup> | Both square factors are invertible. | Undo actions in reverse sequence. |
| AXB = C has solution A<sup>−1</sup>CB<sup>−1</sup>. | A and B are square and invertible. | Apply inverses on the sides where cancellation is justified. |
| A = (A+A<sup>T</sup>)/2 + (A−A<sup>T</sup>)/2 | A is real and square. | Separate the unique symmetric and skew-symmetric parts. |
| x<sup>T</sup>A<sup>T</sup>Ax = ‖Ax‖² | A is real; x has its input dimension. | Establish positive semidefiniteness and identify equality conditions. |
| Q<sup>T</sup>Q = I implies input-length preservation. | Q is real; square shape is not required. | A rectangular embedding can preserve lengths while QQ<sup>T</sup> differs from I. |
| (I−N)<sup>−1</sup> is the finite sum I+N+⋯+N<sup>r−1</sup>. | N<sup>r</sup> = 0. | Derive a structured inverse without convergence or elimination. |
| tr(AB) = tr(BA) | A is m-by-n and B n-by-m. | The square products may have different sizes. Trace equality is not matrix equality. |
| ‖A‖<sub>F</sub>² = tr(A<sup>T</sup>A) | A is real; use the adjoint for complex A. | Connect entry geometry, column lengths, and Gram matrices. |

### 13.2 Shape, indexing, and interpretation: ten rules

1. **Record the shape of every given matrix.** A statement such as “A is rectangular” is insufficient for a chain involving several factors. Carry its row and column counts through each intermediate expression.
2. **Check addition independently of multiplication.** Multiplication needs matching inner dimensions. Addition needs both dimensions equal. A product being defined does not make a sum of its factors defined.
3. **Do not identify a row with a column.** A row-column product is a scalar, while a column-row product is an outer-product matrix. A missing transpose can change the problem's meaning completely.
4. **Check the output shape before calculating entries.** If a proposed answer has the wrong shape, no arithmetic correction can make it the product. This is the fastest reliable rejection criterion.
5. **Track free and dummy indices.** In a product-entry formula the free indices determine the output position; the repeated internal index is summed. A formula that drops an output index cannot specify every entry correctly.
6. **Choose a single indexing convention.** Mathematical formulas here start at one; the pseudocode starts at zero. Translate the range as a whole instead of mixing endpoints.
7. **Recover columns through basis inputs.** To construct a standard matrix, place T(e<sub>j</sub>) in column j. Transposing those images can accidentally produce a map with another input dimension.
8. **Distinguish equality on a vector from equality of maps.** One input can lie in the set where two different maps agree. A basis or the entire input space suffices for a universal equality claim.
9. **Use semantic labels when modeling.** A person-by-item matrix times an item-by-supplier matrix has person-by-supplier meaning. Matching numerical dimensions alone does not prove a model uses the intended axes.
10. **Attach sizes to ambiguous identities and zeros.** For an m-by-n matrix the left identity is I<sub>m</sub> and the right identity I<sub>n</sub>. Different block positions often require different zero shapes.

### 13.3 Algebra and cancellation: ten rules

11. **Associativity preserves the ordered factor list.** It allows ABC to be grouped either way. It provides no permission to rewrite it as ACB.
12. **Distribute before combining terms.** Expand (A+B)² as A²+AB+BA+B². Combining the middle terms requires a proved commutation condition.
13. **A scalar can move across a matrix factor.** Its action scales every entry. A matrix cannot generally be moved in the same way.
14. **A nonzero matrix need not be invertible.** A projection or a nilpotent matrix provides an immediate counterexample. State the inverse hypothesis explicitly when cancelling.
15. **A zero product does not force a zero factor.** Read AB = 0 as A killing every column of B. This identifies the exact lost directions rather than relying on a scalar rule.
16. **Cancellation depends on the side.** A left inverse justifies cancelling the leftmost A from AX = AY. A right inverse justifies cancelling the rightmost A from XA = YA.
17. **Avoid matrix division notation.** For AX = B, the answer is A<sup>−1</sup>B; for XA = B, it is BA<sup>−1</sup>. These expressions can differ.
18. **One-sided inverse equivalence needs square finite-dimensional matrices.** A rectangular embedding and coordinate reader can satisfy LA = I while AL is a nonidentity projection.
19. **Invertibility does not survive arbitrary addition.** I and −I are both invertible but sum to zero. Never distribute the inverse over a sum.
20. **An exceptional parameter value is part of the answer.** Before using a reciprocal or inverse formula, identify where the denominator vanishes. Give a separate singularity argument at those values.

### 13.4 Transposes and structure: ten rules

21. **Transpose swaps dimensions and reverses products.** For a long product reverse every factor, not only the first pair. A rectangular example is an effective check.
22. **An ordinary transpose does not conjugate.** Over complex numbers A<sup>T</sup> and A<sup>*</sup> are distinct operations. Length and positivity statements generally require the latter.
23. **The adjoint conjugates scalar multipliers.** The identity (αA)<sup>*</sup> = <span class="overline">α</span>A<sup>*</sup> is especially important when α is imaginary.
24. **Skew-symmetric real matrices have zero diagonal.** This follows from twice a diagonal entry being zero. Skew-Hermitian complex matrices may have imaginary diagonal entries instead.
25. **A real skew-symmetric quadratic value is zero.** A skew-Hermitian quadratic value is merely purely imaginary. Keep the field and transpose convention visible.
26. **Symmetry of a product requires a condition.** For symmetric factors, the product is symmetric exactly when they commute. The statement does not follow merely from symmetry of each factor.
27. **Gram matrices measure pairwise column or row inner products.** A<sup>T</sup>A uses columns; AA<sup>T</sup> uses rows. Their dimensions and interpretations can differ.
28. **Positive semidefinite does not mean entrywise nonnegative.** Prove positivity by a squared norm or a quadratic value. Negative off-diagonal entries are allowed.
29. **Orthonormal columns preserve input lengths.** For a rectangular matrix this condition does not make the reverse product an identity. It identifies an embedding into a possibly larger space.
30. **A product of orthogonal square matrices is orthogonal.** Use the reversed transpose rule and cancel the adjacent Q<sup>T</sup>Q pairs. The same argument applies to unitary matrices with adjoints.

### 13.5 Powers, blocks, and computation: ten rules

31. **Matrix powers require square matrices.** The zeroth power is an identity of the same size. Negative powers additionally require invertibility.
32. **Polynomials in the same matrix commute.** Every term is a power of that common matrix. This useful special case does not make unrelated matrices commute.
33. **Nilpotence is a repeated-action statement.** N² = 0 can occur with N nonzero. A finite geometric inverse series then terminates exactly, without an analytic convergence issue.
34. **Strict triangularity includes the diagonal.** A strictly upper-triangular n-by-n matrix satisfies N<sup>n</sup> = 0 because no increasing chain can have n steps. An ordinary upper-triangular matrix need not be nilpotent.
35. **Compatible block partitions must match internally.** Matching the number of blocks is not enough. Verify the widths and heights of every block product and the shapes of terms being added.
36. **Preserve order inside block products.** Blocks are matrices, not commuting scalars. A scalar-looking block formula can be false even when each individual block product exists.
37. **Left and right elementary multiplications have distinct effects.** I+αe<sub>i</sub>e<sub>j</sub><sup>T</sup> adds row j into row i on the left, but column i into column j on the right.
38. **Count the algorithm that is actually used.** Classical dense multiplication costs mnp multiplications, but special structure or a different algorithm can change this. State whether initialization additions are counted.
39. **Choose grouping from intermediate dimensions.** Matrix-chain parenthesization changes work and storage while preserving exact algebraic output. It does not reorder transformations.
40. **Exact identities and numerical outcomes are different claims.** Rounding can cause tiny differences between computed parenthesizations. A proof uses exact arithmetic; a numerical implementation should specify tolerances and arithmetic conventions.

### 13.6 Trace, norms, and advanced distinctions: ten rules

41. **Trace is defined for square matrices.** The factors of a traced product can be rectangular as long as the full product is square. Confirm that every cyclically rotated product is compatible.
42. **Cyclic trace rotation is not arbitrary permutation.** tr(ABC) equals tr(BCA), but can differ from tr(ACB). Matrix units provide a short counterexample.
43. **Trace equality discards information.** Distinct matrices can have the same trace, and traced products may even have different sizes. Never infer matrix equality from one scalar statistic.
44. **Frobenius geometry uses all entries.** Its square equals the sum of squared column lengths and also tr(A<sup>T</sup>A). It is not the same as the amount by which every vector length changes.
45. **Orthogonal left or right factors preserve Frobenius norm.** Prove the left case from columns and the right case from rows, or use trace cyclicity with compatible dimensions.
46. **The symmetric/skew decomposition is orthogonal in Frobenius geometry.** The squared norms add because the inner product vanishes. Do not replace that with an unsquared norm sum.
47. **Ordinary, Hadamard, and Kronecker multiplication are distinct.** Their compatibility conditions, output shapes, and commutation properties differ. The product symbol is part of the definition.
48. **Kronecker mixed-product order stays intact.** The rule groups AC and BD; it does not substitute CA or DB. Verify the paired dimensions before using it.
49. **Graph powers count walks, not necessarily simple paths.** Repeated vertices are permitted. Even a graph with no self-loop can have positive diagonal entries in a higher power.
50. **Retain the mixed term in a perturbation identity.** The exact product error is AF+EB+EF. Calling the first two terms the whole error without an approximation qualification is incorrect.

### 13.7 A reliable solution workflow

For a calculation, first annotate shapes and decide what each matrix represents. Predict the output shape. Choose a product view that exposes zeros, selectors, diagonal scaling, outer products, or compatible blocks. Calculate only the entries needed, then check a column or row through an independent viewpoint. If an inverse is involved, substitute the answer back into the original ordered equation.

For a proof, state the dimensions and field. Decide whether an arbitrary-entry proof, a basis-image proof, or a transformation-composition proof is shortest. Carry every free index through the argument. Use a property only after verifying its hypotheses. Conclude equality of the entire matrix, rather than of an illustrative entry.

For a proposed universal statement, identify the scalar rule being transferred. Test undefined dimensions, noncommuting two-by-two matrices, nonzero nilpotent matrices, rectangular one-sided inverses, and complex vectors. One valid counterexample refutes a universal claim, but passing a few examples does not prove it. Prefer the smallest counterexample that isolates the failed assumption.

For a structured problem, reduce it to a definition. A transpose relation suggests comparing reflected entries; a Gram relation suggests a norm; a nilpotent relation suggests a finite polynomial; a block relation suggests matching one block at a time. This approach turns memorized formulas into derivable consequences and supports difficult unfamiliar variants.

## 14. References, provenance, and completion boundary

1. **Stanford University — Stephen Boyd, EE263, archival Matrix Operations, Lecture 2.** Reviewed slides 1–15. [Written primer](https://ee263.stanford.edu/archive/matrix-primer-lect2.pdf). [Archival course lectures, Autumn 2007–08](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures.html). The chapter independently expands proofs and edge cases.
2. **University of Oxford — M1 Linear Algebra I, Michaelmas 2022; course instructor Andrew Wathen.** Reviewed printed pp. 8–13 and 21–24. [Lecture notes](https://courses.maths.ox.ac.uk/pluginfile.php/25471/mod_folder/content/0/lecture_notes22.pdf?forcedownload=1). [Course record](https://courses.maths.ox.ac.uk/course/view.php?id=609). The PDF title page does not identify a separate note author. Strict-triangular and identity-dimension slips are corrected in the synthesis.
3. **University of California, Berkeley — Alexander Paulin, Math 54, Spring 2018.** Reviewed all four handwritten pages of [Matrix Algebra](https://math.berkeley.edu/~apaulin/Matrix%20Algebra.pdf), rendered for visual reading. [Course index](https://math.berkeley.edu/~apaulin/54(Spring%202018%20Videos%20and%20Notes).html). Basis images, composition, and cancellation are recast in the chapter's consistent notation.
4. **Massachusetts Institute of Technology — Gilbert Strang, 18.06SC Linear Algebra, Fall 2011.** [Multiplication and inverse matrices, lecture summary](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/1963da71c4d96e5d14e7939780f79bcc_MIT18_06SCF11_Ses1.3sum.pdf), instructional pp. 1–3. [Transposes and permutations summary](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/33b21afab62ea8df6c7bd241240df60d_MIT18_06SCF11_Ses1.5sum.pdf), instructional pp. 1–2. [Recitation problems](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/8e9ccbcc13300a9bda7f24a684bd16b6_MIT18_06SCF11_Ses1.3prob.pdf) and [solutions](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/d2dc903ca48f3d1ffa1528abde719c94_MIT18_06SCF11_Ses1.3sol.pdf), instructional pages only. Worked Problems 5 and 24 adapt the two relevant mathematical problem types with independently written solutions. The second is identified in the source as Strang, Section 2.5, Problem 24; no claim of reading the complete textbook is made.
5. **Carnegie Mellon University — William Gunther, 21-241 Matrix Algebra, Summer I 2014.** [Summary of Day 7, May 28, 2014](https://www.math.cmu.edu/~wgunther/241/m14/notes/week2/7.pdf), pp. 1–4. [Course index](https://www.math.cmu.edu/~wgunther/241/m14/index.html). Used as the additional application source for quantities, coordinate selection, and graph walks.
6. **Surveyed reserve: Harvard University — Oliver Knill, Math 21b, Spring 2023.** [Matrix product, Lecture 6](https://people.math.harvard.edu/~knill/teaching/math21b2023/handouts/lecture06.pdf) and [Matrix inverse, Lecture 7](https://people.math.harvard.edu/~knill/teaching/math21b2023/handouts/lecture07.pdf), two pages each reviewed. [Course index](https://people.math.harvard.edu/~knill/teaching/math21b2023/). Concise coverage and identified notation slips made these reserve comparisons, rather than selected backbone sources.
7. **Surveyed reserve: University of Cambridge — Stephen J. Cowley, IA Vectors and Matrices, Michaelmas 2010.** [Official teaching index](https://www.damtp.cam.ac.uk/user/sjc1/teaching/). Introductory scope and access conditions were inspected; the matrix chapter body was not reviewed in this run and is not counted among the read courses.

The selected sources cover the chapter's stated matrix-algebra boundary. Original extensions include the systematic proof treatment, worked bank, 50-rule review, typography, and composition laboratory. The chapter does not reproduce all exercises from the surveyed full courses. Its bank contains both in-scope MIT recitation types and selected adapted types from other reviewed materials, together with original problems and complete solutions.

The source audit records what was read and why sources were selected. The quality audit records mathematical checks and display inspection. General rank, elimination, determinant, eigenvalue, and SVD results remain scheduled in their own chapters. No literal guarantee about all future examination questions is made; mastery of this boundary is supported by explicit coverage and verification rather than an unverifiable performance promise. The student explicitly approved this chapter on 2026-10-02; it is now ready in the finished library.
