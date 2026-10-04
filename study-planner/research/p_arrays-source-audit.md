# Arrays: source selection and reading audit

## Discovery and selection method

The accessible candidate pool comprised Cambridge, CMU, Harvard, UC Berkeley, Stanford, MIT, Princeton and ETH Zurich. Each candidate was examined for public written access, coverage of this chapter's boundary cases, semantic depth and exercise value. Scores are comparative editorial judgments on a five-point scale, not objective worldwide rankings. Four complementary primary courses were selected; Stanford and MIT were added because storage growth and iteration mutation required additional treatment. Six courses from six universities were actually read. No claim is made to have enumerated or read every course offered worldwide.

## Actual reading and contributions

### Cambridge — Programming in C, 2017–18; Neel Krishnaswami

Lecture 3, all 25 slides; arrays and pointer arithmetic slides 2–13, exercise slide 25. Primary: typed array objects, strides and C pointer boundaries. Written access / boundary coverage / semantic depth / exercise value: 5 / 5 / 5 / 4.

[Official written material](https://www.cl.cam.ac.uk/teaching/1718/ProgC/lectures/lecture3.pdf). Document acquisition hashes identify the fetched source in the evidence record.

### CMU — 15-122, Fall 2026; Frank Pfenning and André Platzer

Lecture 03 Arrays, all 19 pages including exercises. Primary: invariants, lengths, segment copying and proof obligations. Written access / boundary coverage / semantic depth / exercise value: 5 / 5 / 5 / 5.

[Official written material](https://www.cs.cmu.edu/~15122/handouts/lectures/03-arrays.pdf). Document acquisition hashes identify the fetched source in the evidence record.

### Harvard — CS50x 2025; David J. Malan

Notes 2: Arrays through Strings, String Length and Command-Line Arguments. Primary: initialization, strings, termination and practical traversals. Written access / boundary coverage / semantic depth / exercise value: 5 / 4 / 4 / 4.

[Official written material](https://cs50.harvard.edu/x/2025/notes/2/). Document acquisition hashes identify the fetched source in the evidence record.

### UC Berkeley — CS61A / Composing Programs; John DeNero

Sections 2.3.1–2.3.5 and 2.4.2 read; sequence construction, slicing and identity. Primary: sequence interfaces, mutability and nested sharing. Written access / boundary coverage / semantic depth / exercise value: 5 / 5 / 5 / 4.

[Official written material](https://composingprograms.com/pages/23-sequences.html). Document acquisition hashes identify the fetched source in the evidence record.

### Stanford — CS106B, Fall 2016; Chris Gregg

Implementing Vector, all 29 slides; core allocation and growth slides 3–28. Selected supplement: geometric growth, capacity, release and lifetime. Written access / boundary coverage / semantic depth / exercise value: 5 / 4 / 5 / 4.

[Official written material](https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1172/lectures/17-ImplementingVector/17-ImplementingVector.pdf). Document acquisition hashes identify the fetched source in the evidence record.

### MIT — 6.0001, Fall 2016; Ana Bell, Eric Grimson and John Guttag

Lecture 5, all 24 slides; list mechanics and aliasing slides 7–23. Selected supplement: cloning, nested aliases and mutation during iteration. Written access / boundary coverage / semantic depth / exercise value: 5 / 4 / 4 / 4.

[Official written material](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/1776670e271578eeb99fc25975f20586_MIT6_0001F16_Lec5.pdf). Document acquisition hashes identify the fetched source in the evidence record.

## Screened alternatives

Princeton Introduction to Programming in Java, section 1.4 Arrays: the introductory written material and exercise catalog were screened. Java bounds checks and array length are useful comparisons but do not supply the core C object-boundary or Python alias explanations selected here. This is not a claim to have read the entire Princeton course. [Written section](https://introcs.cs.princeton.edu/java/14array/).

ETH Zurich D-ITET Informatik I 2019: the syllabus and written-material index were screened. The lecture bodies were not read and the course is not counted among the six reviewed sources. [Course index](https://lec.inf.ethz.ch/itet/informatik1/2019/).

## Reconciliation and corrections

C17, C0, C++, Python and mathematical pseudocode have separate contracts. CMU's C0 arrays are zero-initialized and bounds-checked; C automatic arrays are not automatically initialized and invalid accesses are not defined runtime exceptions. C0's managed allocation is not C's explicit lifetime. Cambridge's convenient statement that array names are pointers is qualified by C array-to-pointer conversion exceptions, row-subarray boundaries and pointer types. Numerical byte contiguity alone does not permit flattening a C matrix through a pointer beyond its first row object.

CMU's overlapping copy contract cannot compare a mutated final source with the target as if the source were immutable. Rightward forward copying [1,2,3,4] produces [1,1,1,1], not the original segment [1,2,3]; leftward copying can also falsify final-source equality. This lesson states an original-input snapshot and proves safe copying direction. The source proof's loB/i versus j notation is normalized in our independently derived invariant. Stanford's qualitative efficiency statement about doubling is replaced by explicit time, unused-capacity and peak-storage tradeoffs; example spelling/address-label inconsistencies are not copied.

Harvard's example integer sizes are platform examples, not universal C sizes. strlen returns size_t, character-classification inputs require the unsigned-char or EOF domain, and strings need capacity for their terminator. Berkeley/MIT shallow copies retain inner identities; immutable outer tuples do not make every referenced object immutable. MIT's older print syntax is replaced by Python 3 syntax in independently authored examples. Unrelated old dictionary-order claims are outside the selected scope.

The Python language reference supplies precise slice clipping, default negative-stop behavior and extended-slice assignment. WG14 N1570 supplies public written C rules for array conversion, pointer arithmetic, array initialization and memory-copy contracts; these selected rules also apply to the stated C17 cases. N1570 is labeled a public C11 draft, not presented as a copy of the published C17 standard.

## Exercise inventory and provenance

The bank has 81 original or explicitly course-inspired tasks and two authentic archive bridge revisits. CMU copying, segment invariants and array filling, Cambridge pointer/slice reasoning and bounded substring-search exercise, Harvard average/string work, Berkeley sequence/alias exercises, Stanford growth analysis and MIT iteration mutation were evaluated for chapter relevance. Relevant problem families are represented by independently written variants and expanded boundary questions; the bank does not reproduce every unrelated source exercise or copyrighted course problem verbatim. Original questions are labeled original. Course-inspired prompts name the university and transformation.

MSc CS 1393 Q167 and PhD CS 1404 Q72 are translated/adapted from their original PDF pages at the pinned repository commit. They are explicit revisits, not new unique archive items. Their source hashes, pages, options and independently explained solutions are recorded separately.

## Coverage boundary

The chapter covers array representation, C pointer domains, indexing, dense/affine/packed layouts, traversal proofs, prefix/difference arrays, overlap, insertion/deletion/reversal/rotation/compaction, Python slices/sharing, C string boundaries and dynamic backing storage. Full sorting, searching data structures and arbitrary graph algorithms belong to later chapters. Finite tests support exact authored examples; they do not prove universal course completeness or guaranteed performance on unseen examinations.
