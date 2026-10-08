from pathlib import Path
import json,hashlib,subprocess
R=Path(__file__).resolve().parents[1];B=R/'research';E=B/'l_spaces-evidence';E.mkdir(exist_ok=True)
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
g=json.loads((B/'chapter-gate.json').read_text());assert g['currentTopicId']=='l_det' and g['state']=='awaiting_user_approval'
ls=json.loads((R/'dist/lessons.json').read_text());cs=[c for w in ls for c in w['chapters']]
save(E/'prior-library.json',dict(sourceCommit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),chapterCount=len(cs),questionCount=sum(c['questionCount']for c in cs),chapters=[dict(topicId=c['topicId'],url=c['url'],sha256=hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest(),questions=c['questionCount'])for c in cs]))
for c in cs:
 if c['topicId']=='l_det':c.update(status='ready',statusLabel='Approved chapter',revisionState='student_approved',approvedVersion=80,animationReviewState='student_approved',visualRevisionState='student_approved')
save(R/'dist/lessons.json',ls)
plan=json.loads((R/'dist/schedule.en.json').read_text());have={c['topicId']for c in cs};n=next((w['number'],t)for w in plan['weeks']for u in w['units']for t in u['topicIds']if t not in have);assert n==(3,'l_spaces'),n
g.update(currentTopicId='l_spaces',state='in_progress',approvedTopicId='l_det',approvedVersion=80,nextTopicId=None,reviewScope='Only l_spaces: Vector Spaces, Subspaces, Bases, and Dimension.',activeWork='User approved l_det version 80. Preserve all 42 preceding pages and 2675 worked questions.',publicationState='not_started',publishedVersion=None,publicationRecordPath='research/l_spaces-publication.json',sourceAuditPath='research/l_spaces-source-audit.md',qualityAuditPath='research/l_spaces-quality-audit.md')
save(B/'chapter-gate.json',g)
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\n\n## Active chapter: Vector spaces — 7 October 2026\n\nExplicit approval of determinant version 80 permits only l_spaces, the next missing Week 3 topic. Preserve 42 prior pages and 2675 solved problems. Select genuinely read written courses, teach definitions and proofs deeply, provide an extensive mathematical/conceptual bank with explanatory solutions and exact final rules, and build concept-specific visual laboratories. Audit math fences and animations before delivery; await approval afterward.\n')
print(n,len(cs),sum(c['questionCount']for c in cs))
