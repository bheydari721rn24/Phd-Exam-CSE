"""Bind actual chapter inputs, manuscript math, originals and isolated runs."""
from pathlib import Path
from html.parser import HTMLParser
import hashlib,json,re,runpy,shutil,subprocess,sys,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];B=R/'research';E=B/'deep-library-revision';D=R/'dist/chapters'
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
Q=json.loads((B/'p_functions-questions.json').read_text(encoding='utf8'));A=json.loads((B/'p_functions-authentic.json').read_text(encoding='utf8'))
count=0
def check(ok,msg):
    global count
    assert ok,msg
    count+=1

# Keep independently authored reports and checkers, never course PDFs or secrets.
temp=Path('C:/Users/bheydari/AppData/Local/Temp')
copies={
 'functions-source-refresh-20261018/source-refresh.en.md':'p_functions-supplementary-source-refresh.en.md',
 'functions-source-refresh-20261018/acquisition.json':'p_functions-supplementary-acquisition.json',
 'functions-source-refresh-20261018/python-checks.json':'p_functions-independent-python-checks.json',
 'functions-authentic-refresh-20261018/report.en.md':'p_functions-originals-recheck.en.md',
 'phd-functions-numeric-20261018/review.md':'p_functions-independent-math-review.en.md'}
for src,dest in copies.items():shutil.copyfile(temp/src,E/dest)
code=(temp/'phd-functions-numeric-20261018/oracle.py').read_text(encoding='utf8')
code=code.replace("OUT = pathlib.Path(__file__).parent","OUT = ROOT / 'research/deep-library-revision'")
code=code.replace("(OUT/'oracle-results.json')","(OUT/'p_functions-remaining-oracle.json')")
(B/'verify_functions_remaining.py').write_text(code,encoding='utf8')
subprocess.run([sys.executable,'-X','utf8',str(B/'verify_functions_remaining.py')],check=True)
runpy.run_path(str(B/'verify_functions_review_start.py'))
remaining=json.loads((E/'p_functions-remaining-oracle.json').read_text(encoding='utf8'))
check(remaining['source_sha256']==hashlib.sha256((B/'p_functions-questions.json').read_bytes()).hexdigest(),'actual-input oracle hash')
check(remaining['check_count']==53 and remaining['actual_python_blocks']==20,'isolated original Python and mathematical checks')

page=(D/'p_functions.html').read_text(encoding='utf8')
check(page.count('class="exam-question"')==91,'91 complete question sections')
check(page.count('class="review-rule"')==80,'80 complete decision rules')
check('question-concept-aid'not in page,'unrelated generic question aliases removed')
check('Student-approved chapter'not in page,'new edition not falsely student-approved')
check(len(Q)==89 and len({q['id']for q in Q})==89,'89 distinct original/course-inspired placements')
for q in Q:
    check(len(q['solution'].split())>=100,q['id']+' complete replacement solution')
    for display,inline in re.findall(r'\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$',q['solution']):
        mathml.render(display or inline,bool(display));count+=1
check(A[0]['options'][3]=='`if(n<0)return; b[i+1]=a[n]; store(n-2,i+2);`','original option4 exact corrected source stride')
check('at most one'in A[1]['stem'],'original <=1 base preserved')
for q in A:
    p=Path('C:/Users/bheydari/Desktop/Phd-Exam-CSE')/q['repoPath']
    check(hashlib.sha256(p.read_bytes()).hexdigest()==q['sourceSHA'],q['id']+' original byte hash')
def split(a,depth=1):
    if len(a)<=1:return a,1,depth
    m=sorted(a)[len(a)//2];r,c1,d1=split([x for x in a if x>m],depth+1);l,c2,d2=split([x for x in a if x<m],depth+1)
    return r+[m]+l,1+c1+c2,max(d1,d2)
check(split([7,2,5,1,6,3,4])==([7,6,5,4,3,2,1],7,3),'authentic actual returned blocks, calls and peak depth')
for n in range(0,101):
    a=list(range(n));b=[];i=n-1
    while i>=0:b.append(a[i]);i-=2
    check(b==a[::-2]and len(b)==(n+1)//2,'reverse-stride '+str(n))

models=json.loads((D/'problem-visual-models.json').read_text(encoding='utf8'));new={k:v for k,v in models.items()if k.startswith('p_functions-review-')}
check(len(new)==27,'27 exact question aids')
for key,m in new.items():
    for f in m['frames']:ET.fromstring(f['html']);check(f['state']['question']in{q['id']for q in A+Q},key+' actual question identity')
check(new['p_functions-review-PF31']['frames'][0]['state']['rows'][0][1]=='0','PF31 caller x starts zero, independent of copied n=23')
check(new['p_functions-review-PF84']['frames'][-1]['state']['rows']==[[1,1,1],[2,3,4],[3,6,10],[4,10,20]],'two persistent accumulators differ')
# Token/fence syntax is inspected in every rendered native formula.
native=re.findall(r'<math\b[\s\S]*?</math>',page)
for formula in native:
    tree=ET.fromstring(formula)
    for node in tree.iter():node.tag=node.tag.rsplit('}',1)[-1]
    check(not mathml.delimiter_issues(tree),'native balanced math fences')
check('$'not in page and not re.search(r'[\u0600-\u06ff]',page),'English HTML and no unresolved TeX')
# All unrelated chapter bodies and existing models are byte-preserved.
base='dcf649d217f64234eda897de3be92831d51e96ae'
preserved=0
for p in D.glob('*.html'):
    if p.name=='p_functions.html':continue
    prior=subprocess.check_output(['git','show',base+':dist/chapters/'+p.name],cwd=R)
    check(p.read_bytes().replace(b'\r\n',b'\n')==prior.replace(b'\r\n',b'\n'),p.name+' unrelated body preserved');preserved+=1
old=json.loads(subprocess.check_output(['git','show',base+':dist/chapters/problem-visual-models.json'],cwd=R))
check(all(models[k]==v for k,v in old.items()),'every previous model preserved')
record={'status':'passed_current_functions_document_and_input_checks','checks':count,'nativeFormulas':len(native),'originalSolutions':89,'authenticBridgeSolutions':2,'rules':80,'exactProblemModels':len(new),'exactProblemFrames':sum(len(m['frames'])for m in new.values()),'unrelatedChapterBodiesPreserved':preserved,'actualPythonBlocks':20,'independentGroupedChecks':53,'questionSHA256':remaining['source_sha256'],'limitations':'Proofs plus bounded exact oracles and actual Python. No C/C++ compilation, physical ABI, exhaustive worldwide course reading or universal examination-score guarantee.'}
(E/'p_functions-current-mathematics.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print(record)
