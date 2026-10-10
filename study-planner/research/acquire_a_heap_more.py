from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,fitz,hashlib,json
from html.parser import HTMLParser
class Text(HTMLParser):
 def __init__(self):super().__init__();self.out=[];self.hidden=0
 def handle_starttag(self,t,a):
  if t in ('script','style'):self.hidden+=1
 def handle_endtag(self,t):
  if t in ('script','style'):self.hidden=max(0,self.hidden-1)
  if t in ('p','div','li','h1','h2','h3','pre'):self.out.append('\n')
 def handle_data(self,d):
  if not self.hidden:self.out.append(d)
B=Path(__file__).resolve().parent;C=Path('C:/Users/bheydari/AppData/Local/Temp/a-heap-sources')
items=[('cmu25.pdf','https://cs.cmu.edu/~15122/handouts/lectures/25-pq.pdf'),('cmu26.pdf','https://cs.cmu.edu/~15122/handouts/lectures/26-resinvs.pdf'),('princeton.pdf','https://www.cs.princeton.edu/courses/archive/spring25/cos226/lectures/24PriorityQueues.pdf'),('princeton.html','https://algs4.cs.princeton.edu/24pq/'),('cambridge2.pdf','https://www.cl.cam.ac.uk/teaching/2324/Algorithm1/content/algorithms2.pdf'),('cambridge6.pdf','https://www.cl.cam.ac.uk/teaching/2324/Algorithm1/ex/ex6.pdf')]
def f(it):
 name,url=it;p=C/name
 try:
  if not p.exists():r=requests.get(url,timeout=(8,25));r.raise_for_status();p.write_bytes(r.content)
  z=dict(file=name,url=url,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size,status='acquired_not_yet_read')
  if name.endswith('.pdf'):
   d=fitz.open(p);z['pages']=len(d);t='\n'.join('\n=== PDF page '+str(i+1)+' ===\n'+q.get_text()for i,q in enumerate(d))
  else:q=Text();q.feed(p.read_text(encoding='utf-8'));t=''.join(q.out)
  p.with_name(p.name+'.read.txt').write_text(t,encoding='utf-8');return z
 except Exception as e:return dict(file=name,url=url,status='unavailable',error=str(e))
with ThreadPoolExecutor(max_workers=4)as pool:a=list(pool.map(f,items))
(B/'a_heap-evidence/acquisition-more.json').write_text(json.dumps(a,indent=2)+'\n',encoding='utf-8');print(json.dumps(a,indent=2))
