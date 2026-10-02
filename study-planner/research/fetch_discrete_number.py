"""Download written references into temporary storage; synced sources stay untouched."""
import hashlib,json,tempfile,concurrent.futures
from pathlib import Path
import requests
from pypdf import PdfReader
OUT=Path(tempfile.gettempdir())/'phd-discrete-number-sources';OUT.mkdir(exist_ok=True)
urls={'cmu':'https://www.cs.cmu.edu/~sutner/pdf/60-modari.pdf','berkeley':'https://www.sp22.eecs70.org/assets/pdf/notes/n6.pdf','berkeley_rsa':'https://www.sp22.eecs70.org/assets/pdf/notes/n7.pdf','cambridge':'https://www.cl.cam.ac.uk/teaching/2223/DiscMath/DiscMathProofsNumbersSetsNotes.pdf'}
def get(item):
 key,url=item;p=OUT/(key+'.pdf');r=requests.get(url,timeout=60);r.raise_for_status();p.write_bytes(r.content);reader=PdfReader(p);texts=[x.extract_text() or '' for x in reader.pages];(OUT/(key+'.txt')).write_text('\n'.join('PAGE '+str(i+1)+'\n'+s for i,s in enumerate(texts)),encoding='utf-8');return {'id':key,'url':url,'sha256':hashlib.sha256(r.content).hexdigest(),'pages':len(texts),'localReference':str(p)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(get,urls.items()))
Path('research/d_number-source-downloads.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows,indent=2))
