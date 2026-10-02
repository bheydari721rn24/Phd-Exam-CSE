"""Apply reviewed figure corrections without changing unreviewed text."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
changes=[]
for name in ('d_logic','d_proof','d_induction','a_model'):
 p=ROOT/'research'/f'{name}.en.md';s=p.read_text(encoding='utf-8')
 def split_path(m):
  tag=m[0]
  if 'marker-end' not in tag:return tag
  d=re.search(r'\bd="([^"]+)"',tag)
  if not d or d[1].count('M')<2:return tag
  assert not re.search(r'[m]',d[1]),'Relative subpath must not be rewritten automatically.'
  chunks=re.findall(r'M[^M]+',d[1]);changes.append({'topic':name,'subpaths':len(chunks)})
  return ''.join(tag[:d.start(1)]+chunk.strip()+tag[d.end(1):] for chunk in chunks)
 s=re.sub(r'<path\b[^>]*>',split_path,s)
 if name=='d_induction':
  old='<rect x="132" y="107" width="12" height="12" fill="#79a999"/>'
  assert old in s
  s=s.replace(old,'<rect x="132" y="119" width="12" height="12" fill="#79a999"/>')
  s=s.replace('A hypothesis for only a corner-missing board would be too weak: the original missing position and the three induced gaps need not be corners of their respective quadrants.', 'A hypothesis for only corner-missing boards would be too weak because the original missing cell can be an interior cell of its quadrant. The three induced gaps are center-adjacent corners of their respective quadrants; they are not the source of that failure. The universal missing-position hypothesis handles both kinds of subproblem.')
  s=s.replace('*Discrete Mathematics · Chapter 4 · English review draft · 24 fully worked problems*','*Discrete Mathematics · Chapter 4 · student-approved English edition · 24 fully worked problems*')
 p.write_text(s,encoding='utf-8')
print('Split independent arrow paths:',changes)
