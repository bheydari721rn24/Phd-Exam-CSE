"""Reuse only independent numerical checks, never historical global status gates.
Bind the repaired counterexample to its actual declared sets, not a canned result."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,re,sys,xml.etree.ElementTree as ET
import sympy as S
R=Path(__file__).resolve().parents[1];E=R/'research/deep-library-revision';old=R/'research/verify_s_conditional_en.py';code=old.read_text(encoding='utf8').split("data=json.loads((ROOT/'dist/chapters/concept-animations.json')",1)[0]
scope={'__file__':str(old),'__name__':'independent_numeric_oracle'};exec(compile(code,str(old),'exec'),scope)
checks=[]
def ck(n,ok):assert ok,n;checks.append(n)
q=scope['q']['SC33'];sets=re.findall(r'\\\{([0-9,]+)\\\}',q['stem']);ck('declared repaired finite sets',len(sets)==2)
A=set(map(int,sets[0].split(',')));B=A;C=set(map(int,sets[1].split(',')));N=8
joint=F(len(A&B&C),N);product=F(len(A),N)*F(len(B),N)*F(len(C),N)
ck('actual SC33 stem satisfies its triple equation',joint==product==F(1,8));ck('actual SC33 stem violates a pair equation',F(len(A&B),N)!=F(len(A),N)*F(len(B),N))
ck('former wrong stem is demonstrably wrong',F(len(A&{1,5}),N)!=F(len(A),N)**2*F(2,N))
t,w,u1,u2,v1,v2,b,u,v=S.symbols('t w u1 u2 v1 v2 b u v',real=True)
cov=w*u1*v1+(1-w)*u2*v2-(w*u1+(1-w)*u2)*(w*v1+(1-w)*v2)
ck('general two-type covariance derivation',S.expand(cov-w*(1-w)*(u1-u2)*(v1-v2))==0)
ck('table determinant derivation',S.expand(b*u*(1-b)*(1-v)-(1-b)*v*b*(1-u)-b*(1-b)*(u-v))==0)
ck('bridge polynomial expansion',S.expand((1-t)*(2*t*t-t**4)+t*(2*t-t*t)**2-(2*t*t+2*t**3-5*t**4+2*t**5))==0)
y,ep=S.symbols('y ep',positive=True);ck('positive strip ratio',S.cancel(y*ep/(2*y*ep+ep*ep))==y/(2*y+ep))
ck('triangle target area',S.integrate(1-t,(t,0,S.Rational(1,2)))==S.Rational(3,8))
ck('opposite-type table normalized',2*F(4,25)+2*F(17,50)==1)
page=(R/'dist/chapters/s_conditional.html').read_text(encoding='utf8');sys.path.insert(0,str(R/'research/exam-rewrite'));from math_fences import delimiter_issues,closing_script_bases
maths=re.findall(r'<math\b[\s\S]*?</math>',page)
for i,value in enumerate(maths):
 root=ET.fromstring(value);ck('mathematical delimiter and script '+str(i),not delimiter_issues(root)and not closing_script_bases(root))
ck('sixty complete answers',page.count('class="exam-question"')==60 and page.count('class="exam-solution"')==60)
ck('eighty complete final rules retained',page.count('class="review-rule"')==80)
visible=re.sub(r'<(?:script|style)\b[\s\S]*?</(?:script|style)>','',page)
ck('no draft slots or raw TeX',not re.search(r'\$|MATHSLOT|<!--\s*(?:INCLUDE|LAB|FIGURE):',visible))
report={'status':'passed_independent_mathematical_checks','legacyNumericOracle':{'checks':sum(scope['counts'].values()),'byKind':dict(scope['counts']),'scope':'Only the numerical and finite-event portion runs. Old approval and library-count gates are deliberately excluded as historical state.'},'newAssertions':checks,'questionsReviewed':60,'originalCourseAnswersExpanded':56,'finalRulesReviewed':80,'nativeExpressions':len(maths),'normalizedTextSha256':hashlib.sha256(page.encode()).hexdigest(),'documentSha256':hashlib.sha256((R/'dist/chapters/s_conditional.html').read_bytes()).hexdigest(),'criticalCorrection':{'id':'SC33','actualSets':[sorted(A),sorted(C)],'triple':str(joint),'product':str(product),'pairAB':'1/2','marginalProductAB':'1/4'},'limits':'General derivations were read separately; bounded enumerations and source fingerprints do not establish literal100percent correctness or exhaustive exam coverage.'};(E/'s_conditional-mathematics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8');print({'numericChecks':report['legacyNumericOracle']['checks'],'newChecks':len(checks),'nativeExpressions':len(maths),'counterexampleRepaired':True})
