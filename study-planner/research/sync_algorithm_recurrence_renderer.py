from pathlib import Path
B=Path(__file__).parent;p=B.parent/'dist/chapters/semantic-diagrams.js';s=p.read_text();a='/* ALGORITHM RECURRENCE QUESTION RENDERER */';z='/* END ALGORITHM RECURRENCE QUESTION RENDERER */'
if a in s:s=s[:s.index(a)]+s[s.index(z)+len(z):]
i=s.index('function invariantsQuestion');s=s[:i]+a+'\n'+(B/'algorithm-recurrence-question-renderer.js').read_text()+'\n'+z+'\n'+s[i:]
needle='if(id.startsWith("invariants-question-"))';assert needle in s
if 'id.startsWith("algorithm-recurrence-question-")'not in s:s=s.replace(needle,'if(id.startsWith("algorithm-recurrence-question-"))return algorithmRecurrenceQuestion(p,g,f);'+needle,1)
placement='p.scene.id.startsWith("invariants-question-")'
if placement+'||p.scene.id.startsWith("algorithm-recurrence-question-")'not in s:s=s.replace(placement,placement+'||p.scene.id.startsWith("algorithm-recurrence-question-")')
p.write_text(s,encoding='utf8')
