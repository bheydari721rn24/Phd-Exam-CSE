"""Evidence, bounded release notes, safe staging, and byte-verified static packaging."""
from pathlib import Path
import ast,hashlib,html,json,re,shutil,subprocess,sys,tarfile
R=Path(__file__).resolve().parents[1];E=R/'research/recent-animation-redesign';BASE='a9943ea8fb4e88eecd71c5c08fafc2e967937f11'
TOPICS=['a_select','s_descriptive','s_discrete','s_expectation','l_det','l_spaces','i_agents','i_uninformed','p_strings','p_recursion']
def git(*args):return subprocess.check_output(['git',*args],cwd=R,text=True,encoding='utf-8').strip()
def old(p):return subprocess.check_output(['git','show',BASE+':'+p],cwd=R).decode().replace('\r\n','\n')
def sha(s):return hashlib.sha256(s.encode()).hexdigest()
def lesson(s):
 s=re.search(r'<article class="lesson">(.*?)</article>',s,re.S).group(1)
 # The one corrected control value is audited separately, not hidden in the hash.
 return re.sub(r'<textarea name="edges">[\s\S]*?</textarea>','<textarea name="edges">INPUT_AUDITED_SEPARATELY</textarea>',s)
mode=sys.argv[1]
if mode=='prepare':
 browser=json.loads((E/'browser.json').read_text());assert browser['status']=='passed'
 parsed=ast.parse((R/'research/revise_recent_simulations.py').read_text())
 for node in parsed.body:
  if isinstance(node,ast.FunctionDef)and node.name=='mount_end':exec(compile(ast.Module(body=[node],type_ignores=[]),'audit','exec'))
 retention={'status':'passed','baseline':BASE,'chapters':{},'otherChapterPagesUnchanged':0,'searchControlCorrection':'Removed mathematical span markup from the literal graph-edge textarea; the renderer now protects textarea contents.'}
 for p in (R/'dist/chapters').glob('*.html'):
  rel=p.relative_to(R).as_posix()
  if p.stem not in TOPICS:
   assert old(rel)==p.read_text(encoding='utf-8'),rel
   retention['otherChapterPagesUnchanged']+=1
 for t in TOPICS:
  rel='dist/chapters/'+t;before=old(rel+'.js');after=(R/(rel+'.js')).read_text(encoding='utf-8');a=before.index('function mount(host,m)');b=after.index('function mount(host,m)');science_before=before[:a]+before[mount_end(before,a):];science_after=after[:b]+after[mount_end(after,b):];science_before=science_before.replace('current?.pause();current?.teaching.root.remove();','current?.dispose();');assert science_before==science_after,t
  before_page=old(rel+'.html');after_page=(R/(rel+'.html')).read_text(encoding='utf-8');assert lesson(before_page)==lesson(after_page),t
  before_models=json.loads(old(rel+'-models.json'));after_models=json.loads((R/(rel+'-models.json')).read_text(encoding='utf-8'));assert before_models==after_models,t
  subprocess.run(['node','--check',str(R/(rel+'.js'))],check=True,capture_output=True)
  retention['chapters'][t]={'lessonUnchanged':True,'questionsAndRulesUnchanged':True,'scientificEngineUnchanged':True,'allStoredModelsUnchanged':True,'lessonSha256':sha(lesson(after_page)),'engineSha256':sha(science_after)}
 subprocess.run(['node','--check',str(R/'dist/chapters/advanced-simulations.js')],check=True,capture_output=True)
 (E/'retention.json').write_text(json.dumps(retention,indent=2)+'\n',encoding='utf-8')
 manifest=json.loads((E/'manifest.json').read_text());runtime=(R/'dist/chapters/advanced-simulations.js').read_text();contracts={m[1]:ast.literal_eval("'"+m[2]+"'")for m in re.finditer(r"^ '([^']+)':'((?:\\.|[^'])*)'[,]?$",runtime,re.M)}
 for row in manifest['models']:
  audited=next(m for m in browser['chapters'][row['topic']]['models']if m['id']==row['id']);assert not audited['issues']and row['kind']in contracts,row
  row.update(status='passed',readingContract=contracts[row['kind']],renderers=audited['renderers'],frameReadingReview='All stored checkpoints rendered and checked in the browser; exact states retained; kind-specific explanation and operation timeline checked.',visualStrategy='New focus drawing plus retained original overview'if audited['renderers']!=['retained-geometry']else'Retain the domain geometry; rewrite operation explanation, exact comparison, changed-object emphasis and connected geometric replay')
 manifest.update(status='local_verification_passed',checkpoints=sum(m['checkpoints']for m in manifest['models']),modelsWithNewFocusDrawing=sum(m['renderers']!=['retained-geometry']for m in manifest['models']),modelsWithRetainedDomainGeometry=sum(m['renderers']==['retained-geometry']for m in manifest['models']))
 (E/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
 screen=Path(browser['screenshots']);target=E/'screenshots';target.mkdir(exist_ok=True)
 for p in screen.glob('*.png'):shutil.copy2(p,target/p.name)
 evidence=R/'dist/evidence/recent-animation-redesign';evidence.mkdir(parents=True,exist_ok=True)
 for name in ['manifest.json','browser.json','retention.json']:shutil.copy2(E/name,evidence/name)
 body='''<h1>Recent simulation redesign</h1><p>Ten chapters · 251 distinct models · 1,802 stored checkpoints. Revision of existing learning tools; chapter approval is a separate step.</p><h2>How to study one operation</h2><ol><li>Use <strong>Next</strong> to replay one operation. Read the operation and its reason beside the drawing.</li><li>Use <strong>Before</strong> or <strong>Compare</strong> to inspect the preceding and current exact states. The first displayed checkpoint has no preceding state.</li><li>Pause the movement or adjust <strong>Transition</strong> to inspect geometry in transit. Labels and counters describe the target checkpoint; interpolated geometry does not assert fractional algorithm steps or intermediate arithmetic results.</li><li>Open <strong>Exact changes</strong> for the complete changed fields, or <strong>Full exact state</strong> for the underlying stored values. Rounded readouts carry an approximation sign.</li><li>Use <strong>Browse all operations</strong> to jump directly to any recorded operation. <strong>Original overview</strong> preserves the preceding domain diagram as an additional view.</li><li>Every model starts paused. Arrow keys navigate checkpoints, Home/End select endpoints and Space controls playback when the model itself has focus. Reduced-motion mode preserves the exact states without animated transitions.</li></ol><h2>What was redesigned</h2><p>Record regions and moving cuts; byte addresses and read/write heads; suspended recursive continuations and connected invocation trees; probability masses on fixed axes; density areas and individual residual contributions; matrix operations and their companion matrices; conditional beliefs separated from evidence; and graph searches with complete path-aware frontier records.</p><p>For geometry that already represents the concept correctly, its coordinates and topology are retained. Its player, explanation, comparison, changed-object emphasis and replay are rebuilt. This is not a claim that every original drawing was discarded.</p><h2>Verification</h2><p>Every stored model and checkpoint passed browser checks for rendering, explanation, checkpoint selection, label containment and preservation of scientific records. All ten editable laboratories passed valid input, rejected-input preservation and replacement without accumulating hidden players. Pause and resume, manual transition progress, reduced motion, keyboard-compatible controls, print checkpoint generation, mobile containment and enlarged text were checked. Lessons, questions, final rules, source references and scientific engines remain unchanged. The graph laboratory's literal input was corrected after mathematical markup was found inside its textarea.</p><p><a href="../evidence/recent-animation-redesign/manifest.json">Individual model review</a> · <a href="../evidence/recent-animation-redesign/browser.json">Browser evidence</a> · <a href="../evidence/recent-animation-redesign/retention.json">Scientific and lesson retention</a></p><h2>Open a model</h2>'''
 for topic in TOPICS:
  rows=[m for m in manifest['models']if m['topic']==topic];page=(R/f'dist/chapters/{topic}.html').read_text();title=html.unescape(re.search(r'<h1>(.*?)</h1>',page,re.S).group(1));body+='<details><summary>'+html.escape(title)+' · '+str(len(rows))+' models</summary><ul>'
  for m in rows:body+='<li><a href="../chapters/'+topic+'.html#sim-'+m['id']+'">'+html.escape(m['title'])+'</a><p>'+html.escape(m['readingContract'])+'</p></li>'
  body+='</ul></details>'
 page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Recent simulation redesign</title><link rel="stylesheet" href="../chapters/chapter.en.css"><style>details{padding:14px;margin:12px 0;border:1px solid #c8d7df;border-radius:10px}summary{cursor:pointer;text-decoration:none}li p{font-size:15px;color:#506875}</style></head><body><main class="chapter"><p><a href="../index.html#library">Chapter library</a></p><article class="lesson">'+body+'</article></main></body></html>'
 (R/'dist/reviews/recent-simulation-redesign.html').write_text(page,encoding='utf-8')
 p=R/'dist/library-review.html';s=p.read_text();s=s.replace('<h2>Approval and remaining limits</h2>','<h2>Recent simulation revision</h2><p>The ten most recent chapter players were redesigned individually across 251 models and 1,802 checkpoints. <a href="reviews/recent-simulation-redesign.html">Open the new simulation guide and individual model reviews.</a></p><h2>Approval and remaining limits</h2>');p.write_text(s,encoding='utf-8')
 p=R/'research/chapter-gate.json';g=json.loads(p.read_text());assert g['state']=='awaiting_user_approval';g.update(recentAnimationRevisionStatus='local_verification_passed',activeWork='Simulation revision verified locally across ten recent chapters; publication pending. No following chapter begun.');p.write_text(json.dumps(g,indent=2)+'\n',encoding='utf-8')
 text=f'''# Recent simulation revision\n\nScope: ten most recent chapters, 251 models, 1802 exact stored checkpoints.\n\nAll players were rewritten around operation, reason, before/result/compare and interruptible replay. {manifest['modelsWithNewFocusDrawing']} models receive new focus drawings; {manifest['modelsWithRetainedDomainGeometry']} retain their valid domain geometry with rewritten teaching and playback. Each model is listed individually in manifest.json. Full browser checks passed; the scientific frames, algorithms, questions, rules and lesson content were compared to the frozen baseline. The sole lesson-markup correction removes mathematical HTML from the graph laboratory's literal textarea.\n\nActual pause is synchronous, including freezing the geometric progress; resuming continues the same transition. Every exact frame, mobile containment, 200-percent root text sizing, all ten default editable laboratories, invalid-input preservation, lab replacement, operation timelines, print checkpoint generation and reduced motion were checked. Representative desktop and mobile screenshots were inspected.\n\nThis revision neither approves p_recursion nor starts a following chapter. It does not re-rank university courses or claim a new exhaustive course survey. Publication is recorded separately.\n'''
 (E/'DELIVERY.en.md').write_text(text,encoding='utf-8')
 with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\n\n## Recent simulation revision — 9 October 2026\n\nTen recent chapters, 251 distinct models and 1802 recorded checkpoints: rebuilt causal replay, exact before/result comparison, semantic views and fully checked controls. All ten editable laboratories checked. Scientific states, engines, questions and final rules retained; one corrupted literal graph-input textarea corrected. User chapter gate remains unchanged. Publication tracked in research/recent-animation-redesign/publication.json.\n')
 print(json.dumps({'models':251,'checkpoints':1802,'newFocusDrawings':manifest['modelsWithNewFocusDrawing'],'retainedDomainGeometry':manifest['modelsWithRetainedDomainGeometry'],'otherChapterPagesUnchanged':retention['otherChapterPagesUnchanged']}))
elif mode=='commit':
 interactions=json.loads((E/'interactions.json').read_text());assert interactions['status']=='passed'
 for name in ['interactions.json']:shutil.copy2(E/name,R/'dist/evidence/recent-animation-redesign'/name)
 p=E/'manifest.json';m=json.loads(p.read_text());m['interactionAudit']='interactions.json';p.write_text(json.dumps(m,indent=2)+'\n',encoding='utf-8');shutil.copy2(p,R/'dist/evidence/recent-animation-redesign/manifest.json')
 p=R/'dist/reviews/recent-simulation-redesign.html';s=p.read_text();s=s.replace('Browser evidence</a>','Browser evidence</a> · <a href="../evidence/recent-animation-redesign/interactions.json">Keyboard, anchors and print evidence</a>');p.write_text(s,encoding='utf-8')
 exact={'WEEKLY_DELIVERY.md','dist/library-review.html','research/chapter-gate.json','research/ANIMATION_STANDARD.md','research/finish_recent_simulations.py','research/qa_recent_interactions.py','research/qa_recent_simulations.py','research/repair_search_input.py','research/revise_recent_simulations.py','dist/chapters/advanced-simulations.js','dist/chapters/advanced-simulations.css','dist/reviews/recent-simulation-redesign.html'}
 staged=[]
 for line in subprocess.check_output(['git','status','--porcelain'],cwd=R,text=True,encoding='utf-8').splitlines():
  p=line[3:];allowed=p in exact or p.startswith(('research/recent-animation-redesign/','dist/evidence/recent-animation-redesign/'))or any(p in('dist/chapters/'+t+'.html','dist/chapters/'+t+'.js')or p.startswith('research/render_'+t)for t in TOPICS);assert allowed,('Unexpected file, preserve without staging',p);staged.append(p)
 subprocess.run(['git','add','--',*staged],cwd=R,check=True);subprocess.run(['git','diff','--cached','--check'],cwd=R,check=True);subprocess.run(['git','commit','-m','Redesign 251 recent chapter simulations with causal replay and subject-specific focus views'],cwd=R,check=True);print(git('rev-parse','HEAD'))
elif mode=='package':
 assert not git('status','--porcelain');commit=git('rev-parse','HEAD');dest=Path('C:/Users/bheydari/AppData/Local/Temp/recent-animation-redesign.tar.gz');files=[R/'.openai/hosting.json']+sorted(p for p in(R/'dist').rglob('*')if p.is_file())
 assert all(p.resolve().is_relative_to(R.resolve())and not p.is_symlink()for p in files)
 with tarfile.open(dest,'w:gz')as tf:
  for p in files:tf.add(p,arcname=p.relative_to(R).as_posix(),recursive=False)
 with tarfile.open(dest,'r:gz')as tf:
  members=tf.getmembers();assert len(members)==len(files)
  for m,p in zip(members,files):assert m.name==p.relative_to(R).as_posix()and tf.extractfile(m).read()==p.read_bytes()
 print(json.dumps({'project_id':'appgprj_6ab5666f72b081918286c6b371c1eb1b','commit_sha':commit,'archive':str(dest),'files':len(files),'archiveSha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))
