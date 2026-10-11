"""Inspect the actual rendered chapter, mathematics, solution tables and retained players."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,time
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'deep-asym-browser';OUT.mkdir(exist_ok=True)
profile=OUT/f'edge-{os.getpid()}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report={'status':'in_progress','topicId':'a_asym','screenshots':str(OUT)}
try:
 for _ in range(100):
  if(profile/'DevToolsActivePort').exists():break
  time.sleep(.1)
 port=int((profile/'DevToolsActivePort').read_text().splitlines()[0]);page=next(p for p in requests.get(f'http://127.0.0.1:{port}/json').json()if p['type']=='page');ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=60)
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
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url='http://127.0.0.1:8771/chapters/a_asym.html'))
 for _ in range(100):
  if js('!!window.ConceptAnimations'):break
  time.sleep(.1)
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))')
 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,solutions:document.querySelectorAll(".exam-solution").length,questionTables:document.querySelectorAll(".exam-solution table").length,math:document.querySelectorAll("math").length,errors:__errors})')
 assert report['counts']['questions']==46 and report['counts']['solutions']==46 and report['counts']['questionTables']==7 and not report['counts']['errors'],report['counts']
 report['fonts']=js('({math:getComputedStyle(document.querySelector(".exam-solution math")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),prose:document.fonts.check("18px \'Source Sans 3\'")})');assert report['fonts']['stix']and report['fonts']['prose']
 report['delimiters']=js("""(()=>{const bad=[];for(const m of document.querySelectorAll('.exam-solution math'))for(const x of m.querySelectorAll('msup,msub,msubsup'))if([')',']','}'].includes(x.firstElementChild?.textContent))bad.push(m.getAttribute('aria-label'));return bad;})()""")
 assert not report['delimiters']
 report['models']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){const start=c.scene;for(const s of c.scenes){c.scene=s;c.show(0);const p=c.api;let issues=[];for(let i=0;i<p.model.frames.length;i++){p.show(i);issues.push(...DiagramLayout.audit(p.host.querySelector('svg')).map(x=>({...x,frame:i})));}rows.push({id:p.model.id,frames:p.model.frames.length,issues});}c.scene=start;c.show(0);}return rows;})()""")
 assert report['models'] and all(not p['issues']for p in report['models']),report['models']
 capture('.concept-animation','threshold-animation.png')
 report['controlChecks']=[]
 for sid,count in [('asym-parity-ratio',16),('asym-log-oscillation',8),('asym-floor-ratio',10)]:
  sel='.question-specific-animation[data-scenes="'+sid+'"]'
  row=js('(()=>{const h=document.querySelector('+json.dumps(sel)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host)),w=c.api.host,checks=[];c.api.show(2);w.querySelector("[data-view=before]").click();checks.push(w.dataset.displayedFrame==="1");w.querySelector("[data-view=compare]").click();checks.push(w.querySelectorAll(".sim-compare svg").length===2);w.querySelector("[data-view=after]").click();w.querySelector("[data-next]").click();checks.push(c.api.index===3);w.querySelector("[data-prev]").click();checks.push(c.api.index===2);const seek=w.querySelector("[data-seek]");seek.value='+str(count-1)+';seek.dispatchEvent(new Event("input"));checks.push(c.api.index==='+str(count-1)+');w.querySelector("[data-reset]").click();checks.push(c.api.index===0);return {id:'+json.dumps(sid)+',checks};})()')
  report['controlChecks'].append(row);assert all(row['checks']),row
  for frame in [0,count//2,count-1]:
   js('(()=>{const h=document.querySelector('+json.dumps(sel)+');const c=ConceptAnimations.players.find(c=>c.api.host===h || h.contains(c.api.host));c.api.show('+str(frame)+');})()')
   capture(sel,sid+'-'+str(frame)+'.png')
 report['staticDiagrams']=js("""(()=>[...document.querySelectorAll('.logic-diagram svg')].map(svg=>{const v=svg.viewBox.baseVal;return{label:svg.getAttribute('aria-label'),outside:[...svg.querySelectorAll('text')].filter(t=>{const b=t.getBBox();return b.x<v.x||b.y<v.y||b.x+b.width>v.x+v.width||b.y+b.height>v.y+v.height;}).map(t=>t.textContent)}}))()""")
 assert all(not s['outside']for s in report['staticDiagrams']),report['staticDiagrams']
 capture('.logic-diagram','ratio-envelopes.png')
 capture('.logic-diagram:nth-of-type(2)','strict-hierarchy.png')
 for n in[1,2,3,4,7,10,12,16,45,46]:capture('.exam-question:nth-of-type('+str(n)+')'if False else f'.exam-question[data-deep-index="{n}"]',f'question-{n}.png')
 for sel,name in[('#mathematical-bridge','counting-bridge.png'),('#quick-reference','final-rules.png')]:capture(sel,name)
 report['responsive']=[]
 for width in[1360,768,390]:
  cdp('Emulation.setDeviceMetricsOverride',dict(width=width,height=1000,deviceScaleFactor=1,mobile=width<500))
  js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
  row=js("""(()=>{const b=document.documentElement;return{width:innerWidth,pageWidth:b.scrollWidth,tableOverflow:[...document.querySelectorAll('.exam-solution table')].map(t=>({left:t.getBoundingClientRect().left,right:t.getBoundingClientRect().right})).filter(t=>t.left<0||t.right>innerWidth+2),underlined:[...document.querySelectorAll('a')].filter(a=>getComputedStyle(a).textDecorationLine.includes('underline')).length};})()""")
  report['responsive'].append(row);assert row['pageWidth']<=width+2 and not row['tableOverflow']and not row['underlined'],row
  if width==390:capture('.exam-question[data-deep-index="3"]','question-3-mobile.png');capture('.exam-question[data-deep-index="6"]','question-6-mobile.png');capture('.question-specific-animation','parity-mobile.png')
 cdp('Emulation.setEmulatedMedia',dict(media='print'));js('dispatchEvent(new Event("beforeprint"))')
 report['print']=js('({solutions:[...document.querySelectorAll(".exam-solution")].filter(x=>getComputedStyle(x).display!=="none").length,errors:__errors})');assert report['print']['solutions']==46 and not report['print']['errors']
 report['status']='passed_pending_screenshot_inspection'
finally:
 (R/'research/deep-library-revision/a_asym-browser.json').write_text(json.dumps(report,indent=2)+'\n')
 proc.terminate()
print(json.dumps(report,indent=2))
