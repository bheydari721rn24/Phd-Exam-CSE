from pathlib import Path
import re
R=Path(__file__).resolve().parents[1]
p=R/'dist/chapters/advanced-simulations.js';s=p.read_text(encoding='utf-8')
a="Math.max(14,18*available/b.width)";assert a in s;s=s.replace(a,"Math.max(10,parseFloat(getComputedStyle(t).fontSize)*available/b.width)")
marker=" function pairGeometry(before,after,model)"
# Final font fitting must not enlarge a label after its padding was measured.
# Recenter a single short empty-slot label if fractional glyph metrics reduce its inset.
fix="""  function insetEmptyLabels(svg){for(const t of svg.querySelectorAll('text[data-layout-label-for]')){if(t.textContent!=='empty')continue;const shape=[...svg.querySelectorAll('rect[data-layout-box]')].find(n=>n.dataset.layoutBox===t.dataset.layoutLabelFor);if(!shape)continue;const a=DiagramLayout.box(svg,t),b=DiagramLayout.box(svg,shape);if(Math.min(a.x-b.x,b.x+b.w-a.x-a.w)>=8)continue;const dx=b.x+b.w/2-a.x-a.w/2,m=svg.getScreenCTM().inverse().multiply(t.getScreenCTM()).inverse(),o=new DOMPoint(0,0).matrixTransform(m),d=new DOMPoint(dx,0).matrixTransform(m);t.setAttribute('x',Number(t.getAttribute('x')??0)+d.x-o.x);}}
"""
assert marker in s;s=s.replace(marker,fix+marker)
# Run once while connected in the measurement container, then keep cache immutable.
s=s.replace("host.append(measuring);fit(svg);svg.remove();","host.append(measuring);fit(svg);insetEmptyLabels(svg);svg.remove();")
s=s.replace("clock=probe.animate([{opacity:0},{opacity:0}],{duration:900,fill:'forwards'});", "clock=probe.animate([{opacity:0},{opacity:0}],{duration:900,fill:'forwards'});clock.playbackRate=2200/Number(speed.value);")
s=s.replace("speed.onchange=()=>{if(running)", "speed.onchange=()=>{clock?.updatePlaybackRate(2200/Number(speed.value));if(running)")
p.write_text(s,encoding='utf-8')
assert "w=850/Math.max(1,a.length);let b=slots(a,135,{label:'Retained half-open interval ['+l+', '+r+')'" in s
s=s.replace("w=850/Math.max(1,a.length);let b=slots(a,135,{label:'Retained half-open interval ['+l+', '+r+')'","w=Math.min(116,850/Math.max(1,a.length));let b=tx(500,40,'Retained half-open interval ['+l+', '+r+')')+slots(a,135,{label:''")
s=s.replace("tx(500,y-30,row==='source'?", "tx(500,y-54,row==='source'?")
p.write_text(s,encoding='utf-8')
names='advanced-simulations|concept-unified|problem-visuals|semantic-diagrams'
pattern=re.compile(r'('+names+r')\.(js|css)\?[^\"\s<>]+')
for p in list((R/'dist/chapters').glob('*.html'))+list((R/'research').glob('render_*.py')):
 before=p.read_text(encoding='utf-8');after=pattern.sub(r'\1.\2?player-behavior-2',before)
 if after!=before:p.write_text(after,encoding='utf-8')
print('Font fitting monotonic, empty-slot insets centered, speed changes affect movement, browser cache refreshed.')
