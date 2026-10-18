"""Actual Edge checks for all serialized tree states and dedicated teaching controls."""
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import base64,hashlib,json,subprocess,tempfile,threading,time,uuid
import requests,websocket
R=Path(__file__).resolve().parents[1];E=R/'research/i_games-evidence';E.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=Path(tempfile.gettempdir())/('games-qa-'+uuid.uuid4().hex)
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report={}
try:
 for _ in range(150):
  try:port=int((profile/'DevToolsActivePort').read_text().splitlines()[0]);break
  except(OSError,ValueError,IndexError):time.sleep(.1)
 pg=next(p for p in requests.get(f'http://127.0.0.1:{port}/json').json()if p['type']=='page');ws=websocket.create_connection(pg['webSocketDebuggerUrl'],timeout=120)
 def cdp(method,params=None):
  global seq
  seq+=1;ws.send(json.dumps({'id':seq,'method':method,'params':params or {}}))
  while True:
   r=json.loads(ws.recv())
   if r.get('id')==seq:
    assert 'error'not in r,r
    return r.get('result',{})
 def js(code):
  r=cdp('Runtime.evaluate',{'expression':code,'returnByValue':True,'awaitPromise':True});assert 'exceptionDetails'not in r,r;return r.get('result',{}).get('value')
 def capture(sel,name):
  js('document.querySelector('+json.dumps(sel)+').scrollIntoView({block:"center",behavior:"instant"})');js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');(E/name).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"})
 cdp('Emulation.setDeviceMetricsOverride',{'width':1360,'height':1000,'deviceScaleFactor':1,'mobile':False});url=f'http://127.0.0.1:{server.server_port}/chapters/i_games.html';cdp('Page.navigate',{'url':url})
 for _ in range(150):
  if js('location.href==='+json.dumps(url)+'&&document.readyState==="complete"&&!!window.__gamesTeaching'):break
  time.sleep(.1)
 js('Promise.all([...document.fonts].map(f=>f.load()))');js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(d=>d.open=true)')
 report['inventory']=js('({questions:document.querySelectorAll(".exam-question").length,solutions:document.querySelectorAll("details.exam-solution").length,players:__gamesTeaching.players.length,models:__gamesTeaching.models.size,math:document.querySelectorAll("math").length})')
 assert report['inventory']=={'questions':52,'solutions':52,'players':17,'models':27,'math':533},report['inventory']
 report['frames']=js('''(()=>{const out=[];for(const p of __gamesTeaching.players){for(const id of p.models){const select=p.host.querySelector('[data-case]');if(select){select.value=id;select.dispatchEvent(new Event('change'));}const model=__gamesTeaching.models.get(id),seek=p.host.querySelector('[data-seek]');for(let k=0;k<model.frames.length;k++){seek.value=k;seek.dispatchEvent(new Event('input'));const svg=p.host.querySelector('.game-stage svg'),issues=[];for(const g of svg.querySelectorAll('.game-node')){const box=g.querySelector('rect'),x=+box.getAttribute('x'),y=+box.getAttribute('y'),w=+box.getAttribute('width'),h=+box.getAttribute('height');for(const t of g.querySelectorAll('text')){const b=t.getBBox();if(b.x<x+4||b.x+b.width>x+w-4||b.y<y+4||b.y+b.height>y+h-4)issues.push({node:g.dataset.node,text:t.textContent,b:{x:b.x,y:b.y,w:b.width,h:b.height},box:{x,y,w,h}});}}for(const edge of svg.querySelectorAll('.game-edge')){const a=model.nodes.find(n=>n.id===edge.dataset.from),b=model.nodes.find(n=>n.id===edge.dataset.to),start=edge.getPointAtLength(0),end=edge.getPointAtLength(edge.getTotalLength());if(Math.hypot(start.x-a.x,start.y-a.y-62)>.05||Math.hypot(end.x-b.x,end.y-b.y)>.05)issues.push({edge:edge.dataset,detached:true});}for(const t of svg.querySelectorAll('text')){const b=t.getBBox();if(b.x<0||b.y<0||b.x+b.width>model.width||b.y+b.height>model.height)issues.push({outOfCanvas:t.textContent});}out.push({model:id,checkpoint:k,issues});}p.host.querySelector('[data-first]').click();}const select=p.host.querySelector('[data-case]');if(select){select.value=p.models[0];select.dispatchEvent(new Event('change'));}}return out;})()''')
 assert len(report['frames'])==815
 bad=[x for x in report['frames']if x['issues']]
 if bad:capture('.game-player','geometry-failure.png')
 assert not bad,bad[:5]
 report['controls']=js('''(()=>{const out=[];for(const p of __gamesTeaching.players){const h=p.host,s=h.querySelector('[data-seek]');h.querySelector('[data-first]').click();h.querySelector('[data-next]').click();const next=p.checkpoint;h.querySelector('[data-prev]').click();const prev=p.checkpoint;s.value=s.max;s.dispatchEvent(new Event('input'));const last=p.checkpoint;h.querySelector('[data-first]').click();out.push({model:p.model,next,prev,last,reset:p.checkpoint,ok:next===1&&prev===0&&last===__gamesTeaching.models.get(p.model).frames.length-1&&p.checkpoint===0});}return out;})()''')
 assert all(x['ok']for x in report['controls'])
 report['windowRoles']=js('''(()=>{const out=[];for(const m of __gamesTeaching.models.values())for(const f of m.frames){if(!f.window)continue;const expected=f.caption.startsWith('Enter ')?'incoming':f.caption.startsWith('Return ')?'classification':'current';if(f.windowRole!==expected)throw Error('Window role differs from checkpoint meaning: '+m.id);out.push(f.windowRole);}return{checked:out.length,incoming:out.filter(x=>x==='incoming').length,current:out.filter(x=>x==='current').length,classification:out.filter(x=>x==='classification').length};})()''')
 assert all(report['windowRoles'][k]>0 for k in ['incoming','current','classification'])
 report['playback']=js('''(async()=>{const out=[];for(const p of [__gamesTeaching.players[0],__gamesTeaching.players[6],__gamesTeaching.players.at(-1)]){p.host.scrollIntoView({block:'center',behavior:'instant'});p.host.querySelector('[data-speed]').value='500';p.host.querySelector('[data-first]').click();p.host.querySelector('[data-play]').click();await new Promise(r=>setTimeout(r,1200));const moved=p.checkpoint>=1;p.host.querySelector('[data-play]').click();const stopped=p.host.querySelector('[data-play]').getAttribute('aria-pressed')==='false';out.push({model:p.model,moved,stopped});p.pause();}return out;})()''')
 assert all(x['moved']and x['stopped']for x in report['playback'])
 report['uct']=js('''(()=>{const h=document.querySelector('.game-uct'),r=h.querySelector('input'),out=[];for(const c of [0,1,2]){r.value=c;r.dispatchEvent(new Event('input'));out.push({c,selected:h.dataset.selected,caption:h.querySelector('.uct-caption').textContent});}r.value=1;r.dispatchEvent(new Event('input'));return out;})()''')
 assert [x['selected']for x in report['uct']]==['A','B','B']
 report['chanceSteps']=js('''(()=>{const h=document.querySelector('.game-chance-bounds'),out=[];for(let k=0;k<5;k++){out.push({step:+h.dataset.step,caption:h.querySelector('.bounds-caption').textContent});h.querySelector('button').click();}return out;})()''')
 assert [x['step']for x in report['chanceSteps']]==[0,1,2,3,0]
 report['fonts']=js('({prose:document.fonts.check("17px \'Source Sans 3\'"),heading:document.fonts.check("28px Newsreader"),math:document.fonts.check("18px \'STIX Two Math\'"),code:document.fonts.check("15px \'JetBrains Mono\'"),mathFamily:getComputedStyle(document.querySelector("math")).fontFamily,codeFamily:getComputedStyle(document.querySelector("pre code")).fontFamily})')
 assert all(report['fonts'][x]for x in ['prose','heading','math','code'])and 'STIX Two Math'in report['fonts']['mathFamily']and 'JetBrains Mono'in report['fonts']['codeFamily']
 report['widths']=[]
 for width in [390,768,1360]:
  cdp('Emulation.setDeviceMetricsOverride',{'width':width,'height':1000,'deviceScaleFactor':1,'mobile':False});js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');row=js('({width:innerWidth,scroll:document.documentElement.scrollWidth})');report['widths'].append(row)
  if row['scroll']>width:
   report['overflow']=js('[...document.querySelectorAll("p,div,section,math,pre")].map(e=>({tag:e.localName,cls:e.className,text:e.textContent.slice(0,90),right:e.getBoundingClientRect().right})).filter(x=>x.right>innerWidth+3).slice(0,15)');capture('body','overflow.png')
  assert row['scroll']<=width,row
 cdp('Emulation.setDeviceMetricsOverride',{'width':390,'height':1000,'deviceScaleFactor':1,'mobile':False})
 js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
 report['overview']=js('''(()=>{const p=__gamesTeaching.players.find(p=>p.model==='q5'),h=p.host,stage=h.querySelector('.game-stage'),seek=h.querySelector('[data-seek]');h.querySelector('[data-first]').click();const root=__gamesTeaching.models.get(p.model).nodes[0],rootVisible=root.x>=stage.scrollLeft&&root.x<=stage.scrollLeft+stage.clientWidth;const before=stage.scrollLeft;h.querySelector('.game-overview').dispatchEvent(new KeyboardEvent('keydown',{key:'ArrowRight',bubbles:true}));const keyboardMoved=stage.scrollLeft>before;seek.value=seek.max;seek.dispatchEvent(new Event('input'));const f=__gamesTeaching.models.get(p.model).frames.at(-1),active=__gamesTeaching.models.get(p.model).nodes.find(n=>n.id===f.active),activeVisible=active.x>=stage.scrollLeft&&active.x<=stage.scrollLeft+stage.clientWidth;h.querySelector('[data-first]').click();return{rootVisible,keyboardMoved,activeVisible};})()''')
 assert all(report['overview'].values()),report['overview']
 cdp('Emulation.setDeviceMetricsOverride',{'width':1360,'height':1000,'deviceScaleFactor':1,'mobile':False})
 assert js('[...document.querySelectorAll("a,summary")].every(e=>getComputedStyle(e).textDecorationLine==="none")')
 js('document.querySelector("#authentic-2 [data-seek]").value=document.querySelector("#authentic-2 [data-seek]").max;document.querySelector("#authentic-2 [data-seek]").dispatchEvent(new Event("input"))')
 capture('#authentic-2 .game-player','authentic-interval-tree.png');capture('.game-uct','uct-comparison.png')
 cdp('Emulation.setDeviceMetricsOverride',{'width':390,'height':1000,'deviceScaleFactor':1,'mobile':False});capture('#problem-5 .game-player','mobile-tree-player.png')
 js('document.querySelectorAll(".exam-solution").forEach(d=>d.open=false);dispatchEvent(new Event("beforeprint"))');cdp('Emulation.setEmulatedMedia',{'media':'print'})
 report['print']=js('({solutions:document.querySelectorAll(".exam-solution[open]").length,finalTrees:document.querySelectorAll(".game-final-print svg").length,visiblePrintTrees:[...document.querySelectorAll(".game-final-print")].every(e=>getComputedStyle(e).display!=="none")})')
 assert report['print']=={'solutions':52,'finalTrees':27,'visiblePrintTrees':True}
 cdp('Emulation.setEmulatedMedia',{'media':'screen'});js('dispatchEvent(new Event("afterprint"))');assert js('document.querySelectorAll(".exam-solution[open]").length')==0
 report['errors']=js('__errors');assert not report['errors'],report['errors']
 report['inputSha256']={rel:hashlib.sha256((R/rel).read_bytes()).hexdigest()for rel in ['dist/chapters/i_games.html','dist/chapters/i_games.js','dist/chapters/i_games.css']}
 report['status']='passed_actual_browser_checks';report['limits']='Current portable Edge and finite serialized states/controls; print DOM/CSS checked, not complete PDF pagination or every browser.'
finally:
 server.shutdown();server.server_close()
 try:cdp('Browser.close')
 except Exception:pass
 proc.terminate();(E/'browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print({k:v for k,v in report.items()if k not in ['frames','controls','chanceSteps','uct']})
