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
| Fast recall and later timed-problem pitfalls | Synthesis of four selected sources | §6 compact review sheet |

## Independent checks and limitations

- The ten worked problems are original to the English edition. No archived Iranian master's or doctoral entrance-exam question, answer, option, or PDF link is included in the live chapter.
- `verify_d_logic_en.py` exhaustively checks the stated propositional laws and solution counts over finite valuations; it checks finite-model forms of Problems 2, 5, 6, 8, and 9 and the quantifier-movement side conditions. These checks supplement, rather than replace, review of first-order proofs and capture-free substitution.
- The English app and chapter were rendered on desktop and a narrow viewport. Six HTML pages have no missing local static links. The final Edge print contains 16 nonblank A4 pages, no Arabic-script text, and no replacement glyphs. The live `dist` directory contains English study-facing files only; earlier Persian inputs and exam-audit JSON files are retained under `research` rather than served by the site.
- Source claims and access level are traceable to the prior detailed source audit and the original university links. A globally optimal course ranking and a literal 100% guarantee for unseen future questions cannot be proved. Identified errors or in-scope gaps are release blockers.
- The legacy exam audits are retained as project history but are not used by the current chapter or app workflow. Entrance-exam booklet work is deferred until the final month.
