"""Reproduce the recurrence chapter, its semantic mathematics and original figures."""
import html,json,re
from pathlib import Path
from markdown_it import MarkdownIt
from math_typography import normalize_math,normalize_scripts
ROOT=Path(__file__).resolve().parents[1];base=ROOT/'research'
source=(base/'a_recurrence.en.md').read_text(encoding='utf-8')
for name in ('problems','review'):
 source=source.replace(f'<!-- INCLUDE:{name} -->',(base/f'a_recurrence-{name}.en.md').read_text(encoding='utf-8'))

def text(x,y,s,size=22):
 return f'<text x="{x}" y="{y}" text-anchor="middle" fill="#16384d" font-size="{size}">{html.escape(s)}</text>'
def line(x,y,z,w):
 return f'<line x1="{x}" y1="{y}" x2="{z}" y2="{w}" stroke="#547e95" stroke-width="2.3"/>'
def node(x,y,s):
 return f'<circle cx="{x}" cy="{y}" r="23" fill="#edf5f9" stroke="#87adbf"/>'+text(x,y+8,s)
def fig(title,height,body,caption):
 return f'<figure class="logic-diagram"><svg viewBox="0 0 700 {height}" role="img" aria-label="{html.escape(title)}"><title>{html.escape(title)}</title>{body}</svg><figcaption>{caption}</figcaption></figure>'

body=text(350,32,'Two half-size children; input 16; terminal cost 1',23)
for col,(q,name,values) in enumerate([(0,'Leaf dominated',[1,2,4,8,16]),(1,'Balanced internal levels',[16,16,16,16,16]),(2,'Root dominated',[256,128,64,32,16])]):
 x=120+230*col
 body+=text(x,72,name,20)+text(x,108,f'Toll exponent q = {q}',20)
 for j,value in enumerate(values):
  y=145+45*j
  width=25+140*value/max(values)
  body+=f'<rect x="{x-90}" y="{y-20}" width="{width}" height="31" rx="5" fill="'+('#c8e2d5' if j==4 else '#dceaf3')+'" stroke="#97b5c7"/>'
  body+=text(x,y+3,f'{j}: {value}',20)
 body+=text(x,388,f'Total = {sum(values)}',23)
figures={'levels':fig('Exact contributions at each depth for three different tolls',420,body,'Figure 1. Each label is depth followed by the full contribution of that level. Depths zero through three are internal. The green row at depth four is the terminal leaf cost, which is sixteen in every column. The balanced example has four internal levels, not five; its total is eighty. Bar widths are normalized separately within each column, so compare their labels rather than widths across columns.')}

body=text(350,32,'Normalized internal work: sum of r to the power k',23)
body+=text(93,83,'Depth h',21)
for x,s in [(255,'k = −1/2'),(435,'k = −1'),(610,'k = −2')]:body+=text(x,83,s,23)
for row,h in enumerate([4,16,64,256]):
 y=133+53*row;body+=text(93,y,str(h),23)
 for x,k in [(255,-.5),(435,-1),(610,-2)]:
  value=sum(r**k for r in range(1,h+1))
  body+=text(x,y,f'{value:.3f}',24)
body+=text(350,370,'Threshold: growth, harmonic growth, convergence',23)
figures['critical']=fig('Finite depth sums reveal the critical logarithmic threshold',400,body,'Figure 2. These are computed finite sums, excluding the positive normalized terminal contribution. The first column grows on the scale of the square root of depth; the middle grows logarithmically in depth; the last tends to a finite limit. Since depth is proportional to log input size, the middle column generates log log input size. The proof comes from integral comparison, rather than from extrapolating these four measurements.')

coords={'r':(350,52,'5'),'a':(160,145,'2'),'b':(510,145,'3'),'c':(80,238,'1'),'d':(230,238,'1'),'e':(440,238,'1'),'f':(600,238,'2'),'g':(540,328,'1'),'h':(660,328,'1')}
body=''
for a,b in [('r','a'),('r','b'),('a','c'),('a','d'),('b','e'),('b','f'),('f','g'),('f','h')]:
 x,y,_=coords[a];z,w,_=coords[b];body+=line(x,y+23,z,w-23)
for x,y,s in coords.values():body+=node(x,y,s)
body+=text(350,396,'Leaf depths: 2, 2, 2, 3, 3; their sum is 12',22)
body+=text(350,432,'Four internal nodes: comparison total 12 − 4 = 8',22)
figures['rounded']=fig('Balanced integer splits of five have leaves at two different depths',465,body,'Figure 3. Every node is labeled by its input size. The five singleton leaves lie at depths two and three, so treating every leaf as depth three is incorrect. Charging each size toll to descendant leaves gives twelve. Subtract one comparison for each of the four internal merges to obtain eight, agreeing with the exact formula. The drawing retains the actual floor and ceiling sizes.')

body=text(350,33,'Child ratios: 1/5 and 7/10; combined ratio 9/10',23)
for j in range(5):
 y=88+55*j;value=100*(.9**j)
 body+=f'<rect x="92" y="{y-19}" width="{value*4.8}" height="31" rx="5" fill="#dceaf3" stroke="#97b5c7"/>'
 body+=text(39,y+4,str(j),22)+text(610,y+4,f'{value:.2f}',23)
body+=text(350,386,'Unterminated mass at depth j: 100 × (9/10) to power j',21)
body+=text(350,422,'Stopping nodes only decrease the active mass',22)
figures['mass']=fig('Total size contracts geometrically for unequal recursive branches',450,body,'Figure 4. Before any stopping, depth zero has mass one hundred, depth one ninety, and depth two eighty-one. Linear internal tolls follow this geometric upper envelope. Stopped nodes remove mass, while terminal costs require their own bound. The ideal unrounded mass model explains the linear bound; the adjoining substitution proof handles additive integer-rounding errors explicitly.')
for name,f in figures.items():source=source.replace(f'<!-- FIGURE:{name} -->',f)

def power(base,exponent):return f'<msup>{base}{exponent}</msup>'
def sub(base,index):return f'<msub>{base}{index}</msub>'
def mi(s):return f'<mi>{s}</mi>'
def mn(s):return f'<mn>{s}</mn>'
def row(s):return f'<mrow>{s}</mrow>'
def call(name,arg):return row(mi(name)+row('<mo>(</mo>'+arg+'<mo>)</mo>'))
def math(s,label):return f'<div class="formula-block"><math display="block" aria-label="{html.escape(label)}">{row(s)}</math></div>'
ph=power(mi('a'),mi('h'));pj=power(mi('a'),mi('j'))
summation='<munderover><mo>∑</mo>'+row(mi('j')+'<mo>=</mo>'+mn(0))+row(mi('h')+'<mo>−</mo>'+mn(1))+'</munderover>'
tree=call('T',mi('n'))+'<mo>=</mo>'+ph+call('T',mn(1))+'<mo>+</mo>'+summation+pj+call('f','<mfrac>'+mi('n')+power(mi('b'),mi('j'))+'</mfrac>')
source=source.replace('<!-- MATH:tree -->',math(tree,'Total equals terminal leaf contribution plus the sum of internal level contributions'))
up=power(mi('u'),row(mi('p')+'<mo>+</mo>'+mn(1)))
integral='<msubsup><mo>∫</mo>'+mn(1)+mi('x')+'</msubsup><mfrac>'+call('g',mi('u'))+up+'</mfrac><mspace width=".3em"/>'+mi('d')+mi('u')
akra=call('T',mi('x'))+'<mo>=</mo>'+call('Θ',power(mi('x'),mi('p'))+row('<mo>(</mo>'+mn(1)+'<mo>+</mo>'+integral+'<mo>)</mo>'))
source=source.replace('<!-- MATH:akra -->',math(akra,'Akra Bazzi integral estimate with its positive base contribution'))
ai=sub(mi('a'),mi('i'));bi=sub(mi('b'),mi('i'));wi=sub(mi('w'),mi('i'))
sum_i='<munder><mo>∑</mo>'+mi('i')+'</munder>'
delta=call('Δ',mi('x'))+'<mo>=</mo>'+call('F',mi('x'))+'<mo>−</mo>'+sum_i+ai+call('F',bi+mi('x'))
gap=call('Δ',mi('x'))+'<mo>=</mo>'+power(mi('x'),mi('p'))+sum_i+wi+'<msubsup><mo>∫</mo>'+row(bi+mi('x'))+mi('x')+'</msubsup><mfrac>'+call('g',mi('u'))+up+'</mfrac><mspace width=".3em"/>'+mi('d')+mi('u')
source=source.replace('<!-- MATH:gap -->',math(delta,'Define the parent minus weighted children gap')+math(gap,'The gap is a positive weighted sum of integrals over shrinking intervals'))

lab='''<section class="lab" id="recurrence-lab" aria-label="Exact recurrence-level laboratory"><div class="lab-actions"><button data-preset="leaves">Leaf dominated</button><button data-preset="balanced">Balanced levels</button><button data-preset="root">Root dominated</button><button data-preset="chain">Single chain</button><button data-preset="base">Change the base cost</button></div><form id="recurrence-form"><label>Branch count a<input id="recurrence-a" type="number" value="2" min="1" max="6" step="1" required></label><label>Shrink divisor b<input id="recurrence-b" type="number" value="2" min="2" max="6" step="1" required></label><label>Toll exponent q<input id="recurrence-q" type="number" value="1" min="0" max="4" step="1" required></label><label>Tree height h<input id="recurrence-h" type="number" value="4" min="0" max="8" step="1" required></label><label>Terminal base cost<input id="recurrence-base" type="number" value="1" min="1" max="20" step="1" required></label><button type="submit">Calculate every level</button></form><div id="recurrence-output" aria-live="polite"></div><p>All calculations use exact arbitrary-size integers. An independently accumulated level sum must agree with the bottom-up recurrence before a result is displayed. The terminal row is shown separately; height zero has no internal calls. The parameter bounds keep the table readable.</p></section>'''
source=source.replace('<!-- LAB:recurrence -->',lab)
for label,symbol in [('Branch count','a'),('Shrink divisor','b'),('Toll exponent','q'),('Tree height','h')]:
 source=source.replace(f'{label} {symbol}<input',f'{label} <span class="math-inline">{symbol}</span><input')

def math_inline(m):
 s=html.escape(m.group(1))
 while re.search(r'\^\{([^{}]+)\}',s):s=re.sub(r'\^\{([^{}]+)\}',r'<sup>\1</sup>',s)
 s=re.sub(r'\^([A-Za-z0-9]+)',r'<sup>\1</sup>',s)
 s=re.sub(r'_\{([^{}]+)\}',r'<sub>\1</sub>',s)
 s=re.sub(r'_(\d+|[A-Za-z])',r'<sub>\1</sub>',s)
 s=re.sub(r'\s*([∈∉→⇒⇔≡∧∨≤≥≠≈=+−×⋅])\s*',lambda op:'\u2009'+op.group(1)+'\u2009',s)
 return '<span class="math-inline">'+s+'</span>'
source=re.sub(r'\$([^$\n]+)\$',math_inline,source)
body=normalize_scripts(normalize_math(MarkdownIt('commonmark',{'html':True}).enable('table').render(source)))
anchors=['sources','model','unrolling','trees','substitution','master','logarithmic','rounding','unequal','resources','problems','review','laboratory','references']
it=iter(anchors);body=re.sub(r'<h2>(.*?)</h2>',lambda m:f'<h2 id="{next(it)}">{m.group(1)}</h2>',body)
assert '<!--' not in body and '$' not in body
nav=' '.join(f'<a href="#{x}">{x.capitalize()}</a>' for x in anchors)
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Algorithmic Recurrences and Solution Theorems · Doctoral CSE 1406</title><meta name="description" content="Four reviewed principal university courses, rigorous recurrence proofs, 40 fully solved problems, 80 complete examination rules, four original diagrams and an exact level laboratory."><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="a_recurrence.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-2">← Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Algorithms · Week 2</p><h1>Algorithmic Recurrences and Solution Theorems</h1><p>Student-approved chapter · four principal university courses · 40 fully worked problems · 80 complete examination rules</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">← Chapter library</a></p></main><script src="a_recurrence.js"></script></body></html>'''
(ROOT/'dist/chapters/a_recurrence.html').write_text(page,encoding='utf-8')
audit=(base/'a_recurrence-source-audit.md').read_text(encoding='utf-8')
auditbody=normalize_scripts(normalize_math(MarkdownIt('commonmark',{'html':True}).enable('table').render(audit)))
(ROOT/'dist/reviews/a_recurrence-sources.html').write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Recurrence source comparison and reading audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/a_recurrence.html">← Recurrence chapter</a></p><article class="lesson">{auditbody}</article></main></body></html>',encoding='utf-8')
p=ROOT/'dist/lessons.json';rows=json.loads(p.read_text());week=next(w for w in rows if w['week']==2)
week['chapters']=[c for c in week['chapters'] if c['topicId']!='a_recurrence']+[{'topicId':'a_recurrence','title':'Algorithmic recurrences and solution theorems','status':'ready','url':'chapters/a_recurrence.html'}]
p.write_text(json.dumps(rows,indent=2)+'\n')
print('Rendered recurrence chapter with four diagrams, native MathML, 40 worked problems, and 80 rules.')
