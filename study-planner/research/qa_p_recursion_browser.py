from pathlib import Path
import base64,json,os,subprocess,tempfile,threading,time,shutil
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'p-recursion-visual-qa';OUT.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=OUT/f'edge-{os.getpid()}';proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-firrc-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report=dict(topicId='p_recursion',status='in_progress',screenshots=str(OUT))
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
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"});cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/p_recursion.html'))
 for _ in range(100):
  if js('window.RecursionPlayers?.length'):break
  time.sleep(.1)
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,rules:document.querySelectorAll(".review-rule").length,players:RecursionPlayers.length,math:document.querySelectorAll("math").length})');assert report['counts']['questions']==81 and report['counts']['rules']==80
 report['fonts']=js('({math:getComputedStyle(document.querySelector("math")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),heading:document.fonts.check("18px Newsreader"),prose:document.fonts.check("18px \'Source Sans 3\'"),code:document.fonts.check("18px \'JetBrains Mono\'")})');assert all(report['fonts'][k]for k in['stix','heading','prose','code'])
 report['geometry']=js('''(()=>{const seen=new Set(),rows=[];for(const p of RecursionPlayers){if(seen.has(p.model.id))continue;seen.add(p.model.id);const bad=[];for(let i=0;i<p.model.frames.length;i++){p.show(i);const svg=p.host.querySelector('svg');bad.push(...DiagramLayout.audit(svg).map(x=>({...x,frame:i})));if(!p.teaching.root.dataset.explanation)bad.push({kind:'missing explanation'});for(const t of svg.querySelectorAll('text')){const a=DiagramLayout.box(svg,t);if(a.x<2||a.y<2||a.x+a.w>998||a.y+a.h>svg.viewBox.baseVal.height-2)bad.push({kind:'text outside plot',frame:i,text:t.textContent,bounds:a});const boxes=[...svg.querySelectorAll('rect')].map(r=>DiagramLayout.box(svg,r));const cx=a.x+a.w/2,cy=a.y+a.h/2,b=boxes.find(b=>cx>b.x&&cx<b.x+b.w&&cy>b.y&&cy<b.y+b.h);if(b){const pads=[a.x-b.x,b.x+b.w-a.x-a.w,a.y-b.y,b.y+b.h-a.y-a.h];if(Math.min(...pads)<6)bad.push({kind:'label padding',frame:i,text:t.textContent,pads});}}}rows.push({id:p.model.id,frames:p.model.frames.length,bad});p.show(0);}return {models:rows.length,frames:rows.reduce((n,r)=>n+r.frames,0),issues:rows.flatMap(r=>r.bad.map(x=>({...x,id:r.id})))};})()''')
 (R/'research/p_recursion-evidence/browser.json').write_text(json.dumps(report,indent=2)+'\n');assert not report['geometry']['issues'],report['geometry']['issues'][:25]
 report['mathGeometry']=js('''(()=>{const bare=[],clipped=[];for(const m of document.querySelectorAll('math')){for(const s of m.querySelectorAll('msup,msub,msubsup'))if([')',']','}'].includes(s.firstElementChild?.textContent))bare.push(m.getAttribute('aria-label'));for(const t of m.querySelectorAll('mo'))if(['(',')','[',']'].includes(t.textContent)){const r=t.getBoundingClientRect();if(!r.width||!r.height)clipped.push(t.textContent);}}return {bareClosingScriptBases:bare,zeroSizeFences:clipped,underlined:[...document.querySelectorAll('a')].filter(a=>getComputedStyle(a).textDecorationLine.includes('underline')).length};})()''');assert not report['mathGeometry']['bareClosingScriptBases']and not report['mathGeometry']['zeroSizeFences']and not report['mathGeometry']['underlined']
 for id,step,name in [('fact-four',3,'frames.png'),('fib-five',12,'tree.png'),('memo-six',20,'cache.png'),('hanoi-three',8,'pegs.png'),('subsets-three',13,'choices.png'),('koch-three',3,'geometry.png')]:
  js('RecursionPlayers.find(p=>p.model.id==='+json.dumps(id)+').show('+str(step)+')');capture('[data-rc-model="'+id+'"]',name)
 capture('.hero','title.png');capture('[data-source-id="p-recursion-original-80"]','synthesis-question.png');capture('.review-rule','final-rule.png')
 js('window.p=RecursionPlayers.find(p=>p.model.id==="hanoi-three");p.show(5);p.host.querySelector("[data-next]").click()');time.sleep(.12);js('p.pause();window.times=p.host.querySelector("svg").getAnimations({subtree:true}).map(a=>a.currentTime)');time.sleep(.1)
 report['pause']=js('({motions:times.length,frozen:JSON.stringify(times)===JSON.stringify(p.host.querySelector("svg").getAnimations({subtree:true}).map(a=>a.currentTime))})');assert report['pause']['motions']>0 and report['pause']['frozen']
 js('p.host.querySelector("[data-play]").click()');time.sleep(.12);report['resume']=js('p.host.querySelector("svg").getAnimations({subtree:true}).some(a=>a.currentTime>times[0])');assert report['resume'];js('p.pause();p.show(2);p.host.querySelector("[data-prev]").click()');assert js('p.index')==1
 js('p.host.querySelector("[data-seek]").value=2;p.host.querySelector("[data-seek]").dispatchEvent(new Event("input"))');assert js('p.index')==2
 js('p.host.querySelector("[data-reset]").click()');assert js('p.index')==0
 cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]});js('p.show(0);p.host.querySelector("[data-next]").click()');assert js('p.host.querySelector("svg").getAnimations({subtree:true}).length')==0;report['reducedMotion']=True
 js('p.print()');assert js('p.host.querySelectorAll(".rc-print figure").length')==js('p.model.frames.length');js('p.clearPrint()');report['printCheckpoints']=True
 report['labs']=[]
 for spec in [dict(operation='factorial',n=4),dict(operation='fib',n=5),dict(operation='memo',n=6),dict(operation='hanoi',n=3),dict(operation='subsets',n=3),dict(operation='palindrome',text='abca'),dict(operation='power',a=2,exponent=13),dict(operation='koch',n=3)]:
  obj=js('(()=>{const f=document.querySelector("#rc-form"),spec='+json.dumps(spec)+';for(const [k,v]of Object.entries(spec))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));const bad=[];for(let i=0;i<RecursionLab.model.frames.length;i++){RecursionLab.show(i);bad.push(...DiagramLayout.audit(RecursionLab.host.querySelector("svg")));}return {error:document.querySelector("#rc-error").textContent,result:RecursionLab.model.result,issues:bad};})()');assert not obj['error']and not obj['issues'],obj;report['labs'].append(obj)
 capture('#rc-output .rc-stage','editable-recursion.png')
 for change in [dict(n=-1),dict(n=9),dict(operation='fib',n=6),dict(operation='hanoi',n=5),dict(operation='palindrome',text='é'),dict(operation='power',a=4)]:
  js('(()=>{window.oldLab=RecursionLab;const f=document.querySelector("#rc-form"),base={operation:"factorial",n:3,a:2,b:462,exponent:13,value:738,text:"abccba",target:8},change='+json.dumps(change)+';for(const[k,v]of Object.entries({...base,...change}))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('RecursionLab===oldLab && document.querySelector("#rc-error").textContent.length>0')
 report['invalidPreservesPrevious']=6
 cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=True));report['mobileOverflow']=js('document.documentElement.scrollWidth>innerWidth+1');assert not report['mobileOverflow'];capture('[data-rc-model="fact-four"]','mobile-vacuum.png')
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Emulation.setEmulatedMedia',{'media':'print'});js('p.print()');report['printVisible']=js('getComputedStyle(p.host.querySelector(".rc-print")).display!=="none"');assert report['printVisible'];capture('[data-rc-model="hanoi-three"]','print-threshold.png')
 report['runtimeErrors']=js('__errors');assert not report['runtimeErrors']
 cdp('Emulation.setEmulatedMedia',{'media':'screen'});cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/index.html#library'))
 for _ in range(100):
  if js('document.querySelector("#library a[href=\\"chapters/p_recursion.html\\"]")!==null'):break
  time.sleep(.1)
 report['library']=js('({cards:document.querySelectorAll(".library-card").length,visible:!document.querySelector("#view-lessons").hidden,errors:__errors})');assert report['library']['cards']==47 and report['library']['visible']and not report['library']['errors']
 js('location.hash="week-3"');js('new Promise(r=>setTimeout(r,100))');report['weeklyChapterLink']=js('!document.querySelector("#view-weeks").hidden && document.querySelector("#week-detail a[href=\\"chapters/p_recursion.html\\"]")!==null');assert report['weeklyChapterLink']
 report['status']='passed'
 for f in OUT.glob('*.png'):shutil.copy2(f,R/'research/p_recursion-evidence'/f.name)
finally:
 (R/'research/p_recursion-evidence/browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');server.shutdown();proc.terminate()
print(json.dumps({k:v for k,v in report.items()if k not in['geometry','labs']}))
