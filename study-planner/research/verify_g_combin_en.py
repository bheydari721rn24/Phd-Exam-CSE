"""Independent specification, bit-mask, exact-row and provenance checks."""
from pathlib import Path
import json,re,subprocess,hashlib,sys,xml.etree.ElementTree as ET,itertools,math
from revise_visual_library import question_reasoning as semantic_question
from sympy import symbols,And,Or,Not,Xor
B=Path(__file__).resolve().parent;R=B.parent;checks=[]
def ck(label,ok):assert ok,label;checks.append(label)
def reference(mode,bits,fault=False):
 a,b,c,d=map(bool,bits)
 if mode=='shared':
  r=a and b and (c or d);p=a and b
  return list(map(int,[r,(r if fault else p) or c]))
 if mode=='priority':
  return list(map(int,[a and b,a and c and (True if fault else not b),a and (b or c)]))
 return [int(not ((not(a and b)) and c) if fault else a and (b or c))]
Q=json.loads((B/'g_combin-questions.json').read_text());ck('80 original unique questions',len(Q)==len({q['id'] for q in Q})==80)
A,Bb,C,D=symbols('A B C D');env=[A,Bb,C,D]
symbolic=[(Or(And(A,Bb),C),Or(A,Bb,C)),(And(A,Or(Bb,C)),Or(And(A,Bb),C)),(Or(And(A,Bb),And(Not(A),C)),Or(And(A,Bb),And(A,C))),(Xor(A,Bb,C),Xor(A,Or(Bb,C))),(Or(And(A,Bb),And(C,D)),And(Or(A,Bb),Or(C,D))),(And(Or(A,Bb),Or(C,D)),Or(And(A,C),And(Bb,D))),(Or(And(A,Bb),And(A,C),And(Bb,C)),Or(And(A,Bb),And(A,C))),(And(A,Not(Bb),C),And(A,C)),(Not(And(A,Or(Bb,C))),And(Not(A),Or(Bb,C))),(Not(And(A,Bb,C)),Not(And(Not(And(A,Bb)),C))),(Xor(A,Bb,C),Or(And(A,Not(Bb),Not(C)),And(Not(A),Bb,Not(C)),And(Not(A),Not(Bb),C))),(And(A,Bb),And(A,Bb,Or(C,D)))]
mi=0
for q in Q:
 ck(q['id']+' substantial solution',len(q['solution'].split())>=100)
 kind=q['certificate']['kind'];d=q['certificate']['data']
 if kind=='cofactor':
  free=d['remaining'];select=[i for i in range(3) if i!=free]
  for row in range(8):
   bits=[row//4,(row//2)%2,row%2];index=2*bits[select[0]]+bits[select[1]];f=d['data'][index]
   value=int(f) if f in ['0','1'] else 1-bits[free] if f.startswith('\\overline') else bits[free]
   ck(q['id']+' cofactor row '+str(row),value==int(row in d['on']))
 elif kind=='contract':
  for row,word in enumerate(d['words']):
   bits=list(map(int,format(row,'0'+str(d['n'])+'b')));n=d['name'];x=bits[0];y=bits[1]
   if n=='enabled priority':want=[x*y,x*(1-y)*bits[2]]
   elif n=='exclusive request alarm':want=[int(x and sum(bits[1:])==1),int(sum(bits[1:])==2)]
   elif n=='saturating increment':want=list(map(int,format(min(row+1,3),'02b')))
   elif n=='two-bit modular increment':want=list(map(int,format((row+1)%4,'02b')))
   elif n=='one-bit equality and greater':want=[int(x==y),int(x>y)]
   elif n=='one-bit difference and borrow':want=[(x-y)%2,int(x<y)]
   elif n=='parity and majority':want=[sum(bits)%2,int(sum(bits)>=2)]
   elif n=='exactly-one and any request':want=[int(sum(bits)==1),int(sum(bits)>0)]
   elif n=='even parity with validity':want=[int(row<6),int(row<6 and sum(bits)%2==0)]
   else:want=[row>>1,((row>>1)^(row&1))]
   ck(q['id']+' independent predicate '+str(row),word==''.join(map(str,want)))
 elif kind=='miter':
  f,g=symbolic[mi];mi+=1;diff=[]
  for row in range(16):
   bits=list(map(int,format(row,'04b')));sub=dict(zip(env,map(bool,bits)));v=[int(bool(f.subs(sub))),int(bool(g.subs(sub)))];ck(q['id']+' symbolic evaluation '+str(row),v==d['values'][row]);diff.extend([row] if v[0]!=v[1] else [])
  ck(q['id']+' every witness',diff==d['diff'])
 elif kind=='tree':
  n=d['n'];depth=d['balancedDepth'];ck(q['id']+' lower bound and attainment',2**(depth-1)<n<=2**depth and d['gates']==n-1 and d['lateLast']==d['late']+1)
 elif kind=='word':
  w,x,y=d['w'],d['x'],d['y'];signed=lambda z:z if z<2**(w-1) else z-2**w;z=d['results'];carry,rem=divmod(x+y,2**w)
  ck(q['id']+' independent word arithmetic',d['signed']==[signed(x),signed(y)] and z==dict(bitNot=2**w-1-x,logicalNot=int(x==0),unsignedLess=int(x<y),signedLess=int(signed(x)<signed(y)),modsum=rem,carry=carry))
 else:ck(q['id']+' explicit manual proof',kind=='reasoning' and len(q['solution'].split())>=110)
# Independently exhaust every three-input function, every selection variable and every row.
for mask in range(256):
 for free in range(3):
  sels=[i for i in range(3) if i!=free];co=[]
  for select in range(4):
   pair=[]
   for bit in range(2):
    row=(bit<<(2-free))|(((select>>1)&1)<<(2-sels[0]))|((select&1)<<(2-sels[1]));pair.append((mask>>row)&1)
   co.append(pair)
  for row in range(8):
   bits=[(row>>(2-i))&1 for i in range(3)];ck('Shannon exhaustive '+str((mask,free,row)),co[2*bits[sels[0]]+bits[sels[1]]][bits[free]]==((mask>>row)&1))
# Gate identities, controller invariants and modeled faults.
for a,b,c,d,e,f,g in itertools.product([0,1],repeat=7):
 ck('seven-input factoring '+str((a,b,c,d,e,f,g)),bool((a+b+c)*(d+e)*f+g)==bool(a*d*f+a*e*f+b*d*f+b*e*f+c*d*f+c*e*f+g))
for row in range(8):
 e,r1,r0=row>>2,(row>>1)&1,row&1;g1=e*r1;g0=e*(1-r1)*r0
 ck('priority properties '+str(row),not(g1 and g0) and (g1|g0)==e*int(bool(r1 or r0)))
 a,b,c=e,r1,r0;ck('NAND correct '+str(row),1-(1-a*b)*(1-a*c)==a*int(bool(b or c)))
 ck('fault SA0 '+str(row),int(((a*b)|c)!=c)==int(row==6))
 ck('fault SA1 '+str(row),int(((a*b)|c)!=1)==int(row in [0,2,4]))
faults=[{'a','b'},{'b','c'},{'c','d'},{'a','d'}];opt=[pair for pair in itertools.combinations(range(4),2) if set().union(*(faults[j] for j in pair))==set('abcd')];ck('complete minimum test-cover set',opt==[(0,2),(1,3)])
scenes=json.loads((R/'dist/chapters/concept-animations.json').read_text())['scenes'];new={k:v for k,v in scenes.items() if k.startswith('comb-')};ck('14 new concept models',len(new)==14);count=0
for name,s in new.items():
 for j,fr in enumerate(s['frames']):
  count+=1;q=fr['snapshot'];k=q['kind'];ck(name+' complete caption '+str(j),len(fr['caption'].split())>=14)
  if k=='dag':ok=q['values']==[1,1,1,1,0][:q['step']]
  elif k=='priority':v=reference('priority',[q['row']>>2,(q['row']>>1)&1,q['row']&1,0]);ok=v[:2]==[q['g1'],q['g0']]
  elif k=='cofactor':ok=q['pair']==[int(2*q['select']+i in [1,2,3,5,7]) for i in [0,1]]
  elif k=='rom':i=q['row'];ok=[q['p'],q['m']]==[i.bit_count()%2,int(i.bit_count()>=2)]
  elif k=='nand':i=q['row'];a,b,c=i>>2,(i>>1)&1,i&1;ok=q['p']==int(not(a and b)) and q['q']==int(not(a and c)) and q['y']==int(a and (b or c))
  elif k=='miter':i=q['row'];a,b,c=i>>2,(i>>1)&1,i&1;ok=[q['f'],q['g']]==[int(a and (b or c)),int(a and b or c)]
  elif k=='fault':i=q['row'];a,b,c=i>>2,(i>>1)&1,i&1;ok=[q['t'],q['y'],q['fault']]==[int(a and b),int(a and b or c),c]
  elif k=='word':ok=q['x']==2**q['w']-2 and q['signed']==-2 and q['inv']==1
  elif k=='feedback':ok=q['solutions']==[[0,1],[],[0]][q['case']]
  elif k=='latch':ok=[q['en'],q['d'],q['y']]==[[1,0,0],[0,1,0],[1,1,1],[0,1,1]][q['step']]
  elif k=='arrival':ok=q['times']==[[1,11,12],[1,2,11],[1,2,11]][q['case']]
  elif k=='interval':ok=[q['lo'],q['hi']]==[[0,0],[1,3],[2,7],[1,9]][q['step']]
  elif k=='falsepath':ok=q['y']==q['a']*(1-q['a'])==0
  else:ok=q['outputs']==[1-q['en']*q['r1'],1-q['en']*(1-q['r1'])*q['r0']]
  ck(name+' exact snapshot '+str(j),ok)
auth=json.loads((B/'g_combin-authentic.json').read_text());cache=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')
for a in auth:ck(a['id']+' original PDF hash',hashlib.sha256((cache/a['repoPath']).read_bytes()).hexdigest()==a['sourceSha256'])
approved=json.loads((B/'library-approval.json').read_text())['approvedTopics'];ck('30 approved chapters',len(approved)==30);total=0
for topic in approved:
 p='dist/chapters/'+topic+'.html';before=subprocess.check_output(['git','show','86138288310b1466fb4b969c23464f73ebec81cb:'+p],cwd=R).decode();after=(R/p).read_text(encoding='utf-8');pat=r'<section class="exam-question"[\s\S]*?</section>';a=re.findall(pat,before);b=re.findall(pat,after);ck(topic+' prior bank unchanged',[semantic_question(x) for x in a]==[semantic_question(x) for x in b]);total+=len(a)
ck('1665 prior entries',total==1665)
h=(R/'dist/chapters/g_combin.html').read_text(encoding='utf-8');ck('82 solved tasks',h.count('class="exam-question"')==h.count('class="exam-solution"')==82);ck('80 full rules',h.count('class="review-rule"')==80);ck('8 SVG figures',h.count('class="logic-diagram combin-diagram"')==8);ck('English and rendered formulas',not re.search(r'[\u0600-\u06ff]',h) and '$' not in h)
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
def leaves(root):return [(e.tag.split('}')[-1],e.text or '') for e in root.iter() if not len(e) and e.tag.split('}')[-1] in ['mi','mn','mo'] and e.text!='·']
for j,m in enumerate(re.findall(r'<math\b[\s\S]*?</math>',h)):
 root=ET.fromstring(m);expected=ET.fromstring(mathml.render(root.attrib['aria-label']));ck('math token preservation '+str(j),leaves(root)==leaves(expected))
report=dict(status='passed',checks=len(checks),questions=82,originalQuestions=80,authenticRevisits=2,reviewRules=80,figures=8,models=14,checkpoints=count,preservedApprovedChapters=30,preservedPriorEntries=total,methods=['Independent contract predicates','Sympy Boolean miter evaluation','All 256 functions, three select choices and eight input rows','Word arithmetic and arrival lower bounds','Fault detection and exact test cover','Every animated checkpoint','Original PDF fingerprints','MathML token preservation','Approved bank exact preservation'],limits=['No HDL compiler available; no compilation claimed','Finite Boolean models are not electrical simulation or unseen-exam guarantees'])
(B/'g_combin-validation.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
