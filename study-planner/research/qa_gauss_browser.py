"""Rendered matrices, figures, exact JS traces and input/step controls."""
from pathlib import Path
import tempfile,json
p=Path(__file__).resolve().parent
t=(p/'review_library_browser.py').read_text()
t=t.replace("OUT=Path(tempfile.gettempdir())/'chapter-library-review'","OUT=Path(tempfile.gettempdir())/'l-gauss-browser'")
t=t.replace("topics=[c['topicId'] for w in json.loads((ROOT/'dist/lessons.json').read_text()) for c in w['chapters']]","topics=['l_gauss']")
extra=r'''
  from gauss_exact import solve,matrix,multiply
  cases=[]
  for preset in ['unique','free','affine','inconsistent','fractions','zero']:
   js(f"document.querySelector('[data-gauss-preset={preset}]').click()")
   flags=js("({...document.getElementById('gauss-output').dataset})")
   assert flags['valid']=='true',flags
   original=json.loads(flags['input']);r,piv,x,basis,transform,steps=solve(original)
   assert flags['state']==('inconsistent' if x is None else 'affine' if basis else 'unique')
   assert flags['particular']==('none' if x is None else ','.join(map(str,x)))
   assert json.loads(flags['basis'])==[list(map(str,v)) for v in basis]
   for s in json.loads(flags['trace']):
    assert multiply(matrix(s['transform']),matrix(original))==matrix(s['matrix'])
   js("document.querySelector('[data-gauss-step=next]').click()")
   assert js("document.getElementById('gauss-output').dataset.step")== '1'
   js("document.querySelector('[data-gauss-step=back]').click()")
   assert js("document.getElementById('gauss-output').dataset.step")== '0'
   js("document.querySelector('[data-gauss-step=next]').click();document.querySelector('[data-gauss-step=reset]').click()")
   assert js("document.getElementById('gauss-output').dataset.step")== '0'
   cases.append({'preset':preset,'state':flags['state'],'steps':len(json.loads(flags['trace']))})
  for bad in ['1 2\n1 2 3','1/0 2','abc 2','0.5 1','100001 2','1 2 3 4 5 6','1 2\n1 2\n1 2\n1 2\n1 2','']:
   js("document.getElementById('gauss-form').elements.matrix.value="+json.dumps(bad)+";document.getElementById('gauss-form').dispatchEvent(new Event('input'))")
   assert js("document.getElementById('gauss-output').dataset.valid==='false'")
  js("document.querySelector('[data-gauss-preset=unique]').click();scrollTo(0,0)")
  cdp('Runtime.evaluate',{'expression':'Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))','awaitPromise':True,'returnByValue':True})
  js('window.gaussPlayer=ConceptAnimations.players.find(p=>p.host.id==="animation-elimination");gaussPlayer.host.scrollIntoView({block:"start"});gaussPlayer.show(0,false);window.rowStart=gaussPlayer.positions.get("m0-0");gaussPlayer.buttons.next.click()')
  time.sleep(.15)
  motion=js('({busy:gaussPlayer.busy,start:rowStart,end:gaussPlayer.scene.frames[1].nodes.find(n=>n.id==="m0-0"),actual:gaussPlayer.nodes.get("m0-0").getAttribute("transform")})')
  assert motion['busy'] and motion['start']['y']!=motion['end']['y'],motion
  time.sleep(.6)
  assert js('!gaussPlayer.busy&&gaussPlayer.index===1')
  js('gaussPlayer.buttons.reset.click();scrollTo(0,0)')
  (OUT/'l_gauss-desktop.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
'''
t=t.replace("  row={'topicId':topic,'figures':[]}",extra+"\n  row={'topicId':topic,'figures':[]}")
extra=r'''
  assert row['mobile']['problems']==71 and row['solutionPrint']['count']==71
  assert js("document.querySelectorAll('.review-rule').length")==80
  assert all('STIX Two Math' in f for f in row['fonts']['math']),row['fonts']
  assert any('JetBrains Mono' in f for f in row['mobile']['codeFonts'])
  assert all('STIX Two Math' in label['font'] for f in row['figures'] for label in f['labels'])
  assert js("[...document.querySelectorAll('a')].every(x=>getComputedStyle(x).textDecorationLine==='none')")
  for name,target in [('lab','#gauss-lab'),('matrix','.formula-block:has(mtable)'),('notes','#review'),('problems','#original-questions'),('code','pre'),('animation','#animation-elimination')]:
   js(f"document.querySelector({json.dumps(target)}).scrollIntoView({{block:'start'}})")
   (OUT/f'l_gauss-mobile-{name}.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
  row['labCases']=cases
  row['rowExchangeMotion']=motion
  js("document.querySelector('.gauss-figure-toggle').click()")
  assert js("document.querySelector('.gauss-diagram').classList.contains('expanded')&&document.documentElement.scrollWidth<=innerWidth")
  js("document.querySelector('.gauss-diagram').scrollIntoView({block:'start'})")
  (OUT/'l_gauss-mobile-expanded-figure.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
  js("document.querySelector('.gauss-figure-toggle').click()")
'''
t=t.replace("  cdp('Emulation.setDeviceMetricsOverride',{'width':794",extra+"\n  cdp('Emulation.setDeviceMetricsOverride',{'width':794")
generated=Path(tempfile.gettempdir())/'qa_gauss_browser.generated.py';generated.write_text(t)
exec(compile(t,str(generated),'exec'))
report=json.loads((OUT/'browser-review.json').read_text())
summary=dict(state='passed',chapter='l_gauss',rendered=report,labChecks='six exact presets and every transform checkpoint; eight rejected input cases; next/back/reset controls',screenshots=str(OUT),limits='Local Edge desktop, 390-pixel mobile and print; finite tested interactions, not a universal browser claim.')
(p/'l_gauss-browser-review.json').write_text(json.dumps(summary,indent=2)+'\n')
public=p.parent/'dist/evidence/l_gauss';public.mkdir(parents=True,exist_ok=True)
(public/'browser.json').write_text(json.dumps(summary,indent=2)+'\n')
