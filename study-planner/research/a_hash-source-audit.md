# Written-source selection: hash tables and collision analysis

## Candidate evaluation

The bounded search inspected accessible written-course candidates from eight universities: MIT, CMU, Princeton, ETH Zurich, Stanford, Cambridge, Berkeley and Oxford. Each candidate was checked for relevant text, proof depth, exact algorithms, exercise coverage and retrieval accessibility. This is a documented pool, not a claim that every course worldwide was inspected. Four complementary core courses were selected after reading their relevant text; two further universities provide reviewed comparisons.

| University and course | Actual reading | Selection |
|---|---|---|
| MIT 6.006 Spring 2020; Erik Demaine, Jason Ku, Justin Solomon | All five pages of Lecture 4 through the official PDF web text; native retrieval timed out twice | Core: comparison-model boundary, direct addressing, universal hashing and indicator expectations. No native hash is invented. |
| CMU 15-122 Fall 2026; Frank Pfenning and Rob Simmons | All eleven pages of Lecture 12, including all three exercises and sample solutions, through official PDF web text; native connection refused | Core: key/entry contracts, deterministic hashing and bucket implementation distinctions. Corrections below are essential. |
| Princeton COS226 Spring 2025; Robert Sedgewick and Kevin Wayne | All 46 PDF pages of Hash Tables, and full written Algorithms section 3.4 including exercises | Core: equality contracts, exact implementation, load factors, clustering, deletion and exercise families. Native hashes retained. |
| ETH Zurich Data Structures and Algorithms Spring 2020; Felix Friedrich | All 98 pages of English Lecture 9; parameter, birthday, probing and perfect-hashing formulas also visually inspected | Core: distinct random models, probing, universal and two-level perfect hashing. Printed errors are corrected below. |
| Stanford CS106B Summer 2025; the written page credits Julie Zelenski and Sean Szumlanski | Full 19-part written hashing page, supplementary code and exam-preparation section | Additional comparison: practical traces and string-cost qualifications. Instructor identity is recorded only if independently verified; page authorship is not invented. |
| Cambridge Algorithms 2023–24; Damon Wischik, with Frank Stajano course materials | All 22 pages of lecture 8 inspected; hashing content specifically pages 16–17 | Additional comparison: dictionary/set representation. Insufficient depth for a core hashing source. |
| Berkeley CS61B Spring 2014 / CS170 Spring 2003 candidate | Official search listings inspected; native course/advanced-note requests returned 404 | Screened only. Not counted as a read source. |
| Oxford Concurrent Algorithms and Data Structures 2017–18 | Official inventory inspected; native retrieval unavailable | Screened only; concurrent hashing differs from this chapter's sequential examination scope. |

## Reconciliation and corrections

1. An average bucket has length n/m arithmetically, but a stored key sees a size-biased bucket. Uniform average bucket length alone is not a performance theorem for selected queries.
2. CMU page 9 says sorted unbounded arrays lower both lookup and insertion to logarithmic time. Binary search finds a location in logarithmic comparisons; shifting entries still costs linear worst-case time. Page 10's birthday percentage for 70 people and its implication that enough slots alone rule out collisions are not copied.
3. Princeton's chain-cost shorthand is qualified as total O(1+n/m), while entry comparisons alone can be zero for empty chains. High concentration requires an appropriate load regime; it does not follow for every fixed bucket at unit load. The collision-string exercise constructs 2^r strings of length 2r, not length r as its original heading suggests. Mutable-key lookup outcomes are not presented as universal false values.
4. Stanford's doubling example does not eliminate linear worst cases. A measured small finite average is not a universal expected-time proof. Its immediate insertion at a dirty cell can duplicate a map key already later in the probe route; this chapter remembers the dirty cell and searches for the existing key before insertion. Rearrangement by reinserting a linear-probing cluster is valid with a qualified cost.
5. ETH page 72's condition that the step does not divide the capacity is insufficient. Full-cycle double hashing requires gcd(step,capacity)=1. Page 82 must select a in 1 through p−1 and b in 0 through p−1, not restrict both to a smaller key universe. A verified counterexample accompanies the corrected family.
6. ETH pages 93–96 print m to the power m in the birthday denominator; the correct power is n. The exponential collision expression is an approximation, not an equality. Page 75's zero-tail boundary must be beyond n+1, not at capacity when n=capacity−1. Page 87 must include bucket zero in the second-level construction. Universal collision sums give inequalities, not automatically exact independent-uniform equalities.
7. Full uniform random probe permutations, independent uniform home positions, and universal pair-collision bounds are different models. Their formulas are not interchanged. Linear-probing formulas are asymptotic estimates under their specified random model, not exact counts for a displayed table.

## Scope and evidence

Coverage includes exact hash arithmetic, separate chaining, all three major probe policies, deletion and duplicate invariants, load/occupancy/collision formulas, universal hashing with a proof, resizing, two-level static perfect hashing, and carefully qualified Bloom-filter, cuckoo and Robin Hood comparisons. Cryptographic algorithm internals, concurrent hashing and optimal independence thresholds for linear probing are outside the claimed scope.

Acquisition hashes and failures are in `a_hash-evidence/acquisition.json` and `acquisition-more.json`; genuine reading is separately recorded. Original examination pages are checked visually before inclusion. Selected course exercise families are reconstructed with original data and independent extended solutions; protected source text is not redistributed as course copies.

## Written references

- MIT: [6.006 Lecture 4](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/ce9e94705b914598ce78a00a70a1f734_MIT6_006S20_lec4.pdf).
- CMU: [15-122 Lecture 12](https://www.cs.cmu.edu/~15122/handouts/lectures/12-hashing.pdf).
- Princeton: [COS226 Spring 2025 slides](https://www.cs.princeton.edu/courses/archive/spring25/cos226/lectures/34HashTables.pdf), [Algorithms section 3.4](https://algs4.cs.princeton.edu/34hash/).
- ETH Zurich: [Lecture 9, English](https://lec.inf.ethz.ch/DA/2020/slides/daLecture9.en.pdf), [course and instructor](https://lec.inf.ethz.ch/DA/2020/).
- Stanford: [Summer 2025 written hashing lecture](https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1258/lectures/24-hashing/).
- Cambridge: [Lecture 8](https://www.cl.cam.ac.uk/teaching/2324/Algorithm1/content/slides08.pdf), [course materials](https://www.cl.cam.ac.uk/teaching/2324/Algorithm1/materials.html).
