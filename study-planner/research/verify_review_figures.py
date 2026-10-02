"""Meaningful regressions for newly discovered diagram/content errors."""
from pathlib import Path
import re,json
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[1]
class Shapes(HTMLParser):
 def __init__(self):super().__init__();self.shapes=[]
 def handle_starttag(self,t,a):
  if t in {'rect','circle','path'}:self.shapes.append((t,dict(a)))
source=(ROOT/'research/d_induction.en.md').read_text(encoding='utf-8')
p=Shapes();p.feed(source)
green=[a for t,a in p.shapes if t=='rect' and a.get('fill')=='#79a999']
centers=[(float(a['x'])+float(a['width'])/2,float(a['y'])+float(a['height'])/2) for a in green]
quadrants=[(x>=144,y>=119) for x,y in centers]
assert len(quadrants)==3 and len(set(quadrants))==3
assert set(quadrants)=={(True,False),(False,True),(True,True)},quadrants
assert 'The three induced gaps are center-adjacent corners' in source
source=(ROOT/'research/g_gates.en.md').read_text(encoding='utf-8');first=source[source.index('<figure'):source.index('</figure>')]
p=Shapes();p.feed(first);bubbles=[a for t,a in p.shapes if t=='circle']
assert {(a['cx'],a['cy']) for a in bubbles}=={('650','70'),('140','215'),('650','215')},bubbles
assert 'M390 215H420' in first
for p in (ROOT/'research').glob('*.en.md'):
 for t in re.findall(r'<path[^>]*>',p.read_text(encoding='utf-8')):
  if 'marker-end' in t:
   d=re.search(r'\bd="([^"]+)"',t)
   assert not d or d[1].count('M')<=1,(p.name,t)
s=(ROOT/'research/s_counting.en.md').read_text(encoding='utf-8');assert '⟦1,1⟧: mass 1/9' in s and 'ordinary set {1,1} equals {1}' in s
s=(ROOT/'research/d_logic.en.md').read_text(encoding='utf-8');assert 'both occurrences of y are free' not in s
s=(ROOT/'research/d_proof.en.md').read_text(encoding='utf-8');assert 'must use **both**' not in s and 'not circular merely' in s
print('Reviewed diagram topology, polarity, independent arrowheads, multiplicity, and proof wording passed.')
