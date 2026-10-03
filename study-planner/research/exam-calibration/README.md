# Exam-grounded revision

The student instruction of 3 October 2026 supersedes the earlier deferral of Iranian examination papers. This revision covers the 22 existing chapters; it does not create new chapters or promote drafts without approval.

## Sources and provenance

- `archive-manifest.json`: 84 PDF files at the immutable main-branch revision recorded in the manifest. Inventory does not mean exhaustive reading.
- `READING_LOG.en.md`: the source pages actually checked for included or excluded question records.
- `actual-items.json`: translated stems, original numbered alternatives, independently derived solutions, PDF-page references, repository paths, hashes, and topic associations.
- Three convention-sensitive or defective source records are excluded from single-answer practice and explained in `dist/exam-source-audit.html`.
- Original questions cite a real question family through their pattern reference; they are not attributed as authentic examination items. Medium/hard labels are qualitative author judgments.
- The existing university-course comparisons, reading scopes, rigorous teaching, and exercise tutorials remain intact. This revision does not claim to have newly read every course or every archive question.

## Reproduction order

1. Run the author files, or `clean_authoring.py` to normalize mathematical string escaping and run all authors.
2. Run `research/rebuild_exam_library.py`. The archive-grounded overlay runs after the legacy chapter overlay. Running `build.py` alone reapplies only the latest banks to existing teaching.
3. Run `verify_answers.py`, `verify_expansion.py`, and `research/check_site_en.py`.
4. Run `research/review_library_browser.py` to verify the actual rendered solutions, typography, figures, narrow-screen fit, print preparation, and restoration of solution states.
5. Run `finalize.py`, then `research/qa_library_review_report.py`. Run `finalize.py` again only if new report screenshots need to be included in evidence.

PDF extraction and rendering use cached reference copies outside the checkout. No synced `sources/` file or original archive working-tree file is edited. Do not deploy the full archive cache.

## What the verification establishes

Exact rational calculations, finite enumeration and executable models check specified instances. Structural checks verify alternatives, references, controls, local anchors and native MathML argument structure. Browser checks verify typography and geometry with solutions open. These checks support the worked derivations; they are not a guarantee of universal accuracy or future performance on unseen examinations.

All revised chapters remain drafts pending explicit student approval. Keep the approval gate and study progress intact.

## Tripling revision

The immutable version-55 baseline is `tripling-baseline.json`: 331 chapter problem entries. Every individual chapter must now reach at least three times its own prior count, not merely triple the library total. The expanded banks have 1,067 entries, including 736 additional original questions in 184 related families. These variants are not presented as 736 independent concepts or additional authentic archive questions. The 56 distinct authentic questions and their 111 disclosed placements remain.

Each new family contains two exact numeric instances, one symbolic generalization, and one hypothesis, counterexample, or applicability question. The five `expand_*.py` subject scripts regenerate these additions through `expand_common.py`. `clean_authoring.py` runs both the earlier author scripts and these five subject scripts. `verify_expansion.py` recomputes all 368 added numeric answers and binds the result to the selected option. Some checks use exact algebra rather than exhaustive enumeration; symbolic proofs and difficulty judgments are not independently proved by this script. Its JSON also records hashes of the exact authored inputs and verifies all 22 count targets.
