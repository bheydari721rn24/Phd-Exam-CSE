function booleanQuestion(p,g,f){
 const s=f.snapshot,box=(x,y,w,h,v,fill='#eef5f8')=>{rect(g,x,y,w,h,fill,'#abc4cf');text(g,x+w/2,y+h/2+6,v,17);};
 const head=v=>text(g,380,30,v,19),formula=()=>vectorNative(g,f.formulaHtml,25,298,710,55);
 if(s.kind==='table'){
  head(p.scene.title);const rows=s.stage===0?[]:s.rowsHtml;booleanTable(g,rows,s.headings,35,69,690,185,s.stage===2?-1:0);
  if(s.stage===0)text(g,380,167,'Inputs and column meanings are established; derived rows follow.',17);
  text(g,380,282,s.stage===2?'All rows or classes shown are checked against the named domain.':'Advance to derive the complete table or the displayed representatives.',15);formula();return;
 }
 if(s.kind==='nand'){
  head(`Original input x=${s.x}, y=${s.y}: difference and borrow`);
  const gate=(x,y,label,value,known)=>{path(g,`M${x} ${y}h24a24 24 0 0 1 0 48h-24Z`,C.ink,1.5);g.append(E('circle',{cx:x+53,cy:y+24,r:5,fill:'white',stroke:C.ink,'stroke-width':1.5}));text(g,x+24,y+29,label,16);text(g,x+85,y+58,known?value:'·',18);};
  gate(140,146,'t',s.t,s.stage>=1);gate(345,90,'u',s.u,s.stage>=2);gate(345,205,'v',s.v,s.stage>=2);gate(562,102,'F1',s.f1,s.stage>=3);gate(562,216,'F2',s.f2,s.stage>=3);
  text(g,50,82,'x = '+s.x,17);text(g,50,268,'y = '+s.y,17);
  // Separate primary rails and named fan-out junctions; wire endpoints attach to gate ports.
  path(g,'M55 92H98V158H140M98 92H320V102H345M55 248H113V181H140M113 248H320V238H345',C.blue,1.5);
  dot(g,98,92,3);dot(g,113,248,3);
  path(g,'M198 170H285V125H345M285 170V220H345',s.stage>=1?C.green:C.blue,1.5);dot(g,285,170,3);
  path(g,'M403 114H495V114H562M403 229H472V137H562M472 229H533V228H562M533 228V251H562',s.stage>=2?C.green:C.blue,1.5);dot(g,472,229,3);dot(g,533,228,3);
  path(g,'M620 126H720M620 240H720',s.stage>=3?C.green:C.blue,1.5);
  text(g,680,105,'difference',15);text(g,680,220,'borrow',15);formula();return;
 }
 if(s.kind==='mux'){
  head(`Original select pins a=${s.a}, b=${s.b}`);
  const mux=(x,y)=>{path(g,`M${x} ${y}L${x+75} ${y+22}V${y+107}L${x} ${y+130}Z`,C.ink,1.5);text(g,x+20,y+35,'0',17);text(g,x+20,y+105,'1',17);};
  mux(190,73);mux(470,112);text(g,105,108,'data 1',17);text(g,105,178,'data 0',17);text(g,385,217,'data 0',17);
  path(g,'M145 104H190M145 174H190M265 138H400V143H470M420 213H470M545 177H700',C.blue,1.6);
  text(g,330,119,s.stage>=1?'t = '+s.t:'t pending',17);text(g,648,160,s.stage>=2?'F = '+s.out:'F pending',17);
  path(g,'M230 259V192M510 271V231',C.blue,1.6);text(g,230,280,'select b = '+s.b,16);text(g,510,286,'select a = '+s.a,16);formula();return;
 }
 if(s.kind==='hazard'){
  head('Single-input timing contract; time units are illustrative');
  const names=['a','ab','not-a · c','original Y','bridged Y'],xs=[150,220,320,370,420,470,570],times=s.times;
  text(g,680,70,'time',15);xs.forEach((x,i)=>text(g,x,68,times[i],14));
  names.forEach((name,j)=>{const y=100+j*34;text(g,115,y+4,name,15,'end');if(j>0&&s.stage===0)return;if(j===3&&s.stage<2)return;if(j===4&&s.stage<3)return;let d=`M${xs[0]} ${y+(s.signals[j][0]?0:17)}`;for(let i=1;i<xs.length;i++)d+=`H${xs[i]}V${y+(s.signals[j][i]?0:17)}`;path(g,d,j===4?C.green:j===3?C.red:C.blue,2);});
  text(g,380,280,'b=c=1 stay stable; original output is low from time 4 to 6.',15);formula();return;
 }
 throw Error('Unknown Boolean mechanism '+s.kind);
}
function booleanTable(g,rows,headings,x,y,w,h,activeIndex){
 const node=E('foreignObject',{x,y,width:w,height:h}),div=document.createElementNS('http://www.w3.org/1999/xhtml','div');div.style.cssText="font:14px 'Source Sans 3',sans-serif;width:100%;height:100%;overflow:auto";
 const table=document.createElement('table');table.style.cssText='display:table;width:100%;table-layout:fixed;border-collapse:collapse;margin:0;font-size:14px;line-height:1';
 const tr=document.createElement('tr');headings.forEach(v=>{const c=document.createElement('th');c.textContent=v;c.style.cssText='padding:3px 7px;text-align:left;font-size:14px;line-height:1.15;background:#edf4f8';tr.append(c);});table.append(tr);
 rows.forEach((r,i)=>{const tr=document.createElement('tr');r.forEach(v=>{const c=document.createElement('td');c.innerHTML=v;c.querySelectorAll('math').forEach(m=>m.style.cssText="font-size:14px;font-family:'STIX Two Math';margin:0");c.style.cssText='padding:0 7px;text-align:left;font-size:14px;line-height:1;border-bottom:1px solid white;background:'+(i===activeIndex?'#e0eee7':'#f5f8fa');tr.append(c);});table.append(tr);});div.append(table);node.append(div);g.append(node);
}
