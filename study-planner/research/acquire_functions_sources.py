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
CACHE=Path('C:/Users/bheydari/AppData/Local/Temp/phd-functions-sources');CACHE.mkdir(exist_ok=True)
docs=[
 ('cambridge','https://www.cl.cam.ac.uk/teaching/1718/ProgC/lectures/lecture2.pdf'),
 ('stanford','https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1164/handouts/1-PassbyReference.pdf'),
 ('cmu','https://www.cs.cmu.edu/~15122/handouts/lectures/01-contracts.pdf'),
 ('berkeley13','https://composingprograms.com/pages/13-defining-new-functions.html'),
 ('berkeley16','https://composingprograms.com/pages/16-higher-order-functions.html'),
 ('berkeley24','https://composingprograms.com/pages/24-mutable-data.html'),
 ('harvard1','https://cs50.harvard.edu/x/2025/notes/1/'),
 ('harvard4','https://cs50.harvard.edu/x/2025/notes/4/'),
 ('python','https://docs.python.org/3/tutorial/controlflow.html'),
 ('wg14','https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf'),
 ('mit','https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/6ba59859535f1566dd57a7279aeba5d1_MIT6_0001F16_Lec4.pdf')]
def get(d):
 name,url=d;path=CACHE/(name+('.pdf' if url.endswith('.pdf') else '.html'))
 if not path.exists():
  r=requests.get(url,timeout=60);r.raise_for_status();path.write_bytes(r.content)
 if path.suffix=='.pdf':
  p=PdfReader(path);t='\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+x.extract_text() for i,x in enumerate(p.pages));pages=len(p.pages)
 else:
  parser=TextParser();parser.feed(path.read_text(encoding='utf-8'));t='\n'.join(parser.lines);pages=None
 (CACHE/(name+'.txt')).write_text(t,encoding='utf-8')
 return dict(id=name,url=url,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),pages=pages)
with ThreadPoolExecutor(max_workers=6) as pool:records=list(pool.map(get,docs))
(CACHE/'acquisition.json').write_text(json.dumps(records,indent=2)+'\n')
print([(r['id'],r['pages']) for r in records])
