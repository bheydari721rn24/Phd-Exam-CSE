"""Keep newly added mechanisms independent of an earlier browser asset cache."""
from pathlib import Path
import json,re
B=Path(__file__).parent;R=B.parent;revision='deep-library-14-20261013'
p=R/'dist/chapters/concept-unified.js';s=p.read_text(encoding='utf-8');s=re.sub(r"fetch\('concept-animations\.json(?:\?[^']*)?'(?:,\{cache:'no-cache'\})?\)","fetch('concept-animations.json?v="+revision+"',{cache:'no-cache'})",s);p.write_text(s,encoding='utf-8')
progress=json.loads((B/'deep-library-revision/progress.json').read_text());changed=[]
for entry in progress['chapters']:
 p=R/'dist'/entry['url'];s=p.read_text(encoding='utf-8');old=s
 for name in ['semantic-diagrams.js','concept-unified.js']:
  s=re.sub(r'(src="'+re.escape(name)+r')(?:\?[^" ]*)?"',r'\1?v='+revision+'"',s)
 if s!=old:p.write_text(s,encoding='utf-8');changed.append(entry['topicId'])
print({'assetReferenceRefreshOnly':len(changed),'contentReviewCountUnchanged':progress['revisedChapters']})
