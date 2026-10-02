"""Exercise the chapter laboratory and inspect exact desktop/mobile/print rendering."""
from pathlib import Path
p=Path(__file__).resolve().parent
t=(p/'review_library_browser.py').read_text(encoding='utf-8')
t=t.replace("OUT=Path(tempfile.gettempdir())/'chapter-library-review'","OUT=Path(tempfile.gettempdir())/'d-invariants-browser'")
t=t.replace("topics=[c['topicId'] for w in json.loads((ROOT/'dist/lessons.json').read_text()) for c in w['chapters']]","topics=['d_invariants']")
t=t.replace("if topic in ('d_logic','a_loop','l_matrices','g_gates'):","if topic=='d_invariants':")
t=t.replace("target={'d_logic':'figure','a_loop':'pre','l_matrices':'.formula-block','g_gates':'figure'}[topic]","target='math'")
t=t.replace("if topic in ('d_induction','g_number','g_gates'):","if topic=='d_invariants':")
extra='''
  def flags():
   return js("({...document.getElementById('invariant-output').dataset})")
  assert flags()=={'safe':'true','preserved':'false','terminates':'true'},flags()
  for name,expected in [('inductive',('true','true','false')),('unsafe',('false','false','true')),('chain',('true','true','true')),('cycle',('true','true','false')),('badrank',('true','true','true'))]:
   js(f"document.querySelector('[data-preset={name}]').click()")
   assert tuple(flags()[k] for k in ('safe','preserved','terminates'))==expected,(name,flags())
  assert 'Invalid on reachable edges' in js("document.getElementById('invariant-output').textContent")
  js("document.querySelector('[data-preset=chain]').click();document.querySelector('[data-member=\\\"0\\\"]').click()")
  assert flags()['safe']=='false'
  assert 'initial state 0 is excluded' in js("document.getElementById('invariant-output').textContent"),js("document.getElementById('invariant-output').textContent")
  js("document.querySelector('[data-preset=chain]').click();document.querySelector('[data-edge=\\\"0,0\\\"]').click()")
  assert flags()['terminates']=='false'
  js("document.querySelector('[data-preset=chain]').click();const r=document.querySelector('[data-rank=\\\"0\\\"]');r.value='-1';r.dispatchEvent(new Event('change',{bubbles:true})); ")
  assert js("document.querySelector('[data-rank=\\\"0\\\"]').validity.customError"),'Rank validation did not reject a negative input.'
  js("document.querySelector('[data-preset=noninductive]').click()")
'''
t=t.replace("  row={'topicId':topic,'figures':[]}",extra+"\n  row={'topicId':topic,'figures':[]}")
extra='''
  assert all('STIX Two Math' in f for f in row['fonts']['math']),row['fonts']
  assert any('JetBrains Mono' in f for f in row['mobile']['codeFonts']),row['mobile']
  js("document.getElementById('invariant-lab').scrollIntoView({block:'start'})")
  shot=cdp('Page.captureScreenshot',{'format':'png'})['data']
  (OUT/'d_invariants-mobile-lab.png').write_bytes(base64.b64decode(shot))
'''
t=t.replace("  cdp('Emulation.setDeviceMetricsOverride',{'width':794",extra+"\n  cdp('Emulation.setDeviceMetricsOverride',{'width':794")
exec(compile(t,str(p/'review_library_browser.py'),'exec'))
