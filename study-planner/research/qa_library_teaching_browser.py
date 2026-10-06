"""Measure every redesigned model, then exercise the actual chapter controls."""
import json,os,time,subprocess,threading,tempfile,base64
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'library-decision-qa';OUT.mkdir(exist_ok=True);A=R/'research/library-animation-redesign'
class Handler(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=OUT/f'edge-{os.getpid()}';proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
report=dict(state='in_progress',models=[],chapters=[],controls={},runtimeErrors=[])
try:
 active=profile/'DevToolsActivePort'
 for _ in range(150):
  if active.exists():break
  time.sleep(.1)
 port=int(active.read_text().splitlines()[0]);page=next(p for p in requests.get(f'http://127.0.0.1:{port}/json').json() if p['type']=='page');ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=120);seq=0
 def cdp(method,params=None):
  global seq
  seq+=1;ws.send(json.dumps(dict(id=seq,method=method,params=params or {})))
  while True:
   r=json.loads(ws.recv())
   if r.get('id')==seq:
    if 'error' in r:raise RuntimeError(r)
    return r.get('result',{})
 def js(code):
  r=cdp('Runtime.evaluate',dict(expression=code,returnByValue=True,awaitPromise=True))
  if 'exceptionDetails' in r:raise RuntimeError(r['exceptionDetails'].get('exception',{}).get('description',r))
  return r.get('result',{}).get('value')
 def navigate(topic):
  cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/{topic}.html'));time.sleep(.3);js('document.fonts.ready')
 def shot(name):
  (OUT/name).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.error?.stack||e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"});cdp('Emulation.setDeviceMetricsOverride',dict(width=1280,height=1000,deviceScaleFactor=1,mobile=False));navigate('g_gates')
 js('Promise.all([...document.querySelectorAll(".concept-animation")].map(ConceptAnimations.ready))')
 js('''(async()=>{window.reviewData=await(await fetch('concept-animations.json')).json();window.reviewHost=document.createElement('section');reviewHost.className='concept-animation';document.querySelector('main').prepend(reviewHost);window.reviewPlayer=ConceptAnimations.mount(reviewHost,[reviewData.scenes.insertion]);})()''')
 for id in json.loads((R/'dist/chapters/concept-animations.json').read_text(encoding='utf-8'))['scenes']:
  row=js('''(()=>{const p=reviewPlayer;p.pause();p.scene=reviewData.scenes['''+json.dumps(id)+'''];const bad=[];for(let i=0;i<p.scene.frames.length;i++){p.show(i,false);bad.push(...DiagramLayout.audit(p.canvas).map(x=>({...x,frame:i})));const f=p.scene.frames[i],t=f.teaching,why=t.why.startsWith(t.operation)?t.why.slice(t.operation.length).trim():t.why;if(p.teaching.root.dataset.explanation!==f.caption||!p.teaching.root.querySelector('.teaching-operation').textContent.includes(t.operation)||(why&&!p.teaching.root.querySelector('.teaching-why')?.textContent.includes(why)))bad.push({kind:'missing causal explanation',frame:i});if(t.checks.length!==p.teaching.root.querySelectorAll('.teaching-test').length)bad.push({kind:'missing exact test',frame:i});}return {id:p.scene.id,frames:p.scene.frames.length,bad};})()''');report['models'].append(dict(file='concept-animations.json',**row))
 # All typed SVG diagrams in the dedicated chapters and question aids.
 for topic in ['a_arrays','a_stackqueue','d_counting','d_inclusion','d_pigeonhole']:
  navigate(topic);time.sleep(.2)
  rows=js('''(async()=>{const data=await(await fetch('''+json.dumps(topic+'-models.json')+''')).json(),host=document.createElement('section');host.className='''+json.dumps({'a_arrays':'arrays','a_stackqueue':'sq','d_counting':'counting','d_inclusion':'inclusion','d_pigeonhole':'pigeonhole'}[topic]+'-model')+''';host.innerHTML='<div class="review-stage"></div>';document.querySelector('main').prepend(host);const stage=host.firstChild,rows=[];for(const m of data.models){const p=TeachingTransitions.raw({host,model:m,stage}),bad=[];for(let i=0;i<m.frames.length;i++){p.show(i);for(const svg of stage.querySelectorAll('svg'))bad.push(...DiagramLayout.audit(svg).map(x=>({...x,frame:i})));if(!p.teaching.root.textContent.includes(m.frames[i].caption))bad.push({kind:'missing explanation',frame:i});}rows.push({id:m.id,frames:m.frames.length,bad});p.teaching.root.remove();}host.remove();return rows;})()''');report['models'] += [dict(file=topic+'-models.json',**r) for r in rows]
 navigate('d_logic');time.sleep(.2)
 rows=js('''(async()=>{const data=await(await fetch('problem-visual-models.json')).json(),host=document.createElement('section');host.className='problem-visual';host.innerHTML='<div class="problem-stage"></div>';document.querySelector('main').prepend(host);const stage=host.firstChild,rows=[];for(const [id,m] of Object.entries(data)){const p=TeachingTransitions.raw({host,model:m,stage}),bad=[];for(let i=0;i<m.frames.length;i++){p.show(i);for(const svg of stage.querySelectorAll('svg'))bad.push(...DiagramLayout.audit(svg).map(x=>({...x,frame:i})));}rows.push({id,frames:m.frames.length,bad});p.teaching.root.remove();}host.remove();return rows;})()''');report['models'] += [dict(file='problem-visual-models.json',**r) for r in rows]
 print(json.dumps(dict(models=len(report['models']),frames=sum(r['frames'] for r in report['models']),geometryIssues=sum(len(r['bad']) for r in report['models']))),flush=True)
 # The actual 37 pages, their lazy-loaded concepts, raw players, mobile containment and body counts.
 inventory=json.loads((A/'inventory.json').read_text(encoding='utf-8'))
 for chapter in inventory['chapters']:
  topic=chapter['topicId'];cdp('Emulation.setDeviceMetricsOverride',dict(width=1280,height=1000,deviceScaleFactor=1,mobile=False));navigate(topic)
  js('window.ConceptAnimations?Promise.all([...document.querySelectorAll(".concept-animation")].map(ConceptAnimations.ready)):Promise.resolve()')
  js('window.ProblemVisuals?Promise.all([...document.querySelectorAll("[data-problem-visual]")].map(ProblemVisuals.ready)):Promise.resolve()')
  row=js('({questions:document.querySelectorAll(".exam-question").length,failed:[...document.querySelectorAll("[data-loaded]")].filter(h=>h.dataset.loaded==="error").length,players:TeachingTransitions.players.length,panels:document.querySelectorAll(".teaching-panel").length,errors:__errors})')
  assert row['questions']==chapter['questions'],(topic,'lost questions',row,chapter)
  assert not row['failed'] and not row['errors'],(topic,row)
  cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=True));row['mobileOverflow']=js('document.documentElement.scrollWidth>innerWidth+1');assert not row['mobileOverflow'],(topic,row)
  row['topicId']=topic;report['chapters'].append(row)
 # Freeze a real moving record at an intermediate coordinate, then resume it.
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1280,height=1000,deviceScaleFactor=1,mobile=False));navigate('a_correct');js('Promise.all([...document.querySelectorAll(".concept-animation")].map(ConceptAnimations.ready))')
 js('window.testPlayer=ConceptAnimations.players.find(p=>p.scenes.some(s=>s.id==="insertion"));testPlayer.scene=testPlayer.scenes.find(s=>s.id==="insertion");testPlayer.show(2,false);testPlayer.host.scrollIntoView({block:"start"});testPlayer.buttons.next.click()');time.sleep(.2)
 js('testPlayer.pause();window.pausedPositions=JSON.stringify([...testPlayer.positions]);');time.sleep(.2)
 paused=js('({busy:testPlayer.busy,paused:testPlayer.pausedMotion,frozen:JSON.stringify([...testPlayer.positions])===pausedPositions})');assert paused['busy'] and paused['paused'] and paused['frozen'],paused;report['controls']['conceptPause']=paused
 js('testPlayer.buttons.play.click()');time.sleep(1.1);js('testPlayer.pause()');assert js('!testPlayer.pausedMotion');report['controls']['resume']=True
 shot('record-slots-desktop.png')
 navigate('a_stackqueue');time.sleep(.4);js('window.rawPlayer=TeachingTransitions.players.find(p=>p.model?.frames.some(f=>f.svg.includes("data-entity")));rawPlayer.host.scrollIntoView({block:"start"});rawPlayer.draw(0);rawPlayer.host.querySelector("[data-next]").click()');time.sleep(.1);js('rawPlayer.pause()');freeze=js('rawPlayer.host.querySelectorAll("svg")[0].getAnimations({subtree:true}).every(a=>a.playState==="paused"||a.playState==="finished")');assert freeze;report['controls']['rawPause']=freeze
 js('rawPlayer.host.querySelector("[data-seek]").value=2;rawPlayer.host.querySelector("[data-seek]").dispatchEvent(new Event("input"))');assert js('rawPlayer.index===2');report['controls']['seek']=True
 cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]});js('rawPlayer.draw(1,true)');assert js('rawPlayer.host.querySelectorAll("svg")[0].getAnimations({subtree:true}).length===0');report['controls']['reducedMotion']=True
 js('rawPlayer.print()');assert js('rawPlayer.host.querySelector(".sq-print-trace").querySelectorAll("figure").length===rawPlayer.model.frames.length');report['controls']['print']=True
 cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'no-preference'}]})
 js('rawPlayer.draw(0);rawPlayer.draw(1,true);rawPlayer.pause()');cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]});js('rawPlayer.host.querySelector("[data-play]").click()');assert js('rawPlayer.host.querySelectorAll("svg")[0].getAnimations({subtree:true}).every(a=>a.playState==="finished")');js('rawPlayer.pause()');report['controls']['reducedMotionAfterPause']=True
 cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'no-preference'}]});navigate('a_correct');js('Promise.all([...document.querySelectorAll(".concept-animation")].map(ConceptAnimations.ready))');js('window.testPlayer=ConceptAnimations.players.find(p=>p.scenes.some(s=>s.id==="insertion"));testPlayer.scene=testPlayer.scenes.find(s=>s.id==="insertion");testPlayer.show(2,false);testPlayer.host.scrollIntoView({block:"start"});testPlayer.buttons.next.click()');time.sleep(.1);js('testPlayer.pause()');cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]});js('testPlayer.buttons.play.click();testPlayer.pause();testPlayer.print()');assert js('!testPlayer.busy&&testPlayer.printTrace.querySelectorAll("figure").length===testPlayer.scene.frames.length&&[...testPlayer.printTrace.querySelectorAll("figcaption")].every(e=>e.textContent.startsWith("Step "))');report['controls']['conceptReducedMotionAfterPauseAndPrint']=True
 cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'no-preference'}]})
 for topic,name in [('g_gates','circuit'),('l_matrices','matrix'),('s_bayes','probability'),('p_arrays','storage'),('d_logic','logic')]:
  navigate(topic);js('Promise.all([...document.querySelectorAll(".concept-animation")].map(ConceptAnimations.ready))');js('ConceptAnimations.players[0].host.scrollIntoView({block:"start"});ConceptAnimations.players[0].show(1,false)');shot(name+'-desktop.png')
 cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/animation-review.html'));time.sleep(.3);js('document.fonts.ready');assert js('document.querySelectorAll("tbody tr").length===37&&!__errors.length');shot('review-desktop.png');cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=True));assert js('document.documentElement.scrollWidth<=innerWidth+2');report['controls']['reviewPage']=True
 bad=[r for r in report['models'] if r['bad']];report['state']='passed' if not bad else 'failed';report['geometryIssues']=sum(len(r['bad']) for r in bad)
 print(json.dumps(dict(state=report['state'],chapters=len(report['chapters']),models=len(report['models']),frames=sum(r['frames'] for r in report['models']),issues=report['geometryIssues'],examples=bad[:8],screenshots=str(OUT))),flush=True)
finally:
 (A/'browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
 proc.terminate();server.shutdown()
