"""Inspect the new chapter's exact local rendering and exercise its UI controls."""
from pathlib import Path
p=Path(__file__).resolve().parent;t=(p/'review_library_browser.py').read_text(encoding='utf-8')
t=t.replace("OUT=Path(tempfile.gettempdir())/'chapter-library-review'","OUT=Path(tempfile.gettempdir())/'d-functions-browser'")
t=t.replace("topics=[c['topicId'] for w in json.loads((ROOT/'dist/lessons.json').read_text()) for c in w['chapters']]","topics=['d_functions']")
t=t.replace("if topic in ('d_logic','a_loop','l_matrices','g_gates'):","if topic=='d_functions':")
t=t.replace("target={'d_logic':'figure','a_loop':'pre','l_matrices':'.formula-block','g_gates':'figure'}[topic]","target='math'")
t=t.replace("if topic in ('d_induction','g_number','g_gates'):","if topic=='d_functions':")
extra='''
  assert 'Neither' in js("document.getElementById('function-output').textContent")
  assert '{0, 2}' in js("document.getElementById('function-output').textContent")
  js("document.getElementById('preset-bijection').click()")
  assert 'Bijective' in js("document.getElementById('function-output').textContent")
  assert 'No true inverse' not in js("document.getElementById('function-output').textContent")
  js("document.getElementById('preset-injection').click()")
  assert 'Injective; not onto' in js("document.getElementById('function-output').textContent")
  js("document.getElementById('preset-onto').click()")
  assert 'Onto; not injective' in js("document.getElementById('function-output').textContent")
  js("document.querySelector('[data-select=\\\"3\\\"]').click()")
  assert 'S = {0, 3}' in js("document.getElementById('function-output').textContent")
  js("document.querySelector('[data-input=\\\"2\\\"]').value='0';document.querySelector('[data-input=\\\"2\\\"]').dispatchEvent(new Event('change'))")
  assert 'Neither' in js("document.getElementById('function-output').textContent")
'''
t=t.replace("  row={'topicId':topic,'figures':[]}",extra+"\n  row={'topicId':topic,'figures':[]}")
extra='''
  assert all('STIX Two Math' in f for f in row['fonts']['math']),row['fonts']
  assert any('JetBrains Mono' in f for f in row['mobile']['codeFonts']),row['mobile']
  js("document.getElementById('function-lab').scrollIntoView({block:'start'})")
  shot=cdp('Page.captureScreenshot',{'format':'png'})['data']
  (OUT/'d_functions-mobile-lab.png').write_bytes(base64.b64decode(shot))
'''
t=t.replace("  cdp('Emulation.setDeviceMetricsOverride',{'width':794",extra+"\n  cdp('Emulation.setDeviceMetricsOverride',{'width':794")
exec(compile(t,str(p/'review_library_browser.py'),'exec'))
