# Whole-library animation revision — 6 October 2026

The student approved the sorting decision-led design (Site version 72) and explicitly authorized the same teaching clarity across all existing chapters. No new chapter was started.

## Scope and changes

- All 37 existing chapter pages include the new teaching player layer.
- 730 stored models and 4,002 exact checkpoints are annotated with operations, reasons, current state, state differences and subject-specific reading guidance. Where the saved model supports one, the exact predicate and result are derived and independently checked (236 explicit conditions).
- The 45 sorting models and their 1,194 checkpoints retain their approved data and dedicated renderer.
- The renderer repairs complete record identities and fixed slot indices, duplicate truth-table valuations, matrix operand/accumulator labels, event-time visibility, dependency flow on authored circuit wires, true pause/resume, reduced motion and printable checkpoints. Linked structures preserve their declared topology; bodies are not moved away from attached wires.
- Older gate-timing, vector and matrix editable laboratories had stale drawing element identifiers. Their references and the vector arrow marker now target the live elements.
- All 2,257 complete question bodies, written lessons, proofs and review notes are retained exactly, excluding script includes.

## Evidence

- `inventory.json`: per-model operations and per-chapter placements.
- `browser.json`: 730 models, 4,002 states, 37 pages, controls and mobile containment.
- `controls-browser.json`: additional reduced-motion-after-pause and printed-caption checks.
- `retention.json`: independent body and mathematical-payload comparisons against 5e43af9577a09e425d09809a9d13449122e04ddb.
- `live-reference-repairs.json`: legacy identifier repairs.
- `publication.json`: added only after source and deployment verification.

The scope is animation instruction and retained-content verification. This is not a fresh exhaustive audit of all course sources or a proof that every possible input or unseen examination question is covered. Saved checkpoints are exact; construction motion is illustrative. The revision stays awaiting student approval before a new chapter.

## Regeneration

Run `review_library_animation_teaching.py` after rebuilding raw model data to restore the reviewed teaching metadata, then re-run the browser and retention gates. Do not restore legacy player code from older baseline-repair scripts. The install/redesign scripts document a one-time migration and are not arbitrary repeatable rebuild commands. `finalize_library_animation_review.py` verifies content retention and produces the user-facing review; run it before publication, not after recording a successful publication.
