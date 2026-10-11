from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/a_hash.js';s=p.read_text(encoding='utf-8')
s=s.replace('let y=50+i*rh','let y=58+i*rh').replace("txt(30,368,'Squared allocation", "txt(30,338,'Squared allocation")
s=s.replace("),47,", "),56,").replace("row(z.slots,85,'slot')", "row(z.slots,104,'slot')")
start=s.index('const row=(a,y,tag)=>');end=s.index("\nif(z.kind==='chain')",start)
s=s[:start]+"""const row=(a,y,tag)=>{const width=Math.min(53,650/a.length),x=30;return a.map((v,i)=>{const active=z.cursor===i&&(z.kind!=='cuckoo'||(tag==='right')===Boolean(z.extra.side));const cell=rect('hole-'+tag+'-'+i,x+i*width,y,width-4,42,v===null?'–':v==='DELETED'?'DEL':typeof v==='number'?v:'',i,active?'#d6edf5':v==='DELETED'?'#fff0d7':'#fff');return cell+(v&&typeof v==='object'?rect((tag==='old'?'old-':'')+v.id,x+i*width,y,width-4,42,v.key,'',active?'#d6edf5':'#fff'):'');}).join('');};"""+s[end:]
s=s.replace("if(z.cursor!==null)out+=rect", "if(z.cursor!==null&&z.kind!=='cuckoo')out+=rect")
s=s.replace("Follow the selected bucket and compare real keys.", "Follow the selected bucket and compare real keys; stable K identifiers retain record identity.")
s=s.replace("the dot denotes EMPTY", "the dash denotes EMPTY")
# External chain links are recomputed from their current moving rectangle ports.
s=s.replace('data-connector="true"', 'data-connector="true" data-source="${j?b[j-1].id:\'bucket-\'+i}" data-target="${b[j].id}"')
old="return AdvancedSimulations.mount(host,m,{topic:'a_hash',prefix:'hs',retainDrawing:true});"
new="""const player=AdvancedSimulations.mount(host,m,{topic:'a_hash',prefix:'hs',retainDrawing:true});
const updatePorts=()=>{const svg=host.querySelector('.hs-stage svg');if(!svg)return;for(const e of svg.querySelectorAll('[data-connector]')){const a=svg.querySelector('[data-entity="'+e.dataset.source+'"] rect'),b=svg.querySelector('[data-entity="'+e.dataset.target+'"] rect');if(!a||!b)continue;const aa=DiagramLayout.box(svg,a),bb=DiagramLayout.box(svg,b);e.setAttribute('d',`M${aa.x+aa.w} ${aa.y+aa.h/2} L${bb.x} ${bb.y+bb.h/2}`);}};
const observer=new MutationObserver(updatePorts);observer.observe(host.querySelector('.hs-stage'),{childList:true,subtree:true,attributes:true,attributeFilter:['x','y','width','height','transform']});updatePorts();const dispose=player.dispose.bind(player);player.dispose=()=>{observer.disconnect();dispose();};return player;"""
assert old in s;s=s.replace(old,new)
p.write_text(s,encoding='utf-8')
print('Separated fixed storage from moving records, preserved identity, and attached live chain ports.')
