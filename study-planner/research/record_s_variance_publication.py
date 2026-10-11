from pathlib import Path
import json
B=Path(__file__).resolve().parent;R=B.parent
r=json.loads((B/'s_variance-publication.json').read_text(encoding='utf-8'));assert r['status']=='published_private'and r['deploymentStatus']=='succeeded'
p=B/'chapter-gate.json';g=json.loads(p.read_text(encoding='utf-8'));g['latestPublication']=r
g.update(publicationState='published_private',publicationRecordPath='research/s_variance-publication.json',publishedVersion=None)
for c in g['completedReviewDrafts']:
 if c['topicId']in r['chaptersAdded']:c.update(publicationState='published_private',publicationRecord='research/s_variance-publication.json')
p.write_text(json.dumps(g,indent=2)+'\n',encoding='utf-8')
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\n\n## Five new drafts privately published\n\nNative private deployment '+r['deploymentId']+' succeeded from exact pushed source '+r['sourceCommit']+' and its byte-verified 470-entry archive. It publishes balanced trees, heaps, hashing, amortized analysis and variance/covariance. Library: 57 chapters / 3913 worked entries. GitHub content commit 27ff627. No student approval is inferred. Continue s_distributions under standing authorization. See research/s_variance-publication.json.\n')
print('Confirmed private publication recorded; five drafts are now online.')
