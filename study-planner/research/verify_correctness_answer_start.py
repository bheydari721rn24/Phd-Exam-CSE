from pathlib import Path
from fractions import Fraction
import json,re,sys,math,hashlib
B=Path(__file__).parent;E=B/'deep-library-revision';sys.path.insert(0,str(B/'exam-rewrite'));import mathml
from markdown_it import MarkdownIt
from xml.etree import ElementTree as ET
from read_correctness_bank import rows
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True});checks=0
def ck(x):
 global checks
 assert x;checks+=1
for x in range(-100,101):
 ck(((x+3)**2==25)==(x==2 or x==-8));ck((2*(x+1)-3==7)==(x==4));ck(((-x if x<0 else x+2)>=3)==(x<=-3 or x>=1))
 for y in range(-10,11):
  simultaneous=(y,x+y);sequential=(y,2*y);ck((simultaneous==sequential)==(x==y))
for i in range(8):
 for j in range(8):
  a=[9]*8;a[i]=1;a[j]=2;ck((a[i]==1 and a[j]==2)==(i!=j))
for n in range(1,401):
 x=n;k=0
 while x>0:x=max(0,x-3);k+=1;ck(x==max(0,n-3*k))
 ck(k==(n+2)//3)
for k in range(1,151):ck(Fraction(1,2**k)>0 and Fraction(1,2**k)<Fraction(1,2**(k-1)))
ck((8,13)==(8,5+8));ck((8,16)==(8,8+8));ck(1>=0 and -1<0);ck(1>=0 and 1!=0)
text=(E/'a_correct-solutions.md').read_text();parts=re.split(r'^### Solution (\d+)\s*$',text,flags=re.M);answers={int(parts[i]):parts[i+1].strip()for i in range(1,len(parts),2)};ck(list(answers)==list(range(5,17)));expressions=0
for n,s in answers.items():
 ck(s.startswith('**Correct option: '+str(rows[n-1]['answer'])+'.'))
 for x in re.findall(r'<math\b[\s\S]*?</math>',mathml.markdown_math(s,md)):ET.fromstring(x);expressions+=1
 ck(len(s.split())>=170)
report=dict(topicId='a_correct',status='passed_bounded_initial_answer_checks',completeChapter=False,answerIndices=list(answers),answersWritten=len(answers),answerWords=sum(len(s.split())for s in answers.values()),minimumAnswerWords=min(len(s.split())for s in answers.values()),assertions=checks,parsedNativeExpressions=expressions,manuscriptSha256=hashlib.sha256(text.encode()).hexdigest(),remaining='Forty-two answers, four-source reading criterion, original-exam image reconciliation, deeper additions/final rules, models, independent browser/print audits and publication remain. Draft checks are not a completed chapter.')
(E/'a_correct-answer-start-checks.json').write_text(json.dumps(report,indent=2)+'\n');print(report)
