from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_deep_asym_browser.py').read_text().replace('a_asym','s_axioms').replace('deep-asym-browser','deep-axioms-browser')
s=s.replace("[('asym-parity-ratio',16),('asym-log-oscillation',8),('asym-floor-ratio',10)]","[('axioms-question-atoms39',6),('axioms-question-atoms47',7),('axioms-question-urn',4),('axioms-question-report',4),('axioms-question-collision',3)]")
s=s.replace("['questions']==46","['questions']==48").replace("['solutions']==46","['solutions']==48").replace("['questionTables']==7","['questionTables']==13")
s=s.replace("capture('.logic-diagram','ratio-envelopes.png')", "capture('.logic-diagram','reporting-map.png')").replace(" capture('.logic-diagram:nth-of-type(2)','strict-hierarchy.png')",'')
s=s.replace('[1,2,3,4,7,10,12,16,45,46]','[1,2,3,4,6,11,31,38,39,41,43,45,47,48]')
s=s.replace("capture('.question-specific-animation','threshold-mobile.png')","capture('.question-specific-animation[data-scenes=\"axioms-question-atoms39\"]','atoms-mobile.png')")
s=s.replace("if(profile/'DevToolsActivePort').exists():break", "if(profile/'DevToolsActivePort').exists():\n   try:\n    port_text=(profile/'DevToolsActivePort').read_text();assert port_text.strip();break\n   except (OSError,AssertionError):pass")
s=s.replace("port=int((profile/'DevToolsActivePort').read_text().splitlines()[0])","port=int(port_text.splitlines()[0])")
s=s.replace('c.api.show(2);','c.api.show(1);').replace('w.dataset.displayedFrame==="1"','w.dataset.displayedFrame==="0"').replace('checks.push(c.api.index===2)','checks.push(c.api.index===1)').replace('checks.push(c.api.index===3)','checks.push(c.api.index===2)')
s=s.replace("capture('.logic-diagram','reporting-map.png')", "capture('.logic-diagram','reporting-map.png')\n capture('.exam-figure','four-atomic-masses.png')")
s=s.replace("document.querySelectorAll('.logic-diagram svg')", "document.querySelectorAll('.logic-diagram svg,svg.lesson-diagram')")
s=s.replace("capture('.exam-figure','four-atomic-masses.png')", "capture('.exam-figure','four-atomic-masses.png')\n capture('svg.lesson-diagram','uniform-area.png')")
needle=" capture('.concept-animation','threshold-animation.png')"
extra=''' report['labelFormulaSeparation']=js("""(()=>{const rows=[];for(const c of ConceptAnimations.players){if(!c.api.model.id.startsWith('axioms-question-'))continue;for(let i=0;i<c.api.model.frames.length;i++){c.api.show(i);const svg=c.api.host.querySelector('svg'),bad=[];for(const t of svg.querySelectorAll('text'))for(const m of svg.querySelectorAll('foreignObject math')){const a=t.getBoundingClientRect(),b=m.getBoundingClientRect();if(Math.min(a.right,b.right)-Math.max(a.left,b.left)>1&&Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top)>1)bad.push(t.textContent);}rows.push({id:c.api.model.id,frame:i,height:svg.viewBox.baseVal.height,overlaps:bad});}}return rows;})()""")
 assert len(report['labelFormulaSeparation'])==24 and all(not x['overlaps'] and x['height']<=362 for x in report['labelFormulaSeparation']),report['labelFormulaSeparation']
'''
assert needle in s;s=s.replace(needle,extra+needle,1)
(B/'qa_deep_axioms_browser.py').write_text(s)
