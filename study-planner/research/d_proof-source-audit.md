# Source and boundary audit — d_proof

Date: 2026-09-29. Scope: direct proof, contrapositive, contradiction, cases, biconditional proof, existential witnesses, uniqueness, counterexamples, and proof-error diagnosis. Mathematical induction and well-ordering are reserved for `d_induction`; full number theory and function theory are reserved for later chapters. Archived Iranian entrance-exam papers are deferred to the final month.

## Bounded candidate search and actual review

The search covered openly available written course materials found through official university domains for this chapter. This is not an exhaustive search of all courses worldwide, nor a global ranking. The five selected texts were actually read at the sections shown; “best” means the strongest complementary fit in this bounded set.

| University | Written course, instructor/author, reviewed portions | Chapter strength | Limitation and decision |
| --- | --- | --- | --- |
| MIT | 6.042J *Mathematics for Computer Science* (Eric Lehman, F. Thomson Leighton, Albert R. Meyer; 2015), Chapter 1 §§1.1 and 1.5–1.8, especially pp. 11–17. [Official text](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf). | Canonical proof architecture; two directions of iff; cases; precise boundary between informal exploration and proof. | Limited counterexample workflow in this chapter; selected as primary spine. |
| Stanford | CS103 *Guide to Proofs* (Stanford CS103 course staff; accessed 2026-09-29), sections on direct universal and existential proofs, compound quantifiers, contrapositive, contradiction, cases, and worked exercises. [Official guide](https://web.stanford.edu/class/cs103/guide_to_proofs). | Strongest explanation of what a proof must assume and show; especially ∀ then ∃ witness dependency. | Uses invented predicates in many examples; selected for proof-writing pedagogy. |
| UC Berkeley | CS70 *Discrete Mathematics and Probability Theory*, Summer 2024 Course Notes, Note 2, §§2–8. [Official note](https://su24.eecs70.org/assets/pdf/notes/n2.pdf). | Direct, contrapositive, contradiction, cases, errors and proof style in a compact integrated sequence. | Many examples are elementary, so advanced traps are supplied through synthesis; selected. |
| Cornell | CS2800 *A Course in Discrete Structures* (Rafael Pass and Wei-Lung Dustin Tseng; 2015 archive), Chapter 2 §§2.1–2.2, PDF pp. 17–20. [Official text](https://courses.cs.cornell.edu/cs2800/2015fa/handouts/pass_tseng_discmath.pdf). | Explicit comparison of direct and indirect arguments, irrationality, examples and counterexamples. | Next section is induction, excluded here; selected. |
| ETH Zürich | *Diskrete Mathematik* (Ueli Maurer; Autumn 2024), Chapter 2 §2.6.1–2.6.9, PDF pp. 21–24. [Official notes](https://crypto.ethz.ch/teaching/DM24/ln/DM24_LN.pdf). | Formal soundness of composed implications, case exhaustiveness, existential proofs and counterexample as constructive refutation. | Text is German; mathematical statements and proof patterns were checked in the original, and paraphrased English explanations are used; selected as fifth complement. |
| Oxford | *Introduction to University Mathematics*, 2025–26, “4 Logic and Proof,” direct/contradiction/counterexample sections. [Official lesson](https://courses.maths.ox.ac.uk/mod/page/view.php?id=65664). | Useful discussion of discovery versus proof and boundary examples. | Supplemental comparison only. The HTML extraction around one AM–GM contradiction line appears inconsistent, so that displayed derivation is not used as a mathematical source; any related derivation is checked independently. |

## Topic-to-source coverage

| In-scope pattern | Independent reviewed texts | Chapter location |
| --- | --- | --- |
| Universal implication, direct proof and witness algebra | MIT, Stanford, Berkeley, Cornell, ETH | §§2–3; Problems 1–5 |
| Contrapositive versus converse/inverse | MIT, Stanford, Berkeley, Cornell, ETH | §4; Problems 6–8 |
| Contradiction and quantified negation | MIT, Stanford, Berkeley, Cornell, ETH | §5; Problems 9–11 |
| Exhaustive cases and iff | MIT, Stanford, Berkeley, Cornell, ETH | §6; Problems 12–14 |
| Existential witness, dependence, uniqueness | Stanford, Berkeley, Cornell, ETH | §7; Problems 15–17 |
| Counterexample and invalid-proof diagnosis | Stanford, Berkeley, Cornell, ETH; Oxford supplemental | §8; Problems 18–22 |

The chapter must teach each pattern before the problem bank and provide a complete solution, including domain and edge cases. The final high-yield sheet is supplementary to the detailed lesson. Finite checks can catch selected errors but cannot certify universally quantified claims or guarantee success on every unseen exam question.
