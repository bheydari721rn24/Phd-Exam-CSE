from pathlib import Path
import base64,json,os,subprocess,tempfile,time,uuid
import requests,websocket
R=Path(__file__).resolve().parents[1];O=Path(tempfile.gettempdir())/'offline-teaching-qa';O.mkdir(exist_ok=True);profile=O/f'edge-{os.getpid()}-{uuid.uuid4().hex[:8]}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL);seq=0;results=[]
try:
 for _ in range(100):
  try:
   if(profile/'DevToolsActivePort').exists()and len((profile/'DevToolsActivePort').read_text().strip().splitlines())>=2:break
  except OSError:pass
  time.sleep(.1)
 port=int((profile/'DevToolsActivePort').read_text().splitlines()[0]);p=next(x for x in requests.get(f'http://127.0.0.1:{port}/json').json()if x['type']=='page');ws=websocket.create_connection(p['webSocketDebuggerUrl'],timeout=30)
 def cdp(m,params=None):
  global seq
  seq+=1;ws.send(json.dumps({'id':seq,'method':m,'params':params or{}}))
  while True:
   a=json.loads(ws.recv())
   if a.get('id')==seq:assert'error'not in a,a;return a.get('result',{})
 def js(s):
  a=cdp('Runtime.evaluate',{'expression':s,'returnByValue':True,'awaitPromise':True});assert'exceptionDetails'not in a,a;return a.get('result',{}).get('value')
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"});cdp('Emulation.setDeviceMetricsOverride',{'width':1360,'height':1000,'deviceScaleFactor':1,'mobile':False})
 # External requests are blocked: these two files must teach without a server or internet.
 cdp('Network.enable');cdp('Network.setBlockedURLs',{'urls':['http://*','https://*']})
 for name in['Algorithm Correctness.html','IELTS Academic Session 1.html','Orthogonal Projections.html','IELTS Academic Session 2.html','Conditional Probability.html']:
  fileUrl=(R/'exports'/name).as_uri();cdp('Page.navigate',{'url':fileUrl})
  for _ in range(100):
   if js('location.href==='+json.dumps(fileUrl)+'&&document.readyState==="complete"'):break
   time.sleep(.1)
  js('Promise.all([...document.fonts].map(f=>f.load()))');js('document.fonts.ready');entry={'file':name}
  entry['fonts']=js('({body:document.fonts.check("17px \'Source Sans 3\'"),heading:document.fonts.check("28px \'Newsreader\'"),math:document.fonts.check("18px \'STIX Two Math\'")})');assert all(entry['fonts'].values()),entry
  if name.startswith('Algorithm'):
   js('document.querySelectorAll(".exam-solution").forEach(d=>d.open=true)');js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))')
   entry['models']=js('[...document.querySelectorAll(".concept-animation")].map(h=>({scenes:h.dataset.scenes,loaded:h.dataset.loaded}))');assert all(x['loaded']=='true'for x in entry['models'])
   entry['questionPlayers']=js('ConceptAnimations.players.filter(c=>c.scene.id.startsWith("correctness-question-")).length');assert entry['questionPlayers']==54
   entry['lab']=js('({...document.getElementById("search-output").dataset})');assert entry['lab']['valid']=='true'and entry['lab']['result']=='1'
  elif name=='Conditional Probability.html':
   js('document.querySelectorAll(".exam-solution").forEach(d=>d.open=true)');js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))');entry['questions']=js('document.querySelectorAll(".exam-question").length');assert entry['questions']==60
   entry['models']=js('ConceptAnimations.players.map(p=>({id:p.scene.id,loaded:p.host.dataset.loaded}))');assert len(entry['models'])==11 and all(p['loaded']=='true'for p in entry['models'])
   entry['lab']=js('({...document.getElementById("table-output").dataset})');assert entry['lab']['forward']=='3/4'
   entry['repairedProblem']=js('document.querySelector(\'[data-source-id="SC33"]\').textContent');assert'1,5,6,7'in entry['repairedProblem'].replace(' ','')
  elif name=='Orthogonal Projections.html':
   entry['models']=js('ProjectionPlayers.map(p=>({frames:p.data.length,certificates:p.data.every(f=>f.certificate)}))');assert len(entry['models'])==13 and all(x['certificates']for x in entry['models'])
   entry['controls']=js('(()=>{const p=ProjectionPlayers[0];p.host.querySelector("[data-next]").click();return p.index===1;})()');assert entry['controls']
   entry['questions']=js('document.querySelectorAll(".exam-question").length');assert entry['questions']==52
   entry['widths']=[]
   for width in[390,768,1360]:
    cdp('Emulation.setDeviceMetricsOverride',{'width':width,'height':1000,'deviceScaleFactor':1,'mobile':False});entry['widths'].append(js('({width:innerWidth,document:document.documentElement.scrollWidth})'));assert entry['widths'][-1]['document']<=width
  else:
   entry['audio']=js('Promise.all([...document.querySelectorAll("audio")].map(a=>new Promise(resolve=>{const done=()=>resolve({duration:a.duration,error:a.error?.code||null,embedded:a.src.startsWith("data:")});if(a.readyState>=1)done();else{a.addEventListener("loadedmetadata",done,{once:true});a.addEventListener("error",done,{once:true});a.load();setTimeout(done,7000);}})))');assert len(entry['audio'])==6 and all(x['embedded']and x['duration']and not x['error']for x in entry['audio'])
   if name=='IELTS Academic Session 1.html':
    entry['sentence']=js('document.getElementById("lab-tokens").dataset.sentence');assert entry['sentence']=='I am ready.'
   else:
    entry['sentenceLab']=js('''(()=>{const f=document.getElementById('routine-form'),out=[];for(const subject of [...f.elements.subject.options].map(o=>o.value))for(const verb of [...f.elements.verb.options].map(o=>o.value))for(const form of [...f.elements.form.options].map(o=>o.value)){f.elements.subject.value=subject;f.elements.verb.value=verb;f.elements.form.value=form;f.dispatchEvent(new Event('change'));out.push({subject,verb,form,sentence:document.getElementById('routine-sentence').textContent,explanation:document.getElementById('routine-explanation').textContent});}return out;})()''');assert len(entry['sentenceLab'])==72 and all(x['sentence']and x['explanation']for x in entry['sentenceLab'])
    for x in entry['sentenceLab']:
     singular=x['subject']in['Maya','Leo'];base={'study':'study','read':'read','have':'have'}[x['verb']];third={'study':'studies','read':'reads','have':'has'}[x['verb']]
     if x['form']=='statement':assert(' '+(third if singular else base)+' ')in x['sentence']
     else:assert('does'if singular else'do')in x['sentence'].lower()and(' '+base+' ')in x['sentence']and(' '+third+' ')not in x['sentence']if singular else(' '+base+' ')in x['sentence']
    entry['widths']=[]
    for width in[390,768,1360]:
     cdp('Emulation.setDeviceMetricsOverride',{'width':width,'height':1000,'deviceScaleFactor':1,'mobile':False});entry['widths'].append(js('({width:innerWidth,document:document.documentElement.scrollWidth})'));assert entry['widths'][-1]['document']<=width
  entry['errors']=js('__errors');assert not entry['errors'],entry
  entry['externalTeachingDependencies']=js('[...document.querySelectorAll("script[src],link[rel=stylesheet],audio[src]")].filter(e=>!e.getAttribute("src")?.startsWith("data:")).map(e=>e.outerHTML.slice(0,70))');assert not entry['externalTeachingDependencies'],entry
  results.append(entry)
finally:
 try:ws.send(json.dumps({'id':999999,'method':'Browser.close'}))
 except Exception:pass
 proc.terminate()
 try:proc.wait(timeout=10)
 except subprocess.TimeoutExpired:proc.kill()
report={'status':'passed_offline_file_browser_checks','network':'All http and https requests blocked during the checks. The files were loaded with file URLs; fonts, teaching scripts, models and audio still loaded. External references intentionally remain links.','copies':results,'humanListeningClarity':'Synthetic audio requires learner feedback; technical playback checks are not a comprehension certificate.'};(R/'exports/browser-checks.json').write_text(json.dumps(report,indent=2)+'\n');print({'status':report['status'],'files':len(results),'questionPlayers':results[0]['questionPlayers'],'embeddedAudio':len(results[1]['audio'])})
