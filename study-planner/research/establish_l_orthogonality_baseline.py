"""Anchor retention to the actual immutable publication, with explicit LF normalization."""
from pathlib import Path
import json,subprocess,hashlib
B=Path(__file__).resolve().parent;R=B.parent;E=B/'l_orthogonality-evidence'
p=E/'prior-library.json';old=json.loads(p.read_text())
backup=E/'prior-library-handoff.json'
if not backup.exists():backup.write_bytes(p.read_bytes())
commit='03f3c2006ebf7737e2468163a9e8763fd7c183ad'
changes=[]
for c in old['chapters']:
 published=subprocess.run(['git','show',commit+':dist/'+c['url']],cwd=R,capture_output=True,check=True).stdout.replace(b'\r\n',b'\n')
 current=(R/'dist'/c['url']).read_bytes().replace(b'\r\n',b'\n')
 assert published==current,c['topicId']
 c['canonicalLFsha256']=hashlib.sha256(published).hexdigest()
 if c['sha256']!=c['canonicalLFsha256']:changes.append(c['topicId'])
old.update(baselineSourceCommit=commit,normalization='CRLF converted to LF; no other normalization',note='The preliminary handoff preceded the final l_linear render. Retention is established against the actual published immutable source; original raw handoff is preserved separately.',handoffHashDifferences=changes)
p.write_text(json.dumps(old,indent=2)+'\n')
print('Verified all '+str(len(old['chapters']))+' pages against the immutable publication.')
