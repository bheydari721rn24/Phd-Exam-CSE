"""Record observed visual repair without replacing scientific audit evidence."""
from pathlib import Path
import json, hashlib, shutil, subprocess
B=Path(__file__).resolve().parent; R=B.parent
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def write(p,v): p.write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
v=read(B/'a_arrays-visual-browser-audit.json')
assert v['state']=='passed'
old=json.loads(subprocess.check_output(['git','show','3392f1192fbf95093e4c43b676ac328e1fc5faad:dist/chapters/a_arrays-models.json'],cwd=R))
new=read(R/'dist/chapters/a_arrays-models.json')
assert [[f['state'] for f in m['frames']] for m in old['models']]==[[f['state'] for f in m['frames']] for m in new['models']]
p=B/'a_arrays-quality-audit.md'; s=p.read_text(encoding='utf-8'); marker='## Arrow and label repair'
if marker not in s:
 s+='\n'+marker+'\n\nThe user reported disconnected arrows and crowded labels. Exact boundary ports, smaller fixed-size arrowheads, separate forward/backward lanes, rounded return paths, padded cursor pills and moving endpoint rebinding replace the previous geometry. All 113 checkpoint states are unchanged. Actual browser geometry checks passed all 20 models, 113 checkpoints and 497 editable-laboratory frames, with zero measured padding/connection issues. Four during-motion samples found no detached edges. All 466 numerical laboratory references still agree. Splice, reversal, Floyd and matrix screenshots were visually inspected.\n\n[Visual repair browser evidence](../evidence/a_arrays/visual-browser.json) records the finite checks; these are not a universal claim about every future frame or input.\n'
 p.write_text(s,encoding='utf-8')
p=B/'a_arrays-model-audit.json'; a=read(p); a.update(visualRepairEvidence='research/a_arrays-visual-browser-audit.json',visualRepairPath='research/a_arrays-visual-repair.md',visualRepairState='awaiting_user_approval'); write(p,a)
out=R/'dist/evidence/a_arrays'; shutil.copy2(B/'a_arrays-visual-browser-audit.json',out/'visual-browser.json'); shutil.copy2(B/'a_arrays-model-audit.json',out/'models.json')
p=B/'chapter-gate.json'; g=read(p); assert g['currentTopicId']=='a_arrays'; assert g['state']=='awaiting_user_approval'
g['lastCompletedReview']='a_arrays visual repair: 113 checkpoint states preserved; 497 laboratory frames and four moving-edge samples passed; 466 numerical references retained.'
for name in ['research/a_arrays-visual-browser-audit.json','research/a_arrays-visual-repair.md']:
 if name not in g['reviewEvidence']: g['reviewEvidence'].append(name)
write(p,g)
p=R/'WEEKLY_DELIVERY.md'; s=p.read_text(encoding='utf-8'); marker='## Arrays chapter: corrected arrow connections and text spacing'
if marker not in s:
 s+='\n\n'+marker+'\n\n5 October 2026: The student rejected arrays/list arrow geometry and label spacing. Only this chapter was repaired. Explicit boundary ports, fixed-size arrowheads, separate return lanes, padded labels and animated endpoint rebinding passed all 113 fixed checkpoints, 497 laboratory frames and four moving-edge samples. All 466 numerical references, 86 problems and 80 rules are retained. Evidence: research/a_arrays-visual-repair.md and research/a_arrays-visual-browser-audit.json. The approval gate remains awaiting_user_approval; no subsequent chapter has started. Publication must be verified independently.\n'
 p.write_text(s,encoding='utf-8')
subprocess.run(['python','-X','utf8',str(B/'render_a_arrays.py')],cwd=R,check=True)
p=B/'animation-manifest.json'; a=read(p)
for c in a['chapters']:
 if c['topicId']=='a_arrays': c.update(htmlSha256=hashlib.sha256((R/'dist/chapters/a_arrays.html').read_bytes()).hexdigest(),visualRepairEvidence='research/a_arrays-visual-browser-audit.json',visualRevisionState='awaiting_user_approval')
write(p,a)
print('Recorded visual repair; checkpoint states unchanged; approval gate retained.')
