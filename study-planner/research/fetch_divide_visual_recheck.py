from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests, fitz, tempfile, json, hashlib
B=Path(__file__).parent; E=B/'deep-library-revision'; O=Path(tempfile.gettempdir())/'deep-divide-recheck'; O.mkdir(exist_ok=True)
refs={
 'berkeley':('https://people.eecs.berkeley.edu/~vazirani/algorithms/chap2.pdf',[0,1,13,14,15,16,17,18,26,30]),
 'cmu':('https://www.cs.cmu.edu/~15451-s21/lectures/lec21-closest-pair.pdf',[1,2,5]),
 'eth':('https://lec.inf.ethz.ch/DA/2018/slides/daLecture2.en.handout.2x2.pdf',[7,8,9,10])}
def fetch(item):
 key,(url,pages)=item; p=O/(key+'.pdf')
 try:
  if not p.exists():
   r=requests.get(url,timeout=35);r.raise_for_status();assert r.content.startswith(b'%PDF');p.write_bytes(r.content)
  d=fitz.open(p); out=[]
  for i in pages:
   if i<len(d):
    dest=O/(key+'-page-'+str(i+1)+'.png');d[i].get_pixmap(matrix=fitz.Matrix(1.7,1.7)).save(dest);out.append(str(dest))
  return dict(id=key,url=url,pages=len(d),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),rendered=out,visualInspection='pending actual viewing')
 except Exception as e:return dict(id=key,url=url,error=str(e),visualInspection='not inspected')
with ThreadPoolExecutor(max_workers=3)as ex:rows=list(ex.map(fetch,refs.items()))
(E/'a_divide-source-visual-downloads.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print(json.dumps(r))
