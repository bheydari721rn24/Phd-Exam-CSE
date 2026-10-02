"""Cache only university written references; do not touch synced or exam sources."""
import hashlib,json,tempfile,concurrent.futures
from pathlib import Path
import requests
from pypdf import PdfReader
OUT=Path(tempfile.gettempdir())/'phd-recurrence-sources';OUT.mkdir(exist_ok=True)
urls={'mit':'https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/1869dbf640ded6b31f1bd369d2001ef5_MIT6_006S20_r03.pdf','mit_ab':'https://courses.csail.mit.edu/6.046/spring04/handouts/akrabazzi.pdf','stanford':'https://stanford-cs161.github.io/winter2025/assets/files/lecture3-notes.pdf','stanford_checks':'https://stanford-cs161.github.io/winter2025-bank/recurrence.pdf','cmu':'https://www.cs.cmu.edu/afs/cs/academic/class/15451-f11/www/lectures/lects1-10.pdf','cornell':'https://www.cs.cornell.edu/courses/cs3110/2009sp/lectures/lec20.html','cornell_sub':'https://www.cs.cornell.edu/courses/cs3110/2011sp/Recitations/rec19.htm','princeton':'https://aofa.cs.princeton.edu/20recurrence/'}
def get(item):
 key,url=item;p=OUT/(key+('.pdf' if url.endswith('.pdf') else '.html'));r=requests.get(url,timeout=45);r.raise_for_status();p.write_bytes(r.content)
 pages=0
 if p.suffix=='.pdf':
  texts=[x.extract_text() or '' for x in PdfReader(p).pages];pages=len(texts);(OUT/(key+'.txt')).write_text('\n'.join('PAGE '+str(i+1)+'\n'+s for i,s in enumerate(texts)),encoding='utf-8')
 return {'id':key,'url':url,'sha256':hashlib.sha256(r.content).hexdigest(),'pages':pages,'localReference':str(p)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(get,urls.items()))
Path('research/a_recurrence-source-downloads.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows,indent=2))
