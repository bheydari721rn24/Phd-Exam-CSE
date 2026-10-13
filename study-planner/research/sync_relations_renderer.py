from pathlib import Path
B=Path(__file__).parent;p=B.parent/'dist/chapters/semantic-diagrams.js';s=p.read_text();marker='/* RELATIONS QUESTION RENDERER */';end='/* END RELATIONS QUESTION RENDERER */'
if marker in s:s=s[:s.index(marker)]+s[s.index(end)+len(end):]
i=s.index('/* GATES QUESTION RENDERER */');s=s[:i]+marker+'\n'+(B/'relations-question-renderer.js').read_text()+'\n'+end+'\n'+s[i:]
needle='if(id.startsWith("gates-question-"))'
if 'id.startsWith("relations-question-")'not in s:assert needle in s;s=s.replace(needle,'if(id.startsWith("relations-question-"))return relationsQuestion(p,g,f);'+needle,1)
# These matrix axis labels and Hasse coordinates are explicitly placed and checked.
# Generic label relocation would move header indices into matrix cells.
s=s.replace('window.DiagramLayout?.finish(p.canvas);','window.DiagramLayout?.finish(p.canvas,{labels:!p.scene.id.startsWith("relations-question-")});')
needle='window.DiagramLayout?.finish(p.canvas,{labels:!p.scene.id.startsWith("relations-question-")});'
s=s.replace(needle,'p.canvas.dataset.explicitLabelPlacement=String(p.scene.id.startsWith("relations-question-"));'+needle) if 'p.canvas.dataset.explicitLabelPlacement' not in s else s
p.write_text(s,encoding='utf-8')
