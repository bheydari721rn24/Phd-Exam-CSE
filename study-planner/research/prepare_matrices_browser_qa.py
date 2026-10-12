from pathlib import Path
B=Path(__file__).parent;s=(B/'qa_deep_vectors_browser.py').read_text().replace('l_vectors','l_matrices').replace('deep-vectors-browser','deep-matrices-browser')
s=s.replace("['questions']==46","['questions']==47").replace("['solutions']==46","['solutions']==47").replace("['questionTables']==6","['questionTables']>=4")
s=s.replace(".startsWith('vectors-question-')",".startsWith('matrices-question-')")
s=s.replace("len(report['labelFormulaSeparation'])==43","len(report['labelFormulaSeparation'])>=60").replace("len(report['formulaContainment'])==91","len(report['formulaContainment'])>=80").replace("len(report['playPauseChecks'])==7","len(report['playPauseChecks'])==16")
a=s.index(' for sid,count in ');b=s.index(':',a);names=[('source',4),('allones',4),('shear',3),('fixed',6),('power',6),('rank',4),('basis',4),('block',4),('gram',4),('positivity3',5),('positivity4',5),('trace',3),('blockidentity',4),('power10',11)]
s=s[:a]+' for sid,count in '+repr([('matrices-question-'+name,n) for name,n in names])+s[b:]
s=s.replace(".logic-diagram svg,svg.lesson-diagram",".matrix-figure svg")
a=s.index(" capture('.logic-diagram'");b=s.index(' for n in[',a);s=s[:a]+" capture('.matrix-figure','matrix-product-static.png')\n capture('.matrix-figure:nth-of-type(2)','matrix-composition-static.png')\n"+s[b:]
s=s.replace('[1,2,3,4,8,12,17,22,28,32,37,38,41,42,45,46]','[1,2,3,4,5,9,13,17,22,29,33,38,39,41,42,43,44,45,46,47]')
a=s.index(" report['projectionLaboratory']");b=s.index(" report['responsive']=[]",a)
extra=''' report['compositionLaboratory']=js("""(()=>{const rows=[];for(const values of [[0,100,100,100],[90,0,100,100],[180,100,100,100],[90,100,100,100],[45,-200,-150,150],[90,100,0,0]]){for(const [id,v] of ['angle','shear','x','y'].map((id,i)=>[id,values[i]])){const e=document.getElementById('matrix-'+id);e.value=v;e.dispatchEvent(new Event('input'));}const d=document.querySelector('#matrix-result').dataset;rows.push({values,commute:d.commute,gap:Number(d.gap),first:JSON.parse(d.first),second:JSON.parse(d.second)});}return rows;})()""")
 assert all(abs(sum((a-b)**2 for a,b in zip(r['first'],r['second']))-r['gap'])<1e-9 for r in report['compositionLaboratory'])
 assert [r['commute'] for r in report['compositionLaboratory']]==['true','true','true','false','false','false'] and report['compositionLaboratory'][-1]['gap']==0
 capture('.matrix-lab','composition-laboratory.png')
'''
s=s[:a]+extra+s[b:]
s=s.replace("capture('.question-specific-animation','parity-mobile.png')","capture('.question-specific-animation','matrix-question-mobile.png')")
(B/'qa_deep_matrices_browser.py').write_text(s)
