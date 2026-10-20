"""Check the integrated edition, independent exact visual states and preservation."""
from pathlib import Path
import json,re,hashlib,sys,subprocess,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];E=R/'research/deep-library-revision';D=R/'dist/chapters'
BASE='7d7a5e3e5d89513d66f1a1d0104e01b942fc8d39'
def load(p):return json.loads(p.read_text(encoding='utf8'))
def old(p):return subprocess.check_output(['git','show',BASE+':'+p],cwd=R)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
page=(D/'p_arrays.html').read_text(encoding='utf8');Q=load(R/'research/p_arrays-questions.json');A=load(R/'research/p_arrays-authentic.json')
assert len(Q)==81 and len(A)==2 and len({q['id']for q in Q+A})==83
assert page.count('class="exam-question"')==83 and page.count('class="review-rule"')==80
assert page.count('class="exam-solution"')==83 and page.count('data-problem-visual=')==38
assert all(len(q['solution'].split())>=100 for q in Q+A)
assert '\\x27'not in page and 'SIZE\\_MAX'not in page and 'Ã'not in page
assert 'Why a range check can itself be unsafe'in page and 'Student-approved chapter'not in page
sys.path.insert(0,str(R/'research/exam-rewrite'))
from math_fences import delimiter_issues,closing_script_bases
expressions=re.findall(r'<math\b[\s\S]*?</math>',page)
for expr in expressions:
    node=ET.fromstring(expr);assert not delimiter_issues(node)and not closing_script_bases(node),expr[:200]
    assert not any('\\'in(t.text or'')for t in node.iter()),expr[:200]
M=load(D/'problem-visual-models.json');prior=json.loads(old('dist/chapters/problem-visual-models.json'))
assert all(M[k]==v for k,v in prior.items())
new={k:v for k,v in M.items()if k.startswith('p_arrays-review-')};assert len(new)==38
def states(qid):return [f['state']for f in new['p_arrays-review-'+qid]['frames']]
checks=[]
def check(name,condition):assert condition,name;checks.append(name)
check('PA25 every accumulated boundary',states('PA25')[-1]['values']==[0,3,1,6,7,3])
v=[0,0,0,0,0]
for l,r,w in [(1,4,4),(2,5,-2)]:
    for i in range(l,r):v[i]+=w
d=states('PA26')[-1]['values'];check('PA26 boundary cancellation and reconstruction',[sum(d[:i+1])for i in range(5)]==v)
for qid,s,d,order in [('PA30',0,1,range(4)),('PA31',0,1,range(3,-1,-1)),('PA32',1,0,range(4))]:
    v=[2,4,6,8,10,12];expected=[v.copy()]
    for i in order:v[d+i]=v[s+i];expected.append(v.copy())
    check(qid+' each actual read/write',[f['values']for f in states(qid)]==expected)
for qid,reverse,subtract in [('PA28',False,False),('PA29',True,False),('PA41',True,True)]:
    v=[3,5,9,10]if subtract else[1,2,3,4,5];expected=[v.copy()]
    for i in(range(len(v)-1,0,-1)if reverse else range(1,len(v))):
        v[i]=v[i]-v[i-1]if subtract else v[i]+v[i-1];expected.append(v.copy())
    check(qid+' dependency direction',[f['values']for f in states(qid)]==expected)
check('PA38 left rotation',states('PA38')[-1]['values']==list(range(3,7))+list(range(3)))
v=states('PA40')[-1];check('PA40 stable retained prefix',v['values'][:v['logicalLength']]==[2,4,6,8])
check('PA45 length-changing slice',states('PA45')[-1]['values']==[1,8,6,7,9,5])
check('PA46 redirect one slot not inner identity',states('PA46')[-1]=={'a':['X','Y'],'b':['X','Z'],'X':[2,7],'Y':[5],'Z':[9]})
check('PA47 repeated identity versus comprehension',states('PA47')[1]['rows']==['R']*3 and states('PA47')[-1]['rows']==[[0,0,0,0],[0,0,9,0],[0,0,0,0]])
check('PA48 forward iterator mutation',states('PA48')[-1]['values']==[4,7])
check('PA72 wrapped ring indices',states('PA72')[0]['indices']==[(5+i)%7 for i in range(4)])
check('original167 exact selected indices',[s['sourceIndex']for s in states(A[0]['id'])]==[5,3,1,-1])
best=float('inf');updates=0;expected=[]
for i,v in enumerate([5,2,4,1,3]):
    if v<best:best=v;updates+=1
    expected.append({'read':i,'value':v,'minimum':best,'updates':updates})
check('original72 exact strict record trace',states(A[1]['id'])==expected)
unchanged=[]
for p in sorted(D.glob('*.html')):
    if p.name=='p_arrays.html':continue
    relative=p.relative_to(R).as_posix()
    assert p.read_bytes().replace(b'\r\n',b'\n')==old(relative).replace(b'\r\n',b'\n'),relative
    unchanged.append(p.name)
assert len(unchanged)==63
browser=load(E/'l_arrays-current-evidence/browser.json');assert browser['status']=='passed_arrays_current_revision_browser_checks'
# One decision for every placement, including cases where a state animation would mislead.
ledger=[]
for q in A+Q:
    key='p_arrays-review-'+q['id'];has=key in new
    ledger.append({'id':q['id'],'title':q['title'],'decision':'exact_input_visual_aid'if has else'complete_symbolic_or_semantic_derivation',
      'model':key if has else None,'reason':('The problem has a meaningful finite state or tabulated quantity, shown using its actual input.'if has else'This proof, arithmetic classification or language-contract question is explained directly by its complete derivation and the chapter representation diagrams; an invented execution would obscure its assumptions.'),'solutionWords':len(q['solution'].split())})
(E/'p_arrays-question-visual-decisions.json').write_text(json.dumps(ledger,indent=2)+'\n',encoding='utf8')
report={'status':'passed_arrays_current_revision_integrated_checks','date':'2026-10-20','solutions':83,'rules':80,'nativeMathExpressions':len(expressions),'exactVisualModels':38,'exactVisualFrames':sum(len(v['frames'])for v in new.values()),'independentVisualStateChecks':checks,'otherChapterBodiesUnchanged':len(unchanged),'oldSharedModelEntriesPreserved':len(prior),'questionBankSha256':digest(R/'research/p_arrays-questions.json'),'pageSha256':digest(D/'p_arrays.html'),'limits':'Finite independent reference examples and structural checks supplement proofs. No compiler run, physical cache measurement, exhaustive worldwide source review or universal guarantee.'}
(E/'p_arrays-current-mathematics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print({k:v for k,v in report.items()if k!='independentVisualStateChecks'})
