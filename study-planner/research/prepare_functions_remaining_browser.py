"""Retain actual control evidence and complete the corrected UI selector audit."""
from pathlib import Path
import json
B=Path(__file__).parent;E=B/'deep-library-revision';raw=(E/'d_functions-browser.json').read_bytes();d=json.loads(raw)
assert len(d['controls'])==len(d['playback'])==46 and all(all(v['checks'])for v in d['controls'])and all(v['advanced']and v['paused']for v in d['playback'])
assert len(d['frameRendering'])==758 and all(not v['issues']for v in d['frameRendering'])
(E/'d_functions-browser-controls-before-lab-selector-fix.json').write_bytes(raw)
s=(B/'qa_final_functions_browser.py').read_text();a=s.index(" report['counts']=");z=s.index(" report['controls']=");tail=s.index(' for n in[1,2')
middle=" report=json.loads((R/'research/deep-library-revision/d_functions-browser-controls-before-lab-selector-fix.json').read_text())\n report['incrementalRecheck']='The preceding run actually passed all 46 player controls and play/pause checks. It then selected an unavailable laboratory size in the QA script, after those checks. This run uses the observed options 3,4,5. Model teaching text gained explicit why and before/after fields; all 758 rendered frames, screenshots, laboratory, responsive and print checks are freshly repeated. Scientific assignments and actual control behavior are unchanged.'\n"
(B/'qa_remaining_functions_browser.py').write_text(s[:a]+middle+s[a:z]+s[tail:],encoding='utf-8')
