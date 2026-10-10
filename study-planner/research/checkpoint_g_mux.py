"""Commit only the current reviewed chapter; package exact deployable bytes."""
from pathlib import Path
import subprocess,json,tarfile,hashlib
R=Path(__file__).resolve().parents[1]
def git(*a):return subprocess.check_output(['git',*a],cwd=R,text=True,encoding='utf-8').strip()
assert not git('diff','--cached','--name-only')
paths=git('diff','--name-only').splitlines()+git('ls-files','--others','--exclude-standard').splitlines()
extra={'WEEKLY_DELIVERY.md','dist/lessons.json','research/chapter-gate.json','research/build_g_mux.py','research/prepare_g_mux_qa.py','research/finish_g_mux_diagrams.py','research/upgrade_g_mux_states.py','research/render_g_mux.py','research/verify_g_mux.py','research/qa_g_mux_browser.py','research/refine_g_mux.py','research/finalize_g_mux.py','research/complete_g_mux.py','research/checkpoint_g_mux.py'}
assert paths and all(p in extra or p.startswith(('research/g_mux','research/d_recurrence-evidence/','dist/chapters/g_mux','dist/reviews/g_mux'))for p in paths),paths
subprocess.run(['git','add','--',*paths],cwd=R,check=True);subprocess.run(['git','diff','--cached','--check'],cwd=R,check=True);subprocess.run(['git','commit','-m','Add reviewed selector decoder encoder chapter with 82 solutions and exact routing models'],cwd=R,check=True)
assert not git('status','--porcelain')
files=[R/'.openai/hosting.json']+sorted(p for p in(R/'dist').rglob('*')if p.is_file());dest=Path('C:/Users/bheydari/AppData/Local/Temp/g-mux-reviewed.tar.gz')
with tarfile.open(dest,'w:gz')as t:
 for p in files:assert not p.is_symlink()and p.resolve().is_relative_to(R.resolve());t.add(p,arcname=p.relative_to(R).as_posix(),recursive=False)
with tarfile.open(dest,'r:gz')as t:
 assert len(t.getmembers())==len(files)
 for m,p in zip(t.getmembers(),files):assert m.name==p.relative_to(R).as_posix()and t.extractfile(m).read()==p.read_bytes()
record=dict(project_id='appgprj_6ab5666f72b081918286c6b371c1eb1b',commit_sha=git('rev-parse','HEAD'),archive=str(dest),files=len(files),archiveSha256=hashlib.sha256(dest.read_bytes()).hexdigest(),sourcePushState='pending',onlinePublicationState='pending',reason='Prepared exact source and archive; private publication success must be reconciled separately.')
(dest.with_suffix('.receipt.json')).write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8');print(json.dumps(record))
