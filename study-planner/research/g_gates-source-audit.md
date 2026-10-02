# Logic gates: written-course selection and synthesis audit

Date: 2026-10-02. Topic: g_gates. Previous chapter g_boolean explicitly approved in this turn. Iranian entrance examination archives were not opened, mined or analyzed. No student test was requested.

## Search boundary

Eight-university pool: MIT, Cambridge, Stanford, UC San Diego, Berkeley, Carnegie Mellon, Cornell, ETH Zurich. Primary official pages and their written materials were sought for primitive gates, universality, CMOS construction, mapping, timing and hazards. Selection is chapter-specific and qualitative. It is neither an exhaustive worldwide course enumeration nor proof of globally optimal selection. Video links did not count as reviewed material.

## Candidate-by-candidate evaluation

| Candidate | Actual review | Strength for this chapter | Limitation | Decision |
| --- | --- | --- | --- | --- |
| MIT 6.004, Chris Terman, Spring 2017 | Chapter 3 annotated body: static discipline/noise margins, complementary switches and gates, inverting restriction, propagation/contamination contracts, path sums and lenience | Best integration of physical contracts and gate-level reasoning | Device microphysics intentionally not used in full; one-stage restrictions need topology assumptions | Core source for digital contract, CMOS predicates and timing bounds |
| Cambridge Digital Electronics, Ian Wassell, 2020–21 | Introduction; all nine pages of Multilevel Logic and Hazards; device slides pages 10–17; Examples Paper pages 1–3, screening questions 1–5 and 10 | Direct multilevel tradeoffs, glitch classification, consensus bridging, voter exercises | Extracted symbols/overbars degrade; dynamic hazard removal explicitly outside that course | Core source for hazards and implementation exercise types |
| Stanford EE108A, W. J. Dally reader, Winter 2008 distribution with Philip Levis | Pages 39–42, 58–65, 67–76, 79, 83–85, 100–101; exercise descriptions pages 45 and 66. PDF has 232 pages; unlisted pages were not represented as reviewed | Most detailed selected treatment of graph closure, bubbles, complementary topology and load | Historical simplified RC treatment, incomplete exercise placeholders, and some overly broad statements | Core source for netlists, CMOS, load and closure proof; numerical process figures not transplanted |
| UCSD CSE140, C. K. Cheng, Spring 2022 | Lecture 6 pages 1–25; Lecture 1 relevant gate/equation/cost slides pages 46–62 | Best explicit restricted-library questions, nonassociativity and mapping diagrams | Some claims are abbreviated; constants must be explicit | Core source for universality, gate-resource assumptions, mapping |
| Berkeley CS61C Course Notes | Entire Logic Gates teaching body read, including gate truth tables, universal subsets and n-input XOR. CL Design fetched but not used as a reviewed source for this chapter | Clear gate and parity semantics | Physical implementation intentionally outside the text | Fifth substantive cross-check, not one of the four core sources |
| CMU 18-322 Introduction to CMOS Circuits, Lecture 1 | Extracted 16-page introductory PDF read at screening level; title and model discussion inspected | MOS background and model tradeoff | Mostly transistor introduction; does not supply stronger mapping/timing coverage than chosen sources; course instructor not independently confirmed | Screened, not selected or counted among four |
| Cornell CS3410, 2024fa logic/switches notes | Official URLs sought, local requests timed out; prior chapter familiarity not treated as current reading | Likely clear digital abstraction bridge | No successful new full reading in this run | Not selected or counted |
| ETH Digital Circuits, Onur Mutlu, Spring 2017 candidate slides | Search surfaced official historical slide URL; direct fetch returned 404 | Potential foundational circuit coverage | Slide content not accessible at selected URL in this run | Access-limited; not selected or counted |

Within the usable pool, MIT and Stanford supply detailed contracts and physical reasoning; Cambridge supplies explicit hazards and UCSD supplies the strongest complementary restricted-library examples. Four were retained because removing any one loses a documented aspect. Berkeley adds an independent check of multi-input parity. No arbitrary numerical university ranking was used.

## Actual source corrections and qualifications

1. UCSD Lecture 6 page 6 calls XOR and AND universal; page 9 explicitly introduces constant one. The manuscript proves non-completeness without one and completeness with it. This is a substantive resource qualification, not silent copying.
2. UCSD page 3's broad inverting-output phrasing is restricted in the manuscript to one static complementary stage with uncomplemented controls. Buffered AND/OR cells, complemented controls and other technologies are not excluded.
3. UCSD binary XOR truth-table rows have an unusual x/y row order in the slide. The manuscript consistently uses lexicographic binary order, and generated tables were independently checked.
4. Stanford page 39 footnote reverses conventional DNF/CNF names. The manuscript uses SOP/POS without inheriting that nomenclature error.
5. Stanford page 65 explanatory prose swaps the direction of weak pass levels relative to its figure caption. The chapter uses the complementary pullup/pulldown predicate proof and does not transplant that inaccurate sentence.
6. Stanford page 101's broad claim that arbitrary circuits can be made hazard-free by redundant implicants is stated only for the two-level, single-changing-input static-hazard model. Multilevel dynamic and multiple-input functional hazards remain separate.
7. Cambridge device slides page 14 describes ideal zero steady-state power. Real leakage and short-circuit switching currents are explicitly acknowledged. Historical logic-family speed numbers are not treated as current product specifications.
8. MIT valid-level propagation/contamination contracts and Stanford midpoint/RC estimates are different definitions. The chapter teaches both with explicit limits and does not combine them as interchangeable measurements.

## Visual source review

Local Poppler renderings were inspected for UCSD Lecture 6 page 23 (NAND/NOR bubble transformations) and Cambridge hazards page 8 (overbar scope, select transition and output pulse). Although Poppler warned about substitution fonts, the rendered equations and gate connectivity on these pages were legible. Stanford schematic topology was cross-checked by the corresponding detailed text and independently derived conduction predicates; a claim of inspecting every Stanford figure is not made. Extracted formulas were never accepted solely because a PDF parser returned text.

## Topic-to-problem matrix

| In-scope reasoning pattern | Full teaching section | Fully solved support |
| --- | --- | --- |
| Thresholds, restoration, static contract | 2 | 24, 25, 28 |
| Primitive gates, constants, tied inputs | 3 | 1, 9 |
| Multi-input versus cascaded NAND/NOR | 3, 7 | 2, 17 |
| Parity, exactly-one and XNOR tree convention | 3 | 3, 4, 18 |
| Circuit equations, semantic support, graph proof | 4 | 5, 15, 20 |
| Bubble scope, branch preservation and active-low logic | 5 | 6, 7, 8 |
| Constructive universality and preserved invariants | 6 | 9, 10, 11, 12, 13 |
| NAND/NOR mapping, literal availability, fan-in limits | 7 | 14, 15, 16, 17, 18 |
| Cost, depth, sharing and minimum lower bounds | 7, 9 | 9, 14, 19, 20, 36 |
| CMOS dual networks, invalid topology, one-stage limits | 8 | 21, 22, 23 |
| Load, RC thresholds, energy distinctions | 9 | 18, 20, 25; energy derivation in main teaching |
| Late/early arrival, asymmetric edges, blocked paths | 10 | 26, 27, 28 |
| Static-one/static-zero/dynamic and functional hazards | 11 | 29, 30, 31; dynamic classification in main teaching |
| Transport and inertial assumptions | 10–12 | 29, 32 |
| Unknown/undriven states, fault excitation, HDL completeness | 2, 4, 10 | 33, 34, 35 |

The review section adds five connected summary paragraphs, 60 complete-sentence rules and an eight-step solution procedure. The 36-problem bank covers the declared chapter; it does not assert reproduction of every exercise from every university. Course-derived problems 11, 14, 15 and 29 identify exact source exercise types. All solutions, numbers, exposition and diagrams are independently written. Other reviewed exercise types informed the coverage selection, not copied question text.

## Provenance and unresolved limits

`g_gates-source-manifest.json` contains the official URLs, request outcomes and hashes of fetched files. Downloaded PDFs and full teaching HTML are stored in a temporary cache outside the repository and are not rehosted. Failed requests are preserved in the manifest instead of hidden. Core course texts are historical but their mathematical gate definitions are stable; no current hardware product recommendation relies on historical figures.

Unresolved boundaries: no global exhaustive course search, no unread inaccessible source counted, no university exercise collection completeness claim, no physical certification, no archived Iranian examination analysis, and no guarantee of all unseen questions. Later minimization, arithmetic and sequential topics remain intentionally outside g_gates.
