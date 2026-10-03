"""Preserve the published baseline and record the user's whole-library rejection."""
import hashlib,json,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];base=ROOT/'research/exam-rewrite'
base.mkdir(exist_ok=True);original=base/'baseline';original.mkdir(exist_ok=True)
rows=json.loads((ROOT/'dist/lessons.json').read_text())
chapters=[]
for week in rows:
 for c in week['chapters']:
  topic=c['topicId'];src=ROOT/c['url'].replace('chapters/','dist/chapters/')
  dst=original/(topic+'.html')
  if not dst.exists():shutil.copy2(src,dst)
  chapters.append({'topicId':topic,'week':week['week'],'previousStatus':c['status'],'baselineSha256':hashlib.sha256(dst.read_bytes()).hexdigest(),'state':'pending','questionCount':0,'notesCount':0})
manifest={'started':'2026-10-02','state':'in_progress','scope':'All 22 existing CSE chapters; revise teaching, replace problem banks and examination notes, retain and check deep derivations and useful diagrams. No new topic during this revision.','examArchivePolicy':'Deferred until final month unless the student explicitly changes this instruction.','approvalPolicy':'Existing chapters are revised under the explicit whole-library instruction. Revisions remain drafts until explicit approval; new chapters remain paused.','chapters':chapters}
(base/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
gatep=ROOT/'research/chapter-gate.json';gate=json.loads(gatep.read_text())
gate.update(state='in_progress',activeWork='Whole-library exam-focused rewrite explicitly requested after rejection of all problem banks and review sections.',proposedNextTopicId=None,nextTopicId=None)
gate['libraryRewritePath']='research/exam-rewrite/manifest.json';gate['libraryRewriteRequiresApproval']=True
gatep.write_text(json.dumps(gate,indent=2)+'\n')
print('Preserved 22 chapter baselines; global exam-focused revision is active.')
