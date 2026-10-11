"""Record inspected model evidence without promoting any student approval."""
from pathlib import Path
import hashlib,html,json,tempfile
B=Path(__file__).resolve().parent;R=B.parent;E=B/'deep-library-revision'
def read(p):return json.loads(p.read_text())
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
m=read(E/'a_model-mathematical-checks.json');b=read(E/'a_model-browser.json');s=read(E/'a_model-scene-semantics.json')
assert all(x['passed'] for x in m['checks']) and b['status'].startswith('passed') and s['status']=='passed'
b.update(status='passed',humanInspectedScreenshots=['merge-first.png','merge-middle.png','merge-final.png','merge-mobile.png','question-12-depths.png','question-3-mobile.png','question-4.png','question-45.png','model-representation.png','final-rules.png'],mobileDiagramBehavior='Full-size diagrams use local horizontal scrolling so labels retain readable size. The page itself and question tables have no horizontal overflow.')
save(E/'a_model-browser.json',b)
source=read(E/'a_model-course-recheck.json')
scope={
 'MIT':('Lecture 1, pages 1–4','Problem contracts, correctness, input sizes, basic RAM/address assumptions. Official web text and locally cached PDF text read during this revision.'),
 'CMU':('Lecture 3, pages 1–4','Bounded word operations, multiplication width, integer sorting outside comparison restrictions, preprocessing. Official web PDF text read during this revision.'),
 'Princeton':('Slides 1–8, PDF pages 1–2','Computational models, word versus bit costs, polynomial classification. Local PDF text read during this revision.'),
 'Stanford':('Lecture 1, relevant text including PDF pages 2–3','Input-length arithmetic, growth of operands, asymptotic modeling and precomputation limits. Official web and local text read during this revision.')}
for q in source['sources']:
    name=q['university']
    if name in scope:
        q.update(readingState='selected_written_material_actually_read_in_current_revision',readingBounds=scope[name][0],usedFor=scope[name][1])
        cache=Path(tempfile.gettempdir())/'deep-model-sources'/(name+'.pdf')
        if cache.exists():q['sourceSha256']=hashlib.sha256(cache.read_bytes()).hexdigest()
    else:q.update(readingState='documented_previous_selected_reading_reused',readingBounds='Previously recorded PDF pages 9–11',currentAccess='Old official slide URL unavailable; no fresh reading or complete course reading claimed.')
source.update(scope='Four freshly rechecked official written course selections, plus one bounded prior reading. Six-course documented candidate pool; neither all course content nor a worldwide exhaustive census.',freshUniversityReadings=4,priorUniversityReadingsReused=1)
save(E/'a_model-course-recheck.json',source)
rev=read(E/'a_model-revision.json');rev.update(status='revised_checked_review_draft',checkCount=m['checkCount'],sceneCheckCount=s['checkCount'],questionTables=6,questionDiagrams=2,questionAnimations=1,finalRules=32,lectureAdditionSections=8,mathematicalEvidence='research/deep-library-revision/a_model-mathematical-checks.json',browserEvidence='research/deep-library-revision/a_model-browser.json',sourceReview='research/deep-library-revision/a_model-course-recheck.json',publicationState='prepared_not_yet_deployed')
for q in rev['records']:q['state']='rewritten_and_checked_with_recorded_bounds'
save(E/'a_model-revision.json',rev)
p=read(E/'progress.json')
for q in p['chapters']:
    if q['topicId']=='a_model':q['state']='revised_checked_review_draft'
    elif q['topicId']=='a_asym':q['state']='in_progress'
count=sum(q['state']=='revised_checked_review_draft' for q in p['chapters']);assert count==5
p.update(revisedChapters=count,pendingChapters=len(p['chapters'])-count,currentTopicId='a_asym');save(E/'progress.json',p)
gate=read(B/'chapter-gate.json');gate.update(currentTopicId='a_asym',state='in_progress',activeWork='Continue individual whole-library review: five chapters checked, 55 remaining. Preserve unfinished projection authoring.',qualityAuditPath='research/deep-library-revision/a_model-revision.json',publicationState='logic_and_sets_deployed_three_later_revisions_pending_native_publication');save(B/'chapter-gate.json',gate)
lessons=read(R/'dist/lessons.json')
for week in lessons:
    for c in week['chapters']:
        if c['topicId']=='a_model':c.update(status='draft',statusLabel='Revised and checked · review draft',revisionState='deep_revision_checked_draft',examNotesCount=32)
save(R/'dist/lessons.json',lessons)
path=R/'dist/deep-library-review.html';page=path.read_text().replace('4 revised chapters · 56 remaining chapters','5 revised chapters · 55 remaining chapters').replace('the 56 pending chapters','the 55 pending chapters')
summary='<h3>Computation models: 46 individually rewritten solutions</h3><p><a href="chapters/a_model.html#worked-problems">Read the revised mathematical question bank</a>. Six solution tables, two question-specific tree diagrams, and an exact 23-checkpoint animation distinguish all 16 comparisons from seven uncharged tail copies. Eight added mathematical construction sections and 32 complete final rules supplement the retained full lesson and 16 derivation tutorials.</p><p>Four official university written readings were rechecked within documented bounds. Four authentic examination items retain their source meaning and options. There are 697 bounded mathematical, source and preservation checks, 60 further checks of retained animation states, and geometry checks of every mounted checkpoint. Desktop, tablet, phone, print, mathematical fonts and three static diagrams were inspected. Literal universal correctness and unseen-examination performance are not certified by finite tests. The other 55 chapters still await individual review.</p>'
if '<h3>Computation models:' not in page:page=page.replace('<h2>Required explanation standard</h2>',summary+'<h2>Required explanation standard</h2>')
rows=''.join('<tr><td>'+str(i)+'</td><td><a href="'+html.escape(c['url'],quote=True)+'">'+html.escape(c['title'])+'</a></td><td>'+str(c['questions'])+'</td><td>'+('Revised and checked; new review draft' if c['state']=='revised_checked_review_draft' else 'Individual review in progress' if c['state']=='in_progress' else 'Pending individual semantic review')+'</td></tr>' for i,c in enumerate(p['chapters'],1))
a=page.index('<tbody>');z=page.index('</tbody>',a);page=page[:a]+'<tbody>'+rows+page[z:];path.write_text(page,encoding='utf-8')
path=R/'WEEKLY_DELIVERY.md';v=path.read_text(encoding='utf-8');title='## Computation models individual revision, 11 October 2026'
if title not in v:v+='\n'+title+'\n\n46 individually authored solutions (8,240 words), six question tables, two question diagrams, an exact authentic merge trace (23 checkpoints, 16 comparisons), eight construction sections and 32 complete final rules. 697 bounded mathematics/source/preservation checks plus 60 retained-animation semantic checks passed. Rendered desktop/tablet/mobile/print and fonts inspected. Four fresh bounded university readings and one prior reading documented. Five of 60 revised as checked review drafts; continue a_asym. Native publication of proof and induction timed out before saving versions; current source delivery and online delivery remain distinct.\n'
path.write_text(v,encoding='utf-8')
save(E/'d_induction-upload-attempts.json',dict(sourceCommit='1cb982141cc78010ffe07415b89be253e8094dac',archiveSha256='85042977c975fcc97f84ae5b46a7413d24343b939332849580838196888bb62e',status='archive_upload_timed_out',elapsedMilliseconds=300014,savedVersionId=None,deploymentId=None,publicationState='source_pushed_native_publication_pending'))
print(json.dumps(dict(revised=count,remaining=60-count,next='a_asym')))
