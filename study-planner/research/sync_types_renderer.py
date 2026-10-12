from pathlib import Path
B=Path(__file__).parent;R=B.parent;p=R/'dist/chapters/semantic-diagrams.js';s=p.read_text();start=s.find('function typesQuestion(')
if start>=0:
 end=s.index('function matricesQuestion(',start);s=s[:start]+s[end:]
s=s.replace('function matricesQuestion(', (B/'types-question-renderer.js').read_text()+'\nfunction matricesQuestion(',1)
needle='if(id.startsWith("matrices-question-"))'
if 'id.startsWith("types-question-")' not in s:
 assert needle in s;s=s.replace(needle,'if(id.startsWith("types-question-"))return typesQuestion(p,g,f);'+needle)
p.write_text(s,encoding='utf-8')
