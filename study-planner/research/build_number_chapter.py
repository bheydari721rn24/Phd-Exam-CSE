from pathlib import Path
import json,re
from markdown_it import MarkdownIt
from math_typography import normalize_math,normalize_scripts
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[1]
source='\n\n'.join((ROOT/'research'/name).read_text(encoding='utf-8') for name in ('g_number.en.md','g_number-problems.en.md','g_number-review.en.md'))
assert source.count('### Problem ')==36
assert not re.search(r'[\u0600-\u06ff]',source)
body=normalize_scripts(normalize_math(MarkdownIt('commonmark',{'html':True}).enable('table').render(source)))
class NumberFaces(HTMLParser):
    """Numeric atoms in prose use the mathematics face; code/markup stay intact."""
    def __init__(self):super().__init__(convert_charrefs=False);self.out=[];self.stack=[]
    def handle_starttag(self,tag,attrs):
        self.out.append(self.get_starttag_text())
        if tag not in {'br','hr','input','img','meta','link','wbr'}:self.stack.append((tag,dict(attrs)))
    def handle_endtag(self,tag):
        self.out.append('</'+tag+'>')
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i][0]==tag:del self.stack[i:];break
    def handle_startendtag(self,tag,attrs):self.out.append(self.get_starttag_text())
    def handle_data(self,data):
        excluded=any(t in {'code','pre','math','svg','a','script','style','sub','sup'} or 'math-inline' in (a.get('class') or '') or 'formula-block' in (a.get('class') or '') for t,a in self.stack)
        if not excluded:data=re.sub(r'(?<![\w])(?:[0-9]+(?:\.[0-9]+)?)(?![\w])',lambda m:'<span class="math-inline">'+m[0]+'</span>',data)
        self.out.append(data)
    def handle_entityref(self,name):self.out.append('&'+name+';')
    def handle_charref(self,name):self.out.append('&#'+name+';')
numeric=NumberFaces();numeric.feed(body);body=''.join(numeric.out)
keys=['sources','notation','conversion','fractions','signed','arithmetic','widths','fixed-point','decimal','gray','errors','laboratory','worked-problems','quick-reference','references']
labels=['Scope and sources','Positional notation','Integer conversion','Fractions','Signed encodings','Arithmetic and flags','Widths and shifts','Fixed point','Decimal codes','Gray code','Error control','Laboratory','36 worked problems','60 examination rules','References']
matches=list(re.finditer(r'<h2>(.*?)</h2>',body));assert len(matches)==len(keys)
for match,key in reversed(list(zip(matches,keys))):body=body[:match.start()]+f'<h2 id="{key}">{match[1]}</h2>'+body[match.end():]
nav=' '.join(f'<a href="#{key}">{label}</a>' for key,label in zip(keys,labels))
html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Number Bases and Binary Encoding · Doctoral CSE 1406</title><meta name="description" content="Number representation from first principles: six reviewed university courses, complete proofs, 36 worked problems, 60 examination rules and an interactive word laboratory."><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="g_number.css"><script src="g_number-lab.js" defer></script></head><body><main class="chapter"><p class="top-link"><a href="../index.html#library">← Back to the chapter library</a></p><header class="hero"><p class="eyebrow">Logic Circuits · Chapter 1</p><h1>Number Bases and Binary Encoding</h1><p>Review draft · six reviewed university courses · 36 fully worked problems · 60 examination rules</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">← Back to the chapter library</a></p></main></body></html>'''
(ROOT/'dist/chapters/g_number.html').write_text(html,encoding='utf-8')
p=ROOT/'dist/lessons.json';data=json.loads(p.read_text(encoding='utf-8'))
next(c for w in data for c in w['chapters'] if c['topicId']=='g_number').update(title='Number bases and binary encoding',url='chapters/g_number.html',status='draft')
p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(f'Rendered {len(source.split())} manuscript words, {len(html)} HTML characters, 36 problems.')
