from pathlib import Path
import json
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
pub=read(E/'l_matrices-publication.json');assert pub['status']=='succeeded' and len(pub['includedRevisions'])==11
for topic in ['l_vectors','l_matrices']:
 p=E/(topic+'-revision.json');d=read(p);d.update(publicationState='deployed_private',publicationRecord='research/deep-library-revision/l_matrices-publication.json');save(p,d)
p=E/'l_vectors-publication.json';d=read(p);d.update(supersededBy='research/deep-library-revision/l_matrices-publication.json',note='Historical unsuccessful vector-only upload attempts. The exact later eleven-review archive privately deployed successfully and includes the vector edition; see supersededBy.');save(p,d)
p=B/'chapter-gate.json';d=read(p);d.update(publicationState='eleven_individually_reviewed_chapters_confirmed_online',latestLibraryRevisionPublication=pub,latestConfirmedSiteContentCommit=pub['sourceCommit'],qualityAuditPath='research/deep-library-revision/l_matrices-revision.json');save(p,d)
p=R/'WEEKLY_DELIVERY.md';s=p.read_text();heading='## Confirmed eleven-review private publication, 12 October 2026'
if heading not in s:s+='\n'+heading+'\n\nThe exact source commit 44c760435cb24a1f7eaafac9bfb15905c818e305 and GitHub content commit 3b9fbef contain eleven individually checked review drafts. The immutable 489-entry archive, SHA-256 d5c55a618a968ece3a0f0c2e8ac454c9a5cbf61162b8265de66ae0a19e7872cd, privately deployed successfully as '+pub['deploymentId']+'. Vectors and matrices are now online together with the previous nine reviews. The three historical vector-only upload failures are superseded. The remaining 49 existing chapters are not represented as individually revised. Continue p_types; preserve unfinished l_projection authoring.\n'
p.write_text(s,encoding='utf-8')
print('Recorded successful private publication of all eleven checked reviews.')
