/* Measured native MathML layout; fences, operator order and scripts retain scope. */
"use strict";
(() => {
const NS="http://www.w3.org/1998/Math/MathML",saved=new WeakMap(),M=t=>document.createElementNS(NS,t),script=new Set(["msup","msub","msubsup","mover","munder","munderover"]),relations=new Set(["=","≡","⇒","⇔","≤","≥","≈",",",";","+","−","-","∨","∧","⊕"]);
const base=e=>script.has(e.localName)?base(e.firstElementChild):e;
const token=e=>{const b=base(e);return b.localName==="mo"?b.textContent:"";};
const opening=t=>["(","[","{"].includes(t),closing=t=>[")","]","}"].includes(t),width=e=>e.getBoundingClientRect().width;
function regroup(e){for(const c of [...e.children])regroup(c);if(e.localName!=="mrow"||e.dataset.fenced==="true")return;const nodes=[...e.children],out=[];
 for(let i=0;i<nodes.length;i++){const first=nodes[i];if(!opening(token(first))){out.push(first);continue;}let depth=1,j=i+1;for(;j<nodes.length;j++){if(opening(token(nodes[j])))depth++;if(closing(token(nodes[j])))depth--;if(!depth)break;}if(depth){out.push(first);continue;}
  const last=nodes[j],scripts=script.has(last.localName)?[...last.children].slice(1):[],row=M("mrow"),inside=M("mrow");row.dataset.fenced="true";inside.append(...nodes.slice(i+1,j));regroup(inside);row.append(first,inside,base(last));if(script.has(last.localName)){const holder=M(last.localName);holder.append(row,...scripts);out.push(holder);}else out.push(row);i=j;
 }e.replaceChildren(...out);
}
function table(lines){const t=M("mtable");t.setAttribute("columnalign","left");t.setAttribute("rowspacing",".55em");t.setAttribute("displaystyle","true");for(const line of lines){const tr=M("mtr"),td=M("mtd"),row=M("mrow");row.append(...line);td.append(row);tr.append(td);t.append(tr);}return t;}
function reflow(e,limit){if(limit<90||e.localName==="mtable")return;
 if(e.dataset.fenced==="true")return;
 const allowance=script.has(e.localName)?Math.max(30,[...e.children].slice(1).reduce((n,c)=>n+width(c),0)):e.localName==="msqrt"?20:0;
 for(const c of [...e.children])reflow(c,limit-allowance);
 if(e.localName!=="mrow"||width(e)<=limit)return;const children=[...e.children],chunks=[];let part=[];
 for(const c of children){if(c.localName==="mo"&&relations.has(c.textContent)&&part.length){chunks.push(part);part=[];}part.push(c);}if(part.length)chunks.push(part);if(chunks.length<2)return;
 const commas=children.some(c=>c.localName==="mo"&&[",",";"].includes(c.textContent)),relational=children.some(c=>c.localName==="mo"&&["=","≡","⇒","⇔","≤","≥","≈"].includes(c.textContent));
 const cuts=commas?new Set([",",";"]):relational?new Set(["=","≡","⇒","⇔","≤","≥","≈"]):relations;
 const grouped=[];let group=[];for(const c of children){if(c.localName==="mo"&&cuts.has(c.textContent)&&group.length){grouped.push(group);group=[];}group.push(c);}if(group.length)grouped.push(group);
 const lines=[];let current=[],used=0;for(const group of grouped){const w=group.reduce((n,c)=>n+width(c),0)+8;if(current.length&&used+w>limit){lines.push(current);current=[];used=0;}current.push(...group);used+=w;}if(current.length)lines.push(current);if(lines.length>1)e.replaceChildren(table(lines));
}
function layout(){for(const math of document.querySelectorAll('math[display="block"]')){if(!saved.has(math))saved.set(math,math.innerHTML);math.innerHTML=saved.get(math);const box=math.closest('.formula-block')||math.parentElement,limit=box.clientWidth-48;if(limit<=0)continue;const source=math.textContent;regroup(math);if(width(math)>limit){reflow(math.firstElementChild,limit);math.dataset.semanticWrap="true";}else delete math.dataset.semanticWrap;if(math.textContent!==source)throw Error("Mathematical tokens changed during layout");if(box.classList.contains("formula-block"))box.dataset.scrollable=String(box.scrollWidth>box.clientWidth+2);}}
let raf;const schedule=()=>{cancelAnimationFrame(raf);raf=requestAnimationFrame(layout);};document.fonts.ready.then(schedule);addEventListener("resize",schedule);addEventListener("beforeprint",()=>{for(const math of document.querySelectorAll('math[display="block"]'))if(saved.has(math))math.innerHTML=saved.get(math);});addEventListener("afterprint",schedule);window.MathLayout={layout,schedule};
})();
