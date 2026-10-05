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
 # A dedicated test host mounts every model, irrespective of chapter lazy loading.
 js('(async()=>{window.reviewData=await (await fetch("concept-animations.json")).json();window.reviewHost=document.createElement("section");reviewHost.className="concept-animation";document.querySelector("main").prepend(reviewHost);window.reviewPlayer=ConceptAnimations.mount(reviewHost,[reviewData.scenes["insertion"]]);})()')


 result=js('(()=>{const p=reviewPlayer,rows=[];for(const scene of Object.values(reviewData.scenes)){p.pause();p.scene=scene;let checked=0;const bad=[];for(let i=1;i<scene.frames.length;i++){const f=scene.frames[i],prev=new Map(scene.frames[i-1].nodes.map(n=>[n.id,n]));if(!f.nodes.some(n=>prev.has(n.id)&&(prev.get(n.id).x!==n.x||prev.get(n.id).y!==n.y)))continue;p.index=i;for(const fraction of [.25,.5,.75]){const positions=new Map(f.nodes.map(n=>{const a=prev.get(n.id)||n;let x=a.x+(n.x-a.x)*fraction,y=a.y+(n.y-a.y)*fraction;if(f.motion?.kind==="rotation"&&n.geometry&&prev.has(n.id)){const {cx,cy,angle}=f.motion,c=Math.cos(angle*fraction),s=Math.sin(angle*fraction);x=cx+(a.x-cx)*c-(a.y-cy)*s;y=cy+(a.x-cx)*s+(a.y-cy)*c;}return [n.id,ConceptAnimations.motion(scene,n,a,fraction,{x,y})];}));p.draw(f.nodes,f.edges||[],positions);checked++;bad.push(...DiagramLayout.audit(p.canvas).map(x=>({...x,frame:i,fraction})));}}rows.push({id:scene.id,samples:checked,bad});}return rows;})()')
 report=dict(state='passed' if not any(r['bad'] for r in result) else 'failed',models=result,samples=sum(r['samples'] for r in result))
 (ROOT/'research/library-visual-question-review/moving-browser.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps(dict(state=report['state'],samples=report['samples'],bad=sum(len(r['bad']) for r in result),examples=[r for r in result if r['bad']][:10])))
finally:
 proc.terminate();server.shutdown()
