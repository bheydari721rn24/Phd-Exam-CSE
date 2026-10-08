from pathlib import Path
import json,subprocess,tarfile,hashlib,sys
R=Path(__file__).resolve().parents[1];B=R/'research';E=B/'i_uninformed-evidence'
def git(*args):return subprocess.check_output(['git',*args],cwd=R,text=True,encoding='utf-8').strip()
mode=sys.argv[1]
if mode=='prepare':
 assert json.loads((E/'browser.json').read_text())['status']=='passed';assert json.loads((E/'mathematics.json').read_text())['status']=='passed'
 data=json.loads((R/'dist/chapters/i_uninformed-models.json').read_text());(E/'models.json').write_text(json.dumps(dict(models=len(data['models']),checkpoints=sum(len(m['frames'])for m in data['models']),ids=[m['id']for m in data['models']],scope='Actual executable search traces, exact count specializations and explicitly qualified infinite-prefix illustrations.'),indent=2)+'\n',encoding='utf-8')
 g=json.loads((B/'chapter-gate.json').read_text());assert g['currentTopicId']=='i_uninformed'
 g.update(state='awaiting_user_approval',lastCompletedReview='Uninformed search: 31 sections, 81 fully worked problems, 80 final rules, four core written university courses plus Stanford, 25 models / 251 checkpoints, 6487 checks and 1800 independently compared search runs.',sourceAudit='research/i_uninformed-source-audit.md',qualityAudit='research/i_uninformed-quality-audit.md',reviewEvidence=['research/i_uninformed-evidence/'+s+'.json'for s in ['reading','mathematics','models','browser','lesson-and-retention']],nextReview='Await explicit approval of i_uninformed before writing any following chapter.',activeWork='i_uninformed is complete as a review draft; publication being attempted. No following chapter started.',publicationState='pending',publishedVersion=None)
 (B/'chapter-gate.json').write_text(json.dumps(g,indent=2)+'\n',encoding='utf-8')
 p=R/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf-8').replace('implement subject-specific agent models. Await approval after delivery.','implement subject-specific search models. Await approval after delivery.');s+='\n\n## Uninformed search complete review draft — 8 October 2026\n\n31 sections, 81 complete worked problems, 80 final examination rules, four core written courses plus Stanford application material, and 25 specialized models with 251 checkpoints. Independent finite-graph comparisons cover 1800 runs. All 44 previous chapter pages and 2839 previous problems are preserved. Browser checks include math, typography, every stored frame, real pause/resume, reduced motion, mobile, print and editable graph validation. Await explicit approval of i_uninformed. Publication is tracked separately; local validation alone does not establish online deployment.\n';p.write_text(s,encoding='utf-8')
elif mode=='commit':
 stage=[]
 for row in subprocess.check_output(['git','status','--porcelain'],cwd=R,text=True,encoding='utf-8').splitlines():
  p=row[3:];assert p in ['WEEKLY_DELIVERY.md','dist/lessons.json','research/chapter-gate.json']or'i_uninformed'in p,('Unexpected change; preserve without staging',p);stage.append(p)
 subprocess.run(['git','add','--',*stage],cwd=R,check=True);subprocess.run(['git','diff','--cached','--check'],cwd=R,check=True);subprocess.run(['git','commit','-m','Add rigorous uninformed-search chapter and executable frontier laboratories'],cwd=R,check=True);print(git('rev-parse','HEAD'))
elif mode=='package':
 assert not git('status','--porcelain'),'Package committed clean content only';sha=git('rev-parse','HEAD');dest=Path('C:/Users/bheydari/AppData/Local/Temp/i-uninformed-deploy.tar.gz');files=[R/'.openai/hosting.json']+sorted(p for p in(R/'dist').rglob('*')if p.is_file())
 for p in files:assert p.resolve().is_relative_to(R.resolve())and not p.is_symlink()
 with tarfile.open(dest,'w:gz')as tf:
  for p in files:tf.add(p,arcname=p.relative_to(R).as_posix(),recursive=False)
 with tarfile.open(dest,'r:gz')as tf:
  members=tf.getmembers();assert len(members)==len(files)
  for m,p in zip(members,files):assert m.name==p.relative_to(R).as_posix()and tf.extractfile(m).read()==p.read_bytes()
 print(json.dumps(dict(project_id='appgprj_6ab5666f72b081918286c6b371c1eb1b',commit_sha=sha,archive=str(dest),files=len(files),archiveSha256=hashlib.sha256(dest.read_bytes()).hexdigest())))
