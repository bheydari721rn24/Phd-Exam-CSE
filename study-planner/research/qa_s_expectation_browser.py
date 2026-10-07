"""Real Edge rendering, native math, geometry, controls and laboratory contracts."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,threading,time,shutil
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'s-expectation-visual-qa';OUT.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=OUT/f'edge-{os.getpid()}';proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report=dict(topicId='s_expectation',status='in_progress',screenshots=str(OUT))
try:
 for _ in range(100):
  if (profile/'DevToolsActivePort').exists():break
  time.sleep(.1)
 port=int((profile/'DevToolsActivePort').read_text().splitlines()[0]);page=next(p for p in requests.get(f'http://127.0.0.1:{port}/json').json() if p['type']=='page');ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=60)
 def cdp(method,params=None):
  global seq
  seq+=1;ws.send(json.dumps(dict(id=seq,method=method,params=params or {})))
  while True:
   r=json.loads(ws.recv())
   if r.get('id')==seq:
    assert 'error' not in r,r
    return r.get('result',{})
 def js(code):
  r=cdp('Runtime.evaluate',dict(expression=code,returnByValue=True,awaitPromise=True));assert 'exceptionDetails' not in r,r;return r.get('result',{}).get('value')
 def capture(sel,name):
  js('document.querySelector('+json.dumps(sel)+').scrollIntoView({block:"center",behavior:"instant"})');js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');(OUT/name).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"});cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/s_expectation.html'))
 for _ in range(100):
  if js('window.ExpectationPlayers?.length'):break
  time.sleep(.1)
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,rules:document.querySelectorAll(".review-rule").length,players:ExpectationPlayers.length,math:document.querySelectorAll("math").length})');assert report['counts']['questions']==82 and report['counts']['rules']==80
 report['fonts']=js('({math:getComputedStyle(document.querySelector("math")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),heading:document.fonts.check("18px Newsreader"),prose:document.fonts.check("18px \'Source Sans 3\'"),code:document.fonts.check("18px \'JetBrains Mono\'")})');assert all(report['fonts'][k]for k in ['stix','heading','prose','code'])
 report['geometry']=js('''(()=>{const seen=new Set(),rows=[];for(const p of ExpectationPlayers){if(seen.has(p.model.id))continue;seen.add(p.model.id);const bad=[];for(let i=0;i<p.model.frames.length;i++){p.show(i);const svg=p.host.querySelector('svg');bad.push(...DiagramLayout.audit(svg).map(x=>({...x,frame:i})));if(!p.teaching.root.dataset.explanation)bad.push({kind:'missing explanation'});if(p.teaching.root.querySelectorAll('.teaching-test').length!==p.model.frames[i].teaching.checks.length)bad.push({kind:'missing predicates'});const boxes=[...svg.querySelectorAll('polygon')].map(e=>DiagramLayout.box(svg,e)).filter(b=>b.w>80&&b.h>40);for(const t of svg.querySelectorAll('text')){const a=DiagramLayout.box(svg,t),cx=a.x+a.w/2,cy=a.y+a.h/2,b=boxes.find(b=>cx>b.x&&cx<b.x+b.w&&cy>b.y&&cy<b.y+b.h);if(b){const pads=[a.x-b.x,b.x+b.w-a.x-a.w,a.y-b.y,b.y+b.h-a.y-a.h];if(Math.min(...pads)<6)bad.push({kind:'label padding',frame:i,text:t.textContent,pads});}if(a.x<2||a.y<2||a.x+a.w>998||a.y+a.h>svg.viewBox.baseVal.height-2)bad.push({kind:'text outside plot',frame:i,text:t.textContent,bounds:a});}if(p.model.kind==='permutation-match-count'){for(const path of svg.querySelectorAll('path')){const length=path.getTotalLength(),a=path.getPointAtLength(0),b=path.getPointAtLength(length);if(a.y!==135||b.y!==285)bad.push({kind:'permutation connector endpoint',frame:i});}}}rows.push({id:p.model.id,frames:p.model.frames.length,bad});p.show(0);}return {models:rows.length,frames:rows.reduce((n,r)=>n+r.frames,0),issues:rows.flatMap(r=>r.bad.map(x=>({...x,id:r.id})))};})()''')
 (R/'research/s_expectation-evidence/browser.json').write_text(json.dumps(report,indent=2)+'\n');assert not report['geometry']['issues'],report['geometry']['issues'][:20]
 assert report['geometry']['models']==19 and report['geometry']['frames']==85
 report['nativeMath']=js('({fractions:document.querySelectorAll("mfrac").length,scripts:document.querySelectorAll("msub,msup,msubsup,munder,munderover").length,missing:[...document.querySelectorAll("math")].filter(m=>m.getBoundingClientRect().height<1).length,underlined:[...document.querySelectorAll("a")].filter(a=>getComputedStyle(a).textDecorationLine.includes("underline")).length})');assert not report['nativeMath']['missing']and not report['nativeMath']['underlined']
 capture('.hero','title.png');capture('[data-source-id="s-expectation-original-51"]','question-loss.png');capture('.review-rule','review-rule.png')
 for id,step,name in [('mean-main',3,'mean.png'),('fixed-four',2,'permutation.png'),('bins-four',4,'occupancy.png'),('tail-main',3,'tail-layers.png'),('graph-five',2,'triangle.png'),('window-eight',1,'overlap.png'),('loss-main',2,'loss.png')]:
  js('ExpectationPlayers.find(p=>p.model.id==='+json.dumps(id)+').show('+str(step)+')');capture('[data-exp-model="'+id+'"]',name)
 js('window.p=ExpectationPlayers.find(p=>p.model.id==="record-five");p.show(1);p.host.querySelector("[data-next]").click()');time.sleep(.12);js('p.pause();window.times=p.host.querySelector("svg").getAnimations({subtree:true}).map(a=>a.currentTime)');time.sleep(.1)
 report['pause']=js('({motions:times.length,frozen:JSON.stringify(times)===JSON.stringify(p.host.querySelector("svg").getAnimations({subtree:true}).map(a=>a.currentTime))})');assert report['pause']['motions']>0 and report['pause']['frozen']
 js('p.host.querySelector("[data-play]").click()');time.sleep(.12);report['resume']=js('p.host.querySelector("svg").getAnimations({subtree:true}).some(a=>a.currentTime>times[0])');assert report['resume'];js('p.pause();p.show(3);p.host.querySelector("[data-prev]").click()');assert js('p.index')==2
 js('p.host.querySelector("[data-seek]").value=4;p.host.querySelector("[data-seek]").dispatchEvent(new Event("input"))');assert js('p.index')==4
 js('p.host.querySelector("[data-reset]").click()');assert js('p.index')==0
 cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]});js('p.show(1);p.host.querySelector("[data-next]").click()');assert js('p.host.querySelector("svg").getAnimations({subtree:true}).length')==0;report['reducedMotion']=True
 js('p.print()');assert js('p.host.querySelectorAll(".exp-print figure").length')==js('p.model.frames.length');js('p.clearPrint()');report['printCheckpoints']=True
 fixtures=[('mean','-2,1,4','.2,.5,.3',3,.25,1.3),('square','-2,1,4','.2,.5,.3',3,.25,6.1),('absolute','-2,1,4','.2,.5,.3',3,.25,2.1),('loss','-2,1,4','.2,.5,.3',3,.25,4.41),('tails','0,1,2,3','.25,.25,.25,.25',3,.25,1.5),('cap','-2,1,4','.2,.5,.3',3,.25,37/16),('bins','-2,1,4','.2,.5,.3',4,3,65/27),('tails','0,8','.5,.5',3,.25,4),('cap','0','1',3,0,3),('bins','0','1',0,1,0)]
 report['labs']=[]
 for kind,v,mass,cap,prob,expected in fixtures:
  val=js("(()=>{const f=document.querySelector('#exp-form');for(const [k,v] of Object.entries("+json.dumps(dict(kind=kind,values=v,masses=mass,cap=str(cap),prob=str(prob)))+"))f.elements[k].value=v;f.dispatchEvent(new Event('submit',{cancelable:true,bubbles:true}));const r=ExpectationLab.model.result,k="+json.dumps(kind)+";ExpectationLab.show(ExpectationLab.model.frames.length-1);const result=k==='loss'?r.variance:k==='bins'?r.occupiedMean:r.mean;return {error:document.querySelector('#exp-error').textContent,result,geometry:DiagramLayout.audit(ExpectationLab.host.querySelector('svg'))};})()")
  assert not val['error']and not val['geometry'],(kind,val)
  import math
  assert math.isclose(expected,val['result'],abs_tol=1e-10),(kind,val,expected)
  report['labs'].append(dict(mode=kind,**val))
 invalid=[{'kind':'mean','masses':'.1,.1,.1'},{'kind':'mean','values':'1,,2'},{'kind':'tails','values':'-1,0,2'},{'kind':'tails','values':'0,1.5,2'},{'kind':'cap','cap':'2.5'},{'kind':'cap','prob':'-0.1'},{'kind':'cap','prob':''},{'kind':'bins','prob':'0'},{'kind':'mean','masses':'-.1,.5,.6'}]
 for change in invalid:
  js('(()=>{window.previousModel=ExpectationLab;const f=document.querySelector("#exp-form");for(const [k,v]of Object.entries('+json.dumps(dict(kind='mean',values='-2,1,4',masses='.2,.5,.3',cap='3',prob='.25')|change)+'))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('ExpectationLab===previousModel && document.querySelector("#exp-error").textContent.length>0')
 report['invalidPreservesPrevious']=len(invalid)
 cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=True));report['mobileOverflow']=js('document.documentElement.scrollWidth>innerWidth+1');assert not report['mobileOverflow'];capture('[data-exp-model="tail-main"]','mobile-tail.png')
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Emulation.setEmulatedMedia',{'media':'print'});js('p.print()');report['printVisible']=js('getComputedStyle(p.host.querySelector(".exp-print")).display!=="none"');assert report['printVisible'];capture('[data-exp-model="record-five"]','print-record.png')
 report['runtimeErrors']=js('__errors');assert not report['runtimeErrors']
 cdp('Emulation.setEmulatedMedia',{'media':'screen'});cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/index.html#library'))
 for _ in range(100):
  if js('document.querySelector("#library a[href=\\"chapters/s_expectation.html\\"]")!==null'):break
  time.sleep(.1)
 report['library']=js('({cards:document.querySelectorAll(".library-card").length,visible:!document.querySelector("#view-lessons").hidden,current:document.querySelector("#library a[href=\\"chapters/s_expectation.html\\"]").textContent,errors:__errors})');assert report['library']['cards']==41 and report['library']['visible']and not report['library']['errors']
 js('location.hash="week-3"');js('new Promise(r=>setTimeout(r,100))');report['weeklyChapterLink']=js('!document.querySelector("#view-weeks").hidden && document.querySelector("#week-detail a[href=\\"chapters/s_expectation.html\\"]")!==null');assert report['weeklyChapterLink']
 report['status']='passed'
 for name in ['title.png','mean.png','permutation.png','occupancy.png','tail-layers.png','triangle.png','overlap.png','loss.png','mobile-tail.png','question-loss.png','review-rule.png','print-record.png']:
  shutil.copy2(OUT/name,R/'research/s_expectation-evidence'/name)
finally:
 (R/'research/s_expectation-evidence/browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');server.shutdown();proc.terminate()
print(json.dumps({k:v for k,v in report.items() if k not in ['geometry','labs']}))
