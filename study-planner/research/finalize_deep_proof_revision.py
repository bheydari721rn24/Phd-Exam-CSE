"""Record inspected proof evidence without declaring the remaining library checked."""
from pathlib import Path
import html,json,re
B=Path(__file__).resolve().parent;R=B.parent;E=B/'deep-library-revision'
def read(p):return json.loads(p.read_text())
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
m=read(E/'d_proof-mathematical-checks.json');b=read(E/'d_proof-browser.json')
assert all(c['passed']for c in m['checks'])and b['status'].startswith('passed')
m['status']='passed_with_recorded_finite_bounds'
for p in m['sourcePages']:p['visualRecheck']='Original full PDF page visually rechecked on 11 October 2026. Q19 additionally inspected at enlarged scale; identity wording corrected.'
save(E/'d_proof-mathematical-checks.json',m)
b['status']='passed';b['humanInspectedScreenshots']=['proof-strategies.png','question-2.png','question-6.png','question-6-shift.png','question-8-mobile.png','question-31.png','final-rules.png'];b['animationSemanticReview']='Five fixed proof scenarios read checkpoint by checkpoint: even-square algebra; equivalent contrapositive with predicates explicitly defined in the lesson; reduced-fraction square-root contradiction; each fixed equality witness on a three-object domain; even-only reachability from a zero base and step two. Fixed explanations do not certify arbitrary inputs.';save(E/'d_proof-browser.json',b)
rev=read(E/'d_proof-revision.json');rev.update(status='revised_checked_review_draft',checkCount=m['checkCount'],questionTables=8,questionDiagrams=1,finalRules=18,lectureAdditionSections=7,mathematicalEvidence='research/deep-library-revision/d_proof-mathematical-checks.json',browserEvidence='research/deep-library-revision/d_proof-browser.json',sourceReview='Five previously read university-course texts reused within research/d_proof-source-audit.md bounds; no new worldwide exhaustive comparison claimed.',publicationState='prepared_not_yet_deployed')
for q in rev['records']:q['state']='rewritten_and_checked_with_recorded_bounds'
save(E/'d_proof-revision.json',rev)
sets=read(E/'d_sets-revision.json');sets.update(publicationState='deployed',publicationEvidence='research/deep-library-revision/d_sets-publication.json',animationSemanticEvidence='research/deep-library-revision/d_sets-scene-semantics.json');save(E/'d_sets-revision.json',sets)
p=read(E/'progress.json');p.update(revisedChapters=3,pendingChapters=57,currentTopicId='d_induction')
for c in p['chapters']:
    if c['topicId']=='d_proof':c['state']='revised_checked_review_draft'
    elif c['topicId']=='d_induction':c['state']='in_progress'
save(E/'progress.json',p)
gate=read(B/'chapter-gate.json');gate.update(currentTopicId='d_induction',state='in_progress',activeWork='Individual full-library revision: logic, sets and proof checked as new review drafts. Existing functions authentic Q19 source error corrected; its full revision remains pending.',nextReview='Review d_induction individually, then continue frozen library order.',qualityAuditPath='research/deep-library-revision/d_proof-revision.json',publicationState='proof_prepared_for_deployment_logic_and_sets_deployed');save(B/'chapter-gate.json',gate)
lessons=read(R/'dist/lessons.json')
for week in lessons:
    for c in week['chapters']:
        if c['topicId']=='d_proof':c.update(status='draft',statusLabel='Revised and checked · review draft',revisionState='deep_revision_checked_draft',examNotesCount=18)
save(R/'dist/lessons.json',lessons)
rows=''.join('<tr><td>'+str(i)+'</td><td><a href="'+html.escape(c['url'],quote=True)+'">'+html.escape(c['title'])+'</a></td><td>'+str(c['questions'])+'</td><td>'+('Revised and checked; new review draft'if c['state']=='revised_checked_review_draft'else'Individual review in progress'if c['state']=='in_progress'else'Pending individual semantic review')+'</td></tr>'for i,c in enumerate(p['chapters'],1))
path=R/'dist/deep-library-review.html';page=path.read_text()
page=page.replace('2 revised chapters · 58 remaining chapters','3 revised chapters · 57 remaining chapters')
page=page.replace('the 58 pending chapters','the 57 pending chapters')
summary='''<h3>Proof methods: 48 individually rewritten solutions</h3><p><a href="chapters/d_proof.html#worked-problems">Read the revised proof bank</a>. Eight question tables, a question-specific integer-shift diagram, seven detailed mathematical constructions and eighteen final proof rules accompany the retained full university instruction and its 22 derivation tutorials. Each solution states the domain, derives its result, analyses alternatives and checks the meaningful boundaries.</p><p>Original images exposed a consequential transcription error in PhD CS 1405 Q19: the original claims identity, not injectivity. A strictly increasing integer shift refutes that claim; only the well-orderability assertion is true, giving independently derived option 2. The correction is applied in both authentic placements, proof and functions. The relations chapter has only a pattern reference. Functions still awaits its complete individual review.</p><p>There are 269 recorded exact-model, symbolic-identity, source and preservation checks with explicit finite bounds. Five proof animation scenarios passed geometry checks at 17 checkpoints; both static diagrams, fonts, phone, tablet, desktop and print were checked. The five prior university-course readings are reused within their documented source-audit boundaries. This is a checked review draft, not new student approval or certification of the remaining library.</p>'''
assert '<h3>Proof methods:'not in page
page=page.replace('<h2>Required explanation standard</h2>',summary+'<h2>Required explanation standard</h2>')
a=page.index('<tbody>');z=page.index('</tbody>',a);page=page[:a]+'<tbody>'+rows+page[z:];path.write_text(page,encoding='utf-8')
path=R/'WEEKLY_DELIVERY.md';s=path.read_text(encoding='utf-8');heading='## Proof individual revision, 11 October 2026'
if heading not in s:s+='\n'+heading+'\n\nAll 48 answers individually rewritten; eight mathematical tables, a specific order-shift diagram, seven construction sections and eighteen final rules. Six authentic questions visually rechecked. PhD 1405 Q19 originally says identity, not injectivity: corrected translation and independently derived option 2 in proof and functions. Functions full review remains pending. 269 bounded mathematical/source/preservation checks; five animation scenarios at 17 geometry checkpoints; desktop/tablet/mobile/print passed. Three of 60 chapters now revised, 57 remain. Continue d_induction under standing authorization; preserve unfinished l_projection. Publication evidence is separate.\n'
path.write_text(s,encoding='utf-8')
print(json.dumps(dict(revised=3,remaining=57,currentTopicId='d_induction',proofQuestions=48,checks=m['checkCount'])))
