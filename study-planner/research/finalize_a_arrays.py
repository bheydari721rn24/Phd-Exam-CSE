from pathlib import Path
import json,hashlib,shutil
B=Path(__file__).resolve().parent;R=B.parent
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,a):p.write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
v=read(B/'a_arrays-verification.json');b=read(B/'a_arrays-browser-audit.json');models=read(R/'dist/chapters/a_arrays-models.json')
assert v['state']==b['state']=='passed' and v['retainedChapters']==34 and v['retainedQuestions']==1999
assert b['counts']['questions']==86 and b['counts']['rules']==80 and b['counts']['models']==20
assert len(b['labReferenceChecks'])==466 and all(z['ok'] for z in b['labReferenceChecks'])
assert not b['errors'] and all(b['invalidInputs']) and all(b['invalidForm'].values())
assert b['realMotion']>0 and b['reducedMotionAnimations']==0 and b['print']['checkpoints']==113
quality=f'''# Arrays and Linked Lists: observed quality audit

## Delivery state

Complete English review draft, awaiting explicit student approval. Only this new chapter was authored. The user's approval of the preceding pigeonhole chapter is recorded; the subsequent stacks and queues chapter has not been started.

## Scientific and source scope

Four primary written courses from MIT, Berkeley, Oxford, and Princeton were actually reviewed in the scopes stated in the source audit. Stanford is a fully reviewed complementary handout and selected Cornell sections are a sixth complementary source. This is a documented seven-university candidate comparison, not an exhaustive worldwide review. CMU's inaccessible handout is excluded from instructional-reading counts.

The lesson has 18 substantial sections, complete proofs of stable shifts, geometric growth and quarter-shrink amortization, heap invariants, Floyd meeting and entry, exact counting examples, and workload/memory distinctions. It contains 84 original or independently reconstructed course problems plus two source-checked archive items and 80 actionable examination rules. The MS item is a labeled revisit, not a new unique archive question. PhD Q18's suitability answer is independently justified, not represented as an official key.

## Independent numerical and structural checks

The verifier passed {v['checks']:,} finite assertions. It simulated insertion/deletion content and write counts, reversal region invariants, cycle detection and entry across 1,230 prefix/cycle combinations, geometric growth across 1,152 parameter cases, and all 8,192 thirteen-update bit sequences under the safe contraction policy. Invalid delete-from-empty transitions were skipped. Thirty explicitly annotated numerical bank items were compared with independent references; other worked numerical and conceptual derivations were manually reasoned, not falsely labeled machine-proved.

The verifier confirms that all 34 earlier approved chapter bodies and their 1,999 question entries are retained. The sole permitted earlier HTML change records approval in the pigeonhole header. Both authentic source PDFs have checked SHA-256 fingerprints. Native MathML is structurally parsed; equations retain complete single-line groups with horizontal access on narrow screens, while the potential's genuine two-row cases remain a semantic table.

## Actual browser observations

Edge rendered all 20 concept models and all 113 checkpoints. Bounds and pairwise text overlap measurements passed after correcting the merge-row spacing. Screenshot inspection exposed literal spacing escapes in model formulas; these were corrected, as were null cursor labels. The corrected splice and reversal screenshots were inspected again. The physical slot shifts, two-buffer relocation, doubly linked arrows, cycle cursors, and orthogonal matrix schematic have separate geometry; a generic concept trace is not substituted for them.

All 466 browser laboratory references agree with independent Python results. The growth, insertion, reversal, and Floyd forms were exercised. Five invalid numerical inputs and an empty comma field were rejected; invalid form input retains the last valid trace. Forward/backward steps, restart, seek, play/pause, and actual moving entities passed. Source Sans 3, Newsreader, STIX Two Math, and JetBrains Mono loaded. The browser contains {b['counts']['math']} native math instances including complete printable traces and the active editable example.

At 390 pixels, document and body widths were 375 pixels. No underlined links or uncontained inline mathematics were observed; wide diagrams pan internally. Reduced-motion mode created zero animations. Print opens every solution and displays all 113 fixed-model checkpoints, hides controls, and restores prior solution states afterward. The application Library reaches the new draft. No runtime/resource errors were observed.

## Limits and unresolved assumptions

Finite checks support, and do not replace, general proofs. Word-sized slot copies, exclusive access, separate-buffer peak allocation, exact power-of-two shrink thresholds, and acyclic-list ownership contracts are explicit. No official answer key was available for the two archive items. The source comparison has an accessibility boundary and does not establish worldwide course completeness. Literal 100% scientific certainty or guaranteed future examination performance cannot be demonstrated.

## Evidence

[Mathematical verification](../evidence/a_arrays/verification.json), [browser verification](../evidence/a_arrays/browser.json), [reviewed source scopes](../evidence/a_arrays/courses.json), [model contracts](../evidence/a_arrays/models.json), and the [source-selection audit](a_arrays-sources.html) are retained with the chapter.
'''
(B/'a_arrays-quality-audit.md').write_text(quality,encoding='utf-8')
audit=dict(topicId='a_arrays',state='passed',placements=20,checkpoints=113,editableLaboratories=4,conceptGroups=models['groups'],models=[dict(id=m['id'],kind=m['kind'],invariant=m['invariant'],assumptions=m['assumptions'],checkpoints=len(m['frames'])) for m in models['models']],verificationPath='research/a_arrays-verification.json',browserAuditPath='research/a_arrays-browser-audit.json',limitations='Finite diagrams illustrate the separately written general proofs; comparison and allocation models are explicitly bounded.')
write(B/'a_arrays-model-audit.json',audit)
p=B/'animation-manifest.json';a=read(p)
for c in a['chapters']:
 if c['topicId']=='d_pigeonhole':c['visualRevisionState']='student_approved';c['htmlSha256']=hashlib.sha256((R/'dist/chapters/d_pigeonhole.html').read_bytes()).hexdigest()
a['chapters']=[c for c in a['chapters'] if c['topicId']!='a_arrays']
a['chapters'].append(dict(topicId='a_arrays',placements=20,scenarios=20,sections=models['groups'],questionCount=86,htmlSha256=hashlib.sha256((R/'dist/chapters/a_arrays.html').read_bytes()).hexdigest(),visualRevisionState='awaiting_user_approval',renderer='Array slots, heap links, two-buffer movement, cycle cursors and orthogonal matrix adjacency; four editable exact laboratories',dataUrl='chapters/a_arrays-models.json',modelAuditPath='research/a_arrays-model-audit.json',browserAuditPath='research/a_arrays-browser-audit.json'))
a.update(state='34_approved_chapters_and_one_arrays_review_draft',uniqueScenarios=272,checkpoints=1534,placements=235,scope='252 preceding approved scenarios and 20 new arrays/list draft models. Prior bodies are preserved.',arraysValidationAssertions=v['checks'],checkpointsPrint='The new arrays/list player prints all 113 fixed-model checkpoints plus the currently computed editable trace.')
assert len(a['chapters'])==35 and sum(c['questionCount'] for c in a['chapters'])==2085;write(p,a)
p=R/'dist/index.html';s=p.read_text();s=s.replace('All 33 earlier chapters are student-approved. The new pigeonhole chapter is ready for your review.','All 34 earlier chapters are student-approved. The new arrays and linked lists chapter is ready for your review.');p.write_text(s,encoding='utf-8')
p=R/'dist/animation-review.html';s=p.read_text();s=s.replace('33 approved chapters and 1 pigeonhole review draft · 252 distinct scenarios · 1421 exact checkpoints · 215 embedded walkthroughs.','34 approved chapters and 1 arrays/list review draft · 272 distinct scenarios · 1534 exact checkpoints · 235 embedded walkthroughs.').replace('Pigeonhole chapter: separate review draft','Pigeonhole chapter: student-approved').replace('This chapter awaits explicit student approval.','The pigeonhole chapter has been explicitly approved by the student.').replace('animated teaching in 33 existing chapters','animated teaching in 34 existing chapters')
if '<!-- ARRAYS REVIEW -->' not in s:s=s.replace('<h2>Approval</h2>','<!-- ARRAYS REVIEW --><h2>Arrays and linked lists: separate review draft</h2><p><a href="chapters/a_arrays.html">Open the new chapter with 20 specific models and four editable laboratories.</a> Its 113 checkpoints show slots, resize buffers, sentinel links, reversal, cycle cursors and row/column matrix adjacency. The chapter awaits explicit approval. <a href="reviews/a_arrays-quality.html">Read observed verification.</a></p><h2>Approval</h2>')
p.write_text(s,encoding='utf-8')
out=R/'dist/evidence/a_arrays';out.mkdir(exist_ok=True)
for source,name in [('a_arrays-verification.json','verification.json'),('a_arrays-browser-audit.json','browser.json'),('a_arrays-model-audit.json','models.json'),('a_arrays-reading.json','courses.json')]:shutil.copy2(B/source,out/name)
p=B/'chapter-gate.json';g=read(p);g.update(currentTopicId='a_arrays',state='awaiting_user_approval',approvedTopicId='d_pigeonhole',nextTopicId='a_stackqueue',proposedNextTopicId='a_stackqueue',nextTopicRequiresExplicitApproval=True,sourceAuditPath='research/a_arrays-source-audit.md',sourceAudit='research/a_arrays-source-audit.md',qualityAuditPath='research/a_arrays-quality-audit.md',qualityAudit='research/a_arrays-quality-audit.md',activeWork='Delivered only arrays and linked lists: 86 solved tasks, 80 examination rules, 20 models, 113 checkpoints and four editable laboratories.',reviewScope='Only a_arrays; 34 earlier chapters approved.',lastCompletedReview=f'a_arrays: {v["checks"]} mathematical assertions, 466 browser references, all 113 checkpoints, desktop/mobile/fonts/real motion/print passed.',nextReview='Wait for explicit approval of a_arrays. Do not start a_stackqueue or another chapter.',reviewEvidence=['research/a_arrays-verification.json','research/a_arrays-browser-audit.json','research/a_arrays-model-audit.json']);write(p,g)
p=R/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf-8');heading='## Current delivery: arrays and linked lists, October 5, 2026'
if heading not in s:s+='\n\n'+heading+f'''\n\nThe user explicitly approved d_pigeonhole. Only a_arrays was authored. It is a complete review draft awaiting explicit approval; a_stackqueue has not been started. Four primary courses from MIT, Berkeley, Oxford and Princeton plus Stanford and selected Cornell material were genuinely reviewed. The source audit bounds the candidate pool and records inaccessible CMU material without pretending it was read.
\nThe chapter contains 86 solved problems, 80 examination rules, 20 concept-specific models, 113 checkpoints and four editable laboratories. Two archive questions were checked against original PDF pages; the MS item is a labeled revisit and neither answer is represented as an official key. The mathematical audit passed {v['checks']:,} finite assertions and browser labs passed 466 independent references. All 34 preceding chapters and 1,999 questions are retained. The library totals 35 chapters and 2,085 question entries. Single-line math repairs are retained throughout the prior library.
\nThe local draft and source/quality audits are complete. Publication state must be verified separately; source pushes and a GitHub mirror are not proof of live Site deployment. Native Sites connectivity was intermittently unavailable during this turn.\n'''
p.write_text(s,encoding='utf-8');print('Finalized sole draft and approval gate; publication remains separately verified.')
