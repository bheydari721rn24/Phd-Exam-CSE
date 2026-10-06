from pathlib import Path
import json
from a_sort_engine import trace,decorate
B=Path(__file__).parent;D=B.parent/'dist/chapters';models=[];groups={}
specs=[
('inversions','inversions',[5,2,4,2,1],'Strict inversion witnesses',{}),
('selection','selection',[2,2,1],'Selection swaps and equal identities',{}),
('insertion','insertion',[7,3,5,3,2],'Insertion: held record and moving hole',{}),
('bubble','bubble',[2,3,4,5,6,7,1],'Bubble: a small key moves left one pass at a time',{}),
('shell','shell',[2,2,1],'Shell gaps can cross equal identities',{'gaps':[2,1]}),
('merge','merge',[12,7,5,9,3,8,2,6],'Top-down merge: exact authentic input',{}),
('merge','merge',[1,2,1,2],'Stable merging of two runs',{'mergeOnly':True,'split':2}),
('quick','quick',[4,1,5,2,3],'Lomuto: classified prefix and final pivot',{}),
('quick','hoare',[4,1,3,2],'Hoare: split boundary and crossing scans',{'partitionOnly':True}),
('cmu','cmu',[1,3,5,7,6,4,2],'CMU middle-position pivot: a quadratic witness',{}),
('quick-worst','quick',[2,2,2,2,2,2,2,2],'Equal keys defeat strict Lomuto',{}),
('three','three',[3,1,3,5,2,3,4],'Dutch-national-flag regions',{}),
('heap','heap',[4,10,3,5,1],'Floyd construction and heap/suffix boundary',{}),
('counting','counting',[3,1,3,0,2,1],'Cumulative ends and stable record scatter',{'low':0,'K':4}),
('radix','radix',[329,457,657,839,436,720,355],'Stable LSD digit buckets',{'base':10,'low':0}),
('bucket','bucket',[19,18,17,16,15],'Bucket concentration and local insertion work',{'buckets':5})]
for i,(group,kind,values,title,p) in enumerate(specs,1):
 id='concept-'+str(i);m=decorate(trace(kind,dict(values=values,**p)),id,title,'Keys determine comparisons; letters preserve original identities. The caption gives the current algorithm-specific invariant. Counters exclude loop-bound tests; a nontrivial swap writes two array slots.'+(' Gray source records have been consumed; amber marks the next unconsumed head. The source runs are immutable copies, while Output grows.' if kind=='merge' else ''));models.append(m);groups.setdefault(group,[]).append(id)
# A decision tree is a different visual object from an array-state animation.
def decision():
 from html import escape
 nodes=[(430,65,'a < b?'),(230,170,'b < c?'),(630,170,'a < c?'),(125,275,'abc'),(335,275,'a < c?'),(525,275,'bac'),(735,275,'b < c?'),(270,380,'acb'),(400,380,'cab'),(670,380,'bca'),(800,380,'cba')]
 edges=[(0,1,'yes'),(0,2,'no'),(1,3,'yes'),(1,4,'no'),(2,5,'yes'),(2,6,'no'),(4,7,'yes'),(4,8,'no'),(6,9,'yes'),(6,10,'no')]
 frames=[]
 for upto in [0,2,6,10]:
  s=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" role="img" aria-label="Comparison decision tree for three distinct keys">']
  for a,b,label in edges:
   if b>upto:continue
   x,y,_=nodes[a];xx,yy,_=nodes[b];s.append(f'<path data-edge="" d="M {x} {y+25} L {xx} {yy-25}" stroke="#7b939f" fill="none"/><rect x="{(x+xx)/2+5}" y="{(y+yy)/2-15}" width="36" height="22" rx="4" fill="#f9fcfd"/><text class="sort-id" x="{(x+xx)/2+12}" y="{(y+yy)/2}">{label}</text>')
  for x,y,label in nodes[:upto+1]:s.append(f'<g><rect data-box="" x="{x-53}" y="{y-25}" width="106" height="50" rx="10" fill="#eff4f5" stroke="#9fb8bd"/><text data-contained="" class="sort-label" x="{x}" y="{y+6}" text-anchor="middle">{escape(label)}</text></g>')
  s.append('</svg>');frames.append(dict(svg=''.join(s),rows=[],metrics={},caption='Distinct keys a, b, c: every valid input ordering must reach its own leaf. The deepest paths need three comparisons.',formulaHtml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mo>⌈</mo><msub><mi>log</mi><mn>2</mn></msub><mo>(</mo><mn>3</mn><mo>!</mo><mo>)</mo><mo>⌉</mo><mo>=</mo><mn>3</mn></mrow></math>'))
 return dict(id='concept-17',kind='decision',title='Six orderings, six decision-tree leaves',invariant='Each path encodes comparison outcomes; leaf labels state the increasing key order. Equal keys are outside this distinct-key model.',params={},frames=frames,result=dict(leaves=6,maximumDepth=3))
models.append(decision());groups['lower-bound']=['concept-17']
pm=json.loads((B/'a_sort-problem-models.json').read_text());models+=pm
models.append(decorate(trace('hoare',dict(values=[4,1,3,2],partitionOnly=True)),'problem-42','Hoare partition returns a split, not a pivot','Exact question input. The final checkpoint remains partitioned rather than fully sorted; recursive calls have not been made.'))
qs=json.loads((B/'a_sort-questions.json').read_text());qs[41].update(modelId='problem-42',visualScope='Exact question input; only its first Hoare partition is executed.');(B/'a_sort-questions.json').write_text(json.dumps(qs,indent=2)+'\n')
auth=json.loads((B/'a_sort-authentic.json').read_text());auth[0].update(modelId='concept-6',visualScope='Exact original booklet input; every merge and comparison is included.');(B/'a_sort-authentic.json').write_text(json.dumps(auth,indent=2)+'\n')
assert len({m['id'] for m in models})==len(models)
(D/'a_sort-models.json').write_text(json.dumps(dict(models=models,groups=groups),indent=2)+'\n');print('models',len(models),'frames',sum(len(m['frames']) for m in models))
