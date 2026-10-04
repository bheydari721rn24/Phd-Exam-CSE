"""Preserve approvals and record the one-draft handoff after verification."""
import json,shutil
from pathlib import Path
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent
v=json.loads((BASE/'l_rank-validation.json').read_text());b=json.loads((BASE/'l_rank-browser-review.json').read_text())
a=json.loads((BASE/'animation-browser-audit.json').read_text())
assert v['state']==b['state']=='passed' and not a['layoutIssues']
assert len(a['chapters'])==27 and len(a['scenarios'])==148
models=json.loads((ROOT/'dist/chapters/concept-animations.json').read_text())['scenes']
new={k:s for k,s in models.items() if k.startswith('rank-')}
gate=json.loads((BASE/'chapter-gate.json').read_text())
gate.update(state='awaiting_user_approval',currentTopicId='l_rank',nextTopicId=None,proposedNextTopicId='p_functions',approvedTopicId='l_gauss',activeWork='Rank, invertibility and solution sets is complete as a review draft. Await explicit approval before writing any next chapter.',lastCompletedReview=f'l_rank: four primary written university courses plus a fifth comparison, 90 fully solved questions (88 original/course-derived + 2 authentic revisits), 80 complete rules, seven original figures and twelve simulations/{sum(len(s["frames"]) for s in new.values())} exact checkpoints. Independent math and desktop/mobile/print/lab/motion audits passed; all 26 approvals and 1,317 earlier question entries preserved.',nextReview='After explicit approval, follow Week 2 order to p_functions. Do not author it while awaiting approval.')
(BASE/'chapter-gate.json').write_text(json.dumps(gate,indent=2)+'\n')
pub=ROOT/'dist/evidence/l_rank';out=Path(b['screenshots'])
for path in out.glob('l_rank-*.png'):shutil.copy2(path,pub/path.name)
record=dict(b);record['screenshots']='Created chapter screenshots saved beside this file.'
(pub/'browser.json').write_text(json.dumps(record,indent=2)+'\n')
text=f"""
## Current authoritative handoff — rank, invertibility, and solution sets

4 October 2026: The user explicitly approved l_gauss in Site version 61 and authorized one next chapter. All 26 earlier chapters and their animations are approved. Earlier pending statements above are historical and superseded by this entry.

The sole new draft is l_rank, Week 2 Linear Algebra: Rank, Invertibility, and Solution Sets, delivered at dist/chapters/l_rank.html. Four primary genuinely reviewed written courses from Oxford, MIT, Stanford and UC Berkeley are synthesized with CMU as a fifth reviewed comparison. The bounded pool, exact reading ranges, corrected source slips and accessible prompt inventory appear in research/l_rank-source-audit.md, research/l_rank-reviewed-courses.json and dist/evidence/l_rank/sources.json. No worldwide exhaustive-course claim is made.

The chapter includes full English proofs, 90 worked mathematical/conceptual questions, 80 complete review/examination rules, seven original SVG figures, twelve concept animations with {sum(len(s['frames']) for s in new.values())} exact checkpoints, and an exact rational four-space laboratory. Two authentic questions are explicit revisits of MSc CS 1405 Q41 and PhD CS 1404 Q30; they are not counted as additional unique archive questions. The full library now has 27 authored chapters and 1,407 question entries, with 148 unique animated models and {sum(len(s['frames']) for s in models.values())} checkpoints.

Independent verification passed {v['checks']} checks across all four basis certificates, parameter strata, Schur complements, update kernels, real/complex and finite-field cases, composition/sum inequalities, every new animation snapshot, original archive hashes and unchanged approved-question content. Browser checks passed all seven figure layouts, 390-pixel mobile containment, dedicated mathematical/code/diagram fonts, all printed solutions, six exact laboratory presets, eight invalid-input cases, step controls, actual fiber-point motion and enlargement. The full animated library has zero text clipping or overlap findings. Proofs remain the mathematical basis; finite tests do not guarantee all unseen answers.

The gate is awaiting_user_approval, with proposed next topic p_functions in Week 2. l_rank stays a draft until explicit approval. Do not quiz the user before they study and do not begin another chapter at this boundary.

Rebuild only this chapter using research/author_rank_problems.py, research/rank_sources_record.py, research/build_rank_lab.py and research/build_rank_chapter.py. Verify with research/verify_l_rank_en.py, research/qa_rank_browser.py, research/verify_concept_animations.py, research/qa_animations_browser.py when model data change, and research/check_site_en.py. Native MathML retains STIX Two Math; prose, headings and code retain the accepted fonts. Preserve study-progress data and all private cached original PDFs.

Publish the exact pushed source to the existing owner-private Site and mirror only changed paths to GitHub branch study-planner-1406. Preserve unrelated mirror deletions. No other chapter is delivered or started in this turn.
"""
with (ROOT/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8') as f:f.write(text)
print('Rank draft handed off; 26 approvals preserved and next chapter gated.')
