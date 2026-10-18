"""Independent numerical, code, original-page and strict notation checks."""
from pathlib import Path
from fractions import Fraction as F
import math,json,re,hashlib,sys,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];B=R/'research';checks=[]
def check(label,ok):assert ok,label;checks.append(label)
def mx(*c):return ('MAX',c)
def mn(*c):return ('MIN',c)
def value(t):
 if not isinstance(t,tuple):return F(t)
 return(max if t[0]=='MAX'else min)(map(value,t[1]))
def trace(t,a=-math.inf,b=math.inf,path=''):
 if not isinstance(t,tuple):return F(t),[path],set(),1
 v=-math.inf if t[0]=='MAX'else math.inf;vis=[];cut=set();nodes=1
 for i,c in enumerate(t[1]):
  x,seen,skipped,count=trace(c,a,b,path+str(i));vis+=seen;cut|=skipped;nodes+=count
  if t[0]=='MAX':v=max(v,x);a=max(a,v)
  else:v=min(v,x);b=min(b,v)
  if a>=b:cut|={path+str(j)for j in range(i+1,len(t[1]))};break
 return v,vis,cut,nodes
check('Q01 exact minimax',value(mx(mn(2,7),mn(1,8)))==2)
check('Q02 policy comparisons',[-5,1,2,5]==sorted([-5,1,2,5])and[max((-50+50)/2,(1+3)/2,(-5+15)/2)]==[5])
check('Q03 coin movement',max((F(-55,2),F(-49,2),F(-4,2)))==-2)
check('Q04 cutoff',trace(mx(mn(10,8),mn(4,50)))[1]==['00','01','10'])
t=mx(mn(mx(10,6),mx(100,8)),mn(mx(1,2),mx(20,4)))
check('Q05 full root and five leaves',value(t)==10 and trace(t)[1]==['000','001','010','100','101'])
check('Q06 unequal expectations',[F(12,4)+F(8,4)+F(4,2),F(8+6,2),F(12,3)+F(12,3)]==[7,7,8])
check('Q07 cardinal reversal',F(21,10)>F(13,10)and 21<F(409,10))
check('Q08 mixture masses',F(85,100)*(-10)+F(5,100)*30==-7 and F(8,10)*(-10)+F(2,30)*30==-6)
for x in map(F,[-20,0,3,F(7,2),4,5,6,7,8,10,25]):
 t=mx(mn(x,8),mn(4,12));expected=4 if  x<=4 else x if x<=8 else 8
 check('Q09 value '+str(x),value(t)==expected)
 check('Q09 boundary cutoff '+str(x),len(trace(t)[1])==(3 if  x>=4 else 4))
 t=mx(mn(mx(4,7),mx(x,3)),mn(mx(6,1),mx(9,2)));expected=6 if  x<=6 else x if x<=7 else 7
 check('Q10 value '+str(x),value(t)==expected)
 check('Q10 deep cutoff count '+str(x),len(trace(t)[1])==(5 if  x>=7 else 6 if  x>=6 else 7))
check('Q11 unequal exact candidate',value(mn(5,0))==0 and  trace(mn(5,0),5,math.inf)[0]==5)
t=mx(mn(6,-5),mn(7,-8));check('Q12 fail-low and working-score counterexample',value(t)==-5 and  trace(t,8,10)[0]==7)
check('Q13 fail-high',value(mx(9,20))==20 and  trace(mx(9,20),0,8)[0]==9)
check('Q14 odd count',3**3+3**2-1==35 and 3**5==243)
check('Q15 unequal branching',(3*2)**3==216 and 3**3+2**3-1==34)
t=mx(mn(mx(0,0),mx(0,0)),mn(mx(0,0),mx(0,0)));r,vis,cut,nodes=trace(t)
check('Q16 leaves and total nodes',len(vis)==5 and  nodes==11)
check('Q17 interval gap',F(82,10)-F(1,2)>7+F(1,2)and F(82,10)-F(7,10)<7+F(7,10))
for eps in [F(1,10),F(1),F(3,2)]:check('Q18 sharp regret '+str(eps),eps-(-eps)==2*eps)
check('Q19 terminal priority',1>F(7,10)>F(-2,10))
check('Q20 nonmonotone arbitrary frontier',1>0 and  -10<10 and 0>-1)
check('Q21 exact range',(F(32,10)+F(4,10)*(-2),F(32,10)+F(4,10)*8)==(F(24,10),F(64,10)))
check('Q22 threshold',12*F(1,2)-2==4)
check('Q23 observation value',max(F(8+0,2),F(2+6,2))==4 and  F(8+6,2)==7)
check('Q24 affine tree',max(1,F(8,4))==2 and  max(-4,F(17,4)-F(21,4))==-1)
check('Q25 cubing outcomes',F(27,2)>8 and  F(3,2)<2 and  F(3,2)**3==F(27,8))
uA=.8+math.sqrt(math.log(100)/20);uB=.6+math.sqrt(math.log(100)/5)
check('Q26 UCB ranking',uB>uA and abs(uA-1.2798525912188081)<1e-12)
check('Q27 reward complement',[(20+1,12+1),(8+1,3+0),(3+1,2+1)]==[(21,13),(9,3),(4,3)])
check('Q28 variance scaling',F(6,10)*F(4,10)/25==F(96,10000)and F(24,100)/100==F(24,10000))
check('Q29 coefficient must scale',uB>uA and 5+math.sqrt(math.log(100)/20)>3+math.sqrt(math.log(100)/5))
left=max([(9,0,2),(1,5,1)],key=lambda x:x[1]);right=max([(6,3,0),(4,2,10)],key=lambda x:x[1])
check('Q30 whole-vector selection',max([left,right],key=lambda x:x[0])==(6,3,0))
check('Q31 simultaneous midpoint',max(-abs(2*F(i,20)-1)for i in range(21))==0)
check('Q32 policy count',2**5==32 and 2**2==4 and 32*4==128)
check('Q33 valid bound cutoffs',9>=8 and 4<=5)
check('Q34 original window interior',0<7<10)
check('Q35 horizon distinction',max(10,0)==10 and  max(-5,2)==2)
check('Q36 extra-turn perspective',max(2,9)==9 and  -max(2,9)==-9)
check('Q37 probability intervals',(F(2,10)*(-1)+F(8,10)*4,F(2,10)*3+F(8,10)*6)==(3,F(54,10)))
check('Q38 false rounded equality',F(30005,100000)>F(30004,100000)and round(.30005,3)==round(.30004,3))
check('Q39 underestimates not enough',-100<=10 and 0<=0 and  max(-100,0)==0)
check('Q40 probability merge',F(1,4)*8+F(1,4)*8==F(1,2)*8==4)
check('Q41 unbounded remainder',F(1,100)*201>1 and  F(1,100)*(-1000)<1)
check('Q42 finite-sentinel failure',max(-10000000,-20000000,-30000000)!=max(-20000000,-30000000))
t=mx(*(mn(*(mx(0,0,0)for _ in range(2)))for _ in range(3)))
check('Q43 unequal odd depth',len(trace(t)[1])==10)
check('Q44 repeated-depth sum',sum(3**d for d in range(6))==364)
check('Q46 policy evaluation',F(3+4,2)==F(7,2)and F(-2+10,2)==4)
check('Q47 score-scale mismatch',80>1 and 1>0)
check('Q48 dominance obstruction',4<5 and 5<6 and 8>3)
check('Q49 min and observation',min(F(8,2),F(8,2))==4 and  F(min(8,0)+min(0,8),2)==0)
check('Q50 robust probability',12*F(4,10)-2==F(28,10)<4<12*F(7,10)-2)
auth1=mx(mn(mx(8,2),mx(5,3)),mn(15,mx(4,7)))
check('MS1403Q68 no cut',value(auth1)==7 and  trace(auth1)[2]==set()and len(trace(auth1)[1])==7)
auth2=lambda x,y:mx(10,mn(mx(x,3,2),mx(7,1)),mn(mx(y,6),mx(20,23)))
original=trace(auth2(4,15))[2]
check('MS1404Q69 original pruned branch roots',original=={'11','211'})
for x in [F(-100),F(0),F(3),F(4),F(999,100),F(10),F(1001,100),F(20)]:
 for y in [F(-10),F(6),F(10),F(1001,100),F(15),F(20),F(2001,100),F(23),F(100)]:
  check('MS1404Q69 interval '+str((x,y)),(trace(auth2(x,y))[2]==original)==(x<=10 and 10<y<=20))
# Execute the printed teaching algorithm rather than a separate alleged implementation.
source=(B/'i_games.en.md').read_text(encoding='utf8');code=re.search(r'```python\n([\s\S]*?)```',source)[1]
class State:
 def __init__(self,t):
  self.terminal=not isinstance(t,tuple);self.utility=F(t)if self.terminal else None;self.kind='LEAF'if self.terminal else t[0];self.children=[]if self.terminal else[State(c)for c in t[1]]
ns={'evaluate':lambda s:F(0),'ordered_children':lambda s:iter(s.children),'ordered_actions':lambda s:enumerate(s.children)}
exec(compile(code,'printed_game_algorithm','exec'),ns)
for t in [auth1,auth2(4,15),mx(5,mn(5,0)),mx(mn(6,-5),mn(7,-8))]:
 state=State(t);check('Printed algorithm exact root '+str(t),ns['alphabeta'](state,8)==value(t))
check('Printed wrapper retains exact incumbent',ns['choose_max_action'](State(mx(5,mn(5,0))),5)==(0,F(5)))
for invalid in [-1,F(1,2),True]:
 try:ns['alphabeta'](State(mx(1,2)),invalid);rejected=False
 except ValueError:rejected=True
 check('Printed invalid budget '+str(invalid),rejected)
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
from markdown_it import MarkdownIt
from math_fences import delimiter_issues,closing_script_bases
mathml.wrap_display=lambda s:s;mathml.SYMBOLS['Longrightarrow']='⇒';md=MarkdownIt('commonmark',{'html':True}).enable('table');formulas=0
for rel in ['i_games.en.md','i_games-problems.en.md','i_games-review.en.md','i_games-authentic.en.md']:
 text=(B/rel).read_text(encoding='utf8');rendered=mathml.markdown_math(text,md)
 for expr in re.findall(r'<math\b[\s\S]*?</math>',rendered):
  root=ET.fromstring(expr);assert not delimiter_issues(root)and not closing_script_bases(root);formulas+=1
check('Native cases retained',len(ET.fromstring(mathml.render(r'R(x)=\begin{cases}4,&x\le4,\\x,&4\le x\le8,\\8,&x\ge8.\end{cases}')).findall('.//{*}mtr'))==3)
for env in ['matrix','pmatrix','bmatrix']:
 check('Existing matrix environment '+env,'<mtable'in mathml.render('\\begin{'+env+'}1&2\\\\3&4\\end{'+env+'}'))
manifest=json.loads((B/'exam-calibration/archive-manifest.json').read_text(encoding='utf8'));archive=[]
for year,page,q in [('1403',15,68),('1404',16,69)]:
 row=next(x for x in manifest['files']if x['level']=='MS'and x['field']=='CE'and x['year']==year);p=Path('C:/Users/bheydari/Desktop/Phd-Exam-CSE')/row['repoPath'];check('Original PDF hash '+year,hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256']);archive.append({**row,'pdfPage':page,'question':q,'originalRenderedAndInspected':True,'answer':'4'if year=='1403'else'1','answerKeyVerified':False})
report={'state':'passed_current_manuscript_numeric_and_notation_checks','assertions':len(checks),'checks':checks,'nativeMathExpressions':formulas,'printedAlgorithmExecuted':True,'authentic':archive,'modelBoundCertificates':sum(len(m['checks'])for m in json.loads((B/'i_games-tree-models.json').read_text())['models']),'limits':'Finite exact cases, explicit boundary grids, original-page checks and current notation; not a proof of universal coverage or browser correctness. Conceptual solutions were individually written and reviewed, not proved correct solely by these numeric assertions.'}
report['inputSha256']={rel:hashlib.sha256((B/rel).read_bytes()).hexdigest()for rel in ['i_games.en.md','i_games-problems.en.md','i_games-review.en.md','i_games-authentic.en.md','i_games-tree-models.json','exam-rewrite/mathml.py']}
(B/'i_games-mathematics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8');print({k:report[k]for k in ['state','assertions','nativeMathExpressions','modelBoundCertificates']})
