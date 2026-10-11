from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=R/'dist/chapters/a_amortized.js';s=p.read_text(encoding='utf-8')
s=s.replace("out+=rect(r&&ids?r.id:null,30+i*w,y,w-6,38,r?.value??r??'–');","out+=rect(r&&ids?r.id:null,30+i*w,y,w-6,38,r?.value??r??'–');if(r&&ids&&r.id)out+=txt(30+i*w+(w-6)/2,y+80,r.id,'am-id');")
s=s.replace("if(capacity>16)out+=txt(30,y+90,'Only indices 0–15 shown; full capacity '+capacity+' is in the exact snapshot.');","if(capacity>16)out+=txt(30,y-36,'Shown indices 0–15 of capacity '+capacity+'; full state is in the snapshot.');")
s=s.replace("if(['shrink','thrash'].includes(s.kind)){s.capacity", "if(['shrink','thrash'].includes(s.kind)){if(s.factor!==2)throw Error('The shrink policies use doubling and halving.');s.capacity")
s=s.replace("invariant:'Read the declared primitive model.","invariant:'Numbered labels beneath cells identify current storage positions; K and I labels identify records and original indices. Read the declared primitive model.")
p.write_text(s,encoding='utf-8')
p=R/'research/prepare_a_amortized.py';s=p.read_text(encoding='utf-8');s=s.replace('.am-block{font-family:', '.am-id{font-family:"STIX Two Math",serif;font-size:12px;text-anchor:middle;fill:#557784}.am-block{font-family:');p.write_text(s,encoding='utf-8')
print('Added readable record identity labels and explicit shrink-factor validation.')
