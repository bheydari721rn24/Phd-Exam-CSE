from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_l_linear_browser.py').read_text(encoding='utf-8').replace('l_linear','l_orthogonality').replace('l-linear','l-orthogonality').replace('LinearPlayers','OrthogonalityPlayers').replace('LinearLab','OrthogonalityLab').replace('lt-','og-')
s=s.replace('>38','>30').replace('==59','==60')
a=s.index(' for id,name in');b=s.index("\n js('window.p=",a)
s=s[:a]+''' for id,name in [('line','line.png'),('weighted','weighted.png'),('oblique','oblique.png'),('gram','gram.png'),('qr','qr.png'),('polynomial','polynomial.png'),('reflection','reflection.png'),('computed-9','four-dimensional.png')]:
  js('OrthogonalityPlayers.find(p=>p.model.id==='+json.dumps(id)+').show(OrthogonalityPlayers.find(p=>p.model.id==='+json.dumps(id)+').model.frames.length-1)');capture('[data-og-model="'+id+'"]',name)
'''+s[b:]
s=s.replace('id==="rotation"','id==="reflection"').replace('rotating-grid','reflected-vector')
s=s.replace(" report['rotationMotion']"," report['reflectionMotion']").replace("report['rotationMotion']","report['reflectionMotion']")
a=s.index(" report['labs']=[]");b=s.index("\n cdp('Emulation.setDeviceMetricsOverride',dict(width=390",a)
s=s[:a]+''' report['labs']=[]
 for spec in [dict(matrix='1,1;0,1;1,0',vector='1,2,-1',weights='1,1,1'),dict(matrix='0,0;0,0',vector='2,-3',weights='1,4'),dict(matrix='1,2;1,2',vector='2,-1',weights='3,2'),dict(matrix='1,0;1,1;0,1;1,-1',vector='1,2,0,-1',weights='1,2,3,4')]:
  obj=js('(()=>{const f=document.querySelector("#og-form"),spec='+json.dumps(spec)+';for(const[k,v]of Object.entries(spec))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));return {error:document.querySelector("#og-error").textContent,result:OrthogonalityLab.model.result,issues:DiagramLayout.audit(document.querySelector("#og-output svg"))};})()');assert not obj['error']and not obj['issues'],obj;report['labs'].append(obj)
 for change in [dict(matrix='1.5,0;0,1'),dict(weights='1,0'),dict(weights='1,-2'),dict(vector=''),dict(matrix='11,0;0,1')]:
  js('(()=>{window.oldLab=OrthogonalityLab;const f=document.querySelector("#og-form"),change='+json.dumps(change)+';for(const[k,v]of Object.entries({matrix:"1,0;0,1",vector:"2,-1",weights:"1,1",...change}))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('OrthogonalityLab===oldLab && document.querySelector("#og-error").textContent.length>0'),change
 report['invalidPreservesPrevious']=5
'''+s[b:]
s=s.replace('two-bases','line').replace('mobile-coordinates.png','mobile-line.png')
(B/'qa_l_orthogonality_browser.py').write_text(s,encoding='utf-8')
