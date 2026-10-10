from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,fitz,json,hashlib
O=Path('C:/Users/bheydari/AppData/Local/Temp/g-arithmetic-sources');R=Path(__file__).resolve().parents[1]
urls={
'berkeley-arithmetic':'https://people.eecs.berkeley.edu/~randy/Courses/CS150.F00/Lectures/09-Arith.pdf',
'berkeley-exercises':'https://people.eecs.berkeley.edu/~randy/Courses/CS150.F00/HWs/HW10_11.pdf',
'cornell-arithmetic':'https://www.cs.cornell.edu/courses/cs3410/2017sp/schedule/slides/03-numbers-and-arithmetic.pdf',
'cornell-combin':'https://www.csl.cornell.edu/courses/ece2300/handouts/ece2300-T02-comb-logic.pdf',
'mit-student':'https://6191.mit.edu/_static/fall24/resources/references/6004_student_notes_FA20.pdf',
'eth-combin2':'https://safari.ethz.ch/digitaltechnik/spring2020/lib/exe/fetch.php?media=onur-digitaldesign-2020-lecture5-combinational-logic-ii-afterlecture.pdf',
'cornell-2011':'https://www.cs.cornell.edu/courses/cs3410/2011sp/lecture/03-numbers-and-arithmetic-w.pdf',
}
def fetch(pair):
 key,url=pair
 try:
  p=O/(key+'.pdf')
  if p.exists():content=p.read_bytes()
  else:
   r=requests.get(url,timeout=(10,35));r.raise_for_status();content=r.content;assert content.startswith(b'%PDF');p.write_bytes(content)
  d=fitz.open(p);(O/(key+'.txt')).write_text('\n'.join('PDF PAGE '+str(i+1)+'\n'+pg.get_text()for i,pg in enumerate(d)),encoding='utf-8');return dict(id=key,url=url,path=str(p),sha256=hashlib.sha256(content).hexdigest(),pages=len(d))
 except Exception as e:return dict(id=key,url=url,error=str(e))
rows=list(ThreadPoolExecutor(5).map(fetch,urls.items()));(R/'research/g_arithmetic-evidence/followup-downloads.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8');print(json.dumps(rows,indent=2))
