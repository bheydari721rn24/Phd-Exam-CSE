from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/advanced-simulations.js';s=p.read_text()
old="${tx(100+j*w+(w-12)/2,320-h-12,num(x),'sim-number')}"
new="${p.length<=10?tx(100+j*w+(w-12)/2,320-h-12,num(x),'sim-number'):''}"
assert old in s;s=s.replace(old,new)
old="return wrap(b,'Discrete probability masses on fixed axes',435);"
new="if(p.length>10)b+=tx(500,429,'Exact probability masses are listed in the explanation panel.');return wrap(b,'Discrete probability masses on fixed axes',455);"
assert old in s;s=s.replace(old,new)
needle="   const delta=el('div',undefined,'sim-delta-wrap')"
new="""   const law=s.masses??s.law;
   if(Array.isArray(law)&&law.length&&law.every(x=>typeof x==='number'||x&&typeof x==='object')){const wrap=el('div',undefined,'sim-delta-wrap'),table=el('table',undefined,'sim-delta'),head=el('tr');['Support value','Exact stored mass'].forEach(x=>head.append(el('th',x)));table.append(head);law.forEach((x,j)=>{const row=el('tr'),a=el('td'),b=el('td');a.append(mathValue(typeof x==='number'?s.values?.[j]??j:x.x??x.k??x.value??x.t??j));b.append(mathValue(typeof x==='number'?x:x.mass??x.p??x.probability));row.append(a,b);table.append(row);});wrap.append(table);teach.append(details('law','Exact probability masses',wrap));}
   const delta=el('div',undefined,'sim-delta-wrap')"""
assert needle in s;s=s.replace(needle,new)
# Never morph a connection into a different endpoint relation, even when it is inside an entity.
needle="if(!a||!b||a.tagName!==b.tagName)return;"
new="if(!a||!b||a.tagName!==b.tagName)return;if(b.tagName.toLowerCase()==='path'&&['source','target','layoutSource','layoutTarget','net'].some(k=>a.dataset[k]!==b.dataset[k]))return;"
s=s.replace(needle,new)
p.write_text(s,encoding='utf-8')
print('Dense mass diagrams retain their scale; exact numbers use a dedicated readable table.')
