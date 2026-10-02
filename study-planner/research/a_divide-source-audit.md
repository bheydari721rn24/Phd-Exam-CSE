# Divide and Conquer: Source Selection and Reading Audit

This is a chapter-specific comparison of a bounded public candidate pool, not a ranking of every course in the world. A university's reputation alone is insufficient: accessible written material, exact relevance, proof quality, implementation detail and complementary coverage determine selection. Unread pages are not counted as reviewed material.

## Candidate comparison

| University and written course | Inspection and relevance | Selection |
|---|---|---|
| UC Berkeley, CS170-associated Algorithms reader, Chapter 2, Sanjoy Dasgupta, Christos H. Papadimitriou and Umesh V. Vazirani | PDF pages 1–9 and 12–36 read. Integer multiplication, block matrices, polynomial evaluation, FFT, inverse transforms and the full exercise list were examined. Pages 10–11 on selection were not relied upon. | Principal: the strongest breadth match in this pool; the algebraic backbone. |
| Carnegie Mellon, 15-451/651 Spring 2021, Danny Sleator and David Woodruff | Deterministic closest-pair lecture, April 27, 2021: PDF pages 1–3 read, original page 3 rendered and inspected. Randomized sections on pages 4–5 were screened but are outside scope; image-only code on page 6 was not used. | Principal: geometric proof, maintaining two orders and linear combination. |
| MIT, 6.006 Spring 2020, Erik Demaine, Jason Ku and Justin Solomon | Recitation 3: all seven PDF pages read. Search, sorted-array representations, merge code, recurrence reasoning and stability exercise checked. | Principal: representation and merge implementation obligations. |
| Stanford, CS161, Gregory Valiant, Lecture 2 | All seven PDF pages read. Hosted by the Winter 2017 course page; the actual notes carry September 28, 2016 and name scribes Michael P. Kim (2015) and Ofir Geri (2016). | Principal: merge induction, invariants, recurrence and operation models. |
| ETH Zurich, Data Structures and Algorithms 2018, Felix Friedrich | Handout 2, PDF pages 7–13 read, slides 97–121. Maximum-subarray definitions, cubic/quadratic/divide-and-conquer/linear methods and input-reading lower bound compared. | Selected supplement: strengthens maximum-subarray instruction and the distinction between empty and nonempty intervals. |
| Princeton, COS423 Spring 2013 archive, Kevin Wayne's Divide-and-Conquer II slides | Written deck acquired and topical contents screened. Local extraction has encoded glyphs; a complete reliable page review was not completed. | Candidate only; not counted among genuinely reviewed courses and no exercise attributed to it. |
| Oxford, Algorithm Design Hilary 2022, Elias Koutsoupias | Official syllabus and available divide-and-conquer deck screened. Full relevant deck was not read. | Candidate only; not counted as a reviewed source. |
| Cornell, CS2110 Summer 2019 sorting lecture | Brief course lecture page inspected; linked slides not read. | Candidate only; its brief page adds less depth than the selected merge sources. |

## Selection reasoning and coverage

Four principal university courses are selected for distinct teaching responsibilities rather than chosen at random. Berkeley supplies broad algebraic coverage; CMU supplies the most useful geometric material; MIT supplies concrete representation and boundary checks; Stanford supplies complementary proof exposition. ETH is an additional genuinely reviewed fifth university because the four principal extracts do not adequately develop maximum subarrays. There is no claim that this combination is globally optimal.

| Chapter component | Evidence used | Added instruction and audit obligation |
|---|---|---|
| Search and merge | MIT Recitation 3; Stanford Lecture 2; Berkeley §2.3 and exercises 2.14, 2.16–2.19 | Half-open intervals, exhaustion, multiset preservation, stable ties, strict inversion counting and exact memory accounting. |
| Maximum subarrays | ETH slides 102–121 | Nonempty contract, all-negative cases, four-component associative summaries, witnesses and an independently checked laboratory. |
| Closest pair | CMU pages 1–3; Berkeley exercise 2.32 | Membership by rank and ID, duplicate preprocessing, half-specific cell occupancy and preservation of y-order. |
| Integer multiplication | Berkeley §2.1; exercises 2.1, 2.25–2.26 | Odd widths, difference-product variant, signs, carries and bit-cost qualifications. |
| Matrix multiplication | Berkeley §2.5; exercises 2.11, 2.27 | Ordered block products, all four cancellation proofs and noncommutative counterexamples. |
| Polynomial multiplication and FFT | Berkeley §2.6; exercises 2.7–2.10, 2.28–2.30 | Primitive roots, normalization, zero padding, inverse proof, exact modular alternative and numerical limitations. |

## Differences requiring explicit treatment

1. MIT's displayed merge uses a strict left comparison and explicitly invites a stability repair. The new implementation takes the left item on equality.
2. Stanford's illustrative merge assumes distinct values and leaves exhaustion incomplete. The new contract admits duplicates and checks exhausted halves before indexing.
3. Berkeley's queue-based merging is not automatically stable across original runs: three equal tagged items can emerge in a different run order. Contiguous bottom-up runs preserve that order.
4. ETH's initial nonempty-looking statement and zero-initialized algorithms require a policy choice. This chapter uses nonempty intervals throughout; the empty-allowed variant is separately explained.
5. CMU's geometric cell explanation needs a qualification when points from opposite halves are mixed. The packing guarantee is within each half. The chapter gives the colored-half proof, including tied x-coordinates.
6. Berkeley's odd-width multiplication presentation needs explicit low-part width for the shifts. Its sum-product variant also allows a carry bit; the difference variant avoids that operand-width increase.
7. The unnormalized Fourier matrix does not preserve Euclidean norm. It satisfies F*F = N I; only F divided by the square root of N is unitary.
8. FFT operation counts are arithmetic-operation counts. Floating-point roundoff and growing integer sizes require separate treatment.
9. Berkeley exercise 2.23's reduced-majority hint must not be treated as an unrestricted equivalence: the reduced list can acquire a majority absent from the original. The new problem bank supplies a counterexample and requires final verification in the original array.

## Exercise coverage and copyright boundary

The problem bank contains original questions and independently written solutions. Its coverage map identifies relevant source exercise families; it does not reproduce whole course assignments. Selection/quicksort, recurrence-only exercises and randomized geometry are assigned to their own later chapters. The complete Berkeley exercise list was inspected to locate relevant families, not silently incorporated as a claim of full-course coverage. National entrance-exam archives remain deferred until the final month.

## Reproducibility and limits

The download manifest records seven PDF URLs, page counts and SHA-256 values. Temporary downloaded PDFs remain read-only research references. The visible lesson is independently authored. Source comparison, executable checks and visual QA support the specified chapter boundary; none proves success on every unseen examination question. The public candidate pool is finite and may miss superior inaccessible or newly released material.

## Direct written references

- MIT: [6.006 Recitation 3](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/1869dbf640ded6b31f1bd369d2001ef5_MIT6_006S20_r03.pdf).
- Stanford: [CS161 Lecture 2](https://theory.stanford.edu/~valiant/cs161/CS161Lecture02.pdf), [course page](https://theory.stanford.edu/~valiant/cs161/).
- UC Berkeley: [Algorithms, Chapter 2](https://people.eecs.berkeley.edu/~vazirani/algorithms/chap2.pdf).
- CMU: [Closest Pair lecture](https://www.cs.cmu.edu/~15451-s21/lectures/lec21-closest-pair.pdf), [15-451/651 Spring 2021](https://www.cs.cmu.edu/~15451-s21/).
- ETH Zurich: [Handout 2](https://lec.inf.ethz.ch/DA/2018/slides/daLecture2.en.handout.2x2.pdf), [2018 course](https://lec.inf.ethz.ch/DA/2018/).
- Screened candidates: [Princeton written deck](https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/05DivideAndConquerII.pdf), [Oxford syllabus](https://www.cs.ox.ac.uk/teaching/courses/2021-2022/algdesign/), [Cornell sorting page](https://www.cs.cornell.edu/courses/cs2110/2019su/lectures/lec17-sorting.html).
