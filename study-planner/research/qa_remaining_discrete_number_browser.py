"""Inspect the actual rendered chapter, mathematics, solution tables and retained players."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,time
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'deep-discrete-number-browser';OUT.mkdir(exist_ok=True)
profile=OUT/f'edge-{os.getpid()}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report={'status':'in_progress','topicId':'d_number','screenshots':str(OUT)}
try:
 for _ in range(100):
  if(profile/'DevToolsActivePort').exists():
   try:
    port_text=(profile/'DevToolsActivePort').read_text();assert port_text.strip();break
   except (OSError,AssertionError):pass
  time.sleep(.1)
 port=int(port_text.splitlines()[0]);page=next(p for p in requests.get(f'http://127.0.0.1:{port}/json').json()if p['type']=='page');ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=60)
 def cdp(method,params=None):
  global seq
  seq+=1;ws.send(json.dumps(dict(id=seq,method=method,params=params or{})))
  while True:
   r=json.loads(ws.recv())
   if r.get('id')==seq:assert 'error'not in r,r;return r.get('result',{})
 def js(code):
  r=cdp('Runtime.evaluate',dict(expression=code,returnByValue=True,awaitPromise=True));assert 'exceptionDetails'not in r,r;return r.get('result',{}).get('value')
 def capture(sel,name):
  js('document.querySelector('+json.dumps(sel)+').scrollIntoView({block:"start",behavior:"instant"})');js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');(OUT/name).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"})
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url='http://127.0.0.1:8771/chapters/d_number.html'))
 for _ in range(100):
  if js('!!window.ConceptAnimations'):break
  time.sleep(.1)
 assert js('!!window.ConceptAnimations'), 'Chapter or renderer did not load'
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))')
 report['loadFailures']=js("[...document.querySelectorAll('.concept-animation')].filter(h=>h.dataset.loaded!=='true').map(h=>({scenes:h.dataset.scenes,state:h.dataset.loaded,text:h.textContent}))");assert not report['loadFailures'],report['loadFailures']

 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,solutions:document.querySelectorAll(".exam-solution").length,tutorials:[...document.querySelectorAll("h3")].filter(x=>x.textContent.startsWith("Tutorial ")).length,math:document.querySelectorAll("math").length,errors:__errors})');assert report['counts']['questions']==47 and report['counts']['solutions']==47 and report['counts']['tutorials']==40 and not report['counts']['errors'],report['counts']
 report['fonts']=js('({math:getComputedStyle(document.querySelector(".exam-solution math")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),prose:document.fonts.check("18px \'Source Sans 3\'")})');assert report['fonts']['stix'] and report['fonts']['prose']
 report['models']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){const first=c.scene;for(const scene of c.scenes){c.scene=scene;c.show(0);let issues=[];for(let i=0;i<c.api.model.frames.length;i++){c.api.show(i);issues.push(...DiagramLayout.audit(c.api.host.querySelector('svg')).map(x=>({...x,frame:i})));}rows.push({id:scene.id,frames:scene.frames.length,issues});}c.scene=first;c.show(0);}return rows;})()""")
 assert len(report['models'])>=41 and all(not x['issues']for x in report['models']),report['models']
 report['frameRendering']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){const first=c.scene;for(const scene of c.scenes){c.scene=scene;c.show(0);for(let i=0;i<c.api.model.frames.length;i++){c.api.show(i);const svg=c.api.host.querySelector('svg'),bad=[];for(const t of svg.querySelectorAll('text'))for(const m of svg.querySelectorAll('foreignObject math')){const a=t.getBoundingClientRect(),b=m.getBoundingClientRect();if(Math.min(a.right,b.right)-Math.max(a.left,b.left)>1&&Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top)>1)bad.push({text:t.textContent,kind:'formula overlap'});}for(const fo of svg.querySelectorAll('foreignObject')){const m=fo.querySelector('math');if(!m)continue;const a=fo.getBoundingClientRect(),b=m.getBoundingClientRect();if(b.top<a.top-1||b.bottom>a.bottom+1)bad.push({kind:'formula clipping',math:m.textContent});}rows.push({id:scene.id,frame:i,height:svg.viewBox.baseVal.height,issues:bad});}}c.scene=first;c.show(0);}return rows;})()""")
 assert len(report['frameRendering'])==sum(r['frames']for r in report['models']) and all(not x['issues']and x['height']<=362 for x in report['frameRendering']),report['frameRendering']
 recorded=json.loads((R/'research/deep-library-revision/d_number-browser-controls-before-modulus-one-fix.json').read_text())
 for key in ['controls','selection','playback']:report[key]=recorded[key]
 report['controlEvidence']='research/deep-library-revision/d_number-browser-controls-before-modulus-one-fix.json'
 report['controlEvidenceQualification']='All controls, playback and selections passed before the laboratory-only modulus-one minimum fix. This run freshly renders every frame and checks the corrected laboratory, static figures, responsiveness and print.'
 for n in[1,2,3,4,5,6,7,8,9,10,11,12,13,14,18,22,26,30,34,38,42,46,47]:
  sel=f'.exam-question[data-deep-index="{n}"] .concept-animation';js('(()=>{const h=document.querySelector('+json.dumps(sel)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host));c.api.show(c.api.model.frames.length-1);})()');capture(sel,f'question-{n}-final.png')
 capture('#mathematical-bridge','instruction-bridge.png');capture('#review','final-rules.png')
 report['staticDiagrams']=js("""(()=>[...document.querySelectorAll('figure svg')].map(svg=>{const v=svg.viewBox.baseVal,bad=[];for(const t of svg.querySelectorAll('text')){const b=t.getBBox();if(b.x<v.x-1||b.y<v.y-1||b.x+b.width>v.x+v.width+1||b.y+b.height>v.y+v.height+1)bad.push({kind:'outside',text:t.textContent});}for(const fo of svg.querySelectorAll('foreignObject')){const m=fo.querySelector('math');if(!m)continue;const a=fo.getBoundingClientRect(),b=m.getBoundingClientRect();if(b.left<a.left-1||b.right>a.right+1||b.top<a.top-1||b.bottom>a.bottom+1)bad.push({kind:'formula clipping',formula:m.textContent});}return{label:svg.getAttribute('aria-labelledby')||svg.dataset.schematic,issues:bad};}))()""");assert len(report['staticDiagrams'])>=4 and all(not x['issues']for x in report['staticDiagrams']),report['staticDiagrams']





 report['numberLab']=[]
 def flags():return js("({...document.getElementById('number-output').dataset})")
 for name,count,g,inverse in [('unit',1,1,'5'),('many',4,4,'none'),('none',0,4,'none'),('zero',6,6,'none'),('negative',1,1,'2')]:
  js('document.querySelector("[data-preset='+name+']").click()');actual=flags();assert actual==dict(count=str(count),gcd=str(g),inverse=inverse),(name,actual);assert js('document.querySelectorAll(".map-cell.solution").length')==count;report['numberLab'].append(dict(preset=name,flags=actual))
 for a,b,m,count,g,inverse in [(12,18,30,6,6,'none'),(0,1,1,1,1,'0'),(6,8,14,2,2,'none')]:
  js('document.getElementById("number-a").value='+str(a)+';document.getElementById("number-b").value='+str(b)+';document.getElementById("number-m").value='+str(m)+';document.getElementById("number-form").dispatchEvent(new Event("submit",{cancelable:true}))');actual=flags();assert actual==dict(count=str(count),gcd=str(g),inverse=inverse),(a,b,m,actual);report['numberLab'].append(dict(input=[a,b,m],flags=actual))
 js('document.getElementById("number-m").value=61;document.getElementById("number-m").dispatchEvent(new Event("change"))');assert js('document.getElementById("number-m").validity.rangeOverflow');report['invalidModulusInput']=True
 js('document.querySelector("[data-preset=many]").click();document.getElementById("number-a").value="";document.getElementById("number-a").dispatchEvent(new Event("change"))');assert js('document.getElementById("number-a").validity.valueMissing');report['missingCoefficientInput']=True
 js('document.querySelector("[data-preset=many]").click()')
 for i in range(len(report['staticDiagrams'])):
  js('[...document.querySelectorAll("figure svg")]['+str(i)+'].closest("figure").setAttribute("data-invariants-static-index","'+str(i)+'")');capture('[data-invariants-static-index="'+str(i)+'"]',f'static-{i+1}.png')
 for n in[1,2,3,4,5,6,7,8,9,10]:
  sel='h3';js('(()=>{const title=[...document.querySelectorAll("h3")].find(h=>h.textContent.startsWith("Challenge '+str(n)+'.")),h=title.nextElementSibling,c=ConceptAnimations.players.find(c=>h.contains(c.api.host));c.api.show(c.api.model.frames.length-1);h.setAttribute("data-capture-challenge","'+str(n)+'");})()');capture('[data-capture-challenge="'+str(n)+'"]',f'challenge-{n}-final.png')
 report['responsive']=[]
 for width in[1360,768,390]:
  cdp('Emulation.setDeviceMetricsOverride',dict(width=width,height=1050,deviceScaleFactor=1,mobile=width<500));js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
  row=js("""(()=>{const b=document.documentElement;return{width:innerWidth,pageWidth:b.scrollWidth,tableOverflow:[...document.querySelectorAll('.exam-solution table')].flatMap(t=>{const a=t.getBoundingClientRect(),fo=t.closest('foreignObject');if(fo){const f=fo.getBoundingClientRect(),stage=t.closest('.sim-stage'),s=stage?.getBoundingClientRect();const clipped=stage&&['auto','scroll','hidden'].includes(getComputedStyle(stage).overflowX)&&s.left>=0&&s.right<=innerWidth+2;return a.left<f.left-1||a.right>f.right+1||a.top<f.top-1||a.bottom>f.bottom+1||!clipped?[{reason:'foreignObject/stage containment'}]:[];}return a.left<0||a.right>innerWidth+2?[{left:a.left,right:a.right}]:[];}),underlined:[...document.querySelectorAll('a')].filter(a=>getComputedStyle(a).textDecorationLine.includes('underline')).length};})()""")
  report['responsive'].append(row);assert row['pageWidth']<=width+2 and not row['tableOverflow'] and not row['underlined'],row
  if width==390:capture('.exam-question[data-deep-index="4"]','question-4-mobile.png');capture('.exam-question[data-deep-index="6"]','question-6-mobile.png')
 cdp('Emulation.setEmulatedMedia',dict(media='print'));js('dispatchEvent(new Event("beforeprint"))')
 report['print']=js('({solutions:[...document.querySelectorAll(".exam-solution")].filter(x=>getComputedStyle(x).display!=="none").length,errors:__errors})');assert report['print']['solutions']==47 and not report['print']['errors']
 report['status']='passed_pending_screenshot_inspection'
finally:
 (R/'research/deep-library-revision/d_number-browser.json').write_text(json.dumps(report,indent=2)+'\n')
 proc.terminate()
print(report['status'])
