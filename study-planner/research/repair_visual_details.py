"""Deterministic follow-up fixes from semantic and rendered-state review."""
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'dist/chapters/semantic-diagrams.js'
s=p.read_text(encoding='utf-8')
replacements={
'text(g,(lo+hi)/2,78,':'text(g,Math.max(145,Math.min(615,(lo+hi)/2)),78,',
'max=Math.max(1,...all.map(Math.abs));path(g,"M45 270H715",C.ink);':'max=Math.max(1,...all.map(Math.abs)),baseline=all.some(v=>v<0)?180:270;path(g,`M45 ${baseline}H715`,C.ink);',
'h=135*Math.abs(v)/max':'h=(baseline===180?95:135)*Math.abs(v)/max',
'v>=0?270-h:270':'v>=0?baseline-h:baseline',
'v>=0?255-h:295+h':'v>=0?baseline-15-h:baseline+24+h',
'const i=Math.round((n.x-90)/92);':'const i=records.findIndex(a=>a.id===n.id);',
'text(g,x+w+20,y+6,xlabel,18);':'text(g,x+w/2,y+38,xlabel,17);',
'if(!vars.length)derivation(p,g,f);':'if(!vars.length)derivationExact(p,g,f);',
'[s.caller,s.callee,s.shared].filter(Boolean)':'[s.caller,s.callee,s.shared].filter(v=>v!==undefined)',
'const a=pos.get("value")||{x:s.x||380,y:210};':'const a=pos.get("value")||pos.get("token")||{x:s.x||380,y:210};',
'if(s.shared&&!/No shared/.test(s.shared))':'if(s.shared!==undefined&&s.shared!==null&&!/No shared/.test(String(s.shared)))',
'numeric(p,g,f,pos);\n}':'if(["euclid","division","power","modular-power","gray-code","hamming-code"].includes(id))numeric(p,g,f,pos);else derivationExact(p,g,f);\n}',
'body.textContent=f.nodes.find(n=>n.id==="claim")?.label||f.caption;':'body.textContent=f.nodes.find(n=>n.id==="claim")?.label||f.nodes.filter(n=>n.id!=="token").map(n=>n.label).join("; ");',
'const mark=id==="matrix-product"':'const mark=id==="matrix-product"',
}
for old,new in replacements.items():
 assert old in s,old
 s=s.replace(old,new)
s=s.replace('matrices,tiles,array:arrayExact,memory,derivation:', 'matrices,tiles,array:arrayExact,memory:memoryExact,derivation:')
p.write_text(s,encoding='utf-8')
