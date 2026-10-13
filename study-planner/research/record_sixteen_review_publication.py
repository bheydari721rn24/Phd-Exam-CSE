from pathlib import Path
import json
B=Path(__file__).parent;E=B/'deep-library-revision'
def read(p):return json.loads(p.read_text())
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
pub=read(E/'g_gates-publication.json');assert pub['status']=='succeeded'and pub['reviewedChapters']==16
p=E/'g_gates-revision.json';x=read(p);x.update(publicationState='deployed_owner_private',publicationEvidence='research/deep-library-revision/g_gates-publication.json',deploymentId=pub['deploymentId'],publishedSourceCommit=pub['sourceCommit']);save(p,x)
p=B/'chapter-gate.json';x=read(p);x.update(publicationState='sixteen_checked_reviews_confirmed_owner_private_online',lastConfirmedPrivateDeployment=pub['deploymentId'],latestPublicationEvidence='research/deep-library-revision/g_gates-publication.json');save(p,x)
p=B.parent/'WEEKLY_DELIVERY.md';s=p.read_text();heading='## Sixteen-review private publication confirmed, 13 October 2026'
if heading not in s:s+='\n'+heading+'\n\nSource '+pub['sourceCommit']+' was privately deployed as '+pub['deploymentId']+'. The immutable 489-entry archive has SHA256 '+pub['archiveSha256']+'. GitHub branch study-planner-1406 commit 8f9ea48 mirrors 37 exact changed files. Sixteen checked reviews are confirmed online; forty-four remain. Continue the individual d_relations review and preserve unfinished projection authoring.\n'
p.write_text(s,encoding='utf-8');print('Sixteen checked reviews confirmed privately deployed.')
