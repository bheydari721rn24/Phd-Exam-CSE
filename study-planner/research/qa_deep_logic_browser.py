"""Inspect the actual rendered chapter, mathematics, solution tables and retained players."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,time
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'deep-logic-browser';OUT.mkdir(exist_ok=True)
profile=OUT/f'edge-{os.getpid()}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report={'status':'in_progress','topicId':'d_logic','screenshots':str(OUT)}
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
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url='http://127.0.0.1:8771/chapters/d_logic.html'))
 for _ in range(100):
  if js('!!window.ConceptAnimations'):break
  time.sleep(.1)
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))')
 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,solutions:document.querySelectorAll(".exam-solution").length,questionTables:document.querySelectorAll(".exam-solution table").length,math:document.querySelectorAll("math").length,errors:__errors})')
 assert report['counts']['questions']==53 and report['counts']['solutions']==53 and report['counts']['questionTables']==12 and not report['counts']['errors'],report['counts']
 report['fonts']=js('({math:getComputedStyle(document.querySelector(".exam-solution math")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),prose:document.fonts.check("18px \'Source Sans 3\'")})');assert report['fonts']['stix']and report['fonts']['prose']
 report['delimiters']=js("""(()=>{const bad=[];for(const m of document.querySelectorAll('.exam-solution math'))for(const x of m.querySelectorAll('msup,msub,msubsup'))if([')',']','}'].includes(x.firstElementChild?.textContent))bad.push(m.getAttribute('aria-label'));return bad;})()""")
 assert not report['delimiters']
 report['models']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){const start=c.scene;for(const s of c.scenes){c.scene=s;c.show(0);const p=c.api;let issues=[];for(let i=0;i<p.model.frames.length;i++){p.show(i);issues.push(...DiagramLayout.audit(p.host.querySelector('svg')).map(x=>({...x,frame:i})));}rows.push({id:p.model.id,frames:p.model.frames.length,issues});}c.scene=start;c.show(0);}return rows;})()""")
 assert report['models'] and all(not p['issues']for p in report['models']),report['models']
 report['lab']=[]
 for kind in['imp','rewritten','converse','biconditional','composite']:
  got=js('(()=>{const s=document.querySelector("#formula-select");s.value='+json.dumps(kind)+';s.dispatchEvent(new Event("change"));return [...document.querySelectorAll("#truth-output tbody tr")].map(r=>[...r.children].map(c=>+c.textContent));})()')
  assert len(got)==8
  for p,q,r,v in got:
   expected=int((not p or q)if kind in['imp','rewritten']else(not q or p)if kind=='converse'else(p==q)if kind=='biconditional'else((p or q)and not r));assert v==expected,(kind,p,q,r,v,expected)
  report['lab'].append({'formula':kind,'verifiedRows':8})
 for n in[2,5,6,19,50,52,53]:capture('.exam-question:nth-of-type('+str(n)+')'if False else f'.exam-question[data-deep-index="{n}"]',f'question-{n}.png')
 for sel,name in[('#mathematical-bridge','counting-bridge.png'),('#quick-reference','final-rules.png')]:capture(sel,name)
 report['responsive']=[]
 for width in[1360,768,390]:
  cdp('Emulation.setDeviceMetricsOverride',dict(width=width,height=1000,deviceScaleFactor=1,mobile=width<500))
  js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
  row=js("""(()=>{const b=document.documentElement;return{width:innerWidth,pageWidth:b.scrollWidth,tableOverflow:[...document.querySelectorAll('.exam-solution table')].map(t=>({left:t.getBoundingClientRect().left,right:t.getBoundingClientRect().right})).filter(t=>t.left<0||t.right>innerWidth+2),underlined:[...document.querySelectorAll('a')].filter(a=>getComputedStyle(a).textDecorationLine.includes('underline')).length};})()""")
  report['responsive'].append(row);assert row['pageWidth']<=width+2 and not row['tableOverflow']and not row['underlined'],row
  if width==390:capture('.exam-question[data-deep-index="2"]','question-2-mobile.png');capture('.exam-question[data-deep-index="5"]','question-5-mobile.png')
 cdp('Emulation.setEmulatedMedia',dict(media='print'));js('dispatchEvent(new Event("beforeprint"))')
 report['print']=js('({solutions:[...document.querySelectorAll(".exam-solution")].filter(x=>getComputedStyle(x).display!=="none").length,errors:__errors})');assert report['print']['solutions']==53 and not report['print']['errors']
 report['status']='passed_pending_screenshot_inspection'
finally:
 (R/'research/deep-library-revision/d_logic-browser.json').write_text(json.dumps(report,indent=2)+'\n')
 proc.terminate()
print(json.dumps(report,indent=2))
