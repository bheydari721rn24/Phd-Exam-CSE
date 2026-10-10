from pathlib import Path
import subprocess,json,tarfile,hashlib
R=Path(__file__).resolve().parents[1]
def git(*a):return subprocess.check_output(['git',*a],cwd=R,text=True,encoding='utf-8').strip()
assert not git('diff','--cached','--name-only')
paths=git('diff','--name-only').splitlines()+git('ls-files','--others','--exclude-standard').splitlines()
allowed={'WEEKLY_DELIVERY.md','dist/lessons.json','research/chapter-gate.json','research/acquire_d_generating.py','research/build_d_generating.py','research/checkpoint_d_generating.py','research/complete_d_generating.py','research/finalize_d_generating_teaching.py','research/finish_d_generating_visuals.py','research/fix_d_generating_caption.py','research/polish_d_generating_geometry.py','research/prepare_d_generating_qa.py','research/qa_d_generating_browser.py','research/refine_d_generating.py','research/render_d_generating.py','research/verify_d_generating.py'}
assert paths and all(p in allowed or p.startswith(('research/d_generating','research/a_bst-evidence/','dist/chapters/d_generating','dist/reviews/d_generating'))for p in paths),paths
subprocess.run(['git','add','--',*paths],cwd=R,check=True);subprocess.run(['git','diff','--cached','--check'],cwd=R,check=True);subprocess.run(['git','commit','-m','Add deeply reviewed generating functions with 82 solutions and exact problem-specific models'],cwd=R,check=True)
assert not git('status','--porcelain')
files=[R/'.openai/hosting.json']+sorted(p for p in(R/'dist').rglob('*')if p.is_file());dest=Path('C:/Users/bheydari/AppData/Local/Temp/d-generating-reviewed.tar.gz')
with tarfile.open(dest,'w:gz')as t:
 for p in files:assert not p.is_symlink()and p.resolve().is_relative_to(R.resolve());t.add(p,arcname=p.relative_to(R).as_posix(),recursive=False)
with tarfile.open(dest,'r:gz')as t:
 assert len(t.getmembers())==len(files)
 for m,p in zip(t.getmembers(),files):assert m.name==p.relative_to(R).as_posix()and t.extractfile(m).read()==p.read_bytes()
record=dict(project_id='appgprj_6ab5666f72b081918286c6b371c1eb1b',commit_sha=git('rev-parse','HEAD'),archive=str(dest),files=len(files),archiveSha256=hashlib.sha256(dest.read_bytes()).hexdigest(),sourcePushState='pending',onlinePublicationState='pending',reason='Exact source and byte-verified archive prepared; online success remains unconfirmed.')
dest.with_suffix('.receipt.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8');print(json.dumps(record))
