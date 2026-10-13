from pathlib import Path
import json
B=Path(__file__).parent;E=B/'deep-library-revision'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
pub=read(E/'d_functions-publication.json');assert pub['status']=='succeeded' and pub['reviewedChapters']==18
p=E/'d_functions-revision.json';d=read(p);d.update(publicationState='deployed_owner_private',publicationEvidence='research/deep-library-revision/d_functions-publication.json',deploymentId=pub['deploymentId'],publishedSourceCommit=pub['sourceCommit']);save(p,d)
p=B/'chapter-gate.json';d=read(p);d.update(publicationState='eighteen_checked_reviews_confirmed_owner_private_online',lastConfirmedPrivateDeployment=pub['deploymentId'],latestPublicationEvidence='research/deep-library-revision/d_functions-publication.json');save(p,d)
p=B.parent/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf-8');h='## Eighteen-review private publication confirmed, 13 October 2026'
if h not in s:s+='\n'+h+'\n\nSource '+pub['sourceCommit']+' was privately deployed as '+pub['deploymentId']+'. The immutable 489-entry archive has SHA256 '+pub['archiveSha256']+'. GitHub branch study-planner-1406 commit a65f20c mirrors 50 exact changed files. Eighteen checked reviews are confirmed online; forty-two remain. Continue d_invariants and preserve unfinished projection authoring.\n'
p.write_text(s,encoding='utf-8');print('Eighteen checked reviews confirmed privately deployed.')
