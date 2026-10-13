from pathlib import Path
B=Path(__file__).parent;s=(B/'qa_discrete_number_final_visual.py').read_text();a=s.index(" report['status']='passed';")
s=s[:a]+r'''
 for i in [0,3]:
  js('[...document.querySelectorAll("figure svg")]['+str(i)+'].closest("figure").setAttribute("data-final-static","'+str(i)+'")');capture('[data-final-static="'+str(i)+'"]','static-'+str(i+1)+'-delivery.png')
 sel='.exam-question[data-deep-index="8"] .concept-animation';js('(()=>{const h=document.querySelector('+json.dumps(sel)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host));c.api.show(c.api.model.frames.length-1)})()');capture(sel,'question-8-delivery.png')
 report['finalHeaderAndReferences']=js('({header:document.querySelector(".hero").textContent,toc:document.querySelector(".toc").textContent,berkeley:document.querySelector("#references").nextElementSibling.textContent})');assert '36 detailed examination decisions' in report['finalHeaderAndReferences']['header'] and 'Fall 2026' in report['finalHeaderAndReferences']['berkeley']
 report['status']='passed';(R/'research/deep-library-revision/d_number-browser.json').write_text(json.dumps(report,indent=2)+'\n');print({'staticPorts':'passed','headerAndReferences':'passed','finalImages':'captured'})
finally:
 proc.terminate()
'''
(B/'qa_discrete_number_delivery_visual.py').write_text(s,encoding='utf-8')
