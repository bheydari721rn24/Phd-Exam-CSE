"""Install measured typography and exact ports without changing mathematical states."""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parents[1]; B=R/'research/library-visual-question-review/baseline'; D=R/'dist/chapters'
s=(B/'semantic-diagrams.js').read_text(encoding='utf-8')
a=s.index('function arrow(');z=s.index('\nconst num=',a)
s=s[:a]+'''function arrow(g,x,y,X,Y,color=C.blue){return path(g,`M${x} ${y}L${X} ${Y}`,color,1.6,{'data-layout-arrow':JSON.stringify([[x,y],[X,Y]])});}'''+s[z:]
s=s.replace('p.canvas.dataset.visualContract=p.scene.visual.claim;}','p.canvas.dataset.visualContract=p.scene.visual.claim;window.DiagramLayout?.finish(p.canvas);}')
s=s.replace('text(g,575,223,"reference",15)', 'text(g,680,215,"reference",15)')
s=s.replace('rect(g,130+i*260,270-150*v,80,150*v', 'rect(g,130+i*260,300-110*v,80,110*v').replace('text(g,170+i*260,250-150*v,v,22)', 'text(g,170+i*260,280-110*v,v,22)')
# Opposite relation edges have separate ports and return lanes, including self loops.
a=s.index(' if(id==="transitive-closure"');z=s.index('\n if(id==="image-collapse"',a)
s=s[:a]+''' if(id==="transitive-closure"||id==="reflexive-closure"){const xs=[110,290,470,650],y=95,r=22;const tip=(pathEl)=>{const defs=E("defs"),m=E("marker",{id:"relation-tip-"+p.index,markerWidth:7,markerHeight:6,refX:7,refY:3,orient:"auto",markerUnits:"userSpaceOnUse"});m.append(E("path",{d:"M0 0L7 3L0 6Z",fill:C.blue}));defs.append(m);g.append(defs);pathEl.setAttribute("marker-end","url(#relation-tip-"+p.index+")");};
  s.relation.forEach(([a,b])=>{let d;if(a===b){const t=r/Math.sqrt(2);d=`M${xs[a]-t} ${y-t}C${xs[a]-52} ${y-75} ${xs[a]+52} ${y-75} ${xs[a]+t} ${y-t}`;}else{const left=a<b,x=xs[a]+(left?r:-r),X=xs[b]+(left?-r:r),lane=left?y-30-9*(b-a):y+30+9*(a-b);d=`M${x} ${y}Q${(x+X)/2} ${lane} ${X} ${y}`;}tip(path(g,d,C.blue,1.6));});xs.forEach((x,i)=>{dot(g,x,y,r,i===s.admitted-1?C.amber:C.blue);text(g,x,y+7,i,21,"middle","white");});matrix(g,Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>+s.relation.some(([a,b])=>a===i&&b===j))),245,180,"Reachability matrix");return;}'''+s[z:]
(D/'semantic-diagrams.js').write_text(s,encoding='utf-8')
# The three precomputed players are repaired after each drawing. This is also applied
# to printed frames; the underlying saved states and formulas are never regenerated.
for topic,word in [('d_counting','counting'),('d_inclusion','inclusion'),('d_pigeonhole','pigeonhole')]:
 p=D/(topic+'.js');s=p.read_text(encoding='utf-8')
 if 'DiagramLayout.finish(stage' not in s:s=s.replace('stage.innerHTML=f.svg;', 'stage.innerHTML=f.svg;window.DiagramLayout?.finish(stage.querySelector("svg"));')
 if 'DiagramLayout.finish(stage' in s and 'let pendingLayout' not in s:
  s=s.replace('  window.MathLayout?.schedule();','  let pendingLayout=true;requestAnimationFrame(function follow(){if(!pendingLayout)return;window.DiagramLayout?.finish(stage.querySelector("svg"),{arrows:false,labels:false});if(stage.getAnimations({subtree:true}).length)requestAnimationFrame(follow);else pendingLayout=false;});\n  window.MathLayout?.schedule();',1)
 p.write_text(s,encoding='utf-8')
for c in json.loads((R/'research/animation-manifest.json').read_text())['chapters']:
 p=D/(c['topicId']+'.html');s=p.read_text(encoding='utf-8')
 if 'diagram-layout.js' not in s:s=s.replace('<script ', '<script src="diagram-layout.js?v=library-ports-3"></script><script ',1)
 s=re.sub(r'(semantic-diagrams|concept-animation)\.js(?:\?v=[^"\s]*)?',r'\1.js?v=library-ports-3',s)
 p.write_text(s,encoding='utf-8')
print('Installed shared boundary/padding finish in all 35 chapters.')
