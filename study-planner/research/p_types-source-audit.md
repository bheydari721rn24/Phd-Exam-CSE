# p_types source-selection and reconciliation audit

Reviewed 2026-10-02. Current chapter only; no archived Iranian examinations read. The student explicitly approved l_matrices before work began.

## Bounded discovery pool and actual selection

The pool has seven identifiable offerings from six universities. It is not an exhaustive inventory of all courses in the world, and “selected” means best fit among this documented accessible pool. Criteria, in order: accessible substantive written material; scalar-type/expression coverage; explicit semantics and checkable assumptions; complementary pedagogy; useful exercise reasoning. Institutional reputation is not a substitute for scientific verification.

| Offering | Evidence and actual read depth | Selection rationale |
|---|---|---|
| Stanford CS107 Winter 2020 | Official course index; PDF slide title verifies Jerry Cain/Lisa Yan. Relevant PDF slides 78–101, 109–115 read; earlier representation context inspected. | Core. Strong signedness/conversion cases, but course-machine shorthand needs normative correction. |
| Harvard CS50x 2025 | Official Lecture 1 Types/Operators/Variables, logical examples, More About Operators and Truncation read. | Core. Foundational entry route; signed range/overflow errors corrected rather than reproduced. |
| Berkeley CS61C | C Variables entire instructional body and C Syntax aliases, macros, constants/enums read. | Core. Portability and storage reasoning; identifiable erroneous/version-sensitive claims recorded below. |
| Princeton COS126 resource family | Fall 2017 lecture index inspected; §1.2 teaching body and entire exercise inventory read. | Core. Values/operators distinction and expression-translation patterns. Java semantics remain explicitly distinct. |
| MIT 6.0001 Fall 2016 | Official offering/instructors verified; cached web PDF text, slides 23–34, and all three Lecture 1 written questions read. | Supplement. Improves cross-language binding/division explanations beyond the four core courses. |
| CMU 15-122 Fall 2014 | Official index inspected; instructors Robert Simmons/Tom Cortina verified. Lecture 03-ints.pdf index initially returned metadata, but subsequent body access failed 403 and local download failed. | Not selected or counted as reviewed. C0 is also a different arithmetic contract; unread material cannot be claimed as a scientific foundation. |
| CMU 15-213 Fall 2004 | Official class03.pdf index returned lecture metadata; local written-body retrieval refused. | Reserve only, not counted as reviewed. Adds representation-heavy depth mostly belonging to p_rep; access failure prevents an honest full evaluation. |

Precisely five course bodies from five universities were actually read for the chapter. The two failed CMU candidates are not silently relabelled as reviewed. The four core bodies are Stanford, Harvard, Berkeley, Princeton; MIT is an additional source used where it adds a distinct perspective. Source identities and exact URLs are in p_types-reviewed-courses.json and the chapter references.

## Fetch evidence

Full source files stay in the local temporary p_types_sources cache, outside the repository and deploy archive. Source text is not redistributed. The saved fetch SHA256 values are:

- Stanford PDF: aaafdc1e460ceea56d09f0de3961b0bf380ec87a37b72806e23e67e0fb249946.
- Harvard HTML: 474b80b131768e19cc3736d452108edd6b70c45f3de47328eb602651726f2789.
- Berkeley C Variables HTML: 3faba95d88adfc93a51ff93b1d65e4e42cc4f0df649aee4b24fac6a2f445391e.
- Berkeley C Syntax HTML: 69f0990496745a688b433910cd6d6165e72c8c260a894bbc48d499d974d59211.
- Princeton HTML: 045d2874c12dcdfbecb7e5c5805a2f5b2face149f80a0aefd7b4cab2803e65cd.
- WG14 N1570 PDF: 208969fec021e4f4ce87a1873765298c73e7bbb5209b1c5868967c7adfc8492e.
- MIT was read through web-cached official PDF text and official question text; no local hash is invented for its failed download.

## Source corrections and independent rules

| Source shorthand or error | Reconciled chapter rule | Normative cross-check |
|---|---|---|
| Harvard describes 4294967295 as a possible int maximum in its ordinary signed example and implies wrapping | The declared 32-bit signed model has maximum 2147483647; out-of-range signed arithmetic is undefined | N1570 5.2.4.2.1, 6.5p5 |
| Berkeley's quiz answer says int need only be eight bits and always two's complement | C17 minimum signed range includes -32767..32767; signed representation choices distinguished from the declared two's-complement model | 5.2.4.2.1, 6.2.6.2 |
| Berkeley calls uninitialized values garbage | Automatic indeterminate scalars and static zero initialization distinguished; no invented output | 6.3.2.1, 6.7.9 |
| Berkeley treats sizeof as always compile-time; Stanford uses a long-like signature | size_t result, non-VLA unevaluated operands, VLA exception | 6.5.3.4 |
| Stanford says casts leave bytes unchanged | Value conversions distinguished from representation reinterpretation; no general unchanged-bits claim | 6.3.1.3–6.3.1.5 |
| Stanford simplifies mixed signed/unsigned as unsigned wins or larger width wins | Full rank/signedness/range decision tree; LP64 versus LLP64 counterexample | 6.3.1.8 |
| Stanford describes signed narrowing through truncation as general C | Representable signed preservation; otherwise implementation-defined result/signal in C17 | 6.3.1.3 |
| Stanford says a format placeholder dictates output independent of expression type | Variadic promotions and type-compatible printf formats; mismatches classified as undefined | 6.5.2.2, 7.21.6.1 |
| Berkeley table describes Python 2-style int/long split | Explicit Python 3 comparison, arbitrary-precision int subject to resources | MIT course explicitly uses Python 3.5; official written lecture |
| Berkeley macro explanation says side effect occurs twice without a branch qualification | Condition plus selected branch determines repetition; unselected branch not evaluated; unsequenced conflicts checked separately | 6.5p2, 6.5.15 |
| Princeton overflow/division/Boolean rules are Java-specific | C17 signed overflow, zero division, and scalar truth distinguished rather than imported | 6.3.1.2, 6.5.5; labelled Java course comparison |

Relevant normative pages actually extracted/read include PDF pages 68–71, 82, 94, 103, 106–110, 112–120, with initialization/limits and formatted-output clause text consulted by heading. N1570 is labelled as a public C11 draft for stable relevant C17 rules, not the published C17 standard. No C23 semantic substitution was made.

## Boundary and reasoning-pattern mapping

| In-scope pattern | Main instruction | Worked problems |
|---|---|---|
| Values/assignment/lvalues/initialization | Values and assignment | 1–2, 33; invalid lvalue and uninitialized examples in body |
| Scalar types, width, literals, character codes, sizeof | Types and literals | 3–5 |
| Promotions, unsigned residues, mixed ranks, conditional common type | Conversion pipeline | 6–11, 17, 32 |
| Cast timing, signed quotient/remainder, ceiling and modulo proofs | Conversions and arithmetic | 12–16 |
| Intermediate overflow, guards, minimum-value exceptions | Safety | 16–19, 36 |
| Parsing, logical/bitwise differences, shifts | Operators | 20–24, 34 |
| Full-expression sequencing, increment, comma, macro repeat | Sequencing | 25–27 |
| Binary rational termination, conversion precision, nonassociativity, tolerance | Floating | 28–30, 35 |
| Variadic output-type matching | Output | 31 |
| Language distinction and assignment snapshots | Comparisons | 10, 13, 16, 21, 33 |

## Exercise inventory and honest limits

- Stanford: mixed-type comparison, range, narrowing, and extension patterns read. Problems 8–11/19 cover the semantic patterns; representation-circle and binary-encoding tasks are deferred to p_rep. Every original slide question is not reproduced.
- Harvard: calculator, truncation, finite-range doubling, and logical conditions were read and mapped to Problems 12/16/18/24. Mario/loops/functions are outside this boundary and deferred to their scheduled chapters.
- Berkeley: int-portability quiz, initialization output fragment, macro expansion, aliases/constants were read; erroneous answers were corrected. Problems 5/6/17/27 and teaching counterexamples cover the patterns. Struct/pointer/control-flow applications remain deferred.
- MIT Lecture 1: all three written questions are accounted for in Problems 1 and 33, with independent numbers and prose. No video solution was needed to derive the answers.
- Princeton §1.2: the entire displayed exercise list was inspected. Assignment/swap, truth normalization, integer division/cast timing, expression grouping, chained comparisons, intermediate overflow, numeric formula translation, invalid numeric/string operands, initialization, and floating comparison patterns are represented. Repeated application wrappers, whole input programs, random games, string concatenation, Fibonacci/dragon curves, coordinate transforms, polynomial/loan applications, and library-function projects are not reproduced in full. Those require later chapters or duplicate expression patterns. The chapter explicitly reports a reasoning-pattern bank, not all literal course questions.

All teaching prose and solutions are original explanatory synthesis of facts and independently checked examples, not lecture transcription. No source lecture image is copied; diagrams are original SVG. Course patterns are attributed precisely and not passed off as historical entrance-exam questions. Absolute global source exhaustiveness, literal perfection, or performance on unseen exams is not claimed.
