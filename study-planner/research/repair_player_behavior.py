"""Repair real user controls, displayed-state consistency and insertion identities."""
from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/advanced-simulations.js';s=p.read_text(encoding='utf-8')
def change(a,b):
 global s
 assert a in s,a[:120]
 s=s.replace(a,b)
change("let serial=0;","let serial=0, insertion=0;")
change("if(exactCache.has(key))return exactCache.get(key).cloneNode(true);","if(exactCache.has(key))return freshDrawing(exactCache.get(key));")
change("exactCache.set(key,svg.cloneNode(true));return svg;","exactCache.set(key,svg.cloneNode(true));return freshDrawing(svg);")
marker="  function setGeometry(t)"
addition="""  // Every inserted copy has distinct marker/clip IDs, including printed and compare copies.
  function freshDrawing(node){const copy=node.cloneNode(true),suffix='-copy-'+(++insertion),ids=new Map();for(const n of copy.querySelectorAll('[id]')){ids.set(n.id,n.id+suffix);n.id+=suffix;}for(const n of [copy,...copy.querySelectorAll('*')])for(const a of [...n.attributes]){let value=a.value;for(const [old,id]of ids){value=value.replaceAll('url(#'+old+')','url(#'+id+')');if(value==='#'+old)value='#'+id;}if(value!==a.value)n.setAttribute(a.name,value);}return copy;}
  const syncPlay=()=>{const moving=clock?.playState==='running';play.textContent=running||moving?'Pause':'Play';play.setAttribute('aria-pressed',String(running||moving));host.dataset.playback=running?'playing':moving?'stepping':transition<1?'paused-transition':'paused';};
"""
change(marker,addition+marker)
change("let index=0,running=false,timer=null,raf=null,clock=null,continueMotion=null,pairs=[]","let index=0,replayFrom=0,running=false,timer=null,raf=null,clock=null,continueMotion=null,pairs=[]")
change("if(raf)cancelAnimationFrame(raf);raf=null;};\n  const cancelMotion", "if(raf)cancelAnimationFrame(raf);raf=null;syncPlay();};\n  const cancelMotion")
change("if(withMotion&&view==='after')animate();", "if(withMotion&&view==='after')animate();syncPlay();")
change("setGeometry(0);const tick", "setGeometry(0);syncPlay();const tick")
change("probe.remove();raf=null;continueMotion=null;", "probe.remove();raf=null;continueMotion=null;syncPlay();")
change("const f=model.frames[index],s=actual(f),old=index?actual(model.frames[index-1]):{},t=window.TeachingTransitions?.metadata(model,f,index)??f.teaching??{},changes=index?diff(old,s):[];", "const shown=view==='before'?Math.max(0,index-1):index,f=model.frames[shown],s=actual(f),old=shown?actual(model.frames[shown-1]):{},t=window.TeachingTransitions?.metadata(model,f,shown)??f.teaching??{},changes=shown?diff(old,s):[];host.dataset.displayedFrame=shown;")
change("teach.append(el('p',index?'Operation '+(index+1)","teach.append(el('p',shown?'Operation '+(shown+1)")
change("readouts(s,old)","readouts(s,old,shown)")
change("function readouts(s,old,shown)","function readouts(s,old,shown)")
change("box.dataset.changed=String(index>0", "box.dataset.changed=String(shown>0")
change("if(!changes.length)delta.replaceChildren(el('p',index?", "if(!changes.length)delta.replaceChildren(el('p',shown?")
change("motionSeek.disabled=index===0||view!=='after'", "motionSeek.disabled=replayFrom===index||view!=='after'")
change("function draw(i,withMotion=false){\n   cancelMotion();index=", "function draw(i,withMotion=false){\n   const origin=index;cancelMotion();index=")
change("Math.trunc(i)));stage.replaceChildren();", "Math.trunc(i)));replayFrom=withMotion?origin:Math.max(0,index-1);stage.replaceChildren();")
change("stage.querySelectorAll('svg').forEach(fit);", "")
change("stage.append(svg);fit(svg);if(index&&view==='after'){const before=exactView(index-1);", "stage.append(svg);if(replayFrom!==index&&view==='after'){const before=exactView(replayFrom);")
change("play.onclick=()=>{if(running){stops();return;}", "play.onclick=()=>{if(running||clock?.playState==='running'){stops();return;}")
change("if(index===model.frames.length-1){view='after';draw(0);}", "if(index===model.frames.length-1&&transition===1){view='after';draw(0);}else if(view!=='after'){view='after';draw(index);}")
change("if(clock&&clock.currentTime<900){clock.play();if(continueMotion)raf=requestAnimationFrame(continueMotion);}schedule();", "if(clock&&clock.currentTime<900){clock.play();if(continueMotion)raf=requestAnimationFrame(continueMotion);}else if(transition<1&&stage.querySelector('svg')){const start=transition;animate();clock.currentTime=start*900;setGeometry(start);}syncPlay();schedule();")
change("motionSeek.oninput=()=>{const target=Number(motionSeek.value)/100;stops();cancelMotion();setGeometry(target);};", "motionSeek.oninput=()=>{const target=Number(motionSeek.value)/100;stops();cancelMotion();setGeometry(target);syncPlay();};")
change("get index(){return index;},get running()", "get index(){return index;},get replayFrom(){return replayFrom;},get running()")
change("const map=new Map([...before.querySelectorAll('[data-entity]')].map(n=>[n.dataset.entity,n])),pairs=[];", "const map=new Map([...before.querySelectorAll('[data-entity]')].map(n=>[n.dataset.entity,n])),pairs=[],seen=new WeakMap();")
change("pairs.push({node:b,attr,a:aa,b:bb,template:bv,target:bv});", "{if(!seen.has(b))seen.set(b,new Set());if(seen.get(b).has(attr))continue;seen.get(b).add(attr);pairs.push({node:b,attr,a:aa,b:bb,template:bv,target:bv});}")
change("b.forEach((n,i)=>add(a[i],n));", "if(a.length===b.length&&a.every((n,i)=>n.tagName===b[i].tagName))b.forEach((n,i)=>add(a[i],n));")
change("Connectors outside an entity are paired by structural position. Their endpoint", "Entity descendants morph only when their structural signatures match.")
change("coordinates therefore move with the same interpolation as their attached bodies.", "External connectors require stable endpoint identities; rewiring is atomic.")
p.write_text(s,encoding='utf-8')
print('User controls, previous state, reverse replay and copy identities repaired.')
