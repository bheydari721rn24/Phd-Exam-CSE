"""Build one English relation chapter using shared mathematical typography."""
import html,json,re
from pathlib import Path
from markdown_it import MarkdownIt
from math_typography import normalize_math,normalize_scripts
ROOT=Path(__file__).resolve().parents[1]
base=ROOT/'research'
source=(base/'d_relations.en.md').read_text(encoding='utf-8')
for name in ('problems','review'):
 source=source.replace(f'<!-- INCLUDE:{name} -->',(base/f'd_relations-{name}.en.md').read_text(encoding='utf-8'))
source=source.replace('\\bar g','ḡ')
assert source.count('### Problem ')==46
assert not re.search(r'[\u0600-\u06ff]',source)
def edge(x1,y1,x2,y2,arrow=False):
 return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#547e95" stroke-width="2.3"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>'
def label(x,y,s):
 return f'<text x="{x}" y="{y}" text-anchor="middle" fill="#16384d" font-size="23">{s}</text>'
def node(x,y,s):
 return f'<circle cx="{x}" cy="{y}" r="22" fill="#f1f7fa" stroke="#87adbf"/>'+label(x,y+8,s)
def figure(title,height,inside,caption):
 return f'<figure class="logic-diagram"><svg viewBox="0 0 700 {height}" role="img" aria-label="{html.escape(title)}"><title>{title}</title>{inside}</svg><figcaption>{caption}</figcaption></figure>'
defs='<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="none" stroke="#547e95"/></marker></defs>'
composition=figure('Composition follows R and then S',280,defs+edge(105,130,320,80,True)+edge(105,130,320,200,True)+edge(375,80,592,130,True)+node(80,130,'a')+node(350,80,'b₁')+node(350,200,'b₂')+node(620,130,'c')+label(80,35,'A')+label(350,35,'B')+label(620,35,'C')+label(200,77,'R')+label(485,77,'S'),
 'Figure 1. The upper middle vertex witnesses the composite pair (a,c). The lower R-edge alone gives no composite pair because no S-edge leaves its target. Source and target copies remain distinct roles.')
partition_inside=''
for x,cl,items in [(20,'[0]',[0,3,6]),(255,'[1]',[1,4,7]),(490,'[2]',[2,5])]:
 partition_inside+=f'<rect x="{x}" y="25" width="190" height="210" rx="18" fill="#eef6f9" stroke="#87adbf"/>'+label(x+95,65,cl)
 for j,v in enumerate(items):partition_inside+=node(x+55+80*(j%2),120+75*(j//2),str(v))
partition=figure('Three equivalence classes partition a finite carrier',260,partition_inside,
 'Figure 2. Congruence modulo 3 restricted to {0,1,2,3,4,5,6,7}. Every element lies in one nonempty block; all ordered pairs inside a block belong to the relation, and no pair crosses blocks. Multiple representative labels name the same block.')
coords={1:(155,330),2:(80,235),3:(250,235),4:(80,140),6:(250,140),12:(155,45)}
hasse_inside=''.join(edge(*coords[a],*coords[b]) for a,b in [(1,2),(1,3),(2,4),(2,6),(3,6),(4,12),(6,12)])
hasse_inside+=''.join(node(x,y,str(v)) for v,(x,y) in coords.items())
# A separate four-element nonlattice has two incomparable lower and upper elements.
other={'a':(425,265),'b':(615,265),'u':(425,115),'v':(615,115)}
hasse_inside+=''.join(edge(*other[a],*other[b]) for a,b in [('a','u'),('a','v'),('b','u'),('b','v')])
hasse_inside+=''.join(node(x,y,v) for v,(x,y) in other.items())
hasse=figure('Divisibility covers and incomparable minimal upper bounds',390,hasse_inside,
 'Figure 3. Greater elements are above. Left: the divisor lattice of 12, with only cover edges. Right: both u and v bound {a,b}, but neither lies below the other, so that subset has no supremum in this four-element carrier. Edge crossings create no additional vertices.')
taskcoords={'A':(130,255),'B':(490,255),'C':(130,155),'D':(490,155),'E':(250,55),'F':(610,55)}
sched=''.join(f'<rect x="30" y="{y}" width="640" height="70" rx="10" fill="#eef6f9"/>' for y in [20,120,220])
sched+=''.join(edge(*taskcoords[a],*taskcoords[b]) for a,b in [('A','C'),('A','D'),('B','D'),('C','E'),('D','E'),('D','F')])
sched+=''.join(node(x,y,v) for v,(x,y) in taskcoords.items())
scheduling=figure('Unit task levels realize the critical path bound',320,sched,
 'Figure 4. Read upwards: {A,B} executes in slot 1, {C,D} in slot 2, and {E,F} in slot 3. Each edge is a prerequisite. The chain A,C,E certifies that fewer than three unit-time slots are impossible with unlimited processors.')
for name,diagram in [('composition',composition),('partition',partition),('hasse',hasse),('scheduling',scheduling)]:source=source.replace(f'<!-- FIGURE:{name} -->',diagram)
def math_inline(m):
 s=html.escape(m.group(1))
 s=re.sub(r'\^\{([^{}]+)\}',r'<sup>\1</sup>',s)
 s=re.sub(r'\^([A-Za-z0-9]+)',r'<sup>\1</sup>',s)
 s=re.sub(r'_\{([^{}]+)\}',r'<sub>\1</sub>',s)
 s=re.sub(r'_([A-Za-z])',r'<sub>\1</sub>',s)
 s=s.replace('R⁎','R<sup>∗</sup>')
 # A modest mathematical thin space keeps relational operators legible without
 # changing prose, URLs, indices, or program text.
 s=re.sub(r'\s*([∈∉⊆⊊⊂∪∩∖→⇒⇔↦≡∧∨∣≤≥≠≈∼≼≺⋖∘=+−×⋅])\s*',lambda op:'\u2009'+op.group(1)+'\u2009',s)
 return '<span class="math-inline">'+s+'</span>'
source=re.sub(r'\$([^$\n]+)\$',math_inline,source)
body=MarkdownIt('commonmark',{'html':True}).enable('table').render(source)
body=normalize_scripts(normalize_math(body))
body=body.replace('R⁎','R<sup>∗</sup>')
# SVG text is already mathematical; use semantic SVG indices, not fallback tiny glyphs.
body=body.replace('b₁','b<tspan baseline-shift="sub" font-size="16">1</tspan>').replace('b₂','b<tspan baseline-shift="sub" font-size="16">2</tspan>')
anchors=['sources','objects','properties','closures','equivalence','orders','bounds','scheduling','problems','review','laboratory','references']
it=iter(anchors)
body=re.sub(r'<h2>(.*?)</h2>',lambda m:f'<h2 id="{next(it)}">{m.group(1)}</h2>',body)
assert '<!-- INCLUDE' not in body and '$' not in body
nav=' '.join(f'<a href="#{x}">{x.capitalize()}</a>' for x in anchors)
result=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Relations, Equivalence, and Partial Orders · Doctoral CSE 1406</title><meta name="description" content="Deep English relation chapter: four principal university courses, a Cornell supplement, 46 worked problems, 72 exam rules, proofs, four figures and an interactive closure laboratory."><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="d_relations.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-2">← Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Discrete Mathematics · Chapter 5 · Week 2</p><h1>Relations, Equivalence, and Partial Orders</h1><p>Review draft awaiting your approval · four principal university courses and one focused supplement · 46 fully worked problems · 72 examination rules</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">← Chapter library</a></p></main><script src="d_relations.js"></script></body></html>'''
(ROOT/'dist/chapters/d_relations.html').write_text(result,encoding='utf-8')
audit=(base/'d_relations-source-audit.md').read_text(encoding='utf-8')
auditbody=MarkdownIt('commonmark',{'html':True}).enable('table').render(audit)
auditbody=normalize_scripts(normalize_math(auditbody))
(ROOT/'dist/reviews').mkdir(exist_ok=True)
(ROOT/'dist/reviews/d_relations-sources.html').write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Relations source audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/d_relations.html">← Relations chapter</a></p><article class="lesson">{auditbody}</article></main></body></html>',encoding='utf-8')
lessons=json.loads((ROOT/'dist/lessons.json').read_text(encoding='utf-8'))
week=next((w for w in lessons if w['week']==2),None)
if week is None:
 week={'week':2,'title':'Week 2 chapter drafts','description':'Full chapters appear individually after source synthesis and review. A draft awaits explicit student approval.','chapters':[]};lessons.append(week)
week['chapters']=[c for c in week['chapters'] if c['topicId']!='d_relations']+[{'topicId':'d_relations','title':'Relations, equivalence, and partial orders','status':'draft','url':'chapters/d_relations.html'}]
(ROOT/'dist/lessons.json').write_text(json.dumps(lessons,indent=2)+'\n',encoding='utf-8')
print('Rendered d_relations:',len(source.split()),'manuscript tokens separated by spaces; 46 worked problems, 72 rules, four diagrams')
