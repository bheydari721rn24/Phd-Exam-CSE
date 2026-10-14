from pathlib import Path
import json,os,subprocess,tempfile,time
import requests,websocket
R=Path(__file__).resolve().parents[1];O=Path(tempfile.gettempdir())/f'correctness-mobile-probe-{os.getpid()}';O.mkdir();proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={O}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL);seq=0
try:
 for _ in range(100):
  if(O/'DevToolsActivePort').exists()and(O/'DevToolsActivePort').read_text().strip():break
  time.sleep(.1)
 port=int((O/'DevToolsActivePort').read_text().splitlines()[0]);p=next(x for x in requests.get(f'http://127.0.0.1:{port}/json').json()if x['type']=='page');ws=websocket.create_connection(p['webSocketDebuggerUrl'],timeout=30)
 def cdp(m,params=None):
  global seq
  seq+=1;ws.send(json.dumps({'id':seq,'method':m,'params':params or{}}))
  while True:
   a=json.loads(ws.recv())
   if a.get('id')==seq:return a.get('result',{})
 def js(s):return cdp('Runtime.evaluate',{'expression':s,'returnByValue':True,'awaitPromise':True}).get('result',{}).get('value')
 cdp('Emulation.setDeviceMetricsOverride',{'width':390,'height':1080,'deviceScaleFactor':1,'mobile':True});cdp('Page.navigate',{'url':'http://127.0.0.1:8771/chapters/a_correct.html'});time.sleep(1)
 js('document.fonts.ready');js('document.querySelectorAll("details").forEach(d=>d.open=true)');js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))')
 report=js("""(()=>({width:innerWidth,visual:visualViewport.width,screen:screen.width,offenders:[...document.querySelectorAll('body *')].filter(e=>!e.closest('svg')).map(e=>({tag:e.tagName,id:e.id,cls:e.className,text:e.textContent.slice(0,100),left:e.getBoundingClientRect().left,right:e.getBoundingClientRect().right,overflow:getComputedStyle(e).overflowX})).filter(e=>e.right>391&&e.overflow==='visible').slice(0,25)}))()""");print(report)
finally:
 proc.terminate()
 try:proc.wait(timeout=10)
 except subprocess.TimeoutExpired:proc.kill()
