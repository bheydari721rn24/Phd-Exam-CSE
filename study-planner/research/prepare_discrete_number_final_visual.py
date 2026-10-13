from pathlib import Path
B=Path(__file__).parent;s=(B/'qa_final_discrete_number_browser.py').read_text();s=s[:s.index(" report['counts']=")]
s+=r'''
 report=json.loads((R/'research/deep-library-revision/d_number-browser.json').read_text());assert report['status'].startswith('passed')
 report['finalStaticPorts']=js(r"(()=>[...document.querySelectorAll('figure svg')].map(svg=>{const shapes=[...svg.querySelectorAll('circle,rect')],distance=(x,y)=>Math.min(...shapes.map(e=>{if(e.tagName==='circle')return Math.abs(Math.hypot(x-+e.getAttribute('cx'),y-+e.getAttribute('cy'))-+e.getAttribute('r'));const X=+e.getAttribute('x'),Y=+e.getAttribute('y'),w=+e.getAttribute('width'),h=+e.getAttribute('height');return Math.hypot(Math.max(X-x,x-X-w,0),Math.max(Y-y,y-Y-h,0))||Math.min(Math.abs(x-X),Math.abs(x-X-w),Math.abs(y-Y),Math.abs(y-Y-h));}));for(const e of svg.querySelectorAll('[marker-end]')){const id=e.getAttribute('marker-end').match(/url\(#([^)]*)\)/)[1];if(![...svg.querySelectorAll('marker')].some(m=>m.id===id))throw Error('Unresolved marker');}return{straight:[...svg.querySelectorAll('[data-static-ports]')].map(e=>[distance(+e.getAttribute('x1'),+e.getAttribute('y1')),distance(+e.getAttribute('x2'),+e.getAttribute('y2'))]),curves:[...svg.querySelectorAll('[data-static-path-ports]')].map(e=>{const a=e.dataset.staticPathPorts.split(',').map(Number);return[distance(a[0],a[1]),distance(a[2],a[3])];})};}))()")
 assert sum(len(v['straight'])for v in report['finalStaticPorts'])==9 and sum(len(v['curves'])for v in report['finalStaticPorts'])==2
 assert all(max(p)<.001 for v in report['finalStaticPorts']for p in v['straight']+v['curves'])
 sel='.exam-question[data-deep-index="19"] .concept-animation'
 report['finalAdjacentWindow']=js('(()=>{const h=document.querySelector('+json.dumps(sel)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host));c.api.show(2);const middle=c.api.host.textContent;c.api.show(3);return{middle:middle.includes("Rows 5–9"),final:c.api.host.textContent.includes("Rows 1–5"),answer:c.scene.frames[3].snapshot.answers[0],math:!!c.api.host.querySelector("math")}})()');assert report['finalAdjacentWindow']==dict(middle=True,final=True,answer=65,math=True);capture(sel,'question-19-final.png')
 report['finalInlineMath']=js('getComputedStyle(document.querySelector(".exam-solution .math-inline")).whiteSpace');assert report['finalInlineMath']=='nowrap'
 report['status']='passed';(R/'research/deep-library-revision/d_number-browser.json').write_text(json.dumps(report,indent=2)+'\n');print({'attachedStraightConnections':9,'attachedCurvedConnections':2,'CRTWindow':'checked','math':'nowrap'})
finally:
 proc.terminate()
'''
(B/'qa_discrete_number_final_visual.py').write_text(s,encoding='utf-8')
