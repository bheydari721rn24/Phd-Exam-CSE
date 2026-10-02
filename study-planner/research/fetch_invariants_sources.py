"""Fetch written references outside the publication and record exact provenance."""
import concurrent.futures, hashlib, json, tempfile
from pathlib import Path
import requests
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
OUT=Path(tempfile.gettempdir())/'phd-invariants-sources';OUT.mkdir(exist_ok=True)
SOURCES={
 'mit':'https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf',
 'stanford':'https://web.stanford.edu/class/archive/cs/cs161/cs161.1176/Sections/161-section-1.pdf',
 'cmu_structural':'https://www.cs.cmu.edu/~15150/resources/lectures/04/structural.pdf',
 'cmu_reverse':'https://www.cs.cmu.edu/~15150/resources/lectures/04/rev.pdf',
 'cmu_code':'https://www.cs.cmu.edu/~15150/resources/lectures/04/code04.sml',
 'cambridge':'https://www.cl.cam.ac.uk/teaching/1314/FoundsCS/fcs-notes.pdf',
 'cornell':'https://www.cs.cornell.edu/courses/cs2800/2017sp/lectures/lec21-structural.html',
 'berkeley':'https://www.eecs70.org/assets/pdf/notes/n4.pdf',
 'princeton':'https://www.cs.princeton.edu/courses/archive/spring21/cos226/lectures/22Mergesort.pdf',
 'oxford':'https://www.cs.ox.ac.uk/teaching/courses/2016-2017/imperativeprogramming1/'
}
def fetch(item):
 key,url=item;r=requests.get(url,timeout=55);r.raise_for_status()
 pdf=r.content.startswith(b'%PDF');p=OUT/(key+('.pdf' if pdf else '.html' if '<html' in r.text.lower() else '.txt'));p.write_bytes(r.content)
 if pdf:
  pages=PdfReader(p).pages;text='\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+(pg.extract_text() or '') for i,pg in enumerate(pages));(OUT/f'{key}.txt').write_text(text,encoding='utf-8')
 else:text=r.text;pages=[]
 return {'id':key,'url':url,'sha256':hashlib.sha256(r.content).hexdigest(),'pages':len(pages),'localReference':str(p),'textCharacters':len(text)}
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
 for fut in concurrent.futures.as_completed([pool.submit(fetch,x) for x in SOURCES.items()]):
  try:row=fut.result();rows.append(row);print(row['id'],row['pages'],row['textCharacters'],flush=True)
  except Exception as e:print(type(e).__name__,str(e),flush=True)
(ROOT/'research/d_invariants-source-downloads.json').write_text(json.dumps(rows,indent=2)+'\n')
print('Reference directory:',OUT)
