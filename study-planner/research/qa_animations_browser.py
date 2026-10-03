"""Render all scenarios and checkpoints, then exercise actual controls."""
import base64,json,os,subprocess,tempfile,threading,time
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import requests,websocket
ROOT=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'chapter-animation-review';OUT.mkdir(exist_ok=True)
manifest=json.loads((ROOT/'research/animation-manifest.json').read_text());topics=[r['topicId'] for r in manifest['chapters']]
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=OUT/f'edge-{os.getpid()}';proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
results={'chapters':[],'scenarios':{},'layoutIssues':[]};seq=0
try:
 active=profile/'DevToolsActivePort'
 for _ in range(100):
  if active.exists():break
  time.sleep(.1)
 port=int(active.read_text().splitlines()[0]);page=next(p for p in requests.get(f'http://127.0.0.1:{port}/json',timeout=5).json() if p['type']=='page');ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=60)
 def cdp(method,params=None):
  global seq
  seq+=1;ws.send(json.dumps({'id':seq,'method':method,'params':params or {}}))
  while True:
   r=json.loads(ws.recv())
   if r.get('id')==seq:
    assert 'error' not in r,r
    return r.get('result',{})
 def js(expr,wait=False):
  r=cdp('Runtime.evaluate',{'expression':expr,'returnByValue':True,'awaitPromise':wait});assert 'exceptionDetails' not in r,r
  return r['result'].get('value')
 def screenshot(name):
  (OUT/name).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
 cdp('Page.enable')
 for topic in topics:
  cdp('Emulation.setDeviceMetricsOverride',{'width':1280,'height':1000,'deviceScaleFactor':1,'mobile':False})
  cdp('Page.navigate',{'url':f'http://127.0.0.1:{server.server_port}/chapters/{topic}.html'});time.sleep(.25)
  js('document.fonts.ready',True)
  js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))',True)
  for _ in range(50):
   if js('[...document.querySelectorAll(".concept-animation")].every(h=>h.dataset.loaded==="true")'):break
   time.sleep(.05)
  assert js('[...document.querySelectorAll(".concept-animation")].every(h=>h.dataset.loaded==="true")'),topic
  row=js('({players:ConceptAnimations.players.length,questions:document.querySelectorAll(".exam-question").length,overflow:document.documentElement.scrollWidth>innerWidth+1,underlined:[...document.querySelectorAll(".concept-animation a")].some(x=>getComputedStyle(x).textDecorationLine.includes("underline"))})');assert not row['overflow'] and not row['underlined'],(topic,row)
  row['topicId']=topic;results['chapters'].append(row)
  done=list(results['scenarios']);audit=js('''(()=>{const done=new Set('''+json.dumps(done)+'''),out={},issues=[];for(const p of ConceptAnimations.players){for(let s=0;s<p.scenes.length;s++){const scene=p.scenes[s];if(done.has(scene.id))continue;p.choice.value=s;p.choice.dispatchEvent(new Event('change'));let moving=false;for(let i=0;i<scene.frames.length;i++){p.show(i,false);const boxes=[...p.canvas.querySelectorAll('text')].filter(t=>t.textContent.trim()).map(t=>{const b=t.getBBox(),m=(t.parentElement.transform.baseVal.consolidate()?.matrix||{e:0,f:0});return {label:t.textContent,x:b.x+m.e,y:b.y+m.f,w:b.width,h:b.height,font:getComputedStyle(t).fontFamily,size:parseFloat(getComputedStyle(t).fontSize)};});for(const b of boxes){if(b.x< -1||b.y< -1||b.x+b.w>761||b.y+b.h>361)issues.push({id:scene.id,step:i,kind:'outside',box:b});if(!b.font.includes('STIX'))issues.push({id:scene.id,step:i,kind:'font',box:b});}for(let a=0;a<boxes.length;a++)for(let b=a+1;b<boxes.length;b++){const x=boxes[a],y=boxes[b];if(Math.min(x.x+x.w,y.x+y.w)-Math.max(x.x,y.x)>3&&Math.min(x.y+x.h,y.y+y.h)-Math.max(x.y,y.y)>3)issues.push({id:scene.id,step:i,kind:'label overlap',labels:[x.label,y.label]});}if(i){const before=scene.frames[i-1].nodes;moving ||= scene.frames[i].nodes.some(n=>before.some(b=>b.id===n.id&&(b.x!==n.x||b.y!==n.y)));}if(p.seek.value!=i||Number(p.host.dataset.step)!==i)issues.push({id:scene.id,step:i,kind:'checkpoint mismatch'});}out[scene.id]={frames:scene.frames.length,entityMotion:moving,finalCounterexample:!!scene.frames.at(-1).counterexample};done.add(scene.id);}p.choice.value=0;p.choice.dispatchEvent(new Event('change'));}return {out,issues};})()''')
  results['scenarios'].update(audit['out']);results['layoutIssues'].extend(audit['issues'])
  cdp('Emulation.setDeviceMetricsOverride',{'width':390,'height':844,'deviceScaleFactor':1,'mobile':True})
  assert not js('document.documentElement.scrollWidth>innerWidth+1'),('mobile overflow',topic)
  if topic in ['a_correct','l_vectors','g_gates','a_divide','s_axioms']:
   js('ConceptAnimations.players[0].host.scrollIntoView({block:"start"})');screenshot(topic+'-mobile.png')
  js('ConceptAnimations.players[0].buttons.zoom.click()');assert not js('document.documentElement.scrollWidth>innerWidth+1'),('zoom overflow',topic);js('ConceptAnimations.players[0].buttons.zoom.click()')
  js('dispatchEvent(new Event("beforeprint"));dispatchEvent(new Event("afterprint"))')
  assert js('ConceptAnimations.players.every(p=>!p.running)'),topic
 # Sorting controls are exercised through DOM events rather than by just setting a state.
 cdp('Emulation.setDeviceMetricsOverride',{'width':1280,'height':1000,'deviceScaleFactor':1,'mobile':False})
 cdp('Page.navigate',{'url':f'http://127.0.0.1:{server.server_port}/chapters/a_correct.html#animation-sorting'});time.sleep(.3)
 js('document.fonts.ready',True);js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))',True);time.sleep(.2)
 js('window.auditPlayer=ConceptAnimations.players.find(p=>p.host.id==="animation-sorting");auditPlayer.host.scrollIntoView({block:"start"});auditPlayer.buttons.next.click()');time.sleep(.8)
 assert js('auditPlayer.index===1 && !auditPlayer.running')
 js('auditPlayer.buttons.back.click()');time.sleep(.8);assert js('auditPlayer.index===0')
 js('auditPlayer.seek.value=4;auditPlayer.seek.dispatchEvent(new Event("input"))');assert js('auditPlayer.index===4')
 screenshot('insertion-desktop.png')
 js('auditPlayer.buttons.reset.click()');assert js('auditPlayer.index===0')
 js('auditPlayer.host.dispatchEvent(new KeyboardEvent("keydown",{key:"ArrowRight",bubbles:true}))');time.sleep(.8);assert js('auditPlayer.index===1')
 js('auditPlayer.speedSelect.value=2;auditPlayer.speedSelect.dispatchEvent(new Event("change"));auditPlayer.buttons.play.click()');time.sleep(.15);assert js('auditPlayer.running')
 js('auditPlayer.buttons.play.click()');assert js('!auditPlayer.running&&!auditPlayer.busy')
 # Choose stable merge and verify actual in-between motion of a persistent record.
 js('auditPlayer.choice.value=auditPlayer.scenes.findIndex(s=>s.id==="merge");auditPlayer.choice.dispatchEvent(new Event("change"));auditPlayer.show(1,false);window.firstRecord=auditPlayer.scene.frames[1].nodes[0].id;window.beforePos=auditPlayer.positions.get(firstRecord);auditPlayer.buttons.next.click()');time.sleep(.15)
 results['motionSample']=js('({busy:auditPlayer.busy,record:firstRecord,transform:auditPlayer.nodes.get(firstRecord).getAttribute("transform"),start:beforePos,end:auditPlayer.scene.frames[2].nodes.find(n=>n.id===firstRecord)})')
 assert results['motionSample']['busy'] and results['motionSample']['start']['y']!=results['motionSample']['end']['y'],results['motionSample']
 time.sleep(.6);assert js('!auditPlayer.busy')
 js('auditPlayer.seek.value=8;auditPlayer.seek.dispatchEvent(new Event("input"))');screenshot('merge-desktop.png')
 cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]});js('auditPlayer.buttons.reset.click();auditPlayer.buttons.next.click()');assert js('!auditPlayer.busy');results['reducedMotion']=True
 cdp('Emulation.setEmulatedMedia',{'media':'print'});js('dispatchEvent(new Event("beforeprint"))');assert js('!auditPlayer.running&&auditPlayer.buttons.play.getClientRects().length===0');screenshot('animation-print.png');results['printControlsHidden']=True
 results['allScenariosVisited']=len(results['scenarios'])==manifest['uniqueScenarios'];assert results['allScenariosVisited']
 (ROOT/'research/animation-browser-audit.json').write_text(json.dumps(results,indent=2)+'\n')
 print(json.dumps({'chapters':len(results['chapters']),'scenarios':len(results['scenarios']),'layoutIssues':len(results['layoutIssues']),'screenshots':str(OUT)}))
finally:
 (ROOT/'research/animation-browser-audit.json').write_text(json.dumps(results,indent=2)+'\n')
 try:ws.close()
 except Exception:pass
 proc.terminate();server.shutdown()
