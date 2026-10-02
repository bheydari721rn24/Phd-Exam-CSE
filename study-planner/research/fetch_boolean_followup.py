from fetch_boolean_sources import get,OUT
from concurrent.futures import ThreadPoolExecutor
import json
urls={
 'cambridge':'https://www.cl.cam.ac.uk/teaching/2021/DigElec/slides/comb_log_bool_20.pdf',
 'cambridge-examples':'https://www.cl.cam.ac.uk/teaching/2021/DigElec/examples_20.pdf',
 'cornell':'https://www.cs.cornell.edu/courses/cs3410/2024fa/notes/logic.html',
 'berkeley-algebra':'https://notes.cs61c.org/content/sds-combinational-logic/boolean-algebra/',
 'berkeley-canonical':'https://notes.cs61c.org/content/sds-combinational-logic/cl-design/',
 'berkeley-handout':'https://notes.cs61c.org/build/boolean-3625491ef50d8dc8631d9471be8aad39.pdf',
 'stanford':'https://web.stanford.edu/class/archive/ee/ee108a/ee108a.1082/lectures/01-introduction-w08.pdf',
 'ucsd':'https://cseweb.ucsd.edu/classes/sp22/cse140-a/slides/lec2Boolean.pdf'
}
r=list(ThreadPoolExecutor(8).map(get,urls.items()));p=OUT/'manifest.json';a=json.loads(p.read_text());a.extend(r);p.write_text(json.dumps(a,indent=2),encoding='utf-8');print(json.dumps(r,indent=2))
