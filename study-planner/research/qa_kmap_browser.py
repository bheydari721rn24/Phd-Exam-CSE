"""Desktop/mobile/print and independent JS-laboratory verification."""
from pathlib import Path
import json
p=Path(__file__).resolve().parent
t=(p/'review_library_browser.py').read_text().replace("OUT=Path(tempfile.gettempdir())/'chapter-library-review'","OUT=Path(tempfile.gettempdir())/'g-kmap-browser'").replace("topics=[c['topicId'] for w in json.loads((ROOT/'dist/lessons.json').read_text()) for c in w['chapters']]","topics=['g_kmap']")
extra=r'''
  from verify_g_kmap_en import independent
  cdp('Runtime.evaluate',{'expression':'Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))','awaitPromise':True,'returnByValue':True})
  cases=0
  for mask in range(256):
   on=[i for i in range(8) if mask&(1<<i)]
   # Copy the three-variable function into both A planes of the four-variable lab.
   on=on+[i+8 for i in on]
   for mode in ['SOP','POS']:
    actual=js('KmapLab.solve('+json.dumps(on)+',[],'+json.dumps(mode)+')');req=on if mode=='SOP' else sorted(set(range(16))-set(on))
    prime,cover,cost=independent(4,req)
    assert ([x['pattern'] for x in actual['primes']],sorted(tuple(x) for x in actual['covers']),tuple(actual['cost']))==(prime,cover,cost),(mask,mode,actual);cases+=1
  inputs=[([],[]),([1],[0,3]),([0,2,8,10],[]),([5,6,7,8,9,15],[0,1]),([0,2,3,4,5,7],[]),([1,5],[8,9,10,11]),(list(range(16)),[]),([],[0,1,2,3]),([2,3,5,7],list(range(10,16)))]
  bounds=[];rendered=0
  for on,dc in inputs:
   for mode in ['SOP','POS']:
    js("document.getElementById('kmap-form').elements.on.value="+json.dumps(','.join(map(str,on)))+";document.getElementById('kmap-form').elements.dc.value="+json.dumps(','.join(map(str,dc)))+";document.getElementById('kmap-form').elements.mode.value="+json.dumps(mode)+";document.getElementById('kmap-form').dispatchEvent(new Event('input'))")
    actual=js("JSON.parse(document.getElementById('kmap-output').dataset.result)");req=on if mode=='SOP' else sorted(set(range(16))-set(on)-set(dc));prime,cover,cost=independent(4,req,dc)
    assert ([x['pattern'] for x in actual['primes']],sorted(tuple(x) for x in actual['covers']),tuple(actual['cost']))==(prime,cover,cost)
    states=js("JSON.parse(document.getElementById('kmap-output').dataset.states)")
    for state in states:
     rows=set()
     for c in state['selected']:
      for i in range(16):
       if all(b=='-' or b==format(i,'04b')[j] for j,b in enumerate(c)):rows.add(i)
     assert state['covered']==sorted(rows) and state['requiredCovered']==sorted(rows&set(req))
    bounds.extend(js("""(()=>{const p=ConceptAnimations.players.find(p=>p.host.id==='kmap-player'),issues=[];for(let i=0;i<p.scene.frames.length;i++){p.show(i,false);for(const t of p.canvas.querySelectorAll('text')){if(!t.textContent.trim())continue;const b=t.getBBox(),m=t.parentElement.transform.baseVal.consolidate()?.matrix||{e:0,f:0};if(b.x+m.e<0||b.y+m.f<0||b.x+m.e+b.width>760||b.y+m.f+b.height>360)issues.push(t.textContent);}}p.show(0,false);return issues;})()"""));rendered+=1
  assert not bounds,bounds
  bads=[('16',''),('-1',''),('1,1',''),('1','1'),('NaN',''),('1.5',''),('1,',''),('','0,0'),('','17')]
  for on,dc in bads:
   js("document.getElementById('kmap-form').elements.on.value="+json.dumps(on)+";document.getElementById('kmap-form').elements.dc.value="+json.dumps(dc)+";document.getElementById('kmap-form').dispatchEvent(new Event('input'))")
   assert js("document.getElementById('kmap-output').dataset.valid==='false'&&document.getElementById('kmap-player').hidden")
  js("document.getElementById('kmap-form').elements.on.value='0,2,3,4,5,7';document.getElementById('kmap-form').elements.dc.value='';document.getElementById('kmap-form').elements.mode.value='SOP';document.getElementById('kmap-form').dispatchEvent(new Event('input'));window.labPlayer=ConceptAnimations.players.find(p=>p.host.id==='kmap-player');window.tokenStart=labPlayer.positions.get('token');labPlayer.buttons.next.click()")
  time.sleep(.12);moving=js("({busy:labPlayer.busy,start:tokenStart.x,end:labPlayer.scene.frames[1].nodes.find(n=>n.id==='token').x})");assert moving['busy'] and moving['start']!=moving['end'],moving
  time.sleep(.7);assert js('!labPlayer.busy&&labPlayer.index===1')
  js('labPlayer.buttons.back.click()');time.sleep(.75);assert js('labPlayer.index===0')
  js('labPlayer.seek.value=2;labPlayer.seek.dispatchEvent(new Event("input"))');assert js('labPlayer.index===2')
  js('labPlayer.buttons.reset.click();labPlayer.buttons.zoom.click()');assert js('labPlayer.host.dataset.enlarged==="true"');js('labPlayer.buttons.zoom.click()')
  cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]});js('labPlayer.buttons.next.click()');assert js('!labPlayer.busy&&labPlayer.index===1');cdp('Emulation.setEmulatedMedia',{'features':[]});js('labPlayer.buttons.reset.click()')
  row['laboratory']={'exactInputCases':cases+rendered,'renderedCases':rendered,'invalidInputCases':len(bads),'exactTransitions':True,'tokenMotion':True,'controlChecks':True,'textBounds':True}
  font=js("({body:getComputedStyle(document.querySelector('.lesson p')).fontFamily,title:getComputedStyle(document.querySelector('h1')).fontFamily,code:getComputedStyle(document.querySelector('pre code')).fontFamily,math:[...document.querySelectorAll('math')].every(x=>getComputedStyle(x).fontFamily.includes('STIX')),underline:[...document.querySelectorAll('a')].some(x=>getComputedStyle(x).textDecorationLine.includes('underline'))})")
  assert 'Source Sans' in font['body'] and 'Newsreader' in font['title'] and 'JetBrains' in font['code'] and font['math'] and not font['underline'],font;row['dedicatedFonts']=font
  js('scrollTo(0,0)');(OUT/'g_kmap-desktop.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
'''
t=t.replace("  cdp('Emulation.setDeviceMetricsOverride',{'width':390,'height':844,'deviceScaleFactor':1,'mobile':True})",extra+"\n  cdp('Emulation.setDeviceMetricsOverride',{'width':390,'height':844,'deviceScaleFactor':1,'mobile':True})")
mobile=r'''
  for label,selector in [('problems','#problems'),('notes','#review'),('lab','#kmap-lab'),('formula','.formula-block'),('animation','#animation-covers')]:
   js("document.querySelector("+json.dumps(selector)+").scrollIntoView({block:'start'})");(OUT/('g_kmap-mobile-'+label+'.png')).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
  js("document.querySelector('.kmap-figure-toggle').click();document.querySelector('.kmap-diagram').scrollIntoView({block:'start'})");assert js("document.querySelector('.kmap-diagram').classList.contains('expanded')&&document.documentElement.scrollWidth<=390")
  (OUT/'g_kmap-mobile-expanded-figure.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']));js("document.querySelector('.kmap-figure-toggle').click()")
'''
t=t.replace("  cdp('Emulation.setDeviceMetricsOverride',{'width':794,'height':1123,'deviceScaleFactor':1,'mobile':False})",mobile+"\n  cdp('Emulation.setDeviceMetricsOverride',{'width':794,'height':1123,'deviceScaleFactor':1,'mobile':False})")
exec(compile(t,'kmap-browser','exec'),{'__file__':str(p/'review_library_browser.py')})
out=Path('C:/Users/bheydari/AppData/Local/Temp/g-kmap-browser');rows=json.loads((out/'browser-review.json').read_text());(p/'g_kmap-browser-review.json').write_text(json.dumps(dict(state='passed',screenshots=str(out),chapters=rows),indent=2)+'\n')
