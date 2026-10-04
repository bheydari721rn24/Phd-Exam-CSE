"""Rendered chapter math, exact laboratory and actual concept motion."""
from pathlib import Path
import tempfile,json
p=Path(__file__).resolve().parent
t=(p/'review_library_browser.py').read_text()
t=t.replace("OUT=Path(tempfile.gettempdir())/'chapter-library-review'","OUT=Path(tempfile.gettempdir())/'l-rank-browser'")
t=t.replace("topics=[c['topicId'] for w in json.loads((ROOT/'dist/lessons.json').read_text()) for c in w['chapters']]","topics=['l_rank']")
extra=r'''
  import sympy as S
  cases=[]
  for preset in ['pivot','tall','wide','zero','fractions','exceptional']:
   js(f"document.querySelector('[data-rank-preset={preset}]').click()")
   flags=js("({...document.getElementById('rank-output').dataset})")
   assert flags['valid']=='true',flags
   A=S.Matrix([[S.Rational(v) for v in r] for r in json.loads(flags['input'])]);R,piv=A.rref();r=A.rank()
   assert int(flags['rank'])==r and json.loads(flags['pivots'])==list(piv)
   assert S.Matrix(json.loads(flags['rref'])).applyfunc(S.Rational)==R
   for key,M,dim in [('null',A,A.cols-r),('left',A.T,A.rows-r)]:
    vs=[S.Matrix([S.Rational(v) for v in col]) for col in json.loads(flags[key])]
    assert len(vs)==dim and all(M*v==S.zeros(M.rows,1) for v in vs)
    assert not vs or S.Matrix.hstack(*vs).rank()==dim
   assert json.loads(flags['column'])==[list(map(str,A[:,j])) for j in piv]
   assert json.loads(flags['row'])==[list(map(str,R.row(i))) for i in range(r)]
   js("document.querySelector('[data-rank-step=next]').click()")
   assert js("document.getElementById('rank-output').dataset.step")=='1'
   js("document.querySelector('[data-rank-step=back]').click()")
   assert js("document.getElementById('rank-output').dataset.step")=='0'
   js("document.querySelector('[data-rank-step=next]').click();document.querySelector('[data-rank-step=reset]').click()")
   assert js("document.getElementById('rank-output').dataset.step")=='0'
   cases.append({'preset':preset,'rank':r,'nullity':A.cols-r,'leftNullity':A.rows-r})
  for bad in ['', '1 2\n3', '1/0 2', 'x 1', '0.5 1', '100001', '1 2 3 4 5 6', '1\n1\n1\n1\n1\n1']:
   js("document.getElementById('rank-form').elements.matrix.value="+json.dumps(bad)+";document.getElementById('rank-form').dispatchEvent(new Event('input'))")
   assert js("document.getElementById('rank-output').dataset.valid==='false'")
  js("document.querySelector('[data-rank-preset=pivot]').click()")
  cdp('Runtime.evaluate',{'expression':'Promise.all([...document.querySelectorAll(".concept-animation")].map(h=>ConceptAnimations.ready(h)))','awaitPromise':True,'returnByValue':True})
  js('window.rankPlayer=ConceptAnimations.players.find(p=>p.host.id==="animation-solutions");rankPlayer.show(0,false);window.inputStart=rankPlayer.positions.get("input");rankPlayer.buttons.next.click()')
  time.sleep(.15)
  motion=js('({busy:rankPlayer.busy,start:inputStart,end:rankPlayer.scene.frames[1].nodes.find(n=>n.id==="input"),actual:rankPlayer.nodes.get("input").getAttribute("transform")})')
  assert motion['busy'] and motion['start']['x']!=motion['end']['x'],motion
  time.sleep(.6)
  assert js('!rankPlayer.busy&&rankPlayer.index===1')
  js('rankPlayer.buttons.reset.click();scrollTo(0,0)')
  (OUT/'l_rank-desktop.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
'''
t=t.replace("  row={'topicId':topic,'figures':[]}",extra+"\n  row={'topicId':topic,'figures':[]}")
extra=r'''
  assert row['mobile']['problems']==90 and row['solutionPrint']['count']==90
  assert js("document.querySelectorAll('.review-rule').length")==80
  assert all('STIX Two Math' in f for f in row['fonts']['math'])
  assert any('JetBrains Mono' in f for f in row['mobile']['codeFonts'])
  assert all('STIX Two Math' in x['font'] for f in row['figures'] for x in f['labels'])
  assert js("[...document.querySelectorAll('a')].every(x=>getComputedStyle(x).textDecorationLine==='none')")
  for name,target in [('lab','#rank-lab'),('matrix','.formula-block:has(mtable[columnspacing])'),('notes','#review'),('problems','#original-questions'),('code','pre'),('animation','#animation-solutions')]:
   js(f"document.querySelector({json.dumps(target)}).scrollIntoView({{block:'start'}})")
   (OUT/f'l_rank-mobile-{name}.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
  row['labCases']=cases;row['fiberMotion']=motion
  js("document.querySelector('.rank-figure-toggle').click()")
  assert js("document.querySelector('.rank-diagram').classList.contains('expanded')&&document.documentElement.scrollWidth<=innerWidth")
  js("document.querySelector('.rank-diagram').scrollIntoView({block:'start'})")
  (OUT/'l_rank-mobile-expanded-figure.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png'})['data']))
  js("document.querySelector('.rank-figure-toggle').click()")
'''
t=t.replace("  cdp('Emulation.setDeviceMetricsOverride',{'width':794",extra+"\n  cdp('Emulation.setDeviceMetricsOverride',{'width':794")
generated=Path(tempfile.gettempdir())/'qa_rank_browser.generated.py';generated.write_text(t)
exec(compile(t,str(generated),'exec'))
report=json.loads((OUT/'browser-review.json').read_text())
summary=dict(state='passed',chapter='l_rank',rendered=report,labChecks='six exact four-space presets; eight invalid input cases; next/back/reset; actual moving fiber input',screenshots=str(OUT),limits='Local Edge desktop, 390-pixel mobile and print, finite interactions.')
(p/'l_rank-browser-review.json').write_text(json.dumps(summary,indent=2)+'\n')
print('Rank browser and laboratory passed.')
