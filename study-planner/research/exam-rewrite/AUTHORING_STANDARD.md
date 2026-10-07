# Exam-Focused Whole-Library Revision

The student rejected every previous problem bank and examination-note section on 2026-10-02. Previous approval is not evidence that those sections satisfy the new acceptance criterion.

Each revised chapter must connect definitions and derivations to actual calculations and conceptual decisions. Preserve deep valid proofs and add missing solution derivations; replace generic advice with formula-specific methods. Do not pad the lesson or replace it with a short formula list.

## Required question structure

- A mathematically specified problem in the chapter boundary.
- A calculation, formula selection, parameter classification, execution trace, combinatorial count, interpretation or conceptual multiple-choice decision.
- Four plausible alternatives for multiple-choice questions, with exactly one correct alternative under explicit assumptions.
- A complete step-by-step solution, explaining the necessary definition, substitution, intermediate calculation and conclusion.
- Diagnosis of plausible distractors, not just an answer letter.
- A range of foundational, intermediate and integrative difficulty.
- Original wording; course-derived methods must retain accurate source links and exercise-family attribution.

## Required examination-note structure

Each note names a concrete question trigger, the usable formula or exact implication, all needed conditions, a short calculation or counterexample, and the mistake that leads to a wrong alternative. General statements such as “check assumptions” are insufficient without the actual assumption and its consequence.

## Boundaries

The archive restriction remains active while the clarification is pending. Original practice questions must not be labeled as past national-examination questions or as empirically calibrated without inspection evidence. Existing source readings and their recorded boundaries can be reused; unread texts must not be added as reviewed sources. IELTS remains a separate pathway.

All revised notes remain English review drafts. The explicit request permits revising existing chapters across the library; it does not authorize starting new chapters or automatically promoting rejected notes to ready.

## Mathematical delimiter gate — 7 October 2026

Keep every matched fence pair inside one MathML row. A power or index of a
parenthesized expression must use that complete fenced row as its base; never
attach the script to the closing delimiter alone. Apply the shared
`math_fences.normalize_fences` normalization before rendering, and reject
unbalanced delimiter tokens with `delimiter_issues`. Preserve legitimate
half-open intervals and the intentionally one-sided brace of a cases table.

Before publication, check both real glyphs at desktop and mobile widths,
including formulas with nested scripts, fractions, matrices and sums. Include
stored animation formulas and dynamically inserted mathematical content.
Use `research/qa_math_delimiters.py` as the recorded whole-library regression;
keep formula token order, script payloads, lesson prose and complete problems
unchanged when making a typography-only repair. The shared browser layout also
normalizes incoming MathML, and its asset URL must change after a runtime fix.
