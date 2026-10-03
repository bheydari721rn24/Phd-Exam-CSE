"""Actual browser checks: MathML, diagrams, fonts, solutions and lab behavior."""
import tempfile
from pathlib import Path
p=Path(__file__).resolve().parent
t=(p/'review_library_browser.py').read_text(encoding='utf-8')
t=t.replace("OUT=Path(tempfile.gettempdir())/'chapter-library-review'","OUT=Path(tempfile.gettempdir())/'a-correct-browser'")
t=t.replace("topics=[c['topicId'] for w in json.loads((ROOT/'dist/lessons.json').read_text()) for c in w['chapters']]","topics=['a_correct']")
extra='''
  for preset,status,result,steps in [('duplicates','terminated','1','3'),('empty','terminated','0','0'),('stall','stalled','0','1')]:
   js(f"document.querySelector('[data-search-preset={preset}]').click()")
   flags=js("({...document.getElementById('search-output').dataset})")
   assert flags['valid']=='true' and flags['status']==status and flags['result']==result and flags['steps']==steps and flags['invariant']=='true',flags
  js("document.getElementById('search-array').value='3,1';document.getElementById('search-array').dispatchEvent(new Event('change'))")
  assert js("document.getElementById('search-array').validity.customError")
  js("document.getElementById('search-array').value='1,,2';document.getElementById('search-array').dispatchEvent(new Event('change'))")
  assert js("document.getElementById('search-array').validity.customError")
  js("document.querySelector('[data-search-preset=duplicates]').click();scrollTo(0,0)")
  shot=cdp('Page.captureScreenshot',{'format':'png'})['data']
  (OUT/'a_correct-desktop-opening.png').write_bytes(base64.b64decode(shot))
'''
t=t.replace("  row={'topicId':topic,'figures':[]}",extra+"\n  row={'topicId':topic,'figures':[]}")
extra='''
  assert row['mobile']['problems']==54
  row['wideElements']=js("[...document.querySelectorAll('article *')].filter(x=>x.getBoundingClientRect().right>391).map(x=>({tag:x.tagName,cls:x.className,right:x.getBoundingClientRect().right,text:x.textContent.slice(0,130)})).slice(0,30)")
  if row['mobile']['document']>390:print(row['wideElements'])
  assert row['solutionPrint']['count']==54
  assert js("document.querySelectorAll('.review-rule').length") ==74
  assert all('STIX Two Math' in f for f in row['fonts']['math']),row['fonts']
  assert any('JetBrains Mono' in f for f in row['mobile']['codeFonts'])
  assert all('STIX Two Math' in label['font'] for f in row['figures'] for label in f['labels'])
  assert js("[...document.querySelectorAll('a')].every(x=>getComputedStyle(x).textDecorationLine==='none')")
  for name,target in [('lab','#search-lab'),('formula','.formula-block'),('notes','#review'),('problems','#original-questions'),('code','pre')]:
   js(f"document.querySelector({json.dumps(target)}).scrollIntoView({{block:'start'}})")
   shot=cdp('Page.captureScreenshot',{'format':'png'})['data']
   (OUT/f'a_correct-mobile-{name}.png').write_bytes(base64.b64decode(shot))
'''
t=t.replace("  cdp('Emulation.setDeviceMetricsOverride',{'width':794",extra+"\n  cdp('Emulation.setDeviceMetricsOverride',{'width':794")
generated=Path(tempfile.gettempdir())/'qa_correct_browser.generated.py'
generated.write_text(t,encoding='utf-8')
exec(compile(t,str(generated),'exec'))
