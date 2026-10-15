"""Owned portable Edge session: every finite model, controls, layout and print."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,threading,time
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import requests,websocket
R=Path(__file__).resolve().parents[1];E=R/'research/l_projection-evidence';tmp=Path(tempfile.gettempdir())/'projection-qa';tmp.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=tmp/f'edge-{os.getpid()}';proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL);seq=0;report={}
try:
 for _ in range(100):
  if(profile/'DevToolsActivePort').exists():break
  time.sleep(.1)
 port=int((profile/'DevToolsActivePort').read_text().splitlines()[0]);page=next(p for p in requests.get(f'http://127.0.0.1:{port}/json').json()if p['type']=='page');ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=60)
 def cdp(m,p=None):
  global seq
  seq+=1;ws.send(json.dumps({'id':seq,'method':m,'params':p or{}}))
  while True:
   r=json.loads(ws.recv())
   if r.get('id')==seq:assert'error'not in r,r;return r.get('result',{})
 def js(code):
  r=cdp('Runtime.evaluate',{'expression':code,'returnByValue':True,'awaitPromise':True});assert'exceptionDetails'not in r,r;return r.get('result',{}).get('value')
 def screenshot(selector,name):
  js('document.querySelector('+json.dumps(selector)+').scrollIntoView({block:"center",behavior:"instant"})');js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');(E/name).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"});cdp('Emulation.setDeviceMetricsOverride',{'width':1360,'height':1000,'deviceScaleFactor':1,'mobile':False});url=f'http://127.0.0.1:{server.server_port}/chapters/l_projection.html';cdp('Page.navigate',{'url':url})
 for _ in range(100):
  if js('location.href==='+json.dumps(url)+'&&document.readyState==="complete"&&window.ProjectionPlayers?.length===13'):break
  time.sleep(.1)
 js('Promise.all([...document.fonts].map(f=>f.load()))');js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(d=>d.open=true)')
 report['fonts']=js('({prose:document.fonts.check("17px \'Source Sans 3\'"),headings:document.fonts.check("28px Newsreader"),math:document.fonts.check("18px \'STIX Two Math\'"),code:document.fonts.check("16px \'JetBrains Mono\'")})');assert all(report['fonts'].values()),report
 screenshot('.hero','chapter-title.png');screenshot('#problem-1 .pr-model','plane-problem.png');screenshot('#problem-25 .pr-model','weighted-affine.png')
 report['frames']=js(r'''(()=>{let count=0,bad=[];for(const p of ProjectionPlayers){for(let k=0;k<p.data.length;k++){p.show(k);const svg=p.host.querySelector('svg');count++;if(p.host.dataset.certificate!=='true')bad.push({kind:'certificate',k});const text=[...svg.querySelectorAll('text')];for(const t of text){const b=t.getBBox();if(b.x<4||b.x+b.width>756||b.y<4||b.y+b.height>326)bad.push({kind:'bounds',text:t.textContent,k});for(const r of svg.querySelectorAll('rect')){const x=r.x.baseVal.value,y=r.y.baseVal.value,w=r.width.baseVal.value,h=r.height.baseVal.value;if(b.x>=x&&b.x+b.width<=x+w&&b.y>=y&&b.y+b.height<=y+h){if(Math.min(b.x-x,x+w-b.x-b.width,b.y-y,y+h-b.y-b.height)<8)bad.push({kind:'padding',text:t.textContent,k});}}}for(let i=0;i<text.length;i++)for(let j=i+1;j<text.length;j++){const a=text[i].getBBox(),b=text[j].getBBox();if(Math.min(a.x+a.width,b.x+b.width)-Math.max(a.x,b.x)>1&&Math.min(a.y+a.height,b.y+b.height)-Math.max(a.y,b.y)>1)bad.push({kind:'textOverlap',texts:[text[i].textContent,text[j].textContent],k});}for(const edge of svg.querySelectorAll('[marker-end]')){const ref=edge.getAttribute('marker-end').match(/#([^)]*)/)[1];if(!svg.querySelector('[id="'+ref+'"]'))bad.push({kind:'missingMarker',k});}}p.show(0);}return{checkpoints:count,issues:bad};})()''');assert not report['frames']['issues'],report['frames']['issues'][:20]
 report['controls']=js('''(()=>{const out=[];for(const p of ProjectionPlayers){p.show(0);p.host.querySelector('[data-next]').click();const next=p.index===1;p.host.querySelector('[data-prev]').click();const prev=p.index===0;const s=p.host.querySelector('[data-seek]');s.value=p.data.length-1;s.dispatchEvent(new Event('input'));const seek=p.index===p.data.length-1;p.host.querySelector('[data-reset]').click();out.push({next,prev,seek,reset:p.index===0});}return out;})()''');assert all(all(r.values())for r in report['controls'])
 report['staticFigures']=js('''(()=>{const issues=[];for(const svg of document.querySelectorAll('.pr-static>svg'))for(const t of svg.querySelectorAll('text')){const b=t.getBBox();if(b.x<4||b.y<4||b.x+b.width>756||b.y+b.height>326)issues.push(t.textContent);}return{count:document.querySelectorAll('.pr-static>svg').length,issues};})()''');assert report['staticFigures']['count']==2 and not report['staticFigures']['issues'],report['staticFigures']
 screenshot('#problem-2 .pr-static','coefficient-space.png');screenshot('#problem-34 .pr-static','function-space.png')
 # Exercise real timer-driven playback, not just the public show method.
 report['playback']=js('''(async()=>{const out=[];for(const p of ProjectionPlayers.slice(0,5)){p.show(0);p.host.querySelector('[data-play]').click();await new Promise(r=>setTimeout(r,1700));p.host.querySelector('[data-play]').click();out.push(p.index>=1);p.stop();p.show(0);}return out;})()''');assert all(report['playback'])
 report['explorer']=js('''(()=>{const f=document.getElementById('pr-explorer'),out=[];for(const [angle,x,y,weight]of[[0,0,1,1],[90,2,-1,1],[45,2,-1,4],[30,-3,2,2]]){Object.entries({angle,x,y,weight}).forEach(([k,v])=>f.elements[k].value=v);f.dispatchEvent(new Event('submit',{cancelable:true}));out.push({certificate:ProjectionExplorer.data.every(x=>x.certificate),frames:ProjectionExplorer.data.length});}const html=document.getElementById('pr-explorer-output').innerHTML;f.elements.weight.value=0;f.dispatchEvent(new Event('submit',{cancelable:true}));return{valid:out,invalidError:document.getElementById('pr-error').textContent,preserved:html===document.getElementById('pr-explorer-output').innerHTML};})()''');assert all(x['certificate']for x in report['explorer']['valid'])and report['explorer']['invalidError']and report['explorer']['preserved']
 report['widths']=[]
 for width in[390,768,1360]:
  cdp('Emulation.setDeviceMetricsOverride',{'width':width,'height':1000,'deviceScaleFactor':1,'mobile':False});js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');r=js('({width:innerWidth,document:document.documentElement.scrollWidth,underlined:[...document.querySelectorAll("a")].filter(a=>getComputedStyle(a).textDecorationLine.includes("underline")).length,splitDisplayTables:[...document.querySelectorAll(".formula-block>math>mtable")].length})');report['widths'].append(r);assert r['document']<=r['width']and not r['underlined'],r
 screenshot('#problem-18 .pr-model','alternating-mobile.png')
 cdp('Emulation.setEmulatedMedia',{'media':'print'});js('dispatchEvent(new Event("beforeprint"))');report['print']=js('({opened:[...document.querySelectorAll(".exam-solution")].every(d=>d.open),keyframeFigures:document.querySelectorAll(".pr-print figure").length,visible:getComputedStyle(document.querySelector(".pr-print")).display})');assert report['print']['opened']and report['print']['keyframeFigures']>=26 and report['print']['visible']=='block'
 report['errors']=js('__errors');assert not report['errors'],report['errors'];report['status']='passed_owned_browser_review';report['modelPlacements']=13
finally:
 server.shutdown();server.server_close();proc.terminate()
 try:proc.wait(timeout=10)
 except subprocess.TimeoutExpired:proc.kill()
 (E/'browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(report)
