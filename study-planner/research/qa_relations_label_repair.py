"""Inspect the actual rendered chapter, mathematics, solution tables and retained players."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,time
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'deep-relations-browser';OUT.mkdir(exist_ok=True)
profile=OUT/f'edge-{os.getpid()}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report={'status':'in_progress','topicId':'d_relations','screenshots':str(OUT)}
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
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url='http://127.0.0.1:8771/chapters/d_relations.html'))
 for _ in range(100):
  if js('!!window.ConceptAnimations'):break
  time.sleep(.1)
 assert js('!!window.ConceptAnimations'), 'Chapter or renderer did not load'
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))')
 report['loadFailures']=js("[...document.querySelectorAll('.concept-animation')].filter(h=>h.dataset.loaded!=='true').map(h=>({scenes:h.dataset.scenes,state:h.dataset.loaded,text:h.textContent}))");assert not report['loadFailures'],report['loadFailures']

 report=json.loads((R/'research/deep-library-revision/d_relations-browser-before-text-repair.json').read_text())
 report['incrementalRecheck']='Only three model labels changed from escaped spaces to ordinary text. Existing actual control and playback evidence is retained; all 235 rendered checkpoints, screenshots, laboratory, responsive and print checks are freshly repeated.'
 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,solutions:document.querySelectorAll(".exam-solution").length,tutorials:[...document.querySelectorAll("h3")].filter(x=>x.textContent.startsWith("Tutorial ")).length,math:document.querySelectorAll("math").length,errors:__errors})');assert report['counts']['questions']==45 and report['counts']['solutions']==45 and report['counts']['tutorials']==46 and not report['counts']['errors'],report['counts']
 report['fonts']=js('({math:getComputedStyle(document.querySelector(".exam-solution math")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),prose:document.fonts.check("18px \'Source Sans 3\'")})');assert report['fonts']['stix'] and report['fonts']['prose']
 report['models']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){const first=c.scene;for(const scene of c.scenes){c.scene=scene;c.show(0);let issues=[];for(let i=0;i<c.api.model.frames.length;i++){c.api.show(i);issues.push(...DiagramLayout.audit(c.api.host.querySelector('svg')).map(x=>({...x,frame:i})));}rows.push({id:scene.id,frames:scene.frames.length,issues});}c.scene=first;c.show(0);}return rows;})()""")
 assert len(report['models'])==49 and all(not x['issues']for x in report['models']),report['models']
 report['frameRendering']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){const first=c.scene;for(const scene of c.scenes){c.scene=scene;c.show(0);for(let i=0;i<c.api.model.frames.length;i++){c.api.show(i);const svg=c.api.host.querySelector('svg'),bad=[];for(const t of svg.querySelectorAll('text'))for(const m of svg.querySelectorAll('foreignObject math')){const a=t.getBoundingClientRect(),b=m.getBoundingClientRect();if(Math.min(a.right,b.right)-Math.max(a.left,b.left)>1&&Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top)>1)bad.push({text:t.textContent,kind:'formula overlap'});}for(const fo of svg.querySelectorAll('foreignObject')){const m=fo.querySelector('math');if(!m)continue;const a=fo.getBoundingClientRect(),b=m.getBoundingClientRect();if(b.top<a.top-1||b.bottom>a.bottom+1)bad.push({kind:'formula clipping',math:m.textContent});}rows.push({id:scene.id,frame:i,height:svg.viewBox.baseVal.height,issues:bad});}}c.scene=first;c.show(0);}return rows;})()""")
 assert len(report['frameRendering'])==235 and all(not x['issues']and x['height']<=362 for x in report['frameRendering']),report['frameRendering']
 for n in[1,2,3,4,5,6,7,8,9,10,11,12,13,16,17,20,24,28,32,36,37,40,44,45]:
  sel=f'.exam-question[data-deep-index="{n}"] .concept-animation';js('(()=>{const h=document.querySelector('+json.dumps(sel)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host));c.api.show(c.api.model.frames.length-1);})()');capture(sel,f'question-{n}-final.png')
 capture('#mathematical-bridge','instruction-bridge.png');capture('#review','final-rules.png')
 report['staticDiagrams']=js("""(()=>[...document.querySelectorAll('figure svg')].map(svg=>{const v=svg.viewBox.baseVal,bad=[];for(const t of svg.querySelectorAll('text')){const b=t.getBBox();if(b.x<v.x-1||b.y<v.y-1||b.x+b.width>v.x+v.width+1||b.y+b.height>v.y+v.height+1)bad.push({kind:'outside',text:t.textContent});}for(const fo of svg.querySelectorAll('foreignObject')){const m=fo.querySelector('math');if(!m)continue;const a=fo.getBoundingClientRect(),b=m.getBoundingClientRect();if(b.left<a.left-1||b.right>a.right+1||b.top<a.top-1||b.bottom>a.bottom+1)bad.push({kind:'formula clipping',formula:m.textContent});}return{label:svg.getAttribute('aria-labelledby')||svg.dataset.schematic,issues:bad};}))()""");assert len(report['staticDiagrams'])>=4 and all(not x['issues']for x in report['staticDiagrams']),report['staticDiagrams']


 report['relationLab']=[]
 for name,counts in [('chain',[6,10,16]),('cycle',[9,10,10]),('empty',[0,4,4])]:
  js('document.getElementById("lab-'+name+'").click()')
  row=js('({input:[...document.querySelectorAll("#lab-input button")].filter(b=>b.getAttribute("aria-pressed")==="true").length,closures:[...document.querySelectorAll("#lab-closures table")].map(t=>[...t.querySelectorAll("td span")].reduce((sum,v)=>sum+Number(v.textContent),0)),stage:document.getElementById("lab-stage").textContent})');assert row['closures']==counts and row['stage'].startswith('Stage 0'),row;report['relationLab'].append(dict(inputCase=name,**row))
  for k in range(4):js('document.getElementById("lab-next").click()')
  row=js('({stage:document.getElementById("lab-stage").textContent,disabled:document.getElementById("lab-next").disabled,count:[...document.querySelectorAll("#lab-stage-matrix td span")].reduce((sum,v)=>sum+Number(v.textContent),0)})');assert row['stage'].startswith('Stage 4')and row['disabled']and row['count']==counts[0],row;report['relationLab'].append(row)
 row=js('document.querySelectorAll("#lab-input button")[0].click();({stage:document.getElementById("lab-stage").textContent,disabled:document.getElementById("lab-next").disabled,count:[...document.querySelectorAll("#lab-closures table")][0].querySelectorAll("td span").length})');assert row['stage'].startswith('Stage 0')and not row['disabled']and row['count']==16,row;report['relationLab'].append(row)
 js('document.getElementById("lab-chain").click()')
 for i in range(len(report['staticDiagrams'])):
  js('[...document.querySelectorAll("figure svg")]['+str(i)+'].closest("figure").setAttribute("data-relations-static-index","'+str(i)+'")');capture('[data-relations-static-index="'+str(i)+'"]',f'static-{i+1}.png')
 for n in[4,6,7,8,9,10]:
  sel='h3';js('(()=>{const title=[...document.querySelectorAll("h3")].find(h=>h.textContent.startsWith("Challenge '+str(n)+'.")),h=title.nextElementSibling,c=ConceptAnimations.players.find(c=>h.contains(c.api.host));c.api.show(c.api.model.frames.length-1);h.setAttribute("data-capture-challenge","'+str(n)+'");})()');capture('[data-capture-challenge="'+str(n)+'"]',f'challenge-{n}-final.png')
 report['responsive']=[]
 for width in[1360,768,390]:
  cdp('Emulation.setDeviceMetricsOverride',dict(width=width,height=1050,deviceScaleFactor=1,mobile=width<500));js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
  row=js("""(()=>{const b=document.documentElement;return{width:innerWidth,pageWidth:b.scrollWidth,tableOverflow:[...document.querySelectorAll('.exam-solution table')].flatMap(t=>{const a=t.getBoundingClientRect(),fo=t.closest('foreignObject');if(fo){const f=fo.getBoundingClientRect(),stage=t.closest('.sim-stage'),s=stage?.getBoundingClientRect();const clipped=stage&&['auto','scroll','hidden'].includes(getComputedStyle(stage).overflowX)&&s.left>=0&&s.right<=innerWidth+2;return a.left<f.left-1||a.right>f.right+1||a.top<f.top-1||a.bottom>f.bottom+1||!clipped?[{reason:'foreignObject/stage containment'}]:[];}return a.left<0||a.right>innerWidth+2?[{left:a.left,right:a.right}]:[];}),underlined:[...document.querySelectorAll('a')].filter(a=>getComputedStyle(a).textDecorationLine.includes('underline')).length};})()""")
  report['responsive'].append(row);assert row['pageWidth']<=width+2 and not row['tableOverflow'] and not row['underlined'],row
  if width==390:capture('.exam-question[data-deep-index="4"]','question-4-mobile.png');capture('.exam-question[data-deep-index="6"]','question-6-mobile.png')
 cdp('Emulation.setEmulatedMedia',dict(media='print'));js('dispatchEvent(new Event("beforeprint"))')
 report['print']=js('({solutions:[...document.querySelectorAll(".exam-solution")].filter(x=>getComputedStyle(x).display!=="none").length,errors:__errors})');assert report['print']['solutions']==45 and not report['print']['errors']
 report['status']='passed_pending_screenshot_inspection'
finally:
 (R/'research/deep-library-revision/d_relations-browser.json').write_text(json.dumps(report,indent=2)+'\n')
 proc.terminate()
print(report['status'])
