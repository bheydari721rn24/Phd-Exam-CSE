from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_a_bst_browser.py').read_text(encoding='utf-8').replace('a_bst','a_balanced').replace('a-bst','a-balanced').replace('BSTPlayers','BalancedPlayers').replace('BSTLab','BalancedLab').replace('bt-','bl-').replace('data-bt','data-bl')
a=s.index(' for id,step,name in [');z=s.index(" capture('.hero'",a)
s=s[:a]+''' for id,step,name in [('middle-subtree',15,'middle-transfer.png'),('delete-cascade',6,'cascade.png'),('llrb-minimum',32,'llrb-delete.png'),('multiway-borrow',1,'borrow.png'),('multiway-merge',1,'merge.png'),('classical-triangle',4,'classical.png')]:
  js('BalancedPlayers.find(p=>p.model.id==='+json.dumps(id)+').show(Math.min('+str(step)+',BalancedPlayers.find(p=>p.model.id==='+json.dumps(id)+').model.frames.length-1))');capture('[data-bl-model="'+id+'"]',name)
'''+s[z:]
s=s.replace('original_08','original_80').replace('delete-deep','delete-zero')
# The deletion trace's first rotation has an actual geometry change.
s=s.replace('p.show(1);p.host.querySelector', 'window.rotationFrame=p.model.frames.findIndex(f=>f.snapshot.state.action.startsWith("Rotate"));p.show(rotationFrame-1);p.host.querySelector',1)
a=s.index(" report['labs']=[]");z=s.index(" cdp('Emulation.setDeviceMetricsOverride',dict(width=390",a)
s=s[:a]+''' report['labs']=[]
 for op in ['avl-insert','avl-delete','llrb-insert','llrb-delete','multiway']:
  spec=dict(operation=op,keys='1,2,3,4,5,6,7,8,9,10,11,12',remove='1,6,12,999')
  obj=js('(()=>{const f=document.querySelector("#bl-form"),spec='+json.dumps(spec)+';for(const[k,v]of Object.entries(spec))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));const bad=[];for(let i=0;i<BalancedLab.model.frames.length;i++){BalancedLab.show(i);bad.push(...DiagramLayout.audit(BalancedLab.host.querySelector("svg")));}return {operation:spec.operation,error:document.querySelector("#bl-error").textContent,result:BalancedLab.model.result,issues:bad};})()');assert not obj['error']and not obj['issues'],obj;report['labs'].append(obj)
 for change in [dict(keys=''),dict(keys='1,1'),dict(keys='1,2,'),dict(keys=','.join(map(str,range(13)))),dict(keys='1000'),dict(keys='1.5'),dict(remove=''),dict(remove='1,'),dict(remove='1000'),dict(remove='1.5')]:
  js('(()=>{window.oldLab=BalancedLab;const f=document.querySelector("#bl-form"),base={operation:"avl-delete",keys:"1,2,3",remove:"1"},change='+json.dumps(change)+';for(const[k,v]of Object.entries({...base,...change}))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('BalancedLab===oldLab && document.querySelector("#bl-error").textContent.length>0')
 report['invalidPreservesPrevious']=10
'''+s[z:]
s=s.replace('strict-rank-65','multiway-borrow').replace('insert-nine','middle-subtree').replace("['cards']==52","['cards']==53")
(B/'qa_a_balanced_browser.py').write_text(s,encoding='utf-8')
