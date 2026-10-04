"""Observed browser checks with an independent Python contract oracle."""
from pathlib import Path
import json
B=Path(__file__).resolve().parent
t=(B/'review_library_browser.py').read_text().replace("OUT=Path(tempfile.gettempdir())/'chapter-library-review'","OUT=Path(tempfile.gettempdir())/'g-combin-browser'").replace("topics=[c['topicId'] for w in json.loads((ROOT/'dist/lessons.json').read_text()) for c in w['chapters']]","topics=['g_combin']")
extra=r'''
  from verify_g_combin_en import reference
  cdp('Runtime.evaluate',{'expression':'Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))','awaitPromise':True,'returnByValue':True})
  cases=0;bounds=[]
  for mode in ['shared','priority','nand']:
   for fault in [False,True]:
    for i in range(16):
     bits=[(i>>(3-j))&1 for j in range(4)];a=js('CombinLab.solve('+json.dumps(mode)+','+json.dumps(bits)+','+str(fault).lower()+')')
     want=reference(mode,bits);cand=reference(mode,bits,fault);assert a['reference']==want and a['candidate']==cand and a['miter']==int(want!=cand),(mode,i,a);cases+=1
     assert a['cost']=={'shared':{'gates':4,'depth':3},'priority':{'gates':6,'depth':3},'nand':{'gates':3,'depth':2}}[mode]
    js("document.getElementById('combin-form').elements.mode.value="+json.dumps(mode)+";document.getElementById('combin-form').elements.variant.value="+json.dumps('faulty' if fault else 'correct')+";document.getElementById('combin-form').dispatchEvent(new Event('input'))")
    table=js("JSON.parse(document.getElementById('combin-output').dataset.table)")
    assert all(x['reference']==reference(mode,x['bits']) and x['candidate']==reference(mode,x['bits'],fault) for x in table)
    bounds.extend(js("""(()=>{const p=ConceptAnimations.players.find(p=>p.host.id==='combin-player'),issues=[];for(let i=0;i<p.scene.frames.length;i++){p.show(i,false);for(const t of p.canvas.querySelectorAll('text')){if(!t.textContent.trim())continue;const b=t.getBBox(),m=t.parentElement.transform.baseVal.consolidate()?.matrix||{e:0,f:0};if(b.x+m.e<0||b.y+m.f<0||b.x+m.e+b.width>760||b.y+m.f+b.height>360)issues.push(t.textContent);}}p.show(0,false);return issues;})()"""))
  assert not bounds,bounds
  for expr in ['CombinLab.solve("bad",[0,0,0,0])','CombinLab.solve("shared",[0,2,0,0])','CombinLab.solve("shared",[0,0,0])','CombinLab.solve("nand",[0,0,0,NaN])']:
   assert js('(()=>{try{'+expr+';return false}catch(e){return true}})()')
  js("document.getElementById('combin-form').elements.mode.value='shared';document.getElementById('combin-form').elements.variant.value='correct';document.getElementById('combin-form').dispatchEvent(new Event('input'));window.labPlayer=ConceptAnimations.players.find(p=>p.host.id==='combin-player');window.tokenStart=labPlayer.positions.get('token').x;labPlayer.buttons.next.click()")
  time.sleep(.12);assert js("labPlayer.busy&&tokenStart!==labPlayer.scene.frames[1].nodes.find(n=>n.id==='token').x")
  time.sleep(.7);assert js('!labPlayer.busy&&labPlayer.index===1')
  js('labPlayer.buttons.back.click()');time.sleep(.75);assert js('labPlayer.index===0')
  js('labPlayer.seek.value=2;labPlayer.seek.dispatchEvent(new Event("input"))');assert js('labPlayer.index===2')
  js('labPlayer.buttons.reset.click();labPlayer.buttons.zoom.click()');assert js('labPlayer.host.dataset.enlarged==="true"');js('labPlayer.buttons.zoom.click()')
  cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]});js('labPlayer.buttons.next.click()');assert js('!labPlayer.busy&&labPlayer.index===1');cdp('Emulation.setEmulatedMedia',{'features':[]});js('labPlayer.buttons.reset.click()')
  row['laboratory']={'exactInputCases':cases,'renderedModeVariants':6,'invalidCalls':4,'controls':True,'motion':True,'reducedMotion':True,'labelBounds':True}
  font=js("({body:getComputedStyle(document.querySelector('.lesson p')).fontFamily,title:getComputedStyle(document.querySelector('h1')).fontFamily,code:getComputedStyle(document.querySelector('pre code')).fontFamily,math:[...document.querySelectorAll('math')].every(x=>getComputedStyle(x).fontFamily.includes('STIX')),underline:[...document.querySelectorAll('a')].some(x=>getComputedStyle(x).textDecorationLine.includes('underline'))})")
  assert 'Source Sans' in font['body'] and 'Newsreader' in font['title'] and 'JetBrains' in font['code'] and font['math'] and not font['underline'],font;row['dedicatedFonts']=font
  for label,selector in [('desktop','h1'),('formula','.formula-block'),('lab','#combin-lab'),('notes','#review'),('problems','#original-questions')]:
   js('document.querySelector('+json.dumps(selector)+').scrollIntoView({block:"start"})');(OUT/('g_combin-'+label+'.png')).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
'''
t=t.replace("  cdp('Emulation.setDeviceMetricsOverride',{'width':390,'height':844,'deviceScaleFactor':1,'mobile':True})",extra+"\n  cdp('Emulation.setDeviceMetricsOverride',{'width':390,'height':844,'deviceScaleFactor':1,'mobile':True})")
mobile=r'''
  for label,selector in [('mobile-formula','.formula-block'),('mobile-notes','#review'),('mobile-lab','#combin-lab'),('mobile-animation','#animation-mapping')]:
   js('document.querySelector('+json.dumps(selector)+').scrollIntoView({block:"start"})');(OUT/('g_combin-'+label+'.png')).write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
  js("document.querySelector('.combin-figure-toggle').click();document.querySelector('.combin-diagram').scrollIntoView({block:'start'})");assert js("document.querySelector('.combin-diagram').classList.contains('expanded')&&document.documentElement.scrollWidth<=390"),js("({expanded:document.querySelector('.combin-diagram').classList.contains('expanded'),width:document.documentElement.scrollWidth,formulaIssues:[...document.querySelectorAll('.formula-block')].filter(x=>x.scrollWidth>x.clientWidth+1).map(x=>({text:x.textContent,extra:x.scrollWidth-x.clientWidth})),outside:[...document.querySelectorAll('body *')].filter(x=>x.getBoundingClientRect().right>391).slice(-20).map(x=>({tag:x.tagName,class:x.getAttribute('class'),content:x.textContent.slice(0,120),width:x.getBoundingClientRect().width,right:x.getBoundingClientRect().right}))})")
  (OUT/'g_combin-mobile-expanded.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']));js("document.querySelector('.combin-figure-toggle').click()")
'''
t=t.replace("  cdp('Emulation.setDeviceMetricsOverride',{'width':794,'height':1123,'deviceScaleFactor':1,'mobile':False})",mobile+"\n  cdp('Emulation.setDeviceMetricsOverride',{'width':794,'height':1123,'deviceScaleFactor':1,'mobile':False})")
exec(compile(t,'combin-browser','exec'),{'__file__':str(B/'review_library_browser.py')})
out=Path('C:/Users/bheydari/AppData/Local/Temp/g-combin-browser');rows=json.loads((out/'browser-review.json').read_text());(B/'g_combin-browser-review.json').write_text(json.dumps(dict(state='passed',screenshots=str(out),chapters=rows),indent=2)+'\n')
