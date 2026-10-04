from pathlib import Path
import json,shutil
from markdown_it import MarkdownIt
B=Path(__file__).resolve().parent;R=B.parent
v=json.loads((B/'g_combin-validation.json').read_text());b=json.loads((B/'g_combin-browser-review.json').read_text());a=json.loads((B/'animation-browser-audit.json').read_text());manifest=json.loads((B/'animation-manifest.json').read_text())
assert v['status']=='passed' and b['state']=='passed' and v['preservedPriorEntries']==1665
assert len(a['scenarios'])==206 and not a['layoutIssues']
pub=R/'dist/evidence/g_combin';pub.mkdir(parents=True,exist_ok=True)
shutil.copy2(B/'g_combin-validation.json',pub/'validation.json')
for p in Path(b['screenshots']).glob('g_combin-*.png'):shutil.copy2(p,pub/p.name)
record=dict(b);record['screenshots']='Saved beside this evidence record.';(pub/'browser.json').write_text(json.dumps(record,indent=2)+'\n')
quality=f'''# Combinational circuit design: quality and verification audit

## Delivered scope

The sole new English draft combines five actually reviewed written courses from MIT, Stanford, Cambridge, Cornell and Berkeley. Selection is documented against a bounded nine-university discovery pool, with exact reading ranges, source hashes, course attribution and reconciled conventions. The lesson has twelve detailed worked examples plus three integrated cases; the separate bank contains 82 complete solutions, comprising 80 original/course-inspired mathematical and conceptual problems and two authentic archive revisits. There are 80 full examination rules, eight original SVG figures, fourteen animations with 72 exact checkpoints and a three-mode adjustable laboratory.

The core lesson contains approximately 5,000 words before the separate problem bank and review rules. Its purpose is a complete specification-to-circuit argument, rather than repetition of the previous minimization chapter. The examples distinguish single/multiple outputs, legal-input relations, DAG uniqueness, sharing, fan-in, polarity mapping, cofactor construction, HDL completeness, independent miters, fault activation/propagation and conservative timing bounds.

## Observed scientific verification

Independent verification passed {v['checks']:,} checks. Original cofactors are verified on every truth row. Separate predicate specifications check all ten multi-output designs; Sympy evaluates all twelve reference/candidate miter pairs. The verifier exhausts all 256 three-input functions, each of three residual-variable choices, and all eight rows. It verifies word arithmetic, tree depth bounds, fault detecting sets, the complete optimal two-test cover, controller invariants and the seven-input factoring identity. All fourteen animation models are independently checked at all 72 snapshots. Native MathML token order is preserved during responsive reflow, including list fences and trailing punctuation.

The two original examination PDF fingerprints match the pinned archive. PhD CE 1405 Q23 is visually checked on PDF page 6 and MSc CE 1404 Q80 on page 19. Their equations transcribe the original connected diagrams. These are bridge revisits of previously included questions, not newly unique archive entries; their independently derived answers are not advertised as official keys.

All 30 approved chapters and their 1,665 prior question entries are preserved exactly. The library now has 31 chapters and 1,747 question entries.

## Observed browser verification

The exact laboratory passed 96 independent input/mode/variant comparisons, six rendered mode variants and four rejected malformed calls. Current input values, reference output order, deliberately faulty candidate discrepancies and complete sixteen-row tables are explicit. Declared reference gate counts are four for the shared circuit, six for the priority controller and three for the NAND circuit; maximum depths are three, three and two. The lab does not include physical loading or fan-out buffers.

Playback, backward movement, seek, reset, enlargement and reduced motion passed. An intermediate moving-token sample confirms real motion rather than a color-only substitution. All eight SVG figures have zero clipped or overlapping label findings. Directional connections have arrowheads; math labels use STIX Two Math. All 82 solutions open for printing and restore their previous states afterward. Desktop, 390-pixel mobile and print pass formula and diagram containment. A long inline archive commit initially caused mobile overflow; scoped inline-code wrapping removes it. Long mathematical lists retain their enclosing scope, and punctuation stays attached to its expression. Source Sans 3, Newsreader, STIX Two Math and JetBrains Mono load in their respective roles; links have no underline.

The library animation review passed all 206 models across 31 chapters with zero layout findings. The library has {manifest['checkpoints']:,} checkpoints. Evidence screenshots are saved with the chapter.

## Limits and approval

No HDL compiler is available in this environment, so code examples are checked against explicit independent mathematical contracts and are not claimed to have been compiled. Boolean truth-row checks and timing bounds are not electrical simulation, analog settling certification or hazard-free waveform proofs. Structural false paths, four-state unknowns, memory interfaces and technology costs are qualified explicitly. The selected accessible course pool is bounded; no worldwide exhaustive-course review or literal absolute correctness claim is made. Difficulty labels are author judgments, not measured examination calibration. Finite verification cannot guarantee performance on every conceivable unseen question.

The chapter remains a draft awaiting explicit approval. The proposed next topic, after approval, is d_counting in Week 3. No next chapter is started in this delivery.
'''
(B/'g_combin-quality-audit.md').write_text(quality,encoding='utf-8')
for name,source in [('quality',quality),('sources',(B/'g_combin-source-audit.md').read_text(encoding='utf-8'))]:
 body=MarkdownIt('commonmark').render(source)
 (R/f'dist/reviews/g_combin-{name}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Combinational circuit design audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/g_combin.html">← Combinational circuit design</a></p><article class="lesson">'+body+'</article></main></body></html>',encoding='utf-8')
gate=json.loads((B/'chapter-gate.json').read_text());gate.update(state='awaiting_user_approval',currentTopicId='g_combin',approvedTopicId='g_kmap',nextTopicId=None,proposedNextTopicId='d_counting',activeWork='Combinational Circuit Design is delivered as a verified review draft. Await explicit approval before starting another chapter.',lastCompletedReview=f'g_combin: five reviewed university courses, 82 fully solved problems, 80 rules, eight diagrams, fourteen models / 72 checkpoints and a three-mode verification lab. Independent checks: {v["checks"]:,}. Browser: 96 input comparisons; all 30 earlier chapters and 1,665 entries preserved.',nextReview='After explicit approval, follow Week 3 order to d_counting. Do not begin it while awaiting approval.')
(B/'chapter-gate.json').write_text(json.dumps(gate,indent=2)+'\n')
handoff=f'''
## Current authoritative handoff — combinational circuit design

4 October 2026: The user approved g_kmap in Site version 65 and authorized only the next chapter. g_kmap approval is recorded in both ledgers; there are now 30 approved earlier chapters. Previous pending statements above are historical.

The sole new draft is g_combin, Week 2 Digital Logic, at dist/chapters/g_combin.html. Five written courses from MIT, Stanford, Cambridge, Cornell and Berkeley are genuinely read within exact recorded ranges. The bounded discovery pool contains nine university candidates. Source attribution, cached document fingerprints, reading ranges, selection rationale and source corrections are in research/g_combin-source-audit.md and dist/evidence/g_combin/sources.json. The original course PDFs remain private. No worldwide exhaustive claim is made.

The full English lesson covers complete and relational contracts, DAG closure/uniqueness, internal nets, multilevel sharing, fan-in and arrival-sensitive trees, Shannon cofactors, decoder/ROM construction, NAND/NOR polarity, widths, complete combinational HDL, equivalence miters, stuck-at testing, timing extrema and false paths. It contains twelve detailed examples and three integrated cases, 82 solved tasks (80 original/course-inspired; two authentic verified bridge revisits), 80 complete rules, eight original figures, fourteen animations / 72 checkpoints and a three-mode editable lab. All 30 earlier approved banks and 1,665 entries remain unchanged.

Independent verification passed {v['checks']:,} checks. Browser checks passed 96 exact mode/input/variant comparisons, six rendered variants, four malformed-call rejections, genuine token motion, controls, reduced motion, all eight figure layouts, all 82 printable solutions, fonts and 390-pixel mobile/print containment. Library animation review passed 206 models with no label findings. The library now has 31 chapters, 1,747 entries and 1,211 checkpoints. Code is model-verified, not claimed compiled; finite Boolean checks do not certify analog behavior or every unseen examination question.

The gate is awaiting_user_approval. Proposed next topic is d_counting, following Week 3 schedule order. Keep g_combin a draft until explicit approval; do not start the next chapter or quiz the user before initial study.

Rebuild with research/author_combin_problems.py, research/combin_sources_record.py, research/prepare_combin_build.py, research/build_combin_chapter.py. The renderer imports research/combin_math_layout.py, which preserves scopes and attaches punctuation. Verify with research/verify_g_combin_en.py and research/qa_combin_browser.py; run the global animation checks when model data change. After observed verification, research/finalize_combin.py publishes evidence and closes the gate. Publish the exact pushed source to the existing owner-private Site and mirror only changed files to GitHub branch study-planner-1406, preserving unrelated deletions in that mirror.
'''
p=R/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf-8')
if '## Current authoritative handoff — combinational circuit design' not in s:p.write_text(s+handoff,encoding='utf-8')
print('Verified combinational-design draft finalized; explicit approval gate closed.')
