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

 report=dict(state='in_progress',scenes=[],chapters=[],errors=[]);previews={}
 for id,scene in json.loads((ROOT/'dist/chapters/concept-animations.json').read_text())['scenes'].items():
  row=js('(()=>{const p=reviewPlayer;p.pause();p.scene=reviewData.scenes['+json.dumps(id)+'];const bad=[];for(let i=0;i<p.scene.frames.length;i++){p.show(i,false);bad.push(...DiagramLayout.audit(p.canvas).map(x=>({...x,frame:i})));}return {id:p.scene.id,frames:p.scene.frames.length,bad};})()')
  report['scenes'].append(row)
  previews[id]=js('(()=>{reviewPlayer.show(0,false);return reviewPlayer.canvas.outerHTML;})()')
 # All precomputed checkpoint diagrams are also rendered and measured.
 for topic in ['d_counting','d_inclusion','d_pigeonhole','a_arrays']:
  row=js('(async()=>{const data=await(await fetch('+json.dumps(topic+'-models.json')+')).json(),h=document.createElement("div");document.querySelector("main").prepend(h);const rows=[];for(const m of data.models){const bad=[];for(let i=0;i<m.frames.length;i++){h.innerHTML=m.frames[i].svg;const svg=h.querySelector("svg");if('+json.dumps(topic)+'!=="a_arrays")DiagramLayout.finish(svg);bad.push(...DiagramLayout.audit(svg).map(x=>({...x,frame:i})));}rows.push({id:m.id,frames:m.frames.length,bad});}h.remove();return rows;})()')
  report['scenes'] += [dict(topicId=topic,**r) for r in row]
 report['state']='passed' if not any(r['bad'] for r in report['scenes']) else 'failed'
 (ROOT/'research/library-visual-question-review/animation-browser.json').write_text(json.dumps(report,indent=2)+'\n')
 (ROOT/'research/library-visual-question-review/scene-previews.json').write_text(json.dumps(previews,separators=(',',':'))+'\n')
 print(json.dumps(dict(state=report['state'],models=len(report['scenes']),frames=sum(r['frames'] for r in report['scenes']),bad=sum(len(r['bad']) for r in report['scenes']),examples=[r for r in report['scenes'] if r['bad']][:8])))
finally:
 proc.terminate();server.shutdown()
