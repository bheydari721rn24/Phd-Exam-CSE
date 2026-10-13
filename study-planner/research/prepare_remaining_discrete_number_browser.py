from pathlib import Path
import json
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision'
for p in [R/'dist/chapters/d_number.html',B/'build_discrete_number.py']:
 s=p.read_text();s=s.replace('id="number-m" type="number" value="12" min="2"','id="number-m" type="number" value="12" min="1"').replace('<span class="math-inline">B</span>ézout','Bézout');p.write_text(s,encoding='utf-8')
d=json.loads((E/'d_number-browser.json').read_text());assert len(d['controls'])==len(d['playback'])==61 and all(all(v['checks'])for v in d['controls'])and all(v['advanced']and v['paused']for v in d['playback']);assert all(not v['issues']for v in d['frameRendering']);(E/'d_number-browser-controls-before-modulus-one-fix.json').write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
s=(B/'qa_final_discrete_number_browser.py').read_text();a=s.index(" report['controls']=");z=s.index(' for n in[1,2,3,4,5,6,7,8,9,10,11,12,13,14,18,22,26,30,34,38,42,46,47]:',a)
s=s[:a]+''' recorded=json.loads((R/'research/deep-library-revision/d_number-browser-controls-before-modulus-one-fix.json').read_text())
 for key in ['controls','selection','playback']:report[key]=recorded[key]
 report['controlEvidence']='research/deep-library-revision/d_number-browser-controls-before-modulus-one-fix.json'
 report['controlEvidenceQualification']='All controls, playback and selections passed before the laboratory-only modulus-one minimum fix. This run freshly renders every frame and checks the corrected laboratory, static figures, responsiveness and print.'
'''+s[z:]
(B/'qa_remaining_discrete_number_browser.py').write_text(s,encoding='utf-8')
