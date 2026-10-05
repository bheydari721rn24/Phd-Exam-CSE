from pathlib import Path
p=Path(__file__).resolve().parents[1]/'dist/chapters/semantic-diagrams.js';s=p.read_text(encoding='utf-8')
s=s.replace('const functions={bars,search,venn,truth,graph,geometry:', 'const functions={bars:mergeExact,search,venn,truth,graph:graphExact,geometry:')
needle='if(id==="comb-priority"||id==="comb-active-low")'
pos=s.index(needle)
extra='''if(id==="comb-nand"){network(g,[["A",a,30,45],["B",b,30,140],["C",c,30,290]],[["p","NAND",["A","B"],240,95],["q","NAND",["A","C"],240,255],["Y","NAND",["p","q"],540,180]],["Y"]);return;}
 if(id==="nand-mapping"){network(g,[["A",+f.metrics.A,40,85],["B",+f.metrics.B,40,260]],[["n","NAND",["A","B"],250,170],["Y","NAND",["n","n"],515,170]],["Y"]);return;}
 if(id==="comb-miter"){network(g,[["A",a,30,35],["B",b,30,155],["C",c,30,315]],[["B+C","OR",["B","C"],160,225],["F","AND",["A","B+C"],330,90],["AB","AND",["A","B"],325,275],["G","OR",["AB","C"],480,265],["M","XOR",["F","G"],620,165]],["M"]);return;}
 if(id==="comb-interval"){network(g,[["A",1,30,40],["B",1,30,115],["C",0,30,265],["D",1,415,315]],[["p","AND",["A","B"],180,90],["q","OR",["p","C"],350,200],["Y","AND",["q","D"],580,265]],["Y"]);text(g,400,35,`Step ${s.step}: arrival interval [${s.lo}, ${s.hi}]`,20);text(g,380,350,"Gate delay intervals: p (1,3), q (2,4), Y (1,2).",19);return;}
 '''
s=s[:pos]+extra+s[pos:]
old='if(id==="comb-active-low"){dev.push('
new='if(id==="comb-active-low"){ins[0]=["E_n",1-a,30,40];dev.unshift(["E","NOT",["E_n"],150,40]);dev.push('
assert old in s;s=s.replace(old,new)
old='path(g,`M${from}H710`,values[name]?C.green:C.red,3);'
new='path(g,`M${from}H710`,known&&!known.has(name)?"#c1cbd1":values[name]?C.green:C.red,3);'
assert old in s;s=s.replace(old,new)
p.write_text(s,encoding='utf-8')
