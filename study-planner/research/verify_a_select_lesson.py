from pathlib import Path
import re,json,itertools,hashlib,math
B=Path(__file__).resolve().parent;R=B.parent
s=(B/'a_select.en.md').read_text(encoding='utf-8');ns={}
for code in re.findall(r'```python\n(.*?)```',s,re.S):exec(compile(code,'literal-lesson-code','exec'),ns)
checks={'literalSelectionQueries':0,'literalWeightedQueries':0,'randomPivotRankBounds':0,'finiteInductionSizes':0,'retainedChapters':0}
for n in range(1,7):
 for a in itertools.product(range(3),repeat=n):
  for k in range(1,n+1):
   expect=sorted(a)[k-1]
   assert ns['deterministic_select'](list(a),k)==expect
   assert ns['select_value'](list(a),k,lambda a,l,h:a[l+(h-l)//2])==expect
   checks['literalSelectionQueries']+=1
for n in range(1,5):
 for values in itertools.product(range(2),repeat=n):
  for weights in itertools.product(range(3),repeat=n):
   if not sum(weights):continue
   pairs=sorted(zip(values,weights));cum=0
   for v,w in pairs:
    cum+=w
    if 2*cum>=sum(weights):expect=v;break
   assert ns['lower_weighted_median'](pairs)==expect
   checks['literalWeightedQueries']+=1
assert ns['lower_weighted_median']([(0,10**100),(1,1)])==0
for n in range(8,10001):
 lo=(n+3)//4;hi=3*n//4+1
 assert 2*(hi-lo+1)>=n
 assert max(hi-1,n-lo)*8<=7*n
 checks['randomPivotRankBounds']+=1
for n in range(141,10001):
 a=(n+4)//5;b=7*n//10+6
 assert a<n and b<n and 20*(a+b)<=19*n
 checks['finiteInductionSizes']+=1
baseline=json.loads((B/'a_select-evidence/prior-library.json').read_text())
for c in baseline['chapters']:
 p=R/'dist/chapters'/f"{c['topicId']}.html";raw=p.read_bytes()
 assert hashlib.sha256(raw).hexdigest()==c['sha256']
 assert raw.decode().count('class="exam-question"')==c['questions']
 checks['retainedChapters']+=1
page=(R/'dist/chapters/a_select.html').read_text(encoding='utf-8')
assert not re.search('[\u0600-\u06ff]',page)
assert page.count('class="exam-question"')==89 and page.count('class="review-rule"')==80
assert '$' not in page and '\\frac' not in re.sub(r'<[^>]+>','',page)
checks.update(status='passed',retainedQuestions=baseline['questionCount'],mathElements=page.count('<math'),questionCount=89,ruleCount=80,lessonWords=len(s.split()))
(B/'a_select-evidence/lesson-and-retention.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
print(json.dumps(checks))
