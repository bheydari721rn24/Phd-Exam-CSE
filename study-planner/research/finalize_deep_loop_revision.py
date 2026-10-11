"""Record bounded evidence for the individually revised loop chapter."""
from pathlib import Path
import html,json
B=Path(__file__).resolve().parent;R=B.parent;E=B/'deep-library-revision'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
m=read(E/'a_loop-mathematical-checks.json');b=read(E/'a_loop-browser.json')
assert all(q['passed'] for q in m['checks']) and b['status'].startswith('passed')
assert all(all(x['checks']) for x in b['controlChecks']) and all(not x['issues'] for x in b['models'])
assert len(b['gridAlignment'])==16 and all(x['columnLabels']==8 and x['spread']<.1 and x['height']<=362 for x in b['gridAlignment'])
b.update(status='passed',humanInspectedScreenshots=['strict-triangle.png','exact-schedules.png','loop-question-parity-7.png','loop-question-product-7.png','loop-question-minimum-7.png','model-merge-exact-22.png','question-32.png','question-45.png','question-3-mobile.png','parity-mobile.png','final-rules.png'],mobileDiagramBehavior='Full-sized mathematical state diagrams scroll locally on phones; prose and tables remain within the viewport. All grid columns retain a common baseline and a compact canvas at every checkpoint.')
save(E/'a_loop-browser.json',b)
source=read(E/'a_loop-course-recheck.json')
bounds={
 'MIT':('6.006 Spring 2020, Lecture 1, PDF pages 2–4','Word-RAM assumptions, input/output cost, dependent pair enumeration and early return; downloaded official text actually read.'),
 'Stanford':('CS161 Fall 2014, Lecture 1, PDF pages 6–9','Operation-frequency sums, nested-loop analysis and asymptotic comparisons; official web-extracted PDF text actually read. Garbled extracted formulas were independently derived.'),
 'Princeton':('COS226 Spring 2014, Analysis of Algorithms, PDF pages 6–10','Cost times frequency, pair/triple counts and careful sum approximations; downloaded official text actually read. Historical timing data are not current performance claims.'),
 'Berkeley':('CS61B Spring 2018, Lecture 18 guide: overview and recommended problems','Dependent versus independent loops and simplification practice; official written guide actually read. The earlier Lecture 17 review is prior evidence, not claimed as a fresh reading.')}
for q in source['sources']:q.update(readingState='selected_written_material_actually_read_in_current_revision',readingBounds=bounds[q['university']][0],usedFor=bounds[q['university']][1])
source.update(freshUniversityReadings=4,selectionScope='Four genuinely read written selections from a documented six-university candidate pool. No entire-course reading or exhaustive global-course census is claimed.',originalPdfInspection='All four original question pages inspected. A zoomed code crop additionally confirms j starts at i in Phd_CS_1405_Q20.')
save(E/'a_loop-course-recheck.json',source)
rev=read(E/'a_loop-revision.json');rev.update(status='revised_checked_review_draft',checkCount=m['checkCount'],questionTables=7,staticDiagrams=2,questionAnimations=3,reusedQuestionAnimation='model-merge-exact',mountedAnimationInstances=len(b['models']),uniqueAnimationModels=len(set(x['id'] for x in b['models'])),mountedAnimationFrames=sum(x['frames'] for x in b['models']),controlChecks=sum(len(x['checks']) for x in b['controlChecks']),gridAlignmentChecks=16,finalRules=32,lectureAdditionSections=6,sourceReview='research/deep-library-revision/a_loop-course-recheck.json',mathematicalEvidence='research/deep-library-revision/a_loop-mathematical-checks.json',browserEvidence='research/deep-library-revision/a_loop-browser.json',publicationState='prepared_not_yet_deployed',limits='Finite checks complement analytic proofs under explicit arithmetic and execution conventions. Universal correctness, global course completeness and success on every unseen question are not certified.')
for q in rev['records']:q['state']='rewritten_and_checked_with_recorded_bounds'
save(E/'a_loop-revision.json',rev)
p=read(E/'progress.json')
for q in p['chapters']:
 if q['topicId']=='a_loop':q['state']='revised_checked_review_draft'
 elif q['topicId']=='s_axioms':q['state']='in_progress'
count=sum(q['state']=='revised_checked_review_draft' for q in p['chapters']);assert count==7
p.update(revisedChapters=count,pendingChapters=len(p['chapters'])-count,currentTopicId='s_axioms');save(E/'progress.json',p)
gate=read(B/'chapter-gate.json');gate.update(currentTopicId='s_axioms',state='in_progress',activeWork='Continue individual whole-library review: seven checked review drafts, 53 remaining. Preserve unfinished projection authoring.',lastCompletedReview='a_loop: 46 individually rewritten solutions, 32 final rules, 544 bounded checks, 97 mounted animation checkpoints.',nextReview='Review s_axioms individually, then continue frozen existing-library order.',qualityAuditPath='research/deep-library-revision/a_loop-revision.json',publicationState='five_reviewed_chapters_deployed_two_new_revisions_prepared')
save(B/'chapter-gate.json',gate)
lessons=read(R/'dist/lessons.json')
for week in lessons:
 for c in week['chapters']:
  if c['topicId']=='a_loop':c.update(status='draft',statusLabel='Revised and checked · review draft',revisionState='deep_revision_checked_draft',examNotesCount=32)
save(R/'dist/lessons.json',lessons)
path=R/'dist/deep-library-review.html';page=path.read_text().replace('6 revised chapters · 54 remaining chapters','7 revised chapters · 53 remaining chapters').replace('the 54 pending chapters','the 53 pending chapters')
summary='<h3>Loop analysis: 46 individually rewritten solutions</h3><p><a href="chapters/a_loop.html#worked-problems">Read the revised question bank</a>. Every answer now gives an actual operation ledger, a sum derivation, a constructive worst case or a probability argument as required. Seven mathematical tables, three new question-specific models, the exact verified merge trace, two rebuilt diagrams, six construction sections and 32 complete final rules complement the retained full lesson and 20 derivation tutorials.</p><p>Four selected university readings and four original examination PDF questions were rechecked. All 544 bounded mathematical/source/preservation checks, 97 mounted animation checkpoints, 24 navigation/view checks and 16 compact-grid alignment checks passed. Desktop, tablet, phone, print and mathematical fonts were inspected. This remains a review draft; 53 chapters still await individual review.</p>'
if '<h3>Loop analysis:' not in page:page=page.replace('<h2>Required explanation standard</h2>',summary+'<h2>Required explanation standard</h2>')
rows=''.join('<tr><td>'+str(i)+'</td><td><a href="'+html.escape(c['url'],quote=True)+'">'+html.escape(c['title'])+'</a></td><td>'+str(c['questions'])+'</td><td>'+('Revised and checked; new review draft' if c['state']=='revised_checked_review_draft' else 'Individual review in progress' if c['state']=='in_progress' else 'Pending individual semantic review')+'</td></tr>' for i,c in enumerate(p['chapters'],1))
a=page.index('<tbody>');z=page.index('</tbody>',a);page=page[:a]+'<tbody>'+rows+page[z:];path.write_text(page,encoding='utf-8')
path=R/'WEEKLY_DELIVERY.md';s=path.read_text();heading='## Loop analysis individual revision, 12 October 2026'
if heading not in s:s+='\n'+heading+'\n\n46 individually authored solutions (8,068 words), seven mathematical tables, three dedicated question state models and an existing exact 23-checkpoint merge trace. Two redesigned diagrams, six construction sections and 32 complete final rules. Four genuinely read bounded university selections and four authentic PDF questions rechecked. 544 finite mathematical/source/preservation checks, all 97 mounted checkpoints, 24 control checks, 16 compact-grid alignment checks and responsive/print/font checks passed. Both zero dimensions now have an explicit fixed setup cost in the full lecture. Seven of 60 reviewed; continue s_axioms. The latest confirmed online publication contains five individually revised chapters; asymptotic and loop revisions are prepared, with upload errors recorded separately.\n'
path.write_text(s,encoding='utf-8')
print(json.dumps(dict(revised=count,remaining=60-count,next='s_axioms')))
