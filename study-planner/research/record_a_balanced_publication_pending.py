from pathlib import Path
import json,hashlib,tarfile,subprocess
B=Path(__file__).resolve().parent;R=B.parent
p=Path('C:/Users/bheydari/AppData/Local/Temp/a-balanced-reviewed.tar.receipt.json');x=json.loads(p.read_text())
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip()==x['commit_sha']
with tarfile.open(x['archive'],'r:gz')as t:
 for m in t.getmembers():assert t.extractfile(m).read()==(R/m.name).read_bytes()
x.update(sourcePushState='verified_by_bundled_workflow_before_windows_package_failure',onlinePublicationState='unconfirmed_transport_failure')
p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
r=dict(status='publication_unconfirmed',projectId=x['project_id'],sourceCommit=x['commit_sha'],archiveSha256=x['archiveSha256'],archiveEntries=x['files'],archive=x['archive'],githubBranch='study-planner-1406',githubContentCommit='5e158f3',chaptersAdded=['a_balanced'],libraryChapters=53,questions=3575,reason='Native private save/deploy returned transport error. Reconciliation list_site_versions also failed. A saved version may exist, so inspect matching source before retrying save/deploy.',verified='Exact source pushed and clean-state/remote-SHA verification passed before bundled Windows packaging failed; independently byte-verified archive is retained.')
(B/'a_balanced-publication-pending.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
g=json.loads((B/'chapter-gate.json').read_text());g['pendingPriorPublication']=r;g['publicationState']='unconfirmed_transport_failure'
for q in g['completedReviewDrafts']:
 if q['topicId']=='a_balanced':q.update(publicationState='unconfirmed_transport_failure',publicationRecord='research/a_balanced-publication-pending.json')
(B/'chapter-gate.json').write_text(json.dumps(g,indent=2)+'\n',encoding='utf-8')
print('Recorded unconfirmed publication and byte-verified archive; no success claimed.')
