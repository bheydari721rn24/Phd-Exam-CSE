"use strict";
(() => {
  const NS="http://www.w3.org/2000/svg", colors={plain:"#e9f1f7",active:"#ffda87",done:"#bee4d0",warning:"#efbfd0",muted:"#f3f4f5"};
  let dataPromise;const players=[];
  const data=()=>dataPromise??(dataPromise=fetch("concept-animations.json").then(r=>{if(!r.ok)throw Error("Animation data unavailable");return r.json();}));
  const el=(tag,cls,text)=>{const e=document.createElement(tag);if(cls)e.className=cls;if(text!==undefined)e.textContent=text;return e;};
  const svg=(tag,attrs)=>{const e=document.createElementNS(NS,tag);for(const [k,v] of Object.entries(attrs||{}))e.setAttribute(k,String(v));return e;};
  function motion(scene,n,a,t,fallback){
    if(a.x===n.x&&a.y===n.y)return fallback;
    let points;
    if(scene.id==="merge")points=[a,{x:44,y:a.y},{x:44,y:238},{x:n.x,y:238},n];
    else if(scene.id==="matrix-transpose")points=[a,{x:a.x,y:140},{x:350,y:140},{x:350,y:300},{x:n.x,y:300},n];
    else return fallback;
    const phase=Math.min(points.length-2,Math.floor(t*(points.length-1))),u=t===1?1:t*(points.length-1)-phase,A=points[phase],B=points[phase+1];return {x:A.x+(B.x-A.x)*u,y:A.y+(B.y-A.y)*u};
  }
  class Player{
    constructor(host,scenes){this.host=host;this.scenes=scenes;this.index=0;this.running=false;this.busy=false;this.speed=1;this.nodes=new Map();this.positions=new Map();this.generation=0;this.scene=scenes[0];this.build();this.show(0,false);players.push(this);}
    build(){
      const h=this.host;h.replaceChildren();h.append(el("h3",null,"Animated concept walkthrough"));
      const label=el("label",null,"Choose the concept or boundary case");this.choice=el("select");this.choice.setAttribute("aria-label","Choose an animated concept");
      this.scenes.forEach((s,i)=>{const o=el("option",null,s.title);o.value=i;this.choice.append(o);});label.append(this.choice);h.append(label);
      this.description=el("div","anim-description");h.append(this.description);
      const controls=el("div","anim-controls");this.buttons={};
      for(const [action,title] of [["reset","Restart"],["back","Previous step"],["play","Play"],["next","Next step"],["zoom","Enlarge diagram"]]){const b=el("button",null,title);b.type="button";b.dataset.action=action;this.buttons[action]=b;controls.append(b);b.addEventListener("click",()=>this.action(action));}
      const speed=el("label","anim-speed","Speed");this.speedSelect=el("select");this.speedSelect.setAttribute("aria-label","Animation speed");for(const n of [.5,1,2]){const o=el("option",null,`${n}×`);o.value=n;o.selected=n===1;this.speedSelect.append(o);}speed.append(this.speedSelect);controls.append(speed);h.append(controls);
      const progress=el("div","anim-progress");this.seek=el("input");this.seek.type="range";this.seek.min=0;this.seek.step=1;this.seek.setAttribute("aria-label","Choose the animation checkpoint");this.counter=el("span","anim-counter");progress.append(this.seek,this.counter);h.append(progress);
      const stage=el("div","anim-stage");stage.tabIndex=0;stage.setAttribute("aria-label","Scrollable animated mathematical diagram");this.canvas=svg("svg",{viewBox:"0 0 760 360",role:"img"});this.svgTitle=svg("title");this.canvas.append(this.svgTitle);this.grid=svg("g",{"aria-hidden":"true"});this.links=svg("g");this.nodeLayer=svg("g");this.canvas.append(this.grid,this.links,this.nodeLayer);stage.append(this.canvas);h.append(stage);
      const legend=el("div","anim-legend");this.legend=legend;for(const [tone,txt] of [["active","Currently inspected"],["done","Established or processed"],["warning","Counterexample or violated condition"]]){const s=el("span",null,txt);s.dataset.tone=tone;legend.append(s);}h.append(legend);
      this.metrics=el("dl","anim-metrics");h.append(this.metrics);this.explanation=el("div","anim-explanation");this.explanation.setAttribute("aria-live","polite");h.append(this.explanation);this.formula=el("div");h.append(this.formula);this.invariant=el("div","anim-invariant");h.append(this.invariant);this.status=el("p","anim-status");h.append(this.status);this.code=el("div","anim-code");this.code.setAttribute("aria-label","Highlighted algorithm or proof steps");h.append(this.code);
      this.choice.addEventListener("change",()=>{this.pause();this.scene=this.scenes[Number(this.choice.value)];this.show(0,false);});
      this.seek.addEventListener("input",()=>{this.pause();this.show(Number(this.seek.value),false);});
      this.speedSelect.addEventListener("change",()=>{this.speed=Number(this.speedSelect.value);});
      this.onKey=event=>{if(event.target.matches("input,select"))return;if(event.key==="ArrowRight"||event.key==="ArrowLeft"){event.preventDefault();this.action(event.key==="ArrowRight"?"next":"back");}};this.host.addEventListener("keydown",this.onKey);
    }
    pause(){this.running=false;this.generation++;if(this.raf)cancelAnimationFrame(this.raf);clearTimeout(this.timer);if(this.busy){const f=this.scene.frames[this.index];const end=new Map(f.nodes.map(n=>[n.id,{x:n.x,y:n.y}]));this.draw(f.nodes,f.edges||[],end);this.positions=end;}this.busy=false;this.buttons.play.textContent="Play";this.buttons.play.setAttribute("aria-pressed","false");}
    action(action){
      if(action==="zoom"){const enlarged=this.host.dataset.enlarged!=="true";this.host.dataset.enlarged=String(enlarged);this.buttons.zoom.textContent=enlarged?"Fit diagram":"Enlarge diagram";this.buttons.zoom.setAttribute("aria-pressed",String(enlarged));return;}
      if(action==="play"){if(this.running){this.pause();this.show(this.index,false);return;}players.forEach(p=>{if(p!==this)p.pause();});if(this.index===this.scene.frames.length-1)this.show(0,false);this.running=true;this.buttons.play.textContent="Pause";this.buttons.play.setAttribute("aria-pressed","true");this.advance();return;}
      this.pause();this.show(action==="reset"?0:Math.max(0,Math.min(this.scene.frames.length-1,this.index+(action==="next"?1:-1))),action!=="reset");
    }
    advance(){if(!this.running)return;if(this.index===this.scene.frames.length-1){this.pause();return;}this.show(this.index+1,true,()=>{if(this.running)this.timer=setTimeout(()=>this.advance(),900/this.speed);});}
    draw(nodes,edges,positions){
      if(window.SemanticDiagrams){window.SemanticDiagrams.draw(this,nodes,edges,positions);return;}
      const ids=new Set(nodes.map(n=>n.id));for(const [id,g] of this.nodes)if(!ids.has(id)){g.remove();this.nodes.delete(id);}
      this.links.replaceChildren();for(const edge of edges){const a=positions.get(edge.from),b=positions.get(edge.to);if(!a||!b)continue;const color=edge.tone==="warning"?"#a23c59":edge.tone==="active"?"#b17616":"#537e90";if(edge.from===edge.to){this.links.append(svg("path",{d:`M${a.x-16},${a.y-20} C${a.x-60},${a.y-74} ${a.x+60},${a.y-74} ${a.x+16},${a.y-20}`,fill:"none",stroke:color,"stroke-width":2}));continue;}const line=svg("path",{d:`M${a.x},${a.y} L${b.x},${b.y}`,fill:"none",stroke:color,"stroke-width":edge.tone==="active"?4:2});if(edge.dashed)line.setAttribute("stroke-dasharray","6 5");this.links.append(line);
        if(edge.directed){const dx=b.x-a.x,dy=b.y-a.y,len=Math.hypot(dx,dy)||1,x=b.x-dx/len*26,y=b.y-dy/len*26;this.links.append(svg("path",{d:`M${x-dx/len*10+dy/len*5},${y-dy/len*10-dx/len*5} L${x},${y} L${x-dx/len*10-dy/len*5},${y-dy/len*10+dx/len*5}`,fill:"none",stroke:color,"stroke-width":2}));}
      }
      for(const n of nodes){let g=this.nodes.get(n.id);if(!g){g=svg("g",{"data-entity":n.id});this.nodes.set(n.id,g);this.nodeLayer.append(g);}g.replaceChildren();const p=positions.get(n.id)||n;g.setAttribute("transform",`translate(${p.x} ${p.y})`);const w=n.w||88,h=n.h||46;
        if(n.kind==="point"){g.append(svg("circle",{r:n.radius||7,fill:n.tone==="active"?"#b17b14":n.tone==="warning"?"#a63c5b":"#2f7189"}));}
        else{g.append(svg("rect",{x:-w/2,y:-h/2,width:w,height:h,rx:7,fill:colors[n.tone]||colors.plain,stroke:n.tone==="warning"?"#a84866":"#96b7c7"}));}
        const lines=String(n.label).split("\n");const text=svg("text",{"text-anchor":"middle","font-size":n.size||22,y:n.kind==="point"?-17:lines.length===1?7:-3});lines.forEach((s,i)=>{const span=svg("tspan",{x:n.labelDx||0,dy:i===0?0:24});span.textContent=s;text.append(span);});g.append(text);if(n.labelDy)text.setAttribute("y",Number(text.getAttribute("y"))+n.labelDy);const limit=n.kind==="point"?(n.labelWidth||180):w-12;const measured=text.getBBox().width;if(measured>limit){text.setAttribute("font-size",Math.max(14,(n.size||22)*limit/measured));}
      }
    }
    drawGrid(axes){this.grid.replaceChildren();if(!axes)return;const {cx,cy,scale,xs,ys}=axes;for(const x of xs){const px=cx+x*scale;this.grid.append(svg("path",{d:`M${px},40 L${px},320`,stroke:x===0?"#91abb6":"#e5edf1","stroke-width":x===0?1.5:1}));const t=svg("text",{x:px,y:345,"text-anchor":"middle","font-size":16,fill:"#566f7b"});t.textContent=x;this.grid.append(t);}for(const y of ys){const py=cy-y*scale;this.grid.append(svg("path",{d:`M40,${py} L710,${py}`,stroke:y===0?"#91abb6":"#e5edf1","stroke-width":y===0?1.5:1}));const t=svg("text",{x:23,y:py+5,"text-anchor":"middle","font-size":16,fill:"#566f7b"});t.textContent=y;this.grid.append(t);}}
    show(index,animate,after){
      this.generation++;const gen=this.generation;if(this.raf)cancelAnimationFrame(this.raf);this.index=index;const f=this.scene.frames[index];this.drawGrid(this.scene.axes);this.busy=false;this.description.innerHTML=this.scene.descriptionHtml;this.seek.max=this.scene.frames.length-1;this.seek.value=index;this.seek.setAttribute("aria-valuetext",`Checkpoint ${index+1} of ${this.scene.frames.length}`);this.counter.textContent=`${index+1} / ${this.scene.frames.length}`;this.svgTitle.textContent=`${this.scene.title}. ${f.caption}`;
      this.explanation.innerHTML=f.captionHtml;this.formula.innerHTML=f.formulaHtml||"";this.invariant.innerHTML=this.scene.invariantHtml||"";this.status.textContent=f.status||"This saved state illustrates the stated model; the chapter supplies its general argument.";this.status.dataset.state=f.counterexample?"counterexample":"verified";
      this.metrics.replaceChildren();for(const [key,value] of Object.entries(f.metrics||{})){const d=el("div"),dt=el("dt");dt.innerHTML=f.metricLabels[key];d.append(dt,el("dd",null,String(value)));this.metrics.append(d);}
      this.code.replaceChildren();(this.scene.code||[]).forEach((line,i)=>{const s=el("span","anim-code-line"+(i===f.line?" active":""),`${i+1}  ${line}`);this.code.append(s);});this.code.hidden=!this.scene.code?.length;this.buttons.back.disabled=index===0;this.buttons.next.disabled=index===this.scene.frames.length-1;this.buttons.reset.disabled=index===0;this.host.dataset.scene=this.scene.id;this.host.dataset.step=index;this.host.dataset.steps=this.scene.frames.length;this.host.dataset.counterexample=String(!!f.counterexample);
      const start=new Map(this.positions),end=new Map(f.nodes.map(n=>[n.id,{x:n.x,y:n.y}]));const duration=animate&&!matchMedia("(prefers-reduced-motion: reduce)").matches?700/this.speed:0;
      const finish=()=>{this.draw(f.nodes,f.edges||[],end);this.positions=end;this.busy=false;this.status.textContent=f.status||"This saved state illustrates the stated model; the chapter supplies its general argument.";if(window.MathLayout)MathLayout.schedule();if(after)after();};
      if(!duration||!start.size){finish();return;}this.busy=true;this.status.textContent="Moving drawings interpolate between saved checkpoints; they do not introduce extra mathematical or electrical states.";const begin=performance.now();const tick=now=>{if(gen!==this.generation)return;const q=Math.min(1,(now-begin)/duration),t=q*q*(3-2*q),positions=new Map();for(const n of f.nodes){const a=start.get(n.id)||n;let x=a.x+(n.x-a.x)*t,y=a.y+(n.y-a.y)*t;
        if(f.motion?.kind==="rotation"&&n.geometry&&start.has(n.id)){const {cx,cy,angle}=f.motion,c=Math.cos(angle*t),s=Math.sin(angle*t);x=cx+(a.x-cx)*c-(a.y-cy)*s;y=cy+(a.x-cx)*s+(a.y-cy)*c;}
        positions.set(n.id,motion(this.scene,n,a,t,{x,y}));}this.draw(f.nodes,f.edges||[],positions);if(q<1)this.raf=requestAnimationFrame(tick);else finish();};this.raf=requestAnimationFrame(tick);
    }
  }
  async function init(host){if(host.dataset.loaded)return;host.dataset.loaded="loading";try{const all=await data(),ids=host.dataset.scenes.split(","),scenes=ids.map(id=>all.scenes[id]);if(scenes.some(x=>!x))throw Error("Missing scenario");new Player(host,scenes);host.dataset.loaded="true";}catch{host.dataset.loaded="error";host.textContent="The animation could not load. Reload this page to retry; the complete written explanation remains available above.";}}
  const observer=new IntersectionObserver(entries=>{for(const e of entries){if(e.isIntersecting){init(e.target);}else{const p=players.find(p=>p.host===e.target);if(p&&p.running){p.pause();p.show(p.index,false);}}}},{rootMargin:"250px"});document.querySelectorAll(".concept-animation").forEach(h=>observer.observe(h));
  document.addEventListener("visibilitychange",()=>{if(document.hidden)players.forEach(p=>{p.pause();p.show(p.index,false);});});
  addEventListener("beforeprint",()=>{document.querySelectorAll(".concept-animation").forEach(init);players.forEach(p=>{p.pause();p.show(p.index,false);});});
  // Deterministic access is used by the chapter's finite-example browser audit.
  window.ConceptAnimations={ready:init,players,motion,mount:(host,scenes)=>{for(let i=players.length-1;i>=0;i--)if(players[i].host===host){players[i].pause();host.removeEventListener("keydown",players[i].onKey);players.splice(i,1);}delete host.dataset.enlarged;return new Player(host,scenes);}};
})();
