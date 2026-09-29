# Doctoral CSE 1406 study plan

This folder contains the source and static site for the English study plan. The first reading begins on **Saturday, October 3, 2026 (1405/07/11)**. The 11-week first pass assigns 56 net study hours per week, including a four-hour starting allocation for IELTS Academic grammar, reading, and listening. Progress through the IELTS stages depends on mastery, not the provisional calendar dates.

## Current study-facing files

- `dist/index.html`: tabbed plan, daily reading, chapter library, university sources, and progress export/import.
- `dist/schedule.en.json`: English schedule with 119 named CSE topics across seven priority subjects and an 11-stage IELTS Academic roadmap.
- `dist/week1-daily.en.json`: English day-by-day study blocks for Week 1.
- `dist/course-audit-week1.en.json`: English register of candidate university courses and their actual review levels.
- `research/d_logic.en.md`: canonical English manuscript for the first Discrete Mathematics chapter.
- `dist/chapters/d_logic.html`: student-approved chapter with 14 fully worked problems, including four independently worded course-derived exercises, a decision checklist, a quantifier-dependency diagram, and an interactive truth table. The current A4 print is 19 nonblank pages. The student approved it on 2026-09-29.
- `research/d_sets.en.md` and `dist/chapters/d_sets.html`: English review draft for sets and set operations, combining four principal written university courses and a fifth supplemental source, with 20 fully worked problems, a detailed high-yield review sheet, a set-region diagram, and an interactive membership model. It awaits student approval.
- `research/d_logic-en-quality-audit.md`: source-selection and topic-coverage audit.

The English data are built by `research/build_english_plan.py`; chapter pages are built by `research/build_english_chapter.py` and `research/build_sets_chapter.py`. `research/verify_d_logic_en.py` and `research/verify_d_sets_en.py` independently check selected finite models and the rendered structure; `research/check_site_en.py` checks local links, English script, IELTS stages, and chapter statuses. The visible chapter status is in `dist/lessons.json`; the one-chapter workflow gate is in `research/chapter-gate.json`.

## Priorities and deferred practice

First priority: Discrete Mathematics, Programming Fundamentals, Data Structures and Algorithms, Probability and Statistics, Linear Algebra, Digital Logic, and Artificial Intelligence. Operating Systems and Computer Architecture are second priority. Theory of Languages and Automata is excluded at the student's request. IELTS Academic grammar, reading, and listening run in parallel; Writing and Speaking are outside the requested three-strand pathway.

The archived Iranian master's and doctoral entrance-exam booklets are outside the present chapter-writing and first-reading workflow. They are reserved for **joint, question-by-question study in the final month**. Earlier exam audits remain under `research` as project history and are not served as live study content.

## Chapter standard

Each chapter must synthesize at least four genuinely reviewed written courses from four universities, use more sources when an identified gap requires them, teach its concepts from prerequisites through advanced cases, include a varied bank of fully explained original and attributed course-derived problems, and close with a clear high-yield review sheet. Length must follow substance, not a page-count target. Mathematical and presentation checks precede student review; explicit approval precedes a `ready` label and work on the next chapter. The details are in `WEEKLY_DELIVERY.md`.
