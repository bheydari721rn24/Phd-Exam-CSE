"""Reuse proven figure/font layout auditing, restricted to the new chapter."""
from pathlib import Path
p=Path(__file__).resolve().parent
t=(p/'review_library_browser.py').read_text(encoding='utf-8')
t=t.replace("OUT=Path(tempfile.gettempdir())/'chapter-library-review'","OUT=Path(tempfile.gettempdir())/'d-relations-browser'")
t=t.replace("topics=[c['topicId'] for w in json.loads((ROOT/'dist/lessons.json').read_text()) for c in w['chapters']]","topics=['d_relations']")
t=t.replace("if topic in ('d_logic','a_loop','l_matrices','g_gates'):","if topic == 'd_relations':")
t=t.replace("target={'d_logic':'figure','a_loop':'pre','l_matrices':'.formula-block','g_gates':'figure'}[topic]","target='.formula-block'")
t=t.replace("if topic in ('d_induction','g_number','g_gates'):","if topic == 'd_relations':")
# Check the live staged controls against the proven pure-function output.
needle="  row={'topicId':topic,'figures':[]}"
extra='''
  assert js("document.querySelectorAll('#lab-input button').length") == 16
  js("document.getElementById('lab-cycle').click()")
  for _ in range(4):js("document.getElementById('lab-next').click()")
  assert js("document.getElementById('lab-next').disabled") is True
  assert 'Stage 4 of 4' in js("document.getElementById('lab-stage').textContent")
  final=json.loads(js("JSON.stringify([...document.querySelectorAll('#lab-stage-matrix tbody tr')].map(r=>[...r.querySelectorAll('td')].map(x=>Number(x.textContent))))"))
  assert final==[[1,1,1,0],[1,1,1,0],[1,1,1,0],[0,0,0,0]],final
  js("document.querySelector('#lab-input button[data-row=\"3\"][data-col=\"3\"]').click()")
  assert 'Stage 0 of 4' in js("document.getElementById('lab-stage').textContent")
  js("document.getElementById('lab-chain').click()")
'''
# Use an unambiguous selector for the edited pair.
extra=extra.replace('js("document.querySelector(\'#lab-input button[data-row="3"][data-col="3"]\').click()")', 'js("document.querySelectorAll(\'#lab-input button\')[15].click()")')
t=t.replace(needle,extra+'\n'+needle)
needle="  cdp('Emulation.setDeviceMetricsOverride',{'width':794"
extra='''
  assert all('STIX Two Math' in f for f in row['fonts']['math']),row['fonts']
  assert any('JetBrains Mono' in f for f in row['mobile']['codeFonts']),row['mobile']['codeFonts']
  for target,name in [('math','d_relations-mobile-mathml.png'),('#relation-lab','d_relations-mobile-lab.png')]:
   js("document.querySelector("+json.dumps(target)+").scrollIntoView({block:'start'})")
   shot=cdp('Page.captureScreenshot',{'format':'png'})['data']
   (OUT/name).write_bytes(base64.b64decode(shot))
'''
t=t.replace(needle,extra+'\n'+needle)
exec(compile(t,str(p/'review_library_browser.py'),'exec'))
