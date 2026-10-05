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
function layout(){
 for(const math of document.querySelectorAll('math[display="block"]')){
  const source=math.textContent;removeGeneratedWraps(math);delete math.dataset.semanticWrap;
  if(math.textContent!==source)throw Error("Mathematical tokens changed during layout");
  if(math.closest('.formula-block'))math.dataset.layout="single-line";
 }
 for(const box of document.querySelectorAll('.formula-block'))box.dataset.scrollable=String(box.scrollWidth>box.clientWidth+2);
}
let raf;const schedule=()=>{cancelAnimationFrame(raf);raf=requestAnimationFrame(layout);};
document.fonts.ready.then(schedule);addEventListener("resize",schedule);addEventListener("beforeprint",layout);addEventListener("afterprint",schedule);
window.MathLayout={layout,schedule};
})();
