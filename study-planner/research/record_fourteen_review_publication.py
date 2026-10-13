from pathlib import Path
import json
B=Path(__file__).parent;E=B/'deep-library-revision'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
pub=read(E/'g_number-publication.json');assert pub['status']=='succeeded' and pub['reviewedChapters']==14
p=E/'g_number-revision.json';v=read(p);v.update(publicationState='deployed_owner_private',publicationEvidence='research/deep-library-revision/g_number-publication.json',deploymentId=pub['deploymentId'],publishedSourceCommit=pub['sourceCommit']);save(p,v)
p=B/'chapter-gate.json';v=read(p);v.update(publicationState='fourteen_checked_reviews_confirmed_owner_private_online',lastConfirmedPrivateDeployment=pub['deploymentId'],sourceAuditPath='research/g_boolean-source-audit.md');save(p,v)
p=B.parent/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf-8');heading='## Fourteen-review private publication confirmed, 13 October 2026'
if heading not in s:s+='\n'+heading+'\n\nSource2e0c78831f2630bf2ad888eee6f66d84ed60be5b was privately deployed successfully as'+pub['deploymentId']+'. The immutable489-entry archive has SHA256f65b2803003c099c85da301031e9efef9b98366d9ef49623b6097cde8482815d. GitHub branchstudy-planner-1406 commitbacee04 mirrors35 exact changed files. Fourteen checked reviews are confirmed online;46 remain. Continue g_boolean and retain unfinished l_projection authoring.\n'
p.write_text(s,encoding='utf-8');print('Fourteen checked reviews confirmed privately deployed.')
