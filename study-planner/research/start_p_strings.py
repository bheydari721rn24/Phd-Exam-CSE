from pathlib import Path
import json,hashlib,subprocess
R=Path(__file__).resolve().parents[1];B=R/'research';E=B/'p_strings-evidence';E.mkdir(exist_ok=True)
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
g=json.loads((B/'chapter-gate.json').read_text());assert g['currentTopicId']=='i_uninformed' and g['state']=='awaiting_user_approval'
ls=json.loads((R/'dist/lessons.json').read_text());cs=[c for w in ls for c in w['chapters']]
save(E/'prior-library.json',dict(sourceCommit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),chapterCount=len(cs),questionCount=sum(c['questionCount']for c in cs),chapters=[dict(topicId=c['topicId'],url=c['url'],sha256=hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest(),questions=c['questionCount'])for c in cs]))
for c in cs:
 if c['topicId']=='i_uninformed':c.update(status='ready',statusLabel='Approved chapter',revisionState='student_approved',approvalSource='Explicit user approval, 8 October 2026',approvedVersion=81,animationReviewState='student_approved',visualRevisionState='student_approved')
save(R/'dist/lessons.json',ls)
plan=json.loads((R/'dist/schedule.en.json').read_text());have={c['topicId']for c in cs};n=next((w['number'],t)for w in plan['weeks']for u in w['units']for t in u['topicIds']if t not in have);assert n==(3,'p_strings'),n
g.update(currentTopicId='p_strings',state='in_progress',approvedTopicId='i_uninformed',approvedVersion=81,approvedDelivery='Online version 81 and GitHub',nextTopicId=None,reviewScope='Only p_strings: Strings and Terminators in C17.',activeWork='Write and audit p_strings; preserve 45 preceding pages and 2920 complete worked questions.',publicationState='not_started',publishedVersion=None,publicationRecordPath='research/p_strings-publication.json',sourceAuditPath='research/p_strings-source-audit.md',qualityAuditPath='research/p_strings-quality-audit.md',pendingPriorPublication=None)
save(B/'chapter-gate.json',g)
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\n\n## Active chapter: Strings and terminators — 8 October 2026\n\nExplicit user approval of i_uninformed (online version 81) permits only p_strings, the next missing Week 3 topic. Preserve 45 previous pages and 2920 complete problems. Use C17 contracts, deeply worked mathematical/conceptual problems, full-sentence final rules, and actual memory/string models. Await approval after delivery.\n')
print(n,len(cs),sum(c['questionCount']for c in cs))
