"""Independent direct-law checks, symbolic identities, and editable-law oracles."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations,permutations
import json,subprocess,math,hashlib,re,xml.etree.ElementTree as ET
import sympy as S
B=Path(__file__).resolve().parent;R=B.parent;E=B/'s_variance-evidence';report=dict(status='in_progress',frameChecks=0,independentCases=0)
def eq(a,b):
 assert math.isclose(float(a),float(b),abs_tol=2e-9,rel_tol=2e-10),(a,b)
def raw(a):
 mu=sum(F(str(p['p']))*F(str(p['x']))for p in a);m2=sum(F(str(p['p']))*F(str(p['x']))**2 for p in a);return mu,m2,m2-mu**2
data=json.loads((R/'dist/chapters/s_variance-models.json').read_text(encoding='utf-8'))
for m in data['models']:
 spec=m['spec'];kind=spec['kind']
 for i,f in enumerate(m['frames']):
  ET.fromstring(f['svg']);z=f['snapshot']['state'];report['frameChecks']+=1
  if kind in['moments','sampling','walk']:
   a=z['points'];eq(sum(p['p']for p in a),1);assert all(p['p']>=0 for p in a);mu,m2,var=raw(a)
   for k,v in[('mean',mu),('second',m2),('variance',var)]:eq(z[k],v)
   if kind=='moments':eq(z['accumulated'],sum(p['p']*(p['x']-z['center'])**2 for p in a[:z['cursor']+1]))
   if kind=='walk':
    eq(mu,z['step']*(2*z['rightProbability']-1));eq(var,4*z['step']*z['rightProbability']*(1-z['rightProbability']))
    assert 0<=sum(p['p']for p in z['destination'])<=1+1e-9
    if z['complete']:eq(sum(p['p']for p in z['destination']),1)
    if z.get('from')is not None:
     assert abs(z['to']-z['from'])==1
     sourceMass=next(p['p']for p in z['source']if p['x']==z['from'])
     eq(z['sent'],sourceMass*(z['rightProbability']if z['to']>z['from']else 1-z['rightProbability']))
   if kind=='sampling':p=F(spec['K'],spec['N']);eq(var,z['n']*p*(1-p)*F(spec['N']-z['n'],spec['N']-1))
  elif kind=='joint':
   a=z['points'];eq(sum(p['p']for p in a),1);mx,m2x,vx=raw(a);my,m2y,vy=raw([dict(x=p['y'],p=p['p'])for p in a]);cov=sum(F(str(p['p']))*F(str(p['x']))*F(str(p['y']))for p in a)-mx*my
   eq(z['meanX'],mx);eq(z['meanY'],my);eq(z['varX'],vx);eq(z['varY'],vy);eq(z['accumulated'],sum(p['p']*(p['x']-float(mx))*(p['y']-float(my))for p in a[:z['cursor']+1]))
   if i==len(m['frames'])-1:eq(m['result']['covariance'],cov)
  elif kind=='mixture':
   gs=z['groups'];mu=sum(g['p']*g['mean']for g in gs);eq(z['mean'],mu);direct=sum(g['p']*(g['variance']+g['mean']**2)for g in gs)-mu**2
   eq(z['within']+z['between'],direct);eq(z['partialWithin'],sum(g['p']*g['variance']for g in gs[:z['cursor']+1]));eq(z['partialBetween'],sum(g['p']*(g['mean']-mu)**2 for g in gs[:z['cursor']+1]))
  elif kind in['quadratic','projection']:
   a=S.Matrix(z['coefficients']);M=S.Matrix(z['matrix']);eq(z['variance'],(a.T*M*a)[0])
  elif kind=='averaging':
   count=z['n'];M=S.Matrix(count,count,lambda i,j:spec['matrix'][0][0]if i==j else spec['matrix'][0][1]);a=S.ones(count,1)/count;eq(z['variance'],(a.T*M*a)[0]);assert min(float(v)for v in M.eigenvals())>=-1e-9
  elif kind=='permutations':
   ps=list(permutations(range(1,z['n']+1)))[:z['processed']];hits=[sum(v==i+1 for i,v in enumerate(p))for p in ps];eq(z['partialMean'],sum(hits)/z['total']);eq(z['partialSecond'],sum(h*h for h in hits)/z['total'])
expected={'weighted-three':{'mean':F(7,2),'variance':F(11,4)},'center-shift':{'squaredError':13},'joint-positive':{'covariance':F(1,12)},'bernoulli-opposite':{'covariance':F(-1,4)},'overlap':{'covariance':F(1,4)},'parabola':{'varX':F(2,3),'varY':F(2,9),'covariance':0},'without-replacement':{'variance':F(14,25)},'fixed-points':{'variance':1},'empty-boxes':{'variance':F(3,16)},'two-group':{'within':7,'between':3,'variance':10},'latent-bernoulli':{'variance':F(1,4)},'latent-pair':{'covariance':F(1,12)},'heteroscedastic':{'variance':F(5,2)},'cancel-covariance':{'covariance':0},'quadratic-weight':{'variance':32},'linear-projection':{'variance':61},'averaging':{'variance':F(15,4)},'same-versus-independent':{'variance':F(5,8)},'chebyshev':{'tail':F(1,4),'variance':1},'cantelli':{'tail':F(4,13),'variance':4},'walk-two':{'variance':2},'walk-biased':{'mean':3,'variance':F(9,2)}}
for m in data['models']:
 for key,val in expected.get(m['id'],{}).items():eq(m['result'][key],val)
bad=next(m for m in data['models']if m['id']=='psd-failure');assert any(f['snapshot']['state']['variance']<0 for f in bad['frames'])
eq(next(f for f in bad['frames']if f['snapshot']['state']['weight']==1)['snapshot']['state']['variance'],F(-3,2))
for n in range(1,8):
 vals=[sum(x==i+1 for i,x in enumerate(p))for p in permutations(range(1,n+1))];eq(sum(vals)/len(vals),1);eq(sum(x*x for x in vals)/len(vals)-1,0 if n==1 else 1);report['independentCases']+=1
for N in range(2,10):
 for K in range(N+1):
  for count in range(N+1):
   values=[sum(i<K for i in a)for a in combinations(range(N),count)];mu=sum(values)/len(values);var=sum((x-mu)**2 for x in values)/len(values);p=F(K,N);eq(var,count*p*(1-p)*F(N-count,N-1));report['independentCases']+=1
for steps in range(9):
 for p in[F(1,4),F(1,2),F(3,4)]:
  a=[dict(x=sum(path),p=math.prod(p if x==1 else 1-p for x in path))for path in product([-1,1],repeat=steps)];mu,m2,var=raw(a);eq(mu,steps*(2*p-1));eq(var,4*steps*p*(1-p));report['independentCases']+=1
x,y=S.symbols('x y',real=True);dens=2*x**3+2*y**3
integrate=lambda f:S.integrate(f,(x,0,1),(y,0,1))
eq(integrate(dens),1);eq(integrate(x*dens),S.Rational(13,20));eq(integrate(x*x*dens)-S.Rational(13,20)**2,S.Rational(31,400));eq(integrate(x*y*dens)-S.Rational(13,20)**2,S.Rational(-9,400))
stems=json.loads((B/'s_variance-questions.json').read_text(encoding='utf-8'));assert len(stems)==84 and len({q['id']for q in stems})==84
for q in stems:
 assert len(q['solution'].split())>=55,(q['id'],'insufficient reasoning')
 assert not any(ord(c)<32 and c not in'\n\t'for c in q['stem']+q['solution']),q['id']
 qs=q['stem']+q['solution']
 for m in re.finditer(r'\$([^$]+)\$',qs):
  assert not re.search(r'(?<![\\A-Za-z])(sqrt|mu|sigma|rho|int|sum|infty)(?![A-Za-z])',m[1]),(q['id'],m[1])
  assert not re.search(r'[A-Za-z](?:cdot|cap|mid|epsilon|sqrt|ge[0-9]|le[0-9])|(?:le|ge)sqrt|lambdamu',m[1]),(q['id'],'lost command boundary',m[1])
 eqs=[('uniform density2x variance',S.Rational(1,2)-S.Rational(2,3)**2,S.Rational(1,18)),('triangle covariance',S.Rational(1,4)-S.Rational(1,3)*S.Rational(2,3),S.Rational(1,36)),('adjacent heads count variance',3*S.Rational(3,16)+4*S.Rational(1,16),S.Rational(13,16)),('optimal weight risk',9-S.Rational(36,7),S.Rational(27,7)),('outside weight risk',2*S.Rational(5,4)**2-5*S.Rational(5,4)+4,S.Rational(7,8)),('pgf variance',S.Rational(11,4)-S.Rational(25,16),S.Rational(19,16)),('stream centered sum',2+5*(8-S.Rational(14,3)),S.Rational(56,3))]
for name,a,b in eqs:eq(a,b)
# Run the actual editable browser calculator against an independent rational
# oracle. Duplicate coordinates are deliberately retained in the input.
import subprocess,sys
cases=[]
for count in range(1,10):
 for offset in range(-4,5):
  for joint in [False,True]:
   xs=[max(-20,min(20,(i%3-1)*4+offset))for i in range(count)]
   ps=[F(i+1,count*(count+1)//2)for i in range(count)]
   points=[dict(x=x,p=float(p),**(dict(y=(i%2)*5-offset)if joint else{}))for i,(x,p)in enumerate(zip(xs,ps))]
   cases.append(dict(kind='joint'if joint else'moments',points=points,**({}if joint else dict(center=offset))))
node=r"""const lib=require('./dist/chapters/s_variance.js');let s='';process.stdin.on('data',c=>s+=c);process.stdin.on('end',()=>{const specs=JSON.parse(s);process.stdout.write(JSON.stringify(specs.map(spec=>({result:lib.evaluate(spec).result,circles:(lib.drawing(lib.evaluate(spec).states.at(-1)).match(/<circle /g)||[]).length}))));});"""
out=json.loads(subprocess.check_output(['node','-e',node],input=json.dumps(cases).encode(),cwd=R))
for spec,actual in zip(cases,out):
 a=spec['points'];mu,m2,v=raw(a);result=actual['result']
 if spec['kind']=='moments':
  for key,val in [('mean',mu),('second',m2),('variance',v),('squaredError',sum(F(str(p['p']))*(p['x']-spec['center'])**2 for p in a))]:eq(result[key],val)
 else:
  my,m2y,vy=raw([dict(x=p['y'],p=p['p'])for p in a]);cov=sum(F(str(p['p']))*(p['x']-mu)*(p['y']-my)for p in a)
  for key,val in [('meanX',mu),('meanY',my),('varX',v),('varY',vy),('covariance',cov)]:eq(result[key],val)
  assert actual['circles']==len({(p['x'],p['y'])for p in a if p['p']>0})
  if v==0 or vy==0:assert result['correlation']is None
  else:eq(result['correlation'],float(cov)/math.sqrt(float(v*vy)))
report['editableIndependentCases']=len(cases)
sys.path.insert(0,str(B/'exam-rewrite'))
from math_fences import delimiter_issues,closing_script_bases
maths=re.findall(r'<math\b.*?</math>',(R/'dist/chapters/s_variance.html').read_text(encoding='utf-8'),re.S)
for mathml in maths:
 root=ET.fromstring(mathml);assert not delimiter_issues(root),(root.attrib,delimiter_issues(root));assert not closing_script_bases(root)
report['staticMathFenceChecks']=len(maths)
report.update(status='passed',storedModels=len(data['models']),questionEntries=87,originalEntries=84,finalRules=80,independentMethods='Direct enumeration of permutations, subsets and walk paths; raw moments versus centered sums; independent symbolic integrations and quadratic forms; finite boundary checks.',limitations='Finite tests and selected symbolic derivations are not a proof of universal correctness. Browser behavior and typography are audited separately.')
(E/'mathematics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps(report,indent=2))
