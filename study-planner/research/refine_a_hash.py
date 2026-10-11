from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=R/'dist/chapters/a_hash.js';s=p.read_text(encoding='utf-8')
s=s.replace("return s;}\nfunction probe", """if(s.operation==='chain'&&(s.capacity>8||s.keys.length+s.commands.filter(c=>c.type==='put').length>8))throw Error('Compact chaining accepts at most eight keys and eight buckets.');
if(s.operation==='perfect'){const counts=Array(s.capacity).fill(0);for(const k of s.keys)counts[mod(k,s.capacity)]++;if(Math.max(...counts)>3||counts.filter(Boolean).length>4)throw Error('Compact perfect placement accepts at most three keys per bucket and four occupied buckets.');}
if(s.operation==='rebuild'&&(s.policy!=='linear'||s.newCapacity<new Set(s.keys).size))throw Error('Rebuild requires linear probing and enough new slots for distinct keys.');
if(s.operation==='cuckoo'&&new Set(s.keys).size!==s.keys.length)throw Error('Cuckoo placement accepts distinct keys.');
if(s.operation==='robin'&&new Set(s.keys).size>s.capacity)throw Error('Robin Hood placement requires sufficient slots.');return s;}
function probe""")
s=s.replace("slots[j]={key:k,value:k,id:'R'+k};", "slots[j]=clone(old.find(v=>v&&v!=='DELETED'&&v.key===k));")
s=s.replace('let prime=1009,chosen=null','let prime=2003,chosen=null').replace('a*mod(k,prime)+c','a*(k+999)+c')
s=s.replace("liveKeys:s.operation==='chain'?", "liveKeys:['chain','perfect'].includes(s.operation)?")
s=s.replace("s.operation==='bloom'||s.operation==='horner'?[]:ids()", "s.operation==='bloom'||s.operation==='horner'?[]:s.operation==='cuckoo'?ids().concat((extra.right||[]).filter(Boolean).map(v=>v.key)):ids()")
s=s.replace('${j?x-14:74}', '${j?x-16:72}').replace('${x-8} ${y+14}', '${x} ${y+14}')
s=s.replace('M200 207 L284 207 M409 207 L515 207', 'M190 207 L294 207 M399 207 L525 207')
s=s.replace("row(z.extra.right,212,'right')", "row(z.extra.right||Array(z.capacity).fill(null),212,'right')")
s=s.replace("else{out+=row(z.slots,85,'slot');", "else{if(z.cursor!==null)out+=rect('probe',30+z.cursor*Math.min(53,650/z.slots.length),51,Math.min(53,650/z.slots.length)-4,24,'probe','','#d6edf5');out+=row(z.slots,85,'slot');")
# Use a visual period, not a prose font glyph, for EMPTY.
s=s.replace("'·'", "'–'")
s=s.replace("s.commands=s.commands||[];", "s.commands=s.commands||[];")
s=s.replace("const raw={operation:", "if(!form.elements.capacity.value.trim()||!form.elements.step.value.trim())throw Error('Capacity and step must be specified.');const raw={operation:")
p.write_text(s,encoding='utf-8')
p=R/'research/a_hash.en.md';s=p.read_text(encoding='utf-8');s=s.replace('<!-- PROBLEMS -->','<!-- INCLUDE: problems -->').replace('<!-- REVIEW -->','<!-- INCLUDE: review -->')
s=s.replace('For slots `[32,43,EMPTY', 'For slots `[32,43,EMPTY') # Exact prose corrected below after live lookup.
s=s.replace('## 4. Separate chaining', '<!-- SIM: arithmetic -->\n\n## 4. Separate chaining').replace('## 19. Applications', '<!-- SIM: advanced -->\n\n## 19. Applications')
p.write_text(s,encoding='utf-8')
p=R/'research/a_hash-source-audit.md';s=p.read_text(encoding='utf-8').replace('Nick Bowman and Kylie Jue attribution is not assumed for this later offering; page credits', 'the written page credits');p.write_text(s,encoding='utf-8')
print('Refined compact input contracts, stable rebuild IDs, exact connectors and collision-free key encoding.')
