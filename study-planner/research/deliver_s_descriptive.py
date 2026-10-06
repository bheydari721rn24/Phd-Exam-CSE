from pathlib import Path
import json,shutil
R=Path(__file__).resolve().parents[1];B=R/'research'
for name in ['mathematics','models','browser','lesson-and-retention']:
 d=json.loads((B/f's_descriptive-evidence/{name}.json').read_text());assert d['status']=='passed',name
shutil.copy2(B/'s_descriptive-evidence/reading.json',R/'dist/reviews/s_descriptive-reading.json')
g=json.loads((B/'chapter-gate.json').read_text());assert g['currentTopicId']=='s_descriptive' and g['approvedTopicId']=='a_select'
g.update(state='awaiting_user_approval',nextTopicId=None,nextReview='Await explicit student approval of only s_descriptive; no next chapter has started.',lastCompletedReview='Descriptive Statistics and Exploratory Data Analysis: 82 complete worked problems, 80 rules, five reviewed university courses, 28 models, 198 checkpoints and 14 editable modes.',activeWork='Complete s_descriptive review draft delivered; wait for explicit approval before continuing.',reviewEvidence=[f'research/s_descriptive-evidence/{name}.json' for name in ['reading','mathematics','models','browser','lesson-and-retention']],publicationState='pending',publishedVersion=None)
(B/'chapter-gate.json').write_text(json.dumps(g,indent=2)+'\n')
with (R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8') as f:f.write('\n\n## Descriptive statistics review draft — 6 October 2026\n\nOnly s_descriptive is delivered: 22 deep English lesson sections, five reviewed written university courses with bounded scopes, 82 complete solved problems (80 original/course-inspired and two original-PDF-checked authentic questions), 80 complete final rules, 28 concept-specific models / 198 checkpoints and 14 editable modes. Rational, finite mathematical, actual JavaScript and real-browser checks passed. All 38 preceding chapter pages and 2346 complete problems are retained unchanged. The gate awaits explicit student approval; no next chapter is begun. Source push, GitHub mirror and private publication are tracked separately after verification.\n')
print('Only s_descriptive complete; gate awaits explicit approval.')
