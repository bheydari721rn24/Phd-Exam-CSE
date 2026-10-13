from pathlib import Path
import json
B=Path(__file__).parent;E=B/'deep-library-revision'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
pub=read(E/'p_flow-publication.json');assert pub['status']=='succeeded' and pub['reviewedChapters']==13
for topic in ['p_types','p_flow']:
 p=E/(topic+'-revision.json');v=read(p);v.update(publicationState='deployed_owner_private',publicationEvidence='research/deep-library-revision/p_flow-publication.json',deploymentId=pub['deploymentId'],publishedSourceCommit=pub['sourceCommit']);save(p,v)
p=E/'p_types-publication.json';v=read(p);v.update(supersededBySuccessfulDeployment=pub['deploymentId'],supersedingSourceCommit=pub['sourceCommit']);save(p,v)
p=B/'chapter-gate.json';v=read(p);v.update(publicationState='thirteen_checked_reviews_confirmed_owner_private_online',lastConfirmedPrivateDeployment=pub['deploymentId']);save(p,v)
p=B.parent/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf-8');heading='## Thirteen-review private publication confirmed, 13 October 2026'
if heading not in s:s+='\n'+heading+'\n\nThe immutable source77bb96d8943bae3480a2f90cde622447d29587d4 (489 archive entries; SHA256edbed361e702334563162a39df0e5099d35c14457e8acb482498bf1ee05d8392) was privately published successfully. Deployment'+pub['deploymentId']+' owns the exact saved version. GitHub branchstudy-planner-1406 commit240c9dc mirrors43 exact changed files. All13 checked reviews, including p_types and p_flow, are now confirmed online. Prior failed uploads are retained and superseded. Continue g_number;47 individual reviews remain.\n'
p.write_text(s,encoding='utf-8');print('Thirteen checked reviews confirmed privately deployed.')
