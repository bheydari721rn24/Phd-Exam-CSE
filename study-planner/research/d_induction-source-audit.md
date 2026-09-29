# Source and boundary audit — d_induction

Date: 2026-09-29. Scope: ordinary and strong induction over integers bounded below; shifted starts, multiple bases, step sizes, strengthened hypotheses, well-ordering/minimal counterexamples, and precise error diagnosis. Structural induction and full recurrence solving receive only a bridge; their systematic treatment belongs to later chapters. Archived Iranian examination questions are deferred to the final month.

## Bounded candidate survey and actual reading

The search was restricted to publicly accessible written course material on official university domains. The five selected texts below were read in the cited sections and compared for this chapter. The ranking is a judgment of complementary coverage within this accessible pool, not an exhaustive audit of every university course worldwide. A syllabus or video listing was not counted. Original course exercises are discussed by independently worded type; no claim is made that all published exercises are reproduced.

| Rank | University and actual written course portion reviewed | Particular value for this chapter | Limitation |
| --- | --- | --- | --- |
| 1 | MIT, 6.042J *Mathematics for Computer Science*, Eric Lehman, F. Thomson Leighton, Albert R. Meyer (2015), Chapter 5 §§5.1–5.3, printed pp. 115–130. [Official full text](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf). | Ordinary/strong induction, prime factorization, strengthened tiling predicate, and failure of the horse argument. | Long examples sometimes obscure the short logical dependency; selected as main mathematical spine. |
| 2 | Stanford, CS103 *Guide to Induction* and *Induction Proofwriting Checklist* (course staff, 2024–25 archive), entirety of the relevant HTML guides. [Official guide](https://web.stanford.edu/class/archive/cs/cs103/cs103.1252/guide_to_induction); [checklist](https://web.stanford.edu/class/archive/cs/cs103/cs103.1252/induction_checklist). | Clear proof obligations, well-formed predicate, step-size and multiple-base diagnostics. | Some examples emphasize writing form more than mathematical depth; selected for error-proof exposition. |
| 3 | UC Berkeley, CS70 *Discrete Mathematics and Probability Theory*, Summer 2024, Notes 3–4. [Induction note](https://su24.eecs70.org/assets/pdf/notes/n3.pdf); [well-ordering note](https://su24.eecs70.org/assets/pdf/notes/n4.pdf). | Strengthened inequalities, four-and-five-unit representation, prime factorization, strong/ordinary equivalence, minimal counterexample. | Several exercises leave algebra to the reader; selected to supply advanced problem patterns, with all algebra independently completed here. |
| 4 | Cornell, CS2800 *A Course in Discrete Structures*, Rafael Pass and Wei-Lung Dustin Tseng (2015), Chapter 2 §2.3, printed pp. 17–25; and Chapter 4 §4.3's binomial theorem and alternating-sum corollary, printed p. 68. [Official text](https://courses.cs.cornell.edu/cs2800/2015fa/handouts/pass_tseng_discmath.pdf). | Induction over arbitrary finite sets, graph paths, recurrence-shaped problems, multiple starting cases, hypothesis strengthening, and an independent binomial cross-check. | A power-set displayed equality in the PDF appears to omit the reduced-set mark; its reasoning is independently reconstructed here instead of copying that line. |
| 5 | ETH Zürich, Ueli Maurer, *Diskrete Mathematik* (Autumn 2024), §2.6.10, printed pp. 36–38. [Official notes](https://crypto.ethz.ch/teaching/DM24/ln/DM24_LN.pdf). | Exact induction axiom and initial-index/domain bookkeeping; geometric series model. | Section is shorter than MIT/Berkeley; selected as a fifth independent check of the formal rule. The notes' mathematical chapter is in English. |

## Synthesis matrix

| Pattern | Sources actually used to check it | Manuscript location |
| --- | --- | --- |
| Predicate and base/step semantics, shifted start | MIT, Stanford, Berkeley, Cornell, ETH | §§2–3; Problems 1–5 |
| Step by d, residue classes, multiple bases | Stanford, Berkeley, Cornell, MIT | §4; Problems 6–8, 16 |
| Strong induction, prime decomposition, representation | MIT, Berkeley, Cornell | §5; Problems 9–11 |
| Strong/ordinary/well-ordering equivalence | MIT, Berkeley, ETH | §§5–6; Problems 12–13 |
| Hypothesis strengthening, structural object dependency | MIT, Berkeley, Cornell, Stanford | §7; Problems 14–18 |
| Binomial identity; joint and finite descending variants | Cornell §4.3 for the binomial identity; joint/descending rules independently derived from the reviewed induction axioms | §§3, 7; Problems 22–24 |
| Invalid induction and edge-case diagnosis | MIT, Stanford, Berkeley, Cornell | §8; Problems 19–20 |

## Source-specific observations

- MIT's induction chapter makes the failed horse-color induction useful: the overlapping subsets needed in the step do not overlap at the first transition. A valid proof must audit the *first* value to which its step is applied.
- Stanford's guide separates a conjectured formula from the predicate that is actually quantified; a step manipulating only the desired formula backward is incomplete unless every transformation is reversible.
- Berkeley's stronger harmonic-square upper bound demonstrates that proving a weaker statement may leave too little slack to close the step. Its 4/5 representation needs four consecutive base values before subtraction by four is in range.
- Cornell's finite-set proof makes the quantification over *all* sets of cardinality n explicit; an induction hypothesis about one chosen set does not justify a claim about arbitrary new sets. Its graph-path example similarly quantifies over all paths of a given length.
- ETH states the axiom for N starting at 0 and explicitly discusses changing the initial value; changing convention from N={0,1,...} to positive integers changes the base obligation.

## Limits

The review found no proof that this accessible pool is globally optimal or that any note predicts all unseen doctoral questions. Every identified in-scope derivation and example is independently checked. Finite checks catch selected mistakes but cannot prove a general theorem; explicit mathematical proofs remain essential.
