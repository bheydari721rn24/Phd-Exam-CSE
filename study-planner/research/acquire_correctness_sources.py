"""Cache public references outside the Site, preserving exact URL and content hash."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,json,hashlib
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
CACHE=Path('C:/Users/bheydari/AppData/Local/Temp/phd-correctness-sources');CACHE.mkdir(exist_ok=True)
URLS={
 'cmu-contracts':'https://www.cs.cmu.edu/~wlovas/15122-r11/lectures/02-contracts.pdf',
 'cambridge-hoare':'https://www.cl.cam.ac.uk/archive/mjcg/Lectures/SpecVer1/Notes/Notes.pdf',
 'mit-mcs':'https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf',
 'stanford-cs161':'https://stanford-cs161.github.io/winter2022/assets/files/lecture2-notes.pdf',
 'cornell-invariants':'https://www.cs.cornell.edu/courses/cs2112/2018fa/lectures/',
 'eth-loops':'https://ethz.ch/content/dam/ethz/special-interest/infk/chair-program-method/pm/documents/Education/Courses/SS2026/PV/slides/04-loops-procedures.pdf',
 'oxford-imperative':'https://www.cs.ox.ac.uk/teaching/courses/2016-2017/imperativeprogramming1/',
 'berkeley-cs61b':'https://sp24.datastructur.es/'
}
def fetch(entry):
 name,url=entry;path=CACHE/(name+('.pdf' if url.endswith('.pdf') else '.html'))
 if not path.exists():
  r=requests.get(url,timeout=45);r.raise_for_status();path.write_bytes(r.content)
 record=dict(id=name,url=url,path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest())
 if path.suffix=='.pdf':
  reader=PdfReader(path);record['pages']=len(reader.pages)
  for i,p in enumerate(reader.pages):
   (CACHE/(name+'-'+str(i+1)+'.txt')).write_text(p.extract_text(),encoding='utf-8')
 return record
records=[]
with ThreadPoolExecutor(max_workers=4) as pool:
 futures={name:pool.submit(fetch,(name,url)) for name,url in URLS.items()}
 for name,future in futures.items():
  try:record=future.result()
  except Exception as exc:
   if name in ('cmu-contracts','cambridge-hoare','mit-mcs','stanford-cs161'):raise
   record=dict(id=name,url=URLS[name],accessError=str(exc),reviewLevel='unavailable_not_reviewed')
  records.append(record);print(name,record.get('pages',record.get('accessError','HTML')),flush=True)
(ROOT/'research/a_correct-source-downloads.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
