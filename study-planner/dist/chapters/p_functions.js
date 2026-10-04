"use strict";
addEventListener("DOMContentLoaded",()=>{
 const form=document.getElementById("functions-form"),host=document.getElementById("functions-player"),out=document.getElementById("functions-output");
 let player;
 const node=(id,label,x,y,w=235)=>({id,label:String(label),x,y,w,h:55,tone:id==="token"?"active":"plain",kind:"card",size:21});
 function build(mode,u){
  const states=[];const put=(caller,callee,shared,value,x,caption,extra={})=>states.push({caller,callee,shared,value,x,caption,...extra});
  if(mode==="copy"){
   put(u,null,null,u,160,"Evaluate the caller object to produce its argument value. The caller object remains separate from the new parameter.");
   put(u,u,null,u,560,"Copy the argument into a new local parameter object. Subsequent scalar assignments affect this local object alone.");
   put(u,u+3,null,2*(u+3),560,"Add three to the local parameter and evaluate twice its new value. This prepares the returned result.");
   put(u,null,null,2*(u+3),160,"Copy the returned value into the caller result destination. The original caller object has not been changed.");
  }else if(mode==="pointer"){
   put(u,null,u,"&a",160,"Form the address of the caller object. The argument token represents this address rather than a scalar copy.");
   put(u,"p = &a",u,"&a",560,"Initialize a separate parameter pointer with the same address. Dereferencing it designates the live caller object.");
   put(2*u+3,"p = &a",2*u+3,2*u+3,360,"Write twice the target value plus three through the pointer. This changes the caller target, not the pointer identity.");
   put(2*u+3,null,2*u+3,"void",160,"End the void invocation while preserving the modified caller object. No integer return result is supplied.");
  }else if(mode==="alias"){
   put(u,"p = q = &a",u,u,360,"Bind both copied pointer parameters to one target. Sequential updates therefore act on one changing value.");
   put(u+2,"First statement complete",u+2,u+2,260,"Add two through the first pointer. The second alias now observes the updated value of the same object.");
   put(3*(u+2),"Second statement complete",3*(u+2),3*(u+2),460,"Triple the current value through the second pointer. This is three times the already incremented target.");
  }else if(mode==="static"){
   let s=0;
   for(let k=1;k<=3;k++){
    put(u,"fresh = 0",s,null,160,"Begin a fresh invocation with a new automatic object. The saved static object retains its previous value.",{call:k});
    s+=u;
    put(u,"fresh = 1",s,10+s,560,"Increment the automatic fresh object and add input to persistent saved state. Compute ten times fresh plus saved.",{call:k});
    put(u,null,s,10+s,160,"Return this call result and end its automatic objects. The saved static state remains for the next call.",{call:k});
   }
  }else{
   const first=3*u+1,second=3*first+1;
   put(u,null,null,u,160,"Enter the combine invocation and pause before its first helper call. The saved continuation needs the first result.");
   put(u,"first affine",null,first,560,"The first affine helper receives the original input and returns three times that input plus one.");
   put(u,"first saved",null,first,160,"Save the first returned result in the combine frame. This helper invocation ends before the second begins.");
   put(u,"second affine",null,second,560,"The second affine helper receives the saved first result. It is not called on the original input again.");
   put(u,null,null,first+second,160,"Resume combine after the second helper and add both saved results. This finishes the original continuation.");
  }
  const frames=states.map((s,i)=>({
   nodes:[node("caller","Caller a = "+s.caller,160,65),node("callee",s.callee===null?"Callee not active":s.callee,560,65),
    node("shared",s.shared===null?"No shared target":"Shared state = "+s.shared,360,180,320),node("token",s.value===null?"Result pending":s.value,s.x,290,160)],
   caption:s.caption,captionHtml:"<p>"+s.caption+"</p>",metrics:{"Checkpoint":i+1,"Input":u,...(s.call?{"Call":s.call}:{})},metricLabels:{Checkpoint:"Checkpoint",Input:"Input",Call:"Call"},formula:"",
   line:0,edges:[],snapshot:{mode,input:u,...s}
  }));
  return {id:"functions-custom-"+mode,title:form.elements.mode.selectedOptions[0].textContent,
   description:"Exact curated model with adjustable integer input. The value or address token moves while the caller object retains its identity.",
   descriptionHtml:"<p>Exact curated model with adjustable integer input. The value or address token moves while the caller object retains its identity.</p>",
   invariant:"Every checkpoint follows the stated passing model. All accepted inputs keep arithmetic safely inside every conforming C17 int.",
   invariantHtml:"<p>Every checkpoint follows the stated passing model. All accepted inputs keep arithmetic safely inside every conforming C17 int.</p>",
   frames,code:[]};
 }
 function run(e){
  e?.preventDefault();
  const raw=form.elements.input.value,mode=form.elements.mode.value;
  if(!/^-?\d+$/.test(raw)||Number(raw)<-20||Number(raw)>20){
   if(player)player.pause();out.dataset.valid="false";out.textContent="Enter an integer from -20 through 20.";host.hidden=true;return;
  }
  const scene=build(mode,Number(raw));
  host.hidden=false;host.dataset.loaded="true";
  if(player){player.pause();player.scenes=[scene];player.scene=scene;player.index=0;player.choice.options[0].textContent=scene.title;player.choice.value=0;player.show(0,false);}
  else player=ConceptAnimations.mount(host,[scene]);
  out.dataset.valid="true";out.dataset.mode=mode;out.dataset.states=JSON.stringify(scene.frames.map(f=>f.snapshot));
  out.textContent="Model begins paused. Use Next step to inspect parameter binding, local or shared updates, and return transfer.";
 }
 form.addEventListener("submit",run);form.addEventListener("input",run);form.addEventListener("change",run);run();
 document.querySelectorAll(".functions-diagram").forEach(fig=>{
  const b=document.createElement("button");b.type="button";b.className="functions-figure-toggle";b.textContent="Enlarge diagram";b.setAttribute("aria-expanded","false");
  b.addEventListener("click",()=>{const open=fig.classList.toggle("expanded");b.textContent=open?"Fit diagram to page":"Enlarge diagram";b.setAttribute("aria-expanded",String(open));});fig.prepend(b);
 });
});
