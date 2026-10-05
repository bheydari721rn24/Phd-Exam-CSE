"""Capture every rendered chapter figure and audit labels/mobile geometry."""
import base64,json,os,subprocess,tempfile,threading,time
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import requests,websocket
ROOT=Path(__file__).resolve().parents[1]
OUT=Path(tempfile.gettempdir())/'chapter-library-review';OUT.mkdir(exist_ok=True)
topics=[c['topicId'] for w in json.loads((ROOT/'dist/lessons.json').read_text()) for c in w['chapters']]
server=ThreadingHTTPServer(('127.0.0.1',0),partial(SimpleHTTPRequestHandler,directory=str(ROOT/'dist')))
threading.Thread(target=server.serve_forever,daemon=True).start()
profile=OUT/f'edge-{os.getpid()}-{time.time_ns()}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
results=[]
try:
 active=profile/'DevToolsActivePort'
 for _ in range(100):
  try:
   active_data=active.read_text().splitlines()
   if len(active_data)>=2:break
  except (OSError,ValueError):pass
  time.sleep(.1)
 port=int(active_data[0]);page=next(x for x in requests.get(f'http://127.0.0.1:{port}/json',timeout=5).json() if x['type']=='page')
 ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=30);seq=0
 def cdp(method,params=None):
  global seq
  seq+=1;ws.send(json.dumps({'id':seq,'method':method,'params':params or {}}))
  while True:
   r=json.loads(ws.recv())
   if r.get('id')==seq:
    assert 'error' not in r,r
    return r.get('result',{})
 def js(expr):
  r=cdp('Runtime.evaluate',{'expression':expr,'returnByValue':True})
  assert 'exceptionDetails' not in r,r
  return r['result'].get('value')
 cdp('Page.enable')
 for topic in topics:
  cdp('Emulation.setDeviceMetricsOverride',{'width':1280,'height':1000,'deviceScaleFactor':1,'mobile':False})
  cdp('Page.navigate',{'url':f'http://127.0.0.1:{server.server_port}/chapters/{topic}.html'});time.sleep(.5)
  cdp('Runtime.evaluate',{'expression':'document.fonts.ready','awaitPromise':True,'returnByValue':True})
  row={'topicId':topic,'figures':[]}
  row['solutionPrint']=json.loads(js('''JSON.stringify((()=>{const nodes=[...document.querySelectorAll('.exam-solution')],before=nodes.map(x=>x.open);dispatchEvent(new Event('beforeprint'));const allOpened=nodes.every(x=>x.open);dispatchEvent(new Event('afterprint'));const restored=nodes.every((x,i)=>x.open===before[i]);return {count:nodes.length,allOpened,restored};})())'''))
  assert row['solutionPrint']['allOpened'] and row['solutionPrint']['restored'],row['solutionPrint']
  js("document.querySelectorAll('.exam-solution').forEach(x=>x.open=true)")
  row['fonts']=json.loads(js('''JSON.stringify({loaded:[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family),math:[...new Set([...document.querySelectorAll('math,.math-inline,.formula-block,sub,sup')].map(x=>getComputedStyle(x).fontFamily))]})'''))
  if topic in ('d_logic','d_sets','l_vectors','a_recurrence','a_divide','p_types'):
   for label in ('Formula and conceptual problem bank','Applicable formulas and examination notes'):
    js("[...document.querySelectorAll('h2')].find(x=>x.textContent==="+json.dumps(label)+").scrollIntoView({block:'start'})")
    shot=cdp('Page.captureScreenshot',{'format':'png'})['data']
    (OUT/(topic+('-questions.png' if label.startswith('Formula') else '-notes.png'))).write_bytes(base64.b64decode(shot))
  figures=json.loads(js('''JSON.stringify([...document.querySelectorAll('figure svg')].map((s,i)=>{
   const v=s.viewBox.baseVal,ts=[...s.querySelectorAll('text')],boxes=ts.map(t=>{const b=t.getBBox();return {text:t.textContent,x:b.x,y:b.y,w:b.width,h:b.height,font:getComputedStyle(t).fontFamily};});
   const outside=boxes.filter(b=>b.x<v.x-1||b.y<v.y-1||b.x+b.w>v.x+v.width+1||b.y+b.h>v.y+v.height+1);
   const overlap=[];for(let a=0;a<boxes.length;a++)for(let b=a+1;b<boxes.length;b++){const p=boxes[a],q=boxes[b];if(Math.min(p.x+p.w,q.x+q.w)-Math.max(p.x,q.x)>2 && Math.min(p.y+p.h,q.y+q.h)-Math.max(p.y,q.y)>2)overlap.push([p.text,q.text]);}
   return {index:i,title:s.querySelector('title')?.textContent||s.getAttribute('aria-label')||s.parentElement.querySelector('figcaption')?.textContent,viewBox:[v.width,v.height],outside,overlap,labels:boxes};
  }))'''))
  for f in figures:
   i=f['index'];js(f"document.querySelectorAll('figure svg')[{i}].scrollIntoView({{block:'start'}})");time.sleep(.05)
   box=json.loads(js(f"JSON.stringify((()=>{{const b=document.querySelectorAll('figure svg')[{i}].getBoundingClientRect();return {{x:b.x+scrollX,y:b.y+scrollY,width:b.width,height:b.height,scale:1}}}})())"))
   if box['width']>0 and box['height']>0:
    shot=cdp('Page.captureScreenshot',{'format':'png','captureBeyondViewport':True,'clip':box})['data'];name=f'{topic}-figure-{i+1}.png';(OUT/name).write_bytes(base64.b64decode(shot));f['screenshot']=name
   row['figures'].append(f)
  cdp('Emulation.setDeviceMetricsOverride',{'width':390,'height':844,'deviceScaleFactor':1,'mobile':True})
  js('scrollTo(0,0)');time.sleep(.1)
  row['mobile']=json.loads(js('''JSON.stringify({viewport:innerWidth,document:document.documentElement.scrollWidth,formulaOverflow:[...document.querySelectorAll('.formula-block')].filter(x=>x.scrollWidth>x.clientWidth+1).map(x=>({extra:x.scrollWidth-x.clientWidth,text:x.textContent.slice(0,160)})),inlineMathOverflow:[...document.querySelectorAll('.math-inline')].filter(x=>x.scrollWidth>x.clientWidth+1).map(x=>x.textContent),figureSizes:[...document.querySelectorAll('figure svg')].map(x=>({width:x.clientWidth,fontSize:getComputedStyle(x.querySelector('text')||x).fontSize})),problems:[...document.querySelectorAll('h3')].filter(x=>x.textContent.startsWith('Question ')).length,codeFonts:[...new Set([...document.querySelectorAll('pre code')].map(x=>getComputedStyle(x).fontFamily))]})'''))
  if topic in ('d_sets','a_recurrence'):
   js("document.getElementById('exam-methods').scrollIntoView({block:'start'})")
   shot=cdp('Page.captureScreenshot',{'format':'png'})['data']
   (OUT/f'{topic}-exam-mobile.png').write_bytes(base64.b64decode(shot))
  if topic in ('d_logic','a_loop','l_matrices','g_gates'):
   target={'d_logic':'figure','a_loop':'pre','l_matrices':'.formula-block','g_gates':'figure'}[topic]
   js(f"document.querySelector({json.dumps(target)}).scrollIntoView({{block:'start'}})")
   shot=cdp('Page.captureScreenshot',{'format':'png'})['data']
   (OUT/f'{topic}-mobile.png').write_bytes(base64.b64decode(shot))
  cdp('Emulation.setDeviceMetricsOverride',{'width':794,'height':1123,'deviceScaleFactor':1,'mobile':False})
  cdp('Emulation.setEmulatedMedia',{'media':'print'})
  js('scrollTo(0,0)');time.sleep(.05)
  row['printStyle']=json.loads(js('''JSON.stringify({diagramOverflow:[...document.querySelectorAll('figure svg')].filter(s=>s.getBoundingClientRect().width>s.parentElement.getBoundingClientRect().width+1).length,mathFonts:[...new Set([...document.querySelectorAll('math,.formula-block')].map(x=>getComputedStyle(x).fontFamily))]})'''))
  if topic in ('d_induction','g_number','g_gates'):
   js("document.querySelector('figure').scrollIntoView({block:'start'})")
   shot=cdp('Page.captureScreenshot',{'format':'png'})['data']
   (OUT/f'{topic}-print-style.png').write_bytes(base64.b64decode(shot))
  cdp('Emulation.setEmulatedMedia',{'media':'screen'})
  # Deliberately indivisible matrices and quantified scopes may pan inside a labeled
  # equation region. They must never widen the page or clip mathematical tokens.
  row['mobile']['equationPan']=json.loads(js('''JSON.stringify([...document.querySelectorAll('.formula-block')].filter(e=>e.scrollWidth>e.clientWidth+2).map(e=>({bounded:getComputedStyle(e).overflowX==='auto',label:e.dataset.scrollable==='true',width:e.clientWidth,content:e.scrollWidth})))'''))
  assert row['mobile']['document']<=390,row['mobile']
  assert row['printStyle']['diagramOverflow']==0,row['printStyle']
  assert all(not f['outside'] and not f['overlap'] for f in figures),row
  results.append(row);print(topic, 'figures',len(figures),'label findings',sum(len(f['outside'])+len(f['overlap']) for f in figures),'mobile',row['mobile']['document'],'print diagrams fit',flush=True)
  (OUT/'browser-review.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
 ws.close()
finally:
 proc.terminate();proc.wait(timeout=20);server.shutdown()
print('All figure captures:',OUT)
