# Probability axioms chapter: quality and coverage audit

Date: 2026-10-01. Status: completed English review draft, awaiting student approval. The approved a_loop chapter is ready. Only s_axioms was authored in this cycle. Archived Iranian entrance-exam booklets were not accessed or used.

## Source review

The source-selection register records a bounded candidate survey, actual text-review depth, access failures, and selection reasons. Four core written texts from MIT, Stanford, UC Berkeley, and ETH Zurich were genuinely read in their relevant portions. Oxford is a fifth supplementary source for the union-bound application. Source differences were reconciled explicitly: finite versus countable additivity, singleton masses versus general measures, restricted measurable domains, and incomplete informal notes. The review does not claim that entire university courses or every course worldwide were read.

## Coverage matrix

| In-scope reasoning pattern | Main lesson | Fully worked problems |
|---|---|---|
| Outcome/event distinction, verbal translation, inclusive versus exclusive alternatives | 2.1–2.2 | 1, 9 |
| Induced law and unequal coarse categories | 2.3 | 2 |
| Nonnegative normalized finite law | 4.1, 5.1 | 3, 6 |
| Sigma-algebra closure, atoms, and restricted information | 3.1–3.2 | 4, 5 |
| Complement, monotonicity, one-sided differences | 4.2 | 6, 18, 20 |
| Two-event identities and sharp feasibility | 4.3, 4.5 | 6–9 |
| Three-event inclusion–exclusion and joint feasibility | 4.3 | 10, 11 |
| Dependence-free union bounds and sharp reliability bounds | 4.4 | 12, 23 |
| Countable weighted laws, series normalization, and tails | 5.1 | 14–16 |
| Uniform continuous law and area | 5.2 | 17, 19 |
| Null versus empty, almost sure versus exhaustive | 5.3 | 13, 18, 19, 22 |
| Mixed atomic/continuous law | 5.3 | 13, 22 |
| Symmetric difference and probability stability | 4.5 | 9, 20 |
| Increasing/decreasing continuity | 6.1–6.2 | 21, 22 |
| Liminf, limsup, and invalid limit interchange | 6.3 | 24 |
| Summable failures and the first Borel–Cantelli implication | 6.4 | 23, 24 |

The lesson supplies definitions, proof steps, assumptions, counterexamples, and boundary cases separately from the concise review. The 24 original problems have explained solutions. The 28 final decision rules include an assumption-aware formula map. Two original SVG diagrams show coarse coin reporting and continuous area; the four-atom interactive model rejects infeasible overlaps and reports negative implied regions rather than silently clamping values.

## Mathematical audit

- Checked disjointness and measurability in every additivity application. Derived empty-set mass before obtaining finite additivity.
- Checked the induced-law domain and preimage preservation of event operations.
- Derived two- and three-event identities by membership regions and the finite general formula by the binomial cell coefficient. No infinite alternating extension is asserted.
- Proved the two-event overlap interval both necessary and sufficient using four nonnegative masses.
- Derived countable subadditivity by disjointification; no independence assumption was imported.
- Derived monotone continuity using disjoint increments and complements. Derived liminf/limsup inequalities via tail infima and suprema.
- Checked both mixed-law components, atomic endpoints, countable null unions, and the distinction from uncountable unions.
- Checked the telescoping and geometric sums, the area complement, the reliability bound, and the smallest summable-tail threshold m = 9.
- Checked the dyadic counterexample's half-open endpoints, finite level sizes, infinitely-often event, eventually-always event, and divergent total probability sum.
- `verify_probability_examples.py` passed 25,266 exact rational finite-model and feasibility checks, including independently enumerated event masks and the eight-region three-event example. Finite checks are transcription safeguards; the infinite results retain written proofs.

## Presentation and application checks

- The builder joins the main lesson and problem/review manuscript, normalizes mathematical text and semantic indices through the shared renderer, and emits the chapter's English HTML.
- English-only, local-link, library-status, bundled-font, semantic-index, and unstyled-math checks passed across all 13 HTML pages.
- Edge browser checks at 390 px passed: document width equals viewport width; displayed formulas have zero horizontal overflow; bundled prose, heading, and STIX Two Math fonts load; the chapter link appears in the library.
- The laboratory produced the expected 25%, 40%, 20%, 15% starting masses and rejected an overlap of 5% because the neither region would have mass -5%. It restores the valid default before printing.
- A4 print output is 27 pages, with no replacement characters found in extracted text. Visual inspection covered the opening/mobile layout, the laboratory/mobile layout, the printed inclusion–exclusion proof, the printed laboratory and first problem, and the printed high-yield review. The long general inclusion–exclusion equation was split into two readable lines to remove mobile overflow.
- The final main/proof text was expanded where tail-limit reasoning needed explicit intermediate inequalities. Superscript complements and atom counts use semantic markup rather than ad hoc small Unicode letters.

## Remaining boundaries

The chapter deliberately reserves counting, conditional probability, developed independence theory, random variables, expectation, measure construction, and converse Borel–Cantelli results for their own boundaries. Exam-archive coverage is unassessed under the student's final-month policy. The reviewed sources and audits cannot establish worldwide course optimality, literal universal coverage, or guaranteed performance on every unseen question. Student approval is required before promotion from review draft to ready and before the next chapter starts.
