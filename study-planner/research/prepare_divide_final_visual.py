from pathlib import Path
B=Path(__file__).parent;s=(B/'qa_deep_divide_browser.py').read_text();a=s.index(" report['playerCount']=");z=s.index(' for n in[1,2,3,4,5',a)
s=s[:a]+''' report['playerCount']=js('ConceptAnimations.players.length')
 report['directedPorts']=js("""(()=>{const out=[];for(const c of ConceptAnimations.players){const old=c.scene;for(const scene of c.scenes){if(!scene.id.startsWith('divide-question-'))continue;c.scene=scene;c.show(0);for(let i=0;i<scene.frames.length;i++){c.api.show(i);const svg=c.api.host.querySelector('svg'),rects=[...svg.querySelectorAll('rect')].map(r=>r.getBBox());for(const p of svg.querySelectorAll('[data-divide-ports]')){const v=p.dataset.dividePorts.split(',').map(Number),near=(x,y)=>rects.some(r=>{const inside=x>=r.x-.02&&x<=r.x+r.width+.02&&y>=r.y-.02&&y<=r.y+r.height+.02;const border=Math.min(Math.abs(x-r.x),Math.abs(x-r.x-r.width),Math.abs(y-r.y),Math.abs(y-r.y-r.height))<.02;return inside&&border;}),marker=p.getAttribute('marker-end'),id=marker?.match(/#([^)]*)/)?.[1];out.push({scene:scene.id,frame:i,attached:near(v[0],v[1])&&near(v[2],v[3]),marker:!!id&&!!svg.querySelector('[id="'+id+'"]')});}}}c.scene=old;c.show(0);}return out;})()""")
 assert report['directedPorts']and all(r['attached']and r['marker']for r in report['directedPorts'])
'''+s[z:]
s=s.replace('deep-divide-browser','deep-divide-final-visual').replace('a_divide-browser.json','a_divide-final-visual.json')
(B/'qa_divide_final_visual.py').write_text(s,encoding='utf8')
