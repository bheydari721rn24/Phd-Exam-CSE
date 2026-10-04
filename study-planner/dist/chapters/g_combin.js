(()=>{
 'use strict';
 function solve(mode,bits,faulty=false){
  if(!['shared','priority','nand'].includes(mode)||bits.length!==4||bits.some(x=>x!==0&&x!==1))throw Error('Choose one mode and four binary input bits.');
  const [a,b,c,d]=bits;let values,reference,candidate;
  if(mode==='shared'){
   const p=a&b,q=c|d,r=p&q;
   values=[['AB',p],['C+D',q],['r',r],['Y',r],['Z',(a&b)|c]];
   reference=[r,p|c];candidate=[r,r|c];
  }else if(mode==='priority'){
   const g1=a&b,g0=a&(1-b)&c,v=a&(b|c);
   values=[['G1',g1],['G0',g0],['valid',v]];
   reference=[g1,g0,v];candidate=[g1,a&c,v];
  }else{
   const p=1-(a&b),q=1-(a&c),y=1-(p&q);
   values=[['not AB',p],['not AC',q],['final NAND',y]];
   reference=[a&(b|c)];candidate=[1-((1-(a&b))&c)];
  }
  const actual=faulty?candidate:reference;
  return {mode,bits,values,reference,candidate:actual,miter:reference.some((x,i)=>x!==actual[i])?1:0,cost:mode==='shared'?{gates:4,depth:3}:mode==='priority'?{gates:6,depth:3}:{gates:3,depth:2}};
 }
 function all(mode,faulty){return Array.from({length:16},(_,i)=>solve(mode,[i>>3&1,i>>2&1,i>>1&1,i&1],faulty));}
 window.CombinLab={solve,all};
 const form=document.getElementById('combin-form'),out=document.getElementById('combin-output'),host=document.getElementById('combin-player');
 if(!form)return;
 function update(event){if(event)event.preventDefault();const mode=form.elements.mode.value,bits=['a','b','c','d'].map(x=>Number(form.elements[x].value)),fault=form.elements.variant.value==='faulty';
  try{
   const result=solve(mode,bits,fault),table=all(mode,fault),diff=table.flatMap((x,i)=>x.miter?[i]:[]);
   out.dataset.result=JSON.stringify(result);out.dataset.table=JSON.stringify(table);out.dataset.valid='true';
   const convention=mode==='shared'?'Output order is Y then Z.':mode==='priority'?'A is enable E, B is request R1, C is request R0, and D is unused. Output order is G1, G0, validity.':'D is unused. The single output is A AND (B OR C).';
   out.innerHTML='<p>'+convention+'</p><p><strong>Input:</strong> '+bits.join('')+'. <strong>Reference output:</strong> '+result.reference.join('')+'. <strong>Candidate output:</strong> '+result.candidate.join('')+'.</p><p><strong>All discrepancy indices:</strong> '+(diff.join(', ')||'none')+'. ABCD binary order is used even when D is unused.</p><p><strong>Reference circuit cost:</strong> '+result.cost.gates+' two-input gates; maximum depth '+result.cost.depth+'. Counts include required inversion; fan-out buffers are not modeled.</p><table><thead><tr><th>ABCD</th><th>Reference</th><th>Candidate</th><th>Miter</th></tr></thead><tbody>'+table.map(x=>'<tr><td>'+x.bits.join('')+'</td><td>'+x.reference.join('')+'</td><td>'+x.candidate.join('')+'</td><td>'+x.miter+'</td></tr>').join('')+'</tbody></table>';
   const values=result.values;
   const frames=values.map((_,k)=>({nodes:values.map(([key,v],j)=>({id:'value'+j,label:key+'\n'+(j<=k?v:'pending'),x:110+125*j,y:115,w:116,h:64,kind:'card',tone:j===k?'active':j<k?'done':'plain',size:19})).concat({id:'token',label:'evaluate '+(k+1),x:110+125*k,y:260,w:116,h:42,kind:'card',tone:'active',size:18}),edges:[],captionHtml:'<p>Evaluate internal stage '+(k+1)+' using its already determined predecessors. This checkpoint uses the selected current inputs; the complete miter table independently checks every binary row.</p>',caption:'Evaluate the next stage using known predecessors while the complete miter checks every binary row.',metrics:{'evaluated stages':k+1},metricLabels:{'evaluated stages':'evaluated stages'},formula:'',formulaHtml:'',line:0,snapshot:{mode,bits,computed:values.slice(0,k+1)}}));
   host.hidden=false;
   ConceptAnimations.mount(host,[{id:'combin-custom-'+mode,title:'Exact topological evaluation: '+mode,descriptionHtml:'<p>Internal values advance in dependency order. The selected faulty variant is compared by the separate complete table.</p>',invariantHtml:'<p>Settled two-valued logic; reference costs use the declared two-input gate topology.</p>',frames,code:[]}]);
  }catch(err){out.dataset.valid='false';out.textContent=err.message;host.hidden=true;}
 }
 form.addEventListener('input',update);form.addEventListener('submit',update);
 document.querySelectorAll('.combin-diagram').forEach(fig=>{const b=document.createElement('button');b.className='combin-figure-toggle';b.type='button';b.textContent='Enlarge diagram';b.addEventListener('click',()=>{fig.classList.toggle('expanded');b.textContent=fig.classList.contains('expanded')?'Fit diagram':'Enlarge diagram';});fig.prepend(b);});
 function ready(){if(window.ConceptAnimations)update();else setTimeout(ready,50);}ready();
})();
