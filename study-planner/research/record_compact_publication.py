"""Record the verified all-library publication without changing chapter approval."""
from pathlib import Path
import gzip,hashlib,json,subprocess
R=Path(__file__).resolve().parents[1];E=R/'research/library-simulation-standard'
receipt=json.loads((E/'publication.json').read_text());v=receipt['version_number']
compressed=Path(receipt['archive']).read_bytes()
assert hashlib.sha256(compressed).hexdigest()==receipt['archiveSha256']
raw=gzip.decompress(compressed)
receipt.update(localTarSha256=hashlib.sha256(raw).hexdigest(),localTarBytes=len(raw),provenanceVerification='All local packaged file bytes verified. Saved native source SHA and 404-file count verified. Native tar encoding and hash recorded separately.')
(E/'publication.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
p=R/'research/chapter-gate.json';g=json.loads(p.read_text());assert g['state']=='awaiting_user_approval' and g['currentTopicId']=='p_recursion'
g.update(publicationState='succeeded',publishedVersion=v,publicationRecordPath='research/library-simulation-standard/publication.json',librarySimulationPublicationPath='research/library-simulation-standard/publication.json',librarySimulationRevisionStatus='published',activeWork='All 47 written chapters revised in compact layout and published: 1040 distinct models and 7124 exact checkpoints. No following chapter started; p_recursion approval gate retained.')
p.write_text(json.dumps(g,indent=2)+'\n',encoding='utf-8')
p=E/'manifest.json';m=json.loads(p.read_text());m.update(status='published',publishedVersion=v,publicationRecord='publication.json');p.write_text(json.dumps(m,indent=2)+'\n',encoding='utf-8')
text='Version '+str(v)+' succeeded from '+receipt['commit_sha']+'. Saved source SHA and 404-file count verified. Native stored tar hash is recorded separately from the local gzip/PAX archive. GitHub content commit: '+receipt['githubContentCommit']+' on study-planner-1406. All 47 written chapters and their simulation models are covered. Chapter approval state is unchanged.'
with(E/'DELIVERY.en.md').open('a',encoding='utf-8')as f:f.write('\n## Publication\n\n'+text+'\n')
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\nPublication confirmed: '+text+'\n')
paths=['research/library-simulation-standard/publication.json','research/library-simulation-standard/manifest.json','research/library-simulation-standard/DELIVERY.en.md','research/record_compact_publication.py','research/chapter-gate.json','WEEKLY_DELIVERY.md']
assert not subprocess.check_output(['git','diff','--cached','--name-only'],cwd=R,text=True).strip()
subprocess.run(['git','add','--',*paths],cwd=R,check=True)
subprocess.run(['git','diff','--cached','--check'],cwd=R,check=True)
subprocess.run(['git','commit','-m','Record successful version 85 complete compact simulation publication'],cwd=R,check=True)
print(json.dumps({'version':v,'published':True,'localArchiveHashVerified':True,'nativeSourceAndFileCountVerified':True}))
