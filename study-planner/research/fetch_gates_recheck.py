from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,hashlib,json
S=Path('C:/Users/bheydari/AppData/Local/Temp/deep-gates-recheck');S.mkdir(exist_ok=True)
urls={'mit.html':'https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c3/c3s1/','cambridge-hazards.pdf':'https://www.cl.cam.ac.uk/teaching/2021/DigElec/slides/comb_haz_20.pdf','cambridge-devices.pdf':'https://www.cl.cam.ac.uk/teaching/2021/DigElec/slides/dev_trans_20.pdf','stanford.pdf':'https://web.stanford.edu/class/archive/ee/ee108a/ee108a.1082/reader/ch1to12.pdf','ucsd-universal.pdf':'https://cseweb.ucsd.edu/classes/sp22/cse140-a/slides/lec6UniversalSet.pdf','ucsd-intro.pdf':'https://cseweb.ucsd.edu/classes/sp22/cse140-a/slides/lec1Introduction.pdf','berkeley.html':'https://notes.cs61c.org/content/sds-combinational-logic/'}
def fetch(item):
 name,url=item
 try:
  r=requests.get(url,timeout=45);r.raise_for_status();data=r.content
  if name.endswith('.pdf'):assert data.startswith(b'%PDF')
  (S/name).write_bytes(data);return dict(name=name,url=url,state='retrieved_not_yet_read',bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
 except Exception as e:return dict(name=name,url=url,state='failed',error=str(e))
if __name__=='__main__':
 result=list(ThreadPoolExecutor(max_workers=4).map(fetch,urls.items()));(S/'manifest.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
