"""Repair positional identities and add explicit operands/dependencies to reviewed views."""
from pathlib import Path
R=Path(__file__).resolve().parents[1];P=R/'dist/chapters/semantic-diagrams.js'
def section(s,a,b,value):i=s.index(a);j=s.index(b,i);return s[:i]+value+s[j:]
def main():
 s=P.read_text(encoding='utf-8')
 s=section(s,'function bars(','\nfunction search(','''function bars(p,g,f,pos){
 const a=f.snapshot?.array,records=f.nodes.filter(n=>/^(r|record)\\d+$/.test(n.id)),n=a?.length||records.length;
 if(p.scene.id==='max-subarray'){const selected=({total:[0,7],prefix:[0,5],suffix:[6,7],best:[2,5]}[f.metrics.Component]);text(g,380,40,`${f.metrics.Component}: selected indices [${selected[0]}, ${selected[1]})`,21);records.forEach((r,i)=>{rect(g,55+i*88,120,78,60,i>=selected[0]&&i<selected[1]?'#cce9dc':'#edf5f8');text(g,94+i*88,158,r.label.split(' · ')[0],23);text(g,94+i*88,209,i,16);});text(g,380,290,'The four summary components use different allowed index ranges.',20);return;}
 for(let i=0;i<n;i++){rect(g,49+92*i,75,82,60,'#fafcfd','#b9cbd4');text(g,90+92*i,172,i,16);}
 text(g,380,34,'Fixed array slots; the lower labels are indices',20);
 for(const r of records){const q=pos.get(r.id)||r,held=r.y>200,y=held?q.y:q.y-5,group=E('g',{'data-record':r.id,transform:`translate(${q.x} ${y})`});rect(group,-41,-25,82,54,r.tone==='active'?'#ffe0a1':r.tone==='done'?'#cce9dc':'#edf5f8');const [key,tag]=r.label.split(' · ');text(group,0,-2,key,23);if(tag)text(group,0,19,tag,14);g.append(group);p.nodes.set(r.id,group);}
 if(f.snapshot?.saved){text(g,610,255,'Saved record outside storage',18);text(g,610,285,'The hole is not a second copy.',17);}
 const h=f.nodes.find(n=>n.id==='hole');if(h){const q=pos.get(h.id)||h;path(g,`M${q.x-30} 99h60`,C.amber,2,{'stroke-dasharray':'5 4'});text(g,q.x,130,'hole',16);}
 if(f.snapshot&&'lt' in f.snapshot){const z=f.snapshot;[[0,z.lt,'< pivot'],[z.lt,z.i,'= pivot'],[z.i,z.gt,'unknown'],[z.gt,n,'> pivot']].forEach(([lo,hi,label],j)=>{text(g,115+j*175,245,label,18);text(g,115+j*175,277,`[${lo}, ${hi})`,18);path(g,`M${60+j*175} 299h110`,[C.green,C.blue,C.amber,C.green][j],4);});}
}
''')
 s=section(s,'function truth(','\nfunction graph(','''function truth(p,g,f){
 const rows=[...new Map(p.scene.frames.filter(x=>x.snapshot?.inputs).map(r=>[JSON.stringify(r.snapshot.inputs),r])).values()],arity=rows[0]?.snapshot.inputs.length||2,inputs=f.snapshot?.inputs||[];
 const cols=arity+2,dx=Math.min(110,580/cols),x=(760-cols*dx)/2,y=66,h=Math.min(42,235/rows.length);
 [...Array(arity)].map((_,i)=>String.fromCharCode(112+i)).concat(['Left','Right']).forEach((v,i)=>text(g,x+(i+.5)*dx,y-20,v,20));
 rows.forEach((r,k)=>{const active=JSON.stringify(r.snapshot.inputs)===JSON.stringify(inputs);rect(g,x,y+k*h,cols*dx,h,active?'#ffe0a1':'#fff','#bed0d8');[...r.snapshot.inputs,r.snapshot.left,r.snapshot.right].forEach((v,i)=>text(g,x+(i+.5)*dx,y+k*h+h/2+7,v,19));});
 text(g,380,335,'One row per complete valuation; both expressions receive the same inputs.',18);
}
''')
 # Show actual source operands and accumulator update, outside the matrix entry area.
 old='if(s.op)text(g,380,330,s.op,21);'
 new='''if(id==='matrix-product'){
 const A=[[1,2],[3,4]],B=[[2,0],[1,2]],left=A[s.i][s.k],right=B[s.k][s.j],after=num(s.C[s.i][s.j]),before=after-left*right;
 text(g,380,285,`Accumulate C[${s.i},${s.j}]: ${before} + (${left} × ${right}) = ${after}`,23);
 text(g,380,330,`A[${s.i},${s.k}] and B[${s.k},${s.j}] share inner index ${s.k}.`,19);
 }if(s.op)text(g,380,330,s.op,21);'''
 assert old in s;s=s.replace(old,new,1)
 # Fixed storage representation does not change when the traversal order changes.
 s=s.replace('title:`${s.order}-major offsets`','title:"Physical offsets: row-major storage"')
 # Partial truth-table samples are cases, not a continuous electrical transition.
 # The waveform cursor retains event timing and history but hides unscheduled future samples.
 s=s.replace('history.forEach((a,j)=>{if(j)points.push','history.slice(0,p.index+1).forEach((a,j)=>{if(j)points.push')
 P.write_text(s,encoding='utf-8')
 print('Updated record identity, fixed indices, unique truth rows, matrix arithmetic, storage order and event reveal.')
if __name__=='__main__':main()
