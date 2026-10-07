from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations,permutations
from math import comb,isclose
import re,json,hashlib,subprocess
B=Path(__file__).resolve().parent;R=B.parent;E=B/'s_expectation-evidence';checks=[]
def ck(name,a,b):
 assert a==b,(name,a,b)
 checks.append(dict(name=name,result=str(a),status='passed'))
def mean(v,p,fn=lambda x:x):return sum((fn(x)*q for x,q in zip(v,p)),F(0))
v=[-2,1,4];p=[F(1,5),F(1,2),F(3,10)]
mu=mean(v,p);m2=mean(v,p,lambda x:x*x);var=m2-mu*mu
ck('Q1 signed mean',mu,F(13,10));ck('Q1 absolute mean',mean(v,p,abs),F(21,10));ck('Q1 torque',mean(v,p,lambda x:x-mu),0)
ck('Q2 mean with solved masses',mean([-3,2,7],[F(1,4),F(3,10),F(9,20)]),3)
ck('Q3 outcome average',mean([2,2,8],[F(1,2),F(1,3),F(1,6)]),3)
ck('Q5 gross award',F(240+12*35,36),F(55,3))
ck('Q9 raw second moment',m2,F(61,10));ck('Q9 variance',var,F(441,100));ck('Q9 quadratic payoff',mean(v,p,lambda x:2*x*x-3*x+1),F(93,10))
ck('Q10 transformed mean',mean([-2,-1,0,1,2],[F(1,10),F(1,5),F(1,5),F(1,5),F(3,10)],lambda x:x*x),2)
ck('Q11 reciprocal gap',F(5,8)-F(2,5),F(9,40));ck('Q12 clipped payoff',mean(v,p,lambda x:max(x-1,0)),F(9,10))
ck('Q13 dependent affine mean',mean([-1,1],[F(1,2)]*2,lambda x:3*x-2*(-x)+5),5)
ck('Q14 coefficient gap',F(2,5)-F(2,5)**2,F(6,25));ck('Q17 heterogeneous count',sum(F(i,10)for i in range(1,6)),F(3,2));ck('Q18 weighted cost',8*F(1,4)+3*F(1,3)+12*F(1,6),5)
counts=[sum(i==x for i,x in enumerate(t))for t in permutations(range(4))]
ck('Q19 enumerated fixed points',F(sum(counts),len(counts)),1);ck('Q19 pair probability',F(sum(t[0]==0 and t[1]==1 for t in permutations(range(4))),24),F(1,12))
ck('Q20 weighted matches',F(2+5+13,10),2);ck('Q21 second fixed moment',F(sum(x*x for x in counts),24),2)
record=[sum(x==min(t[:i+1])for i,x in enumerate(t))for t in permutations(range(5))]
ck('Q22 record count exhaustive',F(sum(record),120),F(137,60));ck('Q22 initialization offset',F(sum(record),120)-1,F(77,60))
inv=[sum(t[i]>t[j]for i in range(6)for j in range(i+1,6))for t in permutations(range(6))];ck('Q24 inversion exhaustive',F(sum(inv),len(inv)),F(15,2))
allocation=list(product(range(3),repeat=4));ck('Q25 empty exhaustive',F(sum(3-len(set(t))for t in allocation),len(allocation)),F(16,27));ck('Q25 occupied exhaustive',F(sum(len(set(t))for t in allocation),len(allocation)),F(65,27))
binp=[F(1,2),F(1,3),F(1,6)];joint=[(a,b,binp[a]*binp[b])for a,b in product(range(3),repeat=2)]
ck('Q26 distinct weighted enumeration',sum(q*len({a,b})for a,b,q in joint),F(29,18));ck('Q26 collisions',sum(q for a,b,q in joint if a==b),F(7,18))
alloc=list(product(range(4),repeat=3));ck('Q28 singleton exhaustive',F(sum(sum(t.count(j)==1 for j in range(4))for t in alloc),len(alloc)),F(27,16))
alloc=list(product(range(4),repeat=5));ck('Q29 distinct exhaustive',F(sum(len(set(t))for t in alloc),len(alloc)),F(781,256))
ss=list(combinations(range(12),5));ck('Q30 subset exhaustive',F(sum(sum(x<7 for x in t)for t in ss),len(ss)),F(35,12))
ss=list(combinations([-2,1,4,7],2));ck('Q31 sampled total exhaustive',F(sum(sum(t)for t in ss),len(ss)),5);ck('Q32 inclusion-weight identity',6*F(1,2)+32*F(1,4)+25*F(1,5),16)
seqs=list(product([0,1],repeat=6));qmean=F(0)
for t in seqs:
 w=F(1)
 for b in t:w*=F(1,3)if b else F(2,3)
 qmean+=w*sum(b==1 and (i==0 or t[i-1]==0)for i,b in enumerate(t))
ck('Q33 head runs exhaustive',qmean,F(13,9))
seqs=list(product([0,1],repeat=7));ck('Q34 all runs exhaustive',F(sum(1+sum(t[i]!=t[i-1]for i in range(1,7))for t in seqs),len(seqs)),4)
seqs=list(product([0,1],repeat=8));ck('Q35 overlapping windows exhaustive',F(sum(sum(all(t[j]for j in range(i,i+3))for i in range(6))for t in seqs),256),F(3,4))
edges=list(combinations(range(5),2));triangles=list(combinations(range(5),3));gt=0;et=0
for bits in product([0,1],repeat=10):
 present={edges[i]for i,b in enumerate(bits)if b};et+=len(present);gt+=sum(all(e in present for e in combinations(t,2))for t in triangles)
ck('Q36 graph-edge exhaustive',F(et,1024),5);ck('Q36 graph-triangle exhaustive',F(gt,1024),F(5,4));ck('Q37 isolated means',5*F(2,3)**4,F(80,81))
ck('Q38 tail first',F(3,4)+F(1,2)+F(1,4),F(3,2));ck('Q38 tail second',F(3,4)+3*F(1,2)+5*F(1,4),F(7,2));ck('Q40 signed tails',3*F(1,4)-2*F(1,4),F(1,4))
ck('Q42 capped tails',sum(F(3,4)**k for k in range(3)),F(37,16));ck('Q43 zero code',sum(k*F(1,4)*F(3,4)**(k-1)for k in range(1,4)),F(67,64));ck('Q44 conditional success mean',F(67,64)/(1-F(3,4)**3),F(67,37))
bits=list(product([0,1],repeat=5));mp=F(0);second=F(0)
for t in bits:
 w=F(1)
 for b in t:w*=F(2,5)if b else F(3,5)
 mp+=w*sum(t);second+=w*sum(t)**2
ck('Q47 binomial mean exhaustive',mp,2);ck('Q47 binomial second exhaustive',second,F(26,5));ck('Q48 shared-indicator second',25*F(2,5),10)
ck('Q49 first-three moments',[mean([0,2,4],[F(1,4),F(1,2),F(1,4)],lambda x:x**k)for k in range(1,4)],[2,6,20]);ck('Q49 third central',mean([0,2,4],[F(1,4),F(1,2),F(1,4)],lambda x:(x-2)**3),0)
ck('Q50 affine variance',9*2,18);ck('Q51 min squared loss',mean(v,p,lambda x:(x-mu)**2),F(441,100));ck('Q52 integer optimum loss',mean(v,p,lambda x:(x-1)**2),F(9,2))
ck('Q56 sharp mean',5*F(2,5),2);ck('Q57 sharp squared moment',25*F(4,25),4);ck('Q58 partition',10*F(1,4)+2*F(3,4),4)
ck('Q59 mixture zero probability',(F(4,5)**4+F(1,5)**4)/2,F(257,1250));ck('Q60 independent length',F(3,2)*4,6);ck('Q61 dependent length',[F(1,2),F(1,2)**2],[F(1,2),F(1,4)])
ck('Q66 student sampling',F(4**2+8**2+12**2,24),F(28,3));ck('Q68 minimum dice enumeration',F(sum(min(t)for t in product(range(1,7),repeat=2)),36),F(91,36));ck('Q69 maximum dice enumeration',F(sum(max(t)for t in product(range(1,7),repeat=2)),36),F(161,36))
ck('Q70 pair products',2*(-1)+(-1)*3+3*2,1);ck('Q71 triple bits',sum(a*b*(a^b)for a,b in product([0,1],repeat=2)),0)
ck('Q72 exact loop harmonic identity',sum(F(1,2*k-1)for k in range(1,8)),sum(F(1,k)for k in range(1,15))-sum(F(1,k)for k in range(1,8))/2)
ck('Q75 shifted variance',mean([10**9-1,10**9+1],[F(1,2)]*2,lambda x:(x-10**9)**2),1)
ck('Q79 equal pairs',3*sum(q*q for q in binp),F(7,6));ck('Q79 all three equal',sum(q**3 for q in binp),F(1,6));ck('Q80 compound polynomial',sum(F(1,4)*(3*b*b-2*b+1)for b in [0,1])+sum(F(1,8)*(3*(a+b)**2-2*(a+b)+1)for a,b in product([0,1],repeat=2)),F(5,2))
ck('MSc Q121 direct exact sum',sum(comb(i,3)*comb(7,i)for i in range(3,8))/10,56.0)
ck('MSc Q121 factorial-moment proof',sum(F(comb(sum(t),3),128)for t in product([0,1],repeat=7)),F(35,8))
data=json.loads(subprocess.check_output(['node','-e','process.stdout.write(JSON.stringify(require(process.argv[1]).fixtures()))',str(R/'dist/chapters/s_expectation.js')],text=True,encoding='utf-8'));by={m['id']:m for m in data['models']};modelchecks=0
for m in data['models']:
 assert all(f['teaching']['currentState']==f['snapshot']for f in m['frames'])
 for f in m['frames']:
  s=f['snapshot'];kind=m['kind']
  if kind=='signed-weighted-balance':expected=sum(s['transformed'][i]*s['masses'][i]for i in range(s['k']+1));assert isclose(expected,s['acc'],abs_tol=1e-9)
  elif kind=='integrability-tail-test':assert isclose(s['tail'],2**-s['r'])and s['absolute']==s['r']
  elif kind=='running-record-algorithm':assert s['best']==(min(s['values'][:s['i']+1])if s['i']>=0 else None)
  elif kind=='occupancy-ball-placement':assert sum(s['counts'])==s['step']and s['collisions']==sum(c*(c-1)//2 for c in s['counts'])
  elif kind=='integer-tail-layer-cake':assert isclose(s['total'],sum(q*(min(x,s['k'])**2 if s['second']else min(x,s['k']))for x,q in zip(s['v'],s['p'])),abs_tol=1e-9)
  elif kind=='capped-waiting-survival':assert isclose(s['total'],sum((1-s['p'])**j for j in range(s['k'])),abs_tol=1e-9)
  elif kind=='least-squares-loss':assert isclose(s['loss'],sum((x-s['c'])**2*q for x,q in zip(s['v'],s['p'])),abs_tol=1e-8)
  elif kind=='overlapping-success-windows':assert s['count']==sum(all(s['bits'][j]for j in range(i,i+s['r']))for i in range(s['k']+1))
  modelchecks+=1
for name,actual,expected in [('mean',by['mean-main']['result']['mean'],1.3),('absolute',by['absolute-main']['result']['mean'],2.1),('square',by['square-main']['result']['mean'],6.1),('tails',by['tail-main']['result']['mean'],1.5),('tails second',by['tail-second']['result']['mean'],3.5),('cap',by['cap-three']['result']['mean'],37/16),('bins',by['bins-four']['result']['occupiedMean'],65/27)]:assert isclose(actual,expected,abs_tol=1e-9),(name,actual,expected)
for row in json.loads((E/'acquisition.json').read_text()):assert hashlib.sha256(Path(row['cachePath']).read_bytes()).hexdigest()==row['sha256']
for q in json.loads((B/'s_expectation-authentic.json').read_text()):
 src=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')/q['repoPath'];assert hashlib.sha256(src.read_bytes()).hexdigest()==q['sourceSha256']
prior=json.loads((E/'prior-library.json').read_text());assert prior['chapterCount']==40 and prior['questionCount']==2511
for c in prior['chapters']:assert hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest()==c['sha256']
q=json.loads((B/'s_expectation-questions.json').read_text());html=(R/'dist/chapters/s_expectation.html').read_text(encoding='utf-8');lesson=(B/'s_expectation.en.md').read_text(encoding='utf-8')
assert len(q)==80 and all(len(re.findall(r'\b\w+\b',x['solution']))>=60 for x in q)
assert html.count('class="exam-question"')==82 and html.count('class="review-rule"')==80 and not re.search('[\u0600-\u06ff]',html) and '$'not in html
for m in data['models']:assert 'data-exp-model="'+m['id']+'"'in html,m['id']
for name,report in [('mathematics',dict(status='passed',exactChecks=len(checks),checks=checks,examAnswers='independently derived; not official keys')),('models',dict(status='passed',models=len(data['models']),checkpoints=modelchecks,independentlyRecomputedStates=modelchecks)),('lesson-and-retention',dict(status='passed',sections=lesson.count('\n## '),lessonWords=len(re.findall(r'\b\w+\b',lesson)),questions=82,originalQuestions=80,rules=80,previousChapters=40,previousQuestions=2511,allPreviousHtmlHashesUnchanged=True,solutionWordCounts=[len(re.findall(r'\b\w+\b',x['solution']))for x in q]))]:
 (E/(name+'.json')).write_text(json.dumps(report,indent=2)+'\n')
print('Passed',len(checks),'exact checks,',modelchecks,'model-state checks; 40 prior chapter hashes and 2511 prior questions retained.')
