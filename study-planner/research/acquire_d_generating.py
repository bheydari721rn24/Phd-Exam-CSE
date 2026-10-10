from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,fitz,hashlib,json
T=Path('C:/Users/bheydari/AppData/Local/Temp/d-generating-sources');T.mkdir(exist_ok=True)
sources={'cmu':'https://www.andrew.cmu.edu/course/15-251/Notes/gen-functions.pdf','berkeley-ordinary':'https://math.berkeley.edu/~mhaiman/math172-spring10/ordinary.pdf','berkeley-exponential':'https://math.berkeley.edu/~mhaiman/math172-spring10/exponential.pdf','berkeley-partitions':'https://math.berkeley.edu/~mhaiman/math172-spring10/partitions.pdf','princeton-slides':'https://sedgewick.io/wp-content/uploads/2022/04/AA03-GFs.pdf'}
def get(item):
 name,url=item;p=T/(name+'.pdf')
 try:
  if not p.exists():
   r=requests.get(url,timeout=25);r.raise_for_status();assert r.content.startswith(b'%PDF');p.write_bytes(r.content)
  d=fitz.open(p);(T/(name+'.txt')).write_text('\n\n'.join(f'PAGE {i+1}\n'+x.get_text() for i,x in enumerate(d)),encoding='utf-8')
  return dict(name=name,url=url,pages=len(d),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
 except Exception as e:return dict(name=name,url=url,error=str(e)[:220])
with ThreadPoolExecutor(max_workers=5) as pool: result=list(pool.map(get,sources.items()))
d=fitz.open('C:/Users/bheydari/AppData/Local/Temp/phd-correctness-sources/mit-mcs.pdf');(T/'mit-chapter15.txt').write_text('\n\n'.join(f'PDF PAGE {i+1}\n'+d[i].get_text()for i in range(635,670)),encoding='utf-8')
(T/'acquisition.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result,indent=2))
