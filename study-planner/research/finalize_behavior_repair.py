"""Retain scientific records, publish reproducible evidence, and stage only scoped edits."""
from pathlib import Path
import hashlib,html,json,re,shutil,subprocess,sys,tarfile
R=Path(__file__).resolve().parents[1];E=R/'research/player-behavior-repair';BASE='28fa8a031c78dc1895eb232f5f656d166854b7be'
def git(*args):return subprocess.check_output(['git',*args],cwd=R,text=True,encoding='utf-8').strip()
def old(p):return subprocess.check_output(['git','show',BASE+':'+p],cwd=R)
def norm(b):return b.replace(b'\r\n',b'\n')
mode=sys.argv[1] if len(sys.argv)>1 else 'prepare'
if mode=='prepare':
 reports={n:json.loads((E/n).read_text()) for n in ['browser.json','buttons.json','record-routes.json']}
 assert all(r['status']=='passed' for r in reports.values()),{k:r['status'] for k,r in reports.items()}
 b=reports['browser.json'];assert len(b['chapters'])==47 and len(b['uniqueModels'])==1040
 retention={'baseline':BASE,'status':'passed','writtenChapters':{},'scientificRecords':{}}
 for p in (R/'dist/chapters').glob('*.html'):
  before=old(p.relative_to(R).as_posix()).decode('utf-8');after=p.read_text(encoding='utf-8')
  def body(s):return re.sub(r'<script\b[^>]*>.*?</script>','',re.search(r'<body>(.*?)</body>',s,re.S).group(1),flags=re.S)
  assert body(before)==body(after),p;retention['writtenChapters'][p.stem]={'unchanged':True,'bodySha256':hashlib.sha256(body(after).encode()).hexdigest()}
 for p in (R/'dist/chapters').glob('*.json'):
  assert norm(p.read_bytes())==norm(old(p.relative_to(R).as_posix())),p
  retention['scientificRecords'][p.name]={'unchanged':True,'normalizedSha256':hashlib.sha256(norm(p.read_bytes())).hexdigest()}
 for n in ['advanced-simulations.js','concept-unified.js','problem-visuals.js','semantic-diagrams.js']:subprocess.run(['node','--check',str(R/'dist/chapters'/n)],check=True)
 (E/'retention.json').write_text(json.dumps(retention,indent=2)+'\n')
 manifest={'status':'verified_locally','baseline':BASE,'chapters':47,'models':len(b['uniqueModels']),'checkpoints':sum(m['frames'] for m in b['uniqueModels']),'liveButtonChapters':len(reports['buttons.json']['chapters']),'movingRecordTransitions':sum(len(m['routedSteps']) for m in reports['record-routes.json']['models']),'sampledProgress':[0,.125,.25,.375,.5,.625,.75,.875,1],'limitations':'Finite checks of saved and default-computed traces. Moving-body checks cover sorting and selection models. Other chapters have exact-state/layout checks and representative live button checks. This is not a proof for every possible custom input.'}
 (E/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 public=R/'dist/evidence/player-behavior-repair';public.mkdir(exist_ok=True)
 for n in ['manifest.json','browser.json','buttons.json','record-routes.json','retention.json']:shutil.copy2(E/n,public/n)
 screen=E/'screenshots';screen.mkdir(exist_ok=True)
 for name in ['player-behavior-library-qa','player-behavior-buttons','record-route-qa']:
  for p in (Path('C:/Users/bheydari/AppData/Local/Temp')/name).glob('*.png'):shutil.copy2(p,screen/(name+'-'+p.name))
 page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Simulation behavior corrections</title><link rel="stylesheet" href="../chapters/chapter.en.css"><style>a,summary{text-decoration:none!important}li{margin:12px 0;line-height:1.7}</style></head><body><main class="chapter"><p><a href="../index.html#library">Chapter library</a></p><article class="lesson"><h1>Simulation behavior corrections</h1><p>The previous layout audit did not sufficiently verify actual button behavior or intermediate record movement. This revision corrects specific reproducible failures.</p><h2>Corrected behavior</h2><ul><li>Next offers a working Pause button while one operation is moving. Play resumes the frozen movement, including a paused final checkpoint or a scrubbed transition.</li><li>Previous replays from the actual current checkpoint to its predecessor.</li><li>Before uses the preceding checkpoint's diagram, caption, formula, quantities and full state together.</li><li>Every inserted drawing has independent marker and clip identifiers, including comparison and print copies.</li><li>Sorting and selection records lift, travel through separated lanes and settle. Slot indices stay with slots. An empty-slot marker appears after its moving record has vacated it.</li><li>Camera and group-layout changes are atomic visual reorganizations. They are not invented physical record trajectories. Before and Result provide the two exact states.</li><li>Recursive interval boundary marks use the same spacing as their array cells.</li><li>String-memory headings have separate space from read/write markers. The last font-fitting pass cannot enlarge a label after its padding has been measured.</li><li>Figures remain inside the lesson column and have bounded height. Comparison figures retain readable internal width and pan locally.</li><li>Concurrent requests for a lazy simulation share one initialization promise. The speed selector changes movement speed as well as the interval between checkpoints.</li></ul><h2>Use the controls</h2><p>Use Next for one operation. Pause freezes its movement. Use the Transition slider to inspect its progress and Play to resume. Before shows the previous exact state; Result shows the selected exact state. Compare provides both states. During motion, quantities describe the target checkpoint, rather than an intermediate arithmetic state.</p><h2>Verification and limits</h2>'''
 page+=f'<p>All {manifest["chapters"]} written chapters, {manifest["models"]:,} distinct models and {manifest["checkpoints"]:,} checkpoints were checked. Visible controls were tested in {manifest["liveButtonChapters"]} representative chapters. {manifest["movingRecordTransitions"]} sorting/selection transitions were inspected at nine progress positions for overlapping record bodies and movement outside the drawing.</p><p>'+html.escape(manifest['limitations'])+'</p>'
 page+='<p><a href="../evidence/player-behavior-repair/browser.json">Exact-state and layout checks</a> · <a href="../evidence/player-behavior-repair/buttons.json">Visible-button checks</a> · <a href="../evidence/player-behavior-repair/record-routes.json">Intermediate movement checks</a> · <a href="../evidence/player-behavior-repair/retention.json">Scientific-record retention</a></p><p><a href="../chapters/a_sort.html">Sorting examples</a> · <a href="../chapters/p_recursion.html">Recursion examples</a> · <a href="../chapters/p_strings.html">String-memory examples</a></p></article></main></body></html>'
 (R/'dist/reviews/simulation-behavior-corrections.html').write_text(page,encoding='utf-8')
 p=R/'dist/library-review.html';s=p.read_text(encoding='utf-8');s=s.replace('<h2>Approval and remaining limits</h2>','<h2>Simulation behavior corrections</h2><p><a href="reviews/simulation-behavior-corrections.html">Read the specific corrections and actual interaction checks.</a></p><h2>Approval and remaining limits</h2>');p.write_text(s,encoding='utf-8')
 text='# Simulation behavior corrections\n\n'+json.dumps(manifest,indent=2)+'\n\nThe earlier static/control-endpoint review missed actual Pause behavior, Before readout mismatch, reverse replay origin, record transit collisions, changing-camera clipping and boundary/cell spacing mismatch. The new audit checks these failures explicitly. Scientific JSON and written bodies are unchanged. Publication is recorded separately.\n'
 (E/'DELIVERY.en.md').write_text(text,encoding='utf-8')
 with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\n## Simulation behavior correction — 9 October 2026\n\n'+text.split('\n\n',1)[1])
 with(R/'research/ANIMATION_STANDARD.md').open('a',encoding='utf-8')as f:f.write('\n## Actual control and transit verification\n\nCheck Pause through the visible button during manual movement; reverse replay must start at the current checkpoint. All Before readouts must describe the shown state. Give each inserted SVG copy unique IDs. Do not interpolate across camera/layout reorganization. Sample intermediate record movement, not only exact endpoints. Keep indices attached to slots, reveal holes after vacating, use separate transit lanes, and keep interval markers on the same spacing as their cells. Measure labels in their real style context.\n')
 p=R/'research/chapter-gate.json';g=json.loads(p.read_text());assert g['state']=='awaiting_user_approval';g.update(activeWork='Actual control and intermediate-movement failures corrected; all-library verification passed. Publication pending. No next chapter begun.',simulationBehaviorRevisionPath='research/player-behavior-repair/manifest.json');p.write_text(json.dumps(g,indent=2)+'\n')
 print(json.dumps(manifest))
elif mode=='commit':
 assert not git('diff','--cached','--name-only')
 allowed={'dist/chapters/advanced-simulations.js','dist/chapters/advanced-simulations.css','dist/chapters/concept-unified.js','dist/chapters/problem-visuals.js','dist/chapters/semantic-diagrams.js','dist/library-review.html','dist/reviews/simulation-behavior-corrections.html','WEEKLY_DELIVERY.md','research/ANIMATION_STANDARD.md','research/chapter-gate.json'}
 helpers=['probe_player_defects.py','repair_player_behavior.py','repair_lazy_and_markers.py','qa_player_behavior_library.py','qa_behavior_buttons.py','finish_player_behavior.py','route_record_movements.py','qa_record_routes.py','repair_vacated_slot.py','repair_reflow_and_vertical_routes.py','smooth_and_guard_replay.py','refine_reverse_replay.py','finalize_behavior_repair.py'];allowed.update('research/'+n for n in helpers)
 paths=[]
 for row in subprocess.check_output(['git','status','--porcelain'],cwd=R,text=True).splitlines():
  p=row[3:];assert p in allowed or p.startswith(('research/player-behavior-repair/','dist/evidence/player-behavior-repair/','research/render_')) or(p.startswith('dist/chapters/')and p.endswith('.html')),p;paths.append(p)
 subprocess.run(['git','add','--',*paths],cwd=R,check=True);subprocess.run(['git','diff','--cached','--check'],cwd=R,check=True);subprocess.run(['git','commit','-m','Fix visible simulation controls, state consistency and collision-free record transit'],cwd=R,check=True);print(git('rev-parse','HEAD'))
elif mode=='package':
 assert not git('status','--porcelain');files=[R/'.openai/hosting.json']+sorted(p for p in(R/'dist').rglob('*')if p.is_file());dest=Path('C:/Users/bheydari/AppData/Local/Temp/simulation-behavior-corrections.tar.gz')
 with tarfile.open(dest,'w:gz')as tf:
  for p in files:assert not p.is_symlink()and p.resolve().is_relative_to(R.resolve());tf.add(p,arcname=p.relative_to(R).as_posix(),recursive=False)
 with tarfile.open(dest,'r:gz')as tf:
  members=tf.getmembers();assert len(members)==len(files)
  for m,p in zip(members,files):assert m.name==p.relative_to(R).as_posix()and tf.extractfile(m).read()==p.read_bytes()
 print(json.dumps({'project_id':'appgprj_6ab5666f72b081918286c6b371c1eb1b','commit_sha':git('rev-parse','HEAD'),'archive':str(dest),'files':len(files),'archiveSha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))
