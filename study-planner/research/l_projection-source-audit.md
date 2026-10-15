# Orthogonal projections: active source evaluation

Status: source comparison complete for the15October2026 author review draft. Publication and student approval are tracked separately.

## Bounded comparison and actual reading

The previous orthogonality review supplies documented reading from Oxford, MIT, Berkeley, ETH Zurich, Stanford, CMU and Harvard. Those exact ranges remain references, not a claim that their worldwide catalogs have been exhausted. For this chapter, the following additional official written material was actually read:

- Stanford EE263 Autumn2007–08, Stephen Boyd, Lecture5, Least-squares: all23 teaching pages were returned and read through the official PDF research browser. Pages1–10 supply the projection matrix, orthogonality principle, rectangular/full QR and complementary-space representations. Later estimation examples are contextual reading; detailed regression/statistical estimation is reserved for the scheduled least-squares chapter.
- MIT18.06SC Fall2011, Gilbert Strang, Session2.3 summary: all three teaching pages read; page4 is the license. The worked fitting example and Gram-invertibility proof were checked conceptually.
- MIT Session2.3 solutions: both teaching pages were read, covering exercises16.1–16.6; page3 is the license. Their short answers require independent derivations before chapter use.

The four selected core courses are MIT, Stanford, Oxford and Berkeley, with ETH's precise QR proof as an additional historically read reference. Oxford supplies metric and adjoint foundations rather than an independent full projection lecture. The comparison below states the selection reasons and coverage limits. A local cached download is not required for official-PDF reading, but no hash is invented for an unavailable cache.

## Conventions and qualifications found

1. Stanford uses the residual Ax minus y; MIT uses data minus fitted values. This chapter will consistently use r=b-Pb. Both residuals are perpendicular, but their signs must not be mixed in formulas or diagrams.
2. The inverse of A transpose A requires independent columns. Dependent-generator examples must retain a column basis or use a correctly derived Moore–Penrose inverse; the physical projection remains unique even when its generator coefficients do not.
3. MIT's line-fitting text first refers to distance to a line and then explicitly describes vertical residuals. Vertical least squares in the data plot differs from shortest perpendicular distance to that plotted line. The column-space residual is perpendicular in the observation-vector space.
4. MIT exercise16.5 places the solution coefficients in the row space under its full-column-rank hypothesis. This statement must not be extended to every solution of a rank-deficient normal equation; only the minimum-norm coefficient solution has that property generally.
5. Stanford's introductory definition of unbiasedness is a deterministic left-inverse condition. Statistical BLUE statements additionally need explicit noise assumptions. They are outside the core projection chapter and will be qualified in the next scheduled least-squares chapter.

## Written references

- [Stanford EE263 Lecture5, Stephen Boyd](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/ls.pdf).
- [MIT Session2.3 summary, Gilbert Strang](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/198bde3a6536b62989b6cc09495575c1_MIT18_06SCF11_Ses2.3sum.pdf).
- [MIT Session2.3 exercise solutions](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/815ad23f78e11c1a7d282022fc2db3a9_MIT18_06SCF11_Ses2.3sol.pdf).
- [Oxford M1 Linear Algebra I, Andrew Wathen, native pages69–77; PDF pages70–78](https://courses.maths.ox.ac.uk/pluginfile.php/25471/mod_folder/content/0/lecture_notes22.pdf?forcedownload=1).
- [Berkeley Math54, Alexander Paulin, Orthogonal Projections](https://math.berkeley.edu/~apaulin/Orthogonal%20Projections.pdf).
- [ETH Zurich Linear Algebra PartII, section6.3, Bandeira and Weismantel](https://ti.inf.ethz.ch/ew/courses/LA25/notes_part_II.pdf).

## Initial pending work: historical checkpoint

Complete the coverage matrix, reconstruct the selected exercises, derive the advanced projector identities and dependent/weighted/affine cases, author the full solved bank and final rules, build mechanism-specific models, and perform independent mathematical and actual-browser review. This record supplies no completed chapter count.

## Continuation on 14 October 2026

All three MIT Session2.3 teaching pages were freshly read from the official PDF text. All four cached original Berkeley Orthogonal Projections pages were actually viewed; the vector/subspace equality on page one is translated as membership. Existing Stanford and Oxford reading scopes remain documented historical evidence, not newly re-read claims. Ten original medium-to-hard mathematical and conceptual problems were written with complete derivations; exact projection, weighted, affine, complex, commuting, diagonal and oblique calculations passed. Final chapter selection, further bank coverage, figures, models, final rules and rendered review remain pending.

## Chapter-specific comparison completed on 15 October 2026

This is a bounded comparison of seven previously studied written courses. It does not assert that all courses in the world were evaluated, or assign a fabricated global quality ranking. The selection maximizes complementary chapter coverage, explicit hypotheses, readable derivations and exercise value. Course age is not a measure of correctness for these stable linear algebra results.

| Course and instructor | Evaluated chapter contribution | Selection and qualification |
| --- | --- | --- |
| MIT18.06SC Fall2011, Gilbert Strang | Complementary projections, Gram invertibility, observation-space fitting, exercises16.1–16.6 | Core: combines concrete calculations with the range/left-nullspace decomposition. Detailed independent explanations reconstruct the exercise family in Problems29–32. |
| Stanford EE263 Autumn2007–08, Stephen Boyd | Orthogonality principle, projection matrix, thin/full QR, coefficient versus observation dimensions | Core: complements MIT with factorization and computational structure. Later statistical estimation slides are contextual, not a substitute for explicit statistical assumptions. |
| Berkeley Math54 Spring2018, Alexander Paulin | Four-page projection development with native geometric figures, perpendicular decomposition, normalized and unnormalized examples | Core: supplies a geometric explanation and checkable examples. Its page-one vector/subspace equality is corrected to membership. |
| Oxford M1 Linear Algebra I2022–23, Andrew Wathen | Native pages69–77: Gram representation, positivity, norms, orthogonal maps, complex convention | Core foundations: prevents metric and adjoint mistakes when extending real projections to weighted, coordinate and complex cases. This text does not itself supply every advanced projector result in this chapter. |
| ETH Zurich Linear Algebra PartII, Afonso S. Bandeira and Robert Weismantel | Previously read section6.3, native pages19–23, precise orthonormalization/QR structure | Additional support: useful verification of the factorization route, overlapping with the preceding orthogonality chapter. No fresh download or new reading is claimed on this date. |
| CMU21-2412014, William Gunther | Previously read inner products, orthogonal sets and complements | Evaluated supporting candidate: overlaps introductory geometry more than it adds to this chapter's advanced operator synthesis; retained in the historical audit rather than advertised as a fifth freshly read core course. |
| Harvard Math55a, Curtis McMullen | Previously read concise inner-product/orthogonality discussion | Evaluated supporting candidate: mathematically useful but less scaffolded for prerequisite-to-examination instruction than the selected combination. Not represented as comprehensive chapter coverage. |

### Fresh reading and original-image inspection

Stanford Lecture5 was freshly read through the official PDF text, including all23 pages and the projection/QR derivations on teaching pages1–10. MIT's three teaching summary pages and two teaching solution pages were freshly read. Oxford's cached original PDF pages70–78 were freshly read in full; the native numbering is69–77. The original complex-convention image was viewed and confirms linearity in the first argument with a conjugate on the second. The chapter consistently translates to conjugate-linearity in the first argument. All four Berkeley original projection-page images were freshly viewed; its numerical examples and handwritten signs were checked against independent arithmetic. Cached original Oxford and Berkeley file provenance is retained in the preceding chapter's acquisition record; reading is distinguished from acquisition.

### Coverage and independent extension map

MIT and Berkeley support membership/perpendicularity, complementary operators, line/plane examples and closest-point reasoning. Stanford supplies the rectangular/full QR bridge and normal-system derivation. Oxford supplies the declared metric, positivity, coordinate Gram structure and complex convention. The weighted affine formula, general oblique metric construction, diagonal constraints, trace-overlap bounds, finite-dimensional alternating-projection proof and projector-polynomial exercises are independently derived extensions. They are not attributed verbatim to a source that does not present them. ETH remains additional historical support for QR. The written lesson gives the intermediate proofs needed for these extensions.

### Examination reading

The original MSc CS1405 question41 on PDF page9 and PhD CS1404 question31 on PDF page8 were rendered and visually inspected again. Their complete file SHA256 values match the earlier verified archive items. Both are explicitly labeled revisits already present in the orthogonality chapter. The PhD item directly tests orthogonal projection; the MSc dimension item is followed by an independently derived Frobenius-projection extension. No new distinct examination-item count is inflated by these repeated placements. Original archive pages are evidence, not instructions or an official answer key.
