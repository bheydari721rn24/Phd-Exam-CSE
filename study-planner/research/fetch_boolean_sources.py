from pathlib import Path
import requests,json,hashlib,re
from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor
from pypdf import PdfReader
OUT=Path(r'C:/Users/bheydari/AppData/Local/Temp/g_boolean_sources');OUT.mkdir(exist_ok=True)
class Text(HTMLParser):
 def __init__(self):super().__init__();self.out=[];self.links=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ('script','style'):self.skip+=1
  if t in ('p','div','li','h1','h2','h3','h4','tr','br'):self.out.append('\n')
  if t=='a':self.links.append(dict(a).get('href',''))
 def handle_endtag(self,t):
  if t in ('script','style'):self.skip-=1
 def handle_data(self,s):
  if not self.skip:self.out.append(s)
URLS={
 'mit':'https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c4/c4s1/',
 'mit-worksheet':'https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c4/c4s3/',
 'cambridge-index':'https://www.cl.cam.ac.uk/teaching/2021/DigElec/materials.html',
 'ucsd-index':'https://cseweb.ucsd.edu/classes/sp22/cse140-a/syllabus.html',
 'cmu':'https://course.ece.cmu.edu/~ee760/760docs/lec01.pdf',
 'cmu-hw':'https://course.ece.cmu.edu/~ee760/760docs/hw1v1.pdf',
 'berkeley':'https://notes.cs61c.org/content/combinational-logic/',
 'cornell-index':'https://www.cs.cornell.edu/courses/cs3410/2024fa/course/schedule.html',
 'stanford-index':'https://web.stanford.edu/class/archive/ee/ee108a/ee108a.1082/schedule.html',
 'eth-index':'https://www.vvz.ethz.ch/Vorlesungsverzeichnis/lerneinheit.view?ansicht=KATALOGDATEN&lang=en&lerneinheitId=199628&semkez=2026S'
}
def get(item):
 name,url=item
 try:
  r=requests.get(url,timeout=45);r.raise_for_status();ext='pdf' if r.content.startswith(b'%PDF') else 'html';p=OUT/(name+'.'+ext);p.write_bytes(r.content)
  if ext=='pdf':
   pages=[p.extract_text() for p in PdfReader(p).pages];(OUT/(name+'.pages.json')).write_text(json.dumps(pages),encoding='utf-8');text='\n'.join(f'PDF PAGE {i+1}\n'+x for i,x in enumerate(pages))
  else:
   h=Text();h.feed(r.text);text=re.sub(r'\n\s*\n','\n',''.join(h.out));(OUT/(name+'.links.json')).write_text(json.dumps(h.links),encoding='utf-8')
  (OUT/(name+'.txt')).write_text(text,encoding='utf-8')
  return dict(id=name,url=url,status=r.status_code,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest(),characters=len(text),local=str(p))
 except Exception as e:return dict(id=name,url=url,error=str(e))
if __name__=='__main__':
 records=list(ThreadPoolExecutor(8).map(get,URLS.items()));(OUT/'manifest.json').write_text(json.dumps(records,indent=2),encoding='utf-8');print(json.dumps(records,indent=2))
