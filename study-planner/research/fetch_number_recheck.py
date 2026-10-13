"""Acquire exact written scopes; downloads do not assert completed reading."""
from pathlib import Path
import requests,hashlib,json,concurrent.futures,tempfile,sys
import fitz
B=Path(__file__).parent;O=Path(tempfile.gettempdir())/'deep-number-recheck';O.mkdir(exist_ok=True)
sources={
 'mit':('https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf',[(252,260),(272,282)]),
 'berkeley-2026':('https://www.eecs70.org/assets/pdf/notes/n6.pdf',[(1,8)]),
 'berkeley-rsa-2026':('https://www.eecs70.org/assets/pdf/notes/n7.pdf',[(1,4)]),
 'cmu':('https://www.cs.cmu.edu/~sutner/pdf/60-modari.pdf',[(1,72)]),
 'cambridge':('https://www.cl.cam.ac.uk/teaching/2223/DiscMath/DiscMathProofsNumbersSetsNotes.pdf',[(123,143),(151,182)])}
def fetch(item):
 key,(url,scope)=item;p=O/(key+'.pdf')
 if not p.exists():
  r=requests.get(url,timeout=45);r.raise_for_status();assert r.content.startswith(b'%PDF');p.write_bytes(r.content)
 d=fitz.open(p);text='\n'.join('=== PHYSICAL PAGE '+str(i)+' ===\n'+d[i-1].get_text()for lo,hi in scope for i in range(lo,hi+1))
 (O/(key+'-scope.txt')).write_text(text,encoding='utf-8')
 return dict(id=key,url=url,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),physicalPages=scope,pages=len(d),characters=len(text),state='downloaded_pending_actual_root_reading')
if len(sys.argv)>1:sources={k:v for k,v in sources.items()if k in sys.argv[1:]}
rows=[];failures=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=5)as pool:
 for f in concurrent.futures.as_completed([pool.submit(fetch,x)for x in sources.items()]):
  try:row=f.result();rows.append(row);print(row,flush=True)
  except Exception as e:failures.append(str(e));print(type(e).__name__,str(e),flush=True)
record=B/'deep-library-revision/d_number-source-recheck-downloads.json'
prior=json.loads(record.read_text(encoding='utf-8'))if record.exists()else{'downloads':[],'failures':[]}
previous={v['id']:v for v in prior['downloads']};previous.update({v['id']:v for v in rows})
record.write_text(json.dumps(dict(downloads=list(previous.values()),failures=prior['failures']+failures,state='acquired_scopes_are_not_completed_reading'),indent=2)+'\n',encoding='utf-8')
