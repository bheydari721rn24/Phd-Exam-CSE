from pathlib import Path
import json,xml.etree.ElementTree as ET,subprocess
B=Path(__file__).parent;R=B.parent;data=json.loads((R/'dist/chapters/a_sort-models.json').read_text());checks=0;comparisons=0
for m in data['models']:
 if m['kind']=='decision':continue
 previous=None
 for f in m['frames']:
  t=f['teaching'];assert t['why'] and t['guide'];checks+=1
  if f.get('operation')=='compare':
   ET.fromstring(t['testHtml']);assert t['decision'] in ['True','False'];comparisons+=1
   if previous:
    assert f['rows']==previous['rows'],(m['id'],f['caption'],'comparison moved a record')
    assert f['metrics']['comparisons']==previous['metrics']['comparisons']+1,(m['id'],f['caption'],'comparison counter mismatch')
   checks+=2
  A=f['rows'][0]['cells'];p=f.get('pivotValue')
  if p is not None and m['kind'] in ['quick','three','cmu','hoare']:
   for region in t['regions']:
    a,b=region['lo'],region['hi'];label=region['label'];vals=[x['key'] for x in A[a:b]]
    test={'< pivot':lambda x:x<p,'= pivot':lambda x:x==p,'> pivot':lambda x:x>p,'≤ pivot':lambda x:x<=p,'≥ pivot':lambda x:x>=p}.get(label)
    if test:assert all(test(v) for v in vals),(m['id'],f['caption'],region,vals,p);checks+=1
  previous=f
# All original question prose and answers are retained exactly through the visual revision.
for name in ['a_sort-questions.json','a_sort-authentic.json']:
 current=json.loads((B/name).read_text());old=json.loads(subprocess.check_output(['git','show','a082004b3cce133d360c400d9b95746b211a36ba:research/'+name],cwd=R))
 assert current==old,name;checks+=1
report=dict(state='passed',checks=checks,separatedComparisonSteps=comparisons,modelCount=len(data['models']),storedCheckpoints=sum(len(m['frames']) for m in data['models']),questionProseAndAnswers='unchanged',scope='The declared colored interval predicates and no-movement comparison steps were checked at every recorded state. This supplements the algorithm proofs and output checks.')
(B/'a_sort-teaching-audit.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
