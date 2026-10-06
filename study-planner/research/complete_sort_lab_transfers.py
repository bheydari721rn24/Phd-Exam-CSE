from pathlib import Path
p=Path(__file__).parent/'a_sort_lab.js';s=p.read_text(encoding='utf-8')
changes=[
("'output')];while(i<L.length&&j<R.length)","'output')];add('Prepare two run views and an empty output buffer.',rows(),{operation:'prepare',reason:'The two source runs are already sorted; each head will be tested before emission.',activeLine:1});while(i<L.length&&j<R.length)"),
("add('Copy left remainder without key comparisons.',rows());","add('Copy left remainder without key comparisons.',rows(),{transfer:{row:'left',index:i-1,dest:out.length-1},operation:'move',reason:'The right run is exhausted; copy this remaining left record without comparing keys.',activeLine:4});"),
("add('Copy right remainder without key comparisons.',rows());","add('Copy right remainder without key comparisons.',rows(),{transfer:{row:'right',index:j-1,dest:out.length-1},operation:'move',reason:'The left run is exhausted; copy this remaining right record without comparing keys.',activeLine:4});"),
("if(j+1<end){C++;if(A[j+1].key>A[j].key)j++;}","if(j+1<end){C++;add('Compare children to select the larger one.',[row('Array',A)],{layout:'heap',heapSize:end,test:[A[j+1].key,'>',A[j].key],testResult:A[j+1].key>A[j].key,operation:'compare',reason:'Choose the larger child before testing the parent.',activeLine:1});if(A[j+1].key>A[j].key)j++;}"),
("for(let i=Math.floor(n/2)-1;i>=0;i--)sink(i,n);", "snap('Prepare the complete binary tree view of the live array prefix.',n);for(let i=Math.floor(n/2)-1;i>=0;i--)sink(i,n);"),
("const cumulative=[...counts],out=Array(n).fill(null);for(const r", "const cumulative=[...counts],out=Array(n).fill(null);add('Prepare cumulative ends and an empty output buffer.',[row('Input',A,'reference'),row('Ends',counts.map((key,i)=>({key,id:String(i+low)})),'counts'),row('Output',out)],{operation:'prepare',reason:'Each cumulative count is an exclusive end; decrement it before placement.',activeLine:2});for(const r"),
("row('Output',out)]);}A=out;Object.assign(extra,{cumulative,K,low});", "row('Output',out)],{outputActive:counts[k],operation:'move',reason:'Right-to-left scatter assigns later equal records to later slots, preserving original order.',activeLine:4});}A=out;Object.assign(extra,{cumulative,K,low});"),
("row('Bucket '+k,bs))];for(const r of A)", "row('Bucket '+k,bs))];add(`Prepare empty buckets for pass ${t+1}.`,rows(),{operation:'prepare',reason:'The reference row shows the current order; all buckets start empty.',activeLine:1});for(const r of A)")]
for old,new in changes:
 assert s.count(old)==1,(old,s.count(old));s=s.replace(old,new)
s=s.replace('FIFO arrival order: top to bottom</text>','FIFO arrival order: top to bottom</text>').replace('y="194">FIFO','y="56">FIFO')
old="let top=205;";assert s.count(old)==1;s=s.replace(old,"let top=205,target=null;")
old="r.cells.forEach((v,j)=>s+=cell(v,x+(cardW-60)/2,top+49+j*74,v.id));"
new="r.cells.forEach((v,j)=>{s+=cell(v,x+(cardW-60)/2,top+49+j*74,v.id);if(v.id===f.distributedId&&start-1+c===f.bucketIndex)target=[x+cardW-6,x+(cardW-60)/2+60,top+81+j*74];});"
assert s.count(old)==1;s=s.replace(old,new)
old="height=top+20;"
new="""height=top+20;if(target){const id=f.distributedId,i=f.rows[0].cells.findIndex(r=>r.id===id),x1=216+70*i,[lane,x2,y2]=target;s+=`<path data-edge="" data-source-entity="reference-${id}" data-target-entity="${id}" d="M ${x1} 116 L ${x1+5} 116 L ${x1+5} 190 L ${lane} 190 L ${lane} ${y2} L ${x2} ${y2}" fill="none" stroke="#426e91" stroke-width="2" marker-end="url(#sort-arrow)"/>`;}"""
assert s.count(old)==1;s=s.replace(old,new)
old="\n  }\n  return `<svg"
new="""\n   if(f.outputActive!==undefined){const k=f.outputActive,r=f.rows[2].cells[k],i=f.rows[0].cells.findIndex(x=>x.id===r.id),x1=216+70*i,x2=186+70*k;s+=`<path data-edge="" data-source-entity="reference-${r.id}" data-target-entity="${r.id}" d="M ${x1} 148 L ${x1+5} 148 L ${x1+5} 222 L ${width-18} 222 L ${width-18} 378 L ${x2} 378 L ${x2} 396" fill="none" stroke="#426e91" stroke-width="2" marker-end="url(#sort-arrow)"/>`;}\n  }\n  return `<svg"""
assert s.count(old)==1;s=s.replace(old,new);p.write_text(s,encoding='utf-8')
