# Vector-geometry chapter quality audit

Date: 2026-10-01. Topic: `l_vectors`. Result: completed English **review draft**, pending explicit student approval. The previous `s_counting` chapter was approved and promoted to ready. No subsequent chapter was started.

## Instructional coverage matrix

| Reasoning pattern | Main teaching | Worked coverage / boundary checks |
|---|---|---|
| Points versus displacements, standard/nonstandard coordinates | 2.1–2.2 | 1–2; reconstruction and origin invariance |
| Span membership, redundancy, coefficient uniqueness | 3.1–3.3 | 2–3; explicit dependent coefficient family |
| Subspace versus affine set, closure failures | 3.1, 3.4 | 4, 24–25 |
| Norm, RMS, distance, polarization, real Pythagoras | 4.1 | 5, 7 |
| Angles and zero-vector qualifications | 4.4 | 6, 10; laboratory's zero direction |
| Cauchy–Schwarz proof, equality, triangle and reverse triangle | 4.2–4.3 | 8–10; optimization attainability |
| Weighted definiteness and invalid norms/forms | 5.1 | 11–12, 19, 23 |
| Polynomial/integral and sampling geometry | 5.2 | 13, 30–32 |
| Complex conjugation, inequality derivation, Pythagorean caveat | 5.3 | 14–15, 20 |
| Signed component, coefficient, vector projection | 6.1–6.2 | 16, 20; residual and norm checks |
| Orthogonal span versus coupled Gram equations | 6.3 | 17–19 |
| Orthonormal coordinates, Bessel/Parseval, incomplete bases | 7.1 | 33 |
| Gram–Schmidt invariant, dependent inputs, weighted inputs | 7.2 | 21–23, 34 |
| Orthogonal complements and projection structure | 7.3 | 26, 34 |
| Affine nearest point and hyperplane foot | 8 | 24–25 |
| Cross-product perpendicularity, Lagrange identity, area | 9.1–9.2 | 27, 29; exhaustive finite identity checks |
| Scalar triple volume, orientation, degeneracy | 9.3 | 28 |

Every listed in-scope reasoning pattern has a worked example, proof, or explicit counterexample. Section 12 contains a substantial decision-oriented review in complete sentences; it does not replace the main lesson. Four genuinely read courses from four universities are documented in `l_vectors-source-audit.md`. Exercise types are attributed and independently worded; copyrighted banks are not reproduced wholesale.

## Mathematical verification

- `verify_vector_examples.py` passed **7,886 assertions**. These include 729 pairs of three-dimensional vectors with coordinates in `{-1,0,1}`, norm expansions, parallelogram identity, squared Cauchy–Schwarz, cross-product perpendicularity/Lagrange identity, rational line projections, and candidate-distance decompositions.
- Specific worked calculations independently checked coordinate changes, the nonunit orthogonal plane projection, complex and weighted projection, Gram–Schmidt output, affine line and plane feet, cross-product area, scalar triple volume, and exact rational polynomial integrals.
- Core claims are proved in the lesson. Finite checks are regression evidence, not general proofs or certification of all possible questions.
- Identified source slips were reconciled: zero-angle restriction, unsigned angle convention, complex argument order, positivity qualifiers, and the odd-polynomial integral. The polynomial example is recomputed rather than imported.
- The course survey and independent derivations were checked against the chapter boundary. Later matrix theory and infinite Fourier convergence are explicitly deferred.

## Presentation and application verification

- Shared math typography renderer used; new norm, inner-product, perpendicular, integral, and complex symbols receive the STIX Two Math face. Unicode small indices are converted to semantic sub/sup markup; operator limits, roots, and fractions use MathML. Parentheses inside integral MathML have fixed size to avoid unintended stretching.
- `check_site_en.py` passed: **15 HTML pages**, English-only published text, local links, chapter statuses, IELTS stage/hour consistency, and math-glyph coverage across the existing chapter library.
- Visual QA discovered that Markdown table pipes in absolute-value notation could split and truncate three review rows. The pipes were escaped, all missing statement/equality text restored, and a content-preservation check added. The corrected review table was visually rechecked.
- Edge mobile QA passed at **390 px** with page width 390 and no display-formula overflow. All bundled prose, heading, and math fonts loaded. The library link opens the new draft.
- Projection laboratory passed six parameter states: horizontal, vertical, reversed orientation, scaled direction, near-perpendicular direction, and zero direction. Residual orthogonality and the minimum-plus-excess squared-distance identity were checked. Zero direction explicitly reports undefined quotient-based coefficients without dividing by zero.
- Print QA produced **37 A4 pages** using the browser's print layout. Representative pages were visually inspected for sums, roots, complex conjugates, corrected integral parentheses, Gram–Schmidt code, worked solutions, the complete review table, and English references. Mobile formula, problem-bank, review, and laboratory screenshots were also inspected. Code is kept together in print.

Temporary screenshots and the QA PDF are at `%TEMP%/l_vectors_qa`; source PDFs/scans remain temporary and are not redistributed. The delivery artifact is `dist/chapters/l_vectors.html`, with its laboratory and stylesheet. Browser printing is available; the temporary PDF is a QA artifact, not a separately edited canonical document.

## Remaining uncertainty and approval gate

No known in-scope mathematical error or rendering defect remains after these checks. This is not a claim of infallibility. The bounded source survey cannot establish that every worldwide course was evaluated. The worked bank cannot guarantee performance on all unseen questions. Archived Iranian papers were not read, classified, or solved; their empirical calibration is deferred to joint study in the final month. Full matrix/structural and infinite-dimensional topics remain outside this chapter's declared scope.

After delivery, the gate is `awaiting_user_approval`. The chapter's library status remains `draft` until the student explicitly approves promotion and continuation. An active draft must not silently become ready through its build script.


## Final existing-library revision — 2026-10-02

The full authored manuscripts, every worked answer, final rules, and diagram context were reread during the sixteen-chapter revision. Findings: Reviewed all three manuscripts, thirty-four complete solutions, complex conjugation, projection coefficients, equality cases, and numerical caveats. Corrected a grammatical error in Problem 7. All identified findings were corrected before rebuilding. The rebuilt chapter passed the recorded finite checks, desktop/mobile geometry, font loading, and print-style diagram-width checks. This is evidence of the performed review, not a universal correctness guarantee or a new full reading of every source course. See `LIBRARY_FINAL_REVIEW.en.md` and `library-review.json`.
