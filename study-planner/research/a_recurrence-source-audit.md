# Algorithmic recurrences: candidate selection and genuine reading ledger

Review date: 2026-10-02. Active chapter: a_recurrence, Week 2 Algorithms. This is a bounded comparison of eight university candidates; it does not certify discovery of every worldwide course or a globally optimal ranking. Chapter-specific selection considers usable text, proof detail, domain precision, complementary coverage, and useful exercise types.

## Candidate-by-candidate assessment

| University and course | Actual review level | Strength and limitation | Decision |
| --- | --- | --- | --- |
| MIT 6.006, Spring 2020; Erik Demaine, Jason Ku, Justin Solomon | All seven pages of Recitation 3 read, including all recurrence exercises. Additional MIT 6.046-hosted Tom Leighton 1996 notes pages 1–5 read through extraction and the decoded primary-source text; original pages 2 and 4 visually inspected because PDF extraction has encoded characters. | Direct modeling examples, general master hypotheses, extended nonnegative log-power case. Supplement supplies a proof for unequal ratios. Exact toll versus upper toll is kept distinct; a derivative-bound remark is not adopted as a sufficient comparability criterion. | Principal university source; foundational and advanced theorem spine. |
| Stanford CS 161 Lecture 3 | All six PDF pages and the complete one-page solved concept checks read. Retrieved notes identify Winter 2026, Moses Charikar and Ellen Vitercik, adapted from Virginia Williams with credited contributors. | Explicit upper inequalities and geometric-tree proof; parameter and substitution checks. The winter2025 URL now serves a file headed Winter 2026, so the manuscript cites the actual file header and retains its hash. Rounding is stated but not proved in the note; the new lesson gives separate checks. | Principal course; modeling and theorem reasoning. |
| CMU 15-451, Fall 2011; Avrim Blum author, Avrim and Manuel Blum instructors | PDF pages 10–15 read in full (printed Lecture 2 pages 7–12); pages 24–26 read for selected Lecture 4 passages on randomized/deterministic selection and shrinking-mass recurrences. Cover and contents inspected to verify authorship/page mapping. | Clear unrolling, fixed-constant induction failure, geometric sums, and unequal linear-mass reasoning. A theta claim following only an upper inequality needs compulsory-work qualification; the chapter supplies it and includes leaf costs. | Principal course; proof diagnostics and unequal branches. |
| Princeton Analysis of Algorithms; Robert Sedgewick and Philippe Flajolet | Complete available Chapter 2 web text, formulas, and selected exercise statements read; official course-materials page reviewed. Several section headings have no text and are not represented as full underlying book chapters read. | Telescoping factors, exact floor/ceiling effects, periodic terms, and non-master examples. The web merge recurrence uses toll n; actual worst-case merge comparisons use n−1. Both are derived and distinguished. | Principal course; exact recurrences and normalization. |
| Cornell CS 3110, Spring 2009 lecture and Spring 2011 recitation | Complete Lecture 20 and Recitation 19 text read, including all displayed proof steps. The read pages do not name individual authors, so no instructor is invented. | Especially useful slack induction, parameter thresholds, and an uncovered reciprocal-log example. Typographical issues in uneven-branch notation and a comparison-envelope definition are explicitly corrected. | Genuinely read supplementary university source; four is a minimum, not a ceiling. |
| Berkeley CS 170, historical Jordan/Demmel course listings | Official search entries and course scope screened. Two intended historical lecture addresses did not resolve to usable written text in this pass. | Relevant curriculum, but the specific recurrence text was not obtained and read here. No download or catalogue entry is counted as genuine chapter reading. | Unselected; not counted toward the four. |
| Oxford Design and Analysis of Algorithms, Hilary 2022; Elias Koutsoupias | Official syllabus and lecture-material links screened. No full recurrence passage read. | Strong introductory fit; the selected pool already supplies explicit proofs and exact-analysis complements. | Unselected candidate; future supplement if a gap requires it. |
| ETH Zurich Data Structures and Algorithms, Spring 2022; Felix Friedrich | Official syllabus/agenda and written-material availability screened, including the master-theorem topic. No full recurrence lecture text read. | Algorithms, cost models, and parallelism fit the chapter, but no full recurrence-proof review is claimed. | Unselected candidate; not counted toward the four. |

## Reconciled scientific and presentation issues

1. Stanford's polynomial-toll theorem gives upper conclusions; no tight conclusion is inferred without a lower toll/base or compulsory-work assumption.
2. MIT's critical log-power case states nonnegative log exponents. The negative-exponent thresholds are derived independently by reversing depth and proving the power-sum estimates.
3. Cornell Lecture 20's uneven tree illustrates children n/3 and 2n/3, although one displayed equation writes T(n/3)+2T(n/3). The new lesson states the intended unequal model explicitly and distinguishes the two trees.
4. Cornell Recitation 19's larger envelope is written with original T children in the last display. The lesson defines envelopes recursively on themselves and proves comparison. The reciprocal-log recurrence is solved tightly rather than merely bounded by n log n.
5. CMU's shrinking-mass theorem is displayed after an upper inequality with a theta conclusion. The chapter separates the proven upper bound from a lower bound supplied by exact positive linear work.
6. Princeton's size toll and a size-minus-one comparison toll differ by one per internal merge. The exact balanced-tree identity derives both values and explains their equal leading order.
7. Leighton's polynomial-interval comparability is adopted as an explicit assumption. The remark about a polynomial derivative bound alone is not adopted: a nonnegative smooth function such as sine squared can have zeros and violate the displayed multiplicative comparability condition. Initial logarithmic singularities are handled by a fixed cutoff and bounded extension.
8. The full perturbation proof in later Leighton pages was not read or reproduced. The lesson proves the unperturbed theorem, handles selected floors/ceilings independently, and does not apply a general perturbation theorem to arbitrary child arguments.
9. Tree identities retain positive base work and distinguish internal levels from leaves. Mathematical weighted recurrences are distinguished from physical recursive-call counts.

## Attributed exercise-type map

| Read source | New problems | Adaptation |
| --- | --- | --- |
| MIT Recitation 3 p. 6 | 4, 5, 7, 16, 21 | Independently stated models; exact bases/tolls or extended representation and boundary analysis. |
| Stanford Lecture 3 and solved checks | 3, 13, 17, 34 | Upper-versus-tight diagnosis, detailed level arithmetic, fractional critical exponent, and explicit unequal quadratic induction. |
| CMU Lecture 2 / selected Lecture 4 | 20, 29 | Fixed-constant proof diagnosis and complete mass bound with base leaves and logical lower-bound distinction. |
| Princeton Chapter 2 Exercises 2.13, 2.71, 2.73 and exact split analysis | 8, 27, 32, 36 | New full derivations, corrected cost convention, independent mass check, and direct exponential-toll proof. |
| Cornell read lecture and recitation | 15, 18, 19, 22, 31 | Exact geometric sum, changed parameter family, slack proof, tight log-log boundary, and corrected uneven-branch notation. |
| Leighton MIT theorem examples | 33 | Explicit characteristic-root verification and integral evaluation. |

Other questions are labeled original. The bank covers the chapter's in-scope reasoning patterns but does not reproduce every copyrighted exercise from any source collection. The source pool records a search boundary and access limits; no course is counted as read merely because its university name is prestigious.

## Primary references

- [MIT Recitation 3](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/1869dbf640ded6b31f1bd369d2001ef5_MIT6_006S20_r03.pdf) and [official course resource page](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/mit6_006s20_r03/).
- [MIT-hosted Leighton notes](https://courses.csail.mit.edu/6.046/spring04/handouts/akrabazzi.pdf).
- [Stanford lecture text](https://stanford-cs161.github.io/winter2025/assets/files/lecture3-notes.pdf), [solved concept checks](https://stanford-cs161.github.io/winter2025-bank/recurrence.pdf), and [course lectures](https://stanford-cs161.github.io/winter2025/lectures/).
- [CMU 2011 lecture collection](https://www.cs.cmu.edu/afs/cs/academic/class/15451-f11/www/lectures/lects1-10.pdf).
- [Princeton recurrence text](https://aofa.cs.princeton.edu/20recurrence/) and [official course materials](https://aofa.cs.princeton.edu/online/).
- [Cornell 2009 lecture](https://www.cs.cornell.edu/courses/cs3110/2009sp/lectures/lec20.html) and [2011 recitation](https://www.cs.cornell.edu/courses/cs3110/2011sp/Recitations/rec19.htm).
- [Berkeley historical syllabus](https://people.eecs.berkeley.edu/~demmel/cs170_Spr10/).
- [Oxford 2021–22 course](https://www.cs.ox.ac.uk/teaching/courses/2021-2022/algdesign/).
- [ETH 2022 course](https://lec.inf.ethz.ch/DA/2022/).

Downloaded reference hashes are in research/a_recurrence-source-downloads.json; reference files remain in temporary read-only use. All teaching prose and figures are newly authored. Deferred Iranian entrance-exam archives were not opened or classified. Literal all-world coverage, a zero-error guarantee, and performance on every unseen question cannot be certified.
