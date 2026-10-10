from pathlib import Path
import json
B=Path(__file__).resolve().parent;R=B.parent
x=json.loads(Path('C:/Users/bheydari/AppData/Local/Temp/a-bst-reviewed.tar.receipt.json').read_text())
r=dict(status='published_private',projectId=x['project_id'],sourceCommit=x['commit_sha'],archiveSha256=x['archiveSha256'],archiveEntries=x['files'],versionId='appgprj_6ab5666f72b081918286c6b371c1eb1b~appgver_9cd1190223e48191889977e1bc922ef6',deploymentId='appgdep_6aca943b37948191b5e7357e5b0bc55b',deploymentStatus='succeeded',updatedAt='2026-10-10T19:38:47.744053+00:00',url='https://phd-cse-1406-plan.bheydari-as721rn.chatgpt.site',githubBranch='study-planner-1406',githubContentCommit='84bec74',chaptersAdded=['a_bst'],libraryChapters=52,questions=3493,sourcePushEvidence='Bundled workflow verified pushed SHA and clean source tree before Windows packaging failed; independently byte-verified archive from that exact source supplied to native private save/deploy.',verificationLimit='Native deployment returned succeeded; numeric site version is not invented.')
(B/'a_bst-publication.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
g=json.loads((B/'chapter-gate.json').read_text());g['latestPublication']=r
for q in g['completedReviewDrafts']:
 if q['topicId']=='a_bst':q.update(publicationState='published_private',publicationRecord='research/a_bst-publication.json')
(B/'chapter-gate.json').write_text(json.dumps(g,indent=2)+'\n',encoding='utf-8')
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\n\n## BST privately published — 10 October 2026\n\nNative private deployment appgdep_6aca943b37948191b5e7357e5b0bc55b succeeded from exact pushed source 2aa5cfe5735c24f7716cee0ca378ca17f61a34ff and the byte-verified 440-entry archive. GitHub content commit 84bec74. Library: 52 chapters / 3493 worked questions. The chapter remains an unapproved review draft. Continuous authoring proceeds to balanced trees. See research/a_bst-publication.json.\n')
print('Recorded successful BST private deployment.')
