# Relations chapter: quality and delivery audit

Date: 2026-10-02. Status: review draft, awaiting explicit student approval. No next chapter is authorized by this handoff until approval arrives.

## Authoring and mathematical review

The English manuscript consists of research/d_relations.en.md, research/d_relations-problems.en.md, and research/d_relations-review.en.md. It contains a deep teaching body, 46 complete worked problems, 72 complete examination rules, a decision table mapping reasoning patterns to worked examples, four original vector diagrams, and a finite interactive laboratory. The approved previous library remains available.

Four principal written courses from MIT, Stanford, Cambridge, and Oxford were genuinely read in the ranges recorded in the source audit. Cornell's independently authored quotient notes supply a fifth focused source. A nine-university search pool is documented without equating catalogue screening with full reading. Source errors and convention conflicts were corrected rather than copied into the lesson. No original course PDF or transcript is republished. Archived Iranian entrance-exam papers were not inspected.

The review checked each definition, quantifier, witness, theorem hypothesis, proof dependency, composition direction, matrix convention, finite/infinite qualification, worked conclusion, and final rule. Particular risks reviewed include repeated-vertex transitivity, cycle-induced loops, partial equivalence, right-Euclidean and cyclic axioms, rational denominators, quotient well-definedness, preorder lexicographic failure, finite cover reconstruction, minimal versus least bounds, lattice completeness, unit-task assumptions, matching-cover certificates, and well-founded induction.

## Independent finite validation

- research/verify_d_relations_en.py checked all 531 relations on carriers of sizes zero through three. It verified the manuscript's Python Warshall implementation against independent graph search, the finite positive-power bound, the alternative equivalence axioms, strict/asymmetric equivalence, and constrained counts. It independently confirmed the cycle's exact pivot-stage additions, the incorrect-loop-order counterexample, the divisor cover edges, the task chain partition, problem numbering, and rule numbering.
- research/verify_relations_lab.cjs checked all 65,536 relations on the laboratory's four-element carrier. It compared positive closure and zero-length closure with independent graph traversal, equivalence closure with undirected traversal, and seven property verdicts with pair-set definitions. Every returned failure witness was also checked.
- These finite checks validate the displayed finite examples and the implementation. They do not replace the mathematical proofs or establish correctness for every infinite carrier or every unseen future examination question.

## Presentation and laboratory checks

The chapter-specific browser audit opens the actual rendered HTML in Edge and waits for bundled fonts to load. Mathematical text, display formulas, MathML operators and limits, indices, and SVG mathematical labels use STIX Two Math. Code uses JetBrains Mono; prose uses Source Sans 3 and headings use Newsreader. The common no-underlining rule is preserved. Unrendered exponent carets and mathematical underscore indices are prohibited by the verifier.

All four diagrams were captured and visually inspected. Their cover/composition/partition/dependency structures match the accompanying text. Automated bounds checks found no mathematical label outside its view box and no overlapping label pair. Desktop rendering, a 390-pixel mobile viewport, and A4 print styling were checked. The document width stayed within the mobile viewport; formula blocks had no horizontal overflow; all diagrams fitted their print containers. Mobile diagrams retain legible labels in a local horizontal viewing region.

The interactive controls were exercised in the browser: all 16 matrix buttons were present; the three-cycle preset produced the expected final positive closure with an isolated fourth vertex; the last-stage control disabled after four pivots; editing an input cell reset the computation to stage zero. The browser exercises are recorded alongside the layout/font observations in research/d_relations-evidence/browser-review.json. A favicon request on the local preview returned 404; it has no effect on chapter content or the tested model.

Source reference PDFs were separately rendered read-only and inspected for notation damaged by text extraction. No deliverable PDF is claimed: the study-facing artifact is printable HTML.

## Delivery gate and remaining limits

The finished review draft is dist/chapters/d_relations.html. Its source-selection audit is dist/reviews/d_relations-sources.html. The chapter index lists it under Week 2 as draft; approved Week 1 chapters remain ready. The gate state is awaiting_user_approval. A known error or omission is not being hidden by a ready label.

Coverage is defined by the stated chapter boundary. Advanced infinite-order and domain-theory results outside that boundary are not claimed. Some candidate courses were catalogue-screened only. Original and independently worded course-derived problems cover the identified reasoning patterns but do not reproduce every exercise ever published. The source/proof/finite/browser audit is evidence for this draft, not a literal 100% performance guarantee. The next step is the student's review and explicit approval of this one chapter.
