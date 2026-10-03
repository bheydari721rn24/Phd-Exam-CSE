"""Retain explicit approval of the v56 library across legacy rebuilds."""
import hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def preserve_approval():
    ledger=ROOT/'research/library-approval.json'
    if not ledger.exists():return
    approval=json.loads(ledger.read_text());approved=set(approval['approvedTopics'])
    p=ROOT/'dist/lessons.json';lessons=json.loads(p.read_text())
    for week in lessons:
        for c in week['chapters']:
            if c['topicId'] not in approved:continue
            version=approval.get('approvalByTopic',{}).get(c['topicId'],{}).get('version',approval['approvedSiteVersion'])
            c.update(status='ready',statusLabel='Student-approved chapter',revisionState='exam_grounded_approved',approvedVersion=version)
            page=ROOT/'dist'/c['url'];s=page.read_text(encoding='utf-8')
            s=s.replace('Examination revision draft ·','Student-approved chapter ·')
            s=s.replace('Review draft ·','Student-approved chapter ·')
            page.write_text(s,encoding='utf-8')
    p.write_text(json.dumps(lessons,indent=2)+chr(10),encoding='utf-8')
    p=ROOT/'dist/library-review.html'
    if p.exists():
        s=p.read_text(encoding='utf-8').replace('All 22 chapters remain revision drafts pending explicit approval.','The user approved all 22 revised chapters in version 56 on 3 October 2026.').replace('No new chapter has been started.','The next chapter is prepared separately as a review draft.').replace('awaiting approval</p>','student-approved</p>')
        p.write_text(s,encoding='utf-8')
    p=ROOT/'research/exam-calibration/DELIVERY.en.md'
    if p.exists():
        s=p.read_text(encoding='utf-8').replace('All chapters remain drafts. Await explicit approval before promoting this revision or starting another chapter. Preserve study progress.','The user approved all 22 revised chapters in version 56 on 3 October 2026. Preserve this approval through rebuilds. Newly authored chapters require their own explicit approval. Preserve study progress.')
        p.write_text(s,encoding='utf-8')
    if (ROOT/'dist/chapters/concept-animations.json').exists():
        from build_concept_animations import install_animations
        install_animations()
    for name in ['research/exam-calibration/manifest.json','dist/evidence/exam-calibration/manifest.json']:
        p=ROOT/name
        if p.exists():
            m=json.loads(p.read_text());m['state']='student_approved';m['approvedSiteVersion']=approval['approvedSiteVersion']
            for c in m['chapters']:c['htmlSha256']=hashlib.sha256((ROOT/'dist/chapters'/(c['topicId']+'.html')).read_bytes()).hexdigest()
            p.write_text(json.dumps(m,indent=2)+chr(10),encoding='utf-8')
if __name__=='__main__':preserve_approval()
