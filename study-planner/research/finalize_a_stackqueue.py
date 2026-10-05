"""Record a verified review draft; never promote it without explicit student approval."""
from pathlib import Path
import json,re,hashlib
B=Path(__file__).resolve().parent;R=B.parent
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
v=read(B/'a_stackqueue-verification.json');qa=read(B/'a_stackqueue-browser-audit.json');assert v['state']==qa['state']=='passed';assert v['checks']['approvedChapterRetention']==35
reading=dict(topicId='a_stackqueue',date='2026-10-05',primaryCourses=[
 dict(university='Princeton',course='COS226',scope='All 45 pages of Stacks and Queues I, Spring 2026',method='Complete locally extracted PDF text read this turn',sha256='931a3f25394aa7007415f1d6057453d8b0cce1b385730a9c66fc134793917182'),
 dict(university='Oxford',course='B16',scope='Complete Sections 3.3 and 3.4; relevant linked-list representation passages in 3.5',method='Written course HTML read/rechecked through browser and extracted text',sha256='454fea4fd1fb9238763f2f61f042e5132ff27a215d10faf22b806f886abb615f'),
 dict(university='Carnegie Mellon',course='15-122',scope='Lecture 9, all 19 pages, including six exercises and sample solutions',method='Complete primary-source browser text read this turn; local PDF download failed'),
 dict(university='Stanford',course='CS106B',scope='All 45 PDF pages; technical passages pages 8-29 and 33-45',method='Complete locally extracted text read this turn',sha256='32e47368a23a57c8d33dab53a8291683d421c26948a8b8183d2682e40af10b00')],complementaryCourses=[
 dict(university='MIT',course='6.006',scope='Problem Session 1, Problems 1-2 and 1-3, pages 2-3',method='Primary-source browser text; six-page PDF acquired, only relevant passages counted as read',sha256='b418d0e4795d3762fced7bbe8e09c7f105d4cf45a878fdf455151369dd860c5d'),
 dict(university='Berkeley',course='CS61B',scope='Previously reviewed Chapters 4-5; DLLists rechecked for sentinel/end operations',method='Written textbook recheck; not a newly read full anchor'),
 dict(university='Cornell',course='CS2110',scope='Previously screened linked-list invariants',method='Candidate context; not newly read anchor')],comparisonAudit='a_stackqueue-source-audit.md',limits='Bounded documented candidate pool; no exhaustive worldwide-course claim.',authenticExaminationItems=read(B/'a_stackqueue-authentic.json'))
save(B/'a_stackqueue-reading.json',reading)
downloads=read(B/'a_stackqueue-downloads.json')
for x in downloads:
 if x['key']=='stanford':x['state']='downloaded_and_read_complete';x['readingLedger']='a_stackqueue-reading.json'
 if x['key']=='mit':x['state']='downloaded_relevant_pages_read';x['readingLedger']='a_stackqueue-reading.json'
save(B/'a_stackqueue-downloads.json',downloads)
gate=read(B/'chapter-gate.json');assert gate['currentTopicId']=='a_stackqueue'
gate.update(state='awaiting_user_approval',nextTopicId=None,proposedNextTopicId=None,sourceAudit='research/a_stackqueue-source-audit.md',qualityAudit='research/a_stackqueue-quality-audit.md',lastCompletedReview='Stacks, Queues, and Applications: complete English review draft; 84 solved questions, 80 rules, 67 models and five editable laboratories.',nextReview='Wait for explicit approval of a_stackqueue. Do not begin another chapter.',reviewEvidence=['research/a_stackqueue-reading.json','research/a_stackqueue-source-audit.md','research/a_stackqueue-quality-audit.md','research/a_stackqueue-verification.json','research/a_stackqueue-browser-audit.json'],delivery=dict(date='2026-10-05',topicId='a_stackqueue',status='complete_review_draft',url='chapters/a_stackqueue.html',questions=84,authenticQuestions=3,originalQuestions=81,examRules=80,visualModels=67,checkpoints=678,editableLaboratories=5))
save(B/'chapter-gate.json',gate)
delivery='''# Stacks, Queues, and Applications — review draft

Completed 5 October 2026. The sole new chapter is `a_stackqueue`. Four actually reviewed primary university courses, 84 fully solved problems, 80 final rules, 67 topic-specific models with 678 checkpoints, and five editable laboratories are included. All 35 preceding chapter bodies retain their original SHA-256 hashes and their 2,085 problems.

The chapter is available at `dist/chapters/a_stackqueue.html`; the library links it under Week 3. Source, reading, mathematical and browser audit evidence is adjacent in `research/a_stackqueue-*`. The gate is `awaiting_user_approval`. No next chapter is started. Publishing and GitHub delivery are recorded separately after their actual completion.
'''
(B/'a_stackqueue-DELIVERY.en.md').write_text(delivery,encoding='utf-8')
p=R/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf-8');marker='## Completed draft: Stacks, Queues, and Applications'
if marker not in s:p.write_text(s+'\n\n'+marker+'\n\n'+delivery.split('\n',1)[1],encoding='utf-8')
print('Recorded complete chapter draft; gate awaits explicit approval.')
