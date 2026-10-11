from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_s_distributions_browser.py').read_text(encoding='utf-8')
s=s.replace('s_distributions','l_linear').replace('s-distributions','l-linear').replace('DistributionPlayers','LinearPlayers').replace('DistributionLab','LinearLab').replace('sd-','lt-')
s=s.replace("==88","==84").replace(">26",">38").replace("==58","==59")
a=s.index(" for id,name in");b=s.index("\n js('window.p=",a)
s=s[:a]+''' for id,name in [('two-bases','coordinates.png'),('rotation','rotation.png'),('oblique','oblique.png'),('fiber-sum','fibers.png'),('bridge','bridge.png'),('derivative-bases','derivative.png'),('sylvester','sylvester.png'),('similarity','similarity.png')]:
  js('LinearPlayers.find(p=>p.model.id==='+json.dumps(id)+').show(LinearPlayers.find(p=>p.model.id==='+json.dumps(id)+').model.frames.length-1)');capture('[data-lt-model="'+id+'"]',name)
'''+s[b:]
s=s.replace('poisson-approximation','rotation')
a=s.index(" report['labs']=[]");b=s.index("\n cdp('Emulation.setDeviceMetricsOverride',dict(width=390",a)
s=s[:a]+''' report['labs']=[]
 for spec in [dict(matrix='1,2;0,1',inputBasis='1,0;1,1',outputBasis='1,1;0,1',vector='2,-1'),dict(matrix='0,0;0,0',inputBasis='2,1;1,1',outputBasis='1,1;1,-1',vector='-2,3'),dict(matrix='1,-1;0,0',inputBasis='2,1;0,2',outputBasis='1,2;0,3',vector='3,-1')]:
  obj=js('(()=>{const f=document.querySelector("#lt-form"),spec='+json.dumps(spec)+';for(const[k,v]of Object.entries(spec))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));return {error:document.querySelector("#lt-error").textContent,result:LinearLab.model.result,issues:DiagramLayout.audit(document.querySelector("#lt-output svg"))};})()');assert not obj['error']and not obj['issues'],obj;report['labs'].append(obj)
 for change in [dict(matrix='1.5,0;0,1'),dict(inputBasis='1,2;2,4'),dict(outputBasis='1,1;1,1'),dict(vector=''),dict(matrix='11,0;0,1')]:
  js('(()=>{window.oldLab=LinearLab;const f=document.querySelector("#lt-form"),change='+json.dumps(change)+';for(const[k,v]of Object.entries({matrix:"1,2;0,1",inputBasis:"1,0;1,1",outputBasis:"1,1;0,1",vector:"2,-1",...change}))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('LinearLab===oldLab && document.querySelector("#lt-error").textContent.length>0'),change
 report['invalidPreservesPrevious']=5
'''+s[b:]
s=s.replace('uniform-lattice','two-bases').replace('mobile-uniform.png','mobile-coordinates.png')
# Check the actual in-flight geometric rotation, not merely its endpoint matrix.
needle=" js('p.pause();window.oldIndex="
start=s.index(needle)
s=s[:start]+''' report['rotationMotion']=js('(()=>{const g=p.host.querySelector("[data-entity=rotating-grid]"),m=g.transform.baseVal.consolidate().matrix;return {determinant:m.a*m.d-m.b*m.c,firstLength:m.a*m.a+m.b*m.b,secondLength:m.c*m.c+m.d*m.d};})()');assert all(abs(report['rotationMotion'][k]-1)<1e-6 for k in ['determinant','firstLength','secondLength'])
'''+s[start:]
(B/'qa_l_linear_browser.py').write_text(s,encoding='utf-8')
