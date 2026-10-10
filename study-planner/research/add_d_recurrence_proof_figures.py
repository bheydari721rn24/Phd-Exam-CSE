from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/d_recurrence.js';s=p.read_text(encoding='utf-8')
s=s.replace("'modular','matrix'].includes", "'modular','matrix','conjugate','reflection'].includes")
s=s.replace("if(s.operation==='ferrers'&&s.n<3)","if(['ferrers','conjugate'].includes(s.operation)&&s.n<3)")
needle=" else if(s.operation==='modular'){let u=0,v=1;"
insert=r''' else if(s.operation==='conjugate'){const original=[n-2,1,1],transposed=Array.from({length:n-2},(_,i)=>original.filter(x=>x>i).length);states=[{step:0,original,transposed:[]},{step:1,original,transposed}];result={original,transposed,total:n};}
 else if(s.operation==='reflection'){const original='DUUDUDUDUDUD';let h=0,first=0;for(let j=0;j<original.length;j++){h+=original[j]==='U'?1:-1;if(h<0){first=j+1;break;}}const transformed=original.slice(0,first).split('').map(c=>c==='U'?'D':'U').join('')+original.slice(first);states=[{step:0,path:original,first},{step:1,path:transformed,first}];result={original,transformed,first,endpoint:2};}
'''
assert needle in s;s=s.replace(needle,insert+needle,1)
needle=" else if(s.operation==='modular'){b+="
insert=r''' else if(s.operation==='conjugate'){b+=text(34,40,'Transpose the Ferrers diagram: every cell swaps row and column','rc-prose');function cells(parts,x){parts.forEach((count,row)=>{for(let j=0;j<count;j++)b+=rect(x+j*31,82+row*36,25,28);});}cells(z.original,65);if(z.step)cells(z.transposed,450);b+=line([[310,167],[408,167]],C.active,true)+text(65,66,z.original.join(' + '),'rc-math')+text(450,66,z.step?z.transposed.join(' + '):'Transpose next','rc-math')+text(34,320,'Cell count remains '+r.total+'; applying the operation twice restores the input.','rc-prose');}
 else if(s.operation==='reflection'){const ox=70,base=232,cell=50;let x=ox,y=base,pts=[[x,y]];b+=text(34,42,z.step?'Reflected prefix: seven up steps, five down steps':'Bad balanced path: first crossing below zero','rc-prose')+line([[50,base],[725,base]],C.muted);for(let j=0;j<z.path.length;j++){const old=[x,y];x+=cell;y+=z.path[j]==='U'?-32:32;b+=line([old,[x,y]],j<z.first?C.warm:C.active);pts.push([x,y]);}pts.forEach(([x,y])=>{b+=`<circle cx="${x}" cy="${y}" r="4" fill="${C.ink}"/>`;});b+=text(34,310,z.step?'Endpoint height two; reflect the first visit to height one to invert.':'Reflect through the first negative-one visit to construct the image.','rc-prose');}
'''
assert needle in s;s=s.replace(needle,insert+needle,1)
s=s.replace("const why={unrolling:","const why={conjugate:'Ferrers transposition is a cell-preserving involution relating row-count and largest-part constraints.',reflection:'Reflecting the first below-zero prefix maps bad balanced paths bijectively to paths ending at height two.',unrolling:")
s=s.replace("function frameFormula(s,z,r){const n=z.step;", "function frameFormula(s,z,r){const n=z.step;\n if(s.operation==='conjugate')return '|'+r.original.join('+')+'|=|'+r.transposed.join('+')+'|='+r.total;\n if(s.operation==='reflection')return 'C_6=\\\\binom{12}{6}-\\\\binom{12}{7}=132';")
p.write_text(s,encoding='utf-8')
p=R/'research/build_d_recurrence.py';s=p.read_text(encoding='utf-8');s=s.replace("js=\"const {makeModel}","specs += [('ferrers-conjugate','Seven-cell Ferrers transposition: three rows to largest part three',dict(operation='conjugate',n=7),'conjugate'),('reflection-six','Bad six-pair path and its reflected-prefix image',dict(operation='reflection',n=6),'reflection')]\njs=\"const {makeModel}",1)
s=s.replace("15:'weighted-forcing',",'').replace("41:'all-domino-eight',",'').replace("28:'zero-root-prefix',",'').replace("59:'ferrers-seven'","59:'ferrers-conjugate'").replace("62:'first-return-three'","62:'reflection-six'").replace("75:'fib-mod-three',",'')
s=s.replace('12 distinct mathematical models','14 distinct mathematical models').replace("'animationCount=12'","'animationCount=14'").replace("'animationWalkthroughCount=12'","'animationWalkthroughCount=14'")
# The old generated renderer still originates with seventeen models, so adjust replacements at their source.
s=s.replace("'animationCount=17','animationCount=12'","'animationCount=17','animationCount=14'").replace("'animationWalkthroughCount=17','animationWalkthroughCount=12'","'animationWalkthroughCount=17','animationWalkthroughCount=14'")
p.write_text(s,encoding='utf-8')
p=R/'research/d_recurrence.en.md';s=p.read_text(encoding='utf-8').replace('## 22. Catalan recurrence: a nonlinear decomposition','<!-- SIM: conjugate -->\n\n## 22. Catalan recurrence: a nonlinear decomposition').replace('<!-- SIM: catalan -->','<!-- SIM: catalan -->\n\n<!-- SIM: reflection -->');p.write_text(s,encoding='utf-8')
print('Added proof-specific transposition and reflection, and removed unrelated companion assignments.')
