# Searching, Selection, and Order Statistics — source audit

## Scope and selection method

This is a chapter-specific comparison of an identified, accessible pool, not a claim to have inspected every course offered worldwide. Eight universities were screened. Five university courses supply the reviewed instructional core; Princeton's introductory written chapter and a historical CMU assignment supply additional searching and exercise material. Relevance, explicit correctness arguments, cost-model precision, duplicate handling, and usable written material determine selection. An acquisition is not a reading claim.

| University and course | Material actually reviewed | Strength for this chapter | Decision |
|---|---|---|---|
| MIT, 6.046J Spring 2015; Erik Demaine, Srini Devadas, Nancy Lynch | Lecture 2, PDF pp. 4–5; selection pseudocode, exclusion diagram, recurrence and finite-threshold induction; page 5 visually checked | Explicit additive constants and base threshold repair the idealized deterministic proof | Primary deterministic selection source |
| Stanford, CS161 Winter 2023; Moses Charikar and Nima Anari | Lecture 4 selection and recurrence notes, PDF pp. 1–9; one-page Selection concept checks, visually checked | Rank conversion, correctness, substitution, groups of seven and three | Primary proof and course-problem source |
| Carnegie Mellon, 15-451 Fall 2024 | Lecture 1, PDF pp. 1–14, especially pp. 7–14; models, randomized selection, expectation warning, deterministic proof, four exercises | Clear separation of average-input and randomized worst-input expectation | Primary probability and comparison-model source; instructor not asserted without verified attribution |
| Princeton, COS226 Spring 2025; slides by Robert Sedgewick and Kevin Wayne | Quicksort slides, PDF pp. 28–31 and 34–39 | Executable one-branch selection, rank-index conventions, and duplicate-key partition mechanics | Primary implementation source |
| UC Berkeley, CS170 assigned Algorithms text by Sanjoy Dasgupta, Christos Papadimitriou and Umesh Vazirani | Chapter 2, §2.4, printed pp. 64–66 / PDF pp. 10–12; adjacent sorting lower-bound page screened | Three-way selection and a phase interpretation of expected linear work | Complementary fifth course source |
| Princeton, Introduction to Programming; Robert Sedgewick and Kevin Wayne | §4.2 written searching exposition, searching Q&A and relevant exercises: duplicate count, rotated/bitonic search, two-array median, range queries, threshold doubling | Binary-search contracts and broader searching patterns | Supplement; same university counted once |
| Carnegie Mellon, 15-451 Fall 2005 | Homework 2, PDF p. 1, problem 1; other problems screened out | Median of two sorted arrays and comparison lower-bound prompt | Supplement; same university counted once |
| Cornell, CS4820 Spring 2024 | February 28 median-note availability and format screened; handwritten PDF acquired; March 1 guessed URL unavailable | Potential randomized-analysis alternative | Not used to support substantive claims; no full-reading claim |
| Oxford, B16 2024–25 v2.1; Andrea Vedaldi | Contents screened | Broad data-structure treatment, but less direct selection coverage | Not selected as a core selection course |
| UC Irvine, ICS161; David Eppstein | Identified historical selection URL returned 404 | Potential selection alternative | Unavailable at recorded endpoint; not counted |

## Synthesis and corrections

1. CMU uses zero-based selection indices; this chapter uses one-based ranks and explicitly converts to array index. MIT and Stanford descriptions that isolate a single pivot require distinctness, while Berkeley's equal block supports duplicates. The chapter adopts a three-way contract throughout.
2. A course's sample median is not the global median. Stanford's abbreviated median-of-medians pseudocode leaves fractional ranks implicit; our executable rank is `(len(M)+1)//2`.
3. CMU's idealized good-pivot proof suppresses rounding. Our finite phase proof uses a conservative 7/8 shrink factor for all sizes at least eight and a separately bounded base range. No substitution of `T(E[X])` for `E[T(X)]` is used.
4. MIT's finite induction includes the ceiling contribution: the sum of child bounds is at most `0.9n+7`. The chapter retains a fixed base range through 140 and chooses a sufficient coefficient for the linear induction.
5. Stanford's groups-of-three concept check concerns the displayed recurrence. Its solution does not establish a matching lower bound for every execution of an implementation. The chapter preserves this distinction.
6. Princeton's asymptotic expected comparison constant is implementation-dependent. It is not assigned to our three-way classifier. The decision-led models record their own stated operations and counters.
7. Princeton's searching exercise page contains historical illustrative code and a reversed two-sum hint. We give an independent invariant-based solution and guard empty/out-of-range boundary indices. We do not reproduce its code as authoritative executable code.
8. Worked questions are original or independently reconstructed tasks with exact attribution; entire copyrighted course problem sets are not copied. Three checked Iranian items are labelled authentic revisits or searching bridges, not misrepresented as direct quickselect examination questions.

## Traceability

Raw public source files were obtained into an external temporary reading cache. `a_select-evidence/acquisition.json` records URLs, page counts, paths and SHA-256 hashes. Reading scope is the table above; acquisition status alone does not imply review. The lesson references contain the direct primary URLs. Mathematical properties are independently derived in the lesson and audited with finite checks where appropriate.

The three Iranian original PDF pages were rendered and inspected on 2026-10-06. Archive commit: `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`. All answer options retain the printed ordering. Solutions are independently derived and are not official answer keys. The archive sample is not represented as an exhaustive analysis of every historical examination.
