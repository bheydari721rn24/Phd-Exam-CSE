from pathlib import Path
p=Path(__file__).resolve().parents[1]/'dist/chapters/semantic-diagrams.js';s=p.read_text(encoding='utf-8')
changes={
'function orthogonalRoute(from,to,boxes){const key=JSON.stringify([from,to,boxes]);':'function orthogonalRoute(from,to,boxes,used=[],net=""){const key=JSON.stringify([from,to,boxes,used,net]);',
'const ports={},values={},boxes=':'const ports={},values={},used=[],boxes=',
'orthogonalRoute(from,to,boxes)':'orthogonalRoute(from,to,boxes,used,source)',
'wire.dataset.net=source;':'wire.dataset.net=source;const coordinates=[...wire.getAttribute("d").matchAll(/[ML](-?[0-9.]+),(-?[0-9.]+)/g)].map(m=>[+m[1],+m[2]]);for(let k=1;k<coordinates.length;k++)used.push({a:coordinates[k-1],b:coordinates[k],net:source});',
'a[0]>b[0]&&a[0]<b[2]&&Math.max(a[1],c[1])>b[1]':'a[0]>=b[0]&&a[0]<=b[2]&&Math.max(a[1],c[1])>b[1]',
'if(inside(b)||blocked(a,b))continue;':'if((q.i===start&&dx!==1)||(i===end&&dx!==1)||inside(b)||blocked(a,b)||used.some(u=>u.net!==net&&(a[1]===b[1]&&u.a[1]===u.b[1]&&a[1]===u.a[1]?Math.max(Math.min(a[0],b[0]),Math.min(u.a[0],u.b[0]))<Math.min(Math.max(a[0],b[0]),Math.max(u.a[0],u.b[0])):a[0]===b[0]&&u.a[0]===u.b[0]&&a[0]===u.a[0]?Math.max(Math.min(a[1],b[1]),Math.min(u.a[1],u.b[1]))<Math.min(Math.max(a[1],b[1]),Math.max(u.a[1],u.b[1])):false)))continue;',
'value?C.green:C.red);return {inputs':'value===null||value==="?"?C.ink:value?C.green:C.red);return {inputs',
}
for a,b in changes.items():
 assert a in s,a
 s=s.replace(a,b)
p.write_text(s,encoding='utf-8')
