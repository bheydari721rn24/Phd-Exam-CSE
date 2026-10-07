/* One complete equation per line. Matrices and cases retain their real rows. */
"use strict";
(() => {
const NS="http://www.w3.org/1998/Math/MathML";
const M=tag=>document.createElementNS(NS,tag);
function removeGeneratedWraps(math){
 for(const table of [...math.querySelectorAll('mtable[columnalign="left"][displaystyle="true"]')].reverse()){
  if(![".5em",".55em"].includes(table.getAttribute("rowspacing")))continue;
  const rows=[...table.children];
  if(!rows.length||rows.some(r=>r.localName!=="mtr"||r.children.length!==1||r.firstElementChild.localName!=="mtd"))continue;
  const row=M("mrow");for(const r of rows)row.append(...r.firstElementChild.childNodes);table.replaceWith(row);
 }
}
/* A script belongs to the fenced expression, never just its closing glyph. */
const OPEN="([{⌈⌊⟨",CLOSE=")]}⌉⌋⟩",SCRIPTS=new Set(["msup","msub","msubsup","mover","munder","munderover"]);
function groupFences(math){
 const rows=[math,...math.querySelectorAll("mrow,mtd")].reverse();
 for(const row of rows){
  const children=[...row.children],stack=[];
  for(let i=0;i<children.length;i++){
   const item=children[i],script=SCRIPTS.has(item.localName),token=script?item.firstElementChild:item;
   const s=token?.localName==="mo"?token.textContent:null;
   if(s&&OPEN.includes(s)&&!script)stack.push([i,s]);
   else if(s&&CLOSE.includes(s)&&stack.length){
    const [start,opening]=stack.at(-1);
    if(CLOSE[OPEN.indexOf(opening)]!==s&&!("([".includes(opening)&&")]".includes(s)))continue;
    stack.pop();
    if(start===0&&i===children.length-1&&!script)continue;
    const group=M("mrow");for(const e of children.slice(start,i))group.append(e);
    let replacement;
    if(script){group.append(token);item.prepend(group);replacement=item;}else{group.append(item);replacement=group;}
    children.splice(start,i-start+1,replacement);i=start;
   }
  }
  if(children.length!==row.children.length||children.some((e,i)=>e!==row.children[i]))row.replaceChildren(...children);
 }
}
function layout(){
 observer.disconnect();
 try{
 for(const math of document.querySelectorAll('math')){
  const source=math.textContent;removeGeneratedWraps(math);groupFences(math);delete math.dataset.semanticWrap;
  if(math.textContent!==source)throw Error("Mathematical tokens changed during layout");
  if(math.closest('.formula-block'))math.dataset.layout="single-line";
 }
 for(const box of document.querySelectorAll('.formula-block'))box.dataset.scrollable=String(box.scrollWidth>box.clientWidth+2);
 }finally{observer.observe(document.body,{childList:true,subtree:true});}
}
let raf;const schedule=()=>{cancelAnimationFrame(raf);raf=requestAnimationFrame(layout);};
const observer=new MutationObserver(records=>{
 if(records.some(r=>r.target.closest?.('math')||[...r.addedNodes].some(n=>n.nodeType===1&&(n.localName==='math'||n.querySelector('math')))))schedule();
});
observer.observe(document.body,{childList:true,subtree:true});
document.fonts.ready.then(schedule);addEventListener("resize",schedule);addEventListener("beforeprint",layout);addEventListener("afterprint",schedule);
window.MathLayout={layout,schedule,groupFences};
})();
