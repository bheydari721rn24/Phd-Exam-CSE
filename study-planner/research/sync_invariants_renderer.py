from pathlib import Path
import re
B=Path(__file__).parent;p=B.parent/'dist/chapters/semantic-diagrams.js';s=p.read_text(encoding='utf-8')
renderer=(B/'invariants-question-renderer.js').read_text(encoding='utf-8')
if '/* INVARIANTS QUESTION RENDERER START */' in s:s=re.sub(r'/\* INVARIANTS QUESTION RENDERER START \*/[\s\S]*?/\* INVARIANTS QUESTION RENDERER END \*/','/* INVARIANTS QUESTION RENDERER START */\n'+renderer+'\n/* INVARIANTS QUESTION RENDERER END */',s,count=1)
else:s=s.replace('function functionsQuestion(', '/* INVARIANTS QUESTION RENDERER START */\n'+renderer+'\n/* INVARIANTS QUESTION RENDERER END */\nfunction functionsQuestion(',1)
if 'return invariantsQuestion(p,g,f)'not in s:s=s.replace('if(id.startsWith("functions-question-"))return functionsQuestion(p,g,f);','if(id.startsWith("invariants-question-"))return invariantsQuestion(p,g,f);if(id.startsWith("functions-question-"))return functionsQuestion(p,g,f);',1)
s=s.replace('String(p.scene.id.startsWith("relations-question-")||p.scene.id.startsWith("functions-question-"))','String(p.scene.id.startsWith("relations-question-")||p.scene.id.startsWith("functions-question-")||p.scene.id.startsWith("invariants-question-"))')
p.write_text(s,encoding='utf-8')
