from pathlib import Path
B=Path(__file__).resolve().parent;R=B.parent
p=R/'dist/chapters/a_balanced.js';s=p.read_text(encoding='utf-8')
s=s.replace("txt(p.x,p.y+6,t.key,'bl-math','middle')", "txt(p.x,p.y+6,t.key,'bl-math'+(String(t.key).length>3?' bl-key-long':String(t.key).length>2?' bl-key-medium':''),'middle')")
p.write_text(s,encoding='utf-8')
p=B/'build_a_balanced.py';s=p.read_text(encoding='utf-8')
if '.bl-key-long'not in s:s=s.replace("(R/'dist/chapters/a_balanced.css').write_text", "css+='\\n.bl-model svg .bl-key-long{font-size:14px!important}.bl-model svg .bl-key-medium{font-size:16px!important}\\n'\n(R/'dist/chapters/a_balanced.css').write_text")
p.write_text(s,encoding='utf-8')
p=B/'qa_a_balanced_browser.py';s=p.read_text(encoding='utf-8')
mark=" for change in [dict(keys='')"
addition=''' for op in ['avl-insert','llrb-insert','multiway']:
  spec=dict(operation=op,keys=','.join(map(str,range(-999,-987))),remove='-999')
  obj=js('(()=>{const f=document.querySelector("#bl-form"),spec='+json.dumps(spec)+';for(const[k,v]of Object.entries(spec))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));const bad=[];for(let i=0;i<BalancedLab.model.frames.length;i++){BalancedLab.show(i);const svg=BalancedLab.host.querySelector("svg");bad.push(...DiagramLayout.audit(svg));for(const g of svg.querySelectorAll("[data-key]")){const c=g.querySelector("circle"),t=g.querySelector("text").getBBox();if(c.r.baseVal.value-t.width/2<6)bad.push({kind:"circle key padding",key:g.dataset.key,padding:c.r.baseVal.value-t.width/2});}}return {operation:spec.operation,error:document.querySelector("#bl-error").textContent,issues:bad};})()');assert not obj['error']and not obj['issues'],obj;report['labs'].append(obj)
'''
if 'circle key padding'not in s:s=s.replace(mark,addition+mark)
p.write_text(s,encoding='utf-8')
