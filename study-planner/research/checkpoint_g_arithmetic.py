"""Save only the active chapter changes and package byte-identical static output."""
from pathlib import Path
import json,subprocess,tarfile,hashlib
R=Path(__file__).resolve().parents[1]
def git(*args):return subprocess.check_output(['git',*args],cwd=R,text=True,encoding='utf-8').strip()
assert not git('diff','--cached','--name-only')
paths=git('diff','--name-only').splitlines()+git('ls-files','--others','--exclude-standard').splitlines()
extra={'WEEKLY_DELIVERY.md','dist/lessons.json','research/chapter-gate.json','research/start_g_arithmetic.py','research/acquire_g_arithmetic.py','research/fetch_arithmetic_followup.py','research/prepare_g_arithmetic.py','research/render_g_arithmetic.py','research/verify_g_arithmetic.py','research/qa_g_arithmetic_browser.py','research/refine_g_arithmetic.py','research/finish_arithmetic_models.py','research/finalize_arithmetic_layout.py','research/complete_g_arithmetic.py','research/checkpoint_g_arithmetic.py'}
assert paths and all(p in extra or p.startswith(('research/g_arithmetic','research/g_mux-evidence/','dist/chapters/g_arithmetic','dist/reviews/g_arithmetic'))for p in paths),paths
subprocess.run(['git','add','--',*paths],cwd=R,check=True);subprocess.run(['git','diff','--cached','--check'],cwd=R,check=True);subprocess.run(['git','commit','-m','Add deeply reviewed arithmetic circuits chapter with 82 solutions and exact circuit laboratories'],cwd=R,check=True)
assert not git('status','--porcelain')
files=[R/'.openai/hosting.json']+sorted(p for p in(R/'dist').rglob('*')if p.is_file());dest=Path('C:/Users/bheydari/AppData/Local/Temp/g-arithmetic-reviewed.tar.gz')
with tarfile.open(dest,'w:gz')as tf:
 for p in files:assert not p.is_symlink()and p.resolve().is_relative_to(R.resolve());tf.add(p,arcname=p.relative_to(R).as_posix(),recursive=False)
with tarfile.open(dest,'r:gz')as tf:
 assert len(tf.getmembers())==len(files)
 for m,p in zip(tf.getmembers(),files):assert m.name==p.relative_to(R).as_posix()and tf.extractfile(m).read()==p.read_bytes()
record=dict(project_id='appgprj_6ab5666f72b081918286c6b371c1eb1b',commit_sha=git('rev-parse','HEAD'),archive=str(dest),files=len(files),archiveSha256=hashlib.sha256(dest.read_bytes()).hexdigest(),sourcePushState='pending_new_credential',onlinePublicationState='pending_network',reason='Native Sites backend transport fails; previous source write credential has expired. No new online version is claimed.')
(dest.with_suffix('.receipt.json')).write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8');print(json.dumps(record))
