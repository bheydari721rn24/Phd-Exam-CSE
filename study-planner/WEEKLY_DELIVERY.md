# Chapter delivery contract

## Current instruction

The study plan and every study-facing chapter are written in clear, precise English. Study dates and hours describe the student's reading; they do not impose a chapter-production schedule. Work on one chapter at a time until it passes the source, mathematical, pedagogical, and presentation checks below. The active chapter and its status are recorded in `research/chapter-gate.json`.

Archived Iranian master's and doctoral entrance-exam booklets are **deferred until the final month**. Do not mine, classify, reproduce, or solve those archived questions while writing the present chapters. In the final month, the student and assistant will solve them together, one question at a time, and use the results for targeted revision. Do not ask the student to answer test questions during the first reading.

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
