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
3. Run `verify_answers.py` and `research/check_site_en.py`.
4. Run `research/review_library_browser.py` to verify the actual rendered solutions, typography, figures, narrow-screen fit, print preparation, and restoration of solution states.
5. Run `finalize.py`, then `research/qa_library_review_report.py`. Run `finalize.py` again only if new report screenshots need to be included in evidence.

PDF extraction and rendering use cached reference copies outside the checkout. No synced `sources/` file or original archive working-tree file is edited. Do not deploy the full archive cache.

## What the verification establishes

Exact rational calculations, finite enumeration and executable models check specified instances. Structural checks verify alternatives, references, controls, local anchors and native MathML argument structure. Browser checks verify typography and geometry with solutions open. These checks support the worked derivations; they are not a guarantee of universal accuracy or future performance on unseen examinations.

All revised chapters remain drafts pending explicit student approval. Keep the approval gate and study progress intact.
