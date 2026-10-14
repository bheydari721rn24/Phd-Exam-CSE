"""Independent finite oracles for the answer rewrite; explicit proofs cover the general claims."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations_with_replacement,product
from math import comb,gcd,ceil,log2
from collections import Counter
import json,re,sys,hashlib
from xml.etree import ElementTree as ET
from markdown_it import MarkdownIt
from read_correctness_bank import rows
R=Path(__file__).resolve().parents[1];E=R/'research/deep-library-revision';sys.path.insert(0,str(R/'research/exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table');checks=0
def ck(x,context=''):
 global checks
 assert x,context;checks+=1
def lower(a,t,upper=False):
 lo=0;hi=len(a);mids=[];widths=[hi]
 while lo<hi:
  m=(lo+hi)//2;mids.append(m)
  if a[m]<t or upper and a[m]==t:lo=m+1
  else:hi=m
  widths.append(hi-lo)
 return lo,mids,widths
for n in range(10):
 for a in combinations_with_replacement(range(4),n):
  for t in range(-1,5):
   for upper in[False,True]:
    result,_,widths=lower(a,t,upper);expected=next((i for i,v in enumerate(a)if v>t or not upper and v==t),n);ck(result==expected,(a,t,upper))
    ck(all(new<=old//2 for old,new in zip(widths,widths[1:])))
    ck(len(widths)-1<=ceil(log2(n+1)))
ck(lower([1,3,3,3,8,9],3)[:2]==(1,[3,1,0]));ck(max(len(lower(list(range(31)),t)[1])for t in range(-1,33))==5)
ck(lower([4,1,3],3)[0]==2);ck(next(i for i,v in enumerate([4,1,3])if v>=3)==0)
ck((lower([1,2,2,2,5],2)[0],lower([1,2,2,2,5],2,True)[0])==(1,4));ck((0+1)//2==0)
for L in range(1,1000):
 left=L//2;right=L-left-1;ck(max(left,right)==L//2)
for n in range(7):
 for raw in product(range(3),repeat=n):
  a=list(raw);shifts=0
  for i in range(1,n):
   key=a[i];j=i-1
   while j>=0 and a[j]>key:a[j+1]=a[j];j-=1;shifts+=1
   a[j+1]=key
  ck(a==sorted(raw));ck(Counter(a)==Counter(raw));ck(shifts==sum(raw[i]>raw[j]for i in range(n)for j in range(i+1,n)))
  a=list(raw);lt=i=0;gt=n;count=0
  while i<gt:
   before=gt-i
   if a[i]<1:a[lt],a[i]=a[i],a[lt];lt+=1;i+=1
   elif a[i]==1:i+=1
   else:gt-=1;a[i],a[gt]=a[gt],a[i]
   count+=1;ck(gt-i==before-1);ck(all(x<1 for x in a[:lt])and all(x==1 for x in a[lt:i])and all(x>1 for x in a[gt:]));ck(Counter(a)==Counter(raw))
  ck(count==n)
def partition(a,p):
 a=a.copy();lt=i=0;gt=len(a)
 while i<gt:
  if a[i]<p:a[lt],a[i]=a[i],a[lt];lt+=1;i+=1
  elif a[i]==p:i+=1
  else:gt-=1;a[i],a[gt]=a[gt],a[i]
 return a,lt,gt
ck(partition([3,1,2,3,0],2)==([0,1,2,3,3],2,3));ck(Counter([1,4])+Counter([2])==Counter([1,4,2]));ck([('2','b'),('2','a')]!=[('2','a'),('2','b')])
def merge(l,r):
 i=j=c=0;o=[]
 while i<len(l)and j<len(r):
  c+=1
  if l[i]<=r[j]:o.append(l[i]);i+=1
  else:o.append(r[j]);j+=1
 return o+l[i:]+r[j:],c
ck(merge([1,4,7],[2,3,8])==([1,2,3,4,7,8],5));ck(Counter([0,0])!=Counter([3,1]));ck(0//2==0)
for X in range(101):
 for Y in range(1,21):
  q=0;r=X
  while r>=Y:q+=1;r-=Y;ck(X==q*Y+r and r>=0)
  ck((q,r)==divmod(X,Y))
ck(divmod(47,6)==(7,5));ck(47==999*0+47)
for A in range(41):
 for B in range(41):
  a,b=A,B
  while b:before=b;a,b=b,a%b;ck(gcd(a,b)==gcd(A,B)and b<before)
  ck(a==gcd(A,B))
a,b=34,21;steps=0
while b:a,b=b,a%b;steps+=1
ck(steps==7 and a==1);ck(gcd(21,15)==3 and 15%15==0)
def power(a,B):
 r=1;b=a;e=B;acc=squares=0;trace=[(r,b,e)]
 while e:
  if e%2:r*=b;acc+=1
  b*=b;e//=2;squares+=1;trace.append((r,b,e));ck(r*b**e==a**B)
 return r,acc,squares,trace
for a in range(-4,5):
 for e in range(45):
  result,c,s,_=power(a,e);ck(result==a**e and c==e.bit_count()and s==e.bit_length())
ck(power(3,13)[3][2]==(3,81,3));ck(power(2,45)[1:3]==(4,6));ck(2**2!=2**1);ck(1%1==0);ck((200*200)%256==64 and(200*200)%251==91)
def stable_cert(a,b,c):return sorted(c)==list(range(len(a)))and all(a[c[i]]==b[i]for i in range(len(a)))and all(c[i]<c[i+1]for i in range(len(a)-1)if b[i]==b[i+1])
ck(stable_cert([5,1,5],[1,5,5],[1,0,2]));ck(not stable_cert([5,1,5],[1,5,5],[1,2,0]));ck(17<=17<=17)
ck(not(5<=0+4));ck(0<=5 and 0<=0 and 0<=0);ck(4<=4 and 1<=5 and 1<=4-3);ck(sum([2,-5,1])==-2)
intervals=[(0,10),(1,2),(2,3),(3,4)];feasible=[]
for bits in product([0,1],repeat=4):
 selected=[v for b,v in zip(bits,intervals)if b]
 if all(a[1]<=b[0]or b[1]<=a[0]for a,b in __import__('itertools').combinations(selected,2)):feasible.append(len(selected))
ck(max(feasible)==3);ck(sum(Fraction(1,2**d)for d in[1,2,3])==Fraction(7,8))
for n in range(101):
 ck(sum(j*(n-j+1)for j in range(1,n+1))==comb(n+2,3))
 indices=list(range(n-1,-1,-2));ck(len(indices)==(n+1)//2);ck(all(indices[k]==n-1-2*k for k in range(len(indices))))
 s=0;k=1
 while k<=n:s+=2*k-1;k+=1;ck(s==(k-1)**2 and 1<=k<=n+1)
 ck(s==n*n)
ck(list(range(9,-1,-2))==[9,7,5,3,1]);ck(max([0,-2])==0 and max([-2])==-2)
for x in range(-100,101):
 ck(((x+3)**2==25)==(x in[2,-8]));ck((2*(x+1)-3==7)==(x==4));ck(((-x if x<0 else x+2)>=3)==(x<=-3 or x>=1))
 for y in range(-10,11):ck(((y,x+y)==(y,2*y))==(x==y))
for i,j in product(range(8),repeat=2):
 a=[9]*8;a[i]=1;a[j]=2;ck((a[i]==1 and a[j]==2)==(i!=j))
for n in range(401):
 x=n;c=0
 while x:x=max(0,x-3);c+=1
 ck(c==(n+2)//3)
for k in range(150):ck(Fraction(1,2**k)>0)
text=(E/'a_correct-solutions.md').read_text(encoding='utf8');parts=re.split(r'^### Solution (\d+)\s*$',text,flags=re.M);answers={int(parts[i]):parts[i+1].strip()for i in range(1,len(parts),2)};ck(sorted(answers)==list(range(1,55)));parsed=0
for n,s in answers.items():
 ck(s.startswith('**Correct option: '+str(rows[n-1]['answer'])+'.'),n)
 for x in re.findall(r'<math\b[\s\S]*?</math>',mathml.markdown_math(s,md)):ET.fromstring(x);parsed+=1
 ck(len(s.split())>=170,n)
report={'status':'passed_bounded_answer_oracles','completeChapter':False,'topicId':'a_correct','answers':54,'words':sum(len(s.split())for s in answers.values()),'assertions':checks,'parsedNativeExpressions':parsed,'manuscriptSha256':hashlib.sha256(text.encode()).hexdigest(),'scope':'Sorted lower-bound arrays length 0–9 over four values, thresholds -1–4; insertion/partition arrays length 0–6 over three values; division inputs 0–100 and divisors 1–20; gcd inputs 0–40; powers bases -4–4 exponents 0–44; exact arithmetic and specified concrete certificates. General claims require the written proofs.'}
(E/'a_correct-answer-checks.json').write_text(json.dumps(report,indent=2)+'\n');print(report)
