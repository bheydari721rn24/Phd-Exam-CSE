"""Install uniform controls while retaining concept-specific drawing contracts."""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parents[1];D=R/'dist/chapters'

def replace_block(s,a,b,new):
 start=s.index(a);end=s.index(b,start);return s[:start]+new+s[end:]

def main():
 # Raw-SVG chapters share playback mechanics, not mathematical diagrams.
 for topic,kind in [('a_arrays','arrays'),('d_counting','counting'),('d_inclusion','inclusion'),('d_pigeonhole','pigeonhole')]:
  p=D/(topic+'.js');s=p.read_text(encoding='utf-8')
  new='''function mount(host,model){
 const q=s=>host.querySelector(s),api=TeachingTransitions.raw({host,model,stage:q('.K-stage'),caption:q('.K-caption'),formula:q('.K-formula'),seek:q('[data-seek]'),progress:q('[data-progress]'),play:q('[data-play]'),speed:q('[data-speed]'),prev:q('[data-prev]'),next:q('[data-next]'),reset:q('[data-reset]'),printRoot:q('.K-print-trace')});states.push(api.pause);
}
'''.replace('K-',kind+'-')
  s=replace_block(s,'function mount(host,model){',"fetch('",new);p.write_text(s,encoding='utf-8')
 # Stack/queue editable models use the same exact-state renderer and operation panel.
 p=D/'a_stackqueue.js';s=p.read_text(encoding='utf-8');s=replace_block(s,' function player(el,model){',' function formula(metrics){',''' function player(el,model){
  const q=s=>el.querySelector(s),api=TeachingTransitions.raw({host:el,model,stage:q('.sq-stage'),caption:q('.sq-caption'),formula:q('.sq-formula'),seek:q('[data-seek]'),progress:q('[data-progress]'),play:q('[data-play]'),speed:q('[data-speed]'),prev:q('[data-prev]'),next:q('[data-next]'),reset:q('[data-reset]'),printRoot:q('.sq-print-trace')});players.push(api);return api;
 }
''');p.write_text(s,encoding='utf-8')

 p=D/'concept-animation.js';s=p.read_text(encoding='utf-8')
 s=s.replace('this.show(0,false);players.push(this);','this.show(0,false);players.push(this);TeachingTransitions.register(this);')
 s=s.replace('stage.append(this.canvas);h.append(stage);','stage.append(this.canvas);h.append(stage);this.teaching=TeachingTransitions.panel(h,stage);this.printTrace=el("div","teaching-print");h.append(this.printTrace);')
 s=replace_block(s,'    pause(){','    action(action){','''    pause(){this.running=false;clearTimeout(this.timer);if(this.raf)cancelAnimationFrame(this.raf);this.raf=null;if(this.busy){this.pausedMotion=true;this.status.textContent="Motion paused at its current position. Play resumes this construction; Next step selects the next exact checkpoint.";this.status.dataset.motion="paused";}this.buttons.play.textContent="Play";this.buttons.play.setAttribute("aria-pressed","false");}
    print(){this.pause();this.printTrace.replaceChildren();const old=this.index;for(let i=0;i<this.scene.frames.length;i++){this.show(i,false);const figure=el('figure');figure.innerHTML=this.canvas.outerHTML;figure.append(el('figcaption',`Step ${i+1}. ${this.scene.frames[i].caption}`));this.printTrace.append(figure);}this.show(old,false);}
    clearPrint(){this.printTrace.replaceChildren();}
''')
 old='players.forEach(p=>{if(p!==this)p.pause();});if(this.index===this.scene.frames.length-1)this.show(0,false);this.running=true;this.buttons.play.textContent="Pause";this.buttons.play.setAttribute("aria-pressed","true");this.advance();return;'
 new='TeachingTransitions.players.forEach(p=>{if(p!==this)p.pause();});if(this.index===this.scene.frames.length-1&&!this.pausedMotion)this.show(0,false);this.running=true;this.buttons.play.textContent="Pause";this.buttons.play.setAttribute("aria-pressed","true");if(this.pausedMotion&&this.resumeMotion){this.pausedMotion=false;this.resumeMotion();}else this.advance();return;'
 assert old in s;s=s.replace(old,new)
 s=s.replace('this.pause();this.show(this.index,false);return;','this.pause();return;')
 s=s.replace('this.drawGrid(this.scene.axes);this.busy=false;','this.drawGrid(this.scene.axes);this.busy=false;this.pausedMotion=false;this.teaching.show(this.scene,f,index);')
 a=s.index('      if(!duration||!start.size)');b=s.index('\n    }\n  }',a)
 s=s[:a]+'''      if(!duration||!start.size){finish();return;}this.busy=true;this.status.dataset.motion="moving";this.status.textContent="Construction motion between exact checkpoints; discrete values stay at their stated checkpoint values.";let elapsed=0,last=performance.now();
      const tick=now=>{if(gen!==this.generation)return;elapsed+=now-last;last=now;const q=Math.min(1,elapsed/duration),t=q*q*(3-2*q),positions=new Map();for(const n of f.nodes){const a=start.get(n.id)||n;let x=a.x+(n.x-a.x)*t,y=a.y+(n.y-a.y)*t;
        if(f.motion?.kind==="rotation"&&n.geometry&&start.has(n.id)){const {cx,cy,angle}=f.motion,c=Math.cos(angle*t),s=Math.sin(angle*t);x=cx+(a.x-cx)*c-(a.y-cy)*s;y=cy+(a.x-cx)*s+(a.y-cy)*c;}
        positions.set(n.id,motion(this.scene,n,a,t,{x,y}));}this.positions=positions;this.draw(f.nodes,f.edges||[],positions);if(q<1)this.raf=requestAnimationFrame(tick);else{this.pausedMotion=false;delete this.status.dataset.motion;finish();}};
      this.resumeMotion=()=>{last=performance.now();this.raf=requestAnimationFrame(tick);};this.resumeMotion();
''' +s[b:]
 s=s.replace('700/this.speed','1000/this.speed').replace('900/this.speed','Math.max(1250,1500/this.speed)')
 # Fixed positional identifiers never travel with record identities; exchanges use separate lanes.
 s=s.replace('else return fallback;','else if(scene.visual?.type==="bars"&&Math.abs(a.y-n.y)<1&&/^(r|record)\\d+$/.test(n.id))return {x:a.x+(n.x-a.x)*t,y:a.y+Math.sin(Math.PI*t)*(n.x>a.x?-65:65)};else return fallback;')
 p.write_text(s,encoding='utf-8')
 # Preserve the existing error fallback and use typed problem frames in the same controls.
 p=D/'problem-visuals.js';s=p.read_text(encoding='utf-8');a=s.index('async function mount(host)');b=s.index('\nconst observer=',a)
 s=s[:a]+'''async function mount(host){if(host.dataset.loaded)return;const fallbackMarkup=host.innerHTML;host.dataset.loaded='loading';try{const all=await load(),m=all[host.dataset.problemVisual];if(!m)throw Error('Missing problem model');host.replaceChildren();host.append(el('h4','Visual solution aid'),el('p',m.reading,'problem-reading'));const controls=el('div',undefined,'problem-controls'),q={};for(const [key,label] of [['reset','Restart'],['prev','Previous step'],['play','Play'],['next','Next step']]){q[key]=el('button',label);q[key].type='button';controls.append(q[key]);}const speed=el('select');speed.setAttribute('aria-label','Solution playback speed');for(const v of [.5,1,2]){const option=el('option',v+'×');option.value=v;option.selected=v===1;speed.append(option);}controls.append(el('label','Speed'),speed);const seek=el('input');seek.type='range';seek.min=0;seek.step=1;seek.setAttribute('aria-label','Choose a solution checkpoint');const count=el('span',undefined,'problem-counter'),progress=el('div',undefined,'problem-progress');progress.append(seek,count);if(m.frames.length>1)host.append(controls,progress);const stage=el('div',undefined,'problem-stage');stage.tabIndex=0;const caption=el('p',undefined,'problem-caption');caption.setAttribute('aria-live','polite');const printRoot=el('div',undefined,'teaching-print');host.append(stage,caption,el('p',m.scope,'problem-scope'),printRoot);const api=TeachingTransitions.raw({host,model:m,stage,caption,seek,progress:count,speed,play:q.play,prev:q.prev,next:q.next,reset:q.reset,printRoot});players.push(api);host.dataset.loaded='true';}catch(e){host.innerHTML=fallbackMarkup;host.dataset.loaded='error';host.append(el('p','The interactive aid could not load. Its printed first diagram and full written solution remain available.'));console.error(e);}}
''' +s[b:];p.write_text(s,encoding='utf-8')
 # Script order is important: the transition engine must exist before each chapter player.
 for p in D.glob('*.html'):
  if not re.match(r'^[daslgp]_',p.stem):continue
  s=p.read_text(encoding='utf-8')
  if 'teaching-transitions.js' not in s:s=s.replace('<script ', '<script src="teaching-transitions.js?v=library-decision-1"></script><script ',1)
  if 'teaching-transitions.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="teaching-transitions.css?v=library-decision-1"></head>')
  s=re.sub(r'((?:concept-animation|semantic-diagrams|problem-visuals|a_arrays|a_stackqueue|d_counting|d_inclusion|d_pigeonhole)\.js)(?:\?v=[^"\s]*)?',r'\1?v=library-decision-1',s)
  p.write_text(s,encoding='utf-8')
 print('Installed decision explanations, exact before/after state, true pause and paced controls in all 37 chapters.')
if __name__=='__main__':main()
