from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/advanced-simulations.js';s=p.read_text(encoding='utf-8')
a='const horizontal=Math.max(0,Math.min(1,(t-.25)/.5)),lift=t<.25?t/.25:t>.75?(1-t)/.25:1;'
b='const smooth=x=>x*x*(3-2*x),horizontal=smooth(Math.max(0,Math.min(1,(t-.25)/.5))),lift=t<.25?smooth(t/.25):t>.75?smooth((1-t)/.25):1;'
assert a in s;s=s.replace(a,b)
s=s.replace("[[2600,'Slow'],[2200,'Normal'],[1500,'Fast']]","[[4400,'Slow'],[2200,'Normal'],[1400,'Fast']]")
s=s.replace("function pairGeometry(before,after,model){\n", "function pairGeometry(before,after,model){\n   if(!before.viewBox||!after.viewBox)return []; // Native MathML steps do not have SVG geometry.\n")
p.write_text(s,encoding='utf-8')
