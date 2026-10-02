# Invariants and recursive reasoning: source selection and reading audit

Review date: 2026-10-02. Topic: d_invariants, Discrete Mathematics Chapter 7, Week 2. This audit records a bounded comparison of eight university course candidates. It does not claim an exhaustive enumeration of worldwide courses, a universally optimal ranking, or complete reproduction of entire course exercise collections.

## Selection method

Candidates were sought on official university domains using the chapter's two coupled needs: transition-invariant reasoning and recursive/structural reasoning. A catalogue was insufficient evidence of actual instruction. The comparison favored readable written material, explicit proof obligations, constructor/domain precision, nontrivial worked examples, and complementary coverage. Rankings below are qualitative editorial judgments specific to this chapter, not numerical measures of university quality. Content was checked before assigning the principal roles.

## Candidate pool and disposition

| Priority | University and course | Material actually inspected | Fit and disposition |
|---|---|---|---|
| Principal 1 | MIT 6.042J, Mathematics for Computer Science, Spring 2015; Eric Lehman, F. Thomson Leighton, Albert R. Meyer | Full Section 5.4, printed pages 130–144; selected exercise pages 163–171; Sections 6.1–6.4, printed pages 173–188; Problems 6.1, 6.2, 6.4, 6.5 | Broadest exact fit across both halves: state closure, conservation, monotonic derived variables, lexicographic progress, data constructors, substitution. Some operation-count conventions require clarification. |
| Principal 2 | CMU 15-150, Principles of Functional Programming; Michael Erdmann, Spring 2026 PDFs, originally based in part on Frank Pfenning's draft | All seven structural-induction pages; both reversal pages; lecture code's accumulator and reversal specifications | Most explicit generalized accumulator proofs and two-child hypotheses. Careful separation of totality and equivalence. Its SML implementation costs are not transferred uncritically to Python. |
| Principal 3 | Stanford CS161, Spring 2017; Mary Wootters; section author Jessica Su | All five pages of Section 1: Loop and Recursion Invariants | Clear bridge between induction, merging, and recursive power. Complements the theoretical texts. Add explicit recursion termination and exhaustion guards in the chapter. |
| Principal 4 | Cambridge Foundations of Computer Science, 2013; Lawrence C. Paulson | Printed pages 14–24, 26–35, 56–65; close inspection of accumulator, list-concatenation, reversal, datatype, and tree-count equations | Strong implementation/evaluation complement and explicit representation conventions. Supplies instructional list exercises. Tail-call and arithmetic-cost qualifications retained. |
| Supplement | Cornell CS2800 Discrete Structures, Spring 2017; Michael George | Entire Lecture 21: Structural Induction, including all three review questions | Useful one-argument versus product-induction comparison. The undefined variable in its concatenation equation is corrected through independent constructor definitions, not copied. |
| Supplement | UC Berkeley CS70 Discrete Mathematics and Probability Theory, Fall 2026, staff-authored Note 4 | PDF pages 1–6, particularly quantitative hypothesis strengthening on pages 4–6 | Strong on strengthening, but repeats the approved induction chapter and lacks the detailed accumulator/transition synthesis needed here. Retain one slack-bound exercise rather than replace a principal source. No individual PDF author is inferred. |
| Supplement | Princeton COS226 Algorithms and Data Structures, Spring 2021; Robert Sedgewick and Kevin Wayne | Mergesort slides 4–9; official slide rendering/text and code branches | Independent implementation check for empty-side handling and a merge-comparison question. General sorting and recurrence analysis belong to later chapters. Local PDF extraction is partly garbled; critical guards and counts were checked through official readable text and original page rendering. |
| Not counted as instructional reading | Oxford Imperative Programming I, Hilary 2017; Geraint Jones | Official overview, syllabus, and reading list; attempted materials link | Excellent declared syllabus fit, but the inspected page is a catalogue, and the attempted materials page did not yield readable lectures. Exclude from the genuinely read core count; do not infer quality from unavailable instructional content. |

The selected four are complementary principal courses, not four random search hits. Supplemental sources broaden checks rather than being used to inflate the core-university count. Cornell's main course textbook is MIT's text, so its independent lecture is credited specifically rather than double-counting the shared textbook as a new course treatment.

## Exact reading and original-page checks

Downloaded reference PDFs and extracted texts are kept outside the publication in the local temporary directory `phd-invariants-sources`. The provenance JSON records exact URLs, byte hashes, page counts, and the inspected local paths. Copyrighted PDFs are not included in the Site or GitHub chapter deliverable.

Representative original pages were rendered and inspected: MIT PDF page 144, the formal preservation definition and invariant principle; Stanford PDF page 5, recursive power; CMU structural PDF page 7, the two-subtree accumulator proof; Cambridge PDF page 67, count/depth/external-leaf equations. MIT's printed page labels differ from PDF positions by its front matter. Cite printed labels when describing the section and one-based PDF positions for rendering evidence.

CMU's linked PDF title pages identify Spring 2026 and Michael Erdmann, while its current linked lecture-code file identifies Fall 2026, Dilsun Kaynar and Stephanie Balzer. Preserve this distinction rather than assign all files the current archive's lecturers.

## Reconciliation and corrections

1. MIT distinguishes preserved predicates from properties of all reachable states. The chapter defines both explicitly and uses a four-state counterexample to prevent conflation.
2. Stanford labels the conclusion of recursive-power correctness as termination in its exposition. The chapter separately proves that integer recursive arguments strictly decrease and that returned values meet the specification.
3. Stanford's merge presentation uses sentinel assumptions. The chapter's independently written code uses guarded short-circuit accesses and handles empty sides without requiring an artificial value beyond the entire input domain.
4. The exact exponent-halving body count is floor(log base two of n) plus one for positive n. The MIT ceiling expression is retained only as an upper bound, with separate accounting for a return action or guard checks. A nonpower-of-two example detects the exact-count confusion.
5. Cornell's online two-argument concatenation definition contains an undefined auxiliary variable. The chapter uses the independently checked first-list constructor equations and then proves the required laws.
6. Cambridge's empty-tree leaves are external positions, whereas CMU/MIT full-tree leaves carry data. Both representations are explained and the counting and height formulas are not mixed.
7. The standard Ackermann definition and MIT's alternative are different functions. Both are explicitly defined and their totality arguments use lexicographic induction, without substituting one variant's values into the other.
8. Pure integer arithmetic and linked-list cost assumptions are stated. Machine overflow, side effects, Python slicing, tail-call elimination, and finite implementation stack limits are not hidden behind mathematical notation.

## Selected exercise ledger

This ledger covers the exercise families actually selected for this chapter. It does not claim all exercises in the complete courses, all textbook chapters, or every university question worldwide. Original questions fill the chapter-specific gaps and each appears with a complete solution.

| Course location or family | Chapter destination | Disposition |
|---|---|---|
| MIT Section 5.4.2 diagonal robot | Problem 7 and conservation lesson | Obstruction and constructive converse both proved. |
| MIT Section 5.4.4 jugs | Problem 8 | Independently numbered capacities and all fill/empty/pour cases checked. |
| MIT Section 5.4.6 resetting robot | Problems 20–21 | Lexicographic termination, unbounded family of lengths, and bounded scalar-rank repair. |
| MIT Problem 5.36 | Problem 26 | Exact positive/zero body counts, convention audit, and multiplication accounting. |
| MIT Problem 5.37(a–e) | Problems 16–17 | Normal strategy, highest-bit constructive response, termination, and the complete misère adjustment. |
| MIT Problem 5.38 | Problem 11 | Horizontal and vertical parity cases, target exclusion, odd-width comparison. |
| MIT Problem 5.39(a–d) | Problem 14 | Transitions, all nine derived quantities, safety proof, and constructive empty-bridge deadlock. Capacity generalized. |
| MIT Problem 5.40(a–d) | Problem 13 | Exact coin witness, parity obstruction, reachable-state quantity classifications. State is the nonnegative integer head/tail pair; a flip requires ten available coins and a permitted selected-head count. |
| MIT Problem 5.41 | Problem 15 | Perimeter calculation and justification for sequentializing a simultaneous round. |
| MIT Problem 5.42(a–c) | Problem 49 | All four guarded changes, invariant, exact step count, and maximum population. |
| MIT Problem 5.43(a–c) | Problem 12 | Inversion cases and smaller reversed example, plus nonidentity termination and nonsorting terminal example. |
| MIT Problems 6.1 and 6.2 | Problems 31–32 | Constructor definitions, associativity, reversal of concatenation, involution, and length preservation. |
| MIT Problem 6.4(a–f) | Problem 44 | Soundness/completeness, signed integer coordinates, and canonical unambiguous representation. |
| MIT Problem 6.5(b–c) | Problems 34–35 | Leaf flattening and the total-node identity. Source-figure serialization is not reproduced because a new original tree is used. |
| MIT Theorem 6.4.4 | Problem 40 | Every constant, variable, addition, multiplication, and negation case is explicit. |
| CMU structural notes, Lemmas 2–5 and Theorem 6 | Problems 31, 34 | Totality, append associativity, generalized flattening, and wrapper consequence. |
| CMU reversal theorem and both thought questions | Problem 33 | Arbitrary accumulator, singleton concatenation, and the distinction between symmetric equality and directed evaluation. |
| CMU right-identity exercise | Problem 31 | Complete structural proof. |
| Stanford Section 1 worked merge and exponentiation | Problems 25, 27 | Full proofs, zero cases, exhaustion/duplicates, and domain/call termination. Foundational scalar induction examples are already taught in d_induction. |
| Cambridge Exercises 3.1–3.3 | Problems 41–43 | Summation equivalence and costs, nonempty last-element domain, even-position selection with both bases. |
| Cambridge tree equations | Problems 35–36 | Counting representation, height bound, and equality cases. |
| Cornell Lecture 21 three review prompts | Problems 31–32; prior d_induction | Concatenation length and reversal length handled here. Recursive natural addition commutativity is foundational prior-chapter material rather than a new duplicate problem. |
| Berkeley Note 4 slack-bound exercise | Problem 47 | Positive-denominator algebra and explicit hypothesis repair. |
| Princeton slide 8 merge-comparison question | Problem 25 | Exact equal-length minimum and maximum, with comparison rather than output-step counting. |

MIT's surrounding induction exercises, faro-shuffle permutation structure, finite-memory ant controller design, calculus-function closure, parsing-language exercises, and later graph/game topics are not claimed as reproduced here. They are outside the selected exercise boundary or require separate topic treatment. Cambridge's unrelated date, numerical precision, sorting, and dictionary exercises likewise are not claimed as covered. No Iranian examination archive was opened, classified, or solved.

## Primary links

- [MIT textbook](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf).
- [Stanford section notes](https://web.stanford.edu/class/archive/cs/cs161/cs161.1176/Sections/161-section-1.pdf), [course instructor and archive](https://web.stanford.edu/class/archive/cs/cs161/cs161.1176/).
- [CMU structural notes](https://www.cs.cmu.edu/~15150/resources/lectures/04/structural.pdf), [reversal notes](https://www.cs.cmu.edu/~15150/resources/lectures/04/rev.pdf), [lecture code](https://www.cs.cmu.edu/~15150/resources/lectures/04/code04.sml).
- [Cambridge notes](https://www.cl.cam.ac.uk/teaching/1314/FoundsCS/fcs-notes.pdf).
- [Cornell structural lecture](https://www.cs.cornell.edu/courses/cs2800/2017sp/lectures/lec21-structural.html), [course attribution](https://www.cs.cornell.edu/courses/cs2800/2017sp/).
- [Berkeley induction note](https://www.eecs70.org/assets/pdf/notes/n4.pdf).
- [Princeton mergesort slides](https://www.cs.princeton.edu/courses/archive/spring21/cos226/lectures/22Mergesort.pdf).
- [Oxford syllabus candidate](https://www.cs.ox.ac.uk/teaching/courses/2016-2017/imperativeprogramming1/), not counted as lecture reading.
