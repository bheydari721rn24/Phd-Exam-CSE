from pathlib import Path
import json,hashlib,subprocess
R=Path(__file__).resolve().parents[1];B=R/'research';E=B/'i_agents-evidence';E.mkdir(exist_ok=True)
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
g=json.loads((B/'chapter-gate.json').read_text());assert g['currentTopicId']=='l_spaces' and g['state']=='awaiting_user_approval'
ls=json.loads((R/'dist/lessons.json').read_text());cs=[c for w in ls for c in w['chapters']]
save(E/'prior-library.json',dict(sourceCommit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),chapterCount=len(cs),questionCount=sum(c['questionCount']for c in cs),chapters=[dict(topicId=c['topicId'],url=c['url'],sha256=hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest(),questions=c['questionCount'])for c in cs]))
for c in cs:
 if c['topicId']=='l_spaces':
  c.update(status='ready',statusLabel='Approved chapter',revisionState='student_approved',approvalSource='Explicit user approval of local/GitHub delivery, 8 October 2026',animationReviewState='student_approved',visualRevisionState='student_approved');c.pop('approvedVersion',None)
save(R/'dist/lessons.json',ls)
plan=json.loads((R/'dist/schedule.en.json').read_text());have={c['topicId']for c in cs};n=next((w['number'],t)for w in plan['weeks']for u in w['units']for t in u['topicIds']if t not in have);assert n==(3,'i_agents'),n
g.update(currentTopicId='i_agents',state='in_progress',approvedTopicId='l_spaces',approvedVersion=None,approvedDelivery='Local and GitHub; online l_spaces publication remains pending',nextTopicId=None,reviewScope='Only i_agents: Intelligent Agents, Rationality, Task Environments, and Problem Formulation.',activeWork='Write and audit i_agents; preserve 43 preceding pages and 2757 complete worked questions.',publicationState='not_started',publishedVersion=None,publicationRecordPath='research/i_agents-publication.json',sourceAuditPath='research/i_agents-source-audit.md',qualityAuditPath='research/i_agents-quality-audit.md',pendingPriorPublication='research/l_spaces-publication.json')
save(B/'chapter-gate.json',g)
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\n\n## Active chapter: Intelligent agents — 8 October 2026\n\nExplicit user approval of the local and GitHub vector-space delivery permits only i_agents, the next missing Week 3 topic. No online version is invented for the pending vector-space upload. Preserve 43 previous pages and 2,757 complete problems. Review written university courses, develop rigorous mathematical and conceptual problems with fully worked solutions and strong final rules, and implement subject-specific agent models. Await approval after delivery.\n')
print(n,len(cs),sum(c['questionCount']for c in cs))
