from pathlib import Path
import subprocess,json,tarfile,hashlib
R=Path(__file__).resolve().parents[1]
def git(*a):return subprocess.check_output(['git',*a],cwd=R,text=True,encoding='utf-8').strip()
assert not git('diff','--cached','--name-only')
paths=git('diff','--name-only').splitlines()+git('ls-files','--others','--exclude-standard').splitlines()
allowed={'research/polish_a_bst.py','research/d_generating-publication.json','research/record_d_generating_publication.py','WEEKLY_DELIVERY.md','dist/lessons.json','research/chapter-gate.json','research/acquire_a_bst.py','research/build_a_bst.py','research/checkpoint_a_bst.py','research/complete_a_bst.py','research/finalize_a_bst_teaching.py','research/finish_a_bst_visuals.py','research/fix_a_bst_caption.py','research/polish_a_bst_geometry.py','research/prepare_a_bst_qa.py','research/qa_a_bst_browser.py','research/refine_a_bst.py','research/render_a_bst.py','research/verify_a_bst.py'}
assert paths and all(p in allowed or p.startswith(('research/a_bst','research/a_balanced-evidence/','dist/chapters/a_bst','dist/reviews/a_bst'))for p in paths),paths
subprocess.run(['git','add','--',*paths],cwd=R,check=True);subprocess.run(['git','diff','--cached','--check'],cwd=R,check=True);subprocess.run(['git','commit','-m','Add deeply reviewed binary search trees with 82 solutions and connected tree simulations'],cwd=R,check=True)
assert not git('status','--porcelain')
files=[R/'.openai/hosting.json']+sorted(p for p in(R/'dist').rglob('*')if p.is_file());dest=Path('C:/Users/bheydari/AppData/Local/Temp/a-bst-reviewed.tar.gz')
with tarfile.open(dest,'w:gz')as t:
 for p in files:assert not p.is_symlink()and p.resolve().is_relative_to(R.resolve());t.add(p,arcname=p.relative_to(R).as_posix(),recursive=False)
with tarfile.open(dest,'r:gz')as t:
 assert len(t.getmembers())==len(files)
 for m,p in zip(t.getmembers(),files):assert m.name==p.relative_to(R).as_posix()and t.extractfile(m).read()==p.read_bytes()
record=dict(project_id='appgprj_6ab5666f72b081918286c6b371c1eb1b',commit_sha=git('rev-parse','HEAD'),archive=str(dest),files=len(files),archiveSha256=hashlib.sha256(dest.read_bytes()).hexdigest(),sourcePushState='pending',onlinePublicationState='pending',reason='Exact source and byte-verified archive prepared; online success remains unconfirmed.')
dest.with_suffix('.receipt.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8');print(json.dumps(record))
