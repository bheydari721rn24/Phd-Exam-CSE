from pathlib import Path
import json
B=Path(__file__).resolve().parent;R=B.parent
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=dict(status='published_private',projectId='appgprj_6ab5666f72b081918286c6b371c1eb1b',sourceCommit='7ac738a54daf26186045b4e654e9e1ae40879533',versionId='appgprj_6ab5666f72b081918286c6b371c1eb1b~appgver_db6c4bb162ec81919791532b6f1b5d1d',deploymentId='appgdep_6acba5778a1c8191a7d54578c4d085e9',deploymentStatus='succeeded',url='https://phd-cse-1406-plan.bheydari-as721rn.chatgpt.site',updatedAt='2026-10-11T15:04:49.638772+00:00',archive='C:/Users/bheydari/AppData/Local/Temp/l-orthogonality-reviewed-pushed.tar.gz',archiveSha256='3dbd6524d16eca414ad8c8126e09a55772894e5b12f7580e26b76d2428843f40',archiveEntries=488,githubBranch='study-planner-1406',githubContentCommit='dda3959',chaptersAdded=['l_orthogonality'],libraryChapters=60,questions=4169,studentApproved=False,note='First upload timed out before saving a version. Retrying the same immutable archive succeeded; audience remains owner-private. No numeric version number is invented.')
save(B/'l_orthogonality-publication.json',p)
g=json.loads((B/'chapter-gate.json').read_text())
for c in g['completedReviewDrafts']:
 if c['topicId']=='l_orthogonality':c.update(publicationState='published_private',publication='research/l_orthogonality-publication.json')
g['latestPublication']=p
save(B/'chapter-gate.json',g)
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\n\n## Confirmed orthogonality publication\n\nNative owner-private publication succeeded on2026-10-11 at15:04:49 UTC from exact pushed source7ac738a54daf26186045b4e654e9e1ae40879533. The first archive upload timed out before a version was saved; the same immutable488-entry archive succeeded on retry. Library:60 chapters/4169 worked-entry placements. Publication provenance is research/l_orthogonality-publication.json. The next scheduled draft is l_projection.\n')
print('Recorded confirmed private publication.')
