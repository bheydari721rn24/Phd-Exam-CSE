"""Actual portable Edge inspection of every model, controls and exact explorer."""
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import base64,json,os,subprocess,tempfile,threading,time,uuid
import requests,websocket
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1];E=R/'research/l_leastsquares-evidence';E.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=Path(tempfile.gettempdir())/('least-squares-qa-'+uuid.uuid4().hex);proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL);seq=0;report={}
try:
 for _ in range(150):
  try:
   port=int((profile/'DevToolsActivePort').read_text().splitlines()[0]);break
  except (OSError,ValueError,IndexError):time.sleep(.1)
 pg=next(p for p in requests.get(f'http://127.0.0.1:{port}/json').json()if p['type']=='page');ws=websocket.create_connection(pg['webSocketDebuggerUrl'],timeout=60)
 def cdp(method,params=None):
  global seq
  seq+=1;ws.send(json.dumps({'id':seq,'method':method,'params':params or{}}))
  while True:
   r=json.loads(ws.recv())
   if r.get('id')==seq:assert'error'not in r,r;return r.get('result',{})
 def js(code):
  r=cdp('Runtime.evaluate',{'expression':code,'returnByValue':True,'awaitPromise':True});assert'exceptionDetails'not in r,r;return r.get('result',{}).get('value')
 def capture(sel,name):
  js('document.querySelector('+json.dumps(sel)+').scrollIntoView({block:"center",behavior:"instant"})');js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');(E/name).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"});cdp('Emulation.setDeviceMetricsOverride',{'width':1360,'height':1000,'deviceScaleFactor':1,'mobile':False});url=f'http://127.0.0.1:{server.server_port}/chapters/l_leastsquares.html';cdp('Page.navigate',{'url':url})
 for _ in range(150):
  if js('location.href==='+json.dumps(url)+'&&document.readyState==="complete"&&window.LeastSquaresPlayers?.length===20'):break
  time.sleep(.1)
 js('Promise.all([...document.fonts].map(f=>f.load()))');js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(d=>d.open=true)')
 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,rules:document.querySelectorAll(".review-rule").length,players:LeastSquaresPlayers.length})');assert report['counts']==dict(questions=51,rules=60,players=20)
 report['fonts']=js('({prose:document.fonts.check("17px \'Source Sans 3\'"),math:document.fonts.check("18px \'STIX Two Math\'"),heading:document.fonts.check("28px Newsreader"),code:document.fonts.check("15px \'JetBrains Mono\'")})');assert all(report['fonts'].values())
 report['frames']=js('''(()=>{const out=[];for(const p of LeastSquaresPlayers){for(let k=0;k<p.frames.length;k++){p.show(k);const svg=p.stage.querySelector('svg'),texts=[...svg.querySelectorAll('text')],issues=[];for(const t of texts){const b=t.getBBox();if(b.x<3||b.y<3||b.x+b.width>757||b.y+b.height>327)issues.push({kind:'bounds',text:t.textContent,b:{x:b.x,y:b.y,w:b.width,h:b.height}});}for(let i=0;i<texts.length;i++)for(let j=i+1;j<texts.length;j++){const a=texts[i].getBBox(),b=texts[j].getBBox();if(Math.min(a.x+a.width,b.x+b.width)-Math.max(a.x,b.x)>1&&Math.min(a.y+a.height,b.y+b.height)-Math.max(a.y,b.y)>1)issues.push({kind:'overlap',text:[texts[i].textContent,texts[j].textContent]});}out.push({kind:p.frames[k].kind,model:p.host.dataset.lsModel,k,issues});}p.show(0);}return out;})()''');assert all(not x['issues']for x in report['frames']),[x for x in report['frames']if x['issues']][:6]
 report['controls']=js('''(()=>{const out=[];for(const p of LeastSquaresPlayers){p.buttons.reset.click();if(p.frames.length===1){out.push({single:true,disabled:p.buttons.next.disabled&&p.buttons.prev.disabled});continue;}p.buttons.next.click();const next=p.index===1;p.buttons.prev.click();const previous=p.index===0;p.seek.value=p.frames.length-1;p.seek.dispatchEvent(new Event('input'));const seek=p.index===p.frames.length-1;p.buttons.reset.click();out.push({next,previous,seek,reset:p.index===0});}return out;})()''');assert all(all(x.values())for x in report['controls'])
 report['playback']=js('''(async()=>{const out=[];for(const p of LeastSquaresPlayers.slice(0,4)){p.host.scrollIntoView({block:'center',behavior:'instant'});p.buttons.reset.click();p.buttons.play.click();await new Promise(r=>setTimeout(r,1550));const advanced=p.index>0;p.pause();out.push({model:p.host.dataset.lsModel,advanced});p.show(0);}return out;})()''');assert all(x['advanced']for x in report['playback'])
 report['editableCases']=js('''(()=>{const f=document.getElementById('ls-explorer'),out=[];for(const model of ['line','constant'])for(const y of [[1,2,2],[-10,0,10],[0,0,0],[4,-3,1]])for(const w of [[1,1,1],[1,2,3],[9,1,4]]){for(let i=0;i<3;i++){f.elements['y'+i].value=y[i];f.elements['w'+i].value=w[i];}f.elements.model.value=model;f.dispatchEvent(new Event('submit',{cancelable:true}));out.push({model,y,w,...document.getElementById('ls-exact-output').dataset});}return out;})()''')
 for v in report['editableCases']:
  ts=[1,2,3];y=list(map(F,v['y']));w=list(map(F,v['w']));s=sum(w);st=sum(a*t for a,t in zip(w,ts));st2=sum(a*t*t for a,t in zip(w,ts));sy=sum(a*b for a,b in zip(w,y));sty=sum(a*t*b for a,t,b in zip(w,ts,y));det=s*st2-st*st
  c,d=(sy/s,F(0))if v['model']=='constant'else((st2*sy-st*sty)/det,(s*sty-st*sy)/det);res=[b-c-d*t for t,b in zip(ts,y)];err=sum(a*b*b for a,b in zip(w,res));assert F(v['c'])==c and F(v['d'])==d and F(v['sse'])==err and F(v['normal0'])==0 and(v['model']=='constant'or F(v['normal1'])==0),v
 report['invalidCase']=js('''(()=>{const f=document.getElementById('ls-explorer');f.elements.w0.value=0;f.dispatchEvent(new Event('submit',{cancelable:true}));return{valid:document.getElementById('ls-exact-output').dataset.valid,error:document.getElementById('ls-error').textContent};})()''');assert report['invalidCase']['valid']=='false'and report['invalidCase']['error']
 # Restore a valid original model before screenshots and printing.
 js('document.getElementById("ls-explorer").reset();document.getElementById("ls-explorer").dispatchEvent(new Event("submit",{cancelable:true}))')
 report['widths']=[]
 for width in[390,768,1360]:
  cdp('Emulation.setDeviceMetricsOverride',{'width':width,'height':1000,'deviceScaleFactor':1,'mobile':False});row=js('({width:innerWidth,scroll:document.documentElement.scrollWidth,underlined:[...document.querySelectorAll("a")].filter(a=>getComputedStyle(a).textDecorationLine.includes("underline")).length})');report['widths'].append(row);assert row['scroll']<=width and row['underlined']==0
 capture('.hero','title.png');capture('#problem-1 .ls-model','vertical-fit.png');capture('#problem-11 .ls-model','householder.png');capture('#problem-24 .ls-model','ridge.png');capture('#laboratory','exact-laboratory.png')
 cdp('Emulation.setEmulatedMedia',{'media':'print'});js('dispatchEvent(new Event("beforeprint"))');report['print']=js('({open:[...document.querySelectorAll(".exam-solution")].filter(d=>d.open).length,checkpoints:document.querySelectorAll(".ls-print figure").length})');assert report['print']['open']==51 and report['print']['checkpoints']==len(report['frames'])
 report['errors']=js('__errors');assert not report['errors'];report['status']='passed_leastsquares_browser_checks'
 cdp('Emulation.setEmulatedMedia',{'media':''});ieltsurl=f'http://127.0.0.1:{server.server_port}/ielts/academic-03-nouns.html';cdp('Page.navigate',{'url':ieltsurl})
 for _ in range(100):
  if js('location.href==='+json.dumps(ieltsurl)+'&&document.readyState==="complete"&&!!document.getElementById("reference-sentence")'):break
  time.sleep(.1)
 js('document.fonts.ready')
 report['ieltsReferenceCases']=js('''(()=>{const f=document.getElementById('reference-form'),out=[];for(const number of ['one','many'])for(const reference of ['new','known','near'])for(const noun of ['folder','apple','university card']){f.elements.number.value=number;f.elements.reference.value=reference;f.elements.noun.value=noun;f.dispatchEvent(new Event('submit',{cancelable:true}));out.push({number,reference,noun,sentence:document.getElementById('reference-sentence').textContent});}return out;})()''')
 for v in report['ieltsReferenceCases']:
  many=v['number']=='many';det='the'if v['reference']=='known'else('these'if many else'this')if v['reference']=='near'else'some'if many else'an'if v['noun']=='apple'else'a'
  noun=v['noun']+('s'if many else'');expected=det.capitalize()+' '+noun+(' are ready.'if many else' is ready.');assert v['sentence']==expected,v
 report['ieltsAudio']=js('''Promise.all([...document.querySelectorAll('audio')].map(a=>new Promise((resolve,reject)=>{const done=()=>resolve({src:a.getAttribute('src'),seconds:a.duration,ready:a.readyState});if(a.readyState>=1)done();else{a.addEventListener('loadedmetadata',done,{once:true});a.addEventListener('error',()=>reject(Error('audio failed')),{once:true});a.load();}})))''');assert len(report['ieltsAudio'])==6 and all(x['seconds']>5 for x in report['ieltsAudio'])
 report['ieltsWidths']=[]
 for width in[390,768,1360]:
  cdp('Emulation.setDeviceMetricsOverride',{'width':width,'height':1000,'deviceScaleFactor':1,'mobile':False});row=js('({width:innerWidth,scroll:document.documentElement.scrollWidth,underline:[...document.querySelectorAll("a")].some(a=>getComputedStyle(a).textDecorationLine.includes("underline"))})');report['ieltsWidths'].append(row);assert row['scroll']<=width and not row['underline']
 capture('#section-8','ielts-session3-listening.png');report['ieltsErrors']=js('__errors');assert not report['ieltsErrors']

finally:
 server.shutdown();server.server_close()
 try:cdp('Browser.close')
 except Exception:pass
 proc.terminate()
 try:proc.wait(timeout=10)
 except subprocess.TimeoutExpired:proc.kill()
 (E/'browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print({k:v for k,v in report.items()if k not in ['frames','editableCases','controls']})
