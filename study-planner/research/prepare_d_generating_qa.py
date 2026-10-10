from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_d_recurrence_browser.py').read_text(encoding='utf-8').replace('d_recurrence','d_generating').replace('d-recurrence','d-generating').replace('RecurrencePlayers','GeneratingPlayers').replace('RecurrenceLab','GeneratingLab').replace('rc-','gf-').replace('==83','==82').replace('>14','>12').replace('==50','==51')
start=s.index(" for id,step,name in ");end=s.index(" capture('.hero'",start)
s=s[:start]+" for id,step,name in [('convolution-five',5,'convolution.png'),('durfee-seven',8,'durfee.png'),('catalan-four',5,'catalan.png'),('label-five',15,'labels.png'),('binary-six',31,'marking.png'),('three-boxes',3,'bounds.png'),('triple-pole',7,'pole.png')]:\n  js('GeneratingPlayers.find(p=>p.model.id==='+json.dumps(id)+').show('+str(step)+')');capture('[data-gf-model=\"'+id+'\"]',name)\n"+s[end:]
s=s.replace('all-domino-eight','catalan-four').replace('ternary-forbidden','convolution-five').replace('d_generating_original_34','d_generating_original_47')
start=s.index(" for spec in ");end=s.index(" cdp('Emulation.setDeviceMetricsOverride',dict(width=390",start)
s=s[:start]+''' for op,n in [('inverse',10),('convolution',6),('filter',10),('bounded',9),('coins',10),('composition',7),('partitions',10),('durfee',7),('catalan',4),('labelled',6),('marking',6),('poles',10)]:
  spec=dict(operation=op,n=n)
  obj=js('(()=>{const f=document.querySelector("#gf-form"),spec='+json.dumps(spec)+';for(const[k,v]of Object.entries(spec))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));const bad=[];for(let i=0;i<GeneratingLab.model.frames.length;i++){GeneratingLab.show(i);bad.push(...DiagramLayout.audit(GeneratingLab.host.querySelector("svg")));}return {operation:spec.operation,error:document.querySelector("#gf-error").textContent,result:GeneratingLab.model.result,issues:bad};})()');assert not obj['error']and not obj['issues'],obj;report['labs'].append(obj)
 for change in [dict(n=0),dict(n=11),dict(n=2.5),dict(operation='convolution',n=7),dict(operation='composition',n=8),dict(operation='catalan',n=5),dict(operation='labelled',n=7),dict(operation='bounded',n=10),dict(operation='durfee',n=8)]:
  js('(()=>{window.oldLab=GeneratingLab;const f=document.querySelector("#gf-form"),base={operation:"inverse",n:5},change='+json.dumps(change)+';for(const[k,v]of Object.entries({...base,...change}))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('GeneratingLab===oldLab && document.querySelector("#gf-error").textContent.length>0')
 report['invalidPreservesPrevious']=9
''' +s[end:]
(B/'qa_d_generating_browser.py').write_text(s,encoding='utf-8')
