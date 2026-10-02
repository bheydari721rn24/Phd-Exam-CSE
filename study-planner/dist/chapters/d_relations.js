/* A finite explanatory relation model. Rows are sources; columns are targets. */
(function(){
"use strict";
const names=["a","b","c","d"],n=names.length;
const copy=m=>m.map(row=>row.slice());
function closure(input,identity=false){
 const d=copy(input);if(identity)for(let i=0;i<n;i++)d[i][i]=true;
 for(let k=0;k<n;k++)for(let i=0;i<n;i++)for(let j=0;j<n;j++)d[i][j]=d[i][j]||(d[i][k]&&d[k][j]);
 return d;
}
function equivalence(input){return closure(input.map((row,i)=>row.map((x,j)=>x||input[j][i])),true);}
function properties(m){
 const r=[];let missingLoop=null,loop=null,sym=null,anti=null,asym=null,trans=null,serial=null;
 for(let i=0;i<n;i++){
  if(!m[i][i]&&missingLoop===null)missingLoop=i;
  if(m[i][i]&&loop===null)loop=i;
  if(!m[i].some(Boolean)&&serial===null)serial=i;
  for(let j=0;j<n;j++){
   if(m[i][j]&&!m[j][i]&&sym===null)sym=[i,j];
   if(i!==j&&m[i][j]&&m[j][i]&&anti===null)anti=[i,j];
   if(m[i][j]&&m[j][i]&&asym===null)asym=[i,j];
   for(let k=0;k<n;k++)if(m[i][j]&&m[j][k]&&!m[i][k]&&trans===null)trans=[i,j,k];
  }
 }
 const v=(label,witness,explain)=>r.push({label,holds:witness===null,witness,explain:witness===null?"Every required case holds on this four-element carrier.":explain});
 v("Reflexive",missingLoop,missingLoop===null?"":`${names[missingLoop]} lacks a loop.`);
 v("Irreflexive",loop,loop===null?"":`${names[loop]} has a loop.`);
 v("Symmetric",sym,sym?`${names[sym[0]]} relates to ${names[sym[1]]}, but the reverse edge is absent.`:"");
 v("Antisymmetric",anti,anti?`${names[anti[0]]} and ${names[anti[1]]} are distinct and relate in both directions.`:"");
 v("Asymmetric",asym,asym?`${names[asym[0]]} and ${names[asym[1]]} relate in both directions (a loop also violates asymmetry).`:"");
 v("Transitive",trans,trans?`${names[trans[0]]} → ${names[trans[1]]} → ${names[trans[2]]}, but ${names[trans[0]]} → ${names[trans[2]]} is absent.`:"");
 v("Serial",serial,serial===null?"":`${names[serial]} has no outgoing edge.`);
 return r;
}
// Exposed pure functions let the independent verifier compare the browser model with a set-based oracle.
window.relationModel={closure,equivalence,properties};
let input,stage,k,added=[];
const byId=id=>document.getElementById(id);
function matrix(m,editable=false,highlights=[]){
 const hs=new Set(highlights.map(([i,j])=>i+","+j));
 return '<table><caption>Source rows and target columns</caption><thead><tr><th scope="col">From / to</th>'+names.map(x=>`<th scope="col"><span class="math-inline">${x}</span></th>`).join("")+'</tr></thead><tbody>'+m.map((row,i)=>`<tr><th scope="row"><span class="math-inline">${names[i]}</span></th>`+row.map((v,j)=>`<td class="${hs.has(i+","+j)?"new-pair":""}">${editable?`<button type="button" data-row="${i}" data-col="${j}" aria-label="Pair ${names[i]} to ${names[j]}" aria-pressed="${v}">${Number(v)}</button>`:`<span class="math-inline">${Number(v)}</span>`}</td>`).join("")+'</tr>').join("")+'</tbody></table>';
}
function resetStage(){stage=copy(input);k=0;added=[];}
function showStage(){
 const allowed=k?names.slice(0,k).join(", "):"none";
 byId("lab-stage").textContent=`Stage ${k} of ${n}. Permitted internal vertices: ${allowed}. Green entries were added at the last stage. ${k===n?"All internal vertices are permitted; this is positive-length closure.":"The matrix records paths using only the permitted internal vertices."}`;
 byId("lab-stage-matrix").innerHTML=matrix(stage,false,added);
 byId("lab-next").disabled=k===n;
}
function render(){
 byId("lab-input").innerHTML=matrix(input,true);
 byId("lab-input").querySelectorAll("button").forEach(b=>b.onclick=()=>{const i=Number(b.dataset.row),j=Number(b.dataset.col);input[i][j]=!input[i][j];resetStage();render();});
 byId("lab-properties").innerHTML='<table><thead><tr><th>Property</th><th>Result</th><th>Reason or failure witness</th></tr></thead><tbody>'+properties(input).map(p=>`<tr><th scope="row">${p.label}</th><td>${p.holds?"Holds":"Fails"}</td><td>${p.explain.replace(/\b([abcd])\b/g,'<span class="math-inline">$1</span>').replace(/→/g,'<span class="math-inline">→</span>')}</td></tr>`).join("")+'</tbody></table>';
 const eq=equivalence(input),cases=[["Positive-length closure",closure(input)],["Reflexive transitive closure",closure(input,true)],["Equivalence closure",eq]];
 byId("lab-closures").innerHTML='<div class="closure-grid">'+cases.map(([label,m])=>`<div><p class="matrix-name">${label}</p>${matrix(m)}</div>`).join("")+'</div>';
 const seen=new Set(),blocks=[];for(let i=0;i<n;i++)if(!seen.has(i)){const b=names.filter((_,j)=>eq[i][j]);for(let j=0;j<n;j++)if(eq[i][j])seen.add(j);blocks.push("{"+b.join(", ")+"}");}
 byId("lab-components").innerHTML='Equivalence classes: <span class="math-inline">'+blocks.join("; ")+'</span>. These use edges in either direction.';
 showStage();
}
function load(edges){input=Array.from({length:n},()=>Array(n).fill(false));for(const [i,j]of edges)input[i][j]=true;resetStage();render();}
byId("lab-chain").onclick=()=>load([[0,1],[1,2],[2,3]]);
byId("lab-cycle").onclick=()=>load([[0,1],[1,2],[2,0]]);
byId("lab-empty").onclick=()=>load([]);
byId("lab-next").onclick=()=>{if(k===n)return;const old=copy(stage);added=[];for(let i=0;i<n;i++)for(let j=0;j<n;j++){stage[i][j]=old[i][j]||(old[i][k]&&old[k][j]);if(stage[i][j]&&!old[i][j])added.push([i,j]);}k++;showStage();};
load([[0,1],[1,2],[2,3]]);
})();
