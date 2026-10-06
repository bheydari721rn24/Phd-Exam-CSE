# Comparison and Non-comparison Sorting — delivery audit

## Delivery state

Complete English **review draft**, dated 2026-10-06. The preceding Stacks, Queues, and Applications chapter was explicitly approved by the user. This draft requires its own approval before promotion and before another chapter is started.

## Teaching and problem coverage

The chapter contains 22 sections covering record contracts and strict weak orders; stable and unstable sorting; comparisons, movements, inversions and storage; selection, insertion, bubble and Shell sorting; stable merging, exact merge counts, reusable allocation, structured runs and displaced inputs; distinct partition contracts; randomized quicksort's pair-indicator proof; duplicates and sample-pivot bounds; Floyd heapsort and its height-sum proof; comparison decision trees; counting and stable scatter; signed radix encodings, exact digit counts and word-versus-bit models; bucket second moments and string prefix handling; introspective hybrids and external merge transfers. Selection/order-statistic algorithms and a full priority-queue interface have separate scheduled chapters.

There are **88 complete worked questions**: two checked adaptations of original Iranian booklets and 86 original or independently reconstructed course problems. These emphasize numerical counts, formula derivations, counterexamples, boundary contracts and medium/hard conceptual transfer. The final **80 examination rules** give complete statements, their assumptions and common traps. A dedicated summary explains a repeatable solution method.

## Sources and provenance

The documented pool contains five university courses and twelve PDF documents. Four core courses are selected from MIT, Princeton, Carnegie Mellon and Oxford, with Stanford as a fifth mathematical complement. The source audit records the exact inspected page ranges, strengths, limits and reconciliation decisions. Whole courses, all world courses, and unrelated PDF chapters have not been represented as read.

The two authentic questions identify repository commit, original path, PDF page, question number and source SHA256. Original full pages were visually checked. No official answer key was available; the answers are independently derived. PhD CE 1405 Q16 has answer 16 in original option **1**. Its earlier option ordering and machine-readable answer index were repaired in the three existing chapter occurrences, with explicit before/after hashes. All other question records retain their previous semantic content.

## Mathematical and computational checks

`a_sort-mathematical-audit.json` records **15,641 finite checks**. These exhaustively cover distinct permutations through length six and three-value multisets through length five; compare outputs with independent sorted orders; check insertion's inversion/prefix-minimum formulas, selection's triangular count, bubble's inversion swaps, merge bounds, all-equal quicksort variants, Floyd construction, signed radix digit lengths and the authentic merge count. All saved computational models match their specified algorithm executions. SVG and MathML are parsed as XML. Finite checks supplement the written proofs; they do not establish correctness for every conceivable program input.

The prior 36 chapter files still contain **2,169 problems**. Thirty-three retain their original byte hashes. The remaining three have only the documented Q16 option/answer correction. The new draft adds 88 questions without removing any prior questions.

## Visual and interaction checks

There are **45 distinct recorded models**: 17 lesson models and 28 problem models. They contain 887 stored checkpoints. The exact authentic merge model is intentionally shown both in the lesson and its question, so the browser sweep checks **927 displayed recorded states**. Array holes and saved keys, merge head consumption and transfers, partition regions, actual heap trees, cumulative-end counters, digit/bucket distributions and a six-leaf decision tree have different semantic layouts.

Ten editable laboratory algorithms expose validated integer inputs. **54 fixtures** compare the browser's separately written JavaScript implementations with the specified Python traces, including key order, original identities, exact counters and relevant structural results. All ten real form modes were submitted. Invalid bucket input retains the last valid trace and displays a clear error.

The real Edge browser sweep found no text outside SVG bounds or insufficient internal label clearance across the 927 recorded states. Controls, seeking, keyboard end navigation, actual record motion, pause/resume, reduced motion, full checkpoint printing, MathML rendering and local font loading were checked. At a 390-pixel viewport the document width remains 390 pixels; diagrams and long formulas use local horizontal scrolling. Screenshots of insertion, merge, Hoare partition, three-way partition, heap, counting, radix, decision tree, worked merge, formulas and notes were inspected. Source Sans 3, Newsreader, STIX Two Math and JetBrains Mono load locally. Mathematical notation uses native MathML; code retains its separate monospace face.

## Remaining uncertainty

Course and examination provenance is explicit, and proof assumptions are stated. Literal 100% perfection, exhaustive coverage of every research sorting method, or a guarantee of answering every unseen examination question cannot be certified. All answers and exact counts must be interpreted under their written code and cost conventions. This is a substantive chapter ready for the user's review, with publication tracked separately from content verification.
