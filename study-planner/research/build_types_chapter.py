"""Render an original, audited scalar-expression lesson with separate math/code typography."""
from pathlib import Path
import json, re
from markdown_it import MarkdownIt
from math_typography import normalize_math, normalize_scripts
ROOT=Path(__file__).resolve().parents[1]
source='\n\n'.join((ROOT/'research'/name).read_text(encoding='utf-8') for name in
 ('p_types.en.md','p_types-problems.en.md','p_types-review.en.md'))
assert source.count('### Problem ')==36
assert not re.search(r'[\u0600-\u06ff]',source)
body=MarkdownIt('commonmark',{'html':True}).enable('table').render(source)
body=normalize_scripts(normalize_math(body))
body=body.replace('>C Variables</a>','><span class="math-inline">C</span> Variables</a>')
body=body.replace('>C Syntax</a>','><span class="math-inline">C</span> Syntax</a>')
anchors=['sources','values','types','conversions','operators','sequencing','safety','floating','laboratory','worked-problems','quick-reference','references']
labels=['Scope and sources','Values and assignment','Types and literals','Conversion pipeline','Operators and parsing','Sequencing','Integer safety','Floating and languages','Laboratory','36 worked problems','50 examination rules','References']
headings=list(re.finditer(r'<h2>(.*?)</h2>',body)); assert len(headings)==len(anchors)
for match,key in reversed(list(zip(headings,anchors))):
 body=body[:match.start()]+f'<h2 id="{key}">{match[1]}</h2>'+body[match.end():]
nav=' '.join(f'<a href="#{key}">{label}</a>' for key,label in zip(anchors,labels))
html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Deep C17 scalar types, conversions and expressions: five reviewed university courses, rigorous boundaries, 36 worked problems, 50 examination rules, and a typed conversion laboratory.">
<title>Data Types, Conversions, and Operators · Doctoral CSE 1406</title>
<link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="p_types.css"><script src="p_types-lab.js" defer></script></head>
<body><main class="chapter"><div class="top-link"><a href="../index.html#library">← Back to the chapter library</a></div>
<header class="hero"><p class="eyebrow">Programming Fundamentals · Chapter 1</p><h1>Data Types, Conversions, and Operators</h1><p>Approved chapter · five reviewed university courses · 36 fully worked problems · 50 examination rules</p></header>
<nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">← Back to the chapter library</a></p></main></body></html>'''
(ROOT/'dist/chapters/p_types.html').write_text(html,encoding='utf-8')
path=ROOT/'dist/lessons.json'; data=json.loads(path.read_text(encoding='utf-8'))
next(c for w in data for c in w['chapters'] if c['topicId']=='p_types').update(title='Data types, conversions, and operators',url='chapters/p_types.html',status='ready')
path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
path=ROOT/'dist/course-audit-week1.en.json'; data=json.loads(path.read_text(encoding='utf-8'))
courses=json.loads((ROOT/'research/p_types-reviewed-courses.json').read_text(encoding='utf-8'))
ids={c['id'] for c in courses}; data['courses']=[c for c in data['courses'] if c['id'] not in ids]+courses
data['reviewedAt']='2026-10-02'; path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(f'Rendered {len(source.split())} source words; {len(html)} HTML characters; 36 problems; 12 sections.')
