"""Real Edge rendering, native math, geometry, controls and laboratory contracts."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,threading,time,shutil
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'s-descriptive-visual-qa';OUT.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=OUT/f'edge-{os.getpid()}';proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report=dict(topicId='s_descriptive',status='in_progress',screenshots=str(OUT))
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
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"});cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/s_descriptive.html'))
 for _ in range(100):
  if js('window.StatisticsPlayers?.length'):break
  time.sleep(.1)
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,rules:document.querySelectorAll(".review-rule").length,players:StatisticsPlayers.length,math:document.querySelectorAll("math").length})');assert report['counts']['questions']==82 and report['counts']['rules']==80
 report['fonts']=js('({math:getComputedStyle(document.querySelector("math")).fontFamily,prose:getComputedStyle(document.querySelector(".lesson p")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),heading:document.fonts.check("18px Newsreader"),source:document.fonts.check("18px \'Source Sans 3\'"),code:document.fonts.check("18px \'JetBrains Mono\'")})');assert all(report['fonts'][k] for k in ['stix','heading','source','code'])
 report['geometry']=js('''(()=>{const seen=new Set(),rows=[];for(const p of StatisticsPlayers){if(seen.has(p.model.id))continue;seen.add(p.model.id);const bad=[];for(let i=0;i<p.model.frames.length;i++){p.show(i);bad.push(...DiagramLayout.audit(p.host.querySelector('svg')).map(x=>({...x,frame:i})));if(!p.teaching.root.dataset.explanation)bad.push({kind:'missing explanation'});if(p.teaching.root.querySelectorAll('.teaching-test').length!==p.model.frames[i].teaching.checks.length)bad.push({kind:'missing exact checks'});}rows.push({id:p.model.id,frames:p.model.frames.length,bad});p.show(0);}return {models:rows.length,frames:rows.reduce((n,r)=>n+r.frames,0),issues:rows.flatMap(r=>r.bad.map(x=>({...x,id:r.id})))};})()''')
 (R/'research/s_descriptive-evidence/browser.json').write_text(json.dumps(report,indent=2)+'\n');assert not report['geometry']['issues'],report['geometry']['issues'][:20]
 report['nativeMath']=js('({fractions:document.querySelectorAll("mfrac").length,scripts:document.querySelectorAll("msub,msup,msubsup,munder,munderover").length,missing:[...document.querySelectorAll("math")].filter(m=>m.getBoundingClientRect().height<1).length,underlined:[...document.querySelectorAll("a")].filter(a=>getComputedStyle(a).textDecorationLine.includes("underline")).length})');assert not report['nativeMath']['missing'] and not report['nativeMath']['underlined']
 # Every frame uses the declared fixed number scale; overlays are not passed through node-port adjustment.
 capture('.hero','title.png')
 for id,step,name in [('hist-equal',16,'histogram.png'),('ecdf-ties',3,'ecdf.png'),('loss-gap',3,'median-loss.png'),('box-example',4,'boxplot.png'),('stream-example',12,'stream.png'),('correlation-curve',4,'correlation.png'),('smoothing-ma',3,'moving-average.png')]:
  js('StatisticsPlayers.find(p=>p.model.id==='+json.dumps(id)+').show('+str(step)+')');capture('[data-stat-model="'+id+'"]',name)
 js('window.p=StatisticsPlayers.find(p=>p.model.id==="affine-negative");p.show(1);p.host.querySelector("[data-next]").click()');time.sleep(.15);js('p.pause();window.times=p.host.querySelector("svg").getAnimations({subtree:true}).map(a=>a.currentTime)');time.sleep(.15)
 report['pause']=js('({motions:times.length,frozen:JSON.stringify(times)===JSON.stringify(p.host.querySelector("svg").getAnimations({subtree:true}).map(a=>a.currentTime))})');assert report['pause']['motions']>0 and report['pause']['frozen']
 js('p.host.querySelector("[data-play]").click()');time.sleep(.15);report['resume']=js('p.host.querySelector("svg").getAnimations({subtree:true}).some(a=>a.currentTime>times[0])');assert report['resume'];js('p.pause();p.show(4);p.host.querySelector("[data-prev]").click()');assert js('p.index')==3
 js('p.host.querySelector("[data-seek]").value=5;p.host.querySelector("[data-seek]").dispatchEvent(new Event("input"))');assert js('p.index')==5
 js('p.host.querySelector("[data-reset]").click()');assert js('p.index')==0
 cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]});js('p.show(1);p.host.querySelector("[data-next]").click()');assert js('p.host.querySelector("svg").getAnimations({subtree:true}).length')==0;report['reducedMotion']=True
 js('p.print()');assert js('p.host.querySelectorAll(".stat-print figure").length')==js('p.model.frames.length');js('p.clearPrint()');report['printCheckpoints']=True
 fixtures=[('histogram','0,1,1,2,3,4','3','0,1,2,4',[1,2,3]),('ecdf','1,2,2,5','3','',.75),('mean','1,3,8,10','3','',5.5),('median','1,3,8,10','3','',[3,8]),('quantiles','1,5,8,15','3','',6.5),('variance','0,2,4','3','',8/3),('affine','1,2,3,4,5','-3','7',-2),('box','1,2,3,4,5,6,7,20','3','',[1,7]),('pooling','0,0','3','6,6',9),('stream','0,2,4,10','3','',14),('correlation','-1,0,1','3','1,0,1',0),('qq','0,1,2,4','3','5,7,9,13',9),('ma','2,4,10,8','3','',[2,3,16/3,22/3]),('ewma','2,4,10','.5','',[1,2.5,6.25])]
 report['labs']=[]
 for kind,v,param,other,expected in fixtures:
  val=js('''(()=>{const f=document.querySelector('#stat-form');f.elements.kind.value='''+json.dumps(kind)+''';f.elements.values.value='''+json.dumps(v)+''';f.elements.parameter.value='''+json.dumps(param)+''';f.elements.other.value='''+json.dumps(other)+''';f.dispatchEvent(new Event('submit',{cancelable:true,bubbles:true}));const r=StatisticsLab.model.result,k='''+json.dumps(kind)+''';const result=k==='histogram'?r.counts:k==='ecdf'?r.find(x=>x.value===2).after:k==='mean'?r.mean:k==='median'?r.minimizer:k==='quantiles'?r.find(x=>x.p===.5).type7:k==='affine'?r.mean:k==='box'?r.whiskers:k==='correlation'?r.r:k==='qq'?r.find(x=>x.p===.75).y:['ma','ewma'].includes(k)?r:r.v;return {error:document.querySelector('#stat-error').textContent,result};})()''')
  assert not val['error'],(kind,val)
  # Q–Q probability .75 for B=(5,7,9,13) is 10, not the third record 9.
  if kind=='qq':expected=10
  if isinstance(expected,(list,int,float)):assert json.dumps(val['result'])==json.dumps(expected) or val['result']==expected,(kind,val,expected)
  report['labs'].append(dict(mode=kind,**val))
 invalid=[('histogram','1,2','1','0,0,3'),('correlation','1,2,3','1','1,2'),('ma','1,2','0',''),('ewma','1,2','1.1',''),('variance','1,,2','1','')]
 for kind,v,param,other in invalid:
  js('(()=>{window.previousModel=StatisticsLab;const f=document.querySelector("#stat-form");f.elements.kind.value='+json.dumps(kind)+';f.elements.values.value='+json.dumps(v)+';f.elements.parameter.value='+json.dumps(param)+';f.elements.other.value='+json.dumps(other)+';f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('StatisticsLab===previousModel && document.querySelector("#stat-error").textContent.length>0')
 report['invalidPreservesPrevious']=len(invalid)
 report['allModesGeometry']=js('DiagramLayout.audit(StatisticsLab.host.querySelector("svg"))');assert not report['allModesGeometry']
 cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=True));report['mobileOverflow']=js('document.documentElement.scrollWidth>innerWidth+1');assert not report['mobileOverflow'];capture('[data-stat-model="box-example"]','mobile-boxplot.png')
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Emulation.setEmulatedMedia',{'media':'print'});js('p.print()');report['printVisible']=js('getComputedStyle(p.host.querySelector(".stat-print")).display!=="none"');assert report['printVisible'];capture('[data-stat-model="affine-negative"]','print-affine.png')
 report['runtimeErrors']=js('__errors');assert not report['runtimeErrors']
 cdp('Emulation.setEmulatedMedia',{'media':'screen'});cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/index.html#library'))
 for _ in range(100):
  if js('document.querySelector("#library a[href=\\"chapters/s_descriptive.html\\"]")!==null'):break
  time.sleep(.1)
 report['library']=js('({cards:document.querySelectorAll(".library-card").length,visible:!document.querySelector("#view-lessons").hidden,current:document.querySelector("#library a[href=\\"chapters/s_descriptive.html\\"]").textContent,status:document.querySelector("#library").textContent.includes("39 chapter notes: 38 approved chapters"),errors:__errors})');assert report['library']['cards']==39 and report['library']['visible'] and report['library']['status'] and not report['library']['errors']
 js('location.hash="week-3"');js('new Promise(r=>setTimeout(r,100))');report['weeklyChapterLink']=js('!document.querySelector("#view-weeks").hidden && document.querySelector("#week-detail a[href=\\"chapters/s_descriptive.html\\"]")!==null');assert report['weeklyChapterLink']
 report['status']='passed'
 for name in ['title.png','histogram.png','boxplot.png','stream.png','correlation.png','median-loss.png','mobile-boxplot.png']:
  shutil.copy2(OUT/name,R/'research/s_descriptive-evidence'/name)
finally:
 (R/'research/s_descriptive-evidence/browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');server.shutdown();proc.terminate()
print(json.dumps({k:v for k,v in report.items() if k not in ['geometry','labs']}))
