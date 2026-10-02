"""Rebuild each existing chapter sequentially with the shared math renderer."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[1]
names=['english','sets','proof','induction','model','asym','loop','axioms','counting','vectors','matrices','types','flow','number','boolean','gates']
for name in names:
    file='build_english_chapter.py' if name=='english' else f'build_{name}_chapter.py'
    r=subprocess.run([sys.executable,'-X','utf8',str(root/'research'/file)],cwd=root,capture_output=True,text=True,encoding='utf-8')
    print(file,r.returncode,r.stdout[-450:],flush=True)
    if r.returncode:
        print(r.stderr);sys.exit(r.returncode)
