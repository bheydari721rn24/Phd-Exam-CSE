"""Real rendering, geometry, controls and independent laboratory fixtures."""
import base64,json,os,subprocess,tempfile,threading,time
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'a-stackqueue-visual-qa';OUT.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=OUT/f'edge-{os.getpid()}-{time.time_ns()}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;events=[];report=dict(topicId='a_stackqueue',state='in_progress',screenshots=str(OUT))
try:
 for _ in range(100):
  try:
   active=(profile/'DevToolsActivePort').read_text().splitlines()
   if len(active)>=2:break
  except OSError:pass
  time.sleep(.1)
 port=int(active[0]);page=next(x for x in requests.get(f'http://127.0.0.1:{port}/json',timeout=5).json() if x['type']=='page');ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=60)
 def cdp(method,params=None):
  global seq
  seq+=1;ws.send(json.dumps(dict(id=seq,method=method,params=params or {})))
  while True:
   r=json.loads(ws.recv())
   if r.get('id')==seq:
    assert 'error' not in r,r
    return r.get('result',{})
   events.append(r)
 def js(expr):
  r=cdp('Runtime.evaluate',dict(expression=expr,returnByValue=True,awaitPromise=True));assert 'exceptionDetails' not in r,r;return r['result'].get('value')
 def capture(sel,name):
  js(f'document.querySelector({json.dumps(sel)}).scrollIntoView({{block:"center",behavior:"instant"}})');js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');(OUT/name).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',dict(format='png'))['data']))
 cdp('Page.enable');cdp('Runtime.enable');cdp('Log.enable');cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/a_stackqueue.html'))
 for _ in range(120):
  if js('document.documentElement.dataset.sqLoaded') in ['true','error']:break
  time.sleep(.1)
 assert js('document.documentElement.dataset.sqLoaded')=='true'
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)');time.sleep(.2)
 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,rules:document.querySelectorAll(".review-rule").length,models:StackQueueChapter.players.length-1,math:document.querySelectorAll("math").length})');assert report['counts']['questions']==84 and report['counts']['rules']==80 and report['counts']['models']==67
 report['fonts']=js('({math:getComputedStyle(document.querySelector("math")).fontFamily,prose:getComputedStyle(document.querySelector(".lesson p")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),heading:document.fonts.check("18px Newsreader"),source:document.fonts.check("18px \'Source Sans 3\'"),code:document.fonts.check("18px \'JetBrains Mono\'")})');assert all(report['fonts'][k] for k in ['stix','heading','source','code'])
 report['geometry']=js('''(()=>{let frames=0;const issues=[];for(const player of StackQueueChapter.players){if(player.model.id==='editable')continue;const el=document.querySelector('[data-sq-model="'+player.model.id+'"]');for(let i=0;i<player.model.frames.length;i++){player.draw(i);frames++;const svg=el.querySelector('svg'),vb=svg.viewBox.baseVal,boxes=new Map([...svg.querySelectorAll('rect[data-box]')].map(x=>[x.dataset.box,x.getBBox()]));for(const t of svg.querySelectorAll('text')){const a=t.getBBox(),b=boxes.get(t.dataset.labelFor);if(b){const pad=[a.x-b.x,b.x+b.width-a.x-a.width,a.y-b.y,b.y+b.height-a.y-a.height];if(Math.min(pad[0],pad[1])<7.5||Math.min(pad[2],pad[3])<5.5)issues.push({id:player.model.id,i,text:t.textContent,pad});}for(const [key,c] of boxes){if(key===t.dataset.labelFor)continue;const dx=Math.max(c.x-a.x-a.width,a.x-c.x-c.width,0),dy=Math.max(c.y-a.y-a.height,a.y-c.y-c.height,0);if(Math.hypot(dx,dy)<13.8)issues.push({id:player.model.id,i,text:t.textContent,box:key,gap:Math.hypot(dx,dy)});}if(a.x<-.5||a.y<-.5||a.x+a.width>vb.width+.5||a.y+a.height>vb.height+.5)issues.push({id:player.model.id,i,text:t.textContent,bounds:true});}for(const p of svg.querySelectorAll('[data-connection]')){const expected=JSON.parse(p.dataset.layoutArrow),a=p.getPointAtLength(0),b=p.getPointAtLength(p.getTotalLength());if(Math.hypot(a.x-expected[0][0],a.y-expected[0][1])>.5||Math.hypot(b.x-expected[1][0],b.y-expected[1][1])>.5)issues.push({id:player.model.id,i,connection:p.dataset.connection,detached:true});}}player.draw(0);}return {frames,issues:issues.slice(0,40),issueCount:issues.length};})()''')
 (R/'research/a_stackqueue-browser-audit.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');assert report['geometry']['issueCount']==0,report['geometry']
 fixtures=json.loads((R/'research/a_stackqueue-lab-fixtures.json').read_text(encoding='utf-8'));report['laboratoryFixtures']=len(fixtures)
 for q in fixtures:
  actual=js('StackQueueChapter.evaluate('+json.dumps(q['mode'])+','+json.dumps(q['params'])+').result')
  for key,value in q['expected'].items():assert actual[key]==value,(q,actual)
 # Real form submissions: each mode, exact rational division and failed-run state retention.
 report['formModes']=[]
 for mode,fields in [('ring',dict(capacity='1',ops='E:9,D,E:8')),('two',dict(ops='E:1,E:2,F,D,E:3,D,D')),('postfix',dict(tokens='7 3 /')),('permutation',dict(target='3,1,2')),('window',dict(values='5,5,4,5',window='3'))]:
  js('(()=>{const f=document.querySelector("#sq-form");f.mode.value='+json.dumps(mode)+';f.mode.dispatchEvent(new Event("change"));const fields='+json.dumps(fields)+';for(const [k,v] of Object.entries(fields))f.elements.namedItem(k).value=v;f.requestSubmit();})()');assert not js('document.querySelector("#sq-lab-error").textContent');report['formModes'].append(dict(mode=mode,result=js('JSON.parse(document.querySelector("#sq-output").dataset.result)')))
 old=js('document.querySelector("#sq-output").dataset.result');js('(()=>{const f=document.querySelector("#sq-form");f.mode.value="postfix";f.tokens.value="7 0 /";f.requestSubmit();})()');assert js('document.querySelector("#sq-lab-error").textContent') and js('document.querySelector("#sq-output").dataset.result')==old
 # Buttons, seek, keyboard and actual motion.
 js('(()=>{const el=document.querySelector("[data-sq-model=concept-7]");el.querySelector("[data-next]").click();})()');assert js('document.querySelector("[data-sq-model=concept-7]").dataset.checkpoint')=='1'
 js('(()=>{const el=document.querySelector("[data-sq-model=concept-7]");el.querySelector("[data-next]").click();})()');report['activeAnimations']=js('document.getAnimations().length');assert report['activeAnimations']>0
 js('(()=>{const el=document.querySelector("[data-sq-model=concept-7]");el.querySelector("[data-reset]").click();el.focus();el.dispatchEvent(new KeyboardEvent("keydown",{key:"End",bubbles:true}));})()');assert int(js('document.querySelector("[data-sq-model=concept-7]").dataset.checkpoint'))>1
 js('(()=>{const el=document.querySelector("[data-sq-model=concept-7]");el.querySelector("[data-play]").click();el.querySelector("[data-play]").click();})()');assert js('document.querySelector("[data-sq-model=concept-7] [data-play]").textContent')=='Play'
 for id,checkpoint,name in [('concept-4',0,'linked-deque.png'),('concept-5',3,'ring-wrap.png'),('concept-7',5,'two-stack-transfer.png'),('concept-12',10,'catalan-lattice.png'),('concept-19',8,'histogram.png'),('problem-SQ_33',5,'problem-restoration.png')]:
  js('StackQueueChapter.players.find(x=>x.model.id=='+json.dumps(id)+').draw('+str(checkpoint)+')');capture('[data-sq-model="'+id+'"]',name)
 capture('#review','end-notes.png');capture('#resizing','formula-and-code.png')
 cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=True));time.sleep(.1);report['mobile']=js('({width:innerWidth,scroll:document.documentElement.scrollWidth,offenders:[...document.querySelectorAll("body *")].filter(x=>{const r=x.getBoundingClientRect();return r.right>390&& !x.closest("svg")}).slice(0,25).map(x=>({tag:x.tagName,cls:x.className,text:x.textContent.slice(0,70),right:x.getBoundingClientRect().right,width:x.clientWidth,scroll:x.scrollWidth,overflow:getComputedStyle(x).overflowX}))})');print('MOBILE',report['mobile']);assert report['mobile']['scroll']<=392,report['mobile'];capture('[data-sq-model=concept-5]','mobile-ring.png')
 cdp('Emulation.setEmulatedMedia',dict(features=[dict(name='prefers-reduced-motion',value='reduce')]));js('document.getAnimations().forEach(x=>x.cancel());StackQueueChapter.players[0].draw(1,true)');assert js('document.getAnimations().length')==0
 js('window.dispatchEvent(new Event("beforeprint"))');report['printFigures']=js('document.querySelectorAll(".sq-print-trace figure").length');assert report['printFigures']>=678;js('window.dispatchEvent(new Event("afterprint"))');assert js('document.querySelectorAll(".sq-print-trace figure").length')==0
 report['errors']=[x for x in events if x.get('method')=='Runtime.exceptionThrown'];assert not report['errors'];report['state']='passed';(R/'research/a_stackqueue-browser-audit.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps(report))
finally:
 proc.terminate();server.shutdown()
