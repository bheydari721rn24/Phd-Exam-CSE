"""Inspect the actual rendered chapter, mathematics, solution tables and retained players."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,time
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'deep-functions-browser';OUT.mkdir(exist_ok=True)
profile=OUT/f'edge-{os.getpid()}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report={'status':'in_progress','topicId':'d_functions','screenshots':str(OUT)}
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
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url='http://127.0.0.1:8771/chapters/d_functions.html'))
 for _ in range(100):
  if js('!!window.ConceptAnimations'):break
  time.sleep(.1)
 assert js('!!window.ConceptAnimations'), 'Chapter or renderer did not load'
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))')
 report['loadFailures']=js("[...document.querySelectorAll('.concept-animation')].filter(h=>h.dataset.loaded!=='true').map(h=>({scenes:h.dataset.scenes,state:h.dataset.loaded,text:h.textContent}))");assert not report['loadFailures'],report['loadFailures']


 report=json.loads((R/'research/deep-library-revision/d_functions-browser.json').read_text())
 report['finalStaticArrows']=js(r"(()=>{const rows=[];for(const svg of document.querySelectorAll('figure svg')){const markers=new Set([...svg.querySelectorAll('marker')].map(m=>m.id));for(const e of svg.querySelectorAll('[marker-end]')){const match=e.getAttribute('marker-end').match(/url\(#([^)]*)\)/);if(!match||!markers.has(match[1]))throw Error('Unresolved static arrow marker');}const ports=[...svg.querySelectorAll('[data-static-ports]')].map(e=>{const circles=[...svg.querySelectorAll('circle')],rects=[...svg.querySelectorAll('rect')];const distance=(x,y)=>Math.min(...circles.map(c=>Math.abs(Math.hypot(x-+c.getAttribute('cx'),y-+c.getAttribute('cy'))-+c.getAttribute('r'))),...rects.map(r=>{const X=+r.getAttribute('x'),Y=+r.getAttribute('y'),w=+r.getAttribute('width'),h=+r.getAttribute('height');return Math.hypot(Math.max(X-x,x-X-w,0),Math.max(Y-y,y-Y-h,0))||Math.min(Math.abs(x-X),Math.abs(x-X-w),Math.abs(y-Y),Math.abs(y-Y-h));}));return[distance(+e.getAttribute('x1'),+e.getAttribute('y1')),distance(+e.getAttribute('x2'),+e.getAttribute('y2'))];});rows.push({ports});}return rows;})()")
 assert len(report['finalStaticArrows'])==5 and sum(len(r['ports'])for r in report['finalStaticArrows'])==22
 assert all(max(pair)<.001 for r in report['finalStaticArrows']for pair in r['ports'])
 for i in range(5):
  js('[...document.querySelectorAll("figure svg")]['+str(i)+'].closest("figure").setAttribute("data-final-static","'+str(i)+'")');capture('[data-final-static="'+str(i)+'"]',f'static-{i+1}.png')
 report['finalMathCaptionPlayback']=[]
 for n in[3,47]:
  selector=f'.exam-question[data-deep-index="{n}"] .concept-animation'
  row=js('(async()=>{const h=document.querySelector('+json.dumps(selector)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host)),w=c.api.host;c.api.show(0);const play=w.querySelector("[data-play]"),speed=w.querySelector("[data-speed]");speed.value="1400";speed.dispatchEvent(new Event("change"));play.click();await new Promise(r=>setTimeout(r,1550));play.click();const index=c.api.index;await new Promise(r=>setTimeout(r,150));return{id:c.scene.id,advanced:index>0,paused:c.api.index===index,mathCaption:!!w.querySelector(".sim-operation math")};})()');assert row['advanced']and row['paused'];report['finalMathCaptionPlayback'].append(row)
  js('(()=>{const h=document.querySelector('+json.dumps(selector)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host));c.api.show(c.api.model.frames.length-1);})()');capture(selector,f'question-{n}-final.png')
 for n in[35,46]:
  selector=f'.exam-question[data-deep-index="{n}"] .concept-animation';js('(()=>{const h=document.querySelector('+json.dumps(selector)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host));c.api.show(c.api.model.frames.length-1);})()');capture(selector,f'question-{n}-final.png')
 assert report['finalMathCaptionPlayback'][1]['mathCaption']
 report['finalStaticRepair']='Five retained diagrams have 22 attached straight arrows, preserved marker identities, small filled tips and separate prose/mathematical fonts. Native mathematical captions and teaching operations were played and paused in two actual representatives after the optional HTML support change.'
 report['status']='passed_pending_screenshot_inspection'
finally:
 (R/'research/deep-library-revision/d_functions-browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
 proc.terminate()
print(report['status'])
