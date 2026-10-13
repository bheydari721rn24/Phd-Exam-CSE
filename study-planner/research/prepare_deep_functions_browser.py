from pathlib import Path
B=Path(__file__).parent;s=(B/'qa_final_relations_browser.py').read_text().replace('deep-relations-browser','deep-functions-browser').replace('d_relations','d_functions')
s=s.replace("['questions']==45","['questions']==47").replace("['solutions']==45","['solutions']==47").replace("['tutorials']==46","['tutorials']==42")
s=s.replace("len(report['models'])==49","len(report['models'])==48").replace("len(report['frameRendering'])==235","len(report['frameRendering'])==758")
s=s.replace("len(report['controls'])==44","len(report['controls'])==46").replace("len(report['playback'])==44","len(report['playback'])==46").replace('range(0,44,5)','range(0,46,5)').replace("len(report['selection'])==9","len(report['selection'])==4")
s=s.replace('checks.push(c.api.index===2)','checks.push(c.api.index===Math.min(2,c.api.model.frames.length-1))').replace('checks.push(c.api.index===1)','checks.push(c.api.index===Math.max(0,Math.min(2,c.api.model.frames.length-1)-1))')
s=s.replace('for n in[1,2,3,4,5,6,7,8,9,10,11,12,13,16,17,20,24,28,32,36,37,40,44,45]:','for n in[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,22,23,26,30,31,34,35,38,39,42,43,46,47]:')
a=s.index(" report['relationLab']=");z=s.index(" for i in range(len(report['staticDiagrams'])):",a)
lab=r'''
 report['functionLab']=[]
 for name,expected in [('bijection','Bijective'),('onto','Onto; not injective'),('injection','Injective; not onto')]:
  js('document.getElementById("preset-'+name+'").click()')
  row=js('({classification:document.querySelector("#function-output strong").textContent,values:[...document.querySelectorAll("#function-input select")].map(x=>Number(x.value)),targetSize:Number(document.getElementById("target-size").value),selected:[...document.querySelectorAll("#function-input input")].filter(x=>x.checked).map(x=>Number(x.dataset.select))})');assert row['classification']==expected,row;report['functionLab'].append(row)
 row=js('(()=>{const n=document.getElementById("target-size");n.value="3";n.dispatchEvent(new Event("change"));return{values:[...document.querySelectorAll("#function-input select")].map(x=>Number(x.value)),classification:document.querySelector("#function-output strong").textContent};})()');assert row['values']==[0,1,2,2]and row['classification']=='Onto; not injective',row;report['functionLab'].append(row)
 row=js('(()=>{for(let i=0;i<4;i++){const x=document.querySelectorAll("#function-input select")[i];x.value="1";x.dispatchEvent(new Event("change"));}return{values:[...document.querySelectorAll("#function-input select")].map(x=>Number(x.value)),classification:document.querySelector("#function-output strong").textContent};})()');assert row['values']==[1,1,1,1]and row['classification']=='Neither injective nor onto',row;report['functionLab'].append(row)
 row=js('(()=>{const x=document.querySelectorAll("#function-input input")[3];x.checked=true;x.dispatchEvent(new Event("change"));const values=[1,1,1,1],r=analyzeFiniteFunction(values,3,[0,3]);return{image:r.image,saturation:r.saturation,selected:[...document.querySelectorAll("#function-input input")].filter(x=>x.checked).map(x=>Number(x.dataset.select))};})()');assert row['selected']==[0,3]and row['image']==[1]and row['saturation']==[0,1,2,3],row;report['functionLab'].append(row)
 report['invalidLab']=js('(()=>{const cases=[[[0],0],[[-1],3],[[1.2],3],[[], -1],[[0],1,[1]]];return cases.map(args=>{try{analyzeFiniteFunction(...args);return false;}catch{return true;}});})()');assert all(report['invalidLab'])
 js('document.getElementById("preset-bijection").click()')
'''
s=s[:a]+lab+s[z:];s=s.replace('data-relations-static-index','data-functions-static-index').replace('for n in[4,6,7,8,9,10]:','for n in[1,2,3,4,5,6,7,8,9,10]:')
s=s.replace("report['print']=js(","report['print']=js(")
(B/'qa_final_functions_browser.py').write_text(s,encoding='utf-8')
