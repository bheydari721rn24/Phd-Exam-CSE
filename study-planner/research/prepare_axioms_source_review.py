from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,tempfile,requests,fitz
B=Path(__file__).resolve().parent;OUT=Path(tempfile.gettempdir())/'deep-axioms-sources';OUT.mkdir(exist_ok=True)
sources=[('MIT','https://ocw.mit.edu/courses/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/fee036e2e13527166fb7f8bcd0647844_MIT6_041F10_L01.pdf',[1,2,3]),('Stanford','https://web.stanford.edu/class/archive/cs/cs109/cs109.1206/lectureNotes/LN03_probability.pdf',[1,2,3,4,5]),('ETH Zurich','https://metaphor.ethz.ch/x/2025/hs/401-3601-00L/main.pdf',[14,15,16])]
def fetch(row):
 name,url,pages=row;p=OUT/(name.replace(' ','_')+'.pdf');entry=dict(university=name,url=url,pdfPages=pages)
 try:
  response=requests.get(url,timeout=30);response.raise_for_status();p.write_bytes(response.content)
  doc=fitz.open(p);t=OUT/(name.replace(' ','_')+'.txt');t.write_text('\n'.join(f'PDF page {n}\n'+doc[n-1].get_text() for n in pages),encoding='utf-8')
  entry.update(sourceSha256=hashlib.sha256(p.read_bytes()).hexdigest(),textPath=str(t),readingState='downloaded_pending_actual_read')
 except Exception as e:entry.update(readingState='fetch_unavailable',errorType=type(e).__name__)
 return entry
with ThreadPoolExecutor(max_workers=3) as pool:records=list(pool.map(fetch,sources))
records.append(dict(university='Berkeley',url='https://www.stat.berkeley.edu/~wfithian/courses/stat210a/measure-theory-basics.html',readingState='official_web_text_actually_read',readingBounds='Measures section and probability normalization; source integration discussion is outside the chapter boundary.'))
actual=json.loads((B/'exam-calibration/actual-items.json').read_text());pages=[]
for q in actual:
 if 's_axioms' not in q.get('topics',[]):continue
 path=Path(tempfile.gettempdir())/'exam-calibration-1406/source'/q['repoPath'];assert hashlib.sha256(path.read_bytes()).hexdigest()==q['sourceSha256']
 image=OUT/(q['id']+'.png');doc=fitz.open(path);doc[q['pdfPage']-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(image)
 pages.append(dict(id=q['id'],pdfPage=q['pdfPage'],sourceSha256=q['sourceSha256'],image=str(image)))
report=dict(sources=records,sourcePages=pages,scope='Fresh bounded recheck of the four core written university sources selected in the documented eight-university survey; Oxford supplementary reading remains earlier evidence, not a fresh reading claim.')
(B/'deep-library-revision/s_axioms-course-recheck.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
