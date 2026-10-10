from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_d_generating_browser.py').read_text(encoding='utf-8').replace('d_generating','a_bst').replace('d-generating','a-bst').replace('GeneratingPlayers','BSTPlayers').replace('GeneratingLab','BSTLab').replace('gf-','bt-').replace('>17','>21').replace("cards']==51","cards']==52")
start=s.index(' for id,step,name in');end=s.index(' capture(\'.hero\'',start)
s=s[:start]+''' for id,step,name in [('insert-nine',9,'insertion.png'),('delete-deep',1,'successor-child.png'),('delete-deep',2,'deletion.png'),('delete-immediate',2,'immediate.png'),('preorder-invalid',3,'invalid-preorder.png'),('strict-rank-65',2,'rank.png'),('perfect-orders',30,'orders.png'),('counted-three',1,'multiplicity.png'),('left-rotation',1,'rotation.png')]:
  js('BSTPlayers.find(p=>p.model.id==='+json.dumps(id)+').show('+str(step)+')');capture('[data-bt-model="'+id+'"]',name)
'''+s[end:]
s=s.replace('a_bst_original_47','a_bst_original_08').replace('catalan-four','insert-nine').replace('convolution-five','strict-rank-65')
start=s.index(' for op,n in');end=s.index(' cdp(\'Emulation.setDeviceMetricsOverride\',dict(width=390',start)
s=s[:start]+''' for op,q in [('search',10),('insert',10),('delete',5),('rank',5),('select',8),('range',5)]:
  spec=dict(operation=op,keys='1,2,3,4,5,6,7,8,9',q=q,a=3,b=7)
  obj=js('(()=>{const f=document.querySelector("#bt-form"),spec='+json.dumps(spec)+';for(const[k,v]of Object.entries(spec))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));const bad=[];for(let i=0;i<BSTLab.model.frames.length;i++){BSTLab.show(i);bad.push(...DiagramLayout.audit(BSTLab.host.querySelector("svg")));}return {operation:spec.operation,error:document.querySelector("#bt-error").textContent,result:BSTLab.model.result,issues:bad};})()');assert not obj['error']and not obj['issues'],obj;report['labs'].append(obj)
 for change in [dict(keys=''),dict(keys='1,1'),dict(keys='1,2,'),dict(keys='1,2,3,4,5,6,7,8,9,10'),dict(keys='1000'),dict(keys='1.5'),dict(operation='select',q=-1),dict(operation='select',q=9),dict(operation='range',a=5,b=2),dict(q=1.5)]:
  js('(()=>{window.oldLab=BSTLab;const f=document.querySelector("#bt-form"),base={operation:"search",keys:"1,2,3,4,5,6,7,8,9",q:5,a:3,b:7},change='+json.dumps(change)+';for(const[k,v]of Object.entries({...base,...change}))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('BSTLab===oldLab && document.querySelector("#bt-error").textContent.length>0')
 report['invalidPreservesPrevious']=10
'''+s[end:]
s=s.replace("time.sleep(.12);js('p.pause();", "time.sleep(.12);js('p.pause();")
# The tree stage must stay compact and edges must end at actual node-circle boundaries.
needle=" report['mathGeometry']=js"
extra=''' report['treeConnections']=js(r\'''(()=>{const issues=[];const seen=new Set();let edges=0;for(const p of BSTPlayers){if(seen.has(p.model.id))continue;seen.add(p.model.id);for(let i=0;i<p.model.frames.length;i++){p.show(i);const svg=p.host.querySelector('svg');if(svg.viewBox.baseVal.height>420)issues.push({id:p.model.id,frame:i,kind:'oversized stage'});for(const e of svg.querySelectorAll('[data-edge]')){edges++;const keys=e.dataset.edge.split(':');const a=svg.querySelector('[data-key="'+keys[0]+'"] circle'),b=svg.querySelector('[data-key="'+keys[1]+'"] circle');const nums=e.getAttribute('d').match(/-?\\d+(?:\\.\\d+)?/g).map(Number);if(nums.length!==4||!a||!b){issues.push({id:p.model.id,frame:i,kind:'missing port'});continue;}for(const[c,x,y]of[[a,nums[0],nums[1]],[b,nums[2],nums[3]]]){const dist=Math.hypot(x-c.cx.baseVal.value,y-c.cy.baseVal.value);if(Math.abs(dist-c.r.baseVal.value)>0.001)issues.push({id:p.model.id,frame:i,kind:'detached arrow',dist});}}}p.show(0);}return{edges,issues};})()\''');assert not report['treeConnections']['issues'],report['treeConnections']['issues'][:10]
'''
s=s.replace(needle,extra+needle)
(B/'qa_a_bst_browser.py').write_text(s,encoding='utf-8')
print('Prepared real Edge QA for every tree checkpoint and exact arrow port.')
