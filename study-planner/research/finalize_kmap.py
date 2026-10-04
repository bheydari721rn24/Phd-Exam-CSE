"""Deliver only the verified current draft and preserve the explicit approval gate."""
from pathlib import Path
import json,shutil
from markdown_it import MarkdownIt
B=Path(__file__).resolve().parent;R=B.parent
v=json.loads((B/'g_kmap-validation.json').read_text());b=json.loads((B/'g_kmap-browser-review.json').read_text());a=json.loads((B/'animation-browser-audit.json').read_text())
assert v['status']=='passed' and b['state']=='passed' and v['preservedPriorEntries']==1581
pub=R/'dist/evidence/g_kmap';pub.mkdir(parents=True,exist_ok=True)
shutil.copy2(B/'g_kmap-validation.json',pub/'validation.json')
for path in Path(b['screenshots']).glob('g_kmap-*.png'):shutil.copy2(path,pub/path.name)
record=dict(b);record['screenshots']='Saved beside this evidence record.';(pub/'browser.json').write_text(json.dumps(record,indent=2)+'\n')
quality='''# Logic minimization: quality and verification audit

## Delivered scope

This English review draft combines five actually read university courses, with documented selection from a bounded nine-university discovery pool. It includes ten detailed lesson examples, 84 fully solved problems (81 independently authored/course-inspired and three authentic archive revisits), 80 full review rules, seven original SVG diagrams, fourteen exact concept models with 51 checkpoints, and an adjustable four-variable SOP/POS exact-cover lab. Source URLs, instructors, reading ranges, acquisition hashes and corrections are documented separately. No original course PDFs or figures are redistributed.

## Observed independent verification

Independent verification passed 2,472 checks. The reference model enumerates cubes using bit masks separately from the authoring implementation, compares every authored exact-cover result with iterative QM and Petrick, exhausts all 256 three-input Boolean functions and all 81 two-input incomplete contracts, and verifies explicit algebraic identities and threshold families through six inputs. It checks all fourteen animations against exact snapshot semantics and preserves the mathematical token sequence when long formulas are reflowed. All three original examination PDF fingerprints match their pinned archive provenance.

The archive revisit corrects the shortened earlier transcription of MSc CE 1405 Q78 option 4: the original has five terms. The new tutorial explains why that option violates zero row 4 and why a minimum-literal result protecting O-to-O transitions is not automatically hazard-free on its entire selected DC completion. Independent checks expose the new edge (1,5), validate a consensus repair and validate the alternative zero-DC completion. Earlier approved question banks are preserved; the correction is explicitly documented in this chapter.

## Observed browser verification

The browser independently checked 530 exact laboratory inputs, including 18 rendered cases and nine rejected-input cases. All optimum candidate sets, costs, tied covers and animated checkpoint unions match the separate Python model. Playback, previous/next, reset, seeking, enlargement and reduced-motion behavior passed; actual moving-token positions were checked. All seven figures have no clipped or overlapping labels. All 84 solutions open for printing and restore their previous states afterward. Desktop, 390-pixel mobile and print contain the formulas and figures without page-width overflow. Source Sans 3, Newsreader, STIX Two Math and JetBrains Mono load in their respective roles; no link underline appears.

The final library animation review rendered 192 models across 30 chapters with zero label-layout findings. All 29 approved chapters and their 1,581 existing question entries are preserved. The library now contains 1,665 question entries and 1,139 animation checkpoints.

## Limits and approval

The lesson’s exact cost is lexicographic (terms/factors, then literal occurrences), not arbitrary technology-mapping cost. The functional laboratory does not certify hazards; hazard proofs separately state the allowed transition set, two-level structure and delay assumptions. Difficulty labels are author judgments, not observed score calibration. Course completeness worldwide, absolute scientific perfection and performance on every conceivable unseen question are not guaranteed by finite checks. The current chapter remains a draft and awaits explicit user approval before the next chapter is started.
'''
(B/'g_kmap-quality-audit.md').write_text(quality,encoding='utf-8')
for name,source in [('quality',quality),('sources',(B/'g_kmap-source-audit.md').read_text(encoding='utf-8'))]:
 body=MarkdownIt('commonmark').render(source)
 (R/f'dist/reviews/g_kmap-{name}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Logic minimization audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/g_kmap.html">← Logic minimization chapter</a></p><article class="lesson">'+body+'</article></main></body></html>',encoding='utf-8')
gate=json.loads((B/'chapter-gate.json').read_text());gate.update(state='awaiting_user_approval',currentTopicId='g_kmap',nextTopicId=None,proposedNextTopicId='g_combin',approvedTopicId='p_arrays',activeWork='Logic minimization is delivered as a verified review draft. Await explicit user approval before authoring another chapter.',lastCompletedReview='g_kmap: five genuinely reviewed written courses, 84 fully solved problems including three authentic revisits, 80 full rules, seven diagrams, fourteen animations with 51 checkpoints and an exact SOP/POS laboratory. Independent verification passed 2,472 checks; browser checks passed 530 lab cases, nine rejected cases, desktop/mobile/print and genuine motion. All 29 approved chapters and 1,581 earlier entries are preserved.',nextReview='After explicit approval, follow Week 2 order to g_combin. No other chapter may start while awaiting approval.')
(B/'chapter-gate.json').write_text(json.dumps(gate,indent=2)+'\n')
handoff='''
## Current authoritative handoff — logic minimization

4 October 2026: The user approved p_arrays in Site version 64 and authorized one next chapter. All 29 earlier chapters and their animations remain approved; previous pending statements above are historical.

The sole new draft is g_kmap, Week 2 Digital Logic, at dist/chapters/g_kmap.html. Five genuinely read written courses from MIT, Cambridge, Stanford, Cornell and Columbia are synthesized; four complementary primary sources plus Columbia for exact covering. The bounded discovery pool has nine university candidates. Exact reading, source hashes, course attribution and source corrections are in research/g_kmap-source-audit.md and dist/evidence/g_kmap/sources.json. No worldwide exhaustive-course claim is made.

The full English lesson includes canonical polarity, indexing, cubes, Gray maps, SOP/POS, DC contracts, primes, essential witnesses, cyclic charts, weighted dominance, Petrick, QM completeness, hazard edges, delay traces and multi-output sharing. There are ten detailed lesson examples, 84 fully solved tasks, 80 full rules, seven original figures, fourteen animations with 51 checkpoints and an exact four-input editable lab. Three authentic MSc/PhD questions are verified revisits, not new unique archive items. Q78 option 4’s original fifth term is corrected in this revisit, and its DC transition contract is audited explicitly. Earlier approved banks remain unchanged.

Independent verification passed 2,472 checks, including all 256 three-input functions, all 81 two-input incomplete contracts, bit-mask/QM/Petrick agreement, DC edge counterexample/repairs, formula-token preservation and original PDF fingerprints. Browser checks passed 530 exact lab inputs, nine invalid inputs, controls, real token motion, reduced motion, seven figure layouts, all 84 printable solutions and desktop/mobile/print formulas. Library animation QA passed 192 models across 30 chapters with no label-layout issues. The library has 1,665 question entries and 1,139 checkpoints. Finite checks do not guarantee every unseen examination answer.

The gate is awaiting_user_approval; proposed next topic is g_combin, following Week 2 order. Keep g_kmap a draft until explicit approval. Do not start another chapter or quiz the user before initial study. Preserve all prior content, study-progress data and private original PDFs.

Rebuild using research/author_kmap_problems.py, research/kmap_sources_record.py and research/build_kmap_chapter.py; the renderer imports research/kmap_math_layout.py for scope-preserving list/factor reflow. Verify with research/verify_g_kmap_en.py, research/qa_kmap_browser.py, research/verify_concept_animations.py, research/qa_animations_browser.py when scenario data change, and research/check_site_en.py. After observed verification, research/finalize_kmap.py publishes evidence and locks the gate. Push the exact source state to the existing owner-private Site and mirror only changed files to GitHub branch study-planner-1406, preserving unrelated mirror deletions.
'''
p=R/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf-8')
if '## Current authoritative handoff — logic minimization' not in s:p.write_text(s+handoff,encoding='utf-8')
print('Verified logic-minimization draft finalized; explicit approval gate is closed.')
