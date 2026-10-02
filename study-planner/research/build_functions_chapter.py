"""Render the functions manuscript with semantic math and original vector figures."""
import html,json,re
from pathlib import Path
from markdown_it import MarkdownIt
from math_typography import normalize_math,normalize_scripts
ROOT=Path(__file__).resolve().parents[1];base=ROOT/'research'
source=(base/'d_functions.en.md').read_text(encoding='utf-8')
for name in ('problems','review'):
 source=source.replace(f'<!-- INCLUDE:{name} -->',(base/f'd_functions-{name}.en.md').read_text(encoding='utf-8'))
source=source.replace('\\binom{n}{k}','C(n,k)').replace('√{−ln(y)}','√(−ln(y))').replace('{0,1}^ℕ','{0,1}^{ℕ}').replace('ℕ_+','ℕ_{+}')
def text(x,y,s,size=23):
 s=re.sub(r'([ab])([012])',r'\1<tspan baseline-shift="sub" font-size="16">\2</tspan>',s)
 s=s.replace('⁻¹','<tspan baseline-shift="super" font-size="15">−1</tspan>')
 return f'<text x="{x}" y="{y}" text-anchor="middle" fill="#16384d" font-size="{size}">{s}</text>'
def node(x,y,s,fill='#f1f7fa'):
 return f'<circle cx="{x}" cy="{y}" r="23" fill="{fill}" stroke="#87adbf"/>'+text(x,y+8,s)
def edge(x,y,z,w):
 return f'<line x1="{x}" y1="{y}" x2="{z}" y2="{w}" stroke="#547e95" stroke-width="2.2" marker-end="url(#arrow)"/>'
defs='<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="none" stroke="#547e95"/></marker></defs>'
def figure(title,height,inside,caption):
 return f'<figure class="logic-diagram"><svg viewBox="0 0 700 {height}" role="img" aria-label="{html.escape(title)}"><title>{title}</title>{defs}{inside}</svg><figcaption>{caption}</figcaption></figure>'
inside=text(100,35,'A')+text(375,35,'B')
for i,y in enumerate([90,170,250,330]):inside+=edge(125,y,348,130 if i%2==0 else 250)+node(100,y,str(i))
for y,s in [(130,'b0'),(250,'b1'),(350,'b2')]:inside+=node(375,y,s)
inside+=text(560,130,'F(b0) = {0,2}',22)+text(560,250,'F(b1) = {1,3}',22)+text(560,350,'F(b2) = ∅',22)
figures={'fibers':figure('Fibers distinguish collisions from unused targets',400,inside,'Figure 1. Every input has one outgoing arrow, but two inputs arrive at each of the first two targets. The third target is unused. This is a valid total function that is neither injective nor onto. F denotes the target fiber. Edge crossings are not extra vertices.')}
inside=text(80,35,'A')+text(350,35,'B')+text(620,35,'C')
inside+=edge(104,100,324,100)+edge(104,235,324,235)+edge(374,100,594,100)+edge(374,235,594,235)+edge(374,350,596,113)
for x,y,s in [(80,100,'0'),(80,235,'1'),(350,100,'a'),(350,235,'b'),(350,350,'c'),(620,100,'u'),(620,235,'v')]:inside+=node(x,y,s)
inside+=text(205,75,'f')+text(485,75,'g')
figures['composition']=figure('A bijective composite can have nonbijective factors',400,inside,'Figure 2. The inner map misses c, and the outer map merges a with c. On the attained middle subset {a,b}, the outer map is a bijection to {u,v}. The composite therefore sends 0 to u and 1 to v bijectively. The extra middle input is not an original input.')
inside=''
for x,cap,items,colors in [(20,'S = {0}',[0,2],['#d7eadf','#f1f7fa']),(255,'f[S] = {a}',[],[]),(490,'f⁻¹[f[S]]',[0,2],['#d7eadf','#d7eadf'])]:
 inside+=f'<rect x="{x}" y="35" width="190" height="230" rx="16" fill="#eef6f9" stroke="#87adbf"/>'+text(x+95,80,cap,21)
 for i,k in enumerate(items):inside+=node(x+95,140+80*i,str(k),colors[i])
inside+=node(350,180,'a','#d7eadf')+edge(213,175,253,175)+edge(448,175,488,175)
figures['saturation']=figure('The round trip fills the whole touched fiber',300,inside,'Figure 3. Both 0 and 2 map to a. Selecting just 0 gives image {a}; its preimage contains both inputs. The green region in the right-hand panel is the saturation of the original subset. This is a set operation, not an inverse-function evaluation.')
inside=text(60,35,'A')+text(255,35,'A/∼')+text(455,35,'f[A]')+text(650,35,'B')
inside+=edge(85,100,210,135)+edge(85,200,210,265)+edge(85,300,210,150)+edge(298,140,429,140)+edge(298,265,429,265)+edge(480,140,625,140)+edge(480,265,625,265)
for x,y,s in [(60,100,'0'),(60,200,'1'),(60,300,'2'),(455,140,'b0'),(455,265,'b1'),(650,140,'b0'),(650,265,'b1'),(650,350,'b2')]:inside+=node(x,y,s)
for y,s in [(140,'{0,2}'),(265,'{1}')]:inside+=f'<rect x="211" y="{y-25}" width="88" height="50" rx="13" fill="#e3f0e9" stroke="#87adbf"/>'+text(255,y+8,s,22)
inside+=text(150,65,'q')+text(355,65,'b')+text(550,65,'i')
figures['factorization']=figure('Every function factors through its fiber quotient and image',395,inside,'Figure 4. The quotient map q merges equal-output inputs. The induced map b sends classes bijectively to attained targets. The inclusion i keeps those targets inside B, where b₂ remains unused. The total map is i after b after q.')
for name,s in figures.items():source=source.replace(f'<!-- FIGURE:{name} -->',s)
onto='''<div class="formula-block"><math display="block" aria-label="Number of onto maps equals the alternating sum from j equals zero to n of binomial n choose j times negative one to j times n minus j to m"><mrow><mi mathvariant="normal">Onto</mi><mo>(</mo><mi>m</mi><mo>,</mo><mi>n</mi><mo>)</mo><mo>=</mo><munderover><mo>∑</mo><mrow><mi>j</mi><mo>=</mo><mn>0</mn></mrow><mi>n</mi></munderover><mrow><mo>(</mo><mfrac linethickness="0"><mi>n</mi><mi>j</mi></mfrac><mo>)</mo></mrow><msup><mrow><mo>(</mo><mo>−</mo><mn>1</mn><mo>)</mo></mrow><mi>j</mi></msup><msup><mrow><mo>(</mo><mi>n</mi><mo>−</mo><mi>j</mi><mo>)</mo></mrow><mi>m</mi></msup></mrow></math></div>'''
source=source.replace('<!-- MATH:onto -->',onto)
lab='''<section class="lab" id="function-lab" aria-label="Interactive finite function laboratory"><div class="lab-actions"><button id="preset-bijection">Bijection</button><button id="preset-onto">Onto with a collision</button><button id="preset-injection">Injection with an unused target</button></div><p><label for="target-size">Codomain size:</label> <select id="target-size"><option>3</option><option>4</option><option>5</option></select></p><div id="function-input"></div><div id="function-output" aria-live="polite"></div><p class="lab-caption">S is the subset selected in the last column. Changing an output or a selection recalculates the exact fibers and both subset operations immediately.</p></section>'''
source=source.replace('<!-- LAB:functions -->',lab)
def math_inline(m):
 s=html.escape(m.group(1))
 s=re.sub(r'\^\{([^{}]+)\}',r'<sup>\1</sup>',s)
 s=re.sub(r'\^([A-Za-z0-9]+)',r'<sup>\1</sup>',s)
 s=re.sub(r'_\{([^{}]+)\}',r'<sub>\1</sub>',s)
 s=re.sub(r'_(\d+|[A-Za-z])',r'<sub>\1</sub>',s)
 s=re.sub(r'\s*([∈∉⊆⊊⊂∪∩∖→⇒⇔↦≡∧∨∣≤≥≠≈∼≼≺⋖∘=+−×⋅])\s*',lambda op:'\u2009'+op.group(1)+'\u2009',s)
 return '<span class="math-inline">'+s+'</span>'
source=re.sub(r'\$([^$\n]+)\$',math_inline,source)
body=MarkdownIt('commonmark',{'html':True}).enable('table').render(source)
body=normalize_scripts(normalize_math(body))
anchors=['sources','definitions','fibers','composition','inverses','images','quotients','counting','infinite','problems','review','laboratory','references'];it=iter(anchors)
body=re.sub(r'<h2>(.*?)</h2>',lambda m:f'<h2 id="{next(it)}">{m.group(1)}</h2>',body)
assert '<!--' not in body and '$' not in body and '\\binom' not in body
nav=' '.join(f'<a href="#{x}">{x.capitalize()}</a>' for x in anchors)
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Functions, Inverses, and Cardinality · Doctoral CSE 1406</title><meta name="description" content="Deep English functions chapter: four principal university courses and two supplements, 42 fully worked problems, 72 examination rules, rigorous proofs, four vector figures, and a fiber laboratory."><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="d_functions.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-2">← Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Discrete Mathematics · Chapter 6 · Week 2</p><h1>Functions, Inverses, Injectivity, and Surjectivity</h1><p>Student-approved chapter · four principal university courses and two focused supplements · 42 fully worked problems · 72 examination rules</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">← Chapter library</a></p></main><script src="d_functions.js"></script></body></html>'''
(ROOT/'dist/chapters/d_functions.html').write_text(page,encoding='utf-8')
audit=(base/'d_functions-source-audit.md').read_text(encoding='utf-8')
auditbody=normalize_scripts(normalize_math(MarkdownIt('commonmark',{'html':True}).enable('table').render(audit)))
(ROOT/'dist/reviews/d_functions-sources.html').write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Functions source audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/d_functions.html">← Functions chapter</a></p><article class="lesson">{auditbody}</article></main></body></html>',encoding='utf-8')
p=ROOT/'dist/lessons.json';lessons=json.loads(p.read_text(encoding='utf-8'));week=next(w for w in lessons if w['week']==2)
week['title']='Week 2 chapter library'
week['chapters']=[c for c in week['chapters'] if c['topicId']!='d_functions']+[{'topicId':'d_functions','title':'Functions, inverses, injectivity, and surjectivity','status':'ready','url':'chapters/d_functions.html'}]
p.write_text(json.dumps(lessons,indent=2)+'\n')
print('Functions rendered:',len(source.split()),'space-separated manuscript tokens; 42 worked problems, 72 complete rules, four figures.')
