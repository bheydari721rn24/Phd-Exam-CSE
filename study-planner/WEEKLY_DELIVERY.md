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

As of 2026-10-02, the student explicitly approved `g_boolean`, now `ready`. The current chapter `g_gates` (Logic Gates and Function Implementation, Logic Circuits Chapter 3) is a completed English **review draft** at `dist/chapters/g_gates.html`, linked in the chapter library. The declared eight-university pool selected four genuinely reviewed core courses from MIT, Cambridge, Stanford and UC San Diego; Berkeley provides an additional written cross-check. Actual reading ranges, selection rationale, inaccessible candidates, document hashes and corrected source issues are recorded in `research/g_gates-source-audit.md` and `research/g_gates-source-manifest.json`.

The main lesson teaches stable semantics, complete gate constructions and their proofs, netlists, CMOS switching, noise margins, physical cost models and timed hazards. It contains 36 worked problems with transfer lessons, five connected summary paragraphs, 60 complete-sentence examination rules, an eight-step solving procedure, three original static diagrams, and a two-mode interactive laboratory. Independent checks passed 3525 mathematical assertions and 5547 laboratory assertions. Browser checks covered six truth-table states, five delay states, three invalid inputs, local code/math fonts, all problem headings, and zero page overflow at 390px. A 42-page A4 QA print was sampled visually, including the corrected CMOS label placement. Exact scope and remaining uncertainty are in `research/g_gates-quality-audit.md`.

Iranian archived examinations remain deferred to the final month. The gate is `awaiting_user_approval`: do not promote g_gates or start a following chapter until explicit student approval. There is no writing timetable or scheduled production deadline; prepare one complete chapter at a time, then await approval. The local QA PDF is an inspection artifact, not a promised standalone publication.
