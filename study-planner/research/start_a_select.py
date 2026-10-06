"""Record explicit approval and the sole next scheduled chapter."""
from pathlib import Path
import json,hashlib,subprocess
R=Path(__file__).resolve().parents[1];B=R/'research';O=B/'a_select-evidence';O.mkdir(exist_ok=True)
def save(p,d):p.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
gate=json.loads((B/'chapter-gate.json').read_text(encoding='utf-8'));assert gate['currentTopicId']=='a_sort' and gate['publishedVersion']==73
baseline=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip()
chapters=[c for w in json.loads((R/'dist/lessons.json').read_text(encoding='utf-8')) for c in w['chapters']]
save(O/'prior-library.json',dict(sourceCommit=baseline,chapterCount=len(chapters),questionCount=sum(c['questionCount'] for c in chapters),chapters=[dict(topicId=c['topicId'],sha256=hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest(),questions=c['questionCount']) for c in chapters]))
approval=json.loads((B/'library-animation-redesign/inventory.json').read_text(encoding='utf-8'));approval.update(state='student_approved',approvedVersion=73,approvalDate='2026-10-06');save(B/'library-animation-redesign/inventory.json',approval)
lessons=json.loads((R/'dist/lessons.json').read_text(encoding='utf-8'))
for w in lessons:
 for c in w['chapters']:c['libraryDecisionRevisionState']='student_approved'
save(R/'dist/lessons.json',lessons)
gate.update(currentTopicId='a_select',state='in_progress',nextTopicId=None,approvedVersion=73,approvedLibraryAnimationRevision=True,reviewScope='Only a_select: Searching, Selection, and Order Statistics.',activeWork='The user approved the version-73 library and requested the next chapter. Write the complete English a_select review draft; preserve all 37 previous chapters and 2257 question bodies.',sourceAuditPath='research/a_select-source-audit.md',qualityAuditPath='research/a_select-quality-audit.md',sourceAudit='research/a_select-source-audit.md',qualityAudit='research/a_select-quality-audit.md',publicationState='not_started',publicationRecordPath='research/a_select-publication.json',nextReview='Deliver a_select after source, mathematics, questions, animated instruction and real browser checks; await explicit approval before another chapter.')
save(B/'chapter-gate.json',gate)
with (R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8') as f:f.write('\n\n## Active chapter: Searching, Selection, and Order Statistics — 6 October 2026\n\nThe student explicitly approved the version-73 animation redesign and requested the next scheduled missing chapter a_select. Preserve the 37 existing chapter pages and all 2257 complete question bodies. Work only on this English chapter: genuinely compare written university courses, teach prerequisites through advanced boundary cases, provide a large mathematical/conceptual solved bank and complete final rules, and build exact decision-led, subject-specific models and editable laboratories. Deliver the complete review draft, then wait for explicit approval. Do not ask the student test questions before first reading.\n')
print('Approved library version 73; active chapter a_select; 37 preceding chapters retained.')
