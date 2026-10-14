from pathlib import Path
B=Path(__file__).parent;p=B.parent/'dist/chapters/semantic-diagrams.js';s=p.read_text();a='/* DIVIDE QUESTION RENDERER */';z='/* END DIVIDE QUESTION RENDERER */'
if a in s:s=s[:s.index(a)]+s[s.index(z)+len(z):]
i=s.index('function invariantsQuestion');s=s[:i]+a+'\n'+(B/'divide-question-renderer.js').read_text()+'\n'+z+'\n'+s[i:]
needle='if(id.startsWith("invariants-question-"))'
if 'id.startsWith("divide-question-")'not in s:s=s.replace(needle,'if(id.startsWith("divide-question-"))return divideQuestion(p,g,f);'+needle,1)
placement='p.scene.id.startsWith("invariants-question-")'
if 'p.scene.id.startsWith("divide-question-")'not in s:s=s.replace(placement,placement+'||p.scene.id.startsWith("divide-question-")')
p.write_text(s,encoding='utf8')
