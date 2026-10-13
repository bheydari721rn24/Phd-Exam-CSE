from pathlib import Path
B=Path(__file__).parent;s=(B/'qa_final_discrete_number_browser.py').read_text();s=s[:s.index(" report['counts']=")]
s+=r'''
 c=js('(()=>{const c=ConceptAnimations.players.find(c=>c.scene.id==="discrete-number-question-adjacent-8");c.api.show(c.api.model.frames.length-1);c.api.host.setAttribute("data-geometry","true");const svg=c.api.host.querySelector("svg");return{math:[...svg.querySelectorAll("foreignObject")].map(m=>({attributes:[...m.attributes].map(a=>[a.name,a.value]),rect:m.getBoundingClientRect().toJSON(),math:m.querySelector("math")?.getBoundingClientRect().toJSON()})),texts:[...svg.querySelectorAll("text")].map(t=>({text:t.textContent,y:t.getAttribute("y"),x:t.getAttribute("x"),rect:t.getBoundingClientRect().toJSON()}))}})()');print(c);capture('[data-geometry]','adjacent-eight-geometry.png')
finally:
 proc.terminate()
'''
(B/'qa_discrete_number_geometry.py').write_text(s,encoding='utf-8')
