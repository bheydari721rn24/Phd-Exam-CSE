# Functions: course selection and reading audit

## Scope and evidence standard

This audit concerns d_functions: total and partial functions, domain and codomain, fibers, composition, injections, surjections, inverses, images and preimages, finite function counting, quotient factorization, function spaces, and the cardinality consequences needed to interpret infinite examples. It is a bounded search of nine university candidates, not a claim to have enumerated every course worldwide. Candidate pages establish availability and chapter fit; only the explicitly listed written texts count as read sources. No Iranian entrance-exam archive was inspected.

## Candidate comparison and selection

| University and course | Written evidence evaluated | Chapter fit and decision |
|---|---|---|
| Oxford, Discrete Mathematics, Michaelmas 2010; Andrew D. Ker | Chapter 2, printed pp. 17–30; PDF pp. 27–40, including exercises and answers | Principal 1: the most useful organizing sequence for typed definitions, restrictions, domains, and inverse algebra. Missing image/preimage detail is supplied independently. |
| Stanford, CS103, Spring 2017; Keith Schwarz | Lecture 08, Functions, 76-slide condensed PDF; instructional pp. 1–37 and 46–76; PS3 PDF pp. 5–6, Problems 6–8 and extra credit | Principal 2: strong quantifier-based proofs, invalid-function examples, one-sided inverse and composition counterexamples. Administrative slides 38–45 do not contribute mathematical content. |
| Cambridge, Discrete Mathematics, Peter Robinson; served under teaching/2003 | Actual downloaded edition is Michaelmas 2003 / Lent 2004, not the distinct 0203 file. Functions and cardinality printed pp. 44–49; PDF pp. 46–51, plus revision guide p. 52 | Principal 3: function counting, partial functions, quotient maps, function spaces, Schröder–Bernstein, and the richest advanced exercise set. Some concise statements require additional hypotheses or correction. |
| MIT, 6.042J, Fall 2010; Tom Leighton and Marten van Dijk; notes by Eric Lehman, F. Thomson Leighton, and Albert R. Meyer | Chapter 7, §7.1.5 and §§7.2.1–7.2.2; printed pp. 217–220, PDF pp. 5–8 | Principal 4: graphical interpretation, relation/function distinction, and finite mapping bounds. This is a focused chapter contribution, not a claim to have reread the entire textbook. |
| Carnegie Mellon, 21-127, Summer I 2018; Shaun Allison | Official course reading map and Assignment 5, all seven questions, one-page original PDF | Supplement: explicit composition tests, image-of-difference problem, a binary-factorization pairing map, and finite cardinality proofs. The course textbook is linked but is not counted as fully read. |
| Cornell, CS2800, Spring 2017; Michael George | Full Lecture 4 HTML, “proofs and functions,” with left/right inverse definitions and proof | Supplement: an independent inverse proof cross-check. The empty-domain exception and arbitrary-choice qualification are made explicit in our chapter. |
| UC Berkeley, CS70, Fall 2026; Josh Hug and Manuel Sabin | Official schedule and currently released note list | Not selected for this boundary: no released dedicated general functions text in the inspected schedule; countability is scheduled later. Catalogue inspection only, not a read source. |
| Princeton, COS340, Spring 2014 and Fall 2021 | Official readings schedule and general information | Not selected: a broad computation course that largely points to MIT texts for foundations, without a distinct chapter-level functions treatment identified here. Shared textbook links would not count as an independent reading. |
| ETH Zurich, mathematics course websites | Official course-discovery page and search results for related notes | Not selected: course catalogue discovery alone does not establish a fully reviewed, accessible, instructor-authenticated functions chapter. No claim that ETH lacks a stronger course. |

The principal order reflects usefulness for this particular chapter, not an absolute university ranking. All four principal texts were read before synthesis. CMU and Cornell were added because they supply concrete complementary checks, rather than to inflate the source count. Download hashes and exact original URLs are in d_functions-source-downloads.json. Reference PDFs and extracted text remain in the temporary research folder, outside the published site and GitHub source.

## Synchronization and corrections

| Issue found while reading | Editorial resolution and teaching location |
|---|---|
| Cambridge calls the codomain “range”; Oxford uses “range” for image | Use domain, codomain, and image consistently; explain the ambiguity in the definitions section. |
| MIT's relation terminology permits “function” to mean single-valued without totality | In this chapter, “function” means total unless explicitly qualified as partial. Model the graph with an existence-and-uniqueness axiom. |
| Oxford requires exact matching intermediate types for composition | Use typed composition by default; separately explain that a rule can be evaluated on the whole domain when its image lies inside the next domain, with explicit restriction/corestriction. |
| Cornell's blanket injective iff left inverse statement omits an empty-domain exception | A nonempty-domain injection admits a total left inverse; the empty-to-nonempty injection does not. The empty-to-empty map does. |
| Cornell chooses one antecedent for every output | A finite construction is elementary; for arbitrary families the assertion that every surjection splits uses the axiom of choice. Unique inverses of bijections require no such arbitrary selection. |
| Cambridge countable iff surjection from the naturals omits the empty set | An empty set is countable but cannot be the target of a function from a nonempty natural-number domain. |
| Cambridge countable-union proof chooses an injection for each member of a family | Explain the usual countable-choice setting; avoid an unqualified foundational claim. |
| Extracted CMU pairing formula loses exponent placement | Check it as 2 raised to x, not 2 multiplied by x; verify by unique factorization of a positive integer into a power of 2 and an odd part. |
| Oxford power exercise allows natural-number indexing conventions to differ | State positive exponent restriction. At exponent zero, discuss the domain issue of 0 raised to 0 rather than silently using the odd/even rule. |
| Several sources state inverse existence without a full proof | Supply both directions, uniqueness, reverse-order inverse composition, and all empty-carrier cases in full. |

## Coverage and exercise ledger

The lesson is independently written. It reconstructs proofs, adds fiber-based explanations and original finite counterexamples, and supplies image/preimage laws not developed in equal depth in all selected texts. Course-derived questions are paraphrased; solutions are original. The bank includes the chapter-relevant exercise families below.

| Source family | Worked-bank coverage |
|---|---|
| Oxford Chapter 2 practice 2.1–2.3 | Problems 1–3: intervals and infinite endpoints, disjoint differences, reciprocal-domain validity |
| Oxford 2.4–2.8 | Problems 4–7, 14: exponential/trigonometric/power/constant classification, composition and inverse calculations; the onto-composition proof also appears in the lesson |
| Stanford PS3 Problem 6, all fourteen classification items | Problem 8, with a row-by-row justification and explicit natural-number convention |
| Stanford PS3 Problem 7, all seven inverse subparts | Problems 9–11 and the full inverse proof section |
| Stanford PS3 Problem 8, all three subparts | Problems 12–13 |
| Stanford PS3 extra credit | Problem 30, an explicit closed-to-open interval bijection |
| Cambridge Functions exercises 1–3 | Problems 15, 22, 12; all function spaces are constructively specified, with classifications and an exact enumerator |
| Cambridge exercise 4, all six function-space/product comparisons | Problems 23–25; false comparisons get finite counterexamples and explicit degenerate cases |
| Cambridge exercises 5–7 | Problems 26–28: quotient descent, order isomorphism, partial-function count |
| Cambridge exercises 8–10, including all five sequence classes | Problems 31–33 |
| Cambridge exercise 11 | Problem 34: rational pairs, disjoint open discs, and the circle counterexample |
| CMU Assignment 5, all seven question families | Problems 12, 18, 29, 35–37; finite insertion/deletion and bijection counts are included explicitly |
| Independently authored applications and failure cases | Problems 16–21 and 38–42: cancellation, preimage calculus, restrictions, constrained counts, factorization, permutation dynamics, algorithm verification, and infinite proof construction |

The selected courses contain many questions outside the chapter boundary; those are not represented as functions questions. “All relevant families in the listed readings” does not mean every question in all semester-long courses. Iranian exam-specific frequencies and calibration remain unaudited until the final-month work authorized by the student.

## Exact references

1. Andrew D. Ker. Discrete Mathematics, Michaelmas 2010. University of Oxford. Chapter 2, pp. 17–30. [Lecture notes](https://www.cs.ox.ac.uk/andrew.ker/docs/discretemaths-lecture-notes-mt2010.pdf).
2. Keith Schwarz. CS103: Mathematical Foundations of Computing, Spring 2017. Stanford University. [Course archive](https://web.stanford.edu/class/archive/cs/cs103/cs103.1176/); [Lecture 08 condensed slides](https://web.stanford.edu/class/archive/cs/cs103/cs103.1176/lectures/08/Small08.pdf); [Problem Set 3](https://web.stanford.edu/class/archive/cs/cs103/cs103.1176/handouts/150%20Problem%20Set%203.pdf), pp. 5–6.
3. Peter Robinson. Discrete Mathematics. University of Cambridge. Downloaded edition: Michaelmas 2003 / Lent 2004, printed pp. 44–49. [Original file](https://www.cl.cam.ac.uk/teaching/2003/DiscMaths/DiscMaths.pdf). The similarly named 0203 file is a different edition and is not the principal source here.
4. Eric Lehman, F. Thomson Leighton, and Albert R. Meyer. Mathematics for Computer Science. MIT 6.042J, Fall 2010, instructors Tom Leighton and Marten van Dijk. [Course](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/); [Chapter 7 PDF](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/efac321fdc8d0b27586ca35b04aab808_MIT6_042JF10_chap07.pdf), pp. 217–220.
5. Shaun Allison. 21-127 Concepts of Math, Summer I 2018. Carnegie Mellon University. [Course](https://www.math.cmu.edu/~sallison/concepts18/index.html); [Assignment 5](https://www.math.cmu.edu/~sallison/concepts18/assignment5.pdf). Textbook author: Clive Newstead; textbook linkage was verified, but the full book was not reviewed for this chapter.
6. Michael George. CS2800 Discrete Structures, Spring 2017. Cornell University. [Lecture 4: proofs and functions](https://www.cs.cornell.edu/courses/cs2800/2017sp/lectures/lec04-functions.html).
7. UC Berkeley. [CS70 Fall 2026 schedule](https://www.eecs70.org/). Candidate discovery only.
8. Princeton University. [COS340 Spring 2014 readings](https://www.cs.princeton.edu/courses/archive/spring14/cos340/lectures.php) and [Fall 2021 information](https://www.cs.princeton.edu/courses/archive/fall21/cos340/index.html). Candidate discovery only.
9. ETH Zurich. [Mathematics course websites](https://math.ethz.ch/studies/course-websites.html). Candidate discovery only.
