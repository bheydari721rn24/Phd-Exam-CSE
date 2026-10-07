"""Real Edge rendering, native math, geometry, controls and laboratory contracts."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,threading,time,shutil
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'s-discrete-visual-qa';OUT.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=OUT/f'edge-{os.getpid()}';proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report=dict(topicId='s_discrete',status='in_progress',screenshots=str(OUT))
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
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"});cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/s_discrete.html'))
 for _ in range(100):
  if js('window.DiscretePlayers?.length'):break
  time.sleep(.1)
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,rules:document.querySelectorAll(".review-rule").length,players:DiscretePlayers.length,math:document.querySelectorAll("math").length})');assert report['counts']['questions']==83 and report['counts']['rules']==80
 report['fonts']=js('({math:getComputedStyle(document.querySelector("math")).fontFamily,prose:getComputedStyle(document.querySelector(".lesson p")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),heading:document.fonts.check("18px Newsreader"),source:document.fonts.check("18px \'Source Sans 3\'"),code:document.fonts.check("18px \'JetBrains Mono\'")})');assert all(report['fonts'][k] for k in ['stix','heading','source','code'])
 report['geometry']=js('''(()=>{const seen=new Set(),rows=[];for(const p of DiscretePlayers){if(seen.has(p.model.id))continue;seen.add(p.model.id);const bad=[];for(let i=0;i<p.model.frames.length;i++){p.show(i);bad.push(...DiagramLayout.audit(p.host.querySelector('svg')).map(x=>({...x,frame:i})));if(!p.teaching.root.dataset.explanation)bad.push({kind:'missing explanation'});if(p.teaching.root.querySelectorAll('.teaching-test').length!==p.model.frames[i].teaching.checks.length)bad.push({kind:'missing exact checks'});}rows.push({id:p.model.id,frames:p.model.frames.length,bad});p.show(0);}return {models:rows.length,frames:rows.reduce((n,r)=>n+r.frames,0),issues:rows.flatMap(r=>r.bad.map(x=>({...x,id:r.id})))};})()''')
 (R/'research/s_discrete-evidence/browser.json').write_text(json.dumps(report,indent=2)+'\n');assert not report['geometry']['issues'],report['geometry']['issues'][:20]
 report['nativeMath']=js('({fractions:document.querySelectorAll("mfrac").length,scripts:document.querySelectorAll("msub,msup,msubsup,munder,munderover").length,missing:[...document.querySelectorAll("math")].filter(m=>m.getBoundingClientRect().height<1).length,underlined:[...document.querySelectorAll("a")].filter(a=>getComputedStyle(a).textDecorationLine.includes("underline")).length})');assert not report['nativeMath']['missing'] and not report['nativeMath']['underlined']

 report['mappingPortsAndPadding']=js("""(()=>{const rows=[];for(const p of DiscretePlayers){if(!['weighted-fiber-map','many-to-one-transformation'].includes(p.model.kind))continue;for(let i=0;i<p.model.frames.length;i++){p.show(i);const svg=p.host.querySelector('svg'),boxes=[...svg.querySelectorAll('polygon')].map(e=>DiagramLayout.box(svg,e)).filter(b=>b.w>100&&b.h>40);for(const t of svg.querySelectorAll('text')){const a=DiagramLayout.box(svg,t),cx=a.x+a.w/2,cy=a.y+a.h/2,b=boxes.find(b=>cx>b.x&&cx<b.x+b.w&&cy>b.y&&cy<b.y+b.h);if(b){const pads=[a.x-b.x,b.x+b.w-a.x-a.w,a.y-b.y,b.y+b.h-a.y-a.h];if(Math.min(...pads)<6)rows.push({id:p.model.id,frame:i,text:t.textContent,pads});}}for(const path of svg.querySelectorAll('path')){const length=path.getTotalLength(),start=path.getPointAtLength(0),end=path.getPointAtLength(length);const source=boxes.find(b=>Math.abs(start.x-b.x-b.w)<.1&&start.y>=b.y&&start.y<=b.y+b.h),target=boxes.find(b=>Math.abs(end.x-b.x)<.1&&end.y>=b.y&&end.y<=b.y+b.h);if(!source||!target)rows.push({id:p.model.id,frame:i,kind:'connector endpoint'});}}p.show(0);}return rows;})()""");assert not report['mappingPortsAndPadding'],report['mappingPortsAndPadding']
 assert report['geometry']['models']==37 and report['geometry']['frames']==208

 capture('.hero','title.png')
 capture('[data-source-id="s-discrete-original-30"]','question-convolution.png')
 capture('.review-rule','review-rule.png')
 for id,step,name in [('map-weighted',4,'mapping.png'),('cdf-three',3,'cdf.png'),('interval-three',3,'interval.png'),('square-five',5,'square.png'),('bin-four-quarter',4,'binomial.png'),('hyper-forced',3,'hypergeometric.png'),('cap-four',3,'stopping.png'),('max-four',2,'maximum.png'),('family-conditioning',2,'posterior.png')]:
  js('DiscretePlayers.find(p=>p.model.id==='+json.dumps(id)+').show('+str(step)+')');capture('[data-disc-model="'+id+'"]',name)
 js('window.p=DiscretePlayers.find(p=>p.model.id==="inverse-three");p.show(0);p.host.querySelector("[data-next]").click()');time.sleep(.1);js('p.pause();window.times=p.host.querySelector("svg").getAnimations({subtree:true}).map(a=>a.currentTime)');time.sleep(.1)
 report['pause']=js('({motions:times.length,frozen:JSON.stringify(times)===JSON.stringify(p.host.querySelector("svg").getAnimations({subtree:true}).map(a=>a.currentTime))})');assert report['pause']['motions']>0 and report['pause']['frozen']
 js('p.host.querySelector("[data-play]").click()');time.sleep(.1);report['resume']=js('p.host.querySelector("svg").getAnimations({subtree:true}).some(a=>a.currentTime>times[0])');assert report['resume'];js('p.pause();p.show(3);p.host.querySelector("[data-prev]").click()');assert js('p.index')==2
 js('p.host.querySelector("[data-seek]").value=4;p.host.querySelector("[data-seek]").dispatchEvent(new Event("input"))');assert js('p.index')==4
 js('p.host.querySelector("[data-reset]").click()');assert js('p.index')==0
 cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]});js('p.show(1);p.host.querySelector("[data-next]").click()');assert js('p.host.querySelector("svg").getAnimations({subtree:true}).length')==0;report['reducedMotion']=True
 js('p.print()');assert js('p.host.querySelectorAll(".disc-print figure").length')==js('p.model.frames.length');js('p.clearPrint()');report['printCheckpoints']=True
 fixtures=[('cdf','-2,1,4','.2,.5,.3',1,.25,4,.7),('interval','-2,1,4','.2,.5,.3',1,.25,4,[0,.3,.5,.8]),('quantile','-2,1,4','.2,.5,.3',1,.7,4,1),('square','-2,-1,0,1,2','.05,.1,.2,.25,.4',1,.7,4,[.2,.35,.45]),('binomial','-2,1,4','.2,.5,.3',4,.25,5,27/128),('geometric','-2,1,4','.2,.5,.3',4,.25,5,.75**8),('poisson','-2,1,4','.2,.5,.3',4,3,5,2.718281828459045**-3),('hypergeometric','-2,1,4','.2,.5,.3',8,4,3,[1/14,6/14,6/14,1/14])]
 report['labs']=[]
 for kind,v,mass,n,q,upper,expected in fixtures:
  val=js("(()=>{const f=document.querySelector('#disc-form');for(const [k,v] of Object.entries("+json.dumps(dict(kind=kind,values=v,masses=mass,n=str(n),p=str(q),upper=str(upper)))+"))f.elements[k].value=v;f.dispatchEvent(new Event('submit',{cancelable:true,bubbles:true}));const r=DiscreteLab.model.result,k="+json.dumps(kind)+";const result=k==='cdf'?r[1].after:k==='interval'?r.map(x=>x.p):k==='quantile'?r[0].x:k==='square'?r.map(x=>x.p):k==='binomial'?r[2].p:k==='geometric'?r.tail:k==='poisson'?r.law[0].p:r.map(x=>x.p);return {error:document.querySelector('#disc-error').textContent,result};})()")
  assert not val['error'],(kind,val)
  import math
  if isinstance(expected,list):assert all(math.isclose(a,b,abs_tol=1e-12) for a,b in zip(expected,val['result'])),(kind,val,expected)
  else:assert math.isclose(expected,val['result'],abs_tol=1e-12),(kind,val,expected)
  report['labs'].append(dict(mode=kind,**val))
 invalid=[{'kind':'cdf','masses':'.1,.1,.1'},{'kind':'cdf','values':'1,,2'},{'kind':'quantile','p':'0'},{'kind':'geometric','p':'0'},{'kind':'binomial','n':'2.5'},{'kind':'hypergeometric','n':'4','upper':'5','p':'2'}]
 for change in invalid:
  js('(()=>{window.previousModel=DiscreteLab;const f=document.querySelector("#disc-form");for(const [k,v] of Object.entries('+json.dumps(dict(kind='cdf',values='-2,1,4',masses='.2,.5,.3',n='4',p='.25',upper='5')|change)+'))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('DiscreteLab===previousModel && document.querySelector("#disc-error").textContent.length>0')
 report['invalidPreservesPrevious']=len(invalid)
 report['allModesGeometry']=js('DiagramLayout.audit(DiscreteLab.host.querySelector("svg"))');assert not report['allModesGeometry']
 cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=True));report['mobileOverflow']=js('document.documentElement.scrollWidth>innerWidth+1');assert not report['mobileOverflow'];capture('[data-disc-model="cdf-three"]','mobile-cdf.png')
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Emulation.setEmulatedMedia',{'media':'print'});js('p.print()');report['printVisible']=js('getComputedStyle(p.host.querySelector(".disc-print")).display!=="none"');assert report['printVisible'];capture('[data-disc-model="inverse-three"]','print-inverse.png')
 report['runtimeErrors']=js('__errors');assert not report['runtimeErrors']
 cdp('Emulation.setEmulatedMedia',{'media':'screen'});cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/index.html#library'))
 for _ in range(100):
  if js('document.querySelector("#library a[href=\\"chapters/s_discrete.html\\"]")!==null'):break
  time.sleep(.1)
 report['library']=js('({cards:document.querySelectorAll(".library-card").length,visible:!document.querySelector("#view-lessons").hidden,current:document.querySelector("#library a[href=\\"chapters/s_discrete.html\\"]").textContent,errors:__errors})');assert report['library']['cards']==40 and report['library']['visible'] and not report['library']['errors']
 js('location.hash="week-3"');js('new Promise(r=>setTimeout(r,100))');report['weeklyChapterLink']=js('!document.querySelector("#view-weeks").hidden && document.querySelector("#week-detail a[href=\\"chapters/s_discrete.html\\"]")!==null');assert report['weeklyChapterLink']
 report['status']='passed'
 for name in ['title.png','mapping.png','cdf.png','square.png','hypergeometric.png','stopping.png','maximum.png','mobile-cdf.png']:
  shutil.copy2(OUT/name,R/'research/s_discrete-evidence'/name)
finally:
 (R/'research/s_discrete-evidence/browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');server.shutdown();proc.terminate()
print(json.dumps({k:v for k,v in report.items() if k not in ['geometry','labs']}))
