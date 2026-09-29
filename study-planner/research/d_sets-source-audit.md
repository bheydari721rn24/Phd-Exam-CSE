# Sets and set operations: written-course audit

## Search boundary and ranking rule

This is a bounded search of publicly accessible written materials from university course sites, performed 2026-09-29. It is not a census of every course worldwide. A course is counted as **read** only when its relevant written pages were opened and examined, not when only a syllabus or search result was found. Ranking for this chapter favors precise set semantics, proof technique, edge cases, diagrams, and independently checkable exercises. It does not rank universities in general.

| Candidate | Material and review level | Strength for this chapter | Limit and decision |
| --- | --- | --- | --- |
| MIT 6.042J, *Mathematics for Computer Science*, Lehman, Leighton, Meyer, 2015 (Meyer and Chlipala: course instructors) | Textbook section 4.1, printed pp. 81–85 (PDF pp. 89–93), read. [PDF](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf); [course page](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) | Extensional membership definitions, basic operators, power sets, elementwise distributive proof. | PDF text extraction loses mathematical glyphs; notation was cross-checked against other texts. **Selected.** |
| Stanford CS103, Amy Liu's Winter 2024 course, *Guide to Proofs on Sets* | Entire accessible handout read. [HTML](https://web.stanford.edu/class/archive/cs/cs103/cs103.1244/guide_to_proofs_on_sets); [introductory slides](https://web.stanford.edu/class/archive/cs/cs103/cs103.1244/lectures/00/Lecture%20Slides.pdf), opening portion checked for instructor and topic alignment. | Explicit templates for subset, equality, union, intersection, difference, and power-set proofs. | Mainly proof method, not a full standalone introduction. **Selected.** |
| Cornell CS2800, *A Course in Discrete Structures*, Pass and Tseng, 2015 | Chapter 1.1, printed pp. 1–5 (PDF pp. 5–9), read. [PDF](https://courses.cs.cornell.edu/cs2800/2015fa/handouts/pass_tseng_discmath.pdf) | Informal set foundations, operations, Cartesian products, CS strings, Venn diagrams, example of two-containment proof. | Does not by itself develop the advanced empty-family convention. **Selected.** |
| Carnegie Mellon 15-151, *Mathematical Foundations for Computer Science*, Sutner, 2022 | Set Operations, 26-slide deck, and Cartesian Products, 27-slide deck, relevant slides read and compared. [Set Operations](https://www.cs.cmu.edu/~sutner/pdf/10-sets.pdf); [Cartesian Products](https://www.cs.cmu.edu/~sutner/pdf/15-sets.pdf) | Extensionality, bounded specification, symmetric difference, Boolean laws, indexed families, empty-family caution, tuple/product details. | Slides assume classroom explanation; one Cartesian-product proof slide has a typographic membership slip, corrected in this chapter. **Selected.** |
| UC Berkeley CS70, *Mathematical Foundations*, Summer 2024 | Note 0, relevant first 3–4 of 5 pages read. [PDF](https://su24.eecs70.org/assets/pdf/notes/n0.pdf) | Concise baseline for notation, products, power sets, finite cardinality. | Too brief to be a primary source for all edge cases; **supplemental fifth text**. |

The set chapter does not need separate Oxford or ETH sources to fill an identified gap after these five texts; no claim is made that those courses are inferior. A catalogue-only course is not counted as read. The four selected sources are from four separate universities; Berkeley is a fifth genuinely reviewed written course. Course-derived problem **types** are paraphrased and fully re-solved; no course question is represented as a verbatim reproduction.

## Source-to-topic comparison

| In-scope pattern | MIT | Stanford | Cornell | CMU | Berkeley | Synthesis target |
| --- | :-: | :-: | :-: | :-: | :-: | --- |
| Membership, equality, subset, proper subset | ✓ | ✓ | ✓ | ✓ | ✓ | Distinguish element from set and subset from membership; two-inclusion proofs. |
| Empty set and nested-set edge cases | ✓ | ✓ | ✓ | ✓ | ✓ | Work out ∅, {∅}, and power-set membership carefully. |
| Union, intersection, difference, complement | ✓ | ✓ | ✓ | ✓ | ✓ | Give elementwise semantics with a fixed universe for complement. |
| Symmetric difference and Boolean identities | — | ✓ | — | ✓ | — | Derive associative XOR behavior and Venn regions. |
| Indexed unions/intersections and empty index | — | — | — | ✓ | — | State index-domain convention and why empty intersection needs U. |
| Cartesian product, tuples, distribution | — | — | ✓ | ✓ | ✓ | Prove product identities and identify false distribution over arbitrary sets. |
| Power set and finite cardinality | ✓ | ✓ | ✓ | ✓ | ✓ | Prove subset/power-set links and counting by binary choices. |
| Finite inclusion–exclusion | — | — | — | — | — | One elementary two/three-set derivation is included as a bridge; systematic counting remains in the counting chapter. |
| Russell paradox / unrestricted comprehension caution | — | — | ✓ | ✓ | ✓ | Explain only the precise construction caveat, without a deep axiom-system detour. |

## Error and boundary log

- PDF text extraction from MIT confuses set intersection, backslash, membership and negation glyphs. Definitions and theorem statements were validated semantically against the other sources; the extracted glyphs were not copied.
- A CMU Cartesian Products proof slide appears to write membership in intersections of the factors where membership in Cartesian products is required. The elementwise proof in the lesson uses ordered-pair membership correctly.
- Complement is always relative to a declared universe. The empty intersection is U only when a common universe U is fixed. For a family indexed by an empty set without a universe, there is no universal set of all objects in ordinary ZFC.
- The finite-cardinality formulas explicitly require finite sets; multiplication and inclusion–exclusion for infinite cardinals are not silently inferred.
- Archived Iranian entrance-exam booklets are intentionally deferred until the final month by the student's latest instruction; this is not a claim that the present chapter has been calibrated to those questions.

## Reasoning-pattern coverage in the draft

| Pattern | Full explanation | Worked problems | Final review |
| --- | --- | --- | --- |
| Nested ∅, membership, subset, builder domain | §2 | 1, 2, 14 | §6.1 steps 1 and 6; §6.2 empty-set and power-set rows |
| Two-containment equality and a disjoint decomposition | §§2.2, 3.2 | 3, 6, 7 | §6.1 steps 3–5 |
| Difference, complement, De Morgan, non-cancellation | §§3.1–3.3 | 4, 5, 17, 18 | §6.2 difference and De Morgan rows |
| Symmetric difference and a false identity countermodel | §3.2 | 8, 9, 20 | §6.3 Boolean-pattern notes |
| Indexed-family quantifiers and empty index | §4.1 | 10, 11, 17 | §6.2 indexed rows |
| Product coordinate proof and empty-factor exception | §4.2 | 12 | §6.2 product rows |
| Power-set intersection/union and mixed-subset witness | §4.3 | 13, 14, 16, 19 | §6.2 power-set rows |
| Finite overlap and consistency check | §4.3 | 15 | §6.3 region-counting note |
