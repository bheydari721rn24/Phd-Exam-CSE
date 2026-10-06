"""Repair demonstrated references to figure IDs renamed during older audits."""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parents[1];D=R/'dist/chapters';rows=[]
for p in D.glob('*.html'):
 if not re.match(r'^[daslgp]_',p.stem):continue
 text=p.read_text(encoding='utf-8');ids=set(re.findall(r'\bid=["\x27]([^"\x27]+)',text))
 for source in re.findall(r'<script[^>]+src="([^"]+)"',text):
  q=D/source.split('?')[0]
  if not q.is_file():continue
  code=q.read_text(encoding='utf-8');original=code
  candidates=set(re.findall(r'getElementById\(["\x27]([^"\x27]+)',code)+re.findall(r'url\(#([^\)]+)\)',code)+re.findall(r'querySelector\(["\x27]#([^"\x27 \[.]+)',code))
  for old in candidates-ids:
   choices=[new for new in ids if new.endswith('-'+old)]
   if len(choices)!=1:continue
   new=choices[0]
   code=re.sub(r'(getElementById\(["\x27])'+re.escape(old)+r'(["\x27])',lambda m:m[1]+new+m[2],code)
   code=code.replace('url(#'+old+')','url(#'+new+')')
   code=re.sub(r'(querySelector\(["\x27]#)'+re.escape(old)+r'(["\x27])',lambda m:m[1]+new+m[2],code)
   rows.append(dict(chapter=p.stem,script=q.name,old=old,new=new))
  if original!=code:q.write_text(code,encoding='utf-8')
(R/'research/library-animation-redesign/live-reference-repairs.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
print(json.dumps(rows))
