from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/g_mux.js';s=p.read_text(encoding='utf-8')
s=s.replace("checks:[{label:'Input domain',value:'validated'},{label:'Electrical scope',value:'logical model only'}]", "checks:[{mathHtml:'Input domain',result:'validated'},{mathHtml:'Electrical scope',result:'logical model only'}]")
s=s.replace("text(x+95,cy+6,p.phase>k?", "text(x+95,cy-9,p.phase>k?")
s=s.replace("[465,176],[555,176]", "[465,176],[660,176]")
s=s.replace("text(x-105,yy+6,'I'", "text(x-105,yy-9,'I'")
start=s.index('function integratedDiagram(');end=s.index('function cascadeDiagram(',start)
replacement=r'''function integratedDiagram(s,r,p){let b=text(30,34,'Full-adder, XOR, two inversions, and an addressed output')+text(30,72,'Ports are shown in descending index order, as in the original examination circuit.');
b+=rect(150,220,135,150)+text(166,251,'Full adder')+text(166,290,p.phase>0?'S = '+r.sum:'S = ?','mx-math')+text(166,341,p.phase>0?'C = '+r.carry:'C = ?','mx-math');
for(const[y,label,v]of[[245,'a',s.a],[285,'b',s.b],[350,'Cin',1]])b+=text(30,y+6,label+' = '+v,'mx-math')+wire([[100,y],[150,y]]);
b+=rect(370,122,105,75)+text(393,153,'XOR')+text(393,184,p.phase>1?'t = '+r.t:'t = ?','mx-math');
b+=wire([[285,280],[310,280],[310,142],[370,142]],p.phase>0)+wire([[285,330],[330,330],[330,178],[370,178]],p.phase>0)+`<circle cx="330" cy="330" r="3.5" fill="#426f82"/>`;
b+=wire([[330,330],[510,330],[510,304],[720,304]],p.phase>1)+wire([[330,330],[330,400],[585,400]],p.phase>1);
b+=wire([[475,158],[530,158],[530,228],[720,228]],p.phase>1)+wire([[530,158],[585,158]],p.phase>1)+`<circle cx="530" cy="158" r="3.5" fill="#426f82"/>`;
for(const[y,port]of[[158,152],[400,380]]){b+=`<path d="M585,${y-24} L625,${y} L585,${y+24} Z" fill="#edf4f7" stroke="#426f82" stroke-width="2"/><circle cx="631" cy="${y}" r="6" fill="white" stroke="#426f82" stroke-width="2"/>`+wire([[637,y],[678,y],[678,port],[720,port]],p.phase>1);}
b+=mux(720,120,110,300,'4:1');for(const[i,y]of[[3,152],[2,228],[1,304],[0,380]])b+=text(650,y-12,'I'+i+' = '+(p.phase>1?r.data[i]:'?'),'mx-math');
b+=wire([[830,270],[915,270]],p.phase>2)+text(930,276,p.phase>2?String(r.output):'?','mx-math')+wire([[772,476],[772,410]],p.phase>2)+text(670,510,'select = '+bin(s.address,2),'mx-math');return svg(b,540);}
'''
s=s[:start]+replacement+s[end:]
p.write_text(s,encoding='utf-8')
print('Connected every adder/XOR/inverter/MUX branch; fixed check labels and wire/value separation.')
