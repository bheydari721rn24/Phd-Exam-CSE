from pathlib import Path
import json, hashlib, subprocess
R=Path(__file__).resolve().parents[1]; B=R/'research'; E=B/'g_arithmetic-evidence'; E.mkdir(exist_ok=True)
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
gate=json.loads((B/'chapter-gate.json').read_text())
assert gate['currentTopicId']=='p_recursion'
lessons=json.loads((R/'dist/lessons.json').read_text()); cs=[c for w in lessons for c in w['chapters']]
save(E/'prior-library.json',dict(sourceCommit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),chapters=[dict(topicId=c['topicId'],url=c['url'],sha256=hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest(),questions=c['questionCount'])for c in cs]))
for c in cs:
 if c['topicId']=='p_recursion':c.update(status='ready',statusLabel='Student-approved chapter',revisionState='student_approved',approvalSource='Explicit user approval, 10 October 2026',animationReviewState='student_approved',visualRevisionState='student_approved')
save(R/'dist/lessons.json',lessons)
gate.update(currentTopicId='g_arithmetic',state='in_progress',approvedTopicId='p_recursion',nextTopicRequiresExplicitApproval=False,continuationAuthorization='Explicit user instruction on 10 October 2026 authorizes continuous sequential writing of following chapters; quality review remains mandatory and completed unapproved chapters stay review drafts.',rule='Author one chapter at a time, finish its source, mathematical, problem, visual and browser audits, deliver as a review draft, then continue under standing user authorization. Never label an unapproved draft student-approved.',activeWork='Write and audit g_arithmetic; preserve all 47 prior chapter bodies and questions.',sourceAuditPath='research/g_arithmetic-source-audit.md',qualityAuditPath='research/g_arithmetic-quality-audit.md',nextReview='Complete arithmetic chapter quality audit before the next chapter.',reviewScope='g_arithmetic: adders, comparators, arithmetic circuits')
save(B/'chapter-gate.json',gate)
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\n\n## Standing continuation authorization — 10 October 2026\n\nThe student explicitly approved the delivered simulation correction and authorized continuous sequential writing of following chapters. This supersedes prior per-chapter stop instructions for starting the next chapter. Finish and audit one chapter before starting another. Retain every quality criterion; completed unapproved notes remain review drafts rather than student-approved chapters. The next missing topic is g_arithmetic, followed by g_mux. No production timetable or autonomous runtime guarantee is implied.\n')
print('Approved p_recursion; started g_arithmetic under standing sequential authorization.')
