"""Check exact mathematical data at every retained sets-animation checkpoint."""
from pathlib import Path
import ast,hashlib,itertools,json,re
B=Path(__file__).resolve().parent;R=B.parent;E=B/'deep-library-revision'
source=R/'dist/chapters/concept-animations.json';d=json.loads(source.read_text())['scenes'];checks=[]
def check(scene,index,got,want):
 assert got==want,(scene,index,got,want)
 checks.append(dict(scene=scene,checkpoint=index,passed=True))
for index,f in enumerate(d['powerset']['frames']):
 s=f['snapshot'];want=[i+1 for i in range(3)if s['mask']>>i&1]
 check('powerset',index,[s['subset'],f['metrics']['Subsets counted']],[want,index+1])
for index,f in enumerate(d['cartesian']['frames']):
 check('cartesian',index,[ast.literal_eval(f['metrics']['Pair']),f['metrics']['Pairs counted'],f['metrics']['Total pairs']],[list(itertools.product([1,2,3],[4,5]))[index],index+1,6])
for key in ['set-union','set-intersection','set-difference','set-symmetric','set-complement','set-set-demorgan']:
 for index,f in enumerate(d[key]['frames']):
  s=f['snapshot'];U,A,Bs=map(set,[s['U'],s['A'],s['B']]);seen=set(s['inspected'])
  expected={'set-union':A|Bs,'set-intersection':A&Bs,'set-difference':A-Bs,'set-symmetric':A^Bs,'set-complement':U-A,'set-set-demorgan':U-(A|Bs)}[key]&seen
  check(key,index,[set(s['result']),set(ast.literal_eval(f['metrics']['Result so far']))],[expected,expected])
for index,f in enumerate(d['image-collapse']['frames']):
 a=ast.literal_eval(f['metrics']['Selected subset']);got=ast.literal_eval(f['metrics']['Image set']);check('image-collapse',index,got,sorted({x%2 for x in a}))
(E/'d_sets-scene-semantics.json').write_text(json.dumps(dict(status='passed',checkpoints=len(checks),sourceSha256=hashlib.sha256(source.read_bytes()).hexdigest(),scope='All nine fixed animation scenarios and their 66 stored exact checkpoints; not an arbitrary-input simulation theorem.',checks=checks),indent=2)+'\n')
print(json.dumps(dict(status='passed',checkpoints=len(checks))))
