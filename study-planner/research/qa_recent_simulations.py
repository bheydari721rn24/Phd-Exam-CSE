"""Real-browser review of every stored model and checkpoint in the revision scope."""
from pathlib import Path
import base64,json,os,subprocess,tempfile,threading,time
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=R/'research/recent-animation-redesign';SCREEN=Path(tempfile.gettempdir())/'recent-simulation-qa';SCREEN.mkdir(exist_ok=True)
TOPICS={'a_select':'SelectPlayers','s_descriptive':'StatisticsPlayers','s_discrete':'DiscretePlayers','s_expectation':'ExpectationPlayers','l_det':'DeterminantPlayers','l_spaces':'VectorSpacePlayers','i_agents':'AgentPlayers','i_uninformed':'SearchPlayers','p_strings':'StringPlayers','p_recursion':'RecursionPlayers'}
LABS={'a_select':('select','SelectLab','values','!'),'s_descriptive':('stat','StatisticsLab','values','!'),'s_discrete':('disc','DiscreteLab','values','!'),'s_expectation':('exp','ExpectationLab','values','!'),'l_det':('det','DeterminantLab','matrix','!'),'l_spaces':('vs','VectorSpaceLab','matrix','!'),'i_agents':('ag','AgentLab','prior','!'),'i_uninformed':('us','SearchLab','edges','!'),'p_strings':('st','StringLab','capacity','-999'),'p_recursion':('rc','RecursionLab','n','-999')}
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=SCREEN/f'edge-{os.getpid()}';proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report={'status':'in_progress','chapters':{},'screenshots':str(SCREEN)}
try:
 for _ in range(100):
  if(profile/'DevToolsActivePort').exists():break
  time.sleep(.1)
 port=int((profile/'DevToolsActivePort').read_text().splitlines()[0]);page=next(p for p in requests.get(f'http://127.0.0.1:{port}/json').json()if p['type']=='page');ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=120)
 def cdp(method,params=None):
  global seq
  seq+=1;ws.send(json.dumps(dict(id=seq,method=method,params=params or{})))
  while True:
   r=json.loads(ws.recv())
   if r.get('id')==seq:
    if 'error'in r:raise Exception(r)
    return r.get('result',{})
 def js(code):
  r=cdp('Runtime.evaluate',dict(expression=code,returnByValue=True,awaitPromise=True));assert 'exceptionDetails'not in r,r;return r.get('result',{}).get('value')
 def capture(sel,name):
  js('document.querySelector('+json.dumps(sel)+').scrollIntoView({block:"center",behavior:"instant"})');js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');(SCREEN/name).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"})
 for topic,globalname in TOPICS.items():
  cdp('Emulation.setDeviceMetricsOverride',dict(width=1440,height=1100,deviceScaleFactor=1,mobile=False));cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]});cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/{topic}.html'))
  for _ in range(200):
   if js('window.'+globalname+'?.length>0'):break
   time.sleep(.1)
  js('document.fonts.ready');result={'errors':js('__errors'),'counts':js('({players:'+globalname+'.length,questions:document.querySelectorAll(".exam-question").length,rules:document.querySelectorAll(".review-rule").length})')};report['chapters'][topic]=result
  audit='''(()=>{const seen=new Set(),rows=[];for(const p of PLAYERS){if(seen.has(p.model.id))continue;seen.add(p.model.id);const bad=[],renderers=new Set(),hash=JSON.stringify(p.model.frames);for(let i=0;i<p.model.frames.length;i++){p.show(i);const svg=p.host.querySelector('.sim-stage svg');if(!svg){bad.push({frame:i,kind:'missing SVG'});continue;}renderers.add(p.host.dataset.renderer);if(p.host.dataset.frame!==String(i)||p.host.querySelector('[data-seek]').value!==String(i))bad.push({frame:i,kind:'wrong checkpoint'});if(!p.teaching.root.dataset.explanation)bad.push({frame:i,kind:'missing explanation'});if(p.host.querySelectorAll('.sim-timeline-list button').length!==p.model.frames.length)bad.push({frame:i,kind:'missing operation'});for(const t of svg.querySelectorAll('text')){const b=DiagramLayout.box(svg,t),vb=svg.viewBox.baseVal;if(!Number.isFinite(b.x)||b.x<-1||b.y<-1||b.x+b.w>vb.width+1||b.y+b.h>vb.height+1)bad.push({frame:i,kind:'text outside drawing',text:t.textContent,bounds:b});}const ids=[...svg.querySelectorAll('[id]')].map(n=>n.id);if(new Set(ids).size!==ids.length)bad.push({frame:i,kind:'duplicate SVG IDs'});}if(hash!==JSON.stringify(p.model.frames))bad.push({kind:'mutated scientific frames'});rows.push({id:p.model.id,kind:p.model.kind,frames:p.model.frames.length,renderers:[...renderers],issues:bad});p.show(0);}return rows;})()'''.replace('PLAYERS',globalname)
  result['models']=js(audit);result['errors']=js('__errors')
  assert {m['id']for m in result['models']}=={m['id']for m in json.loads((R/f'dist/chapters/{topic}-models.json').read_text())['models']}
  prefix,lab,badfield,badvalue=LABS[topic]
  result['editable']=js('''(()=>{const form=document.querySelector('#PREFIX-form');form.dispatchEvent(new Event('submit',{cancelable:true}));if(!window.LAB)return {error:document.querySelector('#PREFIX-error').textContent};const count=AdvancedSimulations.players.length;form.dispatchEvent(new Event('submit',{cancelable:true}));const p=window.LAB,issues=[];for(let i=0;i<p.model.frames.length;i++){p.show(i);const svg=p.host.querySelector('.sim-stage svg');for(const t of svg.querySelectorAll('text')){const b=DiagramLayout.box(svg,t),v=svg.viewBox.baseVal;if(b.x<-1||b.y<-1||b.x+b.w>v.width+1||b.y+b.h>v.height+1)issues.push({frame:i,text:t.textContent});}}const old=p,field=form.elements.BADFIELD,value=field.value;field.value=BADVALUE;form.dispatchEvent(new Event('submit',{cancelable:true}));const preserves=window.LAB===old&&document.querySelector('#PREFIX-error').textContent.length>0;field.value=value;form.dispatchEvent(new Event('submit',{cancelable:true}));return {frames:p.model.frames.length,issues,invalidPreserves:preserves,noPlayerLeak:AdvancedSimulations.players.length===count,error:document.querySelector('#PREFIX-error').textContent};})()'''.replace('PREFIX',prefix).replace('LAB',lab).replace('BADFIELD',badfield).replace('BADVALUE',json.dumps(badvalue)))
  assert result['editable'].get('frames')and not result['editable']['error']and not result['editable']['issues']and result['editable']['invalidPreserves']and result['editable']['noPlayerLeak'],result['editable']
  # Test both exact states, all controls, timeline seeking and immutable labels during replay.
  result['controls']=js('''(()=>{const p=PLAYERS.find(p=>p.model.frames.length>2),h=p.host;p.show(2);h.querySelector('[data-view=before]').click();const before=h.querySelector('.sim-stage svg').outerHTML;h.querySelector('[data-view=compare]').click();const compare=h.querySelectorAll('.sim-stage svg').length;h.querySelector('[data-view=after]').click();h.querySelector('[data-prev]').click();const prev=p.index;h.querySelector('[data-seek]').value=2;h.querySelector('[data-seek]').dispatchEvent(new Event('input'));const seek=p.index;h.querySelector('.sim-timeline-list button').click();const timeline=p.index;h.querySelector('[data-next]').click();const next=p.index;h.querySelector('[data-reset]').click();const reset=p.index;p.show(1);h.querySelector('[data-view=reference]').click();const reference=!!h.querySelector('.sim-stage svg');h.querySelector('[data-view=after]').click();p.print();const printed=h.querySelectorAll('.sim-print figure').length;p.clearPrint();return {before:before.length>100,compare,prev,seek,timeline,next,reset,reference,printed,expected:p.model.frames.length};})()'''.replace('PLAYERS',globalname))
  c=result['controls'];assert c['before']and c['compare']==2 and c['prev']==1 and c['seek']==2 and c['timeline']==0 and c['next']==1 and c['reset']==0 and c['reference']and c['printed']==c['expected'],c
  # Choose a substantial operation, not the untouched initial frame, for human visual inspection.
  chosen=js(globalname+'.find(p=>p.model.frames.length>3).model.id');js(globalname+'.find(p=>p.model.id==='+json.dumps(chosen)+').show(3)');capture('.sim-redesign[data-frame="3"] .sim-shell',topic+'.png')
  examples={'a_select':['three-way-selection'],'s_discrete':['geometric-wait'],'l_det':['cofactor-deletion'],'l_spaces':['matrix-column-selection'],'i_agents':['belief-bars','vacuum-motion'],'i_uninformed':['search-graph'],'p_recursion':['call-tree','hanoi-pegs']}
  for kind in examples.get(topic,[]):
   js('window.visualPlayer='+globalname+'.find(p=>p.model.kind==='+json.dumps(kind)+');visualPlayer.show(Math.min(8,visualPlayer.model.frames.length-1));visualPlayer.host.dataset.capture="current"');capture('[data-capture=current] .sim-shell',topic+'-'+kind+'.png');js('delete visualPlayer.host.dataset.capture')
  js(globalname+'.find(p=>p.model.id==='+json.dumps(chosen)+').show(3)');cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=True));result['mobileOverflow']=js('document.documentElement.scrollWidth>innerWidth+1');capture('.sim-redesign[data-frame="3"] .sim-shell',topic+'-mobile.png')
  cdp('Emulation.setDeviceMetricsOverride',dict(width=1440,height=1100,deviceScaleFactor=1,mobile=False));js('document.documentElement.style.fontSize="200%"');result['enlargedOverflow']=js('document.documentElement.scrollWidth>innerWidth+1');js('document.documentElement.style.fontSize=""');
  result['underlined']=js('[...document.querySelectorAll(".sim-redesign a,.sim-redesign summary")].filter(n=>getComputedStyle(n).textDecorationLine.includes("underline")).length')
  result['fonts']=js('({math:document.fonts.check("18px \'STIX Two Math\'"),code:document.fonts.check("16px \'JetBrains Mono\'"),prose:document.fonts.check("16px \'Source Sans 3\'")})');result['errors']=js('__errors');assert not result['errors'],result['errors']
  (OUT/'browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(topic,len(result['models']),'models;',sum(m['frames']for m in result['models']),'checkpoints;',sum(len(m['issues'])for m in result['models']),'geometry issues',flush=True)
 # Actual motion pause, resume, scrubbing and reduced-motion tests on recursion.
 cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'no-preference'}]});time.sleep(.1);js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');js('window.p=RecursionPlayers.find(p=>p.model.id==="hanoi-three");p.show(5);p.host.querySelector("[data-next]").click()');time.sleep(.2);js('p.pause();window.times=p.host.querySelector(".sim-stage").getAnimations({subtree:true}).map(a=>a.currentTime);window.progress=p.transition');time.sleep(.15)
 report['motionPause']=js('({motions:times.length,frozen:JSON.stringify(times)===JSON.stringify(p.host.querySelector(".sim-stage").getAnimations({subtree:true}).map(a=>a.currentTime)),geometryFrozen:p.transition===progress})');assert report['motionPause']['motions']and report['motionPause']['frozen']and report['motionPause']['geometryFrozen'],report['motionPause']
 js('p.host.querySelector("[data-play]").click()');time.sleep(.15);report['motionResume']=js('p.transition>progress');assert report['motionResume'];js('p.pause();p.show(6);p.host.querySelector(".sim-motion-control input").value=40;p.host.querySelector(".sim-motion-control input").dispatchEvent(new Event("input"))');report['manualTransition']=js('p.transition');assert report['manualTransition']==.4
 cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]});js('p.show(5);p.host.querySelector("[data-next]").click()');report['reducedMotion']=js('p.host.querySelector(".sim-stage").getAnimations({subtree:true}).length===0&&p.transition===1');assert report['reducedMotion'];
 report['status']='passed'if not any(m['issues']for c in report['chapters'].values()for m in c['models'])and not any(c['mobileOverflow']or c['enlargedOverflow']or c['errors']or c['underlined']for c in report['chapters'].values())else'needs_repair'
finally:
 (OUT/'browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');server.shutdown();proc.terminate()
print(json.dumps({'status':report['status'],'motionPause':report.get('motionPause'),'motionResume':report.get('motionResume')}))
