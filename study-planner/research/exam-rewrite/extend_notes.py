"""Append audited boundary notes reproducibly after generating the main author data."""
import json,re
from pathlib import Path
base=Path(__file__).parent
for t,entries in json.loads((base/'extra_notes.json').read_text()).items():
 p=base/(t+'.md');s=p.read_text(encoding='utf-8')
 # Replace only a previously generated extension, preserving authored primary notes.
 s=s.split('<!-- BOUNDARY-NOTES -->')[0].rstrip()+'\n\n'
 section=s.split('## Applicable formulas and examination notes')[1]
 n=len(re.findall(r'^### \d+',section,re.M))
 s+='<!-- BOUNDARY-NOTES -->\n\n'
 for i,(title,body) in enumerate(entries,n+1):s+=f'### {i}. {title}\n\n{body}\n\n'
 p.write_text(s.rstrip()+'\n',encoding='utf-8')
print('Added concrete boundary notes to all 22 chapters.')
