from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,fitz,json,tempfile,hashlib
B=Path(__file__).parent;O=Path(tempfile.gettempdir())/'deep-correctness-recheck';O.mkdir(exist_ok=True)
urls={
 'cmu':'https://www.cs.cmu.edu/~wlovas/15122-r11/lectures/02-contracts.pdf',
 'cambridge':'https://www.cl.cam.ac.uk/archive/mjcg/Lectures/SpecVer1/Notes/Notes.pdf',
 'mit':'https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf',
 'stanford':'https://stanford-cs161.github.io/winter2022/assets/files/lecture2-notes.pdf'}
def get(item):
 k,url=item;p=O/(k+'.pdf')
 try:
  if k=='mit'and not p.exists():
   cache=Path(tempfile.gettempdir())/'phd-correctness-sources/mit-mcs.pdf'
   if cache.exists():p.write_bytes(cache.read_bytes())
  if not p.exists():
   r=requests.get(url,timeout=35);r.raise_for_status();assert r.content.startswith(b'%PDF');p.write_bytes(r.content)
  d=fitz.open(p);scope=list(range(24))if k=='cmu'else list(range(10,28))+list(range(46,59))+list(range(62,72))if k=='cambridge'else list(range(139,152))if k=='mit'else list(range(4))
  out=[]
  for i in scope:
   q=O/(k+'-page-'+str(i+1)+'.txt');q.write_text(d[i].get_text(),encoding='utf8');out.append(str(q))
  return dict(university=k,url=url,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),pages=len(d),selectedPhysicalPages=[i+1 for i in scope],extracted=out,readingStatus='acquired_not_yet_read_in_this_revision')
 except Exception as e:return dict(university=k,url=url,error=str(e),readingStatus='not_read')
with ThreadPoolExecutor(max_workers=4)as pool:rows=list(pool.map(get,urls.items()))
(B/'deep-library-revision/a_correct-source-recheck-downloads.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print({k:v for k,v in r.items()if k!='extracted'})
