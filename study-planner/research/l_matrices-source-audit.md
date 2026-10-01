# Matrix chapter: source selection and reading evidence

Reviewed on 2026-10-01. Topic: `l_matrices`. No archived Iranian examination paper was opened or classified.

## Search boundary and comparison rule

The bounded survey contains seven identifiable university offerings with official written materials or an official written-material index. It does not enumerate every university course worldwide. Selection concerns this chapter's matrix-algebra boundary, not a global university ranking. Written coverage, inspectability, correctness under independent recomputation, proof value, and complementary instructional value were compared. Catalog access is explicitly distinguished from body reading.

| University / offering | Reading level | Strength and limitation | Decision |
|---|---|---|---|
| Stanford, Stephen Boyd, archival EE263 matrix primer, Lecture 2 | All 15 slides read as extracted text and compared with formulas | Precise dimensions, powers, transpose and inverse rules; proofs need expansion | Core: notation and algebra |
| Oxford, M1 Linear Algebra I, Michaelmas 2022, instructor Andrew Wathen | Printed pp. 8–13 and 21–24 read from the cached original PDF; later elimination material excluded from this chapter | Detailed definitions and entrywise proofs; identified slips corrected below | Core: foundations and proofs |
| UC Berkeley, Alexander Paulin, Math 54, Spring 2018 | All four handwritten Matrix Algebra pages rendered and visually read | Connects functions, basis images, composition, cancellation and transpose; inverse algorithm is a later boundary | Core: conceptual structure |
| MIT, Gilbert Strang, 18.06SC, Fall 2011 | All instructional pages of Multiplication and Inverse Matrices summary (3), Transposes/Permutations summary (2), and multiplication recitation problems (1) and solutions (2) read through official PDF extraction | Four multiplication views and compatible blocks; inverse recitation supports a independently derived nilpotent formula | Core: multiplication views and problem provenance |
| CMU, William Gunther, 21-241, Summer I 2014 | All four pages of Summary of Day 7 read through official PDF extraction | Quantities-times-prices application, coordinate selection, graph walks; supplements core without replacing a fourth university | Additional selected source for applications |
| Harvard, Oliver Knill, Math 21b, Spring 2023 | Two-page multiplication handout and two-page inverse handout read through official PDF extraction | Concise geometric examples; product-definition and reflection notation slips make it a weaker chapter backbone | Reviewed reserve; no exercise text reproduced |
| Cambridge, Stephen Cowley, IA Vectors and Matrices, Michaelmas 2010 | Official teaching index and introductory scope inspected; matrix chapter body not reviewed in this run | Broad rigorous scope, but index explicitly limits use and PDF states no redistribution | Surveyed reserve, not counted as a read course |

Four core courses from four universities were selected after comparison. CMU is used as a fifth, specific application source. No video or transcript inferred from a video was used. Failed local downloads (MIT timeouts, Harvard HTTP 403, CMU certificate chain) were not treated as successful reads; accessible official PDF text through the web reader supplied the reading evidence. No certificate validation was disabled.

## Independent corrections

- Oxford printed p. 21 defines strictly upper triangular using `i > j`; strict triangularity must also zero the diagonal, hence `i >= j`. The chapter uses the corrected definition and proves nilpotence by increasing index chains.
- Oxford printed p. 12 writes the left identity with the wrong dimension in one proof line. The correct identity for an m-by-n matrix is I_m A = A = A I_n.
- Oxford printed p. 22's zero-row inverse argument uses the first coordinate selector without ensuring the zero row is first. The general inverse algorithm is deferred, and no such proof is imported.
- MIT's upper-triangular inverse solution labels a row operation as R2 minus c R2 where R3 is needed, and labels the final inverse L rather than U. The chapter instead derives the inverse by the finite polynomial I − N + N², and verifies both products.
- Harvard's multiplication-definition line interchanges A/B and AB/BA; reflection entries also contain inconsistent angle notation. The chapter derives its geometric matrices from basis images and checks products independently.
- CMU's row-selection proof refers to a row in the place where a column is needed for the dot product. The chapter states e_i^T A and proves it by the entry formula.

## Synchronization map

| Chapter material | Reading anchors | Added original teaching work |
|---|---|---|
| Shapes, equality, sum, scalar operations | Stanford slides 2–5; Oxford pp. 8–10; Berkeley p. 1 | Semantic dimensions, matrix units and entry-recovery proof |
| Matrix-vector and four product views | Stanford slides 6–10; MIT multiplication summary pp. 1–2; Berkeley pp. 2–3 | One coherent rectangular example recomputed in all views |
| Composition, associativity, failure of scalar rules | Oxford pp. 10–13; Berkeley pp. 2–4 | Entrywise finite-sum proof, directional cancellation, quantified counterexamples |
| Transpose, inverse, structured matrices | Stanford slides 2 and 11–15; Oxford pp. 21–24; MIT transpose summary p. 1 | Conjugate-transpose convention, Hermitian decomposition, Gram and Frobenius proofs |
| Block products and nilpotent inverse | MIT summary p. 2; recitation Problem 3.2 and solution | Block dimension audit, finite-series derivation, noncommuting block counterexample |
| Applied dimensions and walk counts | CMU Day 7 pp. 1–2 | New numerical data, unit checks and inductive walk-count proof |
| Computation and advanced connections | Oxford p. 23 operation-count remark; core definitions | Original exact algorithm, cost conventions, chain-order comparison, perturbation calculation |

## Question provenance and reproduction boundary

The worked bank uses original questions and newly written solutions. MIT recitation's two in-scope mathematical problem types are identified individually and adapted; the triangular inverse is solved without the deferred Gaussian algorithm. Selected examples from the other courses are transformed into newly worded, independently solved problems. This is not a reproduction of all copyrighted exercises or every full course's problem bank. Exact source links and course/instructor identities accompany attribution. No source PDF or extracted full source text is redistributed in the repository.
