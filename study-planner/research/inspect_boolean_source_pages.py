from pathlib import Path
import json,hashlib,fitz
from read_boolean_bank import rows
B=Path(__file__).parent;S=Path('C:/Users/bheydari/Desktop/Phd-Exam-CSE');O=Path('C:/Users/bheydari/AppData/Local/Temp/deep-boolean-exam-pages');O.mkdir(exist_ok=True)
result=[]
for r in rows[:7]:
 q=r['canonical'];p=S/q['repoPath'];data=p.read_bytes();assert hashlib.sha256(data).hexdigest()==q['sourceSha256']
 d=fitz.open(p);out=O/(q['id']+'.png');d[q['pdfPage']-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(out)
 result.append(dict(id=q['id'],page=q['pdfPage'],source=p.as_posix(),sha256=q['sourceSha256'],image=out.as_posix(),inspection='pending'))
(O/'pages.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
