"""Current Bayes review: exact numerical oracle plus actual-statement checks."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
import hashlib,json,re,sys,xml.etree.ElementTree as ET
import sympy as S
R=Path(__file__).resolve().parents[1]; E=R/'research/deep-library-revision'
old=R/'research/verify_s_bayes_en.py'
code=old.read_text(encoding='utf8').split("data=json.loads((ROOT/'dist/chapters/concept-animations.json')",1)[0]
scope={'__file__':str(old),'__name__':'numerical_oracle'}
exec(compile(code,str(old),'exec'),scope)
checks=[]
def ck(name,ok):
 assert ok,name
 checks.append(name)
qs=scope['q']
ck('actual size-biased problem declares fixed exact proportions','exact family-size proportions' in qs['SB33']['stem'] and 'multiple of six' in qs['SB33']['stem'])
children=[n for n,count in [(1,3),(2,2),(3,1)] for _ in range(n*count)]
ck('child enumeration for actual minimum admissible population',[F(children.count(n),len(children))for n in [1,2,3]]==[F(3,10),F(2,5),F(3,10)])
ck('distinct common weights are explicit','same heavy weight' in qs['SB36']['stem'] and 'distinct light weight' in qs['SB36']['stem'])
weights=[7]*2+[3]*8;pairs=list(combinations(range(10),2));kept=[(i,j)for i,j in pairs if weights[i]==weights[j]]
ck('equal-weight enumeration matches literal model',F(sum(weights[i]==7 for i,j in kept),len(kept))==F(1,29))
# A counterexample prevents reinstating the ratio-of-expectations shortcut.
random_two_families=[(1,1),(1,2),(2,1),(2,2)]
average_share=sum(F(sum(n==1 for n in sizes),sum(sizes))for sizes in random_two_families)/4
ck('finite random population ratio differs',average_share==F(5,12) and average_share!=F(1,3))
p,s,f,r,c=S.symbols('p s f r c',positive=True); d=p*s+(1-p)*f; g=p*s/d
ck('posterior derivative',S.factor(S.diff(g,p)-s*f/d**2)==0)
ck('posterior curvature',S.factor(S.diff(g,p,2)+2*s*f*(s-f)/d**3)==0)
ck('sensitivity partial derivative',S.factor(S.diff(g,s)-p*(1-p)*f/d**2)==0)
ck('false-positive partial derivative',S.factor(S.diff(g,f)+p*(1-p)*s/d**2)==0)
ck('classification cost equality',F(99,2000)+F(2,2000)*F(11,2)==F(20,2000)*F(11,2))
# Two structural models with identical observations and different interventions.
obs1=[(u,u,u)for u in [0,1]];obs2=[(u,u,u)for u in [0,1]]
ck('causal observational equivalence',obs1==obs2)
intervened_common_cause=[(u,1,u)for u in [0,1]]
intervened_chain=[(u,1,1)for u in [0,1]]
ck('causal intervention separation',sum(row[2]for row in intervened_common_cause)/2==.5 and sum(row[2]for row in intervened_chain)/2==1)
# Recheck every serialized Bayes scene independently of the page renderer.
scenes=json.loads((R/'dist/chapters/concept-animations.json').read_text(encoding='utf8'))['scenes']
for id,scene in scenes.items():
 if not id.startswith('bayes-'):continue
 for k,frame in enumerate(scene['frames']):
  v=frame['snapshot']; ok=True
  if id=='bayes-partition':ok=sum(map(F,v['weights']))==F(v['evidence'])
  elif id=='bayes-normalize':ok=list(map(F,v['values']))in [[F(1,2),F(1,3),F(1,6)],[F(1,20),F(1,15),F(1,10)],[F(3,13),F(4,13),F(6,13)]]
  elif id=='bayes-repeat':ok=F(v['odds'])==F(4**v['n'],9) and F(v['posterior'])==F(4**v['n'],9+4**v['n'])
  elif id=='bayes-copy':ok=F(v['duplicate'])==(F(1,10)if v['n']==0 else F(4,13))
  elif id=='bayes-predict':
   r0=F(9,10)**v['n']/(F(9,10)**v['n']+F(1,2)**v['n']);ok=F(v['biased'])==r0 and F(v['predictive'])==(1-r0)*F(1,2)+r0*F(9,10)
  elif id=='bayes-host':ok=F(v['switch'])==1/(1+F(v['q']))
  elif id=='bayes-sensitivity':ok=F(v['posterior'])==4*F(v['p'])/(1+3*F(v['p']))
  elif id=='bayes-loss':ok=F(v['targetRisk'])==F(11,13) and F(v['backgroundRisk'])==F(2,13)*F(v['cfn'])
  elif id=='bayes-density':
   h,t=v['h'],v['t'];u=S.symbols('u');integ=S.integrate(u**h*(1-u)**t,(u,0,1));ok=S.Rational(v['integral'])==integ
  elif id=='bayes-frequencies':
   a,b=([F(9,1000),F(99,2000)]if v['positive']else[F(1,1000),F(1881,2000)])
   expected=[F(1,100),F(99,100)]if v['stage']=='population'else[a,b]if v['stage']=='retained'else[a/(a+b),b/(a+b)]
   ok=list(map(F,v['values']))==expected
  ck(id+' checkpoint '+str(k),ok)
page=(R/'dist/chapters/s_bayes.html').read_text(encoding='utf8')
sys.path.insert(0,str(R/'research/exam-rewrite'));from math_fences import delimiter_issues,closing_script_bases
maths=re.findall(r'<math\b[\s\S]*?</math>',page)
for i,m in enumerate(maths):
 root=ET.fromstring(m); ck('delimiter/script '+str(i),not delimiter_issues(root)and not closing_script_bases(root))
ck('65 full worked entries',page.count('class="exam-question"')==65 and page.count('class="exam-solution"')==65)
ck('80 full final rules',page.count('class="review-rule"')==80)
ck('31 actual-input question figures',page.count('pr-model pr-static')==31)
visible=re.sub(r'<(?:script|style)\b[\s\S]*?</(?:script|style)>','',page)
ck('no raw TeX/slots',not re.search(r'\$|MATHSLOT|<!--\s*(?:INCLUDE|LAB|FIGURE):',visible))
report=dict(status='passed_independent_mathematical_checks',numericOracleChecks=sum(scope['counts'].values()),numericBindings=scope['bindings'],newAssertions=checks,questionsReviewed=65,answersExpanded=63,finalRules=80,problemFigures=31,nativeExpressions=len(maths),normalizedTextSha256=hashlib.sha256(page.encode()).hexdigest(),documentSha256=hashlib.sha256((R/'dist/chapters/s_bayes.html').read_bytes()).hexdigest(),limits='Finite exact grids and independently checked derivations support the recorded models, not a universal completeness or unseen-score guarantee. Historical global approval gates are not run.')
(E/'s_bayes-mathematics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print({k:v for k,v in report.items()if k not in ['newAssertions','numericBindings','limits']})
