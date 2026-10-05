# Inclusion-exclusion: source selection and reading audit

## Discovery and selection boundary

This is a bounded comparison of eight located course offerings. It is not an exhaustive survey of every university course. Actual reading means inspecting the written material in the ranges below, including its examples, assumptions and formulas. A catalogue or syllabus alone does not qualify. The new lesson, diagrams, solutions, exact-multiplicity inversion, Bonferroni proof, bounded-allocation derivation, rook-board treatment and subset algorithm are independently authored mathematical explanations; their correctness is checked separately. No source is presented as covering every extension.

| Candidate | Actual evidence reviewed | Selection decision |
|---|---|---|
| MIT 6.042J, Spring 2015, Lehman, Leighton and Meyer | Textbook section 14.9, PDF pages 590–596, from section start through the totient derivation; original cached PDF inspected | Primary: adjacency intersections, inclusive versus pair-only overlap, subset-index notation, and prime-factor sieve |
| Oxford Discrete Mathematics, Andrew Ker, Michaelmas 2010 | Official lecture notes sections 3.3–3.4, PDF pages 47–50, through Example 3.12; original PDF text through web reader | Primary: leading-zero restrictions, derangements, strict integer endpoints and floors |
| Cornell CS2800 written text by Rafael Pass and Wei-Lung Dustin Tseng | A Course in Discrete Structures, section 4.4, PDF pages 74–76 (zero-based web pages 73–75), including proof and Examples 4.24–4.27 | Primary: multiplicity proof, onto maps and complement counting |
| CMU 21-301, Michael Tait, Fall 2018 | Section 2.5, physical PDF pages 20–24, printed pages 16–20 | Primary: complement form with empty intersection, derangements, onto maps and totient product |
| UC Berkeley EECS70, Spring 2020 | Note 14 section 4.3, physical pages 10–11, through union bound before section 5 | Reviewed complementary fifth course: weighted events, independence and dice counterexample |
| Stanford CS109, Lisa Yan, Spring 2020 | Lecture Notes 1, all four pages | Reviewed but not selected for main synthesis: accurate introductory sum/product/union presentation, less depth for this chapter than the four primary texts |
| CMU 15-251, Gupta and Sleator, Fall 2010 | Lecture 7 opening two-set union slides through official PDF text discovery | Screened; narrower than the selected CMU 21-301 text; not counted as a second university |
| Harvard Math 55, Spring 2018, Williams course page | Lecture 19 topic and assigned textbook exercises on official schedule | Discovery-level only; page explicitly says notes are incomplete. Not counted as a reviewed text |

Selection prioritizes direct chapter relevance, explicit proof, complementary hard examples, readable official written access and correctable notation. MIT supplies structural intersections; Oxford supplies position-sensitive counts; Cornell supplies a complete multiplicity proof; CMU supplies complement and map derivations. Berkeley adds the weighted interpretation that the four primary treatments do not develop as directly. There is no numerical world-ranking claim. Four primary universities plus one genuinely read complementary university are used.

## Access and source corrections

The MIT and CMU originals and Berkeley/Stanford originals have SHA-256 records in d_inclusion-downloads.json. Cornell and Oxford native downloads timed out, but the full specified sections of the official original PDFs were read through the web PDF reader. No local checksum is claimed for those two. Cached copyrighted originals remain outside Git; only citations, reading evidence and independently written teaching are published.

CMU's opening example gives 32 students, 21 math majors, 14 seniors and three in both, then prints a result of two for neither. The arithmetic gives **zero**, because 32 − (21 + 14 − 3) = 0. The chapter includes a corrected, explicitly attributed reconstruction. Its surjection intermediate displayed intersection notation has an ambiguous free set; the lesson sums over a specified subset or, after verifying symmetry, over its size. The totient notation is written as a set-builder cardinality with a positive integer domain.

Cornell's general union display must exclude the empty index set; the proof and cardinality-grouped version establish this. The chapter uses a nonempty-subset union and an all-subset complement with the empty intersection equal to the universe. Its spelling “Sterling” is normalized to “Stirling.”

Oxford's digit-sum illustration in the preceding section includes zero if padded strings are unrestricted despite saying positive integers; that example is not used as a positive count here. In section 3.4, the listed multiples “3, 5, 9” and the ceiling definition's final floor symbol are corrected to “3, 6, 9” and the ceiling symbol. Six-digit numbers never have a zero first digit. General derangement formulas in this chapter explicitly include n = 0 and n = 1, rather than assuming cancellation of the first two terms is meaningful for every n.

Berkeley describes successive truncations as getting better. The chapter proves the odd-order upper and even-order lower bounds, but does not claim each consecutive numerical truncation is closer in absolute error: that stronger interpretation is false. It also distinguishes independence from disjointness.

## Reviewed example and exercise inventory

All inclusion-exclusion examples in the four selected section ranges are represented with fresh teaching solutions in the bank or lesson: MIT major counts (inclusive/pair-only distinction), directed adjacency blocks and totient derivation; Oxford two required digits, derangements and three-prime sieve; Cornell two-divisor union, general onto formula and the poker complement; CMU corrected survey, complement proof, derangements, surjections and totient product. Berkeley's three-dice union is included. Parameter changes are explicitly marked as course-inspired rather than authentic course questions. The many unrelated exercises in entire textbooks and courses were not read or claimed included. In particular Berkeley Note 14 section 5 concerns broader probability topics and is outside the selected section.

## Coverage and provenance boundary

The chapter covers finite set counting and atom feasibility, arbitrary-set union/complement proofs, exactly/at-least multiplicity, binomial inversion, Bonferroni, required labels and onto functions, image sizes and labeled/unlabeled partitions, derangements/partial fixed-point restrictions, forbidden positions with rook numbers, bounded weak compositions, modular/divisibility intersections, adjacency compatibility, weighted events, subset transforms, exact arithmetic and independent checks. General generating-function solving, arbitrary poset theory, full graph-coloring theory and probability distributions remain separate chapters; only the bridges needed here are proved.

Two authentic archive revisits are checked against rendered original PDF pages: MSc CS 1405 Q124 (PDF page 27), and PhD CS 1405 Q21 (PDF page 8). Their translations, options, identifiers and original SHA-256 fingerprints are retained. The independently derived answers are not advertised as official answer keys. New problems have original stems or independent course-inspired reconstructions; no claim is made to reproduce an entire copyrighted course bank.

## References

1. Eric Lehman, F. Thomson Leighton and Albert R. Meyer. MIT 6.042J, Mathematics for Computer Science, Spring 2015, section 14.9. [Official textbook](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf).
2. Andrew D. Ker. Oxford Discrete Mathematics, Michaelmas 2010, sections 3.3–3.4. [Official notes](https://www.cs.ox.ac.uk/andrew.ker/docs/discretemaths-lecture-notes-mt2010.pdf).
3. Rafael Pass and Wei-Lung Dustin Tseng. A Course in Discrete Structures, Cornell CS2800 course text, section 4.4. [Official course copy](https://www.cs.cornell.edu/courses/cs2800/2016sp/handouts/pass_tseng_discmath.pdf).
4. Michael Tait. CMU 21-301 Combinatorics, Fall 2018, section 2.5. [Official notes](https://www.math.cmu.edu/users/math/mtait/301/Notes.pdf).
5. UC Berkeley EECS70, Spring 2020, Note 14, section 4.3. [Official notes](https://sp20.eecs70.org/static/notes/n14.pdf). The note does not name an individual author; no authorship is invented.
6. Lisa Yan, based on Sahami and Piech. Stanford CS109, Spring 2020, Lecture Notes 1. [Comparison source](https://web.stanford.edu/class/archive/cs/cs109/cs109.1206/lectureNotes/LN01_counting.pdf).
