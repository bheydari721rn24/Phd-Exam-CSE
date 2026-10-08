from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_l_spaces_browser.py').read_text(encoding='utf-8').replace('l_spaces','i_agents').replace('l-spaces','i-agents').replace('VectorSpacePlayers','AgentPlayers').replace('VectorSpaceLab','AgentLab').replace('vs-','ag-').replace('data-vs','data-ag')
a=s.index(' for id,step,name in [');b=s.index(" js('window.p=",a)
s=s[:a]+''' for id,step,name in [('loop-main',2,'loop.png'),('voi-main',2,'information-tree.png'),('vacuum-main',2,'vacuum.png'),('alias-main',1,'aliasing.png'),('sensorless-main',3,'sensorless.png'),('key-main',1,'key.png'),('graph-main',2,'state-node.png'),('takeaway-main',4,'takeaway.png')]:
  js('AgentPlayers.find(p=>p.model.id==='+json.dumps(id)+').show('+str(step)+')');capture('[data-ag-model="'+id+'"]',name)
 capture('.hero','title.png');capture('[data-source-id="i-agents-original-80"]','synthesis-question.png');capture('.review-rule','final-rule.png')
''' +s[b:]
s=s.replace('parameter-span','threshold-main').replace('pivot-main','vacuum-main')
a=s.index(" report['labs']=[]");b=s.index(" cdp('Emulation.setDeviceMetricsOverride',dict(width=390",a)
s=s[:a]+''' report['labs']=[]
 for p,h,l,u,c in [('3/10','4/5','1/5','12,-4;5,5','1/4'),('1/2','1','0','12,-4;5,5','0'),('1/2','1/2','1/2','12,-4;5,5','0'),('0','1','0','12,-4;5,5','0'),('1','1','1','12,-4;5,5','0'),('1/4','4/5','1/5','-7,-3;-2,-8','1'),('9999/10000','7777/10000','3333/10000','10000,-10000;-9999,9999','9999/10000')]:
  obj=js('(()=>{const f=document.querySelector("#ag-form");f.elements.prior.value='+json.dumps(p)+';f.elements.lh.value='+json.dumps(h)+';f.elements.ll.value='+json.dumps(l)+';f.elements.utilities.value='+json.dumps(u)+';f.elements.cost.value='+json.dumps(c)+';f.dispatchEvent(new Event("submit",{cancelable:true}));const bad=[];for(let i=0;i<AgentLab.model.frames.length;i++){AgentLab.show(i);bad.push(...DiagramLayout.audit(AgentLab.host.querySelector("svg")));}return {error:document.querySelector("#ag-error").textContent,result:AgentLab.model.result,issues:bad};})()');assert not obj['error']and not obj['issues']and all(obj['result']['checks'].values()),obj;report['labs'].append(obj)
 capture('#ag-output .ag-stage','exact-rational-lab.png')
 for field,value in [('prior','2'),('prior','-1/4'),('lh','1/0'),('ll','abc'),('utilities','1,2,3;4,5'),('cost','-1'),('prior','10001/10000'),('utilities','1.5,2;3,4')]:
  js('(()=>{window.oldLab=AgentLab;const f=document.querySelector("#ag-form");f.elements.prior.value="3/10";f.elements.lh.value="4/5";f.elements.ll.value="1/5";f.elements.utilities.value="12,-4;5,5";f.elements.cost.value="1/4";f.elements['+json.dumps(field)+'].value='+json.dumps(value)+';f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('AgentLab===oldLab && document.querySelector("#ag-error").textContent.length>0')
 report['invalidPreservesPrevious']=8
''' +s[b:]
s=s.replace("==43 and report['library']","==44 and report['library']").replace('mobile-cofactor.png','mobile-vacuum.png').replace('print-area.png','print-threshold.png')
(B/'qa_i_agents_browser.py').write_text(s,encoding='utf-8')
print('Built full-frame geometry, font, interaction, rational-lab, print, mobile and library checks.')
