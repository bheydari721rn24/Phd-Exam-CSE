"""Render current chapter and test every accepted lab input against a model."""
from pathlib import Path
p=Path(__file__).resolve().parent
t=(p/'review_library_browser.py').read_text()
t=t.replace("OUT=Path(tempfile.gettempdir())/'chapter-library-review'","OUT=Path(tempfile.gettempdir())/'p-functions-browser'")
t=t.replace("topics=[c['topicId'] for w in json.loads((ROOT/'dist/lessons.json').read_text()) for c in w['chapters']]","topics=['p_functions']")
extra=r'''
  assert js('document.getElementById("functions-output").dataset.valid')=='true',js('({errors:window.chapterErrors,html:document.getElementById("functions-output").outerHTML})')
  cdp('Runtime.evaluate',{'expression':'Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))','awaitPromise':True,'returnByValue':True})
  expectedModels=0;bounds=[]
  for mode in ['copy','pointer','alias','static','nested']:
   for u in range(-20,21):
    js("document.getElementById('functions-form').elements.mode.value="+json.dumps(mode)+";document.getElementById('functions-form').elements.input.value="+json.dumps(str(u))+";document.getElementById('functions-form').dispatchEvent(new Event('input'))")
    values=js("JSON.parse(document.getElementById('functions-output').dataset.states)")
    actual=[(s['caller'],s['shared'],s['value']) for s in values]
    if mode=='copy':expected=[(u,None,u),(u,None,u),(u,None,2*(u+3)),(u,None,2*(u+3))]
    elif mode=='pointer':expected=[(u,u,'&a'),(u,u,'&a'),(2*u+3,2*u+3,2*u+3),(2*u+3,2*u+3,'void')]
    elif mode=='alias':expected=[(u,u,u),(u+2,u+2,u+2),(3*(u+2),3*(u+2),3*(u+2))]
    elif mode=='static':expected=[v for k in range(1,4) for v in [(u,(k-1)*u,None),(u,k*u,10+k*u),(u,k*u,10+k*u)]]
    else:expected=[(u,None,u),(u,None,3*u+1),(u,None,3*u+1),(u,None,9*u+4),(u,None,12*u+5)]
    assert actual==expected,(mode,u,actual,expected)
    assert js("document.getElementById('functions-output').dataset.valid==='true'"),(mode,u)
    assert js("ConceptAnimations.players.find(p=>p.host.id==='functions-player').index===0"),(mode,u,js("ConceptAnimations.players.find(p=>p.host.id==='functions-player').index"))
    bounds.extend(js("""(()=>{const p=ConceptAnimations.players.find(p=>p.host.id==='functions-player'),issues=[];for(let i=0;i<p.scene.frames.length;i++){p.show(i,false);const boxes=[...p.canvas.querySelectorAll('text')].filter(x=>x.textContent.trim()).map(t=>{const b=t.getBBox(),m=t.parentElement.transform.baseVal.consolidate()?.matrix||{e:0,f:0};return {x:b.x+m.e,y:b.y+m.f,w:b.width,h:b.height,text:t.textContent};});for(const b of boxes)if(b.x<0||b.y<0||b.x+b.w>760||b.y+b.h>360)issues.push(b);}p.show(0,false);return issues;})()"""))
    expectedModels+=1
  assert not bounds,bounds
  for bad in ['', '1.5','NaN','21','-21','1e1','+2','4 5']:
   js("document.getElementById('functions-form').elements.input.value="+json.dumps(bad)+";document.getElementById('functions-form').dispatchEvent(new Event('input'))")
   assert js("document.getElementById('functions-output').dataset.valid==='false'&&document.getElementById('functions-player').hidden")
  js("document.getElementById('functions-form').elements.input.value='4';document.getElementById('functions-form').elements.mode.value='copy';document.getElementById('functions-form').dispatchEvent(new Event('input'));window.labPlayer=ConceptAnimations.players.find(p=>p.host.id==='functions-player');window.tokenStart=labPlayer.positions.get('token');labPlayer.buttons.next.click()")
  time.sleep(.12)
  moving=js("({busy:labPlayer.busy,start:tokenStart.x,end:labPlayer.scene.frames[1].nodes.find(n=>n.id==='token').x,transform:labPlayer.nodes.get('token').getAttribute('transform')})")
  assert moving['busy'] and moving['start']!=moving['end'],moving
  time.sleep(.65);assert js("!labPlayer.busy&&labPlayer.index===1")
  js("labPlayer.buttons.back.click()");time.sleep(.75);assert js('labPlayer.index===0')
  js('labPlayer.seek.value=3;labPlayer.seek.dispatchEvent(new Event("input"))');assert js('labPlayer.index===3')
  js('labPlayer.buttons.reset.click();labPlayer.buttons.zoom.click()');assert js('labPlayer.host.dataset.enlarged==="true"')
  js('labPlayer.buttons.zoom.click()')
  cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]})
  js('labPlayer.buttons.next.click()');assert js('!labPlayer.busy&&labPlayer.index===1')
  cdp('Emulation.setEmulatedMedia',{'features':[]});js('labPlayer.buttons.reset.click()')
  row['laboratory']={'models':5,'acceptedInputCases':expectedModels,'invalidInputCases':8,'exactTransitions':True,'tokenMotion':True,'controlChecks':True,'textBounds':True}
  font=js("({body:getComputedStyle(document.querySelector('.lesson p')).fontFamily,title:getComputedStyle(document.querySelector('h1')).fontFamily,code:getComputedStyle(document.querySelector('pre code')).fontFamily,math:[...document.querySelectorAll('math')].every(x=>getComputedStyle(x).fontFamily.includes('STIX')),underline:[...document.querySelectorAll('a')].some(x=>getComputedStyle(x).textDecorationLine.includes('underline'))})")
  assert 'Source Sans' in font['body'] and 'Newsreader' in font['title'] and 'JetBrains' in font['code'] and font['math'] and not font['underline'],font
  row['dedicatedFonts']=font
  js('scrollTo(0,0)');(OUT/'p_functions-desktop.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
'''
t=t.replace("  cdp('Emulation.setDeviceMetricsOverride',{'width':390,'height':844,'deviceScaleFactor':1,'mobile':True})",extra+"\n  cdp('Emulation.setDeviceMetricsOverride',{'width':390,'height':844,'deviceScaleFactor':1,'mobile':True})")
t=t.replace(" cdp('Page.enable')"," cdp('Page.enable')\n cdp('Page.addScriptToEvaluateOnNewDocument',{'source':'window.chapterErrors=[];addEventListener(\"error\",e=>chapterErrors.push({message:e.message,line:e.lineno,url:e.filename}));'})")
mobile=r'''
  for label,selector in [('problems','#problems'),('notes','#review'),('lab','#functions-lab'),('code','pre'),('formula','.formula-block'),('animation','#animation-values')]:
   js("document.querySelector("+json.dumps(selector)+").scrollIntoView({block:'start'})")
   (OUT/('p_functions-mobile-'+label+'.png')).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
  js("document.querySelector('.functions-figure-toggle').click();document.querySelector('.functions-diagram').scrollIntoView({block:'start'})")
  assert js("document.querySelector('.functions-diagram').classList.contains('expanded')")
  assert js('document.documentElement.scrollWidth<=390')
  (OUT/'p_functions-mobile-expanded-figure.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
  js("document.querySelector('.functions-figure-toggle').click()")
'''
t=t.replace("  cdp('Emulation.setDeviceMetricsOverride',{'width':794,'height':1123,'deviceScaleFactor':1,'mobile':False})",mobile+"\n  cdp('Emulation.setDeviceMetricsOverride',{'width':794,'height':1123,'deviceScaleFactor':1,'mobile':False})")
Path('C:/Users/bheydari/AppData/Local/Temp/expanded-functions-browser.py').write_text(t,encoding='utf-8')
exec(compile(t,'C:/Users/bheydari/AppData/Local/Temp/expanded-functions-browser.py','exec'),{'__file__':str(p/'review_library_browser.py')})
import json
out=Path('C:/Users/bheydari/AppData/Local/Temp/p-functions-browser')
rows=json.loads((out/'browser-review.json').read_text())
(p/'p_functions-browser-review.json').write_text(json.dumps(dict(state='passed',screenshots=str(out),chapters=rows),indent=2)+'\n')
