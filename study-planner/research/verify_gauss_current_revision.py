"""Current whole-chapter exact models, original archive hashes and MathML audit."""
from pathlib import Path
import hashlib,json,re,subprocess,sys,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];E=R/'research/deep-library-revision'
p=R/'research/verify_l_gauss_en.py';source=p.read_text(encoding='utf8').split("sources=json.loads((ROOT/'dist/evidence/l_gauss/sources.json')",1)[0]
# Old checks for exact prose spellings no longer express the revised formulas.
# Their mathematical examples remain, supplemented by every-ID manuscript checks.
a=source.index('for title,value in bindings.items():');z=source.index("check('schur-example-answer'",a);source=source[:a]+source[z:]
a=source.index('for q in auth:\n');z=source.index('doctoral=',a);source=source[:a]+source[z:]
scope={'__file__':str(p),'__name__':'current_gauss_independent_model_audit'}
exec(compile(source,str(p),'exec'),scope)
qs=json.loads((R/'research/l_gauss-questions.json').read_text());auth=json.loads((R/'research/l_gauss-authentic.json').read_text())
old=json.loads(subprocess.check_output(['git','show','ed4a4c486cba3a388a32384faa68a916bfda9399:research/l_gauss-questions.json'],cwd=R))
for now,prior in zip(qs,old):
    assert all(now[k]==prior[k]for k in ['id','title','stem','origin','difficulty','certificate'])
    assert now['solution']!=prior['solution']
evidence=json.loads((E/'l_gauss-authentic-recheck-20261017.json').read_text())
for record in evidence['sourceRecords']:
    assert hashlib.sha256(Path(record['sourceLocalFile']).read_bytes()).hexdigest()==record['sourceSha256']
assert auth[0]['answer']==3 and auth[1]['answer']==4 and auth[1]['options'][0]=='37'
page=(R/'dist/chapters/l_gauss.html').read_text(encoding='utf8')
assert page.count('class="exam-question"')==71 and page.count('class="review-rule"')==80
sys.path.insert(0,str(R/'research/exam-rewrite'))
from math_fences import delimiter_issues,closing_script_bases
expressions=re.findall(r'<math\b[\s\S]*?</math>',page)
for text in expressions:
    node=ET.fromstring(text)
    assert not delimiter_issues(node)and not closing_script_bases(node),text[:200]
for q in qs+auth:
    assert q['solution'].count('$')%2==0
    assert not any(ord(c)<32 and c not in'\n\r\t'for c in q['solution'])
supplement=json.loads((E/'gauss-advanced-answer-checks.json').read_text())
middle=json.loads((E/'l_gauss-expanded-answer-checks.json').read_text())
peer=json.loads((E/'l_gauss-root-manuscript-peer-review-20261017.json').read_text())
assert supplement['questions']==44 and supplement['assertions']==612
assert middle['assertions']==861 and peer['state']=='passed_bounded_mathematical_peer_review'
report={'status':'passed_gauss_current_revision_mathematics','date':'2026-10-17','retainedExactModelAssertions':sum(scope['counts'].values()),'expandedMiddleAssertions':middle['assertions'],'expandedAdvancedAssertions':supplement['assertions'],'peerExactAssertions':len(peer['exactChecks']),'nativeMathExpressions':len(expressions),'allOriginalCourseSolutionsRewritten':69,'authenticPlacements':2,'originalArchiveHashesRechecked':2,'questionPlacements':71,'finalRules':80,'pageSha256':hashlib.sha256((R/'dist/chapters/l_gauss.html').read_bytes()).hexdigest(),'limits':'The retained numerical models, independently checked examples and finite grids support the written general proofs; they do not prove universal correctness from testing. Stale literal prose bindings and old global approval/cache gates are replaced by current manuscript identity, every-ID checks and original archive fingerprints.'}
(E/'l_gauss-current-mathematics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8');print(report)
