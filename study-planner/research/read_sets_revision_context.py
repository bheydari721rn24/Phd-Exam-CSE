from pathlib import Path
import json,re,sys
B=Path(__file__).resolve().parent;R=B.parent
s=(R/'dist/chapters/d_sets.html').read_text(encoding='utf-8')
kind=sys.argv[1]
if kind=='sources':
 a=json.loads((B/'exam-calibration/actual-items.json').read_text())
 print(json.dumps([x for x in a if 'd_sets' in x.get('topics',[])],indent=2))
 print(s[s.index('id="course-selection"'):s.index('id="objects"')])
 print((B/'d_sets-source-audit.md').read_text(encoding='utf-8')[:7000])
elif kind=='rules':print(s[s.index('id="quick-reference"'):s.index('id="laboratory"')])
elif kind=='lab':print(s[s.rfind('<script>'):][-15000:])
elif kind=='builder':print((B/'finalize_deep_logic_revision.py').read_text(encoding='utf-8'))
elif kind=='sourceshort':
 a=json.loads((B/'exam-calibration/actual-items.json').read_text())
 for x in a:
  if 'd_sets' in x.get('topics',[]):print({k:x.get(k)for k in ['id','repoPath','pdfPage','sourceSha256']})
