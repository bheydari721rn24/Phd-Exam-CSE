from pathlib import Path
import json
B=Path(__file__).parent; E=B/'deep-library-revision'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
pub=read(E/'d_relations-publication.json'); assert pub['status']=='succeeded' and pub['reviewedChapters']==17
p=E/'d_relations-revision.json';d=read(p);d.update(publicationState='deployed_owner_private',publicationEvidence='research/deep-library-revision/d_relations-publication.json',deploymentId=pub['deploymentId'],publishedSourceCommit=pub['sourceCommit']);save(p,d)
p=B/'chapter-gate.json';d=read(p);d.update(publicationState='seventeen_checked_reviews_confirmed_owner_private_online',lastConfirmedPrivateDeployment=pub['deploymentId'],latestPublicationEvidence='research/deep-library-revision/d_relations-publication.json');save(p,d)
p=B.parent/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf-8');heading='## Seventeen-review private publication confirmed, 13 October 2026'
if heading not in s:s+='\n'+heading+'\n\nSource '+pub['sourceCommit']+' was privately deployed as '+pub['deploymentId']+'. The immutable 489-entry archive has SHA256 '+pub['archiveSha256']+'. GitHub branch study-planner-1406 commit 65b95ea mirrors 48 exact changed files. Seventeen checked reviews are confirmed online; forty-three remain. Continue the individual d_functions revision and preserve unfinished projection authoring.\n'
p.write_text(s,encoding='utf-8');print('Seventeen checked reviews confirmed privately deployed.')
