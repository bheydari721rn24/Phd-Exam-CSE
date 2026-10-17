"""Actual current Bayes page; every retained finite scene and new figure."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,threading,time
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import requests,websocket
R=Path(__file__).resolve().parents[1];E=R/'research/deep-library-revision/s_bayes-evidence';tmp=Path(tempfile.gettempdir())/'bayes-revision-qa';tmp.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=tmp/f'edge-{os.getpid()}';proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL);seq=0;report={}
try:
 for _ in range(100):
  if(profile/'DevToolsActivePort').exists():break
  time.sleep(.1)
 port=int((profile/'DevToolsActivePort').read_text().splitlines()[0]);pg=next(p for p in requests.get(f'http://127.0.0.1:{port}/json').json()if p['type']=='page');ws=websocket.create_connection(pg['webSocketDebuggerUrl'],timeout=60)
 def cdp(m,p=None):
  global seq
  seq+=1;ws.send(json.dumps({'id':seq,'method':m,'params':p or{}}))
  while True:
   r=json.loads(ws.recv())
   if r.get('id')==seq:assert'error'not in r,r;return r.get('result',{})
 def js(code):
  r=cdp('Runtime.evaluate',{'expression':code,'returnByValue':True,'awaitPromise':True});assert'exceptionDetails'not in r,r;return r.get('result',{}).get('value')
 def capture(sel,name):
  js('document.querySelector('+json.dumps(sel)+').scrollIntoView({block:"center",behavior:"instant"})');js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');(E/name).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"});cdp('Emulation.setDeviceMetricsOverride',{'width':1360,'height':1000,'deviceScaleFactor':1,'mobile':False});url=f'http://127.0.0.1:{server.server_port}/chapters/s_bayes.html';cdp('Page.navigate',{'url':url})
 for _ in range(100):
  if js('location.href==='+json.dumps(url)+'&&document.readyState==="complete"&&!!window.ConceptAnimations'):break
  time.sleep(.1)
 js('Promise.all([...document.fonts].map(f=>f.load()))');js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(d=>d.open=true)');js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))')
 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,answers:document.querySelectorAll(".exam-solution").length,rules:document.querySelectorAll(".review-rule").length,staticFigures:document.querySelectorAll(".pr-static").length,players:ConceptAnimations.players.length})');assert report['counts']['questions']==65 and report['counts']['answers']==65 and report['counts']['rules']==80 and report['counts']['staticFigures']==31
 report['fonts']=js('({prose:document.fonts.check("17px \'Source Sans 3\'"),math:document.fonts.check("18px \'STIX Two Math\'"),headings:document.fonts.check("28px Newsreader")})');assert all(report['fonts'].values())
 report['newFigureGeometry']=js('''(()=>{const bad=[];for(const svg of document.querySelectorAll('.pr-static>svg')){const ts=[...svg.querySelectorAll('text')];for(const t of ts){const b=t.getBBox();if(b.x<4||b.y<4||b.x+b.width>756||b.y+b.height>326)bad.push({kind:'bounds',text:t.textContent});for(const r of svg.querySelectorAll('rect')){const x=r.x.baseVal.value,y=r.y.baseVal.value,w=r.width.baseVal.value,h=r.height.baseVal.value;if(b.x>=x&&b.x+b.width<=x+w&&b.y>=y&&b.y+b.height<=y+h&&Math.min(b.x-x,x+w-b.x-b.width,b.y-y,y+h-b.y-b.height)<8)bad.push({kind:'padding',text:t.textContent});}}for(let i=0;i<ts.length;i++)for(let j=i+1;j<ts.length;j++){const a=ts[i].getBBox(),b=ts[j].getBBox();if(Math.min(a.x+a.width,b.x+b.width)-Math.max(a.x,b.x)>1&&Math.min(a.y+a.height,b.y+b.height)-Math.max(a.y,b.y)>1)bad.push({kind:'textOverlap',texts:[ts[i].textContent,ts[j].textContent]});}}return bad;})()''');assert not report['newFigureGeometry'],report['newFigureGeometry'][:20]
 report['finiteScenes']=js('''(()=>{const out=[];for(const p of ConceptAnimations.players){const first=p.scene;for(const scene of p.scenes){p.scene=scene;p.show(0);const issues=[];for(let k=0;k<scene.frames.length;k++){p.api.show(k);const svg=p.host.querySelector('svg');issues.push(...DiagramLayout.audit(svg).map(x=>({...x,k})));}out.push({id:scene.id,frames:scene.frames.length,issues});}p.scene=first;p.show(0);}return out;})()''');assert all(not x['issues']for x in report['finiteScenes']),[x for x in report['finiteScenes']if x['issues']][:3]
 report['controls']=js('''(()=>{const out=[];for(const p of ConceptAnimations.players){p.api.show(0);p.buttons.next.click();const next=Number(p.seek.value)===1;p.buttons.back.click();const previous=Number(p.seek.value)===0;p.seek.value=p.scene.frames.length-1;p.seek.dispatchEvent(new Event('input'));const seek=Number(p.seek.value)===p.scene.frames.length-1;p.buttons.reset.click();out.push({next,previous,seek,reset:Number(p.seek.value)===0});}return out;})()''');assert all(all(r.values())for r in report['controls'])
 report['playback']=js('''(async()=>{const out=[];for(const p of ConceptAnimations.players.slice(0,3)){p.host.scrollIntoView({block:'center',behavior:'instant'});await new Promise(r=>setTimeout(r,250));p.buttons.reset.click();p.buttons.play.click();await new Promise(r=>setTimeout(r,2300));const moved=Number(p.seek.value)>0;p.buttons.play.click();out.push({id:p.scene.id,moved});p.buttons.reset.click();}return out;})()''');assert all(x['moved']for x in report['playback'])
 report['widths']=[]
 for width in[390,768,1360]:
  cdp('Emulation.setDeviceMetricsOverride',{'width':width,'height':1000,'deviceScaleFactor':1,'mobile':False});r=js('({width:innerWidth,document:document.documentElement.scrollWidth,underlined:[...document.querySelectorAll("a")].filter(a=>getComputedStyle(a).textDecorationLine.includes("underline")).length})');report['widths'].append(r);assert r['document']<=width and not r['underlined'],r
 capture('[data-source-id="SB33"]','child-sampling.png');capture('[data-source-id="SB48"] .pr-static','dependence-tables.png');capture('[data-source-id="SB57"] .pr-static','posterior-density.png')
 report['posteriorLab']=js('''(()=>{const f=document.getElementById('bayes-form'),out=[];for(const a of[['1/100','9/10','1/20',1,'independent'],['1/10','4/5','1/5',2,'independent'],['1/10','4/5','1/5',2,'duplicate'],['1/2','0','0',1,'independent'],['0','0','0',0,'independent'],['1/10','4/5','1/5',20,'independent']]){['prior','target','background','reports','mode'].forEach((k,i)=>f.elements[k].value=a[i]);f.dispatchEvent(new Event('submit',{cancelable:true}));out.push({...document.getElementById('bayes-output').dataset});}return out;})()''');assert [r['posterior']for r in report['posteriorLab'][:5]]==['2/13','16/25','4/13','undefined','0']
 cdp('Emulation.setEmulatedMedia',{'media':'print'});js('dispatchEvent(new Event("beforeprint"))');report['print']=js('({openAnswers:[...document.querySelectorAll(".exam-solution")].filter(d=>d.open).length,figures:document.querySelectorAll("figure").length})');assert report['print']['openAnswers']==65
 report['errors']=js('__errors');assert not report['errors'],report['errors'];report['status']='passed_bayes_revision_browser_checks'
finally:
 server.shutdown();server.server_close();proc.terminate()
 try:proc.wait(timeout=10)
 except subprocess.TimeoutExpired:proc.kill()
 (E/'browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(report)
