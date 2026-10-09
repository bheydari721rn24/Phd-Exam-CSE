/* One interface; each scenario retains its subject-specific drawing and exact states. */
"use strict";
(() => {
 const NS='http://www.w3.org/2000/svg',players=[];let dataPromise;
 const data=()=>dataPromise??(dataPromise=fetch('concept-animations.json').then(r=>{if(!r.ok)throw Error('Animation data unavailable');return r.json();}));
 const el=(tag,text,cls)=>{const n=document.createElement(tag);if(text!==undefined)n.textContent=text;if(cls)n.className=cls;return n;};
 const svg=(tag,attrs={})=>{const n=document.createElementNS(NS,tag);for(const [k,v]of Object.entries(attrs))n.setAttribute(k,v);return n;};
 const plain=markup=>{const n=el('div');n.innerHTML=markup??'';return n.textContent.trim();};
 function sceneCopy(scene){
  const type=scene.visual?.type??(scene.id.startsWith('functions-custom-')?'memory':scene.id.startsWith('arrays-custom-')?'array':scene.id.startsWith('kmap-custom-')?'kmap':scene.id.startsWith('combin-custom-')?'circuit':null);
  if(!type)throw Error('No subject-specific visual contract for '+scene.id);
  return {...scene,kind:'concept:'+type,visual:{...scene.visual,type},invariant:scene.invariant??plain(scene.invariantHtml),description:scene.description??plain(scene.descriptionHtml)};
 }
 class Player{
  constructor(host,scenes){this.host=host;this.scenes=scenes;this.scene=scenes[0];this.api=null;this.currentScene=null;this.build();this.show(0);players.push(this);}
  build(){
   const h=this.host;h.replaceChildren();h.append(el('h3','Animated concept walkthrough'));const label=el('label','Choose the concept or boundary case');this.choice=el('select');this.choice.setAttribute('aria-label','Choose an animated concept');this.scenes.forEach((s,i)=>{const o=el('option',s.title);o.value=i;this.choice.append(o);});label.append(this.choice);h.append(label);this.description=el('div',undefined,'sim-description');this.workspace=el('section',undefined,'sim-concept-workspace');this.legend=el('div',undefined,'anim-legend');h.append(this.description,this.workspace,this.legend);h.tabIndex=0;
   this.choice.onchange=()=>{this.pause();this.scene=this.scenes[Number(this.choice.value)];this.show(0);};
  }
  render(f,index){
   if(this.cache.has(index))return this.cache.get(index);
   const measuring=el('div',undefined,'sim-measure');measuring.style.cssText='position:fixed;left:-10000px;top:0;width:760px;visibility:hidden';
   const canvas=svg('svg',{viewBox:'0 0 760 360',role:'img'}),title=svg('title');title.textContent=this.scene.title+'. '+f.caption;canvas.append(title);const grid=svg('g'),links=svg('g'),nodeLayer=svg('g');canvas.append(grid,links,nodeLayer);measuring.append(canvas);this.workspace.append(measuring);
   try{
    const p={scene:this.renderScene,index,canvas,grid,links,nodeLayer,nodes:new Map(),positions:new Map(),legend:this.legend};
    SemanticDiagrams.draw(p,f.nodes??[],f.edges??[],new Map((f.nodes??[]).map(n=>[n.id,{x:n.x,y:n.y}])));
    for(const n of canvas.querySelectorAll('[data-record]'))n.dataset.entity=n.dataset.record;
    const markup=canvas.outerHTML;this.cache.set(index,markup);return markup;
   }finally{measuring.remove();}
  }
  show(index){
   if(this.scene!==this.currentScene){
    this.api?.dispose();this.workspace.replaceChildren();this.currentScene=this.scene;this.renderScene=sceneCopy(this.scene);this.cache=new Map();this.description.textContent=this.renderScene.description;
    const elements=AdvancedSimulations.structure(this.workspace),reading=this.scene.frames[0]?.teaching?.reading??this.renderScene.visual.claim??this.renderScene.description??this.renderScene.invariant;
    this.api=AdvancedSimulations.mount(this.workspace,this.renderScene,{topic:location.pathname.split('/').at(-1).replace(/\.html$/,''),elements,renderFrame:(f,i)=>this.render(f,i),reading});
    this.buttons={play:this.workspace.querySelector('[data-play]'),back:this.workspace.querySelector('[data-prev]'),next:this.workspace.querySelector('[data-next]'),reset:this.workspace.querySelector('[data-reset]')};this.seek=this.workspace.querySelector('[data-seek]');
   }
   this.api.show(index);this.host.dataset.loaded='true';this.host.dataset.scene=this.scene.id;this.host.dataset.step=this.api.index;this.host.dataset.steps=this.scene.frames.length;
  }
  get index(){return this.api?.index??0;}set index(n){/* Legacy labs select the exact state with show after assigning their new scene. */}
  get running(){return this.api?.running??false;}
  pause(){this.api?.pause();}print(){this.api?.print();}clearPrint(){this.api?.clearPrint();}
  dispose(){this.api?.dispose();const i=players.indexOf(this);if(i>=0)players.splice(i,1);}
 }
 async function init(host){if(host.dataset.loaded)return;host.dataset.loaded='loading';try{const all=await data(),scenes=host.dataset.scenes.split(',').map(id=>all.scenes[id]);if(scenes.some(x=>!x))throw Error('Missing scenario');return new Player(host,scenes);}catch(e){host.dataset.loaded='error';host.textContent='The animation could not load. The complete written explanation remains available.';console.error(e);}}
 const observer=new IntersectionObserver(entries=>{for(const e of entries)if(e.isIntersecting)init(e.target);else players.find(p=>p.host===e.target)?.pause();},{rootMargin:'250px'});document.querySelectorAll('.concept-animation').forEach(h=>observer.observe(h));
 addEventListener('beforeprint',()=>{document.querySelectorAll('.concept-animation').forEach(init);players.forEach(p=>p.print());});
 window.ConceptAnimations={ready:init,players,mount:(host,scenes)=>{players.filter(p=>p.host===host).forEach(p=>p.dispose());delete host.dataset.enlarged;return new Player(host,scenes);}};
})();
