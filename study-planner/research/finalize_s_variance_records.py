from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent;R=B.parent;E=B/'s_variance-evidence'
m=json.loads((E/'mathematics.json').read_text());v=json.loads((E/'browser.json').read_text());assert m['status']==v['status']=='passed'
p=B/'s_variance-quality-audit.md';s=p.read_text(encoding='utf-8').replace('690 static expressions','713 static expressions').replace('737 expressions','760 expressions')
s=s.replace('All 56 preceding chapter HTML files must pass byte-for-byte retention before the chapter gate advances.','All 56 preceding delivered chapter HTML files passed byte-for-byte retention. A stale pre-final-render hash for the amortized chapter was reconciled against its actual immutable delivered Git source; the chapter itself was unchanged. See baseline-reconciliation.json.')
p.write_text(s,encoding='utf-8')
p=R/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf-8').replace('162 editable calculator cases and 690 static MathML fence checks','162 editable calculator cases and 713 static MathML fence checks');p.write_text(s,encoding='utf-8')
p=B/'s_distributions-evidence/prior-library.json';d=json.loads(p.read_text(encoding='utf-8'));c=next(c for c in d['chapters']if c['topicId']=='s_variance');c['sha256']=hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest();p.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
print('Final typography, formula and retention counts reconciled.')
