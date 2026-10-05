"""Real Chromium rendering and interaction audit, limited to the new chapter."""
import base64,json,os,subprocess,tempfile,threading,time
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import requests,websocket
ROOT=Path(__file__).resolve().parents[1];OUT=Path(tempfile.gettempdir())/'d-inclusion-qa';OUT.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT/'dist')));threading.Thread(target=server.serve_forever,daemon=True).start()
profile=OUT/f'edge-{os.getpid()}-{time.time_ns()}'
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--disable-gpu','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
events=[];seq=0
try:
    for _ in range(100):
        try:
            active=(profile/'DevToolsActivePort').read_text().splitlines()
            if len(active)>=2:break
        except (OSError,ValueError):pass
        time.sleep(.1)
    port=int(active[0]);page=next(x for x in requests.get(f'http://127.0.0.1:{port}/json',timeout=5).json() if x['type']=='page')
    ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=30)
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
        r=cdp('Runtime.evaluate',dict(expression=expr,returnByValue=True,awaitPromise=True))
        assert 'exceptionDetails' not in r,r
        return r['result'].get('value')
    def capture(sel,name):
        b=js(f'''(()=>{{const e=document.querySelector({json.dumps(sel)});e.scrollIntoView({{block:'start'}});const b=e.getBoundingClientRect();return {{x:b.x+scrollX,y:b.y+scrollY,width:b.width,height:b.height}};}})()''')
        data=cdp('Page.captureScreenshot',dict(format='png',captureBeyondViewport=True,clip=dict(**b,scale=1)))['data'];(OUT/name).write_bytes(base64.b64decode(data))
    cdp('Page.enable');cdp('Runtime.enable');cdp('Log.enable')
    cdp('Emulation.setDeviceMetricsOverride',dict(width=1280,height=1000,deviceScaleFactor=1,mobile=False))
    cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/d_inclusion.html'))
    for _ in range(50):
        if js('document.documentElement.dataset.inclusionLoaded')=='true':break
        time.sleep(.1)
    js('document.fonts.ready');time.sleep(.15)
    report=dict(topicId='d_inclusion',state='passed',models=[],lab=[],screenshots=str(OUT))
    report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,rules:document.querySelectorAll(".review-rule").length,models:document.querySelectorAll(".inclusion-model").length,math:document.querySelectorAll("math").length})')
    assert report['counts']['questions']==82 and report['counts']['rules']==80 and report['counts']['models']==13
    report['fonts']=js('({body:getComputedStyle(document.querySelector(".lesson p")).fontFamily,heading:getComputedStyle(document.querySelector("h1")).fontFamily,math:getComputedStyle(document.querySelector("math")).fontFamily,code:getComputedStyle(document.querySelector("pre code")).fontFamily,stixLoaded:document.fonts.check("17px \'STIX Two Math\'"),sourceLoaded:document.fonts.check("17px \'Source Sans 3\'"),newsreaderLoaded:document.fonts.check("17px Newsreader"),monoLoaded:document.fonts.check("17px \'JetBrains Mono\'")})')
    assert all(report['fonts'][x] for x in ['stixLoaded','sourceLoaded','newsreaderLoaded','monoLoaded'])
    models=js('[...document.querySelectorAll(".inclusion-model")].map(x=>x.dataset.inclusionModel)')
    for id in models:
        row=js(f'''(()=>{{const h=document.querySelector('[data-inclusion-model="{id}"]'),s=h.querySelector('[data-seek]'),before=h.querySelector('.inclusion-stage').innerHTML;s.value=s.max;s.dispatchEvent(new Event('input'));const changed=before!==h.querySelector('.inclusion-stage').innerHTML;const last=h.querySelector('[data-progress]').textContent;h.querySelector('[data-prev]').click();const prev=h.querySelector('[data-progress]').textContent;h.querySelector('[data-reset]').click();const reset=h.querySelector('[data-progress]').textContent;h.querySelector('[data-next]').click();const next=h.querySelector('[data-progress]').textContent;return {{id:'{id}',changed,last,prev,reset,next,printed:h.querySelectorAll('.inclusion-print-trace figure').length}};}})()''')
        assert row['changed'] and row['reset'].startswith('Checkpoint 1 ') and row['next'].startswith('Checkpoint 2 '),row
        js(f'document.querySelector(\'[data-inclusion-model="{id}"] [data-reset]\').click()');time.sleep(.55)
        row['labelBounds']=js(f'''(()=>{{const svg=document.querySelector('[data-inclusion-model="{id}"] .inclusion-stage svg');return [...svg.querySelectorAll('text')].filter(e=>{{const b=e.getBBox();return b.x<-1||b.y<-1||b.x+b.width>761||b.y+b.height>401;}}).map(e=>e.textContent);}})()''')
        assert not row['labelBounds'],row
        row['allFrameTextChecks']=js(f'''(()=>{{const h=document.querySelector('[data-inclusion-model="{id}"]'),seek=h.querySelector('[data-seek]'),bad=[];for(let k=0;k<=Number(seek.max);k++){{seek.value=k;seek.dispatchEvent(new Event('input'));const ts=[...h.querySelectorAll('.inclusion-stage svg text')];for(let a=0;a<ts.length;a++)for(let b=a+1;b<ts.length;b++){{const x=ts[a].getBBox(),y=ts[b].getBBox();if(Math.min(x.x+x.width,y.x+y.width)-Math.max(x.x,y.x)>1&&Math.min(x.y+x.height,y.y+y.height)-Math.max(x.y,y.y)>1)bad.push({{checkpoint:k+1,a:ts[a].textContent,b:ts[b].textContent}});}}}}h.querySelector('[data-reset]').click();return {{frames:Number(seek.max)+1,overlaps:bad}};}})()''')
        assert not row['allFrameTextChecks']['overlaps'],row
        time.sleep(.55)
        capture(f'[data-inclusion-model="{id}"]',id+'.png');report['models'].append(row)
    js('document.querySelector("[data-play]").click()');time.sleep(1.6)
    report['play']=js('document.querySelector("[data-progress]").textContent');assert not report['play'].startswith('Checkpoint 1 ')
    js('document.querySelector("[data-play]").click()');at=js('document.querySelector("[data-progress]").textContent');time.sleep(.95);assert js('document.querySelector("[data-progress]").textContent')==at
    js('document.querySelector("[data-reset]").click()')
    for mode,n,m,cap,expected in [('sets',4,3,2,19),('maps',5,3,2,150),('maps',0,0,2,1),('maps',0,3,2,0),('permutations',5,3,2,64),('permutations',4,4,2,9),('caps',8,4,3,31),('caps',5,3,2,3)]:
        row=js(f"""(()=>{{const f=document.querySelector('#inclusion-form');f.elements.mode.value='{mode}';f.elements.n.value={n};f.elements.m.value={m};f.elements.cap.value={cap};f.elements.mode.dispatchEvent(new Event('change'));return {{mode:'{mode}',n:{n},m:{m},cap:{cap},count:Number(document.querySelector('#inclusion-output').dataset.count)}};}})()""")
        assert row['count']==expected,row;report['lab'].append(row);capture('#inclusion-lab','lab-'+mode+'.png')
    js('document.querySelector("#inclusion-form").elements.mode.value="permutations";document.querySelector("#inclusion-form").elements.n.value=2;document.querySelector("#inclusion-form").elements.m.value=3;document.querySelector("#inclusion-form").dispatchEvent(new Event("submit",{cancelable:true}))')
    report['labInvalidInput']=js('document.querySelector("#inclusion-output").textContent');assert 'cannot exceed' in report['labInvalidInput']
    report['invalidCalls']=js("""(()=>{const cases=[['maps',9,3,2,[]],['maps',3,5,2,[]],['caps',4,0,2,[]],['caps',4,3,6,[]],['permutations',2,3,2,[]],['sets',0,0,0,[1,2]],['sets',0,0,0,Array(8).fill(-1)]];return cases.map(c=>{try{InclusionLab.evaluate(...c);return false}catch(e){return true}})})()""");assert all(report['invalidCalls'])
    # Independent Python references were serialized before browser execution.
    import json as _json
    references=_json.loads((ROOT/'research/d_inclusion-lab-reference.json').read_text())
    report['labReferenceChecks']=js("""(()=>{const rows="""+_json.dumps(references)+""";return rows.map(r=>{const z=InclusionLab.evaluate(r.mode,r.n,r.m,r.cap,r.atoms);return {mode:r.mode,n:r.n,m:r.m,cap:r.cap,actual:z.count,expected:r.count};});})()""")
    assert all(x['actual']==x['expected'] for x in report['labReferenceChecks'])
    js('document.querySelector(\'[data-inclusion-model="di-cancel"] [data-seek]\').value=1;document.querySelector(\'[data-inclusion-model="di-cancel"] [data-seek]\').dispatchEvent(new Event("input"))');time.sleep(.5)
    js('document.querySelector(\'[data-inclusion-model="di-cancel"] [data-next]\').click()');report['realMotion']=js('document.querySelector(\'[data-inclusion-model="di-cancel"] .inclusion-stage\').getAnimations({subtree:true}).length');assert report['realMotion']>0
    # Fonts and scripts remain separate across long derivations.
    js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true);MathLayout.layout()');capture('#allocations','allocations-desktop.png')
    cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=False));time.sleep(.2);js('MathLayout.layout()')
    report['mobile']=js('({width:innerWidth,scroll:document.documentElement.scrollWidth,body:document.body.scrollWidth,badAnchors:[...document.querySelectorAll("a")].filter(x=>getComputedStyle(x).textDecorationLine.includes("underline")).length,mathOverflow:[...document.querySelectorAll("math")].filter(x=>{const b=x.getBoundingClientRect();return b.width>innerWidth&&!x.closest(".formula-block")&&!x.closest(".inclusion-print-trace");}).map(x=>x.getAttribute("aria-label"))})')
    if report['mobile']['scroll']>392: print(js('JSON.stringify([...document.body.querySelectorAll("*")].filter(x=>{const b=x.getBoundingClientRect();return b.right>392&&!x.closest(".inclusion-stage,.inclusion-print-trace,.inclusion-lab-diagram,.formula-block");}).map(x=>({tag:x.tagName,cls:x.className,text:x.textContent.slice(0,110),right:x.getBoundingClientRect().right,width:x.getBoundingClientRect().width})).slice(0,25))'))
    assert report['mobile']['scroll']<=392 and report['mobile']['body']<=392 and report['mobile']['badAnchors']==0,report['mobile']
    assert not report['mobile']['mathOverflow'],report['mobile']
    report['mobilePan']=js('(()=>{const e=document.querySelector(".inclusion-stage");e.scrollLeft=190;return {client:e.clientWidth,scroll:e.scrollWidth,moved:e.scrollLeft};})()');assert report['mobilePan']['moved']>0
    capture('.hero','mobile-hero.png');capture('[data-inclusion-model="di-rooks"]','mobile-gap.png');capture('#review','mobile-review.png')
    cdp('Emulation.setEmulatedMedia',dict(features=[dict(name='prefers-reduced-motion',value='reduce')]))
    report['reducedMotion']=js('matchMedia("(prefers-reduced-motion: reduce)").matches');assert report['reducedMotion']
    js('document.querySelector("[data-next]").click()');report['motionAnimations']=js('document.querySelector(".inclusion-stage").getAnimations({subtree:true}).length');assert report['motionAnimations']==0
    js('document.querySelectorAll(".exam-solution").forEach((x,i)=>x.open=i===0)')
    report['print']=js('(()=>{const a=[...document.querySelectorAll(".exam-solution")],before=a.map(x=>x.open);dispatchEvent(new Event("beforeprint"));const opened=a.every(x=>x.open);dispatchEvent(new Event("afterprint"));return {opened,restored:a.every((x,i)=>x.open===before[i]),checkpoints:document.querySelectorAll(".inclusion-print-trace figure").length};})()');assert report['print']['opened'] and report['print']['restored'] and report['print']['checkpoints']==56
    cdp('Emulation.setDeviceMetricsOverride',dict(width=1280,height=1000,deviceScaleFactor=1,mobile=False));cdp('Emulation.setEmulatedMedia',dict(media='print'));js('dispatchEvent(new Event("beforeprint"))');time.sleep(.1)
    report['printVisibility']=js('({controls:getComputedStyle(document.querySelector(".inclusion-controls")).display,checkpoints:getComputedStyle(document.querySelector(".inclusion-print-trace")).display})');assert report['printVisibility']['controls']=='none' and report['printVisibility']['checkpoints']=='block'
    capture('[data-inclusion-model="di-cancel"] .inclusion-print-trace figure','print-periodic.png')
    # The chapter must also be reachable from the real application library.
    cdp('Emulation.setEmulatedMedia',dict(media='screen'));cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/index.html'))
    for _ in range(50):
        if js('document.querySelector("#library")?.textContent.includes("Inclusion-Exclusion: Overlap, Exact Multiplicity, and Forbidden Configurations")'):break
        time.sleep(.1)
    js('document.querySelector("[data-view=lessons]").click()')
    report['applicationLibrary']=js('({chapterLink:!!document.querySelector("#library a[href=\\\"chapters/d_inclusion.html\\\"]"),draftLabel:document.querySelector("#library").textContent.includes("New chapter awaiting review"),approvedNotice:document.querySelector("#view-lessons>p").textContent.includes("student-approved")})')
    assert all(report['applicationLibrary'].values()),report['applicationLibrary']
    capture('#view-lessons','application-library.png')
    report['errors']=[r for r in events if r.get('method')=='Runtime.exceptionThrown' or (r.get('method')=='Log.entryAdded' and r.get('params',{}).get('entry',{}).get('level')=='error' and 'favicon.ico' not in r.get('params',{}).get('entry',{}).get('url',''))]
    assert not report['errors'],report['errors']
    (ROOT/'research/d_inclusion-browser-audit.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(state='passed',counts=report['counts'],mobile=report['mobile'],models=len(models),checkpoints=report['print']['checkpoints'],errors=len(report['errors']),screenshots=str(OUT))))
finally:
    try:cdp('Browser.close')
    except Exception:pass
    proc.terminate();server.shutdown()
