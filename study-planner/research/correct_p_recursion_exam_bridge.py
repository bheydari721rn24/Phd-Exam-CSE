"""Correct only the source-checked Q167 adaptation; preserve other chapter content."""
from pathlib import Path
from html import escape
import json,re,hashlib
B=Path(__file__).resolve().parent;R=B.parent;E=B/'p_recursion-evidence'
q=json.loads((B/'p_recursion-authentic.json').read_text())[0]
solution=r'''1. After $t$ copies, the source index is $N-1-2t$ and the destination index is $t$. The recursive edge must therefore decrease `n` by two and increase `i` by one.
2. Option 1 starts at b[0], preserves those indices, and stops before a negative source index is read. It copies the ceiling of N/2 elements.
3. All printed alternatives have the guard n<0. Option 2 starts writing at b[1]. Option 3 advances the destination by two and skips slots. Option 4 both starts at b[1] and uses a source stride of one, so it fails the requested selection.
4. The source is integer pseudocode, not a strictly declared C17 interface. A real C implementation must use compatible signed bounds or a prechecked remaining-length representation.

**Source correction.** Options were visually rechecked against MSc CS 1393, Q167, PDF page 34 on 9 October 2026. The independently derived answer remains option 1. This is a bridge revisit, not a new unique archive question.'''
q['solution']=solution+r'\n\n**Exact count and visual scope.** The number of copied elements is $\lceil N/2\rceil$ and the number of invocations is $\lceil N/2\rceil+1$, including the negative-index base. The animation specializes this contract to $N=7$, selecting source indices 6, 4, 2, and 0.'.replace(r'\n','\n')
(B/'p_recursion-authentic.json').write_text(json.dumps([q],indent=2)+'\n',encoding='utf-8')
import render_p_recursion as render
options='<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+render.text(s)+'</div></div>'for i,s in enumerate(q['options'],1))+'</div>'
records=[]
oldrecords={r['path']:r for r in json.loads((E/'source-corrections.json').read_text())['records']}if(E/'source-corrections.json').exists()else{}
baseline={'dist/'+c['url']:c['sha256']for c in json.loads((E/'prior-library.json').read_text())['chapters']}
for p in (R/'dist/chapters').glob('*.html'):
 if p.stem=='p_recursion':continue
 before=p.read_text(encoding='utf-8');needle='data-source-id="MS_CS_1393_Q167"'
 if needle not in before:continue
 start=before.rfind('<section',0,before.index(needle));end=before.find('data-source-id=',before.index(needle)+len(needle));end=before.rfind('<section',start,end)if end>=0 else len(before)
 chunk=before[start:end];a=chunk.index('<div class="exam-options">');b=chunk.index('<details class="exam-solution">',a);chunk=chunk[:a]+options+chunk[b:]
 a=chunk.index('</summary>')+len('</summary>');stop=chunk.find('<div class="question-concept-aid">',a)
 if stop<0:stop=chunk.find('</details>',a)
 assert stop>a
 chunk=chunk[:a]+'<p><strong>Correct option: 1.</strong></p>'+render.text(solution)+chunk[stop:]
 after=before[:start]+chunk+before[end:];assert after.count('data-source-id=')==before.count('data-source-id=');p.write_text(after,encoding='utf-8')
 relative=p.relative_to(R).as_posix();records.append(dict(path=relative,beforeSha256=baseline[relative],afterSha256=hashlib.sha256(p.read_bytes()).hexdigest(),scope='Only Q167 option text and explanatory answer; content outside its question block retained.'))
def revise(obj):
 if isinstance(obj,dict):
  if obj.get('id')=='MS_CS_1393_Q167'and 'options'in obj:obj.update(options=q['options'],solution=solution,verification=q['verification'])
  for v in obj.values():revise(v)
 elif isinstance(obj,list):
  for v in obj:revise(v)
for name in ['p_arrays-authentic.json','p_functions-authentic.json','a_arrays-authentic.json','exam-calibration/actual-items.json']:
 p=B/name;obj=json.loads(p.read_text(encoding='utf-8'));revise(obj);p.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
(E/'source-corrections.json').write_text(json.dumps(dict(status='corrected',questionId=q['id'],originalPage=34,records=records),indent=2)+'\n',encoding='utf-8')
print('Corrected only the checked Q167 adaptation in',len(records),'existing pages; question counts unchanged.')
