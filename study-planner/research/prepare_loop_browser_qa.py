from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_deep_asym_browser.py').read_text().replace('a_asym','a_loop').replace('deep-asym-browser','deep-loop-browser')
s=s.replace("[('asym-parity-ratio',16),('asym-log-oscillation',8),('asym-floor-ratio',10)]","[('model-merge-exact',23),('loop-question-parity',8),('loop-question-minimum',8),('loop-question-product',8)]")
s=s.replace('ratio-envelopes.png','strict-triangle.png').replace('strict-hierarchy.png','exact-schedules.png').replace('threshold-animation.png','triangular-animation.png').replace('[1,2,3,4,7,10,12,16,45,46]','[1,2,3,4,8,9,10,11,32,45,46]')
s=s.replace("capture('.question-specific-animation','parity-mobile.png')", "capture('.question-specific-animation[data-scenes=\"loop-question-parity\"]','parity-mobile.png')")
needle=" capture('.concept-animation','triangular-animation.png')"
extra=''' report['gridAlignment']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){if(!['loop-question-parity','loop-question-product'].includes(c.api.model.id))continue;for(let i=0;i<c.api.model.frames.length;i++){c.api.show(i);const svg=c.api.host.querySelector('svg'),v=svg.viewBox.baseVal;const labels=[...svg.querySelectorAll('text')].filter(t=>/^\\d+$/.test(t.textContent)&&t.getBBox().y>290);rows.push({id:c.api.model.id,frame:i,height:v.height,columnLabels:labels.length,spread:labels.length?Math.max(...labels.map(t=>t.getBBox().y))-Math.min(...labels.map(t=>t.getBBox().y)):999});}}return rows;})()""")
 assert len(report['gridAlignment'])==16 and all(x['height']<=362 and x['columnLabels']==8 and x['spread']<.1 for x in report['gridAlignment']),report['gridAlignment']
'''
assert needle in s;s=s.replace(needle,extra+needle,1)
(B/'qa_deep_loop_browser.py').write_text(s)
