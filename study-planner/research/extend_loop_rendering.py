from pathlib import Path
R=Path(__file__).resolve().parent.parent;p=R/'dist/chapters/semantic-diagrams.js';s=p.read_text()
needle='function gridEnumeration(p,g,f){const id=p.scene.id,s=f.snapshot||{};'
if 'return loopQuestion(p,g,f)' not in s:
    assert s.count(needle)==1;s=s.replace(needle,needle+'if(id.startsWith("loop-question-"))return loopQuestion(p,g,f);')
code=r'''function loopQuestion(p,g,f){
 const s=f.snapshot,id=p.scene.id;
 if(id==="loop-question-minimum"){
  text(g,380,34,"One comparison per key; assignments only on a true test",18);
  s.values.forEach((v,j)=>{const x=100+j*72;rect(g,x,80,58,55,j+1===s.i?"#ffe1a2":j+1<s.i?"#cce6d7":"#eef3f6");text(g,x+29,115,v,24);text(g,x+29,159,j+1,17);});
  text(g,380,197,`Position ${s.i}: compare ${s.key} with ${s.before}`,19);
  text(g,380,238,s.update?"True: assign this key as the new minimum":"False: preserve the established minimum",20,"middle",s.update?C.green:C.red);
  text(g,380,282,`Minimum now ${s.after}; comparisons ${s.comparisons}; updates ${s.updates}`,20);
  text(g,380,335,"The initial minimum is positive infinity; no array entry is skipped.",17);return;
 }
 const parity=id==="loop-question-parity";
 text(g,380,22,parity?"Rows: i; columns: j; keep i+j even inside j ≤ i":`Fixed i=${s.i}; rows: j; columns: k; keep i*j*k ≤ ${s.n}`,18);
 for(let row=1;row<=8;row++){
  text(g,130,79+(row-1)*28,row,17);
  for(let col=1;col<=8;col++){
   const valid=parity?col<=row: s.i*row*col<=s.n;
   const visited=!parity||row<=s.i,keep=valid&&(!parity||(row+col)%2===0);
   const x=165+(col-1)*52,y=60+(row-1)*28;
   rect(g,x,y,43,26,visited&&keep?"#b5d9c3":visited&&valid?"#f1d6dd":"#f3f5f7",parity&&row===s.i?C.amber:"#bdcfd8");
   if(visited&&valid&&!keep)text(g,x+21.5,y+19,"×",17,"middle",C.red);
  }
 }
 for(let col=1;col<=8;col++)text(g,186.5+(col-1)*52,312,col,17);
 text(g,380,338,parity?`Active row ${s.i}: ${s.rowCount} bodies; cumulative ${s.total}`:`Layer i=${s.i}: ${s.layerCount} triples; cumulative ${s.total}`,18);
}

'''
if 'function loopQuestion(' not in s:s=s.replace('function asymPlot(',code+'function asymPlot(',1)
else:
    a=s.index('function loopQuestion(');z=s.index('function asymPlot(',a);s=s[:a]+code+s[z:]
p.write_text(s,encoding='utf-8')
