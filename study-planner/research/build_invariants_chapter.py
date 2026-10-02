"""Render the independently authored manuscript, semantic math, and vector figures."""
import html,json,re
from pathlib import Path
from markdown_it import MarkdownIt
from math_typography import normalize_math,normalize_scripts
ROOT=Path(__file__).resolve().parents[1];base=ROOT/'research'
source=(base/'d_invariants.en.md').read_text(encoding='utf-8')
for name in ('problems','review'):source=source.replace(f'<!-- INCLUDE:{name} -->',(base/f'd_invariants-{name}.en.md').read_text(encoding='utf-8'))
def text(x,y,s,size=22):return f'<text x="{x}" y="{y}" text-anchor="middle" fill="#16384d" font-size="{size}">{html.escape(s)}</text>'
def node(x,y,s,fill='#edf5f9',radius=24):return f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}" stroke="#87adbf"/>'+text(x,y+8,s)
def line(x,y,z,w):return f'<line x1="{x}" y1="{y}" x2="{z}" y2="{w}" stroke="#547e95" stroke-width="2.3" marker-end="url(#arrow)"/>'
defs='<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="none" stroke="#547e95"/></marker></defs>'
def figure(title,height,body,caption):return f'<figure class="logic-diagram"><svg viewBox="0 0 700 {height}" role="img" aria-label="{html.escape(title)}"><title>{title}</title>{defs}{body}</svg><figcaption>{caption}</figcaption></figure>'
body=text(350,35,'P = {0,1,2}; R = {0,1}',25)
body+= '<rect x="35" y="60" width="495" height="165" rx="18" fill="#edf5f9" stroke="#87adbf"/>'
body+= '<rect x="50" y="78" width="305" height="100" rx="15" fill="#e1f0e5" stroke="#80aa8e"/>'
body+=line(115,128,242,128)+line(468,128,608,128)
for x,s,fill in [(90,'0','#d7eadf'),(270,'1','#d7eadf'),(440,'2','#dceaf2'),(635,'3','#fff1e6')]:body+=node(x,128,s,fill)
body+=text(202,207,'reachable')+text(440,207,'unreachable')+text(635,207,'outside P')
body+=text(350,267,'J = {0,1} excludes the bad predecessor',23)
figures={'closure':figure('A reachable property can fail preservation at an unreachable state',305,body,'Figure 1. The blue candidate includes state 2, so the edge from 2 to 3 violates its preservation. The green reachable set contains only 0 and 1; every actual execution stays green. Strengthening the certificate removes the unreachable bad predecessor. The arrow into 0 denotes no additional transition; the initial state is explicitly 0 in the text.')}
# No initial-arrow symbol is drawn; the caption is deliberately literal.
figures['closure']=figures['closure'].replace(' The arrow into 0 denotes no additional transition; the initial state is explicitly 0 in the text.',' The initial state is 0.')
body=text(350,35,'x + 2y = 10',28)
for i,(x,y) in enumerate([(0,5),(2,4),(4,3),(6,2),(8,1),(10,0)]):
 center=50+120*i
 body+=f'<rect x="{center-39}" y="70" width="78" height="65" rx="12" fill="'+('#d7eadf' if (x,y)==(4,3) else '#edf5f9')+'" stroke="#87adbf"/>'+text(center,110,f'({x},{y})',21)
 if i<5:body+=line(center+42,88,center+77,88)+line(center+77,119,center+42,119)
body+=text(350,185,'(x,y) → (x + 2,y − 1) or (x − 2,y + 1)',23)+text(350,223,'Each enabled move stays on the same weighted level',22)
figures['conservation']=figure('Six feasible states share a conserved weighted sum',255,body,'Figure 2. Coordinates are nonnegative integers, and the highlighted start is (4,3). Opposite moves connect all six feasible points on this level. This constructive connectivity is specific to this move set; conservation alone does not establish it in a different system.')
body=text(350,35,'A full tree: each internal node has two children',24)
for x,y,z,w in [(332,99,190,156),(368,99,508,156),(503,205,448,267),(536,204,610,267)]:body+=line(x,y,z,w)
for x,y,s,fill in [(350,80,'N','#dceaf2'),(175,180,'2','#d7eadf'),(520,180,'N','#dceaf2'),(435,290,'5','#d7eadf'),(625,290,'7','#d7eadf')]:body+=node(x,y,s,fill)
body+=text(160,270,'I = 2')+text(160,305,'L = 3')+text(160,340,'N = 5')+text(480,350,'flatten(T) = [2,5,7]',23)
figures['tree']=figure('Full binary-tree counts and leaf output order',385,body,'Figure 3. Blue nodes are the two internal constructors and green nodes are the three data-bearing leaves. Total node count is five. In the node labels, N names a constructor; in the count N = 5, N denotes total nodes. The leaf sequence is read left-to-right, and the identity is leaves = internal nodes + 1.')
body=text(350,35,'Primary coordinate first: rank = (y,x)',25)
body+=text(95,103,'(2,0)')+text(290,103,'(1,5)')+text(475,103,'(1,4)')+text(650,103,'(1,0)')
body+=line(133,94,243,94)+line(335,94,430,94)+line(520,94,595,94)+text(185,75,'reset',20)+text(565,75,'…',24)
body+='<path d="M645,130 C650,175 310,175 293,217" fill="none" stroke="#547e95" stroke-width="2.3" marker-end="url(#arrow)"/>'
body+=text(420,235,'primary drops; x resets',21)+text(290,263,'(0,M)')+text(465,263,'(0,M − 1)')+text(640,263,'(0,0)')
body+=line(337,254,405,254)+line(525,254,591,254)+text(562,235,'…',24)+text(350,323,'Each chosen M is finite; the choices are unbounded',23)
figures['lexicographic']=figure('Lexicographic rank decreases despite secondary resets',360,body,'Figure 4. The primary counter y decreases on a reset; between resets only x decreases. Dots abbreviate repeated unit decrements rather than adding direct transition edges. Every actual path is finite, while the reset value M can make the family of lengths arbitrarily large.')
for name,s in figures.items():source=source.replace(f'<!-- FIGURE:{name} -->',s)
reach='''<div class="formula-block"><math display="block" aria-label="The reachable set is the union over k from zero through infinity of R sub k"><mrow><mi>R</mi><mo>=</mo><munderover><mo>⋃</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mo>∞</mo></munderover><msub><mi>R</mi><mi>k</mi></msub></mrow></math></div>'''
prefix='''<div class="formula-block"><math display="block" aria-label="The invariant is zero less than or equal to i less than or equal to n, and total equals the sum over j from zero through i minus one of a sub j"><mrow><mn>0</mn><mo>≤</mo><mi>i</mi><mo>≤</mo><mi>n</mi><mo>,</mo><mspace width="1em"/><mi mathvariant="normal">total</mi><mo>=</mo><munderover><mo>∑</mo><mrow><mi>j</mi><mo>=</mo><mn>0</mn></mrow><mrow><mi>i</mi><mo>−</mo><mn>1</mn></mrow></munderover><msub><mi>a</mi><mi>j</mi></msub></mrow></math></div>'''
source=source.replace('<!-- MATH:reachability -->',reach).replace('<!-- MATH:prefix -->',prefix)
lab='''<section class="lab" id="invariant-lab" aria-label="Finite invariant and termination laboratory"><div class="lab-actions"><button data-preset="noninductive">True but not inductive</button><button data-preset="inductive">Inductive safety with a cycle</button><button data-preset="unsafe">Reachable violation</button><button data-preset="chain">Terminating chain</button><button data-preset="cycle">Reachable cycle</button><button data-preset="badrank">Terminating with a bad rank</button></div><div id="invariant-input"></div><div id="invariant-output" aria-live="polite"></div><p>Preservation examines every edge from the proposed truth set. The rank and cycle reports examine only states reachable from the fixed initial state <span class="math-inline">0</span>.</p></section>'''
source=source.replace('<!-- LAB:invariants -->',lab)
def math_inline(m):
 s=html.escape(m.group(1));s=re.sub(r'\^\{([^{}]+)\}',r'<sup>\1</sup>',s);s=re.sub(r'\^([A-Za-z0-9]+)',r'<sup>\1</sup>',s)
 s=re.sub(r'_\{([^{}]+)\}',r'<sub>\1</sub>',s);s=re.sub(r'_(\d+|[A-Za-z])',r'<sub>\1</sub>',s)
 s=re.sub(r'\s*([∈∉⊆⊊⊂∪∩∖→⇒⇔↦≡∧∨∣≤≥≠≈∼≼≺⋖∘=+−×⋅⊕⧺])\s*',lambda op:'\u2009'+op.group(1)+'\u2009',s)
 return '<span class="math-inline">'+s+'</span>'
source=re.sub(r'\$([^$\n]+)\$',math_inline,source)
body=normalize_scripts(normalize_math(MarkdownIt('commonmark',{'html':True}).enable('table').render(source)))
anchors=['sources','states','invariants','discovery','loops','rankings','recursion','structural','accumulators','advanced','problems','review','laboratory','references'];it=iter(anchors)
body=re.sub(r'<h2>(.*?)</h2>',lambda m:f'<h2 id="{next(it)}">{m.group(1)}</h2>',body)
assert '<!--' not in body and '$' not in body and '\\' not in body
nav=' '.join(f'<a href="#{x}">{x.capitalize()}</a>' for x in anchors)
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Invariants and Recursive Reasoning · Doctoral CSE 1406</title><meta name="description" content="Deep English chapter with four reviewed principal university courses, 49 fully worked problems, 80 complete examination rules, four original figures, semantic mathematical notation, and an exact finite-state laboratory."><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="d_invariants.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-2">← Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Discrete Mathematics · Chapter 7 · Week 2</p><h1>Invariants and Recursive Reasoning</h1><p>Review draft awaiting your approval · four principal university courses · 49 fully worked problems · 80 complete examination rules</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">← Chapter library</a></p></main><script src="d_invariants.js"></script></body></html>'''
(ROOT/'dist/chapters/d_invariants.html').write_text(page,encoding='utf-8')
audit=(base/'d_invariants-source-audit.md').read_text(encoding='utf-8');auditbody=normalize_scripts(normalize_math(MarkdownIt('commonmark',{'html':True}).enable('table').render(audit)))
(ROOT/'dist/reviews/d_invariants-sources.html').write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Invariants source audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/d_invariants.html">← Invariants chapter</a></p><article class="lesson">{auditbody}</article></main></body></html>',encoding='utf-8')
p=ROOT/'dist/lessons.json';rows=json.loads(p.read_text());week=next(w for w in rows if w['week']==2)
week['chapters']=[c for c in week['chapters'] if c['topicId']!='d_invariants']+[{'topicId':'d_invariants','title':'Invariants and recursive reasoning','status':'draft','url':'chapters/d_invariants.html'}]
p.write_text(json.dumps(rows,indent=2)+'\n')
print('Invariants rendered:',len(source.split()),'space-separated manuscript tokens; 49 worked problems, 80 rules, four figures.')
