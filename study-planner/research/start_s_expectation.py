from pathlib import Path
import json,hashlib,subprocess
R=Path(__file__).resolve().parents[1];B=R/'research';O=B/'s_expectation-evidence';O.mkdir(exist_ok=True)
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
g=json.loads((B/'chapter-gate.json').read_text());assert g['currentTopicId']=='s_discrete' and g['state']=='awaiting_user_approval'
ls=json.loads((R/'dist/lessons.json').read_text());cs=[c for w in ls for c in w['chapters']]
save(O/'prior-library.json',dict(sourceCommit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),chapterCount=len(cs),questionCount=sum(c['questionCount'] for c in cs),chapters=[dict(topicId=c['topicId'],url=c['url'],sha256=hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest(),questions=c['questionCount']) for c in cs]))
for c in cs:
 if c['topicId']=='s_discrete':c.update(status='ready',statusLabel='Approved chapter',revisionState='student_approved',approvedVersion=77,animationReviewState='student_approved',visualRevisionState='student_approved')
save(R/'dist/lessons.json',ls)
plan=json.loads((R/'dist/schedule.en.json').read_text());have={c['topicId'] for c in cs};n=next((w['number'],t) for w in plan['weeks'] for u in w['units'] for t in u['topicIds'] if t not in have);assert n==(3,'s_expectation'),n
g.update(currentTopicId='s_expectation',state='in_progress',approvedTopicId='s_discrete',approvedVersion=77,nextTopicId=None,reviewScope='Only s_expectation: Expectation and Its Linearity.',activeWork='Explicit approval permits one next chapter. Preserve 40 preceding chapters and 2511 complete worked problems.',publicationState='not_started',publishedVersion=None,publicationRecordPath='research/s_expectation-publication.json',sourceAuditPath='research/s_expectation-source-audit.md',qualityAuditPath='research/s_expectation-quality-audit.md')
save(B/'chapter-gate.json',g)
with (R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8') as f:f.write('\n\n## Active chapter: Expectation and Its Linearity — 7 October 2026\n\nThe student explicitly approved s_discrete version 77. Work only on the next missing Week 3 chapter s_expectation, preserving the 40 preceding chapter files and 2511 complete solved problems. Deep English instruction, genuinely reviewed courses, mathematical/conceptual solved problems, strong final notes and concept-specific visual reasoning remain required. Await explicit approval after delivery.\n')
print('s_expectation active; previous approval recorded; retention baseline captured.')
