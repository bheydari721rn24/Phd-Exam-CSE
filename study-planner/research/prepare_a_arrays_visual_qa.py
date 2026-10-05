"""Extend the actual-browser audit with edge attachment and text padding checks."""
from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_a_arrays_browser.py').read_text().replace('a-arrays-qa','a-arrays-visual-qa').replace('-v1.png','-v2.png')
# Avoid nested literal quoting in this generator by reading the JS independently.
jsfile=B/'a_arrays-diagram-check.js'
init="    js("+repr(jsfile.read_text())+")\n"
s=s.replace("    for id in ids:\n",init+"    for id in ids:\n",1)
s=s.replace("const ts=[...h.querySelectorAll('.arrays-stage svg text')];","const svg=h.querySelector('.arrays-stage svg');bad.push(...checkDiagram(svg).map(z=>({{...z,checkpoint:k+1}})));const ts=[...svg.querySelectorAll('text')];")
s=s.replace('x.y+x.height>411','x.y+x.height>svg.viewBox.baseVal.height+1')
s=s.replace("    refs=json.loads(","    report['diagramContracts']='All 113 fixed checkpoints: exact edge ports, >=8 horizontal and >=6 vertical label padding, >=14 exterior clearance.'\n    refs=json.loads(",1)
extra=r'''
    report['labLayoutChecks']=js('(()=>{const rows='+json.dumps(refs)+';const holder=document.createElement("div");document.body.append(holder);const bad=[];let frames=0;for(const r of rows){const z=ArrayLab.evaluate(r.mode,r.params);if(z.mode==="growth")continue;for(const f of z.states){holder.innerHTML=ArrayLab.picture(z,f);for(const e of checkDiagram(holder.querySelector("svg")))bad.push({mode:r.mode,params:r.params,...e});frames++;}}holder.remove();return {frames,bad};})()')
    assert not report['labLayoutChecks']['bad'],report['labLayoutChecks']
    js('document.querySelector(\'[data-arrays-model="dll"] [data-reset]\').click()');time.sleep(.6);js('document.querySelector(\'[data-arrays-model="dll"] [data-next]\').click()')
    report['movingEdgeChecks']=[]
    for pause in [.08,.12,.15,.2]:
        time.sleep(pause)
        result=js('(()=>{const svg=document.querySelector(\'[data-arrays-model="dll"] svg\'),boxes=new Map([...svg.querySelectorAll("[data-box]")].map(r=>[r.dataset.box,r.getBoundingClientRect()])),bad=[];for(const p of svg.querySelectorAll("[data-arrow]")){for(const [end,key] of [[0,"source"],[p.getTotalLength(),"target"]]){const v=p.getPointAtLength(end),q=new DOMPoint(v.x,v.y).matrixTransform(p.getScreenCTM()),b=boxes.get(p.dataset[key]),gap=Math.min(Math.abs(q.x-b.left),Math.abs(q.x-b.right),Math.abs(q.y-b.top),Math.abs(q.y-b.bottom));if(gap>2)bad.push({edge:p.dataset.source+" → "+p.dataset.target,gap});}}return bad;})()')
        report['movingEdgeChecks'].append(result)
    assert not any(report['movingEdgeChecks']),report['movingEdgeChecks']
'''
s=s.replace("    report['labForms']=[]",extra+"    report['labForms']=[]",1)
s=s.replace("(ROOT/'research/a_arrays-browser-audit.json')","(ROOT/'research/a_arrays-visual-browser-audit.json')")
(B/'qa_a_arrays_visual_browser.py').write_text(s,encoding='utf-8')
