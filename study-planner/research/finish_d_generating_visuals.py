from pathlib import Path
B=Path(__file__).resolve().parent;R=B.parent
p=R/'dist/chapters/d_generating.js';s=p.read_text(encoding='utf-8')
s=s.replace("n:Number(raw.n??5)}", "n:Number(raw.n??5)};if(s.operation==='convolution')s.base=Number(raw.base??2);if(s.operation==='filter')s.residue=Number(raw.residue??1);if(s.operation==='bounded')s.boxes=Number(raw.boxes??3);if(s.operation==='coins')s.weights=raw.weights??[1,2,3]")
s=s.replace("if(s.operation==='bounded'&&s.n>9)throw Error('Three boxes capped at three have total at most nine.');return s;", "if(s.base!==undefined&&![2,3].includes(s.base))throw Error('The convolution base is two or three.');if(s.residue!==undefined&&![0,1,2].includes(s.residue))throw Error('A residue modulo three is zero, one or two.');if(s.boxes!==undefined&&![3,4].includes(s.boxes))throw Error('Use three or four capped boxes.');if(s.operation==='bounded'&&s.n>3*s.boxes)throw Error('The total exceeds the sum of the box caps.');if(s.weights!==undefined&&![[1,2,3],[1,2,5]].some(a=>JSON.stringify(a)===JSON.stringify(s.weights)))throw Error('The declared coin inventories are one/two/three or one/two/five.');return s;")
s=s.replace('(k+1)*2**(n-k)','(k+1)*s.base**(n-k)').replace('(_,i)=>2**i)}','(_,i)=>s.base**i)}')
s=s.replace('k%3===1','k%3===s.residue').replace('modulus:3,residue:1','modulus:3,residue:s.residue')
s=s.replace("s.operation==='bounded'?[1,1,1]:s.operation==='coins'?[1,2,3]", "s.operation==='bounded'?Array(s.boxes).fill(1):s.operation==='coins'?s.weights")
s=s.replace("Array.from({length:64},(_,m)=>[m%4,Math.floor(m/4)%4,Math.floor(m/16)])", "Array.from({length:4**s.boxes},(_,m)=>Array.from({length:s.boxes},(_,j)=>Math.floor(m/4**j)%4))")
s=s.replace("function svg(b){return '<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 760 350\" role=\"img\" aria-label=\"Exact generating-function checkpoint\"><rect x=\"1\" y=\"1\" width=\"758\" height=\"348\"", "function svg(b,h=350){return '<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 760 '+h+'\" role=\"img\" aria-label=\"Exact generating-function checkpoint\"><rect x=\"1\" y=\"1\" width=\"758\" height=\"'+(h-2)+'\"")
s=s.replace("txt(28,26,'Choose only", "txt(28,36,'Choose only").replace('const cell=38,x0=155,y0=55','const cell=38,x0=155,y0=90').replace('y0-9,i','y0-20,i').replace('(i+1)*2**j','(i+1)*s.base**j')
s=s.replace("'Keep indices with residue one modulo three'", "'Keep indices with residue '+s.residue+' modulo three'").replace('if(i%3===1)','if(i%3===s.residue)')
s=s.replace("'Three boxes: each multiplicity is zero through three'", "s.boxes+' boxes: each multiplicity is zero through three'").replace("'Unordered change: denominations one, two, and three'", "'Unordered change: denominations '+s.weights.join(', ')")
s=s.replace('return svg(b);}', "return svg(b,s.operation==='convolution'?380:350);}")
s=s.replace("return 'n\\\\equiv1\\\\pmod3'", "return 'n\\\\equiv'+s.residue+'\\\\pmod3'")
start=s.index('function stateMath(');end=s.index('\nfunction action(',start)
s=s[:start]+'''function stateMath(s,z,r){const num=v=>'<mn>'+esc(v)+'</mn>',id=v=>'<mi>'+v+'</mi>',sub=(v,k)=>'<msub>'+id(v)+num(k)+'</msub>',equal=(a,b)=>a+'<mo>=</mo>'+num(b);let body;
 if(s.operation==='inverse')body=equal(sub('b',z.step),z.value);
 else if(s.operation==='convolution')body=equal(sub('S',z.step),z.total);
 else if(s.operation==='filter')body=equal(sub('a',z.step),z.value)+'<mtext>'+ (z.keep?' retained':' suppressed')+'</mtext>';
 else if(['bounded','coins','partitions'].includes(s.operation))body=equal('<mo>[</mo><msup>'+id('x')+num(s.n)+'</msup><mo>]</mo>'+sub('P',z.step),z.rows.at(-1)[s.n]);
 else if(s.operation==='durfee')body=equal(id('d'),z.d)+'<mo>,</mo>'+equal(id('n'),s.n);
 else if(s.operation==='marking')body=equal(sub('S',z.step),z.total);
 else if(s.operation==='labelled')body=equal(id('k'),z.k)+'<mo>,</mo>'+equal(id('N'),z.multiplicity);
 else if(s.operation==='poles')body=equal(sub('a',z.step),z.value);
 else body=equal(id('N'),r.coefficient);
 return '<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow>'+body+'</mrow></math>';}
''' +s[end:]
s=s.replace('formulaHtml:stateMath(z)','formulaHtml:stateMath(s,z,r)')
p.write_text(s,encoding='utf-8')
p=B/'build_d_generating.py';s=p.read_text(encoding='utf-8');before="js=\"const {makeModel}"
i=s.index(before)
s=s[:i]+"specs += [('question-four','Degree-three product: linear coefficients times powers of three',{'operation':'convolution','n':3,'base':3},'problem-only'),('question-nine','Retain indices congruent to two modulo three',{'operation':'filter','n':8,'residue':2},'problem-only'),('question-thirtyone','Four named boxes capped at three; total nine',{'operation':'bounded','n':9,'boxes':4},'problem-only'),('question-thirtysix','Unordered change of ten with weights one, two, and five',{'operation':'coins','n':10,'weights':[1,2,5]},'problem-only'),('question-eighty','Every ordered one/two composition of total six',{'operation':'composition','n':6},'problem-only')]\n"+s[i:]
s=s.replace("# A companion uses", "visuals.update({4:'question-four',9:'question-nine',31:'question-thirtyone',36:'question-thirtysix',80:'question-eighty'})\n# A companion uses")
s=s.replace('for n in[5,9,18,43,46,50,75,77]', 'for n in[5,18,43,46,50,75,77]')
s=s.replace("'animationCount=12'", "'animationCount=17'").replace("'animationWalkthroughCount=12'", "'animationWalkthroughCount=17'").replace("'12 distinct mathematical models'", "'17 distinct mathematical models'")
p.write_text(s,encoding='utf-8')
p=B/'qa_d_generating_browser.py';s=p.read_text(encoding='utf-8').replace("'players']>12", "'players']>17")
p.write_text(s,encoding='utf-8')
print('Installed five exact question-specific models and semantic live MathML readouts.')
