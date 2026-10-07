from pathlib import Path
import json,subprocess,tarfile,hashlib,sys,datetime
R=Path(__file__).resolve().parents[1];B=R/'research';E=B/'l_det-evidence'
def git(*args):return subprocess.check_output(['git',*args],cwd=R,text=True,encoding='utf-8').strip()
mode=sys.argv[1]
if mode=='commit':
 paths=subprocess.check_output(['git','status','--porcelain'],cwd=R,text=True,encoding='utf-8').splitlines();stage=[]
 for row in paths:
  p=row[3:];allowed=p in['WEEKLY_DELIVERY.md','dist/lessons.json','research/chapter-gate.json']or'l_det'in p
  assert allowed,('Unexpected change; preserve it rather than stage',p)
  stage.append(p)
 subprocess.run(['git','add','--',*stage],cwd=R,check=True);subprocess.run(['git','diff','--cached','--check'],cwd=R,check=True)
 subprocess.run(['git','commit','-m','Add deeply reviewed determinant chapter, worked bank and concept-specific laboratories'],cwd=R,check=True)
 print(git('rev-parse','HEAD'))
elif mode=='package':
 assert not git('status','--porcelain'),'Package committed clean content only'
 sha=git('rev-parse','HEAD');dest=Path('C:/Users/bheydari/AppData/Local/Temp/l-det-deploy.tar.gz')
 files=[R/'.openai/hosting.json']+sorted(p for p in(R/'dist').rglob('*')if p.is_file())
 for p in files:assert p.resolve().is_relative_to(R.resolve())and not p.is_symlink()
 with tarfile.open(dest,'w:gz')as tf:
  for p in files:tf.add(p,arcname=p.relative_to(R).as_posix(),recursive=False)
 with tarfile.open(dest,'r:gz')as tf:
  members=tf.getmembers();assert len(members)==len(files)
  for m,p in zip(members,files):assert m.name==p.relative_to(R).as_posix()and tf.extractfile(m).read()==p.read_bytes()
 print(json.dumps(dict(project_id='appgprj_6ab5666f72b081918286c6b371c1eb1b',commit_sha=sha,archive=str(dest),files=len(files),archiveSha256=hashlib.sha256(dest.read_bytes()).hexdigest())))
elif mode=='receipt':
 receipt=json.loads(Path(sys.argv[2]).read_text());assert receipt['deployment']['status']=='succeeded'and receipt['version']['source']['commit_sha']==receipt['contentCommit']
 receipt['version'].pop('screenshot_url',None)  # Do not persist a temporary signed preview URL.
 (B/'l_det-publication.json').write_text(json.dumps(receipt,indent=2)+'\n')
 version=receipt['version']['version_number'];g=json.loads((B/'chapter-gate.json').read_text());g.update(state='awaiting_user_approval',publicationState='published',publishedVersion=version,lastCompletedReview='Determinants: 29 sections, 82 complete solved problems, 80 condition-bearing final rules, four reviewed written courses from four universities, 17 concept models / 67 checkpoints, exact-rational editable laboratories and validated mathematical typography.',nextReview='Await explicit approval of l_det before any following chapter.',activeWork='l_det delivered as a review draft; approval required to promote and continue.')
 (B/'chapter-gate.json').write_text(json.dumps(g,indent=2)+'\n')
 with (R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\n\n## Determinants draft delivered\n\nPublished private Site version '+str(version)+'. l_det remains a draft awaiting explicit approval. Four core written university courses; 82 solved questions including two original-PDF-checked adaptations; 80 rewritten retrieval notes; 17 specialized models and 67 exact checkpoints; 342 exact checks; fonts, MathML delimiters, pause/resume, reduced motion, print and mobile passed. All 41 prior HTML files and 2,593 questions retained. The next chapter has not started.\n')
 subprocess.run(['git','add','research/l_det-publication.json','research/chapter-gate.json','WEEKLY_DELIVERY.md'],cwd=R,check=True)
 subprocess.run(['git','commit','-m','Record determinant publication and explicit approval gate'],cwd=R,check=True)
 print('Recorded version',version,'and awaiting_user_approval gate.')
