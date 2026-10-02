# Proof chapter review draft: quality audit

Date: 2026-09-29. Status: explicitly approved by the student; `ready`.

## Source and teaching coverage

- MIT 6.042J Chapter 1 §§1.1 and 1.5–1.8, Stanford CS103 *Guide to Proofs* relevant sections, UC Berkeley CS70 Summer 2024 Note 2, Cornell CS2800 Chapter 2 §§2.1–2.2, and ETH Zürich *Diskrete Mathematik* Chapter 2 §2.6.1–2.6.9 were compared as written texts. The original German ETH notes were used for mathematical patterns and independently explained in English. Oxford's 2025–26 Logic and Proof page was a supplemental comparison. The exact boundaries and each source's strengths and limitations are in `d_proof-source-audit.md`.
- The main lesson covers quantified proof obligations, exact domains, definitions and witnesses, forward direct arguments, lemma composition, contrapositive, formal negation, contradiction, exhaustive cases, iff, existence, dependent witnesses, uniqueness, and counterexample construction. These are taught with intermediate reasoning before the worked bank; the 24-rule final review is a distinct recall aid.
- The 22 fully worked problems include named university exercise *types* in new wording and solutions, plus original mixed problems. They cover zero divisors, equality endpoints, negative integers, sign-sensitive square roots, omitted hypotheses, quantifier dependency, and false universal statements.
- Induction and well-ordering are reserved for `d_induction`. The archived Iranian master's and doctoral exam booklets are deferred to joint study in the final month.

## Verification performed

- `research/verify_d_proof_en.py`: 22 sequential problems, 24 sequential final rules, English-only study text, equal table column counts, required fonts and diagram, finite checks of parity, divisibility, residues, witnesses, and selected counterexamples. These finite checks are regression aids, **not** proofs of universal claims.
- `research/check_site_en.py`: English-only site assets, local links, IELTS stages and hours, chapter statuses, and bundled font files.
- Edge HTTP/CDP at 390 CSS pixels: document scroll width 390, all three font files served with HTTP 200 and reported loaded, chapter screenshot visually reviewed.
- Edge A4 print: 18 nonblank pages, all 22 problem headings and final references in extracted text, no replacement characters. Teaching, diagram, final review, and references pages visually reviewed.

The survey does not establish a globally optimal choice among all courses. No written lesson can guarantee answers to every unseen exam problem. The review goal is to remove identified in-scope errors and omissions before student approval; any new objection should keep the chapter in `draft` until corrected.


## Final existing-library revision — 2026-10-02

The full authored manuscripts, every worked answer, final rules, and diagram context were reread during the sixteen-chapter revision. Findings: Corrected contradiction and unused-assumption guidance. Clarified the square-root domain and equality characterization. Restored each proof-route arrowhead. All identified findings were corrected before rebuilding. The rebuilt chapter passed the recorded finite checks, desktop/mobile geometry, font loading, and print-style diagram-width checks. This is evidence of the performed review, not a universal correctness guarantee or a new full reading of every source course. See `LIBRARY_FINAL_REVIEW.en.md` and `library-review.json`.
