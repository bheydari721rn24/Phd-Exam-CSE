from pathlib import Path
B=Path(__file__).parent;s=(B/'qa_final_invariants_browser.py').read_text();prefix=s[:s.index(" report['counts']=")]
tail=r'''
 report=json.loads((R/'research/deep-library-revision/d_invariants-browser.json').read_text())
 report['finalStaticArrows']=js(r"(()=>[...document.querySelectorAll('figure svg')].map(svg=>{const shapes=[...svg.querySelectorAll('circle,rect')],distance=(x,y)=>Math.min(...shapes.map(e=>{if(e.tagName==='circle')return Math.abs(Math.hypot(x-+e.getAttribute('cx'),y-+e.getAttribute('cy'))-+e.getAttribute('r'));const X=+e.getAttribute('x'),Y=+e.getAttribute('y'),w=+e.getAttribute('width'),h=+e.getAttribute('height');return Math.hypot(Math.max(X-x,x-X-w,0),Math.max(Y-y,y-Y-h,0))||Math.min(Math.abs(x-X),Math.abs(x-X-w),Math.abs(y-Y),Math.abs(y-Y-h));}));for(const e of svg.querySelectorAll('[marker-end]')){const id=e.getAttribute('marker-end').match(/url\(#([^)]*)\)/)[1];if(![...svg.querySelectorAll('marker')].some(m=>m.id===id))throw Error('Unresolved marker');}return{ports:[...svg.querySelectorAll('[data-static-ports]')].map(e=>[distance(+e.getAttribute('x1'),+e.getAttribute('y1')),distance(+e.getAttribute('x2'),+e.getAttribute('y2'))]),reset:[...svg.querySelectorAll('[data-attached-reset]')].map(e=>[distance(612.5,119),distance(262.5,213)])};}))()")
 assert len(report['finalStaticArrows'])==4 and sum(len(v['ports'])for v in report['finalStaticArrows'])==21
 assert all(max(p)<.001 for v in report['finalStaticArrows']for p in v['ports']+v['reset']) and sum(len(v['reset'])for v in report['finalStaticArrows'])==1
 report['finalMathCaptionPlayback']=[]
 for selector,name in[('.exam-question[data-deep-index="1"] .concept-animation','question-1-final.png'),('#animation-accumulators','flat-acc-playback.png')]:
  row=js('(async()=>{const h=document.querySelector('+json.dumps(selector)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host)),w=c.api.host;c.api.show(0);const play=w.querySelector("[data-play]"),speed=w.querySelector("[data-speed]");speed.value="1400";speed.dispatchEvent(new Event("change"));play.click();await new Promise(r=>setTimeout(r,1550));play.click();const i=c.api.index;await new Promise(r=>setTimeout(r,150));return{id:c.scene.id,advanced:i>0,paused:c.api.index===i,mathCaption:!!w.querySelector(".sim-operation math")};})()');assert row['advanced']and row['paused']and row['mathCaption'];report['finalMathCaptionPlayback'].append(row)
  js('(()=>{const h=document.querySelector('+json.dumps(selector)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host));c.api.show(c.api.model.frames.length-1);})()');capture(selector,name)
 for i in range(4):
  js('[...document.querySelectorAll("figure svg")]['+str(i)+'].closest("figure").setAttribute("data-final-static","'+str(i)+'")');capture('[data-final-static="'+str(i)+'"]',f'static-{i+1}.png')
 report['inlineFormulaWrapping']=js('(()=>{const span=[...document.querySelectorAll(".lesson .math-inline")].find(x=>x.textContent.includes("B")&&x.textContent.includes("y")&&x.textContent.includes("x"));return{whiteSpace:getComputedStyle(span).whiteSpace,display:getComputedStyle(span).display,overflowX:getComputedStyle(span).overflowX};})()');assert report['inlineFormulaWrapping']['whiteSpace']=='nowrap'
 report['finalVisualRepair']='Fractions use native mathematical notation; concatenation markers do not stretch. The static lexicographic diagram now has state boxes, 21 attached straight arrows across the four figures, an attached curved reset and an explicit positive-M branch/zero-M exit qualification. Inline formulas retain one line inside a bounded scrollable span.'
 report['status']='passed_pending_screenshot_inspection'
finally:
 (R/'research/deep-library-revision/d_invariants-browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');proc.terminate()
print(report['status'])
'''
(B/'qa_invariants_final_visual.py').write_text(prefix+tail,encoding='utf-8')
