from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent;R=B.parent
archive=Path('C:/Users/bheydari/AppData/Local/Temp/a-hash-reviewed.tar.gz');digest=hashlib.sha256(archive.read_bytes()).hexdigest();assert digest=='0d7b27941c2109919de4ab335934401351f80bd95277f8bf78234f23e5a10463'
x=dict(status='publication_pending_archive_upload',projectId='appgprj_6ab5666f72b081918286c6b371c1eb1b',sourceCommit='23744d2aea44e0d5dc38f018662d26ca8ea1e020',archive=str(archive),archiveSha256=digest,archiveEntries=458,githubContentCommit='6a20214',githubBranch='study-planner-1406',chaptersAdded=['a_balanced','a_heap','a_hash'],libraryChapters=55,questions=3739,reason='Fresh native source credential succeeded. Bundled workflow pushed exact source and passed remote-SHA/clean-source verification before its Windows packaging step failed. Independently byte-verified committed-blob archive was supplied to native private save/deploy, which failed before upload at backend-api/files. No saved version or deployment was returned.',lastConfirmedOnlineSource='2aa5cfe5735c24f7716cee0ca378ca17f61a34ff')
(B/'a_hash-publication-pending.json').write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
g=json.loads((B/'chapter-gate.json').read_text());g['publicationState']=x['status'];g['publicationRecordPath']='research/a_hash-publication-pending.json'
for q in g['completedReviewDrafts']:
 if q['topicId']in x['chaptersAdded']:q.update(publicationState=x['status'],publicationRecord='research/a_hash-publication-pending.json')
(B/'chapter-gate.json').write_text(json.dumps(g,indent=2)+'\n',encoding='utf-8')
print('Recorded archive-upload blocker; reviewed source is pushed to GitHub and Sites, publication remains unconfirmed.')
