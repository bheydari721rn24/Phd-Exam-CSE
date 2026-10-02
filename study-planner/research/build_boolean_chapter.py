from pathlib import Path
import json,re
from markdown_it import MarkdownIt
from math_typography import normalize_math,normalize_scripts
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[1]
source='\n\n'.join((ROOT/'research'/name).read_text(encoding='utf-8') for name in ('g_boolean.en.md','g_boolean-problems.en.md','g_boolean-review.en.md'))
assert source.count('### Problem ')==40
assert not re.search(r'[\u0600-\u06ff]',source)
class Atoms(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=False);self.stack=[];self.out=[]
 def handle_starttag(self,t,a):
  self.out.append(self.get_starttag_text())
  if t not in {'br','hr','input','img','meta','link','wbr'}:self.stack.append((t,dict(a)))
 def handle_endtag(self,t):
  self.out.append('</'+t+'>')
  for i in range(len(self.stack)-1,-1,-1):
   if self.stack[i][0]==t:del self.stack[i:];break
 def handle_startendtag(self,t,a):self.out.append(self.get_starttag_text())
 def handle_data(self,s):
  excluded=any(t in {'code','pre','math','svg','a','script','style'} or 'math-inline' in (a.get('class') or '') or 'formula-block' in (a.get('class') or '') for t,a in self.stack)
  if not excluded:
   # Boolean literal products and attached primes must not fall back to prose.
   s=re.sub(r"(?<![\w'’])(?:[fghpqrstuvwxyz](?:[₀-₉])?(?:′)?){1,5}(?![\w'’])",lambda m:m[0] if m[0] in {'up','why','try','truth'} else '<span class="math-inline">'+m[0]+'</span>',s)
   s=re.sub(r'(?<![\w])(?:[0-9]+(?:\.[0-9]+)?)(?![\w])',lambda m:'<span class="math-inline">'+m[0]+'</span>',s)
  self.out.append(s)
 def handle_entityref(self,n):self.out.append('&'+n+';')
 def handle_charref(self,n):self.out.append('&#'+n+';')
raw=MarkdownIt('commonmark',{'html':True}).enable('table').render(source)
parser=Atoms();parser.feed(raw);body=normalize_scripts(normalize_math(''.join(parser.out)))
body=re.sub(r'</span>([′·]+)',r'\1</span>',body)
keys=['sources','notation','specification','laws','duality','simplification','xor','selectors','cofactors','sensitivity','verification','laboratory','worked-problems','quick-reference','references']
labels=['Scope and sources','Values and notation','Truth tables','Laws and proofs','Duality and complements','Simplification','XOR and ANF','Row selectors','Shannon decomposition','Sensitivity and quantifiers','Equivalence','Laboratory','40 worked problems','60 examination rules','References']
matches=list(re.finditer(r'<h2>(.*?)</h2>',body));assert len(matches)==len(keys)
for match,key in reversed(list(zip(matches,keys))):body=body[:match.start()]+f'<h2 id="{key}">{match[1]}</h2>'+body[match.end():]
nav=' '.join(f'<a href="#{key}">{label}</a>' for key,label in zip(keys,labels))
html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Boolean Algebra and Truth Tables · Doctoral CSE 1406</title><meta name="description" content="Boolean algebra from definitions to proofs, Shannon decomposition and exact verification: six reviewed university courses, 40 solved problems and 60 examination rules."><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="g_boolean.css"><script src="g_boolean-lab.js" defer></script></head><body><main class="chapter"><p class="top-link"><a href="../index.html#library">← Back to the chapter library</a></p><header class="hero"><p class="eyebrow">Logic Circuits · Chapter 2</p><h1>Boolean Algebra and Truth Tables</h1><p>Approved chapter · four core courses and two university cross-checks · 40 fully worked problems · 60 examination rules</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">← Back to the chapter library</a></p></main></body></html>'''
(ROOT/'dist/chapters/g_boolean.html').write_text(html,encoding='utf-8')
p=ROOT/'dist/lessons.json';data=json.loads(p.read_text(encoding='utf-8'));next(c for w in data for c in w['chapters'] if c['topicId']=='g_boolean').update(title='Boolean algebra and truth tables',url='chapters/g_boolean.html',status='ready');p.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(f'Rendered {len(source.split())} manuscript words and {len(html)} HTML characters; 40 problems.')
