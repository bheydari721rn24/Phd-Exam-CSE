# Sorting: source comparison and synchronization audit

Date: 6 October 2026. Topic: a_sort. Written material only.

## Selection method and bounded candidate pool

The pool comprises five accessible courses from five universities, with twelve acquired PDF documents. Each course was evaluated for chapter coverage, proof quality, implementation precision, treatment of duplicates/stability, mathematical exercises, and complementary material. The four core courses are MIT 6.006, Princeton COS226, CMU 15-122, and Oxford B16. Stanford CS161 is an additional selected course because its expectation counterexample and indicator-variable derivation materially improve the randomized analysis. These are five deliberately complementary selections, rather than four arbitrarily collected links. This pool is documented and bounded; it is not an assertion that every course in the world has been examined.

| University and course | Written scope actually inspected | Strength | Coverage limitation and decision |
| --- | --- | --- | --- |
| MIT, 6.006, Spring 2020; Erik Demaine, Jason Ku, Justin Solomon | Lecture 3, all six PDF pages; Lecture 5 and Recitation 5, all five pages each | Cost model, sorting contract, direct access, stable counting, tuple/radix sorting, all three recitation exercises | Quicksort and bucket distribution proofs absent from these selections. Core for non-comparison sorting. |
| Princeton, COS226, Spring 2026; Robert Sedgewick and Kevin Wayne, lecture-slide authors | Elementary Sorts pp. 3–36; Mergesort pp. 3–37; Quicksort pp. 5–24 and 34–45; Priority Queues pp. 33–40 | Complete comparison-sort trade-offs, precise code, duplicate handling, memory and structured inputs | Slides need expanded proofs. Heapsort deck uses top-down construction and describes bottom-up as improvement. Core algorithm/variant anchor. |
| CMU, 15-122, Spring 2026; Frank Pfenning, Lecture 7 author | Quicksort pp. 1–31; contracts, partition proof, six exercises and sample solutions | Half-open boundaries, invariants, permutation specification, deterministic pivot counterexample | Its illustrated partition differs from both Lomuto and classic Hoare. Randomized expectation proof is outside that note's scope. Core formal-correctness anchor. |
| Oxford, B16 Algorithms and Data Structures 1, 2024–25 v2.1; Andrea Vedaldi | Complete Chapter 2, PDF pp. 14–23, Sections 2.1–2.3, including optional implementation | Rigorous model-based lower bound, merging, counts-only counting variant, iterator/storage distinctions | Counting reconstructs integers, not payload-bearing stable records; pseudocode assumes nonempty merge-sort input. Core model/representation anchor. |
| Stanford, CS161, Fall 2025; Mary Wootters | Insertion proof, both pages; Lecture 5 pp. 29–54; Lecture 6 pp. 24–58 | Incorrect expectation argument explicitly refuted; pair indicators; radix invariant and base/space trade-off | Distinct-key randomized analysis. Some PDF glyph extraction is corrupted, so the key pair-probability slide was also visually inspected. Selected fifth course. |

The acquisition ledger retains exact URLs, SHA256 hashes, page counts and local reference paths. Scope above distinguishes chapter readings from full courses or unrelated lecture passages. No video, complete transcript archive or full-course completion is claimed.

## Cross-source reconciliation

1. **In-place:** MIT/CMU use constant auxiliary storage; Princeton/Stanford allow logarithmic recursion storage in some sorting summaries. This chapter reports element buffer and call-stack storage separately and uses the strict constant-space definition when saying strictly in-place.
2. **Insertion:** the animation uses saved-key shifts, while Princeton also presents adjacent exchanges. Shift count and adjacent-swap count both equal the strict inversion count; total key comparisons also include failed tests. A held key and array hole are explicit in the simulation.
3. **Empty input:** base cases accept zero or one record. No maximum or base-n digit computation is attempted on an empty input. The Stanford proof's insertion position is repaired to put a new equal key after existing equals and to cover an insertion at the front.
4. **Quicksort:** Princeton's scan partition, CMU's one-sided scan, Lomuto, classic Hoare and three-way partition have different return contracts and exact comparison counts. The chapter never transfers an exact formula between them. The ideal randomized formula counts each nonpivot once, not scan-crossing overhead.
5. **Radix digits:** the MIT sample bit-length ratio is not adopted as an exact digit-count formula. For n=3 and exclusive universe U=59049, that ratio gives nine passes although U−1 needs ten base-three digits. The chapter uses repeated division or the exact integer condition B^d ≥ U, with zero/singleton cases handled.
6. **Counting payloads:** Oxford's integer reconstruction preserves multiplicities but cannot preserve attached record identities. MIT/Stanford's stable record versions retain identities using FIFO buckets or cumulative positions. Both variants are taught with explicit storage and stability conditions.
7. **Expectation:** a balanced mean split does not prove a balanced recurrence. Stanford's random-extreme-pivot counterexample and the full pair-indicator proof replace that invalid shortcut.
8. **Heap construction:** top-down insertion and Floyd bottom-up sinking are distinguished. The linear bottom-up proof is independently derived by counting nodes of each height, not asserted from the logarithmic height of the root.
9. **Boundary correction in authentic question:** the original PhD CE 1405 Q16 page gives options 16,14,12,10. Earlier adaptation had their order wrong. This chapter and three previous actual-question occurrences restore option 1; the mathematical result 16 and all other questions are preserved. This is the sole documented exception to byte-for-byte prior-chapter retention.

## Exercise mapping and copyright handling

MIT Recitation 5's three exercise types are represented by independently explained radix traces, shifted integer universes, and fixed-length strings. CMU Lecture 7's six exercises are represented by permutation contracts, recursive proof obligations, adversarial deterministic pivots, temporary partitioning, selection stability and timing interpretation. Princeton's relevant mathematical polls are independently restated around exact counts, allocation versus peak space, structured inputs, duplicates and lower-bound quantifiers. These are labeled course-derived reconstructions; wholesale course question reproduction is not claimed. Most problems are newly authored medium/hard mathematical and conceptual questions with complete independent solutions.

## References

- MIT — [6.006 Lecture 3: Sorting](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/6d1ae5278d02bbecb5c4428928b24194_MIT6_006S20_lec3.pdf); [Lecture 5: Linear Sorting](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/78a3c3444de1ff837f81e52991c24a86_MIT6_006S20_lec5.pdf); [Recitation 5](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/cda4cc0c0e626bfbd30bc15fb78c3994_MIT6_006S20_r05.pdf).
- Princeton — [COS226 Spring 2026 written lectures](https://www.cs.princeton.edu/courses/archive/spring26/cos226/lectures.php), Elementary Sorts, Mergesort, Quicksort, Priority Queues.
- CMU — [15-122 Lecture 7: Quicksort](https://www.cs.cmu.edu/~15122-archive/s26/handouts/lectures/07-quicksort.pdf).
- Oxford — [B16 written notes, v2.1](https://www.robots.ox.ac.uk/~vedaldi/assets/teach/2024/b16/b16-notes.pdf), Chapter 2.
- Stanford — [CS161 Fall 2025 written lectures](https://cs161-stanford.github.io/lectures/), Lecture 2 proof handout and Lectures 5–6.

## Remaining limits

This chapter covers its explicit topic checklist, not every research-level sorting algorithm. Selection and priority-queue operations are adjacent scheduled chapters. Shell-sort bounds depend on the gap sequence; no universal optimality claim is made. No official Iranian answer key was available for the two included archive questions. Answers are independently derived and options visually checked. Finite computational checks supplement proofs; they cannot certify literal perfection or performance on every unseen examination problem.
