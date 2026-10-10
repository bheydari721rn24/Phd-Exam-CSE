"""Compare executable circuits with independent exact-integer references."""
from pathlib import Path
import json,subprocess,tempfile,hashlib,re,sys,xml.etree.ElementTree as ET
B=Path(__file__).resolve().parent;R=B.parent;E=B/'g_arithmetic-evidence';cases=[]
def signed(v,n):return v if v<2**(n-1)else v-2**n
def add(op,n,a,b,c=0,z=0,expected=None):cases.append(dict(spec=dict(operation=op,n=n,a=a,b=b,c=c,z=z),expected=expected))
for n in range(1,6):
 M=2**n
 for a in range(M):
  for b in range(M):
   for c in [0,1]:
    exact=signed(a,n)+signed(b,n)+c;out=(a+b+c)%M
    exp=dict(sum=out,carry=(a+b+c)//M,overflow=int(exact< -M//2 or exact>M//2-1),negative=int(out>=M//2),zero=int(out==0),signedExact=exact)
    add('ripple',n,a,b,c,expected=exp);add('prefix',n,a,b,c,expected=dict(sum=out,carry=(a+b+c)//M))
   out=(a-b)%M;exact=signed(a,n)-signed(b,n)
   add('subtract',n,a,b,expected=dict(sum=out,carry=int(a>=b),borrow=int(a<b),overflow=int(exact< -M//2 or exact>M//2-1),negative=int(out>=M//2),zero=int(out==0),signedExact=exact))
   add('compare',n,a,b,expected=dict(less=int(a<b),equal=int(a==b),greater=int(a>b)))
   add('multiply',n,a,b,expected=dict(product=a*b))
   product=signed(a,n)*signed(b,n);add('booth',n,a,b,expected=dict(signedProduct=product,outputEncoding=product%(M*M)))
   if b:add('division',n,a,b,expected=dict(quotient=a//b,remainder=a%b))
for a in range(16):
 for b in range(16):
  for z in range(16):add('csa',4,a,b,z=z,expected=dict(total=a+b+z))
for a in range(10):
 for b in range(10):
  for c in [0,1]:add('bcd',4,a,b,c,expected=dict(digit=(a+b+c)%10,decimalCarry=(a+b+c)//10,total=a+b+c))
for a in [0,1]:
 for b in [0,1]:
  for c in [0,1]:add('full',1,a,b,c,expected=dict(sum=(a+b+c)%2,carry=(a+b+c)//2))
  add('nand',1,a,b,expected=dict(difference=a^b,borrow=int(a<b)))
for a in [0,1,7,15,16,127,128,254,255]:
 for b in [0,1,15,16,127,128,255]:
  for c in [0,1]:add('select',8,a,b,c,expected=dict(sum=(a+b+c)%256,carry=(a+b+c)//256,fullAdders=12,multiplexers=5))
tmp=Path(tempfile.gettempdir())/'g-arithmetic-reference.json';tmp.write_text(json.dumps(cases),encoding='utf-8')
script=r'''const fs=require('fs'),{makeModel}=require('./dist/chapters/g_arithmetic.js');let checked=0,states=0;for(const test of JSON.parse(fs.readFileSync(process.argv[1],'utf8'))){const m=makeModel('verification','Independent integer comparison',test.spec);for(const [k,v]of Object.entries(test.expected))if(m.result[k]!==v)throw Error(JSON.stringify({spec:test.spec,key:k,expected:v,actual:m.result}));for(const f of m.frames){let s=f.snapshot;if(s.columns)for(const col of s.columns){if(col.a+col.b+col.in!==col.sum+2*col.out)throw Error('Local column weight failed');if(col.i&&col.in!==s.columns[col.i-1].out)throw Error('Disconnected carry');}if(test.spec.operation==='division'){if(s.prefix!==s.b*s.Q+s.R||s.R<0||s.R>=s.b)throw Error('Division invariant failed');}if(test.spec.operation==='csa'){let v=s.done.reduce((v,i)=>v+((s.a>>i&1)+(s.b>>i&1)+(s.z>>i&1))*2**i,0);if(v!==s.sum+2*s.carry)throw Error('Compressor checkpoint weight failed');}states++;}checked++;}const bad=[{operation:'division',n:4,a:8,b:0,c:0,z:0},{operation:'bcd',n:4,a:10,b:0,c:0,z:0},{operation:'full',n:4,a:2,b:0,c:0,z:0},{operation:'select',n:4,a:1,b:1,c:0,z:0},{operation:'ripple',n:0,a:0,b:0,c:0,z:0},{operation:'ripple',n:4,a:16,b:0,c:0,z:0}];for(const spec of bad){let rejected=false;try{makeModel('bad','Invalid',spec)}catch(e){rejected=true}if(!rejected)throw Error('Invalid input accepted');}process.stdout.write(JSON.stringify({checkedCases:checked,checkedStates:states,rejectedInputs:bad.length}));'''
stats=json.loads(subprocess.check_output(['node','-e',script,str(tmp)],cwd=R,text=True,encoding='utf-8'))
sys.path.insert(0,str(B/'exam-rewrite'));from math_fences import delimiter_issues,closing_script_bases
html=(R/'dist/chapters/g_arithmetic.html').read_text(encoding='utf-8');maths=re.findall(r'<math\b.*?</math>',html,re.S)
for raw in maths:
 root=ET.fromstring(raw);assert not delimiter_issues(root),(raw,delimiter_issues(root));assert not closing_script_bases(root),raw
assert len(maths)>400
assert '<!--'not in html and '$'not in html
assert html.count('class="exam-question"')==82 and html.count('class="review-rule"')==80
previous=json.loads((E/'prior-library.json').read_text(encoding='utf-8'));print('Snapshot schema:',list(previous)if isinstance(previous,dict)else'list')
retention=[]
for q in previous.get('chapters',[]):
 path=R/'dist'/q['url'];actual=hashlib.sha256(path.read_bytes()).hexdigest();assert actual==q['sha256'],q['url'];retention.append(q['url'])
models=json.loads((R/'dist/chapters/g_arithmetic-models.json').read_text(encoding='utf-8'))
report=dict(topicId='g_arithmetic',status='passed',**stats,mathmlExpressions=len(maths),fenceIssues=0,originalProblems=80,authenticBridges=2,finalRules=80,models=len(models['models']),savedCheckpoints=sum(len(m['frames'])for m in models['models']),referenceFixtureSha256=hashlib.sha256(tmp.read_bytes()).hexdigest(),retainedPages=len(retention),limits='Independent integer references and checkpoint identities. No physical timing signoff or HDL synthesis claim.')
(E/'mathematics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps(report))
