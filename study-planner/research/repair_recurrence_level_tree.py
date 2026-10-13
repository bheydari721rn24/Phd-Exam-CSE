from pathlib import Path
p=Path(__file__).parent.parent/'dist/chapters/semantic-diagrams.js';s=p.read_text();a=s.index('if(p.scene.id==="recurrence-levels")');z=s.index('return;}',a)+len('return;}')
v='''if(p.scene.id==="recurrence-levels"){
 const depth=+f.metrics.Level,tip='recurrence-level-tip-'+p.index,defs=E('defs'),marker=E('marker',{id:tip,markerWidth:7,markerHeight:6,refX:7,refY:3,orient:'auto',markerUnits:'userSpaceOnUse'});marker.append(E('path',{d:'M0 0L7 3L0 6Z',fill:C.blue}));defs.append(marker);g.append(defs);
 const points=[];
 for(let d=0;d<=depth;d++){const count=2**d;for(let i=0;i<count;i++)points.push({d,i,x:70+(i+.5)*620/count,y:65+62*d});}
 points.filter(v=>v.d>0).forEach(B=>{const A=points.find(v=>v.d===B.d-1&&v.i===Math.floor(B.i/2)),dx=B.x-A.x,dy=B.y-A.y,L=Math.hypot(dx,dy),P=[A.x+16*dx/L,A.y+16*dy/L],Q=[B.x-16*dx/L,B.y-16*dy/L],q=path(g,`M${P}L${Q}`,C.blue,1.4);q.setAttribute('marker-end','url(#'+tip+')');q.dataset.recurrencePorts=P.concat(Q).join(',');});
 points.forEach(v=>{dot(g,v.x,v.y,16,v.d===depth?C.amber:C.blue);const t=text(g,v.x,v.y+6,8/2**v.d,17,'middle','white');t.style.setProperty('font-family','"STIX Two Math"','important');t.style.setProperty('font-size','17px','important');});
 const t=text(g,380,292,`Complete depth ${depth}: each shown node contributes its stated local cost`,14,'middle',C.ink);t.style.setProperty('font-family','"Source Sans 3"','important');t.style.setProperty('font-size','14px','important');vectorNative(g,f.formulaHtml,30,309,700,40);return;}
'''
s=s[:a]+v+s[z:]
old='p.scene.id.startsWith("algorithm-recurrence-question-")||';new='p.scene.id==="recurrence-levels"||'+old
if new not in s:s=s.replace(old,new)
p.write_text(s,encoding='utf8')
