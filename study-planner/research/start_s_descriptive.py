from pathlib import Path
import json,hashlib,subprocess
R=Path(__file__).resolve().parents[1];B=R/'research';O=B/'s_descriptive-evidence';O.mkdir(exist_ok=True)
def save(p,d):p.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
g=json.loads((B/'chapter-gate.json').read_text());assert g['currentTopicId']=='a_select' and g['state']=='awaiting_user_approval'
lessons=json.loads((R/'dist/lessons.json').read_text());cs=[c for w in lessons for c in w['chapters']]
save(O/'prior-library.json',dict(sourceCommit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),chapterCount=len(cs),questionCount=sum(c['questionCount'] for c in cs),chapters=[dict(topicId=c['topicId'],url=c['url'],sha256=hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest(),questions=c['questionCount']) for c in cs]))
for c in cs:
 if c['topicId']=='a_select':c.update(status='ready',statusLabel='Approved chapter',revisionState='student_approved',animationReviewState='student_approved',visualRevisionState='student_approved')
save(R/'dist/lessons.json',lessons)
g.update(currentTopicId='s_descriptive',state='in_progress',approvedTopicId='a_select',approvedVersion=74,nextTopicId=None,proposedNextTopicId=None,reviewScope='Only s_descriptive: Descriptive Statistics and Exploratory Data Analysis.',activeWork='Write only s_descriptive. The student explicitly approved a_select; preserve 38 preceding chapters and 2346 complete questions.',sourceAuditPath='research/s_descriptive-source-audit.md',qualityAuditPath='research/s_descriptive-quality-audit.md',sourceAudit='research/s_descriptive-source-audit.md',qualityAudit='research/s_descriptive-quality-audit.md',publicationState='not_started',publicationRecordPath='research/s_descriptive-publication.json')
g.pop('delivery',None);save(B/'chapter-gate.json',g)
with (R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8') as f:f.write('\n\n## Active chapter: Descriptive Statistics, 6 October 2026\n\nExplicit approval of a_select version 74 authorizes only s_descriptive. Preserve all 38 preceding chapter pages and 2346 complete question bodies. Deep English instruction, genuinely reviewed written courses, mathematical/conceptual problems, complete review rules and concept-specific animated visual instruction remain required. Deliver the complete draft and await explicit approval.\n')
print('Only s_descriptive active; a_select approved; 38 chapter pages retained.')
