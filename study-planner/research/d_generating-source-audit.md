# Generating functions: written-course selection and reading audit

## Selection method and limits

The comparison is a bounded, documented search of accessible written university teaching materials. It is not a claim that every course worldwide was acquired or ranked. Selection considers explicit assumptions, proof depth, coefficient extraction, recurrence boundaries, counting models, labelled structures, and useful exercise patterns. Four complementary core courses were selected after comparing the pool below. The chapter's derivations are original; a source's institution does not exempt its notation or conclusions from checking.

| Priority | University and course | Author or instructor | Written scope actually read | Contribution |
|---|---|---|---|---|
| Core 1 | MIT, 6.042J Mathematics for Computer Science, Spring 2015 | Eric Lehman, F. Thomson Leighton, Albert R. Meyer, textbook authors | Chapter 15, one-based PDF pages 636–670, including Problems 15.1–15.26 | Formal-series foundations, convolution, rational coefficients, recurrence boundaries, counting exercises |
| Core 2 | UC Berkeley, Math 172 Combinatorics, Spring 2010 | Mark Haiman | All 7 pages of Ordinary Generating Functions, all 10 pages of Exponential Generating Functions and Structures, all 9 pages of Partitions and Their Generating Functions | Weight-preserving constructions, labelled products and composition, partition identities and their proofs |
| Core 3 | Carnegie Mellon, 15-251 Great Theoretical Ideas in Computer Science, Lecture 8, 20 September 2012 | Handout originally written by John Lafferty in 2008; the handout does not establish the 2012 lecturer | All 9 pages, through references; official PDF text | Coefficient operations, Iverson initial-condition corrections, forcing and symbolic tiling construction |
| Core 4 | Princeton, An Introduction to the Analysis of Algorithms / Analytic Combinatorics Part One, Lecture 3 | Robert Sedgewick; companion textbook coauthor Philippe Flajolet | All 52 slides of AA03-GFs, including OGF, recurrence, Catalan, EGF, counting and cumulative-cost sections | Rational cancellation, harmonic sums, recursive objects, marked parameters and averaged costs |

## Screened candidate pool

1. MIT 6.042J: selected for its substantial complete written chapter.
2. Berkeley Math 172: selected above the simpler Math 55 lecture because it supplies proofs of labelled constructions and partition identities.
3. CMU 15-251: selected for its formal, explicit treatment of sequence transforms and initial corrections.
4. Princeton AofA Lecture 3: selected for algorithmic and parameter-marking coverage. The full written slide deck was read at the author's official mirror; some extracted mathematical glyphs are damaged. Every equation used here is independently derived. The Princeton booksite itself returned HTTP 403 in later requests. No native PDF hash is claimed for a download that timed out.
5. Stanford Math 108, Winter 2016, Persi Diaconis and Jan Vondrak: official syllabus includes generating functions, but the course page explicitly expects students to take their own lecture notes and links a commercial reference. Its accessible syllabus alone is not a substitute for a read lecture derivation. Not selected as a core written source.
6. Oxford Discrete Mathematics 2023–2024: the catalogue mentions generating functions, but the linked older Andrew Ker notes read for the previous chapter explicitly omit a full treatment. Catalogue screening is not counted as reading a generating-function course.
7. Berkeley Math 55, Spring 2004, James Demmel hosted Lecture 26: an initial search result exposed a generating-function lecture; the later PDF request returned 404. Not counted as read or used.
8. Cambridge Part II Mathematical Biology, Lent 2017: probability generating functions are relevant to the probability bridge but the course's main scope is stochastic population models. Only the accessible introductory excerpt was screened; it is not counted as a core course.
9. Berkeley Math 172 additional tree and cycle notes: screened as advanced extensions. The chapter deliberately proves its own elementary coefficient-inversion result and does not claim to have fully reviewed these additional notes.

## Corrections and synchronization

- Coefficients use rational or complex scalars unless a different ring is explicitly stated. A formal series over a general commutative ring is invertible exactly when its constant coefficient is a unit, not merely nonzero.
- Berkeley's ordinary notes use a shifted Fibonacci convention with first values 1,1. This chapter always uses the ordinary Fibonacci sequence 0,1 and states shifted counts explicitly.
- The sequence construction requires positive-size components for local finiteness. An algebraic inverse can still exist when a component series has a nonzero constant other than one; algebraic invertibility does not validate infinite combinatorial enumeration.
- The Berkeley composition example's statement about a binomial coefficient with upper index minus one is not used to handle the empty case. The empty composition is treated separately.
- In MIT's general forced-recurrence discussion, the degree of a polynomial factor in the solution is controlled by the actual reduced denominator and forcing poles. It need not be bounded by the original recurrence order.
- Several MIT PDF text extractions interchange sums and products or lose minus signs. The chapter proves the convolution identity and uses coefficientwise checks instead of trusting extraction.
- CMU's integration variable is normalized to the actual dummy variable. Ordered tiling sequences retain order even when their scalar generating-function multiplication is commutative: expansion multiplicity retains that information.
- Princeton's expected binary-tree leaves means internal vertices with two empty children, not external null leaves. Both definitions and the empty-tree exception are stated here.
- Formal coefficient equality does not justify numerical substitution at a divergent point. Moment statements and asymptotics have their own analytic hypotheses.

## Exact primary references

- MIT OCW, [Mathematics for Computer Science, Spring 2015 textbook](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf), Chapter 15.
- Mark Haiman, UC Berkeley, [Math 172 Spring 2010 course](https://math.berkeley.edu/~mhaiman/math172-spring10/), [Ordinary Generating Functions](https://math.berkeley.edu/~mhaiman/math172-spring10/ordinary.pdf), [Exponential Generating Functions and Structures](https://math.berkeley.edu/~mhaiman/math172-spring10/exponential.pdf), [Partitions and Their Generating Functions](https://math.berkeley.edu/~mhaiman/math172-spring10/partitions.pdf).
- Carnegie Mellon, [15-251 Lecture 8 handout](https://www.andrew.cmu.edu/course/15-251/Notes/gen-functions.pdf), 20 September 2012; originally John Lafferty, 2008.
- Princeton, [AofA course material listing](https://aofa.cs.princeton.edu/online/); Robert Sedgewick, [Lecture 3 written slides at the author's mirror](https://sedgewick.io/wp-content/uploads/2022/04/AA03-GFs.pdf).
- Stanford, [Math 108 Winter 2016](https://theory.stanford.edu/~jvondrak/MATH108-2016/MATH108.html), candidate screening only.
- Oxford, [Discrete Mathematics 2023–2024](https://www.cs.ox.ac.uk/teaching/courses/2023-2024/discretemaths/), catalogue screening only.

The evidence manifest records native hashes only for actually acquired PDFs. Remote text reading is distinguished from native acquisition. The bank uses original questions and explicitly credited course-pattern reconstructions; it does not reproduce entire copyrighted exercise collections.
