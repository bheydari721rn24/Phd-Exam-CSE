from pathlib import Path
import base64,json,os,subprocess,tempfile,threading,time,shutil
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'l-spaces-visual-qa';OUT.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=OUT/f'edge-{os.getpid()}';proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report=dict(topicId='l_spaces',status='in_progress',screenshots=str(OUT))
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
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"});cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/l_spaces.html'))
 for _ in range(100):
  if js('window.VectorSpacePlayers?.length'):break
  time.sleep(.1)
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,rules:document.querySelectorAll(".review-rule").length,players:VectorSpacePlayers.length,math:document.querySelectorAll("math").length})');assert report['counts']['questions']==82 and report['counts']['rules']==80
 report['fonts']=js('({math:getComputedStyle(document.querySelector("math")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),heading:document.fonts.check("18px Newsreader"),prose:document.fonts.check("18px \'Source Sans 3\'"),code:document.fonts.check("18px \'JetBrains Mono\'")})');assert all(report['fonts'][k]for k in['stix','heading','prose','code'])
 report['geometry']=js('''(()=>{const seen=new Set(),rows=[];for(const p of VectorSpacePlayers){if(seen.has(p.model.id))continue;seen.add(p.model.id);const bad=[];for(let i=0;i<p.model.frames.length;i++){p.show(i);const svg=p.host.querySelector('svg');bad.push(...DiagramLayout.audit(svg).map(x=>({...x,frame:i})));if(!p.teaching.root.dataset.explanation)bad.push({kind:'missing explanation'});for(const t of svg.querySelectorAll('text')){const a=DiagramLayout.box(svg,t);if(a.x<2||a.y<2||a.x+a.w>998||a.y+a.h>svg.viewBox.baseVal.height-2)bad.push({kind:'text outside plot',frame:i,text:t.textContent,bounds:a});const boxes=[...svg.querySelectorAll('rect')].map(r=>DiagramLayout.box(svg,r));const cx=a.x+a.w/2,cy=a.y+a.h/2,b=boxes.find(b=>cx>b.x&&cx<b.x+b.w&&cy>b.y&&cy<b.y+b.h);if(b){const pads=[a.x-b.x,b.x+b.w-a.x-a.w,a.y-b.y,b.y+b.h-a.y-a.h];if(Math.min(...pads)<6)bad.push({kind:'label padding',frame:i,text:t.textContent,pads});}}}rows.push({id:p.model.id,frames:p.model.frames.length,bad});p.show(0);}return {models:rows.length,frames:rows.reduce((n,r)=>n+r.frames,0),issues:rows.flatMap(r=>r.bad.map(x=>({...x,id:r.id})))};})()''')
 (R/'research/l_spaces-evidence/browser.json').write_text(json.dumps(report,indent=2)+'\n');assert not report['geometry']['issues'],report['geometry']['issues'][:25]
 report['mathGeometry']=js('''(()=>{const bare=[],clipped=[];for(const m of document.querySelectorAll('math')){for(const s of m.querySelectorAll('msup,msub,msubsup'))if([')',']','}'].includes(s.firstElementChild?.textContent))bare.push(m.getAttribute('aria-label'));for(const t of m.querySelectorAll('mo'))if(['(',')','[',']'].includes(t.textContent)){const r=t.getBoundingClientRect();if(!r.width||!r.height)clipped.push(t.textContent);}}return {bareClosingScriptBases:bare,zeroSizeFences:clipped,underlined:[...document.querySelectorAll('a')].filter(a=>getComputedStyle(a).textDecorationLine.includes('underline')).length};})()''');assert not report['mathGeometry']['bareClosingScriptBases']and not report['mathGeometry']['zeroSizeFences']and not report['mathGeometry']['underlined']
 for id,step,name in [('closure-plane',3,'plane.png'),('pivot-main',3,'pivot.png'),('coordinates-main',2,'coordinates.png'),('symmetric-trace',2,'symmetric.png'),('intersection-main',2,'intersection.png'),('quotient-main',1,'quotient.png'),('finite-basis',2,'finite-field.png'),('projection-main',2,'projection.png'),('intersection-parameter',1,'intersection-jump.png'),('matrix-balances',4,'matrix-balances.png')]:
  js('VectorSpacePlayers.find(p=>p.model.id==='+json.dumps(id)+').show('+str(step)+')');capture('[data-vs-model="'+id+'"]',name)
 capture('.hero','title.png');capture('[data-source-id="l-spaces-original-59"]','question-quotient.png');capture('.review-rule','final-rule.png')
 js('window.p=VectorSpacePlayers.find(p=>p.model.id==="parameter-span");p.show(0);p.host.querySelector("[data-next]").click()');time.sleep(.12);js('p.pause();window.times=p.host.querySelector("svg").getAnimations({subtree:true}).map(a=>a.currentTime)');time.sleep(.1)
 report['pause']=js('({motions:times.length,frozen:JSON.stringify(times)===JSON.stringify(p.host.querySelector("svg").getAnimations({subtree:true}).map(a=>a.currentTime))})');assert report['pause']['motions']>0 and report['pause']['frozen']
 js('p.host.querySelector("[data-play]").click()');time.sleep(.12);report['resume']=js('p.host.querySelector("svg").getAnimations({subtree:true}).some(a=>a.currentTime>times[0])');assert report['resume'];js('p.pause();p.show(2);p.host.querySelector("[data-prev]").click()');assert js('p.index')==1
 js('p.host.querySelector("[data-seek]").value=2;p.host.querySelector("[data-seek]").dispatchEvent(new Event("input"))');assert js('p.index')==2
 js('p.host.querySelector("[data-reset]").click()');assert js('p.index')==0
 cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]});js('p.show(0);p.host.querySelector("[data-next]").click()');assert js('p.host.querySelector("svg").getAnimations({subtree:true}).length')==0;report['reducedMotion']=True
 js('p.print()');assert js('p.host.querySelectorAll(".vs-print figure").length')==js('p.model.frames.length');js('p.clearPrint()');report['printCheckpoints']=True
 report['labs']=[]
 for mat,target,rank,consistent in [('1,2,0,3;2,4,1,4;3,6,2,5','1,3,5',2,True),('0,1;1,0','2,3',2,True),('1,2;2,4','1,3',1,False),('0,0;0,0','0,0',0,True),('1;2;3','2,4,6',1,True),('1,2,3,4,5;2,4,6,8,10;0,1,0,1,0;0,0,1,0,1','2,4,1,1',3,True),('20,-19,17,11;-13,20,16,-18;19,11,-17,20;16,-13,20,19','20,-19,17,11',4,True)]:
  obj=js('(()=>{const f=document.querySelector("#vs-form");f.elements.matrix.value='+json.dumps(mat)+';f.elements.target.value='+json.dumps(target)+';f.dispatchEvent(new Event("submit",{cancelable:true}));const bad=[];for(let i=0;i<VectorSpaceLab.model.frames.length;i++){VectorSpaceLab.show(i);bad.push(...DiagramLayout.audit(VectorSpaceLab.host.querySelector("svg")));}return {error:document.querySelector("#vs-error").textContent,result:VectorSpaceLab.model.result,checks:VectorSpaceLab.model.frames.every(f=>f.teaching.checks.every(c=>c.result==="true")),issues:bad};})()');assert not obj['error']and not obj['issues']and obj['result']['rank']==rank and obj['result']['consistent']==consistent and obj['checks']and all(obj['result']['checks'].values()),obj;report['labs'].append(obj)
 capture('#vs-output .vs-stage','dense-rational-lab.png')
 for mat,target in [('1,,2;2,3','1,2'),('1,2;3','1,2'),('1.5,1;2,3','1,2'),('21,1;2,3','1,2'),('1,2;3,4','1'),('1,2,3,4,5,6;1,2,3,4,5,6','1,2')]:
  js('(()=>{window.oldLab=VectorSpaceLab;const f=document.querySelector("#vs-form");f.elements.matrix.value='+json.dumps(mat)+';f.elements.target.value='+json.dumps(target)+';f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('VectorSpaceLab===oldLab && document.querySelector("#vs-error").textContent.length>0')
 report['invalidPreservesPrevious']=6
 cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=True));report['mobileOverflow']=js('document.documentElement.scrollWidth>innerWidth+1');assert not report['mobileOverflow'];capture('[data-vs-model="pivot-main"]','mobile-cofactor.png')
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Emulation.setEmulatedMedia',{'media':'print'});js('p.print()');report['printVisible']=js('getComputedStyle(p.host.querySelector(".vs-print")).display!=="none"');assert report['printVisible'];capture('[data-vs-model="parameter-span"]','print-area.png')
 report['runtimeErrors']=js('__errors');assert not report['runtimeErrors']
 cdp('Emulation.setEmulatedMedia',{'media':'screen'});cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/index.html#library'))
 for _ in range(100):
  if js('document.querySelector("#library a[href=\\"chapters/l_spaces.html\\"]")!==null'):break
  time.sleep(.1)
 report['library']=js('({cards:document.querySelectorAll(".library-card").length,visible:!document.querySelector("#view-lessons").hidden,errors:__errors})');assert report['library']['cards']==43 and report['library']['visible']and not report['library']['errors']
 js('location.hash="week-3"');js('new Promise(r=>setTimeout(r,100))');report['weeklyChapterLink']=js('!document.querySelector("#view-weeks").hidden && document.querySelector("#week-detail a[href=\\"chapters/l_spaces.html\\"]")!==null');assert report['weeklyChapterLink']
 report['status']='passed'
 for f in OUT.glob('*.png'):shutil.copy2(f,R/'research/l_spaces-evidence'/f.name)
finally:
 (R/'research/l_spaces-evidence/browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');server.shutdown();proc.terminate()
print(json.dumps({k:v for k,v in report.items()if k not in['geometry','labs']}))
