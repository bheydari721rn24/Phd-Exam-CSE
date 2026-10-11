from pathlib import Path
R=Path(__file__).resolve().parents[1];B=R/'research'
p=R/'dist/chapters/a_hash.js';s=p.read_text(encoding='utf-8')
s=s.replace('s.capacity>13)',"s.capacity>(s.operation==='horner'?31:13))").replace("Capacity must be an integer from 2 through 13.","Capacity must be 2–13, or 2–31 for polynomial arithmetic.")
s=s.replace("const row=(a,y,tag)","const row=(a,y,tag)")
s=s.replace("function snap(action,why,complete=false,formula=''){", """function snap(action,why,complete=false,formula=''){
if(!formula&&cursor!==null&&key!==null&&['open','shift','rebuild','robin'].includes(s.operation)){formula=`h(${key})=${key}\\\\bmod${s.capacity}=${mod(key,s.capacity)}`;if(s.operation==='shift'&&extra.distanceToHole!==undefined)formula=`D(h,u)=${extra.distanceToHole} \\\\quad D(h,v)=${extra.distanceToSlot}`;}
""")
s=s.replace("checks:[{mathHtml:'Completed operation checkpoint',result:String(z.complete)}]", """checks:(()=>{const a=[{mathHtml:'Operation is complete',result:String(z.complete)}];if(z.cursor!==null&&['open','shift','rebuild','robin'].includes(z.kind)){const v=z.slots[z.cursor];a.push({mathHtml:'Current slot is EMPTY',result:String(v===null)},{mathHtml:'Current slot is DELETED',result:String(v==='DELETED')});if(v&&typeof v==='object')a.push({mathHtml:'Current live key equals requested key',result:String(v.key===z.key)});}if(z.kind==='shift'&&z.extra.distanceToHole!==undefined)a.push({mathHtml:'Distance to hole is less than distance to current position',result:String(z.extra.distanceToHole<z.extra.distanceToSlot)});return a;})()""")
s=s.replace("'Place bucket '+b+' without collisions','The compact sample deterministically searches parameters; the written randomized theorem is separate.'", "'Place bucket '+b+' without collisions','Encode k as k+999 in the 2003-element prime field, then deterministically search affine parameters; the randomized theorem is separate.'")
p.write_text(s,encoding='utf-8')
p=B/'build_a_hash.py';s=p.read_text(encoding='utf-8')
s=s.replace("capacity=12,policy='double',step=8,keys=[0,12,24,36]", "capacity=12,policy='double',step=8,keys=[2,14,26,38]")
s=s.replace("capacity=13,base=5,keys=[3,1,4,1]", "capacity=17,base=5,keys=[1,2,3]")
s=s.replace("'Q4: exact polynomial prefix residues'", "'Q4: base-five polynomial prefix residues modulo seventeen'")
s=s.replace("('all-markers','Q38: a finite scan can reuse an all-tombstone table',dict(operation='open',capacity=3,keys=[0,1,2],commands=[dict(type='delete',key=k)for k in[0,1,2]]+[dict(type='put',key=9)]))", "('all-markers','Q38: one live key, nine markers and bounded reuse',dict(operation='open',capacity=10,keys=list(range(10)),commands=[dict(type='delete',key=k)for k in range(9)]+[dict(type='get',key=10),dict(type='put',key=10)]))")
s=s.replace("The laboratory evaluates the displayed code sequence [3,1,4,1] at base 5 and modulus 13; the written problem has its own stated arithmetic inputs.", "Exact companion for the first part: [1,2,3] at base five modulo seventeen. The written second part separately demonstrates the degenerate base eighteen.")
p.write_text(s,encoding='utf-8')
p=B/'verify_a_hash.py';s=p.read_text(encoding='utf-8').replace("assert by['all-markers']['result']['liveKeys']==[9]", "assert sorted(by['all-markers']['result']['liveKeys'])==[9,10]");p.write_text(s,encoding='utf-8')
print('Aligned numerical companions, exposed mathematical decision checks and clarified polynomial limits.')
