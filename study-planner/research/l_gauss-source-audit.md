# Gaussian elimination: written-source evaluation

## Candidate pool, ranking and decisions

Five accessible university course offerings were compared individually for this chapter. The pool is bounded and explicitly documented: it is not an assertion that every worldwide course, restricted LMS handout or historical offering was read. All five contribute genuinely reviewed written material; the four primary choices are MIT, Oxford, Stanford and Berkeley. CMU is an additional error/definition/example comparison. No video, transcript substitute or inaccessible homework was counted as read.

| Priority | University and course | Written scope actually read | Distinct value | Limit and decision |
|---|---|---|---|---|
| 1 | MIT, 18.700, Fall 2013; David Vogan | Gaussian Elimination, all 21 PDF pages; instructional pp. 2–20 | General fields, rectangular RREF, elementary matrices, preserved subspaces and left inverses | Uniqueness proof is omitted in the handout; supplied independently in the chapter. Primary theoretical source. |
| 2 | Oxford, M1 Linear Algebra I, 2022; Andrew Wathen listed as lecturer | Printed pp. 3–7 and 16–20, corresponding to PDF pp. 4–8 and 17–21; adjoining p. 8 inspected for boundary | Complete rectangular, incompatible and parameter branches; inductive existence argument | Note author is not separately attributed. Uniqueness is deferred elsewhere in the course; supplied independently here. Primary branch and completeness source. |
| 3 | Stanford, CME108/MATH114, Introduction to Scientific Computing | All three Gaussian-elimination pages, all three LU pages and all five Permuted-LU pages; complete instructional bodies | Algorithm loops, factor recording, repeated loads, permutation convention and declared rounding | Public retrieved pages do not identify lecturer. Corrected mathematical/transcription slips listed below. Primary computational source. |
| 4 | UC Berkeley, Math 54, Spring 2018; Alexander Paulin | All seven handwritten Systems of Linear Equations and Row Reduction pages; rendered individually and visually read | Two-dimensional geometry, plane intersections and a five-variable nonconsecutive-pivot example | The notes state some theorems without full proof; independent proofs supplied. Primary geometric source. |
| 5 | CMU, 21-241 Matrix Algebra, Summer I 2014; William Gunther | All three pages each of Day 1, Day 2 and Day 8 | Contrasting introduction, elementary inverses and introductory exercise structures | Several slips are corrected. Additional comparison source rather than the sole basis for a proof. |

The ranking combines coverage, proof quality, the chapter's need for exceptional cases, readable written access and computational treatment. A source's prestige does not override a detected error. All five were read before choosing the four complementary primary roles. More courses would be needed if the declared scope included sparse pivoting, QR, least squares or certified floating-point error bounds; those topics belong to later chapters.

## Exact documents and section links

- MIT: [Gaussian Elimination](https://ocw.mit.edu/courses/18-700-linear-algebra-fall-2013/b144082f6883d02faeec26d7f708c63e_MIT18_700F13_gauss.pdf).
- Oxford: [M1 lecture notes](https://courses.maths.ox.ac.uk/pluginfile.php/25471/mod_folder/content/0/lecture_notes22.pdf?forcedownload=1).
- Berkeley: [Systems of Linear Equations](https://math.berkeley.edu/~apaulin/Systems%20of%20Linear%20Equations.pdf).
- CMU: [Day 1](https://www.math.cmu.edu/~wgunther/241/m14/notes/week1/1.pdf), [Day 2](https://www.math.cmu.edu/~wgunther/241/m14/notes/week1/2.pdf), [Day 8](https://www.math.cmu.edu/~wgunther/241/m14/notes/week2/8.pdf).
- Stanford Gaussian elimination: [Part 1](https://web.stanford.edu/class/math114/decks/linear_systems/gauss_elim21.html), [Part 2](https://web.stanford.edu/class/math114/decks/linear_systems/gauss_elim29.html), [Part 3](https://web.stanford.edu/class/math114/decks/linear_systems/gauss_elim37.html).
- Stanford LU: [Part 1](https://web.stanford.edu/class/math114/decks/linear_systems/lu_factorization.html), [Part 2](https://web.stanford.edu/class/math114/decks/linear_systems/lu_factorization49.html), [Part 3](https://web.stanford.edu/class/math114/decks/linear_systems/lu_factorization64.html). The third HTML title repeats “2/3”; the linked instructional body is the concluding part.
- Stanford Permuted LU: [Part 1](https://web.stanford.edu/class/math114/decks/linear_systems/permuted_lu.html), [Part 2](https://web.stanford.edu/class/math114/decks/linear_systems/permuted_lu8.html), [Part 3](https://web.stanford.edu/class/math114/decks/linear_systems/permuted_lu16.html), [Part 4](https://web.stanford.edu/class/math114/decks/linear_systems/permuted_lu32.html), [Part 5](https://web.stanford.edu/class/math114/decks/linear_systems/permuted_lu64.html).

Content hashes, actual page counts and read scopes are preserved in the downloadable [source record](../evidence/l_gauss/sources.json). Original university PDFs and private archive caches are not copied into the public site.

## Source disagreements and independent corrections

1. Stanford Gaussian Part 1 reverses the wording for which side of the diagonal can have nonzero entries. Upper triangular means zero below the diagonal; lower triangular means zero above it.
2. Stanford Gaussian Part 3 contains a prose update omitting the old target row and subtraction. The actual legal update is the old row minus its multiplier times the unchanged pivot row. The chapter uses the correctly derived loop.
3. Stanford's operation-count presentation is not imported as a universal formula. The chapter independently counts the declared trailing-block loop, distinguishes load updates and states every scalar-operation convention.
4. Stanford LU concluding part prints an inverse factor with exponent minus two in several intermediate lines; the final line has the correct minus-one exponent. The derivation here uses the inverse of each transform once, in reverse product order.
5. Stanford Gauss-transform entry notation can be read as overwriting the identity diagonal and includes inconsistent signs in its intermediate naming. The chapter explicitly defines a strictly lower multiplier vector and proves the nilpotent rank-one inverse.
6. Stanford's final in-place PLU pseudocode can be misread as updating the stored multiplier column during a full-row subtraction. The separate-array code here updates only trailing coefficient columns, explicitly sets known zeros and swaps completed multiplier columns.
7. MIT p. 19 says full column rank implies a pivot in every row, although its own rectangular diagram contains additional zero rows. The correct condition is a pivot in every coefficient column, with possible additional zero rows when there are more equations than unknowns.
8. MIT p. 13 gives a positive normalization in its displayed operation but a negative scalar in the adjacent prose for the same example. Our exact row certificates and substitutions determine the correct sign.
9. CMU Day 1 uses a trigonometric simplification with different variable arguments; that identity does not apply as printed. Its triangular example also prints an incorrect first coordinate; the chapter derives backward substitution from the equations instead.
10. CMU Day 2 says a column containing a leading entry is free in one sentence; its intended condition is absence of a leading entry. The chapter consistently distinguishes coefficient pivot and free columns.
11. CMU Day 8 drops the load in a prose inverse-solve expression. The correct formula is the inverse applied to the load, not the inverse matrix alone. The following theorem in the note gives the correct formula.
12. Oxford Example 7(b)'s displayed last array is described as RREF, but retains nonzero entries above the last-column pivot. It already certifies inconsistency; a full augmented RREF would clear those entries. Our coefficient-only versus full-augmented conventions are explicitly separated.

These corrections are not reasons to discard otherwise valuable sources. They demonstrate why multiple written sources and independent certificates are needed.

## Coverage crosswalk and prompt inventory

| Chapter area | Sources compared | Independent additions and problem transfer |
|---|---|---|
| Equations, geometry and augmentation | Berkeley pp. 1–3; Oxford pp. 3–5; CMU Day 1 | Same-intersection animation, zero-equation boundary and synchronized-load counterexample |
| REF, RREF, free columns | Berkeley pp. 4–7; Oxford pp. 16–20; MIT Sections 2–4; CMU Day 2 | Exact skip-column algorithm, termination invariant and canonical uniqueness proof |
| Rectangular compatibility and complete families | Oxford Examples 7 and 46; Berkeley pp. 2, 5–7; MIT Sections 2, 6 | Particular/direction substitution certificates and left-null impossibility witnesses |
| Parameters | Oxford Example 8 | All exceptional values; additional cancellation, early-free-column and quadratic-factor tasks |
| LU and permutations | Stanford complete LU/Permuted-LU sequences | Nonsingular leading-minor criterion, normalization freedom, later-multiplier swap certificate and authentic doctoral Q33 |
| Inverses | MIT Section 6; CMU Day 8 | Two-sided checks, singular inverse attempt, rectangular left-inverse limitations |
| Cost and rounding | Stanford Gaussian/Permuted-LU | Independently derived exact loop counts, residual amplification and explicit three-digit rounding |
| Fields and restrictions | MIT field formulation; Oxford real formulation | Binary-field comparison, finite-field counts, integer and nonnegative constraints |

In-scope written exercise structures were inventoried rather than claiming all homework in full courses was reproduced. Oxford Examples 2/5, 7(a), 7(b), 8 and 46 are represented by worked tasks or the solution-family lesson; its elementary-matrix proof prompt is resolved in the operations section. Berkeley's two introductory solves and five-variable example are represented in the geometry lesson and problem bank. Stanford's forward/backward substitution, elementary multiplication, Gauss-transform inverse, permutation inverse, zero-pivot, rounding and LU example prompts are answered in the proofs and bank. MIT's check-the-solution and left-inverse constructions are independently certified; it has no separately reproduced full problem set in this handout. CMU's introductory classification and inverse-example patterns are represented by independent exact tasks; book exercises referenced without their full statement were not counted as accessed. Stanford protected HW2 was not accessed and is not claimed as reviewed.

## Examination evidence

Doctoral CS 1404 Q33 was newly located on original booklet PDF page 8 and its options visually checked. Its unrestricted lower/upper factors allow diagonal scaling; assuming a unit lower diagonal would change the question. Master's CS 1405 Q113 was rechecked on original booklet PDF page 25 and intentionally revisited to connect elimination of a shared sum to an integer count. Both use the pinned archive commit and source hashes recorded with their statements. Answers are independent derivations, not claims about an official key.

Only these inspected pages and documented items are claimed here. No assertion is made that every archived examination page has been scanned for this chapter or that every possible examination question is covered.
