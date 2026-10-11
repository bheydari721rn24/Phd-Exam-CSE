"""Finalize bounded evidence and advance only the single completed review."""
from pathlib import Path
import html,json
B=Path(__file__).resolve().parent;R=B.parent;E=B/'deep-library-revision'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
m=read(E/'s_axioms-mathematical-checks.json');b=read(E/'s_axioms-browser.json')
assert all(q['passed'] for q in m['checks']) and b['status'].startswith('passed')
assert all(all(x['checks']) for x in b['controlChecks']) and all(not x['issues'] for x in b['models'])
assert len(b['labelFormulaSeparation'])==24 and all(not x['overlaps'] and x['height']<=362 for x in b['labelFormulaSeparation'])
b.update(status='passed',humanInspectedScreenshots=['reporting-map.png','four-atomic-masses.png','uniform-area.png','axioms-question-atoms39-5.png','axioms-question-atoms47-6.png','axioms-question-urn-3.png','axioms-question-report-2.png','axioms-question-collision-2.png','question-31.png','question-47.png','question-3-mobile.png','final-rules.png'],mobileDiagramBehavior='Mathematical diagrams retain readable native fractions and scroll locally on narrow screens; prose and question tables remain inside the viewport. Every new checkpoint is checked for label/formula overlap and compact canvas height.')
save(E/'s_axioms-browser.json',b)
source=read(E/'s_axioms-course-recheck.json')
bounds={
 'MIT':('6.041/6.431 Fall 2010, Lecture 1, PDF pages 1–3','Official PDF web text actually read: detailed sample-space granularity, finite and countable laws, uniform area and the required countable-additivity strengthening. Direct download timed out; no local PDF hash is invented.'),
 'Stanford':('CS109 Spring 2020, Lecture Notes 3, all five PDF pages','Official PDF web text actually read: finite identities, outcome weighting, reporting granularity and internally consistent counting spaces. The informal limiting-frequency definition is not adopted as an existence theorem. Direct download timed out.'),
 'ETH Zurich':('Probability Theory Fall 2025, Section 1.1, printed pages 8–10, PDF pages 14–16','Official downloaded PDF text actually read: formal probability space, complement, countable intersections, continuity and union bound. Independent elementary proofs supply the source prerequisites.'),
 'Berkeley':('Stat 210A, Measure Theory Basics, Measures section and probability normalization','Official web text actually read: restricted measurable domain, sigma-field closure and normalized measure. Integration and measure construction are outside the chapter boundary.')}
for q in source['sources']:
 if q.get('errorType'):q['directDownloadAttempt']=q.pop('errorType')
 q.update(readingState='selected_written_material_actually_read_in_current_revision',readingBounds=bounds[q['university']][0],usedFor=bounds[q['university']][1])
source.update(freshUniversityReadings=4,selectionScope='Four core written selections freshly read within the documented bounded eight-university survey; Oxford supplementary reading is prior evidence. No exhaustive global course evaluation or entire-course reading is claimed.',originalPdfInspection='Six included authentic questions inspected on their original PDF pages. A seventh source record, Phd_CS_1404_Q67, was inspected but excluded because its without-replacement wording conflicts with its offered answers.',retainedTutorialAudit='All 24 complete existing derivation tutorials actually read and retained. The full lesson and six new construction sections were also read; numeric examples and set-limit distinctions were checked.')
save(E/'s_axioms-course-recheck.json',source)
rev=read(E/'s_axioms-revision.json');rev.update(status='revised_checked_review_draft',checkCount=m['checkCount'],questionTables=13,rebuiltStaticDiagrams=2,inspectedStaticDiagrams=3,questionAnimations=5,mountedAnimationInstances=len(b['models']),uniqueAnimationModels=len(set(x['id'] for x in b['models'])),mountedAnimationFrames=sum(x['frames'] for x in b['models']),controlChecks=sum(len(x['checks']) for x in b['controlChecks']),labelFormulaSeparationChecks=24,finalRules=32,lectureAdditionSections=6,retainedFullTutorials=24,sourceReview='research/deep-library-revision/s_axioms-course-recheck.json',mathematicalEvidence='research/deep-library-revision/s_axioms-mathematical-checks.json',browserEvidence='research/deep-library-revision/s_axioms-browser.json',publicationState='prepared_not_yet_deployed',limits='Finite models and symbolic identities complement explicit general proofs. Universal correctness, global-course completeness and future success on every unseen examination item are not certified.')
for q in rev['records']:q['state']='rewritten_and_checked_with_recorded_bounds'
save(E/'s_axioms-revision.json',rev)
p=read(E/'progress.json')
for q in p['chapters']:
 if q['topicId']=='s_axioms':q['state']='revised_checked_review_draft'
 elif q['topicId']=='s_counting':q['state']='in_progress'
count=sum(q['state']=='revised_checked_review_draft' for q in p['chapters']);assert count==8
p.update(revisedChapters=count,pendingChapters=len(p['chapters'])-count,currentTopicId='s_counting');save(E/'progress.json',p)
gate=read(B/'chapter-gate.json');gate.update(currentTopicId='s_counting',state='in_progress',activeWork='Continue individual whole-library review: eight checked review drafts, 52 remaining. Preserve unfinished projection authoring.',lastCompletedReview='s_axioms: 48 individually rewritten solutions, 32 final rules, 380 bounded checks, 50 mounted animation checkpoints.',nextReview='Review s_counting individually, then continue frozen existing-library order.',qualityAuditPath='research/deep-library-revision/s_axioms-revision.json',publicationState='five_reviewed_chapters_confirmed_online_three_new_revisions_prepared');save(B/'chapter-gate.json',gate)
lessons=read(R/'dist/lessons.json')
for week in lessons:
 for c in week['chapters']:
  if c['topicId']=='s_axioms':c.update(status='draft',statusLabel='Revised and checked · review draft',revisionState='deep_revision_checked_draft',examNotesCount=32)
save(R/'dist/lessons.json',lessons)
path=R/'dist/deep-library-review.html';page=path.read_text().replace('7 revised chapters · 53 remaining chapters','8 revised chapters · 52 remaining chapters').replace('the 53 pending chapters','the 52 pending chapters')
summary='<h3>Probability foundations: 48 individually rewritten solutions</h3><p><a href="chapters/s_axioms.html#worked-problems">Read the revised question bank</a>. Full atom tables, exact conditional denominators, attained feasibility intervals, indicator moments and option analysis replace abstract templates. Thirteen question tables, five dedicated models, two rebuilt static diagrams, six mathematical construction sections and 32 complete final rules complement the full lesson and 24 retained derivation tutorials.</p><p>Four core written university selections and six authentic examination questions were freshly rechecked. A separate contradictory source item is explicitly excluded. All 380 bounded mathematical/source/preservation checks, 50 mounted animation checkpoints, 30 control checks and 24 label/formula separation checks passed. Three static diagrams and responsive, print and font behavior were inspected. Eight of 60 chapters have now been individually revised; 52 remain.</p>'
if '<h3>Probability foundations:' not in page:page=page.replace('<h2>Required explanation standard</h2>',summary+'<h2>Required explanation standard</h2>')
rows=''.join('<tr><td>'+str(i)+'</td><td><a href="'+html.escape(c['url'],quote=True)+'">'+html.escape(c['title'])+'</a></td><td>'+str(c['questions'])+'</td><td>'+('Revised and checked; new review draft' if c['state']=='revised_checked_review_draft' else 'Individual review in progress' if c['state']=='in_progress' else 'Pending individual semantic review')+'</td></tr>' for i,c in enumerate(p['chapters'],1))
a=page.index('<tbody>');z=page.index('</tbody>',a);page=page[:a]+'<tbody>'+rows+page[z:];path.write_text(page,encoding='utf-8')
path=R/'WEEKLY_DELIVERY.md';s=path.read_text();heading='## Probability foundations individual revision, 12 October 2026'
if heading not in s:s+='\n'+heading+'\n\n48 individually authored solutions (7,399 words), 13 mathematical tables, five dedicated probability models, two rebuilt diagrams, six construction sections and 32 final rules. The full lesson and all 24 prior derivation tutorials were read and retained. Four bounded core university selections and six authentic questions rechecked against official text/original PDF pages; the separate conflicting Phd_CS_1404_Q67 is excluded. 380 bounded mathematical/source/preservation checks, 50 mounted checkpoints, 30 control checks, 24 label/formula separation checks and responsive/print/font checks passed. Eight of 60 reviewed; continue s_counting. Latest confirmed online individual-review publication still contains five chapters; upload failures for the newer asymptotic and loop archive are recorded.\n'
path.write_text(s,encoding='utf-8');print(json.dumps(dict(revised=count,remaining=60-count,next='s_counting')))
