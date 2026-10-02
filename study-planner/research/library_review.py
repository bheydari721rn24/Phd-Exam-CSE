"""Inventory the full chapter library and persist honest revision coverage."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/'research/library-review.json'
chapters=[c for w in json.loads((ROOT/'dist/lessons.json').read_text(encoding='utf-8')) for c in w['chapters']]
data=json.loads(PATH.read_text(encoding='utf-8')) if PATH.exists() else {'started':'2026-10-02','state':'in_progress','requestedScope':'All 16 existing chapters: sentence-level semantic review, worked solutions, end rules, formulas, all diagrams and interactive models. No new chapters during this revision.','chapters':[]}
existing={c['topicId']:c for c in data['chapters']}
for c in chapters:
 topic=c['topicId'];files=sorted((ROOT/'research').glob(topic+'*.en.md'))
 row=existing.get(topic,{'topicId':topic,'semanticReview':'pending','diagramReview':'pending','findings':[]})
 row['manuscripts']=[{'path':str(p.relative_to(ROOT)).replace('\\','/'),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'words':len(p.read_text(encoding='utf-8').split())} for p in files]
 row['renderedPath']=c['url'];existing[topic]=row
data['chapters']=[existing[c['topicId']] for c in chapters]
PATH.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print('Inventoried',len(chapters),'chapters;',sum(f['words'] for c in data['chapters'] for f in c['manuscripts']),'manuscript words. Semantic review stays pending until actually read.')
