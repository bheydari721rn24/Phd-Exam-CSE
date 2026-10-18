"""Real Edge geometry, algorithm, interaction, mobile, typography and print checks."""
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from itertools import product
import base64,hashlib,json,subprocess,tempfile,threading,time,uuid
import requests,websocket
from csp_exact import CSP,ac3
R=Path(__file__).resolve().parents[1];E=R/'research/i_csp-evidence';E.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=Path(tempfile.gettempdir())/('csp-qa-'+uuid.uuid4().hex)
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report={}
try:
 for _ in range(150):
  try:port=int((profile/'DevToolsActivePort').read_text().splitlines()[0]);break
  except(OSError,ValueError,IndexError):time.sleep(.1)
 pg=next(p for p in requests.get(f'http://127.0.0.1:{port}/json').json()if p['type']=='page');ws=websocket.create_connection(pg['webSocketDebuggerUrl'],timeout=120)
 def cdp(method,params=None):
  global seq
  seq+=1;ws.send(json.dumps(dict(id=seq,method=method,params=params or{})))
  while True:
   r=json.loads(ws.recv())
   if r.get('id')==seq:
    assert 'error'not in r,r
    return r.get('result',{})
 def js(code):
  r=cdp('Runtime.evaluate',dict(expression=code,returnByValue=True,awaitPromise=True));assert 'exceptionDetails'not in r,r;return r.get('result',{}).get('value')
 def capture(sel,name):
  js('document.querySelector('+json.dumps(sel)+').scrollIntoView({block:"center",behavior:"instant"})');js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');(E/name).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"})
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1000,deviceScaleFactor=1,mobile=False));url=f'http://127.0.0.1:{server.server_port}/chapters/i_csp.html';cdp('Page.navigate',{'url':url})
 for _ in range(150):
  if js('document.readyState==="complete"&&!!window.__cspTeaching'):break
  time.sleep(.1)
 assert js('!!window.__cspTeaching'),'Teaching script did not initialize'
 js('Promise.all([...document.fonts].map(f=>f.load()))');js('document.fonts.ready');js('document.querySelectorAll("details").forEach(d=>d.open=true)')
 report['inventory']=js('({questions:document.querySelectorAll(".exam-question").length,solutions:document.querySelectorAll(".exam-solution").length,players:__cspTeaching.players.length,models:__cspTeaching.models.size,specials:__cspTeaching.specials.length,math:document.querySelectorAll("math").length})');assert report['inventory']==dict(questions=54,solutions=54,players=28,models=26,specials=5,math=749),report['inventory']
 report['frames']=js('''(()=>{const out=[];for(const p of __cspTeaching.players){for(const id of p.ids){const s=p.host.querySelector('[data-case]');if(s){s.value=id;s.dispatchEvent(new Event('change'));}for(let k=0;k<p.model.frames.length;k++){p.go(k);const svg=p.host.querySelector('.csp-stage svg'),issues=[];for(const g of svg.querySelectorAll('.csp-node')){const r=g.querySelector('rect'),x=+r.getAttribute('x'),y=+r.getAttribute('y'),w=+r.getAttribute('width'),h=+r.getAttribute('height');for(const t of g.querySelectorAll('text')){const b=t.getBBox();if(b.x<x+7||b.x+b.width>x+w-7||b.y<y+7||b.y+b.height>y+h-7)issues.push('Text touches card:'+t.textContent);}}for(const edge of svg.querySelectorAll('.csp-edge,.csp-active')){for(const [at,name]of[[0,edge.dataset.from],[edge.getTotalLength(),edge.dataset.to]]){const pt=edge.getPointAtLength(at),r=svg.querySelector('[data-variable="'+name+'"] rect'),x=+r.getAttribute('x'),y=+r.getAttribute('y'),w=+r.getAttribute('width'),h=+r.getAttribute('height');const onVertical=Math.min(Math.abs(pt.x-x),Math.abs(pt.x-x-w))<.05&&pt.y>=y-.05&&pt.y<=y+h+.05,onHorizontal=Math.min(Math.abs(pt.y-y),Math.abs(pt.y-y-h))<.05&&pt.x>=x-.05&&pt.x<=x+w+.05;if(!onVertical&&!onHorizontal)issues.push('Detached connector:'+name);}}const f=p.model.frames[k],rows=p.host.querySelectorAll('.csp-supports tbody tr');if(rows.length!==f.supports.length)issues.push('Support table count differs');if(p.host.querySelector('.csp-queue').textContent.includes('undefined'))issues.push('Undefined queue');out.push({model:id,checkpoint:k,issues});}}const s=p.host.querySelector('[data-case]');if(s){s.value=p.ids[0];s.dispatchEvent(new Event('change'));}p.go(0);}return out;})()''')
 bad=[x for x in report['frames']if x['issues']]
 if bad:capture('.csp-player','geometry-failure.png')
 assert not bad,bad[:8]
 report['controls']=js('''(()=>{const out=[];for(const p of __cspTeaching.players){const h=p.host;p.go(0);h.querySelector('[data-next]').click();const next=p.index;h.querySelector('[data-prev]').click();const prev=p.index;const seek=h.querySelector('[data-seek]');seek.value=seek.max;seek.dispatchEvent(new Event('input'));const last=p.index;h.querySelector('[data-first]').click();out.push({model:p.model.id,next,prev,last,reset:p.index,ok:next===1&&prev===0&&last===p.model.frames.length-1&&p.index===0});}return out;})()''');assert all(x['ok']for x in report['controls'])
 report['playback']=js('''(async()=>{const out=[];for(const p of [__cspTeaching.players[0],__cspTeaching.players[4],__cspTeaching.players.at(-1)]){p.host.scrollIntoView({block:'center',behavior:'instant'});p.host.querySelector('[data-speed]').value='500';p.go(0);p.host.querySelector('[data-play]').click();await new Promise(r=>setTimeout(r,1150));const moved=p.index>=1;if(p.timer)p.host.querySelector('[data-play]').click();out.push({model:p.model.id,moved,paused:!p.timer});p.go(0);}return out;})()''');assert all(x['moved']and x['paused']for x in report['playback'])
 # Independent Python closure results for every three-variable Boolean binary relation system.
 cases=[];pairs=list(product([0,1],repeat=2));tables=[[list(p)for i,p in enumerate(pairs)if m>>i&1]for m in range(16)]
 for a,b,c in product(range(16),repeat=3):
  raw=dict(domains={v:[0,1]for v in 'ABC'},constraints=[dict(x=x,y=y,allowed=tables[k])for(x,y),k in zip([('A','B'),('A','C'),('B','C')],[a,b,c])]);ok,D,_=ac3(CSP(raw['domains'],raw['constraints']),record=False);cases.append([raw,ok,D])
 report['labExact']=js('''(()=>{let checked=0;for(const[raw,ok,D]of '''+json.dumps(cases,separators=(',',':'))+'''){const m=__cspTeaching.run(raw),last=m.frames.at(-1);if(m.failed===ok||JSON.stringify(last.domains)!==JSON.stringify(D))throw Error('Laboratory differs from exact Python closure');checked++;}return{checked};})()''');assert report['labExact']['checked']==4096
 report['labEndpoints']=js('''(()=>{const out=[];for(const raw of [{domains:{},constraints:[]},{domains:{X:[]},constraints:[]},{domains:{X:[-9,0,9]},constraints:[]},{domains:{X:[0,1],Y:[0,1]},constraints:[{x:'X',y:'Y',allowed:[[0,0],[1,1]]},{x:'Y',y:'X',allowed:[[0,1],[1,0]]}]}]){const m=__cspTeaching.run(raw);out.push({failed:m.failed,domains:m.frames.at(-1).domains});}return out;})()''');assert [x['failed']for x in report['labEndpoints']]==[False,True,False,True]
 report['invalidInputs']=js('''(()=>{const out=[];for(const raw of [null,{}, {domains:{x:[1]},constraints:[]},{domains:{X:[1,1]},constraints:[]},{domains:{X:[10]},constraints:[]},{domains:{X:[1.5]},constraints:[]},{domains:{X:[1]},constraints:[{x:'X',y:'X',allowed:[[1,1]]}]},{domains:{X:[1]},constraints:[{x:'X',y:'Y',allowed:[]}]},{domains:{X:[1],Y:[1]},constraints:[{x:'X',y:'Y',allowed:[[1,2]]}]}]){let rejected=false;try{__cspTeaching.run(raw)}catch(e){rejected=true}out.push(rejected);}const h=document.querySelector('.csp-lab'),t=h.querySelector('textarea'),saved=t.value;t.value='{bad JSON';h.querySelector('[data-run]').click();out.push(h.querySelector('.csp-error').textContent.startsWith('Input not run:'));t.value=saved;h.querySelector('[data-run]').click();return out;})()''');assert all(report['invalidInputs'])
 report['specials']=js('''(()=>{const out=[];for(const h of document.querySelectorAll('[data-special="queens"]')){const r=h.querySelector('input'),scores=[];for(let n=1;n<=4;n++){r.value=n;r.dispatchEvent(new Event('input'));scores.push(+h.dataset.conflicts);}r.value=1;r.dispatchEvent(new Event('input'));h.querySelector('button').click();const solved=+h.dataset.conflicts===0;h.querySelector('button').click();const other=+h.dataset.conflicts===0;h.querySelector('button').click();out.push({type:'queens',scores,solved,other});}for(const h of document.querySelectorAll('[data-special="hall"]')){const seq=[];for(let n=0;n<5;n++){seq.push(+h.dataset.step);h.querySelector('button').click();}out.push({type:'hall',seq});}return out;})()''');assert all(x['scores']==[4,2,2,2]and x['solved']and x['other']if x['type']=='queens'else x['seq']==[0,1,2,3,0]for x in report['specials'])
 report['fonts']=js('({prose:document.fonts.check("17px \'Source Sans 3\'"),heading:document.fonts.check("28px Newsreader"),math:document.fonts.check("18px \'STIX Two Math\'"),code:document.fonts.check("15px \'JetBrains Mono\'"),mathFamily:getComputedStyle(document.querySelector("math")).fontFamily,codeFamily:getComputedStyle(document.querySelector("pre code")).fontFamily})');assert all(report['fonts'][x]for x in ['prose','heading','math','code'])and 'STIX Two Math'in report['fonts']['mathFamily']and 'JetBrains Mono'in report['fonts']['codeFamily']
 report['widths']=[]
 for width in [390,768,1360]:
  cdp('Emulation.setDeviceMetricsOverride',dict(width=width,height=1000,deviceScaleFactor=1,mobile=False));js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');row=js('({width:innerWidth,scroll:document.documentElement.scrollWidth})');report['widths'].append(row)
  if row['scroll']>width:
   report['overflow']=js('[...document.querySelectorAll("p,div,section,math,pre,table")].map(e=>({tag:e.localName,cls:e.className,text:e.textContent.slice(0,90),right:e.getBoundingClientRect().right})).filter(x=>x.right>innerWidth+3).slice(0,20)');capture('body','overflow.png')
  assert row['scroll']<=width,row
 assert js('[...document.querySelectorAll("a,summary")].every(e=>getComputedStyle(e).textDecorationLine==="none")')
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1000,deviceScaleFactor=1,mobile=False));capture('#IC10 .csp-player','rollback-desktop.png');capture('[data-special="hall"]','hall-matching.png');capture('#MS_CE_1404_Q73 .csp-map','authentic-map.png')
 cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=1000,deviceScaleFactor=1,mobile=False));capture('#MS_CE_1404_Q75 .csp-player','numeric-mobile.png');capture('#IC49','cycle-formula-mobile.png')
 js('document.querySelectorAll("details").forEach(d=>d.open=false);dispatchEvent(new Event("beforeprint"))');cdp('Emulation.setEmulatedMedia',{'media':'print'});report['print']=js('({openSolutions:document.querySelectorAll("details.exam-solution[open]").length,printGraphs:document.querySelectorAll(".csp-print svg").length,printBlocks:[...document.querySelectorAll(".csp-print")].every(e=>getComputedStyle(e).display!=="none")})');assert report['print']['openSolutions']==54 and report['print']['printGraphs']>=52 and report['print']['printBlocks'];cdp('Emulation.setEmulatedMedia',{'media':'screen'});js('dispatchEvent(new Event("afterprint"))');assert js('document.querySelectorAll("details[open]").length')==0
 report['errors']=js('__errors');assert not report['errors'],report['errors']
 report['inputSha256']={p:hashlib.sha256((R/p).read_bytes()).hexdigest()for p in ['dist/chapters/i_csp.html','dist/chapters/i_csp.css','dist/chapters/i_csp.js']};report['status']='passed_actual_browser_checks';report['limits']='Current Edge; all declared states, finite independent laboratory cases, actual controls and print DOM/CSS. Not every browser or full PDF pagination.'
finally:
 server.shutdown();server.server_close()
 try:cdp('Browser.close')
 except Exception:pass
 proc.terminate();(E/'browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print({k:v for k,v in report.items()if k not in ['frames','controls']})
