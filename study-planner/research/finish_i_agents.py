from pathlib import Path
import json,subprocess,tarfile,hashlib,sys
R=Path(__file__).resolve().parents[1];B=R/'research';E=B/'i_agents-evidence'
def git(*args):return subprocess.check_output(['git',*args],cwd=R,text=True,encoding='utf-8').strip()
mode=sys.argv[1]
if mode=='commit':
 stage=[]
 for row in subprocess.check_output(['git','status','--porcelain'],cwd=R,text=True,encoding='utf-8').splitlines():
  p=row[3:];assert p in['WEEKLY_DELIVERY.md','dist/lessons.json','research/chapter-gate.json']or'i_agents'in p,('Unexpected change; preserve without staging',p);stage.append(p)
 subprocess.run(['git','add','--',*stage],cwd=R,check=True);subprocess.run(['git','diff','--cached','--check'],cwd=R,check=True)
 subprocess.run(['git','commit','-m','Add deeply reviewed intelligent-agent chapter and exact information-value laboratory'],cwd=R,check=True)
 print(git('rev-parse','HEAD'))
elif mode=='package':
 assert not git('status','--porcelain'),'Package committed clean content only'
 sha=git('rev-parse','HEAD');dest=Path('C:/Users/bheydari/AppData/Local/Temp/i-agents-deploy.tar.gz');files=[R/'.openai/hosting.json']+sorted(p for p in(R/'dist').rglob('*')if p.is_file())
 for p in files:assert p.resolve().is_relative_to(R.resolve())and not p.is_symlink()
 with tarfile.open(dest,'w:gz')as tf:
  for p in files:tf.add(p,arcname=p.relative_to(R).as_posix(),recursive=False)
 with tarfile.open(dest,'r:gz')as tf:
  members=tf.getmembers();assert len(members)==len(files)
  for m,p in zip(members,files):assert m.name==p.relative_to(R).as_posix()and tf.extractfile(m).read()==p.read_bytes()
 print(json.dumps(dict(project_id='appgprj_6ab5666f72b081918286c6b371c1eb1b',commit_sha=sha,archive=str(dest),files=len(files),archiveSha256=hashlib.sha256(dest.read_bytes()).hexdigest())))
