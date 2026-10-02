# Relations: written-course selection and synthesis audit

Review date: 2026-10-02. Topic: d_relations, Discrete Mathematics Chapter 5, first scheduled in Week 2. Four principal university courses and one independent focused supplement inform the chapter.

## Search boundary and selection method

Searches targeted official university lecture notes, slides with readable text, and written exercises on relation properties, equivalence, closures, partial orders, bounds, and well-foundedness. The candidate pool below spans nine universities. Accessible chapter-level texts received deeper reading after a preliminary comparison of coverage and prerequisites. A catalogue or search result is not counted as reading the lecture body. This is a bounded search, not a proof that every course offered worldwide was found or exhaustively read. Course dates are kept distinct from current catalogue dates.

Selection criteria were: explicit definitions and theorem hypotheses; breadth within this chapter; availability of substantive written text; proofs and problem types; complementarity with other sources; and the work required to correct omissions or imprecise claims. Reputation alone did not decide selection. Instead of inventing decimal rankings, the register records each text's actual contribution and limitations.

| University and offering | Review depth | Decision and reason |
|---|---|---|
| MIT, 6.042J / 18.062J, Fall 2010; Tom Leighton and Marten van Dijk | Chapter 7, PDF pp. 1–24, read as extracted text; property page visually checked against PDF p. 11. | Principal. Best application coverage in this pool: typed relations, scheduling, linear extensions, and finite height/width implications. Some partition proofs are omitted; terminology separates function and totality. |
| Stanford, CS103, Spring 2017; Keith Schwarz | Binary Relations I: pp. 7–8, 17–21, 24–25, 28–36, 42–49, 56–57. Binary Relations II: pp. 4–20, 27–28, 40–42, 64–78. Problem Set 3 relation questions on pp. 2–4. Original slide p. 69 visually checked. | Principal. Strongest definition-based proof exercises and counterexamples in the pool. Limited coverage of closures and bounds; repeated animation pages and announcements excluded from the reading claim. |
| Cambridge, Discrete Mathematics, Michaelmas 2003 / Lent 2004; Peter Robinson | Printed pp. 35–43 / PDF pp. 37–45 read; PDF p. 40 visually checked for Boolean matrices. Cover and syllabus also inspected. | Principal. Adds closure-existence conditions, Warshall's invariant, well-founded induction, and rich closure exercises. Several overbroad source claims require correction. |
| Oxford, Discrete Mathematics, Michaelmas 2010; Andrew D. Ker | Chapters 4 and 8, PDF pp. 55–66 and 107–120, read including exercise answers; PDF p. 115 visually checked for bounds and quantifier direction. | Principal. Broad formal account of relations, constrained counting, orders, bounds, and isomorphisms. Contains errors documented below. The later 2022–2023 catalogue was only screened and is not attributed to Ker. |
| Cornell, CS2800, Spring 2017; Michael George | Independently authored Lecture 6 relation section and all Lecture 7 read as HTML text; course page inspected for author/year. | Focused fifth source. Useful quotient and representative-independence emphasis; too brief for the principal treatment of orders. Its linked MIT textbook is not counted as independent Cornell authorship. |
| CMU, 21-127 Concepts of Math, Summer I 2018; Shaun Allison | Official course page and reading/assignment list screened. Textbook link and equivalence assignment located; chapter body not deeply reviewed. | Not selected as a principal text. Accessible pool already provides complementary relation/order/closure instruction; catalogue-only screening is not scored as text synthesis. |
| Princeton, COS510, Spring 2013; Software Foundations, Relations chapter | HTML definitions of properties and reflexive transitive closure examined, including closure rule structure. Coq-only exercises not worked. | Not principal. Useful formal perspective but Coq prerequisites and limited bounds/Hasse coverage add burden. The separate Princeton-hosted MIT textbook mirror is not a distinct independent source. |
| Berkeley, CS70, Fall 2026 | Official course overview and note list screened. No broad relation/order chapter was selected from it. | Not principal for this boundary; strong mathematical course does not automatically match this particular chapter. No assertion is made that all Berkeley courses lack these topics. |
| ETH Zurich, Discrete Mathematics, Autumn 2026; catalogue listing | Official catalogue and textbook availability entries screened during search; a complete relevant lecture body was not read. | Not principal. Catalogue and physical-library availability alone do not meet the written-text reading requirement. No rejection of scientific quality is implied. |

The register includes nine universities. Oxford's two catalogue/text offerings and the Princeton mirror are not extra universities. There are four principal courses plus Cornell, not five repackaged copies of one book.

## Evidence and provenance

Downloaded reference PDFs remain outside the site, in the system temporary research directory. Their verified original URLs, page counts, and SHA-256 hashes are recorded in research/d_relations-source-downloads.json. Only original authored manuscripts, the source audit, and generated educational assets are published. No source PDF or extracted course transcript is republished in the site or GitHub chapter bundle.

Text extraction loses some relation negations and misorders matrix entries. The four sample original pages were rendered and inspected. Stanford's missing extraction slashes were verified as negated symbols in the original slide. Cambridge's matrix was read as a Boolean table rather than trusting the extracted sequence of characters. More generally, extracted typography is evidence to interpret, not an automatic source of correct mathematical statements.

## Corrections and hypothesis reconciliation

1. MIT uses a right-unique relation as a function and separately specifies totality. This chapter reserves total function for exactly one output at every source and explicitly distinguishes partial functions.
2. Cambridge's first-then composition notation is opposite the function-compatible convention used here. Every composition and Boolean product was reconciled with the explicit witness definition.
3. Cambridge, printed p. 40, says any irreflexive relation on a finite set is well-founded. A directed two-cycle refutes this. The chapter states finite acyclicity as the correct general criterion and proves the finite strict-order special case.
4. Cambridge's assertion about eventually constant descending sequences requires order/acyclicity qualifications. A predecessor-free nonempty-subset definition is used as the primary definition, with a direct minimal-element proof of lexicographic well-foundedness. The full dictionary-order descending example is retained with an explicit alphabet order.
5. Cambridge's fraction example must exclude zero denominators; the chapter states positive denominators and provides a transitivity counterexample when zero is allowed.
6. Cambridge's well-founded induction is presented here with one universally quantified induction step; its minimal cases are included by vacuity. No separate base claim is silently substituted for the full predecessor hypothesis.
7. Oxford, printed pp. 99–100, applies a lexicographic construction to arbitrary preorders using comparison plus inequality for its strict part. Returning between equivalent unequal first coordinates can violate transitivity. The chapter states the valid poset construction and supplies an explicit counterexample in Problem 46.
8. Oxford, printed p. 105, calls ordinary real order a complete lattice. It is not: empty subsets and unbounded subsets need endpoints. The chapter distinguishes a complete lattice from the bounded-nonempty least-upper-bound property and chain completeness.
9. Oxford's printed p. 105 formulation of no upper bound reverses the witness comparison. The correct failure of candidate upper bound u is some subset member s with s not below u. All bound definitions in the manuscript use that direction.
10. Oxford's answer to exercise 8.4(i) describes upper bounds as divisors of the lcm. They are its multiples; the lcm is least in divisibility order. The chapter independently derives both gcd and lcm roles.
11. Cornell's generalized smallest-extension phrasing needs existence hypotheses; these are supplied from Cambridge's intersection criterion. Antisymmetric extension failure is explicitly taught.
12. Cornell's sequence-rearrangement quotient must retain multiplicities; it produces multisets rather than fixed-size subsets when repeated entries are allowed. No incorrect subset claim is adopted.
13. Directed reachability is distinguished from undirected connectivity and from mutual directed reachability. Only the appropriate constructions are called equivalence relations.
14. MIT's finite chain-length convention counts vertices. This chapter uses that convention throughout scheduling and height arguments, and excludes self-comparisons when speaking of strict task predecessors.

## Topic-to-source-and-problem matrix

| Teaching boundary | Principal / supplemental support | Worked-problem coverage |
|---|---|---|
| Typed relation, active domain/range, functional constraints, images | MIT §7.1–7.2; Cambridge p. 35; Oxford §4.1 | 1–3 |
| Converse, composition, witnesses, Boolean matrix orientation | MIT §7.1.4–7.1.5; Cambridge p. 35; Oxford §4.4–4.5 | 4–7 |
| Properties, vacuity, nonnegation, partial equivalence, alternative axioms | MIT §7.3; Stanford I/II and PS3; Oxford §4.2 | 8–14 |
| Counting local entry constraints | Oxford §4.6; Cambridge exercises 3–4 | 2, 15, 25 |
| Powers, positive/zero-length closure, finite cycle bounds | Oxford §4.4; Cambridge pp. 36–37 and exercises 6–10; MIT §7.6 | 16–23 |
| Closure existence, leastness, noncommuting operations | Cambridge pp. 36–37; Cornell Lecture 7 | 20–23 |
| Warshall recurrence, pivot invariant, in-place argument | Cambridge pp. 37–38; original independent loop-order counterexample | 18–19; laboratory |
| Partitions, quotient classes, representatives, rational equivalence | Oxford §4.3; MIT §7.4; Stanford; Cambridge p. 36; Cornell Lecture 7 | 10, 14, 24–27 |
| Preorder quotient and strongly connected classes | Oxford §8.1; original proof from relation/quotient foundations | 28–29 |
| Strict/nonstrict, product/lexicographic, isomorphism | Oxford §§8.1–8.2, 8.6; Cambridge pp. 38–39; Stanford PS3 | 30–31, 40, 46 |
| Covers, finite reconstruction, Hasse geometry | Oxford §8.3; MIT §7.6.4; Stanford PS3, Problem Five | 32–33 |
| Extrema, bounds, ambient membership, suprema and infima | Oxford §8.4–8.5; MIT §7.7 | 34–39 |
| Lattice identities and limits of completeness | Oxford p. 105 qualified; original bound-based derivations | 36, 39, 45 |
| Linear extensions, layers, height–width bounds, subsequences | MIT §§7.7–7.9; Cambridge p. 41 | 33, 41–42 |
| Dilworth chain partition, matching-cover proof | Original self-contained advanced extension of MIT's finite chain–antichain discussion | 33, 43 |
| Well-foundedness, induction, recursive descent | Cambridge pp. 40–42, corrected; prior approved induction chapter | 44, 46 |

All forty-six solutions are authored and checked within this chapter. Course-derived indicates an attributed mathematical pattern, not copied exercise prose or a claim that all source exercises were reproduced. Each of the twelve top-level sections has a declared role; the deliberately concise final review is separate from the detailed lesson.

## Reference links

- [MIT course](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/) and [Chapter 7](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/efac321fdc8d0b27586ca35b04aab808_MIT6_042JF10_chap07.pdf).
- [Stanford CS103 archive](https://web.stanford.edu/class/archive/cs/cs103/cs103.1176/), [Relations I](https://web.stanford.edu/class/archive/cs/cs103/cs103.1176/lectures/06/Small06.pdf), [Relations II](https://web.stanford.edu/class/archive/cs/cs103/cs103.1176/lectures/07/Small07.pdf), [Problem Set 3](https://web.stanford.edu/class/archive/cs/cs103/cs103.1176/handouts/150%20Problem%20Set%203.pdf).
- [Cambridge, Peter Robinson notes](https://www.cl.cam.ac.uk/teaching/2003/DiscMaths/DiscMaths.pdf).
- [Oxford, Andrew D. Ker notes](https://www.cs.ox.ac.uk/andrew.ker/docs/discretemaths-lecture-notes-mt2010.pdf) and [2022–2023 screened catalogue](https://www.cs.ox.ac.uk/teaching/courses/2022-2023/discretemaths/).
- [Cornell course](https://www.cs.cornell.edu/courses/cs2800/2017sp/), [Lecture 6](https://www.cs.cornell.edu/courses/cs2800/2017sp/lectures/lec06-relations.html), [Lecture 7](https://www.cs.cornell.edu/courses/cs2800/2017sp/lectures/lec07-equivalence.html).
- [CMU screened course page](https://www.math.cmu.edu/~sallison/concepts18/index.html).
- [Princeton formal relation chapter](https://www.cs.princeton.edu/courses/archive/spring13/cos510/sf/Rel.html).
- [Berkeley screened CS70 page](https://www.eecs70.org/).
- [ETH screened catalogue](https://www.vvz.ethz.ch/Vorlesungsverzeichnis/lerneinheit.view?ansicht=KATALOGDATEN&lang=en&lerneinheitId=204115&semkez=2026W) and [textbook availability entry](https://textbooks.inf.ethz.ch/lectures/1st-semester/267/).

## Remaining limits

No universal exhaustiveness or future-exam performance guarantee is asserted. Independent finite checks validate the implemented finite model and selected identities, while the written proofs address general statements under their stated hypotheses. Source screening is not equivalent to reading an entire unrelated course. Infinite order theory and full domain/lattice representation theory remain outside this chapter's boundary. Iranian MSc and PhD archives were not examined; they remain deferred to the final month. This chapter remains a review draft until explicit student approval.
