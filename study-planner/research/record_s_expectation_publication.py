from pathlib import Path
import json
B=Path(__file__).resolve().parent;R=B.parent
p=json.loads((B/'s_expectation-publication.json').read_text());assert p['deploymentState']=='succeeded'and p['savedSourceCommit']==p['contentCommit']
g=json.loads((B/'chapter-gate.json').read_text());assert g['state']=='awaiting_user_approval'and g['currentTopicId']=='s_expectation'
g.update(publicationState='published_review_draft',publishedVersion=p['versionNumber'],publicationRecordPath='research/s_expectation-publication.json',nextTopicId=None,proposedNextTopicId=None,activeWork='Published and verified review draft of only s_expectation. Await explicit student approval before starting the next chapter.')
(B/'chapter-gate.json').write_text(json.dumps(g,indent=2)+'\n')
with (R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\n\n## Verified expectation publication — 7 October 2026\n\nPrivate Site version '+str(p['versionNumber'])+' succeeded. Saved source matches '+p['contentCommit']+'. The local static archive contains '+str(p['archiveFileCount'])+' files, byte-checked against the committed checkout. Exact chapter and evidence were pushed to GitHub branch study-planner-1406, content commit '+p['githubContentCommit']+'. Owner-only audience was preserved. This chapter remains a review draft; no subsequent chapter has started.\n')
print('Verified expectation publication recorded; approval gate preserved.')
