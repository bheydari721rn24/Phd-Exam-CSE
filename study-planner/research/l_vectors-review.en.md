## 12. High-yield review and examination reasoning

This section is a revision companion to the full lesson. Each rule states its assumptions and the mistake it prevents. If a statement here is unfamiliar, return to its derivation rather than memorizing it in isolation.

### 12.1 Start by identifying the object, field, and geometry

1. Determine whether each supplied list represents a point, a displacement, standard coordinates, or coordinates in another basis. A displacement from A to B is B−A; a distance to an affine set begins by subtracting a base point. Problems 1 and 24 illustrate the distinction.
2. Check the ambient dimension before addition, dot products, or projections. Every coordinatewise operation requires matching coordinate counts. A low-dimensional diagram may illustrate a theorem in higher dimensions, but it does not change the theorem's ambient space.
3. Identify the allowed scalar field before deciding dependence or dimension. The pair 1,i is independent over the reals and dependent over the complex numbers. A complex vector space considered as real can have a different dimension.
4. Identify the actual inner product. Ordinary, weighted, polynomial-integral, and complex geometries can have the same algebraic span but different projections and orthogonality. Problems 19 and 23 show why using one geometry for the numerator and another for normalization is invalid.
5. Verify that a proposed inner product is bilinear and symmetric over the reals, or appropriately sesquilinear and conjugate-symmetric over the complex numbers. Then check strict positivity on every nonzero vector. Nonnegativity alone is insufficient: Problems 11 and 13 supply zero-length nonzero counterexamples.

### 12.2 Span, independence, and coordinates: a reliable decision procedure

**To test span membership**, write a general linear combination, compare coordinates, and solve the coefficient constraints. Reconstruct the candidate after solving. A failed constraint proves nonmembership; counting the supplied vectors without checking redundancy proves nothing.

**To test independence**, set the combination equal to zero. If only the all-zero coefficient list works, the list is independent. One explicit nonzero coefficient list producing zero proves dependence. A zero input, duplicate input, or scalar multiple supplies an immediate relation. Every pair being nonparallel does not prove a larger list independent.

**To establish a basis**, prove both spanning and independence. The first provides representations; the second makes them unique. An independent list is always a basis of its own span, but may fail to span the stated ambient space. The empty list is the basis of the zero subspace.

**To test a subspace**, check zero membership and closure under arbitrary linear combinations. A nonhomogeneous linear equation typically gives an affine set. A curved or union-shaped set needs actual closure checks: the union of two axes contains zero but fails addition. Intersections of subspaces are subspaces; their union generally is not.

For a basis, coefficient extraction by an ordinary dot product is safe only if the basis is orthonormal. For a nonunit orthogonal basis divide by its squared norm. For a nonorthogonal basis, solve coupled equations or use a justified dual-basis method. Coordinate lists cannot be treated as Euclidean vectors without checking what geometry the chosen basis induces.

### 12.3 Norm identities and equality conditions

| Reasoning tool | Exact statement and domain | Equality / trap |
|---|---|---|
| Homogeneity | ‖αx‖=\|α\|‖x‖ in a normed space | The absolute value is required, including negative or complex scalars. |
| Cauchy–Schwarz | \|⟨x,y⟩\|≤‖x‖‖y‖ in an inner-product space | Equality means linear dependence over the specified field, including zero inputs. |
| Triangle inequality | ‖x+y‖≤‖x‖+‖y‖ | For nonzero vectors in inner-product geometry, equality requires positive real proportionality. Dependence alone is insufficient. |
| Reverse triangle | \|‖x‖−‖y‖\|≤‖x−y‖ | It often rejects impossible lengths before any coordinate calculation. |
| Real norm expansion | ‖x+y‖²=‖x‖²+2⟨x,y⟩+‖y‖² | Cross terms vanish only with orthogonality. |
| Complex norm expansion | The cross term is 2 Re⟨x,y⟩ | Pythagorean equality does not force the imaginary part to vanish. |
| Parallelogram law | ‖x+y‖²+‖x−y‖²=2‖x‖²+2‖y‖² | A failed instance rules out an inner-product-induced norm. |
| Real polarization | ⟨x,y⟩=(‖x+y‖²−‖x−y‖²)/4 | This displayed formula determines the real product; complex products need additional information. |

When solving an optimization problem, a bound is only half the solution. Use the equality condition to construct a feasible maximizer or minimizer, then verify the constraint. For example, a fixed-length linear-functional maximum comes from alignment with its coefficient vector. If that coefficient vector is zero, the objective is constant and every feasible vector is optimal.

Angles require two nonzero real vectors. The signed dot product distinguishes acute from obtuse; its absolute value instead gives the smaller angle between unoriented lines. The zero vector is orthogonal to every vector but has neither a unit direction nor a defined angle. For complex inputs, first choose an appropriate angle convention; never put a complex ratio directly into a real arccos formula.

### 12.4 Projection: verify the answer rather than trusting its appearance

Use this sequence for a line projection:

1. Confirm the direction b is nonzero. If it is zero, the target span is {0} and its projection is zero; the usual quotient cannot be used.
2. Compute the chosen inner product and squared norm consistently. Under first-argument conjugation, the coefficient is ⟨b,x⟩/⟨b,b⟩.
3. Multiply the coefficient by b to obtain the projected vector. A coefficient or signed scalar component is not itself the projected vector.
4. Subtract to obtain the residual and check its inner product with b is zero. This catches missing denominators and misplaced conjugation.
5. Check Pythagoras and compute the residual norm as the distance. For an affine line translate the target first and translate the foot back.

For a multidirectional span, verify that the proposed foot lies in the span and that the residual is perpendicular to **every generator**. These two properties characterize the unique orthogonal projection. Orthogonality to a single generator is insufficient if the target span has more directions.

If the generators are orthogonal and nonzero, sum the independently scaled components. If they are nonorthogonal, their Gram equations are coupled. If they are dependent, coefficient solutions can be nonunique while the projected vector remains unique. Projection onto a span is independent of the basis used to compute it.

The nearest-point proof is reusable: decompose the error to an alternative candidate into an orthogonal residual plus a within-span difference. Their squared norms add, and the second term is nonnegative. Equality forces the candidate to be the foot. This proof supplies uniqueness and is stronger than saying “the shortest line is perpendicular” without checking the target set and its geometry.

### 12.5 Orthonormal expansions and Gram–Schmidt

An orthogonal list is independent only when every member is nonzero. An orthonormal list already has that condition because all norms are 1. Inner products extract its coefficients directly, but expansion of an arbitrary ambient vector gives only its projection unless the list spans the whole space.

Bessel's inequality measures the captured energy: the sum of squared coefficient magnitudes does not exceed the squared norm. The shortfall is exactly the squared residual norm. Parseval equality holds for vectors in the spanned subspace; with a basis of the whole finite-dimensional space it holds for every vector. Use coefficient **magnitudes squared** for complex coordinates.

Gram–Schmidt subtracts the components along all retained directions before normalizing. Checking against only the most recent direction is inadequate. A zero residual is a dependence signal in exact arithmetic, not an invitation to divide by zero. Zero inputs and redundant generators must be skipped when constructing a basis of the input span. The output can depend on input order; the spanned subspace cannot.

The invariant is the best way to reason about an algorithmic variation: retained vectors are orthonormal and their span equals the processed input span. Verify both parts after subtraction, skipping, and normalization. In floating-point code, replace exact-zero tests only with a clearly justified scale-aware numerical policy; a small nonzero residual can represent a genuinely independent direction, as Problem 34 shows.

### 12.6 Orthogonal complements and affine distances

W⊥ is a subspace, and perpendicularity to a spanning list implies perpendicularity to all of W. The intersection W∩W⊥ is {0}. In finite dimensions, every vector has a unique W plus W⊥ decomposition, their dimensions add to the ambient dimension, and taking the complement twice returns W. Infinite-dimensional versions require additional hypotheses, so these finite statements must not be extended casually.

Orthogonal projection is linear, idempotent, and distance-nonincreasing. Idempotence means P²=P, not that every vector is unchanged; only vectors already in the target span are fixed. Its kernel is the orthogonal complement because those vectors have every projection coefficient zero. The complementary residual is itself projection onto W⊥.

For a hyperplane n·Z=d, the foot uses division by ‖n‖² while the scalar distance uses division by ‖n‖. Keep these denominators distinct. Use the absolute value only for unsigned distance. Verify foot membership by substitution. If the normal is zero, distinguish the whole-space equation from an inconsistent empty equation before interpreting the problem.

### 12.7 Three-dimensional cross-product and volume traps

The dot product produces a scalar and the cross product produces a vector. The standard cross product here is defined in oriented real three-space. Reversing input order negates it; distributivity is valid but reassociation is not. A cross-product magnitude is an area, and half that magnitude is the corresponding triangle area.

For a triangle, form two differences from the same vertex. For a tetrahedron, form three edge differences from the same vertex and divide absolute triple product by six. The signed scalar triple product records orientation; physical volume is its absolute value. Swapping two inputs changes sign while cyclic permutations preserve it.

Zero cross product means the pair is dependent, including zero inputs. Zero scalar triple product means the three-vector list is dependent; it need not mean all vectors are parallel. Degenerate triangles and volumes remain well-defined as zero even when direction or angle formulas become undefined.

### 12.8 Final answer audit

Before accepting a solution, ask whether its field and geometry are explicit, whether every divided quantity was shown nonzero, whether the answer has the correct type, and whether reconstruction or substitution verifies it. Check orthogonality with the actual inner product, not a different one. Check equality conditions separately from inequality statements. When an answer relies on a basis, identify exactly what space it spans. When a source formula conflicts with parity, positivity, or dimensions, derive the result independently instead of copying the conflict.

## 13. References and coverage limits

### Official course texts used

1. **Stanford University — Stephen Boyd. EE263, Introduction to Linear Dynamical Systems, Autumn 2007–08.** [Course lecture archive](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures.html). [Linear Algebra Review](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/lin-alg.pdf), all 31 slides reviewed; [Orthonormal Sets of Vectors and QR Factorization](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/qr.pdf), all 23 slides reviewed. Full QR factorization theory is deferred.
2. **University of Oxford — M1 Linear Algebra I, Michaelmas 2022.** [Official 2022–23 course page](https://courses.maths.ox.ac.uk/course/view.php?id=609), instructor Andrew Wathen. [Lecture notes](https://courses.maths.ox.ac.uk/pluginfile.php/25471/mod_folder/content/0/lecture_notes22.pdf?forcedownload=1), printed pp. 25–43 and 69–77 reviewed. The title page does not individually identify the note author. Row/column conventions and the complex inner-product convention were explicitly reconciled.
3. **University of California, Berkeley — Alexander Paulin. Math 54, Spring 2018.** [Official course archive](https://math.berkeley.edu/~apaulin/54(Spring%202018%20Videos%20and%20Notes).html). [Vectors in Rn](https://math.berkeley.edu/~apaulin/Vectors%20in%20Rn.pdf); [Inner Products, Length and Orthogonality](https://math.berkeley.edu/~apaulin/Inner%20Products,%20Length%20and%20Orthogonality.pdf); [Orthogonal Projections](https://math.berkeley.edu/~apaulin/Orthogonal%20Projections.pdf); [Inner Product Spaces](https://math.berkeley.edu/~apaulin/Inner%20Product%20Spaces.pdf). All four handwritten pages of each note were visually reviewed. Problem 30 independently corrects the parity error in the final polynomial example.
4. **Massachusetts Institute of Technology — Denis Auroux. 18.02SC Multivariable Calculus, Fall 2010.** [Official course](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/). [Dot Product](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/6082f2744b609da87e23f3d8feed0565_MIT18_02SC_notes_1.pdf), instructional pp. 1–2; [Components and Projection](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/f1b2876cbb4207c972b90eb04ebc861d_MIT18_02SC_notes_2.pdf), instructional p. 1; [Cross Product](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/38b6892f5294ed562cf3dedaf5b99ba4_MIT18_02SC_notes_3.pdf), instructional pp. 1–2. These written notes were read; videos were not required.

The selected texts were compared with candidates from CMU, Cambridge, Harvard, and an ETH-hosted teaching page. Some candidates received only index or sample review; they do not count toward the four genuinely reviewed sources. The separate source audit states exact review levels and access limitations. No assertion is made that every course worldwide was found or that this selection is globally optimal.

### What this chapter does and does not establish

The lesson covers the finite-dimensional vector-geometry reasoning patterns listed in its scope, including identified zero, dependence, nonorthogonal, weighted, and complex exceptions. It provides complete proofs of its core projection and inequality claims and worked examples mapped to its topic audit. Structural matrix theory, general basis-exchange arguments, infinite Fourier convergence, advanced numerical rank estimation, and other later-chapter topics are deliberately outside this boundary.

The 34 problems are an instructional selection, not every exercise published in the surveyed courses. They include course-derived types in new wording and original diagnostic extensions with full solutions. Archived Iranian entrance-exam booklets remain reserved for joint study in the final month. No claim of empirical calibration to those untouched papers is made here. The goal is to eliminate every identified in-scope error and omission; finite checks and source comparisons cannot prove literal perfection or guarantee future performance on every unseen question. This chapter remains a review draft until explicit student approval.
