from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_d_pigeonhole_browser.py').read_text()
prefix=s[:s.index("    report=dict(")].replace('d-pigeonhole-qa','a-arrays-qa').replace('d_pigeonhole.html','a_arrays.html').replace('pigeonholeLoaded','arraysLoaded')
a=prefix.index('    def capture(');z=prefix.index("    cdp('Page.enable')",a)
prefix=prefix[:a]+'''    def capture(sel,name):
        js('document.documentElement.style.scrollBehavior="auto"')
        js(f'document.querySelector({json.dumps(sel)}).scrollIntoView({{block:"center",behavior:"instant"}})')
        js('new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)))')
        data=cdp('Page.captureScreenshot',dict(format='png',captureBeyondViewport=False))['data']
        (OUT/name).write_bytes(base64.b64decode(data))
'''+prefix[z:]
tail=r"""
    report=dict(topicId='a_arrays',state='passed',models=[],screenshots=str(OUT))
    report['counts']=js('({questions:document.querySelectorAll(".exam-question").length,rules:document.querySelectorAll(".review-rule").length,models:document.querySelectorAll(".arrays-model[data-arrays-model]:not([data-arrays-model=editable])").length,math:document.querySelectorAll("math").length})')
    assert report['counts']['questions']==86 and report['counts']['rules']==80 and report['counts']['models']==20,report['counts']
    report['fonts']=js('({math:getComputedStyle(document.querySelector("math")).fontFamily,code:getComputedStyle(document.querySelector("pre code")).fontFamily,stix:document.fonts.check("17px \'STIX Two Math\'"),source:document.fonts.check("17px \'Source Sans 3\'"),heading:document.fonts.check("17px Newsreader"),mono:document.fonts.check("17px \'JetBrains Mono\'")})')
    assert all(report['fonts'][k] for k in ['stix','source','heading','mono'])
    ids=js('[...document.querySelectorAll("[data-arrays-model]:not([data-arrays-model=editable])")].map(x=>x.dataset.arraysModel)')
    for id in ids:
        row=js(f'''(()=>{{const h=document.querySelector('[data-arrays-model="{id}"]'),seek=h.querySelector('[data-seek]'),bad=[],initial=h.querySelector('.arrays-stage').innerHTML;for(let k=0;k<=Number(seek.max);k++){{seek.value=k;seek.dispatchEvent(new Event('input'));const ts=[...h.querySelectorAll('.arrays-stage svg text')];for(let a=0;a<ts.length;a++){{const x=ts[a].getBBox();if(x.x<-1||x.y<-1||x.x+x.width>761||x.y+x.height>411)bad.push({{checkpoint:k+1,bounds:ts[a].textContent}});for(let b=a+1;b<ts.length;b++){{const y=ts[b].getBBox();if(Math.min(x.x+x.width,y.x+y.width)-Math.max(x.x,y.x)>1&&Math.min(x.y+x.height,y.y+y.height)-Math.max(x.y,y.y)>1)bad.push({{checkpoint:k+1,overlap:[ts[a].textContent,ts[b].textContent]}});}}}}}}const changed=initial!==h.querySelector('.arrays-stage').innerHTML;h.querySelector('[data-prev]').click();const prev=h.querySelector('[data-progress]').textContent;h.querySelector('[data-reset]').click();const reset=h.querySelector('[data-progress]').textContent;h.querySelector('[data-next]').click();const next=h.querySelector('[data-progress]').textContent;return {{id:'{id}',frames:Number(seek.max)+1,bad,changed,prev,reset,next,printed:h.querySelectorAll('.arrays-print-trace figure').length}};}})()''')
        assert not row['bad'] and row['changed'] and row['reset'].startswith('Checkpoint 1 ') and row['next'].startswith('Checkpoint 2 '),row
        js(f'document.querySelector(\'[data-arrays-model="{id}"] [data-reset]\').click()');time.sleep(.5)
        if id in ['insert','resize','dll','splice','reverse','floyd','orthogonal']:capture(f'[data-arrays-model="{id}"]',id+'-start-v1.png')
        js(f'''(()=>{{const s=document.querySelector('[data-arrays-model="{id}"] [data-seek]');s.value=s.max;s.dispatchEvent(new Event('input'));}})()''');time.sleep(.5)
        if id in ['insert','resize','dll','splice','reverse','floyd','orthogonal']:capture(f'[data-arrays-model="{id}"]',id+'-final-v1.png')
        report['models'].append(row)
    refs=json.loads((ROOT/'research/a_arrays-lab-reference.json').read_text())
    report['labReferenceChecks']=js('(()=>{const rows='+json.dumps(refs)+';return rows.map(r=>{const z=ArrayLab.evaluate(r.mode,r.params);return {mode:r.mode,ok:Object.entries(r.expected).every(([k,v])=>JSON.stringify(z[k])===JSON.stringify(v))};});})()')
    assert len(report['labReferenceChecks'])==466 and all(z['ok'] for z in report['labReferenceChecks'])
    report['labForms']=[]
    for mode in ['growth','shift','reverse','floyd']:
        row=js(f'''(()=>{{const f=document.querySelector('#arrays-form');f.mode.value='{mode}';f.mode.dispatchEvent(new Event('change'));f.dispatchEvent(new Event('submit',{{cancelable:true}}));return {{mode:'{mode}',valid:!document.querySelector('#arrays-lab-error').textContent,state:JSON.parse(document.querySelector('#arrays-output').dataset.result),frames:document.querySelector('#arrays-output [data-seek]').max}};}})()''')
        assert row['valid'] and int(row['frames'])>0,row
        report['labForms'].append(dict(mode=mode,frames=row['frames']));capture('#arrays-lab','lab-'+mode+'-v1.png')
    report['invalidInputs']=js('(()=>{const cs=[["growth",{m:0,c0:1,g:2}],["growth",{m:2,c0:1,g:1}],["shift",{values:[1,2],index:3,value:1}],["reverse",{n:8}],["floyd",{mu:1,lam:0}]];return cs.map(c=>{try{ArrayLab.evaluate(...c);return false}catch(e){return true}});})()');assert all(report['invalidInputs'])
    report['invalidForm']=js('(()=>{const f=document.querySelector("#arrays-form");f.mode.value="shift";f.mode.dispatchEvent(new Event("change"));const old=document.querySelector("#arrays-output").dataset.result;f.values.value="1,,3";f.dispatchEvent(new Event("submit",{cancelable:true}));return {error:!!document.querySelector("#arrays-lab-error").textContent,retained:document.querySelector("#arrays-output").dataset.result===old};})()');assert all(report['invalidForm'].values())
    js('document.querySelector(\'[data-arrays-model="address"] [data-reset]\').click();document.querySelector(\'[data-arrays-model="address"] [data-play]\').click()');time.sleep(1.6)
    assert not js('document.querySelector(\'[data-arrays-model="address"] [data-progress]\').textContent').startswith('Checkpoint 1 ')
    js('document.querySelector(\'[data-arrays-model="address"] [data-play]\').click()');paused=js('document.querySelector(\'[data-arrays-model="address"] [data-progress]\').textContent');time.sleep(.95)
    assert js('document.querySelector(\'[data-arrays-model="address"] [data-progress]\').textContent')==paused
    js('document.querySelector(\'[data-arrays-model="address"] [data-reset]\').click()');time.sleep(.5);js('document.querySelector(\'[data-arrays-model="address"] [data-next]\').click()')
    report['realMotion']=js('document.querySelector(\'[data-arrays-model="address"] .arrays-stage\').getAnimations({subtree:true}).length');assert report['realMotion']>0
    js('document.querySelectorAll(".exam-solution").forEach(x=>x.open=true);MathLayout.layout()');capture('#amortization','potential-desktop-v1.png')
    cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=False));time.sleep(.2);js('MathLayout.layout()')
    report['mobile']=js('({width:innerWidth,scroll:document.documentElement.scrollWidth,body:document.body.scrollWidth,underlines:[...document.querySelectorAll("a")].filter(e=>getComputedStyle(e).textDecorationLine.includes("underline")).length,mathOverflow:[...document.querySelectorAll("math")].filter(x=>x.getBoundingClientRect().width>innerWidth&&!x.closest(".formula-block,.arrays-print-trace")).map(x=>x.getAttribute("aria-label"))})')
    assert report['mobile']['scroll']<=392 and report['mobile']['body']<=392 and report['mobile']['underlines']==0 and not report['mobile']['mathOverflow'],report['mobile']
    report['mobilePan']=js('(()=>{const e=document.querySelector(".arrays-stage");e.scrollLeft=190;return e.scrollLeft;})()');assert report['mobilePan']>0
    capture('.hero','mobile-header-v1.png');capture('[data-arrays-model="splice"]','mobile-splice-v1.png');capture('#review','mobile-rules-v1.png')
    cdp('Emulation.setEmulatedMedia',dict(features=[dict(name='prefers-reduced-motion',value='reduce')]))
    js('document.querySelector(\'[data-arrays-model="address"] [data-next]\').click()');report['reducedMotionAnimations']=js('document.querySelector(\'[data-arrays-model="address"] .arrays-stage\').getAnimations({subtree:true}).length');assert report['reducedMotionAnimations']==0
    js('document.querySelectorAll(".exam-solution").forEach((x,i)=>x.open=i===0)')
    report['print']=js('(()=>{const a=[...document.querySelectorAll(".exam-solution")],before=a.map(x=>x.open);dispatchEvent(new Event("beforeprint"));const opened=a.every(x=>x.open);dispatchEvent(new Event("afterprint"));return {opened,restored:a.every((x,i)=>x.open===before[i]),checkpoints:document.querySelectorAll("[data-arrays-model]:not([data-arrays-model=editable]) .arrays-print-trace figure").length};})()');assert report['print']['opened'] and report['print']['restored'] and report['print']['checkpoints']==113
    cdp('Emulation.setDeviceMetricsOverride',dict(width=1280,height=1000,deviceScaleFactor=1,mobile=False));cdp('Emulation.setEmulatedMedia',dict(media='print'));js('dispatchEvent(new Event("beforeprint"))')
    report['printVisibility']=js('({controls:getComputedStyle(document.querySelector(".arrays-controls")).display,trace:getComputedStyle(document.querySelector(".arrays-print-trace")).display})');assert report['printVisibility']==dict(controls='none',trace='block')
    capture('[data-arrays-model="reverse"] .arrays-print-trace figure','print-reversal-v1.png')
    cdp('Emulation.setEmulatedMedia',dict(media='screen'));cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/index.html'))
    for _ in range(50):
        if js('document.querySelector("#library")?.textContent.includes("Arrays, Linked Lists, and Operation Costs")'):break
        time.sleep(.1)
    js('document.querySelector("[data-view=lessons]").click()')
    report['applicationLibrary']=js('({chapter:!!document.querySelector("#library a[href=\\\"chapters/a_arrays.html\\\"]"),draft:document.querySelector("#library").textContent.includes("New chapter awaiting review")})');assert all(report['applicationLibrary'].values())
    report['errors']=[r for r in events if r.get('method')=='Runtime.exceptionThrown' or (r.get('method')=='Log.entryAdded' and r.get('params',{}).get('entry',{}).get('level')=='error' and 'favicon.ico' not in r.get('params',{}).get('entry',{}).get('url',''))]
    assert not report['errors'],report['errors']
    (ROOT/'research/a_arrays-browser-audit.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(state='passed',counts=report['counts'],models=len(ids),checkpoints=113,labReferences=466,mobile=report['mobile'],screenshots=str(OUT))))
finally:
    try:cdp('Browser.close')
    except Exception:pass
    proc.terminate();server.shutdown()
"""
(B/'qa_a_arrays_browser.py').write_text(prefix+tail,encoding='utf-8')
