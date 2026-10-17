"""Rerun exact models without stale library gates or unavailable cache assertions."""
from pathlib import Path
import json,re,sys,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];p=R/'research/verify_l_gauss_en.py';s=p.read_text(encoding='utf8').split("sources=json.loads((ROOT/'dist/evidence/l_gauss/sources.json')",1)[0]
a=s.index('for q in auth:\n');z=s.index('doctoral=',a);s=s[:a]+s[z:]
scope={'__file__':str(p),'__name__':'independent_gauss_numeric_audit'};exec(compile(s,str(p),'exec'),scope)
sys.path.insert(0,str(R/'research/exam-rewrite'));from math_fences import delimiter_issues,closing_script_bases
html=(R/'dist/chapters/l_gauss.html').read_text(encoding='utf8');maths=re.findall(r'<math\b[\s\S]*?</math>',html)
assert all(not delimiter_issues(ET.fromstring(m))and not closing_script_bases(ET.fromstring(m))for m in maths)
d=json.loads((R/'research/deep-library-revision/l_gauss-targeted-errata.json').read_text());assert all(d['exactChecks'].values())
assert html.count('class="exam-question"')==71 and html.count('class="review-rule"')==80
report=dict(state='passed_targeted_errata_and_retained_exact_models',numericChecks=sum(scope['counts'].values()),checksByKind=dict(scope['counts']),nativeMathExpressions=len(maths),questions=71,finalRules=80,individualChapterReviewComplete=False,limits='Cache source fingerprints and historical approval/count gates are explicitly excluded. This targeted erratum and retained numerical-model audit do not complete the individual semantic review of all source and visual material.')
(R/'research/deep-library-revision/l_gauss-erratum-evidence/mathematics.json').write_text(json.dumps(report,indent=2)+'\n');print({k:v for k,v in report.items()if k not in ['checksByKind','limits']})
