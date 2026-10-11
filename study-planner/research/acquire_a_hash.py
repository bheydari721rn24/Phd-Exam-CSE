from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import requests,fitz,hashlib,json
B=Path(__file__).resolve().parent;C=Path('C:/Users/bheydari/AppData/Local/Temp/a-hash-sources');C.mkdir(exist_ok=True)
items=[('mit.pdf','https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/ce9e94705b914598ce78a00a70a1f734_MIT6_006S20_lec4.pdf'),('cmu.pdf','https://www.cs.cmu.edu/~15122/handouts/lectures/12-hashing.pdf'),('princeton.pdf','https://www.cs.princeton.edu/courses/archive/spring25/cos226/lectures/34HashTables.pdf'),('princeton.html','https://algs4.cs.princeton.edu/34hash/'),('stanford.html','https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1258/lectures/24-hashing/'),('berkeley.html','https://people.eecs.berkeley.edu/~jrs/61b/'),('berkeley-advanced.pdf','https://people.eecs.berkeley.edu/~daw/teaching/cs170-s03/Notes/lecture9.pdf'),('eth.html','https://lec.inf.ethz.ch/DA/2020/'),('cambridge.html','https://www.cl.cam.ac.uk/teaching/2324/Algorithm1/materials.html'),('oxford.html','https://www.cs.ox.ac.uk/teaching/courses/2017-2018/cads/')]
class Text(HTMLParser):
 def __init__(self):super().__init__();self.out=[];self.depth=0;self.links=[]
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.depth+=1
  if t in ['p','div','li','h1','h2','h3','h4','pre','br','tr']:self.out.append('\n')
  if t=='a':self.links.extend(v for k,v in a if k=='href')
 def handle_endtag(self,t):
  if t in ['script','style']:self.depth=max(0,self.depth-1)
 def handle_data(self,d):
  if not self.depth:self.out.append(d)
def fetch(item):
 name,url=item;p=C/name
 try:
  if not p.exists():r=requests.get(url,timeout=(12,35));r.raise_for_status();p.write_bytes(r.content)
  out=dict(file=name,url=url,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size,status='acquired_not_yet_read')
  if name.endswith('.pdf'):
   d=fitz.open(p);out['pages']=len(d);t='\n'.join('\n=== PDF page '+str(i+1)+' ===\n'+q.get_text()for i,q in enumerate(d))
  else:q=Text();q.feed(p.read_text(encoding='utf-8'));t=''.join(q.out);out['links']=q.links
  p.with_name(p.name+'.read.txt').write_text(t,encoding='utf-8');return out
 except Exception as e:return dict(file=name,url=url,status='unavailable',error=str(e))
if __name__=='__main__':
 with ThreadPoolExecutor(max_workers=5)as pool:out=list(pool.map(fetch,items))
 (B/'a_hash-evidence/acquisition.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 for q in out:print(q['file'],q['status'],q.get('pages',''),q.get('error',''))
