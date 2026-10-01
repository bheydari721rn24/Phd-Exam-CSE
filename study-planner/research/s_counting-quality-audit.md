# Counting probabilities and independence: delivery audit

Date: 2026-10-01. Status: completed English review draft awaiting student approval. This audit records checks within a declared boundary, not a literal perfection or examination-performance guarantee.

## Scope and source gate

Four core courses from MIT, Stanford, UC Berkeley, and Oxford contribute genuinely read written instructional sections. The source-selection audit records nine candidate courses across eight universities, actual reading scope, unavailable bodies, selection reasons, and corrections. Metadata-only candidates do not count toward the four. Source PDFs were cached in a temporary directory, not redistributed in GitHub or the Site.

The complete manuscript has approximately 12,100 words in eleven sections. Its main teaching includes definitions, construction proofs, probability-law assumptions, advanced counterexamples, and boundary cases. The compact final review is a separate companion, not a substitute for that teaching. Archived Iranian master's and doctoral papers were not accessed in this chapter cycle.

## Instructional coverage matrix

| Reasoning pattern | Main explanation | Fully explained application or diagnostic case |
|---|---|---|
| Ordered objects, repetition, leading restrictions | Sections 2–3 | Problems 1–3 |
| Variable branching and bijections | Sections 2.3–2.4 | Problems 2, 3, 11, 33, 34 |
| Constant and unequal reporting fibers | Sections 2.4, 3.2–3.4 | Problems 4–7, 15; reporting diagram |
| Named and unnamed groups; distinct-label symmetry | Sections 3.3, 4.5 | Problems 6–8 |
| Adjacency blocks and separation gaps | Section 4.1 | Problems 9–11, 34 |
| Stars and bars; lower bounds; slack; upper bounds | Sections 4.2–4.3 | Problems 12–14; separator diagram |
| Labeled placements versus occupancy vectors | Section 4.4, 6.3 | Problems 15–17, 30 |
| Pigeonhole guarantees versus random collisions | Sections 4.6, 6.4 | Problems 21, 32 |
| Combinatorial identities and case counting | Section 5 | Problems 13, 33, 34; proofs of Pascal, Vandermonde, subset sum, hockey stick, and binomial expansion |
| Without-replacement and repeated-trial models | Sections 6.1–6.2 | Problems 3, 18–20 |
| Birthday bounds and fixed-position exclusion | Sections 6.4–6.5 | Problems 21–22 |
| Repeated race and geometric-series indexing | Section 6.6 | Problem 31; explicit finite-sum derivation |
| Independence, complements, disjointness, null cases | Sections 7.1–7.2 | Problems 23, 26 |
| Pairwise, largest-intersection, and mutual distinctions | Sections 7.3–7.4 | Problems 24–25; exact parity laboratory |
| Summaries of disjoint versus overlapping input groups | Section 7.5 | Problem 27 |
| Conditional selection and hidden shared type | Section 7.6 | Problems 28–29 |

All 34 question formulations and solutions are independently authored. They cover course-derived instructional types but do not pretend to reproduce all university exercise banks. The final section provides an eight-step decision procedure, a ten-row exact counting reference, eight independence rules, ten detailed trap/boundary explanations, and a method for error diagnosis.

## Mathematical checks

The written derivations were checked for compatible numerator/denominator sample spaces, uniformity assumptions, constant fiber size, disjoint case partitions, first forbidden upper-bound values, negative residual totals, zero-factor boundaries, independence strength, and positive conditioning denominators. Two explicit four-point laws distinguish the insufficiency of pairwise tests from the insufficiency of the triple condition alone.

`verify_counting_examples.py` passed independent finite enumeration of code restrictions, permutations, unlabeled pairs, reflection classes, adjacency restrictions, constrained integral vectors, placement occupancy, without-replacement sampling, weighted Bernoulli outcomes, collisions, and fixed points. Fixed-point counts were checked through six labels, including the empty permutation. Exact rational enumeration verifies hidden mixtures, overlapping group events, conditional selection, and weighted hashing.

The parity family was checked at five exact rational parameter values: minus one, minus one half, zero, one half, and one. All masses normalize, each marginal is one half, every binary pair cell is one quarter, and the triple factorization holds exactly at zero. These finite checks supplement the general proofs; they do not prove unrelated or unbounded claims.

## Presentation and integration

- `check_site_en.py` passed English-only assets, local links, chapter statuses, math-run coverage, semantic scripts, bundled font assets, and the existing plan/IELTS consistency checks.
- Headless Edge at 390 pixels reported a 390-pixel document width, loaded bundled fonts, and zero mathematical-display overflow. Newsreader headings, Source Sans 3 prose, and STIX Two Math notation remain distinct.
- Summation/product bounds are represented using MathML operator limits; other indices use semantic subscript/superscript markup. Source-specified stars and separators are drawn as an original vector figure with STIX labels.
- The actual browser laboratory passed four parameter states, checking normalization, all marginals and pairwise both-one probabilities, the triple probability, and the mutual-independence indicator. All 34 problem headings were present.
- The A4 browser-print rendering is 37 pages, with no replacement characters in extracted text. Representative final pages 7, 13, and 36 were visually inspected for the separator diagram, operator limits, and English references. Earlier representative solved-problem and review-table pages were also inspected before the operator-geometry improvement. No formal standalone PDF is delivered by this chapter cycle.
- The approved preceding `s_axioms` chapter is marked ready and its visible header says Approved chapter. The new draft is linked from the library. Its four actually reviewed courses were added to the study-facing source register with explicit review levels and scope limits.

## Residual limits and approval

The source pool is bounded; some official materials were unavailable, and most unrelated course sections were intentionally not reviewed. General group actions, unrestricted unlabeled partitions, generating functions, full conditional-probability theory, and limit distributions require other chapter boundaries. No promise is made of success on every unseen examination question. The chapter is submitted for student review; only explicit approval may promote it to ready and authorize the next chapter.
