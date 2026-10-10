# Written course selection: heaps and priority queues

## Survey and selection

The reproducible candidate pool contains MIT 6.006 Spring 2020, CMU 15-122 Fall 2026, Princeton COS226 Spring 2025, Stanford CS106B Spring 2020 and Autumn 2023, Cambridge Algorithms 2023–2024, ETH Zurich Data Structures and Algorithms 2020, Berkeley CS61B Spring 2014, and Oxford Algorithms 2023–2024. It spans nine offerings from eight universities. This is a bounded survey of accessible written material; it does not claim to have inspected every course worldwide. An inaccessible document or a course inventory is never counted as a read lecture.

Four core university sources were selected by complementary coverage, proof quality, implementation precision and accessible written evidence. MIT contributes zero-based representation and the construction/sorting distinction. CMU contributes strengthened loop invariants and contracts. Princeton contributes indexed queues, multiway heaps, practical interfaces and heapsort. Cambridge contributes binomial and Fibonacci heaps, potential analysis and degree proofs. Stanford's fifth-university comparison explains basic repair traces; its limited advanced coverage makes it a complement rather than a substitute for Cambridge or CMU.

| Offering | Material actually read | Decision |
|---|---|---|
| MIT 6.006 Spring 2020; Erik Demaine, Jason Ku, Justin Solomon | All seven pages of Lecture 8, Binary Heaps; page 3 visually rendered to check height notation | Core: representation and build proof; printed height uses a ceiling where the edge-height convention requires a floor. |
| CMU 15-122 Fall 2026; Frank Pfenning | All 13 PDF pages of Lecture 25 and all 24 pages of Lecture 26 via official PDF web text; final proof assumptions and all conclusions read in text | Core: safety, order exceptions, grandparent conditions and client boundaries. Native retrieval failed; no native hash is invented. |
| Princeton COS226 Spring 2025; Robert Sedgewick and Kevin Wayne | All 43 PDF pages of Priority Queues plus the full §2.4 written booksite, exercises and supplied discussion | Core: PQ interfaces, indexed arrays, multiway tradeoffs and heapsort. The slide table places ordinary Fibonacci amortized bounds under a worst-case heading; the chapter corrects that qualification. |
| Cambridge Algorithms 2023–2024; Damon Wischik, with course materials by Frank Stajano | Algorithms 2, PDF pages 53–76 / printed pages 51–74, including binomial recap, Fibonacci algorithms, implementations and analysis; both pages of example sheet 6 | Core: advanced PQs and amortization. Other graph/disjoint-set sections were not used or represented as read for this chapter. |
| Stanford CS106B Spring 2020; Chris Gregg and Julie Zelenski | All 16 written HTML slides on heaps; additional Autumn 2023 written heap page inspected | Additional comparison: repair illustrations and code. Random-input average insertion and incomplete arbitrary-deletion discussion are not promoted to universal guarantees. |
| ETH Zurich 2020 | Course inventory and exact Lecture 11 written-material links | Screened only; not counted as a read teaching source. |
| Berkeley CS61B Spring 2014 | Official candidate listing/search evidence; attempted PDF unavailable | Screened only; not counted as read. |
| Oxford 2023–2024 | Course listing; native connection unavailable | Screened only; not counted as read. |

## Reconciliation and independent corrections

1. All primary executable binary models use zero-based indices. One-based source formulas are translated explicitly, including root and missing-child cases.
2. The edge height of a nonempty complete binary tree is the floor of the base-two logarithm of its size. A ceiling is not interchangeable, even if both give the same asymptotic bound.
3. Repair takes logarithmic worst-case route work and can terminate immediately. A dynamic-array resize can make a single insertion linear. Amortized cost is stated separately.
4. Fibonacci insertion/meld/decrease-key are constant amortized costs for the ordinary structure; extract-min is logarithmic amortized cost. A cascade or consolidation can take linear actual time. No claim about strict Fibonacci heaps is transferred to ordinary heaps.
5. A weakened order invariant excluding one upward edge is insufficient by itself: the displaced parent must remain below the active node's children. The chapter supplies a counterexample and the additional grandparent condition.
6. CMU Lecture 26 page 19 describes a singleton with next equal to one, although its representation requires next equal to two. The chapter distinguishes size from next. Page 21 calls an index-based helper with payloads in its minimum-priority scan; the chapter compares entries directly and does not copy that code.
7. Cambridge page 73 writes a cancellation of an unspecified big-O coefficient against a potential drop. The chapter proves amortization in normalized primitive units and explains scaling; it never subtracts an unknown coefficient as though it were one.
8. Princeton's written min-max heap paragraph reverses the extrema relative to its even-min level invariant. Under root depth zero and even-min levels, the root is minimum and maximum is among its children. The chapter uses that explicit convention.
9. Distinct label counting concerns valid heap arrangements, not sorted orders. Heap construction has a linear comparison lower bound; sorting has a logarithmic-per-item aggregate lower bound.
10. Course exercises are independently reconstructed in selected families with changed data and extended solutions. The bank is not a reproduction of every copyrighted assignment, and no unsolved source exercise is silently described as solved.

## Coverage boundary

This chapter covers exact binary and multiway shape arithmetic, construction, repair proofs, indexed handles, sorting, selection/stream applications, binomial forests and ordinary Fibonacci amortization. It includes a worked survey of min-max and leftist meldable alternatives. Specialized optimal heap-selection proofs, strict Fibonacci heaps, pairing-heap optimal bounds, external-memory queues and language-specific production libraries are outside its claimed scope. The candidate search, problem bank and audits provide evidence, not an infallibility or unseen-examination guarantee.

## Written references

- MIT: [6.006 Lecture 8, Binary Heaps](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/40d4851e550507ca14dc778b9b2266cc_MIT6_006S20_lec8.pdf).
- CMU: [15-122 Lecture 25, Priority Queues](https://www.cs.cmu.edu/~15122/handouts/lectures/25-pq.pdf) and [Lecture 26, Restoring Invariants](https://www.cs.cmu.edu/~15122/handouts/lectures/26-heap.pdf).
- Princeton: [COS226 Spring 2025 Priority Queues slides](https://www.cs.princeton.edu/courses/archive/spring25/cos226/lectures/24PriorityQueues.pdf) and [Algorithms §2.4](https://algs4.cs.princeton.edu/24pq/).
- Cambridge: [Algorithms 2 notes](https://www.cl.cam.ac.uk/teaching/2324/Algorithm1/content/algorithms2.pdf), printed §§7.1–7.8, and [Example sheet 6](https://www.cl.cam.ac.uk/teaching/2324/Algorithm1/ex/ex6.pdf).
- Stanford: [CS106B Spring 2020 written heap slides](https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1206/lectures/heaps/) and [Autumn 2023 priority-queue notes](https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1242/lectures/17-pqheap/).
