# p_flow source-selection and reconciliation audit

Date: 2026-10-02. The student explicitly approved p_types and authorized this chapter. Archived Iranian entrance-exam documents were not read, classified, mined, or reproduced.

## Search boundary and candidate evaluation

Eight identifiable written offerings were considered from eight universities. Selection means best complementary fit within this accessible pool, not verified global optimality. Criteria in descending priority: substantive accessible written teaching; control-flow coverage; checkable semantic assumptions; proof depth; instructional exercises; contribution beyond already selected sources. Four core courses plus one supplement were actually read in scope. No video was needed or watched.

| Offering | Actual inspection | Decision and limitation |
|---|---|---|
| Harvard CS50x 2025, David J. Malan | Lecture 1 Conditionals, compare.c, agree.c, Loops/meow.c, input validation and Mario code read in downloaded text and official web body | Core: most direct C entry route. Extends examples with explicit checkpoint counts, safe bounds and separate input-termination assumptions. Its signed-overflow shorthand does not override C semantics. |
| MIT 6.0001 Fall 2016, Ana Bell / Eric Grimson / John Guttag | Lecture 2 PDF downloaded; all 24 pages extracted; pages 7–23 read, including indentation, range, break and comparison of loop forms | Core: iterator-versus-three-clause distinction. The slide's 'stop - 1' simplification is limited to step one; general range excludes stop without requiring that last visited value. Claims about rewriting while to for are language-context-specific. |
| Princeton COS126 resource family, Robert Sedgewick / Kevin Wayne | §1.3 instructional body, other control constructs and complete exercise inventory inspected | Core: tracing and numerical boundary patterns. Java boolean requirements, labeled jumps, overflow and definite-assignment diagnostics are not applied wholesale to C. Exercise inventory screened for this boundary, not every exercise solved or reproduced. |
| Cornell CS2110 Spring 2026, course teaching staff | Lecture 4 loop anatomy, range/diagram conventions, frequency invariant construction, initialization/guard/body derivation and recap read. Argmin and later exercise inventory inspected for boundary placement | Core: precise checkpoint proof construction. Array implementation exercises stay in their later chapters. Generic for-to-while rewrite gains an explicit continue restriction. Individual authorship not inferred from an inaccessible staff URL. |
| Cambridge Programming in C 2017–18, Neel Krishnaswami | Official offering metadata; Lecture 1 23-page PDF web body, specifically pages 14–18 and 20–23 read | Supplement: scoped names, comma-loop exercise and goto exception. Old implicit-int example not presented as valid C17. Original char-loop exercise repaired to initialized bounded int variables to isolate control semantics. |
| Stanford CS106A Summer 2021, Lecture 2 Control Flow | Official written body examined for test/body sequence, zero-entry case, state sketches and robot-loop patterns | Reserve: strong visual entry pedagogy, limited additional C dispatch/machine/proof coverage. Not counted among five selected courses. Robot exercise app links not treated as read written solutions. |
| Berkeley CS61C, C Syntax | Entire short §1.5 Control Flow inspected, related reference syntax read | Reserve: confirms do/switch/goto reference but too short to serve as a substantive fourth core chapter text; does not add invariant depth. |
| CMU 15-122 Spring 2024 | Official handout index and staff page inspected; index Contracts PDF returns 404 | Not selected; written body unavailable at linked address. No claim of review or inferred C0 semantics. |

## Evidence and fetch identity

Source downloads remain temporary under p_flow_sources and are not shipped in the Site or GitHub repository. This audit records content identity without redistributing full source material.

- Harvard notes HTML SHA256: 474b80b131768e19cc3736d452108edd6b70c45f3de47328eb602651726f2789.
- MIT Lecture 2 PDF SHA256: c65fb02d7a68f9bdbd9f715ff9f1a8eec61235510bb931ca5c2f039b2ea3adf9; 715048 bytes, 24 pages.
- Princeton §1.3 HTML SHA256: 65bbd77d8e5de8ad4d5f4ef641d09b59a18b814cdad724cb0e71219dd06a8d95.
- Cornell Lecture 4 HTML SHA256: cfcfc128fda39188817f1be612de2be86ccf2237c889dfc73de2f3f45343ce68.
- Stanford reserve HTML SHA256: 8398d41624b546e7cede1bf682c61d4263644d64ecbafeca01361e2947c316d3.
- Berkeley reserve HTML SHA256: 69f0990496745a688b433910cd6d6165e72c8c260a894bbc48d499d974d59211.
- Cambridge PDF read via official web-extracted 23-page text. No local fetch hash fabricated.
- WG14 N1570 public draft, independently cached in p_types_sources: SHA256 208969fec021e4f4ce87a1873765298c73e7bbb5209b1c5868967c7adfc8492e. Actual §§6.8.3–6.8.6 read from PDF-indexed pages 166–172 (one-based). Relevant expression and conversion clauses already audited in approved p_types.

Exact primary URLs and course identities are provided in p_flow-reviewed-courses.json and the English chapter's final references.

## Reconciliation and coverage matrix

| Boundary | Source contribution | Independent extension / correction | Worked problems |
|---|---|---|---|
| Statements and blocks | Harvard / Cambridge | Null-statement tree, local object identity, definition before reads | 4, 11, 20 |
| Conditional selection | Harvard / MIT / Princeton | Domain partition, residual path facts, chained-comparison error | 1–7 |
| Dispatch and fallthrough | Cambridge / Princeton; Berkeley reserve consulted | Converted case uniqueness, C17 constant expressions, switch-continue target, skipped initializer | 8–11 |
| While/do/for order | All four core bodies | Guard/input/output checkpoints, break/update counts, exact failed-test side effects | 12–17 |
| Nesting and transfers | MIT / Princeton / Cambridge | Separate nearest targets for switch and loop, ordinary-entry exception, labels and VLA restrictions | 10, 18–20, 35 |
| Invariants | Cornell | Scalar accumulators, partial/total distinction, meaningful checkpoint, continue and break proof edges | 23–26, 36 |
| Exact counts | Princeton / MIT | Closed-form progression derivation and independent exact checks; statement counts distinct from entries | 19, 21–22 |
| Termination boundary | Princeton numerical examples / Cambridge semantic caution | Signed UB, unsigned congruences, rounding stagnation, optimizer and environmental limits | 27–32 |
| Cross-language control | MIT / Princeton / Cambridge | Range binding distinct from C index mutation, comma guard semantics | 33–34 |

### Normative checks

- Scalar conditions and nearest else: N1570 §6.8.4.1.
- Integer switch, promoted controlling type and converted unique constants: §6.8.4.2.
- Nonconstant nonobservable loop termination permission: §6.8.5p6; constant omitted guard distinguished.
- While/do/for ordering and for-scope: §§6.8.5.1–6.8.5.3.
- Goto scope/entry, continue, break and return: §§6.8.6.1–6.8.6.4.
- Statement after a label / null statement: §§6.8.1 and 6.8.3.
- Logical and conditional/comma sequencing: §§6.5.13–6.5.17; unsequenced scalar conflicts §6.5p2.

The standards draft is additional normative evidence, not a sixth university course. The chapter is an original synthesis; source-dependent descriptions and exercise-family attributions are brief, and no entire copyrighted course/problem inventory is copied. General technical explanations and independently constructed problems supply the depth.

## Remaining limits

The pool is bounded and not globally exhaustive. Selected course bodies were read in chapter scope, not every lecture of every semester. This chapter deliberately excludes array partition/sort/merge implementations, full numerical solvers, pointer lifetime, complete I/O parsing and concurrent control. Course-exercise families are represented rather than universally reproduced. No archived Iranian paper used. Model checks do not prove all future exam answers, and a literal 100% perfection guarantee is not claimed.
