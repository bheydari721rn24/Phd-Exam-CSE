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

 cdp('Page.enable');cdp('Runtime.enable');cdp('Emulation.setDeviceMetricsOverride',dict(width=1280,height=1000,deviceScaleFactor=1,mobile=False))
 results=[]
 for row in ([] if '--screenshots-only' in sys.argv else json.loads((ROOT/'research/library-visual-question-review/input.json').read_text())):
  topic=row['topicId'];cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/{topic}.html'));time.sleep(.35)
  js('(async()=>{for(let i=0;i<150;i++){if(location.pathname.endsWith('+json.dumps(topic+'.html')+')&&document.readyState==="complete"&&window.ProblemVisuals&&window.ConceptAnimations)return;await new Promise(r=>setTimeout(r,50));}throw Error("Chapter scripts did not initialize");})()')
  js('document.fonts.ready')
  js('Promise.all([...document.querySelectorAll("details.exam-solution")].map(d=>{d.open=true;return Promise.all([...d.querySelectorAll("[data-problem-visual]")].map(ProblemVisuals.ready).concat([...d.querySelectorAll(".concept-animation")].map(ConceptAnimations.ready)));}))')
  check=js("""(()=>{const bad=[...document.querySelectorAll("[data-loaded=error]")].length;return {questions:document.querySelectorAll("section.exam-question").length,failedModels:bad,problemPlayers:ProblemVisuals.players.length,conceptPlayers:ConceptAnimations.players.length,mathFont:getComputedStyle(document.querySelector("math")).fontFamily,documentWidth:document.documentElement.scrollWidth,viewport:innerWidth,loadedFonts:document.fonts.check('18px "STIX Two Math"')};})()""")
  assert check['questions']==row['questionCount'] and check['failedModels']==0 and check['loadedFonts'] and 'STIX' in check['mathFont'],(topic,check)
  cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=False));time.sleep(.1)
  mobile=js('({width:document.documentElement.scrollWidth,viewport:innerWidth})')
  assert mobile['width']<=mobile['viewport']+1,(topic,mobile)
  cdp('Emulation.setEmulatedMedia',dict(media='print'));js('window.dispatchEvent(new Event("beforeprint"))')
  printed=js('({open:[...document.querySelectorAll("details.exam-solution")].every(d=>d.open),hiddenControls:[...document.querySelectorAll(".problem-controls")].every(c=>getComputedStyle(c).display==="none")})')
  assert printed['open'] and printed['hiddenControls'],(topic,printed)
  cdp('Emulation.setEmulatedMedia',dict(media=''));js('window.dispatchEvent(new Event("afterprint"))');cdp('Emulation.setDeviceMetricsOverride',dict(width=1280,height=1000,deviceScaleFactor=1,mobile=False))
  results.append(dict(topicId=topic,desktop=check,mobile=mobile,print=printed))
  print(topic,check['questions'],'problems: loaded, mobile contained, print ready',flush=True)
 if results:(ROOT/'research/library-visual-question-review/page-browser.json').write_text(json.dumps(dict(state='passed',chapters=results),indent=2)+'\n')
 # Capture representative real solution cards, not isolated renderer mocks.
 for topic,number in [('g_combin',37),('g_combin',58),('g_kmap',5),('l_gauss',5),('p_functions',25),('a_arrays',1)]:
  cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/{topic}.html'));time.sleep(.2);js('document.fonts.ready')
  js('(async()=>{for(let i=0;i<150;i++){if(location.pathname.endsWith('+json.dumps(topic+'.html')+')&&document.readyState==="complete"&&window.ProblemVisuals)return;await new Promise(r=>setTimeout(r,50));}throw Error("Capture scripts did not initialize");})()')
  js('(async()=>{const q=document.querySelectorAll("section.exam-question")['+str(number-1)+'];q.querySelector("details").open=true;await Promise.all([...q.querySelectorAll("[data-problem-visual]")].map(ProblemVisuals.ready));(q.querySelector(".problem-visual")||q).scrollIntoView();})()');time.sleep(.15)
  screenshot=cdp('Page.captureScreenshot',dict(format='png'))['data'];(ROOT/'research/library-visual-question-review'/f'{topic}-q{number}.png').write_bytes(base64.b64decode(screenshot))
finally:
 proc.terminate();server.shutdown()
