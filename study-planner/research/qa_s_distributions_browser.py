"""Inspect real fonts, every stored checkpoint, controls and editable circuits in Edge."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,threading,time,shutil
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'s-distributions-visual-qa';OUT.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=OUT/f'edge-{os.getpid()}';proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report=dict(topicId='s_distributions',status='in_progress',screenshots=str(OUT))
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
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"});cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/s_distributions.html'))
 for _ in range(100):
  if js('window.DistributionPlayers?.length'):break
  time.sleep(.1)
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,rules:document.querySelectorAll(".review-rule").length,players:DistributionPlayers.length,math:document.querySelectorAll("math").length,errors:__errors})');assert report['counts']['questions']==88 and report['counts']['rules']==84 and report['counts']['players']>26,report['counts']
 report['fonts']=js('({math:getComputedStyle(document.querySelector("math")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),heading:document.fonts.check("18px Newsreader"),prose:document.fonts.check("18px \'Source Sans 3\'"),code:document.fonts.check("18px \'JetBrains Mono\'")})');assert all(report['fonts'][k]for k in['stix','heading','prose','code'])

 capture('.hero','title.png')

 report['geometry']=js(r"""(()=>{const seen=new Set(),rows=[];for(const p of DistributionPlayers){if(seen.has(p.model.id))continue;seen.add(p.model.id);const bad=[];for(let i=0;i<p.model.frames.length;i++){p.show(i);const svg=p.host.querySelector('svg');bad.push(...DiagramLayout.audit(svg).map(x=>({...x,frame:i})));if(svg.viewBox.baseVal.height>420)bad.push({kind:'oversized'});if(!p.teaching.root.dataset.explanation)bad.push({kind:'missing explanation'});const ids=[...svg.querySelectorAll('[data-entity]')].map(e=>e.dataset.entity);if(new Set(ids).size!==ids.length)bad.push({kind:'duplicate moving record'});for(const t of svg.querySelectorAll('text')){const a=DiagramLayout.box(svg,t);if(a.x<2||a.y<2||a.x+a.w>758||a.y+a.h>358)bad.push({kind:'text outside',frame:i,text:t.textContent,bounds:a});const cx=a.x+a.w/2,cy=a.y+a.h/2;const b=[...svg.querySelectorAll('rect')].map(r=>DiagramLayout.box(svg,r)).filter(b=>cx>b.x&&cx<b.x+b.w&&cy>b.y&&cy<b.y+b.h).sort((a,b)=>a.w*a.h-b.w*b.h)[0];if(b){const pads=[a.x-b.x,b.x+b.w-a.x-a.w,a.y-b.y,b.y+b.h-a.y-a.h];if(Math.min(...pads)<6)bad.push({kind:'padding',frame:i,text:t.textContent,pads});}}}rows.push({id:p.model.id,frames:p.model.frames.length,bad});p.show(0);}return{models:rows.length,frames:rows.reduce((n,r)=>n+r.frames,0),issues:rows.flatMap(r=>r.bad.map(x=>({...x,id:r.id})))};})()""")
 (R/'research/s_distributions-evidence/browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');assert not report['geometry']['issues'],report['geometry']['issues'][:15]
 report['mathGeometry']=js("""(()=>{const bad=[];for(const m of document.querySelectorAll('math')){for(const s of m.querySelectorAll('msup,msub,msubsup'))if([')',']','}'].includes(s.firstElementChild?.textContent))bad.push(m.getAttribute('aria-label'));}return {bareClosingScriptBases:bad,underlined:[...document.querySelectorAll('a')].filter(a=>getComputedStyle(a).textDecorationLine.includes('underline')).length};})()""");assert not report['mathGeometry']['bareClosingScriptBases']and not report['mathGeometry']['underlined']
 for id,name in [('binomial-eight','binomial.png'),('classification','classification.png'),('negative-two','waiting.png'),('finite-wait','finite-wait.png'),('poisson-splitting','splitting.png'),('poisson-approximation','approximation.png'),('censored','censoring.png'),('uniform-lattice','uniform.png')]:
  js('DistributionPlayers.find(p=>p.model.id==='+json.dumps(id)+').show(DistributionPlayers.find(p=>p.model.id==='+json.dumps(id)+').model.frames.length-1)');capture('[data-sd-model="'+id+'"]',name)
 js('DistributionPlayers.find(p=>p.model.id==="binomial-eight").show(16)');capture('[data-sd-model="binomial-eight"]','mass-transfer.png')

 js('window.p=DistributionPlayers.find(p=>p.model.id==="poisson-approximation");p.show(1);p.host.querySelector("[data-next]").click()');time.sleep(.12)
 report['motion']=js('({pairs:p.motionPairs,progress:p.transition,clocks:p.host.querySelector("svg").getAnimations({subtree:true}).length})');assert report['motion']['pairs']>0 and 0<report['motion']['progress']<1
 js('p.pause();window.oldIndex=p.index;window.times=p.host.querySelector("svg").getAnimations({subtree:true}).map(a=>a.currentTime);window.oldTransition=p.transition');time.sleep(.15)
 report['pause']=js('({motions:times.length,frozen:JSON.stringify(times)===JSON.stringify(p.host.querySelector("svg").getAnimations({subtree:true}).map(a=>a.currentTime)),sameIndex:p.index===oldIndex,running:p.running})');assert report['pause']['frozen']and report['pause']['sameIndex']and not report['pause']['running']
 js('p.host.querySelector("[data-play]").click()');time.sleep(.12);assert js('p.transition>oldTransition');js('p.pause()');report['resume']=True
 js('p.show(2);p.host.querySelector("[data-view=before]").click()');assert js('p.host.dataset.displayedFrame')=='1'
 js('p.host.querySelector("[data-view=compare]").click()');assert js('p.host.querySelectorAll(".sim-compare svg").length')==2
 js('p.host.querySelector("[data-view=after]").click()');assert js('p.host.dataset.displayedFrame')=='2';report['comparison']=True
 js('p.host.querySelector("[data-prev]").click()');assert js('p.index')==1
 js('p.host.querySelector("[data-seek]").value=2;p.host.querySelector("[data-seek]").dispatchEvent(new Event("input"))');assert js('p.index')==2
 js('p.host.querySelector("[data-reset]").click()');assert js('p.index')==0
 cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]});js('p.show(0);p.host.querySelector("[data-next]").click()');assert js('p.host.querySelector("svg").getAnimations({subtree:true}).length')==0;report['reducedMotion']=True
 js('p.print()');assert js('p.host.querySelectorAll(".sd-print figure").length')==js('p.model.frames.length');js('p.clearPrint()');report['printCheckpoints']=True
 report['labs']=[]
 for spec in [dict(kind='binomial',n='0',p='0'),dict(kind='binomial',n='12',p='1'),dict(kind='geometric',p='0.2',limit='12'),dict(kind='negative-binomial',r='6',p='0.5',limit='12'),dict(kind='hypergeometric',N='8',K='6',n='5'),dict(kind='poisson',lambdaValue='8',limit='12')]:
  obj=js('(()=>{const f=document.querySelector("#sd-form"),spec='+json.dumps(spec)+';for(const[k,v]of Object.entries({kind:"binomial",n:"6",p:"0.5",r:"2",N:"10",K:"4",lambda:"1",limit:"8",...spec}))if(k!=="lambdaValue")f.elements[k].value=v;if(spec.lambdaValue)f.elements.lambda.value=spec.lambdaValue;f.dispatchEvent(new Event("submit",{cancelable:true}));return {error:document.querySelector("#sd-error").textContent,result:DistributionLab.result,issues:DiagramLayout.audit(document.querySelector("#sd-output svg"))};})()');assert not obj['error']and not obj['issues'],obj;report['labs'].append(obj)
 for change in [dict(p='-0.1'),dict(n='1.5'),dict(n='13'),dict(kind='geometric',p='0'),dict(kind='negative-binomial',r='0'),dict(kind='hypergeometric',K='11'),dict(kind='poisson',lambdaValue='NaN'),dict(limit='')]:
  js('(()=>{window.oldLab=DistributionLab;const f=document.querySelector("#sd-form"),change='+json.dumps(change)+';for(const[k,v]of Object.entries({kind:"binomial",n:"6",p:"0.5",r:"2",N:"10",K:"4",lambda:"1",limit:"8",...change}))if(k!=="lambdaValue")f.elements[k].value=v;if(change.lambdaValue)f.elements.lambda.value=change.lambdaValue;f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('DistributionLab===oldLab && document.querySelector("#sd-error").textContent.length>0'),change
 report['invalidPreservesPrevious']=8

 cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=True));report['mobileOverflow']=js('document.documentElement.scrollWidth>innerWidth+1');assert not report['mobileOverflow'];capture('[data-sd-model="uniform-lattice"]','mobile-uniform.png')
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Emulation.setEmulatedMedia',{'media':'print'});js('p.print()');report['printVisible']=js('getComputedStyle(p.host.querySelector(".sd-print")).display!=="none"');assert report['printVisible']
 report['runtimeErrors']=js('__errors');assert not report['runtimeErrors'];assert not js('DistributionPlayers.some(p=>p.teaching.root.textContent.includes("undefined"))')
 cdp('Emulation.setEmulatedMedia',{'media':'screen'});cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/index.html#library'))
 for _ in range(100):
  if js('document.querySelector("#library a[href=\\"chapters/s_distributions.html\\"]")!==null'):break
  time.sleep(.1)
 report['library']=js('({cards:document.querySelectorAll(".library-card").length,visible:!document.querySelector("#view-lessons").hidden,errors:__errors})');assert report['library']['cards']==58 and report['library']['visible']and not report['library']['errors']
 js('location.hash="week-4"');js('new Promise(r=>setTimeout(r,100))');report['weeklyChapterLink']=js('!document.querySelector("#view-weeks").hidden && document.querySelector("#week-detail a[href=\\"chapters/s_distributions.html\\"]")!==null');assert report['weeklyChapterLink']
 report['status']='passed'
 for f in OUT.glob('*.png'):shutil.copy2(f,R/'research/s_distributions-evidence'/f.name)
finally:
 (R/'research/s_distributions-evidence/browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
 try:ws.close()
 except:pass
 proc.terminate();server.shutdown()
print(json.dumps({k:v for k,v in report.items()if k not in ['labs']},indent=2))
