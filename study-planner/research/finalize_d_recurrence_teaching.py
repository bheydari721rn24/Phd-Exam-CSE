from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/d_recurrence.js';s=p.read_text(encoding='utf-8')
f=r'''function operationText(s,z,r){
 if(s.operation==='unrolling')return z.step?'Add contribution '+z.terms.at(-1).value+' from injection index '+z.step+'; the accumulated sum becomes '+z.sum+'.':'Start with the initial value propagated to the target, equal to '+z.base+'.';
 if(s.operation==='differences')return z.step?'Subtract each earlier entry from its right neighbor to obtain difference order '+z.step+'.':'Read the quadratic sample row before taking any differences.';
 if(s.operation==='boundary')return z.step<3?'Retain the independently specified value at index '+z.step+'.':'Double the preceding tail value to obtain index '+z.step+'.';
 if(s.operation==='tiling')return z.step?'Inspect complete covering '+z.step+' and classify it by its first placement.':'Read the empty rectangular board before enumerating complete coverings.';
 if(s.operation==='resonance')return z.step<2?'Retain a normalized boundary value before the second-difference equation applies.':'The preceding two normalized values give the next value with constant second difference one.';
 if(s.operation==='automaton')return z.step===1?'Initialize each possible last-symbol count to one at length one.':'From preceding counts '+(z.v-z.u)+' and '+(2*z.u-z.v)+', update the restricted-ending count to '+z.u+' and the unrestricted-ending count to '+z.v+'.';
 if(s.operation==='derangements')return z.step<2?'Use the empty-permutation or one-element boundary, rather than an unavailable negative index.':'Combine '+z.two+' two-cycle cases and '+z.long+' longer-cycle cases after accounting for every image choice.';
 if(s.operation==='partitions')return z.step?'For each block count, combine a new singleton with insertion into one of the existing blocks.':'Initialize the unique empty partition in the zero-block column.';
 if(s.operation==='ferrers')return z.case+'; the right diagram shows its exact reduced partition.';
 if(s.operation==='catalan')return z.step?'Locate the first return at step '+z.split+' to separate the enclosed and following path.':'Begin enumeration of all valid nonnegative paths of the declared size.';
 if(s.operation==='conjugate')return z.step?'Swap every cell coordinate; the transposed diagram preserves all seven cells.':'Read the original row lengths before transposition.';
 if(s.operation==='reflection')return z.step?'Swap up and down steps only in the prefix through the first negative-one visit.':'Locate the first crossing below zero in a bad balanced path.';
 if(s.operation==='modular')return z.returnTo===undefined?'Replace the pair by its second residue and the sum of both residues, reduced modulo '+s.modulus+'.':'The complete starting pair returns, proving the displayed period of '+r.period+'.';
 return 'Multiply the latest term by five, subtract six times the preceding term, and shift the pair forward.';
}
function exactStateMath(s,z,r){const name=s.operation==='unrolling'?'W':['derangements'].includes(s.operation)?'D':s.operation==='partitions'?'B':s.operation==='resonance'?'a':s.operation==='automaton'||s.operation==='tiling'?'T':'a';let value=z.sum??z.value??z.total??z.bell??z.a??(z.values?.at(-1));if(value===undefined&&s.operation==='tiling')value=r.count;if(value===undefined)return '';return '<math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msub><mi>'+name+'</mi><mn>'+z.step+'</mn></msub><mo>=</mo><mn>'+esc(value)+'</mn></mrow></math>';}
'''
assert 'function operationText'not in s;s=s.replace('function makeModel(id,title,raw){',f+'function makeModel(id,title,raw){')
s=s.replace('formula:frameFormula(s,z,r),snapshot:', 'formula:frameFormula(s,z,r),formulaHtml:exactStateMath(s,z,r),snapshot:')
s=s.replace("operation:'Inspect this exact mathematical update or enumerated object.'",'operation:operationText(s,z,r)')
s=s.replace('preserves all seven cells','preserves the total cell count')
# A live tiling checkpoint indexes enumeration, not the board width: its result count is T_n.
s=s.replace("if(value===undefined&&s.operation==='tiling')value=r.count;", "if(s.operation==='tiling')return '<math xmlns=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mrow><msub><mi>T</mi><mn>'+s.n+'</mn></msub><mo>=</mo><mn>'+r.count+'</mn></mrow></math>';")
p.write_text(s,encoding='utf-8');print('Replaced generic operation text with precise model-specific explanations; live exact values use native MathML.')
