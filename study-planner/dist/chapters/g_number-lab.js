/* Exact abstract fixed-width words. Inputs denote unsigned stored words. */
(() => {
  'use strict';
  function model(width, a, b, operation) {
    if (!Number.isInteger(width) || width < 2 || width > 16 || !['add','sub'].includes(operation)) throw new Error('Invalid model contract');
    const n = BigInt(width), modulus = 1n << n, top = modulus >> 1n;
    if (a < 0n || b < 0n || a >= modulus || b >= modulus) throw new Error('Operand outside word range');
    const signed = u => u >= top ? u - modulus : u;
    const bits = u => u.toString(2).padStart(width, '0');
    const sub = operation === 'sub', operand = sub ? modulus - 1n - b : b;
    let carry = sub ? 1n : 0n, word = 0n;
    const trace = [];
    for (let i = 0; i < width; i++) {
      const shift = BigInt(i), aa = (a >> shift) & 1n, bb = (operand >> shift) & 1n;
      const incoming = carry, sum = aa + bb + incoming, result = sum & 1n;
      carry = sum >> 1n; word |= result << shift;
      trace.push([i, aa, bb, incoming, result, carry].map(String));
    }
    const exactUnsigned = sub ? a - b : a + b;
    const exactSigned = sub ? signed(a) - signed(b) : signed(a) + signed(b);
    const overflow = exactSigned < -top || exactSigned >= top;
    const carryXor = trace[width-1][3] !== trace[width-1][5];
    if (carryXor !== overflow) throw new Error('Internal flag disagreement');
    const gray = a ^ (a >> 1n);
    return {width, operation, a:String(a), b:String(b), signedA:String(signed(a)), signedB:String(signed(b)), word:String(word), binary:bits(word), signedResult:String(signed(word)), exactUnsigned:String(exactUnsigned), exactSigned:String(exactSigned), carry:String(carry), borrow:sub ? String(1n-carry) : null, overflow:String(overflow), gray:bits(gray), trace};
  }
  window.numberWordModel = model;
  const byId = id => document.getElementById(id);
  const result = byId('number-result'), body = byId('number-trace');
  if (!result || !body) return;
  function update() {
    try {
      const rawW = byId('number-width').value, rawA = byId('number-a').value, rawB = byId('number-b').value;
      if (![rawW,rawA,rawB].every(x => /^\d+$/.test(x))) throw new Error('Enter whole, nonnegative decimal values in every field.');
      const w = Number(rawW), a = BigInt(rawA), b = BigInt(rawB);
      if (!Number.isInteger(w) || w < 2 || w > 16) throw new Error('Choose a width from two through sixteen bits.');
      const maximum = (1n << BigInt(w)) - 1n;
      if (a > maximum || b > maximum) throw new Error(`For this width, each stored word must be between 0 and ${maximum}.`);
      const m = model(w,a,b,byId('number-operation').value);
      Object.assign(result.dataset, {valid:'true',word:m.word,signed:m.signedResult,carry:m.carry,borrow:m.borrow ?? '',overflow:m.overflow,gray:m.gray});
      const fields = [
        ['First word: unsigned / signed', `${m.a} / ${m.signedA}`],
        ['Second word: unsigned / signed', `${m.b} / ${m.signedB}`],
        ['Exact unsigned arithmetic', m.exactUnsigned],
        ["Exact two's complement arithmetic", m.exactSigned],
        ['Retained result word', m.binary],
        ['Retained result: unsigned / signed', `${m.word} / ${m.signedResult}`],
        [m.operation==='sub' ? 'Final carry (no borrow) / borrow' : 'Final unsigned carry', m.operation==='sub' ? `${m.carry} / ${m.borrow}` : m.carry],
        ['Signed overflow', m.overflow==='true' ? '1' : '0'],
        ['Gray encoding of first unsigned index', m.gray],
        ['Carry into / out of sign bit', `${m.trace[w-1][3]} / ${m.trace[w-1][5]}`]
      ];
      result.innerHTML = `<div class="number-results">${fields.map(([label,value])=>`<div><span class="label">${label}</span><span class="math-inline">${value}</span></div>`).join('')}</div><p class="number-summary">${m.overflow==='true' ? 'The exact signed answer is outside the declared signed range; the retained word is its modular residue.' : 'The exact signed answer fits the declared signed range and matches the decoded retained word.'}</p>`;
      body.innerHTML = m.trace.map(row=>`<tr>${row.map(x=>`<td>${x}</td>`).join('')}</tr>`).join('');
    } catch(error) {
      Object.assign(result.dataset,{valid:'false',word:'',signed:'',carry:'',borrow:'',overflow:'',gray:''});
      result.replaceChildren(); const p = document.createElement('p');p.className='lab-error';p.textContent=error.message;result.append(p);body.replaceChildren();
    }
  }
  for(const id of ['number-width','number-a','number-b','number-operation']) byId(id).addEventListener('input',update);
  update();
})();
