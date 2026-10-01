# Vectors: written-course selection and reading audit

Reviewed 2026-10-01. Chapter: `l_vectors`. Archived Iranian exam papers were not accessed.

## Search boundary and ranking

The bounded survey examined eight candidate course offerings associated with seven universities. This is an accessible official-text survey, not an exhaustive inventory of every course worldwide. Ranking used chapter fit, inspectable mathematical content, proof depth, geometry, exercise utility, and the ability to reconcile notation. University reputation alone was not a selection rule.

| Rank / decision | University and offering | Actual reading | Reason |
|---|---|---|---|
| Core 1 | Stanford, Stephen Boyd, EE263, Autumn 2007–08 | Linear Algebra Review, all 31 slides; Orthonormal Sets of Vectors and QR Factorization, all 23 slides | Strongest computational bridge between orthonormal coordinates, projection, and Gram–Schmidt. Matrix factorization beyond the chapter boundary is deferred. |
| Core 2 | Oxford, M1 Linear Algebra I, Michaelmas 2022; course instructor Andrew Wathen | Notes: printed pp. 25–43 and 69–77, corresponding to PDF pp. 26–44 and 70–78; title and syllabus checked | Precise definitions, vector/coordinate distinction, real inner-product axioms, Cauchy–Schwarz proof, complex conventions. Notes do not identify an author on their title page; Wathen is credited as course instructor. |
| Core 3 | UC Berkeley, Alexander Paulin, Math 54, Spring 2018 | Four handwritten PDFs, all four pages each: Vectors in Rn; Inner Products, Length and Orthogonality; Orthogonal Projections; Inner Product Spaces | Actual scans were rendered and visually read, not treated as empty extracted text. Excellent geometric progression, nonunit orthogonal bases, polynomial geometry. One worked integral was independently corrected below. |
| Core 4 | MIT, Denis Auroux, 18.02SC, Fall 2010 | Dot Product, instructional pp. 1–2; Components and Projection, instructional p. 1; Cross Product, instructional pp. 1–2. Attribution pages also checked | Clearest geometric interpretation of signed components and 3D area. The cross-product magnitude proof omitted in the source is supplied independently in the chapter. |
| Rejected core | CMU, William Gunther, 21-241, Summer I 2014 | Day 3 vector sections; all pages of Day 4; Day 17 and Day 20 bodies sampled/read through official web PDF extraction | Relevant content exists, but the extracted Day 4 norm/triangle formulas contain apparent slips; Day 17's body is diagonalization despite its index label. Rejected in favor of clearer core texts; no extracted anomaly is presented as a visually verified source erratum. |
| Reserve, incomplete body access | Cambridge, Stephen J. Cowley, IA Vectors and Matrices, Michaelmas 2010 | Official course index and syllabus; direct notes access failed with certificate/HTTP retrieval errors | Suitable syllabus but inaccessible body in this environment; not counted as read or used for proofs. |
| Reserve, metadata/sample only | Harvard, Oliver Knill, Math 21b, Spring 2023 | Course index and indexed Lecture 12 sample | Relevant geometry, but no full body review in this audit. No claim that this source is inferior or fully read. |
| Excluded identity | ETH-hosted Harald Lorenz teaching page, Module 110PMA207 | Official-hosted index only | Hosting at ETH does not establish that the offering is an ETH-taught course. Not counted as a reviewed ETH course. |

## Reconciliation and independent corrections

1. Oxford uses row-coordinate notation in parts of its notes and a complex inner product linear in the **first** argument. This chapter consistently uses column interpretation and a complex product conjugate-linear in the **first** argument. Consequently, the projection coefficient here is `<b,x>/<b,b>`. These are convention changes, not source errors.
2. Stanford Review slide 30 includes a negative right angle while slide 29 defines an unsigned arccos angle. This chapter defines that angle in `[0, pi]`; orthogonal nonzero vectors have angle `pi/2`. Zero vectors remain orthogonal algebraically but have no angle or unit direction.
3. Berkeley Inner Product Spaces p. 4 claims a nonzero integral for `x^3(x^2-1/3)` over `[-1,1]`. The integrand is odd; its integral is zero. Thus the projection of `x^3` onto `span(1,x^2)` is zero. The chapter explains and solves this independently. The source's orthogonalization `x^2-1/3` and squared norm `8/45` are correct.
4. Oxford's positivity lines in Definitions 200/218 and norm Proposition 205 must be read with the nonzero-vector qualification. The chapter explicitly states strict positivity only for nonzero vectors. Example 108's printed basis contains a coordinate inconsistency: `(0,2,-1)` does not satisfy `x+2y+z=0`; the independently derived correct second vector is `(0,1,-2)`. Neither slip is imported.
5. Oxford Example 208 requires care with negative frequencies: `cos(-mx)=cos(mx)`, so distinct signed integers alone do not ensure orthogonality. The chapter's finite trigonometric example uses distinct **positive** frequencies and handles the constant separately. Infinite Fourier convergence is outside scope.
6. MIT's determinant-shaped cross-product mnemonic is not a determinant with scalar entries. The chapter defines the coordinate formula first and derives perpendicularity, the Lagrange identity, and area before using the mnemonic.

## Source-to-content map

| Chapter content | Sources compared | Independent additions |
|---|---|---|
| Vectors, coordinates, span, independence | Berkeley Vectors; Stanford Review 2–8, 23–24; Oxford 25–43 | Zero space, affine distinction, subspace counterexamples, coordinate uniqueness proof |
| Norms, dot products, angles | All four; Oxford 69–73 | Equality classifications, zero/complex exceptions, reverse triangle, norm counterexamples |
| Projection and best approximation | MIT Components; Berkeley Projections; Stanford QR | Complete residual proof, nonorthogonal Gram equations, affine line/plane derivation |
| General inner products and complex vectors | Oxford 69–77; Berkeley Inner Product Spaces; Stanford conventions | Weighted positivity by completing squares, sampling degeneracy, conjugate convention translation |
| Orthonormal coordinates, Gram–Schmidt | Stanford QR; Berkeley Projections; Oxford 75 | Dependent-input invariant, numerical distinction, weighted and polynomial worked examples |
| 3D area and volume | MIT Cross Product; Oxford geometric basis perspective | Coordinate proof of Lagrange identity, scalar triple volume, nonassociativity and degenerate cases |

## Exact official links

- MIT course: https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/
- MIT Dot Product: https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/6082f2744b609da87e23f3d8feed0565_MIT18_02SC_notes_1.pdf
- MIT Components: https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/f1b2876cbb4207c972b90eb04ebc861d_MIT18_02SC_notes_2.pdf
- MIT Cross Product: https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/38b6892f5294ed562cf3dedaf5b99ba4_MIT18_02SC_notes_3.pdf
- Stanford course/archive: https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures.html
- Stanford Review: https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/lin-alg.pdf
- Stanford QR: https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/qr.pdf
- Berkeley course: https://math.berkeley.edu/~apaulin/54(Spring%202018%20Videos%20and%20Notes).html
- Berkeley Vectors: https://math.berkeley.edu/~apaulin/Vectors%20in%20Rn.pdf
- Berkeley Dot: https://math.berkeley.edu/~apaulin/Inner%20Products,%20Length%20and%20Orthogonality.pdf
- Berkeley Projections: https://math.berkeley.edu/~apaulin/Orthogonal%20Projections.pdf
- Berkeley Inner: https://math.berkeley.edu/~apaulin/Inner%20Product%20Spaces.pdf
- Oxford course/instructor: https://courses.maths.ox.ac.uk/course/view.php?id=609
- Oxford notes: https://courses.maths.ox.ac.uk/pluginfile.php/25471/mod_folder/content/0/lecture_notes22.pdf?forcedownload=1
- CMU index: https://www.math.cmu.edu/~wgunther/241/m14/index.html
- Cambridge index: https://www.damtp.cam.ac.uk/user/sjc1/teaching/
- Harvard sample: https://people.math.harvard.edu/~knill/teaching/math21b2023/handouts/lecture12.pdf
- ETH-hosted index: https://people.math.ethz.ch/~halorenz/4students/LinAlg.html

Only course sections actually reviewed are credited. Downloaded PDFs and rendered source scans are temporary reading aids, not redistributed site assets. Chapter explanations, proofs, diagrams, and worked problem statements are independently written. Course-derived problem *types* are attributed; source exercise banks are not copied wholesale.
