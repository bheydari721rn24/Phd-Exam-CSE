from pathlib import Path
import json,subprocess,tarfile,hashlib,io
B=Path(__file__).resolve().parent;R=B.parent
sha=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip()
assert sha.startswith('ea5670c')
archive=Path('C:/Users/bheydari/AppData/Local/Temp/a-heap-reviewed.tar.gz')
files=[R/'.openai/hosting.json']+sorted(p for p in (R/'dist').rglob('*')if p.is_file())
with tarfile.open(archive,'w:gz')as t:
 for p in files:
  rel=p.relative_to(R).as_posix();committed=subprocess.check_output(['git','show',sha+':'+rel],cwd=R)
  assert p.read_bytes()==committed or p.read_bytes().replace(b'\r\n',b'\n')==committed,rel
  info=tarfile.TarInfo(rel);info.size=len(committed);info.mode=0o644;t.addfile(info,io.BytesIO(committed))
with tarfile.open(archive,'r:gz')as t:
 for q in t:assert t.extractfile(q).read()==subprocess.check_output(['git','show',sha+':'+q.name],cwd=R)
x=dict(status='publication_pending_source_credential',projectId='appgprj_6ab5666f72b081918286c6b371c1eb1b',sourceCommit=sha,archive=str(archive),archiveSha256=hashlib.sha256(archive.read_bytes()).hexdigest(),archiveEntries=len(files),githubContentCommit='6f2f29c',githubBranch='study-planner-1406',chaptersAdded=['a_balanced','a_heap'],libraryChapters=54,questions=3657,reason='Native source-write credential request failed at the backend MCP transport. Heap source has not been confirmed pushed to Sites; no save/deploy was attempted for this source. GitHub mirror push succeeded and a byte-verified archive is retained.')
(B/'a_heap-publication-pending.json').write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
g=json.loads((B/'chapter-gate.json').read_text());g['publicationState']=x['status'];g['publicationRecordPath']='research/a_heap-publication-pending.json'
for q in g['completedReviewDrafts']:
 if q['topicId']=='a_heap':q.update(publicationState=x['status'],publicationRecord='research/a_heap-publication-pending.json')
(B/'chapter-gate.json').write_text(json.dumps(g,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in x.items()if k!='reason'}))
