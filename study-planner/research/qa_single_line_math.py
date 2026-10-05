"""Actual-browser regression for one-line equations in every chapter."""
import base64,json,os,subprocess,tempfile,threading,time,re,hashlib
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import requests,websocket,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'single-line-math-qa';OUT.mkdir(exist_ok=True)
baseline='30abb8302e74145914312d954ad8959311349e26'
# Mathematical values, scripts, matrices and question inventory must remain identical.
retained=[]
for p in sorted((ROOT/'dist/chapters').glob('*.html')):
 old=subprocess.check_output(['git','show',baseline+':dist/chapters/'+p.name],cwd=ROOT).decode('utf-8');new=p.read_text(encoding='utf-8')
 a=re.findall(r'<math\b[\s\S]*?</math>',old);b=re.findall(r'<math\b[\s\S]*?</math>',new);assert len(a)==len(b),p.name
 for x,y in zip(a,b):
  X=ET.fromstring(x);Y=ET.fromstring(y);assert ''.join(X.itertext())==''.join(Y.itertext())
  for tag in ['msub','msup','msubsup','mfrac','msqrt','mover','munder','munderover']:
   assert [ET.tostring(z) for z in X.iter() if z.tag.split('}')[-1]==tag]==[ET.tostring(z) for z in Y.iter() if z.tag.split('}')[-1]==tag]
  actual=lambda T:[ET.tostring(z) for z in T.iter() if z.tag.split('}')[-1]=='mtable' and not (z.attrib.get('columnalign')=='left' and z.attrib.get('rowspacing') in ['.5em','.55em'])]
  assert actual(X)==actual(Y),'Actual matrix/case table changed'
 assert old.count('class="exam-question"')==new.count('class="exam-question"')
 retained.append(dict(chapter=p.stem,formulas=len(a),questions=old.count('class="exam-question"')))
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
 def do_GET(self):
  if self.path.startswith('/_baseline/'):
   relative=self.path.split('?',1)[0][len('/_baseline/'):]
   try: data=subprocess.check_output(['git','show',baseline+':dist/'+relative],cwd=ROOT,stderr=subprocess.DEVNULL)
   except subprocess.CalledProcessError:self.send_error(404);return
   self.send_response(200);self.send_header('Content-Type',self.guess_type(relative));self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data);return
  super().do_GET()
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=OUT/f'edge-{os.getpid()}-{time.time_ns()}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
events=[];seq=0
try:
 for _ in range(100):
  try:
   active=(profile/'DevToolsActivePort').read_text().splitlines()
   if len(active)>=2:break
  except OSError:pass
  time.sleep(.1)
 port=int(active[0]);page=next(x for x in requests.get(f'http://127.0.0.1:{port}/json',timeout=5).json() if x['type']=='page');ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=30)
 def cdp(method,params=None):
  global seq
  seq+=1;ws.send(json.dumps(dict(id=seq,method=method,params=params or {})))
  while True:
   r=json.loads(ws.recv())
   if r.get('id')==seq:
    assert 'error' not in r,r
    return r.get('result',{})
   events.append(r)
 def js(expr):
  r=cdp('Runtime.evaluate',dict(expression=expr,returnByValue=True,awaitPromise=True));assert 'exceptionDetails' not in r,r;return r['result'].get('value')
 def capture(selector,name):
  b=js('(async()=>{const e=document.querySelector('+json.dumps(selector)+');document.documentElement.style.scrollBehavior="auto";e.scrollIntoView({block:"center",behavior:"instant"});await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));const b=e.getBoundingClientRect();return {x:b.x+scrollX,y:b.y+scrollY,width:b.width,height:b.height};})()')
  data=cdp('Page.captureScreenshot',dict(format='png',captureBeyondViewport=True,clip=dict(**b,scale=1)))['data'];(OUT/name).write_bytes(base64.b64decode(data))
  if name=='d_pigeonhole-390.png':
   data=cdp('Page.captureScreenshot',dict(format='png',captureBeyondViewport=False))['data'];(OUT/'mobile-viewport-final.png').write_bytes(base64.b64decode(data))
 def navigate(name,prefix=''):
  cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/{prefix}chapters/{name}.html'))
  for _ in range(100):
   if js('document.readyState==="complete" && !!window.MathLayout'):break
   time.sleep(.05)
  js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true);MathLayout.layout()');time.sleep(.06)
 cdp('Page.enable');cdp('Runtime.enable');cdp('Log.enable')
 def runtime_errors():
  return [r['params']['exceptionDetails'] for r in events if r.get('method')=='Runtime.exceptionThrown']
 # Reproduce existing unrelated laboratory errors using the exact pre-edit source.
 for name in ['g_gates','l_vectors']:navigate(name,'_baseline/')
 preexisting=runtime_errors()
 error_key=lambda e:(e.get('exception',{}).get('description','').split('\n')[0],e.get('url','').split('/')[-1],e.get('lineNumber'))
 preexisting_keys={error_key(e) for e in preexisting}
 events.clear()
 rows=[];scrolls=[];before=[]
 query='''(()=>{const math=[...document.querySelectorAll('math[display="block"]')];return {formulas:math.length,generatedWraps:document.querySelectorAll('math mtable[columnalign="left"][rowspacing=".5em"],math mtable[columnalign="left"][rowspacing=".55em"]').length,semanticWraps:document.querySelectorAll('math[data-semantic-wrap]').length,bodyWidth:document.body.scrollWidth,documentWidth:document.documentElement.scrollWidth,viewport:innerWidth,font:document.fonts.check("18px 'STIX Two Math'"),badSingle:[...document.querySelectorAll('.formula-block>math')].filter(x=>!x.querySelector('mtable') && [...x.firstElementChild.children].filter(c=>c.getBoundingClientRect().width>0&&c.localName==='mo'&&c.textContent==='=').map(c=>c.getBoundingClientRect().y+c.getBoundingClientRect().height/2).some((y,_,a)=>Math.abs(y-a[0])>3)).map(x=>x.getAttribute('aria-label'))};})()'''
 for entry in retained:
  name=entry['chapter'];navigate(name)
  for w in [1280,390]:
   cdp('Emulation.setDeviceMetricsOverride',dict(width=w,height=950,deviceScaleFactor=1,mobile=False));js('MathLayout.layout()');time.sleep(.03)
   z=js(query);z.update(chapter=name,width=w);assert z['generatedWraps']==0 and z['semanticWraps']==0 and z['font'],z
   assert z['bodyWidth']<=w+2 and z['documentWidth']<=w+2,z
   assert not z['badSingle'],z
   rows.append(z)
   if name in ['d_counting','d_inclusion','d_pigeonhole']:
    scroll=js('''(()=>{const boxes=[...document.querySelectorAll('.formula-block')].filter(x=>x.scrollWidth>x.clientWidth+2);return boxes.map(x=>{x.scrollLeft=150;return {moved:x.scrollLeft,viewport:x.clientWidth,complete:x.scrollWidth,tokens:x.textContent.trim().slice(0,110)};});})()''');assert all(x['moved']>0 for x in scroll),scroll;scrolls.append(dict(chapter=name,width=w,cases=scroll))
    # Pick the longest actual display to verify before/after aesthetics.
    js('(()=>{document.querySelectorAll("#math-qa-target").forEach(x=>x.removeAttribute("id"));const a=[...document.querySelectorAll(".lesson>.formula-block")].filter(x=>x.querySelector("math"));if(!a.length)return;const e=a.sort((x,y)=>y.querySelector("math").getBoundingClientRect().width-x.querySelector("math").getBoundingClientRect().width)[0];e.id="math-qa-target";e.scrollLeft=0;})()')
    if js('!!document.querySelector("#math-qa-target")'):capture('#math-qa-target',name+'-'+str(w)+'.png')
  print(name+' passed',flush=True)
 # Explicitly compare an originally wrapped formula using the original HTML and script.
 name='d_pigeonhole';navigate(name);cdp('Emulation.setDeviceMetricsOverride',dict(width=1280,height=950,deviceScaleFactor=1,mobile=False))
 old=subprocess.check_output(['git','show',baseline+':dist/chapters/d_pigeonhole.html'],cwd=ROOT).decode('utf-8');oldMath=next(x for x in re.findall(r'<math\b[\s\S]*?</math>',old) if 'columnalign="left"' in x and x.count('<mtr>')>1)
 js('(()=>{const x=document.createElement("div");x.id="before-after-math";x.className="formula-block";x.innerHTML='+json.dumps(oldMath)+';document.querySelector(".lesson").prepend(x);})()');capture('#before-after-math','before.png');js('MathLayout.layout()');capture('#before-after-math','after.png')
 assert js('document.querySelector("#before-after-math").querySelectorAll("mtable").length')==0
 # Print still preserves the complete equation and genuine matrix rows.
 js('document.querySelector("#before-after-math").remove()');cdp('Emulation.setEmulatedMedia',dict(media='print'));js('dispatchEvent(new Event("beforeprint"))');pr=js(query);assert pr['generatedWraps']==0 and pr['semanticWraps']==0;cdp('Emulation.setEmulatedMedia',dict(media='screen'))
 errors=runtime_errors();new_errors=[e for e in errors if error_key(e) not in preexisting_keys]
 assert not new_errors,new_errors
 report=dict(state='passed',chapters=len(retained),questionCount=sum(x['questions'] for x in retained),retainedFormulas=sum(x['formulas'] for x in retained),retained=retained,views=rows,scrollTests=scrolls,print=pr,newRuntimeErrors=new_errors,preexistingRuntimeErrors=preexisting,preexistingBaseline=baseline,screenshots=str(OUT),scope='Actual desktop/mobile checks of all existing chapters; all mathematical tokens, scripts and actual matrices/cases preserved. Two unrelated lab errors reproduced on the exact pre-edit baseline are reported separately.')
 (ROOT/'research/single-line-math-browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:report[k] for k in ['state','chapters','questionCount','retainedFormulas','screenshots']}))
finally:
 try:cdp('Browser.close')
 except Exception:pass
 proc.terminate();server.shutdown()
