from pathlib import Path
import re,xml.etree.ElementTree as ET
from collections import Counter
R=Path(__file__).resolve().parents[1]
c=Counter();samples={};q=0
for p in (R/'dist/chapters').glob('*.html'):
 s=p.read_text(encoding='utf-8');q+=s.count('class="exam-question"')
 for m in re.findall(r'<math\b[\s\S]*?</math>',s):
  for t in ET.fromstring(m).iter():
   if t.tag.split('}')[-1]!='mtable':continue
   key=str(t.attrib);c[key]+=1;samples.setdefault(key,(p.name,''.join(t.itertext())[:150]))
print(c);print(samples);print('Questions',q)
