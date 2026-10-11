"""Record inspected sets evidence and advance only the individual-review queue."""
from pathlib import Path
import html,json
B=Path(__file__).resolve().parent;R=B.parent;E=B/'deep-library-revision'
def read(p):return json.loads(p.read_text())
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
m=read(E/'d_sets-mathematical-checks.json');b=read(E/'d_sets-browser.json')
assert all(c['passed']for c in m['checks'])and b['status'].startswith('passed')
m['status']='passed_with_recorded_finite_bounds'
for p in m['sourcePages']:p['visualRecheck']='Original full booklet page visually rechecked on 11 October 2026; mathematical meaning and option order retained.'
save(E/'d_sets-mathematical-checks.json',m)
b['status']='passed';b['humanInspectedScreenshots']=['question-3.png','question-5.png','question-45.png','question-21-mobile.png','set-animation.png','final-rules.png'];save(E/'d_sets-browser.json',b)
rev=read(E/'d_sets-revision.json');rev.update(status='revised_checked_review_draft',checkCount=m['checkCount'],questionTables=7,finalRules=20,lectureAdditionSections=7,mathematicalEvidence='research/deep-library-revision/d_sets-mathematical-checks.json',browserEvidence='research/deep-library-revision/d_sets-browser.json',sourceReview='Four previously read university courses plus a fifth supplemental written text reused within research/d_sets-source-audit.md bounds. Stanford proof guide refreshed in this review. No worldwide exhaustive comparison is claimed.',publicationState='prepared_not_yet_deployed')
for q in rev['records']:q['state']='rewritten_and_checked_with_recorded_bounds'
save(E/'d_sets-revision.json',rev)
logic=read(E/'d_logic-revision.json');logic['publicationState']='deployed';logic['publicationEvidence']='research/deep-library-revision/d_logic-publication.json';save(E/'d_logic-revision.json',logic)
p=read(E/'progress.json');p.update(revisedChapters=2,pendingChapters=58,currentTopicId='d_proof')
for c in p['chapters']:
 if c['topicId']=='d_sets':c['state']='revised_checked_review_draft'
 elif c['topicId']=='d_proof':c['state']='in_progress'
save(E/'progress.json',p)
gate=read(B/'chapter-gate.json');gate.update(currentTopicId='d_proof',state='in_progress',activeWork='Full existing-library revision. Logic and sets revised with individual mathematical solutions; proof is next.',nextReview='Complete d_proof individual review, then d_induction in frozen library order.',qualityAuditPath='research/deep-library-revision/d_sets-revision.json',publicationState='sets_prepared_for_deployment_logic_deployed');save(B/'chapter-gate.json',gate)
lessons=read(R/'dist/lessons.json')
for week in lessons:
 for c in week['chapters']:
  if c['topicId']=='d_sets':c.update(status='draft',statusLabel='Revised and checked · review draft',revisionState='deep_revision_checked_draft',examNotesCount=20)
save(R/'dist/lessons.json',lessons)
rows=''.join('<tr><td>'+str(i)+'</td><td><a href="'+html.escape(c['url'],quote=True)+'">'+html.escape(c['title'])+'</a></td><td>'+str(c['questions'])+'</td><td>'+('Revised and checked; new review draft'if c['state']=='revised_checked_review_draft'else'Individual review in progress'if c['state']=='in_progress'else'Pending individual semantic review')+'</td></tr>'for i,c in enumerate(p['chapters'],1))
old=(R/'dist/deep-library-review.html').read_text()
start=old.index('<h2>Completed logic revision</h2>');end=old.index('<h2>Required explanation standard</h2>')
summary='''<h2>Completed individual revisions</h2><h3>Logic: 53 rewritten solutions</h3><p><a href="chapters/d_logic.html#worked-problems">Read the revised logic bank</a>. Twelve question tables, seven additional mathematical teaching sections and seventeen final rules. A missing parameter hypothesis and two incorrectly transcribed PhD 1405 Q15 options were corrected. Original booklet images were rechecked. The four documented core written-course readings are reused within their recorded bounds. There are 164 recorded finite, exact-count and preservation checks; four animation scenarios passed geometry checks at 22 checkpoints, and five laboratory choices passed 40 truth-row checks.</p><h3>Sets: 46 rewritten solutions</h3><p><a href="chapters/d_sets.html#worked-problems">Read the revised sets bank</a>. Seven actual question tables, seven detailed counting constructions and twenty final rules. Every answer now derives its result, explains the relevant definitions, distinguishes alternatives and checks meaningful boundaries. All four authentic questions were rechecked against original PDF images; their meanings and option order are retained. Four prior core university-course readings and a fifth supplemental text are reused within the recorded source-audit bounds.</p><p>The sets review passed 316 recorded checks, including finite-universe enumerations from zero through four objects, prescribed subsets in that range, exact examples, source-file hashes and preservation checks. All nine retained animation scenarios passed geometry checks at 66 checkpoints. The membership laboratory passed all 32 expression evaluations, with mathematical labels rendered in STIX Two Math. Desktop, tablet, phone and print checks passed. Finite tests supplement the general proofs; neither they nor this report certify the 58 pending chapters or promise performance on unseen examination questions.</p>'''
old=old[:start]+summary+old[end:]
old=old.replace('1 revised chapter · 59 remaining chapters','2 revised chapters · 58 remaining chapters')
a=old.index('<tbody>');z=old.index('</tbody>',a);old=old[:a]+'<tbody>'+rows+old[z:]
(R/'dist/deep-library-review.html').write_text(old,encoding='utf-8')
path=R/'WEEKLY_DELIVERY.md';s=path.read_text(encoding='utf-8')
heading='## Sets individual revision, 11 October 2026'
if heading not in s:s+='\n'+heading+'\n\nAll 46 problem solutions rewritten individually; seven mathematical construction sections and twenty final rules added. Four authentic booklet pages visually rechecked. 316 bounded checks passed; nine animation scenarios / 66 geometry checkpoints, 32 membership-lab evaluations, mobile and print passed. Logic and sets now revised: 2 of 60; 58 remain. Continue d_proof under standing full-library revision authorization; preserve unfinished l_projection. Publication evidence is kept separately.\n'
path.write_text(s,encoding='utf-8')
print(json.dumps(dict(revised=2,remaining=58,currentTopicId='d_proof',setsQuestions=46,checks=m['checkCount'])))
