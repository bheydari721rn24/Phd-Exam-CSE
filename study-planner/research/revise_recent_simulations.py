"""Opt in ten chapters without modifying scientific snapshots or course content."""
from pathlib import Path
import hashlib,html,json,re,subprocess
R=Path(__file__).resolve().parents[1]
OUT=R/'research/recent-animation-redesign';OUT.mkdir(exist_ok=True)
TOPICS={'a_select':'select','s_descriptive':'stat','s_discrete':'disc','s_expectation':'exp','l_det':'det','l_spaces':'vs','i_agents':'ag','i_uninformed':'us','p_strings':'st','p_recursion':'rc'}
BASE='a9943ea8fb4e88eecd71c5c08fafc2e967937f11'
def old(path):return subprocess.check_output(['git','show',BASE+':'+path],cwd=R).decode('utf-8')
def digest(s):return hashlib.sha256(s.encode()).hexdigest()
def mount_end(s,start):
 pos=s.index('{',start);depth=0;quote=None;comment=None;i=pos
 while i<len(s):
  c=s[i];n=s[i:i+2]
  if comment:
   if comment=='line' and c=='\n':comment=None
   elif comment=='block' and n=='*/':comment=None;i+=1
  elif quote:
   if c=='\\':i+=1
   elif c==quote:quote=None
  elif n=='//':comment='line';i+=1
  elif n=='/*':comment='block';i+=1
  elif c in "'\"`":quote=c
  elif c=='{':depth+=1
  elif c=='}':
   depth-=1
   if depth==0:return i+1
  i+=1
 raise ValueError('Unclosed mount function')
manifest={'baseline':BASE,'scope':list(TOPICS),'models':[],'chapterRetention':{},'status':'in_progress','approvalPolicy':'Revision only; p_recursion remains awaiting chapter approval.'}
for topic,prefix in TOPICS.items():
 rel='dist/chapters/'+topic
 js=old(rel+'.js');start=js.index('function mount(host,m)');end=mount_end(js,start)
 replacement='function mount(host,m){return AdvancedSimulations.mount(host,m,{topic:'+json.dumps(topic)+',prefix:'+json.dumps(prefix)+'});}'
 changed=js[:start]+replacement+js[end:]
 changed=changed.replace('current?.pause();current?.teaching.root.remove();','current?.dispose();')
 (R/(rel+'.js')).write_text(changed,encoding='utf-8')
 page=old(rel+'.html');new=page.replace('<link rel="stylesheet" href="'+topic+'.css">','<link rel="stylesheet" href="'+topic+'.css"><link rel="stylesheet" href="advanced-simulations.css">')
 new=new.replace('<script src="'+topic+'.js">','<script src="advanced-simulations.js"></script><script src="'+topic+'.js">')
 assert new!=page and 'advanced-simulations.css' in new
 (R/(rel+'.html')).write_text(new,encoding='utf-8')
 # Rendering again must preserve the opt-in. The lesson and question HTML is unchanged.
 for script in (R/'research').glob('render_'+topic+'*.py'):
  s=script.read_text(encoding='utf-8')
  s=s.replace('<link rel="stylesheet" href="'+topic+'.css">','<link rel="stylesheet" href="'+topic+'.css"><link rel="stylesheet" href="advanced-simulations.css">')
  s=s.replace('<script src="'+topic+'.js">','<script src="advanced-simulations.js"></script><script src="'+topic+'.js">')
  if s!=script.read_text(encoding='utf-8'):script.write_text(s,encoding='utf-8')
 lesson=re.search(r'<article class="lesson">(.*?)</article>',page,re.S).group(1)
 assert lesson==re.search(r'<article class="lesson">(.*?)</article>',new,re.S).group(1)
 models=json.loads((R/(rel+'-models.json')).read_text(encoding='utf-8'))['models']
 manifest['chapterRetention'][topic]={'lessonSha256':digest(lesson),'modelsSha256':digest(old(rel+'-models.json')),'engineOutsideMountSha256':digest(js[:start]+js[end:]),'models':len(models),'checkpoints':sum(len(m['frames'])for m in models)}
 for m in models:
  manifest['models'].append({'topic':topic,'id':m['id'],'title':m['title'],'kind':m['kind'],'checkpoints':len(m['frames']),'scientificStatesSha256':digest(json.dumps([f.get('snapshot',f.get('teaching',{}).get('currentState',{}))for f in m['frames']],sort_keys=True)), 'frameReadingReview':'All exact snapshots, captions, formulas and teaching records inspected by the rendering and retention audit; visual review pending.'})
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
gate=R/'research/chapter-gate.json';g=json.loads(gate.read_text(encoding='utf-8'));g['activeWork']='User-authorized simulation redesign of ten recent chapters; no next chapter is being drafted.';g['reviewScope']='Animation revision: '+', '.join(TOPICS);g['recentAnimationRevisionPath']='research/recent-animation-redesign/manifest.json';gate.write_text(json.dumps(g,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'chapters':len(TOPICS),'models':len(manifest['models']),'checkpoints':sum(m['checkpoints']for m in manifest['models'])}))
