"""Visual chapter QA and independent adjustable-laboratory reference checks."""
from pathlib import Path
import json
p=Path(__file__).resolve().parent
t=(p/'review_library_browser.py').read_text().replace("OUT=Path(tempfile.gettempdir())/'chapter-library-review'","OUT=Path(tempfile.gettempdir())/'p-arrays-browser'").replace("topics=[c['topicId'] for w in json.loads((ROOT/'dist/lessons.json').read_text()) for c in w['chapters']]","topics=['p_arrays']")
extra=r'''
  cdp('Runtime.evaluate',{'expression':'Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))','awaitPromise':True,'returnByValue':True})
  cases=0;bounds=[]
  inputs=[[u] for u in range(-20,21)]+[[u,1,-2,4,-5,6] for u in range(-20,21)]+[list(range(n)) for n in range(2,7)]+[[-20]*6,[20]*6,[1,3,5,7,9,11]]
  for mode in ['prefix','right','bad','reverse','difference','compact']:
   for a in inputs:
    js("document.getElementById('arrays-form').elements.mode.value="+json.dumps(mode)+";document.getElementById('arrays-form').elements.input.value="+json.dumps(','.join(map(str,a)))+";document.getElementById('arrays-form').dispatchEvent(new Event('input'))")
    states=js("JSON.parse(document.getElementById('arrays-output').dataset.states)")
    expected=[];b=a[:];prefix=[0];w=0
    def put():expected.append((b[:],prefix[:],w))
    put()
    if mode=='prefix':
     for v in a:prefix.append(prefix[-1]+v);put()
    elif mode in ('right','bad'):
     for i in (range(len(a)-2,-1,-1) if mode=='right' else range(len(a)-1)):b[i+1]=b[i];put()
    elif mode=='reverse':
     for i in range(len(a)//2):j=len(a)-1-i;b[i],b[j]=b[j],b[i];put()
    elif mode=='difference':
     for i in range(len(a)-1,0,-1):b[i]-=b[i-1];put()
    else:
     for i,v in enumerate(a):
      if v%2==0:b[w]=v;w+=1
      put()
    if len(expected)==1:put()
    actual=[(s['values'],s['prefix'],s['write']) for s in states];assert actual==expected,(mode,a,actual,expected)
    assert js("document.getElementById('arrays-output').dataset.valid==='true'&&ConceptAnimations.players.find(p=>p.host.id==='arrays-player').index===0"),(mode,a)
    bounds.extend(js("""(()=>{const p=ConceptAnimations.players.find(p=>p.host.id==='arrays-player'),issues=[];for(let i=0;i<p.scene.frames.length;i++){p.show(i,false);for(const t of p.canvas.querySelectorAll('text')){if(!t.textContent.trim())continue;const b=t.getBBox(),m=t.parentElement.transform.baseVal.consolidate()?.matrix||{e:0,f:0};if(b.x+m.e<0||b.y+m.f<0||b.x+m.e+b.width>760||b.y+m.f+b.height>360)issues.push(t.textContent);}}p.show(0,false);return issues;})()"""));cases+=1
  assert not bounds,bounds
  bads=['','1.5','NaN','21','-21','1e1','+2','1 2','1,2,3,4,5,6,7','2,','--2']
  for bad in bads:
   js("document.getElementById('arrays-form').elements.input.value="+json.dumps(bad)+";document.getElementById('arrays-form').dispatchEvent(new Event('input'))")
   assert js("document.getElementById('arrays-output').dataset.valid==='false'&&document.getElementById('arrays-player').hidden"),bad
  js("document.getElementById('arrays-form').elements.input.value='2,4,6,8,10,12';document.getElementById('arrays-form').elements.mode.value='prefix';document.getElementById('arrays-form').dispatchEvent(new Event('input'));window.labPlayer=ConceptAnimations.players.find(p=>p.host.id==='arrays-player');window.tokenStart=labPlayer.positions.get('token');labPlayer.buttons.next.click()")
  time.sleep(.12);moving=js("({busy:labPlayer.busy,start:tokenStart.x,end:labPlayer.scene.frames[1].nodes.find(n=>n.id==='token').x})");assert moving['busy'] and moving['start']!=moving['end'],moving
  time.sleep(.65);assert js('!labPlayer.busy&&labPlayer.index===1')
  js('labPlayer.buttons.back.click()');time.sleep(.75);assert js('labPlayer.index===0')
  js('labPlayer.seek.value=3;labPlayer.seek.dispatchEvent(new Event("input"))');assert js('labPlayer.index===3')
  js('labPlayer.buttons.reset.click();labPlayer.buttons.zoom.click()');assert js('labPlayer.host.dataset.enlarged==="true"');js('labPlayer.buttons.zoom.click()')
  cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]});js('labPlayer.buttons.next.click()');assert js('!labPlayer.busy&&labPlayer.index===1');cdp('Emulation.setEmulatedMedia',{'features':[]});js('labPlayer.buttons.reset.click()')
  row['laboratory']={'models':6,'acceptedInputCases':cases,'invalidInputCases':len(bads),'exactTransitions':True,'tokenMotion':True,'controlChecks':True,'textBounds':True}
  font=js("({body:getComputedStyle(document.querySelector('.lesson p')).fontFamily,title:getComputedStyle(document.querySelector('h1')).fontFamily,code:getComputedStyle(document.querySelector('pre code')).fontFamily,math:[...document.querySelectorAll('math')].every(x=>getComputedStyle(x).fontFamily.includes('STIX')),underline:[...document.querySelectorAll('a')].some(x=>getComputedStyle(x).textDecorationLine.includes('underline'))})")
  assert 'Source Sans' in font['body'] and 'Newsreader' in font['title'] and 'JetBrains' in font['code'] and font['math'] and not font['underline'],font;row['dedicatedFonts']=font
  js('scrollTo(0,0)');(OUT/'p_arrays-desktop.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
'''
t=t.replace("  cdp('Emulation.setDeviceMetricsOverride',{'width':390,'height':844,'deviceScaleFactor':1,'mobile':True})",extra+"\n  cdp('Emulation.setDeviceMetricsOverride',{'width':390,'height':844,'deviceScaleFactor':1,'mobile':True})")
mobile=r'''
  for label,selector in [('problems','#problems'),('notes','#review'),('lab','#arrays-lab'),('code','pre'),('formula','.formula-block'),('animation','#animation-mutation')]:
   js("document.querySelector("+json.dumps(selector)+").scrollIntoView({block:'start'})");(OUT/('p_arrays-mobile-'+label+'.png')).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
  js("document.querySelector('.arrays-figure-toggle').click();document.querySelector('.arrays-diagram').scrollIntoView({block:'start'})");assert js("document.querySelector('.arrays-diagram').classList.contains('expanded')&&document.documentElement.scrollWidth<=390")
  (OUT/'p_arrays-mobile-expanded-figure.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']));js("document.querySelector('.arrays-figure-toggle').click()")
'''
t=t.replace("  cdp('Emulation.setDeviceMetricsOverride',{'width':794,'height':1123,'deviceScaleFactor':1,'mobile':False})",mobile+"\n  cdp('Emulation.setDeviceMetricsOverride',{'width':794,'height':1123,'deviceScaleFactor':1,'mobile':False})")
exec(compile(t,'arrays-browser','exec'),{'__file__':str(p/'review_library_browser.py')})
out=Path('C:/Users/bheydari/AppData/Local/Temp/p-arrays-browser');rows=json.loads((out/'browser-review.json').read_text());(p/'p_arrays-browser-review.json').write_text(json.dumps(dict(state='passed',screenshots=str(out),chapters=rows),indent=2)+'\n')
