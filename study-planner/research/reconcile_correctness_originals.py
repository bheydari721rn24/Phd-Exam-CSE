from pathlib import Path
import fitz,hashlib,json,subprocess,tempfile
from read_correctness_bank import rows
R=Path(__file__).resolve().parents[1];M=Path('C:/Users/bheydari/AppData/Local/Temp/phd-exam-1406-analysis/repo');O=Path(tempfile.gettempdir())/'correctness-original-recheck';O.mkdir(exist_ok=True);out=[]
for row in rows[:4]:
 item=row['canonical'];p=O/(item['id']+'.pdf');data=subprocess.check_output(['git','show',item['sourceCommit']+':'+item['repoPath']],cwd=M)
 digest=hashlib.sha256(data).hexdigest();assert digest==item['sourceSha256'];p.write_bytes(data);doc=fitz.open(p);page=doc[item['pdfPage']-1];image=O/(item['id']+'.png');page.get_pixmap(matrix=fitz.Matrix(1.55,1.55)).save(image)
 out.append({'id':item['id'],'question':item['questionNumber'],'pdfPage':item['pdfPage'],'sha256':digest,'sourceCommit':item['sourceCommit'],'image':str(image),'visualReconciled':False,'answerProvenance':'Independently derived, not an official key'})
(R/'research/deep-library-revision/a_correct-original-recheck.json').write_text(json.dumps(out,indent=2)+'\n')
print(out)
