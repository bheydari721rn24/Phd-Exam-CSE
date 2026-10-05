"""Freeze the review input and inventory every problem and model."""
from pathlib import Path
import json,re,shutil,html,hashlib
def plain(s): return html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]*>',' ',s))).strip()
R=Path(__file__).resolve().parents[1]; O=R/'research/library-visual-question-review'; O.mkdir(exist_ok=True)
B=O/'baseline'; B.mkdir(exist_ok=True)
chapters=json.loads((R/'research/animation-manifest.json').read_text())['chapters']; rows=[]
for c in chapters:
 p=R/f'dist/chapters/{c["topicId"]}.html'
 dest=B/p.name
 if not dest.exists(): shutil.copy2(p,dest)
 qs=[]
 for i,q in enumerate(re.findall(r'<section class="exam-question"[\s\S]*?</section>',dest.read_text(encoding='utf-8')),1):
  sol=re.search(r'<details class="exam-solution"[\s\S]*?</details>',q); heading=re.search(r'<h3>([\s\S]*?)</h3>',q); formulas=[html.unescape(m) for m in re.findall(r'<math\b[^>]*aria-label="([^"]*)"',q)]
  qs.append(dict(id=f'{c["topicId"]}-q{i}',number=i,title=plain(heading[1]),text=plain(q),solution=plain(sol[0]) if sol else '',formulas=formulas,html=q,existingFigures=len(re.findall(r'<figure\b|<svg\b',q)),existingAnimations=len(re.findall(r'class="concept-animation"|data-arrays-model',q))))
 assert len(qs)==c['questionCount'],(c['topicId'],len(qs),c['questionCount'])
 rows.append(dict(topicId=c['topicId'],questionCount=len(qs),questions=qs,htmlSha256=hashlib.sha256(dest.read_bytes()).hexdigest()))
(O/'input.json').write_text(json.dumps(rows,ensure_ascii=True,indent=2)+'\n',encoding='utf-8')
(O/'question-outline.txt').write_text('\n'.join('\n'+r['topicId']+'\n'+'\n'.join(f'{q["number"]}: {q["title"]} | {q["text"][len(q["title"]):][:180]}'.rstrip() for q in r['questions']) for r in rows),encoding='utf-8')
for name in ['semantic-diagrams.js','concept-animation.js','concept-animation.css']:
 if not (B/name).exists():shutil.copy2(R/'dist/chapters'/name,B/name)
p=R/'research/chapter-gate.json'; g=json.loads(p.read_text()); g.update(state='in_progress',reviewScope='All 35 existing chapters: all animated models and all 2085 worked problems.',activeWork='User-authorized whole-library arrow/padding redesign and problem-specific visual instruction; no new chapter.',nextReview='Complete this whole-library revision and deliver for explicit approval.',libraryRewriteRequiresApproval=True,libraryVisualQuestionReviewPath='research/library-visual-question-review/manifest.json');p.write_text(json.dumps(g,indent=2)+'\n')
p=R/'WEEKLY_DELIVERY.md'; s=p.read_text(encoding='utf-8'); s+='\n\n## Whole-library animation and worked-problem visual revision\n\n5 October 2026: The user approved the arrays arrow/spacing repair and explicitly requested the same visual review across every chapter, plus individual review of every problem for necessary diagrams, circuit schematics and animations alongside its solution. Work is authorized for all 35 existing chapters and 2085 problems. The previous one-chapter limitation is superseded for this revision only. No new chapter starts. Preserve problem statements, source provenance, mathematical solutions and study progress, except documented corrections. Visual additions require review before promotion.\n';p.write_text(s,encoding='utf-8')
print(dict(chapters=len(rows),questions=sum(r['questionCount'] for r in rows)))
