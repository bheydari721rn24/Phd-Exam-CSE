"""Inspect the actual rendered chapter, mathematics, solution tables and retained players."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,time
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'deep-matrices-browser';OUT.mkdir(exist_ok=True)
profile=OUT/f'edge-{os.getpid()}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report={'status':'in_progress','topicId':'l_matrices','screenshots':str(OUT)}
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
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url='http://127.0.0.1:8771/chapters/l_matrices.html'))
 for _ in range(100):
  if js('!!window.ConceptAnimations'):break
  time.sleep(.1)
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))')
 report['loadFailures']=js("[...document.querySelectorAll('.concept-animation')].filter(h=>h.dataset.loaded!=='true').map(h=>({scenes:h.dataset.scenes,state:h.dataset.loaded,text:h.textContent}))");assert not report['loadFailures'],report['loadFailures']
 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,solutions:document.querySelectorAll(".exam-solution").length,questionTables:document.querySelectorAll(".exam-solution table").length,math:document.querySelectorAll("math").length,errors:__errors})')
 assert report['counts']['questions']==47 and report['counts']['solutions']==47 and report['counts']['questionTables']>=4 and not report['counts']['errors'],report['counts']
 report['fonts']=js('({math:getComputedStyle(document.querySelector(".exam-solution math")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),prose:document.fonts.check("18px \'Source Sans 3\'")})');assert report['fonts']['stix']and report['fonts']['prose']
 report['delimiters']=js("""(()=>{const bad=[];for(const m of document.querySelectorAll('.exam-solution math'))for(const x of m.querySelectorAll('msup,msub,msubsup'))if([')',']','}'].includes(x.firstElementChild?.textContent))bad.push(m.getAttribute('aria-label'));return bad;})()""")
 assert not report['delimiters']
 report['models']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){const start=c.scene;for(const s of c.scenes){c.scene=s;c.show(0);const p=c.api;let issues=[];for(let i=0;i<p.model.frames.length;i++){p.show(i);issues.push(...DiagramLayout.audit(p.host.querySelector('svg')).map(x=>({...x,frame:i})));}rows.push({id:p.model.id,frames:p.model.frames.length,issues});}c.scene=start;c.show(0);}return rows;})()""")
 assert report['models'] and all(not p['issues']for p in report['models']),report['models']
 report['labelFormulaSeparation']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){if(!c.api.model.id.startsWith('matrices-question-'))continue;for(let i=0;i<c.api.model.frames.length;i++){c.api.show(i);const svg=c.api.host.querySelector('svg'),bad=[];for(const t of svg.querySelectorAll('text'))for(const m of svg.querySelectorAll('foreignObject math')){const a=t.getBoundingClientRect(),b=m.getBoundingClientRect();if(Math.min(a.right,b.right)-Math.max(a.left,b.left)>1&&Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top)>1)bad.push({text:t.textContent,textRect:{top:a.top,bottom:a.bottom},mathRect:{top:b.top,bottom:b.bottom}});}rows.push({id:c.api.model.id,frame:i,height:svg.viewBox.baseVal.height,overlaps:bad});}}return rows;})()""")
 assert len(report['labelFormulaSeparation'])>=60 and all(not x['overlaps'] and x['height']<=362 for x in report['labelFormulaSeparation']),report['labelFormulaSeparation']
 report['formulaContainment']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){if(!c.api.model.id.startsWith('matrices-question-'))continue;for(let i=0;i<c.api.model.frames.length;i++){c.api.show(i);for(const fo of c.api.host.querySelectorAll('svg foreignObject')){const m=fo.querySelector('math');if(!m)continue;const a=fo.getBoundingClientRect(),b=m.getBoundingClientRect();rows.push({id:c.api.model.id,frame:i,cut:b.top<a.top-1||b.bottom>a.bottom+1,mathHeight:b.height,boxHeight:a.height});}}}return rows;})()""")
 assert len(report['formulaContainment'])>=80 and all(not r['cut'] for r in report['formulaContainment']),report['formulaContainment']
 report['playPauseChecks']=js("""(async()=>{const rows=[];for(const c of ConceptAnimations.players){if(!c.api.model.id.startsWith('matrices-question-'))continue;const w=c.api.host;c.api.show(0);const play=w.querySelector('[data-play]'),speed=w.querySelector('[data-speed]');speed.value='1400';speed.dispatchEvent(new Event('change'));play.click();await new Promise(r=>setTimeout(r,1600));play.click();const stopped=c.api.index;await new Promise(r=>setTimeout(r,150));rows.push({id:c.api.model.id,advanced:stopped>0,paused:c.api.index===stopped&&play.getAttribute('aria-pressed')==='false'});w.querySelector('[data-reset]').click();}return rows;})()""")
 assert len(report['playPauseChecks'])==16 and all(x['advanced'] and x['paused'] for x in report['playPauseChecks']),report['playPauseChecks']
 capture('.concept-animation','threshold-animation.png')
 report['controlChecks']=[]
 for sid,count in [('matrices-question-source', 4), ('matrices-question-allones', 4), ('matrices-question-shear', 3), ('matrices-question-fixed', 6), ('matrices-question-power', 6), ('matrices-question-rank', 4), ('matrices-question-basis', 4), ('matrices-question-block', 4), ('matrices-question-gram', 4), ('matrices-question-positivity3', 5), ('matrices-question-positivity4', 5), ('matrices-question-trace', 3), ('matrices-question-blockidentity', 4), ('matrices-question-power10', 11)]:
  sel='.concept-animation[data-scenes="'+sid+'"]'
  row=js('(()=>{const h=document.querySelector('+json.dumps(sel)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host)),w=c.api.host,checks=[];c.api.show(1);w.querySelector("[data-view=before]").click();checks.push(w.dataset.displayedFrame==="0");w.querySelector("[data-view=compare]").click();checks.push(w.querySelectorAll(".sim-compare svg").length===2);w.querySelector("[data-view=after]").click();w.querySelector("[data-next]").click();checks.push(c.api.index===2);w.querySelector("[data-prev]").click();checks.push(c.api.index===1);const seek=w.querySelector("[data-seek]");seek.value='+str(count-1)+';seek.dispatchEvent(new Event("input"));checks.push(c.api.index==='+str(count-1)+');w.querySelector("[data-reset]").click();checks.push(c.api.index===0);return {id:'+json.dumps(sid)+',checks};})()')
  report['controlChecks'].append(row);assert all(row['checks']),row
  for frame in [0,count//2,count-1]:
   js('(()=>{const h=document.querySelector('+json.dumps(sel)+');const c=ConceptAnimations.players.find(c=>c.api.host===h || h.contains(c.api.host));c.api.show('+str(frame)+');})()')
   capture(sel,sid+'-'+str(frame)+'.png')
 report['staticDiagrams']=js("""(()=>[...document.querySelectorAll('.matrix-figure svg')].map(svg=>{const v=svg.viewBox.baseVal;return{label:svg.getAttribute('aria-label'),outside:[...svg.querySelectorAll('text')].filter(t=>{const b=t.getBBox();return b.x<v.x||b.y<v.y||b.x+b.width>v.x+v.width||b.y+b.height>v.y+v.height;}).map(t=>t.textContent)}}))()""")
 assert all(not s['outside']for s in report['staticDiagrams']),report['staticDiagrams']
 capture('.matrix-figure','matrix-product-static.png')
 capture('.matrix-figure:nth-of-type(2)','matrix-composition-static.png')
 for n in[1,2,3,4,5,9,13,17,22,29,33,38,39,41,42,43,44,45,46,47]:capture('.exam-question:nth-of-type('+str(n)+')'if False else f'.exam-question[data-deep-index="{n}"]',f'question-{n}.png')
 for sel,name in[('#mathematical-bridge','counting-bridge.png'),('#quick-reference','final-rules.png')]:capture(sel,name)
 report['compositionLaboratory']=js("""(()=>{const rows=[];for(const values of [[0,100,100,100],[90,0,100,100],[180,100,100,100],[90,100,100,100],[45,-200,-150,150],[90,100,0,0]]){for(const [id,v] of ['angle','shear','x','y'].map((id,i)=>[id,values[i]])){const e=document.getElementById('matrix-'+id);e.value=v;e.dispatchEvent(new Event('input'));}const d=document.querySelector('#matrix-result').dataset;rows.push({values,commute:d.commute,gap:Number(d.gap),first:JSON.parse(d.first),second:JSON.parse(d.second)});}return rows;})()""")
 assert all(abs(sum((a-b)**2 for a,b in zip(r['first'],r['second']))-r['gap'])<1e-9 for r in report['compositionLaboratory'])
 assert [r['commute'] for r in report['compositionLaboratory']]==['true','true','true','false','false','false'] and report['compositionLaboratory'][-1]['gap']==0
 capture('.matrix-lab','composition-laboratory.png')
 report['responsive']=[]
 for width in[1360,768,390]:
  cdp('Emulation.setDeviceMetricsOverride',dict(width=width,height=1000,deviceScaleFactor=1,mobile=width<500))
  js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
  row=js("""(()=>{const b=document.documentElement;return{width:innerWidth,pageWidth:b.scrollWidth,tableOverflow:[...document.querySelectorAll('.exam-solution table')].map(t=>({left:t.getBoundingClientRect().left,right:t.getBoundingClientRect().right})).filter(t=>t.left<0||t.right>innerWidth+2),underlined:[...document.querySelectorAll('a')].filter(a=>getComputedStyle(a).textDecorationLine.includes('underline')).length};})()""")
  report['responsive'].append(row);assert row['pageWidth']<=width+2 and not row['tableOverflow']and not row['underlined'],row
  if width==390:capture('.exam-question[data-deep-index="3"]','question-3-mobile.png');capture('.exam-question[data-deep-index="6"]','question-6-mobile.png');capture('.question-specific-animation','matrix-question-mobile.png')
 cdp('Emulation.setEmulatedMedia',dict(media='print'));js('dispatchEvent(new Event("beforeprint"))')
 report['print']=js('({solutions:[...document.querySelectorAll(".exam-solution")].filter(x=>getComputedStyle(x).display!=="none").length,errors:__errors})');assert report['print']['solutions']==47 and not report['print']['errors']
 report['status']='passed_pending_screenshot_inspection'
finally:
 (R/'research/deep-library-revision/l_matrices-browser.json').write_text(json.dumps(report,indent=2)+'\n')
 proc.terminate()
print(json.dumps(report,indent=2))
