from pathlib import Path
B=Path(__file__).parent;s=(B/'qa_final_functions_browser.py').read_text();prefix=s[:s.index(" report['counts']=")]
probe=r'''
 for selector,name in[('#animation-fibers','fibers'),('.exam-question[data-deep-index="15"] .concept-animation','injection')]:
  js('(()=>{const h=document.querySelector('+json.dumps(selector)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host));c.api.show(c.api.model.frames.length-1);})()');capture(selector,'inspection-'+name+'.png')
  print(js('(()=>{const h=document.querySelector('+json.dumps(selector)+'),svg=h.querySelector(".sim-stage svg");return [...svg.querySelectorAll("text")].map(t=>({text:t.textContent,x:t.getAttribute("x"),y:t.getAttribute("y"),box:DiagramLayout.box(svg,t),size:getComputedStyle(t).fontSize,style:t.getAttribute("style"),transform:t.getAttribute("transform")}));})()'),flush=True)
finally:
 proc.terminate()
'''
(B/'inspect_functions_layout_run.py').write_text(prefix+probe,encoding='utf-8')
