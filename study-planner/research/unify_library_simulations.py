"""Standardize every written chapter without changing its scientific records."""
from pathlib import Path
import json,re,subprocess,hashlib
R=Path(__file__).resolve().parents[1];E=R/'research/library-simulation-standard';E.mkdir(exist_ok=True)
BASE='9fb90add0f9238788a407433259927f18d2eadc6'
def boundary(s,start):
 i=s.index('{',start);depth=0;quote=None;comment=None
 while i<len(s):
  c=s[i];n=s[i:i+2]
  if comment:
   if comment=='line'and c=='\n':comment=None
   elif comment=='block'and n=='*/':comment=None;i+=1
  elif quote:
   if c=='\\':i+=1
   elif c==quote:quote=None
  elif n=='//':comment='line';i+=1
  elif n=='/*':comment='block';i+=1
  elif c in "'\"`":quote=c
  elif c=='{':depth+=1
  elif c=='}':
   depth-=1
   if not depth:return i+1
  i+=1
 raise ValueError('Unclosed function')
def includes(s):
 s=re.sub(r'<link rel="stylesheet" href="advanced-simulations.css[^\"]*">','',s)
 s=re.sub(r'<script src="advanced-simulations.js[^\"]*"></script>','',s)
 s=s.replace('</head>','<link rel="stylesheet" href="advanced-simulations.css?v=library-unified-1"></head>')
 first=s.find('<script src=');assert first>=0
 s=s[:first]+'<script src="advanced-simulations.js?v=library-unified-1"></script>'+s[first:]
 if not re.search(r'src="diagram-layout.js',s):s=s.replace('<script src="advanced-simulations.js?v=library-unified-1"></script>','<script src="advanced-simulations.js?v=library-unified-1"></script><script src="diagram-layout.js?v=library-ports-3"></script>')
 for name in ['teaching-transitions.js','concept-animation.js','problem-visuals.js','a_sort.js']:
  s=re.sub(r'(src="'+re.escape(name)+r')(?:\?[^\"]*)?"',r'\1?v=library-unified-1"',s)
 return s
chapters=sorted(p.stem for p in(R/'dist/chapters').glob('*.html'))
for topic in chapters:
 p=R/f'dist/chapters/{topic}.html';p.write_text(includes(p.read_text(encoding='utf-8')),encoding='utf-8')
 # Preserve the standard if a chapter is rendered from its authoring source again.
 for p in(R/'research').glob('render_'+topic+'*.py'):
  s=p.read_text(encoding='utf-8')
  if '</head>'in s and '<script src='in s:p.write_text(includes(s),encoding='utf-8')
p=R/'dist/chapters/a_sort.js';s=p.read_text();start=s.index('function player(el,model)');end=boundary(s,start)
s=s[:start]+'''function player(el,model){const api=AdvancedSimulations.mount(el,model,{topic:'a_sort',prefix:'sort',retainDrawing:true,reading:teachingGuides[model.kind]?.join(' ')??model.frames[0].teaching?.why??'Follow comparison branches and input-order leaves; tree height bounds worst-case comparisons.'});players.push(api);return api;}'''+s[end:]
s=s.replace('active.pause();players.splice(players.indexOf(active),1);','active.dispose();players.splice(players.indexOf(active),1);');p.write_text(s,encoding='utf-8')
manifest={'baseline':BASE,'chapters':chapters,'chapterCount':len(chapters),'status':'in_progress','policy':'Consistent controls and layout; concept-specific scientific geometry and full lesson retained. No chapter promotion.'}
(E/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
p=R/'research/ANIMATION_STANDARD.md';s=p.read_text();s+='''\n\n## Entire written library: consistent simulation interface (9 October 2026)\n\nAll written chapters, including visual aids within worked solutions and adjustable traces, load advanced-simulations.js and advanced-simulations.css after chapter styles. Use AdvancedSimulations.mount for checkpoint models, adaptRaw for existing exact SVG models and ConceptAnimations.mount for SemanticDiagrams models. Use the same paused controls, before/result/compare/reference views, transition slider, operation timeline, teaching sidebar, exact snapshot and print trace. Preserve subject-specific diagrams, including circuit wiring, Karnaugh maps, matrices, geometry and probability diagrams. Never replace scientific geometry with a generic cartoon to achieve consistency. Keep predicates, decision results, counterexample labels, region intervals and invariant instructions. Regeneration must retain the shared interface. Verify every written chapter, every distinct used model and all its saved states.\n''';p.write_text(s,encoding='utf-8')
print(json.dumps({'chapters':len(chapters),'baseline':BASE}))
