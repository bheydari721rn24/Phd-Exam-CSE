# Correctness individual revision: reading and mathematical findings

Date: 14 October 2026. State: in progress; no new checked chapter edition is claimed.

## Material actually reviewed in this turn

The complete retained 27,506-character lesson, the bounded eight-university source comparison, all 74 historical examination rules, and all 54 live question stems and alternatives were actually read. Course-derived canonical questions are stored separately in `a_correct-questions.json`; the pure bank reader now includes that file and normalizes its doubled command backslashes without changing the mathematical meaning. Full source-derived answer rewriting and the new models have not yet been completed.

CMU 15-122 Lecture 2, Frank Pfenning, Contracts, 13 January 2011: all available official text across all 24 physical pages was freshly read through overlapping browser outputs, lines 0–625. Direct PDF retrieval failed; no new local original-diagram inspection is claimed. The lecture's final repaired program includes exponent zero, unchanged original arguments, the multiplicative invariant, a nonnegative exponent assertion, termination, machine-range behavior and two exercise statements. Its broad sentence describing C machine arithmetic as modular must not be applied to C signed-overflow semantics. The isolated word positive does not supersede the written nonnegative precondition.

Stanford CS161 Winter 2022 Lecture 2: all available official text of physical pages one through four was freshly read, browser lines 0–156. Later recursion-tree text through physical page seven was incidentally read in the same output but is not counted as a new complete-course reading. The insertion predecessor definition uses a strict inequality while its implementation shifts only strictly greater keys. For duplicate keys, the actual insertion position follows the last key less than or equal to the saved key, with a negative-one sentinel when none exists. The source's incomplete merge scaffold also lacks exhausted-head handling and initial pointer definitions. These are source qualifications, not executable code to copy literally.

MIT MCS selected physical pages 140–152 were acquired from the historical local PDF, whose hash matches the recorded source, but their text has not yet been freshly read in this revision. Cambridge direct retrieval failed; no fresh content-reading credit is claimed. Official browser reading is the next acquisition fallback. Therefore only two selected university scopes have fresh actual reading credit at this checkpoint; the four-source chapter criterion is not yet satisfied.

## Individually identified question issues and proof obligations

- Question 11 has a misleading old title about unreachable-state preservation. Its actual predicate x nonnegative is inductive but too weak to imply x=y. The replacement title should say that an inductive invariant can be insufficient. Question 12 supplies the different reachable-truth/noninductiveness mechanism.
- Question 16 distinguishes termination of each finite nondeterministic reset from a uniform runtime bound. No single unbounded execution is obtained by choosing an arbitrarily large finite reset. The rewritten stem must explicitly state a decrement by one while the second coordinate is positive and termination at (0,0); the vague phrase decreases to zero does not itself specify an exact transition count.
- Question 24 conserves the logical-hole multiset plus the saved key; the temporary physical array need not be a permutation.
- Question 29's exact partition trace returns boundaries (2,3), not a sortedness or stability promise. Question 30 needs a two-element trace explaining why advancing past the incoming unknown key fails.
- Question 36 has seven Euclidean remainder updates. Question 38 distinguishes four accumulator multiplications from six base squarings for exponent 45. The final unused square remains part of this displayed program and can violate a machine safety contract.
- Question 41 has wrapped product 64 versus exact residue 91 modulo 251. Reduction after a narrow overflow cannot repair the lost product.
- Question 45 passes local parent equalities and edge inequalities but its parent cycle never reaches the root. An actual attaining path is essential.
- Question 49's mass 7/8 not only fails to prove fullness; for a finite binary tree with the complete listed leaf set it refutes fullness. The final solution should explain this stronger consequence without changing the correct option.
- Question 52's equality invariant must be supplemented with index bounds before the exit implication can prove the final square. A value relationship alone does not establish termination or access safety.

## Remaining work

Finish fresh MIT and Cambridge scope reading and original source-image reconciliation. Reconcile the four authentic original examination items with actual PDFs. Rewrite all 54 solutions and strengthen complete final decisions, with subject-specific assignment/state, loop-region, logical-hole, partition, arithmetic and certificate models. Complete mathematical, rendered, control, responsive and print checks before marking this chapter a checked review draft. Continue under standing user authorization; the earlier one-chapter approval gate no longer stops ongoing revisions.
