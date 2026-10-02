"""Actual browser typography, diagram, MathML and lab checks."""
import tempfile
from pathlib import Path
p=Path(__file__).resolve().parent
t=(p/'review_library_browser.py').read_text(encoding='utf-8')
t=t.replace("OUT=Path(tempfile.gettempdir())/'chapter-library-review'","OUT=Path(tempfile.gettempdir())/'a-divide-browser'")
t=t.replace("topics=[c['topicId'] for w in json.loads((ROOT/'dist/lessons.json').read_text()) for c in w['chapters']]","topics=['a_divide']")
t=t.replace("if topic in ('d_logic','a_loop','l_matrices','g_gates'):","if topic=='a_divide':")
t=t.replace("target={'d_logic':'figure','a_loop':'pre','l_matrices':'.formula-block','g_gates':'figure'}[topic]","target='math'")
t=t.replace("if topic in ('d_induction','g_number','g_gates'):","if topic=='a_divide':")
extra='''
  def flags():return js("({...document.getElementById('subarray-output').dataset})")
  for name,best,start,end in [('crossing','9','2','5'),('negative','-2','1','2'),('left','9','0','2'),('ties','2','0','1')]:
   js(f"document.querySelector('[data-preset={name}]').click()")
   assert flags()=={'best':best,'start':start,'end':end,'verified':'true'},(name,flags())
  js("document.getElementById('subarray-split').value='3';document.getElementById('subarray-split').dispatchEvent(new Event('change',{bubbles:true}))")
  assert js("document.getElementById('subarray-split').validity.rangeOverflow") and flags()['verified']=='false'
  js("document.querySelector('[data-preset=crossing]').click();document.getElementById('subarray-input').value='1,,2';document.getElementById('subarray-input').dispatchEvent(new Event('change',{bubbles:true}))")
  assert js("document.getElementById('subarray-input').validity.customError") and flags()['verified']=='false'
  js("document.querySelector('[data-preset=crossing]').click();document.getElementById('subarray-input').value='1,100';document.getElementById('subarray-split').value='1';document.getElementById('subarray-input').dispatchEvent(new Event('change',{bubbles:true}))")
  assert js("document.getElementById('subarray-input').validity.customError") and flags()['verified']=='false'
  js("document.querySelector('[data-preset=crossing]').click()")
  js("scrollTo(0,0)")
  shot=cdp('Page.captureScreenshot',{'format':'png'})['data']
  (OUT/'a_divide-desktop-opening.png').write_bytes(base64.b64decode(shot))
'''
t=t.replace("  row={'topicId':topic,'figures':[]}",extra+"\n  row={'topicId':topic,'figures':[]}")
extra='''
  assert row['mobile']['problems']==48
  assert all('STIX Two Math' in f for f in row['fonts']['math']),row['fonts']
  assert any('JetBrains Mono' in f for f in row['mobile']['codeFonts'])
  assert all('STIX Two Math' in label['font'] for f in row['figures'] for label in f['labels'])
  assert js("[...document.querySelectorAll('a')].every(x=>getComputedStyle(x).textDecorationLine==='none')")
  assert js("[...document.querySelectorAll('svg tspan')].every(x=>getComputedStyle(x).fontFamily.includes('STIX Two Math'))")
  for index in range(12):
   js(f"document.querySelectorAll('math')[{index}].scrollIntoView({{block:'start'}})")
   shot=cdp('Page.captureScreenshot',{'format':'png'})['data']
   (OUT/f'a_divide-mobile-math-{index+1}.png').write_bytes(base64.b64decode(shot))
  for name,target in [('lab','#subarray-lab'),('code','pre'),('rules','#review')]:
   js(f"document.querySelector({json.dumps(target)}).scrollIntoView({{block:'start'}})")
   shot=cdp('Page.captureScreenshot',{'format':'png'})['data']
   (OUT/f'a_divide-mobile-{name}.png').write_bytes(base64.b64decode(shot))
'''
t=t.replace("  cdp('Emulation.setDeviceMetricsOverride',{'width':794",extra+"\n  cdp('Emulation.setDeviceMetricsOverride',{'width':794")
generated=Path(tempfile.gettempdir())/'qa_divide_browser.generated.py'
generated.write_text(t,encoding='utf-8')
exec(compile(t,str(generated),'exec'))
