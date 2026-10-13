from pathlib import Path
import re,xml.etree.ElementTree as ET
for m in re.findall(r'<figure[\s\S]*?(<svg[\s\S]*?</svg>)',(Path(__file__).parents[1]/'dist/chapters/d_number.html').read_text()):
 root=ET.fromstring(m);print(root.attrib)
 for v in root.iter():
  if v.tag.split('}')[-1]in['path','line','circle','rect','polyline']:print(v.tag.split('}')[-1],v.attrib)
