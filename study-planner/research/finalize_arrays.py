"""Record verified delivery and close the one-chapter approval gate."""
import json,shutil
from pathlib import Path
B=Path(__file__).resolve().parent;R=B.parent
v=json.loads((B/'p_arrays-validation.json').read_text());b=json.loads((B/'p_arrays-browser-review.json').read_text());a=json.loads((B/'animation-browser-audit.json').read_text())
assert v['state']==b['state']=='passed' and v['approvedQuestionsPreserved']==1498
assert len(a['chapters'])==29 and len(a['scenarios'])==178 and not a['layoutIssues']
from preserve_library_approval import preserve_approval
preserve_approval()
scenes=json.loads((R/'dist/chapters/concept-animations.json').read_text())['scenes'];assert len(scenes)==178 and sum(len(s['frames']) for s in scenes.values())==1088
gate=json.loads((B/'chapter-gate.json').read_text());gate.update(state='awaiting_user_approval',currentTopicId='p_arrays',nextTopicId=None,proposedNextTopicId='g_kmap',approvedTopicId='p_functions',activeWork='Arrays and Indexing is delivered as a review draft. Await explicit approval before writing the next chapter.',lastCompletedReview='p_arrays: six genuinely reviewed university courses, 83 fully solved problems (81 original/course-inspired, two authentic bridge revisits), 80 complete rules, seven figures, eighteen exact animations with 114 checkpoints and a six-model adjustable lab. Independent checks and desktop/mobile/print/motion reviews passed. All 28 approved chapters and 1,498 earlier question entries are preserved.',nextReview='After explicit approval, follow Week 2 order to g_kmap. Do not author another chapter while awaiting approval.')
(B/'chapter-gate.json').write_text(json.dumps(gate,indent=2)+'\n')
pub=R/'dist/evidence/p_arrays'
for path in Path(b['screenshots']).glob('p_arrays-*.png'):shutil.copy2(path,pub/path.name)
record=dict(b);record['screenshots']='Chapter screenshots are saved beside this record.';(pub/'browser.json').write_text(json.dumps(record,indent=2)+'\n')
quality=B/'p_arrays-quality-audit.md';s=quality.read_text(encoding='utf-8');s=s.split('\n## Final observed verification')[0]
s+='''
## Final observed verification

Independent verification passed 5,922 checks, including ten actual Python question executions, exhaustive legal overlap segments for arrays of sizes zero through eight, inverse layouts through eleven rows/columns, growth and exact animation-state checks, original examination PDF fingerprints and preservation of all 1,498 earlier approved question entries. All 18 new concept models and 114 checkpoints were checked against independent semantic relations. The six-model adjustable laboratory passed 540 accepted input cases and eleven rejected-input cases; every saved state, controls and genuine token motion were checked.

Browser review passed desktop, 390-pixel mobile and print checks. All seven original figures have no clipped or overlapping labels. All 83 solutions open for printing and restore their prior open state afterward. Source Sans 3, Newsreader, STIX Two Math and JetBrains Mono are loaded in their respective roles. There is no page-width overflow or link underline. The final library animation review rendered all 178 models across 29 chapters without label-layout findings. C cases use explicit language rules and independent models; no local compiler is available, so compiled execution is not claimed. Finite checks do not guarantee correctness for every conceivable input or performance on unseen questions.
'''
quality.write_text(s,encoding='utf-8')
from markdown_it import MarkdownIt
audit=MarkdownIt('commonmark').render(s)
(R/'dist/reviews/p_arrays-quality.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Arrays chapter audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/p_arrays.html">← Arrays chapter</a></p><article class="lesson">'+audit+'</article></main></body></html>',encoding='utf-8')
handoff='''
## Current authoritative handoff — arrays and indexing

4 October 2026: The user approved p_functions in Site version 63 and authorized one next chapter. All 28 earlier chapters and their animations are approved; earlier pending statements above are historical.

The sole new draft is p_arrays, Week 2 Programming Fundamentals, at dist/chapters/p_arrays.html. Four primary written courses from Cambridge, CMU, Harvard and UC Berkeley are synthesized with Stanford and MIT as two genuinely read complementary sources. Exact reading ranges, bounded eight-university candidate evaluation, source corrections and question provenance are recorded in research/p_arrays-source-audit.md, research/p_arrays-reviewed-courses.json and dist/evidence/p_arrays/sources.json. No worldwide exhaustive-course claim is made.

The detailed English lesson covers array objects and bounds, layouts and inverses, C pointer domains, traversals and proof obligations, prefix/difference tables, overlap and mutation order, Python sharing/slices, strings, capacity and packed storage. It includes complete overlap-safe C element-moving and segment-reversal implementations. There are 83 worked mathematical/conceptual tasks, 80 complete examination rules, seven SVG figures, eighteen animations with 114 checkpoints and a six-model adjustable lab. MSc CS 1393 Q167 and PhD CS 1404 Q72 are verified authentic bridge revisits, not new unique archive items. The library now has 29 chapters, 1,581 question entries, 178 animation models and 1,088 checkpoints.

Independent verification passed 5,922 checks and ten actual Python question executions. All 1,498 previously approved question entries were preserved. Browser checks passed all seven figure layouts, all 83 printable solutions, dedicated prose/heading/math/code fonts, 390-pixel mobile containment, 540 valid laboratory cases, eleven invalid cases, exact transitions, controls, enlargement and actual motion. The final library animation audit passed 178 models across 29 chapters with zero label-layout findings. No local C/C++ compiler is available; C cases have written language-rule reasoning and independent models. Finite checks do not guarantee performance on every unseen examination question.

The gate is awaiting_user_approval with proposed next topic g_kmap (Minterms, maxterms, and simplification), following Week 2 order. p_arrays stays a draft until explicit approval; do not start another chapter or quiz the user before study.

Rebuild with research/author_arrays_problems.py, research/arrays_sources_record.py and research/build_arrays_chapter.py. Verify with research/verify_p_arrays_en.py, research/qa_arrays_browser.py, research/verify_concept_animations.py, research/qa_animations_browser.py when model data change, and research/check_site_en.py. Preserve all approved content, progress and private original PDFs. Publish exact pushed source to the owner-private existing Site and mirror only changed paths to GitHub branch study-planner-1406, preserving unrelated mirror changes.
'''
p=R/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf-8')
if '## Current authoritative handoff — arrays and indexing' not in s:p.write_text(s+handoff,encoding='utf-8')
print('Arrays draft delivered; gate awaits approval; previous 28 approvals preserved.')
