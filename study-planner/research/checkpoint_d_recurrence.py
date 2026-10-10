from pathlib import Path
import subprocess,json,tarfile,hashlib
R=Path(__file__).resolve().parents[1]
def git(*a):return subprocess.check_output(['git',*a],cwd=R,text=True,encoding='utf-8').strip()
assert not git('diff','--cached','--name-only')
paths=git('diff','--name-only').splitlines()+git('ls-files','--others','--exclude-standard').splitlines()
allowed={'WEEKLY_DELIVERY.md','dist/lessons.json','research/chapter-gate.json','research/acquire_d_recurrence.py','research/add_d_recurrence_proof_figures.py','research/build_d_recurrence.py','research/checkpoint_d_recurrence.py','research/complete_d_recurrence.py','research/finalize_d_recurrence_teaching.py','research/finish_d_recurrence_visuals.py','research/prepare_d_recurrence_qa.py','research/qa_d_recurrence_browser.py','research/record_d_recurrence_reading.py','research/refine_d_recurrence_visuals.py','research/render_d_recurrence.py','research/verify_d_recurrence.py','research/g_mux-publication-pending.json'}
assert paths and all(p in allowed or p.startswith(('research/d_recurrence','research/d_generating-evidence/','dist/chapters/d_recurrence','dist/reviews/d_recurrence'))for p in paths),paths
subprocess.run(['git','add','--',*paths],cwd=R,check=True);subprocess.run(['git','diff','--cached','--check'],cwd=R,check=True);subprocess.run(['git','commit','-m','Add deeply reviewed discrete recurrence chapter with 83 solutions and proof-specific models'],cwd=R,check=True)
assert not git('status','--porcelain')
files=[R/'.openai/hosting.json']+sorted(p for p in(R/'dist').rglob('*')if p.is_file());dest=Path('C:/Users/bheydari/AppData/Local/Temp/d-recurrence-reviewed.tar.gz')
with tarfile.open(dest,'w:gz')as t:
 for p in files:assert not p.is_symlink()and p.resolve().is_relative_to(R.resolve());t.add(p,arcname=p.relative_to(R).as_posix(),recursive=False)
with tarfile.open(dest,'r:gz')as t:
 assert len(t.getmembers())==len(files)
 for m,p in zip(t.getmembers(),files):assert m.name==p.relative_to(R).as_posix()and t.extractfile(m).read()==p.read_bytes()
record=dict(project_id='appgprj_6ab5666f72b081918286c6b371c1eb1b',commit_sha=git('rev-parse','HEAD'),archive=str(dest),files=len(files),archiveSha256=hashlib.sha256(dest.read_bytes()).hexdigest(),sourcePushState='pending',onlinePublicationState='pending',reason='Exact source and byte-verified archive prepared; online success remains unconfirmed.')
(dest.with_suffix('.receipt.json')).write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8');print(json.dumps(record))
