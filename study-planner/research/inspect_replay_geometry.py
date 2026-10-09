from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/advanced-simulations.js';s=p.read_text()
old="const a=outside(before),b=outside(after);if(a.length===b.length)b.forEach((n,i)=>add(a[i],n));"
new="""const key=n=>[n.tagName,n.dataset.source??n.dataset.layoutSource??'',n.dataset.target??n.dataset.layoutTarget??'',n.dataset.net??''].join('|');
  const linked=new Map(outside(before).filter(n=>n.dataset.source||n.dataset.layoutSource||n.dataset.net).map(n=>[key(n),n]));
  for(const n of outside(after)){const a=linked.get(key(n));if(a&&(n.dataset.source||n.dataset.layoutSource||n.dataset.net))add(a,n);} // A changed target is an atomic rewire, never an unattached moving tip."""
assert old in s;s=s.replace(old,new)
s=s.replace("'height','fill'].map(a=>n.getAttribute(a))","'height','fill','stroke'].map(a=>n.getAttribute(a))")
p.write_text(s,encoding='utf-8')
p=R/'research/qa_unified_library.py';s=p.read_text();needle="checks++;}p.show(0);"
s=s.replace(needle,"for(const issue of DiagramLayout.audit(svg))issues.push({frame:i,...issue});checks++;}p.show(0);")
p.write_text(s,encoding='utf-8')
print('Only identified, unchanged connector relations can move; rewiring is discrete. Full glyph/padding/port audit enabled.')
