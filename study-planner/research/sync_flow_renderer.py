from pathlib import Path
B=Path(__file__).parent;R=B.parent;p=R/'dist/chapters/semantic-diagrams.js';s=p.read_text();start=s.find('function flowQuestion(')
if start>=0:
 end=s.index('function typesQuestion(',start);s=s[:start]+s[end:]
s=s.replace('function typesQuestion(', (B/'flow-question-renderer.js').read_text()+'\nfunction typesQuestion(',1)
needle='if(id.startsWith("types-question-"))'
if 'id.startsWith("flow-question-")' not in s:
 assert needle in s;s=s.replace(needle,'if(id.startsWith("flow-question-"))return flowQuestion(p,g,f);'+needle)
p.write_text(s,encoding='utf-8')
