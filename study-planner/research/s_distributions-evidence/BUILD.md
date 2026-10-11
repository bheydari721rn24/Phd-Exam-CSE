# Reproducible chapter build

Run from the study-planner repository. Scripts affect only the new chapter, its evidence, its review pages and its library entry.

1. Run write_s_distributions_bank.py to recreate the first 43 questions.
2. Run extend_s_distributions_bank.py once to complete the 85-question bank.
3. Run polish_s_distributions.py to apply reviewed notation and wording.
4. Run normalize_s_distributions_review.py, prepare_s_distributions.py and prepare_s_distributions_renderer.py.
5. Run render_s_distributions.py.
6. Run verify_s_distributions.py and qa_s_distributions_browser.py. Inspect representative retained screenshots.

The source acquisition script records hashes and access outcomes, not automatic reading claims. Actual reading ranges are recorded in reading.json and the source audit. The one-time completion helper advances the gate and therefore must not be rerun after the handoff. Rebuilding a delivered chapter must preserve its student-review status and compare earlier chapter hashes.
