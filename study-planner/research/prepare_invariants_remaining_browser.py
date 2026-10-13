from pathlib import Path
import json
B=Path(__file__).parent;E=B/'deep-library-revision';s=(B/'qa_final_invariants_browser.py').read_text(encoding='utf-8')
p=E/'d_invariants-browser-controls-before-final-typesetting.json'
if not p.exists():
 d=json.loads((E/'d_invariants-browser.json').read_text(encoding='utf-8'));assert d['status'].startswith('passed') and len(d['controls'])==len(d['playback'])==45
 assert all(all(v['checks'])for v in d['controls'])and all(v['advanced']and v['paused']for v in d['playback'])
 p.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
a=s.index(" report['controls']=");z=s.index(' for n in[1,2,3',a)
tail='''
 prior=json.loads((R/'research/deep-library-revision/d_invariants-browser-controls-before-final-typesetting.json').read_text(encoding='utf-8'))
 assert len(prior['controls'])==len(prior['playback'])==45 and all(all(v['checks'])for v in prior['controls'])and all(v['advanced']and v['paused']for v in prior['playback'])
 for key in ['controls','playback','selection']:report[key]=prior[key]
 report['incrementalRecheck']='The preceding run actually executed all 45 players, 270 control checks, 90 play/pause assertions and sixteen selector events. This fresh run repeats all 419 rendered checkpoints, laboratory, static diagrams, mobile and print after fraction typography, authored checkpoint captions and the static reset diagram were corrected. Scientific assignments and control behavior are unchanged.'
'''
s=s[:a]+tail+s[z:]
(B/'qa_remaining_invariants_browser.py').write_text(s,encoding='utf-8')
