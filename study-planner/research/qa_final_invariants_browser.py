"""Inspect the actual rendered chapter, mathematics, solution tables and retained players."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,time
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'deep-invariants-browser';OUT.mkdir(exist_ok=True)
profile=OUT/f'edge-{os.getpid()}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report={'status':'in_progress','topicId':'d_invariants','screenshots':str(OUT)}
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
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url='http://127.0.0.1:8771/chapters/d_invariants.html'))
 for _ in range(100):
  if js('!!window.ConceptAnimations'):break
  time.sleep(.1)
 assert js('!!window.ConceptAnimations'), 'Chapter or renderer did not load'
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))')
 report['loadFailures']=js("[...document.querySelectorAll('.concept-animation')].filter(h=>h.dataset.loaded!=='true').map(h=>({scenes:h.dataset.scenes,state:h.dataset.loaded,text:h.textContent}))");assert not report['loadFailures'],report['loadFailures']

 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,solutions:document.querySelectorAll(".exam-solution").length,tutorials:[...document.querySelectorAll("h3")].filter(x=>x.textContent.startsWith("Tutorial ")).length,math:document.querySelectorAll("math").length,errors:__errors})');assert report['counts']['questions']==46 and report['counts']['solutions']==46 and report['counts']['tutorials']==49 and not report['counts']['errors'],report['counts']
 report['fonts']=js('({math:getComputedStyle(document.querySelector(".exam-solution math")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),prose:document.fonts.check("18px \'Source Sans 3\'")})');assert report['fonts']['stix'] and report['fonts']['prose']
 report['models']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){const first=c.scene;for(const scene of c.scenes){c.scene=scene;c.show(0);let issues=[];for(let i=0;i<c.api.model.frames.length;i++){c.api.show(i);issues.push(...DiagramLayout.audit(c.api.host.querySelector('svg')).map(x=>({...x,frame:i})));}rows.push({id:scene.id,frames:scene.frames.length,issues});}c.scene=first;c.show(0);}return rows;})()""")
 assert len(report['models'])==53 and all(not x['issues']for x in report['models']),report['models']
 report['frameRendering']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){const first=c.scene;for(const scene of c.scenes){c.scene=scene;c.show(0);for(let i=0;i<c.api.model.frames.length;i++){c.api.show(i);const svg=c.api.host.querySelector('svg'),bad=[];for(const t of svg.querySelectorAll('text'))for(const m of svg.querySelectorAll('foreignObject math')){const a=t.getBoundingClientRect(),b=m.getBoundingClientRect();if(Math.min(a.right,b.right)-Math.max(a.left,b.left)>1&&Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top)>1)bad.push({text:t.textContent,kind:'formula overlap'});}for(const fo of svg.querySelectorAll('foreignObject')){const m=fo.querySelector('math');if(!m)continue;const a=fo.getBoundingClientRect(),b=m.getBoundingClientRect();if(b.top<a.top-1||b.bottom>a.bottom+1)bad.push({kind:'formula clipping',math:m.textContent});}rows.push({id:scene.id,frame:i,height:svg.viewBox.baseVal.height,issues:bad});}}c.scene=first;c.show(0);}return rows;})()""")
 assert len(report['frameRendering'])==419 and all(not x['issues']and x['height']<=362 for x in report['frameRendering']),report['frameRendering']
 report['controls']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){const w=c.api.host,checks=[];c.api.show(1);w.querySelector('[data-view=before]').click();checks.push(w.dataset.displayedFrame==='0');w.querySelector('[data-view=compare]').click();checks.push(w.querySelectorAll('.sim-compare svg').length===2);w.querySelector('[data-view=after]').click();w.querySelector('[data-next]').click();checks.push(c.api.index===Math.min(2,c.api.model.frames.length-1));w.querySelector('[data-prev]').click();checks.push(c.api.index===Math.max(0,Math.min(2,c.api.model.frames.length-1)-1));const seek=w.querySelector('[data-seek]');seek.value=c.api.model.frames.length-1;seek.dispatchEvent(new Event('input'));checks.push(c.api.index===c.api.model.frames.length-1);w.querySelector('[data-reset]').click();checks.push(c.api.index===0);rows.push({id:c.api.model.id,checks});}return rows;})()""")
 assert len(report['controls'])==45 and all(all(x['checks'])for x in report['controls']),report['controls']
 report['selection']=js("(()=>{const rows=[];for(const c of ConceptAnimations.players){if(c.scenes.length<2)continue;for(let i=0;i<c.scenes.length;i++){c.choice.value=i;c.choice.dispatchEvent(new Event('change'));rows.push({id:c.scene.id,valid:c.api.model.id===c.scene.id&&c.api.index===0});}c.choice.value=0;c.choice.dispatchEvent(new Event('change'));}return rows;})()");assert len(report['selection'])==16 and all(x['valid']for x in report['selection'])
 report['playback']=[]
 for start in range(0,45,5):
  report['playback'].extend(js("""(async()=>{const rows=[];for(const c of ConceptAnimations.players.slice("""+str(start)+','+str(start+5)+""")){const w=c.api.host;c.api.show(0);const play=w.querySelector('[data-play]'),speed=w.querySelector('[data-speed]');speed.value='1400';speed.dispatchEvent(new Event('change'));play.click();await new Promise(r=>setTimeout(r,1550));play.click();const stopped=c.api.index;await new Promise(r=>setTimeout(r,150));rows.push({id:c.api.model.id,advanced:stopped>0,paused:c.api.index===stopped&&play.getAttribute('aria-pressed')==='false'});w.querySelector('[data-reset]').click();}return rows;})()"""))
 assert len(report['playback'])==45 and all(x['advanced']and x['paused']for x in report['playback']),report['playback']
 for n in[1,2,3,4,5,6,7,8,9,10,11,12,13,14,17,18,21,22,25,26,29,30,33,34,37,38,41,42,45,46]:
  sel=f'.exam-question[data-deep-index="{n}"] .concept-animation';js('(()=>{const h=document.querySelector('+json.dumps(sel)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host));c.api.show(c.api.model.frames.length-1);})()');capture(sel,f'question-{n}-final.png')
 capture('#mathematical-bridge','instruction-bridge.png');capture('#review','final-rules.png')
 report['staticDiagrams']=js("""(()=>[...document.querySelectorAll('figure svg')].map(svg=>{const v=svg.viewBox.baseVal,bad=[];for(const t of svg.querySelectorAll('text')){const b=t.getBBox();if(b.x<v.x-1||b.y<v.y-1||b.x+b.width>v.x+v.width+1||b.y+b.height>v.y+v.height+1)bad.push({kind:'outside',text:t.textContent});}for(const fo of svg.querySelectorAll('foreignObject')){const m=fo.querySelector('math');if(!m)continue;const a=fo.getBoundingClientRect(),b=m.getBoundingClientRect();if(b.left<a.left-1||b.right>a.right+1||b.top<a.top-1||b.bottom>a.bottom+1)bad.push({kind:'formula clipping',formula:m.textContent});}return{label:svg.getAttribute('aria-labelledby')||svg.dataset.schematic,issues:bad};}))()""");assert len(report['staticDiagrams'])>=4 and all(not x['issues']for x in report['staticDiagrams']),report['staticDiagrams']




 report['invariantsLab']=[]
 def flags():return js("({...document.getElementById('invariant-output').dataset})")
 assert flags()=={'safe':'true','preserved':'false','terminates':'true'},flags()
 for name,expected in [('noninductive',('true','false','true')),('inductive',('true','true','false')),('unsafe',('false','false','true')),('chain',('true','true','true')),('cycle',('true','true','false')),('badrank',('true','true','true'))]:
  js('document.querySelector("[data-preset='+name+']").click()');actual=flags();assert tuple(actual[k]for k in('safe','preserved','terminates'))==expected,(name,actual);report['invariantsLab'].append(dict(preset=name,flags=actual))
 assert 'Invalid on reachable edges' in js("document.getElementById('invariant-output').textContent")
 js('document.querySelector("[data-preset=chain]").click();document.querySelector(\'[data-member="0"]\').click()');assert flags()['safe']=='false';assert 'initial state 0 is excluded'in js("document.getElementById('invariant-output').textContent");report['invariantsLab'].append(dict(case='exclude initial state',flags=flags()))
 js('document.querySelector("[data-preset=chain]").click();document.querySelector(\'[data-edge="0,0"]\').click()');assert flags()['terminates']=='false';report['invariantsLab'].append(dict(case='add reachable self-loop',flags=flags()))
 js('document.querySelector("[data-preset=chain]").click();const r=document.querySelector(\'[data-rank="0"]\');r.value="-1";r.dispatchEvent(new Event("change",{bubbles:true}));');assert js('document.querySelector(\'[data-rank="0"]\').validity.customError');report['invalidRankInput']=True
 js('document.querySelector("[data-preset=noninductive]").click()')
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
 (R/'research/deep-library-revision/d_invariants-browser.json').write_text(json.dumps(report,indent=2)+'\n')
 proc.terminate()
print(report['status'])
