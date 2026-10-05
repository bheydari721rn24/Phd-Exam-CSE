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
 for id,s in json.loads((ROOT/'dist/chapters/concept-animations.json').read_text())['scenes'].items():
  try:
   r=js('(()=>{const p=reviewPlayer;p.pause();p.scene=reviewData.scenes['+json.dumps(id)+'];const failures=[];let max=0,first;for(let i=0;i<p.scene.frames.length;i++){p.show(i,false);if(i===0)first=p.canvas.outerHTML;const e=p.canvas.outerHTML;if(/NaN|undefined/.test(e))failures.push({step:i,error:"nonfinite or missing data"});for(const t of p.canvas.querySelectorAll("text")){const local=t.getBBox(),matrix=p.canvas.getScreenCTM().inverse().multiply(t.getScreenCTM()),corners=[[local.x,local.y],[local.x+local.width,local.y],[local.x,local.y+local.height],[local.x+local.width,local.y+local.height]].map(([x,y])=>new DOMPoint(x,y).matrixTransform(matrix)),b={x:Math.min(...corners.map(a=>a.x)),y:Math.min(...corners.map(a=>a.y)),width:Math.max(...corners.map(a=>a.x))-Math.min(...corners.map(a=>a.x)),height:Math.max(...corners.map(a=>a.y))-Math.min(...corners.map(a=>a.y))};if(b.x<-.5||b.y<0||b.x+b.width>760.5||b.y+b.height>360.5)failures.push({step:i,text:t.textContent,error:"out of viewBox",box:[b.x,b.y,b.width,b.height]});max=Math.max(max,b.x+b.width);}}p.show(p.scene.frames.length-1,false);p.canvas.scrollIntoView({block:"center"});return {id:p.scene.id,type:p.canvas.dataset.visualType,frames:p.scene.frames.length,failures,svg:p.canvas.outerHTML,first,max};})()')
   svg=r.pop('svg');first=r.pop('first');(OUT/(id+'.svg')).write_text(svg,encoding='utf-8');(OUT/(id+'.first.svg')).write_text(first,encoding='utf-8');rows.append(r)
   if id in ['nand-mapping','cmos-nand','comb-priority','comb-active-low','comb-dag','conditional-strip','rank-collapse','matrix-product','fn-pointer','insertion','km-corners','gauss-geometry']:
    (OUT/(id+'.png')).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',dict(format='png'))['data']))
  except Exception as e:errors.append(dict(id=id,error=str(e)))
 for name in ['gate-symbols','nand-mux','half-subtractor','factored','multi-miter']:
  svg=js('(()=>{const svg=SemanticDiagrams.staticDiagram('+json.dumps(name)+');reviewPlayer.canvas.replaceWith(svg);reviewPlayer.canvas=svg;svg.scrollIntoView({block:"center"});return svg.outerHTML;})()');(OUT/(name+'.svg')).write_text(svg,encoding='utf-8');(OUT/(name+'.png')).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',dict(format='png'))['data']))
 circuit_cases=0
 cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/g_combin.html'));time.sleep(.2);js('document.fonts.ready')
 for mode in ['shared','priority','nand']:
  for i in range(16):
   bits=[i>>3&1,i>>2&1,i>>1&1,i&1]
   actual=js('(()=>{const form=document.getElementById("combin-form");form.elements.mode.value='+json.dumps(mode)+';form.elements.variant.value="correct";["a","b","c","d"].forEach((k,i)=>form.elements[k].value='+json.dumps(bits)+'[i]);form.dispatchEvent(new Event("input"));const p=ConceptAnimations.players.find(p=>p.host.id==="combin-player");p.show(p.scene.frames.length-1,false);return {values:JSON.parse(p.nodeLayer.dataset.netValues),gates:p.nodeLayer.querySelectorAll("[data-gate]").length}})()')
   a,b,c,d=bits;v=actual['values']
   expected={'shared':{'Y':(a&b)&(c|d),'Z':(a&b)|c},'priority':{'G1':a&b,'G0':a&(1-b)&c,'V':a&(b|c)},'nand':{'Y':a&(b|c)}}[mode]
   assert all(v[k]==want for k,want in expected.items()),(mode,bits,actual,expected)
   assert actual['gates']=={'shared':4,'priority':6,'nand':3}[mode],actual
   circuit_cases+=1
 # Formula reflow must preserve every mathematical leaf and source, at actual
 # mobile width. Only labeled internal panning is allowed for indivisible scopes.
 math_rows=[]
 for topic in [r['topicId'] for r in json.loads((ROOT/'research/subject-visual-review.json').read_text())['chapters']]:
  cdp('Emulation.setDeviceMetricsOverride',dict(width=1280,height=1000,deviceScaleFactor=1,mobile=False))
  cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/{topic}.html'));time.sleep(.12);js('document.fonts.ready')
  js('window.mathOriginal=[...document.querySelectorAll("math")].map(m=>({text:m.textContent,source:m.getAttribute("aria-label")}))')
  cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=True));js('MathLayout.layout()')
  record=js('(()=>{const math=[...document.querySelectorAll("math")],pans=[...document.querySelectorAll(".formula-block")].filter(e=>e.scrollWidth>e.clientWidth+2);return {tokensPreserved:math.every((m,i)=>m.textContent===mathOriginal[i].text&&m.getAttribute("aria-label")===mathOriginal[i].source),mathCount:math.length,documentWidth:document.documentElement.scrollWidth,mathFont:math.every(m=>getComputedStyle(m).fontFamily.includes("STIX")),pans:pans.map(e=>{const old=e.scrollLeft;e.scrollLeft=e.scrollWidth;const accessible=e.scrollLeft>0;e.scrollLeft=old;return {bounded:getComputedStyle(e).overflowX==="auto",labeled:e.dataset.scrollable==="true",accessible}})}})()')
  assert record['tokensPreserved'] and record['mathFont'] and record['documentWidth']<=390,(topic,record)
  assert all(p['bounded'] and p['labeled'] and p['accessible'] for p in record['pans']),(topic,record)
  if topic in ['d_logic','l_matrices','g_gates']:
   js('document.querySelector(".formula-block").scrollIntoView({block:"center"})');(OUT/(topic+'.math-mobile.png')).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',dict(format='png'))['data']))
  js('dispatchEvent(new Event("beforeprint"))')
  record['printTokensPreserved']=js('[...document.querySelectorAll("math")].every((m,i)=>m.textContent===mathOriginal[i].text)')
  assert record['printTokensPreserved'],topic
  math_rows.append(dict(topicId=topic,**record))
 print(json.dumps(dict(scenes=len(rows),errors=errors,layoutFailures=sum(len(r['failures']) for r in rows),mathChapters=len(math_rows),renderedCircuitTruthCases=circuit_cases,preview=str(OUT))))
 (ROOT/'research/subject-visual-browser-audit.json').write_text(json.dumps(dict(scenes=rows,errors=errors,mathematicalLayout=math_rows,renderedCircuitTruthCases=circuit_cases),indent=2)+'\n')
finally:
 proc.terminate();server.shutdown()
