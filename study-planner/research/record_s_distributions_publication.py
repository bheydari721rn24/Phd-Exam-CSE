from pathlib import Path
import json
B=Path(__file__).resolve().parent;R=B.parent
r=json.loads((B/'s_distributions-publication.json').read_text(encoding='utf-8'));assert r['status']=='published_private'and r['deploymentStatus']=='succeeded'
p=B/'chapter-gate.json';g=json.loads(p.read_text(encoding='utf-8'));g['latestPublication']=r
g.update(publicationState='published_private',publicationRecordPath='research/s_distributions-publication.json',publishedVersion=None)
for c in g['completedReviewDrafts']:
 if c['topicId']in r['chaptersAdded']:c.update(publicationState='published_private',publicationRecord='research/s_distributions-publication.json')
p.write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:
 f.write('\n\n## Discrete distributions privately published\n\nNative private deployment '+r['deploymentId']+' succeeded from exact pushed source '+r['sourceCommit']+' and its byte-verified 476-entry archive. Discrete distributions is now online. Library: 58 chapters / 4001 worked entries. GitHub content commit 082d930. Student approval is not inferred. Continue l_linear under standing authorization. See research/s_distributions-publication.json.\n')
print('Confirmed private publication recorded; discrete distributions is online.')
