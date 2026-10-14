from pathlib import Path
from collections import Counter
from fractions import Fraction
from math import comb
import hashlib,json,re,subprocess,sys
from xml.etree import ElementTree as ET
from space_number_prose import fix
from read_correctness_bank import ns
R=Path(__file__).resolve().parents[1];E=R/'research/deep-library-revision';sys.path.insert(0,str(R/'research/exam-rewrite'));from math_fences import delimiter_issues
checks=0
def ck(x,context=''):
 global checks
 assert x,context;checks+=1
old=fix(subprocess.check_output(['git','show','c09d0bb:dist/chapters/a_correct.html'],cwd=R).decode('utf8').replace('\r\n','\n'));page=(R/'dist/chapters/a_correct.html').read_text(encoding='utf8')
start='<h2 id="contracts">';end='<section class="exam-question"';ck(old[old.index(start):old.index(end)]==page[page.index(start):page.index('<section class="exam-question"')], 'Original full teaching body must be retained verbatim before the rewritten bank.')
questions=ns['questions'](page);ck(len(questions)==54);ck(page.count('data-deep-index=')==54);ck('Student-approved chapter'not in page);ck('proof-construction'in page)
parsed=0
for value in re.findall(r'<math\b[\s\S]*?</math>',page):
 root=ET.fromstring(value);ck(not delimiter_issues(root),value[:100]);parsed+=1
for _,_,attrs,q in questions:
 n=int(attrs['data-deep-index']);ck(q.count('correctness-question-q'+str(n)+'"')==1,n);ck(q.count('<details class="exam-solution">')==1,n);ck(q.count('exam-option"')==4,n)
models=json.loads((E/'a_correct-models.json').read_text(encoding='utf8'))['models'];ck(len(models)==54);ck(sum(len(s['frames'])for s in models.values())==203)
for key,s in models.items():
 ck(s['id']==key and s['description']and len(s['frames'])>0)
 for f in s['frames']:
  ck(f['caption']and f['teaching']['why']);ck(not delimiter_issues(ET.fromstring(f['formulaHtml'])))
def states(n):return[f['snapshot']for f in models['correctness-question-q'+str(n)]['frames']]
for n,N in[(2,6),(51,10)]:
 for k,s in enumerate(states(n)):
  ck(s['rows'][0]['values']==list(range(N)));ck(s['rows'][1]['values'][:k]==list(range(N-1,N-1-2*k,-2)))
for n,N,c0 in[(4,15,10),(50,4,7)]:
 total=0
 for k,s in enumerate(states(n),1):
  expected=sum(N-j+1 for j in range(k,N+1));total+=expected;ck(s['values']==[k,expected,total,c0+total])
 ck(total==comb(N+2,3))
ck(states(6)[-1]['values']==[7,10]);ck(states(7)[-1]['values']==[8,13,8,16]);ck(states(8)[0]['outputs']==[-x if x<0 else x+2 for x in range(-4,4)])
for n in[17,18,19,20,21]:
 for s in states(n):
  ck(0<=s['lo']<=s['hi']<=len(s['values']))
  if s['mid']is not None:ck(s['lo']<=s['mid']<s['hi'])
ck(states(17)[-1]['lo']==1);ck(states(18)[-1]['iterations']==5);ck(states(19)[-1]['lo']==0 and states(19)[-1]['hi']==1);ck(states(20)[-1]['lo']==2);ck(states(21)[-1]['lo']==4)
for s in states(22):
 L,left,right,maximum=s['values'];ck(left==L//2 and right==L-L//2-1 and maximum==max(left,right))
ck(states(23)[-1]['rows'][0]['values']==[1,2,3,4]);ck(states(24)[1]['rows'][0]['values']==[1,4,4]and states(24)[1]['rows'][0]['hole']==1)
for n in[29,31]:
 first=states(n)[0];initial=Counter(first['values'])
 for k,s in enumerate(states(n)):
  a=s['values'];p=s['pivot'];ck(Counter(a)==initial);ck(all(v<p for v in a[:s['lt']])and all(v==p for v in a[s['lt']:s['i']])and all(v>p for v in a[s['gt']:]));ck(s['gt']-s['i']==len(a)-k)
ck(states(29)[-1]['lt']==2 and states(29)[-1]['gt']==3);bad=states(30)[-1];ck(bad['values']==[1,3]and bad['lt']==0 and bad['i']==bad['gt']==1)
for s in states(33):q,r,guard=s['values'];ck(47==6*q+r and r>=0 and(guard=='true')==(r>=6))
for s in states(34):q,r,guard=s['values'];ck(47==q*0+r and r==47 and guard=='true')
ck(states(36)[-1]['values']==[1,0,7])
for n,a,B in[(37,3,13),(38,2,45)]:
 for s in states(n):
  r,b,e,c,sq=s['values'];ck(int(r)*int(b)**e==a**B);ck(c<=sq)
 ck(states(n)[-1]['values'][3:]==[B.bit_count(),B.bit_length()])
ck(states(37)[2]['values']==['3','81',3,1,2]);ck(states(39)[-1]['values']==[4,4,0]);ck(states(40)[-1]['values']==[1,0,0])
for n in[44,45,46,47]:
 for s in states(n):
  d={v['id']:v['value']for v in s['nodes']}
  for u,v,w,flag in s['graphEdges']:ck(flag==(d[v]<=d[u]+w))
ck(sum(x[2]for x in states(47)[0]['graphEdges'])==-2)
for s in states(52):k,value,guard,variant=s['values'];ck(value==(k-1)**2 and variant==5-k and(guard=='true')==(k<=4))
ck(states(53)[0]['treeEdges']==[['left','output'],['right','output']]);ck(Fraction(1,2)+Fraction(1,4)+Fraction(1,8)==Fraction(7,8))
source=(E/'a_correct-current-source-review.md').read_text(encoding='utf8');ck(all(x in source for x in['Carnegie Mellon','Stanford','Massachusetts','Cornell']));original=json.loads((E/'a_correct-original-recheck.json').read_text());ck(len(original)==4 and all(x['visualReconciled']for x in original))
report={'topicId':'a_correct','status':'passed_document_and_exact_model_checks','assertions':checks,'nativeExpressions':parsed,'models':54,'frames':203,'retainedOriginalTeachingBody':True,'courseScopesActuallyReviewed':4,'authenticQuestionsReconciled':4,'pageSha256':hashlib.sha256(page.encode()).hexdigest(),'limits':'Finite concrete model checks supplement written general proofs. The candidate pool is bounded. Checks are not a universal guarantee.'}
(E/'a_correct-document-checks.json').write_text(json.dumps(report,indent=2)+'\n');print(report)
