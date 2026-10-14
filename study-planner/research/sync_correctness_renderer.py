from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/semantic-diagrams.js';s=p.read_text(encoding='utf8');a='/* CORRECTNESS QUESTION RENDERER */';z='/* END CORRECTNESS QUESTION RENDERER */'
if a in s:s=s[:s.index(a)]+s[s.index(z)+len(z):]
i=s.index('function invariantsQuestion');s=s[:i]+a+'\n'+(R/'research/correctness-question-renderer.js').read_text(encoding='utf8')+'\n'+z+'\n'+s[i:]
needle='if(id.startsWith("invariants-question-"))'
if'id.startsWith("correctness-question-")'not in s:s=s.replace(needle,'if(id.startsWith("correctness-question-"))return correctnessQuestion(p,g,f);'+needle,1)
placement='p.scene.id.startsWith("invariants-question-")'
if'p.scene.id.startsWith("correctness-question-")'not in s:s=s.replace(placement,placement+'||p.scene.id.startsWith("correctness-question-")')
p.write_text(s,encoding='utf8')
