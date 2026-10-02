# Invariants and Recursive Reasoning: quality audit

Review date: 2026-10-02. Status: completed review draft; explicit student approval is required before promotion.

## Content and source review

The candidate comparison covers eight accessible university course candidates. MIT, Stanford, CMU, and Cambridge supply the four principal genuinely read courses; Cornell, Berkeley, and Princeton supply targeted supplementary checks. Oxford's syllabus is recorded as an unselected candidate, not as a reviewed instructional source. Exact reading scopes, source links, reconciled conventions, and selected exercise mappings are recorded in d_invariants-source-audit.md. Original PDF pages from all four principal courses were visually inspected. Princeton's original merge implementation slide was also inspected to check guard order and stable tie handling.

The main instruction develops transition semantics, least reachability closure, inductive versus reachable assertions, algebra of certificates, conservation and modular obstructions, loop contracts, ranking functions, recursive totality, structural induction, generalized accumulator specifications, mutual recursion, substitution, and finite-state certificates. Forty-nine worked problems explain complete solutions and failed arguments; eighty full-sentence examination rules organize assumptions, techniques, boundary cases, and common mistakes. The review section supplements the detailed lesson rather than replacing it.

The manual mathematical review reconciled exact halving counts with loose logarithmic bounds, data leaves with empty-child trees, partial correctness with body termination, existence of finite runs with uniform length bounds, safety with liveness, and ordinary Nim with misere terminal semantics. The generated-pair exercise includes direct unambiguous recursive rules with separate soundness, completeness, and unique-predecessor arguments.

## Independent checks

The manuscript's actual prefix-sum, power, and merge implementations were extracted and checked. The finite report records 781 prefix-sum inputs, 490 power inputs, 15,876 merge pairs, 10,000 halving inputs, 3,294 triple-rotation cases, 1,728 sliding-puzzle moves, 1,296 positions per Nim variant, 944 growth transitions, 294 bridge-policy transitions, 3,375 list triples, and 1,176 population transitions. These bounded checks supplement the written proofs; they do not prove all unbounded input cases.

The JavaScript laboratory was checked independently against transitive-closure reachability and topological-deletion termination oracles: 32,768 graph/initial-set/predicate cases and 32,768 ranking assignments. Counterexample paths and reachable-cycle witnesses were checked as actual graph walks. Invalid input types and ranks are rejected. Browser interaction checks cover all six presets, membership changes, self-loop transitions, and negative-rank validation.

## Rendering review

Local Edge rendering was checked at desktop width 1,280, mobile width 390, and print-media width 794. The mobile document has no horizontal page overflow and the displayed formula blocks fit. Four original SVG figures have no text outside their viewBoxes and no overlapping label rectangles. Screenshots of all four figures, mobile mathematical text, mobile laboratory controls, and the print-media layout were visually reviewed. A reset-arrow crossing its explanatory label was found visually and corrected before the final capture.

All mathematical elements, inline symbols, subscripts, and superscripts use the loaded local STIX Two Math font. Code uses JetBrains Mono; prose uses Source Sans 3 and headings use Newsreader. Native MathML supplies summation and union limits. The chapter uses no underlined text. The screenshot evidence and artifact hashes are retained in d_invariants-evidence.

## Boundaries and remaining uncertainty

No archived Iranian MSc or PhD examination PDFs were opened or classified; their study remains deferred to the final month. Course exercise collections are not copied exhaustively: the chapter's source ledger explicitly identifies the selected problems and adaptations. Course comparison is bounded and does not establish that every course worldwide was evaluated or that these four are globally optimal. Print-media inspection is not a page-by-page audit of a separately exported PDF. No literal zero-error guarantee, exhaustive examination coverage claim, or guarantee of success on every unseen problem is made. Further student questions and discovered errors should trigger a documented revision of this same chapter.
