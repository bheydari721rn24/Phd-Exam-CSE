from pathlib import Path
import json,hashlib,subprocess
R=Path(__file__).resolve().parents[1];B=R/'research';O=B/'s_discrete-evidence';O.mkdir(exist_ok=True)
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
g=json.loads((B/'chapter-gate.json').read_text());assert g['currentTopicId']=='s_descriptive' and g['state']=='awaiting_user_approval'
ls=json.loads((R/'dist/lessons.json').read_text());cs=[c for w in ls for c in w['chapters']]
save(O/'prior-library.json',dict(sourceCommit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),chapterCount=len(cs),questionCount=sum(c['questionCount'] for c in cs),chapters=[dict(topicId=c['topicId'],url=c['url'],sha256=hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest(),questions=c['questionCount']) for c in cs]))
for c in cs:
 if c['topicId']=='s_descriptive':c.update(status='ready',statusLabel='Approved chapter',revisionState='student_approved',approvedVersion=76,animationReviewState='student_approved',visualRevisionState='student_approved')
save(R/'dist/lessons.json',ls)
plan=json.loads((R/'dist/schedule.en.json').read_text());have={c['topicId'] for c in cs};n=next((w['number'],t) for w in plan['weeks'] for u in w['units'] for t in u['topicIds'] if t not in have)
assert n==(3,'s_discrete'),n
g.update(currentTopicId='s_discrete',state='in_progress',approvedTopicId='s_descriptive',approvedVersion=76,nextTopicId=None,reviewScope='Only s_discrete: Discrete Random Variables and Common Distributions.',activeWork='Latest explicit approval permits one next chapter. Preserve 39 preceding chapters and 2428 complete worked problems.',publicationState='not_started',publishedVersion=None,publicationRecordPath='research/s_discrete-publication.json',sourceAuditPath='research/s_discrete-source-audit.md',qualityAuditPath='research/s_discrete-quality-audit.md')
g.pop('delivery',None);save(B/'chapter-gate.json',g)
with (R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8') as f:f.write('\n\n## Active chapter: Discrete Random Variables, 7 October 2026\n\nThe student explicitly approved s_descriptive version 76. The next missing scheduled topic is s_discrete in Week 3. Author and audit only this chapter; preserve all 39 preceding chapters and 2428 complete problem bodies. Await explicit approval after delivery.\n')
print('s_discrete active; previous chapter approved; retention baseline captured.')
