# Binary search trees: source selection and reconciliation

## Scope and method

This is a bounded comparison of accessible written courses, not a claim to have inspected every course worldwide. Candidates were screened for ordering contracts, operation correctness, traversal reconstruction, augmentation, exact cost accounting and exercises. Four complementary core courses were read in full within the scopes below; Stanford was also read as a fifth implementation reference. Our prose, proofs, examples and problem solutions are independently authored. Entire copyrighted exercise collections are not republished.

| Priority | University, course and authors | Material actually read | Selection reason |
|---|---|---|---|
| Core 1 | CMU 15-122 Principles of Imperative Computation; Frank Pfenning, André Platzer, Rob Simmons and Iliano Cervesato | Lecture 15, Binary Search Trees, current PDF labelled Fall 2026, all 22 pages including five exercises and sample solutions | Strong representation contracts, interval validation, root updates and implementation reasoning |
| Core 2 | Princeton COS226 Algorithms and Data Structures, Spring 2024 archive; written slides by Robert Sedgewick and Kevin Wayne | 3.2 Binary Search Trees, all 31 slides, updated 3 October 2023; official Algorithms §3.2 booksite including rank, select, deletion and exercises | Ordered queries, traversal, exact comparison model, random-order distinctions and augmentation |
| Core 3 | UC Berkeley CS61B, Spring 2014, Jonathan Richard Shewchuk | Lecture 24, Trees and Traversals, all 215 text lines; Lecture 26, Binary Search Trees, all 232 lines including footnotes | Parent references, three deletion cases, bracketing queries and traversal applications |
| Core 4 | MIT 6.006 Introduction to Algorithms, Fall 2011, Erik Demaine and Srini Devadas | Lecture 5, Scheduling and Binary Search Trees, all 8 pages | Scheduling application, successor, rank augmentation and height-dependent operations |
| Additional reviewed source | Stanford CS106B Programming Abstractions, Summer 2025, Sean Szumlanski | Lecture 22, More on Binary Trees, all written sections, supplementary deletion code, memory clarification, level-order code and 15 exam-preparation prompts | Predecessor deletion, C++ pointer lifetime, missing-null height bug and sentinel ambiguity |

Native acquisition succeeded for all seven core/additional files. The reading ledger records exact SHA-256 values, page or line ranges and source URLs. These cached references remain outside the published app; only original teaching and source citations are distributed.

## Further candidates screened

Oxford Algorithms and Data Structures 2023–2024 was screened through its official syllabus: ordered trees are covered, but the page alone is not a proof source. ETH Zürich Data Structures and Algorithms HS2016 self-study syllabus explicitly lists traversal, search, insertion and deletion, but screening its topic list is not counted as reading its complete lectures. Stanford's Spring 2025 introductory tree lecture was screened, then the fuller Summer 2025 written deletion lecture was selected. These eight candidate offerings include separate Stanford offerings; they represent seven comparison entries plus that alternative, not eight different universities. No inaccessible material is claimed as read.

## Reconciled scientific differences

1. CMU counts height in nodes; Berkeley counts edges. This chapter uses empty height minus one and leaf height zero, so a path-bound operation costs at most a constant times height plus one. Both conventions describe the same tree.
2. CMU and Princeton use unique keys and replacement values. Berkeley permits equal keys on either side under a weak invariant and inserts equals to the left. We use strict unique keys; a separately proved counted-node multiset changes subtree mass, rank and deletion consistently. A duplicate-side rule must never be silently combined with the unique-key proofs.
3. MIT's rank counts keys less than or equal to the query; Princeton's rank counts strictly smaller keys. We define strict rank and explicitly add the membership term for inclusive rank.
4. Princeton's slide shorthand “one plus depth” applies to searching an existing node. Inserting an absent key at final depth d compares with d existing keys, not d plus one; a null-pointer test is not a key comparison.
5. Stanford's commentary about logarithmic average height needs a specified random model. Uniform insertion permutations and uniform Catalan shapes are different distributions. The latter does not justify the same logarithmic claim. Our expected-depth proof explicitly uses uniform permutations of distinct keys; it is not transferred to arbitrary deletion sequences.
6. Stanford's sum of field widths is not a portable object-size calculation. Alignment and padding can change the actual allocation. Our storage examples state an explicit ABI and separately count allocator overhead.
7. A child-only ordering check is insufficient; a finite acyclic tree with locally ordered children may violate an ancestor bound. Interval validation and strictly increasing inorder are proved equivalent to the global strict invariant under the stated representation assumptions.
8. A successor need not be a leaf: it has no left child but can have a right child. Deleting it must preserve that child. Value copying and physical transplantation have different node-identity effects and are taught separately.

## References

- CMU: [Lecture 15, Binary Search Trees](https://www.cs.cmu.edu/~15122/handouts/lectures/15-bst.pdf).
- Princeton: [COS226 written slides](https://www.cs.princeton.edu/courses/archive/spring24/cos226/lectures/32BinarySearchTrees.pdf); [Algorithms §3.2](https://algs4.cs.princeton.edu/32bst/).
- Berkeley: [Lecture 24](https://people.eecs.berkeley.edu/~jrs/61b/lec/24); [Lecture 26](https://people.eecs.berkeley.edu/~jrs/61b/lec/26); [course home](https://people.eecs.berkeley.edu/~jrs/61b/).
- MIT: [Lecture 5](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/d9c745bbfb610e9e53f6aef4261f3805_MIT6_006F11_lec05.pdf).
- Stanford: [Lecture 22](https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1258/lectures/22-bst/); [Summer 2025 course](https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1258/).
- Oxford: [2023–2024 syllabus](https://www.cs.ox.ac.uk/teaching/courses/2023-2024/algorithms/index.html).
- ETH Zürich: [HS2016 written self-study syllabus](https://cadmo.ethz.ch/education/lectures/HS16/DA/self-study/index.html).
