from pathlib import Path
import re
B=Path(__file__).resolve().parent
s=(B/'qa_a_balanced_browser.py').read_text().replace('a_balanced','a_heap').replace('a-balanced','a-heap').replace('BalancedPlayers','HeapPlayers').replace('BalancedLab','HeapLab').replace('data-bl','data-hp').replace('bl-','hp-').replace('#bl','#hp').replace('data-key','data-node').replace('dataset.key','dataset.node')
start=s.index(' for id,step,name in');stop=s.index(" js('window.p=",start)
s=s[:start]+''' for id,step,name in [('up',6,'insertion.png'),('down',6,'extraction.png'),('indexed',4,'indexed.png'),('fibonacci',2,'first-loss.png'),('fibonacci',5,'second-loss.png'),('binomial',16,'binomial.png'),('sort',8,'heapsort.png')]:
  js('HeapPlayers.find(p=>p.model.id==='+json.dumps(id)+').show(Math.min('+str(step)+',HeapPlayers.find(p=>p.model.id==='+json.dumps(id)+').model.frames.length-1))');capture('[data-hp-model="'+id+'"]',name)
 capture('.hero','title.png');capture('[data-source-id="a_heap_Q80"]','synthesis-question.png');capture('.review-rule','final-rule.png')
'''+s[stop:]
s=s.replace('model.id==="delete-zero"','model.id==="up"').replace('f.snapshot.state.action.startsWith("Rotate")','f.snapshot.state.action.startsWith("Exchange")')
start=s.index(" for op in ['avl-insert'");stop=s.index(" cdp('Emulation.setDeviceMetricsOverride',dict(width=390",start)
s=s[:start]+''' for spec in [dict(operation='build',keys='9,4,7,1,0,3,2'),dict(operation='insert',keys='1,4,2,8,5,3,7',value='-999'),dict(operation='extract',keys='1,4,2,8,5,3,7'),dict(operation='change',keys='1,4,2,8,5,3,7',index='5',value='-999'),dict(operation='delete',keys='1,10,2,11,12,3,4',index='3'),dict(operation='sort',keys='5,5,-999,3'),dict(operation='multiway',arity='4',keys='9,4,7,1,0,3,2'),dict(operation='topk',keys='5,1,9,4,8,2,10',k='3'),dict(operation='frontier',keys='1,4,2,8,5,3,7',k='4'),dict(operation='binomial',keys='8,7,6,5,4,3,2,1'),dict(operation='fibonacci',keys='1')]+[dict(operation=op,keys=','.join(map(str,range(-999,-984))))for op in ['build','sort','binomial']]:
  obj=js('(()=>{const f=document.querySelector("#hp-form"),spec='+json.dumps(spec)+';f.elements.arity.value="2";f.elements.orientation.value="min";for(const[k,v]of Object.entries(spec))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));const bad=[];for(let i=0;i<HeapLab.model.frames.length;i++){HeapLab.show(i);const svg=HeapLab.host.querySelector("svg");bad.push(...DiagramLayout.audit(svg));for(const g of svg.querySelectorAll("[data-node]")){const c=g.querySelector("circle"),t=g.querySelector("text").getBBox();if(c.r.baseVal.value-t.width/2<6)bad.push({kind:"circle key padding",id:g.dataset.node,padding:c.r.baseVal.value-t.width/2});}}return {operation:spec.operation,error:document.querySelector("#hp-error").textContent,result:HeapLab.model.result,issues:bad};})()');assert not obj['error']and not obj['issues'],obj;report['labs'].append(obj)
 for change in [dict(keys=''),dict(keys='1,2,'),dict(keys=','.join(map(str,range(16)))),dict(keys='1000'),dict(keys='1.5'),dict(index=''),dict(index='-1'),dict(index='3'),dict(value=''),dict(value='1000'),dict(value='2.5'),dict(keys='3,1,2')]:
  js('(()=>{window.oldLab=HeapLab;const f=document.querySelector("#hp-form"),base={operation:"change",keys:"1,2,3",index:"0",value:"5",arity:"2",orientation:"min"},change='+json.dumps(change)+';for(const[k,v]of Object.entries({...base,...change}))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('HeapLab===oldLab && document.querySelector("#hp-error").textContent.length>0')
 report['invalidPreservesPrevious']=12
'''+s[stop:]
s=s.replace('data-hp-model="multiway-borrow"','data-hp-model="fibonacci"').replace('data-hp-model="middle-subtree"','data-hp-model="up"').replace("['cards']==53","['cards']==54")
(B/'qa_a_heap_browser.py').write_text(s,encoding='utf-8')
print('Prepared independent real-Edge geometry, motion, input, font, mobile and print inspection.')
