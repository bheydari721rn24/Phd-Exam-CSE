# Written-source evaluation: rank, invertibility, and solution sets

## Search and selection boundary

Five accessible written course offerings from five universities were individually inspected. The pool was located through official university course indexes and written-material links, then the actual in-scope pages were read. It is a bounded documented pool, not a claim to have enumerated all university courses worldwide. Four primary courses and one additional comparison are used because no single retrieved source supplies all proofs, exact rectangular examples, conceptual interpretations and error checks.

| Candidate | Actual reading | Scientific contribution | Limitation and decision |
| --- | --- | --- | --- |
| Oxford M1, 2022; Andrew Wathen, lecturer | PDF 42–51, 57–61, 68–69; all these pages read | Basis exchange, rank–nullity proof, restriction dimensions, invertibility and factorization proofs | Highest theoretical coverage in this pool; primary. The PDF's note author is not separately credited. Infinite-dimensional and later determinant topics are not counted as this chapter's full coverage. |
| MIT 18.700, Fall 2013; David Vogan | PDF 13–20, especially 17–20 | Exact row/null/column transformation distinctions, canonical subspace bases, rectangular left inverse | Primary for transformation and coordinate precision. The displayed “pivot in every row” wording on p. 19 must be “every column” for a tall injective map. |
| Stanford EE263, Autumn 2007–08; Stephen Boyd | Lecture 3 slides 3–1 through 3–19 | Measurements, attainable outputs, ambiguity, left/right inverses, conservation of dimension | Primary for interpretation. The slide claims of Gram invertibility are proved in the lesson with their real Euclidean hypotheses. No protected homework or transcript is claimed read. |
| Berkeley Math 54, Spring 2018; Alexander Paulin | Both pages of Rank and Nullity rendered and visually read | Original pivot-column extraction and an exact four-by-five example with two kernel directions | Primary for concrete basis construction. This compact note does not replace the deeper proofs from the other sources. |
| CMU 21-241, Summer I 2014; William Gunther | Days 9 and 10: all six pages; Day 24: all four pages | Row-basis and subspace prompts, rectangular cases and polynomial transfers | Additional genuinely reviewed comparison. Numerous transcription slips are corrected; not used as the sole authority for any theorem. |

The ordering is by chapter-specific proof coverage, precision and complementary teaching value, not a purported university ranking or an invented universal numerical score. Four primary courses meet the four-university minimum; CMU adds accessible written prompts and independent error comparison.

## Corrections and reconciliation

MIT's tall full-column-rank matrix need not have a pivot in every row. Its p. 20 construction uses the first n rows of the invertible reduction transform to obtain a left inverse, which is explained consistently in the lesson.

CMU Day 9's displayed row-basis first vector ends in −2, while its own RREF has −1. The original four-by-five matrix is independently reduced and a complete exact certificate is supplied in the bank. Day 10 p. 3 writes “number of zero rows” where its rank argument needs nonzero rows. The statements that “the column space is a basis” and “the row space is a basis” must instead say that the respective columns or rows form bases. The spaces are not lists. Day 24 p. 1 calls more than n vectors independent where dependent is required. Day 24 p. 2 calls three quadratic polynomials a basis in P3; they form a basis in P2 and do not span P3. Day 24 p. 3 wrongly lists x mapped to 2x as a nonlinear nonexample. Its extension-from-a-basis theorem also omits the phrase “extending the assigned basis values.” These slips are explicitly corrected rather than imported.

Stanford's conservation-of-dimension picture is interpreted in an adapted basis. It does not imply that individual original coordinates are independently deleted. Its comment about infinite dimension is not adopted as “no basis”: an infinite-dimensional vector space can have a basis; its dimension is not a finite integer.

Plain-transpose orthogonality, positive Gram forms and rank–trace interpretations are restricted to their stated scalar fields. Complex cases use conjugate transpose; the bank includes an explicit failure of the plain-transpose shortcut.

## Accessible written prompt inventory

Berkeley's sole matrix example is expanded into all four basis calculations and exact checks. MIT's canonical subspace and one-sided-inverse constructions are developed in the lesson and factorization/inverse tasks. Oxford's Example 138 is reproduced as a course-derived calculation; its rank–nullity, invertibility, basis-exchange, restriction-dimension and factorization proof prompts have complete lesson derivations and bank tasks. Oxford Example 121 is the additional row-space membership task recorded at the end of the bank.

CMU Days 9–10's concrete prompts about the identity, shifted lines, the sign-constrained set, a line given by two constraints, proportional vectors, row-space membership, the four-by-five row-basis example and the zero space are answered in the lesson or explicitly labeled tasks. Day 24's finite polynomial examples and the listed linear/nonlinear examples are addressed with corrected hypotheses. Abstract continuous-function spaces, infinite cardinality classifications and unsupplied book exercises are outside this chapter's finite matrix rank boundary; they are not falsely counted as acquired questions.

Stanford slides in the read range contain statements and interpretations rather than a separate exercise sheet. They are taught and proved; no invented Stanford homework provenance is assigned to original questions. Original tasks additionally cover medium/hard rank inequalities, parameter strata, block matrices, updates, projections, nilpotent powers, polynomial constraints and graph incidence.

## Examination provenance and rights

The two authentic archive questions are explicit revisits: MSc CS 1405 Q41, PDF p. 9; PhD CS 1404 Q30, PDF p. 8. Both source pages were visually rechecked, and the source SHA-256 fingerprints match the pinned repository commit. Answers are independently derived and are not represented as official answer-key entries.

Private source PDFs remain outside Site assets. Public evidence records URLs, page ranges and hashes. The chapter is original mathematical exposition and independent diagrams; it does not copy full university publications or inaccessible exercise banks.

## Remaining limits

All stated scopes are finite. Broader sources may be added when a concrete coverage gap is identified. No claim of exhaustive worldwide course access, universal scientific certainty or guaranteed performance on every unseen examination is made.


# Current source revalidation


## What was actually read

Four official PDFs were freshly downloaded, fingerprinted, and their stated scopes read in this task. Download success is recorded separately from reading. No whole-course or worldwide exhaustive reading claim is made. The complete current `l_rank.en.md` lesson was read and reconciled with the selected sources; the problem bank and browser inspection are separate work.

| University and course | Pages actually reread, one-based PDF numbering | Teaching contribution |
| --- | --- | --- |
| MIT 18.700, Fall 2013, David Vogan, Gaussian Elimination | 13–20 | Row transformations, preserved kernel/row space, transformed column space, rank equality, canonical RREF bases and tall left inverse |
| Oxford M1 Linear Algebra I, 2022, Andrew Wathen as course lecturer | 42–51, 57–61, 68–69 | Exchange and dimension, basis extension, dimension formula, rank–nullity proof, one-sided inverses, restriction bound and rank factorization |
| Stanford EE263, Autumn 2007–08, Stephen Boyd, Lecture 3 | 1–19, slide labels 3–1 through 3–19 | Null-space ambiguity, attainable measurements, injection/surjection, inverse direction, dual bases and dimension interpretation |
| UC Berkeley Math 54, Spring 2018, Alexander Paulin, Rank and Nullity | Both handwritten pages, rendered and visually read | Exact four-by-five matrix, original pivot-column extraction, independent kernel directions and rank–nullity count |

The mathematical ranking remains chapter-specific: Oxford for proofs; MIT for row-operation and inverse precision; Berkeley for the concrete exact example; Stanford for interpretation. All four contribute different components. The fifth CMU comparison in the previous audit was not freshly reread here and remains explicitly historical.

## Fingerprints and access

All four requests succeeded on this run. The Oxford web reader itself returned an internal error, but the direct official HTTP download succeeded and yielded a valid 78-page PDF. Thus Oxford reading is based on the downloaded official document, not a search snippet.

| Document | SHA-256 |
| --- | --- |
| MIT | `7e6f2c9a2a3681d95c1ab2a41ba23fff43fdc339cffaf93c809c3898ec5985a3` |
| Oxford | `b7b49ddc40a68cd3d4376143178d259140a0fa01f5098c7df295d6ef85cf69ba` |
| Stanford | `a38713dbed8b74cd3f50491b9e476072a586727a5d0c7e8f6e991231b1f66e3f` |
| Berkeley | `2282a237bbdd0b9d9f0030cf91ec2a66c442c3bc1d00c95f40605338e139d76b` |

## Corrections that must not be imported from sources

1. **MIT PDF p. 13:** The prose says to multiply a row with leading entry 3 by −1/3; its own diagram correctly uses +1/3. The positive reciprocal is required. The original rendered page was inspected.
2. **MIT PDF p. 18:** The third displayed supposed two-dimensional RREF row-basis matrix has rows `(0,1,0)` and `(0,0,0)`, hence rank one. For its stated yz plane the second row must be `(0,0,1)`. The original page was visually inspected and both ranks independently checked. The current rank lesson does not reproduce the faulty display.
3. **MIT PDF p. 19:** An injective tall matrix requires a pivot in every **column**, not every row. The printed p. 20 construction itself uses the correct rank-n condition. The current lesson already states this correctly.
4. **Oxford PDF p. 50, Proposition 135 proof:** The extending vector is written as belonging to an undefined U minus the current span. It should be chosen in V minus that span. The current lesson uses the actual finite-dimensional domain.
5. **Oxford PDF p. 50, Corollary 137 proof:** Deleting a dependent spanning vector preserves spanning; it need not immediately leave an independent set. For instance, from `{e1,e2,e1+e2,e1+2e2}`, removing the last vector leaves a dependent spanning set. Preserved spanning alone contradicts minimality, so the theorem remains valid without the unnecessary false step. The current lesson's repeated deletion construction is correct.
6. **Stanford slide 3–8:** Lack of a finite basis must not be rephrased as lack of any basis. Infinite-dimensional spaces can have infinite bases. The lesson remains finite-dimensional and does not import the overcompressed parenthesis.
7. **Stanford slide 3–19:** Dimension conservation is interpreted in a kernel-adapted basis. It does not say that each original coordinate is independently retained or deleted. The current lesson's `(1,1)` measurement example makes that distinction correctly.

Additional small Oxford notation slips, such as a k−n versus m−n zero-block label and w labels at the end of the rank–nullity independence proof, do not change the corresponding theorem after dimensions and objects are made explicit. Infinite sequence examples are boundary context, not a claim to teach infinite-dimensional algebra in this chapter.

## Independent exact cross-checks

The Berkeley matrix was transcribed again from the original handwritten first page. Its RREF has pivot columns 1, 3 and 5 and rank 3. Both original kernel directions `(-2,1,0,0,0)` and `(-1,0,-1,1,0)` are annihilated, independent, and span a two-dimensional kernel. These results agree with the current lesson and the handwritten second page.

The main lesson's rank inequalities, finite-field fiber count, rank-one update branch, finite-dimensional one-sided inverse restriction, Schur-complement hypothesis and real-versus-complex Gram distinction were checked against their stated hypotheses. No new error in the main lesson was identified by this bounded source reconciliation. This is not a completion certificate for the bank, simulations, typography or browser behavior.

## Official written references

- David Vogan, MIT 18.700, Fall 2013, [Gaussian Elimination](https://ocw.mit.edu/courses/18-700-linear-algebra-fall-2013/b144082f6883d02faeec26d7f708c63e_MIT18_700F13_gauss.pdf).
- University of Oxford, M1 Linear Algebra I, 2022, Andrew Wathen as course lecturer, [Lecture Notes](https://courses.maths.ox.ac.uk/pluginfile.php/25471/mod_folder/content/0/lecture_notes22.pdf?forcedownload=1). A separate note author is not inferred.
- Stephen Boyd, Stanford EE263, Autumn 2007–08, [Lecture 3: Linear Algebra Review](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/lin-alg.pdf).
- Alexander Paulin, UC Berkeley Math 54, Spring 2018, [Rank and Nullity](https://math.berkeley.edu/~apaulin/Rank%20and%20Nullity.pdf).

Private source PDFs, extracted text and rendered source images remain outside the repository in the Temp research cache. The companion JSON records exact paths, scopes, hashes and limits. No source files, gates, counts, question banks, or deployed pages were changed by this research task.
