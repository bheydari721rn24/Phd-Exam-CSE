# Stacks, Queues, and Applications: completed draft audit

## Delivery and approval

This English chapter is a complete review draft. It is not student-approved. Only this chapter was authored after the user approved the previous 35-chapter visual revision. No subsequent chapter is authorized until explicit approval of this draft.

## Teaching and source coverage

The 22-section chapter develops abstract contracts, legal histories, fixed and shared array stacks, linked queues/deques, two ring conventions, logical-order resizing, shrinking potentials, two-stack amortization, queue-based stacks, restoration and copying, greedy stack permutations, the 312 obstruction, Catalan/ballot counting, bracket types, expression evaluation/conversion, extrema/monoid augmentation, next-greater stacks, histogram widths, window deques, worklist boundaries, and Josephus recurrence. Procedures are accompanied by their invariants, proof arguments, numerical examples and boundary cases; the 80 complete retrieval rules follow the full instruction rather than replacing it.

Four primary written courses at Princeton, Oxford, Carnegie Mellon and Stanford were genuinely reviewed. MIT and Berkeley add focused complementary checks; Cornell is a screened candidate rather than a falsely counted newly reviewed anchor. The source-selection audit records exact scopes and the bounded seven-university comparison. The reading ledger separates download status, actual reading, previously reviewed material and independent extensions. It does not claim exhaustive access to every course worldwide.

## Problem bank and original examination evidence

There are 84 complete worked questions: three visually checked original MSc/PhD items and 81 original or independently reconstructed course problems. Original items retain booklet, original question number, PDF page, repository commit, PDF hash, options and independent answer provenance. No official answer key is asserted. Diagram inputs match stated data or explicitly identify a separate concrete teaching example. Solutions explain arithmetic, representation, reasoning, failure conditions and why an attractive alternative fails. Difficulty labels are provisional and not calibrated by student response statistics.

The bank covers formula derivations, prefix legality, exact primitive counts, potential calculations, memory footprints, capacity-limited counting, operand order, tie handling, counterexamples, boundary cases and proof obligations. It includes the six inspected CMU exercise themes through independent reconstructions; it is not a republication of every exercise on every course website.

## Independent mathematical verification

The machine-readable report is `a_stackqueue-verification.json`. Tests compare against independently simpler specifications:

- 5,913 permutations through size seven: greedy attainability, 312 avoidance and minimum capacity versus independently enumerated legal histories.
- 35 bounded Catalan cases against legal-history enumeration; reflection/first-return reasoning appears in the lesson.
- 656 legal ring histories across every front offset for capacities one through five.
- 2,184 strict/non-strict next-greater cases, including duplicates.
- 1,092 histogram inputs against all-interval brute-force area calculation.
- 6,015 sliding-window cases against direct window maxima.
- 480 Josephus simulations against the independent survivor recurrence.
- 120 auxiliary-stack sorting permutations; 13 recursive-restoration and 26 iterative restoration/copy cases.
- 180 two-stack histories against FIFO order and the exact primitive-cost formula.
- All 67 published model results independently recomputed from their stated inputs.
- All 35 approved chapter HTML hashes match the pre-work retention baseline.

These finite checks supplement general proofs. They establish the listed cases and implementation behavior; they do not prove literal scientific certainty or guaranteed answers to all future exam questions.

## Visual and interaction verification

The Chromium browser report is `a_stackqueue-browser-audit.json`. All 678 checkpoints of 67 models were rendered after fonts loaded. The audit found no failed inside-label padding, outside-label clearance, canvas-boundary or declared arrow-endpoint checks. Twenty-five models are in the lesson and 42 in relevant problem solutions. The lesson uses physical rings, indexed storage, real linked next/previous arrows, stack orientation and transfers, lattice counts, histogram rectangles and application-specific candidate states. It does not substitute a generic simulation for every topic.

Five editable laboratories independently recompute circular queues, two-stack queues including front observation, rational postfix expressions, stack permutations and sliding-window maxima. Sixty-six cross-language fixtures agreed with the independently checked Python results. Real form submissions exercised all five modes; division-by-zero rejection retained the preceding valid model. Previous/next/reset, seek, play/pause, keyboard navigation, real element motion, reduced motion and print checkpoint generation were checked.

Source Sans 3, Newsreader, STIX Two Math and JetBrains Mono were loaded and verified. Formulas use native MathML and preserve mathematical scope. Wide equations and diagrams have their own horizontal scrolling; the 390-pixel mobile document does not overflow. A textual current-state view supports narrow-screen reading. Long code lines remain available inside their code scroller. Printing exposes complete solutions and all model checkpoints; no exported PDF was generated or certified.

## Scientific scope and remaining limits

The implementations assume sequential exclusive access and their stated payload/allocation model. Exact rational laboratory input has an explicit digit limit. Priority queues, comprehensive graph algorithms, concurrent lock-free representations, fully persistent real-time queues, advanced parser grammars and full language ownership implementations remain separate topics. Source inconsistencies were identified and resolved explicitly. Original examination reading is targeted, not an exhaustive archive census. The chapter remains a draft pending the student's explicit review.
