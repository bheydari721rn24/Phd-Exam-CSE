/* Exact binary expression model. No eval, network calls, or physical simulation. */
(function(root){
  'use strict';
  function parse(source){
    if(typeof source!=='string'||source.length>300)throw Error('Use at most 300 characters.');
    const s=source.replace(/\s+/g,'');let p=0;
    if(!s.length)throw Error('Enter an expression.');
    function atom(){
      const c=s[p++];
      if(c==='!')return ['not',atom()];
      if(c==='('){const v=or();if(s[p++]!==')')throw Error('A closing parenthesis is missing.');return v;}
      if(c==='0'||c==='1')return ['constant',Number(c)];
      if(c==='x'||c==='y'||c==='z')return ['variable',c];
      throw Error('Expected x, y, z, 0, 1, !, or a parenthesized expression.');
    }
    function chain(next,op){let n=next();while(s[p]===op){p++;n=[op,n,next()];}return n;}
    function and(){return chain(atom,'&');}
    function xor(){return chain(and,'^');}
    function or(){return chain(xor,'|');}
    const ast=or();if(p!==s.length)throw Error('Unexpected character. Use explicit &, ^, and | operators.');return ast;
  }
  function evaluate(n,env){
    switch(n[0]){
      case 'constant':return n[1];case 'variable':return env[n[1]];
      case 'not':return 1-evaluate(n[1],env);
      case '&':return evaluate(n[1],env)&evaluate(n[2],env);
      case '^':return evaluate(n[1],env)^evaluate(n[2],env);
      case '|':return evaluate(n[1],env)|evaluate(n[2],env);
      default:throw Error('Invalid internal expression node.');
    }
  }
  function analyze(first,second,variable){
    if(!['x','y','z'].includes(variable))throw Error('Select x, y, or z.');
    const f=parse(first),g=parse(second),rows=[];
    for(let i=0;i<8;i++){const env={x:(i>>2)&1,y:(i>>1)&1,z:i&1};const a=evaluate(f,env),b=evaluate(g,env);rows.push({bits:[env.x,env.y,env.z],a,b,mismatch:a^b});}
    const other=['x','y','z'].filter(v=>v!==variable),cofactors=[];
    for(let i=0;i<4;i++){const env={[other[0]]:i>>1,[other[1]]:i&1};env[variable]=0;const zero=evaluate(f,env);env[variable]=1;const one=evaluate(f,env);cofactors.push({bits:[i>>1,i&1],zero,one,difference:zero^one,universal:zero&one,existential:zero|one});}
    const positive=cofactors.every(r=>r.zero<=r.one),negative=cofactors.every(r=>r.one<=r.zero),independent=positive&&negative;
    return {rows,other,cofactors,equivalent:rows.every(r=>!r.mismatch),counterexample:rows.find(r=>r.mismatch)?.bits??null,positive,negative,independent};
  }
  const api={parse,evaluate,analyze};if(typeof module!=='undefined'&&module.exports)module.exports=api;root.BooleanLab=api;
  if(typeof document==='undefined')return;
  const first=document.getElementById('bool-first'),second=document.getElementById('bool-second'),variable=document.getElementById('bool-variable');if(!first)return;
  const status=document.getElementById('bool-status'),table=document.querySelector('#bool-table tbody'),cofTable=document.querySelector('#bool-cofactors tbody'),head=document.querySelector('#bool-cofactors thead'),classification=document.getElementById('bool-classification');
  function row(values,mismatch=false){const tr=document.createElement('tr');if(mismatch)tr.className='mismatch-row';for(const value of values){const td=document.createElement('td');td.textContent=String(value);tr.append(td);}return tr;}
  function update(){
    table.replaceChildren();cofTable.replaceChildren();head.replaceChildren();classification.textContent='';
    try{
      const r=analyze(first.value,second.value,variable.value);status.dataset.valid='true';status.dataset.equivalent=String(r.equivalent);status.className='';
      status.replaceChildren(document.createTextNode(r.equivalent?'Equivalent on all eight assignments.':'Not equivalent. First counterexample, in x, y, z order: '));
      if(r.counterexample){const span=document.createElement('span');span.className='math-inline';span.textContent=r.counterexample.join('');status.append(span);}
      for(const a of r.rows)table.append(row([...a.bits,a.a,a.b,a.mismatch],!!a.mismatch));
      const tr=document.createElement('tr');for(const title of [...r.other,'At zero','At one','Difference','For all','Exists']){const th=document.createElement('th');th.textContent=title;if(r.other.includes(title))th.className='math-inline';tr.append(th);}head.append(tr);
      for(const a of r.cofactors)cofTable.append(row([...a.bits,a.zero,a.one,a.difference,a.universal,a.existential]));
      classification.dataset.independent=String(r.independent);classification.dataset.positive=String(r.positive);classification.dataset.negative=String(r.negative);
      classification.textContent=r.independent?'The selected input is independent: its cofactors agree on all four contexts.':r.positive?'The selected input is essential and positive unate: changing zero to one never lowers the output.':r.negative?'The selected input is essential and negative unate: changing zero to one never raises the output.':'The selected input is binate: some contexts rise and others fall when it changes from zero to one.';
    }catch(e){status.dataset.valid='false';delete status.dataset.equivalent;status.className='lab-error';status.textContent=e.message;for(const key of ['independent','positive','negative'])delete classification.dataset[key];}
  }
  [first,second,variable].forEach(el=>el.addEventListener('input',update));
  document.getElementById('bool-example').addEventListener('click',()=>{first.value='(x & y) | (x & z) | (y & z)';second.value='(x & y) ^ (x & z) ^ (y & z)';variable.value='x';update();});
  update();
})(typeof globalThis!=='undefined'?globalThis:this);
