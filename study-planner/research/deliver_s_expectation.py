from pathlib import Path
import json,re
from urllib.parse import urlsplit,unquote
B=Path(__file__).resolve().parent;R=B.parent;E=B/'s_expectation-evidence'
for name in ['mathematics','models','browser','lesson-and-retention']:assert json.loads((E/(name+'.json')).read_text())['status']=='passed',name
assert json.loads((E/'reading.json').read_text())['status']=='completed'
for path in [R/'dist/chapters/s_expectation.html',R/'dist/reviews/s_expectation-sources.html',R/'dist/reviews/s_expectation-quality.html']:
 for href in re.findall(r'(?:href|src)="([^"]+)"',path.read_text(encoding='utf-8')):
  if href.startswith(('https:','http:')):continue
  parts=urlsplit(href);dest=path if not parts.path else path.parent/unquote(parts.path)
  assert dest.is_file(),(path.name,href)
  if parts.fragment and dest.name!='index.html':assert re.search(r'id="'+re.escape(parts.fragment)+'"',dest.read_text(encoding='utf-8')),(path.name,href)
g=json.loads((B/'chapter-gate.json').read_text());assert g['currentTopicId']=='s_expectation'and g['state']=='in_progress'
g.update(state='awaiting_user_approval',lastCompletedReview='Expectation, Linearity, Indicators, and Moments: 29 sections, 82 fully solved mathematical/conceptual problems including two original-PDF-checked examinations, 80 final rules, four core written university courses and an additional Cornell lecture, 19 exact-state models, 85 checkpoints, seven editable modes.',nextReview='Await explicit approval of only s_expectation; no following chapter has started.',activeWork='Completed and locally verified review draft. Publish this chapter, then await explicit approval.',sourceAudit='research/s_expectation-source-audit.md',qualityAudit='research/s_expectation-quality-audit.md',reviewEvidence=['research/s_expectation-evidence/'+n+'.json'for n in ['reading','mathematics','models','browser','lesson-and-retention']],publicationState='verified_local_draft_pending_publication')
(B/'chapter-gate.json').write_text(json.dumps(g,indent=2)+'\n')
with (R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:
 f.write('\n\n## Expectation — completed review draft, 7 October 2026\n\nExplicit approval of discrete random variables permits only this next Week 3 chapter. s_expectation contains 29 sections, 80 original/reconstructed complete solutions and two original-PDF-checked authentic questions, 80 final condition-bearing rules, 19 concept-specific models with 85 stored checkpoints, and seven editable modes. Four core written courses were actually read from Oxford, MIT, Berkeley and CMU; Cornell supplies a supplementary lecture check. Stanford was excluded because locally downloaded bytes did not match the advertised Moments content. Seventy independent mathematical checks and every stored model checkpoint passed. Real Edge checks cover geometry, padding, connector boundaries, actual in-flight pause/resume, print, reduced motion, mobile and all seven laboratory modes. Forty preceding chapter pages and 2,511 complete problems are retained unchanged. The library has 41 chapters and 2,593 problems. Private Site and GitHub publication will be recorded after their actual verification. Gate awaiting_user_approval; no next chapter starts without explicit approval.\n')
print('Only s_expectation is complete and awaiting explicit approval; local artifact links verified.')
