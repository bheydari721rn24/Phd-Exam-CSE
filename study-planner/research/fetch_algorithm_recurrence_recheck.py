from pathlib import Path
import concurrent.futures,hashlib,json,tempfile
import requests,fitz
from html.parser import HTMLParser
class Extract(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.skip=0
 def handle_starttag(self,tag,attrs):
  if tag in ['script','style','nav']:self.skip+=1
  elif tag in ['p','h1','h2','h3','li','br','tr']:self.parts.append('\n')
 def handle_endtag(self,tag):
  if tag in ['script','style','nav']:self.skip=max(0,self.skip-1)
 def handle_data(self,data):
  if not self.skip:self.parts.append(data)
B=Path(__file__).parent;O=Path(tempfile.gettempdir())/'deep-algorithm-recurrence-recheck';O.mkdir(exist_ok=True)
items=[('mit','https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/1869dbf640ded6b31f1bd369d2001ef5_MIT6_006S20_r03.pdf',[(1,7)]),('stanford','https://stanford-cs161.github.io/winter2025/assets/files/lecture3-notes.pdf',[(1,6)]),('cmu','https://www.cs.cmu.edu/afs/cs/academic/class/15451-f11/www/lectures/lects1-10.pdf',[(10,15),(24,26)]),('mit-ab','https://courses.csail.mit.edu/6.046/spring04/handouts/akrabazzi.pdf',[(1,5)]),('princeton','https://aofa.cs.princeton.edu/20recurrence/',[]),('cornell','https://www.cs.cornell.edu/courses/cs3110/2009sp/lectures/lec20.html',[]),('cornell-sub','https://www.cs.cornell.edu/courses/cs3110/2011sp/Recitations/rec19.htm',[])]
def fetch(item):
 key,url,scope=item
 try:
  response=requests.get(url,timeout=35);response.raise_for_status();ext='.pdf'if url.endswith('.pdf')else'.html';p=O/(key+ext);p.write_bytes(response.content)
  if ext=='.pdf':
   doc=fitz.open(p);text='\n'.join('PHYSICAL PAGE '+str(i)+'\n'+doc[i-1].get_text()for a,b in scope for i in range(a,b+1));pages=len(doc)
  else:
   parser=Extract();parser.feed(response.text);text=''.join(parser.parts);pages=None
  (O/(key+'-scope.txt')).write_text(text,encoding='utf-8');return dict(id=key,url=url,sha256=hashlib.sha256(response.content).hexdigest(),pages=pages,physicalPages=scope,characters=len(text),state='downloaded_pending_actual_scoped_reading')
 except Exception as e:return dict(id=key,url=url,state='failed_local_fetch',error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=4)as pool:rows=list(pool.map(fetch,items))
(B/'deep-library-revision/a_recurrence-source-recheck-downloads.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8');print([{k:v for k,v in r.items()if k!='error'}for r in rows])
