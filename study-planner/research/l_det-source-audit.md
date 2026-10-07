# Determinants source-selection and reading audit

## Selected written university courses

Selection used chapter coverage, proof quality, identifiable course provenance, examples, geometry, and scientific consistency. Four distinct universities contribute genuinely inspected written course content. Inspection is scoped to determinant-relevant pages, not every page of every full course.

| Priority | University / instructor / course | Inspected scope | Contribution and limits |
|---|---|---|---|
| 1 | Oxford / Richard Earl / M1 Linear Algebra II, Hilary 2026 | PDF pages 5–21 | Definitions, multilinearity, uniqueness, operations, multiplicativity, permutation matrices, structured examples, adjugate, Cramer, basis-invariant linear maps. Page 16 printed indexing mistakes are corrected independently. |
| 2 | Cambridge / Stephen J. Cowley / Mathematical Tripos IA Vectors and Matrices, Michaelmas 2010 | PDF pages 74–84, determinant paragraph on 89, Appendix B on 148 | Signed geometry, permutation sign, transpose and product proofs, cofactors, inverse, computational cost. Read-only reference; source text, diagrams, and pages are not redistributed. |
| 3 | MIT / Gilbert Strang / 18.06SC Linear Algebra, Fall 2011 | Instructional pages 1–3 of sessions 2.5 and 2.6; 1–4 of session 2.7 | Properties, geometric intuition, cofactor explanation, Cramer, volume and tridiagonal recurrence. Printed formula and index errors are explicitly corrected. |
| 4 | UC Berkeley / Alexander Paulin / Math 54, Spring 2018 | All four scanned Determinants pages, visually read | Deletion/minor computation, checkerboard signs, row-operation algorithm and a complete four-by-four elimination example. Compact notes alone would not supply the whole chapter's depth. |

These sources complement rather than simply repeat one another. Original proofs cover additional structured identities and boundary cases after their prerequisites are taught. The chapter is not a stitched copy of source prose.

## Candidate pool and exclusions

Harvard Math 21b (Oliver Knill, Spring 2023), both determinant pages, was reviewed but not selected as a core. The printed Leibniz formula on page 1 includes an extra factor (-1)^(n+1); testing the identity matrix of even order exposes the error. The triple-product parenthesis is also unclosed. These defects were visually confirmed and were not transferred into the lesson.

CMU 21-241 Summer I 2014 (William Gunther) was screened through its calendar and advertised determinant PDF. That PDF actually contains linear-map notes, so the mismatched link does not count as a reviewed determinant course. The ETH-hosted module 110PMA207 notes have uncertain institutional course provenance; hosting alone does not make them an ETH course. Stanford SUMO notes are student-organization material rather than an identified instructor course. Their locations/provenance were screened, not represented as full course readings. This finite accessible pool does not support a claim to have evaluated every university course worldwide.

## Corrections and independent validation

1. Oxford PDF page 16 prints a11 a22 a23 in an identity-permutation term and repeats a23 in the displayed position (3,2). The correct identity term is a11 a22 a33 and the correct entry is a32. The general Leibniz definition, independent enumeration, and the earlier source formula all confirm the repair.
2. Oxford PDF page 7 correctly excludes Sarrus at n >= 4. Text extraction looked like n > 4; visual inspection prevented a false source-error allegation.
3. MIT cofactor summary page 1 prints a11 a23 a33 where the negative permutation term requires a11 a23 a32. It was visually checked against the displayed selected pattern and corrected.
4. MIT Cramer summary page 1 uses Cj1 instead of C1j for a diagonal product and includes an extra A in the final inverse statement. The lesson derives both adjugate identities with explicit indices and verifies products independently.
5. Physical area and volume are always absolute determinants. A signed-area expression is never presented as universally nonnegative.
6. Proofs do not divide by a zero pivot or extend an inverse formula to a singular matrix. Characteristic-two exceptions, order-one adjugates, singular rank cases, strict positivity boundaries, and rectangular dimensions are stated explicitly.

## Coverage mapping

| Chapter sections | Primary course anchors | Independent extension or correction |
|---|---|---|
| 2–7: definition, geometry, permutations, axioms, multilinearity and ledger | Oxford definitions and permutation section; Cambridge 3.7; MIT 2.5–2.6; Berkeley pages 1–4 | Characteristic-two caveat, simultaneous-row examples, explicit determinant ledger |
| 8–12: products, singularity, cofactors, adjugate and Cramer | Oxford 1.1–1.2; Cambridge 3.7.6 and 4.1–4.2; MIT 2.5–2.7; Berkeley page 4 | Rank of adjugate, order-one exception, consistency counterexample, corrected indices |
| 13–17: parameter and structured determinants | Oxford examples 23–24; MIT 2.6 tridiagonal recurrence; Cambridge permutation/operation framework | Schur proof, inversion-free rank-one identity, complete Vandermonde proof, singular parameter ranks |
| 18–22: Gram, special maps, positivity and derivatives | Cambridge geometry/orthogonality; Oxford linear-map determinants; MIT volume | Original Cauchy–Binet proof, complex conjugation distinction, proved positivity bridge, Jacobi/cofactor sensitivity |
| 23–27: computation, solutions and final retrieval rules | Cambridge elimination and Appendix B; Berkeley elimination; all four conceptual anchors | Exact-rational editable lab, 80 original solutions, 80 explicit condition-bearing checks, two authentic adaptations |

## Original examination pages

The repository is pinned to commit bdadf6e2c9cadc4772ae137a96a3da753c7cfd08. PhD CS 1404 Q32 (PDF page 8) and MSc CS 1405 Q44 (PDF page 10) were visually inspected from their original PDFs. All options remain in printed order. The first calibrates a determinant-versus-positivity trap; the second uses a triangular characteristic determinant. The additional determinant-six conclusion for Q44 is explicitly labelled as a derived extension, not a modification of the question. Answers are independently derived, not official answer keys. PDF hashes and checked adaptations are in l_det-authentic.json.

## Source fingerprints

Course PDFs are cached outside the repository and are not part of the published site. Recorded hashes identify the inspected snapshots, not the permanent availability of remote URLs.

| Source ID | PDF pages | SHA-256 |
|---|---:|---|
| oxford | 55 | `92edfc6618a734f6eb633d9c7d553126358ed42d85108bf6125ed1df8cd4128e` |
| berkeley | 4 | `2befee163cff3dd36bbcd756f204c48824511b8ae4b368c7fa5502e0b18a9b0c` |
| mit-properties | 4 | `aea16eae29ec03cfc3bda4d8c0019d55b56e839d490ecddde62b2e2caeda27bc` |
| harvard | 2 | `f75cb1d3e7f5a3cf055cc5b13e3c15ba0a383a4ffba65863f2f398e5d8bd9ebb` |
| cmu-advertised | 3 | `bedfd4efcdb242ba3ac488fd11754bfd502195a85e546b6d66ff8824b490b35f` |
| eth-hosted | 12 | `70dcd0a6fe4888d328d345a167f3774f16557f99f293a6a6f49bb0454b3183b9` |
| stanford-sumo | 69 | `9c568ba3b51187c7a9d16ea98cbfac01db1f45e810b42d7ff9ae90c05568eaaa` |
| mit-cofactors | 4 | `ee780a63031f19a66e87d248cc513feb5988489ec4c0542a05e41f6f1ee739c2` |
| mit-cramer | 5 | `fbb1d787e1a1da3b38189c4628c4040c6fdf7f8dac5c9142f825001718bf09c8` |
| cambridge | 148 | `e0c76cb317e0c457660f26dad0e0658d6048574a8f20de51152f2c706ecc9f02` |

## References

- University of Oxford — Richard Earl, M1 Linear Algebra II, Hilary 2026: [Official notes](https://courses.maths.ox.ac.uk/mod/resource/view.php?id=61510).
- University of Cambridge — Stephen J. Cowley, IA Vectors and Matrices, Michaelmas 2010: [Official notes](https://www.damtp.cam.ac.uk/user/sjc1/teaching/VandM/notes.pdf).
- MIT — Gilbert Strang, 18.06SC, Fall 2011: [Properties](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/5dd3f8ec0a398fd74264fef3fd591f81_MIT18_06SCF11_Ses2.5sum.pdf), [Cofactors](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/cc79f04d92ee282758780bac2ec5e403_MIT18_06SCF11_Ses2.6sum.pdf), [Cramer and volume](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/f6e46da0d783d8f9c0a25c407c76166a_MIT18_06SCF11_Ses2.7sum.pdf).
- UC Berkeley — Alexander Paulin, Math 54, Spring 2018: [Official determinant notes](https://math.berkeley.edu/~apaulin/Determinants.pdf).
- Harvard — Oliver Knill, Math 21b, Spring 2023, rejected core candidate: [Determinants](https://people.math.harvard.edu/~knill/teaching/math21b2023/handouts/lecture14.pdf).
- CMU — William Gunther, 21-241 Summer I 2014, mismatched calendar candidate: [Calendar](https://www.math.cmu.edu/~wgunther/241/m14/index.html).
- ETH-hosted — Lorenz Halbeisen, module 110PMA207, unverified institutional provenance: [Notes](https://people.math.ethz.ch/~halorenz/4students/linalg/linalgln.pdf).
- Stanford SUMO — student organization, not counted as an instructor course: [Notes](https://sumo.stanford.edu/pdfs/LinearAlgebraNotes.pdf).
