"""Correct a stale pre-final-render baseline using the actual delivered commit."""
from pathlib import Path
import json,hashlib,subprocess
B=Path(__file__).resolve().parent;R=B.parent;E=B/'s_variance-evidence'
p=E/'prior-library.json';data=json.loads(p.read_text(encoding='utf-8'))
record=next(c for c in data['chapters']if c['topicId']=='a_amortized')
current=(R/'dist'/record['url']).read_bytes()
blob=subprocess.check_output(['git','show','25e1913d6ffc939bd7c4b4d3bdf78b08686e63b1:dist/'+record['url']],cwd=R)
assert current.replace(b'\r\n',b'\n')==blob
actual=hashlib.sha256(current).hexdigest()
if record['sha256']!=actual:
 evidence=dict(reason='The baseline was captured before the final amortized render. The unchanged working page is the actual delivered immutable 25e1913 source, verified against its Git blob after newline normalization.',oldEarlyRenderHash=record['sha256'],deliveredWorkingHash=actual,deliveredBlobHash=hashlib.sha256(blob).hexdigest(),deliveredSource='25e1913d6ffc939bd7c4b4d3bdf78b08686e63b1',chapterChangedDuringVariance=False)
 (E/'baseline-reconciliation.json').write_text(json.dumps(evidence,indent=2)+'\n',encoding='utf-8')
 record['sha256']=actual;p.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print('Verified amortized page matches delivered source; corrected stale early-render retention record.')
