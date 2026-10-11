# Linear transformations: written-course selection and reading audit

## Candidate boundary and selection

The previously acquired vector-space course pool was re-evaluated for this chapter. Seven universities were screened: Oxford, MIT, Stanford, Berkeley, CMU, ETH Zurich and Harvard. Five universities have chapter-relevant written material actually read here. Four core courses were selected because their combined written scope includes abstract proofs, explicit coordinate direction, application geometry and inverse/recovery interpretation. Inventory screening is not counted as reading. This is a bounded comparison; exhaustive worldwide course evaluation or proof of a globally best four-course set is not claimed.

| Priority | Course | Actual reading | Contribution and limitation |
|---|---|---|---|
| Core, abstract structure | Oxford M1 Linear Algebra I, Andrew Wathen, 2022–23 | Native PDF pages53–67 in full, split into53–59 and60–67 to prevent output truncation | Linear maps, basis-image extension, kernel/image proofs, rank–nullity, representations, composition, changes of coordinates, similarity and transpose warning. The lecturer is credited as course lecturer, not unverified PDF author. |
| Core, geometric construction | MIT18.06SC, Gilbert Strang, Fall2011 | Session3.6 all four teaching pages, both exercise statements, both solution teaching pages visually read; Session3.7 all three teaching pages. Final license pages identified separately. | Geometric maps, derivative matrix, basis images, similar representations, lossless conversion and lossy compression. Two published exercises are independently reconstructed in the bank. |
| Core, recovery and applications | Stanford EE263, Stephen Boyd, Autumn2007–08, Lecture3 | Native pages5–13, covering slides3–9 through3–26, read in full | Attainable outputs, kernel ambiguity, left/right inverses, rank factorization, coordinates and conjugation. Gram identities are explicitly restricted to real matrices; complex versions require conjugate transpose. |
| Core, coordinate direction | Berkeley Math54, Alexander Paulin, Spring2018 | All eight scanned pages of Vector Spaces and Linear Transformations and Bases and Coordinate Systems, read visually at native render | Abstract linear examples, coordinate isomorphisms, directional transition matrices and augmented solves. Limited theorem depth is supplied by Oxford. |
| Additional comparison | CMU21-241, William Gunther, SummerI2014, Day24 | All four native pages read | Basis extension, function/matrix operators and image spanning. Errors and incomplete theorem statements prevent core selection. |
| Screened, not counted as a read chapter source | ETH Zurich Linear AlgebraHS2024, Bernd Gaertner and Robert Weismantel | Previously acquired PartI inventory evaluated against the current operator chapter | Vector-space background; not a replacement for this chapter's operator/coordinate proofs. |
| Screened, not counted as a read chapter source | Harvard Math21b2023, Oliver Knill, Lecture04 | Previously acquired two-page vector-space inventory compared for scope | Background on bases; insufficient current chapter depth. |

The manuscript's reference section contains exact official URLs. Acquisition hashes and native page counts are retained in acquisition.json. Reading evidence is recorded separately from download success.

## Corrections and reconciled conventions

1. Oxford page56 inverse proof repeats one input label in its final scalar-combination line; the proof in this chapter uses the two distinct preimages.
2. Oxford page57 Vandermonde example has an inconsistent exponent in the final column. The evaluation matrix here uses powers zero through the stated maximum degree.
3. Oxford page59 image-independence proof changes vector labels in its conclusion. The proof here consistently uses the images of the basis extension.
4. Oxford page62 contains a transposition/index convention inconsistent with the chosen column-coordinate equation. This chapter derives columns as output coordinates of input basis images.
5. MIT Session3.6 has column-index slips in the general basis-image notation. This chapter states the typed equation before listing columns.
6. Berkeley Coordinates page3 repeats the first basis subscript beside the second coordinate result. The second result is in the other basis, as its solve and the subsequent directional formula show.
7. CMU page1 labels a list longer than dimension as independent; it must be dependent.
8. CMU page2 calls three quadratics a basis of P3; they can form a basis of P2, not the four-dimensional P3.
9. CMU page2 differentiation has an incorrect codomain scalar label. A derivative is a function/polynomial, not generally a scalar.
10. CMU page3 places x mapped to2x among nonlinear examples; it is linear. Its basis-image extension theorem omits the condition that the extension agree with the prescribed images.

## Source-to-instruction mapping

- Sections2–7: Oxford proof spine with Berkeley abstract operators and Stanford fibers.
- Sections8–14: Berkeley coordinate arrows and Oxford matrix proofs with Stanford recovery interpretation.
- Sections15–16: MIT geometry with independently derived oblique projection and motion constraints.
- Sections17–18: MIT derivative/compression and Oxford evaluation; characteristic and fixed-mask boundaries independently derived.
- Sections19–24: Oxford transpose boundary and CMU matrix-space comparison; Sylvester, dual/adjoint and field counterexamples independently derived.
- Question bank: two MIT exercises independently reconstructed, eighty authored/computed extensions, and two explicitly revisited Iranian originals. Revisited originals are not new distinct archive questions. There is no unverified claim that every exercise ever issued by the selected universities is included.

## Coverage and uncertainty

Coverage is tied to the thirty-section declared scope, including proofs and special cases. Full spectral theory, orthogonality algorithms, numerical conditioning theory and functional analysis are intentionally outside this chapter. Independent exact computations and browser QA test specified cases, not all possible inputs or unseen examination performance. No literal100% accuracy or rank guarantee is made.
