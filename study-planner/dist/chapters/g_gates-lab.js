(function(root){
  'use strict';
  const KINDS=['AND','OR','NAND','NOR','XOR','XNOR'];
  function gate(kind,bits){
    if(!KINDS.includes(kind)||!bits.length||bits.some(x=>x!==0&&x!==1))throw new Error('Invalid gate or bits.');
    const a=bits.every(Boolean)?1:0,o=bits.some(Boolean)?1:0,p=bits.reduce((s,x)=>s^x,0);
    return {AND:a,OR:o,NAND:1-a,NOR:1-o,XOR:p,XNOR:1-p}[kind];
  }
  function rows(kind,n){
    if(!Number.isInteger(n)||n<2||n>4)throw new Error('Input count must be 2, 3, or 4.');
    return Array.from({length:2**n},(_,i)=>{
      const bits=Array.from({length:n},(_,j)=>(i>>(n-1-j))&1);
      return {bits,multi:gate(kind,bits),cascade:bits.slice(1).reduce((v,x)=>gate(kind,[v,x]),bits[0])};
    });
  }
  function hazard(a,b,c,d){
    if([a,b,c,d].some(x=>!Number.isFinite(x)||x<0||x>20))throw new Error('Each delay must be a finite number from 0 to 20 ns.');
    const direct=b,complement=a+c,width=Math.max(0,complement-direct);
    return {direct,complement,width,fall:width>0?direct+d:null,rise:width>0?complement+d:null,protected:1};
  }
  const API={gate,rows,hazard};
  if(typeof module==='object'&&module.exports)module.exports=API;
  if(!root.document)return;
  root.GatesLab=API;
  const doc=root.document,$=id=>doc.getElementById(id);
  function cell(row,text){const c=doc.createElement('td');c.textContent=text;c.className='math-inline';row.append(c);}
  function renderGates(){
    const kind=$('gate-kind').value,n=Number($('gate-count').value),data=rows(kind,n);
    $('gate-table').tHead.innerHTML='';const hr=doc.createElement('tr');
    for(const s of ['Input vector','True '+n+'-input '+kind,'Binary left cascade','Agreement']){const th=doc.createElement('th');th.textContent=s;hr.append(th);}
    $('gate-table').tHead.append(hr);$('gate-table').tBodies[0].replaceChildren();
    for(const item of data){const tr=doc.createElement('tr');if(item.multi!==item.cascade)tr.className='mismatch';cell(tr,item.bits.join(''));cell(tr,item.multi);cell(tr,item.cascade);const td=doc.createElement('td');td.textContent=item.multi===item.cascade?'Matches':'Different';tr.append(td);$('gate-table').tBodies[0].append(tr);}
    const mismatches=data.filter(x=>x.multi!==x.cascade).length;
    $('gate-status').textContent=mismatches===0?'The true multi-input function and this binary cascade agree on every row.':`${mismatches} rows differ. A cascade does not preserve this multi-input definition.`;
    $('gate-status').dataset.mismatches=String(mismatches);
  }
  const NS='http://www.w3.org/2000/svg';
  function el(tag,attrs,text){const e=doc.createElementNS(NS,tag);for(const [k,v]of Object.entries(attrs))e.setAttribute(k,v);if(text!==undefined)e.textContent=text;return e;}
  function waveform(r,a,b,c,d){
    const svg=$('haz-wave');svg.replaceChildren();const end=Math.max(8,a+c+d+3,b+d+3),X=t=>150+610*t/end;
    const traces=[['Select',[[0,0]]],['Direct product',[[b,0]]],['Complemented product',[[a+c,1]]],['Unprotected output',r.width>0?[[r.fall,0],[r.rise,1]]:[]],['Protected output',[]]];
    const initial=[1,1,0,1,1];
    traces.forEach(([name,events],i)=>{
      const baseline=42+i*51,hi=baseline-16,lo=baseline+6,Y=v=>v?hi:lo;let previous=initial[i];
      let path=`M ${X(0)} ${Y(previous)}`;
      events.forEach(([t,v])=>{path+=` H ${X(t)} V ${Y(v)}`;previous=v;});path+=` H ${X(end)}`;
      svg.append(el('text',{x:8,y:baseline,class:'diagram-label'},name),el('path',{d:path,fill:'none',stroke:i===3?'#b04428':'#176579','stroke-width':2.5}));
    });
    svg.append(el('path',{d:'M150 292H760',fill:'none',stroke:'currentColor'}));
    for(let i=0;i<=4;i++){const t=end*i/4;svg.append(el('path',{d:`M${X(t)} 290v6`,stroke:'currentColor'}),el('text',{x:X(t),y:315,'text-anchor':'middle',class:'math-label'},Number(t.toFixed(2))+' ns'));}
  }
  function renderHazard(){
    try{
      const ids=['haz-inv','haz-direct','haz-comp','haz-or'];
      if(ids.some(id=>$(id).value.trim()===''))throw new Error('Enter all four delays.');
      const [a,b,c,d]=ids.map(id=>Number($(id).value)),r=hazard(a,b,c,d);
      const status=$('haz-status');status.dataset.valid='true';status.dataset.width=String(r.width);
      status.textContent=r.width>0?`The unprotected output has a ${r.width} ns low pulse from ${r.fall} to ${r.rise} ns. The settled consensus branch keeps the protected output high.`:'The two products overlap or switch together: this transition produces no low pulse in the specified transport model. The protected output also stays high.';
      const events=[[0,'Select falls','The stable endpoint function remains one.'],[a,'Inverted select rises','The complemented branch can now respond.'],[b,'Direct product falls','This branch stops holding the OR high.'],[a+c,'Complemented product rises','This branch starts holding the OR high.']];
      if(r.width>0)events.push([r.fall,'Unprotected output falls','Transported beginning of the low pulse.'],[r.rise,'Unprotected output rises','Transported end of the low pulse.']);
      events.sort((u,v)=>u[0]-v[0]);$('haz-events').tBodies[0].replaceChildren();
      for(const [t,event,meaning]of events){const tr=doc.createElement('tr');cell(tr,t);for(const s of[event,meaning]){const td=doc.createElement('td');td.textContent=s;tr.append(td);}$('haz-events').tBodies[0].append(tr);}
      waveform(r,a,b,c,d);
    }catch(e){$('haz-status').dataset.valid='false';delete $('haz-status').dataset.width;$('haz-status').textContent=e.message;$('haz-events').tBodies[0].replaceChildren();$('haz-wave').replaceChildren();}
  }
  ['gate-kind','gate-count'].forEach(id=>$(id).addEventListener('change',renderGates));
  ['haz-inv','haz-direct','haz-comp','haz-or'].forEach(id=>$(id).addEventListener('input',renderHazard));
  renderGates();renderHazard();
})(typeof window==='undefined'?{}:window);
