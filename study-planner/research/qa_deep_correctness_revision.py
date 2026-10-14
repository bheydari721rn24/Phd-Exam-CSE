"""Verify all rendered model frames and controls, print, responsive layout and the retained search lab."""
from pathlib import Path
import base64,hashlib,json,os,subprocess,sys,tempfile,time
import requests,websocket
R=Path(__file__).resolve().parents[1];E=R/'research/deep-library-revision';O=Path(tempfile.gettempdir())/'deep-correctness-visual';O.mkdir(exist_ok=True)
profile=O/f'edge-{os.getpid()}';proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report={'status':'in_progress','topicId':'a_correct','screenshots':str(O)}
try:
 for _ in range(100):
  if(profile/'DevToolsActivePort').exists()and(profile/'DevToolsActivePort').read_text().strip():break
  time.sleep(.1)
 port=int((profile/'DevToolsActivePort').read_text().splitlines()[0]);page=next(x for x in requests.get(f'http://127.0.0.1:{port}/json').json()if x['type']=='page');ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=60)
 def cdp(method,params=None):
  global seq
  seq+=1;ws.send(json.dumps({'id':seq,'method':method,'params':params or{}}))
  while True:
   x=json.loads(ws.recv())
   if x.get('id')==seq:assert'error'not in x,x;return x.get('result',{})
 def js(code):
  x=cdp('Runtime.evaluate',{'expression':code,'returnByValue':True,'awaitPromise':True});assert'exceptionDetails'not in x,x;return x.get('result',{}).get('value')
 def shot(selector,name):
  js('document.querySelector('+json.dumps(selector)+').scrollIntoView({block:"start",behavior:"instant"})');js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');(O/name).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
 cdp('Page.enable');cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"})
 cdp('Emulation.setDeviceMetricsOverride',{'width':1360,'height':1080,'deviceScaleFactor':1,'mobile':False});cdp('Page.navigate',{'url':'http://127.0.0.1:8771/chapters/a_correct.html'})
 for _ in range(100):
  if js('!!window.ConceptAnimations'):break
  time.sleep(.1)
 assert js('!!window.ConceptAnimations');js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)');js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))')
 report['loadFailures']=js('[...document.querySelectorAll(".concept-animation")].filter(h=>h.dataset.loaded!=="true").map(h=>({scenes:h.dataset.scenes,state:h.dataset.loaded,text:h.textContent}))');assert not report['loadFailures'],report['loadFailures']
 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,solutions:document.querySelectorAll(".exam-solution").length,models:[...document.querySelectorAll(".exam-question .concept-animation")].map(h=>h.dataset.scenes),errors:__errors})');assert report['counts']['questions']==54 and report['counts']['solutions']==54 and len(report['counts']['models'])==54 and len(set(report['counts']['models']))==54 and not report['counts']['errors'],report['counts']
 report['frames']=js("""(()=>{const out=[];for(const c of ConceptAnimations.players){const old=c.scene;for(const scene of c.scenes){c.scene=scene;c.show(0);for(let i=0;i<scene.frames.length;i++){c.api.show(i);const svg=c.api.host.querySelector('svg'),v=svg.viewBox.baseVal,a=svg.getBoundingClientRect(),issues=DiagramLayout.audit(svg);for(const t of svg.querySelectorAll('text')){const b=t.getBoundingClientRect();if(b.left<a.left-1||b.top<a.top-1||b.right>a.right+1||b.bottom>a.bottom+1)issues.push({kind:'text outside svg',text:t.textContent});}for(const fo of svg.querySelectorAll('foreignObject')){const m=fo.querySelector('math');if(!m)continue;const a=fo.getBoundingClientRect(),b=m.getBoundingClientRect();if(b.top<a.top-1||b.bottom>a.bottom+1)issues.push({kind:'formula clipping',math:m.textContent});for(const t of svg.querySelectorAll('text')){const z=t.getBoundingClientRect();if(Math.min(b.right,z.right)-Math.max(b.left,z.left)>1&&Math.min(b.bottom,z.bottom)-Math.max(b.top,z.top)>1)issues.push({kind:'math/text overlap',text:t.textContent});}}out.push({scene:scene.id,index:i,height:v.height,issues});} }c.scene=old;c.show(0);}return out;})()""")
 assert sum(x['scene'].startswith('correctness-question-')for x in report['frames'])==203
 assert all(not x['issues']for x in report['frames']),[x for x in report['frames']if x['issues']]
 report['ports']=js("""(()=>{const out=[];for(const c of ConceptAnimations.players){const old=c.scene;for(const scene of c.scenes){if(!scene.id.startsWith('correctness-question-'))continue;c.scene=scene;c.show(0);for(let i=0;i<scene.frames.length;i++){c.api.show(i);const svg=c.api.host.querySelector('svg'),rects=[...svg.querySelectorAll('rect')].map(r=>r.getBBox()),near=(x,y)=>rects.some(r=>x>=r.x-.02&&x<=r.x+r.width+.02&&y>=r.y-.02&&y<=r.y+r.height+.02&&Math.min(Math.abs(x-r.x),Math.abs(x-r.x-r.width),Math.abs(y-r.y),Math.abs(y-r.y-r.height))<.02);for(const p of svg.querySelectorAll('[data-correctness-ports]')){const v=p.dataset.correctnessPorts.split(',').map(Number),id=p.getAttribute('marker-end')?.match(/#([^)]*)/)?.[1];out.push({scene:scene.id,frame:i,attached:(()=>{const m=svg.getScreenCTM().inverse().multiply(p.getScreenCTM()),a=p.getPointAtLength(0).matrixTransform(m),b=p.getPointAtLength(p.getTotalLength()).matrixTransform(m);return near(a.x,a.y)&&near(b.x,b.y);})(),declaredAttached:near(v[0],v[1])&&near(v[2],v[3]),marker:!!id&&!!svg.querySelector('[id="'+id+'"]')});}}}c.scene=old;c.show(0);}return out;})()""");assert report['ports']and all(x['attached']and x['marker']for x in report['ports'])
 report['controls']=js("""(()=>{const out=[];for(const c of ConceptAnimations.players.filter(c=>c.scene.id.startsWith('correctness-question-'))){c.api.show(0);c.buttons.next.click();const next=c.api.index===Math.min(1,c.scene.frames.length-1);c.buttons.back.click();const back=c.api.index===0;c.seek.value=c.scene.frames.length-1;c.seek.dispatchEvent(new Event('input',{bubbles:true}));const seek=c.api.index===c.scene.frames.length-1;c.buttons.reset.click();out.push({scene:c.scene.id,next,back,seek,reset:c.api.index===0});}return out;})()""");assert len(report['controls'])==54 and all(all(x[k]for k in['next','back','seek','reset'])for x in report['controls'])
 # Exercise actual play/pause buttons for all multiple-frame question players. Their timer progresses while visible.
 count=js("window.__playPlayers=ConceptAnimations.players.filter(c=>c.scene.id.startsWith('correctness-question-')&&c.scene.frames.length>1);__playPlayers.length")
 report['playPause']=[]
 if '--reuse-playback' in sys.argv:
  prior=json.loads((E/'a_correct-controls-browser.json').read_text());assert prior['status']=='passed_controls_and_playback_only'
  for key,path in [('modelDataSha256','concept-animations.json'),('playerScriptSha256','concept-unified.js')]:assert prior[key]==hashlib.sha256((R/'dist/chapters'/path).read_bytes()).hexdigest()
  report['playbackReuseScope']='The model data and player script are byte-identical to the actual 47-player playback pass. Connector routing and arrowhead colors were then repaired; the current render, geometry and controls are checked independently in this pass.'
  assert len(prior['playPause'])==count and all(x['started']and x['advanced']and x['stopped']for x in prior['playPause']);report['playPause']=prior['playPause'];report['playbackEvidence']='research/deep-library-revision/a_correct-controls-browser.json';count=0
 for first in range(0,count,10):
  results=js("""(async()=>{const out=[];for(const c of __playPlayers.slice(FIRST,LAST)){c.host.scrollIntoView({block:'center',behavior:'instant'});await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));const speed=c.workspace.querySelector('[data-speed]');speed.value='1400';speed.dispatchEvent(new Event('change'));c.api.show(0);c.buttons.play.click();const started=c.running;await new Promise(r=>setTimeout(r,1550));const advanced=c.api.index>0;c.buttons.play.click();const stopped=!c.running;c.pause();out.push({scene:c.scene.id,started,advanced,stopped});}return out;})()""".replace('FIRST',str(first)).replace('LAST',str(first+10)))
  report['playPause'].extend(results);assert all(x['started']and x['advanced']and x['stopped']for x in results),results
  print('Verified playback group '+str(first//10+1),flush=True)
 report['lab']=[]
 for preset,expected,status in[('duplicates','1','terminated'),('empty','0','terminated'),('stall','0','stalled')]:
  js('document.querySelector('+json.dumps('[data-search-preset='+preset+']')+').click()');flags=js('({...document.getElementById("search-output").dataset})');assert flags['result']==expected and flags['status']==status and flags['invariant']=='true',flags;report['lab'].append(flags)
 report['staticFigures']=js("""(()=>[...document.querySelectorAll('figure svg')].map(svg=>{const v=svg.viewBox.baseVal,issues=DiagramLayout.audit(svg);for(const t of svg.querySelectorAll('text')){const b=t.getBBox();if(b.x<v.x-1||b.y<v.y-1||b.x+b.width>v.x+v.width+1||b.y+b.height>v.y+v.height+1)issues.push({kind:'outside',text:t.textContent});}return{label:svg.getAttribute('aria-labelledby'),issues};}))()""");assert all(not x['issues']for x in report['staticFigures']),report['staticFigures']
 for n in[2,3,8,10,17,23,24,29,38,41,44,45,47,48,49]:
  sel=f'.exam-question[data-deep-index="{n}"] .concept-animation';js('(()=>{const h=document.querySelector('+json.dumps(sel)+'),c=ConceptAnimations.players.find(c=>c.host===h);c.api.show(c.scene.frames.length-1);})()');shot(sel,f'question-{n}.png')
 shot('#review','final-decisions.png');shot('#proof-construction','proof-constructions.png')
 report['responsive']=[]
 for width in[1360,768,390]:
  cdp('Emulation.setDeviceMetricsOverride',{'width':width,'height':1080,'deviceScaleFactor':1,'mobile':width==390});js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
  row=js('({width:innerWidth,pageWidth:document.documentElement.scrollWidth,underlines:[...document.querySelectorAll("a")].filter(a=>getComputedStyle(a).textDecorationLine.includes("underline")).length,mathFont:getComputedStyle(document.querySelector(".exam-solution math")).fontFamily,errors:__errors})');assert row['pageWidth']<=width+2 and not row['underlines']and not row['errors'],row;report['responsive'].append(row)
  if width==390:shot('.exam-question[data-deep-index="49"] .concept-animation','tree-mobile.png')
 cdp('Emulation.setEmulatedMedia',{'media':'print'});js('dispatchEvent(new Event("beforeprint"))');report['print']=js('({solutions:[...document.querySelectorAll(".exam-solution")].every(d=>d.open),sceneCount:ConceptAnimations.players.length,errors:__errors})');assert report['print']['solutions']and not report['print']['errors']
 report['status']='passed_rendered_control_responsive_print_checks'
finally:
 proc.terminate()
 try:proc.wait(timeout=10)
 except subprocess.TimeoutExpired:proc.kill()
 (E/'a_correct-browser.json').write_text(json.dumps(report,indent=2)+'\n')
print({'status':report['status'],'frames':len(report.get('frames',[])),'ports':len(report.get('ports',[])),'controls':len(report.get('controls',[])),'playPause':len(report.get('playPause',[])),'screenshots':str(O)})
