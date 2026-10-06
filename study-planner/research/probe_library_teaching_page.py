"""Measure every redesigned model, then exercise the actual chapter controls."""
import json,os,time,subprocess,threading,tempfile,base64
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'library-decision-qa';OUT.mkdir(exist_ok=True);A=R/'research/library-animation-redesign'
class Handler(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=OUT/f'edge-{os.getpid()}';proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
report=dict(state='in_progress',models=[],chapters=[],controls={},runtimeErrors=[])
try:
 active=profile/'DevToolsActivePort'
 for _ in range(150):
  if active.exists():break
  time.sleep(.1)
 port=int(active.read_text().splitlines()[0]);page=next(p for p in requests.get(f'http://127.0.0.1:{port}/json').json() if p['type']=='page');ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=120);seq=0
 def cdp(method,params=None):
  global seq
  seq+=1;ws.send(json.dumps(dict(id=seq,method=method,params=params or {})))
  while True:
   r=json.loads(ws.recv())
   if r.get('id')==seq:
    if 'error' in r:raise RuntimeError(r)
    return r.get('result',{})
 def js(code):
  r=cdp('Runtime.evaluate',dict(expression=code,returnByValue=True,awaitPromise=True))
  if 'exceptionDetails' in r:raise RuntimeError(r['exceptionDetails'].get('exception',{}).get('description',r))
  return r.get('result',{}).get('value')
 def navigate(topic):
  cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/{topic}.html'));time.sleep(.3);js('document.fonts.ready')
 def shot(name):
  (OUT/name).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.error?.stack||e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"});cdp('Emulation.setDeviceMetricsOverride',dict(width=1280,height=1000,deviceScaleFactor=1,mobile=False));navigate('g_gates')
 js('Promise.all([...document.querySelectorAll(".concept-animation")].map(ConceptAnimations.ready))')
 js('''(async()=>{window.reviewData=await(await fetch('concept-animations.json')).json();window.reviewHost=document.createElement('section');reviewHost.className='concept-animation';document.querySelector('main').prepend(reviewHost);window.reviewPlayer=ConceptAnimations.mount(reviewHost,[reviewData.scenes.insertion]);})()''')

 js('Promise.all([...document.querySelectorAll("[data-problem-visual]")].map(ProblemVisuals.ready))')
 time.sleep(1)
 print(js('__errors'))

finally:
 (A/'probe-console.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
 proc.terminate();server.shutdown()
