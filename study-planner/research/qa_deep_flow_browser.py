"""Inspect the actual rendered chapter, mathematics, solution tables and retained players."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,time
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'deep-flow-browser';OUT.mkdir(exist_ok=True)
profile=OUT/f'edge-{os.getpid()}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report={'status':'in_progress','topicId':'p_flow','screenshots':str(OUT)}
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
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url='http://127.0.0.1:8771/chapters/p_flow.html'))
 for _ in range(100):
  if js('!!window.ConceptAnimations'):break
  time.sleep(.1)
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))')
 report['loadFailures']=js("[...document.querySelectorAll('.concept-animation')].filter(h=>h.dataset.loaded!=='true').map(h=>({scenes:h.dataset.scenes,state:h.dataset.loaded,text:h.textContent}))");assert not report['loadFailures'],report['loadFailures']
 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,solutions:document.querySelectorAll(".exam-solution").length,questionTables:document.querySelectorAll(".exam-solution table").length,math:document.querySelectorAll("math").length,errors:__errors})')
 assert report['counts']['questions']==45 and report['counts']['solutions']==45 and report['counts']['questionTables']>=8 and not report['counts']['errors'],report['counts']
 report['fonts']=js('({math:getComputedStyle(document.querySelector(".exam-solution math")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),prose:document.fonts.check("18px \'Source Sans 3\'")})');assert report['fonts']['stix']and report['fonts']['prose']
 report['delimiters']=js("""(()=>{const bad=[];for(const m of document.querySelectorAll('.exam-solution math'))for(const x of m.querySelectorAll('msup,msub,msubsup'))if([')',']','}'].includes(x.firstElementChild?.textContent))bad.push(m.getAttribute('aria-label'));return bad;})()""")
 assert not report['delimiters']
 report['models']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){const start=c.scene;for(const s of c.scenes){c.scene=s;c.show(0);const p=c.api;let issues=[];for(let i=0;i<p.model.frames.length;i++){p.show(i);issues.push(...DiagramLayout.audit(p.host.querySelector('svg')).map(x=>({...x,frame:i})));}rows.push({id:p.model.id,frames:p.model.frames.length,issues});}c.scene=start;c.show(0);}return rows;})()""")
 assert report['models'] and all(not p['issues']for p in report['models']),report['models']
 report['labelFormulaSeparation']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){if(!c.api.model.id.startsWith('flow-question-'))continue;for(let i=0;i<c.api.model.frames.length;i++){c.api.show(i);const svg=c.api.host.querySelector('svg'),bad=[];for(const t of svg.querySelectorAll('text'))for(const m of svg.querySelectorAll('foreignObject math')){const a=t.getBoundingClientRect(),b=m.getBoundingClientRect();if(Math.min(a.right,b.right)-Math.max(a.left,b.left)>1&&Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top)>1)bad.push({text:t.textContent,textRect:{top:a.top,bottom:a.bottom},mathRect:{top:b.top,bottom:b.bottom}});}rows.push({id:c.api.model.id,frame:i,height:svg.viewBox.baseVal.height,overlaps:bad});}}return rows;})()""")
 assert len(report['labelFormulaSeparation'])==164 and all(not x['overlaps'] and x['height']<=362 for x in report['labelFormulaSeparation']),report['labelFormulaSeparation']
 report['formulaContainment']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){if(!c.api.model.id.startsWith('flow-question-'))continue;for(let i=0;i<c.api.model.frames.length;i++){c.api.show(i);for(const fo of c.api.host.querySelectorAll('svg foreignObject')){const m=fo.querySelector('math');if(!m)continue;const a=fo.getBoundingClientRect(),b=m.getBoundingClientRect();rows.push({id:c.api.model.id,frame:i,cut:b.top<a.top-1||b.bottom>a.bottom+1,mathHeight:b.height,boxHeight:a.height});}}}return rows;})()""")
 assert len(report['formulaContainment'])==164 and all(not r['cut'] for r in report['formulaContainment']),report['formulaContainment']
 report['playPauseChecks']=js("""(async()=>{const rows=[];for(const c of ConceptAnimations.players){if(!c.api.model.id.startsWith('flow-question-'))continue;const w=c.api.host;c.api.show(0);const play=w.querySelector('[data-play]'),speed=w.querySelector('[data-speed]');speed.value='1400';speed.dispatchEvent(new Event('change'));play.click();await new Promise(r=>setTimeout(r,1600));play.click();const stopped=c.api.index;await new Promise(r=>setTimeout(r,150));rows.push({id:c.api.model.id,advanced:stopped>0,paused:c.api.index===stopped&&play.getAttribute('aria-pressed')==='false'});w.querySelector('[data-reset]').click();}return rows;})()""")
 assert len(report['playPauseChecks'])==25 and all(x['advanced'] and x['paused'] for x in report['playPauseChecks']),report['playPauseChecks']
 capture('.concept-animation','threshold-animation.png')
 report['controlChecks']=[]
 for sid,count in [('flow-question-triples', 4), ('flow-question-split', 4), ('flow-question-copy-source', 9), ('flow-question-copy10', 8), ('flow-question-dangling', 3), ('flow-question-filter-odd', 8), ('flow-question-filter-third', 17), ('flow-question-sum-before', 7), ('flow-question-switch', 4), ('flow-question-orbit-unreachable', 7), ('flow-question-orbit-target', 7), ('flow-question-postfix', 5), ('flow-question-stateful', 12), ('flow-question-ranking', 7), ('flow-question-nested', 10), ('flow-question-threshold', 6), ('flow-question-binary-tree', 4), ('flow-question-toll', 5), ('flow-question-swap', 4), ('flow-question-posttest', 7), ('flow-question-priorities', 4)]:
  sel='.concept-animation[data-scenes="'+sid+'"]'
  row=js('(()=>{const h=document.querySelector('+json.dumps(sel)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host)),w=c.api.host,checks=[];c.api.show(1);w.querySelector("[data-view=before]").click();checks.push(w.dataset.displayedFrame==="0");w.querySelector("[data-view=compare]").click();checks.push(w.querySelectorAll(".sim-compare svg").length===2);w.querySelector("[data-view=after]").click();w.querySelector("[data-next]").click();checks.push(c.api.index===2);w.querySelector("[data-prev]").click();checks.push(c.api.index===1);const seek=w.querySelector("[data-seek]");seek.value='+str(count-1)+';seek.dispatchEvent(new Event("input"));checks.push(c.api.index==='+str(count-1)+');w.querySelector("[data-reset]").click();checks.push(c.api.index===0);return {id:'+json.dumps(sid)+',checks};})()')
  report['controlChecks'].append(row);assert all(row['checks']),row
  for frame in [0,count//2,count-1]:
   js('(()=>{const h=document.querySelector('+json.dumps(sel)+');const c=ConceptAnimations.players.find(c=>c.api.host===h || h.contains(c.api.host));c.api.show('+str(frame)+');})()')
   capture(sel,sid+'-'+str(frame)+'.png')
 report['staticDiagrams']=js("""(()=>[...document.querySelectorAll('.flow-diagram svg')].map(svg=>{const v=svg.viewBox.baseVal;return{label:svg.getAttribute('aria-label'),outside:[...svg.querySelectorAll('text')].filter(t=>{const b=t.getBBox();return b.x<v.x||b.y<v.y||b.x+b.width>v.x+v.width||b.y+b.height>v.y+v.height;}).map(t=>t.textContent)}}))()""")
 assert all(not s['outside']for s in report['staticDiagrams']),report['staticDiagrams']
 capture(' .flow-diagram','for-control-static.png')
 capture(' .flow-diagram:nth-of-type(2)','invariant-prefix-static.png')
 for n in[1,2,3,4,5,6,7,8,9,10,11,20,24,28,32,36,40,44,45]:capture('.exam-question:nth-of-type('+str(n)+')'if False else f'.exam-question[data-deep-index="{n}"]',f'question-{n}.png')
 for sel,name in[('#mathematical-bridge','counting-bridge.png'),('#quick-reference','final-rules.png')]:capture(sel,name)
 report['flowLaboratory']=js("""(()=>{const rows=[];for(const [mode,limit,start]of [['for',5,0],['while',5,0],['do',0,0],['bug',5,0],['break',5,0],['for',0,0],['do',5,12],['while',5,12],['bug',5,1]]){for(const [id,v]of [['flow-case',mode],['flow-limit',limit],['flow-start',start]]){const e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event('input'));}document.querySelector('#flow-end').click();const d=document.querySelector('#flow-state').dataset;rows.push({mode,limit,start,status:d.status,i:Number(d.i),sum:Number(d.sum),tests:Number(d.tests),entries:Number(d.entries),updates:Number(d.updates)});}return rows;})()""")
 assert [(x['status'],x['i'],x['sum'])for x in report['flowLaboratory']]==[('normal',5,4),('normal',5,10),('normal',1,0),('cycle',0,0),('break',3,3),('normal',0,0),('normal',13,12),('normal',12,0),('cycle',2,1)],report['flowLaboratory']
 assert [(x['tests'],x['entries'],x['updates'])for x in report['flowLaboratory'][:5]]==[(6,5,5),(6,5,5),(1,1,1),(1,1,0),(4,4,3)]
 capture('.flow-lab','execution-laboratory.png')
 report['responsive']=[]
 for width in[1360,768,390]:
  cdp('Emulation.setDeviceMetricsOverride',dict(width=width,height=1000,deviceScaleFactor=1,mobile=width<500))
  js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
  row=js("""(()=>{const b=document.documentElement;return{width:innerWidth,pageWidth:b.scrollWidth,tableOverflow:[...document.querySelectorAll('.exam-solution table')].map(t=>({left:t.getBoundingClientRect().left,right:t.getBoundingClientRect().right})).filter(t=>t.left<0||t.right>innerWidth+2),underlined:[...document.querySelectorAll('a')].filter(a=>getComputedStyle(a).textDecorationLine.includes('underline')).length};})()""")
  report['responsive'].append(row);assert row['pageWidth']<=width+2 and not row['tableOverflow']and not row['underlined'],row
  if width==390:capture('.exam-question[data-deep-index="3"]','question-3-mobile.png');capture('.exam-question[data-deep-index="6"]','question-6-mobile.png');capture('.question-specific-animation','flow-question-mobile.png')
 cdp('Emulation.setEmulatedMedia',dict(media='print'));js('dispatchEvent(new Event("beforeprint"))')
 report['print']=js('({solutions:[...document.querySelectorAll(".exam-solution")].filter(x=>getComputedStyle(x).display!=="none").length,errors:__errors})');assert report['print']['solutions']==45 and not report['print']['errors']
 report['status']='passed_pending_screenshot_inspection'
finally:
 (R/'research/deep-library-revision/p_flow-browser.json').write_text(json.dumps(report,indent=2)+'\n')
 proc.terminate()
print(report['status'])
