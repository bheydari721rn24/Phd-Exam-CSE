from pathlib import Path
B=Path(__file__).parent;p=B.parent/'dist/chapters/semantic-diagrams.js';s=p.read_text();marker='/* GATES QUESTION RENDERER */';end='/* END GATES QUESTION RENDERER */'
if marker in s:s=s[:s.index(marker)]+s[s.index(end)+len(end):]
i=s.index('/* BOOLEAN QUESTION RENDERER */');s=s[:i]+marker+'\n'+(B/'gates-question-renderer.js').read_text()+'\n'+end+'\n'+s[i:]
needle='if(id.startsWith("boolean-question-"))'
if 'id.startsWith("gates-question-")'not in s:assert needle in s;s=s.replace(needle,'if(id.startsWith("gates-question-"))return gatesQuestion(p,g,f);'+needle,1)
p.write_text(s,encoding='utf-8')
