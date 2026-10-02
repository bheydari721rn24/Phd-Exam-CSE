"""Reproduce the English divide-and-conquer chapter and original vector figures."""
import ast,html,json,re
from pathlib import Path
from markdown_it import MarkdownIt
from math_typography import normalize_math,normalize_scripts
ROOT=Path(__file__).resolve().parents[1];base=ROOT/'research'
# Reuse pure typography helpers without executing the previous chapter's builder.
tree=ast.parse((base/'build_recurrence_chapter.py').read_text(encoding='utf-8'))
for fn in tree.body:
 if isinstance(fn,ast.FunctionDef) and fn.name in ('text','line','fig','math_inline'):
  exec(compile(ast.Module(body=[fn],type_ignores=[]),'<shared chapter helpers>','exec'))
source=(base/'a_divide.en.md').read_text(encoding='utf-8')
for part in ('problems','review'):
 source=source.replace(f'<!-- INCLUDE:{part} -->',(base/f'a_divide-{part}.en.md').read_text(encoding='utf-8'))

def box(x,y,w,h,label,fill='#e7f0f6'):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#90afc1"/>'+text(x+w/2,y+h/2+8,label,24)
figures={}
b=text(350,34,'Left: 2, 4, 7     Right: 1, 4, 6',25)
for y,label,action in [(97,'Right 1 < left 2','Add 3: pairs with 2, 4, 7'),(157,'Left 4 = right 4','Take left; add 0'),(217,'Right 4 < left 7','Add 1: pair with 7'),(277,'Right 6 < left 7','Add 1: pair with 7')]:
 b+=box(25,y-28,275,46,label)+text(495,y+3,action,23)
b+=text(350,340,'Cross inversions = 3 + 0 + 1 + 1 = 5',25)
figures['merge']=fig('Strict inversion charges during a stable merge',375,b,'Figure 1. Only right items that are strictly smaller trigger a charge. The right four contributes an inversion with seven despite tying the earlier left four. The left two emission and final seven emission add no inversions; they are omitted from the four displayed decision rows.')

b=text(350,34,'Array: 4, −6, 8 | −2, 3, −9, 5',24)
b+=box(30,75,290,65,'Left: (6, 6, 8, 8)')+box(380,75,290,65,'Right: (−3, 1, 5, 5)')
b+=line(175,140,270,197)+line(525,140,430,197)
b+=box(170,200,360,60,'Crossing: 8 + 1 = 9','#d8e9df')
b+=text(350,303,'Best interval: 8, −2, 3',25)
b+=text(350,350,'Parent: (total, prefix, suffix, best) = (3, 7, 5, 9)',23)
figures['subarray']=fig('Combine adjacent four-component maximum-subarray summaries',390,b,'Figure 2. The left suffix eight joins the right prefix negative two plus three. The crossing interval beats both internal answers. The four numbers in each summary are total, best nonempty prefix, best nonempty suffix and best nonempty interval. Endpoints of the winning interval are two and five in zero-based half-open notation.')

b=text(350,31,'Window height δ; two half-specific four-cell grids',23)
for x,fill in [(110,'#e1edf6'),(350,'#e1eee4')]:
 for r in range(2):
  for c in range(2):
   b+=f'<rect x="{x+c*120}" y="{85+r*100}" width="120" height="100" fill="{fill}" stroke="#93afbf"/>'
b+=f'<line x1="350" y1="72" x2="350" y2="300" stroke="#3d6480" stroke-width="3" stroke-dasharray="7 5"/>'
b+=text(230,331,'Left membership',22)+text(470,331,'Right membership',22)
for x,y,color in [(145,111,'#3c7097'),(293,120,'#3c7097'),(165,232,'#3c7097'),(305,220,'#3c7097'),(364,123,'#46765b'),(530,149,'#46765b'),(393,240,'#46765b'),(557,240,'#46765b')]:
 b+=f'<circle cx="{x}" cy="{y}" r="7" fill="{color}"/>'
b+=text(230,65,'Width δ',22)+text(470,65,'Width δ',22)
b+=text(350,378,'At most 4 left + 4 right = 8 including current point',22)
b+=text(350,418,'At most 7 successors can improve the distance',23)
figures['geometry']=fig('Closest-pair packing with separate recursive-half membership',455,b,'Figure 3. The schematic shows four cells per half, each with side length delta divided by two in the mathematical proof; screen axes are drawn at different scales. Same-half points cannot share a cell. The figure is a packing illustration, not a numerical closest-pair dataset. A left and a right point may be arbitrarily close across the divider, and tied divider coordinates retain their assigned half.')

b=text(350,32,'Three recursive products recover all four terms',24)
for x,label in [(20,'z₂ = high × high'),(250,'z₀ = low × low'),(480,'zᵈ = difference × difference')]:
 b+=box(x,75,200,70,label)
b+=line(120,145,275,207)+line(350,145,350,207)+line(580,145,425,207)
b+=box(155,210,390,65,'Mixed = z₂ + z₀ − zᵈ','#d8e9df')
b+=text(350,327,'Result = high shift + mixed shift + low',24)
b+=text(350,370,'Shift widths: 2m, m, 0; m is the low-part width',22)
# Narrow labels are explicit two-line text to retain legibility.
b=b.replace(text(580.0,118.0,'zᵈ = difference × difference',24),text(580,105,'zᵈ = (high − low)',20)+text(580,130,'× (high − low)',20))
figures['karatsuba']=fig('Karatsuba difference-product dependency graph',410,b,'Figure 4. The third product multiplies the signed high-minus-low differences. Its index d labels the difference product. All three products are evaluated on smaller operands; additions and shifts reconstruct the exact full product. The low-part width determines the shifts even for odd original digit counts.')

b=text(350,32,'FFT butterfly: two children, two parent evaluations',23)
b+=box(30,90,160,60,'Eⱼ')+box(30,235,160,60,'Oⱼ')
b+=box(275,235,140,60,'× ωʲ','#d8e9df')
b+=box(490,90,175,60,'Eⱼ + ωʲOⱼ')+box(490,235,175,60,'Eⱼ − ωʲOⱼ')
for args in [(190,120,490,120),(190,265,275,265),(415,265,490,265),(190,120,490,265),(415,265,490,120)]:b+=line(*args)
b+=text(350,345,'Upper output: index j; lower output: index j + N/2',21)
b+=text(350,386,'Both children use the primitive root squared',23)
figures['fft']=fig('Two-output Fourier butterfly with a shared twiddle product',420,b,'Figure 5. The even child provides E at index j; the odd child provides O at index j. Multiply O once by the twiddle factor and reuse it in a sum and a difference. Crossing dependency lines are connections, not extra arithmetic operations. Child roots have half the parent order.')
def svg_indices(m):
 s=m.group(2)
 for char,index,position in [('₂','2','sub'),('₀','0','sub'),('ⱼ','j','sub'),('ʲ','j','super'),('ᵈ','d','sub')]:
  s=s.replace(char,f'<tspan baseline-shift="{position}" font-size=".72em">{index}</tspan>')
 return m.group(1)+s+'</text>'
for key,value in figures.items():
 value=re.sub(r'(<text[^>]*>)(.*?)</text>',svg_indices,value)
 source=source.replace(f'<!-- FIGURE:{key} -->',value)

def row(s):return '<mrow>'+s+'</mrow>'
def mi(s):return '<mi>'+html.escape(str(s))+'</mi>'
def mn(s):return '<mn>'+str(s)+'</mn>'
def op(s):return '<mo>'+html.escape(s)+'</mo>'
def sub(s,t):return '<msub>'+s+t+'</msub>'
def sup(s,t):return '<msup>'+s+t+'</msup>'
def frac(s,t):return '<mfrac>'+row(s)+row(t)+'</mfrac>'
def par(s):return row(op('(')+s+op(')'))
def call(s,arg):return row(mi(s)+par(arg))
def eq(a,b):return row(a+op('=')+b)
def math(s,label):return '<div class="formula-block"><math display="block" aria-label="'+html.escape(label)+'">'+row(s)+'</math></div>'
def table(lines):
 return '<mtable displaystyle="true" columnalign="left" rowspacing=".6em">'+''.join('<mtr><mtd>'+row(a)+'</mtd></mtr>' for a in lines)+'</mtable>'
def v(a,b):return sub(mi(a),mi(b))
summary=[]
for a,rhs in [('T',v('T','X')+op('+')+v('T','Y')),('P',call('max',v('P','X')+op(',')+v('T','X')+op('+')+v('P','Y'))),('S',call('max',v('S','Y')+op(',')+v('T','Y')+op('+')+v('S','X'))),('B',call('max',v('B','X')+op(',')+v('B','Y')+op(',')+v('S','X')+op('+')+v('P','Y')))]:
 summary.append(eq(v(a,'XY'),rhs))
source=source.replace('<!-- MATH:summary -->',math(table(summary),'Four exact rules for concatenating adjacent segment summaries'))
source=source.replace('<!-- MATH:split -->',math(table([eq(mi('x'),v('x','H')+sup(mi('B'),mi('m'))+op('+')+v('x','L')),eq(mi('y'),v('y','H')+sup(mi('B'),mi('m'))+op('+')+v('y','L'))]),'Split both integers using the same low-part digit width'))
source=source.replace('<!-- MATH:karatsuba -->',math(eq(mi('xy'),v('z','2')+sup(mi('B'),row(mn(2)+mi('m')))+op('+')+par(v('z','2')+op('+')+v('z','0')+op('−')+v('z','d'))+sup(mi('B'),mi('m'))+op('+')+v('z','0')),'Reconstruct the product from three smaller products'))
def matrix(a,b,c,d):return row(op('[')+'<mtable columnspacing="1em"><mtr><mtd>'+a+'</mtd><mtd>'+b+'</mtd></mtr><mtr><mtd>'+c+'</mtd><mtd>'+d+'</mtd></mtr></mtable>'+op(']'))
source=source.replace('<!-- MATH:blocks -->',math(table([eq(mi('X'),matrix(*map(mi,['A','B','C','D']))),eq(mi('Y'),matrix(*map(mi,['E','F','G','H']))),eq(mi('XY'),matrix(mi('AE')+op('+')+mi('BG'),mi('AF')+op('+')+mi('BH'),mi('CE')+op('+')+mi('DG'),mi('CF')+op('+')+mi('DH')))]),'Compatible input blocks and their ordinary ordered products'))
P=lambda n:sub(mi('P'),mn(n))
products=[mi('A')+par(mi('F')+op('−')+mi('H')),par(mi('A')+op('+')+mi('B'))+mi('H'),par(mi('C')+op('+')+mi('D'))+mi('E'),mi('D')+par(mi('G')+op('−')+mi('E')),par(mi('A')+op('+')+mi('D'))+par(mi('E')+op('+')+mi('H')),par(mi('B')+op('−')+mi('D'))+par(mi('G')+op('+')+mi('H')),par(mi('A')+op('−')+mi('C'))+par(mi('E')+op('+')+mi('F'))]
source=source.replace('<!-- MATH:strassen-products -->',math(table([eq(P(j+1),s) for j,s in enumerate(products)]),'Seven fixed Strassen product definitions'))
blocks=[P(5)+op('+')+P(4)+op('−')+P(2)+op('+')+P(6),P(1)+op('+')+P(2),P(3)+op('+')+P(4),P(1)+op('+')+P(5)+op('−')+P(3)+op('−')+P(7)]
source=source.replace('<!-- MATH:strassen-result -->',math(table([eq(sub(mi('R'),mn(name)),s) for name,s in zip([11,12,21,22],blocks)]),'Recombination into four output blocks'))
wj=sup(mi('ω'),mi('j'))
source=source.replace('<!-- MATH:butterfly -->',math(table([eq(v('Y','j'),v('E','j')+op('+')+wj+v('O','j')),eq(sub(mi('Y'),row(mi('j')+op('+')+frac(mi('N'),mn(2)))),v('E','j')+op('−')+wj+v('O','j'))]),'The two butterfly outputs use the same twiddle product'))
shifted=sup(mi('ω'),row(mi('j')+op('+')+frac(mi('N'),mn(2))))
source=source.replace('<!-- MATH:parity -->',math(table([eq(sup(par(shifted),mn(2)),sup(mi('ω'),row(mn(2)+mi('j')))),eq(shifted,op('−')+sup(mi('ω'),mi('j')))]),'Root identities justify the shared child evaluations and negative butterfly branch'))
sumj='<munderover>'+op('∑')+eq(mi('j'),mn(0))+row(mi('N')+op('−')+mn(1))+'</munderover>'
inv=eq(v('a','t'),frac(mn(1),mi('N'))+sumj+v('Y','j')+sup(mi('ω'),row(op('−')+mi('j')+mi('t'))))
source=source.replace('<!-- MATH:inverse -->',math(inv,'Inverse Fourier coefficient with full-length normalization and negative exponent'))
sumr='<munderover>'+op('∑')+eq(mi('r'),mn(0))+row(mi('N')+op('−')+mn(1))+'</munderover>'
source=source.replace('<!-- MATH:forward -->',math(eq(v('Y','j'),sumr+v('a','r')+sup(mi('ω'),row(mi('j')+mi('r')))),'Forward Fourier transform with positive exponent'))
source=source.replace('<!-- MATH:geometric -->',math(table([eq(v('S','q'),sumj+sup(mi('ω'),row(mi('j')+mi('q')))),eq(v('S','q'),frac(mn(1)+op('−')+sup(mi('ω'),row(mi('N')+mi('q'))),mn(1)+op('−')+sup(mi('ω'),mi('q'))))+op('=')+mn(0)]),'Geometric sum vanishes for a nonzero exponent difference modulo the transform length'))
norm=lambda s:row(op('‖')+s+op('‖'))
identities=[eq(sup(mi('F'),op('*'))+mi('F'),mi('NI')),eq(sup(norm(mi('Fa')),mn(2)),mi('N')+sup(norm(mi('a')),mn(2))),eq(mi('U'),frac(mi('F'),'<msqrt>'+mi('N')+'</msqrt>'))]
source=source.replace('<!-- MATH:normalization -->',math(table(identities),'Unnormalized Fourier norm scaling and the normalized unitary matrix'))

lab='''<section class="lab" id="subarray-lab" aria-label="Exact maximum-subarray summary laboratory"><div class="lab-actions"><button data-preset="crossing">Crossing answer</button><button data-preset="negative">All negative</button><button data-preset="left">Left-side answer</button><button data-preset="ties">Equal best sums</button></div><form id="subarray-form"><label>Integer sequence<input id="subarray-input" value="4, -6, 8, -2, 3, -9, 5" required></label><label>Split position<input id="subarray-split" type="number" min="1" max="6" step="1" value="3" required></label><button type="submit">Compare both methods</button></form><div id="subarray-output" aria-live="polite"></div><p>Enter two through sixteen integers between negative ninety-nine and ninety-nine, separated by commas or spaces. The split must leave both halves nonempty. All sums lie safely within exact integer range. The displayed witness uses zero-based half-open endpoints.</p></section>'''
source=source.replace('<!-- LAB:subarray -->',lab)
source=re.sub(r'\$([^$\n]+)\$',math_inline,source)
body=normalize_scripts(normalize_math(MarkdownIt('commonmark',{'html':True}).enable('table').render(source)))
anchors=['sources','design','merging','subarrays','geometry','karatsuba','strassen','fourier','methods','problems','review','laboratory','references']
it=iter(anchors)
body=re.sub(r'<h2>(.*?)</h2>',lambda m:f'<h2 id="{next(it)}">{m.group(1)}</h2>',body)
assert '<!--' not in body and '$' not in body
nav=' '.join(f'<a href="#{a}">{a.capitalize()}</a>' for a in anchors)
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Divide and Conquer: Design and Analysis · Doctoral CSE 1406</title><meta name="description" content="Four principal reviewed universities plus ETH, rigorous algorithms and proofs, 48 fully worked problems, 88 complete rules, five original diagrams and an exact summary laboratory."><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="a_divide.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-2">← Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Algorithms · Week 2</p><h1>Divide and Conquer: Design and Analysis</h1><p>English review draft · five reviewed universities · 48 fully worked problems · 88 complete examination rules</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">← Chapter library</a></p></main><script src="a_divide.js"></script></body></html>'''
(ROOT/'dist/chapters/a_divide.html').write_text(page,encoding='utf-8')
audit=(base/'a_divide-source-audit.md').read_text(encoding='utf-8')
auditbody=normalize_scripts(normalize_math(MarkdownIt('commonmark',{'html':True}).enable('table').render(audit)))
(ROOT/'dist/reviews/a_divide-sources.html').write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Divide-and-conquer source comparison and reading audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/a_divide.html">← Divide-and-conquer chapter</a></p><article class="lesson">{auditbody}</article></main></body></html>',encoding='utf-8')
p=ROOT/'dist/lessons.json';rows=json.loads(p.read_text());week=next(w for w in rows if w['week']==2)
week['chapters']=[c for c in week['chapters'] if c['topicId']!='a_divide']+[{'topicId':'a_divide','title':'Divide and conquer: design and analysis','status':'draft','url':'chapters/a_divide.html'}]
p.write_text(json.dumps(rows,indent=2)+'\n')
print('Rendered divide-and-conquer chapter: 48 problems, 88 rules, five diagrams, native MathML and exact summary lab.')
