"""Inspect current Gaussian models, exact laboratory, controls, fonts and print."""
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import base64,json,random,subprocess,tempfile,threading,time,uuid
import requests,websocket,sympy as S

R=Path(__file__).resolve().parents[1];E=R/'research/deep-library-revision/l_gauss-current-evidence';E.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R/'dist')))
threading.Thread(target=server.serve_forever,daemon=True).start()
profile=Path(tempfile.gettempdir())/('gauss-current-qa-'+uuid.uuid4().hex)
proc=subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','--headless=new','--no-first-run','--remote-allow-origins=*','--remote-debugging-port=0',f'--user-data-dir={profile}','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
seq=0;report={}
try:
    for _ in range(150):
        try:port=int((profile/'DevToolsActivePort').read_text().splitlines()[0]);break
        except (OSError,ValueError,IndexError):time.sleep(.1)
    pg=next(p for p in requests.get(f'http://127.0.0.1:{port}/json').json()if p['type']=='page')
    ws=websocket.create_connection(pg['webSocketDebuggerUrl'],timeout=60)
    def cdp(method,params=None):
        global seq
        seq+=1;ws.send(json.dumps({'id':seq,'method':method,'params':params or{}}))
        while True:
            result=json.loads(ws.recv())
            if result.get('id')==seq:
                assert 'error'not in result,result
                return result.get('result',{})
    def js(code):
        result=cdp('Runtime.evaluate',{'expression':code,'returnByValue':True,'awaitPromise':True})
        assert 'exceptionDetails'not in result,result
        return result.get('result',{}).get('value')
    def capture(selector,name):
        js('document.querySelector('+json.dumps(selector)+').scrollIntoView({block:"center",behavior:"instant"})')
        js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
        (E/name).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
    cdp('Page.enable')
    cdp('Page.addScriptToEvaluateOnNewDocument',{'source':"window.__errors=[];addEventListener('error',e=>__errors.push(e.message));addEventListener('unhandledrejection',e=>__errors.push(String(e.reason)));"})
    cdp('Emulation.setDeviceMetricsOverride',{'width':1360,'height':1000,'deviceScaleFactor':1,'mobile':False})
    url=f'http://127.0.0.1:{server.server_port}/chapters/l_gauss.html';cdp('Page.navigate',{'url':url})
    for _ in range(150):
        if js('location.href==='+json.dumps(url)+'&&document.readyState==="complete"&&!!window.ProblemVisuals&&!!window.ConceptAnimations'):break
        time.sleep(.1)
    js('document.fonts.ready')
    js('document.querySelectorAll("details.exam-solution").forEach(d=>d.open=true)')
    js('Promise.all([...document.querySelectorAll("[data-problem-visual]")].map(h=>ProblemVisuals.ready(h)))')
    js('Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))')
    assert js('document.querySelectorAll("details.exam-solution").length')==71
    assert js('ProblemVisuals.players.length')==33
    report['problemFrames']=js('''(()=>{const out=[];for(const p of ProblemVisuals.players){for(let k=0;k<p.model.frames.length;k++){p.show(k);out.push({id:p.host.dataset.problemVisual,k,issues:[...p.host.querySelectorAll('.problem-stage svg')].flatMap(s=>DiagramLayout.audit(s))});}p.show(0);}return out;})()''')
    assert all(not f['issues']for f in report['problemFrames']),[f for f in report['problemFrames']if f['issues']][:8]
    report['conceptFrames']=js('''(()=>{const out=[];for(const p of ConceptAnimations.players){for(const scene of p.scenes){p.scene=scene;p.show(0);for(let k=0;k<scene.frames.length;k++){p.api.show(k);out.push({id:scene.id,k,issues:DiagramLayout.audit(p.host.querySelector('svg'))});}}p.show(0);}return out;})()''')
    assert all(not f['issues']for f in report['conceptFrames'])
    report['controls']=js('''(()=>{const out=[];for(const p of ProblemVisuals.players){if(p.model.frames.length<2)continue;const reset=p.host.querySelector('[data-reset]'),next=p.host.querySelector('[data-next]'),prev=p.host.querySelector('[data-prev]'),seek=p.host.querySelector('[data-seek]');reset.click();const a=p.index;next.click();const b=p.index;prev.click();const c=p.index;seek.value=p.model.frames.length-1;seek.dispatchEvent(new Event('input'));const z=p.index;reset.click();out.push({id:p.host.dataset.problemVisual,ok:a===0&&b===1&&c===0&&z===p.model.frames.length-1&&p.index===0});}return out;})()''')
    assert all(x['ok']for x in report['controls'])
    report['playback']=js('''(async()=>{const out=[];for(const p of [ConceptAnimations.players.find(p=>p.scene.id==='gauss-swap')||ConceptAnimations.players[0],...ProblemVisuals.players.filter(p=>p.model.frames.length>1).slice(0,3)]){const h=p.host;h.scrollIntoView({block:'center',behavior:'instant'});await new Promise(r=>setTimeout(r,300));if(p.api){p.buttons.reset.click();p.buttons.play.click();}else{h.querySelector('[data-reset]').click();h.querySelector('[data-play]').click();}await new Promise(r=>setTimeout(r,2400));const moved=(p.api?p.api.index:p.index)>0;out.push({id:h.dataset.problemVisual||p.scene.id,moved});p.pause();}return out;})()''')
    assert all(x['moved']for x in report['playback']),report['playback']
    def mat(a):return S.Matrix([[S.Rational(x)for x in row]for row in a])
    report['labCases']=[];trace_checks=0
    rng=random.Random(1406)
    cases=[('unique',None),('free',None),('affine',None),('inconsistent',None),('fractions',None),('zero',None)]
    cases += [('grid-'+str(k),[[rng.randint(-3,3)for _ in range(1+k%4+1)]for _ in range(1+(k//4)%4)])for k in range(48)]
    for label,values in cases:
        if values is None:js('document.querySelector("[data-gauss-preset='+label+']").click()')
        else:js('document.getElementById("gauss-form").elements.matrix.value='+json.dumps('\n'.join(' '.join(map(str,row))for row in values))+';document.getElementById("gauss-form").dispatchEvent(new Event("input"))')
        data=js('({...document.getElementById("gauss-output").dataset})');assert data['valid']=='true',data
        original=mat(json.loads(data['input']));A=original[:,:-1];b=original[:,-1];rank=A.rank()
        expected='inconsistent'if original.rank()>rank else'unique'if rank==A.cols else'affine'
        assert data['state']==expected,(label,data)
        if expected!='inconsistent':
            xp=S.Matrix([S.Rational(x)for x in data['particular'].split(',')]);basis=[S.Matrix([S.Rational(x)for x in v])for v in json.loads(data['basis'])]
            assert A*xp==b and all(A*v==S.zeros(A.rows,1)for v in basis)
            assert len(basis)==A.cols-rank and (not basis or S.Matrix.hstack(*basis).rank()==len(basis))
        for f in json.loads(data['trace']):
            T=mat(f['transform']);assert T.det()!=0 and T*original==mat(f['matrix']);trace_checks+=1
        js('document.querySelector("[data-gauss-step=next]").click()');assert js('document.getElementById("gauss-output").dataset.step')=='1'
        js('document.querySelector("[data-gauss-step=back]").click()');assert js('document.getElementById("gauss-output").dataset.step')=='0'
        js('document.querySelector("[data-gauss-step=next]").click();document.querySelector("[data-gauss-step=reset]").click()');assert js('document.getElementById("gauss-output").dataset.step')=='0'
        report['labCases'].append({'id':label,'state':expected})
    report['independentTraceChecks']=trace_checks
    bad=['1 2\n1 2 3','1/0 2','abc 2','0.5 1','100001 2','1 2 3 4 5 6','1 2\n1 2\n1 2\n1 2\n1 2','']
    for value in bad:
        js('document.getElementById("gauss-form").elements.matrix.value='+json.dumps(value)+';document.getElementById("gauss-form").dispatchEvent(new Event("input"))')
        assert js('document.getElementById("gauss-output").dataset.valid')=='false'
    report['invalidInputsRejected']=len(bad);js('document.querySelector("[data-gauss-preset=unique]").click()')
    report['fonts']=js('({math:getComputedStyle(document.querySelector("math")).fontFamily,prose:getComputedStyle(document.querySelector(".lesson p")).fontFamily,code:getComputedStyle(document.querySelector("pre code")).fontFamily,loaded:[...document.fonts].filter(f=>f.status==="loaded").map(f=>f.family)})')
    assert 'STIX Two Math'in report['fonts']['math'] and 'JetBrains Mono'in report['fonts']['code']
    assert js('[...document.querySelectorAll("a")].every(a=>getComputedStyle(a).textDecorationLine==="none")')
    report['widths']=[]
    for width in[390,768,1360]:
        cdp('Emulation.setDeviceMetricsOverride',{'width':width,'height':1000,'deviceScaleFactor':1,'mobile':False})
        js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');value=js('({width:innerWidth,scroll:document.documentElement.scrollWidth})');report['widths'].append(value)
        if value['scroll']>width:
            report['overflow']=js('''[...document.querySelectorAll('p,math,svg,pre,section,div')].map(e=>({tag:e.localName,cls:e.getAttribute('class'),text:e.textContent.slice(0,90),right:e.getBoundingClientRect().right,width:e.getBoundingClientRect().width})).filter(x=>x.right>innerWidth+2).sort((a,b)=>b.right-a.right).slice(0,20)''');capture('body','overflow-diagnostic.png')
        assert value['scroll']<=width
    capture('[data-source-id="LG13"]','parameter-answer.png');capture('[data-source-id="MS_CS_1405_Q113"] .problem-visual','integer-choice-model.png');capture('.gauss-column-erratum','column-space-comparison.png')
    js('document.querySelectorAll("details.exam-solution").forEach(d=>d.open=false);dispatchEvent(new Event("beforeprint"))')
    cdp('Emulation.setEmulatedMedia',{'media':'print'})
    report['print']=js('({solutions:document.querySelectorAll("details.exam-solution[open]").length,problemFrames:document.querySelectorAll("[data-problem-visual] .teaching-print figure").length,modelFrames:ProblemVisuals.players.reduce((n,p)=>n+p.model.frames.length,0)})')
    assert report['print']['solutions']==71 and report['print']['problemFrames']==report['print']['modelFrames']
    cdp('Emulation.setEmulatedMedia',{'media':'screen'});js('dispatchEvent(new Event("afterprint"))')
    assert js('document.querySelectorAll("details.exam-solution[open]").length')==0
    report['errors']=js('__errors');assert not report['errors'],report['errors']
    report['status']='passed_gauss_current_revision_browser_checks'
    report['limits']='Portable Edge, finite exact input grid and current serialized states. Print DOM/CSS checked; no cross-browser or full PDF pagination claim.'
finally:
    server.shutdown();server.server_close()
    try:cdp('Browser.close')
    except Exception:pass
    proc.terminate()
    try:proc.wait(timeout=10)
    except subprocess.TimeoutExpired:proc.kill()
    (E/'browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print({k:(len(v)if isinstance(v,list)else v)for k,v in report.items()if k not in ['limits']})
