import requests,json,hashlib,concurrent.futures,re
from pathlib import Path
from html.parser import HTMLParser
OUT=Path('C:/Users/bheydari/AppData/Local/Temp/a-arrays-sources');OUT.mkdir(exist_ok=True)
class Plain(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ['script','style','nav']:self.skip+=1
  if t in ['h1','h2','h3','h4','p','li','pre','tr']:self.parts.append('\n')
 def handle_endtag(self,t):
  if t in ['script','style','nav']:self.skip=max(0,self.skip-1)
 def handle_data(self,d):
  if not self.skip:self.parts.append(d)
specs=[('mit','https://live.ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/c08a3b63dfe5f6f6b32257d35f86ae63_MIT6_006S20_r02.pdf'),('berkeley-sl','https://cs61b-2.gitbook.io/cs61b-textbook/4.-sllists.md'),('berkeley-dl','https://cs61b-2.gitbook.io/cs61b-textbook/5.-dllists.md'),('berkeley-index','https://cs61b-2.gitbook.io/cs61b-textbook/llms.txt'),('cornell-array','https://www.cs.cornell.edu/courses/cs2110/2025fa/lectures/lec12/'),('cornell-list','https://www.cs.cornell.edu/courses/cs2110/2025fa/lectures/lec13/'),('oxford','https://www.robots.ox.ac.uk/~vedaldi/assets/teach/2024/b16/notes/3-elementary-data-structures.html'),('princeton','https://www.cs.princeton.edu/courses/archive/spring26/cos226/lectures/13StacksAndQueuesI.pdf'),('stanford','https://see.stanford.edu/materials/icspacs106b/H21-LinkedListCode.pdf'),('cmu','https://www.cs.cmu.edu/~15122/handouts/lectures/11-unbounded.pdf')]
def acquire(spec):
 key,u=spec
 try:
  r=requests.get(u,timeout=(5,20));r.raise_for_status();p=OUT/(key+('.pdf' if u.endswith('.pdf') else '.html' if not u.endswith(('.txt','.md')) else '.txt'));p.write_bytes(r.content)
  if u.endswith('.pdf'):
   from pypdf import PdfReader
   text='\n'.join('PAGE '+str(i+1)+'\n'+p.extract_text() for i,p in enumerate(PdfReader(p).pages))
  elif u.endswith(('.md','.txt')):text=r.text
  else:
   parser=Plain();parser.feed(r.text);text=''.join(parser.parts)
  text=re.sub(r'\n[ \t]*\n(?:[ \t]*\n)+','\n\n',text);(OUT/(key+'-read.txt')).write_text(text,encoding='utf-8')
  return dict(key=key,url=u,path=str(p),readingPath=str(OUT/(key+'-read.txt')),sha256=hashlib.sha256(r.content).hexdigest(),characters=len(text),state='downloaded_not_yet_reviewed')
 except Exception as e:return dict(key=key,url=u,state='inaccessible',error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(acquire,specs))
Path('research/a_arrays-downloads.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{k:v for k,v in r.items() if k not in ['sha256','error']} for r in rows],indent=2),flush=True)
