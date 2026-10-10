"""Inspect real fonts, every stored checkpoint, controls and editable circuits in Edge."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,threading,time,shutil
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'d-generating-visual-qa';OUT.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=OUT/f'edge-{os.getpid()}';proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report=dict(topicId='d_generating',status='in_progress',screenshots=str(OUT))
try:
 for _ in range(100):
  if(profile/'DevToolsActivePort').exists():break
  time.sleep(.1)
 port=int((profile/'DevToolsActivePort').read_text().splitlines()[0]);page=next(p for p in requests.get(f'http://127.0.0.1:{port}/json').json()if p['type']=='page');ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=60)
 def cdp(method,params=None):
  global seq
  seq+=1;ws.send(json.dumps(dict(id=seq,method=method,params=params or{})))
  while True:
   r=json.loads(ws.recv())
   if r.get('id')==seq:assert 'error'not in r,r;return r.get('result',{})
 def js(code):
  r=cdp('Runtime.evaluate',dict(expression=code,returnByValue=True,awaitPromise=True));assert 'exceptionDetails'not in r,r;return r.get('result',{}).get('value')
 def capture(sel,name):
  js('document.querySelector('+json.dumps(sel)+').scrollIntoView({block:"center",behavior:"instant"})');js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');(OUT/name).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"});cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/d_generating.html'))
 for _ in range(100):
  if js('window.GeneratingPlayers?.length'):break
  time.sleep(.1)
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,rules:document.querySelectorAll(".review-rule").length,players:GeneratingPlayers.length,math:document.querySelectorAll("math").length,errors:__errors})');assert report['counts']['questions']==82 and report['counts']['rules']==80 and report['counts']['players']>17,report['counts']
 report['fonts']=js('({math:getComputedStyle(document.querySelector("math")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),heading:document.fonts.check("18px Newsreader"),prose:document.fonts.check("18px \'Source Sans 3\'"),code:document.fonts.check("18px \'JetBrains Mono\'")})');assert all(report['fonts'][k]for k in['stix','heading','prose','code'])
 audit=r'''(()=>{const seen=new Set(),rows=[];for(const p of GeneratingPlayers){if(seen.has(p.model.id))continue;seen.add(p.model.id);const bad=[];for(let i=0;i<p.model.frames.length;i++){p.show(i);const svg=p.host.querySelector('svg');bad.push(...DiagramLayout.audit(svg).map(x=>({...x,frame:i})));if(!p.teaching.root.dataset.explanation)bad.push({kind:'missing explanation'});for(const t of svg.querySelectorAll('text')){const a=DiagramLayout.box(svg,t);if(a.x<2||a.y<2||a.x+a.w>758||a.y+a.h>svg.viewBox.baseVal.height-2)bad.push({kind:'text outside plot',frame:i,text:t.textContent,bounds:a});const boxes=[...svg.querySelectorAll('rect')].map(r=>DiagramLayout.box(svg,r));const cx=a.x+a.w/2,cy=a.y+a.h/2,b=boxes.find(b=>cx>b.x&&cx<b.x+b.w&&cy>b.y&&cy<b.y+b.h);if(b){const pads=[a.x-b.x,b.x+b.w-a.x-a.w,a.y-b.y,b.y+b.h-a.y-a.h];if(Math.min(...pads)<6)bad.push({kind:'label padding',frame:i,text:t.textContent,pads});}}}rows.push({id:p.model.id,frames:p.model.frames.length,bad});p.show(0);}return {models:rows.length,frames:rows.reduce((n,r)=>n+r.frames,0),issues:rows.flatMap(r=>r.bad.map(x=>({...x,id:r.id})))};})()'''
 report['geometry']=js(audit)
 (R/'research/d_generating-evidence/browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');assert not report['geometry']['issues'],report['geometry']['issues'][:30]
 report['mathGeometry']=js('''(()=>{const bare=[],clipped=[];for(const m of document.querySelectorAll('math')){for(const s of m.querySelectorAll('msup,msub,msubsup'))if([')',']','}'].includes(s.firstElementChild?.textContent))bare.push(m.getAttribute('aria-label'));for(const t of m.querySelectorAll('mo'))if(['(',')','[',']'].includes(t.textContent)){const r=t.getBoundingClientRect();if(!r.width||!r.height)clipped.push(t.textContent);}}return {bareClosingScriptBases:bare,zeroSizeFences:clipped,underlined:[...document.querySelectorAll('a')].filter(a=>getComputedStyle(a).textDecorationLine.includes('underline')).length};})()''');assert not report['mathGeometry']['bareClosingScriptBases']and not report['mathGeometry']['zeroSizeFences']and not report['mathGeometry']['underlined']
 for id,step,name in [('convolution-five',5,'convolution.png'),('durfee-seven',8,'durfee.png'),('catalan-four',5,'catalan.png'),('label-five',15,'labels.png'),('binary-six',31,'marking.png'),('three-boxes',3,'bounds.png'),('triple-pole',7,'pole.png')]:
  js('GeneratingPlayers.find(p=>p.model.id==='+json.dumps(id)+').show('+str(step)+')');capture('[data-gf-model="'+id+'"]',name)
 capture('.hero','title.png');capture('[data-source-id="d_generating_original_47"]','synthesis-question.png');capture('.review-rule','final-rule.png')
 js('window.p=GeneratingPlayers.find(p=>p.model.id==="catalan-four");p.show(0);p.host.querySelector("[data-play]").click()');time.sleep(.12);js('p.pause();window.oldIndex=p.index;window.times=p.host.querySelector("svg").getAnimations({subtree:true}).map(a=>a.currentTime)');time.sleep(.15)
 report['pause']=js('({motions:times.length,frozen:JSON.stringify(times)===JSON.stringify(p.host.querySelector("svg").getAnimations({subtree:true}).map(a=>a.currentTime)),sameIndex:p.index===oldIndex,running:p.running})');assert report['pause']['frozen']and report['pause']['sameIndex']and not report['pause']['running']
 js('p.host.querySelector("[data-play]").click()');time.sleep(.12);assert js('p.running');js('p.pause();p.show(2);p.host.querySelector("[data-prev]").click()');assert js('p.index')==1
 js('p.host.querySelector("[data-seek]").value=2;p.host.querySelector("[data-seek]").dispatchEvent(new Event("input"))');assert js('p.index')==2
 js('p.host.querySelector("[data-reset]").click()');assert js('p.index')==0
 cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]});js('p.show(0);p.host.querySelector("[data-next]").click()');assert js('p.host.querySelector("svg").getAnimations({subtree:true}).length')==0;report['reducedMotion']=True
 js('p.print()');assert js('p.host.querySelectorAll(".gf-print figure").length')==js('p.model.frames.length');js('p.clearPrint()');report['printCheckpoints']=True
 report['labs']=[]
 for op,n in [('inverse',10),('convolution',6),('filter',10),('bounded',9),('coins',10),('composition',7),('partitions',10),('durfee',7),('catalan',4),('labelled',6),('marking',6),('poles',10)]:
  spec=dict(operation=op,n=n)
  obj=js('(()=>{const f=document.querySelector("#gf-form"),spec='+json.dumps(spec)+';for(const[k,v]of Object.entries(spec))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));const bad=[];for(let i=0;i<GeneratingLab.model.frames.length;i++){GeneratingLab.show(i);bad.push(...DiagramLayout.audit(GeneratingLab.host.querySelector("svg")));}return {operation:spec.operation,error:document.querySelector("#gf-error").textContent,result:GeneratingLab.model.result,issues:bad};})()');assert not obj['error']and not obj['issues'],obj;report['labs'].append(obj)
 for change in [dict(n=0),dict(n=11),dict(n=2.5),dict(operation='convolution',n=7),dict(operation='composition',n=8),dict(operation='catalan',n=5),dict(operation='labelled',n=7),dict(operation='bounded',n=10),dict(operation='durfee',n=8)]:
  js('(()=>{window.oldLab=GeneratingLab;const f=document.querySelector("#gf-form"),base={operation:"inverse",n:5},change='+json.dumps(change)+';for(const[k,v]of Object.entries({...base,...change}))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('GeneratingLab===oldLab && document.querySelector("#gf-error").textContent.length>0')
 report['invalidPreservesPrevious']=9
 cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=True));report['mobileOverflow']=js('document.documentElement.scrollWidth>innerWidth+1');assert not report['mobileOverflow'];capture('[data-gf-model="convolution-five"]','mobile-automaton.png')
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Emulation.setEmulatedMedia',{'media':'print'});js('p.print()');report['printVisible']=js('getComputedStyle(p.host.querySelector(".gf-print")).display!=="none"');assert report['printVisible'];capture('[data-gf-model="catalan-four"]','print-prefix.png')
 assert not js('GeneratingPlayers.some(p=>p.teaching.root.textContent.includes("undefined"))');report['runtimeErrors']=js('__errors');assert not report['runtimeErrors']
 cdp('Emulation.setEmulatedMedia',{'media':'screen'});cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/index.html#library'))
 for _ in range(100):
  if js('document.querySelector("#library a[href=\\"chapters/d_generating.html\\"]")!==null'):break
  time.sleep(.1)
 report['library']=js('({cards:document.querySelectorAll(".library-card").length,visible:!document.querySelector("#view-lessons").hidden,errors:__errors})');assert report['library']['cards']==51 and report['library']['visible']and not report['library']['errors']
 js('location.hash="week-4"');js('new Promise(r=>setTimeout(r,100))');report['weeklyChapterLink']=js('!document.querySelector("#view-weeks").hidden && document.querySelector("#week-detail a[href=\\"chapters/d_generating.html\\"]")!==null');assert report['weeklyChapterLink']
 report['status']='passed'
 for f in OUT.glob('*.png'):shutil.copy2(f,R/'research/d_generating-evidence'/f.name)
finally:
 (R/'research/d_generating-evidence/browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');server.shutdown();proc.terminate()
print(json.dumps({k:v for k,v in report.items()if k not in['geometry','labs']}))
