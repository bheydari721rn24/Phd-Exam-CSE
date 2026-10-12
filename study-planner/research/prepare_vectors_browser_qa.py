from pathlib import Path
B=Path(__file__).parent
s=(B/'qa_deep_counting_browser.py').read_text().replace('s_counting','l_vectors').replace('deep-counting-browser','deep-vectors-browser').replace('counting-question-','vectors-question-')
s=s.replace("['questions']==77","['questions']==46").replace("['solutions']==77","['solutions']==46").replace("['questionTables']==6","['questionTables']==6")
a=s.index(' for sid,count in ');b=s.index(':',a)
s=s[:a]+" for sid,count in [('vectors-question-source',4),('vectors-question-positivity',7),('vectors-question-gram37',6),('vectors-question-gram45',6),('vectors-question-coordinates',4),('vectors-question-minimum',8),('vectors-question-gram-schmidt',8)]"+s[b:]
s=s.replace("len(report['labelFormulaSeparation'])==51","len(report['labelFormulaSeparation'])==43").replace("len(report['formulaContainment'])==51","len(report['formulaContainment'])==91").replace("len(report['playPauseChecks'])==6","len(report['playPauseChecks'])==7")
s=s.replace('.question-specific-animation[data-scenes=','.concept-animation[data-scenes=')
needle=" report['counts']=js("
s=s.replace(needle," report['loadFailures']=js(\"[...document.querySelectorAll('.concept-animation')].filter(h=>h.dataset.loaded!=='true').map(h=>({scenes:h.dataset.scenes,state:h.dataset.loaded,text:h.textContent}))\");assert not report['loadFailures'],report['loadFailures']\n"+needle)
a=s.index(" report['parityLaboratory']");b=s.index(' for n in[',a);s=s[:a]+s[b:]
s=s.replace('[1,3,7,9,16,24,28,32,39,40,52,56,68,71,74,77]','[1,2,3,4,8,12,17,22,28,32,37,38,41,42,45,46]')
s=s.replace("capture('.logic-diagram','reporting-map.png')","capture('.logic-diagram','vector-addition.png')").replace("capture('.logic-diagram:nth-of-type(2)','stars-bars-static.png')","capture('.logic-diagram:nth-of-type(2)','projection-static.png')").replace("capture('.exam-figure','four-atomic-masses.png')","capture('.exam-figure','nonunit-static.png')")
s=s.replace(" capture('.logic-diagram:nth-of-type(2)','projection-static.png')"," capture('.logic-diagram:nth-of-type(2)','projection-static.png')\n capture('.exam-figure','nonunit-static.png')")
s=s.replace("['solutions']==77","['solutions']==46")
# Exact checks of the retained editable geometry laboratory.
needle=" report['responsive']=[]"
extra=''' report['projectionLaboratory']=js("""(()=>{const out=[];for(const [a,l,c] of [[0,100,0],[180,100,100],[90,100,100],[146,200,-100],[60,0,500],[60,200,500]]){for(const [id,v] of [['vector-angle',a],['vector-length',l],['vector-candidate',c]]){const e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event('input'));}const d=document.querySelector('#vector-result').dataset;out.push({angle:a,length:l,candidate:c,valid:d.valid,minimum:Number(d.minimum),actual:Number(d.actual),excess:Number(d.excess),dot:Number(d.orthogonality)});}return out;})()""")
 assert all(abs(x['dot'])<1e-9 and abs(x['minimum']+x['excess']-x['actual'])<1e-9 and (x['valid']=='true')==(x['length']!=0) for x in report['projectionLaboratory']),report['projectionLaboratory']
 report['projectionCandidateVisible']=js("document.querySelector('#vector-result').dataset.candidateVisible==='true'");assert report['projectionCandidateVisible']
 capture('.vector-lab','editable-laboratory.png')
'''
assert needle in s;s=s.replace(needle,extra+needle)
motion=''' report['geometricTransit']=js("""(()=>{const c=ConceptAnimations.players.find(c=>c.api.model.id==='vectors-question-minimum'),a=c.api; a.show(0);a.host.querySelector('[data-next]').click();const seek=a.host.querySelector('.sim-motion-control input');seek.value=50;seek.dispatchEvent(new Event('input'));const point=a.host.querySelector('[data-entity=feasible-candidate] circle'),cx=Number(point.getAttribute('cx')),cy=Number(point.getAttribute('cy'));return {progress:Number(a.host.dataset.transition),cx,cy,expectedX:95+400/12,expectedY:220-70*(3*(1/12-2/3)**2+2/3)};})()""")
 assert abs(report['geometricTransit']['cx']-report['geometricTransit']['expectedX'])<1e-8 and abs(report['geometricTransit']['cy']-report['geometricTransit']['expectedY'])<1e-8 and report['geometricTransit']['progress']==.5,report['geometricTransit']
 capture('.concept-animation[data-scenes="vectors-question-minimum"]','minimum-transit.png')
 cdp('Emulation.setEmulatedMedia',dict(features=[dict(name='prefers-reduced-motion',value='reduce')]))
 report['reducedMotion']=js("""(()=>{const c=ConceptAnimations.players.find(c=>c.api.model.id==='vectors-question-minimum'),a=c.api;a.show(0);a.host.querySelector('[data-next]').click();return {index:a.index,progress:Number(a.host.dataset.transition),disabled:a.host.querySelector('.sim-motion-control input').disabled};})()""")
 assert report['reducedMotion']==dict(index=1,progress=1,disabled=True),report['reducedMotion']
 cdp('Emulation.setEmulatedMedia',dict(features=[]))
'''
s=s.replace(" report['responsive']=[]",motion+" report['responsive']=[]")
(B/'qa_deep_vectors_browser.py').write_text(s)
