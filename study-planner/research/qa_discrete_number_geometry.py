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


 c=js('(()=>{const c=ConceptAnimations.players.find(c=>c.scene.id==="discrete-number-question-adjacent-8");c.api.show(c.api.model.frames.length-1);c.api.host.setAttribute("data-geometry","true");const svg=c.api.host.querySelector("svg");return{math:[...svg.querySelectorAll("foreignObject")].map(m=>({attributes:[...m.attributes].map(a=>[a.name,a.value]),rect:m.getBoundingClientRect().toJSON(),math:m.querySelector("math")?.getBoundingClientRect().toJSON()})),texts:[...svg.querySelectorAll("text")].map(t=>({text:t.textContent,y:t.getAttribute("y"),x:t.getAttribute("x"),rect:t.getBoundingClientRect().toJSON()}))}})()');print(c);capture('[data-geometry]','adjacent-eight-geometry.png')
finally:
 proc.terminate()
