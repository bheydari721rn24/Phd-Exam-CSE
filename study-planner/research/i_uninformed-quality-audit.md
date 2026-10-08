# Uninformed search: mathematical, teaching and visual audit

Review date: 8 October 2026. Status: complete review draft, awaiting explicit student approval. This report describes inspected evidence and its limits; it does not claim universal error-free coverage or guarantee a future examination score.

## Instruction and source coverage

The chapter has 31 sections. It develops state/node distinctions, event accounting, BFS layer invariants, graph and tree DFS, depth-limited three-outcome semantics, depth-sensitive duplicate pruning, IDS correctness and exact repeated-work counts, UCS relaxation and its frontier-cut proof, an executable Python implementation, infinite-space completeness conditions, graph/heap complexity, negative-cost counterexamples, cost transformations, bidirectional stopping conditions, sufficient state keys and application modelling. The source audit documents four core written courses from four universities and a fifth supplementary Stanford course, with a bounded comparison pool and explicit exclusions.

The full problem bank contains 80 original or independently reconstructed problems and one checked English adaptation of MSc CE 1404 Question 68. The original PDF page 16 was visually inspected, and its SHA-256 and pinned archive commit are recorded. Option 4 is independently derived under the classical tree-search assumptions; an official key is not claimed. No unverified PhD question is labelled authentic. Complete copyrighted university problem sets are not reproduced.

The 80 final rules use complete conditional sentences and retain exceptions. The bank covers exact queue/stack/heap traces, geometric and weighted sums, root and boundary conventions, counterexamples, proof obligations, memory budgets, state augmentation, joint-state counting, resource dominance, stopping certificates and implementation repairs. Foundational boundary checks are identified alongside medium–hard synthesis; not every question is labelled difficult.

## Mathematical and implementation checks

`i_uninformed-evidence/mathematics.json` records 6,487 checks. Five search algorithms were independently compared on 360 seeded finite directed graphs, for 1,800 runs. A separate Python Bellman–Ford computation supplies optimal costs; an independent FIFO traversal supplies minimum depths and reachability. Returned paths are checked against actual directed edges. BFS and IDS depths, UCS costs, and DFS/DLS reachability match the applicable independent results.

Exact finite-sum identities were checked for branching factors 1–11 and depths 0–9, with a separate unary formula. Important values include 57 versus 31 visits for binary depth-four IDS, 123456 versus 111111 at branching ten and depth five, 29 generated nodes in the binary goal-on-removal example, and 161243136 bytes for the specified BFS layer. Targeted checks cover lazy stale-entry removal, zero-cost relaxation, the shallow/deep duplicate trap, boundary cutoff, IDS resetting, and a costly first DLS route.

All 523 static MathML instances were parsed and checked for complete delimiters and closing-fence script errors. Browser checks also cover the dynamically inserted mathematical state panels. Formulas use STIX Two Math; Source Sans 3, Newsreader and JetBrains Mono are loaded for prose, headings and code. The English-only and no-underline checks passed.

The core UCS explanation was corrected during review: rejecting every already discovered state returns cost 9 in the example, while a different hybrid rejection policy can return 6. The logical selected counter excludes stale removals consistently with the laboratory. Generated, accepted, selected, expanded and raw removed events are distinct.

## Visual and interaction checks

There are 25 specialized models with 251 stored checkpoints. Search graph models display actual execution events, path records, ordered priority candidates, frontier contents, best-cost labels and counters. Counting models use exact finite sums; infinite-chain models show finite prefixes and explicitly refer to the proof for the infinite conclusion. Bidirectional layers are labelled an ideal growth illustration, not a weighted bidirectional implementation. The grid model moves along a legal route without covering coordinate labels. Diagrams attached to solved problems use the corresponding graph or an explicitly stated numerical specialization.

`i_uninformed-evidence/browser.json` records inspection of all 251 unique stored frames for text overlap, plot bounds and box padding. Eight representative model screenshots plus title, final rule, synthesis problem, mobile, print and editable-lab views were captured. The graph, depth-budget, counting, title and corrected grid views were visually inspected. A layout issue in the automatic lab graph was fixed by assigning graph-distance layers instead of a fixed row-major layout.

Play/pause freezes a real geometry transition, resume advances it, and previous, seek and restart controls work. Reduced-motion preference suppresses interpolation. Print exposes stored checkpoints and complete solutions. Six valid edited graphs and six invalid inputs were exercised; invalid submissions preserve the last valid result. Mobile page overflow and runtime error checks passed. The finite laboratory accepts only bounded nonnegative integer costs; negative-edge failure is taught in a deliberately invalid counterexample instead of silently accepting it.

## Retention, delivery and approval

SHA-256 checks confirm all 44 preceding chapter HTML files remain byte-for-byte unchanged. Their 2,839 worked problems remain present. Adding this draft yields 45 chapter cards and 2,920 worked problems. The preceding intelligent-agents chapter was promoted only because of the student's explicit approval. Library and Week 3 links to this draft work in the browser.

Publication status is recorded separately in `i_uninformed-publication.json`. A local browser pass does not establish successful online deployment. The current chapter remains a draft until explicit approval; no subsequent chapter has been started.

## Remaining limits

The finite graph checks are strong implementation evidence, not a proof for arbitrary programs or all infinite spaces. Independent mathematical arguments state their assumptions in the lesson. No visual verification of inaccessible university source diagrams is claimed. The editable graph layout is intended for small teaching graphs, not arbitrary large networks. Informed search, adversarial games, and advanced planning are outside this chapter. Accessible candidate comparison does not certify that every university course worldwide has been read or that unseen examination performance is guaranteed.
