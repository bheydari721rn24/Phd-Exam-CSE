# Sets chapter: English draft quality review

Reviewed on 2026-09-29. This is a review draft awaiting the student's explicit approval, not a ready chapter.

## Source and pedagogy

- Four principal written university courses from MIT, Stanford, Cornell, and Carnegie Mellon were compared at their relevant set-theory sections; UC Berkeley Note 0 served as a fifth foundational cross-check. Exact section-level review limits and a source-to-topic matrix are in `d_sets-source-audit.md`.
- The 20 worked problems cover every reasoning family in the source matrix. They include nested empty sets, domain-sensitive builders, two-inclusion proofs, distributive identities, symmetric difference, indexed families, quantifier order, Cartesian-product empty factors, power-set counterexamples, and overlap counting. The source-derived **types** are reworded and solved independently.
- The final review sheet has a seven-step decision procedure, a formula-and-trap table, and high-difficulty pattern notes. It complements the full proofs rather than abbreviating them.
- The Venn-region diagram and interactive three-bit set laboratory explicitly distinguish a finite membership model from a general proof.

## Verification performed

- `research/verify_d_sets_en.py`: 20 sequential problems; English-only manuscript and output; balanced table columns; exhaustive checks over all subsets of a three-element universe for the principal identities, power-set characterization, finite counting formulas, and the displayed counterexample.
- `research/check_site_en.py`: all local links, English-only study assets, approved d_logic status, draft d_sets link, IELTS stage and hour consistency.
- `node --check dist/app.en.js`: no syntax error.
- Edge browser: desktop top view and CDP-emulated 390-pixel mobile top view inspected; mobile document width equaled viewport width.
- Edge A4 print: 16 pages, every page nonblank, 20 problem headings, readable mathematical symbols in extracted text. Pages with key formulas and references were visually inspected. Print stylesheet hides input controls while retaining the model output.

The exhaustive finite check is a countermodel search and regression aid, **not a proof** for arbitrary sets. The written elementwise proofs supply the general claims. Archived Iranian master's and doctoral examination booklets remain deferred to the final month by instruction. A literal claim of perfect coverage of every possible future examination question is not verifiable.
