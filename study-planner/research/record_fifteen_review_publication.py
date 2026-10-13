from pathlib import Path
import json
B=Path(__file__).parent;E=B/'deep-library-revision'
def read(p):return json.loads(p.read_text())
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
pub=read(E/'g_boolean-publication.json');assert pub['status']=='succeeded'and pub['reviewedChapters']==15
p=E/'g_boolean-revision.json';x=read(p);x.update(publicationState='deployed_owner_private',publicationEvidence='research/deep-library-revision/g_boolean-publication.json',deploymentId=pub['deploymentId'],publishedSourceCommit=pub['sourceCommit']);save(p,x)
p=B/'chapter-gate.json';x=read(p);x.update(publicationState='fifteen_checked_reviews_confirmed_owner_private_online',lastConfirmedPrivateDeployment=pub['deploymentId'],latestPublicationEvidence='research/deep-library-revision/g_boolean-publication.json');save(p,x)
p=B.parent/'WEEKLY_DELIVERY.md';s=p.read_text();heading='## Fifteen-review private publication confirmed, 13 October 2026'
if heading not in s:s+='\n'+heading+'\n\nSource '+pub['sourceCommit']+' was privately deployed as '+pub['deploymentId']+'. The immutable 489-entry archive has SHA256 '+pub['archiveSha256']+'. GitHub branch study-planner-1406 commit 817f268 mirrors 35 exact changed files. Fifteen checked reviews are confirmed online; forty-five remain. Continue the individual g_gates review and preserve unfinished projection authoring.\n'
p.write_text(s,encoding='utf-8');print('Fifteen checked reviews confirmed privately deployed.')
