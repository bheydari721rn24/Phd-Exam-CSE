"""Remove only the two known artificial line-wrap table signatures."""
from pathlib import Path
import json,re,hashlib,xml.etree.ElementTree as ET
B=Path(__file__).resolve().parent;R=B.parent
MATH=re.compile(r'<math\b[\s\S]*?</math>');WRAP=re.compile(r'<mtable\b[^>]*columnalign="left"[^>]*>[\s\S]*?</mtable>')
changes=[];count=0
def unwrap(match):
 global count
 s=match[0];t=ET.fromstring(s)
 if t.attrib.get('displaystyle')!='true' or t.attrib.get('rowspacing') not in ('.5em','.55em'):return s
 rows=list(t)
 if not rows or any(r.tag!='mtr' or len(r)!=1 or r[0].tag!='mtd' for r in rows):return s
 body=s[s.index('>')+1:-len('</mtable>')]
 body=re.sub(r'</?(?:mtr|mtd)\b[^>]*>','',body)
 count+=1
 return '<mrow>'+body+'</mrow>'
for p in sorted((R/'dist/chapters').glob('*.html')):
 before=p.read_text(encoding='utf-8');n=count
 after=MATH.sub(lambda m:WRAP.sub(unwrap,m[0]),before)
 if before==after:continue
 old=MATH.findall(before);new=MATH.findall(after)
 assert len(old)==len(new)
 for a,b in zip(old,new):
  A=ET.fromstring(a);C=ET.fromstring(b)
  assert ''.join(A.itertext())==''.join(C.itertext()),p.name
  for tag in ['msub','msup','msubsup','mfrac','msqrt','mover','munder','munderover']:
   tagname=lambda x:x.tag.split('}')[-1]
   assert [ET.tostring(x) for x in A.iter() if tagname(x)==tag]==[ET.tostring(x) for x in C.iter() if tagname(x)==tag],(p.name,tag)
 assert before.count('class="exam-question"')==after.count('class="exam-question"')
 p.write_text(after,encoding='utf-8');changes.append(dict(chapter=p.stem,removedWraps=count-n,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
modelchanges=[]
for p in sorted((R/'dist/chapters').glob('*models.json')):
 a=json.loads(p.read_text(encoding='utf-8'));n=count
 for model in a.get('models',[]):
  for f in model.get('frames',[]):
   if 'formulaHtml' in f:f['formulaHtml']=WRAP.sub(unwrap,f['formulaHtml'])
 if count>n:p.write_text(json.dumps(a,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8');modelchanges.append(dict(file=p.name,removedWraps=count-n))
report=dict(state='source_repaired_pending_browser_validation',removedWraps=count,chapterChanges=changes,modelChanges=modelchanges,policy='Complete equations stay on one line; actual matrix/case rows remain unchanged.',questionCount=sum(p.read_text(encoding='utf-8').count('class="exam-question"') for p in (R/'dist/chapters').glob('*.html')))
(B/'single-line-math-audit.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report))
