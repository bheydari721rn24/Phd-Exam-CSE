from pathlib import Path
import subprocess
R=Path(__file__).resolve().parents[1]
status=subprocess.check_output(['git','status','--porcelain'],cwd=R,text=True,encoding='utf-8').splitlines()
paths=[]
for line in status:
 p=line[3:]
 assert p in ['WEEKLY_DELIVERY.md','dist/lessons.json','research/chapter-gate.json']or's_expectation'in p,(p,'Unexpected change requires inspection')
 paths.append(p)
subprocess.run(['git','add','--',*paths],cwd=R,check=True)
subprocess.run(['git','diff','--cached','--check'],cwd=R,check=True)
subprocess.run(['git','commit','-m','Add deeply worked expectation chapter with verified models and source audits'],cwd=R,check=True)
print('CONTENT_COMMIT='+subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip())
