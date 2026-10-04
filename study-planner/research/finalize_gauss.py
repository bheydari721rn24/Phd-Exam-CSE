"""Record the sole draft handoff after substantive and browser audits pass."""
import json,shutil
from pathlib import Path
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent
v=json.loads((BASE/'l_gauss-validation.json').read_text());b=json.loads((BASE/'l_gauss-browser-review.json').read_text())
a=json.loads((BASE/'animation-browser-audit.json').read_text())
assert v['state']==b['state']=='passed' and not a['layoutIssues']
assert len(a['chapters'])==26 and len(a['scenarios'])==136
gate=json.loads((BASE/'chapter-gate.json').read_text())
gate.update(state='awaiting_user_approval',currentTopicId='l_gauss',nextTopicId=None,proposedNextTopicId='l_rank',approvedTopicId='s_bayes',activeWork='Gaussian elimination delivery is complete as a review draft; await explicit approval before any further chapter.',lastCompletedReview='l_gauss: five reviewed written courses, 71 solved tasks (2 authentic entries + 69 original/course-derived), 80 rules, seven figures, twelve models/60 checkpoints and exact rational elimination laboratory. Independent symbolic/finite checks and desktop/mobile/print/motion QA passed. All 25 earlier approvals and 1,246 question entries preserved.',nextReview='After explicit approval, use the Week 2 order to consider l_rank; do not author it while this gate awaits approval.')
(BASE/'chapter-gate.json').write_text(json.dumps(gate,indent=2)+'\n')
public=ROOT/'dist/evidence/l_gauss';out=Path(b['screenshots'])
for path in out.glob('l_gauss-*.png'):shutil.copy2(path,public/path.name)
browser=dict(b);browser['screenshots']='Chapter screenshots are saved beside this evidence file.'
(public/'browser.json').write_text(json.dumps(browser,indent=2)+'\n')
handoff=f"""
## Current authoritative handoff — Gaussian elimination

4 October 2026: The user explicitly approved Bayes in Site version 60 and authorized the next chapter. All 25 earlier chapters and their animations are approved. Earlier pending statements above are historical and superseded by this entry.

The sole new chapter is l_gauss, Week 2 Linear Algebra: Gaussian Elimination and Linear Systems. Delivery is dist/chapters/l_gauss.html. It includes deep English teaching and proofs from four primary genuinely reviewed courses (MIT 18.700, Oxford M1, Stanford CME108/MATH114 and Berkeley Math 54), with CMU 21-241 as a fifth reviewed comparison. The bounded written pool, actual reading ranges, source slips and prompt inventory are documented in research/l_gauss-source-audit.md and research/l_gauss-reviewed-courses.json; exact document fingerprints are in dist/evidence/l_gauss/sources.json.

The chapter has 71 fully solved tasks: newly inspected doctoral CS 1404 Q33, an explicit master's CS 1405 Q113 revisit, and 69 original/course-derived mathematical and conceptual problems. It includes 80 complete summary/examination rules, seven original SVG figures, twelve exact animated models with 60 checkpoints, and an exact rational matrix laboratory. The library totals 26 authored chapters and 1,317 question entries; its 136 unique animated models contain 868 checkpoints. Revisited authentic questions are entries, not additional unique examinations.

Independent symbolic and finite checks passed {v['checks']} assertions, with twelve exact full-reduction problem certificates, parameter branches, LU/PLU products, inverse/coordinate maps, field enumeration, operation counts and original archive hashes. Browser QA passed seven figure layouts, 390-pixel mobile containment, dedicated math/code/diagram fonts, print solutions, six rational laboratory presets, eight input-error cases, step controls, actual row-exchange motion and figure enlargement. The complete animated library was rendered with zero clipped or overlapping text-label findings. Preserve all 1,246 prior questions and existing study-progress data.

The current gate is awaiting_user_approval; l_gauss remains a draft. The proposed next topic is l_rank, following Week 2 subject order. Do not author it or any other next chapter until explicit approval. Do not quiz the user before they study. Source comparison and checked input sets are finite; never replace that evidence with universal scientific or unseen-score guarantees.

Rebuild only this chapter with research/author_gauss_problems.py and research/build_gauss_chapter.py. Check with research/verify_l_gauss_en.py, research/qa_gauss_browser.py, research/verify_concept_animations.py, research/qa_animations_browser.py when animation data change, and research/check_site_en.py. The strict native MathML renderer now handles matrix tables and explicit accent notation; matrices, formula indices and sums retain STIX Two Math. Public course-register wording counts chapter-specific entries rather than pretending repeated sections are distinct offerings. Keep private source PDFs outside Site assets.

Publish the exact committed/pushed source to the existing owner-private Site and mirror only its changed paths to GitHub branch study-planner-1406. Preserve unrelated unstaged mirror changes. This is a one-chapter delivery and approval boundary.
"""
with (ROOT/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8') as f:f.write(handoff)
print('Gaussian handoff recorded; only this chapter awaits explicit approval.')
