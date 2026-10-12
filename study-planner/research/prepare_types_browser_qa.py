from pathlib import Path
import json
B=Path(__file__).parent;s=(B/'qa_deep_matrices_browser.py').read_text().replace('l_matrices','p_types').replace('deep-matrices-browser','deep-types-browser')
s=s.replace("['questions']==47","['questions']==45").replace("['solutions']==47","['solutions']==45").replace("['questionTables']>=4","['questionTables']>=3")
s=s.replace(".startsWith('matrices-question-')",".startsWith('types-question-')").replace("len(report['labelFormulaSeparation'])>=60","len(report['labelFormulaSeparation'])==108").replace("len(report['formulaContainment'])>=80","len(report['formulaContainment'])==108").replace("len(report['playPauseChecks'])==16","len(report['playPauseChecks'])==26")
a=s.index(' for sid,count in ');b=s.index(':',a);models=json.loads((B/'deep-library-revision/p_types-models.json').read_text());s=s[:a]+' for sid,count in '+repr([(k,v['frames']) for k,v in models.items()])+s[b:]
s=s.replace('.matrix-figure svg','.type-diagram svg').replace('.matrix-figure',' .type-diagram').replace('matrix-product-static.png','typed-pipeline-static.png').replace('matrix-composition-static.png','expression-trees-static.png')
s=s.replace('[1,2,3,4,5,9,13,17,22,29,33,38,39,41,42,43,44,45,46,47]','[1,2,3,4,5,6,7,8,9,10,11,20,24,28,32,36,40,44,45]')
a=s.index(" report['compositionLaboratory']");b=s.index(" report['responsive']=[]",a)
extra=''' report['typedLaboratory']=js("""(()=>{const rows=[];for(const [mode,a,b]of [['store',255,1],['compare',-1,1],['divide',-16,3],['divide',-2147483648,-1],['divide',1,0],['guard',1,0],['guard',-2147483648,-1],['cast',7,3],['store',256,1]]){for(const [id,v]of [['type-case',mode],['type-a',a],['type-b',b]]){const e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event('input'));}const e=document.querySelector('#type-result');rows.push({mode,a,b,valid:e.dataset.valid,value:e.dataset.value,text:e.textContent});}return rows;})()""")
 assert [(x['valid'],x['value'])for x in report['typedLaboratory']]==[('true','0'),('true','0'),('true','-5'),('false',''),('false',''),('true','0'),('false',''),('true','2'),('false','')],report['typedLaboratory']
 capture('.types-lab','typed-laboratory.png')
'''
s=s[:a]+extra+s[b:];s=s.replace('matrix-question-mobile.png','typed-question-mobile.png')
(B/'qa_deep_types_browser.py').write_text(s,encoding='utf-8')
