"""Check the new report and its visible link in the existing chapter screen."""
import base64,json,os,subprocess,tempfile,threading,time
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import requests,websocket
ROOT=Path(__file__).resolve().parents[1]
OUT=Path(tempfile.gettempdir())/'chapter-library-review'
class QuietHandler(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(QuietHandler,directory=str(ROOT/'dist')))
threading.Thread(target=server.serve_forever,daemon=True).start()
profile=OUT/f'edge-report-{os.getpid()}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
try:
 active=profile/'DevToolsActivePort'
 for _ in range(100):
  if active.exists():break
  time.sleep(.1)
 port=int(active.read_text().splitlines()[0])
 page=next(x for x in requests.get(f'http://127.0.0.1:{port}/json',timeout=5).json() if x['type']=='page')
 ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=20);seq=0
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
 cdp('Page.enable');result=[]
 for path,width in [('library-review.html',1280),('library-review.html',390),('index.html#library',390)]:
  cdp('Emulation.setDeviceMetricsOverride',{'width':width,'height':900,'deviceScaleFactor':1,'mobile':width==390})
  cdp('Page.navigate',{'url':f'http://127.0.0.1:{server.server_port}/{path}'});time.sleep(.6)
  cdp('Runtime.evaluate',{'expression':'document.fonts.ready','awaitPromise':True,'returnByValue':True})
  row=json.loads(js('''JSON.stringify({title:document.title,documentWidth:document.documentElement.scrollWidth,viewport:innerWidth,reviewLink:[...document.querySelectorAll('a')].some(a=>a.getAttribute('href')==='library-review.html'&&a.getBoundingClientRect().height>0),chapterRows:document.querySelectorAll('tbody tr').length,underlinedLinks:[...document.querySelectorAll('a')].filter(a=>getComputedStyle(a).textDecorationLine.includes('underline')).length})'''))
  assert row['documentWidth']<=width and row['underlinedLinks']==0,row
  if path.startswith('index'):assert row['reviewLink'],row
  else:assert row['chapterRows']==22,row
  shot=cdp('Page.captureScreenshot',{'format':'png'})['data']
  (OUT/f"{'report' if not path.startswith('index') else 'library'}-{width}.png").write_bytes(base64.b64decode(shot))
  result.append({'path':path,'width':width,**row})
 (OUT/'report-review.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps(result))
 ws.close()
finally:
 proc.terminate();proc.wait(timeout=20);server.shutdown()
