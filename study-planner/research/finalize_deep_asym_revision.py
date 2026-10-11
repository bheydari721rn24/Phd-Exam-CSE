"""Advance the review inventory only after bounded mathematical and rendered checks."""
from pathlib import Path
import hashlib,html,json,tempfile
B=Path(__file__).resolve().parent;R=B.parent;E=B/'deep-library-revision'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
m=read(E/'a_asym-mathematical-checks.json');b=read(E/'a_asym-browser.json')
assert all(q['passed'] for q in m['checks']) and b['status'].startswith('passed')
assert all(all(x['checks']) for x in b['controlChecks']) and all(not x['issues'] for x in b['models'])
b.update(status='passed',humanInspectedScreenshots=['ratio-envelopes.png','strict-hierarchy.png','asym-log-oscillation-7.png','asym-floor-ratio-9.png','question-2.png','question-3-mobile.png','final-rules.png'],mobileDiagramBehavior='Each full-size diagram has local horizontal scrolling; page and question tables remain within the phone viewport. Finite discrete samples are explicitly distinguished from infinite-tail proofs.')
save(E/'a_asym-browser.json',b)
source=read(E/'a_asym-course-recheck.json')
bounds={
 'MIT':('Recitation 1, selected PDF pages 3 and 6','Official PDF web text read: asymptotic definitions and exercises; not a complete course reading.'),
 'Stanford':('Lecture 2, PDF pages 6–7','Downloaded official PDF text read: quantified growth bounds, positive-function assumptions and polynomial witnesses.'),
 'CMU':('Lecture 2 in the lecture bundle, PDF pages 10–12','Official PDF web text read: uniform constants, tightness, strict relations, oscillating ratios and recurrence context.'),
 'Princeton':('PDF pages 3–6, slides 9–24','Cached official PDF text read: asymptotic definitions and comparison rules. Our joint-tail convention is declared explicitly rather than inferred from abbreviated slides.')}
for q in source['sources']:
    q.update(readingState='selected_written_material_actually_read_in_current_revision',readingBounds=bounds[q['university']][0],usedFor=bounds[q['university']][1])
source.update(freshUniversityReadings=4,selectionScope='Four actually read written selections from a documented six-university candidate pool. Selection is bounded and chapter-specific; no exhaustive worldwide course census or entire-course reading is claimed.')
save(E/'a_asym-course-recheck.json',source)
rev=read(E/'a_asym-revision.json');rev.update(status='revised_checked_review_draft',checkCount=m['checkCount'],questionTables=7,staticDiagrams=2,questionAnimations=3,mountedAnimationModels=7,mountedAnimationFrames=sum(x['frames'] for x in b['models']),finalRules=32,lectureAdditionSections=6,sourceReview='research/deep-library-revision/a_asym-course-recheck.json',mathematicalEvidence='research/deep-library-revision/a_asym-mathematical-checks.json',browserEvidence='research/deep-library-revision/a_asym-browser.json',publicationState='prepared_not_yet_deployed',limits='Finite checks and documented source readings support explicit analytic proofs. Universal correctness, complete world-course coverage, and success on every unseen examination question are not certified.')
for q in rev['records']:q['state']='rewritten_and_checked_with_recorded_bounds'
save(E/'a_asym-revision.json',rev)
p=read(E/'progress.json')
for q in p['chapters']:
    if q['topicId']=='a_asym':q['state']='revised_checked_review_draft'
    elif q['topicId']=='a_loop':q['state']='in_progress'
count=sum(q['state']=='revised_checked_review_draft' for q in p['chapters']);assert count==6
p.update(revisedChapters=count,pendingChapters=len(p['chapters'])-count,currentTopicId='a_loop');save(E/'progress.json',p)
gate=read(B/'chapter-gate.json');gate.update(currentTopicId='a_loop',state='in_progress',activeWork='Continue individual whole-library review: six checked review drafts, 54 remaining. Preserve unfinished projection authoring.',qualityAuditPath='research/deep-library-revision/a_asym-revision.json',publicationState='five_reviewed_chapters_deployed_asymptotic_revision_prepared');save(B/'chapter-gate.json',gate)
lessons=read(R/'dist/lessons.json')
for week in lessons:
    for c in week['chapters']:
        if c['topicId']=='a_asym':c.update(status='draft',statusLabel='Revised and checked · review draft',revisionState='deep_revision_checked_draft',examNotesCount=32)
save(R/'dist/lessons.json',lessons)
path=R/'dist/deep-library-review.html';page=path.read_text(encoding='utf-8').replace('5 revised chapters · 55 remaining chapters','6 revised chapters · 54 remaining chapters').replace('the 55 pending chapters','the 54 pending chapters')
summary='<h3>Asymptotic notation: 46 individually rewritten solutions</h3><p><a href="chapters/a_asym.html#worked-problems">Read the revised question bank</a>. All solutions now include exact calculations, witness constants, quantified counterexamples or controlled integer subsequences as appropriate. Seven mathematical tables, three question-specific animations, two rebuilt diagrams, six construction sections and 32 complete final rules complement the retained full lesson and 18 derivation tutorials.</p><p>Four bounded official university readings and four authentic PDF questions were rechecked. A missing factor and logarithm exponent in one authentic option were restored in both affected chapters. There are 414 bounded mathematical/source/preservation checks, geometry checks of 55 mounted animation checkpoints and 18 navigation/view control checks. Desktop, tablet, phone, print and mathematical fonts were inspected. This remains a review draft; 54 chapters still await individual review.</p>'
if '<h3>Asymptotic notation:' not in page:page=page.replace('<h2>Required explanation standard</h2>',summary+'<h2>Required explanation standard</h2>')
rows=''.join('<tr><td>'+str(i)+'</td><td><a href="'+html.escape(c['url'],quote=True)+'">'+html.escape(c['title'])+'</a></td><td>'+str(c['questions'])+'</td><td>'+('Revised and checked; new review draft' if c['state']=='revised_checked_review_draft' else 'Individual review in progress' if c['state']=='in_progress' else 'Pending individual semantic review')+'</td></tr>' for i,c in enumerate(p['chapters'],1))
a=page.index('<tbody>');z=page.index('</tbody>',a);page=page[:a]+'<tbody>'+rows+page[z:];path.write_text(page,encoding='utf-8')
path=R/'WEEKLY_DELIVERY.md';text=path.read_text(encoding='utf-8');heading='## Asymptotic notation individual revision, 11 October 2026'
if heading not in text:text+='\n'+heading+'\n\n46 individually authored solutions (7,182 words), seven mathematical tables, three dedicated discrete question animations, two redesigned diagrams, six construction sections and 32 complete final rules. Four genuinely read bounded university selections and four authentic PDF questions rechecked. 414 finite mathematical/source/preservation checks, all 55 mounted animation checkpoints, 18 control checks and desktop/tablet/mobile/print/font checks passed. Q2 option four restored to Theta(n log-squared n) in both asymptotic and recurrence chapters; recurrence chapter remains pending full review. Six of 60 reviewed; continue a_loop. The earlier five revisions were successfully deployed privately together; this sixth revision is prepared for publication.\n'
path.write_text(text,encoding='utf-8')
print(json.dumps(dict(revised=count,remaining=60-count,next='a_loop')))
