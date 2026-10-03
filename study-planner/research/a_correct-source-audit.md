# Algorithm correctness — source selection and reading audit

Reviewed on 3 October 2026. Selection concerns the chapter's mathematical scope and accessible written texts. Downloading a PDF is not counted as reading all its pages. A course catalogue or an unavailable slide URL is not counted as a reviewed course.

## Candidate comparison

| University / candidate | Access and review level | Selection decision |
| --- | --- | --- |
| CMU 15-122, Frank Pfenning, Contracts | Complete 24-page written lecture read; exponentiation and arithmetic derivations checked | Principal source for contracts and finite arithmetic boundaries |
| Cambridge Specification and Verification I, Mike Gordon | 121-page text downloaded; pages 11–28, 47–59 and 63–72 read | Principal source for formal rules, array aliasing, verification conditions and variants |
| MIT 6.042J, Meyer and Chlipala; Lehman–Leighton–Meyer text | 920-page text downloaded; §5.4, PDF pages 140–152 read | Principal source for state-machine induction and well-founded progress |
| Stanford CS161 Winter 2022, Lecture 2 | 11-page text downloaded; pages 1–4 read | Principal source for sorting and recursive proof composition |
| Cornell CS2112 Fall 2018 | Public lecture index screened; topic listing includes loop invariants; complete note body not read in this review | Candidate only; no content-reading credit and no source-count inflation |
| ETH Zurich Program Verification, loops/procedures candidate | The searched official slide URL returned HTTP 404 | Unavailable candidate; no claim to have read its contents or compared their scientific quality |
| Oxford Imperative Programming I, 2016–2017 | Official course catalogue screened for scope | Candidate only; catalogue is not a reviewed lecture text |
| Berkeley CS61B Spring 2024 | Public course landing page screened | Candidate only; broad data-structure scope provides no additional reviewed correctness text here |

This is a bounded pool of eight identified universities, with four genuinely reviewed principal written courses. It cannot establish a global ranking against inaccessible, unpublished or unidentified courses. Availability, relevance and complementary rigor determined selection. Among the read texts, Cambridge provides the most explicit proof-rule treatment, CMU the clearest executable contract example, MIT the broadest transition/termination perspective, and Stanford the direct recursive-sorting connection. These are scope judgments, not objective scores or a claim of absolute best courses worldwide.

## Exact reading and synthesis map

| Chapter content | Principal written sources | Additions and repairs in this chapter |
| --- | --- | --- |
| States, contracts and old input snapshots | CMU all lecture; Cambridge pages 11–22 | Distinguish safety from normal-termination partial correctness; explicit record and frame contracts |
| Assignment, consequence, sequencing, conditionals and arrays | Cambridge pages 19–28 and 50–59 | Independently derived numeric questions and aliasing counterexample |
| Initialization, inductiveness and reachable states | MIT pages 140–152; CMU pages 20–21; Cambridge pages 55–56 | Separate reachable truth from preservation over all annotation states |
| Natural and lexicographic variants | MIT §5.4; Cambridge pages 63–72 | Explain arbitrary finite reset versus uniform runtime bound |
| Lower-bound binary search and three-way partition | Original synthesis of reviewed proof frameworks | Full implementations, duplicate/empty cases, exact variants and counterexamples |
| Insertion and merge sort | Stanford pages 1–4, with Cambridge/MIT proof rules | Saved-key hole, multiset preservation, stable ties, exhausted merge inputs and empty recursion |
| Division, gcd and power | Cambridge division examples; CMU power; MIT state-machine power | Explicit positive divisor; old-state updates; modular normalization and overflow |
| Optimality certificates and proof-method comparison | Original synthesis using reviewed invariant and induction methods | Parent-cycle counterexample and meeting-witness/bound argument; later graph/greedy/DP chapters remain distinct |

## Source-scaffold issues handled explicitly

CMU's nonnegative-exponent contract includes exponent zero; an isolated prose description using “positive” must not erase that boundary. The chapter's proof allows zero and states its exponent-zero convention. Arithmetic wrapping claims are separated from C signed-overflow semantics.

Cambridge's mathematical language assumes expression evaluation is defined under its model. The chapter adds explicit implementation safety. Partial division verification and total division verification are separated; a positive divisor is required for the decreasing remainder proof. Chosen annotations can fail even when the underlying command is correct.

Stanford's insertion proof describes a predecessor position without completely spelling out the no-predecessor case. The chapter permits the sentinel index negative one and handles duplicates with a stability-preserving comparison. Its merge scaffold is completed with both exhausted-input cases. Child sortedness is strengthened by multiset preservation.

MIT's state-machine reasoning is applied under the chapter's declared integer model. The text's broader mathematical exponentiation model does not automatically certify finite-width implementations. A real strictly decreasing measure is not treated as a termination proof.

## Provenance and visual inspection

The acquisition manifest records exact official URLs, PDF lengths and SHA-256 digests in `research/a_correct-source-downloads.json`. PDFs and extraction caches remain outside the published site; third-party course texts are not republished. Source formula layouts were visually checked on CMU PDF page 20, Cambridge page 66, MIT page 149 and Stanford page 2 after rendering. Relevant passages were read from extracted page text, with the rendered samples confirming exponent indices and rule structure.

Four authentic archive records are reused from the existing page-checked question selection: PhD CE 1405 Q3 and Q9; PhD CS 1405 Q20; MSc CS 1393 Q167. Their full stored stems, alternatives, provenance and independent solutions were reread for this chapter. This is not a new exhaustive archive reading or official-answer-key verification. The immutable source revision is `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`.

The fifty independently written questions include source-derived concept applications and new problems. Each source-derived question states its precise origin. The bank does not claim to reproduce or solve every exercise from every selected course. Broader library questions remain available for additional practice.

## Official source links

- [CMU Contracts lecture](https://www.cs.cmu.edu/~wlovas/15122-r11/lectures/02-contracts.pdf)
- [Cambridge Specification and Verification I notes](https://www.cl.cam.ac.uk/archive/mjcg/Lectures/SpecVer1/Notes/Notes.pdf)
- [MIT Mathematics for Computer Science text](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf)
- [Stanford CS161 Lecture 2 notes](https://stanford-cs161.github.io/winter2022/assets/files/lecture2-notes.pdf)
- [Cornell CS2112 lecture index](https://www.cs.cornell.edu/courses/cs2112/2018fa/lectures/)
- [Oxford course catalogue](https://www.cs.ox.ac.uk/teaching/courses/2016-2017/imperativeprogramming1/)
- [Berkeley CS61B Spring 2024](https://sp24.datastructur.es/)
