# Recursion: written-source selection and reconciliation

Review date: 9 October 2026. Scope: Programming, Week 3, p_recursion only.

## Accessible candidate pool and selection

Candidates were evaluated for accessible written material, instructional precision, execution semantics, proofs, exact costs, and restoration/caching coverage. The selection is a finite reviewed pool; it is not described as every university course worldwide. Scores summarize suitability for this chapter on a five-point scale; they are editorial judgments, not measured university rankings.

| Candidate | Written material actually read | Conceptual coverage | Execution/proof | Advanced complement | Decision |
|---|---|---:|---:|---:|---|
| Berkeley CS61A, John DeNero | Complete Composing Programs 1.7.1–1.7.5 | 5 | 5 | 4 | Core: contracts, mutual and tree recursion, partitions |
| MIT 6.0001, Fall 2016 | Complete extracted text, Lecture 6, 58 PDF pages | 5 | 5 | 5 | Core: frames, induction, Hanoi, memoization |
| Stanford CS106B, Eric Roberts, Winter 2015 | Handouts 14 and 16, six pages extracted text | 5 | 4 | 5 | Core: decomposition, geometry, maze continuations and paths |
| CMU 15-112, Pat Virtue, Fall 2023 | Week 9 Lecture 2, 48 slides extracted text | 5 | 4 | 5 | Core: tracing, debugging, repeated calls, backtracking undo |
| Harvard CS50x 2025, David J. Malan | Notes 3 binary-search, recursion and merge-sort sections | 3 | 3 | 2 | Supplement: C surface syntax and shrinking search |
| Stanford CS106B Summer 2023 | Lecture 8 index inspected; PDF not read | Not scored | Not scored | Not scored | Catalog candidate, not counted as a read course |
| Stanford CS106B Winter 2015 Handout 19A | Extracted headings only; solutions embedded as images | Not scored | Not scored | Not scored | Not treated as a fully reviewed exercise bank |

The four core selections come from four universities and are genuinely read written materials. Selecting Harvard in place of one would weaken coverage of contracts or backtracking. Different Stanford editions are not counted as different universities. Course exercises are reconstructed selectively into original worked variants; no claim is made to reproduce every copyrighted external question.

## Reading evidence and scientific reconciliations

1. Berkeley: its old-edition Fibonacci has bases at indices one and two, while the chapter fixes F0=0 and F1=1. Digit sum, factorial frames, cascade order, mutual parity and partition classes were reconciled with explicit domains. A statement about independent bindings is qualified: mutable pointees and globals can remain shared.
2. MIT: rabbit-count initial values and memo-cache seeds differ from this chapter. The chapter normalizes them before deriving counts. The lecture's size-one Hanoi policy is distinguished from the zero-base construction. Its dictionary-order claims reflect the course's historical Python version and are not reused as modern Python guarantees.
3. Stanford: path-retaining backtracking is distinguished from full state restoration. Maze search with path unmarking is not assigned global-visited O(V+E) complexity. The handout's P/NP discussion is not used as a complexity theorem. Fractal branching is taught through independently generated connected geometry.
4. CMU: the repeated recursive evaluation in alternating-case code motivates reuse and operation counting. Incomplete demonstration code is not copied as a complete implementation. Backtracking's undo policy is reconciled with whether a successful path is retained.
5. Harvard: the C drawing example is supplementary. Informal descriptions of Omega as best case and Theta as equality of best and worst are not repeated as definitions; bound notation and input-case analysis are kept distinct.
6. Primary C rules: N1570 Sections 5.1.2.3 and 6.5.2.2 were read for operand order, indeterminately sequenced function bodies, and permitted direct/indirect recursion. The draft is identified as C11, used only for unchanged C17 rules. Fixed-width arithmetic, unsigned boundaries, automatic lifetime, and missing returned results are explicitly qualified.

## Chapter-to-source map

| Chapter material | Core overlap | Independent extension |
|---|---|---|
| Contracts, termination, induction | Berkeley, MIT, Stanford, CMU | Well-founded measures, stride guards, lexicographic encoding |
| Frames and output order | Berkeley, MIT, CMU, Stanford | C17 expression ordering, pointer identity, static state |
| Tree recursion and exact counts | Berkeley, MIT, CMU | Fibonacci closed counts, bit work, full-tree identities |
| Memoization | MIT, Berkeley conceptual overlap | Requests versus misses, warm cache, complete state keys |
| Hanoi | MIT, Stanford, CMU | Separate calls/moves, optimality cases, checked disk transit |
| Backtracking and restoration | Stanford, CMU, Berkeley partitions | Output-size counts, pruning counterexamples, prefix contracts |
| Geometry | Stanford | Connected Koch replacement and exact call/length formulas |

## Original examination verification

MSc Computer Science 1393, Q167, PDF page 34, was visually rechecked from the pinned archive commit bdadf6e2c9cadc4772ae137a96a3da753c7cfd08. File: Exams/MS/CS/1393/olum_93_konkurcomputer.pdf. SHA256: 7ed89fae8eb601a964355fde5e5d297cbb30844e5240b9e3908b798fb86e349d. All printed options use n<0. The adaptation's options were corrected from the original scan rather than blindly reused from the previous chapter. The answer is independently proved, not represented as an official key. This is a bridge revisit, not a new unique archive item. The same source-backed correction was applied only to Q167 options and explanations in its six earlier chapter adaptations; every other part of those pages was retained.

## Remaining qualifications

Image-only source demonstrations were not counted as read transcripts. The university sources do not all cover every extension: independently proved language and counting material is identified rather than falsely attributed. No source review can certify literal 100% universal coverage or examination performance. The six previous Q167 adaptations were corrected from the source scan without changing their answer, question count, or any content outside that question. Forty other preceding pages remain byte-for-byte unchanged.

Exact human-readable links are listed in the chapter References section; the reading record is research/p_recursion-evidence/reading.json.
