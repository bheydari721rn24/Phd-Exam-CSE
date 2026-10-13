"""Cache bounded written source scopes; downloading does not mark them read."""
from pathlib import Path
import json,hashlib,tempfile,concurrent.futures
import requests
from pypdf import PdfReader
B=Path(__file__).parent; E=B/'deep-library-revision'; out=Path(tempfile.gettempdir())/'deep-functions-recheck'; out.mkdir(exist_ok=True)
sources=json.loads((B/'d_functions-source-downloads.json').read_text())
ranges={'stanford':list(range(1,38))+list(range(46,77)),'stanford_ps3':[5,6],'cambridge':list(range(46,52)),'mit':[5,6,7,8],'cmu_assignment':[1]}
def fetch(v):
 key=v['id']; cached=Path(tempfile.gettempdir())/'deep-relations-recheck'/(key+'.pdf')
 if cached.exists(): content=cached.read_bytes()
 else:
  r=requests.get(v['url'],timeout=35); r.raise_for_status(); content=r.content
 assert content.startswith(b'%PDF'); p=out/(key+'.pdf'); p.write_bytes(content); pdf=PdfReader(p)
 body='\n'.join('\n=== PHYSICAL PDF PAGE '+str(i)+' ===\n'+(pdf.pages[i-1].extract_text() or '') for i in ranges[key]); (out/(key+'-scope.txt')).write_text(body,encoding='utf-8')
 return dict(id=key,url=v['url'],sha256=hashlib.sha256(content).hexdigest(),matchesHistoricalHash=hashlib.sha256(content).hexdigest()==v['sha256'],scopedPages=ranges[key],scopeCharacters=len(body),localReference=str(p),state='downloaded_reading_pending')
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
 jobs={pool.submit(fetch,v):v for v in sources if v['id'] in ranges}
 for job in concurrent.futures.as_completed(jobs):
  try: row=job.result(); rows.append(row); print(row['id'],row['scopeCharacters'],flush=True)
  except Exception as exc: rows.append(dict(id=jobs[job]['id'],state='fresh_access_failed',error=str(exc)));print(jobs[job]['id'],'access failed',flush=True)
(E/'d_functions-source-recheck-downloads.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
