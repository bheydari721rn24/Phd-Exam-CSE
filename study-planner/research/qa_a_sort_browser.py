"""Real rendering, geometry, controls and independent laboratory fixtures."""
import base64,json,os,subprocess,tempfile,threading,time
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import requests,websocket
R=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'a-sort-visual-qa';OUT.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=OUT/f'edge-{os.getpid()}-{time.time_ns()}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;events=[];report=dict(topicId='a_sort',state='in_progress',screenshots=str(OUT))
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
 cdp('Page.enable');cdp('Runtime.enable');cdp('Log.enable');cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/a_sort.html'))
 for _ in range(120):
  if js('document.documentElement.dataset.sortLoaded') in ['true','error']:break
  time.sleep(.1)
 assert js('document.documentElement.dataset.sortLoaded')=='true'
 js('document.fonts.ready');js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true)');time.sleep(.2)
 report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,rules:document.querySelectorAll(".review-rule").length,players:SortingChapter.players.length,math:document.querySelectorAll("math").length})');assert report['counts']['questions']==88 and report['counts']['rules']==80
 report['fonts']=js('({math:getComputedStyle(document.querySelector("math")).fontFamily,prose:getComputedStyle(document.querySelector(".lesson p")).fontFamily,stix:document.fonts.check("18px \'STIX Two Math\'"),heading:document.fonts.check("18px Newsreader"),source:document.fonts.check("18px \'Source Sans 3\'"),code:document.fonts.check("18px \'JetBrains Mono\'")})');assert all(report['fonts'][k] for k in ['stix','heading','source','code'])
 report['geometry']=js('''(()=>{let frames=0;const issues=[];for(const player of SortingChapter.players){if(player.model.id==='editable')continue;const el=document.querySelector('[data-sort-model="'+player.model.id+'"]');for(let i=0;i<player.model.frames.length;i++){player.draw(i);frames++;const svg=el.querySelector('svg'),vb=svg.viewBox.baseVal;for(const t of svg.querySelectorAll('text')){const a=t.getBBox(),box=t.hasAttribute('data-contained')?t.parentElement.querySelector('[data-box]'):null;if(box){const b=box.getBBox(),pad=[a.x-b.x,b.x+b.width-a.x-a.width,a.y-b.y,b.y+b.height-a.y-a.height];if(Math.min(pad[0],pad[1])<7.5||Math.min(pad[2],pad[3])<5.5)issues.push({id:player.model.id,i,text:t.textContent,pad});}if(a.x<-.5||a.y<-.5||a.x+a.width>vb.width+.5||a.y+a.height>vb.height+.5)issues.push({id:player.model.id,i,text:t.textContent,bounds:true});}for(const p of svg.querySelectorAll('[data-edge]')){const a=p.getPointAtLength(0),b=p.getPointAtLength(p.getTotalLength());if([a,b].some(q=>q.x<0||q.x>vb.width||q.y<0||q.y>vb.height))issues.push({id:player.model.id,i,edgeOutside:true});}}player.draw(0);}return {frames,issueCount:issues.length,issues:issues.slice(0,40)};})()''')
 (R/'research/a_sort-browser-audit.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');assert report['geometry']['issueCount']==0,report['geometry']
 fixtures=json.loads((R/'research/a_sort-lab-fixtures.json').read_text(encoding='utf-8'));report['laboratoryFixtures']=len(fixtures)
 for f in fixtures:
  actual=js('SortingChapter.evaluate('+json.dumps(f['kind'])+','+json.dumps(f['params'])+').result');assert actual==f['expected'],(f,actual)
 report['forms']=[]
 for mode in ['selection','insertion','bubble','merge','quick','three','heap','counting','radix','bucket']:
  js('(()=>{const f=document.querySelector("#sort-form");f.kind.value='+json.dumps(mode)+';f.values.value="4,1,3,1,2";f.base.value="5";f.requestSubmit();})()');assert not js('document.querySelector("#sort-lab-error").textContent');report['forms'].append(mode)
 old=js('document.querySelector("#sort-output").dataset.result');js('(()=>{const f=document.querySelector("#sort-form");f.values.value="100,-1";f.requestSubmit();})()');assert js('document.querySelector("#sort-lab-error").textContent') and js('document.querySelector("#sort-output").dataset.result')==old
 js('(()=>{const el=document.querySelector("[data-sort-model=concept-3]");el.querySelector("[data-next]").click();el.querySelector("[data-next]").click();el.querySelector("[data-next]").click();el.querySelector("[data-next]").click();})()');report['motionAnimations']=js('document.getAnimations().length');assert report['motionAnimations']>0
 js('(()=>{const el=document.querySelector("[data-sort-model=concept-3]");el.querySelector("[data-reset]").click();el.focus();el.dispatchEvent(new KeyboardEvent("keydown",{key:"End",bubbles:true}));})()');assert int(js('document.querySelector("[data-sort-model=concept-3]").dataset.checkpoint'))>1
 js('(()=>{const el=document.querySelector("[data-sort-model=concept-3]");el.querySelector("[data-play]").click();el.querySelector("[data-play]").click();})()');assert js('document.querySelector("[data-sort-model=concept-3] [data-play]").textContent')=='Play'
 for id,k,name in [('concept-3',5,'insertion.png'),('concept-6',10,'merge.png'),('concept-9',3,'hoare.png'),('concept-12',6,'three-way.png'),('concept-13',5,'heap.png'),('concept-14',9,'counting.png'),('concept-15',5,'radix.png'),('concept-17',3,'decision-tree.png'),('problem-25',4,'problem-merge.png')]:
  js('SortingChapter.players.find(x=>x.model.id=='+json.dumps(id)+').draw('+str(k)+')');capture('[data-sort-model="'+id+'"]',name)
 capture('#review','end-notes.png');capture('#random-quick','formula.png')
 cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=True));time.sleep(.1);report['mobile']=js('({width:innerWidth,scroll:document.documentElement.scrollWidth})');assert report['mobile']['scroll']<=392,report['mobile'];capture('[data-sort-model=concept-13]','mobile-heap.png')
 cdp('Emulation.setEmulatedMedia',dict(features=[dict(name='prefers-reduced-motion',value='reduce')]));js('document.getAnimations().forEach(x=>x.cancel());SortingChapter.players[0].draw(1,true)');assert js('document.getAnimations().length')==0
 js('window.dispatchEvent(new Event("beforeprint"))');report['printFigures']=js('document.querySelectorAll(".sort-print-trace figure").length');assert report['printFigures']>=887;js('window.dispatchEvent(new Event("afterprint"))');assert js('document.querySelectorAll(".sort-print-trace figure").length')==0
 report['errors']=[x for x in events if x.get('method')=='Runtime.exceptionThrown'];assert not report['errors'];report['state']='passed';(R/'research/a_sort-browser-audit.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps(report))
finally:
 proc.terminate();server.shutdown()
