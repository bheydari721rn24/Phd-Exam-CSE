"""Exercise the exact residue laboratory and inspect desktop/mobile/print geometry."""
from pathlib import Path
p=Path(__file__).resolve().parent
t=(p/'review_library_browser.py').read_text(encoding='utf-8')
t=t.replace("OUT=Path(tempfile.gettempdir())/'chapter-library-review'","OUT=Path(tempfile.gettempdir())/'d-number-browser'")
t=t.replace("topics=[c['topicId'] for w in json.loads((ROOT/'dist/lessons.json').read_text()) for c in w['chapters']]","topics=['d_number']")
t=t.replace("if topic in ('d_logic','a_loop','l_matrices','g_gates'):","if topic=='d_number':")
t=t.replace("target={'d_logic':'figure','a_loop':'pre','l_matrices':'.formula-block','g_gates':'figure'}[topic]","target='math'")
t=t.replace("if topic in ('d_induction','g_number','g_gates'):","if topic=='d_number':")
extra='''
  def flags():return js("({...document.getElementById('number-output').dataset})")
  for name,count,g,inverse in [('unit',1,1,'5'),('many',4,4,'none'),('none',0,4,'none'),('zero',6,6,'none'),('negative',1,1,'2')]:
   js(f"document.querySelector('[data-preset={name}]').click()")
   assert flags()=={'count':str(count),'gcd':str(g),'inverse':inverse},(name,flags())
   assert js("document.querySelectorAll('.map-cell.solution').length")==count
  js("document.querySelector('[data-preset=many]').click();document.getElementById('number-m').value='61';document.getElementById('number-m').dispatchEvent(new Event('change'))")
  assert js("document.getElementById('number-m').validity.rangeOverflow")
  js("document.querySelector('[data-preset=many]').click();document.getElementById('number-a').value='';document.getElementById('number-a').dispatchEvent(new Event('change'))")
  assert js("document.getElementById('number-a').validity.valueMissing")
  js("document.querySelector('[data-preset=many]').click()")
'''
t=t.replace("  row={'topicId':topic,'figures':[]}",extra+"\n  row={'topicId':topic,'figures':[]}")
extra='''
  assert all('STIX Two Math' in f for f in row['fonts']['math']),row['fonts']
  assert any('JetBrains Mono' in f for f in row['mobile']['codeFonts']),row['mobile']
  js("document.getElementById('number-lab').scrollIntoView({block:'start'})")
  shot=cdp('Page.captureScreenshot',{'format':'png'})['data']
  (OUT/'d_number-mobile-lab.png').write_bytes(base64.b64decode(shot))
'''
t=t.replace("  cdp('Emulation.setDeviceMetricsOverride',{'width':794",extra+"\n  cdp('Emulation.setDeviceMetricsOverride',{'width':794")
exec(compile(t,str(p/'review_library_browser.py'),'exec'))
