"""Actual portable Edge inspection of every model, controls and exact explorer."""
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import base64,json,os,subprocess,tempfile,threading,time,uuid
import requests,websocket
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1];E=R/'research/deep-library-revision/l_gauss-erratum-evidence';E.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=Path(tempfile.gettempdir())/('gauss-erratum-qa-'+uuid.uuid4().hex);proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL);seq=0;report={}
try:
 for _ in range(150):
  try:
   port=int((profile/'DevToolsActivePort').read_text().splitlines()[0]);break
  except (OSError,ValueError,IndexError):time.sleep(.1)
 pg=next(p for p in requests.get(f'http://127.0.0.1:{port}/json').json()if p['type']=='page');ws=websocket.create_connection(pg['webSocketDebuggerUrl'],timeout=60)
 def cdp(method,params=None):
  global seq
  seq+=1;ws.send(json.dumps({'id':seq,'method':method,'params':params or{}}))
  while True:
   r=json.loads(ws.recv())
   if r.get('id')==seq:assert'error'not in r,r;return r.get('result',{})
 def js(code):
  r=cdp('Runtime.evaluate',{'expression':code,'returnByValue':True,'awaitPromise':True});assert'exceptionDetails'not in r,r;return r.get('result',{}).get('value')
 def capture(sel,name):
  js('document.querySelector('+json.dumps(sel)+').scrollIntoView({block:"center",behavior:"instant"})');js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');(E/name).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"});cdp('Emulation.setDeviceMetricsOverride',{'width':1360,'height':1000,'deviceScaleFactor':1,'mobile':False});url=f'http://127.0.0.1:{server.server_port}/chapters/l_gauss.html';cdp('Page.navigate',{'url':url})
 for _ in range(150):
  if js('location.href==='+json.dumps(url)+'&&document.readyState==="complete"&&!!document.querySelector(".gauss-column-erratum")'):break
  time.sleep(.1)
 js('document.fonts.ready');js("document.querySelector('[data-source-id=\"LG56\"] .exam-solution').open=true")
 report['figure']=js('''(()=>{const s=document.querySelector('.gauss-column-erratum svg');return{title:s.getAttribute('aria-label'),texts:[...s.querySelectorAll('text')].map(t=>({s:t.textContent,x:t.getBBox().x,end:t.getBBox().x+t.getBBox().width})),polygons:s.querySelectorAll('polygon').length};})()''')
 assert report['figure']['polygons']==2 and all(x['x']>=3 and x['end']<=757 for x in report['figure']['texts'])
 js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))')
 report['matchedSceneFrames']=js('''(()=>{const out=[];for(const p of ConceptAnimations.players){for(const scene of p.scenes){p.scene=scene;p.show(0);for(let k=0;k<scene.frames.length;k++){p.api.show(k);out.push({id:scene.id,k,issues:DiagramLayout.audit(p.host.querySelector('svg'))});}}p.show(0);}return out;})()''')
 assert all(not x['issues']for x in report['matchedSceneFrames'])
 report['questionModels']=js('''[...document.querySelectorAll('.exam-question')].filter(q=>q.querySelector('.concept-animation')).map(q=>({id:q.dataset.sourceId,scenes:q.querySelector('.concept-animation').dataset.scenes}))''');assert len(report['questionModels'])==11
 report['playback']=js('''(async()=>{const out=[];for(const p of ConceptAnimations.players.slice(0,2)){p.host.scrollIntoView({block:'center',behavior:'instant'});await new Promise(r=>setTimeout(r,250));p.buttons.reset.click();p.buttons.play.click();await new Promise(r=>setTimeout(r,2300));out.push({id:p.scene.id,moved:p.api.index>0});p.pause();}return out;})()''');assert all(x['moved']for x in report['playback'])
 report['widths']=[]
 for width in[390,768,1360]:
  cdp('Emulation.setDeviceMetricsOverride',{'width':width,'height':1000,'deviceScaleFactor':1,'mobile':False});v=js('({width:innerWidth,scroll:document.documentElement.scrollWidth})');report['widths'].append(v);assert v['scroll']<=width
 capture('.gauss-column-erratum','distinct-column-spaces.png');report['errors']=js('__errors');assert not report['errors'];report['status']='passed_targeted_gauss_erratum_browser_checks'

finally:
 server.shutdown();server.server_close()
 try:cdp('Browser.close')
 except Exception:pass
 proc.terminate()
 try:proc.wait(timeout=10)
 except subprocess.TimeoutExpired:proc.kill()
 (E/'browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print({k:v for k,v in report.items()if k not in ['frames','editableCases','controls']})
