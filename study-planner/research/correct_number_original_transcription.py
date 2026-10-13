"""Repair independently identified source errors without altering historical baselines."""
from pathlib import Path
import ast, hashlib, json, re, sys
from markdown_it import MarkdownIt
from write_discrete_number_answers import A
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision'
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',mathml.markdown_math(s,md))
target={'MS_CS_1405_Q125':(2,4),'MS_CS_1405_Q129':(3,4)}
canonical={}
for p in [B/'exam-calibration/actual-items.json',B/'d_counting-authentic.json']:
 data=json.loads(p.read_text())
 for q in data:
  if q['id']not in target:continue
  i,key=target[q['id']];q['stem']=q['stem'].replace('(x^2+1/x)^{14}','(x^2+1/x)^{15}').replace('a+b+c=20','a+b+c=40');q['answer']=key;q['solution']=A[i];q['translationStatus']='Corrected against enlarged original PDF crop, 13 October 2026; previous transcription superseded';canonical[q['id']]=q
 p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Correct the source producer by replacing only the two author calls.
p=B/'exam-calibration/author_actual.py';s=p.read_text()
for ident,number in [('MS_CS_1405_Q125',125),('MS_CS_1405_Q129',129)]:
 q=canonical[ident];start=s.index("add('MS_CS_1405',"+str(q['pdfPage'])+','+str(number)+',');end=s.index('\nadd(',start)
 args=['MS_CS_1405',q['pdfPage'],number,' '.join(q['topics']),q['title'],q['stem'],q['options'],q['answer'],q['solution'],q['pattern']]
 if q.get('difficulty')=='Hard':args.append('Hard')
 s=s[:start]+'add('+','.join(repr(v)for v in args)+')'+s[end:]
p.write_text(s,encoding='utf-8')
# Keep the individually written counting manuscript and its producer coherent.
p=B/'write_counting_answers.py';s=p.read_text()
for i,answer in [(8,A[2]),(9,A[3])]:
 start=s.index('put('+str(i)+',');end=s.index('\nput(',start)if i==8 else s.index('\n# Identical authentic',start)
 s=s[:start]+f'put({i},4,r\'\'\'\n{answer}\n\'\'\')'+s[end:]
p.write_text(s,encoding='utf-8')
p=E/'s_counting-solutions.md';s=p.read_text()
for i,answer in [(8,A[2]),(9,A[3])]:s=re.sub(r'(^## Q'+str(i)+r'\s*$)[\s\S]*?(?=^## Q\d+\s*$|\Z)',lambda m:m[1]+'\n\n**Correct option: 4.**\n\n'+answer+'\n\n',s,flags=re.M)
p.write_text(s,encoding='utf-8')
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'pure_question_helpers','exec'),ns)
changed=[]
for p in (R/'dist/chapters').glob('*.html'):
 raw=p.read_text();edits=[]
 for a,b,attrs,q in ns['questions'](raw):
  ident=attrs.get('data-source-id')
  if ident not in target:continue
  item=canonical[ident];i,key=target[ident];m=list(re.finditer(r'<p class="exam-provenance">[\s\S]*?</p>',q));assert m,(p,ident)
  prefix=q[:m[-1].end()];prefix=re.sub(r'data-answer="\d+"','data-answer="4"',prefix)
  tail=''
  if p.stem=='s_counting' and i==3:tail='<section class="concept-animation question-specific-animation" data-scenes="counting-question-parity"><p>The model enumerates the five disjoint rows of this exact corrected problem.</p></section>'
  options='<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(k)+'.</b><div>'+render(v)+'</div></div>'for k,v in enumerate(item['options'],1))+'</div>'
  replacement=prefix+render(item['stem'])+options+'<details class="exam-solution"><summary>Read the full derivation and corrected source interpretation</summary>'+render('Correct option: 4.\n\n'+A[i])+tail+'</details></section>'
  edits.append((a,b,replacement))
 for a,b,v in reversed(edits):raw=raw[:a]+v+raw[b:]
 if edits:
  raw=re.sub(r'(concept-animations\.json|semantic-diagrams\.js|concept-animation\.js|advanced-simulations\.js|concept-unified\.js)(?:\?[^"\s>]*)?',r'\1?v=source-errata-20261013',raw)
  p.write_text(raw,encoding='utf-8');changed.append(dict(path=str(p.relative_to(R)),items=len(edits)))
p=B/'build_counting_question_models.py';s=p.read_text().replace('counts=[10,10,9,9,8]','counts=[20,20,19,19,18]').replace('upper=(19-b)//2','upper=(39-b)//2').replace('upper=[9,9,8,8,7]','upper=[19,19,18,18,17]').replace('{20-b}','{40-b}').replace('2j+c=20-b','2j+c=40-b').replace('reaches 46','reaches 96').replace('exact answer 46','exact answer 96');p.write_text(s,encoding='utf-8')
for name in ['verify_deep_counting_revision.py','verify_d_counting.py']:
 p=B/name;s=p.read_text().replace('20-a-b>=1 for a in range(21) for b in range(21-a))==46','40-a-b>=1 for a in range(41) for b in range(41-a))==96').replace("'MS_CS_1405_Q129':46","'MS_CS_1405_Q129':96")
 # Update the separately stored original-item oracle, not unrelated original examples.
 s=s.replace("'MS_CS_1405_Q129':count", "'MS_CS_1405_Q129':count")
 if name=='verify_deep_counting_revision.py':s=s.replace("oldkey)","(4 if a.get('data-source-id')=='MS_CS_1405_Q129' else oldkey))")
 p.write_text(s,encoding='utf-8')
p=E/'s_counting-revision.json';data=json.loads(p.read_text())
for record in data.get('records',[]):
 if record.get('sourceId')in target:
  i,key=target[record['sourceId']];record.update(answer=key,words=len(A[i].split()),solutionSha256=hashlib.sha256(A[i].encode()).hexdigest(),sourceCorrection='13 October enlarged original scan; earlier source transcription invalidated')
data['sourceErrataEvidence']='research/deep-library-revision/number-source-errata.json';p.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
record=dict(status='text_corrected_pending_current_browser_and_independent_oracles',date='2026-10-13',originalSha256='198f75f9f9d195adc5c09ab14d17029e63a3cd11030d62cffcdfcb5df7627527',corrections=[dict(id='MS_CS_1405_Q125',oldExponent=14,correctExponent=15,coefficient=0,correctOption=4),dict(id='MS_CS_1405_Q129',oldTotal=20,correctTotal=40,oldCount=46,correctCount=96,oldOption=2,correctOption=4)],changedPages=changed,historicalEvidence='Previous finite checks validated incorrectly transcribed inputs and do not establish source fidelity. Historical browser/check reports are preserved, superseded for these two items by this new correction record.')
(E/'number-source-errata.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8');print(changed)
