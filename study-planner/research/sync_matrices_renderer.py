from pathlib import Path
B=Path(__file__).parent;R=B.parent;p=R/'dist/chapters/semantic-diagrams.js';s=p.read_text();start=s.find('function matricesQuestion(')
if start>=0:
 end=s.index('function vectorNative(',start);s=s[:start]+s[end:]
s=s.replace('function vectorNative(', (B/'matrices-question-renderer.js').read_text()+'\nfunction vectorNative(',1)
needle='if(id.startsWith("vectors-question-"))'
if 'id.startsWith("matrices-question-")' not in s:
 assert needle in s;s=s.replace(needle,'if(id.startsWith("matrices-question-"))return matricesQuestion(p,g,f);'+needle)
p.write_text(s)
