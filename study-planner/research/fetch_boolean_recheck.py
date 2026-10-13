"""Refresh primary written bodies into a temporary, unpublished research cache."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,hashlib,json
S=Path('C:/Users/bheydari/AppData/Local/Temp/deep-boolean-recheck');S.mkdir(exist_ok=True)
urls={
'mit.html':'https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c4/c4s1/',
'cambridge.pdf':'https://www.cl.cam.ac.uk/teaching/2021/DigElec/slides/comb_log_bool_20.pdf',
'cambridge-examples.pdf':'https://www.cl.cam.ac.uk/teaching/2021/DigElec/examples_20.pdf',
'stanford.pdf':'https://web.stanford.edu/class/archive/ee/ee108a/ee108a.1082/lectures/01-introduction-w08.pdf',
'cmu.pdf':'https://course.ece.cmu.edu/~ee760/760docs/lec01.pdf',
'cmu-hw.pdf':'https://course.ece.cmu.edu/~ee760/760docs/hw1v1.pdf',
'berkeley-algebra.html':'https://notes.cs61c.org/content/sds-combinational-logic/boolean-algebra/',
'berkeley-design.html':'https://notes.cs61c.org/content/sds-combinational-logic/cl-design/',
'cornell.html':'https://www.cs.cornell.edu/courses/cs3410/2024fa/notes/logic.html'}
def fetch(item):
 name,url=item
 try:
  r=requests.get(url,timeout=60);r.raise_for_status();data=r.content
  if name.endswith('.pdf'):assert data.startswith(b'%PDF'), 'Not a PDF body'
  (S/name).write_bytes(data)
  return dict(name=name,url=url,status='retrieved_not_yet_read',bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
 except Exception as e:return dict(name=name,url=url,status='failed',error=str(e))
if __name__=='__main__':
 result=list(ThreadPoolExecutor(max_workers=4).map(fetch,urls.items()))
 (S/'manifest.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
