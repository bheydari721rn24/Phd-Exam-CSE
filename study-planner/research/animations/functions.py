"""Exact semantic checkpoints; coordinate motion is transfer of a value token."""
from common import node,frame,scene

def card(id,label,x,y,tone='plain',w=235):return node(id,label,x,y,w=w,h=55,tone=tone,size=21)
def seq(id,title,description,invariant,states,formula='',code=()):
 fs=[]
 for s in states:
  ns=[card('caller',s['caller'],160,70),card('callee',s['callee'],560,70),
      card('shared',s.get('shared','No shared object'),360,180,w=320),
      card('value',str(s['value']),s['x'],290,'active',w=135)]
  fs.append(frame(ns,s['caption'],s.get('metrics',{}),formula,snapshot={k:v for k,v in s.items() if k not in ['caption','metrics']}))
 scene(id,title,description,invariant,fs,code)

seq('fn-copy','A copied value moves; the caller object stays','Call f(a) where f increments a parameter copy then returns twice that copy. Motion transports a value token, not the caller object.','Caller a remains four; the new parameter changes and its returned value is copied back.',[
 dict(caller='a = 4; result pending',callee='Not entered',value=4,x=160,caption='Evaluate caller a to obtain four. The object a stays in the caller while its value is prepared as an argument.'),
 dict(caller='a = 4; result pending',callee='x = 4',value=4,x=560,caption='Initialize a new callee parameter object with four. It does not designate the caller scalar object.'),
 dict(caller='a = 4; result pending',callee='x = 7 after x += 3',value=14,x=560,caption='Change the local parameter to seven and evaluate the returned expression twice x, yielding fourteen.'),
 dict(caller='a = 4; result = 14',callee='Invocation ended',value=14,x=160,caption='Return fourteen to the saved caller continuation. The original caller a remains four throughout the completed call.')],r'a=4\quad x_{new}=7\quad r=14')

seq('fn-pointer','An address value enables a target write','Copy the address of caller a into a local pointer p; then write through p. The address token and target value are different quantities.','p is a separate pointer object; its designated caller target remains the same live object.',[
 dict(caller='a = 4',callee='Not entered',shared='Target object a: 4',value='&a',x=160,caption='Form the address of live caller object a. The argument is an address value rather than the integer four.'),
 dict(caller='a = 4',callee='p designates a',shared='Target object a: 4',value='&a',x=560,caption='Copy that address into local pointer p. The caller and callee can now refer to the same target object.'),
 dict(caller='a = 11',callee='p still designates a',shared='Target object a: 11',value='*p = 11',x=360,caption='Write twice the target plus three through p. This changes the caller object because dereferencing p designates that object.'),
 dict(caller='a = 11',callee='Invocation ended',shared='Target object a: 11',value='void return',x=160,caption='End the void invocation. Its pointer parameter disappears, while the modified caller object remains live with value eleven.')])

seq('fn-alias','Two aliases observe sequential updates','Both pointers designate the same valid integer object. Each full statement completes before the next statement reads it.','The shared value follows u, then u+2, then 3(u+2), with no second independent target.',[
 dict(caller='One object: a = 4',callee='p = &a; q = &a',shared='Both aliases select a',value=4,x=360,caption='Bind both copied pointer parameters to one target. There is one stored integer value, not two separate outputs.'),
 dict(caller='One object: a = 6',callee='Complete *p += 2',shared='Both aliases select a',value=6,x=260,caption='The first full statement adds two through p. Reading through q afterward would observe the updated value six.'),
 dict(caller='One object: a = 18',callee='Complete *q *= 3',shared='Both aliases select a',value=18,x=460,caption='The second statement triples the shared current value six. The final value is eighteen, not twelve from a stale copy.')],r'u\mapsto u+2\mapsto3u+6')

seq('fn-nested','A nested body suspends its continuation','combine(2) saves the first affine result, then calls affine on that result. Affine returns three times its argument plus one.','The two affine frames are sequential; each returns to the same paused combine frame.',[
 dict(caller='combine: x = 2',callee='First affine pending',value=2,x=160,caption='The combine frame is active with parameter two. It pauses before initializing first from the first nested helper result.'),
 dict(caller='combine: first pending',callee='affine: x = 2',value=7,x=560,caption='The first affine invocation computes three times two plus one. It prepares seven for its caller continuation.'),
 dict(caller='combine: first = 7',callee='First affine ended',value=7,x=160,caption='Seven returns into first. The first helper frame ends before the next affine invocation is created.'),
 dict(caller='combine: second pending',callee='affine: x = 7',value=22,x=560,caption='The second helper receives the saved value seven, not original two. It prepares twenty-two as its own returned value.'),
 dict(caller='combine: first + second',callee='Second affine ended',value=29,x=160,caption='The combine continuation adds seven and twenty-two. Its final return value is twenty-nine, with peak helper depth two.')],r'(3x+1)+(3(3x+1)+1)=12x+5')

states=[]
for k in range(1,4):
 states.extend([
 dict(caller=f'Call {k}: pending',callee='fresh = 0',shared=f'saved = {k-1}',value=k,x=160,caption=f'Call number {k} creates a new automatic fresh initialized to zero. The one static saved object retains its previous value.'),
 dict(caller=f'Call {k}: pending',callee='fresh = 1',shared=f'saved = {k}',value=10+k,x=560,caption=f'Increment fresh and the persistent saved object once. The returned expression ten times fresh plus saved now yields {10+k}.'),
 dict(caller=f'Call {k}: result {10+k}',callee='Invocation ended',shared=f'saved = {k}',value=10+k,x=160,caption='Copy the result back and end the automatic invocation. The static object persists for the next separate call.')])
seq('fn-static','Automatic locals reset; one static object persists','Three calls in separate statements create fresh automatic locals but share one saved object.','For call k, fresh becomes one and saved becomes k; the result is ten plus k.',states,r'r_k=10+k')

seq('fn-lookup','A caller is not a lexical parent','The file-level read_x returns file x=10, even while a caller has its own local x=3.','The lexical definition selects the file object; the call continuation selects where execution resumes.',[
 dict(caller='caller local x = 3',callee='read_x pending',shared='File object x = 10',value='lookup x',x=560,caption='The read_x body requires the declaration associated with its lexical definition. The active caller also has a different x object.'),
 dict(caller='caller local x = 3',callee='read_x uses file x',shared='File object x = 10',value=10,x=360,caption='Resolve x to the file-scope object containing ten. The caller local is not in this separately defined function scope.'),
 dict(caller='Return 10 + 3 = 13',callee='read_x ended',shared='File object x = 10',value=13,x=160,caption='Return ten to the paused caller, which adds its own local three. The final result is thirteen with two unchanged x objects.')])

states=[]
for order in ['left first','right first']:
 for phase in range(3):
  left=1 if order=='left first' else 2;right=3-left
  states.append(dict(caller=f'{order}: sub pending' if phase<2 else f'Result: {left-right}',callee=f'{phase} next calls complete',shared=f'counter = {phase}',value=(0 if phase==0 else 1 if phase==1 else left-right),x=(160 if phase==0 else 560 if phase==1 else 160),order=order,phase=phase,left=left,right=right,caption=('Reset the counter to zero for this alternative permitted order. Each next function body will finish before the other runs.' if phase==0 else 'Complete the first next body and retain its value one for its selected argument position. The other position remains pending.' if phase==1 else 'The second next body returns two. Place both saved values in their argument positions and subtract, yielding this permitted result.')))
seq('fn-orders','Enumerate both permitted C17 call-body orders','Two alternative traces restart from counter zero. This is not a chronological sequence of six calls.','Both branches end with counter two; the result is minus one or plus one.',states)

fs=[]
for depth in range(4):
 ns=[card(f'frame{k}',f'n = {3-k}; addition pending',170,65+70*k,w=290) for k in range(depth+1)]
 ns.append(card('token',f'argument {3-depth}',570,65+70*depth,'active',w=230))
 fs.append(frame(ns,'Create one new parameter object for the next call. Earlier invocations retain their own n and wait for the returned tail value.',{'Active helper frames':depth+1},snapshot=dict(kind='descent',depth=depth,value=3-depth)))
for depth,value in [(3,0),(2,1),(1,3),(0,6)]:
 ns=[card(f'frame{k}',f'n = {3-k}; '+('return '+str(value) if k==depth else 'addition pending'),170,65+70*k,w=290) for k in range(depth+1)]
 ns.append(card('token',f'returned value {value}',570,65+70*depth,'active',w=230))
 fs.append(frame(ns,'Return the completed tail value to the nearest paused caller. Its own saved parameter supplies the next addition on the way back.',{'Active helper frames':depth+1,'Returned value':value},snapshot=dict(kind='ascent',depth=depth,value=value)))
scene('fn-recursion','Distinct recursive parameters and moving return values','sum_down(3) descends to zero and unwinds one saved addition at a time.','At depth d, the frame parameter is 3-d; each suspended caller resumes once.',fs,code=['if (n == 0) return 0;','tail = sum_down(n - 1);','return n + tail;'])

fs=[]
for k,(old,new,local) in enumerate([('[2]','Not created','Original list'),('[2,7]','Not created','Original list'),('[2,7]','[99]','New list'),('[2,7]','[99]','Invocation ended')]):
 ns=[card('caller','caller data → original',170,65,w=285),card('local','local values: '+local,560,65,w=300),card('old','Original: '+old,170,240,w=230),card('new','New: '+new,560,240,w=230),card('token','Binding target',170 if k<2 else 560,145,'active',w=175)]
 fs.append(frame(ns,['The parameter and caller name initially designate one original list. No list copy is made by parameter binding.','Append seven through the shared local binding. The same original list is changed and remains visible through the caller name.','Rebind the local name to a new list containing ninety-nine. The caller still designates the original mutated list.','Return the new list to the result binding. Original data remains the separate list containing two and seven.'][k],snapshot=dict(old=old,new=new,stage=k)))
scene('fn-sharing','Mutation changes an object; rebinding changes a name','A Python list argument is mutated, then the local name is rebound to a fresh list.','The caller name keeps its original target; only mutation changes that original object.',fs)

seq('fn-closure','A retained lexical binding follows its function','make_shift(4) returns a closure; a later caller with local k=9 invokes it on three.','The closure reads its definition environment k=4 rather than the active caller k=9.',[
 dict(caller='Factory: k = 4',callee='Define shift',shared='Retained binding k = 4',value='function',x=560,caption='Define the inner function with the current factory environment as its lexical parent. Its free k selects that binding.'),
 dict(caller='Factory call has ended',callee='Closure still reachable',shared='Retained binding k = 4',value='function',x=160,caption='Return the function object. The retained environment remains reachable even though the factory is no longer executing.'),
 dict(caller='Later caller: k = 9',callee='shift: x = 3',shared='Retained binding k = 4',value=7,x=560,caption='Invoke the closure on three. Its lexical parent supplies four, so it returns seven despite the caller local nine.'),
 dict(caller='Caller receives 7',callee='Invocation ended',shared='Retained binding k = 4',value=7,x=160,caption='Return seven to this caller continuation without changing the retained k binding. Future calls can reuse the same function object.')])

seq('fn-default','One mutable default belongs to a definition','Two no-explicit-list calls append to the same saved default. Returned snapshots are fresh copies.','The saved list grows from empty to one item then two; the first snapshot remains one item.',[
 dict(caller='Definition executes',callee='No call yet',shared='Saved default: []',value='[]',x=360,caption='Evaluate the empty-list default expression once when the function definition executes. No invocation has appended any value yet.'),
 dict(caller='First call: f(2)',callee='a → saved default',shared='Saved default: [2]',value='[2]',x=560,caption='Bind the first call parameter to the saved list and append two. The returned snapshot is a separate one-element list.'),
 dict(caller='First snapshot: [2]',callee='Second call: f(5)',shared='Saved default: [2,5]',value='[2,5]',x=560,caption='Bind the second invocation to the same default and append five. The original snapshot does not grow because it was copied.'),
 dict(caller='Snapshots: [2]; [2,5]',callee='Both calls ended',shared='Saved default: [2,5]',value='two snapshots',x=160,caption='Both invocations end while the function retains its default object. Future calls using the default begin with these saved contents.')])

seq('fn-output','One aliased output cannot retain two values','Compute quotient and remainder of twenty-three divided by five into the same output object.','The scalar input copies stay fixed, but the second output overwrites the first.',[
 dict(caller='output x = 0',callee='n = 23; d = 5',shared='q and r both designate x',value=0,x=160,caption='Copy the two scalar inputs and bind both output pointers to the same caller integer object. Its initial value is zero.'),
 dict(caller='output x = 4',callee='Complete *q = n/d',shared='q and r both designate x',value=4,x=360,caption='Compute the quotient from fixed input copies and write four. Both output pointers now observe that same stored four.'),
 dict(caller='output x = 3',callee='Complete *r = n%d',shared='q and r both designate x',value=3,x=360,caption='Compute the remainder from the unchanged input copies and overwrite x with three. Both promised final outputs cannot survive in one object.'),
 dict(caller='output x = 3',callee='Invocation ended',shared='Two-output contract violated',value=3,x=160,caption='The execution itself is defined for these valid targets, but a contract promising both quotient and remainder in distinct results is unsatisfied.')],r'23=4\cdot5+3')
