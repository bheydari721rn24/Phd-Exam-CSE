from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];p=ROOT/'dist/chapters/semantic-diagrams.js';s=p.read_text(encoding='utf-8')
changes={
'enumeration:gridEnumeration,kmap,waveform':'enumeration:gridEnumeration,kmap:kmapExact,waveform',
'text(g,720,from[1]+7,name,18,"start");':'text(g,744,from[1]-12,name,18,"end");',
'const old=s.row||s.old,newObject=s.new;':'const old=s.row||(typeof s.old==="string"?JSON.parse(s.old):s.old),newObject=typeof s.new==="string"&&s.new.startsWith("[")?JSON.parse(s.new):s.new;',
's.heading||s.phase||`Included sources: ${s.included}`':'s.heading||s.phase||(id==="bayes-frequencies"?`${s.positive?"Positive":"Negative"} report: ${s.stage}`:`Included sources: ${s.included}`)',
'for(let i=0;i<5;i++)for(let j=0;j<i;j++){rect(g,170+j*55,60+i*45,45,35,i===s.i&&j===s.j?"#ffe0a1":"#d1e8f1");text(g,192+j*55,84+i*45,`${i},${j}`,16);}':'for(let i=1;i<=5;i++)for(let j=1;j<=i;j++){rect(g,115+j*55,35+i*45,45,35,i===s.i&&j===s.j?"#ffe0a1":"#d1e8f1");text(g,137+j*55,59+i*45,`${i},${j}`,16);}',
'derivation(p,g,f);\n}\nfunction tiles':'derivationExact(p,g,f);\n}\nfunction tiles',
'let groups=[];if(id==="matrix-product")':'let groups=[];if(id==="matrix-summaries")groups=[["A: trace 5; squared Frobenius norm 30",[[1,2],[3,4]]]];else if(id==="matrix-product")',
'const mark=id==="matrix-product"?':'const mark=id==="matrix-summaries"?[[Math.floor(p.index/2),p.index%2]]:id==="matrix-product"?',
}
for a,b in changes.items():
 assert a in s,a
 s=s.replace(a,b)
p.write_text(s,encoding='utf-8')
