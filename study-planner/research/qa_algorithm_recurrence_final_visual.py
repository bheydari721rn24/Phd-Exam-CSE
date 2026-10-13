"""Inspect the actual rendered chapter, mathematics, solution tables and retained players."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,time
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'deep-algorithm-recurrence-browser';OUT.mkdir(exist_ok=True)
profile=OUT/f'edge-{os.getpid()}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report={'status':'in_progress','topicId':'a_recurrence','screenshots':str(OUT)}
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
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url='http://127.0.0.1:8771/chapters/a_recurrence.html'))
 for _ in range(100):
  if js('!!window.ConceptAnimations'):break
  time.sleep(.1)
 assert js('!!window.ConceptAnimations'), 'Chapter or renderer did not load'
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))')
 report['loadFailures']=js("[...document.querySelectorAll('.concept-animation')].filter(h=>h.dataset.loaded!=='true').map(h=>({scenes:h.dataset.scenes,state:h.dataset.loaded,text:h.textContent}))");assert not report['loadFailures'],report['loadFailures']

 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,solutions:document.querySelectorAll(".exam-solution").length,tutorials:[...document.querySelectorAll("h3")].filter(x=>x.textContent.startsWith("Tutorial ")).length,math:document.querySelectorAll("math").length,errors:__errors})');assert report['counts']['questions']==53 and report['counts']['solutions']==53 and report['counts']['tutorials']==40 and not report['counts']['errors'],report['counts']
 report['fonts']=js('({math:getComputedStyle(document.querySelector(".exam-solution math")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),prose:document.fonts.check("18px \'Source Sans 3\'")})');assert report['fonts']['stix'] and report['fonts']['prose']
 report['finalFrames']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){const first=c.scene;for(const scene of c.scenes){if(!scene.id.startsWith('algorithm-recurrence-question-')&&scene.id!=='recurrence-levels')continue;c.scene=scene;c.show(0);for(let i=0;i<scene.frames.length;i++){c.api.show(i);const svg=c.api.host.querySelector('svg'),v=svg.viewBox.baseVal,issues=DiagramLayout.audit(svg);for(const fo of svg.querySelectorAll('foreignObject')){const m=fo.querySelector('math');if(!m)continue;const a=fo.getBoundingClientRect(),b=m.getBoundingClientRect();if(b.top<a.top-1||b.bottom>a.bottom+1)issues.push({kind:'math clipping',formula:m.textContent});}rows.push({id:scene.id,frame:i,height:v.height,issues});}}c.scene=first;c.show(0);}return rows;})()""")
 assert all(not x['issues']and x['height']<=362 for x in report['finalFrames']),[x for x in report['finalFrames']if x['issues']or x['height']>362]
 report['staticPorts']=js("""(()=>{const svg=document.querySelector('figure:nth-of-type(3) svg')||[...document.querySelectorAll('figure svg')][2],circles=[...svg.querySelectorAll('circle')];const distance=(x,y)=>Math.min(...circles.map(c=>Math.abs(Math.hypot(x-+c.getAttribute('cx'),y-+c.getAttribute('cy'))-+c.getAttribute('r'))));return[...svg.querySelectorAll('[data-recurrence-static-ports]')].map(e=>({start:distance(+e.getAttribute('x1'),+e.getAttribute('y1')),end:distance(+e.getAttribute('x2'),+e.getAttribute('y2')),resolved:!!svg.querySelector('#'+e.getAttribute('marker-end').match(/url\(#([^)]*)\)/)[1])}));})()""")
 assert len(report['staticPorts'])==8 and all(v['start']<.001 and v['end']<.001 and v['resolved']for v in report['staticPorts']),report['staticPorts']
 report['staticBounds']=js("""(()=>[...document.querySelectorAll('figure svg')].map(svg=>{const v=svg.viewBox.baseVal,issues=[];for(const t of svg.querySelectorAll('text')){const b=t.getBBox();if(b.x<v.x-1||b.y<v.y-1||b.x+b.width>v.width+1||b.y+b.height>v.height+1)issues.push({text:t.textContent,kind:'outside'});}for(const fo of svg.querySelectorAll('foreignObject')){const m=fo.querySelector('math');if(!m)continue;const a=fo.getBoundingClientRect(),b=m.getBoundingClientRect();if(b.left<a.left-1||b.right>a.right+1||b.top<a.top-1||b.bottom>a.bottom+1)issues.push({kind:'math clipping',math:m.textContent});}return{issues};}))()""")
 assert len(report['staticBounds'])==5 and all(not v['issues']for v in report['staticBounds']),report['staticBounds']
 for n in[2,4,5,8,10,15,52,53]:
  sel=f'.exam-question[data-deep-index="{n}"] .concept-animation';js('(()=>{const h=document.querySelector('+json.dumps(sel)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host));c.api.show(c.api.model.frames.length-1);})()');capture(sel,f'question-{n}-delivery.png')
 for n in[3,5,6,8,9,10]:
  js('(()=>{const title=[...document.querySelectorAll("h3")].find(h=>h.textContent.startsWith("Challenge '+str(n)+'.")),h=title.nextElementSibling,c=ConceptAnimations.players.find(c=>h.contains(c.api.host));c.api.show(c.api.model.frames.length-1);h.dataset.finalCapture="'+str(n)+'";})()');capture('[data-final-capture="'+str(n)+'"]',f'challenge-{n}-delivery.png')
 for i in[0,2,4]:
  js('[...document.querySelectorAll("figure")]['+str(i)+'].dataset.finalStatic="'+str(i)+'"');capture('[data-final-static="'+str(i)+'"]',f'static-{i+1}-delivery.png')
 capture('#review','rules-delivery.png')
 report['responsive']=[]
 for width in[1360,768,390]:
  cdp('Emulation.setDeviceMetricsOverride',dict(width=width,height=1050,deviceScaleFactor=1,mobile=width<500));js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');row=js("({width:innerWidth,pageWidth:document.documentElement.scrollWidth,underlined:[...document.querySelectorAll('a')].filter(a=>getComputedStyle(a).textDecorationLine.includes('underline')).length,mathWrap:[...document.querySelectorAll('.exam-solution .math-inline')].filter(x=>getComputedStyle(x).whiteSpace!=='nowrap').length})");assert row['pageWidth']<=width+2 and row['underlined']==0 and row['mathWrap']==0,row;report['responsive'].append(row)
  if width==390:capture('.exam-question[data-deep-index="4"]','question-4-mobile-delivery.png')
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url='http://127.0.0.1:8771/chapters/a_asym.html'))
 for _ in range(100):
  if js('!!document.querySelector("[data-source-id=MS_CE_1405_Q58]")'):break
  time.sleep(.1)
 js('document.fonts.ready');js('document.querySelector("[data-source-id=MS_CE_1405_Q58] details").open=true')
 report['originalOptionErratum']=js("(()=>{const q=document.querySelector('[data-source-id=MS_CE_1405_Q58]');return{options:[...q.querySelectorAll('.exam-option math')].map(m=>m.getAttribute('aria-label')),solution:q.querySelector('details').textContent,errors:__errors};})()")
 assert report['originalOptionErratum']['options']==[r'O(\log n\log\log n)',r'O(n\log n\log\log n)',r'O(n\log\log n)',r'O(\log\log n)']
 assert 'options 2 and 3 are valid looser' in report['originalOptionErratum']['solution']and not report['originalOptionErratum']['errors']
 capture('[data-source-id=MS_CE_1405_Q58]','a-asym-original-options-delivery.png')
 report['status']='passed_pending_root_visual_inspection'
finally:
 (R/'research/deep-library-revision/a_recurrence-final-visual.json').write_text(json.dumps(report,indent=2)+'\n')
 proc.terminate()
print(report['status'])
