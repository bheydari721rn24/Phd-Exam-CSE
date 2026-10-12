from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,tempfile,requests,fitz
B=Path(__file__).resolve().parent;OUT=Path(tempfile.gettempdir())/'deep-counting-sources';OUT.mkdir(exist_ok=True)
sources=[('Stanford-combinatorics','Stanford','https://web.stanford.edu/class/archive/cs/cs109/cs109.1206/lectureNotes/LN02_combinatorics.pdf',list(range(1,8))),('Stanford-independence','Stanford','https://web.stanford.edu/class/archive/cs/cs109/cs109.1206/lectureNotes/LN05_independence.pdf',[1,2,3,4,5]),('Berkeley-counting','Berkeley','https://www.su19.eecs70.org/static/notes/n12.pdf',[1,2,3,4,5]),('Berkeley-probability','Berkeley','https://www.su19.eecs70.org/static/notes/n14.pdf',[6,7,8,9,10,11])]
def fetch(row):
 name,university,url,pages=row;p=OUT/(name+'.pdf');entry=dict(name=name,university=university,url=url,pdfPages=pages)
 try:
  response=requests.get(url,timeout=20);response.raise_for_status();p.write_bytes(response.content);doc=fitz.open(p);t=OUT/(name+'.txt');t.write_text('\n'.join(f'PDF page {n}\n'+doc[n-1].get_text() for n in pages),encoding='utf-8');entry.update(sourceSha256=hashlib.sha256(p.read_bytes()).hexdigest(),textPath=str(t),readingState='downloaded_pending_actual_read')
 except Exception as e:entry.update(readingState='download_unavailable',errorType=type(e).__name__)
 return entry
with ThreadPoolExecutor(max_workers=4) as pool:records=list(pool.map(fetch,sources))
records.append(dict(university='MIT',readingState='previous_current_revision_reading_reused',record='research/deep-library-revision/s_counting-initial-review.json',portions='6.041 / 6.431 Lectures 3 and 4, instructional PDF pages 1–2 actually read on 12 October 2026.'))
records.append(dict(university='Oxford',url='https://www.cs.ox.ac.uk/people/elias.koutsoupias/pc2016-17/lectures.html',readingState='pending_actual_web_read',portions='Lecture 2 independence definitions and Lecture 18 pairwise independence and bits-for-free construction.'))
actual=json.loads((B/'exam-calibration/actual-items.json').read_text());ids=['MS_CS_1405_Q113','MS_CS_1405_Q115','MS_CS_1405_Q120','MS_CS_1405_Q121','MS_CS_1405_Q122','MS_CS_1405_Q123','MS_CS_1405_Q124','MS_CS_1405_Q125','MS_CS_1405_Q129','Phd_CS_1404_Q25'];pages=[]
for q in actual:
 if q['id'] not in ids:continue
 path=Path(tempfile.gettempdir())/'exam-calibration-1406/source'/q['repoPath'];assert hashlib.sha256(path.read_bytes()).hexdigest()==q['sourceSha256'];image=OUT/(q['id']+'.png');doc=fitz.open(path);doc[q['pdfPage']-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(image);pages.append(dict(id=q['id'],pdfPage=q['pdfPage'],sourceSha256=q['sourceSha256'],image=str(image)))
report=dict(topicId='s_counting',state='in_progress',sources=records,originalPdfPages=pages,priorOriginalQuestionReview='Five authentic questions repeat the same source items individually checked in a_loop and s_axioms; reuse their recorded original-PDF inspections within those bounds.',selectionScope='Four selected universities from the documented eight-university written-course pool. Downloaded text is not counted as read until actually inspected; no worldwide census is claimed.')
(B/'deep-library-revision/s_counting-course-recheck.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
