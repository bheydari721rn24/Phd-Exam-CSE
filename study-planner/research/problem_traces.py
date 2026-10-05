"""Replay only explicit programming contracts using independently checked values."""
def programming(api,topic,cert,raw):
 strip,frame,model=api;k,d=cert.get('kind'),cert.get('data');frames=[]
 stem=raw.get('stem','');compact=stem.replace(' ','');scope='Actual question data or explicitly labeled derived values; independently checked against its numerical certificate. This is the stated abstract semantics, not execution of undefined C behavior.'
 def storage(values,title):
  import html
  text=lambda x,y,s:f'<text x="{x}" y="{y}" text-anchor="middle" font-size="20">{html.escape(str(s))}</text>'
  box=lambda x,y,w,h:f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#edf5f8" stroke="#91adb9"/>'
  wire=lambda a,b:f'<path d="M{a[0]} {a[1]}L{b[0]} {b[1]}" stroke="#557e91" stroke-width="1.6" fill="none" marker-end="url(#storage-tip)"/>'
  body=text(380,35,title)
  shared=k=='alias-affine' and d[2] or k=='qr' and '&x,&x' in compact or k=='iterate' and 'bothpointers' in compact.lower()
  if k=='alias-affine' or k=='qr' and 'voidqr' in compact or k=='iterate' and 'bothpointers' in compact.lower():
   names=['q','r'] if k=='qr' else ['p','q'];xs=[200,560]
   for x,name in zip(xs,names):body+=box(x-50,80,100,52)+text(x,113,name)
   centers=[380] if shared else xs
   targetnames=['n','rem'] if k=='qr' and '&n,&rem' in compact else names
   for j,(x,v) in enumerate(zip(centers,values)):body+=box(x-55,210,110,64)+text(x,250,v)+text(x,315,'shared object x' if shared else 'target '+targetnames[j])
   for x,X in zip(xs,[380,380] if shared else xs):body+=wire((x,132),(X,210))
  else:
   names={'Caller a':['a'],'Caller a; returned f(a)':['a','f(a)'],'Final caller a and b':['a','b'],'Derived candidate input':['x'],'Returned inner g(x)':['x','g(x)'],'Returned outer f(g(x))':['x','f(g(x))'],'Callback input':['x'],'Returned step(x)':['step(x)'],'Returned step(step(x))':['step(step(x))'],'Assigned return values':['x'],'Integer-halving caller state':['x'],'Persistent static s':['s'],'Automatic a and persistent s':['a','s'],'Quotient and remainder':['q','r'],'Argument a, argument b, result, final counter':['a','b','a − b','counter']}.get(title,[f'value {i+1}' for i in range(len(values))])
   width=min(130,600/max(1,len(values)));start=(760-width*len(values))/2
   for i,v in enumerate(values):x=start+i*width;body+=box(x+8,130,width-16,72)+text(x+width/2,174,v)+text(x+width/2,246,names[i])
  return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" role="img" aria-label="'+html.escape(title,quote=True)+'"><defs><marker id="storage-tip" markerWidth="7" markerHeight="6" refX="7" refY="3" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0L7 3L0 6Z" fill="#557e91"/></marker></defs>'+body+'</svg>'
 def save(values,caption,title,active=None):frames.append(frame(storage(values,title) if topic=='p_functions' else strip(values,active,title),caption,values=list(values)))
 if topic=='p_functions':
  if k=='affine':
   a,b,c,e,x,expected=d;u=a*x+b;v=c*u+e;assert v==expected
   if 'f(g(x))' in compact:
    save([x],f'The derivation produces candidate x={x}. This frame evaluates that candidate; it is not an extra given assumption.','Derived candidate input')
    save([x,u],f'Inner g({x}) = {a} × {x} + ({b}) = {u}.','Returned inner g(x)')
    save([x,v],f'Outer f({u}) = {c} × {u} + ({e}) = {v}; the candidate satisfies the requested equation. The written derivation establishes uniqueness.','Returned outer f(g(x))')
   elif 'apply(step,4)' in compact:
    save([x],'Initial callback argument from the question.','Callback input');save([u],f'The first step call returns {a} × {x} + ({b}) = {u}.','Returned step(x)');save([v],f'The second step call receives {u} and returns {v}. It is not a call on twice the original argument.','Returned step(step(x))')
   else:
    save([x],'The caller object a retains this value throughout; helper parameters are separate copies.','Caller a')
    save([x,u],f'f receives {x}, computes {a} × {x} + ({b}), and returns {u}.','Caller a; returned f(a)')
    save([x,v],f'g receives {u}, computes {c} × {u} + ({e}), and returns {v}; only b receives it.','Final caller a and b')
  elif k=='alias-affine':
   x,y,alias,expected=d
   save([x] if alias else [x,y], 'Both pointers designate one object.' if alias else 'The two pointers designate distinct objects.','Actual target storage')
   if alias:
    x+=2;save([x],'The first statement adds two to the shared object.','After *p += 2');x*=3;actual=[x,x];save([x],'The second statement reads the value already changed by the first statement.','After *q *= 3')
   else:
    x+=2;save([x,y],'Only the p target changes.','After *p += 2');y*=3;actual=[x,y];save([x,y],'Only the distinct q target changes.','After *q *= 3')
   assert actual==expected
  elif k=='iterate':
   a,b,x,n,expected=d;alias='bothpointers' in compact.lower();save([x],'Initial shared target object.' if alias else 'Initial caller state. Each return is assigned back to this object.','Assigned return values')
   for i in range(n):
    old=x
    if alias:
     x=2*x+1;save([x],f'Illustrative call {i+1}, first statement: *p becomes 2 × {old} + 1 = {x}. Both pointers still designate this one object.','After first alias write')
     x+=x;save([x],f'Illustrative call {i+1}, second statement: *q reads both aliases after the first write and doubles {x//2}, producing {x}.','After second alias write')
    else:x=a*x+b;save([x],f'Assignment {i+1}: {a} × {old} + ({b}) = {x}.','Assigned return values')
   assert x==expected
   if 'afterkcalls' in compact:scope='The three-call numerical witness is explicitly illustrative. The complete solution proves the general k-call recurrence; these three frames do not replace that proof.'
  elif k=='halves':
   x,expected=d;actual=[];save([x],'Initial nonnegative integer. Division truncates toward zero.','Integer-halving caller state')
   while x:x//=2;actual.append(x);save([x],f'Call {len(actual)} returns {x}; assigning this value changes the caller.','Integer-halving caller state')
   assert actual==expected
  elif k=='static':
   static,args,expected=d;actual=[];save([static],'The static object exists across calls; each automatic a starts again at one.','Persistent static s')
   # The certificate stores the computed automatic increments (1+d), not raw d.
   for i,arg in enumerate(args):static+=arg;actual.append(static);save([arg,static],f'Call {i+1}: automatic a restarts at 1, then becomes {arg}; static s accumulates it and becomes {static}.','Automatic a and persistent s')
   assert actual==expected
  elif k in ['qr','signed-qr']:
   n,den,q,r=d;assert n==den*q+r
   if k=='qr' and '&x,&x' in compact:save([0],'Both output pointers designate the same scalar x.','Shared output object x');save([q],f'The quotient statement writes {q}.','After quotient write');save([r],f'The later remainder write replaces {q} with {r}; one scalar cannot retain both outputs.','After remainder write')
   elif k=='qr' and '&n,&rem' in compact:
    save([n,'unused'],'The caller n is copied into a separate value parameter before any output write. The remainder target is not read.','Caller output objects')
    save([q,'unused'],f'The quotient write changes caller n to {q}, while callee n still contains original {n}.','After quotient write')
    save([q,r],f'The remainder is computed from the preserved callee copy {n}, so rem receives {r}.','After remainder write')
   else:save([q,r],f'{n} = {den} × ({q}) + ({r}). C truncates division toward zero; the nonzero remainder has the dividend sign.','Quotient and remainder')
  elif k=='orders':
   outputs,final=d
   for v in outputs:
    a,b=(1,2) if v==-1 else (2,1);assert a-b==v;save([a,b,v,final],f'One permitted order binds a={a}, b={b}; difference is {v}. Both calls leave the counter at {final}.','Argument a, argument b, result, final counter')
 else:
  if k=='inplace':
   a,direction,expected=d;a=a[:];save(a,'Initial array. Each following update reads current storage.','In-place recurrence')
   for i in (range(1,len(a)) if direction=='forward' else range(len(a)-1,0,-1)):
    a[i]+=a[i-1];save(a,f'Index {i}: add the current predecessor A[{i-1}] = {a[i-1]}.','In-place recurrence',i)
   assert a==expected
  elif k=='reverse':
   a,l,r,expected=d;a=a[:];save(a,f'Only the half-open segment [{l},{r}) is reversed.','Original segment')
   while l<r-1:r-=1;a[l],a[r]=a[r],a[l];save(a,f'Swap endpoints {l} and {r}; the remaining unprocessed segment shrinks.','Segment reversal',l);l+=1
   assert a==expected
  elif k=='insert':
   a,p,value,expected,shifts=d;a=a[:]+['free'];save(a,'One extra live slot is required before shifting.','Insertion storage')
   count=0
   for j in range(len(a)-2,p-1,-1):a[j+1]=a[j];count+=1;save(a,f'Copy original slot {j} right to {j+1}. Right-to-left order preserves unread sources.','Insertion shift',j+1)
   a[p]=value;save(a,f'Write {value} at insertion index {p}.','Completed insertion',p);assert a==expected and count==shifts
  elif k=='delete':
   a,p,expected,shifts=d;a=a[:];save(a,'Original active storage; the specified slot is removed from the sequence.','Original active array')
   count=0
   for j in range(p,len(a)-1):a[j]=a[j+1];count+=1;save(a,f'Move original slot {j+1} left to {j}. The last physical slot is outside the new logical length.','Deletion shift',j)
   assert a[:-1]==expected and count==shifts;save(expected,'Reduce logical length by one. The inactive trailing storage is not part of this sequence.','Final logical sequence')
  elif k=='prefix':
   a,expected=d;p=[0];save(a,'Original input; prefix zero is an empty sum.','Input sequence')
   for i,v in enumerate(a):p.append(p[-1]+v);save(p,f'P[{i+1}] = P[{i}] + A[{i}] = {p[-1]}.','Built prefix values',i+1)
   assert p==expected
  elif k=='filter':
   a,expected=d;out=[];save(a,'The read cursor sees every source element once; only even elements are retained.','Original filter input')
   for i,v in enumerate(a):
    if v%2==0:out.append(v);save(out,f'Read index {i}: retain even value {v}. Write cursor advances; order of survivors is preserved.','Retained prefix',len(out)-1)
   assert out==expected
  elif k=='difference':
   diff,expected=d;a=[];total=0;save(diff,'The difference entries describe starts and cancellations of updates.','Difference values')
   for i,v in enumerate(diff[:-1]):total+=v;a.append(total);save(a,f'Prefix sum through difference index {i} reconstructs A[{i}] = {total}.','Reconstructed array',i)
   assert a==expected
 if not frames:return
 return model('exact-program-state',frames,'Read one program update or helper evaluation at a time. Object identity and operation order are preserved as specified; any derived numerical witness is labeled in its caption.',scope)
