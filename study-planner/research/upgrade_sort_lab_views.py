from pathlib import Path
B=Path(__file__).parent;p=B/'a_sort_lab.js';s=p.read_text(encoding='utf-8');start=s.index(' function picture(');end=s.index(' function evaluate(',start);s=s[:start]+(B/'a_sort_lab_picture.js').read_text(encoding='utf-8')+s[end:]
before="f.teaching={operation:"
assert s.count(before)==1;s=s.replace(before,"f.layout=f.layout||(rows.some(r=>r.role==='left')?'merge':(kind==='radix'||kind==='bucket')&&rows.length>1?'buckets':'array');f.teaching={operation:")
before="add('Compare heads and emit one; equality chooses left.',rows());"
after="add('Compare heads and emit one; equality chooses left.',rows(),{transfer:{row:L[i-1]?.id===out.at(-1).id?'left':'right',index:L[i-1]?.id===out.at(-1).id?i-1:j-1,dest:out.length-1},operation:'move',reason:'The selected source record is copied into the next output slot; the source is an immutable run reference.',activeLine:3});"
assert s.count(before)==1;s=s.replace(before,after);p.write_text(s,encoding='utf-8')
