# Doctoral CSE 1406 study plan

This folder contains the source and static site for the English study plan. The first reading begins on **Saturday, October 3, 2026 (1405/07/11)**. The 11-week first pass assigns 56 net study hours per week, including a four-hour starting allocation for IELTS Academic grammar, reading, and listening. Progress through the IELTS stages depends on mastery, not the provisional calendar dates.

## Current study-facing files

- `dist/index.html`: tabbed plan, daily reading, chapter library, university sources, and progress export/import.
- `dist/schedule.en.json`: English schedule with 119 named CSE topics across seven priority subjects and an 11-stage IELTS Academic roadmap.
- `dist/week1-daily.en.json`: English day-by-day study blocks for Week 1.
- `dist/course-audit-week1.en.json`: English register of candidate university courses and their actual review levels.
- `research/d_logic.en.md`: canonical English manuscript for the first Discrete Mathematics chapter.
- `dist/chapters/d_logic.html`: student-approved chapter with 14 fully worked problems, including four independently worded course-derived exercises, a decision checklist, a quantifier-dependency diagram, and an interactive truth table. The current A4 print is 19 nonblank pages. The student approved it on 2026-09-29.
- `research/d_sets.en.md` and `dist/chapters/d_sets.html`: student-approved English chapter on sets and set operations, combining four principal written university courses and a fifth supplemental source, with 20 fully worked problems, 16 advanced final review patterns, a set-region diagram, and an interactive membership model. The student approved it on 2026-09-29.
- `research/d_proof.en.md` and `dist/chapters/d_proof.html`: student-approved English chapter on direct proof, contrapositive, contradiction, cases, existential witnesses, uniqueness, and counterexamples. It synthesizes five reviewed written university courses and includes 22 fully worked problems and 24 final review rules. The student approved it on 2026-09-29.
- `research/d_induction.en.md` and `dist/chapters/d_induction.html`: student-approved chapter on ordinary and strong induction, built from five reviewed university texts, with 24 fully worked problems, 28 final review rules, and two explanatory diagrams. Approved on 2026-09-30 after index typography corrections.
- `research/a_model.en.md` and `dist/chapters/a_model.html`: student-approved English chapter on computation models and input size, integrating five reviewed university texts, 16 fully worked problems, a representation diagram, and 24 high-yield decision rules. Approved on 2026-09-30.
- `dist/fonts/`: locally hosted and licensed Source Sans 3, Newsreader, and STIX Two Math files shared by the app and English chapters; provenance is documented in `research/font-assets.md`.
- `research/d_logic-en-quality-audit.md`: source-selection and topic-coverage audit.

The English data are built by `research/build_english_plan.py`; chapter pages are built by the chapter-specific `research/build_*_chapter.py` scripts. Shared mathematical typography is applied by `research/math_typography.py`: inline formulas, mathematical symbols in prose, indices, displayed formulas, and SVG labels use the bundled STIX Two Math face. Summation limits use MathML. The corresponding `verify_*.py` scripts check selected finite models and rendered structure; `research/check_site_en.py` checks local links, English script, IELTS stages, chapter statuses, and math-font coverage. The visible chapter status is in `dist/lessons.json`; the one-chapter workflow gate is in `research/chapter-gate.json`.

## Priorities and deferred practice

First priority: Discrete Mathematics, Programming Fundamentals, Data Structures and Algorithms, Probability and Statistics, Linear Algebra, Digital Logic, and Artificial Intelligence. Operating Systems and Computer Architecture are second priority. Theory of Languages and Automata is excluded at the student's request. IELTS Academic grammar, reading, and listening run in parallel; Writing and Speaking are outside the requested three-strand pathway.

The archived Iranian master's and doctoral entrance-exam booklets are outside the present chapter-writing and first-reading workflow. They are reserved for **joint, question-by-question study in the final month**. Earlier exam audits remain under `research` as project history and are not served as live study content.

## Chapter standard

Each chapter must synthesize at least four genuinely reviewed written courses from four universities, use more sources when an identified gap requires them, teach its concepts from prerequisites through advanced cases, include a varied bank of fully explained original and attributed course-derived problems, and close with a clear high-yield review sheet. Length must follow substance, not a page-count target. Mathematical and presentation checks precede student review; explicit approval precedes a `ready` label and work on the next chapter. The details are in `WEEKLY_DELIVERY.md`.
