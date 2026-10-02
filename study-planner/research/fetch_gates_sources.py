from pathlib import Path
import requests,json,hashlib,re
from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor
from pypdf import PdfReader
OUT=Path(r'C:/Users/bheydari/AppData/Local/Temp/g_gates_sources');OUT.mkdir(exist_ok=True)
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
 'mit-c3':'https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c3/c3s1/',
 'mit-c4':'https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c4/c4s1/',
 'cambridge-index':'https://www.cl.cam.ac.uk/teaching/2021/DigElec/materials.html',
 'stanford-reader':'https://web.stanford.edu/class/archive/ee/ee108a/ee108a.1082/reader/ch1to12.pdf',
 'berkeley-index':'https://notes.cs61c.org/content/sds-combinational-logic/',
 'cornell-logic':'https://www.cs.cornell.edu/courses/cs3410/2024fa/notes/logic.html',
 'cornell-switches':'https://www.cs.cornell.edu/courses/cs3410/2024fa/notes/switches.html',
 'ucsd-index':'https://cseweb.ucsd.edu/classes/sp22/cse140-a/syllabus.html',
 'cmu-intro':'https://course.ece.cmu.edu/~ece322/LECTURES/Lecture1/Lecture1.PDF',
 'eth-intro':'https://ethz.ch/content/dam/ethz/special-interest/infk/inst-infsec/system-security-group-dam/education/Digitaltechnik_17/onur-DigitalDesign-2017-lecture2-mysteries-afterlecture.pdf'
}
def get(item):
 name,url=item
 try:
  r=requests.get(url,timeout=35);r.raise_for_status();ext='pdf' if r.content.startswith(b'%PDF') else 'html';p=OUT/(name+'.'+ext);p.write_bytes(r.content)
  if ext=='pdf':
   pages=[page.extract_text() for page in PdfReader(p).pages];(OUT/(name+'.pages.json')).write_text(json.dumps(pages),encoding='utf-8');text='\n'.join(f'PDF PAGE {i+1}\n'+x for i,x in enumerate(pages))
  else:
   h=Text();h.feed(r.text);text=re.sub(r'\n\s*\n','\n',''.join(h.out));(OUT/(name+'.links.json')).write_text(json.dumps(h.links),encoding='utf-8')
  (OUT/(name+'.txt')).write_text(text,encoding='utf-8')
  return dict(id=name,url=url,status=r.status_code,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest(),characters=len(text),local=str(p))
 except Exception as e:return dict(id=name,url=url,error=str(e))
if __name__=='__main__':
 records=list(ThreadPoolExecutor(8).map(get,URLS.items()));(OUT/'manifest.json').write_text(json.dumps(records,indent=2),encoding='utf-8');print(json.dumps([{k:v for k,v in r.items() if k in ('id','characters','error')} for r in records],indent=2))
