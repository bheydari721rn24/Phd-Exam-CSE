from pathlib import Path
B=Path(__file__).parent;p=B.parent/'dist/chapters/semantic-diagrams.js';s=p.read_text();marker='/* DISCRETE NUMBER QUESTION RENDERER */';end='/* END DISCRETE NUMBER QUESTION RENDERER */'
if marker in s:s=s[:s.index(marker)]+s[s.index(end)+len(end):]
i=s.index('function invariantsQuestion');s=s[:i]+marker+'\n'+(B/'discrete-number-question-renderer.js').read_text()+'\n'+end+'\n'+s[i:]
needle='if(id.startsWith("invariants-question-"))';assert needle in s
if 'id.startsWith("discrete-number-question-")'not in s:s=s.replace(needle,'if(id.startsWith("discrete-number-question-"))return discreteNumberQuestion(p,g,f);'+needle,1)
placement='p.scene.id.startsWith("invariants-question-")'
if placement+'||p.scene.id.startsWith("discrete-number-question-")'not in s:s=s.replace(placement,placement+'||p.scene.id.startsWith("discrete-number-question-")')
p.write_text(s,encoding='utf-8')
