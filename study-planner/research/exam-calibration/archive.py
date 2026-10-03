"""Read original exam blobs without altering the repository working tree."""
from pathlib import Path
import subprocess,json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2]
REPO=Path('C:/Users/bheydari/AppData/Local/Temp/phd-exam-1406-analysis/repo')
CACHE=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406')
CACHE.mkdir(exist_ok=True)
sha=subprocess.check_output(['git','rev-parse','origin/main'],cwd=REPO,text=True).strip()
paths=subprocess.check_output(['git','ls-tree','-r','--name-only',sha,'Exams'],cwd=REPO,text=True).splitlines()
pdfs=[]
for path in paths:
 if not path.endswith('.pdf'):continue
 p=CACHE/'source'/path;p.parent.mkdir(parents=True,exist_ok=True)
 if not p.exists():p.write_bytes(subprocess.check_output(['git','show',sha+':'+path],cwd=REPO))
 parts=Path(path).parts
 pdfs.append(dict(repoPath=path,level=parts[1],field=parts[2],year=parts[3],sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
out=ROOT/'research/exam-calibration/archive-manifest.json'
out.write_text(json.dumps(dict(repository='https://github.com/bheydari721rn24/Phd-Exam-CSE',branch='main',commit=sha,files=pdfs),indent=2)+'\n',encoding='utf-8')
print('Read',len(pdfs),'PDF blobs from',sha,'without changing any archive files in the working tree.')
