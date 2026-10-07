from pathlib import Path
import json,hashlib,subprocess
R=Path(__file__).resolve().parents[1];B=R/'research';O=B/'l_det-evidence';O.mkdir(exist_ok=True)
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
g=json.loads((B/'chapter-gate.json').read_text());assert g['currentTopicId']=='s_expectation'and g['state']=='awaiting_user_approval'
ls=json.loads((R/'dist/lessons.json').read_text());cs=[c for w in ls for c in w['chapters']]
save(O/'prior-library.json',dict(sourceCommit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),chapterCount=len(cs),questionCount=sum(c['questionCount']for c in cs),chapters=[dict(topicId=c['topicId'],url=c['url'],sha256=hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest(),questions=c['questionCount'])for c in cs]))
for c in cs:
 if c['topicId']=='s_expectation':c.update(status='ready',statusLabel='Approved chapter',revisionState='student_approved',approvedVersion=79,animationReviewState='student_approved',visualRevisionState='student_approved')
save(R/'dist/lessons.json',ls)
plan=json.loads((R/'dist/schedule.en.json').read_text());have={c['topicId']for c in cs};n=next((w['number'],t)for w in plan['weeks']for u in w['units']for t in u['topicIds']if t not in have);assert n==(3,'l_det'),n
g.update(currentTopicId='l_det',state='in_progress',approvedTopicId='s_expectation',approvedVersion=79,nextTopicId=None,reviewScope='Only l_det: Determinants, Orientation, and Structured Computation.',activeWork='Explicit approval permits one next chapter. Preserve 41 preceding chapters and 2593 complete worked problems.',publicationState='not_started',publishedVersion=None,publicationRecordPath='research/l_det-publication.json',sourceAuditPath='research/l_det-source-audit.md',qualityAuditPath='research/l_det-quality-audit.md')
save(B/'chapter-gate.json',g)
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\n\n## Active chapter: Determinants — 7 October 2026\n\nThe student explicitly approved expectation and the version-79 delimiter correction. Work only on the next missing Week 3 chapter l_det, preserving all 41 preceding chapter pages and 2593 complete worked problems. Require genuinely reviewed written courses, deep English instruction, mathematical/conceptual solved questions, strong final rules and concept-specific geometric/computational models. Await explicit approval after delivery.\n')
print('l_det active; approval and retained library recorded.')
