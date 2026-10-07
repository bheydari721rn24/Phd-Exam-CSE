"""Whole-library content retention and real-browser fence regression."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,threading,time,re,sys,collections,xml.etree.ElementTree as ET
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=R/'research/delimiter-evidence';OUT.mkdir(exist_ok=True)
sys.path.insert(0,str(R/'research/exam-rewrite'))
from math_fences import signature,closing_script_bases,delimiter_issues
import mathml
BASE='188b2be087fa37a99d2e5da8a3ad672629dfbd74';PAT=re.compile(r'<math\b[\s\S]*?</math>')
report={'status':'in_progress','chapters':[],'baseline':BASE,'formulaCount':0,'problemCount':0}
for p in sorted((R/'dist/chapters').glob('*.html')):
 old=subprocess.check_output(['git','show',BASE+':dist/chapters/'+p.name],cwd=R).decode('utf-8');new=p.read_text(encoding='utf-8')
 a=PAT.findall(old);b=PAT.findall(new);assert len(a)==len(b),p.name
 for x,y in zip(a,b):
  X=ET.fromstring(x);Y=ET.fromstring(y)
  assert ''.join(X.itertext())==''.join(Y.itertext()),p.name
  assert signature(X)==signature(Y),p.name
  assert X.attrib==Y.attrib,p.name
  assert not closing_script_bases(Y),(p.name,Y.attrib)
  assert not delimiter_issues(Y),(p.name,Y.attrib)
 clean=lambda s:re.sub(r'math-layout\.js(?:\?v=\d+)?','math-layout.js',PAT.sub('MATH',s))
 assert clean(old)==clean(new),p.name
 count=new.count('class="exam-question"');report['formulaCount']+=len(a);report['problemCount']+=count
 report['chapters'].append({'id':p.stem,'formulas':len(a),'questions':count})
assert len(report['chapters'])==41 and report['problemCount']==2593
def retained_json(old,new):
 if isinstance(old,str):
  a=PAT.findall(old);b=PAT.findall(new);assert len(a)==len(b)
  assert PAT.sub('MATH',old)==PAT.sub('MATH',new)
  for x,y in zip(a,b):
   X=ET.fromstring(x);Y=ET.fromstring(y)
   assert ''.join(X.itertext())==''.join(Y.itertext()) and signature(X)==signature(Y)
   assert not closing_script_bases(Y) and not delimiter_issues(Y)
  return len(a)
 if isinstance(old,list):
  assert len(old)==len(new);return sum(retained_json(a,b) for a,b in zip(old,new))
 if isinstance(old,dict):
  assert old.keys()==new.keys();return sum(retained_json(old[k],new[k]) for k in old)
 assert old==new;return 0
report['cachedFormulaCount']=0
for p in sorted((R/'dist/chapters').glob('*.json')):
 old=json.loads(subprocess.check_output(['git','show',BASE+':dist/chapters/'+p.name],cwd=R).decode('utf-8'))
 report['cachedFormulaCount']+=retained_json(old,json.loads(p.read_text(encoding='utf-8')))
examples=[r'(x+y)^2',r'((x+y)^2)^3',r'(\frac{x+y}{x-y})^2',r'\sum_{i=1}^n(1-p_i)^m',r'E[(X-\mu)^2]',r'(a,b]',r'[a,b)',r'\begin{pmatrix}a&b\\c&d\end{pmatrix}^2',r'\{x\in\mathbb R\mid x>0\}']
for formula in examples:
 root=ET.fromstring(mathml.render(formula));assert not closing_script_bases(root) and not delimiter_issues(root)
for formula in [r'(x+y',r'E[X',r'x+y)',r'\langle x,y)',r'(x+y)^2)']:
 try:mathml.render(formula)
 except (ValueError,AssertionError):pass
 else:raise AssertionError('Malformed future formula accepted: '+formula)
report['rendererExamples']=len(examples);report['rejectedMalformedExamples']=5
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=Path(tempfile.gettempdir())/f'delimiter-qa-{os.getpid()}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0
try:
 for _ in range(100):
  if (profile/'DevToolsActivePort').exists():break
  time.sleep(.1)
 port=int((profile/'DevToolsActivePort').read_text().splitlines()[0]);page=next(p for p in requests.get(f'http://127.0.0.1:{port}/json').json() if p['type']=='page');ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=120)
 def cdp(method,params=None):
  global seq
  seq+=1;ws.send(json.dumps(dict(id=seq,method=method,params=params or {})))
  while True:
   r=json.loads(ws.recv())
   if r.get('id')==seq:
    assert 'error' not in r,r
    return r.get('result',{})
 def js(code):
  r=cdp('Runtime.evaluate',dict(expression=code,returnByValue=True,awaitPromise=True));assert 'exceptionDetails' not in r,r;return r.get('result',{}).get('value')
 def navigate(name):
  cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/{name}.html'))
  for _ in range(100):
   if js('document.readyState==="complete"&&!!window.MathLayout'):break
   time.sleep(.05)
  js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true);MathLayout.layout()')
 def capture(name,expression):
  js('window.target='+expression+';target.scrollIntoView({block:"center",behavior:"instant"})');js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
  (OUT/name).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
 cdp('Page.enable');report['browser']=[]
 query='''(()=>{const issues=[],math=[...document.querySelectorAll('math')];let pairs=0;for(const m of math){for(const s of m.querySelectorAll('msup,msub,msubsup,mover,munder,munderover')){const b=s.firstElementChild;if(b?.localName==='mo'&&')]}⌉⌋⟩'.includes(b.textContent))issues.push({kind:'closing-glyph script',tex:m.getAttribute('aria-label')});}for(const r of m.querySelectorAll('mrow')){const a=r.firstElementChild,b=r.lastElementChild;if(a?.localName!=='mo'||b?.localName!=='mo'||a===b)continue;const opening=a.textContent,closing=b.textContent;if(!'([{⌈⌊⟨'.includes(opening)||!')]}⌉⌋⟩'.includes(closing))continue;const A=a.getBoundingClientRect(),B=b.getBoundingClientRect();if(!A.height&&!B.height)continue;pairs++;if(A.height<1||B.height<1||A.width<1||B.width<1)issues.push({kind:'invisible delimiter',opening,closing,tex:m.getAttribute('aria-label')});if(')]}⌉⌋⟩'['([{⌈⌊⟨'.indexOf(opening)]===closing&&Math.abs(A.height-B.height)>2)issues.push({kind:'unequal paired height',opening,closing,heights:[A.height,B.height],tex:m.getAttribute('aria-label')});}}return {width:innerWidth,formulas:math.length,pairs,issues,stix:document.fonts.check("18px 'STIX Two Math'"),overflow:document.documentElement.scrollWidth>innerWidth+2};})()'''
 for entry in report['chapters']:
  navigate(entry['id'])
  for width in [1280,390]:
   cdp('Emulation.setDeviceMetricsOverride',dict(width=width,height=1050,deviceScaleFactor=1,mobile=False));js('MathLayout.layout()')
   result=js(query);result['chapter']=entry['id'];report['browser'].append(result)
   (OUT/'qa.json').write_text(json.dumps(report,indent=2)+'\n')
   assert not result['issues'] and result['stix'] and not result['overflow'],result
  print(entry['id']+' passed',flush=True)
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));navigate('s_expectation')
 capture('after-occupancy.png','[...document.querySelectorAll("math")].find(m=>m.getAttribute("aria-label")==="n[1-(1-1/n)^m]")')
 capture('after-loss.png','[...document.querySelectorAll("math")].find(m=>m.getAttribute("aria-label")?.includes("(X-\\\\mu)^2"))')
 # Check dynamic old-style incoming formulas and observer normalization.
 js('window.probe=document.createElement("p");probe.id="delimiter-probe";probe.innerHTML=\'<math><mrow><mo>(</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mo>)</mo><mn>2</mn></msup></mrow></math>\';document.querySelector(".lesson").append(probe)')
 js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
 assert js('probe.querySelector("msup").firstElementChild.localName==="mrow"')
 capture('after-fraction.png','probe');report['dynamicInsertion']=True
 js('window.before=probe.innerHTML;MathLayout.layout();MathLayout.layout()');assert js('before===probe.innerHTML');report['runtimeIdempotence']=True
 cdp('Emulation.setEmulatedMedia',{'media':'print'});assert not js(query)['issues'];report['printFenceGeometry']=True
 cdp('Emulation.setEmulatedMedia',{'media':'screen'});js('probe.remove()')
 cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=1050,deviceScaleFactor=1,mobile=False));capture('after-mobile.png','[...document.querySelectorAll("math")].find(m=>m.getAttribute("aria-label")==="n[1-(1-1/n)^m]")')
finally:
 proc.terminate();server.shutdown()
report['status']='passed';(OUT/'qa.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['browser','chapters']},indent=2))
