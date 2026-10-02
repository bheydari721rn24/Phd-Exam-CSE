# Boolean algebra: bounded source selection and actual reading audit

Date: 2026-10-02. Chapter: g_boolean. Research scope is Boolean algebra and truth tables, with algebraic verification extensions. No Iranian examination archive was read or mined. Synced sources remain read-only.

## Selection rule

Evaluate public written offerings for (1) binary definitions and specification precision, (2) derivations rather than asserted recipes, (3) cofactor and advanced verification depth, (4) accessible readable text, and (5) complementary problem patterns. Familiar university names are not sufficient evidence. A year is taken from the offering or document, not a search crawl date. This bounded eight-university pool is not a worldwide exhaustive survey or a ranking of all universities. Four complementary core courses were chosen; two additional course bodies were genuinely read to cross-check the core. The inaccessible candidates are not counted toward the minimum.

| Priority / role | Candidate | Actual reading | Decision |
|---|---|---|---|
| Foundation core | MIT 6.004, Chris Terman, Spring 2017 | C4 annotated teaching body: specification, SOP building blocks, associativity, De Morgan, reduction, input freedom, nonminimal SOP caveat. Gate and map sections screened to keep the chapter boundary. | Best accessible continuous narrative in this pool for specification-to-expression reasoning. Some algebra is in image slides; independent definitions and proofs supply the chapter's law table. |
| Algebra core | Cambridge Digital Electronics, Ian Wassell, 2020–21 | comb_log_bool_20.pdf, all 14 PDF pages; algebraic core pp. 8–12. Examples pp. 1–2 screened and read in scope. Page 9 visually inspected; original overbar placement matters. | Compact systematic law coverage and nested-algebra examples; expanded independently into deeper prose. |
| Verification core | Stanford EE108A, William J. Dally and Philip Levis, Winter 2008 | Lecture 1 PDF pp. 8–16; p.14 visually inspected. Other lecture pages screened but not counted as Boolean chapter coverage. | Precise memoryless/acyclic model and majority verification; useful correction opportunity in axiom labels. |
| Advanced core | CMU 18-760, Rob A. Rutenbar, Fall 2001 | Lecture 1 PDF pp.4–24 and 30–39 (printed slide numbers differ from PDF page numbers). Homework 1 items1–5, PDF pp.1–3, actually read. Network-repair and state-machine problems screened but excluded from this chapter. | Strongest advanced cofactor, difference, quantification and recursive-verification material in the inspected pool. Corrected qualifications and notation; not reproduced verbatim. |
| Additional cross-check | Berkeley CS61C, John Wawrzynek with edits by Lisa Yan | Boolean Algebra and Canonical Form, CL Design, full written teaching bodies at the canonical URLs in References. | Definitions, majority derivation and equality comparison corroborate the core. Material linked; prose/artwork not copied. |
| Additional cross-check | Cornell CS3410, Adrian Sampson and Giulia Guidi, Fall 2024 | Gates & Logic: Truth Tables, Logic Notation, universal construction and XNOR/selector exercise prompts. Arithmetic sections only screened for boundaries. | Clear construction from a specification and distinction between scalar logic and bitwise notation. |
| Screened, not selected | UCSD CSE140, Spring 2022 | Official syllabus and linked 60-page lec2Boolean.pdf located with browser; local HTTPS retrieval timed out twice. The lecture includes axioms, consensus, Shannon and normal forms, but no complete local reading occurred. | Strong topical match, but not counted as genuinely read. It cannot replace a completed core review in this delivery. |
| Unverified candidate | ETH Zurich Digital Logic Design catalogue lookup | Catalogue request returned HTML, but the candidate's course identity/materials were not established from the retrieved body. | Do not present a catalogue lookup as a read university course or a verified offering. |

## Resource integrity

The copied manifest `g_boolean-source-manifest.json` records actual request URLs, byte counts, SHA-256 hashes, local cache locations and failures. Original external PDFs/HTML remain in a temporary research cache; copyrighted course files are not republished in the GitHub mirror or Site. A successful HTTP 200 alone does not establish a lecture download: the Berkeley historical handout URL and one initial wrong content URL returned the HTML course landing page, so both were excluded as content evidence. The substantive Berkeley reading used the two correct teaching URLs.

Local Poppler omitted some formula glyphs in old PDFs because of unavailable substitute fonts. Cambridge p.9 and Stanford p.14 were visually legible and inspected; CMU extracted formulas were checked against the primary browser extraction and independently rederived, not blindly inferred from empty image regions. The audit does not claim all original PDF pages were visually reviewed. HTML extraction showed some UTF-8 punctuation mojibake in MIT annotations, but the literal equations and surrounding teaching content were readable; final prose is independently written English.

## Corrections and qualifications applied

1. CMU PDF p.6 (slide12) repeats positive-x cofactor indices in the displayed expansion of the zero-x branch. Correct branch indices must retain x=0. The independently proved four-branch expansion and Problem26 preserve that distinction.
2. CMU PDF p.10 (slide20) says a function only of x has difference one. This requires a nonconstant unary function; constants have difference zero. The chapter states the exact essential-support condition.
3. CMU PDF p.33 (slide66) treats opposite literal polarities in one example cover as evidence of semantic binateness, though its x terms can absorb to a function independent of x. The chapter separates syntactic cover unateness from semantic cofactor containment; Problem32 explicitly exercises the counterexample pattern.
4. Stanford PDF p.14 labels domination identities as Identity and neutral-element identities as Idempotence. The chapter uses definition-based labels and does not present that abbreviated slide as an independently sufficient axiom set.
5. The Berkeley finite expression/circuit correspondence is used for representability, not interpreted as a global one-to-one correspondence of all circuit structures and functions. Distinct expressions can share a truth table.
6. Source statements about fewer gates or faster circuitry are model-dependent. The chapter does not infer delay from literal count or claim functional simplification removes physical hazards.

## Coverage matrix and independent contributions

| Topic | Core correspondence | Chapter evidence |
|---|---|---|
| Domain, operator meanings, specification completeness | MIT / Cambridge / Stanford / Cornell | Sections2–3; Problems1–5; explicit two-valued model. |
| Laws, duality, complement scope, algebraic proof | Cambridge / Stanford / Berkeley / MIT | Sections4–6; general proofs and Problems6–16. |
| XOR, parity and disjointness | Cambridge / Cornell / MIT; independent ring extension | Section7, Problems17–21; ANF reconstruction independently checked for every four-input truth table. |
| Full row representation and cube coverage | MIT / Berkeley / Cornell / CMU | Section8; Problems22–23; canonical indexing and minimization expressly assigned to later g_kmap. |
| Restriction, Shannon SOP/POS, essential support | CMU, independently cross-linked with MIT selector model | Section9; Problems24–27,38–39; proof on both input slices. |
| Difference, quantified bounds, unateness | CMU | Section10; corrected semantics and Problems28–33,36. |
| Equivalence, care sets, recursive proof | MIT care discussion / CMU recursive methods / Stanford verification | Section11; Problems34–37,40; complete finite miter and explicit counterexamples. |

Self-duality counts, ANF subset inversion, mixed-quantifier example, multi-output error aggregation and additional model-boundary derivations are independently authored extensions, not claims that every source covered them. Sections cite the reviewed source pool at the start and exact reading locations at the end. Source-specific question patterns are represented with independent wording and complete solutions; an entire copyrighted exercise collection is neither copied nor claimed to be included.

## Remaining limits

At least four courses from four universities were genuinely reviewed for this chapter; six contributed. The pool is bounded. Universal 100% accuracy, coverage of every conceivable topic and guaranteed answers to unseen exams are not asserted. Scope coverage is reviewed against the explicit matrix above. Advanced physical gate design, detailed canonical/minimization methods, and timing are subsequent chapters. User approval is required to promote this draft and to start another chapter.
