from pathlib import Path
from itertools import product,permutations
import math,json,re,sys,hashlib
from read_divide_bank import rows
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';checks=0
def check(v,label=''):
 global checks
 assert v,label;checks+=1
def merge_count(a):
 if len(a)<2:return list(a),0
 l,x=merge_count(a[:len(a)//2]);r,y=merge_count(a[len(a)//2:]);i=j=0;out=[];c=x+y
 while i<len(l)and j<len(r):
  c+=1
  if l[i]<=r[j]:out.append(l[i]);i+=1
  else:out.append(r[j]);j+=1
 return out+l[i:]+r[j:],c
check(merge_count([12,7,5,9,3,8,2,6])==([2,3,5,6,7,8,9,12],16))
check(merge_count(list(range(1,9)))[1]==12)
for a in permutations(range(8)):check(merge_count(a)[1]<=17)
check(max(merge_count(a)[1]for a in permutations(range(6)))==11)
def adversary(keys):return keys if len(keys)<2 else adversary(keys[::2])+adversary(keys[1::2])
for h in range(11):
 N=2**h;check(merge_count(adversary(list(range(N))))[1]==h*N-N+1);check(merge_count(list(range(N)))[1]==h*N//2)
def cross(l,r):return sum(x>y for x in l for y in r)
check(cross([1,3,3],[2,3,4])==2)
for n in range(1,33):check(cross(list(range(n,2*n)),list(range(n)))==n*n)
def summary(a):
 total=sum(a);prefix=max(sum(a[:i])for i in range(1,len(a)+1));suffix=max(sum(a[i:])for i in range(len(a)));best=max(sum(a[i:j])for i in range(len(a))for j in range(i+1,len(a)+1));return total,prefix,suffix,best
def join(a,b):
 t,p,s,v=a;u,q,r,w=b;return t+u,max(p,t+q),max(r,u+s),max(v,w,s+q)
for n in range(2,7):
 for a in product([-2,0,3],repeat=n):
  for k in range(1,n):check(join(summary(a[:k]),summary(a[k:]))==summary(a))
left=[3,-6,5,-5,1];right=[6,-2];check(summary(left)==(-2,3,1,5));check(summary(right)==(4,6,4,6));check(join(summary(left),summary(right))==(2,4,5,7))
check(8*100+(55-8-21)*10+21==23*47==1081)
def groups(n):
 out=[];positive=3
 for i in range(1,n+1):out.append([-3*i-2,-3*i-1,-3*i,positive,positive+1]);positive+=2
 out.append([-2,-1,0,1,2])
 for i in range(n):out.append(list(range(positive,positive+5)));positive+=5
 return out
for n in range(1,51):
 gs=groups(n);values=[v for g in gs for v in g];medians=sorted(sorted(g)[2]for g in gs);check(len(values)==10*n+5 and len(values)==len(set(values)));check(medians[n]==0);check(sum(v<0 for v in values)==3*n+2);check(sum(v>0 for v in values)==7*n+2)
 for g in gs:check(len(g)==5)
for n in range(1,41):
 counts=[1,1,0]
 for _ in range(n):counts=[3*counts[0],7*counts[1],2*counts[2]+2**(_)]
 check(counts[0]==3**n);check(counts[1]==7**n);check(counts[2]==n*2**n//2)
 ones=[1]*n;conv=[sum(ones[i]*ones[k-i]for i in range(n)if 0<=k-i<n)for k in range(2*n-1)];check(len(conv)==2*n-1 and conv[0]==conv[-1]==1)
 def visited(lo,hi):
  if lo==hi:return 1
  return 1+visited(lo,(lo+hi)//2)
 check(visited(0,2**n-1)==n+1)
check([sum(a*pow(4,j*k,17)for k,a in enumerate([1,2,0,0]))%17 for j in range(4)]==[3,9,16,10])
check([c for c in range(-10,11)if c%17==7]==[-10,7])
for B0 in range(21):
 for M in range(2*B0+1,2*B0+7):check(len({c%M for c in range(-B0,B0+1)})==2*B0+1)
fns=[lambda n:n*2**n-2**n+1,lambda n:n*n,lambda n:3**n,lambda n:7**n,lambda n:2*n-1,lambda n:n*2**n//2,lambda n:3*n+2,lambda n:n+1]
for i,fn in enumerate(fns):
 start=13+4*i
 for j,n in enumerate([5,8]):r=rows[start+j-1];check(r['options'][r['answer']-1]=='$'+str(fn(n))+'$',(start+j,n))
sys.path.insert(0,str(B/'exam-rewrite'));import mathml;mathml.wrap_display=lambda s:s
manuscript=(E/'a_divide-solutions.md').read_text();equations=re.findall(r'\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$',manuscript)
for a,b in equations:mathml.render(a or b,bool(a));checks+=1
sources={q['id']:q for q in json.loads((B/'exam-calibration/actual-items.json').read_text())}
for id in ['Phd_CE_1405_Q1','Phd_CE_1405_Q9','Phd_CE_1405_Q16','MS_CE_1405_Q59']:
 q=sources[id];p=Path('C:/Users/bheydari/Desktop/Phd-Exam-CSE')/q['repoPath'];check(hashlib.sha256(p.read_bytes()).hexdigest()==q['sourceSha256'])
record=dict(status='passed_bounded_answer_oracles_pending_full_chapter_and_visual_audits',topicId='a_divide',checks=checks,nativeFormulaStringsParsed=len(equations),authenticSourceHashesChecked=4,questionCount=46,manuscriptSha256=hashlib.sha256(manuscript.encode()).hexdigest(),limits='This checks the answer manuscript and its declared finite mechanisms. The deeper lesson, final rules, original-course diagram reconciliation, dedicated animations, browser and private publication are not completed by this report.')
(E/'a_divide-answer-checks.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8');print(record)
