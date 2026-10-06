"""Publishable inventory and independent preservation check for the library revision."""
import json,re,hashlib,subprocess,html
from pathlib import Path
R=Path(__file__).resolve().parents[1]; A=R/'research/library-animation-redesign'; D=R/'dist/chapters'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(x):return hashlib.sha256(x.encode()).hexdigest()
def content(x):
 x=re.search(r'<body\b[^>]*>(.*?)</body>',x,re.S|re.I).group(1)
 return re.sub(r'<script\b[^>]*>.*?</script>','',x,flags=re.S|re.I)
def strip_metadata(x):
 if isinstance(x,dict):return {k:strip_metadata(v) for k,v in x.items() if k not in ['teaching','teachingPolicy']}
 if isinstance(x,list):return [strip_metadata(v) for v in x]
 return x
inventory=read(A/'inventory.json');baseline=inventory['baselineCommit'];retained=[]
for row in inventory['chapters']:
 topic=row['topicId'];old=(A/'baseline'/f'{topic}.html').read_text(encoding='utf-8');new=(D/f'{topic}.html').read_text(encoding='utf-8')
 assert content(old)==content(new),f'Body changed: {topic}'
 retained.append(dict(topicId=topic,bodySha256=digest(content(new)),questions=row['questions'],bodyRetainedExactlyExcludingScriptIncludes=True))
for row in inventory['files']:
 old=json.loads(subprocess.check_output(['git','show',f'{baseline}:dist/chapters/{row["file"]}'],cwd=R));new=read(D/row['file'])
 assert strip_metadata(old)==strip_metadata(new),f'Mathematical payload changed: {row["file"]}'
oldsort=subprocess.check_output(['git','show',f'{baseline}:dist/chapters/a_sort-models.json'],cwd=R)
assert oldsort.decode('utf-8').replace('\r\n','\n')==(D/'a_sort-models.json').read_text(encoding='utf-8')
save(A/'retention.json',dict(state='passed',baselineCommit=baseline,chapterCount=len(retained),questionCount=sum(r['questions'] for r in retained),chapters=retained,mathematicalPayloadsRetained=[r['file'] for r in inventory['files']],approvedSortingModelsRetainedAfterWindowsNewlineNormalization=True))
qa=read(A/'browser.json');assert qa['state']=='passed',qa['state'];assert len(qa['chapters'])==37
assert all(not c['errors'] and not c['mobileOverflow'] and not c['failed'] for c in qa['chapters'])
inventory.update(state='awaiting_user_approval',questionCount=sum(r['questions'] for r in retained),reviewedModels=sum(r['models'] for r in inventory['files']),reviewedCheckpoints=sum(r['frames'] for r in inventory['files']),approvedSortingModels=45,approvedSortingCheckpoints=1194,browserAuditPath='research/library-animation-redesign/browser.json',retentionAuditPath='research/library-animation-redesign/retention.json')
inventory['additionalControlsAuditPath']='research/library-animation-redesign/controls-browser.json'
save(A/'inventory.json',inventory)
lessons=read(R/'dist/lessons.json');lookup={c['topicId']:c for w in lessons for c in w.get('chapters',[])}
for row in inventory['chapters']:
 c=lookup[row['topicId']];c['libraryDecisionRevisionState']='awaiting_user_approval'
 if row['topicId']=='a_sort':c.update(status='ready',statusLabel='Student-approved chapter',revisionState='student_approved',approvedVersion=72,animationReviewState='student_approved',visualRevisionState='student_approved')
save(R/'dist/lessons.json',lessons)
manifest=read(R/'research/animation-manifest.json');manifest.update(decisionLedReviewPath='research/library-animation-redesign/inventory.json',currentLibraryChapterCount=37,currentLibraryRevisionState='awaiting_user_approval');save(R/'research/animation-manifest.json',manifest)
gate=read(R/'research/chapter-gate.json');gate.update(state='awaiting_user_approval',approvedTopicId='a_sort',approvedVersion=72,reviewScope='Animation redesign across all 37 existing chapters, including worked-solution aids. No new chapter.',activeWork='Whole-library decision-led animation redesign completed; publication verification pending. Await explicit user approval of this revision before a new chapter.',lastCompletedReview='37 existing chapters; 730 redesigned stored models and 4002 checkpoints, plus 45 approved sorting models and 1194 checkpoints. All 2257 question bodies retained.',nextReview='Review the whole-library animation revision; do not start a new chapter.',animationInventoryPath='research/library-animation-redesign/inventory.json',animationBrowserAuditPath='research/library-animation-redesign/browser.json',publicationState='pending',publicationRecordPath='research/library-animation-redesign/publication.json',reviewEvidence=['research/library-animation-redesign/inventory.json','research/library-animation-redesign/browser.json','research/library-animation-redesign/retention.json','research/library-animation-redesign/live-reference-repairs.json'])
gate['delivery']=dict(date='2026-10-06',status='whole_library_visual_review',chapterCount=37,questionCount=2257,reviewedModels=730,reviewedCheckpoints=4002,previouslyApprovedSortingModels=45,previouslyApprovedSortingCheckpoints=1194,url='animation-review.html')
save(R/'research/chapter-gate.json',gate)
def title(topic):
 return lookup[topic].get('title') or html.unescape(re.sub(r'<[^>]*>','',re.search(r'<h1\b[^>]*>(.*?)</h1>',(D/f'{topic}.html').read_text(encoding='utf-8'),re.S).group(1)))
chapters=''.join(f'<tr><td><a href="chapters/{r["topicId"]}.html">{html.escape(title(r["topicId"]))}</a></td><td>{r["questions"]}</td><td>{r["players"]}</td></tr>' for r in inventory['chapters'])
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Chapter animation review</title><link rel="stylesheet" href="chapters/chapter.en.css"><style>.lesson h1{display:block;font-family:Newsreader,serif;font-size:2.6rem;font-weight:430;line-height:1.15;margin:0 0 22px}a,a:hover,a:focus{text-decoration:none} .review-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px}.review-grid section{padding:20px;border:1px solid #d4e2e4;border-radius:16px;background:#f6faf9}.review-grid h3{margin-top:0}.review-table{overflow:auto} .review-table table{width:100%}td,th{padding:12px;text-align:left}p{max-width:75ch}.review-status{background:#edf5f5;padding:18px;border-radius:14px}</style></head><body><main class="chapter"><p class="top-link"><a href="index.html#library">← Chapter library</a></p><article class="lesson"><h1>Clearer animations across the chapter library</h1><p class="review-status">All 37 existing chapters are included. This library-wide animation revision awaits your review. The previously approved sorting chapter remains approved; no new chapter has been started.</p><p>The revision covers concept walkthroughs and worked-solution visual aids. It preserves every lesson, proof, review rule and the full explanations of all 2,257 questions.</p><h2>What to inspect</h2><div class="review-grid"><section><h3>Decision before movement</h3><p>Read the current operation, its reason and any exact predicate. Use “Before and after” to inspect the recorded state changes.</p></section><section><h3>A model suited to the subject</h3><p>Probability uses retained mass and normalization. Matrices show operand roles and exact arithmetic. Circuits retain gate ports and wire topology. Records move while storage indices stay fixed.</p></section><section><h3>Control every transition</h3><p>Start paused. Step forward or backward, restart, change speed or select a checkpoint. Pause freezes an ongoing movement; Play continues it. Reduced motion displays exact states.</p></section></div><h2>Reading a walkthrough</h2><ol><li>Choose a concept or a boundary case. Read its assumptions and the “How to read this model” section.</li><li>Inspect the current operation and test before selecting Next step.</li><li>Compare the exact before and after states. Indices, values, object identities and counters have distinct roles.</li><li>Use Play after the decision is clear. An animated route depicts construction between exact checkpoints; it does not introduce fractional algorithm states.</li><li>Return to the complete written proof or solution. A finite example illustrates it and does not establish a general theorem.</li></ol><h2>Verified scope</h2><p>730 stored models with 4,002 saved checkpoints received the library revision. The previously approved sorting system contributes another 45 models and 1,194 checkpoints. Stored model totals include distinct scenarios and reused question aids; they are not counts of unique algorithms.</p><p>Browser checks covered all 37 pages, every revised saved checkpoint, visible explanations, exact-test display, diagram bounds, glyph spacing and port attachment. Desktop and mobile checks, pause and resume, checkpoint selection, reduced motion and printable traces passed. The audit found and repaired broken links between three older laboratories and their renamed drawing elements.</p><p>These checks do not constitute a new exhaustive mathematical proof audit of every chapter or an animation of every possible input. Existing mathematical checkpoint data and complete written teaching were independently compared with the approved baseline and retained.</p><h2>Open a chapter</h2><p>The last column counts authored embedded visual placements, including solution aids. A placement can offer several cases; repeated models can appear in more than one placement.</p><div class="review-table"><table><thead><tr><th>Chapter</th><th>Solved questions</th><th>Visual placements</th></tr></thead><tbody>'''+chapters+'''</tbody></table></div></article></main></body></html>'''
(R/'dist/animation-review.html').write_text(page+'\n',encoding='utf-8')
(A/'REVIEW.en.md').write_text('''# Whole-library animation revision — 6 October 2026

The student approved the sorting decision-led design (Site version 72) and explicitly authorized the same teaching clarity across all existing chapters. No new chapter was started.

## Scope and changes

- All 37 existing chapter pages include the new teaching player layer.
- 730 stored models and 4,002 exact checkpoints are annotated with operations, reasons, current state, state differences and subject-specific reading guidance. Where the saved model supports one, the exact predicate and result are derived and independently checked (236 explicit conditions).
- The 45 sorting models and their 1,194 checkpoints retain their approved data and dedicated renderer.
- The renderer repairs complete record identities and fixed slot indices, duplicate truth-table valuations, matrix operand/accumulator labels, event-time visibility, dependency flow on authored circuit wires, true pause/resume, reduced motion and printable checkpoints. Linked structures preserve their declared topology; bodies are not moved away from attached wires.
- Older gate-timing, vector and matrix editable laboratories had stale drawing element identifiers. Their references and the vector arrow marker now target the live elements.
- All 2,257 complete question bodies, written lessons, proofs and review notes are retained exactly, excluding script includes.

## Evidence

- `inventory.json`: per-model operations and per-chapter placements.
- `browser.json`: 730 models, 4,002 states, 37 pages, controls and mobile containment.
- `retention.json`: independent body and mathematical-payload comparisons against 5e43af9577a09e425d09809a9d13449122e04ddb.
- `live-reference-repairs.json`: legacy identifier repairs.
- `publication.json`: added only after source and deployment verification.

The scope is animation instruction and retained-content verification. This is not a fresh exhaustive audit of all course sources or a proof that every possible input or unseen examination question is covered. Saved checkpoints are exact; construction motion is illustrative. The revision stays awaiting student approval before a new chapter.

## Regeneration

Run `review_library_animation_teaching.py` after rebuilding raw model data to restore the reviewed teaching metadata, then re-run the browser and retention gates. Do not restore legacy player code from older baseline-repair scripts. The install/redesign scripts document a one-time migration and are not arbitrary repeatable rebuild commands. `finalize_library_animation_review.py` verifies content retention and produces the user-facing review; run it before publication, not after recording a successful publication.
''',encoding='utf-8')
print(dict(state='passed',chapters=len(retained),questions=sum(r['questions'] for r in retained),models=inventory['reviewedModels'],checkpoints=inventory['reviewedCheckpoints']))
