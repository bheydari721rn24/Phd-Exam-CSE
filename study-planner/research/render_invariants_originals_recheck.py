from pathlib import Path
import fitz, json, hashlib, tempfile
B=Path(__file__).parent;O=Path(tempfile.gettempdir())/'deep-invariants-recheck';O.mkdir(exist_ok=True)
ids=['Phd_CE_1405_Q3','Phd_CE_1405_Q9','MS_CS_1393_Q167','Phd_CS_1404_Q28']
rows=[]
for q in json.loads((B/'exam-calibration/actual-items.json').read_text()):
 if q['id']not in ids:continue
 p=Path('C:/Users/bheydari/Desktop/Phd-Exam-CSE')/q['repoPath'];digest=hashlib.sha256(p.read_bytes()).hexdigest();assert digest==q['sourceSha256']
 d=fitz.open(p);out=O/(q['id']+'-original.png');d[q['pdfPage']-1].get_pixmap(matrix=fitz.Matrix(1.7,1.7)).save(out)
 rows.append(dict(id=q['id'],sourceSha256=digest,physicalPage=q['pdfPage'],image=str(out),state='rendered_pending_actual_visual_reading'))
for key,page in [('cambridge',67),('stanford',5)]:
 p=O/(key+'.pdf');d=fitz.open(p);d[page-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(O/(key+'-source-original.png'))
(O/'original-pages.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8');print(rows)
