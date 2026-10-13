from pathlib import Path
B=Path(__file__).parent;p=B.parent/'dist/chapters/semantic-diagrams.js';s=p.read_text(encoding='utf-8');marker='/* FUNCTIONS QUESTION RENDERER */';end='/* END FUNCTIONS QUESTION RENDERER */'
if marker in s:s=s[:s.index(marker)]+s[s.index(end)+len(end):]
i=s.index('/* RELATIONS QUESTION RENDERER */');s=s[:i]+marker+'\n'+(B/'functions-question-renderer.js').read_text(encoding='utf-8')+'\n'+end+'\n'+s[i:]
needle='if(id.startsWith("relations-question-"))'
if 'id.startsWith("functions-question-")' not in s:assert needle in s;s=s.replace(needle,'if(id.startsWith("functions-question-"))return functionsQuestion(p,g,f);'+needle,1)
s=s.replace('p.canvas.dataset.explicitLabelPlacement=String(p.scene.id.startsWith("relations-question-"));','p.canvas.dataset.explicitLabelPlacement=String(p.scene.id.startsWith("relations-question-")||p.scene.id.startsWith("functions-question-"));')
s=s.replace('labels:!p.scene.id.startsWith("relations-question-")','labels:p.canvas.dataset.explicitLabelPlacement!=="true"')
p.write_text(s,encoding='utf-8')
