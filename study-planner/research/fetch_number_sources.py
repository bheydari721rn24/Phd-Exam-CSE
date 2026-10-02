from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import urllib.request,json,hashlib,sys
sys.path.insert(0,r'C:\Users\bheydari\AppData\Local\Temp\phd-study-pydeps')
from pypdf import PdfReader
OUT=Path(r'C:\Users\bheydari\AppData\Local\Temp\g_number_sources');OUT.mkdir(exist_ok=True)
URLS={
'mit':'https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c1/c1s1/',
'mitworksheet':'https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c1/c1s3/',
'berkeleyradix':'https://notes.cs61c.org/content/number-rep/binary-decimal-hex/',
'berkeleyinteger':'https://notes.cs61c.org/content/number-rep/integer-representations/',
'cornellnumber':'https://www.cs.cornell.edu/courses/cs3410/2024fa/notes/numbers.html',
'cornellfloat':'https://www.cs.cornell.edu/courses/cs3410/2024fa/notes/float.html',
'princeton':'https://algs4.cs.princeton.edu/lectures/keynote/67CombinatorialSearch.pdf',
'cambridge':'https://www.cl.cam.ac.uk/teaching/2021/DigElec/materials.html',
'cmu':'https://www.cs.cmu.edu/afs/cs/academic/class/15213-s25/www/lectures/02-bits-bytes-ints.pdf',
'eth':'https://iis-students.ee.ethz.ch/lectures/digital-circuits/'}
class Text(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ('script','style'):self.skip+=1
  if t in ('p','h1','h2','h3','li','div'):self.parts.append('\n')
 def handle_endtag(self,t):
  if t in ('script','style'):self.skip-=1
 def handle_data(self,d):
  if not self.skip:self.parts.append(d)
def fetch(pair):
 name,url=pair
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(req,timeout=35) as r:data=r.read()
  suffix='.pdf' if data.startswith(b'%PDF') else '.html';p=OUT/(name+suffix);p.write_bytes(data)
  if suffix=='.pdf':
   pages=[x.extract_text() for x in PdfReader(p).pages];text='\n\n'.join(f'PAGE {i+1}\n{x}' for i,x in enumerate(pages));(OUT/(name+'.pages.json')).write_text(json.dumps(pages),encoding='utf-8')
  else:
   parser=Text();parser.feed(data.decode('utf-8'));text=''.join(parser.parts)
  (OUT/(name+'.txt')).write_text(text,encoding='utf-8')
  return dict(name=name,url=url,status='fetched',sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),textChars=len(text))
 except Exception as e:return dict(name=name,url=url,status='unavailable',error=str(e))
records=list(ThreadPoolExecutor(max_workers=6).map(fetch,URLS.items()))
(OUT/'manifest.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print(json.dumps(records,indent=2))
