from pathlib import Path
import requests,json,hashlib,concurrent.futures
from pypdf import PdfReader
B=Path(__file__).resolve().parent;OUT=Path('C:/Users/bheydari/AppData/Local/Temp/a-stackqueue-sources');OUT.mkdir(exist_ok=True)
specs=[('cmu','https://www.cs.cmu.edu/~15122-archive/s26/handouts/lectures/09-stackqueue.pdf'),('stanford','https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1176/lectures/5-Stacks_Queues/5-Stacks_Queues.pdf'),('mit','https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/1ecbb4149fe5f5166033bdde285dba07_MIT6_006S20_prob1sol.pdf')]
def get(z):
 k,u=z
 try:
  r=requests.get(u,timeout=(5,20));r.raise_for_status();p=OUT/(k+'.pdf');p.write_bytes(r.content);pages=PdfReader(p).pages
  t='\n'.join('PAGE '+str(i+1)+'\n'+(a.extract_text() or '') for i,a in enumerate(pages));(OUT/(k+'-read.txt')).write_text(t,encoding='utf-8')
  return dict(key=k,url=u,path=str(p),sha256=hashlib.sha256(r.content).hexdigest(),pages=len(pages),state='downloaded_not_yet_read')
 except Exception as e:return dict(key=k,url=u,state='download_failed',reason=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:a=list(pool.map(get,specs))
(B/'a_stackqueue-downloads.json').write_text(json.dumps(a,indent=2)+'\n',encoding='utf-8');print(json.dumps(a,indent=2))
