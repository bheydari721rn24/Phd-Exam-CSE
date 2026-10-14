"""Inspect the actual rendered chapter, mathematics, solution tables and retained players."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,time
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'deep-divide-final-visual';OUT.mkdir(exist_ok=True)
profile=OUT/f'edge-{os.getpid()}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report={'status':'in_progress','topicId':'a_divide','screenshots':str(OUT)}
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
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url='http://127.0.0.1:8771/chapters/a_divide.html'))
 for _ in range(100):
  if js('!!window.ConceptAnimations'):break
  time.sleep(.1)
 assert js('!!window.ConceptAnimations'), 'Chapter or renderer did not load'
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))')
 report['loadFailures']=js("[...document.querySelectorAll('.concept-animation')].filter(h=>h.dataset.loaded!=='true').map(h=>({scenes:h.dataset.scenes,state:h.dataset.loaded,text:h.textContent}))");assert not report['loadFailures'],report['loadFailures']

 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,solutions:document.querySelectorAll(".exam-solution").length,tutorials:[...document.querySelectorAll("h3")].filter(x=>x.textContent.startsWith("Tutorial ")).length,math:document.querySelectorAll("math").length,errors:__errors})');assert report['counts']['questions']==46 and report['counts']['solutions']==46 and report['counts']['tutorials']==48 and not report['counts']['errors'],report['counts']
 report['fonts']=js('({math:getComputedStyle(document.querySelector(".exam-solution math")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),prose:document.fonts.check("18px \'Source Sans 3\'")})');assert report['fonts']['stix'] and report['fonts']['prose']
 report['models']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){const first=c.scene;for(const scene of c.scenes){c.scene=scene;c.show(0);let issues=[];for(let i=0;i<c.api.model.frames.length;i++){c.api.show(i);issues.push(...DiagramLayout.audit(c.api.host.querySelector('svg')).map(x=>({...x,frame:i})));}rows.push({id:scene.id,frames:scene.frames.length,issues});}c.scene=first;c.show(0);}return rows;})()""")
 assert len(report['models'])>=46 and all(not x['issues']for x in report['models']),report['models']
 report['frameRendering']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){const first=c.scene;for(const scene of c.scenes){c.scene=scene;c.show(0);for(let i=0;i<c.api.model.frames.length;i++){c.api.show(i);const svg=c.api.host.querySelector('svg'),bad=[];for(const t of svg.querySelectorAll('text'))for(const m of svg.querySelectorAll('foreignObject math')){const a=t.getBoundingClientRect(),b=m.getBoundingClientRect();if(Math.min(a.right,b.right)-Math.max(a.left,b.left)>1&&Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top)>1)bad.push({text:t.textContent,kind:'formula overlap'});}for(const fo of svg.querySelectorAll('foreignObject')){const m=fo.querySelector('math');if(!m)continue;const a=fo.getBoundingClientRect(),b=m.getBoundingClientRect();if(b.top<a.top-1||b.bottom>a.bottom+1)bad.push({kind:'formula clipping',math:m.textContent});}rows.push({id:scene.id,frame:i,height:svg.viewBox.baseVal.height,issues:bad});}}c.scene=first;c.show(0);}return rows;})()""")
 assert len(report['frameRendering'])==sum(r['frames']for r in report['models']) and all(not x['issues']and x['height']<=362 for x in report['frameRendering']),report['frameRendering']
 report['playerCount']=js('ConceptAnimations.players.length')
 report['directedPorts']=js("""(()=>{const out=[];for(const c of ConceptAnimations.players){const old=c.scene;for(const scene of c.scenes){if(!scene.id.startsWith('divide-question-'))continue;c.scene=scene;c.show(0);for(let i=0;i<scene.frames.length;i++){c.api.show(i);const svg=c.api.host.querySelector('svg'),rects=[...svg.querySelectorAll('rect')].map(r=>r.getBBox());for(const p of svg.querySelectorAll('[data-divide-ports]')){const v=p.dataset.dividePorts.split(',').map(Number),near=(x,y)=>rects.some(r=>{const inside=x>=r.x-.02&&x<=r.x+r.width+.02&&y>=r.y-.02&&y<=r.y+r.height+.02;const border=Math.min(Math.abs(x-r.x),Math.abs(x-r.x-r.width),Math.abs(y-r.y),Math.abs(y-r.y-r.height))<.02;return inside&&border;}),marker=p.getAttribute('marker-end'),id=marker?.match(/#([^)]*)/)?.[1];out.push({scene:scene.id,frame:i,attached:near(v[0],v[1])&&near(v[2],v[3]),marker:!!id&&!!svg.querySelector('[id="'+id+'"]')});}}}c.scene=old;c.show(0);}return out;})()""")
 assert report['directedPorts']and all(r['attached']and r['marker']for r in report['directedPorts'])
 for n in[1,2,3,4,5,6,7,8,9,10,11,12,13,17,21,25,29,33,37,41,45,46]:
  sel=f'.exam-question[data-deep-index="{n}"] .concept-animation';js('(()=>{const h=document.querySelector('+json.dumps(sel)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host));c.api.show(c.api.model.frames.length-1);})()');capture(sel,f'question-{n}-final.png')
 capture('#mathematical-bridge','instruction-bridge.png');capture('#review','final-rules.png')
 report['staticDiagrams']=js("""(()=>[...document.querySelectorAll('figure svg')].map(svg=>{const v=svg.viewBox.baseVal,bad=[];for(const t of svg.querySelectorAll('text')){const b=t.getBBox();if(b.x<v.x-1||b.y<v.y-1||b.x+b.width>v.x+v.width+1||b.y+b.height>v.y+v.height+1)bad.push({kind:'outside',text:t.textContent});}for(const fo of svg.querySelectorAll('foreignObject')){const m=fo.querySelector('math');if(!m)continue;const a=fo.getBoundingClientRect(),b=m.getBoundingClientRect();if(b.left<a.left-1||b.right>a.right+1||b.top<a.top-1||b.bottom>a.bottom+1)bad.push({kind:'formula clipping',formula:m.textContent});}return{label:svg.getAttribute('aria-labelledby')||svg.dataset.schematic,issues:bad};}))()""");assert len(report['staticDiagrams'])>=3 and all(not x['issues']for x in report['staticDiagrams']),report['staticDiagrams']





 report['summaryLab']=[]
 for name,expected in [('crossing',9),('negative',-2),('left',9),('ties',2)]:
  js('document.querySelector('+json.dumps('[data-preset='+name+']')+').click()');actual=js('({...document.getElementById("subarray-output").dataset})');assert int(actual['best'])==expected and actual['verified']=='true',(name,actual);report['summaryLab'].append(dict(preset=name,flags=actual))
 js('document.getElementById("subarray-input").value="3,-6,5,-5,1,6,-2";document.getElementById("subarray-split").value=5;document.getElementById("subarray-form").dispatchEvent(new Event("submit",{cancelable:true}))');actual=js('({...document.getElementById("subarray-output").dataset})');assert actual['best']=='7'and actual['start']=='2'and actual['end']=='6';report['summaryLab'].append(dict(preset='earliest-crossing-tie',flags=actual))
 js('document.querySelector("[data-preset=crossing]").click()')
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
 report['print']=js('({solutions:[...document.querySelectorAll(".exam-solution")].filter(x=>getComputedStyle(x).display!=="none").length,errors:__errors})');assert report['print']['solutions']==46 and not report['print']['errors']
 report['status']='passed_pending_screenshot_inspection'
finally:
 (R/'research/deep-library-revision/a_divide-final-visual.json').write_text(json.dumps(report,indent=2)+'\n')
 proc.terminate()
print(report['status'])
