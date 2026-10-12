from pathlib import Path
import json
B=Path(__file__).parent;s=(B/'qa_deep_types_browser.py').read_text().replace('p_types','p_flow').replace('deep-types-browser','deep-flow-browser')
s=s.replace("['questionTables']>=3","['questionTables']>=8").replace(".startsWith('types-question-')",".startsWith('flow-question-')").replace("len(report['labelFormulaSeparation'])==108","len(report['labelFormulaSeparation'])==164").replace("len(report['formulaContainment'])==108","len(report['formulaContainment'])==164").replace("len(report['playPauseChecks'])==26","len(report['playPauseChecks'])==25")
a=s.index(' for sid,count in ');b=s.index(':',a);models=json.loads((B/'deep-library-revision/p_flow-models.json').read_text());s=s[:a]+' for sid,count in '+repr([(k,v['frames']) for k,v in models.items()])+s[b:]
s=s.replace('.type-diagram','.flow-diagram').replace('typed-pipeline-static.png','for-control-static.png').replace('expression-trees-static.png','invariant-prefix-static.png').replace('typed-question-mobile.png','flow-question-mobile.png')
a=s.index(" report['typedLaboratory']");b=s.index(" report['responsive']=[]",a)
extra=''' report['flowLaboratory']=js("""(()=>{const rows=[];for(const [mode,limit,start]of [['for',5,0],['while',5,0],['do',0,0],['bug',5,0],['break',5,0],['for',0,0],['do',5,12],['while',5,12],['bug',5,1]]){for(const [id,v]of [['flow-case',mode],['flow-limit',limit],['flow-start',start]]){const e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event('input'));}document.querySelector('#flow-end').click();const d=document.querySelector('#flow-state').dataset;rows.push({mode,limit,start,status:d.status,i:Number(d.i),sum:Number(d.sum),tests:Number(d.tests),entries:Number(d.entries),updates:Number(d.updates)});}return rows;})()""")
 assert [(x['status'],x['i'],x['sum'])for x in report['flowLaboratory']]==[('normal',5,4),('normal',5,10),('normal',1,0),('cycle',0,0),('break',3,3),('normal',0,0),('normal',13,12),('normal',12,0),('cycle',2,1)],report['flowLaboratory']
 assert [(x['tests'],x['entries'],x['updates'])for x in report['flowLaboratory'][:5]]==[(6,5,5),(6,5,5),(1,1,1),(1,1,0),(4,4,3)]
 capture('.flow-lab','execution-laboratory.png')
'''
s=s[:a]+extra+s[b:];s=s.replace('print(json.dumps(report,indent=2))',"print(report['status'])")
(B/'qa_deep_flow_browser.py').write_text(s,encoding='utf-8')
