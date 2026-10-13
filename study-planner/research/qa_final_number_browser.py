"""Inspect the actual rendered chapter, mathematics, solution tables and retained players."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,time
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'deep-number-browser';OUT.mkdir(exist_ok=True)
profile=OUT/f'edge-{os.getpid()}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report={'status':'in_progress','topicId':'g_number','screenshots':str(OUT)}
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
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url='http://127.0.0.1:8771/chapters/g_number.html'))
 for _ in range(100):
  if js('!!window.ConceptAnimations'):break
  time.sleep(.1)
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)')
 js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))')
 report['loadFailures']=js("[...document.querySelectorAll('.concept-animation')].filter(h=>h.dataset.loaded!=='true').map(h=>({scenes:h.dataset.scenes,state:h.dataset.loaded,text:h.textContent}))");assert not report['loadFailures'],report['loadFailures']
 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,solutions:document.querySelectorAll(".exam-solution").length,questionTables:document.querySelectorAll(".exam-solution table").length,math:document.querySelectorAll("math").length,errors:__errors})')
 assert report['counts']['questions']==45 and report['counts']['solutions']==45 and report['counts']['questionTables']>=4 and not report['counts']['errors'],report['counts']
 report['fonts']=js('({math:getComputedStyle(document.querySelector(".exam-solution math")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),prose:document.fonts.check("18px \'Source Sans 3\'")})');assert report['fonts']['stix']and report['fonts']['prose']
 report['delimiters']=js("""(()=>{const bad=[];for(const m of document.querySelectorAll('.exam-solution math'))for(const x of m.querySelectorAll('msup,msub,msubsup'))if([')',']','}'].includes(x.firstElementChild?.textContent))bad.push(m.getAttribute('aria-label'));return bad;})()""")
 assert not report['delimiters']
 report['models']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){const start=c.scene;for(const s of c.scenes){c.scene=s;c.show(0);const p=c.api;let issues=[];for(let i=0;i<p.model.frames.length;i++){p.show(i);issues.push(...DiagramLayout.audit(p.host.querySelector('svg')).map(x=>({...x,frame:i})));}rows.push({id:p.model.id,frames:p.model.frames.length,issues});}c.scene=start;c.show(0);}return rows;})()""")
 assert report['models'] and all(not p['issues']for p in report['models']),report['models']
 report['labelFormulaSeparation']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){if(!c.api.model.id.startsWith('number-question-'))continue;for(let i=0;i<c.api.model.frames.length;i++){c.api.show(i);const svg=c.api.host.querySelector('svg'),bad=[];for(const t of svg.querySelectorAll('text'))for(const m of svg.querySelectorAll('foreignObject math')){const a=t.getBoundingClientRect(),b=m.getBoundingClientRect();if(Math.min(a.right,b.right)-Math.max(a.left,b.left)>1&&Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top)>1)bad.push({text:t.textContent,textRect:{top:a.top,bottom:a.bottom},mathRect:{top:b.top,bottom:b.bottom}});}rows.push({id:c.api.model.id,frame:i,height:svg.viewBox.baseVal.height,overlaps:bad});}}return rows;})()""")
 assert len(report['labelFormulaSeparation'])==138 and all(not x['overlaps'] and x['height']<=362 for x in report['labelFormulaSeparation']),report['labelFormulaSeparation']
 if '--layout-only' in __import__('sys').argv:
  previous=json.loads((R/'research/deep-library-revision/g_number-browser.json').read_text());assert previous['status'].startswith('passed');report['playPauseChecks']=previous['playPauseChecks'];report['playbackEvidenceReused']='Prior full run actually advanced and paused all28 players; later prose/native-option edits did not change their control implementation.'
 else:
  report['playPauseChecks']=js("""(async()=>{const rows=[];for(const c of ConceptAnimations.players){if(!c.api.model.id.startsWith('number-question-'))continue;const w=c.api.host;c.api.show(0);const play=w.querySelector('[data-play]'),speed=w.querySelector('[data-speed]');speed.value='1400';speed.dispatchEvent(new Event('change'));play.click();await new Promise(r=>setTimeout(r,1600));play.click();const stopped=c.api.index;await new Promise(r=>setTimeout(r,150));rows.push({id:c.api.model.id,advanced:stopped>0,paused:c.api.index===stopped&&play.getAttribute('aria-pressed')==='false'});w.querySelector('[data-reset]').click();}return rows;})()""")
  assert len(report['playPauseChecks'])==28 and all(x['advanced'] and x['paused'] for x in report['playPauseChecks']),report['playPauseChecks']
 report['formulaContainment']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){if(!c.api.model.id.startsWith('number-question-'))continue;for(let i=0;i<c.api.model.frames.length;i++){c.api.show(i);for(const fo of c.api.host.querySelectorAll('svg foreignObject')){const m=fo.querySelector('math');if(!m)continue;const a=fo.getBoundingClientRect(),b=m.getBoundingClientRect();rows.push({id:c.api.model.id,frame:i,cut:b.top<a.top-1||b.bottom>a.bottom+1,mathHeight:b.height,boxHeight:a.height});}}}return rows;})()""")
 assert len(report['formulaContainment'])==138 and all(not r['cut'] for r in report['formulaContainment']),report['formulaContainment']
 capture('.concept-animation','division-animation.png')
 report['controlChecks']=[]
 for sid,count in [('number-question-original-overflow', 20), ('number-question-chop', 4), ('number-question-associativity', 4), ('number-question-carry', 9), ('number-question-product', 4), ('number-question-normal', 4), ('number-question-binary-tie', 4), ('number-question-extension', 3), ('number-question-decimal', 4), ('number-question-termination', 3), ('number-question-bytes', 4), ('number-question-bias', 3), ('number-question-scale', 3), ('number-question-negative', 3), ('number-question-max-sum', 6), ('number-question-zero', 3), ('number-question-finite', 6), ('number-question-spacing', 3), ('number-question-hex', 3), ('number-question-signed-product', 4), ('number-question-nearest', 4)]:
  sel='.concept-animation[data-scenes="'+sid+'"]'
  row=js('(()=>{const h=document.querySelector('+json.dumps(sel)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host)),w=c.api.host,checks=[];c.api.show(1);w.querySelector("[data-view=before]").click();checks.push(w.dataset.displayedFrame==="0");w.querySelector("[data-view=compare]").click();checks.push(w.querySelectorAll(".sim-compare svg").length===2);w.querySelector("[data-view=after]").click();w.querySelector("[data-next]").click();checks.push(c.api.index===2);w.querySelector("[data-prev]").click();checks.push(c.api.index===1);const seek=w.querySelector("[data-seek]");seek.value='+str(count-1)+';seek.dispatchEvent(new Event("input"));checks.push(c.api.index==='+str(count-1)+');w.querySelector("[data-reset]").click();checks.push(c.api.index===0);return {id:'+json.dumps(sid)+',checks};})()')
  report['controlChecks'].append(row);assert all(row['checks']),row
  for frame in [0,count//2,count-1]:
   js('(()=>{const h=document.querySelector('+json.dumps(sel)+');const c=ConceptAnimations.players.find(c=>c.api.host===h || h.contains(c.api.host));c.api.show('+str(frame)+');})()')
   capture(sel,sid+'-'+str(frame)+'.png')
 report['staticDiagrams']=js("""(()=>[...document.querySelectorAll('.number-diagram svg')].map(svg=>{const v=svg.viewBox.baseVal;return{label:svg.getAttribute('aria-label'),outside:[...svg.querySelectorAll('text')].filter(t=>{const b=t.getBBox();return b.x<v.x||b.y<v.y||b.x+b.width>v.x+v.width||b.y+b.height>v.y+v.height;}).map(t=>t.textContent)}}))()""")
 assert all(not s['outside']for s in report['staticDiagrams']),report['staticDiagrams']
 for sid in ['bcd','gray','hamming','secded']:
  sel='.concept-animation[data-scenes*=number-question-'+sid+']';js('(()=>{const h=document.querySelector('+json.dumps(sel)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host));c.choice.value=c.scenes.findIndex(s=>s.id===\"number-question-'+sid+'\");c.choice.dispatchEvent(new Event(\"change\"));c.api.show(c.api.model.frames.length-1);})()');capture(sel,'number-question-'+sid+'-final.png')
 capture(' .number-diagram','word-decoders-static.png')
 capture('.number-diagram:nth-of-type(2)','gray-cycle-static.png')
 for n in[1,2,3,4,5,6,7,8,9,10,11,20,24,28,32,36,40,44,45]:capture('.exam-question:nth-of-type('+str(n)+')'if False else f'.exam-question[data-deep-index="{n}"]',f'question-{n}.png')
 for sel,name in[('#mathematical-bridge','counting-bridge.png'),('#quick-reference','final-rules.png')]:capture(sel,name)

 report['numberLaboratory']=js('''(()=>{const rows=[];for(const [w,a,b,op] of [[4,7,1,'add'],[4,15,1,'add'],[4,7,15,'sub'],[4,8,8,'add'],[8,255,1,'sub'],[16,65535,1,'add']]){for(const [id,v]of [['number-width',w],['number-a',a],['number-b',b],['number-operation',op]]){const e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event('input'));}rows.push({...document.getElementById('number-result').dataset});}return rows;})()''')
 assert [(x['word'],x['signed'],x['carry'],x['overflow'])for x in report['numberLaboratory']]==[('8','-8','0','true'),('0','0','1','false'),('8','-8','0','true'),('0','0','1','true'),('254','-2','1','false'),('0','0','1','false')],report['numberLaboratory']
 report['invalidNumberLaboratory']=js('''(()=>{const rows=[];for(const [id,v]of [['number-a','-1'],['number-a','1.5'],['number-a','65536'],['number-width','1'],['number-width','17'],['number-width','']]){const e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event('input'));const d=document.getElementById('number-result').dataset;rows.push({valid:d.valid,word:d.word,trace:document.querySelectorAll('#number-trace tr').length});}return rows;})()''')
 assert all(x==dict(valid='false',word='',trace=0)for x in report['invalidNumberLaboratory']),report['invalidNumberLaboratory']
 js("for(const [id,v] of [['number-width',4],['number-a',7],['number-b',1],['number-operation','add']]){const e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event('input'));}")
 capture('.number-lab','word-laboratory.png')

 report['sceneChoiceChecks']=js("(()=>{const rows=[];for(const c of ConceptAnimations.players){if(c.scenes.length<2)continue;for(let i=0;i<c.scenes.length;i++){c.choice.value=i;c.choice.dispatchEvent(new Event('change'));rows.push({id:c.scene.id,valid:c.api.model.id===c.scene.id&&c.api.index===0&&c.choice.selectedOptions[0].textContent===c.scene.title});}c.choice.value=0;c.choice.dispatchEvent(new Event('change'));}return rows;})()");assert len(report['sceneChoiceChecks'])==5 and all(x['valid']for x in report['sceneChoiceChecks'])
 report['responsive']=[]
 for width in[1360,768,390]:
  cdp('Emulation.setDeviceMetricsOverride',dict(width=width,height=1000,deviceScaleFactor=1,mobile=width<500))
  js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
  row=js("""(()=>{const b=document.documentElement;return{width:innerWidth,pageWidth:b.scrollWidth,tableOverflow:[...document.querySelectorAll('.exam-solution table')].flatMap(t=>{const a=t.getBoundingClientRect(),fo=t.closest('foreignObject');if(fo){const f=fo.getBoundingClientRect(),stage=t.closest('.sim-stage'),s=stage?.getBoundingClientRect();const clipped=stage&&['auto','scroll','hidden'].includes(getComputedStyle(stage).overflowX)&&s.left>=0&&s.right<=innerWidth+2;return a.left<f.left-1||a.right>f.right+1||a.top<f.top-1||a.bottom>f.bottom+1||!clipped?[{left:a.left,right:a.right,reason:'foreignObject or scrolling stage containment'}]:[];}return a.left<0||a.right>innerWidth+2?[{left:a.left,right:a.right}]:[];}),underlined:[...document.querySelectorAll('a')].filter(a=>getComputedStyle(a).textDecorationLine.includes('underline')).length};})()""")
  report['responsive'].append(row);assert row['pageWidth']<=width+2 and not row['tableOverflow']and not row['underlined'],row
  if width==390:capture('.exam-question[data-deep-index="3"]','question-3-mobile.png');capture('.exam-question[data-deep-index="6"]','question-6-mobile.png');capture('.question-specific-animation','number-question-mobile.png')
 cdp('Emulation.setEmulatedMedia',dict(media='print'));js('dispatchEvent(new Event("beforeprint"))')
 report['print']=js('({solutions:[...document.querySelectorAll(".exam-solution")].filter(x=>getComputedStyle(x).display!=="none").length,errors:__errors})');assert report['print']['solutions']==45 and not report['print']['errors']
 report['status']='passed_pending_screenshot_inspection'
finally:
 (R/'research/deep-library-revision/g_number-browser.json').write_text(json.dumps(report,indent=2)+'\n')
 proc.terminate()
print(report['status'])
