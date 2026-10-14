from pathlib import Path
import array,base64,hashlib,json,os,subprocess,tempfile,time,wave
import requests,websocket
R=Path(__file__).resolve().parents[1];E=R/'research/ielts';O=Path(tempfile.gettempdir())/'ielts-first-lesson-qa';O.mkdir(exist_ok=True)
report={'lesson':'academic-01-sentences','status':'in_progress','humanAudioClarity':'Not certified; original synthetic audio requires learner playback feedback.'}
manifest=json.loads((R/'dist/ielts/audio/manifest.json').read_text(encoding='utf-8-sig'));assert len(manifest)==6
report['audio']=[]
for item in manifest:
 p=R/'dist/ielts/audio'/item['file']
 with wave.open(str(p),'rb')as w:
  assert w.getsampwidth()==2 and w.getnchannels()==1
  samples=array.array('h',w.readframes(w.getnframes()));duration=len(samples)/w.getframerate()
  rms=(sum(x*x for x in samples)/len(samples))**.5
  assert duration>5 and rms>50 and all(-32768<x<32767 for x in samples)
  report['audio'].append({'file':item['file'],'seconds':round(duration,2),'rms':round(rms,2),'voice':item['voice'],'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'transcript':item['transcript']})
profile=O/f'edge-{os.getpid()}';proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0
try:
 for _ in range(100):
  if(profile/'DevToolsActivePort').exists()and(profile/'DevToolsActivePort').read_text().strip():break
  time.sleep(.1)
 port=int((profile/'DevToolsActivePort').read_text().splitlines()[0]);page=next(x for x in requests.get(f'http://127.0.0.1:{port}/json').json()if x['type']=='page');ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=60)
 def cdp(method,params=None):
  global seq
  seq+=1;ws.send(json.dumps({'id':seq,'method':method,'params':params or{}}))
  while True:
   x=json.loads(ws.recv())
   if x.get('id')==seq:assert'error'not in x,x;return x.get('result',{})
 def js(code):
  x=cdp('Runtime.evaluate',{'expression':code,'returnByValue':True,'awaitPromise':True});assert'exceptionDetails'not in x,x;return x.get('result',{}).get('value')
 def shot(selector,name):
  js('document.querySelector('+json.dumps(selector)+').scrollIntoView({block:"start",behavior:"instant"})');js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');(O/name).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"})
 cdp('Emulation.setDeviceMetricsOverride',{'width':1360,'height':1000,'deviceScaleFactor':1,'mobile':False});cdp('Page.navigate',{'url':'http://127.0.0.1:8771/ielts/academic-01-sentences.html'})
 for _ in range(100):
  if js('!!document.querySelector("#lab-tokens [role=listitem]")'):break
  time.sleep(.1)
 js('document.fonts.ready')
 report['fonts']=js('({body:getComputedStyle(document.querySelector(".lesson p")).fontFamily,heading:getComputedStyle(document.querySelector("h1")).fontFamily,bodyLoaded:document.fonts.check("17px \'Source Sans 3\'"),headingLoaded:document.fonts.check("28px \'Newsreader\'")})');assert report['fonts']['bodyLoaded']and report['fonts']['headingLoaded']
 report['sentenceCases']=js("""(()=>{const out=[];for(const s of ['I','You','Emma','We','They'])for(const m of ['ready','late','in room fourteen'])for(const f of ['affirmative','negative','question']){for(const[id,v]of [['subject',s],['meaning',m],['form',f]]){const e=document.getElementById('lab-'+id);e.value=v;e.dispatchEvent(new Event('change'));}out.push({subject:s,meaning:m,form:f,sentence:document.getElementById('lab-tokens').dataset.sentence,roles:[...document.querySelectorAll('.sentence-token')].map(x=>x.dataset.role),explanation:document.getElementById('lab-explanation').textContent});}return out;})()""")
 for x in report['sentenceCases']:
  verb='am'if x['subject']=='I'else'is'if x['subject']=='Emma'else'are'
  expected=(verb.capitalize()+' '+(x['subject']if x['subject']in['I','Emma']else x['subject'].lower())+' '+x['meaning']+'?')if x['form']=='question'else x['subject']+' '+verb+(' not'if x['form']=='negative'else'')+' '+x['meaning']+'.'
  assert x['sentence']==expected,x
 assert len(report['sentenceCases'])==45
 report['audioElements']=js('Promise.all([...document.querySelectorAll("audio")].map(a=>new Promise(resolve=>{const done=()=>resolve({src:a.getAttribute("src"),duration:a.duration,readyState:a.readyState,error:a.error?.code||null});if(a.readyState>=1||a.error)done();else{a.addEventListener("loadedmetadata",done,{once:true});a.addEventListener("error",done,{once:true});a.load();setTimeout(done,10000);}})))');assert len(report['audioElements'])==6 and all(x['duration']and not x['error']for x in report['audioElements'])
 report['references']=js('[...document.querySelectorAll("#section-11 ~ ul a")].map(a=>({url:a.href,text:a.textContent}))');assert len(report['references'])==5
 js('document.querySelectorAll("details").forEach(x=>x.open=true)');report['responsive']=[]
 for width in[1360,768,390]:
  cdp('Emulation.setDeviceMetricsOverride',{'width':width,'height':1000,'deviceScaleFactor':1,'mobile':width==390});js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
  row=js('({width:innerWidth,pageWidth:document.documentElement.scrollWidth,underlines:[...document.querySelectorAll("a")].filter(a=>getComputedStyle(a).textDecorationLine.includes("underline")).length,clippedTokens:[...document.querySelectorAll(".sentence-token")].filter(x=>x.scrollWidth>x.clientWidth+1).length,errors:__errors})');assert row['pageWidth']<=width+2 and not row['underlines']and not row['clippedTokens']and not row['errors'],row;report['responsive'].append(row)
  if width in[1360,390]:
   shot('.hero',f'hero-{width}.png');shot('#sentence-lab',f'lab-{width}.png');shot('#section-8',f'listening-{width}.png')
 js('document.querySelectorAll("details").forEach(x=>x.open=false)');cdp('Emulation.setEmulatedMedia',{'media':'print'});js('dispatchEvent(new Event("beforeprint"))');report['print']=js('({allAnswersVisible:[...document.querySelectorAll("details")].every(d=>d.open),underlined:[...document.querySelectorAll("a")].some(a=>getComputedStyle(a).textDecorationLine.includes("underline"))})');assert report['print']['allAnswersVisible']and not report['print']['underlined']
 js('dispatchEvent(new Event("afterprint"))');assert js('[...document.querySelectorAll("details")].every(d=>!d.open)')
 cdp('Emulation.setEmulatedMedia',{'media':''});cdp('Page.navigate',{'url':'http://127.0.0.1:8771/index.html#ielts'})
 for _ in range(100):
  if js("!!document.querySelector('#ielts a[href=\"ielts/academic-01-sentences.html\"]')"):break
  time.sleep(.1)
 report['appEntry']=js("({link:!!document.querySelector('#ielts a[href=\"ielts/academic-01-sentences.html\"]'),viewVisible:!document.querySelector('#view-ielts').hidden,errors:__errors})");assert report['appEntry']['link']and report['appEntry']['viewVisible']and not report['appEntry']['errors']
 report['status']='passed_technical_and_rendered_checks';report['screenshots']=str(O)
finally:
 proc.terminate()
 try:proc.wait(timeout=10)
 except subprocess.TimeoutExpired:proc.kill()
 (E/'academic-01-qa.json').write_text(json.dumps(report,indent=2)+'\n')
print({k:report[k]for k in['status','fonts','responsive','print','appEntry','screenshots']})
