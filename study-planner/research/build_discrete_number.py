"""Render the number-theory manuscript with semantic scripts and original figures."""
import html,json,re
from pathlib import Path
from markdown_it import MarkdownIt
from math_typography import normalize_math,normalize_scripts
ROOT=Path(__file__).resolve().parents[1];base=ROOT/'research'
source=(base/'d_number.en.md').read_text(encoding='utf-8')
for name in ('problems','review'):source=source.replace(f'<!-- INCLUDE:{name} -->',(base/f'd_number-{name}.en.md').read_text(encoding='utf-8'))
def text(x,y,s,size=23):return f'<text x="{x}" y="{y}" text-anchor="middle" fill="#16384d" font-size="{size}">{html.escape(s)}</text>'
def line(x,y,z,w):return f'<line x1="{x}" y1="{y}" x2="{z}" y2="{w}" stroke="#547e95" stroke-width="2.3"/>'
def node(x,y,s):return f'<circle cx="{x}" cy="{y}" r="24" fill="#edf5f9" stroke="#87adbf"/>'+text(x,y+8,s)
def fig(title,height,body,caption):return f'<figure class="logic-diagram"><svg viewBox="0 0 700 {height}" role="img" aria-label="{html.escape(title)}"><title>{title}</title>{body}</svg><figcaption>{caption}</figcaption></figure>'
coords={1:(350,310),2:(215,225),3:(490,225),4:(215,130),6:(490,130),12:(350,45)}
body=''
for a,b in [(1,2),(1,3),(2,4),(2,6),(3,6),(4,12),(6,12)]:
 x,y=coords[a];z,w=coords[b];body+=line(x,y,z,w)
for a,(x,y) in coords.items():body+=node(x,y,str(a))
body+=text(350,368,'gcd(4,6) = 2; lcm(4,6) = 12',24)
figures={'lattice':fig('The divisibility lattice of the positive divisors of twelve',400,body,'Figure 1. Upward connections show cover relations: a lower number divides its upper neighbor, and there is no intermediate divisor. For any two nodes, gcd is their greatest common lower bound and lcm is their least common upper bound. The slanted connection from 2 to 6 is essential; 2 and 3 are incomparable.')}
body=text(350,33,'f(x) = 8x mod 12',27)
for i,(res,pre) in enumerate([(0,'0, 3, 6, 9'),(4,'2, 5, 8, 11'),(8,'1, 4, 7, 10')]):
 x=120+230*i
 body+=f'<rect x="{x-100}" y="60" width="200" height="160" rx="14" fill="#edf5f9" stroke="#87adbf"/>'
 body+=text(x,95,'preimages',21)+text(x,135,pre,22)+text(x,178,'↓',25)+text(x,209,str(res),26)
body+=text(350,269,'Image: {0,4,8}; each fiber contains four residues',23)
figures['fibers']=fig('The three fibers of multiplication by eight modulo twelve',300,body,'Figure 2. Every domain residue from 0 through 11 appears exactly once. The fiber over zero is the kernel. The other two fibers are translates of that kernel, explaining the equal size gcd(8,12) = 4. Targets outside the displayed image have no solution.')
body=text(350,30,'Column: x mod 5; row: x mod 3',24)
for b in range(5):body+=text(150+105*b,75,str(b))
for a in range(3):
 body+=text(62,132+70*a,str(a))
 for b in range(5):
  x=next(x for x in range(15) if x%3==a and x%5==b);px=150+105*b;py=124+70*a
  body+=f'<rect x="{px-45}" y="{py-25}" width="90" height="52" rx="8" fill="'+('#d7eadf' if x==11 else '#edf5f9')+'" stroke="#87adbf"/>'+text(px,py+8,str(x),25)
body+=text(350,348,'Highlighted: x ≡ 2 (mod 3), x ≡ 1 (mod 5)',23)
figures['crt']=fig('The CRT bijection from fifteen residues to a three-by-five grid',380,body,'Figure 3. A cell contains the unique canonical integer from 0 through 14 with its row and column residues. Every integer appears once. The highlighted cell is 11. If the moduli shared factors, some coordinate pairs would be incompatible; this complete rectangular bijection uses coprimality.')
body=text(350,32,'Powers of 2 modulo 12',26)
for x,s,k in [(65,'1','k = 0'),(245,'2','k = 1'),(425,'4','even k ≥ 2'),(625,'8','odd k ≥ 3')]:
 body+=node(x,110,s)+text(x,175,k,21)
body+=line(92,110,216,110)+text(155,104,'→',25)+line(272,110,395,110)+text(335,104,'→',25)
body+='<path d="M445,89 Q525,48 607,89" fill="none" stroke="#547e95" stroke-width="2.3"/>'+text(525,77,'→',25)
body+='<path d="M607,131 Q525,158 445,131" fill="none" stroke="#547e95" stroke-width="2.3"/>'+text(525,143,'←',25)
body+=text(350,236,'A transient precedes the two-cycle {4,8}',24)
figures['powers']=fig('A nonunit power sequence has a transient followed by a cycle',265,body,'Figure 4. Multiplying by 2 sends 1 to 2 to 4 to 8 and then back to 4. Exponents differing by two agree once both are at least two, but exponent zero cannot be reduced into that cycle. Euler reduction requires a unit; 2 has no inverse modulo 12.')
for name,f in figures.items():source=source.replace(f'<!-- FIGURE:{name} -->',f)
source=source.replace('<!-- MATH:crt -->','''<div class="formula-block"><math display="block" aria-label="x is congruent to the sum from i equals one to r of a i M i u i modulo M"><mrow><mi>x</mi><mo>≡</mo><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>r</mi></munderover><msub><mi>a</mi><mi>i</mi></msub><msub><mi>M</mi><mi>i</mi></msub><msub><mi>u</mi><mi>i</mi></msub><mspace width="1em"/><mo>(</mo><mi mathvariant="normal">mod</mi><mspace width=".3em"/><mi>M</mi><mo>)</mo></mrow></math></div>''')
lab='''<section class="lab" id="number-lab" aria-label="Exact residue multiplication laboratory"><div class="lab-actions"><button data-preset="unit">Invertible coefficient</button><button data-preset="many">Four solutions</button><button data-preset="none">Incompatible target</button><button data-preset="zero">Zero coefficient</button><button data-preset="negative">Negative coefficient</button></div><form id="number-form"><label>Coefficient a <input id="number-a" type="number" value="8" min="-10000" max="10000" step="1" required></label><label>Target b <input id="number-b" type="number" value="4" min="-10000" max="10000" step="1" required></label><label>Modulus m <input id="number-m" type="number" value="12" min="2" max="60" step="1" required></label><button type="submit">Analyze every residue</button></form><div id="number-output" aria-live="polite"></div><p>The map table enumerates every residue in this finite laboratory. Solutions and the Bézout certificate are also constructed by extended Euclid, providing two independently checkable descriptions. Inputs are bounded to keep the displayed table readable and all JavaScript arithmetic exact.</p></section>'''
source=source.replace('<!-- LAB:number -->',lab)
def math_inline(m):
 s=html.escape(m.group(1))
 while re.search(r'\^\{([^{}]+)\}',s):s=re.sub(r'\^\{([^{}]+)\}',r'<sup>\1</sup>',s)
 s=re.sub(r'\^([A-Za-z0-9]+)',r'<sup>\1</sup>',s)
 s=re.sub(r'_\{([^{}]+)\}',r'<sub>\1</sub>',s);s=re.sub(r'_(\d+|[A-Za-z])',r'<sub>\1</sub>',s)
 s=re.sub(r'\s*([∈∉⊆⊊⊂∪∩∖→⇒⇔↦≡∧∨∣≤≥≠≈∼∘=+−×⋅])\s*',lambda op:'\u2009'+op.group(1)+'\u2009',s)
 return '<span class="math-inline">'+s+'</span>'
source=re.sub(r'\$([^$\n]+)\$',math_inline,source)
body=normalize_scripts(normalize_math(MarkdownIt('commonmark',{'html':True}).enable('table').render(source)))
anchors=['sources','divisibility','gcd','integer-equations','residues','crt','powers','consequences','problems','review','laboratory','references'];it=iter(anchors)
body=re.sub(r'<h2>(.*?)</h2>',lambda m:f'<h2 id="{next(it)}">{m.group(1)}</h2>',body)
assert '<!--' not in body and '$' not in body and '\\' not in body
nav=' '.join(f'<a href="#{x}">{x.replace("-"," ").capitalize()}</a>' for x in anchors)
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Divisibility, Modular Arithmetic, and Number Theory · Doctoral CSE 1406</title><meta name="description" content="Four reviewed university courses; rigorous number theory, 40 fully solved problems, 70 examination rules, four original vector diagrams, and an exact residue laboratory."><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="d_number.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-2">← Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Discrete Mathematics · Chapter 8 · Week 2</p><h1>Divisibility, Modular Arithmetic, and Number Theory</h1><p>Review draft · four principal university courses · 40 fully worked problems · 70 complete examination rules</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">← Chapter library</a></p></main><script src="d_number.js"></script></body></html>'''
(ROOT/'dist/chapters/d_number.html').write_text(page,encoding='utf-8')
audit=(base/'d_number-source-audit.md').read_text(encoding='utf-8');auditbody=normalize_scripts(normalize_math(MarkdownIt('commonmark',{'html':True}).enable('table').render(audit)))
(ROOT/'dist/reviews/d_number-sources.html').write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Number theory source audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/d_number.html">← Number theory chapter</a></p><article class="lesson">{auditbody}</article></main></body></html>',encoding='utf-8')
p=ROOT/'dist/lessons.json';rows=json.loads(p.read_text());week=next(w for w in rows if w['week']==2)
week['chapters']=[c for c in week['chapters'] if c['topicId']!='d_number']+[{'topicId':'d_number','title':'Divisibility, modular arithmetic, and number theory','status':'draft','url':'chapters/d_number.html'}]
p.write_text(json.dumps(rows,indent=2)+'\n')
print('Number theory rendered:',len(source.split()),'space-separated tokens; 40 worked problems, 70 rules, four figures.')
