"""Record a reviewed draft and the subsequent chapter without claiming student approval."""
from pathlib import Path
import json,hashlib,re
B=Path(__file__).resolve().parent;R=B.parent;E=B/'l_linear-evidence'
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
reading=dict(status='completed',coreUniversities=4,universitiesRead=5,screenedUniversities=7,
 courses=[
 dict(university='Oxford',course='M1 Linear Algebra I 2022–23',lecturer='Andrew Wathen',id='oxford',nativePages=list(range(53,68)),method='Full native text read in two untruncated ranges',core=True),
 dict(university='MIT',course='18.06SC Fall2011',lecturer='Gilbert Strang',id='mit-maps',nativePages=[1,2,3,4],method='Full official PDF text read; license page identified',core=True),
 dict(university='MIT',id='mit-problems',nativePages=[1],method='Both official exercise statements read; independently reconstructed',core=True),
 dict(university='MIT',id='mit-solutions',nativePages=[1,2],method='Both native rendered teaching pages visually read',core=True),
 dict(university='MIT',id='mit-basis',nativePages=[1,2,3],method='All teaching pages read as native text; license page identified',core=True),
 dict(university='Stanford',course='EE263 Autumn2007–08 Lecture3',lecturer='Stephen Boyd',id='stanford',nativePages=list(range(5,14)),method='Full native text read, two slides per physical page',core=True),
 dict(university='Berkeley',course='Math54 Spring2018',lecturer='Alexander Paulin',id='berkeley-spaces',nativePages=[1,2,3,4],method='Every scanned page visually read',core=True),
 dict(university='Berkeley',id='berkeley-coordinates',nativePages=[1,2,3,4],method='Every scanned page visually read',core=True),
 dict(university='CMU',course='21-241 SummerI2014 Day24',lecturer='William Gunther',id='cmu-maps',nativePages=[1,2,3,4],method='All native text read; source mistakes independently corrected',core=False)])
acquisition=json.loads((E/'acquisition.json').read_text());by={a['id']:a for a in acquisition}
for c in reading['courses']:
 a=by[c['id']];assert hashlib.sha256(Path(a['cachePath']).read_bytes()).hexdigest()==a['sha256']
 c.update(url=a['url'],sha256=a['sha256'])
save(E/'reading.json',reading)
mathematics=json.loads((E/'mathematics.json').read_text());browser=json.loads((E/'browser.json').read_text())
assert mathematics['status']==browser['status']=='passed'and not browser['geometry']['issues']and not browser['runtimeErrors']
models=json.loads((R/'dist/chapters/l_linear-models.json').read_text());assert browser['geometry']['models']==len(models['models'])==39
assert browser['geometry']['frames']==137
prior=json.loads((E/'prior-library.json').read_text())['chapters'];assert len(prior)==58
for c in prior:assert hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest()==c['sha256']
all=[c for w in json.loads((R/'dist/lessons.json').read_text())for c in w['chapters']]
assert len(all)==59 and sum(c['questionCount']for c in all)==4085
save(E/'retention.json',dict(status='passed',unchangedChapterPages=58,libraryCards=59,workedQuestionEntries=4085))
save(E/'lesson-and-retention.json',dict(status='quality_review_complete',sections=30,questions=84,originalOrReconstructed=82,authenticRevisited=2,rules=84,models=39,checkpoints=137,placements=63,studentApproved=False,mathematicalChecks=mathematics['exactChecks'],actualJSOracleCases=120,staticMathMLChecks=mathematics['staticMathMLChecks'],mountedMath=browser['counts']['math']))
(B/'l_linear-quality-audit.md').write_text('''# Linear transformations: completed review draft

## Delivery and scope

Thirty sections derive linearity, prescribed inputs, fibers, rank–nullity, typed representations, composition, inverses, equivalence versus similarity, geometric operators, polynomial and matrix-space maps, product rank, dual/adjoint boundaries and finite-dimensional qualifications. The bank contains84 complete worked entries:82 authored or independently reconstructed, including both MIT Session3.6 exercises, and two explicitly revisited authenticated Iranian items. Eighty-four final rules include their assumptions and failure modes. The draft is not student-approved.

## Reading

Four core courses from Oxford, MIT, Stanford and Berkeley were actually read; CMU was also read and evaluated. Seven universities form the bounded candidate pool. Native page ranges, methods and hashes are in reading.json and acquisition.json. The source audit records ten convention/typography/content corrections. Course inventories and cached downloads are not counted as reading.

## Scientific verification

Independent symbolic calculations checked the specific basis, similarity, projection, evaluation, interpolation, adjoint, nilpotent and Sylvester examples. The actual JavaScript exact-rational calculator was compared with independently computed SymPy answers for120 reproducible random cases, including singular operators and skewed invertible bases. Model checkpoint outputs are checked against their original operator. The final verification report records1735 exact/static/retention checks, including1124 native MathML checks. These counts describe specified checks, not exhaustive proofs of all possible program behavior.

## Visual and behavioral verification

Thirty-nine distinct model instances use geometry, typed coordinate pipelines, coefficient flows, matrix-space measurements and kernel fibers. All137 stored checkpoints were inspected in real Edge. Sixty-three lesson/solution placements use the shared controls and compact760-by360 drawing canvas. Real fonts, text bounds, arrow paths and box padding passed. Rotation uses an actual angle transform; an in-flight check confirmed determinant and both basis-vector squared lengths remain one. Other intermediate maps are explicitly distinguished from final projections. A zero output is shown as a point instead of a zero-length arrow. Print checkpoints, reduced motion, before/after comparison, navigation, speed, pause/resume, and invalid-input preservation passed.

Representative desktop and mobile captures were visually read. Phone diagrams retain readable labels in an internal horizontal scroll region; they are not claimed to fit all four pipeline boxes simultaneously on a narrow phone. Page overflow and runtime errors were absent. The actual library contains59 cards, and the week-four link reaches this chapter.

## Retention and provenance

All58 preceding chapter page hashes are unchanged. Library total is59 chapters and4085 worked-entry placements. Authentic originals were rehashed and their rendered pages reread: MS CS1405 Q41, native page9, and PhD CS1404 Q31, native page8. Option order is preserved, answers are independently derived, and no official answer-key authority is claimed. Revisited items are not new distinct archive questions.

## Limits

The chapter does not claim to include every exercise ever issued by the selected universities. Full spectral, orthogonality, conditioning and functional-analysis chapters remain separate. No literal100% coverage of unbounded worldwide courses or guarantee about every unseen question is made. Publication is recorded separately after the private deployment succeeds.
''',encoding='utf-8')
g=json.loads((B/'chapter-gate.json').read_text());assert g['currentTopicId']=='l_linear'
g['completedReviewDrafts']=[c for c in g['completedReviewDrafts']if c['topicId']!='l_linear']+[dict(topicId='l_linear',state='quality_review_complete',studentApproved=False,url='chapters/l_linear.html',qualityAudit='research/l_linear-quality-audit.md',evidence=['research/l_linear-evidence/'+k+'.json'for k in['reading','mathematics','browser']],publicationState='pending_upload')]
# The next scheduled topic is read from the planner, not inferred from the textbook order.
plan=json.loads((R/'dist/schedule.en.json').read_text())
topicOrder=list(plan['topics'])
assert topicOrder[topicOrder.index('l_linear')+1]=='l_orthogonality'
g.update(currentTopicId='l_orthogonality',state='in_progress',nextTopicRequiresExplicitApproval=False,activeWork='Evaluate the next linear-algebra chapter under continuous authorization.',reviewScope='Orthogonality, inner products, Gram matrices and projections; verify the scheduled topic identifier against the planner before authoring.',sourceAuditPath='research/l_orthogonality-source-audit.md',qualityAuditPath='research/l_orthogonality-quality-audit.md',lastCompletedReview='l_linear: 84 worked entries, 84 rules, four core written courses plus CMU comparison, 39 models / 137 checkpoints; 120 actual JS oracle cases.',nextReview='Verify the planner sequence and continue the next pending chapter.',reviewEvidence=['research/l_linear-evidence/'+k+'.json'for k in['reading','mathematics','browser']],currentChapterPublicationState='in_authoring')
save(B/'chapter-gate.json',g)
g.update(sourceAudit='research/l_orthogonality-source-audit.md',qualityAudit='research/l_orthogonality-quality-audit.md')
save(B/'chapter-gate.json',g)
N=B/'l_orthogonality-evidence';N.mkdir(exist_ok=True)
save(N/'prior-library.json',dict(chapters=[dict(topicId=c['topicId'],url=c['url'],questions=c['questionCount'],sha256=hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest())for c in all]))
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\n\n## Linear transformations review draft\n\nCompleted l_linear:30 instructional sections,84 complete worked entries,84 final rules,four core read university courses plus CMU comparison,39 compact subject models/137 checkpoints/63 placements. Exact formulas and120 actual JavaScript calculator cases passed; Edge verified1252 mounted formulas, every model, motion/pause, comparison, print, phone containment and library routes. All58 prior chapter pages are unchanged. Library:59 chapters/4085 worked entries. The chapter remains a review draft, not student-approved; publication is recorded separately. Continue sequentially under the existing user authorization.\n')
print('Finalized the reviewed l_linear draft.')
