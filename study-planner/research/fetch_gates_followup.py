from fetch_gates_sources import get,OUT
from concurrent.futures import ThreadPoolExecutor
import json
URLS={
 'cambridge-intro':'https://www.cl.cam.ac.uk/teaching/2021/DigElec/slides/comb_intro_20_1.pdf',
 'cambridge-hazards':'https://www.cl.cam.ac.uk/teaching/2021/DigElec/slides/comb_haz_20.pdf',
 'cambridge-devices':'https://www.cl.cam.ac.uk/teaching/2021/DigElec/slides/dev_trans_20.pdf',
 'cambridge-exercises':'https://www.cl.cam.ac.uk/teaching/2021/DigElec/examples_20.pdf',
 'ucsd-universal':'https://cseweb.ucsd.edu/classes/sp22/cse140-a/slides/lec6UniversalSet.pdf',
 'ucsd-intro':'https://cseweb.ucsd.edu/classes/sp22/cse140-a/slides/lec1Introduction.pdf',
 'berkeley-design':'https://notes.cs61c.org/content/sds-combinational-logic/cl-design/'
}
records=list(ThreadPoolExecutor(7).map(get,URLS.items()))
p=OUT/'manifest.json';old=json.loads(p.read_text(encoding='utf-8'));old.extend(records);p.write_text(json.dumps(old,indent=2),encoding='utf-8')
print(json.dumps([{k:v for k,v in r.items() if k in ('id','characters','error')} for r in records],indent=2))
