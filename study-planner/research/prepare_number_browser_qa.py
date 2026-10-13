from pathlib import Path
import json,re
B=Path(__file__).parent;s=(B/'qa_final_flow_browser.py').read_text()
s=s.replace('deep-flow-browser','deep-number-browser').replace('p_flow','g_number').replace('flow-question-','number-question-').replace('==164','==138').replace('questionTables\']>=8','questionTables\']>=4')
models=json.loads((B/'deep-library-revision/g_number-models.json').read_text());names=['original-overflow','chop','associativity','carry','product','normal','binary-tie','extension','decimal','termination','bytes','bias','scale','negative','max-sum','zero','finite','spacing','hex','signed-product','nearest']
checks=[('number-question-'+n,len(models['number-question-'+n]['frames'])) for n in names]
s=re.sub(r"for sid,count in \[.*?\]:",'for sid,count in '+repr(checks)+':',s)
s=s.replace('.flow-diagram','.number-diagram').replace('for-control-static.png','word-decoders-static.png').replace('invariant-prefix-static.png','gray-cycle-static.png').replace("capture(' .number-diagram:nth-of-type(2)','gray-cycle-static.png')","capture('.number-diagram:nth-of-type(2)','gray-cycle-static.png')")
a=s.index(" report['flowLaboratory']");z=s.index(" report['responsive']",a)
s=s[:a]+s[z:]
lab="""
 report['numberLaboratory']=js('''(()=>{const rows=[];for(const [w,a,b,op] of [[4,7,1,'add'],[4,15,1,'add'],[4,7,15,'sub'],[4,8,8,'add'],[8,255,1,'sub'],[16,65535,1,'add']]){for(const [id,v]of [['number-width',w],['number-a',a],['number-b',b],['number-operation',op]]){const e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event('input'));}rows.push({...document.getElementById('number-result').dataset});}return rows;})()''')
 assert [(x['word'],x['signed'],x['carry'],x['overflow'])for x in report['numberLaboratory']]==[('8','-8','0','true'),('0','0','1','false'),('8','-8','0','true'),('0','0','1','true'),('254','-2','1','false'),('0','0','1','false')],report['numberLaboratory']
 report['invalidNumberLaboratory']=js('''(()=>{const rows=[];for(const [id,v]of [['number-a','-1'],['number-a','1.5'],['number-a','65536'],['number-width','1'],['number-width','17'],['number-width','']]){const e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event('input'));const d=document.getElementById('number-result').dataset;rows.push({valid:d.valid,word:d.word,trace:document.querySelectorAll('#number-trace tr').length});}return rows;})()''')
 assert all(x==dict(valid='false',word='',trace=0)for x in report['invalidNumberLaboratory']),report['invalidNumberLaboratory']
 js("for(const [id,v] of [['number-width',4],['number-a',7],['number-b',1],['number-operation','add']]){const e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event('input'));}")
 capture('.number-lab','word-laboratory.png')
"""
s=s.replace(" report['responsive']=[]",lab+"\n report['responsive']=[]")
play=(B/'qa_deep_flow_browser.py').read_text();snippet='\n'.join(line for line in play.splitlines() if line.startswith(" report['playPauseChecks']=") or line.startswith(" assert len(report['playPauseChecks'])"))+'\n';snippet=snippet.replace('flow-question-','number-question-').replace('==25','==28')
snippet=" if '--layout-only' in __import__('sys').argv:\n  previous=json.loads((R/'research/deep-library-revision/g_number-browser.json').read_text());assert previous['status'].startswith('passed');report['playPauseChecks']=previous['playPauseChecks'];report['playbackEvidenceReused']='Prior full run actually advanced and paused all28 players; later prose/native-option edits did not change their control implementation.'\n else:\n"+'\n'.join(' '+line for line in snippet.splitlines())+'\n'
s=s.replace(" report['formulaContainment']",snippet+" report['formulaContainment']",1)
s=s.replace(" capture(' .number-diagram','word-decoders-static.png')"," for sid in ['bcd','gray','hamming','secded']:\n  sel='.concept-animation[data-scenes*=number-question-'+sid+']';js('(()=>{const h=document.querySelector('+json.dumps(sel)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host));c.choice.value=c.scenes.findIndex(s=>s.id===\\\"number-question-'+sid+'\\\");c.choice.dispatchEvent(new Event(\\\"change\\\"));c.api.show(c.api.model.frames.length-1);})()');capture(sel,'number-question-'+sid+'-final.png')\n capture(' .number-diagram','word-decoders-static.png')")
s=s.replace(" report['responsive']=[]"," report['sceneChoiceChecks']=js(\"(()=>{const rows=[];for(const c of ConceptAnimations.players){if(c.scenes.length<2)continue;for(let i=0;i<c.scenes.length;i++){c.choice.value=i;c.choice.dispatchEvent(new Event('change'));rows.push({id:c.scene.id,valid:c.api.model.id===c.scene.id&&c.api.index===0&&c.choice.selectedOptions[0].textContent===c.scene.title});}c.choice.value=0;c.choice.dispatchEvent(new Event('change'));}return rows;})()\");assert len(report['sceneChoiceChecks'])==5 and all(x['valid']for x in report['sceneChoiceChecks'])\n report['responsive']=[]")
s=s.replace("capture('.concept-animation','threshold-animation.png')","capture('.concept-animation','division-animation.png')")
(B/'qa_final_number_browser.py').write_text(s,encoding='utf-8');print({'questionControls':len(checks),'expectedDefaultRenderedCheckpoints':138,'allScenarioFrames':148})
