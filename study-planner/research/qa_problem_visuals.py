"""Render all saved states, retain previews and record actual SVG contracts."""
import json,os,time,subprocess,threading,tempfile,base64,sys
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
import requests,websocket
ROOT=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'subject-visual-review';OUT.mkdir(exist_ok=True)
class Handler(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(ROOT/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=OUT/f'edge-{os.getpid()}';proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
rows=[];errors=[]
try:
 active=profile/'DevToolsActivePort'
 for _ in range(150):
  if active.exists():break
  time.sleep(.1)
 port=int(active.read_text().splitlines()[0]);page=next(p for p in requests.get(f'http://127.0.0.1:{port}/json').json() if p['type']=='page');ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=60);seq=0
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
 cdp('Page.enable');cdp('Emulation.setDeviceMetricsOverride',dict(width=1280,height=1000,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/g_gates.html'));time.sleep(.8)
 js('document.fonts.ready');js('Promise.all([...document.querySelectorAll(".concept-animation")].map(ConceptAnimations.ready))')

 js('(async()=>{window.problemModels=await (await fetch("problem-visual-models.json")).json();window.problemTest=document.createElement("div");problemTest.className="problem-stage";document.querySelector("main").prepend(problemTest);})()')
 report=dict(state='in_progress',models=[]);previews={}
 for id,model in json.loads((ROOT/'dist/chapters/problem-visual-models.json').read_text()).items():
  row=js('(()=>{const model=problemModels['+json.dumps(id)+'],bad=[];for(let i=0;i<model.frames.length;i++){problemTest.innerHTML=model.frames[i].html;for(const svg of problemTest.querySelectorAll("svg")){DiagramLayout.finish(svg,{arrows:false});bad.push(...DiagramLayout.audit(svg).map(x=>({...x,frame:i})));}}return {id:'+json.dumps(id)+',kind:model.kind,frames:model.frames.length,bad};})()')
  report['models'].append(row)
  previews[id]=js('(()=>{problemTest.innerHTML=problemModels['+json.dumps(id)+'].frames[0].html;for(const s of problemTest.querySelectorAll("svg"))DiagramLayout.finish(s,{arrows:false});return problemTest.innerHTML;})()')
 report['state']='passed' if not any(r['bad'] for r in report['models']) else 'failed'
 (ROOT/'research/library-visual-question-review/problem-browser.json').write_text(json.dumps(report,indent=2)+'\n')
 (ROOT/'research/library-visual-question-review/problem-previews.json').write_text(json.dumps(previews,separators=(',',':'))+'\n')
 print(json.dumps(dict(state=report['state'],models=len(report['models']),frames=sum(r['frames'] for r in report['models']),bad=sum(len(r['bad']) for r in report['models']),examples=[r for r in report['models'] if r['bad']][:12])))
finally:
 proc.terminate();server.shutdown()
