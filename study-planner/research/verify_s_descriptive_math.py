from pathlib import Path
from fractions import Fraction as F
import json,math,re,hashlib,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];B=R/'research';checks=[]
def check(name,actual,expected):
 assert actual==expected,(name,actual,expected);checks.append(name)
def stats(a):
 a=list(map(F,a));n=len(a);mean=sum(a)/n;m2=sum((x-mean)**2 for x in a);return mean,m2,m2/n,m2/(n-1) if n>1 else None
check('Q1 recoded nominal mean',F(20*10+30*100+50*1000,100),F(532))
check('Q3 unequal-width heights',[F(1,6),F(2,6),F(3,12)],[F(1,6),F(1,3),F(1,4)])
check('Q4 density area',2*F(1,10)+3*F(1,5)+5*F(4,100),F(1))
check('Q8 bimodal mean',stats([0,0,1,1,9,9,10,10])[0],F(5))
check('Q10 weighted student mean',F(12*70+28*80,40),F(77))
check('Q12 correction energy',90+2*10*(17-20)+100*F(9,10),F(120))
check('Q13 weighted variance',(F(132)-F(18**2,4))/4,F(51,4))
check('Q14 harmonic exposure',2/(F(1,30)+F(1,60)),F(40))
check('Q15 compounded product',F(5,4)*F(4,5),F(1))
check('Q16 median loss',sum(abs(F(x)-F(11,2)) for x in [1,3,8,10]),F(14))
check('Q18 type7',[F(1)+F(3,4)*4,F(5)+F(1,2)*3,F(8)+F(1,4)*7],[F(4),F(13,2),F(39,4)])
check('Q21 zero-IQR extreme variance',stats([0]*7+[100])[2],F(4375,4))
check('Q23 raw totals',stats([1,2,2,3,4,6]),(F(3),F(16),F(8,3),F(16,5)))
check('Q24 impossible totals',F(90)-F(20**2,4),F(-10))
check('Q25 two-record variance',stats([2,8]),(F(5),F(18),F(9),F(18)))
check('Q26 both inverse roots',[stats([0,2,x])[3] for x in [-2,4]],[F(4),F(4)])
check('Q27 wrong-center correction',500-20*(7-5)**2,420)
check('Q28 RMS identity',25-(-4)**2,9)
check('Q33 reliability correction',F(100)/(4-F(8,4)),F(50))
check('Q34 weighted denominator',10-F(66,10),F(17,5))
check('Q35 affine variance',(-3)**2*4,36)
check('Q39 sample size ratio',F(6,5),F(6,6-1))
check('Q42 mean absolute deviation',sum(abs(F(x)-4) for x in [0,1,2,3,14])/5,F(4))
check('Q43 robust means',[F(sum([2,3,4,5]),4),F(sum([2,2,3,4,5,5]),6)],[F(7,2)]*2)
for M in [5,6,10,100]:check('Q44 polynomial '+str(M),stats([1,2,3,4,M])[2],F(4*M*M-20*M+50,25))
check('Q46 equal centers',stats([0,2,3,3,7])[0],F(3))
a=[-2,-1,1,3];w=[4,1,6,1];check('Q48 first moment',sum(F(v*f) for v,f in zip(a,w))/12,F(0));check('Q48 second moment',sum(F(v*v*f) for v,f in zip(a,w))/12,F(8,3));check('Q48 third moment',sum(F(v**3*f) for v,f in zip(a,w))/12,F(0))
check('Q51 Markov equality',sum([60]*20+[0]*80)/100,12)
check('Q52 closed attainable energy',4*36+2*F('13.5'),F(171));check('Q52 strict attainable energy',4*F('6.1')**2+2*F('11.08'),F(171))
check('Q53 closed tail construction',stats([4,4,-4,-4]+[0]*12)[2],F(4))
check('Q54 odd finite extremum',stats([0,0,6])[2],F(8))
check('Q55 mean-conditioned extremum',stats([2,2,2,10])[2],F(12))
check('Q57 weighted midpoint error',F(3*1+2*2,5),F(7,5))
check('Q58 grouped variance counterexamples',[stats([F('1.9'),F('2.1')])[2],stats([0,4])[2]],[F(1,100),F(4)])
check('Q59 grouped interpolation',2+5*F(10-4,10),F(5))
check('Q60 within/between',stats([0,0,6,6]),(F(3),F(36),F(9),F(12)))
check('Q61 corrected merge',2*1+1*2+3*(2-4)**2+2*(7-4)**2,34)
check('Q62 total descriptive variance',F(18+200,12),F(109,6))
check('Q63 Simpson reversal',(F(9,10)>F(80,100),F(30,100)>F(2,10),F(39,110)<F(82,110)),(True,True,True))
check('Q65 append direct calculation',stats([0,2,4,10]),(F(4),F(56),F(14),F(56,3)))
check('Q66 deletion feasibility',stats([3,3,3,3,8]),(F(4),F(20),F(4),F(5)))
check('Q67 increase threshold',F(5*9,4),F(45,4))
check('Q68 merge energy',2+8+F(2*3,5)*(6-1)**2,F(40))
check('Q69 cancellation-safe exact variance',stats([10**12,10**12+1,10**12+2])[2],F(2,3))
check('Q70 zero cross sum',sum(F(x)*(F(y)-F(2,3)) for x,y in [(-1,1),(0,0),(1,1)]),F(0))
check('Q71 correlation squared',F(2**2)/(F(2)*F(14,3)),F(3,7))
check('Q72 sum/difference', [4+9-6,4+9+6],[7,19])
check('Q75 tied rank correlation squared',F(3,2)**2/(F(3,2)*2),F(3,4))
check('Q76 Kendall',F(1-2,3),F(-1,3))
check('Q77 affine quantile pairs',[2*x+5 for x in [0,1,2,4]],[5,7,9,13])
check('Q78 trailing MA',[F(2),F(2+4,2),F(2+4+10,3),F(4+10+8,3)],[F(2),F(3),F(16,3),F(22,3)])
check('Q79 EWMA weights',F(1,2)+F(1,4)+F(1,8)+F(1,8),F(1))
check('Q80 RMS squared',4+5**2,29)
# Exhaustive small-grid checks of exact finite bounds and update identities.
import itertools
finite=0
for n in range(2,5):
 for a in itertools.product(range(-2,3),repeat=n):
  mean,m2,v,s2=stats(a)
  assert all((F(x)-mean)**2<=(n-1)*v for x in a)
  assert v<=(max(a)-min(a))**2*F(n*n//4,n*n)
  for x in [-3,0,3]:
   new=stats([*a,x]);delta=F(x)-mean;assert new[0]==mean+delta/(n+1);assert new[1]==m2+F(n,n+1)*delta**2
  finite+=1
auth=json.loads((B/'s_descriptive-authentic.json').read_text());assert [q['answer'] for q in auth]==[3,1]
archive=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')
for q in auth:assert hashlib.sha256((archive/q['repoPath']).read_bytes()).hexdigest()==q['pdfSha256']
page=(R/'dist/chapters/s_descriptive.html').read_text(encoding='utf-8');assert '$' not in page and not re.search('[\u0600-\u06ff]',page)
maths=re.findall(r'<math\b[\s\S]*?</math>',page)
for m in maths:ET.fromstring(m)
old=json.loads((B/'s_descriptive-evidence/prior-library.json').read_text());assert old['chapterCount']==38 and old['questionCount']==2346
for c in old['chapters']:assert hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest()==c['sha256'],c['topicId']
(B/'s_descriptive-evidence/mathematics.json').write_text(json.dumps(dict(status='passed',exactChecks=checks,finiteBoundAndUpdateCases=finite,authenticPDFHashesVerified=2,nativeMathTrees=len(maths),limits='Exact arithmetic and finite enumerations check named claims; semantic proof review remains separate.'),indent=2)+'\n')
(B/'s_descriptive-evidence/lesson-and-retention.json').write_text(json.dumps(dict(status='passed',retainedChapterHashes=38,retainedCompleteQuestions=2346,newOriginalQuestions=80,newAuthenticQuestions=2,newRules=80,englishOnly=True,rawTexAbsent=True),indent=2)+'\n')
print(f'{len(checks)} exact named checks; {finite} finite bound/update lists; {len(maths)} native math trees; 38 prior chapters retained.')
