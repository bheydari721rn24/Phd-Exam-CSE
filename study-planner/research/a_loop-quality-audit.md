# Loop chapter quality audit

Date: 2026-10-01. Review state: **draft for student approval**. The prior `a_asym` chapter was promoted to ready following explicit approval. Only `a_loop` was drafted in this cycle. Archived Iranian examination booklets remain deferred until the final month.

## Source and scope

The four selected written university course texts and their actually read portions are documented in `a_loop-source-audit.md`. MIT grounds the word-RAM and dependent search example; Stanford grounds input-dependent insertion work; Princeton grounds exact operation frequency, pair/triple counts, and finite sums; Berkeley grounds the warning against inferring complexity from nesting alone. Each source was compared against the chapter's use rather than counted from a catalogue listing. The survey is bounded and makes no claim of worldwide completeness.

## Topic-to-problem coverage

| Reasoning pattern | Main lesson | Fully explained problem(s) |
| --- | --- | --- |
| Cost contract; body, update, and final guard | 2.1–2.3, 6.2 | 1, 3 |
| Strict and inclusive endpoints; zero-size case | 2.3 | 1, 2, 19 |
| Dependent triangular and triple regions | 3.1, 3.3 | 3, 4 |
| Nonconstant per-pass cost and power sums | 3.1, 4.3, 6.1 | 5, 10, 11, 16 |
| Linear outer and logarithmic inner | 4.1 | 6 |
| Geometric outer and linear inner | 4.1 | 7 |
| Multiples and harmonic sum | 3.2, 4.1 | 8 |
| Doubling from each starting index; summation-order exchange | 4.2 | 9 |
| Repeated squaring and log-log boundary | 4.4 | 12 |
| Early return, best/worst, feasible witnesses | 5.1 | 13, 14 |
| Insertion shifts versus comparisons; inversions | 5.2 | 15 |
| Branch-dependent cost and lower-bound feasibility | 5.3 | 17 |
| Two independent dimensions and allocation | 6.2 | 18 |
| Nontermination and overflow assumptions | 4.4, 6.3 | 10, 12, 19 |
| Exact discrete count versus integral estimate | 3.3 | 20 |

The high-yield section contains 24 complete decision rules and traps. Two original SVG diagrams depict the triangular index region and contrasting summation patterns. Formulas and indices pass through the shared STIX Two Math renderer; algorithm fragments use a separate monospaced font.

## Verification completed

- Rendered the 6,950-word English manuscript to an 18-page A4 equivalent HTML/PDF print view. The word count is descriptive, not a quality proxy.
- Local-link, English-only, chapter-status, font-file, and unstyled-math checks passed (`check_site_en.py`).
- Mobile browser at 390 px reported no document-width or formula overflow; the chapter link appeared in the library. A4 print output generated successfully. Visual inspection covered the opening page, the index-grid diagram, and the review/reference page.
- Independent finite enumeration checked strict pair/triple counts, endpoint formulas, geometric and harmonic loop counts, the reversing-summation identity, repeated squaring for small values, and insertion shifts against inversion counts (`verify_loop_examples.py`). These examples detect transcription mistakes but do not replace the general proofs in the lesson.
- References identify the exact written material used, and Stanford's instructor name was confirmed on its PDF cover page.

## Remaining limits

No finite source search can prove that the chosen four courses are globally optimal, and no note can guarantee perfect performance on every unseen question. Machine-specific operation costs, large-integer bit complexity, and expected values without a distribution are deliberately conditional. The chapter remains a review draft until the student explicitly approves it.


## Final existing-library revision — 2026-10-02

The full authored manuscripts, every worked answer, final rules, and diagram context were reread during the sixteen-chapter revision. Findings: Checked all twenty exact-count solutions, including powers of two, short-circuit comparisons, inversions, and zero-size cases. Removed rhetorical ambiguity in the geometric-sum solution. All identified findings were corrected before rebuilding. The rebuilt chapter passed the recorded finite checks, desktop/mobile geometry, font loading, and print-style diagram-width checks. This is evidence of the performed review, not a universal correctness guarantee or a new full reading of every source course. See `LIBRARY_FINAL_REVIEW.en.md` and `library-review.json`.
