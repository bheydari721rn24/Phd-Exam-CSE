"""Download reference PDFs outside the site; record provenance, never publish copies."""
import concurrent.futures, hashlib, json, tempfile
from pathlib import Path
import requests
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
OUT=Path(tempfile.gettempdir())/'phd-functions-sources'; OUT.mkdir(exist_ok=True)
SOURCES={
 'mit':'https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/efac321fdc8d0b27586ca35b04aab808_MIT6_042JF10_chap07.pdf',
 'stanford':'https://web.stanford.edu/class/archive/cs/cs103/cs103.1176/lectures/08/Small08.pdf',
 'stanford_ps3':'https://web.stanford.edu/class/archive/cs/cs103/cs103.1176/handouts/150%20Problem%20Set%203.pdf',
 'cambridge':'https://www.cl.cam.ac.uk/teaching/2003/DiscMaths/DiscMaths.pdf',
 'oxford':'https://www.cs.ox.ac.uk/andrew.ker/docs/discretemaths-lecture-notes-mt2010.pdf',
 'cmu_assignment':'https://www.math.cmu.edu/~sallison/concepts18/assignment5.pdf'}

def fetch(item):
 key,url=item
 r=requests.get(url,timeout=50);r.raise_for_status();assert r.content[:4]==b'%PDF'
 file=OUT/f'{key}.pdf';file.write_bytes(r.content)
 pages=PdfReader(file).pages
 text='\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+(p.extract_text() or '') for i,p in enumerate(pages))
 (OUT/f'{key}.txt').write_text(text,encoding='utf-8')
 return {'id':key,'url':url,'sha256':hashlib.sha256(r.content).hexdigest(),'pages':len(pages),'localReference':str(file),'textCharacters':len(text)}
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
 for future in concurrent.futures.as_completed([pool.submit(fetch,x) for x in SOURCES.items()]):
  try: row=future.result();rows.append(row);print(row['id'],row['pages'],row['textCharacters'],flush=True)
  except Exception as exc: print(type(exc).__name__,str(exc),flush=True)
(ROOT/'research/d_functions-source-downloads.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print('Reference directory:',OUT)
