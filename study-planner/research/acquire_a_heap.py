"""Retrieve official written sources; acquisition and genuine reading are separate ledger states."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import requests,fitz,hashlib,json
B=Path(__file__).resolve().parent;C=Path('C:/Users/bheydari/AppData/Local/Temp/a-heap-sources');C.mkdir(exist_ok=True)
items=[('mit.pdf','https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/40d4851e550507ca14dc778b9b2266cc_MIT6_006S20_lec8.pdf'),('cmu25.pdf','https://www.cs.cmu.edu/~15122/handouts/lectures/25-pq.pdf'),('cmu26.pdf','https://www.cs.cmu.edu/~15122/handouts/lectures/26-resinvs.pdf'),('princeton.pdf','https://www.cs.princeton.edu/courses/archive/spring25/cos226/lectures/24PriorityQueues.pdf'),('princeton.html','https://algs4.cs.princeton.edu/24pq/'),('stanford.html','https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1206/lectures/heaps/'),('cambridge.html','https://www.cl.cam.ac.uk/teaching/2324/Algorithm1/materials.html'),('oxford.html','https://www.cs.ox.ac.uk/teaching/courses/2023-2024/algorithms/'),('eth.html','https://lec.inf.ethz.ch/DA/2020/'),('berkeley25.pdf','https://people.eecs.berkeley.edu/~jrs/61b/lec/25.pdf')]
class Text(HTMLParser):
 def __init__(self):super().__init__();self.out=[];self.depth=0
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.depth+=1
  if t in ['p','div','li','h1','h2','h3','pre','br']:self.out.append('\n')
 def handle_endtag(self,t):
  if t in ['script','style']:self.depth=max(0,self.depth-1)
 def handle_data(self,d):
  if not self.depth:self.out.append(d)
def fetch(item):
 name,url=item;p=C/name
 try:
  if not p.exists():r=requests.get(url,timeout=(15,45));r.raise_for_status();p.write_bytes(r.content)
  out=dict(file=name,url=url,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size,status='acquired_not_yet_read')
  if name.endswith('.pdf'):
   d=fitz.open(p);out['pages']=len(d);t='\n'.join('\n=== PDF page '+str(i+1)+' ===\n'+q.get_text()for i,q in enumerate(d))
  else:q=Text();q.feed(p.read_text(encoding='utf-8'));t=''.join(q.out)
  p.with_name(p.name+'.read.txt').write_text(t,encoding='utf-8');return out
 except Exception as e:return dict(file=name,url=url,status='unavailable',error=str(e))
with ThreadPoolExecutor(max_workers=4)as pool:results=list(pool.map(fetch,items))
(C/'acquisition.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
E=B/'a_heap-evidence';E.mkdir(exist_ok=True);(E/'acquisition.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{k:v for k,v in r.items()if k!='sha256'}for r in results],indent=2))
