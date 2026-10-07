from pathlib import Path
import json,re,shutil
from urllib.parse import urlsplit,unquote
B=Path(__file__).resolve().parent;R=B.parent;E=B/'s_discrete-evidence'
for name in ['mathematics','models','browser','lesson-and-retention']:
 d=json.loads((E/(name+'.json')).read_text());assert d['status']=='passed',name
browser=json.loads((E/'browser.json').read_text());assert browser['geometry']['models']==37 and browser['geometry']['frames']==208 and not browser['mappingPortsAndPadding']
for name in ['question-convolution.png','review-rule.png']:
 shutil.copy2(Path(browser['screenshots'])/name,E/name)
for path in [R/'dist/chapters/s_discrete.html',R/'dist/reviews/s_discrete-sources.html',R/'dist/reviews/s_discrete-quality.html']:
 content=path.read_text(encoding='utf-8')
 for href in re.findall(r'(?:href|src)="([^"]+)"',content):
  if href.startswith(('http:','https:')):continue
  parts=urlsplit(href);dest=path if not parts.path else path.parent/unquote(parts.path)
  assert dest.is_file(),(path.name,href)
  if parts.fragment and dest.suffix=='.html' and dest.name!='index.html':assert re.search(r'id="'+re.escape(parts.fragment)+'"',dest.read_text(encoding='utf-8')),(path.name,href)
g=json.loads((B/'chapter-gate.json').read_text());assert g['currentTopicId']=='s_discrete' and g['state']=='in_progress'
g.update(state='awaiting_user_approval',lastCompletedReview='Discrete Random Variables and Common Distributions: 26 sections, 83 complete worked problems, 80 rules, four core university courses and a bounded Harvard review, 37 distinct models, 208 checkpoints, eight editable modes.',nextReview='Await explicit student approval of only s_discrete; no following chapter has started.',activeWork='Completed and locally verified review draft. Publish this chapter and await explicit approval before any following chapter.',sourceAudit='research/s_discrete-source-audit.md',qualityAudit='research/s_discrete-quality-audit.md',reviewEvidence=['research/s_discrete-evidence/'+n+'.json' for n in ['reading','mathematics','models','browser','lesson-and-retention']],publicationState='verified_local_draft_pending_publication')
(B/'chapter-gate.json').write_text(json.dumps(g,indent=2)+'\n')
with (R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8') as f:
 f.write('\n\n## Discrete random variables — completed review draft, 7 October 2026\n\nThe explicit approval of descriptive statistics permits only this next Week 3 chapter. `s_discrete` is now a complete English draft: 26 sections, 80 original/reconstructed worked problems, three original-PDF-checked examination adaptations, 80 final rules, 37 subject-specific models with 208 checkpoints, and eight editable modes. Four core written courses were read from Oxford, MIT, UC Berkeley and Stanford; Harvard contributes bounded additional exercise material. Seventy rational checks and 616 independent enumeration comparisons passed. Real Edge checks cover all 208 checkpoints, connector boundaries, label padding, controls, reduced motion, print and mobile. The 39 previous HTML pages and 2,428 complete problems remain unchanged. Private Site and GitHub publication will be recorded after their actual verification. Gate: awaiting_user_approval; no next chapter begins before explicit approval.\n')
print('Local review draft verified; approval gate set for only s_discrete.')
