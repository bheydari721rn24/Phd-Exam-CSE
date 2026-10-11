"""Materialize bounded official course readings and authentic question images."""
from pathlib import Path
import hashlib,json,re,tempfile
import fitz,requests
B=Path(__file__).resolve().parent;E=B/'deep-library-revision';out=Path(tempfile.gettempdir())/'deep-model-sources';out.mkdir(exist_ok=True)
sources=[
('MIT','https://live.ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/477c78e0af2df61fa205bcc6cb613ceb_MIT6_006S20_lec1.pdf',[1,2,3,4]),
('CMU','https://www.cs.cmu.edu/~15451-s25/notes/lecture03.pdf',[2,3,4]),
('Princeton','https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/02AlgorithmAnalysis-2x2.pdf',[1,2]),
('Stanford','https://web.stanford.edu/class/archive/cs/cs161/cs161.1182/Lectures/Lecture1/CS161Lecture01.pdf',[2,3]),
('Berkeley','https://cs170.org/assets/lec/lec-13_blank.pdf',[9,10,11])]
records=[]
for university,url,pages in sources:
    dest=out/(university+'.pdf')
    try:
        response=requests.get(url,timeout=30);response.raise_for_status();dest.write_bytes(response.content)
    except requests.RequestException as exc:
        records.append(dict(university=university,url=url,pdfPages=pages,readingState='local_fetch_unavailable_use_official_web_text_or_documented_prior_reading',errorType=type(exc).__name__))
        print(university,': direct fetch unavailable; official web reading remains usable.');continue
    d=fitz.open(dest);text='\n'.join('PAGE '+str(n)+'\n'+d[n-1].get_text()for n in pages);d.close();(out/(university+'.txt')).write_text(text,encoding='utf-8')
    records.append(dict(university=university,url=url,pdfPages=pages,sourceSha256=hashlib.sha256(dest.read_bytes()).hexdigest(),textPath=str(out/(university+'.txt')),readingState='downloaded_pending_actual_read'))
    print(university,':',len(text),'characters; pages',pages)
for q in json.loads((B/'exam-calibration/actual-items.json').read_text()):
    if 'a_model'not in q.get('topics',[]):continue
    p=Path(tempfile.gettempdir())/'exam-calibration-1406/source'/q['repoPath'];assert hashlib.sha256(p.read_bytes()).hexdigest()==q['sourceSha256'];d=fitz.open(p);d[q['pdfPage']-1].get_pixmap(matrix=fitz.Matrix(1.7,1.7)).save(out/(q['id']+'.png'));d.close()
(E/'a_model-course-recheck.json').write_text(json.dumps(dict(scope='Five official written readings within the previously documented six-course pool; not complete courses or a worldwide census.',sources=records),indent=2)+'\n')
print('Authentic source images:',out)
