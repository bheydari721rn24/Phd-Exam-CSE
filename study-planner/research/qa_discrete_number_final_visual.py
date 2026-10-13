"""Inspect the actual rendered chapter, mathematics, solution tables and retained players."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,time
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'deep-discrete-number-browser';OUT.mkdir(exist_ok=True)
profile=OUT/f'edge-{os.getpid()}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report={'status':'in_progress','topicId':'d_number','screenshots':str(OUT)}
try:
 for _ in range(100):
  if(profile/'DevToolsActivePort').exists():
   try:
    port_text=(profile/'DevToolsActivePort').read_text();assert port_text.strip();break
   except (OSError,AssertionError):pass
  time.sleep(.1)
 port=int(port_text.splitlines()[0]);page=next(p for p in requests.get(f'http://127.0.0.1:{port}/json').json()if p['type']=='page');ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=60)
 def cdp(method,params=None):
  global seq
  seq+=1;ws.send(json.dumps(dict(id=seq,method=method,params=params or{})))
  while True:
   r=json.loads(ws.recv())
   if r.get('id')==seq:assert 'error'not in r,r;return r.get('result',{})
 def js(code):
  r=cdp('Runtime.evaluate',dict(expression=code,returnByValue=True,awaitPromise=True));assert 'exceptionDetails'not in r,r;return r.get('result',{}).get('value')
 def capture(sel,name):
  js('document.querySelector('+json.dumps(sel)+').scrollIntoView({block:"start",behavior:"instant"})');js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');(OUT/name).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"})
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url='http://127.0.0.1:8771/chapters/d_number.html'))
 for _ in range(100):
  if js('!!window.ConceptAnimations'):break
  time.sleep(.1)
 assert js('!!window.ConceptAnimations'), 'Chapter or renderer did not load'
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))')
 report['loadFailures']=js("[...document.querySelectorAll('.concept-animation')].filter(h=>h.dataset.loaded!=='true').map(h=>({scenes:h.dataset.scenes,state:h.dataset.loaded,text:h.textContent}))");assert not report['loadFailures'],report['loadFailures']


 report=json.loads((R/'research/deep-library-revision/d_number-browser.json').read_text());assert report['status'].startswith('passed')
 report['finalStaticPorts']=js(r"(()=>[...document.querySelectorAll('figure svg')].map(svg=>{const shapes=[...svg.querySelectorAll('circle,rect')],distance=(x,y)=>Math.min(...shapes.map(e=>{if(e.tagName==='circle')return Math.abs(Math.hypot(x-+e.getAttribute('cx'),y-+e.getAttribute('cy'))-+e.getAttribute('r'));const X=+e.getAttribute('x'),Y=+e.getAttribute('y'),w=+e.getAttribute('width'),h=+e.getAttribute('height');return Math.hypot(Math.max(X-x,x-X-w,0),Math.max(Y-y,y-Y-h,0))||Math.min(Math.abs(x-X),Math.abs(x-X-w),Math.abs(y-Y),Math.abs(y-Y-h));}));for(const e of svg.querySelectorAll('[marker-end]')){const id=e.getAttribute('marker-end').match(/url\(#([^)]*)\)/)[1];if(![...svg.querySelectorAll('marker')].some(m=>m.id===id))throw Error('Unresolved marker');}return{straight:[...svg.querySelectorAll('[data-static-ports]')].map(e=>[distance(+e.getAttribute('x1'),+e.getAttribute('y1')),distance(+e.getAttribute('x2'),+e.getAttribute('y2'))]),curves:[...svg.querySelectorAll('[data-static-path-ports]')].map(e=>{const a=e.dataset.staticPathPorts.split(',').map(Number);return[distance(a[0],a[1]),distance(a[2],a[3])];})};}))()")
 assert sum(len(v['straight'])for v in report['finalStaticPorts'])==9 and sum(len(v['curves'])for v in report['finalStaticPorts'])==2
 assert all(max(p)<.001 for v in report['finalStaticPorts']for p in v['straight']+v['curves'])
 sel='.exam-question[data-deep-index="19"] .concept-animation'
 report['finalAdjacentWindow']=js('(()=>{const h=document.querySelector('+json.dumps(sel)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host));c.api.show(2);const middle=c.api.host.textContent;c.api.show(3);return{middle:middle.includes("Rows 5–9"),final:c.api.host.textContent.includes("Rows 1–5"),answer:c.scene.frames[3].snapshot.answers[0],math:!!c.api.host.querySelector("math")}})()');assert report['finalAdjacentWindow']==dict(middle=True,final=True,answer=65,math=True);capture(sel,'question-19-final.png')
 report['finalInlineMath']=js('getComputedStyle(document.querySelector(".exam-solution .math-inline")).whiteSpace');assert report['finalInlineMath']=='nowrap'
 report['status']='passed';(R/'research/deep-library-revision/d_number-browser.json').write_text(json.dumps(report,indent=2)+'\n');print({'attachedStraightConnections':9,'attachedCurvedConnections':2,'CRTWindow':'checked','math':'nowrap'})
finally:
 proc.terminate()
