from pathlib import Path
import concurrent.futures,json,hashlib,tempfile
import requests
from pypdf import PdfReader
B=Path(__file__).parent;E=B/'deep-library-revision';OUT=Path(tempfile.gettempdir())/'deep-relations-recheck';OUT.mkdir(exist_ok=True)
src=json.loads((B/'d_relations-source-downloads.json').read_text())
ranges={'mit':list(range(1,25)),'cambridge':list(range(37,46)),'oxford':list(range(55,67))+list(range(107,121)),'stanford1':[7,8]+list(range(17,22))+[24,25]+list(range(28,37))+list(range(42,50))+[56,57],'stanford2':list(range(4,21))+[27,28]+list(range(40,43))+list(range(64,79)),'stanford_ps3':[2,3,4]}
def fetch(v):
 key=v['id'];r=requests.get(v['url'],timeout=45);r.raise_for_status();assert r.content.startswith(b'%PDF');p=OUT/(key+'.pdf');p.write_bytes(r.content);pages=PdfReader(p).pages
 text='\n'.join('\n=== PHYSICAL PDF PAGE '+str(i)+' ===\n'+(pages[i-1].extract_text()or'')for i in ranges[key]);(OUT/(key+'-scope.txt')).write_text(text,encoding='utf-8')
 return dict(id=key,url=v['url'],sha256=hashlib.sha256(r.content).hexdigest(),matchesHistoricalHash=hashlib.sha256(r.content).hexdigest()==v['sha256'],pages=len(pages),scopedPages=ranges[key],scopeCharacters=len(text),localReference=str(p),state='downloaded_reading_pending')
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=6)as pool:
 futures={pool.submit(fetch,v):v for v in src}
 for f in concurrent.futures.as_completed(futures):
  try:row=f.result();rows.append(row);print(row['id'],row['scopeCharacters'],flush=True)
  except Exception as exc:rows.append(dict(id=futures[f]['id'],url=futures[f]['url'],state='fresh_access_failed',error=str(exc)));print(futures[f]['id'],'access failed',flush=True)
(E/'d_relations-source-recheck-downloads.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8');print('Cached scopes are not marked read until actually examined.')
