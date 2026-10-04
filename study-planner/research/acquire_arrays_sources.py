from pathlib import Path
import requests,json,hashlib
from concurrent.futures import ThreadPoolExecutor
from pypdf import PdfReader
from html.parser import HTMLParser
class TextParser(HTMLParser):
 def __init__(self):super().__init__();self.lines=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip=max(0,self.skip-1)
 def handle_data(self,d):
  if not self.skip and d.strip():self.lines.append(d.strip())
CACHE=Path('C:/Users/bheydari/AppData/Local/Temp/phd-arrays-sources');CACHE.mkdir(exist_ok=True)
docs=[
 ('cambridge3','https://www.cl.cam.ac.uk/teaching/1718/ProgC/lectures/lecture3.pdf'),
 ('cmu','https://www.cs.cmu.edu/~15122/handouts/lectures/03-arrays.pdf'),
 ('berkeley23','https://composingprograms.com/pages/23-sequences.html'),
 ('berkeley24','https://composingprograms.com/pages/24-mutable-data.html'),
 ('harvard','https://cs50.harvard.edu/x/2025/notes/2/'),
 ('stanford','https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1172/lectures/17-ImplementingVector/17-ImplementingVector.pdf'),
 ('mit','https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/1776670e271578eeb99fc25975f20586_MIT6_0001F16_Lec5.pdf'),
 ('python','https://docs.python.org/3/library/stdtypes.html')]
def get(d):
 name,url=d;path=CACHE/(name+('.pdf' if url.endswith('.pdf') else '.html'))
 if not path.exists():
  r=requests.get(url,params={'chapter':'arrays'},timeout=45);r.raise_for_status();path.write_bytes(r.content)
 if path.suffix=='.pdf':
  p=PdfReader(path);t='\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+x.extract_text() for i,x in enumerate(p.pages));pages=len(p.pages)
 else:
  parser=TextParser();parser.feed(path.read_text(encoding='utf-8'));t='\n'.join(parser.lines);pages=None
 (CACHE/(name+'.txt')).write_text(t,encoding='utf-8')
 return dict(id=name,url=url,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),pages=pages)
with ThreadPoolExecutor(max_workers=6) as pool:records=list(pool.map(get,docs))
(CACHE/'acquisition.json').write_text(json.dumps(records,indent=2)+'\n')
print([(r['id'],r['pages']) for r in records])
