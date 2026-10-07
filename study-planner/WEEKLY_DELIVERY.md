# Chapter delivery contract

## Current instruction

The study plan and every study-facing chapter are written in clear, precise English. Study dates and hours describe the student's reading; they do not impose a chapter-production schedule. Work on one chapter at a time until it passes the source, mathematical, pedagogical, and presentation checks below. The active chapter and its status are recorded in `research/chapter-gate.json`.

The later explicit instruction to study the repository's Iranian master's and doctoral questions supersedes the earlier final-month deferral. Use those archives for faithful calibration and attribution alongside original questions; do not ask the student to answer test questions during the first reading.

## University-course selection

For each chapter, survey a broad pool of relevant written courses from leading universities. Record the candidate university, instructor, title, year, directly accessible lecture text or slides, exact chapter coverage, actual review level, strength, and limitation. Evaluate source quality for **that chapter**, not just the university brand. At least four distinct course texts from four universities must genuinely be read, compared, and synthesized. Four is a minimum; add further sources when they resolve a documented gap. A syllabus, promotional page, or video without usable text does not count toward the four.

It is impossible to prove that every course worldwide was found or that a selected set is globally best. The source register must state the search boundary and access limits honestly. Never describe a catalogue-only course as fully reviewed.

## Required chapter content

1. State the chapter boundary, prerequisites, exact university sources, and actual review level.
2. Teach concepts from basic definitions through advanced cases with precise semantics, derivations, proofs, formulas, counterexamples, and all identified in-scope exceptions.
3. Provide an instructional bank of original problems and source-attributed, independently worded course-derived exercise types, each with a fully explained solution. Select a sufficient range of types for the chapter; do not imply that every exercise ever published by every course has been reproduced. Do not reproduce copyrighted source text without permission.
4. Add a **clear, high-yield review sheet** of definitions, decision rules, boundary cases, common mistakes, and exam-oriented reasoning patterns. This is an important companion to the full explanation, not a replacement for it.
5. Use precise mathematical notation and a readable math font. Add diagrams or interactive models where they clarify a difficult dependency or dynamic behavior; state what each model does and does not simulate. Use a clearly differentiated code font when an algorithm or implementation is taught.
6. End with exact references and a truthful statement of unresolved limits.

Length follows instructional need. Do not inflate pages through repetition, decorative spacing, copied lecture prose, or unrelated topics. Distinguish full teaching from the deliberately concise review sheet.

All mathematical presentation in the chapter library uses the bundled STIX Two Math font, distinct from prose: displayed and inline formulas, standalone mathematical symbols in body text, semantic indices, MathML operators and limits, and mathematical labels in diagrams. Build every chapter through the shared typography renderer, audit for unstyled math characters, and check mobile and print rendering before delivery. Preserve the mathematical statements when correcting typography.

The student approved the first logic chapter on 2026-09-29 and asked for **more emphasis on solved problems and the final high-yield section** in subsequent chapters. For each new chapter, map every in-scope reasoning pattern to at least one fully explained problem or boundary-case counterexample. The final review section must give complete, unambiguous statements, usable decision procedures, and the common traps that distinguish difficult questions. Do not let a long conceptual introduction crowd out these two sections.

The student approved the revised sets chapter on 2026-09-29 and emphasized that the **main lesson must retain maximum instructional depth**. The final high-yield sheet is a separate review aid; it must never replace intermediate derivations, proof assumptions, worked explanations, or advanced in-scope cases in the teaching body.

## Accuracy gate

Before setting a chapter to `ready`, compare its topic matrix with the selected course texts; check every formula transformation, theorem assumption, worked answer, edge case, attribution, source link, and print/mobile presentation. Keep a chapter `draft` while a known mathematical error or in-scope gap remains. Use independent finite checks where meaningful, without presenting a test script as a proof of general first-order claims.

The target is to remove every **identified** error and in-scope omission. A literal 100% guarantee about all unseen future questions or all courses in the world cannot be established. State residual uncertainty precisely rather than using an unsupported perfection claim. A chapter remains a review draft until the student explicitly approves it; approval promotes that chapter to the finished library and permits work on the next chapter.

## IELTS English track

English is a separate IELTS pathway, not doctoral-exam English. The requested scope has three strands: grammar, reading, and listening, taught from foundations through advanced task interpretation. State each session's planned duration before instruction. Teach and demonstrate first; use guided checks and error correction only after the teaching. Do not advance a stage merely because its provisional calendar week has passed. The current four weekly hours are a starting allocation, not a guarantee of readiness from a beginner baseline. The student confirmed IELTS Academic on 2026-09-29; the reading pathway uses that module. The Listening format is common to Academic and General Training. Official IELTS has Writing and Speaking as well, so this three-strand request cannot by itself ensure an overall band score.

The study-facing output is `dist/chapters/<topicId>.html`, generated from a reviewed English manuscript. The chapter index is `dist/lessons.json`. The English schedule is `dist/schedule.en.json`; the Persian schedule input is retained only as archival internal data. After delivery of one chapter, the existing chapter gate requires explicit user approval before work starts on the next chapter.

## Current chapter handoff

2026-10-02: The student explicitly approved a_recurrence. Its chapter index and reproducible builder preserve ready status.

The sole new chapter is a_divide, Week 2 Algorithms: Divide and Conquer: Design and Analysis. Its English review draft covers design contracts, search, stable merging and strict inversions, maximum-subarray sufficient summaries, deterministic planar closest pair, signed and odd-width Karatsuba, all ordered Strassen proofs, FFT and exact-recovery conditions. Four principal university courses and an additional ETH course were genuinely reviewed from an eight-university screened pool. It contains 48 fully worked problems, 88 complete examination rules, five original vector diagrams, twelve native MathML displays and an independently checked exact summary laboratory.

Study page: dist/chapters/a_divide.html. Source comparison: dist/reviews/a_divide-sources.html. Reading scopes: research/a_divide-source-audit.md. Quality evidence: research/a_divide-quality-audit.md, research/a_divide-math-checks.json and research/a_divide-evidence. Deferred entrance-exam archives were not opened or classified.

The gate is awaiting_user_approval. a_divide remains draft until explicit approval. The proposed next topic is a_correct; it has not been started. Prior chapter and library-review evidence remain preserved.

## Authoritative whole-library examination revision

2026-10-03: The explicit whole-library rewrite supersedes older delivery counts and approval states below. All 22 existing chapters remain revision drafts. No new topic may start until explicit approval of this revision. Current evidence and delivery: research/exam-rewrite/manifest.json, DELIVERY.en.md, answer-checks.json and evidence/browser-review.json. App report: dist/library-review.html. Previous Iranian exam-archive deferral remains active. Do not reset study progress.

The authoritative rebuild is research/rebuild_exam_library.py using research/exam-rewrite/baseline and the new authored chapter files. Run it after any legacy builder. Never publish a legacy builder’s output alone. See research/exam-rewrite/README.md for the complete generation and validation sequence.

## Exam-grounded problem-bank revision

2026-10-03: The student explicitly authorized studying the original MS and PhD PDFs in main/Exams and rejected the replacement banks as insufficient. This supersedes final-month exam deferral. Each existing chapter must include attributed, accurately translated actual examination items where relevant, plus independently worded medium-to-hard original analogues with complete solutions. Record year, field, question number, original PDF page, original options and answer provenance; do not invent official answers or exact chapter matches. University-course teaching and source standards remain active. Existing material remains draft until explicit approval.

## Completed exam-grounded problem banks

22 chapters; 56 distinct authentic questions, 111 authentic placements, 912 original authored analogues, 44 retained challenges; 1067 total problem entries; 339 examination notes; 70 figure instances.

The latest instruction supersedes archive deferral. Every source question has original options, PDF page, year, field, immutable commit and an independent worked solution. Three ambiguous/defective records are excluded and documented. Difficulty for original questions is qualitative.

145 existing finite/exact and output checks, plus 368 expanded numeric recomputations, passed. The 22 pages and 70 figures passed mobile and print-style geometry checks. These checks do not prove universal correctness or unseen-exam performance.

User-facing report: dist/library-review.html. Source audit: dist/exam-source-audit.html. Sources: actual-items.json and READING_LOG.en.md. The 736 additions comprise 184 related four-question families; this is not a claim of 736 independent concepts. Authoring: original-*.json, author_*.py and expand_*.py. Audit: verify_answers.py and verify_expansion.py. Reauthor: clean_authoring.py regenerates both the earlier banks and all five expansion collections. Rebuild: research/rebuild_exam_library.py applies the calibration overlay after the legacy banks.

All chapters remain drafts. Await explicit approval before promoting this revision or starting another chapter. Preserve study progress.

## Current handoff — algorithm correctness

The user approved the version-56 library of 22 chapters on 3 October 2026. Approval is preserved in research/library-approval.json. The next chapter, a_correct, is now a complete English review draft; do not start another chapter before explicit approval.

Delivery: dist/chapters/a_correct.html. Four reviewed written courses: CMU, Cambridge, MIT and Stanford, with exact reading scope in research/a_correct-source-audit.md. Fifty original/course-derived tasks plus four attributed authentic archive questions; 74 complete notes; five original diagrams; native MathML; safe bounded binary-search proof laboratory. Verification: research/a_correct-validation.json and research/a_correct-browser-review.json. Evidence states finite domains and limits. All prior study progress is preserved.

## Superseding visual-teaching requirement — 3 October 2026

The user rejected a_correct because sorting and other special concepts require precise, understandable animated simulations in this chapter and earlier chapters. The written approval of the previous 22 chapters remains recorded, but these visual additions need review. Do not start another chapter before approval of this revision.

The animation catalog embeds 105 distinct bounded models with 697 exact checkpoints into 107 instructional placements across all 23 chapters. Models include tagged-record sorting, stable merge, binary-search and partition counterexamples, proof constructions, sets, quantifier order, induction, closures, Euclid, recurrence trees, probabilities, projections, ordered matrix operations, FFT butterflies, program-store transitions, finite arithmetic, Gray/Hamming codes, CMOS switch states, and explicitly modeled gate-delay hazards. Each player has pause/play, previous/next, restart, speed and checkpoint controls; mobile readers can enlarge diagrams. Text, worked answers, 1,121 problem entries, final notes and study progress are retained.

Inventory and exact coverage: research/animation-manifest.json and dist/animation-review.html. Mathematical models: research/animations/. Required future standard: research/ANIMATION_STANDARD.md. Independent state checks: research/animation-model-audit.json. Browser QA: research/animation-browser-audit.json. A listed finite trace is not a universal proof, a physical-circuit model, or a claim that every exercise or every parameter is animated. Future drafting must identify and implement necessary concept-specific simulations before delivery.

## Current authoritative handoff — conditional probability

3 October 2026: The user explicitly approved the version-58 animated library and algorithm correctness chapter. All 23 existing chapters are ready; the earlier 22 approvals from version 56 and the additional correctness approval from version 58 are preserved in `research/library-approval.json`. The approved visual inventory is separately recorded in `research/animation-approval.json`. Historical pending statements above are superseded by this entry.

The sole new chapter is `s_conditional`, Week 2 Probability and Statistics: Conditional Probability, Multiplication, and Independence. Delivery: `dist/chapters/s_conditional.html`. It contains deep English instruction, four primary university courses plus a supplementary Oxford reading, 60 solved questions (four authentic and 56 original/course-derived), 80 complete rules, seven original diagrams, nine exact simulations with 60 checkpoints, and an exact integer-weight joint-table laboratory.

Sources and scope: `research/s_conditional-source-audit.md` and `research/s_conditional-source-downloads.json`. Audits: `research/s_conditional-quality-audit.md`, `research/s_conditional-validation.json`, and `research/s_conditional-browser-review.json`. The full animated library now has 114 scenarios in 24 chapters; all checkpoints were rendered without label-layout findings. Preserve the existing 1,121 questions and the 60 new questions. Browser review passed formula and diagram fonts, mobile containment, exact lab outputs, input boundaries and printing.

The current gate is `awaiting_user_approval`; `s_conditional` remains a draft. The proposed next topic is `s_bayes`. Do not author it until explicit approval. Course-selection completeness is bounded to the documented candidate pool, and finite checks do not establish a universal accuracy or unseen-exam guarantee. Preserve study progress and all existing approvals during rebuilds.

Rebuild only this chapter with `research/author_conditional_problems.py` and `research/build_conditional_chapter.py`; then run `research/verify_s_conditional_en.py`, `research/qa_conditional_browser.py`, the animation model/browser audits when their data change, and `research/check_site_en.py`. Keep source PDFs in the private research cache rather than distributing them with the Site.

## Current authoritative handoff — Bayes and base rates

4 October 2026: The user explicitly approved the version-59 conditional-probability chapter and authorized the next chapter. All 24 prior chapters and their animations are approved; their per-topic version records are preserved. Historical pending statements above are superseded by this entry.

The sole new chapter is `s_bayes`, Week 2 Probability and Statistics: Bayes' Rule, Base Rates, and Evidence. Delivery: `dist/chapters/s_bayes.html`. It contains deep English instruction from four primary reviewed written courses (MIT, Stanford, CMU, Oxford), a fifth supplementary Berkeley course, 65 solved problems (two authentic revisits and 63 original/course-derived), 80 complete rules, seven original figures, ten exact simulations with 51 checkpoints, and a rational posterior laboratory with independent/copy report models.

Sources and actual reading boundaries: `research/s_bayes-source-audit.md` and `research/s_bayes-source-downloads.json`. Quality/verification: `research/s_bayes-quality-audit.md`, `research/s_bayes-validation.json`, `research/s_bayes-browser-review.json`. Mathematical and structural checks passed 7,446 assertions; local desktop, mobile and print review passed without figure-label or formula overflow findings. The library now contains 25 chapters, 1,246 question entries, 124 models and 808 checkpoints. Revisited authentic items are entries rather than additional unique examinations. Preserve the 1,181 prior questions and all study-progress data.

The gate is `awaiting_user_approval`; `s_bayes` remains a draft. The proposed next topic is `l_gauss` according to the Week 2 subject order. Do not author it or another chapter without explicit approval. Source selection is bounded to the documented accessible pool; scientific coverage and unseen-question performance are not asserted as universal guarantees.

Rebuild only Bayes with `research/author_bayes_problems.py` and `research/build_bayes_chapter.py`. Verify with `research/verify_s_bayes_en.py`, `research/qa_bayes_browser.py`, `research/verify_concept_animations.py`, `research/qa_animations_browser.py` when animation data change, and `research/check_site_en.py`. Keep source PDFs in the private cache. Publication uses the existing owner-private Site; mirror exact changed source paths into GitHub branch `study-planner-1406` while preserving unrelated local mirror changes.

## Current authoritative handoff — Gaussian elimination

4 October 2026: The user explicitly approved Bayes in Site version 60 and authorized the next chapter. All 25 earlier chapters and their animations are approved. Earlier pending statements above are historical and superseded by this entry.

The sole new chapter is l_gauss, Week 2 Linear Algebra: Gaussian Elimination and Linear Systems. Delivery is dist/chapters/l_gauss.html. It includes deep English teaching and proofs from four primary genuinely reviewed courses (MIT 18.700, Oxford M1, Stanford CME108/MATH114 and Berkeley Math 54), with CMU 21-241 as a fifth reviewed comparison. The bounded written pool, actual reading ranges, source slips and prompt inventory are documented in research/l_gauss-source-audit.md and research/l_gauss-reviewed-courses.json; exact document fingerprints are in dist/evidence/l_gauss/sources.json.

The chapter has 71 fully solved tasks: newly inspected doctoral CS 1404 Q33, an explicit master's CS 1405 Q113 revisit, and 69 original/course-derived mathematical and conceptual problems. It includes 80 complete summary/examination rules, seven original SVG figures, twelve exact animated models with 60 checkpoints, and an exact rational matrix laboratory. The library totals 26 authored chapters and 1,317 question entries; its 136 unique animated models contain 868 checkpoints. Revisited authentic questions are entries, not additional unique examinations.

Independent symbolic and finite checks passed 2043 assertions, with twelve exact full-reduction problem certificates, parameter branches, LU/PLU products, inverse/coordinate maps, field enumeration, operation counts and original archive hashes. Browser QA passed seven figure layouts, 390-pixel mobile containment, dedicated math/code/diagram fonts, print solutions, six rational laboratory presets, eight input-error cases, step controls, actual row-exchange motion and figure enlargement. The complete animated library was rendered with zero clipped or overlapping text-label findings. Preserve all 1,246 prior questions and existing study-progress data.

The current gate is awaiting_user_approval; l_gauss remains a draft. The proposed next topic is l_rank, following Week 2 subject order. Do not author it or any other next chapter until explicit approval. Do not quiz the user before they study. Source comparison and checked input sets are finite; never replace that evidence with universal scientific or unseen-score guarantees.

Rebuild only this chapter with research/author_gauss_problems.py and research/build_gauss_chapter.py. Check with research/verify_l_gauss_en.py, research/qa_gauss_browser.py, research/verify_concept_animations.py, research/qa_animations_browser.py when animation data change, and research/check_site_en.py. The strict native MathML renderer now handles matrix tables and explicit accent notation; matrices, formula indices and sums retain STIX Two Math. Public course-register wording counts chapter-specific entries rather than pretending repeated sections are distinct offerings. Keep private source PDFs outside Site assets.

Publish the exact committed/pushed source to the existing owner-private Site and mirror only its changed paths to GitHub branch study-planner-1406. Preserve unrelated unstaged mirror changes. This is a one-chapter delivery and approval boundary.

## Current authoritative handoff — rank, invertibility, and solution sets

4 October 2026: The user explicitly approved l_gauss in Site version 61 and authorized one next chapter. All 26 earlier chapters and their animations are approved. Earlier pending statements above are historical and superseded by this entry.

The sole new draft is l_rank, Week 2 Linear Algebra: Rank, Invertibility, and Solution Sets, delivered at dist/chapters/l_rank.html. Four primary genuinely reviewed written courses from Oxford, MIT, Stanford and UC Berkeley are synthesized with CMU as a fifth reviewed comparison. The bounded pool, exact reading ranges, corrected source slips and accessible prompt inventory appear in research/l_rank-source-audit.md, research/l_rank-reviewed-courses.json and dist/evidence/l_rank/sources.json. No worldwide exhaustive-course claim is made.

The chapter includes full English proofs, 90 worked mathematical/conceptual questions, 80 complete review/examination rules, seven original SVG figures, twelve concept animations with 48 exact checkpoints, and an exact rational four-space laboratory. Two authentic questions are explicit revisits of MSc CS 1405 Q41 and PhD CS 1404 Q30; they are not counted as additional unique archive questions. The full library now has 27 authored chapters and 1,407 question entries, with 148 unique animated models and 916 checkpoints.

Independent verification passed 1923 checks across all four basis certificates, parameter strata, Schur complements, update kernels, real/complex and finite-field cases, composition/sum inequalities, every new animation snapshot, original archive hashes and unchanged approved-question content. Browser checks passed all seven figure layouts, 390-pixel mobile containment, dedicated mathematical/code/diagram fonts, all printed solutions, six exact laboratory presets, eight invalid-input cases, step controls, actual fiber-point motion and enlargement. The full animated library has zero text clipping or overlap findings. Proofs remain the mathematical basis; finite tests do not guarantee all unseen answers.

The gate is awaiting_user_approval, with proposed next topic p_functions in Week 2. l_rank stays a draft until explicit approval. Do not quiz the user before they study and do not begin another chapter at this boundary.

Rebuild only this chapter using research/author_rank_problems.py, research/rank_sources_record.py, research/build_rank_lab.py and research/build_rank_chapter.py. Verify with research/verify_l_rank_en.py, research/qa_rank_browser.py, research/verify_concept_animations.py, research/qa_animations_browser.py when model data change, and research/check_site_en.py. Native MathML retains STIX Two Math; prose, headings and code retain the accepted fonts. Preserve study-progress data and all private cached original PDFs.

Publish the exact pushed source to the existing owner-private Site and mirror only changed paths to GitHub branch study-planner-1406. Preserve unrelated mirror deletions. No other chapter is delivered or started in this turn.

## Current authoritative handoff — functions, scope and parameter passing

4 October 2026: The user explicitly approved l_rank in Site version 62 and authorized one next chapter. All 27 earlier chapters and their animations are approved. Earlier pending statements above are historical and superseded by this entry.

The sole new draft is p_functions, Week 2 Programming Fundamentals: Functions, Variable Scope, and Parameter Passing, at dist/chapters/p_functions.html. Four primary written courses from Cambridge, UC Berkeley, Harvard and CMU are synthesized with Stanford and MIT as two additional genuinely reviewed comparisons. Exact reading ranges, bounded discovery/selection criteria, language differences, source corrections and prompt inventory are recorded in research/p_functions-source-audit.md, research/p_functions-reviewed-courses.json and dist/evidence/p_functions/sources.json. No worldwide exhaustive-course claim is made.

The chapter contains detailed English instruction, 91 fully explained mathematical/conceptual problems, 80 complete summary/examination rules, seven SVG figures, twelve exact animations with 58 checkpoints and an adjustable five-model laboratory. Its two authentic archive items are explicit bridge revisits of MSc CS 1393 Q167 and PhD CE 1405 Q9; they are not claimed as new unique examination items or functions-specific archive questions. The library now contains 28 authored chapters, 1,498 question entries, 160 animated models and 974 checkpoints.

Independent verification passed 5,587 checks and 21 actual Python executions. All 1,407 earlier approved question entries were preserved. Browser review passed all seven figure layouts, all 91 printable solutions, dedicated prose/heading/math/code fonts, 390-pixel mobile containment, 205 valid laboratory input cases, eight invalid-input cases, controls, enlargement and actual motion. The final library animation review passed 160 scenarios across 28 chapters with zero label-layout findings. No local C/C++ compiler is available: C/C++ cases have explicit language-rule reasoning and independent finite models, not a compiled-execution claim. Finite checks do not guarantee unseen-question performance.

The gate is awaiting_user_approval, with proposed next topic p_arrays. p_functions remains a draft until explicit approval. Do not begin another chapter or quiz the user before they study.

Rebuild this chapter with research/author_functions_problems.py, research/functions_sources_record.py and research/build_functions_chapter.py. Verify with research/verify_p_functions_en.py, research/qa_functions_browser.py, research/verify_concept_animations.py, research/qa_animations_browser.py when model data change, and research/check_site_en.py. Preserve study-progress data, all approved content and private cached original PDFs. Publish exact pushed source to the existing owner-private Site and mirror only changed paths to GitHub branch study-planner-1406, preserving unrelated mirror changes.

## Current authoritative handoff — arrays and indexing

4 October 2026: The user approved p_functions in Site version 63 and authorized one next chapter. All 28 earlier chapters and their animations are approved; earlier pending statements above are historical.

The sole new draft is p_arrays, Week 2 Programming Fundamentals, at dist/chapters/p_arrays.html. Four primary written courses from Cambridge, CMU, Harvard and UC Berkeley are synthesized with Stanford and MIT as two genuinely read complementary sources. Exact reading ranges, bounded eight-university candidate evaluation, source corrections and question provenance are recorded in research/p_arrays-source-audit.md, research/p_arrays-reviewed-courses.json and dist/evidence/p_arrays/sources.json. No worldwide exhaustive-course claim is made.

The detailed English lesson covers array objects and bounds, layouts and inverses, C pointer domains, traversals and proof obligations, prefix/difference tables, overlap and mutation order, Python sharing/slices, strings, capacity and packed storage. It includes complete overlap-safe C element-moving and segment-reversal implementations. There are 83 worked mathematical/conceptual tasks, 80 complete examination rules, seven SVG figures, eighteen animations with 114 checkpoints and a six-model adjustable lab. MSc CS 1393 Q167 and PhD CS 1404 Q72 are verified authentic bridge revisits, not new unique archive items. The library now has 29 chapters, 1,581 question entries, 178 animation models and 1,088 checkpoints.

Independent verification passed 5,922 checks and ten actual Python question executions. All 1,498 previously approved question entries were preserved. Browser checks passed all seven figure layouts, all 83 printable solutions, dedicated prose/heading/math/code fonts, 390-pixel mobile containment, 540 valid laboratory cases, eleven invalid cases, exact transitions, controls, enlargement and actual motion. The final library animation audit passed 178 models across 29 chapters with zero label-layout findings. No local C/C++ compiler is available; C cases have written language-rule reasoning and independent models. Finite checks do not guarantee performance on every unseen examination question.

The gate is awaiting_user_approval with proposed next topic g_kmap (Minterms, maxterms, and simplification), following Week 2 order. p_arrays stays a draft until explicit approval; do not start another chapter or quiz the user before study.

Rebuild with research/author_arrays_problems.py, research/arrays_sources_record.py and research/build_arrays_chapter.py. Verify with research/verify_p_arrays_en.py, research/qa_arrays_browser.py, research/verify_concept_animations.py, research/qa_animations_browser.py when model data change, and research/check_site_en.py. Preserve all approved content, progress and private original PDFs. Publish exact pushed source to the owner-private existing Site and mirror only changed paths to GitHub branch study-planner-1406, preserving unrelated mirror changes.

## Current authoritative handoff — logic minimization

4 October 2026: The user approved p_arrays in Site version 64 and authorized one next chapter. All 29 earlier chapters and their animations remain approved; previous pending statements above are historical.

The sole new draft is g_kmap, Week 2 Digital Logic, at dist/chapters/g_kmap.html. Five genuinely read written courses from MIT, Cambridge, Stanford, Cornell and Columbia are synthesized; four complementary primary sources plus Columbia for exact covering. The bounded discovery pool has nine university candidates. Exact reading, source hashes, course attribution and source corrections are in research/g_kmap-source-audit.md and dist/evidence/g_kmap/sources.json. No worldwide exhaustive-course claim is made.

The full English lesson includes canonical polarity, indexing, cubes, Gray maps, SOP/POS, DC contracts, primes, essential witnesses, cyclic charts, weighted dominance, Petrick, QM completeness, hazard edges, delay traces and multi-output sharing. There are ten detailed lesson examples, 84 fully solved tasks, 80 full rules, seven original figures, fourteen animations with 51 checkpoints and an exact four-input editable lab. Three authentic MSc/PhD questions are verified revisits, not new unique archive items. Q78 option 4’s original fifth term is corrected in this revisit, and its DC transition contract is audited explicitly. Earlier approved banks remain unchanged.

Independent verification passed 2,472 checks, including all 256 three-input functions, all 81 two-input incomplete contracts, bit-mask/QM/Petrick agreement, DC edge counterexample/repairs, formula-token preservation and original PDF fingerprints. Browser checks passed 530 exact lab inputs, nine invalid inputs, controls, real token motion, reduced motion, seven figure layouts, all 84 printable solutions and desktop/mobile/print formulas. Library animation QA passed 192 models across 30 chapters with no label-layout issues. The library has 1,665 question entries and 1,139 checkpoints. Finite checks do not guarantee every unseen examination answer.

The gate is awaiting_user_approval; proposed next topic is g_combin, following Week 2 order. Keep g_kmap a draft until explicit approval. Do not start another chapter or quiz the user before initial study. Preserve all prior content, study-progress data and private original PDFs.

Rebuild using research/author_kmap_problems.py, research/kmap_sources_record.py and research/build_kmap_chapter.py; the renderer imports research/kmap_math_layout.py for scope-preserving list/factor reflow. Verify with research/verify_g_kmap_en.py, research/qa_kmap_browser.py, research/verify_concept_animations.py, research/qa_animations_browser.py when scenario data change, and research/check_site_en.py. After observed verification, research/finalize_kmap.py publishes evidence and locks the gate. Push the exact source state to the existing owner-private Site and mirror only changed files to GitHub branch study-planner-1406, preserving unrelated mirror deletions.

## Current authoritative handoff — combinational circuit design

4 October 2026: The user approved g_kmap in Site version 65 and authorized only the next chapter. g_kmap approval is recorded in both ledgers; there are now 30 approved earlier chapters. Previous pending statements above are historical.

The sole new draft is g_combin, Week 2 Digital Logic, at dist/chapters/g_combin.html. Five written courses from MIT, Stanford, Cambridge, Cornell and Berkeley are genuinely read within exact recorded ranges. The bounded discovery pool contains nine university candidates. Source attribution, cached document fingerprints, reading ranges, selection rationale and source corrections are in research/g_combin-source-audit.md and dist/evidence/g_combin/sources.json. The original course PDFs remain private. No worldwide exhaustive claim is made.

The full English lesson covers complete and relational contracts, DAG closure/uniqueness, internal nets, multilevel sharing, fan-in and arrival-sensitive trees, Shannon cofactors, decoder/ROM construction, NAND/NOR polarity, widths, complete combinational HDL, equivalence miters, stuck-at testing, timing extrema and false paths. It contains twelve detailed examples and three integrated cases, 82 solved tasks (80 original/course-inspired; two authentic verified bridge revisits), 80 complete rules, eight original figures, fourteen animations / 72 checkpoints and a three-mode editable lab. All 30 earlier approved banks and 1,665 entries remain unchanged.

Independent verification passed 7,911 checks. Browser checks passed 96 exact mode/input/variant comparisons, six rendered variants, four malformed-call rejections, genuine token motion, controls, reduced motion, all eight figure layouts, all 82 printable solutions, fonts and 390-pixel mobile/print containment. Library animation review passed 206 models with no label findings. The library now has 31 chapters, 1,747 entries and 1,211 checkpoints. Code is model-verified, not claimed compiled; finite Boolean checks do not certify analog behavior or every unseen examination question.

The gate is awaiting_user_approval. Proposed next topic is d_counting, following Week 3 schedule order. Keep g_combin a draft until explicit approval; do not start the next chapter or quiz the user before initial study.

Rebuild with research/author_combin_problems.py, research/combin_sources_record.py, research/prepare_combin_build.py, research/build_combin_chapter.py. The renderer imports research/combin_math_layout.py, which preserves scopes and attaches punctuation. Verify with research/verify_g_combin_en.py and research/qa_combin_browser.py; run the global animation checks when model data change. After observed verification, research/finalize_combin.py publishes evidence and closes the gate. Publish the exact pushed source to the existing owner-private Site and mirror only changed files to GitHub branch study-planner-1406, preserving unrelated deletions in that mirror.

## Current authoritative handoff — subject-specific whole-library revision

5 October 2026: The user rejected the shared simulation style, missing circuit schematics and disorganized formulas across all existing chapters. This instruction authorized revision of the full 31-chapter library; no new chapter was started. Earlier next-chapter instructions above are historical.

The delivered review draft is dist/subject-visual-review.html. All 206 models now dispatch through twenty explicit subject-specific families in semantic-diagrams.js. Thirteen static logic/circuit figures and 169 printable initial walkthroughs use the revised models. Corrected transistor connectivity, enable/polarity, priority validity, ring capacity, matrix transpose, coordinate scaling, probability conditioning, shared nets and circuit routing are included. Interactive remounting now disposes prior players and keyboard handlers instead of keeping stale laboratory states.

Every chapter receives visual reading instructions. Existing deep lessons, proofs, rules and all 1,747 question entries are retained; stems, solution reasoning and TeX sources are checked against the opening source SHA. This is not a claim that all prose was freshly reauthored. Sources were not re-searched worldwide during this visual revision. Mathematical layout preserves leaves and scope, restores canonical expressions for print, spaces matrix entries, and provides labeled internal mobile panning for indivisible expressions.

Observed evidence: all 1,211 checkpoint renders / 206 models, all 31 chapter figure layouts and printable solutions, actual 390-pixel mathematical containment and leaf/source preservation, 48 rendered circuit input predicates / topology counts, and 5,266 serialized/reference assertions. Separate combinational checks passed 7,911 assertions and 96 input/variant comparisons. Finite models do not certify electrical behavior or unseen examination performance. See research/subject-visual-review.json, research/subject-visual-browser-audit.json and research/subject-library-browser-audit.json.

The gate is awaiting_user_approval for this whole-library revision. Historical chapter approvals remain recorded separately; revised visual layers are pending. Do not begin d_counting until the user approves continuation. Do not ask the user test questions before initial study. Study-progress storage and private PDFs are preserved.

Maintenance: research/revise_visual_library.py assigns explicit contracts and canonical math; research/qa_subject_visuals.py renders models and checks mobile mathematical preservation; research/install_subject_figures.py installs printable SVGs and math-styled captions; research/finalize_subject_visual_review.py refreshes hashes, evidence, report and gate after observed QA. build_concept_animations.py retains reviewed visual contracts/previews and canonical math. Historical one-time patch scripts are migration provenance, not required maintenance commands. Publish the exact pushed source to the existing owner-private Site and mirror changed files only to GitHub branch study-planner-1406, preserving unrelated mirror deletions.


## Current delivery: English discrete counting chapter, October 5, 2026

The student explicitly approved Site version 67: the prior 31 chapters and their visual/mathematical revision. Their 1,747 question entries remain intact except the verified correction of MSc CS 1405 Q113 option 1 from 32 to 37. The new sole d_counting chapter is now a review draft awaiting explicit approval, with four genuinely reviewed written university courses from MIT, Berkeley, Stanford and CMU, 88 solved questions (80 new plus eight authentic revisits), 80 examination rules, and 15 dedicated models with 76 checkpoints. Read research/chapter-gate.json before any further chapter work. Do not start d_inclusion or another chapter before approval. No test is requested from the student before initial reading.

Sources, boundaries and access limits: research/d_counting-source-audit.md and research/d_counting-reviewed-courses.json. Main lesson: research/d_counting.en.md; questions: research/d_counting-questions.json; rules: research/d_counting-review.en.md. Build only this chapter with research/build_d_counting_models.py and research/render_d_counting.py. The counting renderer is independent of the older shared scene catalog and uses dist/chapters/d_counting-models.json, d_counting.js and d_counting.css. Do not erase its inventory when running a legacy all-scene rebuild. Combined inventory records 221 models and 1,287 checkpoints, while original 206-model evidence remains historical.

Observed numerical and interaction evidence: research/d_counting-verification.json, d_counting-browser-audit.json and d_counting-model-audit.json. The real browser checks all 76 checkpoint text layouts, actual 390-pixel formula containment, loaded fonts, controls, reduced motion and printable full solutions/checkpoints. Source pool comparison is bounded to eight located candidates; no worldwide exhaustive ranking or universal examination-success guarantee is asserted.

Publish the exact pushed source to the existing owner-private Site and mirror only changed files to GitHub study-planner-1406, preserving unrelated mirror deletions. The gate remains awaiting_user_approval after delivery.


## Active chapter: inclusion-exclusion, October 5, 2026

The user explicitly approved d_counting in Site version 68 and authorized only the next chapter d_inclusion. All 32 existing chapters remain approved. Work continuously on this chapter until its complete review draft is delivered, then wait for explicit approval. Preserve all existing questions, formulas, visuals and study progress.


## Current delivery: English inclusion-exclusion chapter, October 5, 2026

The user explicitly approved d_counting in Site version 68 and requested the next sole chapter. The 32 earlier chapters and their 1,835 question entries are preserved. d_inclusion is now a review draft awaiting explicit approval, with four genuinely reviewed primary written courses from MIT, Oxford, Cornell and CMU and a fifth reviewed Berkeley note. A documented eight-candidate pool supports a bounded selection; no worldwide exhaustive comparison is claimed. The chapter has a deep 16-section lesson, 80 original or independently reconstructed course tasks plus two authentic archive revisits, 80 complete examination rules, 13 distinct animated traces with 56 checkpoints, and four editable exact-enumeration labs.

Read research/chapter-gate.json before further work. Do not start d_pigeonhole or any other chapter before explicit approval. The approval ledgers retain the preceding 32 chapters as approved; this chapter is not promoted by its delivery. Do not ask the student a test before initial reading.

Source audit: research/d_inclusion-source-audit.md. Main lesson: research/d_inclusion.en.md. Task bank and archive provenance: research/d_inclusion-questions.json and d_inclusion-authentic.json. Rules: research/d_inclusion-review.en.md. Build only this chapter with build_d_inclusion_models.py, render_d_inclusion.py and install_d_inclusion_assets.py. Do not run start_d_inclusion.py again: it records the previous approval once. Do not overwrite this independent player or its inventory with the legacy shared model builder. The combined inventory has 33 chapters, 1,917 question entries, 234 models, 1,343 checkpoints and 197 embedded walkthroughs.

Observed evidence: d_inclusion-verification.json passed 1,267 independent mathematical assertions; d_inclusion-browser-audit.json records 308 independently checked lab cases, seven rejected inputs, all 56 measured checkpoint layouts, actual motion/controls, loaded fonts, 390-pixel containment and complete printable solutions/checkpoints. d_inclusion-model-audit.json records each distinct model contract. The quality audit records source errors corrected, finite verification limits and authentic revisits. The two archive questions were visually checked against the original PDFs; their answers are independent derivations rather than official keys.

Publish the exact pushed source to the existing owner-private Site. Mirror only changed files to the GitHub study-planner-1406 branch, preserving unrelated mirror deletions. Keep the gate awaiting_user_approval after delivery.


## Active chapter: pigeonhole principle, October 5, 2026

The user explicitly approved d_inclusion in Site version 69 and authorized only the next chapter d_pigeonhole. All 33 existing chapters remain approved. Work continuously on this chapter until its complete review draft is delivered, then wait for explicit approval. Preserve all existing questions, formulas, visuals and study progress.


## Current delivery: English pigeonhole chapter, October 5, 2026

The user explicitly approved d_inclusion in Site version 69, source c958f2b5b8eae701ab686ba77051991cc1b24278. Only d_pigeonhole was written. It is now a complete review draft awaiting explicit student approval. Five genuinely reviewed primary courses from MIT (two), Oxford, Stanford and Toronto, plus a reviewed Cornell complementary text, were selected from nine located candidates. This bounded comparison is not a claim to have evaluated every course worldwide.

The English lesson has 17 substantial sections, 80 original or independently reconstructed course problems plus two original-PDF-checked authentic adaptations, 80 examination rules, 18 subject-specific animated models, 78 checkpoints and four editable laboratories. Both source and quality audit pages are reachable. Mathematics uses native MathML and STIX Two Math; code uses JetBrains Mono, headings Newsreader and prose Source Sans 3. Existing bodies and all 1,917 questions are retained across 33 approved chapters. The combined library has 34 chapters, 1,999 question entries, 252 models, 1,421 checkpoints and 215 placements.

The independent verifier passed 68972 assertions. Actual browser checks covered 330 independent laboratory reference vectors, seven rejected numerical calls and an invalid list-parser input, every model checkpoint layout, moving elements and controls, reduced motion, loaded fonts, 390-pixel containment and all printable solutions/checkpoints. Original answers are independently derived rather than official keys; MSc CS 1405 Q116 is a newly checked worst-case-search bridge and PhD CS 1404 Q25 a parity-counting revisit. Source PDF fingerprints and exact reading ranges remain in evidence.

**Publication is pending, not live.** Chapter source 963f1e038ccd9716d503977c235ce6a16c09107c was pushed successfully. All 43 changed files were mirrored to GitHub branch study-planner-1406 at ddc986ecf4e4de96b09d2968f26f5a5bf1758353. Compressed-archive publication failed twice at the OpenAI file-request endpoint; an uncompressed archive reached the blob upload but timed out after 300006 ms at sdmntprpolandcentral.oaiusercontent.com. No saved version was returned. The native history was reconciled afterwards and remains Site version 69, source c958f2b5b8eae701ab686ba77051991cc1b24278. Do not claim version 70 exists or offer its URL as a published chapter. The new HTML and all assets are usable locally and in the repository. Before the next chapter, retry private publication of the CURRENT exact pushed source with a freshly packaged archive; preserve owner-private access and reconcile history if any result is ambiguous. This handoff itself may produce a newer source commit. Student approval of the chapter and deployment status are distinct; keep the existing approval gate.

Read research/chapter-gate.json first. Do not start the next scheduled missing chapter a_arrays until explicit approval of this draft. Do not rerun start_d_pigeonhole.py: it records preceding approval once. Rebuild only this chapter with build_d_pigeonhole_models.py, prepare_d_pigeonhole.py and render_d_pigeonhole.py; preserve the dedicated models rather than using the legacy shared builder. Authoritative handoff files are d_pigeonhole.en.md, d_pigeonhole-questions.json, d_pigeonhole-review.en.md, source and quality audits, verification.json, browser-audit.json and model-audit.json. Publication uses the exact pushed source on the existing owner-private Site. Mirror only changed files to the GitHub study-planner-1406 branch, preserving unrelated deletions. Keep awaiting_user_approval after delivery.


## Complete-equation layout correction, October 5, 2026

Automatic equation fragmentation was removed from the renderer and shared browser layer. Complete equations stay on one line, with horizontal scrolling when needed. Real matrix and piecewise rows are preserved. The actual browser audit covers all 34 chapters at desktop and mobile widths and retains all 20,879 MathML instances and 1,999 question entries. See research/single-line-math-review.md and the associated JSON evidence. Two unrelated existing laboratory errors were reproduced on the exact baseline and are documented separately; there are no new runtime errors from this revision. The d_pigeonhole approval gate is unchanged.


## Active chapter: arrays and linked lists, October 5, 2026

The user explicitly approved d_pigeonhole and its formula correction and authorized the next sole chapter a_arrays. Approval applies to the delivered local source; online publication is separate and currently unconfirmed. Preserve all 34 approved chapters and 1,999 questions. Write a deep English lesson, at least four genuinely reviewed university courses, a large mathematical/conceptual solved bank, concrete examination rules, and subject-specific pointer and storage animations. The a_arrays chapter stays draft until explicit approval.


## Current delivery: arrays and linked lists, October 5, 2026

The user explicitly approved d_pigeonhole. Only a_arrays was authored. It is a complete review draft awaiting explicit approval; a_stackqueue has not been started. Four primary courses from MIT, Berkeley, Oxford and Princeton plus Stanford and selected Cornell material were genuinely reviewed. The source audit bounds the candidate pool and records inaccessible CMU material without pretending it was read.

The chapter contains 86 solved problems, 80 examination rules, 20 concept-specific models, 113 checkpoints and four editable laboratories. Two archive questions were checked against original PDF pages; the MS item is a labeled revisit and neither answer is represented as an official key. The mathematical audit passed 92,701 finite assertions and browser labs passed 466 independent references. All 34 preceding chapters and 1,999 questions are retained. The library totals 35 chapters and 2,085 question entries. Single-line math repairs are retained throughout the prior library.

The local draft and source/quality audits are complete. Publication state must be verified separately; source pushes and a GitHub mirror are not proof of live Site deployment. Native Sites connectivity was intermittently unavailable during this turn.

Publication blocker: fresh Sites write-credential requests failed twice with HTTP transport errors at chatgpt.com/backend-api/ps/mcp. The earlier token expired at 11:20:57 UTC and was not reused. The complete local draft is retained; no live deployment is claimed.

Verified handoff: complete draft source commit afa7126; GitHub branch study-planner-1406 at 6d84224cd61e1be2fe8b241f486fd84b078ec5c1, confirmed with remote reference. All 87 unrelated unstaged mirror deletions are retained. Local preview is available at http://127.0.0.1:8870/chapters/a_arrays.html while its local server is running; the Codex browser opening was queued. The current production Site is not claimed to contain this draft. Obtain a fresh Sites credential, push the exact source and publish owner-private when connectivity returns. The chapter gate remains awaiting_user_approval; do not author a_stackqueue without approval.


## Arrays chapter: corrected arrow connections and text spacing

5 October 2026: The student rejected arrays/list arrow geometry and label spacing. Only this chapter was repaired. Explicit boundary ports, fixed-size arrowheads, separate return lanes, padded labels and animated endpoint rebinding passed all 113 fixed checkpoints, 497 laboratory frames and four moving-edge samples. All 466 numerical references, 86 problems and 80 rules are retained. Evidence: research/a_arrays-visual-repair.md and research/a_arrays-visual-browser-audit.json. The approval gate remains awaiting_user_approval; no subsequent chapter has started. Publication must be verified independently.


## Whole-library animation and worked-problem visual revision

5 October 2026: The user approved the arrays arrow/spacing repair and explicitly requested the same visual review across every chapter, plus individual review of every problem for necessary diagrams, circuit schematics and animations alongside its solution. Work is authorized for all 35 existing chapters and 2085 problems. The previous one-chapter limitation is superseded for this revision only. No new chapter starts. Preserve problem statements, source provenance, mathematical solutions and study progress, except documented corrections. Visual additions require review before promotion.


## Whole-library visual instruction: delivered for approval

5 October 2026: All 35 chapter animation placements use measured boundary/padding geometry. All 2085 original worked-problem bodies are retained; visual teaching and inspected transitions were added where relevant. The record distinguishes 317 question-linked aids, 74 separate arrays examples, and 1362 supporting concept placements. Finite saved-state, intermediate-movement, question-model, desktop/mobile/print and retention checks passed. This is a visual-instruction review, not a new exhaustive proof audit. Evidence: research/library-visual-question-review/manifest.json. Report: dist/library-visual-question-review.html. Gate: awaiting_user_approval; no new chapter begun. Publication is verified separately.


## Active chapter: Stacks, Queues, and Applications

5 October 2026: The user explicitly approved the whole-library visual revision and requested the next chapter. The sole active chapter is a_stackqueue. Preserve the 35 existing chapter HTML files byte for byte, including their 2,085 complete problem bodies and reviewed animations. The next chapter remains a draft until explicit approval. Publication remains a separate verification step.


## Completed draft: Stacks, Queues, and Applications

Publication follow-up: the complete chapter was pushed to GitHub (`study-planner-1406`, content commit `2badc8d`) and its exact source was pushed to Sites. Online publication is unconfirmed because the native archive upload and version-list reconciliation returned connection errors. Use the working local preview until publication is confirmed. See `research/a_stackqueue-publication.json`. This is a hosting limitation; the completed chapter still awaits explicit student approval.


Completed 5 October 2026. The sole new chapter is `a_stackqueue`. Four actually reviewed primary university courses, 84 fully solved problems, 80 final rules, 67 topic-specific models with 678 checkpoints, and five editable laboratories are included. All 35 preceding chapter bodies retain their original SHA-256 hashes and their 2,085 problems.

The chapter is available at `dist/chapters/a_stackqueue.html`; the library links it under Week 3. Source, reading, mathematical and browser audit evidence is adjacent in `research/a_stackqueue-*`. The gate is `awaiting_user_approval`. No next chapter is started. Publishing and GitHub delivery are recorded separately after their actual completion.


## Active chapter: Comparison and Non-comparison Sorting

6 October 2026: The user explicitly approved a_stackqueue and requested the next chapter. Only a_sort is active. Preserve the 36 previous chapter HTML files and their 2,169 question bodies. Source comparison, complete solutions, algorithm-specific models, formula layout, and mathematical/browser verification are required before delivery. The new chapter remains a draft until explicit approval.

## Sorting review draft — 2026-10-06

Delivered only `a_sort`: 88 worked questions, 80 rules, five selected university courses, 45 distinct models and ten editable algorithms. Mathematical and browser audits passed. Status: awaiting explicit user approval. Native publication is tracked separately in `research/a_sort-publication.json`. No following chapter has been started. Three earlier occurrences of PhD CE 1405 Q16 have the documented original option-order correction.

## Sorting visual revision — 2026-10-06

All 45 a_sort models now expose decisions, reasons and named regions. Array slots remain fixed; heap labels move on a fixed tree; copy markers follow authored transfer paths. 1,194 stored checkpoints, 402 explicit comparison steps and all 88 original problem bodies retained. Teaching and browser audits are adjacent. The chapter stays awaiting_user_approval, and no following chapter begins.

## Approved sorting and whole-library animation revision — 2026-10-06

The student approved Site version 72 and authorized the same decision-led teaching clarity across every existing chapter. The current work covers all 37 chapter pages, their concept walkthroughs and relevant worked-solution aids; no new chapter has been started. Preserve all 2257 complete question bodies and the existing proofs, lessons and review notes.

The library revision includes 730 stored models and 4002 exact checkpoints, in addition to the already approved sorting system's 45 models and 1194 checkpoints. These totals include reused question aids and must not be described as counts of unique algorithms. The full-library browser and retained-content evidence is recorded in research/library-animation-redesign; the study-facing report is dist/animation-review.html. Publication is recorded only after the pushed source and successful deployment are verified. The revised library awaits student review before a subsequent chapter.


## Active chapter: Searching, Selection, and Order Statistics — 6 October 2026

The student explicitly approved the version-73 animation redesign and requested the next scheduled missing chapter a_select. Preserve the 37 existing chapter pages and all 2257 complete question bodies. Work only on this English chapter: genuinely compare written university courses, teach prerequisites through advanced boundary cases, provide a large mathematical/conceptual solved bank and complete final rules, and build exact decision-led, subject-specific models and editable laboratories. Deliver the complete review draft, then wait for explicit approval. Do not ask the student test questions before first reading.

## Searching and selection review draft — 2026-10-06

Only `a_select` is delivered: five genuinely reviewed university courses with bounded reading scopes, 89 complete solved problems, 80 examination rules, 33 concept-specific models / 363 checkpoints and eight editable modes. Mathematical, literal-code, browser geometry, arrow-port, control, font, mobile and retention checks passed. All 37 preceding chapter HTML files and 2257 complete problem bodies are unchanged. A shared raw-animation control fix holds time exactly while pausing. The gate awaits explicit user approval; no next chapter has started. Source/GitHub push and private publication are recorded separately after verification.


## Active chapter: Descriptive Statistics, 6 October 2026

Explicit approval of a_select version 74 authorizes only s_descriptive. Preserve all 38 preceding chapter pages and 2346 complete question bodies. Deep English instruction, genuinely reviewed written courses, mathematical/conceptual problems, complete review rules and concept-specific animated visual instruction remain required. Deliver the complete draft and await explicit approval.


## Descriptive statistics review draft — 6 October 2026

Only s_descriptive is delivered: 22 deep English lesson sections, five reviewed written university courses with bounded scopes, 82 complete solved problems (80 original/course-inspired and two original-PDF-checked authentic questions), 80 complete final rules, 28 concept-specific models / 198 checkpoints and 14 editable modes. Rational, finite mathematical, actual JavaScript and real-browser checks passed. All 38 preceding chapter pages and 2346 complete problems are retained unchanged. The gate awaits explicit student approval; no next chapter is begun. Source push, GitHub mirror and private publication are tracked separately after verification.


## Verified descriptive-statistics publication — 6 October 2026

Private Site version 76 succeeded and its saved source matches dbfc92896b6ad50da341ae3692f5a448ffad6529. The exact loss-curve revision and chapter artifacts were pushed to GitHub branch study-planner-1406 (content commit c1544c99dd4159847a031436fda95e407b74817f). The publication receipt records recovery from the initial upload timeout and the Windows package-helper path issue. The chapter remains a draft awaiting explicit approval; no following chapter has started.


## Active chapter: Discrete Random Variables, 7 October 2026

The student explicitly approved s_descriptive version 76. The next missing scheduled topic is s_discrete in Week 3. Author and audit only this chapter; preserve all 39 preceding chapters and 2428 complete problem bodies. Await explicit approval after delivery.


## Discrete random variables — completed review draft, 7 October 2026

The explicit approval of descriptive statistics permits only this next Week 3 chapter. `s_discrete` is now a complete English draft: 26 sections, 80 original/reconstructed worked problems, three original-PDF-checked examination adaptations, 80 final rules, 37 subject-specific models with 208 checkpoints, and eight editable modes. Four core written courses were read from Oxford, MIT, UC Berkeley and Stanford; Harvard contributes bounded additional exercise material. Seventy rational checks and 616 independent enumeration comparisons passed. Real Edge checks cover all 208 checkpoints, connector boundaries, label padding, controls, reduced motion, print and mobile. The 39 previous HTML pages and 2,428 complete problems remain unchanged. Private Site and GitHub publication will be recorded after their actual verification. Gate: awaiting_user_approval; no next chapter begins before explicit approval.
