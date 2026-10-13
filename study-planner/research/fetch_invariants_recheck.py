"""Acquire fresh written scopes without altering historical provenance."""
from pathlib import Path
import requests, hashlib, json, concurrent.futures, tempfile
import fitz
B=Path(__file__).parent; O=Path(tempfile.gettempdir())/'deep-invariants-recheck'; O.mkdir(exist_ok=True)
sources={
 'mit':('https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf',[(143,158),(176,185),(186,202)]),
 'stanford':('https://web.stanford.edu/class/archive/cs/cs161/cs161.1176/Sections/161-section-1.pdf',[(1,5)]),
 'cmu_structural':('https://www.cs.cmu.edu/~15150/resources/lectures/04/structural.pdf',[(1,7)]),
 'cmu_reverse':('https://www.cs.cmu.edu/~15150/resources/lectures/04/rev.pdf',[(1,2)]),
 'cambridge':('https://www.cl.cam.ac.uk/teaching/1314/FoundsCS/fcs-notes.pdf',[(16,37),(58,67)])}
def fetch(item):
 key,(url,scope)=item;p=O/(key+'.pdf')
 if not p.exists():
  r=requests.get(url,timeout=50);r.raise_for_status();assert r.content.startswith(b'%PDF');p.write_bytes(r.content)
 d=fitz.open(p); text='\n'.join('=== PHYSICAL PAGE '+str(i)+' ===\n'+d[i-1].get_text() for lo,hi in scope for i in range(lo,hi+1))
 (O/(key+'-scope.txt')).write_text(text,encoding='utf-8')
 return dict(id=key,url=url,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),physicalPages=scope,pageCount=len(d),characters=len(text),acquisitionState='downloaded_pending_actual_root_reading')
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
 for f in concurrent.futures.as_completed([pool.submit(fetch,x)for x in sources.items()]):
  try:row=f.result();rows.append(row);print(row,flush=True)
  except Exception as e:print(type(e).__name__,str(e),flush=True)
(B/'deep-library-revision/d_invariants-source-recheck-downloads.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
print('Acquisition is not instructional reading.',flush=True)
