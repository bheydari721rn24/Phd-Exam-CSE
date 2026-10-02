"""Download primary written references without modifying synced project sources."""
from pathlib import Path
import hashlib,json,tempfile
from concurrent.futures import ThreadPoolExecutor
import requests
from pypdf import PdfReader
R=Path(__file__).resolve().parent;OUT=Path(tempfile.gettempdir())/'phd-divide-sources';OUT.mkdir(exist_ok=True)
refs={
 'mit':'https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/1869dbf640ded6b31f1bd369d2001ef5_MIT6_006S20_r03.pdf',
 'stanford':'https://theory.stanford.edu/~valiant/cs161/CS161Lecture02.pdf',
 'berkeley':'https://people.eecs.berkeley.edu/~vazirani/algorithms/chap2.pdf',
 'cmu':'https://www.cs.cmu.edu/~15451-s21/lectures/lec21-closest-pair.pdf',
 'princeton':'https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/05DivideAndConquerII.pdf',
 'oxford':'https://www.cs.ox.ac.uk/files/13284/divide-and-conquer.pdf',
 'eth':'https://lec.inf.ethz.ch/DA/2018/slides/daLecture2.en.handout.2x2.pdf'}
def get(item):
 key,url=item;p=OUT/(key+'.pdf')
 if not p.exists():
  r=requests.get(url,timeout=40);r.raise_for_status()
  assert r.content.startswith(b'%PDF'),key
  p.write_bytes(r.content)
 return dict(id=key,url=url,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),pages=len(PdfReader(p).pages),localReference=str(p))
with ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(get,refs.items()))
(R/'a_divide-source-downloads.json').write_text(json.dumps(rows,indent=2)+'\n')
for row in rows:print(row['id'],row['pages'],'pages',row['sha256'][:12])
