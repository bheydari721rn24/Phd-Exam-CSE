"""Build the original matrix lesson with semantic MathML arrays and fractions."""
from pathlib import Path
import json
import re
from html import escape, unescape
from markdown_it import MarkdownIt
from math_typography import normalize_math, normalize_scripts

ROOT=Path(__file__).resolve().parents[1]
source='\n\n'.join((ROOT/'research'/name).read_text(encoding='utf-8') for name in
 ('l_matrices.en.md','l_matrices-problems.en.md','l_matrices-review.en.md'))
assert source.count('### Problem ')==36
assert not re.search(r'[\u0600-\u06ff]',source)
# HTML range bounds are machine-readable ASCII numbers, not typography.
source=source.replace('min="−','min="-')
# A raw ASCII star in an inline HTML superscript can become a Markdown
# emphasis delimiter spanning several formulas. Use the math asterisk glyph.
source=source.replace('<sup>*</sup>','<sup>∗</sup>')

def math_row(value):
 value=re.sub(r'<sub>(.*?)</sub>',r'_{\1}',value)
 value=re.sub(r'<sup>(.*?)</sup>',r'^{\1}',value)
 value=unescape(re.sub(r'<[^>]+>','',value))
 tokens=re.findall(r'[_^]\{[^}]*\}|[_^](?:−?-?\d+|[A-Za-z])|\d+(?:\.\d+)?|cos|sin|tr|diag|[A-Za-z]|\S',value)
 out=[]
 for token in tokens:
  if token[0] in '_^' and out:
   index=token[1:].strip('{}')
   tag='msub' if token[0]=='_' else 'msup'
   out[-1]=f'<{tag}>{out[-1]}{math_row(index)}</{tag}>'
  elif token.replace('.','',1).isdigit(): out.append(f'<mn>{token}</mn>')
  elif token.isalpha():
   normal=' mathvariant="normal"' if token in {'cos','sin','tr','diag'} else ''
   out.append(f'<mi{normal}>{escape(token)}</mi>')
  else: out.append(f'<mo stretchy="false">{escape(token)}</mo>')
 return '<mrow>'+''.join(out)+'</mrow>'

def cell(value):
 match=re.fullmatch(r'([−-]?\d+)/(\d+)',value.strip())
 return f'<mfrac>{math_row(match[1])}{math_row(match[2])}</mfrac>' if match else math_row(value)

def matrix(match):
 rows=[row.split(',') for row in match[1].split(';')]
 assert len({len(row) for row in rows})==1,match[1]
 table=''.join('<mtr>'+''.join('<mtd>'+cell(v.strip())+'</mtd>' for v in row)+'</mtr>' for row in rows)
 return '<math class="matrix-array"><mrow><mo stretchy="true">[</mo><mtable>'+table+'</mtable><mo stretchy="true">]</mo></mrow></math>'

source=re.sub(r'@M\{([^{}]+)\}',matrix,source)
source=re.sub(r'@F\{([^{};]+);([^{}]+)\}',lambda m:'<math class="math-fraction"><mfrac>'+math_row(m[1])+math_row(m[2])+'</mfrac></math>',source)
assert '@M{' not in source and '@F{' not in source
source=source.replace('²','<sup>2</sup>').replace('³','<sup>3</sup>').replace('⁰','<sup>0</sup>')
source=source.replace('⁴','<sup>4</sup>')
source=normalize_scripts(source)
body=MarkdownIt('commonmark',{'html':True}).enable('table').render(source)
assert '<em>' not in body, 'Unexpected Markdown emphasis in mathematical notation.'
def limits(match):
 op,low,high=match.groups()
 tag='munderover' if high else 'munder'
 return f'<math class="math-limits"><{tag}><mo largeop="true">{op}</mo>{math_row(low)}'+(math_row(high) if high else '')+f'</{tag}></math>'
body=re.sub(r'([∑∏∫])<sub>([^<>]+)</sub>(?:<sup>([^<>]+)</sup>)?',limits,body)
parts=re.split(r'(<[^>]+>)',body)
stack=[]
void={'input','br','hr','img','meta','link','wbr'}
for i,part in enumerate(parts):
 if i%2:
  start=re.match(r'<([\w:-]+)\b',part); end=re.match(r'</([\w:-]+)\b',part)
  if start and start[1] not in void: stack.append((start[1],'math-inline' in part or 'formula-block' in part))
  elif end:
   for j in range(len(stack)-1,-1,-1):
    if stack[j][0]==end[1]: del stack[j:]; break
 elif not any(t in {'math','svg','code','pre','script','style','a'} or styled for t,styled in stack):
  part=re.sub(r'[⟨⟩‖⊥ℂ⊗⊙∫∗]',lambda m:f'<span class="math-inline">{m[0]}</span>',part)
  part=re.sub(r'\b(?:[A-Z]{2,6}[a-z]?|mnp|mn)\b',lambda m:m[0] if m[0] in {'MIT','CMU','SVD','IELTS','CSE'} else f'<span class="math-inline">{m[0]}</span>',part)
  parts[i]=part
body=normalize_scripts(normalize_math(''.join(parts)))
anchors=['sources','shapes','matrix-vector','multiplication','composition','transpose','inverse','blocks','trace-norms','computation','laboratory','worked-problems','quick-reference','references']
labels=['Scope and sources','Shapes and entries','Matrix–vector product','Four product views','Composition and proofs','Transpose and Gram','Inverses and powers','Block operations','Trace and norms','Algorithms','Laboratory','36 worked problems','50 examination rules','References']
headings=list(re.finditer(r'<h2>(.*?)</h2>',body))
assert len(headings)==len(anchors)
for match,key in reversed(list(zip(headings,anchors))):
 body=body[:match.start()]+f'<h2 id="{key}">{match[1]}</h2>'+body[match.end():]
nav=' '.join(f'<a href="#{key}">{label}</a>' for key,label in zip(anchors,labels))
html=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Deep matrix algebra from five reviewed university courses: four product views, rigorous proofs, 36 fully worked problems, 50 examination rules, and a composition laboratory.">
<title>Matrices and Matrix Operations · Doctoral CSE 1406</title>
<link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="l_matrices.css">
<script src="l_matrices-lab.js" defer></script></head>
<body><main class="chapter"><div class="top-link"><a href="../index.html#library">← Back to the chapter library</a></div>
<header class="hero"><p class="eyebrow">Linear Algebra · Chapter 2</p><h1>Matrices and Matrix Operations</h1>
<p>Approved chapter · five reviewed university courses · 36 fully worked problems · 50 examination rules</p></header>
<nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article>
<p class="top-link"><a href="../index.html#library">← Back to the chapter library</a></p></main></body></html>'''
(ROOT/'dist/chapters/l_matrices.html').write_text(html,encoding='utf-8')
path=ROOT/'dist/lessons.json'; data=json.loads(path.read_text(encoding='utf-8'))
next(c for w in data for c in w['chapters'] if c['topicId']=='l_matrices').update(url='chapters/l_matrices.html',status='ready')
path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
path=ROOT/'dist/course-audit-week1.en.json'; data=json.loads(path.read_text(encoding='utf-8'))
courses=json.loads((ROOT/'research/l_matrices-reviewed-courses.json').read_text(encoding='utf-8'))
ids={c['id'] for c in courses}
data['courses']=[c for c in data['courses'] if c['id'] not in ids]+courses
data['reviewedAt']='2026-10-02'
path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(f'Rendered {len(source.split())} source tokens; {len(html)} HTML characters; 36 problems; 14 sections.')
