# Stacks and Queues: source selection and reading audit

## What was compared

The candidate pool is bounded to accessible written courses at seven universities: Princeton, Oxford, Carnegie Mellon, Stanford, MIT, Berkeley, and Cornell. This audit does not claim that all courses worldwide were available, or that every candidate institution has a single universally best course. Selection is chapter-specific: interface precision, representation proofs, quantitative analysis, application coverage, and inspectable text matter more than a university name or publication date.

| Candidate | Actual reading scope | Selection and reason |
|---|---|---|
| Princeton COS226, Robert Sedgewick and Kevin Wayne; Spring 2026, Stacks and Queues I | All 45 PDF pages, including APIs, fixed arrays, ring buffers, doubling, contraction, amortized versus worst-case analysis, two-stack queue challenge, and Java generics | Primary. Strongest integrated representation/cost spine in the inspected pool. The extracted code font is unreliable; algorithms are independently written rather than copied from extraction. |
| Oxford B16, Andrea Vedaldi; 2024, Chapter 3 | Sections 3.3 and 3.4 including their complete C++ implementations; relevant linked-list representation passages in 3.5 | Primary. Explicit array indices and a useful contrasting backward-growing queue convention. The chapter deliberately adopts a forward-growing front/count convention and derives the translation instead of mixing formulas. |
| Carnegie Mellon 15-122, Frank Pfenning, Andre Platzer, Rob Simmons; Spring 2026, Lecture 9 | PDF pages 1-19 read through the browser text, including all six exercises and their sample solutions | Primary. Strong interface contracts, aliasing, restoration, and client algorithms. Local download failed; browser reading is the evidence, not a nonexistent local PDF. The source's ascending/descending prose and strict comparisons are inconsistent in places; the new chapter explicitly defines nondecreasing versus strictly increasing order and derives its own code. Its impure-assertion warning is retained as a conceptual issue, not copied as executable code. |
| Stanford CS106B, Chris Gregg; Spring 2017, Lecture 5 | All 45 PDF pages; technical scope pages 8-29, 33-45 | Primary. Strong postfix operand-order instruction, typed brackets, function-call order, changing-size loop counterexample, and client use. Logistics/history illustrations are not instructional sources for this chapter. The generic claim about vector end operations is refined into worst-case versus amortized costs. |
| MIT 6.006, Erik Demaine, Jason Ku, Justin Solomon; Spring 2020, Problem Session 1 | Pages 2-3, sequence-end operations and double-ended representation; the remainder screened for relevance | Complementary. Adds deque rotation and rebuilding arguments. The printed indexing guard in Problem 1-3 is not adopted: the logical rank must satisfy 0 <= j < n; the physical index is offset + j. |
| Berkeley CS61B textbook, SLLists and DLLists | Previously inspected full Chapters 4-5; DLLists chapter rechecked for sentinel and end-operation design | Complementary representation reference. Its linked structures reinforce empty/singleton cases; it adds less expression-processing depth than Stanford for this chapter. Not counted as a newly read full stacks/queues course. |
| Cornell CS2110, Fall 2025, linked-list lecture | Previously inspected invariant sections; candidate context only in this chapter | Screened supporting candidate. Adds no distinct missing chapter topic sufficient to replace the four anchors. Not counted among the four genuinely read anchor courses. |

## Source synchronization

The four primary courses agree on abstract LIFO/FIFO order and underflow contracts. They do not use identical physical index conventions or library signatures. Oxford separates front/top access from removal; other interfaces may return the removed item. This lesson states its own return-value contract and orientation in every algorithm. Princeton supplies the cost distinction, CMU supplies client restoration, Oxford supplies explicit storage boundaries, and Stanford supplies parsing and changing-container examples.

Catalan paths, the complete permutation criterion, monoid aggregates, monotone stacks/deques, histogram widths, 0-1 BFS boundaries, and Josephus recurrences are independently developed extensions. They are not falsely described as passages read in the four introductory lectures. General proofs and independent finite checks support those extensions. Course-inspired problems are rewritten in original wording and solved independently, with their exact conceptual origin stated. The six CMU exercise themes are all represented; this is not republication of every exercise on every university website.

## Exact references

1. Princeton COS226. Robert Sedgewick and Kevin Wayne. *Stacks and Queues I*, Spring 2026. [Lecture slides](https://www.cs.princeton.edu/courses/archive/spring26/cos226/lectures/13StacksAndQueuesI.pdf).
2. Oxford B16. Andrea Vedaldi. *Algorithms and Data Structures 1*, Chapter 3, Sections 3.3-3.5, 2024. [Written course notes](https://www.robots.ox.ac.uk/~vedaldi/assets/teach/2024/b16/notes/3-elementary-data-structures.html).
3. Carnegie Mellon 15-122. Frank Pfenning, Andre Platzer, Rob Simmons. *Lecture 9: Stacks and Queues*, Spring 2026, pages 1-19. [Lecture notes](https://www.cs.cmu.edu/~15122-archive/s26/handouts/lectures/09-stackqueue.pdf).
4. Stanford CS106B. Chris Gregg. *Lecture 5: Stacks and Queues*, April 12, 2017. [Lecture slides](https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1176/lectures/5-Stacks_Queues/5-Stacks_Queues.pdf).
5. MIT 6.006. Erik Demaine, Jason Ku, Justin Solomon. *Problem Session 1 Solutions*, Spring 2020, Problems 1-2 and 1-3, pages 2-3. [Written solutions](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/1ecbb4149fe5f5166033bdde285dba07_MIT6_006S20_prob1sol.pdf).
6. Berkeley CS61B. *DLLists*, Chapter 5. [Written textbook](https://cs61b-2.gitbook.io/cs61b-textbook/5.-dllists.md).
7. Cornell CS2110. *Lecture 13: Linked Lists*, Fall 2025. [Course notes](https://www.cs.cornell.edu/courses/cs2110/2025fa/lectures/lec13/).

## Archive reading

Original rendered PDF page 4 of PhD CE 1404 was read for Q9 (max-stack design) and Q11 (doubly linked deque). Original rendered PDF page 10 of MS CE 1393 was read for Q49 (remove dominated rear elements before append). These are genuine source questions, independently translated and solved, with repository commit, PDF hashes and original option numbering preserved. The MS question's numerical upper bound depends on charging one unit per individual insertion/deletion; asymptotically it is linear under any fixed per-node unit cost. No official answer key was available. The archive reading is targeted, not an exhaustive census of all years.

## What this audit cannot establish

Coverage is measured against the explicit chapter map, source scopes, worked bank, and boundary cases. It is not proof of literal 100% certainty, exhaustive worldwide source review, or guaranteed performance on every future question. Concurrency, persistence, advanced parser grammars, and priority queues have explicit boundaries. Read/write costs and allocation assumptions are stated separately. Source download fingerprints are recorded where an actual local artifact exists.
