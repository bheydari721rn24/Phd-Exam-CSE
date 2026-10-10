from pathlib import Path
import subprocess,json,tarfile,hashlib
R=Path(__file__).resolve().parents[1]
def git(*a):return subprocess.check_output(['git',*a],cwd=R,text=True,encoding='utf-8').strip()
assert not git('diff','--cached','--name-only')
paths=git('diff','--name-only').splitlines()+git('ls-files','--others','--exclude-standard').splitlines()
allowed={'WEEKLY_DELIVERY.md','dist/lessons.json','research/chapter-gate.json','research/a_bst-publication.json','research/record_a_bst_publication.py'}
prefixes=('research/a_balanced','dist/chapters/a_balanced','dist/reviews/a_balanced','research/a_heap-evidence/')
helpers={'research/'+n+'_a_balanced'+s+'.py'for n in ['build','render','verify','prepare','normalize','fix','finalize','refine','complete','checkpoint','debug','qa']for s in ['', '_render','_notation','_geometry','_evidence','_boundaries','_qa','_browser']}
assert paths and all(p in allowed or p in helpers or p.startswith(prefixes)for p in paths),paths
subprocess.run(['git','add','--',*paths],cwd=R,check=True);subprocess.run(['git','diff','--cached','--check'],cwd=R,check=True);subprocess.run(['git','commit','-m','Add source-reviewed balanced trees with 82 solved problems and 26 exact models'],cwd=R,check=True)
assert not git('status','--porcelain')
files=[R/'.openai/hosting.json']+sorted(p for p in(R/'dist').rglob('*')if p.is_file());dest=Path('C:/Users/bheydari/AppData/Local/Temp/a-balanced-reviewed.tar.gz')
with tarfile.open(dest,'w:gz')as t:
 for p in files:assert not p.is_symlink()and p.resolve().is_relative_to(R.resolve());t.add(p,arcname=p.relative_to(R).as_posix(),recursive=False)
with tarfile.open(dest,'r:gz')as t:
 assert len(t.getmembers())==len(files)
 for m,p in zip(t.getmembers(),files):assert m.name==p.relative_to(R).as_posix()and t.extractfile(m).read()==p.read_bytes()
x=dict(project_id='appgprj_6ab5666f72b081918286c6b371c1eb1b',commit_sha=git('rev-parse','HEAD'),archive=str(dest),files=len(files),archiveSha256=hashlib.sha256(dest.read_bytes()).hexdigest(),sourcePushState='pending',onlinePublicationState='pending')
dest.with_suffix('.receipt.json').write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8');print(json.dumps(x))
