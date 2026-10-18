# CSP written-source peer review — 18 October 2026

## Review boundary and provenance

This report covers two universities, not an exhaustive worldwide search. The parent author is evaluating the other candidates. No checkout files were edited. Page numbers below are **one-based physical PDF pages**, not printed slide numbers. MIT places two slides on most physical pages.

The original official PDFs were read through the web tool's extracted PDF text. Local direct downloads repeatedly timed out during TLS connection, including the final bounded retry. Screenshot requests returned text placeholders rather than inspectable image pixels in this agent. Therefore **no visual inspection or file SHA-256 is claimed yet**. Do not convert this ledger to a fully visually audited source record until the original pages can be rendered. Acquisition failures are recorded in `acquisition-final.json`.

### Cornell University

- Course: CS4700, Foundations of Artificial Intelligence, Fall 2013.
- Lecturer: Bart Selman, identified on the title page.
- Official PDF: https://www.cs.cornell.edu/courses/cs4700/2013fa/slides/CS4700-CSP_v6.pdf
- Length: 85 physical pages.
- Main fresh reading: pp61–85, covering backtracking, MRV/degree/LCV, forward checking, arc consistency, AC-3 complexity, consistency hierarchy and AllDiff.
- Additional text read: pp1–16,32–39,44–53. These support modeling, assignment counting, queens encodings, cryptarithmetic and graph coloring. Other pages are not counted as freshly read.
- Diagram limitations: pp69–72 and77–80 are mainly visual; the textual labels were available, but color states/edges were **not** visually verified.
- Bounded appraisal: strong comparison source for explicit quantified definitions and small exam-style counterexamples; less useful than MIT for executable queue details and conflict explanations. Tree structure is listed as a technique on p62, but this packet does not teach the tree algorithm or cutset conditioning. Do not cite it as substantive support for those proofs.

### Massachusetts Institute of Technology

- Course: 16.410/16.413, Principles of Autonomy and Decision Making, Fall 2010.
- Course instructors: Brian Charles Williams and Emilio Frazzoli; the three selected constraint lectures are by **Brian C. Williams**. Lecture07a credits contributions from Patrick Prosser in the official index.
- Official index: https://ocw.mit.edu/courses/16-410-principles-of-autonomy-and-decision-making-fall-2010/pages/lecture-notes/
- Lecture05, 39 PDF pages: https://ocw.mit.edu/courses/16-410-principles-of-autonomy-and-decision-making-fall-2010/43a72dc4afb4a2813f28944d6d4d9056_MIT16_410F10_lec05.pdf
- Lecture06, 28 PDF pages: https://ocw.mit.edu/courses/16-410-principles-of-autonomy-and-decision-making-fall-2010/7434ba1355d03e83bfac5effa7edd1d0_MIT16_410F10_lec06.pdf
- Lecture07a, 21 PDF pages: https://ocw.mit.edu/courses/16-410-principles-of-autonomy-and-decision-making-fall-2010/7a5cd091e89dff7ca4eed31df8a0aa08_MIT16_410F10_lec07a.pdf
- Fresh reading scopes: Lecture05 pp10–20 and the trace text pp21–34; Lecture06 pp4–27; Lecture07a pp10–20. Title/index attribution was also checked. Lecture05 line-labeling geometry and scheduling appendix were excluded from substantive use. Lecture07a pp1–9 are mostly graphical setup and were only surveyed, not fully reconstructed.
- Bounded appraisal: strongest of these two candidates for AC-1 versus AC-3 analysis, transactional domain restoration and conflict-set propagation. The conflict-directed material fills a genuine gap rather than merely duplicating elementary backtracking. Retain as a substantive primary or fifth source when the full chapter includes CBJ. Old empirical queens limits and machine-time plots are historical context, not performance guarantees.

## Source issues and claims to quarantine

1. **Cornell p8:** the number of distinct complete assignments is written as n^d twice; it must be d^n for n variables of uniform domain size d. Its unrestricted action-order search has n! d^n paths at depth n; fixing one variable per depth removes ordering duplicates.
2. **Cornell p32:** 8^8 is approximately 1.6×10^7, not 1.6×10^6. Exact independently computed count: 16,777,216.
3. **Cornell p37:** the 2013 slide calls queens completion an open NP-completeness conjecture. This is historically obsolete. Gent, Jefferson and Nightingale proved NP-completeness and #P-completeness in 2017: https://doi.org/10.1613/jair.5512 . Only the abstract/result was checked here; no claim of reading the full proof.
4. **Cornell p51:** NP-completeness by itself is not an unconditional exponential-time lower bound. State that a polynomial general solver would imply P=NP; a specific exponential lower bound needs additional assumptions.
5. **Cornell p81:** the dense graph bound O(n²d³) is a valid upper bound for a simple binary graph, but n² is not literally the number of constraints. The sparse formulation is O(e d³). A worklist contains **directed arcs**, not variables. Reprocessing is charged to changes in the supporting/head domain.
6. **Cornell pp83–84:** use strong n-consistency, including nonempty unary-consistent domains, for the general backtrack-free extension claim. Bare n-consistency can hold vacuously when no consistent (n−1)-assignment exists. Binary path consistency alone need not include lower consistency levels unless stated.
7. **MIT Lecture06 p7:** extracted AC-3 initialization repeats (xi,xj) rather than including the reversed arc. Lecture05 p20 explicitly gives (xi,xj) and (xj,xi). This is a **suspected source typo pending original pixels**, not a verified typesetting error. Never reproduce the duplicate initialization.
8. **MIT Lecture05 p20 / Lecture06 p7:** worklist reinsertion must restrict xk to actual neighbors of xi. The printed abbreviated comprehension only excludes i,j. Adding nonexistent arcs is not a correct implementation of a sparse binary constraint graph.
9. **MIT Lecture06 p22:** the extracted Select-Value-FC indentation is ambiguous. Returning after checking only one future variable would be unsound. The independent chapter algorithm must check every relevant unassigned neighbor, reject if any domain empties, and restore all branch deletions on failure.
10. **MIT Lecture07a p19:** the Dechter pseudocode and supporting definitions are explicitly removed for copyright. They cannot be counted as read or reconstructed from this packet. The accessible Prosser-style forward checks and explicit conflict-set update on pp11–18 are sufficient to motivate an independently written, tested version.

## Precise source-derived exercise data, paraphrased

These are mathematical reconstructions suitable for attribution as adapted course exercises, not claims of original authorship or official solutions. No original images should be copied.

| ID | Exact location | Reconstructed task/data | Independently checked conclusion |
|---|---|---|---|
| MIT-Q13 | Lecture05 p13, printed slide26 | Four queens; Qi is the row of the queen in column i, domains {1,2,3,4}; list allowed pairs C13 under unequal rows and diagonal avoidance. | C13={(1,2),(1,4),(2,1),(2,3),(3,2),(3,4),(4,1),(4,3)}. |
| MIT-AC3-TRIANGLE | Lecture05 pp20–34 | Three pairwise-unequal color variables V1:{R,G,B}, V2:{R,G}, V3:{G}; trace a declared directed-arc queue. | Unique solution and final closure: (V1,V2,V3)=(B,R,G). Every deletion must show its missing support. |
| MIT-AC-COST | Lecture06 pp4–7 | n variables, e binary constraints, maximum initial domain k; derive REVISE, AC-1 and AC-3 costs under constant-time relation checks. | REVISE O(k²); AC-1 O(e n k³); AC-3 O(e k³). These are upper bounds for the specified naive algorithms. |
| CORNELL-RELATION | p76 | Dx={1,2,3}, Dy={3,4,5,6}; allowed pairs {(1,3),(1,5),(3,3),(3,6)}; find the arc-consistent restricted domains. | Dx'={1,3}, Dy'={3,5,6}; x=2 and y=4 lack support. |
| CORNELL-TRIANGLE | p82 | Three variables, all domains {1,2}, pairwise inequality; determine arc consistency and satisfiability. | Both directed orientations of every edge have support, but no solution exists: three distinct values would be required. |
| MIT-CBJ-MERGE | Lecture07a pp13–17 | Dead variable6 has conflict set {4,1,0}; variable4 currently has {2,0}; apply the deepest-conflict jump and merge, then exhaust4. | Jump6→4; Conf4 becomes {2,1,0}; reset variables5,6; next exhaustion of4 jumps to2. Index0 is the termination sentinel, not an actual decision. |

Machine checks for the first, second, fourth and assignment count are in `independent-checks.json`. A root author still needs to connect any adapted prompt to complete explanatory solutions and figures; this report alone is not a lesson.

## Independent mathematical guidance for the chapter

The following are derivations/checks by this reviewer, not quotations or claims that the exact proofs appear in the packets.

### AC-3 invariant and cost proof

Let S be the original full solution set. A value a in Di is removed only when no b in the current Dj satisfies Rij. If a full solution still present used a, its j-value would be a support, a contradiction. Inductively every original solution survives every deletion. This is a **solution-preserving filter**, not a complete satisfiability decision procedure.

Domains decrease monotonically through a finite lattice. Fair processing terminates. At worklist exhaustion every arc is consistent: any lost support would have caused that incoming arc to be reinserted. To prove the greatest closure, take any arc-consistent subdomains E contained in the original domains. At each removal, a value of Ei must have a support in Ej, which remains inside the current Dj by induction, so it cannot be removed. Thus E remains contained in the final closure. This also explains schedule independence of the final successful domains.

For m directed arcs (m=2e for e undirected binary constraints) and maximum initial domain d, each arc is initially scheduled and can be rescheduled at most d times due to losses in its head domain. A naive revision scans at most d² pairs. Hence O(m d³)=O(e d³) relation checks. Keep queue deduplication explicit; memory O(e+n d) includes domains and pending arcs, with relation storage accounted separately. If one relation lookup costs T rather than O(1), multiply the bound by T. Precheck empty domains, including isolated variables; an empty initial isolated domain would otherwise never trigger REVISE.

The usual exclusion of the just-processed reverse arc is safe when each edge represents one merged relation and reversing an edge uses its transpose. If multiple predicates share a scope, first intersect them or make the consistency test conjunctive; independent supports for separate predicates can be incompatible. For example X,Y in {0,1} with X=Y and X≠Y: separate constraints each appear arc-consistent, while their conjunction is empty.

### A conflict set is an explanation, not a list of nearby vertices

For a dead variable Xi, every candidate value must have a sound rejection reason in earlier assignments. The union of those reasons identifies a prefix nogood. If its deepest decision is Xh, changing later decisions cannot invalidate that explanation; jumping to h is sound. On exhaustion at i, merge Conf(i) minus {h} into Conf(h). Without this merge, successive jumps can discard the explanation that justified rejection at h. Reasons need not be minimal, but a smaller valid explanation can permit a longer jump. Forward-checking domain deletions require their own recorded explanations; a naive direct-conflict-only set cannot be used unchanged in a MAC/FC hybrid.

### Consistency hierarchy edge case

Three variables each with singleton domain {0} and pairwise inequality provide a useful vacuity check: no consistent assignment exists to two variables, so the extension condition for 3-consistency is vacuously true; 2-consistency fails. Therefore a bare n-consistency claim must not silently replace **strong n-consistency**. The latter supports successive extension from a consistent empty assignment, provided unary conditions and nonempty domains are included.

### Remaining primary-source gap

The two reviewed packets do not substantively establish the tree solver O(n d²), cycle-cutset conditioning, treewidth elimination, or Hall-based AllDiff filtering. Those parts must be grounded in the parent's Stanford/Berkeley/CMU written reading. Do not list this MIT/Cornell reading as evidence for a derivation it does not contain. MIT is a strong specialized CBJ contributor; Cornell provides useful correctness counterexamples and modeling comparisons. Final selection should be based on the complete bounded pool and the actual chapter outline, not an arbitrary count of universities.
