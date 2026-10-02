from pathlib import Path
import json,re
from markdown_it import MarkdownIt
from math_typography import normalize_math,normalize_scripts
ROOT=Path(__file__).resolve().parents[1]
source='\n\n'.join((ROOT/'research'/name).read_text(encoding='utf-8') for name in ('p_flow.en.md','p_flow-problems.en.md','p_flow-review.en.md'))
assert source.count('### Problem ')==36
assert not re.search(r'[\u0600-\u06ff]',source)
body=normalize_scripts(normalize_math(MarkdownIt('commonmark',{'html':True}).enable('table').render(source)))
keys=['sources','state','conditionals','switch','loops','transfers','proofs','termination','laboratory','worked-problems','quick-reference','references']
labels=['Scope and sources','State and statements','Conditionals','Switch','Loop order','Transfers','Proofs','Counts and termination','Laboratory','36 worked problems','60 examination rules','References']
matches=list(re.finditer(r'<h2>(.*?)</h2>',body));assert len(matches)==len(keys),(len(matches),len(keys))
for match,key in reversed(list(zip(matches,keys))):body=body[:match.start()]+f'<h2 id="{key}">{match[1]}</h2>'+body[match.end():]
nav=' '.join(f'<a href="#{key}">{label}</a>' for key,label in zip(keys,labels))
html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Conditionals, Loops, and Execution Order · Doctoral CSE 1406</title><meta name="description" content="Deep C17 control flow: five reviewed university courses, proofs, exact execution traces, 36 solved problems, 60 examination rules and an interactive laboratory."><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="p_flow.css"><script src="p_flow-lab.js" defer></script></head><body><main class="chapter"><p class="top-link"><a href="../index.html#library">← Back to the chapter library</a></p><header class="hero"><p class="eyebrow">Programming Fundamentals · Chapter 2</p><h1>Conditionals, Loops, and Execution Order</h1><p>Approved chapter · five reviewed university courses · 36 fully worked problems · 60 examination rules</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">← Back to the chapter library</a></p></main></body></html>'''
(ROOT/'dist/chapters/p_flow.html').write_text(html,encoding='utf-8')
p=ROOT/'dist/lessons.json';d=json.loads(p.read_text(encoding='utf-8'))
next(c for w in d for c in w['chapters'] if c['topicId']=='p_flow').update(title='Conditionals, loops, execution order',url='chapters/p_flow.html',status='ready')
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(f'Rendered {len(source.split())} manuscript words, {len(html)} HTML characters, 36 problems.')
