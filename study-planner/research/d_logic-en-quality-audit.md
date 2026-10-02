# English chapter quality audit — d_logic

## Chapter boundary

The live chapter covers propositions, truth-functional semantics, equivalence, satisfiability, entailment, normal forms, predicates, quantifiers, first-order model semantics, scope, substitution, basic sound inference, and finite versus infinite models. Sets, formal deduction systems, induction, physical circuit timing, and algorithmic SAT complexity are separate chapters or subjects.

## Candidate screen and source decision

| Candidate | Access and review | Decision for this chapter |
| --- | --- | --- |
| MIT 6.042J, Leighton and van Dijk (2010), Chapter 1 | All 17 substantive pages read; original PDF symbols checked visually | Selected: precise foundation and quantifier examples |
| Stanford CS103, Trevisan (2014), Lecture 9 | All 8 pages read; scope examples checked | Selected: syntax and free/bound occurrences |
| UC Berkeley CS70, Shahzar and Wu (2024), Note 1 | All 14 pages and relation diagrams read | Selected: restricted quantifiers and complementary examples |
| CMU 15-311, Heule (2026), propositional and first-order decks | All 75 + 58 physical PDF pages read, including animation frames | Selected: structural proofs, models, substitution, infinite cases |
| Cornell CS2800, Lecture 36 (2017) | Public lecture text inspected | Supplementary comparison, not counted among the four |
| Princeton COS 341, Charikar (2002), Lecture 2 | Public 24-page PDF screened for relevant topic range | Candidate, not counted; full logic sequence not reviewed |
| Illinois CS173 (Fall 2024), Logic 1 | Public lecture text screened | Candidate, not counted; full sequence not reviewed |
| Oxford, Logic and Proof (2022–2023) | Public syllabus located, chapter lecture text not verified | Scope benchmark, not counted |
| ETH Zurich, Discrete Mathematics (2026) | Course catalogue and a separate open text located; exact course linkage not established | Not counted |

The wider English course register contains 13 logic-related entries, including different versions of some courses. Selection criterion: accessible written material for the exact chapter, topic coverage, proof quality, and scientific precision. This is a documented comparison of accessible candidates, not a claim to have inspected literally every course worldwide.

## Topic-to-source synthesis

| Topic | Compared locations | Treatment in English chapter |
| --- | --- | --- |
| Atomic statements, valuations, connectives, truth tables | MIT §1.1; Stanford Lecture 9 pp. 1–3; Berkeley Note 1 pp. 1–4 | §§2.1–2.2 and interactive lab |
| Recursive syntax, formula size and depth | Stanford Lecture 9; CMU propositional slides | §2.3, full structural-induction proof |
| Equivalence, validity, satisfiability, entailment | MIT §§1.1–1.5; Berkeley Note 1; CMU propositional slides | §§2.2, 3.1, 3.3, Problems 1, 3, 7 |
| Normal forms, resolution, equisatisfiability | CMU propositional slides; MIT §1.5 | §3.2 and Problem 4 |
| Predicate semantics, free variables, quantified sentences | MIT §1.3; Stanford Lecture 9 pp. 4–8; Berkeley Note 1; CMU first-order slides | §§4.1–4.3, Problems 2, 5, 6, 9 |
| Scope, alpha-renaming, capture-free substitution | Stanford Lecture 9 pp. 6–7; CMU first-order slides | §4.4, Problem 10 |
| Inference rules and witness side conditions | Berkeley Note 1; CMU first-order slides | §4.5, Problems 3 and 8 |
| Quantifier movement and nonempty-domain conditions | CMU first-order slides; MIT §1.3 | §§4.1, 4.6, Problem 6 |
| Infinite-only models and finite-search limits | CMU first-order slides | §4.7 |
| Fast recall and later timed-problem pitfalls | Synthesis of four selected sources | §6 review sheet and 12-row decision checklist |
| Course-derived reasoning exercises | MIT Problem Set 1 P3; Stanford HW4 P1; Berkeley Discussion 1B P2; CMU propositional slide 14 | Problems 11–14, independently worded and fully solved |

## Independent checks and limitations

- Problems 1–10 are original to the English edition; Problems 11–14 are independently worded adaptations of the cited university exercise types, with newly derived solutions. No archived Iranian master's or doctoral entrance-exam question, answer, option, or PDF link is included in the live chapter.
- `verify_d_logic_en.py` exhaustively checks the stated propositional laws and solution counts over finite valuations; it checks finite-model forms of Problems 2, 5, 6, 8, and 9 and the quantifier-movement side conditions. These checks supplement, rather than replace, review of first-order proofs and capture-free substitution.
- The expanded fourteen-problem edition was rendered in Edge at desktop and 600-pixel narrow widths. A DevTools mobile emulation at 390 pixels confirmed that the chapter and IELTS app have 390-pixel document widths with no horizontal page overflow; both screenshots were reviewed. The six HTML pages passed local-link and English-script checks. Edge produced a 19-page A4 print with no blank pages or replacement glyphs in extracted text. The student explicitly approved this chapter on 2026-09-29. The live `dist` directory contains English study-facing files only; earlier Persian inputs and exam-audit JSON files are retained under `research` rather than served by the site.
- Source claims and access level are traceable to the prior detailed source audit and the original university links. A globally optimal course ranking and a literal 100% guarantee for unseen future questions cannot be proved. Identified errors or in-scope gaps are release blockers.
- The legacy exam audits are retained as project history but are not used by the current chapter or app workflow. Entrance-exam booklet work is deferred until the final month.


## Final existing-library revision — 2026-10-02

The full authored manuscripts, every worked answer, final rules, and diagram context were reread during the sixteen-chapter revision. Findings: Corrected free-variable count and fresh-bound-name condition. Added four quantifier movement laws with empty-domain cases and precise distribution laws. Corrected formal-calculus scope; split diagram arrows to retain every arrowhead. All identified findings were corrected before rebuilding. The rebuilt chapter passed the recorded finite checks, desktop/mobile geometry, font loading, and print-style diagram-width checks. This is evidence of the performed review, not a universal correctness guarantee or a new full reading of every source course. See `LIBRARY_FINAL_REVIEW.en.md` and `library-review.json`.
