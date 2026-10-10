from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_g_arithmetic_browser.py').read_text(encoding='utf-8').replace('g_arithmetic','g_mux').replace('g-arithmetic','g-mux').replace('ArithmeticPlayers','MuxPlayers').replace('ArithmeticLab','MuxLab').replace('.ar-','.mx-').replace('#ar-','#mx-').replace('data-ar-','data-mx-')
s=s.replace("report['counts']['players']>15","report['counts']['players']>17")
start=s.index(" for id,step,name in");end=s.index(" capture('.hero'",start)
s=s[:start]+" for id,step,name in [('decoder-gates',2,'decoder-gates.png'),('authentic-nor',2,'cascade.png'),('tree-eight',3,'tree.png'),('two-banks',2,'banks.png'),('priority-high',3,'priority.png'),('display-two',2,'display.png'),('adder-selector',3,'integrated.png')]:\n  js('MuxPlayers.find(p=>p.model.id==='+json.dumps(id)+').show('+str(step)+')');capture('[data-mx-model=\"'+id+'\"]',name)\n"+s[end:]
s=s.replace('g_mux_original_80','g_mux_original_80').replace('prefix-chain','tree-eight').replace('full-basic','mux-basic')
start=s.index(" report['labs']=[]");end=s.index(" cdp('Emulation.setDeviceMetricsOverride',dict(width=390",start)
s=s[:start]+''' report['labs']=[]
 for spec in [dict(operation='mux',n=2,address=3,data='1,0,1,0'),dict(operation='tree',n=3,address=5,data='7,3,9,2,4,11,6,8'),dict(operation='decoder',n=2,address=2,enable=0,polarity='low'),dict(operation='priority',n=3,requests=90,order='low'),dict(operation='rotate',n=3,requests=137,pointer=6),dict(operation='display',n=4,address=11),dict(operation='integrated',n=2,a=1,b=1,address=3),dict(operation='bus',n=1,address=0,data='0,1',enables='0,0')]:
  obj=js('(()=>{const f=document.querySelector("#mx-form"),base={operation:"mux",n:2,address:0,data:"1,1,0,1",requests:0,residual:0,enable:1,polarity:"high",order:"high",pointer:0,a:0,b:0,enables:"0,0"},spec='+json.dumps(spec)+';for(const[k,v]of Object.entries({...base,...spec}))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));const bad=[];for(let i=0;i<MuxLab.model.frames.length;i++){MuxLab.show(i);bad.push(...DiagramLayout.audit(MuxLab.host.querySelector("svg")));}return {error:document.querySelector("#mx-error").textContent,result:MuxLab.model.result,issues:bad};})()');assert not obj['error']and not obj['issues'],obj;report['labs'].append(obj)
 for change in [dict(n=0),dict(n=5),dict(address=4),dict(data='1,0'),dict(enable=2),dict(requests=16)]:
  js('(()=>{window.oldLab=MuxLab;const f=document.querySelector("#mx-form"),base={operation:"mux",n:2,address:0,data:"1,1,0,1",requests:0,residual:0,enable:1,polarity:"high",order:"high",pointer:0,a:0,b:0,enables:"0,0"},change='+json.dumps(change)+';for(const[k,v]of Object.entries({...base,...change}))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('MuxLab===oldLab && document.querySelector("#mx-error").textContent.length>0')
 report['invalidPreservesPrevious']=6
''' +s[end:]
s=s.replace("report['library']['cards']==48","report['library']['cards']==49")
s=s.replace("report['runtimeErrors']=js('__errors');","assert not js('document.querySelector(\".lesson\").textContent.includes(\"undefined\")');report['runtimeErrors']=js('__errors');")
(B/'qa_g_mux_browser.py').write_text(s,encoding='utf-8')
print('Prepared actual-browser font, diagram, control, lab and retention QA.')
