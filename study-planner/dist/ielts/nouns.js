"use strict";
(()=>{
 const form=document.getElementById('reference-form');
 const nouns={folder:{plural:'folders',article:'a'},apple:{plural:'apples',article:'an'},'university card':{plural:'university cards',article:'a'}};
 function update(){
  const n=nouns[form.elements.noun.value],many=form.elements.number.value==='many',ref=form.elements.reference.value;
  const determiner=ref==='known'?'the':ref==='near'?(many?'these':'this'):(many?'some':n.article);
  const noun=many?n.plural:form.elements.noun.value;
  const sentence=determiner[0].toUpperCase()+determiner.slice(1)+' '+noun+' '+(many?'are':'is')+' ready.';
  document.getElementById('reference-sentence').textContent=sentence;
  document.getElementById('reference-reason').textContent=(ref==='known'?'Context: the speaker and listener have already identified the intended object or group.':ref==='near'?'Context: the speaker points to the nearby object or objects.':'Context: one unidentified object, or an unspecified group, is introduced.')+' '+(many?'The plural main noun requires are.':'The singular main noun requires is.')+(ref==='new'&&!many?' The choice of a/an follows the first sound of '+form.elements.noun.value+'.':'');
 }
 form.addEventListener('submit',e=>{e.preventDefault();update();});form.addEventListener('change',update);update();
})();
