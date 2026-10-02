# Divisibility, modular arithmetic, and number theory: delivery audit

Date: 2026-10-02. Chapter d_number is an English review draft; d_invariants was explicitly approved and promoted during this turn. Only this one new chapter was authored.

## Mathematical and teaching review

The manuscript was reread alongside its problem bank and final rules. The central proofs cover signed division and uniqueness, Euclid's full common-divisor invariant and termination, Bézout coefficients, prime-factor existence and uniqueness, gcd/lcm exponent coordinates, complete integer solution families and nonnegative bounds, the two-denomination threshold, well-defined residue operations, inverse existence, reduced-modulus cancellation, complete linear fibers, ordinary and generalized CRT, totient and Euler's permutation proof, exact order and nonunit transients, modular-power correctness, divisor functions, factorial valuations, complete square-zero/square-one classifications, Wilson and the Fermat converse counterexample, additive cycles, and RSA recovery including nonunits.

The principal teaching text is substantial and separate from its review sheet. It contains 40 fully explained worked problems and 70 full-sentence examination rules, a conceptual summary, a method-selection table, and a reusable solution-writing procedure. Nine selected course exercise types are attributed in the source ledger; other questions are labeled original. Neither the entire world's course pool nor every course's full exercise collection is represented as exhaustively reviewed or reproduced.

Four actual written principal courses from four universities were read: MIT, Berkeley, CMU, and Cambridge. Eight candidates were compared, with screening and actual reading distinguished. Exact scopes, primary links, reconciled conventions, and local reference hashes are preserved. Reference PDFs were read only and remain outside the published authored lesson. Iranian examination archives remain deferred to the final month.

## Corrections made before delivery

- Euclid's halving statement now covers equality and early termination explicitly.
- CRT's canonical representative uses an inclusive upper endpoint of product minus one.
- Bézout's input condition explicitly means that both inputs are not simultaneously zero.
- A unit-base prime-power example no longer carries a misleading nonunit title.
- Nested powers now have real nested superscripts instead of an unrendered caret/brace expression.
- Main summation and product limits use native MathML with STIX Two Math.
- The laboratory verifies its Bézout identity by exact substitution before reporting results.
- Mobile form labels keep their mathematical letters on the label line, and wide diagrams explicitly invite horizontal inspection.

## Independent finite checks

The retained report `research/d_number-finite-check.json` records:

- 40,401 signed extended-Euclid pairs compared with Python's independent gcd and exact coefficient substitution.
- 37,200 modular-power inputs compared with built-in modular exponentiation, including modulus one, negative bases, and exponent zero.
- 28,830 actual JavaScript laboratory cases compared with independently enumerated Python solutions, images, and kernels.
- 6,084 generalized CRT systems compared with full residue enumeration, including incompatible conditions and modulus one.
- 3,043 Euler unit checks, 100 coprime coin pairs, and square-zero/square-one counts for 300 moduli.
- Direct independent checks of worked numerical answers, all RSA residues in the example, factorial valuations, root lists, and divisor counts/sums.

Finite checks are error detectors, not substitutes for the general proofs. A literal zero-error guarantee or performance guarantee on all unseen examination questions cannot be certified.

## Visual and interaction review

Four independently authored SVG diagrams teach the divisor lattice, multiplication fibers, the CRT coordinate bijection, and transient versus periodic powers. Every figure was captured and visually inspected. Browser bounding-box checks found no overlapping or clipped SVG text labels. Images, browser measurements, and exact artifact hashes are retained in `research/d_number-evidence`.

Desktop width 1280 and mobile width 390 were checked. The document has no mobile page overflow; formulas stay within their containers. Wide vector diagrams remain horizontally inspectable at legible text size, with an explicit swipe hint. All mathematical text, indices, native limits, and vector labels use STIX Two Math; prose uses Source Sans 3, headings Newsreader, and code JetBrains Mono. No new underlined text is introduced. All five laboratory presets were exercised; solution highlights agree with the counts. Blank and out-of-range inputs are rejected.

Print-media width 794 was inspected, with no diagram overflow and the expected math fonts. This verifies print styling; it is not a claim that a paginated PDF was generated or every printed page break was inspected. The site-wide English/link/status/typography check passes for 30 HTML pages.

## Delivery boundary

The chapter remains draft pending explicit student approval. The proposed next chapter is a_recurrence; it has not been started. This chapter's stated boundaries exclude analytic number theory, quadratic reciprocity, general discrete logarithms, advanced factorization, and practical cryptographic security engineering. A newly identified in-scope gap should be corrected in this chapter before promotion.
