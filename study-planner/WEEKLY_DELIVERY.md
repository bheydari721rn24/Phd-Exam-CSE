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
