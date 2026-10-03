# Algorithm correctness — delivery quality audit

## Scope and content

The chapter covers contracts, mathematical and implementation models, backward assignment reasoning, sequencing, conditionals, consequence, array aliasing, verification conditions, invariants, reachable-state subtleties, termination, lower-bound search, insertion/merge sorting, three-way partition, division, Euclid, power, certificate verification and proof-method selection. Full greedy, dynamic-programming and graph algorithms are reserved for their scheduled chapters; this chapter supplies proof-method foundations and explicit certificate examples.

Four university written texts were read at the recorded page scope. The source audit separates four reviewed texts from screened or inaccessible candidates. Detailed theory is preserved alongside 54 worked questions: four authentic archive translations and fifty original/course-derived tasks. The final review has 74 complete, conditional rules, plus a complete problem-solving procedure.

## Scientific review priorities

Review focuses on hidden assumptions, exact checkpoint locations, duplicate and empty inputs, preservation during temporary storage, finite arithmetic, recursion measures, aliasing and feasibility versus optimality. Every multiple-choice problem has one intended answer under its stated domain and a derivation explaining other alternatives. Course-derived tasks use independent wording and declare provenance; no entire course exercise collection is claimed.

## Verification evidence

Exact independent finite-model checks and artifact checks are recorded in `a_correct-validation.json`, published as the chapter's validation evidence. The bounded searches test branch preservation and progress, not merely returned outputs. Corrupted implementations are checked against explicit small counterexamples. Numeric question answers are connected to stored selected alternatives. Native MathML, font families, formula fit, SVG label geometry, print behavior and the interactive laboratory are checked in a real browser, with results in `a_correct-browser-review.json`.

The completed run passed 353,842 assertion checks across the stated finite domains, including 5,544 sorted-array/target cases, 1,093 tagged sorting arrays, 3,279 array/pivot partitions, 2,880 division inputs, 6,400 gcd inputs, 13,628 power cases and all 65,536 pairs of eight-bit multiplication operands. This is a count of checks, not distinct independent theorems. Twelve numeric answer bindings connect independent calculations to the question alternatives; remaining symbolic statements and distractors received written derivation review.

The browser run checked all 54 solutions open at a 390-pixel viewport, all five figures for label containment and overlaps, print-style fit and restoration of solution expansion state. Math uses STIX Two Math and code uses JetBrains Mono. The laboratory passed duplicate, empty and deliberately stalling cases, and rejected unsorted and malformed input. Desktop, mobile problems, final notes, formulas and laboratory screenshots were visually inspected.

[Read the exact finite-model validation record](../evidence/a_correct/validation.json) and [the browser validation record](../evidence/a_correct/browser-review.json).

The finite domains and the exact counts are stated in the evidence rather than represented as an unbounded theorem proof. General claims rely on the written arguments and their assumptions. Browser checks cannot certify every printer or possible environment. No literal 100% scientific accuracy, universal course coverage or unseen-exam performance guarantee is asserted.

## Workflow

The user's explicit approval of the previous 22-chapter library is preserved in an approval ledger. This new chapter remains a draft until explicit approval. Study-progress selections are preserved. No learner examination is required now and no following chapter is started as part of this delivery.
