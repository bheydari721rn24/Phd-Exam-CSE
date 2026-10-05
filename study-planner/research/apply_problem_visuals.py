"""Idempotently add reviewed aids to the exact existing solutions."""
from pathlib import Path
import json,re,hashlib
R=Path(__file__).resolve().parents[1];O=R/'research/library-visual-question-review';D=R/'dist/chapters';data=json.loads((O/'problem-models.json').read_text());inputs=json.loads((O/'input.json').read_text())
review=json.loads((O/'concept-review.json').read_text());mapping={q['id']:q for r in review['chapters'] for q in r['questions']};scenes=json.loads((D/'concept-animations.json').read_text())['scenes'];previews=json.loads((O/'scene-previews.json').read_text()) if (O/'scene-previews.json').exists() else {}
for r in inputs:
 topic=r['topicId'];p=D/(topic+'.html');s=p.read_text(encoding='utf-8')
 # Reapply to original problem bodies, keeping current lesson/player fixes intact.
 i=0
 def replace(m):
  global i
  q=r['questions'][i];i+=1;body=q['html'];model=data.get(q['id'])
  if model:
   first=model['frames'][0]
   aid=f'<div class="problem-visual" data-problem-visual="{q["id"]}"><h4>Visual solution aid</h4><p>{model["reading"]}</p><div class="problem-stage">{first["html"]}</div><p class="problem-caption">{first["caption"]}</p><noscript><p>The first diagram and complete written solution are available without scripts.</p></noscript></div>'
   body=body.replace('</details>',aid+'</details>',1)
  ids=mapping[q['id']]['conceptModels']
  if ids:
   scene=scenes[ids[0]];scope='This is a separate teaching example of '+scene['title']+'. Its numeric values are not the data or answer of this question. Use the stated invariant to interpret the written solution.'
   aid=f'<div class="question-concept-aid"><h4>Concept model supporting this solution</h4><p>{scope}</p><div class="concept-animation" data-scenes="{",".join(ids)}">'+previews.get(ids[0],'')+f'<noscript><p>{scene["title"]}. The complete written solution remains available.</p></noscript></div></div>'
   body=body.replace('</details>',aid+'</details>',1)
  return body
 s=re.sub(r'<section class="exam-question"[\s\S]*?</section>',replace,s);assert i==len(r['questions'])
 if 'problem-visuals.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="problem-visuals.css?v=question-visuals-3"></head>')
 if 'problem-visuals.js' not in s:s=s.replace('</body>','<script src="problem-visuals.js?v=question-visuals-3"></script></body>')
 if 'concept-animation.js' not in s:s=s.replace('</body>','<script src="semantic-diagrams.js?v=library-ports-3"></script><script src="concept-animation.js?v=library-ports-3"></script></body>')
 if 'concept-animation.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="concept-animation.css?v=library-ports-3"></head>')
 p.write_text(s,encoding='utf-8')
print('Problem statements, options, source labels and full solutions retained; exact visual aids added.')
