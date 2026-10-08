from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_l_det_browser.py').read_text(encoding='utf-8').replace('l_det','l_spaces').replace('l-det','l-spaces').replace('DeterminantPlayers','VectorSpacePlayers').replace('DeterminantLab','VectorSpaceLab').replace('det-','vs-').replace('data-det','data-vs')
a=s.index(' for id,step,name in[');b=s.index(" js('window.p=",a)
s=s[:a]+''' for id,step,name in [('closure-plane',3,'plane.png'),('pivot-main',3,'pivot.png'),('coordinates-main',2,'coordinates.png'),('symmetric-trace',2,'symmetric.png'),('intersection-main',2,'intersection.png'),('quotient-main',1,'quotient.png'),('finite-basis',2,'finite-field.png'),('projection-main',2,'projection.png'),('intersection-parameter',1,'intersection-jump.png'),('matrix-balances',4,'matrix-balances.png')]:
  js('VectorSpacePlayers.find(p=>p.model.id==='+json.dumps(id)+').show('+str(step)+')');capture('[data-vs-model="'+id+'"]',name)
 capture('.hero','title.png');capture('[data-source-id="l-spaces-original-59"]','question-quotient.png');capture('.review-rule','final-rule.png')
''' +s[b:]
s=s.replace('geometry-main','parameter-span').replace('cofactor-main','pivot-main')
a=s.index(" report['labs']=[]");b=s.index(" cdp('Emulation.setDeviceMetricsOverride',dict(width=390",a)
s=s[:a]+''' report['labs']=[]
 for mat,target,rank,consistent in [('1,2,0,3;2,4,1,4;3,6,2,5','1,3,5',2,True),('0,1;1,0','2,3',2,True),('1,2;2,4','1,3',1,False),('0,0;0,0','0,0',0,True),('1;2;3','2,4,6',1,True),('1,2,3,4,5;2,4,6,8,10;0,1,0,1,0;0,0,1,0,1','2,4,1,1',3,True),('20,-19,17,11;-13,20,16,-18;19,11,-17,20;16,-13,20,19','20,-19,17,11',4,True)]:
  obj=js('(()=>{const f=document.querySelector("#vs-form");f.elements.matrix.value='+json.dumps(mat)+';f.elements.target.value='+json.dumps(target)+';f.dispatchEvent(new Event("submit",{cancelable:true}));const bad=[];for(let i=0;i<VectorSpaceLab.model.frames.length;i++){VectorSpaceLab.show(i);bad.push(...DiagramLayout.audit(VectorSpaceLab.host.querySelector("svg")));}return {error:document.querySelector("#vs-error").textContent,result:VectorSpaceLab.model.result,checks:VectorSpaceLab.model.frames.every(f=>f.teaching.checks.every(c=>c.result==="true")),issues:bad};})()');assert not obj['error']and not obj['issues']and obj['result']['rank']==rank and obj['result']['consistent']==consistent and obj['checks']and all(obj['result']['checks'].values()),obj;report['labs'].append(obj)
 capture('#vs-output .vs-stage','dense-rational-lab.png')
 for mat,target in [('1,,2;2,3','1,2'),('1,2;3','1,2'),('1.5,1;2,3','1,2'),('21,1;2,3','1,2'),('1,2;3,4','1'),('1,2,3,4,5,6;1,2,3,4,5,6','1,2')]:
  js('(()=>{window.oldLab=VectorSpaceLab;const f=document.querySelector("#vs-form");f.elements.matrix.value='+json.dumps(mat)+';f.elements.target.value='+json.dumps(target)+';f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('VectorSpaceLab===oldLab && document.querySelector("#vs-error").textContent.length>0')
 report['invalidPreservesPrevious']=6
''' +s[b:]
s=s.replace("==42 and report['library']","==43 and report['library']")
(B/'qa_l_spaces_browser.py').write_text(s,encoding='utf-8')
print('Built geometry, typography, interaction, print, exact-lab and mobile audit.')
