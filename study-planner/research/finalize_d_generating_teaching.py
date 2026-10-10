from pathlib import Path
B=Path(__file__).resolve().parent;R=B.parent
p=B/'d_generating.en.md';s=p.read_text(encoding='utf-8')
s=s.replace('<!-- SIM: poles -->', '''### Why the complete repeated-pole basis is necessary

After polynomial division, write the denominator as a product of relatively prime powers of distinct linear factors over the complex numbers. The Chinese remainder decomposition of the numerator modulo that denominator separates one residue polynomial of degree below each factor's multiplicity. Dividing those residue polynomials by their factor powers, then expressing each numerator in powers of its own linear factor, yields exactly the displayed family of inverse powers. Uniqueness follows after clearing denominators: reduce at each pole modulo its factor power to force the corresponding residue polynomial to zero. Thus partial fractions are a basis decomposition, not a guess based on how many constants look convenient.

For a pole of multiplicity $m$, the coefficient of the highest inverse power is the value at that pole of the rational function after multiplying by the factor to the power $m$. Subtract that highest term before finding the lower powers. Repeating this step, or expanding the remaining numerator locally at the pole, determines all of them. A surviving highest-order coefficient is nonzero in the reduced expression; a numerator cancellation lowers the order before this calculation begins. The polynomial quotient remains a separate finite-prefix contribution.

<!-- SIM: poles -->''')
s=s.replace('<!-- SIM: partitions -->', '''### Reconstructing a self-conjugate diagram from its hooks

Number the diagonal cells from the top left. In a self-conjugate diagram, the arm and leg of the $i$th diagonal cell have equal length $a_i$, so its diagonal hook has length $2a_i+1$. Successive arm lengths are strictly decreasing: the row length cannot increase, while the diagonal index increases by one. The hook lengths are therefore distinct odd positive integers. Every cell belongs to exactly one diagonal hook: a cell weakly above the diagonal belongs to its row's diagonal hook, and a cell below it belongs to its column's diagonal hook. The total hook length equals the total number of cells.

Conversely, sort a finite collection of distinct odd hook lengths in decreasing order and write them as $2a_i+1$. Put $a_i$ cells to the right and $a_i$ cells below diagonal cell $i$. Strict decrease ensures that the resulting row lengths are nonincreasing and that the diagonal cells and their hooks form one Ferrers diagram. Transposition preserves the construction. Extracting the diagonal hooks recovers the original lengths, so the two constructions are inverse bijections. This proves the product over distinct odd lengths and explains why ordinary odd parts with unrestricted repetition represent a different class.

<!-- SIM: partitions -->''')
p.write_text(s,encoding='utf-8')
p=B/'build_d_generating.py';s=p.read_text(encoding='utf-8')
s=s.replace('assert len(qs)==80;save', '''for q in qs:
 n=int(q['id'].split('_')[-1])
 if n in[4,9,31,36,37,47,49,56,69]:q['visualQualification']='This walkthrough uses the same target and inventory as the problem. Compare its exact checkpoints with the coefficient derivation above.'
 if n==80:q['visualQualification']='This walkthrough enumerates the ordered strings in the first part of this question. The unordered and labelled classes are derived separately above.'
assert len(qs)==80;save''')
p.write_text(s,encoding='utf-8')
p=R/'dist/chapters/d_generating.js';s=p.read_text(encoding='utf-8')
insert="""function teachingCheck(s,z){const op=s.operation;const names={inverse:'Constant inverse coefficient',convolution:'Selected exponent sum',filter:'Retained residue modulo three',bounded:'Maximum per box',coins:'Current denomination',composition:'Allowed positive part sizes',partitions:'Largest processed part size',durfee:'Square plus arm plus leg',catalan:'Declared number of pairs',labelled:'Labels used exactly once',marking:'Binary word length',poles:'Surviving pole multiplicity'};let value;if(op==='inverse')value=1;else if(op==='convolution')value=z.i+z.j;else if(op==='filter')value=s.residue;else if(op==='bounded')value=3;else if(op==='coins')value=z.factor;else if(op==='composition')value='one or two';else if(op==='partitions')value=z.factor;else if(op==='durfee')value=z.d*z.d+z.arm.reduce((a,b)=>a+b,0)+z.leg.reduce((a,b)=>a+b,0);else if(op==='catalan')value=s.n;else if(op==='labelled')value=z.left.length+z.right.length;else if(op==='marking')value=z.word.length;else value=3;return[{mathHtml:names[op],result:String(value)}];}
"""
s=s.replace('function makeModel(',insert+'function makeModel(')
s=s.replace("checks:[{mathHtml:'Input contract',result:'validated'},{mathHtml:'Coefficient domain',result:'finite exact model'}]", 'checks:teachingCheck(s,z)')
p.write_text(s,encoding='utf-8')
