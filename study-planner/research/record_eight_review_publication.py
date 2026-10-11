from pathlib import Path
import json
B=Path(__file__).resolve().parent;R=B.parent;E=B/'deep-library-revision'
def read(p):return json.loads(p.read_text())
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
publication=read(E/'s_axioms-publication.json');assert publication['status']=='succeeded' and len(publication['includedRevisions'])==8
for topic in ['a_asym','a_loop','s_axioms']:
 p=E/(topic+'-revision.json');d=read(p);assert d['status']=='revised_checked_review_draft';d.update(publicationState='deployed_private',publicationRecord='research/deep-library-revision/s_axioms-publication.json');save(p,d)
for topic in ['a_asym','a_loop']:
 p=E/(topic+'-publication.json');d=read(p);d['supersededBy']='research/deep-library-revision/s_axioms-publication.json';d['note']='Historical failed upload attempt. The exact later eight-review immutable archive was successfully published privately; see supersededBy for the current confirmed deployment.';save(p,d)
p=B/'chapter-gate.json';d=read(p);d.update(publicationState='eight_individually_revised_chapters_deployed_private',latestLibraryRevisionPublication=publication,qualityAuditPath='research/deep-library-revision/s_axioms-revision.json');save(p,d)
p=R/'WEEKLY_DELIVERY.md';s=p.read_text();heading='## Confirmed eight-review private publication, 12 October 2026'
if heading not in s:s+='\n'+heading+'\n\nThe source commit cac0ef58f67a154295bc10f557b00dd6a3989a1e and GitHub content commit 4a96fb9 contain eight individually revised review drafts. The 489-entry byte-verified archive (SHA-256 89a56713899d5e13b1c82af4c7ec7d0e96e2aae2c34e8491fa17064ca9f790b1) was saved and privately deployed successfully as appgdep_6acc0c3c7a048191bd517ab26e3b8172. Asymptotic, loop and probability revisions are now online together with the earlier five. Historical failed uploads are retained as superseded attempts. Continue s_counting; 52 individual chapter reviews remain.\n'
p.write_text(s,encoding='utf-8');print('Recorded confirmed private publication of all eight completed reviews.')
