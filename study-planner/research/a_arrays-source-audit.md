# Arrays and Linked Lists: written-source selection audit

## Selection method and honest boundary

Seven university course candidates were screened for accessible written instruction, match to the chapter, proof quality, implementation invariants, solved/exercise families, and complementarity. The four primary courses are MIT 6.006, Berkeley CS61B, Oxford B16, and Princeton COS226. Stanford CS106B is a fifth reviewed written course; selected Cornell CS2110 sections add a sixth complementary course. This is not an exhaustive inventory of every university course worldwide. CMU's linked handouts could not be read and are not counted as reviewed. A course index does not count as reading its instruction.

| Candidate | Actual reading | Selection rationale and limitations |
|---|---|---|
| MIT 6.006 Spring 2020 | Browser PDF, Recitation 2, all pages 1–9 | Primary: sequence interface, arrays, linked lists, resizing, Floyd exercise, indexed-list adapter. Local download timed out; no local source hash asserted. Historical runtime-specific capacity formula is not treated as current universal behavior. |
| Berkeley CS61B | Downloaded written Chapters 4 and 5, complete relevant list design | Primary: sentinel invariants, cached size, tail-removal and circular DLL contrasts. Course index screened for discovery only. An apparent source typo about special cases is corrected by the actual invariant. |
| Oxford B16 2024 | Chapter 3 §§3.1, 3.2, 3.5 read in browser and cached text | Primary: array shift ordering, implementation contracts, ownership. Stack/queue sections screened but deferred. Language-specific pseudocode conventions are not represented as actual Python semantics. |
| Princeton COS226 Spring 2026 | Stacks and Queues I, PDF pages 21–34; interface pages screened | Primary: geometric copying, hysteresis, deterministic amortization, latency contrast. Algorithm arguments used without importing next chapter's ADT teaching. Implementation growth-factor table is not generalized to every runtime. |
| Stanford CS106B Handout 21, 2008 | All four written pages | Complement: iterative freeing, recursive reverse printing, sorted insertion. Iterative and recursive examples have different duplicate policies; independently authored lesson states this rather than copying inconsistent code. |
| Cornell CS2110 Fall 2025 | Lecture 13 invariant passage and exercises on DLL/circular variants | Complement only within recorded scope. Lecture 12 introductory interface passage screened; no claim all lectures were read. Local download failed but browser text for selected sections was available. |
| CMU 15-122 Spring 2024 | Official handout index only; linked unbounded-array PDF unavailable | Excluded from reviewed source count. Access failure is not an assessment of academic quality. |

The first four jointly cover direct indexing, safe shifts, geometric amortization, shrink hysteresis, singly and doubly linked invariants, and representation costs. Stanford strengthens lifetime and recursion reasoning. Cornell reinforces an independently specified sentinel invariant. Four courses were selected for complementary chapter coverage, rather than selected at random or ranked by institutional prestige alone.

## Concept-to-source synchronization

| Chapter sections | Primary grounding | Independent extension and check |
|---|---|---|
| 2–3 | MIT pages 1–3; Oxford §3.1 | Exact shift counts, biased expectations, overlap counterexample, batch insertion order |
| 4–5 | MIT pages 6–7; Princeton PDF pages 21–34 | General-factor sums, initial potential, full quarter-shrink proof, two-buffer peak memory |
| 6–7 | MIT pages 4–5; Berkeley Chapters 4–5; Cornell selected invariants | Object identity limits, six-write range splice, size-maintenance cost, same-list preconditions |
| 8 | Stanford pages 1–4; Oxford §3.5 | Reversal region invariant, exact writes, iterative versus recursive storage |
| 9–10 | MIT pages 8–9 | Meeting congruence and entry proof, nonstandard-speed counterexample, list binary-search traversal models |
| 11–12 | Oxford linked-list reasoning; Stanford insertion | Stable merge, compaction, rotation, shared ownership, alignment and locality models |
| 13 | Source-checked PhD CE 1405 Q18; independent matrix algebra | Orthogonal schematic, general matrix versus rank-one factorization, zero-divisor counterexample |

## Examination provenance

Original PDFs were rendered and visually inspected for PhD CE 1405 Q18 (physical page 5) and MS CS 1393 Q167 (physical page 34), from immutable repository commit `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`. The MS item is an explicitly identified revisit. Its option guards are corrected against the scan in this chapter; earlier derived metadata was not blindly reused. Answers here are independent derivations, not official keys. PhD Q18 is a representation-suitability question; its explanatory condition is stated rather than claiming that other structures cannot do matrix arithmetic.

The original/course-derived bank is independently worded and does not reproduce entire copyrighted course exercise sets. Exact numerical answers are checked by simulations and algebra; general theorems retain proofs. Four-university reading is documented, but literal scientific infallibility and guaranteed scores on future questions cannot be established.

## Local evidence

`a_arrays-downloads.json` records actual download status, URLs, paths, and SHA-256 values. `a_arrays-reading.json` distinguishes actual reading from access/discovery. `a_arrays-authentic.json` records immutable examination paths and PDF hashes. `a_arrays-verification.json` and browser evidence record the checks actually executed; no intended check is labeled passed before execution.
