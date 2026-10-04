"""Recompute serialized checkpoint claims independently of their constructors."""
import json,math,re,hashlib
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];data=json.loads((ROOT/'dist/chapters/concept-animations.json').read_text())['scenes'];audit=[]
def verify(label,ok):
 assert ok,label
 audit.append(label)
for id,s in data.items():
 verify(id+' multiple checkpoints',len(s['frames'])>=2)
 for i,f in enumerate(s['frames']):
  key=f'{id}/{i}';q=f.get('snapshot',{});verify(key+' unique entity keys',len({n['id'] for n in f['nodes']})==len(f['nodes']))
  verify(key+' structured formula',not f['formula'] or '<math' in f['formulaHtml'])
  verify(key+' pseudocode position',not s['code'] or 0<=f['line']<len(s['code']))
  verify(key+' resolvable edges',all(e['from'] in {n['id'] for n in f['nodes']} and e['to'] in {n['id'] for n in f['nodes']} for e in f['edges']))
  if id.startswith('insertion'):
   records=[tuple(x) for x in q['array'] if x is not None]+([tuple(q['saved'])] if q['saved'] else [])
   verify(key+' tagged record multiset',Counter(records)==Counter(map(tuple,q['input'])))
  if id=='merge':
   left,right,out=q['left'],q['right'],q['output'];verify(key+' multiset conservation',Counter(map(tuple,out+left[q['i']:]+right[q['j']:]))==Counter(map(tuple,left+right)));verify(key+' ordered output',all(out[k][1]<=out[k+1][1] for k in range(len(out)-1)))
  if id in ['lower-bound','search-stall']:
   a,t,lo,hi=q['array'],q['target'],q['lo'],q['hi'];verify(key+' safe boundaries',0<=lo<=hi<=len(a));verify(key+' outer classifications',all(x<t for x in a[:lo]) and all(x>=t for x in a[hi:]))
  if id=='euclid':verify(key+' original gcd',math.gcd(q['a'],q['b'])==math.gcd(q['A'],q['B']));verify(key+' exact coefficient certificates',q['a']==q['A']*q['x0']+q['B']*q['y0'] and q['b']==q['A']*q['x1']+q['B']*q['y1'])
  if id=='division':verify(key+' quotient remainder identity',q['X']==q['q']*q['Y']+q['r'] and q['r']>=0)
  if id in ['power','modular-power']:
   v=q['r']*q['b']**q['e'];target=q['x']**q['y'];verify(key+' accumulated power invariant',v==target if q['M'] is None else v%q['M']==target%q['M'])
  if id.startswith('set-'):
   U,A,B=set(q['U']),set(q['A']),set(q['B']);kind=id[4:];expected={x for x in q['inspected'] if {'union':x in A or x in B,'intersection':x in A and x in B,'difference':x in A and x not in B,'symmetric':(x in A)!=(x in B),'complement':x not in A,'set-demorgan':x not in A and x not in B}[kind]};verify(key+' independent membership predicate',set(q['result'])==expected)
  if id.startswith('induction-') and id!='induction-gap':verify(key+' constructive tile count',q['count']==q['n']*(q['n']+1)//2 if id.endswith('triangular') else q['count']==q['n']**2)
  if id=='strong-coins':verify(key+' coin witness',all(x in [3,5] for x in q['coins']) and sum(q['coins'])==q['n'])
  if id=='matrix-product':
   A=[[1,2],[3,4]];B=[[2,0],[1,2]];r,c,k=q['i'],q['j'],q['k'];verify(key+' current cell exact partial dot',q['C'][r][c]==sum(A[r][t]*B[t][c] for t in range(k+1)))
  if id=='row-elimination':
   from fractions import Fraction
   verify(key+' same explicit solution',all(Fraction(row[0])+2*Fraction(row[1])==Fraction(row[2]) for row in q['matrix']))
verify('stable insertion final order',data['insertion']['frames'][-1]['snapshot']['array']==sorted(data['insertion']['frames'][0]['snapshot']['input'],key=lambda r:r[1]))
verify('unstable insertion identified',data['insertion-unstable']['frames'][-1]['counterexample'])
verify('faulty interval repeats',data['search-stall']['frames'][-1]['snapshot']==data['search-stall']['frames'][-2]['snapshot'])
verify('faulty partition identified',data['partition-skip']['frames'][-1]['counterexample'])
verify('hazard exact low interval',[f['snapshot']['time'] for f in data['static-hazard']['frames'] if f['snapshot']['f']==0]==[2,3])
verify('consensus bridge remains high',all(f['metrics']['Output with consensus']==1 for f in data['hazard-consensus']['frames']))
verify('Gray all consecutive distances',[f['metrics']['Changed Gray bits'] for f in data['gray-code']['frames'][1:]]==[1]*7)
verify('single-error syndrome',data['hamming-code']['frames'][-1]['metrics']['Syndrome']==5)
verify('binary32 exact cases',[f['metrics']['Binary32 result'] for f in data['float-rounding']['frames']]==[16777216,16777216,16777218,16777220])
approved=json.loads((ROOT/'research/animation-approval.json').read_text())['approvedTopics']
verify('all approved-library questions retained',sum(len(re.findall(r'class="exam-question"',(ROOT/f'dist/chapters/{id}.html').read_text(encoding='utf-8'))) for id in approved)==1498)
result=dict(state='passed',assertions=len(audit),scenarioCount=len(data),checkpointCount=sum(len(s['frames']) for s in data.values()),checks=audit,limitations='Finite serialized checkpoint and selected reference-result checks. Construction assertions and browser layout checks are recorded separately. These are not universal proofs or physical-circuit validation.')
(ROOT/'research/animation-model-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(f'Passed {len(audit)} independent checkpoint and reference assertions.')
