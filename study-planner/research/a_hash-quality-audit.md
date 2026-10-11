# Hash-table chapter: scientific and visual audit

## Delivery status

Quality-reviewed English draft; student approval is not inferred. Publication status is recorded separately. The chapter contains twenty teaching sections, a complete-sentence summary, 82 fully worked problems, 80 final reasoning rules, an editable laboratory and exact written references. The previous 54 chapter pages retain their original byte hashes.

## Written-source synthesis

The documented candidate pool covers eight universities. Four core written courses were genuinely read: MIT 6.006 Spring 2020 Lecture 4, CMU 15-122 Lecture 12, Princeton COS226 Spring 2025 hashing slides and Algorithms section 3.4, and ETH Zurich Spring 2020 Lecture 9. Stanford and Cambridge provide two additional reviewed comparisons. The [source audit](a_hash-sources.html) records actual page ranges, inaccessible candidates and scientific corrections. Native acquisition hashes are distinguished from official web-text reading; unavailable native files are not assigned invented hashes. This is a bounded, disclosed search, not a claim to have inspected every course worldwide.

The synthesis reconciles equality versus hash equality, string-processing costs, size-biased bucket sampling, collision pairs versus per-query collisions, universal versus fully independent hashing, exact versus asymptotic probe formulas, marker reachability and uniqueness, modular cycle coverage, initialization costs and static-perfect construction. Published errors concerning birthday arithmetic, parameter ranges, double-hash steps and bucket zero are explicitly corrected.

## Mathematical and implementation checks

Independent verification passed 1,167 generated inputs and 70,392 checkpoint states, including 11,967 dictionary-operation contract checks. Separate finite-space enumeration checked occupancy, collision pairs, squared allocation and birthday probabilities. Ideal-probe expectations were checked across 40,318 permutation outcomes. Universal-family collision inequalities were enumerated for 66 fixed-pair/parameter cases; the restricted-parameter counterexample was verified. Modular cycle lengths, signed-square prime coverage and triangular power-of-two coverage were checked separately from the animation implementation.

Exact hand traces cover circular insertion, deletion markers, duplicate-value updates, marker reuse, backward shifting, nonpermuting route failure, double-hash query termination, fourteen-slot perfect allocation and cuckoo candidate obstruction. The lesson provides the proofs that extend beyond these finite observations. Saved intermediate repair states are distinguished from completed dictionary invariants. Rebuilding preserves record identity and values and recomputes placement under the new capacity.

## Problem and examination review

Eighty original or reconstructed problems emphasize exact fractions, modular routes, expectations, inequalities, counterexamples, amortized sequences and multi-operation design. Their complete solutions teach the reasoning, rather than provide answer letters alone. Reconstructed course exercise families use original data; they are not redistributed copies of complete course assignments.

Two authentic examination bridges were visually checked against their original PDF pages and retain archive commit and SHA-256 provenance: doctoral CE 1404 Q4, PDF page 3, and MSc CE 1404 Q65, PDF page 15. The doctoral pair-count answer is independently derived. The MSc design question contains unspecified augmentation choices; option 4 is justified with an explicit tree and hash-index construction, while a sufficiently augmented interpretation of option 3 can also be viable. A uniquely certified official key is not asserted. List-order tie semantics and the expected cost of the hash index are stated.

Every problem has an explicit visual decision. Eighteen problem companions illustrate routes or changing representations; parameter differences are prominently labeled. Algebraic proofs, contract arguments and expectation calculations remain complete written derivations without unrelated decorative animation.

## Visual and interaction review

Twenty-one concept-specific models contain 551 exact checkpoints and are mounted 35 times alongside relevant instruction and solutions. The layouts distinguish chains, circular probes, marker reuse, backward repair, square and triangular coverage, double-hash cycles, old/new routing contexts, two-level arrays, polynomial evaluation, bit filters, candidate relocation and displacement exchange. Fixed storage indices and stable record identities are separate.

Real Edge verification passed all stored checkpoint geometry with no recorded overlap or padding issue, and checked 69 chain connections against rectangle boundary ports. Native MathML uses STIX Two Math; heading, prose and code font files load correctly. The rendered chapter contains 566 native mathematical expressions; no bare closing-delimiter script base, zero-size parenthesis or underlined link was found. Probe motion, pause/resume, previous/next, seek, restart, before/result comparison, reduced motion and printable checkpoints passed. Fifteen editable laboratory cases and fourteen invalid-input preservation cases passed. Mobile page containment, library navigation and the week-four chapter link passed without runtime errors.

Initial geometry failures were repaired rather than suppressed: compact headings and column labels, chain glyph insets, probe padding, secondary-array footer separation and fixed-index visibility. Screenshots of chaining, tombstone updates and perfect placement were visually inspected after the repairs. Mathematical checkpoint data were retained during these layout changes.

## Scope and remaining uncertainty

Sequential word-key hashing is the primary model. Cryptographic internals, concurrent memory protocols, optimal independence thresholds, dynamic perfect-hash production engineering and arbitrary-size animation layouts are not claimed. Bloom-filter probability estimates are identified as approximations; its laboratory uses declared deterministic bit functions. Cuckoo relocation failure is separated from graph impossibility. Compact perfect placement deterministically searches verified parameters rather than pretending to sample the randomized theorem.

The audit provides evidence of the stated coverage and checks. It does not guarantee literal universal correctness or performance on every unseen examination question. Student mastery and timed examination performance require subsequent practice and feedback.

## Evidence

Research records: `a_hash-evidence/reading.json`, `mathematics.json`, `browser.json`, `problem-visual-decisions.json`, `concept-inventory.json` and `retention.json`. Source lecture links and exact course identities appear in the source audit and chapter references. Publication and GitHub commits are recorded separately from the quality checks.
