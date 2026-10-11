"""Independent finite enumerations and preservation checks for the rewritten logic bank."""
from pathlib import Path
import ast, hashlib, itertools as it, json, math, re, subprocess
import xml.etree.ElementTree as ET
import fitz
B=Path(__file__).resolve().parent; R=B.parent; E=B/'deep-library-revision'
checks=[]
def check(name,got,want):
 assert got==want,(name,got,want)
 checks.append(dict(name=name,result=got,expected=want,passed=True))
imp=lambda a,b:not a or b
bits=lambda n:it.product((0,1),repeat=n)
check('Q1 quantified witnesses',all(any(x<y for y in range(5))for x in range(5)),False)
check('Q1 order preservation',all(imp(x<y,(x+1)%5<(y+1)%5)for x in range(5)for y in range(5)),False)
rel={(0,1),(1,2),(2,0)}
check('Q2 assigned formula',[all(imp((x,y)in rel,((y+1)%3,0)in rel)for y in range(3))for x in[0,2]],[True,False])
check('Q3 semantic simplification',[4*a+2*b+c for a,b,c in bits(3)if a!=c],[1,3,4,6])
girls={'03','06','09'};boys={'02','04','05','08'};edges={('03','02'),('06','08'),('04','03'),('09','02')}
check('Q4 unique directed target',[sum((g,b)in edges for b in boys)for g in sorted(girls)],[1,1,1])
check('Q4 existential boy-to-girl',any((b,g)in edges for b in boys for g in girls),True)
check('Q5 self exclusion distinguishes option3',imp(True,imp(False,False))and not imp(True,imp(True,False)),True)
check('Q6 threshold rows',[4*p+2*q+r for p,q,r in bits(3)if p+q+r>=2],[3,5,6,7])
check('Q7 true row indices',[4*p+2*q+r for p,q,r in bits(3)if imp(p,r)and p==q],[0,1,7])
check('Q8 models',[''.join(map(str,x))for x in bits(4)if x[0]==x[1]and imp(x[0],x[2])and x[2]!=x[3]],['0001','0010','1110'])
check('Q9 odd parity indices',[4*p+2*q+r for p,q,r in bits(3)if(p+q+r)%2],[1,2,4,7])
rr=lambda x,y:y==(x+1)%4
check('Q10 cycle conditions',[all(any(rr(x,y)and rr(y,x)for y in range(4))for x in range(4)),all(any(rr(x,y)and rr(y,z)and rr(z,(x+1)%4)for y in range(4)for z in range(4))for x in range(4))],[False,False])
check('Q12 empty restriction',[all(imp(False,b)for b in[0,1]),any(False and b for b in[0,1])],[True,False])
models=[x for x in bits(4)if imp(x[0],x[1])and imp(x[2],x[1])and(not x[1]or x[3])]
check('Q13 unique entailed option',[all(f(*x)for x in models)for f in[lambda p,q,r,s:imp(s,p),lambda p,q,r,s:imp(p,s),lambda p,q,r,s:imp(q,p),lambda p,q,r,s:imp(not s,r)]],[False,True,False,False])
check('Q14 cyclic exact-two count',sum(sum([imp(p,q),imp(q,r),imp(r,p)])==2 for p,q,r in bits(3)),6)
for n in range(1,5):
 check(f'Q16-19 triple extensions n={n}',sum(x[0]==x[1]and imp(x[1],x[2])for x in bits(n+2)),3*2**(n-1))
 if n>=3:check(f'Q19 independent added equality n={n}',sum(x[0]==x[1]and imp(x[1],x[2])and x[3]==x[4]for x in bits(n+2)),3*2**(n-2))
 check(f'Q20-23 nonempty proper unary n={n}',sum(0<sum(x)<n for x in bits(n)),2**n-2)
 check(f'Q32-35 parity false rows n={n}',sum(sum(x)%2==0 for x in bits(n)),2**(n-1))
 check(f'Q36-39 converse countermodels n={n}',sum(all(imp(x[2*i],x[2*i+1])for i in range(n))and not all(imp(x[2*i+1],x[2*i])for i in range(n))for x in bits(2*n)),3**n-2**n)
 check(f'Q40-43 disjoint-pair disjunction n={n}',sum(any(x[2*i]and x[2*i+1]for i in range(n))for x in bits(2*n)),4**n-3**n)
 check(f'Q44-47 class selection n={n}',sum(any(x)for x in bits(n)),2**n-1)
 if n<=3:
  matrices=list(bits(n*n))
  check(f'Q24-27 row nonempty n={n}',sum(all(any(x[i*n:(i+1)*n])for i in range(n))for x in matrices),(2**n-1)**n)
  check(f'Q28-31 unique per row n={n}',sum(all(sum(x[i*n:(i+1)*n])==1 for i in range(n))for x in matrices),n**n)
  check(f'Q15 negate unique existence n={n}',all((not all(sum(x[i*n:(i+1)*n])==1 for i in range(n)))==any(sum(x[i*n:(i+1)*n])==0 or sum(x[i*n:(i+1)*n])>=2 for i in range(n))for x in matrices),True)
  check(f'Q48-51 empty-row count n={n}',sum(any(not any(x[i*n:(i+1)*n])for i in range(n))for x in matrices),2**(n*n)-(2**n-1)**n)
  check(f'Q50 independent inclusion-exclusion n={n}',sum((-1)**(j+1)*math.comb(n,j)*2**(n*(n-j))for j in range(1,n+1)),2**(n*n)-(2**n-1)**n)
check('Q43 shared atom',[sum((p and q)or(p and r)for p,q,r in bits(3)),sum((p and q)or(r and s)for p,q,r,s in bits(4))],[3,7])
check('Q47 exact3 true objects with class sizes1,2,3',sum(sum(a*b for a,b in zip(x,[1,2,3]))==3 for x in bits(3)),2)
rows=list(bits(4));G=[p and q for p,q,r,s in rows];H=[p or r for p,q,r,s in rows]
check('Q52 all Boolean function output tables',sum(all(imp(g,f)and imp(f,h)for g,f,h in zip(G,x,H))for x in bits(16)),256)
check('Q53 all512 relations',sum(all(any(x[i*3:(i+1)*3])for i in range(3))and any(all(x[i*3+j]for i in range(3))for j in range(3))for x in bits(9)),169)
check('Q53 full-column histogram',[sum(sum(all(x[i*3+j]for i in range(3))for j in range(3))==k for x in bits(9))for k in[1,2,3]],[147,21,1])
numeric={16:48,17:384,20:30,21:254,24:28629151,25:17878103347812890625,28:3125,29:16777216,32:16,33:128,36:211,37:6305,40:781,41:58975,44:31,45:255,48:4925281,49:568640725896660991}
forms=[lambda n:3*2**(n-1),lambda n:2**n-2,lambda n:(2**n-1)**n,lambda n:n**n,lambda n:2**(n-1),lambda n:3**n-2**n,lambda n:4**n-3**n,lambda n:2**n-1,lambda n:2**(n*n)-(2**n-1)**n]
for j,f in enumerate(forms):
 for offset,n in[(0,5),(1,8)]:check(f'Q{16+4*j+offset} decimal count',f(n),numeric[16+4*j+offset])
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text())
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
old=subprocess.check_output(['git','show','f890223f3111d27958eb483056556fded2d59ff3:dist/chapters/d_logic.html']).decode().replace('\r\n','\n')
new=(R/'dist/chapters/d_logic.html').read_text();oq=ns['questions'](old);nq=ns['questions'](new)
check('53 question identities retained',len(nq),53)
for i in range(7):
 check(f'Q{i+1} authentic source identity retained',nq[i][2]['data-source-id'],oq[i][2]['data-source-id'])
 check(f'Q{i+1} authentic answer order retained',nq[i][2]['data-answer'],oq[i][2]['data-answer'])
 if i!=5:
  pattern=r'<div class="exam-options">[\s\S]*?(?=<details)'
  check(f'Q{i+1} authentic options unchanged',re.search(pattern,nq[i][3])[0]==re.search(pattern,oq[i][3])[0],True)
check('Every answer has disclosure control',sum('<details class="exam-solution">'in q for a,b,c,q in nq),53)
check('Generic unrelated question animations removed',sum('question-concept-aid'in q for a,b,c,q in nq),0)
for a,b,attrs,q in nq:
 for m in re.findall(r'<math\b[\s\S]*?</math>',q):ET.fromstring(m)
check('Question MathML parses',True,True)
inventory=json.loads((E/'inventory.json').read_text())
for c in inventory['chapters']:
 if c['topicId']!='d_logic':check('Untouched chapter '+c['topicId'],hashlib.sha256((R/'dist'/c['url']).read_text().encode()).hexdigest(),c['canonicalLFsha256'])
actual=[q for q in json.loads((B/'exam-calibration/actual-items.json').read_text())if 'd_logic'in q['topics']]
cache=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source');images=Path('C:/Users/bheydari/AppData/Local/Temp/deep-logic-source-pages');images.mkdir(exist_ok=True)
pages=[]
for path in sorted({q['repoPath']for q in actual}):
 p=cache/path;qs=[q for q in actual if q['repoPath']==path]
 check('Source PDF hash '+Path(path).name,hashlib.sha256(p.read_bytes()).hexdigest(),qs[0]['sourceSha256'])
 doc=fitz.open(p)
 for page in sorted({q['pdfPage']for q in qs}):
  image=images/(('ms'if '/MS/'in path else'phd')+f'-p{page}.png');doc[page-1].get_pixmap(matrix=fitz.Matrix(1.7,1.7)).save(image)
  pages.append(dict(pdf=path,page=page,image=str(image),questions=[q['id']for q in qs if q['pdfPage']==page],visualRecheck='pending'))
report=dict(status='finite_checks_passed_visual_pdf_and_browser_pending',checks=checks,checkCount=len(checks),sourcePages=pages,limits='Finite enumerations certify their stated bounds. General counts rely on the written bijections and complement proofs. The wider library remains pending.')
(E/'d_logic-mathematical-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(checks=len(checks),passed=True,pages=pages),indent=2))
