from pathlib import Path
B=Path(__file__).parent;p=B.parent/'dist/chapters/semantic-diagrams.js';s=p.read_text(encoding='utf-8');marker='/* BOOLEAN QUESTION RENDERER */';end='/* END BOOLEAN QUESTION RENDERER */'
if marker in s:s=s[:s.index(marker)]+s[s.index(end)+len(end):]
i=s.index('/* NUMBER QUESTION RENDERER */');s=s[:i]+marker+'\n'+(B/'boolean-question-renderer.js').read_text()+'\n'+end+'\n'+s[i:]
needle='if(id.startsWith("number-question-"))'
if 'id.startsWith("boolean-question-")'not in s:assert needle in s;s=s.replace(needle,'if(id.startsWith("boolean-question-"))return booleanQuestion(p,g,f);'+needle,1)
p.write_text(s,encoding='utf-8')
