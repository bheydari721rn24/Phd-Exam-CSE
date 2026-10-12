from pathlib import Path
B=Path(__file__).parent
s=(B/'qa_deep_matrices_browser.py').read_text();a=s.index(" report['models']=");b=s.index('finally:',a)
extra=r''' report['signs']=js("""(()=>{const c=ConceptAnimations.players.find(c=>c.api.model.id==='matrices-question-shear');c.api.show(2);return [...c.api.host.querySelectorAll('svg math msup')].map(m=>({markup:m.outerHTML,text:m.textContent,children:[...m.querySelectorAll('mo,mn')].map(x=>({text:x.textContent,width:x.getBoundingClientRect().width,display:getComputedStyle(x).display}))}));})()""")
 print(json.dumps(report['signs'],indent=2))
 capture('.concept-animation[data-scenes="matrices-question-shear"]','signs-full.png')
 clip=js("""(()=>{const h=document.querySelector('.concept-animation[data-scenes="matrices-question-shear"]'),m=h.querySelector('svg foreignObject math'),b=m.getBoundingClientRect();return {x:b.x+scrollX,y:b.y+scrollY,width:b.width,height:b.height,scale:3};})()""")
 (OUT/'signs-zoom.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png','clip':clip})['data']))
 js("document.querySelectorAll('.concept-animation[data-scenes=\"matrices-question-shear\"] svg math mo').forEach(m=>{if(m.textContent==='-')m.textContent='−';})")
 (OUT/'signs-unicode.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png','clip':clip})['data']))
'''
s=s[:a]+extra+s[b:];s=s.replace("l_matrices-browser.json","l_matrices-signs.json")
exec(compile(s,str(B/'qa_deep_matrices_browser.py'),'exec'))
