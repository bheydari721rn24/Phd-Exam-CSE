from pathlib import Path
import requests,json,hashlib
from html.parser import HTMLParser
class Html(HTMLParser):
 def __init__(self,s):
  super().__init__();self.text=[];self.links=[];self.current=None;self.feed(s)
 def handle_starttag(self,tag,attrs):
  if tag=='a':self.current=dict(url=dict(attrs).get('href',''),text='')
 def handle_data(self,s):
  self.text.append(s)
  if self.current is not None:self.current['text']+=s
 def handle_endtag(self,tag):
  if tag=='a' and self.current is not None:self.links.append(self.current);self.current=None
from urllib.parse import urljoin
R=Path(__file__).resolve().parents[1]; O=Path('C:/Users/bheydari/AppData/Local/Temp/g-arithmetic-sources'); O.mkdir(exist_ok=True)
urls={
'mit8':'https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c8/c8s1/',
'mit4':'https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c4/c4s1/',
'stanford':'https://web.stanford.edu/class/archive/ee/ee108a/ee108a.1082/reader/ch1to12.pdf',
'stanford-calendar':'https://web.stanford.edu/class/archive/ee/ee108a/ee108a.1082/schedule.html',
'berkeley':'https://people.eecs.berkeley.edu/~randy/Courses/CS150.F00/',
'washington':'https://courses.cs.washington.edu/courses/cse370/08au/Lecture%20Slides/Lec14-Adders.pdf',
'cornell':'https://www.cs.cornell.edu/courses/cs3410/2017sp/schedule/slides/03-numbers-and-arithmetic.pdf',
'cmu':'https://users.ece.cmu.edu/~chraska/240home.html',
'eth':'https://safari.ethz.ch/digitaltechnik/spring2020/doku.php?id=schedule',
'imperial':'https://www.doc.ic.ac.uk/~sdemetri/co501_website_fall20/',
}
records=[]
for key,url in urls.items():
 try:
  r=requests.get(url,timeout=35);r.raise_for_status();pdf=r.content.startswith(b'%PDF');p=O/(key+('.pdf'if pdf else '.html'));p.write_bytes(r.content);rec=dict(id=key,url=url,status=r.status_code,path=str(p),sha256=hashlib.sha256(r.content).hexdigest())
  if pdf:
   import fitz
   doc=fitz.open(p);text='\n'.join('PDF PAGE '+str(i+1)+'\n'+pg.get_text()for i,pg in enumerate(doc));(O/(key+'.txt')).write_text(text,encoding='utf-8');rec.update(pages=len(doc),characters=len(text))
  else:
   soup=Html(r.text);(O/(key+'.txt')).write_text('\n'.join(t.strip()for t in soup.text if t.strip()),encoding='utf-8');rec['links']=[dict(text=a['text'].strip(),url=urljoin(url,a['url']))for a in soup.links if any(s in (a['text']+' '+a['url']).lower()for s in ['adder','arithmetic','.pdf','annotated','multipl','carry'])]
  records.append(rec)
 except Exception as ex:records.append(dict(id=key,url=url,error=str(ex)))
(R/'research/g_arithmetic-evidence/downloads.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
print(json.dumps(records,indent=2))
