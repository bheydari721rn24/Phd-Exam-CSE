from pathlib import Path
R=Path(__file__).resolve().parent.parent;p=R/'dist/chapters/semantic-diagrams.js';s=p.read_text()
needle='function gridEnumeration(p,g,f){const id=p.scene.id,s=f.snapshot||{};'
if 'return axiomsQuestion(p,g,f)' not in s:
 assert s.count(needle)==1;s=s.replace(needle,needle+'if(id.startsWith("axioms-question-"))return axiomsQuestion(p,g,f);')
code=r'''function axiomsQuestion(p,g,f){
 const s=f.snapshot,id=p.scene.id;
 if(id.includes("atoms")){
  text(g,380,24,`Triple mass t = ${s.t}; binary labels identify A, B and C membership`,18);
  ["111","110","101","011","100","010","001","000"].forEach((label,i)=>{
   const x=50+(i%4)*175,y=80+Math.floor(i/4)*125,q=num(s.masses[i]);
   rect(g,x,y,135,75,q<0?"#f4d3dc":q===0?"#f1f4f6":"#d9ecdf",q<0?C.red:C.ink);
   text(g,x+67.5,y-20,label,19);nativeFormula(g,{formulaHtml:s.massMath[i]},x+10,y+18,115,45);
  });
  text(g,380,313,s.valid?"All masses are nonnegative: a valid atomic law":"Negative mass: this candidate law is impossible",19,"middle",s.valid?C.green:C.red);
  text(g,380,338,"The total is one; nonnegativity must also be checked.",17);return;
 }
 if(id==="axioms-question-urn"){
  text(g,380,28,["Original ten equally likely pairs","Condition: at least one red","Renormalize the nine retained pairs","Target: three red-red pairs"][s.stage],20);
  s.pairs.forEach((pair,i)=>{const x=45+(i%5)*137,y=80+Math.floor(i/5)*122,kept=s.stage===0||s.kept[i];
   rect(g,x,y,115,78,!kept?"#f1f4f6":s.target[i]?"#d1e8d9":"#dcebf5");
   text(g,x+57.5,y-20,pair.join(", "),18);nativeFormula(g,{formulaHtml:s.massMath[i]},x+7,y+20,101,45);
  });text(g,380,337,s.stage===0?"Original mass per pair: 1/10":s.stage===1?"Retained original mass: 9/10; normalize next":"Conditional target: 3 of 9 retained pairs",18);return;
 }
 const report=id==="axioms-question-report",counts=s.counts;
 text(g,380,28,report?"Eight equally likely sequences; group sizes 1, 3, 3, 1":"64 equally likely ordered outcomes; count each category exactly",18);
 path(g,"M75 270H705",C.ink,2);
 counts.forEach((q,i)=>{const x=report?105+155*i:125+190*i,h=report?45*q:4*q,w=report?95:110;
  rect(g,x,270-h,w,h,report?(i===s.active?"#f4d795":"#bad4e3"):(s.stage>0&&i>0?"#b7dac5":"#bad4e3"));
  text(g,x+w/2,256-h,q,21);text(g,x+w/2,301,report?`K=${i}`:["All distinct","One repeated pair","All equal"][i],17);
 });text(g,380,338,report?`Active K=${s.active}; probability ${s.counts[s.active]}/8`:["24+36+4 = 64 outcomes","Exact repetition: 36+4 = 40 outcomes","Pair-equality bound: 36+3×4 = 48 counts"][s.stage],18);
}

'''
if 'function axiomsQuestion(' not in s:s=s.replace('function loopQuestion(',code+'function loopQuestion(',1)
else:
 a=s.index('function axiomsQuestion(');z=s.index('function loopQuestion(',a);s=s[:a]+code+s[z:]
p.write_text(s,encoding='utf-8')
