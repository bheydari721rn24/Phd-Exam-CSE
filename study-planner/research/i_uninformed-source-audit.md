# Uninformed search: source selection and reading audit

Reviewed 8 October 2026. The candidate pool is bounded by accessible written material; it is not an inspection of every course worldwide. The lesson, proofs, code, numerical examples and diagrams are independently authored. A course catalogue is never counted as a read lecture.

## Four selected university courses

| Course | Material actually read | Selection and qualification |
|---|---|---|
| UC Berkeley CS188 | Complete written textbook section 1.3, Uninformed Search, including generic pseudocode and DFS/BFS/UCS properties | Compact common framework. Its infinite-space completeness claims need finite branching and a finite sublevel set; its complexity counts need a declared goal-test convention. The textbook is a staff resource without a named term-specific lecturer. Summer 2024 lecture cover was screened and names Eve Fleisig and Evgeny Pobachienko, but the full 102-page deck is not claimed as read. |
| CMU 15-281, Spring 2023, Stephanie Rosenthal | Course-linked staff Search Notes: problem, tree/graph, uninformed algorithms, worked traces, properties and their explanations; Lecture 2 activity solutions, all three pages | Explicit frontier replacement and state modelling. The generic no-duplicate pseudocode is not sufficient for UCS without relaxation. Its sample IDS explored-set trace can lose the shallow solution; the chapter independently demonstrates why depth-sensitive handling matters. |
| MIT 6.034, Spring 2005, Leslie Kaelbling and Tomas Lozano-Perez | Complete 21-page written notes, Sections 2.1–2.3, Search I, including terminology, frontier implementation, visited/expanded distinctions, DFS/BFS and progressive deepening | Valuable implementation distinctions. The notes use a particular visited-on-generation convention and call a popped goal expanded. The chapter declares a different explicit count convention. The notes' average progressive-deepening ratio is not substituted for our independently derived exhaustive-iteration ratio. |
| Edinburgh INF2D | Complete extracted text of Lecture 3, Search Strategies, all 57 PDF pages, plus Lecture 2 formulation and node implementation sections | Broad DLS/IDS treatment and an explicit finite-space DFS qualification. Lecture 3 page 3 defines depth by least-cost solution; we instead use shallowest goal depth and keep optimal cost separate. No individual lecturer is named in this 2025-path PDF; current course team is Wenda Li, Nadin Kokciyan and Craig Innes, not an invented author credit. |

## Compared candidates and supplementary reading

- Stanford CS221, Summer 2012–2013, Chris Piech; Search problem set by Chris Piech and Percy Liang: complete assignment text read. Selected as a fifth supplementary course for a new, independently worded text-segmentation exercise. Informed-search and autonomous-TA subproblems are deferred to their proper chapters. The guessed handout URL failed; it is not counted as read.
- Stanford CS221, Autumn 2012–2013, Percy Liang: official schedule verified; linked one-page search lecture fetch failed. Excluded from the read-source count.
- Oxford Artificial Intelligence, Hilary 2026, Sara Bernardini: catalogue screened; protected lecture text was not obtained. Excluded from the read-source count.
- ETH Zurich: search surfaced a library book table of contents rather than an accessible taught-course lecture. Excluded, without attributing the book to an ETH course.
- Berkeley CS188 Summer 2022 midterm search section was located, but a complete exam problem was not yet read; it is a candidate, not a used question source.

## Independent synthesis decisions

The chapter supplies its own counterexamples for premature UCS goal testing, visited-on-generation errors, stale priority entries, zero-cost starvation, shrinking positive edge costs, negative edges, depth-limited duplicate pruning, and unsound bidirectional first-contact stopping. It derives both goal-on-generation and goal-on-removal counting bounds, distinguishes expansions from generations, proves the UCS frontier-cut invariant, and derives exhaustive IDS counts rather than copying a summary table. Exact trace models are computed from the declared graph, not from unverified source pictures.

Web full-text retrieval was used for the read material. No local source-byte hashes or visual checks of inaccessible university diagrams are claimed. Original Iranian examination adaptations, when included, are checked separately against locally available original PDF pages. Complete copyrighted course problem sets are not reproduced; attributed reconstructions use changed data and independent solutions.

## References

- [UC Berkeley CS188, Uninformed Search](https://inst.eecs.berkeley.edu/~cs188/textbook/search/uninformed.html).
- [UC Berkeley CS188 Summer 2024 lecture cover and candidate deck](https://inst.eecs.berkeley.edu/~cs188/su24/assets/lectures/cs188-su24-lec02.pdf).
- [CMU 15-281 Spring 2023 course and instructor](https://www.cs.cmu.edu/~15281-s23/).
- [CMU staff Search Notes](https://www.cs.cmu.edu/~15281/coursenotes/search/).
- [CMU Lecture 2 activity solutions](https://www.cs.cmu.edu/~15281-s23/activities/15281_S23_Lecture_2_Activity_Solutions.pdf).
- [MIT 6.034 Spring 2005, Search I written notes](https://ocw.mit.edu/courses/6-034-artificial-intelligence-spring-2005/921a7a2eca07e1721e8c1cac1813f4c6_ch2_search1.pdf).
- [Edinburgh INF2D Lecture 3, Search Strategies](https://opencourse.inf.ed.ac.uk/sites/default/files/https/opencourse.inf.ed.ac.uk/inf2d/2025/inf2dlectureslides-03searchstrategies_0.pdf).
- [Edinburgh INF2D course team](https://opencourse.inf.ed.ac.uk/inf2d).
- [Stanford CS221 Search problem set, Chris Piech and Percy Liang](https://web.stanford.edu/~cpiech/cs221/homework/pset/search.html).
- [Stanford Summer 2012–2013 course](https://web.stanford.edu/~cpiech/cs221/).
- [Stanford Autumn 2012–2013 course](https://stanford.edu/~cpiech/cs221/fall12/).
- [Oxford AI course catalogue](https://www.cs.ox.ac.uk/teaching/courses/2025-2026/ai/).
