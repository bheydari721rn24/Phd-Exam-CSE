# Authoritative examination revision

The baseline directory preserves the delivered version 52 chapters. Correct deep teaching and source exercise derivations are retained. The authored chapter files replace the rejected problem banks and examination notes and add formula-solving instruction. All replacement questions are original; Iranian entrance-examination archives remain deferred.

## Rebuild sequence

Run from the study-planner directory, with the project's Python dependencies available:

1. `python research/exam-rewrite/prepare_authoring.py`
2. `python research/exam-rewrite/extend_notes.py`
3. `python research/exam-rewrite/challenges.py`
4. `python research/exam-rewrite/figures.py`
5. `python research/rebuild_exam_library.py`
6. `python research/verify_exam_revision.py`
7. `python research/check_site_en.py`
8. `python research/review_library_browser.py`
9. Visually inspect representative figure, question, notes and mobile captures.
10. `python research/finalize_exam_revision.py`

The preparation step regenerates 21 base authoring files. The logic chapter is directly authored. Steps 2 and 3 must follow preparation to restore boundary notes and multi-step questions. Change generator sources rather than only changing generated chapter Markdown, or preparation will overwrite the change. The overlay builder restores the revision after legacy builders. Never deliver output from a legacy builder alone. The aggregate legacy rebuild now invokes the authoritative overlay automatically.

The browser audit writes temporary screenshots. Finalization verifies the complete audit and copies current evidence into this directory. Rebuilding marks the revision in progress; finalization restores awaiting_user_approval after the audits. Do not run start_exam_rewrite.py again for this revision. Do not promote drafts or start new chapters without explicit approval.

The report distinguishes numerical verification, source-derived proof, presentation checks and national-examination calibration. No literal completeness or unseen-examination performance guarantee is made.
