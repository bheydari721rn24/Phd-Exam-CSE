from pathlib import Path
import fitz,hashlib,json,requests,tempfile
R=Path(__file__).resolve().parents[1];out=Path(tempfile.gettempdir())/'deep-asym-sources';out.mkdir(exist_ok=True)
sources=[('MIT','https://live.ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/c6d8f06c6f11e3342633dec85498f551_MIT6_006S20_r01.pdf',[3,6]),('Stanford','https://web.stanford.edu/class/archive/cs/cs161/cs161.1172/CS161Lecture02.pdf',[6,7]),('CMU','https://www.cs.cmu.edu/afs/cs/academic/class/15451-s06/www/lectures/lects1-5.pdf',[10,11,12]),('Princeton','https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/02AlgorithmAnalysis-2x2.pdf',[3,4,5,6])]
report=[]
for name,url,pages in sources:
    p=out/(name+'.pdf')
    try:
        if not p.exists():
            if name=='Princeton':p.write_bytes((Path(tempfile.gettempdir())/'deep-model-sources/Princeton.pdf').read_bytes())
            else:
                r=requests.get(url,timeout=12);r.raise_for_status();p.write_bytes(r.content)
        d=fitz.open(p);text='\n'.join(f'PDF page {i}\n'+d[i-1].get_text() for i in pages);d.close();(out/(name+'.txt')).write_text(text,encoding='utf-8')
        report.append(dict(university=name,url=url,pdfPages=pages,sourceSha256=hashlib.sha256(p.read_bytes()).hexdigest(),readingState='downloaded_pending_actual_read',textPath=str(out/(name+'.txt'))))
        print(name+'\n'+text)
    except Exception as e:report.append(dict(university=name,url=url,pdfPages=pages,readingState='local_fetch_unavailable_official_web_text_or_prior_reading',errorType=type(e).__name__))
items=[]
for q in json.loads((R/'research/exam-calibration/actual-items.json').read_text()):
    if 'a_asym' not in q.get('topics',[]):continue
    p=Path(tempfile.gettempdir())/'exam-calibration-1406/source'/q['repoPath'];assert hashlib.sha256(p.read_bytes()).hexdigest()==q['sourceSha256']
    d=fitz.open(p);target=out/(q['id']+'.png');d[q['pdfPage']-1].get_pixmap(matrix=fitz.Matrix(1.6,1.6)).save(target);d.close();items.append(dict(id=q['id'],pdfPage=q['pdfPage'],image=str(target)))
(R/'research/deep-library-revision/a_asym-course-recheck.json').write_text(json.dumps(dict(sources=report,sourcePages=items,scope='Selected written materials from a bounded documented six-university pool; no worldwide exhaustive ranking or whole-course reading claimed.'),indent=2)+'\n')
print(json.dumps(items,indent=2))
