"""Actual native math/SVG layout and controls in Edge; no modifications to existing chapters."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,threading,time
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'a-select-visual-qa';OUT.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=OUT/f'edge-{os.getpid()}';proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report=dict(topicId='a_select',status='in_progress',screenshots=str(OUT))
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
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"});cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/a_select.html'))
 for _ in range(100):
  if js('window.SelectPlayers?.length')==39:break
  if js('window.SelectPlayers?.length'):break
  time.sleep(.1)
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,rules:document.querySelectorAll(".review-rule").length,players:SelectPlayers.length,math:document.querySelectorAll("math").length})');assert report['counts']['questions']==89 and report['counts']['rules']==80
 report['fonts']=js('({math:getComputedStyle(document.querySelector("math")).fontFamily,prose:getComputedStyle(document.querySelector(".lesson p")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),heading:document.fonts.check("18px Newsreader"),source:document.fonts.check("18px \'Source Sans 3\'"),code:document.fonts.check("18px \'JetBrains Mono\'")})');assert all(report['fonts'][k] for k in ['stix','heading','source','code'])
 report['geometry']=js('''(()=>{const seen=new Set(),rows=[];for(const p of SelectPlayers){if(seen.has(p.model.id))continue;seen.add(p.model.id);const bad=[];for(let i=0;i<p.model.frames.length;i++){p.show(i);bad.push(...DiagramLayout.audit(p.host.querySelector('svg')).map(x=>({...x,frame:i})));if(!p.teaching.root.dataset.explanation)bad.push({kind:'missing explanation'});if(p.teaching.root.querySelectorAll('.teaching-test').length!==p.model.frames[i].teaching.checks.length)bad.push({kind:'missing exact checks'});}rows.push({id:p.model.id,frames:p.model.frames.length,bad});p.show(0);}return {models:rows.length,frames:rows.reduce((n,r)=>n+r.frames,0),issues:rows.flatMap(r=>r.bad.map(x=>({...x,id:r.id})))};})()''')
 (R/'research/a_select-evidence/browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');assert not report['geometry']['issues'],report['geometry']['issues'][:20]
 report['nativeMath']=js('({fractions:document.querySelectorAll("mfrac").length,sums:document.querySelectorAll("munderover,munder,msubsup").length,missing:[...document.querySelectorAll("math")].filter(m=>m.getBoundingClientRect().height<1).length,underlined:[...document.querySelectorAll("a")].filter(a=>getComputedStyle(a).textDecorationLine.includes("underline")).length})');assert not report['nativeMath']['missing'] and not report['nativeMath']['underlined']
 capture('.hero','title.png');js('SelectPlayers.find(p=>p.model.id==="groups-example").show(5)');capture('[data-select-model="groups-example"]','groups.png');js('SelectPlayers.find(p=>p.model.id==="tournament-example").show(4)');capture('[data-select-model="tournament-example"]','tournament.png');js('let node=document.querySelector("#random").nextElementSibling;while(node&&!node.classList.contains("formula-block"))node=node.nextElementSibling;node.id="qa-expectation"');capture('#qa-expectation','math-proof.png');capture('[data-select-model="two-example"]','two-arrays.png')
 report['arrowPorts']=js('''(()=>{let checked=0;const bad=[];for(const p of SelectPlayers){for(const f of p.model.frames){const svg=document.createElement('div');svg.innerHTML=f.svg;const paths=[...svg.querySelectorAll('path[data-arrow]')];if(!paths.length)continue;p.show(p.model.frames.indexOf(f));const actual=p.host.querySelector('svg'),boxes=[...actual.querySelectorAll('rect')].filter(r=>r.getAttribute('fill')!=='none').map(r=>r.getBBox());for(const path of actual.querySelectorAll('path[data-arrow]')){for(const d of [0,path.getTotalLength()]){const q=path.getPointAtLength(d);if(!boxes.some(b=>q.x>=b.x-.1&&q.x<=b.x+b.width+.1&&q.y>=b.y-.1&&q.y<=b.y+b.height+.1&&Math.min(Math.abs(q.x-b.x),Math.abs(q.x-b.x-b.width),Math.abs(q.y-b.y),Math.abs(q.y-b.y-b.height))<.1))bad.push({model:p.model.id,point:[q.x,q.y]});checked++;}}}p.show(0);}return {checked,bad};})()''');assert not report['arrowPorts']['bad']
 js('window.p=SelectPlayers.find(p=>p.model.id==="partition-example");p.show(1);p.host.querySelector("[data-next]").click()');time.sleep(.15);js('p.pause();window.times=p.host.querySelector("svg").getAnimations({subtree:true}).map(a=>a.currentTime)');time.sleep(.15)
 report['pause']=js('({motions:times.length,frozen:JSON.stringify(times)===JSON.stringify(p.host.querySelector("svg").getAnimations({subtree:true}).map(a=>a.currentTime))})');assert report['pause']['motions']>0 and report['pause']['frozen']
 js('p.host.querySelector("[data-play]").click()');time.sleep(.15);report['resume']=js('p.host.querySelector("svg").getAnimations({subtree:true}).some(a=>a.currentTime>times[0])');assert report['resume'];js('p.pause();p.show(4);p.host.querySelector("[data-prev]").click()');assert js('p.index')==3
 js('p.host.querySelector("[data-seek]").value=5;p.host.querySelector("[data-seek]").dispatchEvent(new Event("input"))');assert js('p.index')==5
 js('p.host.querySelector("[data-reset]").click()');assert js('p.index')==0
 cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]});js('p.show(1);p.host.querySelector("[data-next]").click()');assert js('p.host.querySelector("svg").getAnimations({subtree:true}).length')==0;report['reducedMotion']=True
 js('p.print()');assert js('p.host.querySelectorAll(".select-print figure").length')==js('p.model.frames.length');js('p.clearPrint()');report['printCheckpoints']=True
 fixtures=[('lower','1,3,3,7','3','',1),('upper','1,3,3,7','3','',3),('quick','9,3,5,1,8,5,2,7','6','',7),('deterministic','9,2,6,5,1,8,7,3,4','7','',7),('two','1,4,9','4','2,3,7,10',4),('weighted','1,5,5,8','1','2,2,3,3',5),('groups','9,1,8,2,7,3,6,4,5,10','1','',5),('tournament','5,1,9,4,8,2,7,3','1','',8)]
 report['labs']=[]
 for kind,v,param,other,expected in fixtures:
  val=js('''(()=>{const f=document.querySelector('#select-form');f.elements.kind.value='''+json.dumps(kind)+''';f.elements.values.value='''+json.dumps(v)+''';f.elements.parameter.value='''+json.dumps(param)+''';f.elements.other.value='''+json.dumps(other)+''';f.dispatchEvent(new Event('submit',{cancelable:true,bubbles:true}));const r=SelectLab.model.result;return {error:document.querySelector('#select-error').textContent,result:typeof r==='object'?(r.second??r.pivot):r};})()''');assert not val['error'] and val['result']==expected,(kind,val,expected);report['labs'].append(dict(mode=kind,**val))
 js('window.previousModel=SelectLab;const f=document.querySelector("#select-form");f.elements.kind.value="lower";f.elements.values.value="3,1,2";f.dispatchEvent(new Event("submit",{cancelable:true}))');assert js('SelectLab===previousModel && document.querySelector("#select-error").textContent.length>0');report['invalidPreservesPrevious']=True
 cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=True));report['mobileOverflow']=js('document.documentElement.scrollWidth>innerWidth+1');assert not report['mobileOverflow'];capture('[data-select-model="binary-example"]','mobile-binary.png')
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Emulation.setEmulatedMedia',{'media':'print'});js('p.print()');report['printVisible']=js('getComputedStyle(p.host.querySelector(".select-print")).display!=="none"');assert report['printVisible'];capture('[data-select-model="partition-example"]','print-partition.png')
 report['runtimeErrors']=js('__errors');assert not report['runtimeErrors'];report['status']='passed'
finally:
 (R/'research/a_select-evidence/browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');server.shutdown();proc.terminate()
print(json.dumps({k:v for k,v in report.items() if k not in ['geometry','labs']}))
