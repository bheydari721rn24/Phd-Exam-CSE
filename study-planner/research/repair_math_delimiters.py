"""Apply the token-preserving fence repair to published static mathematics.

Also process stored model/audit HTML, so cached checkpoints and print copies
have the same structure. No TeX authoring, problems or lessons are rewritten.
"""
from pathlib import Path
import re,json,sys,collections,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R/'research/exam-rewrite'))
from math_fences import normalize_fences,closing_script_bases
PAT=re.compile(r'<math\b[\s\S]*?</math>')
report={'status':'in_progress','files':[],'instances':0,'fixedScriptBases':0,'remainingBadScriptBases':[]}
def rewrite(text,where,record=True):
 changed=0;bad=0;count=0
 def replace(m):
  nonlocal changed,bad,count
  before=m[0];count+=1;bad+=len(closing_script_bases(ET.fromstring(before)))
  after=normalize_fences(before);changed+=before!=after
  assert normalize_fences(after)==after,'Repair is not idempotent'
  remaining=closing_script_bases(ET.fromstring(after))
  if remaining and record:report['remainingBadScriptBases'].append({'path':where,'tex':ET.fromstring(after).get('aria-label')})
  return after
 value=PAT.sub(replace,text)
 if record:report['instances']+=count;report['fixedScriptBases']+=bad
 return value,changed
def visit(value,where):
 if isinstance(value,str):return rewrite(value,where,False)
 if isinstance(value,list):
  parts=[visit(x,where) for x in value];return [x[0] for x in parts],sum(x[1] for x in parts)
 if isinstance(value,dict):
  parts={k:visit(v,where) for k,v in value.items()};return {k:v[0] for k,v in parts.items()},sum(v[1] for v in parts.values())
 return value,0
for path in sorted((R/'dist').rglob('*')):
 if path.suffix not in {'.html','.json'}:continue
 old=path.read_text(encoding='utf-8')
 if path.suffix=='.json':
  changed=[0]
  def replace_string(m):
   value=json.loads(m[0]);new,n=rewrite(value,str(path.relative_to(R)));changed[0]+=n
   return json.dumps(new,ensure_ascii=not any(ord(c)>127 for c in m[0])) if n else m[0]
  new=re.sub(r'"(?:[^"\\]|\\.)*"',replace_string,old);n=changed[0]
  assert visit(json.loads(old),'validation')[0]==json.loads(new)
 else:new,n=rewrite(old,str(path.relative_to(R)))
 if n:
  # Removing the MathML expressions must leave the entire surrounding HTML
  # byte-identical, including all 2,593 problem stems and solution prose.
  if path.suffix=='.html':assert PAT.sub('MATH',old)==PAT.sub('MATH',new)
  path.write_text(new,encoding='utf-8');report['files'].append({'path':str(path.relative_to(R)),'groupedInstances':n})
assert not report['remainingBadScriptBases'],report['remainingBadScriptBases'][:10]
report['status']='passed';(R/'research/delimiter-evidence/repair.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='files'}|{'changedFiles':len(report['files']),'groupedInstances':sum(x['groupedInstances'] for x in report['files'])},indent=2))
