from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,tempfile,requests,fitz
B=Path(__file__).resolve().parent;OUT=Path(tempfile.gettempdir())/'deep-loop-sources';OUT.mkdir(exist_ok=True)
sources=[('MIT','https://live.ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/477c78e0af2df61fa205bcc6cb613ceb_MIT6_006S20_lec1.pdf',[2,3,4]),('Stanford','https://web.stanford.edu/class/archive/cs/cs161/cs161.1152/Lecture-1.pdf',[6,7,8,9]),('Princeton','https://www.cs.princeton.edu/courses/archive/spr14/cos226/lectures/14AnalysisOfAlgorithms-2x2.pdf',[6,7,8,9,10])]
def fetch(row):
    name,url,pages=row;p=OUT/(name+'.pdf');entry=dict(university=name,url=url,pdfPages=pages)
    try:
        cached=Path(tempfile.gettempdir())/'deep-model-sources'/(name+'.pdf')
        if name=='MIT' and cached.exists():p.write_bytes(cached.read_bytes())
        else:
            response=requests.get(url,timeout=20);response.raise_for_status();p.write_bytes(response.content)
        doc=fitz.open(p);text='\n'.join(f'PDF page {n}\n'+doc[n-1].get_text() for n in pages);t=OUT/(name+'.txt');t.write_text(text,encoding='utf-8');entry.update(sourceSha256=hashlib.sha256(p.read_bytes()).hexdigest(),textPath=str(t),readingState='downloaded_pending_actual_read')
    except Exception as e:entry.update(readingState='fetch_unavailable',errorType=type(e).__name__)
    return entry
with ThreadPoolExecutor(max_workers=3) as pool:records=list(pool.map(fetch,sources))
records.append(dict(university='Berkeley',url='https://sp18.datastructur.es/materials/lectures/lec18/lec18',readingState='official_web_text_actually_read',readingBounds='Overview and recommended problems; no execution of malformed examples or whole-course reading claimed.'))
actual=json.loads((B/'exam-calibration/actual-items.json').read_text());pages=[]
for q in actual:
    if 'a_loop' not in q.get('topics',[]):continue
    path=Path(tempfile.gettempdir())/'exam-calibration-1406/source'/q['repoPath'];assert hashlib.sha256(path.read_bytes()).hexdigest()==q['sourceSha256']
    image=OUT/(q['id']+'.png');doc=fitz.open(path);doc[q['pdfPage']-1].get_pixmap(matrix=fitz.Matrix(1.4,1.4)).save(image)
    pages.append(dict(id=q['id'],pdfPage=q['pdfPage'],sourceSha256=q['sourceSha256'],image=str(image)))
report=dict(sources=records,sourcePages=pages,scope='Chapter-specific recheck of four written university selections from the documented six-university candidate pool. No complete-course or exhaustive worldwide claim.')
(B/'deep-library-revision/a_loop-course-recheck.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
