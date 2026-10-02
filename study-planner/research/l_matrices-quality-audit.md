# Matrix chapter: quality and delivery audit

Completed 2026-10-02. Topic: `l_matrices`; delivery status: completed review draft, awaiting explicit student approval. The previously delivered `l_vectors` was explicitly approved and promoted to `ready` in this turn.

## Coverage review

The stated chapter boundary includes shaped arrays and equality; matrix units; addition and scaling; matrix-vector semantics and basis images; all four multiplication views; composition and finite-sum proofs; zero divisors and directional cancellation; transpose and complex adjoint; symmetric/skew and Hermitian/skew-Hermitian decomposition; Gram positivity and equality conditions; square orthogonal and rectangular isometric cases; inverse uniqueness and ordered inverse identities; two-by-two singular and nonsingular cases; diagonal and triangular structure; powers and finite nilpotent series; compatible blocks; permutations and elementary additions; cyclic trace; Frobenius geometry; Hadamard/Kronecker distinctions; exact classical cost, chain grouping, and perturbation terms.

Four core course texts from four universities were compared after a seven-offering bounded survey. A fifth, CMU, adds applications. Reading evidence, access limits, independent corrections, and section-to-source mapping are in `l_matrices-source-audit.md`. No catalog-only entry is counted among the five genuinely reviewed courses.

The teaching is followed by 36 fully explained problems and 50 complete-sentence examination rules. Both in-scope mathematical types from the MIT multiplication recitation are included with attribution, independently written solutions, and corrected notation. This is not an exhaustive reproduction of all full-course exercise banks. General elimination, rank classification, determinant expansion, eigendecomposition, and SVD remain separate scheduled chapters. Archived Iranian examination papers were not opened, classified, or solved.

## Mathematical verification

`verify_matrix_examples.py` passed **26,565 exact assertions**. It recomputes numerical products and answers; verifies both directions of sampled inverse formulas; checks triangular nilpotent inverse parameters on 125 triples; recomputes norms, permutations, trace counterexamples, complex self-products, idempotent powers, perturbation entries, and classical cost counts; independently enumerates graph walks; and checks transpose, trace, associativity and distributivity on all ordered pairs of 81 small two-by-two matrices, with a deterministic third matrix for the triple checks.

The finite tests support the explicit written proofs. They do not prove all universal claims by themselves and do not guarantee performance on unseen questions. The mathematical prose was reviewed for field assumptions, compatible shapes, side-specific cancellation, zero/nonzero conditions, and the distinction between exact algebra and floating-point output.

## Typography and content preservation

The manuscript uses the shared mathematical typography renderer plus chapter-local semantic MathML matrices and fractions. The rendered chapter has 139 matrix tables including the initial live-lab output. STIX Two Math is confirmed for both the MathML element and its cells. Newsreader headings and Source Sans 3 prose load from bundled fonts. Code uses the configured Cascadia Code / IBM Plex Mono / Consolas monospace stack.

During QA, ASCII adjoint stars inside inline HTML were found to trigger Markdown emphasis across formulas. They were replaced in rendering with the mathematical asterisk, the adjoint notation was visually rechecked, and the builder now rejects unexpected emphasis. A fourth-power Unicode glyph after a Greek base was converted to a semantic superscript. A partial inline formula was explicitly grouped to avoid mixed typefaces. The site-wide audit rejects residual unstyled math and Unicode small-index glyphs outside SVG/MathML.

`check_site_en.py` passed for **16 HTML pages**, including English-only study output, local assets and links, IELTS stages and hours, approved vector status, draft matrix status, and mathematical indices. The final result map is a scrollable table on mobile; no cell text is discarded. Diagrams retain readable labels through local horizontal scrolling. Code can scroll inside its own box instead of expanding the page. No underlines were added.

## Browser and print verification

`qa_proof_browser.py l_matrices` passed at a 390-pixel mobile viewport: document width and scroll width were both 390, all fonts were loaded, and maximum formula overflow was zero. The chapter link was present in the actual library. The laboratory was exercised in eight states, including zero shear, zero/half-turn rotation, negative parameters, a zero input, and extreme controls. Both composition outputs and their squared-distance commutator identity were checked. Source-labelled numerical comparisons remain available alongside the equal-scale SVG plot.

The browser produced a **44-page A4 print layout**. Sampled mobile displays were visually inspected for arrays, code, laboratory and review. Printed pages around transpose/adjoint notation, the nilpotent inverse solution, and final rules were rendered and visually inspected. The adjoint emphasis defect was corrected and the affected printed page rechecked. Print text had no blank pages or unexpanded matrix/fraction markers in the inspected extraction. QA artifacts and source caches remain in the system temporary directory and are not redistributed.

## Remaining limits and approval gate

No identified mathematical error or in-scope omission remains after these checks. The survey is bounded, the source exercise selection is documented, and later chapter topics remain explicitly deferred. Literal worldwide-course completeness, literal zero future errors, and success on every unseen exam question cannot be certified. The chapter is linked as a review draft and will be promoted only after explicit student approval. No next chapter has been started.


## Final existing-library revision — 2026-10-02

The full authored manuscripts, every worked answer, final rules, and diagram context were reread during the sixteen-chapter revision. Findings: Reviewed all three manuscripts, thirty-six solutions, rectangular/square distinctions, Hermitian identities, matrix norms, and conditioning. Replaced an unsupported backward reference with a self-contained exchange proof that n independent vectors in R^n span. All identified findings were corrected before rebuilding. The rebuilt chapter passed the recorded finite checks, desktop/mobile geometry, font loading, and print-style diagram-width checks. This is evidence of the performed review, not a universal correctness guarantee or a new full reading of every source course. See `LIBRARY_FINAL_REVIEW.en.md` and `library-review.json`.
