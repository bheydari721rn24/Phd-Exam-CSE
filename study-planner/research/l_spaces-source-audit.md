# Vector Spaces: Source Selection and Reading Audit

## Selection boundary

Seven university course candidates were identified through official teaching pages and written materials. Six relevant text sets were read; the Berkeley scanned candidate was screened for access and topic titles but was not fully read and is not counted as a reviewed core. Four courses from four universities were selected for complementary proof, computation, and application coverage. This documented pool is finite; “all courses in the world” is not a verifiable search boundary. Course age was not used as a proxy for mathematical correctness.

## Four core courses and exact locations

| University | Course and instructor | Written document and reading | Contribution |
|---|---|---|---|
| Oxford | M1 Linear Algebra I, Michaelmas 2022; Andrew Wathen, course lecturer | [Course](https://courses.maths.ox.ac.uk/course/view.php?id=609); [lecture_notes22.pdf](https://courses.maths.ox.ac.uk/pluginfile.php/25471/mod_folder/content/0/lecture_notes22.pdf?forcedownload=1), PDF pages 26–44 and 47–52 | Abstract axioms, span, independence, exchange, basis, finite dimension |
| ETH Zurich | Linear Algebra 401-0131-00L, HS2024; Bernd Gaertner and Robert Weismantel; notes by Gaertner | [Course](https://ti.inf.ethz.ch/ew/courses/LA24/index.html); [notes_part_I.pdf](https://ti.inf.ethz.ch/ew/courses/LA24/notes_part_I.pdf), PDF pages 114–132, sections 4.1–4.2 and computational bridge | Precise field and subspace hypotheses, Steinitz exchange, constructive basis arguments |
| MIT | 18.06SC, Fall 2011; Gilbert Strang | [Session 1.9](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/ax-b-and-the-four-subspaces/independence-basis-and-dimension/); summary PDF pages 1–3; Problems 9.1–9.2 and solution PDF pages 1–2 | Pivot columns, coefficient dependencies, rectangular matrices, connected differences, equation-defined planes |
| Stanford | EE263, Autumn 2007–08; Stephen Boyd | [Course](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/); [Lecture 3](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/lin-alg2.pdf), PDF pages 1–11, slides 3–1 through 3–22 | Range and kernel, coordinate representations, measurement ambiguity and coordinate-reading functionals |

The Oxford lecturer attribution identifies the course, not an unsupported claim about the authorship of every line of its PDF. The ETH instructor attribution is verified on the actual HS2024 course page. PDF page numbers above are physical page indices, starting at one. The acquisition manifest retains URLs, byte hashes and page counts; reading.json records the actual reading boundary and mathematical corrections.

## Compared candidates

| Candidate | Actual review | Selection decision |
|---|---|---|
| CMU, William Gunther, 21-241 Summer I 2014 | Abstract spaces, week 5/22.pdf, four pages; bases, week 6/23.pdf, four pages. The course calendar dates differ from document dates. | Not a core: concise exposition and multiple substantive statement errors requiring correction. |
| Harvard, Oliver Knill, Math 21b Spring 2023 | lecture04.pdf, both pages | Useful compact computational review, but insufficient detailed exchange and sum/intersection proofs for the present scope. |
| UC Berkeley, Alexander Paulin, Math 54 Spring 2018 | Four accessible scanned notes: vector spaces and linear transformations; subspaces/kernels/ranges; spanning/independence/dimension; bases/coordinates. Titles and access screened only. | Not counted as a fully reviewed course. |

## Corrections discovered during reading

1. Oxford PDF page 37 labels three-coordinate vectors as elements of the two-dimensional coordinate space and interchanges terms in two coefficient equations. The conclusion remains true, but the displayed data require correction. Page 39 prints the vector (0,2,−1) for the plane x + 2y + z = 0; substitution gives three rather than zero. The corrected vector is (0,1,−2). Both pages were visually inspected.
2. Oxford PDF page 50's minimal-spanning argument does not need the claim that deleting one redundant vector immediately leaves an independent list. That claim is false in general; the smaller spanning list already contradicts minimality. The chapter gives the valid finite deletion and exchange proofs.
3. ETH PDF page 119's subspace lemma must require the zero vector in the subset, not merely in its ambient space. The accompanying proof uses the correct requirement. Page 123's real geometric series needs absolute value below one. Page 127 changes coefficient notation in an exchange denominator. None of these slips is propagated into the chapter.
4. MIT Session 1.9 summary page 3 prints an incorrect null vector for equal first and fourth columns. The valid relation has opposite coefficients on those columns. The page was visually checked; multiplication independently verifies the correction.
5. Stanford slide 3–8's infinite-dimensional shorthand must mean no finite basis; it does not mean that an algebraic basis cannot be infinite. The chapter distinguishes finite linear combinations from convergent series.
6. CMU bases PDF page 3 incorrectly calls sine and cosine dependent, and page 4 incorrectly calls a list longer than the dimension independent. Both statements were visually checked and rejected. Evaluation at zero and pi/2 proves the independence of sine and cosine, while exchange proves the dimension bound.

Finding errors in a source does not by itself invalidate an entire course. Selection used explanatory coverage, provable structure and cross-checkability; every adopted statement was reconciled with the other sources or independently proved.

## Synthesis map

Sections 2–10 combine Oxford and ETH's abstract development with MIT's coefficient interpretation. Section 11 and the editable laboratory make MIT's original-versus-reduced column distinction explicit. Sections 12–14 transfer the same arguments to function, polynomial and structured matrix coordinates. Sections 15–18 independently prove the sum/intersection and directness results from adapted bases. Sections 19 and 23 combine coordinate functionals and Stanford's measurement interpretation. Quotients, scalar restriction, finite-field counts and parameter branches are independently derived extensions with complete assumptions, rather than claims that every core course covers every extension identically.

Problems 71 and 72 explicitly reconstruct and extend MIT Problems 9.1 and 9.2. Their numerical data or scope are changed and solutions are independently written. Problem 5 reconstructs a CMU nonexample with an independently explained axiom failure. Problem 73 is original, calibrated to Stanford's range/kernel interpretation. The remaining items identify their original status or their authentic-exam generalization. No copied assignment solution or full copyrighted source corpus is republished.

## Original examination checks

Two authentic items were visually read in the repository PDFs pinned to commit bdadf6e2c9cadc4772ae137a96a3da753c7cfd08. MSc CS 1405 Q41, PDF page 9, tests dimension of symmetric trace-zero matrices. PhD CS 1404 Q31, PDF page 8, tests the projection defined by an orthonormal basis. The English adaptations retain all options in their original order. Their answer derivations are independent and are not represented as official keys. File hashes and exact repository paths appear in l_spaces-authentic.json. PhD CS 1405 pages 6–11 were also screened; their nearby linear-algebra questions concern other topics and were not inserted merely to increase the authentic count.

## Remaining limits

The course pool and examination selections are documented samples, not worldwide or archive-wide exhaustive reviews. Infinite-dimensional topics are boundary explanations rather than a course in functional analysis. Four core courses support the central scope, but not every extension appears in all four. Scientific validity is checked by explicit assumptions, proofs, exact computations and independent counterexamples; no literal guarantee about every future unseen examination is asserted.
