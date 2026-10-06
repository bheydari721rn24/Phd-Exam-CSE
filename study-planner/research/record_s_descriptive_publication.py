from pathlib import Path
import json,subprocess
R=Path(__file__).resolve().parents[1];B=R/'research'
p=json.loads((B/'s_descriptive-publication.json').read_text());assert p['deploymentState']=='succeeded' and p['versionNumber']==76
g=json.loads((B/'chapter-gate.json').read_text());assert g['state']=='awaiting_user_approval' and g['currentTopicId']=='s_descriptive'
g.update(publicationState='published_review_draft',publishedVersion=p['versionNumber'],publicationRecordPath='research/s_descriptive-publication.json',nextTopicId=None,proposedNextTopicId=None)
(B/'chapter-gate.json').write_text(json.dumps(g,indent=2)+'\n')
with (R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8') as f:f.write('\n\n## Verified descriptive-statistics publication — 6 October 2026\n\nPrivate Site version 76 succeeded and its saved source matches dbfc92896b6ad50da341ae3692f5a448ffad6529. The exact loss-curve revision and chapter artifacts were pushed to GitHub branch study-planner-1406 (content commit c1544c99dd4159847a031436fda95e407b74817f). The publication receipt records recovery from the initial upload timeout and the Windows package-helper path issue. The chapter remains a draft awaiting explicit approval; no following chapter has started.\n')
print('Verified Site version 76 recorded; only s_descriptive awaits explicit approval.')
