"""Record only a verified native publication; do not start the following chapter."""
from pathlib import Path
import json
B=Path(__file__).resolve().parent;R=B.parent
p=json.loads((B/'s_discrete-publication.json').read_text())
assert p['deploymentState']=='succeeded' and p['savedSourceCommit']==p['contentCommit']
g=json.loads((B/'chapter-gate.json').read_text());assert g['state']=='awaiting_user_approval' and g['currentTopicId']=='s_discrete'
g.update(publicationState='published_review_draft',publishedVersion=p['versionNumber'],publicationRecordPath='research/s_discrete-publication.json',nextTopicId=None,proposedNextTopicId=None,activeWork='Published and verified review draft of only s_discrete. Await explicit approval before starting the next chapter.')
(B/'chapter-gate.json').write_text(json.dumps(g,indent=2)+'\n')
with (R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8') as f:
 f.write('\n\n## Verified discrete-variable publication — 7 October 2026\n\nPrivate Site version '+str(p['versionNumber'])+' succeeded. Its saved source matches '+p['contentCommit']+'. The archive contains 348 files and was byte-checked against the clean content checkout. The exact chapter and evidence were also pushed to GitHub branch study-planner-1406, content commit '+p['githubContentCommit']+'. The Windows package-helper path failure occurred after the helper verified the source push; local static packaging recovered without changing source or audience. The chapter remains a review draft awaiting explicit approval. No following chapter has started.\n')
print('Verified private publication recorded; only s_discrete awaits approval.')
