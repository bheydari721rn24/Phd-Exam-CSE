# Constraint satisfaction: bounded candidate evaluation started

## Delivery boundary

The preceding rank revision is complete and published privately as version 110. The next new chapter is `i_csp`; it has not yet been added to the authored-chapter count. Four contributing written courses from four universities have not yet passed the full reading and reconciliation gate for this new chapter. Course discovery, file acquisition and actual reading are distinct states.

## Candidate pool and current reading

| University | Accessible written candidate | Current evidence and decision |
| --- | --- | --- |
| UC Berkeley | CS188 textbook, sections 2.1–2.6 | Complete prose of 2.3 Filtering and 2.4 Ordering/Structure read. Embedded pseudocode and map images are not yet visually checked. Remaining sections and exercises still require reading. Strong candidate for propagation, ordering and tree structure. |
| CMU | 15-281 Fall 2025, CSP course notes | Complete written page, including textual pseudocode and complexity arguments, read. Embedded map/arc images not yet visually read. Strong candidate for the binary algorithm foundation, subject to the corrections below. |
| Stanford | CS221 Spring 2026 modules and written source bodies | Course module index inspected. CSP modeling, factor graphs, dynamic ordering and arc-consistency modules identified. Actual source bodies not yet read; no selection claim. |
| MIT | 16.410 Fall 2010, Brian Williams: Constraints I–III | Official lecture-note index located. Actual lecture PDFs not yet read; promising advanced coverage of constraint programming, satisfaction and conflict-directed backjumping. |
| MIT | 6.034 Fall 2010, Patrick H. Winston: Lectures 7–9 and Tutorial 2 | Written transcript/tutorial candidates located through the official course index. Not yet read. This is another course, not another university. |
| Cornell | CS4700 Fall 2013 CSP slides | Official written slide candidate located; acquisition and reading remain separate. Potential additional perspective; instructor attribution will be verified from the actual offering. |
| Harvard | CS50 AI, Optimization notes and crossword project | The complete CSP-through-final-summary prose and textual pseudocode were read from the freshly acquired official note. Earlier local-search/linear-programming portions and embedded images were not counted. The crossword specification was additionally inspected through its official page. Useful implementation comparison, not yet a selected primary. |

Official references:

- [Berkeley Filtering](https://inst.eecs.berkeley.edu/~cs188/textbook/csp/filtering.html), [Ordering and Structure](https://inst.eecs.berkeley.edu/~cs188/textbook/csp/ordering.html).
- [CMU CSP notes](https://www.cs.cmu.edu/~15281-f25/coursenotes/constraints/index.html).
- [Stanford modules](https://stanford-cs221.github.io/spring2026/modules/).
- [MIT 16.410 written lecture index](https://ocw.mit.edu/courses/16-410-principles-of-autonomy-and-decision-making-fall-2010/pages/lecture-notes/).
- [MIT 6.034 resources](https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/download/).
- [Cornell CSP slides](https://www.cs.cornell.edu/courses/cs4700/2013fa/slides/CS4700-CSP_v6.pdf).
- [Harvard optimization notes](https://cs50.harvard.edu/ai/notes/3/), [crossword project](https://cs50.harvard.edu/ai/projects/3/crossword/).

This is seven candidate offerings from six universities, not an exhaustive worldwide search or a final ranking. Selection will depend on proof precision, coverage, complementary examples, visible written exercises and actual successful reading.

## Reconciliation findings already identified

The CMU textual backtracking wrapper calls `backtracking` although the recursive function is named `backtrack`. Its sketch does not expose domain restoration or the complete domain-wipeout failure contract. These must be explicit in executable chapter code. Its forward-checking bound is deliberately coarse; after an assignment restricts the head to one value, a tighter implementation-specific bound is possible. Its prose description of least-constraining value speaks of neighbors, while the chapter must state whether it counts deleted values or affected variables; these are different scores.

Harvard's MAC discussion describes inference output as assignments, but general propagation also removes values from domains without making any singleton assignment. Both effects and their restoration on backtracking must be represented. Its simple AC-3 sketch detects emptiness after a deletion; robust executable code must also reject initially empty isolated domains. Its LCV prose similarly counts affected variables, which must not silently replace a declared deleted-value score.

Berkeley's reenqueue wording must be read as existing incoming constraint arcs, not unconstrained ordered pairs. Its cutset bound assumes a supplied cutset and excludes the work of finding a minimum one. A chapter proof must also check constraints inside the assigned cutset, account for boundary pruning and handle empty residual graphs. Merely multiplying by the number of residual variables can incorrectly report zero work when every variable is in the cutset. These are scope/implementation qualifications; source statements are not copied without their hypotheses.

## Required chapter and question mechanisms

The planned scope starts with variables, domains, relations, partial assignments and exact solution semantics. It proceeds through binary graphs versus higher-arity constraints, commutative assignment search, finite backtracking soundness/completeness, deterministic tie rules, MRV/degree/LCV, forward checking versus maintaining arc consistency, domain trails and restoration, AC-3 queue direction and its soundness/fixed-point/termination/complexity proofs, arc-consistent unsatisfiable cycles, stronger consistency, tree/forest solving, supplied cutset conditioning, and the limits of incomplete local search. All-different needs a distinction between pairwise inequalities and stronger global propagation. Weighted factor graphs must not be confused with plain feasibility.

Visuals must trace actual support witnesses, directed queue changes, deleted domain values, restored branch state and complete constraint checks. Candidate solved tasks include support-table calculations, exact deletion and requeue counts, propagation versus satisfiability counterexamples, conditional complexity derivations, tree assignments, cutset branches and global-constraint comparisons. Original Iranian examination questions will be identified and checked against original PDF images before inclusion. No fabricated examination provenance or automatic official-key claim is allowed.

The full question bank, final decisions, executable models and browser gates are still pending. Neither a completed note nor four fully read primary courses is claimed at this checkpoint.

## Acquisition boundary

The official Harvard note was freshly downloaded, SHA-256 `558694fb0f929c720c5f9b6a271316bfcbd21595dd17c40a34f85b0ad529efa7`. Six other direct acquisition requests failed on local DNS, connection or read-timeout errors. Berkeley and CMU prose reading succeeded through the web reader independently of those direct-download failures; no local byte fingerprint is invented for those reads. Stanford, MIT and Cornell remain at discovery/index or unsuccessful direct-acquisition stages. The companion JSON preserves both the raw acquisition results and the separate actual-reading record. These access failures do not erase the web-readable material, and failed downloads are not counted as read courses.
