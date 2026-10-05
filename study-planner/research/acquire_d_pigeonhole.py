from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,hashlib,json,tempfile
B=Path(__file__).resolve().parent
OUT=Path(tempfile.gettempdir())/'phd-pigeonhole-sources';OUT.mkdir(exist_ok=True)
specs=[('stanford','https://web.stanford.edu/class/archive/cs/cs103/cs103.1264/lectures/11/Lecture%20Slides.pdf'),('toronto','https://www.math.toronto.edu/balazse/2019_Summer_MAT344/Lec_7.pdf'),('mit18','https://ocw.mit.edu/courses/18-310-principles-of-discrete-applied-mathematics-fall-2013/ce68ab24d3cac4f2d808ced2705e6375_MIT18_310F13_Ch2.pdf')]
def fetch(row):
 key,url=row;p=OUT/(key+'.pdf')
 try:
  if not p.exists():
   r=requests.get(url,timeout=25);r.raise_for_status();assert r.content[:4]==b'%PDF';p.write_bytes(r.content)
  return dict(key=key,url=url,path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
 except Exception as e:return dict(key=key,url=url,accessError=type(e).__name__)
with ThreadPoolExecutor(max_workers=3) as pool:a=list(pool.map(fetch,specs))
a.append(dict(key='mit',url='https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf',path=str(Path(tempfile.gettempdir())/'phd-invariants-sources/mit.pdf')))
a[-1]['sha256']=hashlib.sha256(Path(a[-1]['path']).read_bytes()).hexdigest()
(B/'d_pigeonhole-downloads.json').write_text(json.dumps(a,indent=2)+'\n')
print(json.dumps(a))
