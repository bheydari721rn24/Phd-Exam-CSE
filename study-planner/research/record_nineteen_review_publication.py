from pathlib import Path
import json
B=Path(__file__).parent;E=B/'deep-library-revision'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
pub=read(E/'d_invariants-publication.json');assert pub['status']=='succeeded'and pub['reviewedChapters']==19
p=E/'d_invariants-revision.json';d=read(p);d.update(publicationState='deployed_owner_private',publicationEvidence='research/deep-library-revision/d_invariants-publication.json',deploymentId=pub['deploymentId'],publishedSourceCommit=pub['sourceCommit']);save(p,d)
p=B/'chapter-gate.json';d=read(p);d.update(publicationState='nineteen_checked_reviews_confirmed_owner_private_online',lastConfirmedPrivateDeployment=pub['deploymentId'],latestPublicationEvidence='research/deep-library-revision/d_invariants-publication.json');save(p,d)
p=B.parent/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf-8');h='## Nineteen-review private publication confirmed, 13 October 2026'
if h not in s:s+='\n'+h+'\n\nSource '+pub['sourceCommit']+' was privately deployed as '+pub['deploymentId']+'. The immutable 489-entry archive has SHA256 '+pub['archiveSha256']+'. GitHub branch study-planner-1406 commit 117bc3c mirrors 47 exact changed files. Nineteen checked reviews are confirmed online; forty-one remain. Continue d_number and preserve unfinished projection authoring.\n'
p.write_text(s,encoding='utf-8');print('Nineteen checked reviews confirmed privately deployed.')
