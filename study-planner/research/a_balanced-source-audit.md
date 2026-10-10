# Written course selection: balanced search trees

## Search scope and decision

The search evaluated eight accessible offerings or official written-material candidates: MIT 6.006 Fall 2011; CMU 15-122 Fall 2026; Princeton COS226 Spring 2023; Stanford CS166 Spring 2026; Berkeley CS61B Spring 2014; ETH Zurich Datenstrukturen und Algorithmen Spring 2020; Oxford Algorithms and Data Structures 2023–2024; and the older Princeton COS226 Fall 2005 balanced-tree slides. This is a bounded, reproducible survey, not a claim that every course worldwide has been inspected. An official syllabus was not counted as a read lecture.

The four core courses were selected for complementary mathematical coverage, explicit invariants, implementation contracts, precise diagrams and accessible written evidence. CMU is strongest for AVL pointer and height contracts; MIT supplies the minimum-node argument and edge-height convention; Princeton supplies the precise 2–3/LLRB correspondence and full implementation; Stanford supplies the general red-black/2–3–4 correspondence, cost-model distinctions and augmentation argument. Berkeley Lecture 27 is an additional genuinely read comparison of top-down multiway insertion and deletion. No prestige-only or random selection was used.

| Candidate | Material actually inspected | Decision and limitation |
|---|---|---|
| CMU 15-122, Frank Pfenning, Fall 2026 | All 29 pages of Lecture 16, including 11 exercises and sample solutions | Core: AVL contracts and rotation reasoning; deletion and the height proof require independently supplied extensions. |
| MIT 6.006, Erik Demaine and Srini Devadas, Fall 2011 | All eight pages of Lecture 6 | Core: height recurrence and rotation cases; printed Fibonacci index and insertion commentary require correction. |
| Princeton COS226, written material by Robert Sedgewick and Kevin Wayne, Spring 2023 archive | All 45 PDF pages, §3.3 booksite and the full linked RedBlackBST.java listing | Core: specific 2–3 LLRB variant; do not transfer classical red-black rotation counts to this algorithm. |
| Stanford CS166, Keith Schwarz, Spring 2026 | All 58 and 66 condensed slides for Lectures 6 and 7 | Core: multiway isometry and augmentation; two/three rotation claims concern the classical red-black algorithm. |
| Berkeley CS61B, Jonathan Richard Shewchuk, Spring 2014 | All 195 text lines of Lecture 27 via official web text | Additional: top-down 2–3–4 insertion/deletion. Native retrieval failed; no file hash is invented. |
| ETH Zurich, Spring 2020 | Official course schedule and written-material link inventory | Screened: relevant AVL offering; English handout itself not read, so not used as a core source. |
| Oxford, Paul Goldberg, Hilary 2024 | Official course syllabus and material links | Screened: red-black and splay topics; syllabus is not evidence of a lecture being read. |
| Princeton, Fall 2005 | Official search-index description of balanced-tree slides | Screened older alternative; modern 2023 LLRB slides and Stanford's general correspondence selected instead. |

## Exact written references

1. [CMU 15-122 Lecture 16: AVL Trees](https://www.cs.cmu.edu/~15122/handouts/lectures/16-avl.pdf), Frank Pfenning, Fall 2026, 29 PDF pages. SHA-256: `e54da27f0b8a73151d924be517642543c183384e69791706bdf4706a1380adb3`.
2. [MIT 6.006 Lecture 6](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/83cdd705cd418d10d9769b741e34a2b8_MIT6_006F11_lec06.pdf), Fall 2011, eight PDF pages. SHA-256: `b4835818a5ba89b2e82b9abda0ff42d8445217b1256a112b8e1c8ae14d9f1209`.
3. [Princeton COS226 §3.3 slides](https://www.cs.princeton.edu/courses/archive/spring23/cos226/lectures/33BalancedSearchTrees.pdf), Sedgewick and Wayne, updated 2 March 2023, 45 PDF pages; slide labels skip numbers, so page references here use PDF pages. SHA-256: `2cb5150a0586c0cfe4584bde286d76fde8e39e92a3ea6727e26373cf46e82658`.
4. [Princeton §3.3 booksite](https://algs4.cs.princeton.edu/33balanced/) and [RedBlackBST.java](https://algs4.cs.princeton.edu/33balanced/RedBlackBST.java.html). The page, exercises and entire public code listing were reviewed, including deletion preconditions and metadata refresh. The public listing is a reference, not a wholesale copied implementation.
5. [Stanford CS166 Lecture 6 condensed slides](https://web.stanford.edu/class/archive/cs/cs166/cs166.1266/lectures/06/Condensed%20Slides.pdf), 58 pages, SHA-256 `ee5433eea7aab338509ab1ad71249af07e5780d65c74ad136978809190175f69`; [Lecture 7 condensed slides](https://web.stanford.edu/class/archive/cs/cs166/cs166.1266/lectures/07/Condensed%20Slides.pdf), 66 pages, SHA-256 `e22fc73fa01e0577f6b682c72692dbc6ef4c28b6528b031358ec7a4f0c18e198`. [Course home](https://web.stanford.edu/class/archive/cs/cs166/cs166.1266/) establishes the Spring 2026 offering and Keith Schwarz as instructor; the inherited copyright footer says 2025 and is not used as the offering date.
6. [Berkeley CS61B Lecture 27](https://people.eecs.berkeley.edu/~jrs/61b/lec/27), Jonathan Richard Shewchuk, 2 April 2014, 195 lines of official written text. Retrieved through the web reader after native HTTPS retrieval failed.
7. Screening only: [ETH Zurich Spring 2020 schedule](https://lec.inf.ethz.ch/DA/2020/), [Oxford 2023–2024 syllabus](https://www.cs.ox.ac.uk/teaching/courses/2023-2024/algorithms/), and [Princeton Fall 2005 alternative](https://www.cs.princeton.edu/courses/archive/fall05/cos226/lectures/balanced.pdf).

## Reconciliation and independently checked corrections

- CMU uses empty height zero and singleton height one; this chapter consistently uses empty height minus one and singleton zero. Every recurrence base case is translated, not merely relabelled.
- MIT PDF page 3 prints an inconsistent Fibonacci subscript. With the chapter's convention the exact minimum is F_(h+3) minus one. Small base cases and induction establish the correction. Its page 5 wording about several rotations is separated into multiple primitive rotations within one insertion repair site, versus multiple deletion repair sites.
- CMU PDF page 27's suggested contracts do not by themselves make every rotation return an AVL tree. A rotation of an already perfect three-node tree supplies a counterexample. Our structural primitive promises ordering/content preservation and metadata correctness; a stronger balance postcondition is asserted only with the exact height-case hypotheses. The strict outer-height comparison in CMU's insertion helper is not reused for deletion's balanced-heavy-child case.
- Princeton's completed 2–3 LLRB tree excludes persistent right-red links and four-nodes. General red-black trees can encode 2–3–4 nodes and allow a black node with two red children. Their insertion/deletion procedures and rotation bounds are named separately.
- Stanford's order parameter is minimum degree: nonroot key capacity is b−1 through 2b−1, with a root exception. It is not the maximum-child convention used by some books. A page-41 integer minimization suggestion rounds the continuous optimum e down; under the stated b/ln(b) objective, comparing integers gives b=3, not b=2. This numerical correction does not select a universally optimal practical fanout or suppress block-access costs.
- Weak duplicate bounds in Berkeley are replaced by this chapter's strict distinct-key policy. Multiplicities are stored in one node when needed. The top-down and bottom-up multiway variants may produce different valid shapes.
- Complexity upper bounds describe worst-case routes under constant-cost comparisons and metadata. Root hits, absent deletion and tiny trees need not take Theta(log n) actual time. Full certification is linear and is not invoked after every production update.

## Scope and originality

The lesson supplies its own complete AVL insertion/deletion proof and implementation, exact height/counting arguments, general red-black repair case analysis, a distinct LLRB implementation route, multiway split/borrow/merge reasoning, and applications of augmentation. Sources are credited by section and in the final references. Course-pattern questions use independently chosen data and original complete solutions. Entire copyrighted exercise collections are not reproduced. Source access, implemented lab domains and unproved advanced extensions are declared rather than represented as universal certainty.
