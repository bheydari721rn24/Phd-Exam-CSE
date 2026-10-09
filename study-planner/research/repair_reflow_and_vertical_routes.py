from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/advanced-simulations.js';s=p.read_text(encoding='utf-8')
s=s.replace("function pairGeometry(before,after,model){\n", "function pairGeometry(before,after,model){\n   if(before.viewBox.baseVal.width!==after.viewBox.baseVal.width||before.viewBox.baseVal.height!==after.viewBox.baseVal.height||model.kind==='median-groups')return []; // A camera or grouping change is a layout update, not physical record transit.\n")
s=s.replace("if(recordRoutes.length){const svg=stage.querySelector('svg'),records=", "if(pairs.length){const svg=stage.querySelector('svg'),records=")
a="const [x,y,w,h]=dims(r),[ox,oy,ow,oh]=dims(oldRect),dx=x+B[0]-ox-A[0];if(Math.abs(dx)<2||Math.abs(y+B[1]-oy-A[1])>.1||w!==ow||h!==oh)continue;"
b="const [x,y,w,h]=dims(r),[ox,oy,ow,oh]=dims(oldRect),dx=x+B[0]-ox-A[0],dy=y+B[1]-oy-A[1],axis=Math.abs(dx)>=2&&Math.abs(dy)<.1?'x':Math.abs(dy)>=2&&Math.abs(dx)<.1?'y':null;if(!axis||w!==ow||h!==oh)continue;"
assert a in s;s=s.replace(a,b)
s=s.replace("const lane=-Math.sign(dx)*(h+10),route={node:g,base:g.getAttribute('transform')??'',lane,transformPair:", "const lane=-Math.sign(axis==='x'?dx:dy)*((axis==='x'?h:w)+10),route={node:g,base:g.getAttribute('transform')??'',lane,axis,transformPair:")
s=s.replace("+' translate(0 '+(r.lane*lift)+')'", "+' translate('+(r.axis==='y'?r.lane*lift:0)+' '+(r.axis==='x'?r.lane*lift:0)+')'")
a="const corridor={x:Math.min(x+B[0],ox+A[0]),y:y+B[1]+Math.min(0,lane),w:Math.abs(dx)+w,h:h+Math.abs(lane)};"
b="const corridor={x:Math.min(x+B[0],ox+A[0])+(axis==='y'?Math.min(0,lane):0),y:Math.min(y+B[1],oy+A[1])+(axis==='x'?Math.min(0,lane):0),w:Math.abs(dx)+w+(axis==='y'?Math.abs(lane):0),h:Math.abs(dy)+h+(axis==='x'?Math.abs(lane):0)};"
assert a in s;s=s.replace(a,b)
p.write_text(s,encoding='utf-8');print('Camera/group changes are atomic; vertical bucket movements use separate lanes.')
