"""Exact logic trees and fixed-width arithmetic, checked against truth contracts."""
import re,math

def parse(formula):
 s=formula.replace('R_1','B').replace('R_0','C').replace('E','A')
 tokens=re.findall(r'\\overline|\\oplus|[ABCD01()+{}]',s);i=0
 def atom():
  nonlocal i
  t=tokens[i];i+=1
  if t=='\\overline':return ('NOT',atom())
  if t in ['(','{']:
   v=expr();assert tokens[i] in [')','}'];i+=1;return v
  assert t in 'ABCD01',t
  return t
 def product():
  nonlocal i
  v=atom()
  while i<len(tokens) and tokens[i] not in ['+','\\oplus',')','}']:v=('AND',v,atom())
  return v
 def xor():
  nonlocal i
  v=product()
  while i<len(tokens) and tokens[i]=='\\oplus':i+=1;v=('XOR',v,product())
  return v
 def expr():
  nonlocal i
  v=xor()
  while i<len(tokens) and tokens[i]=='+':i+=1;v=('OR',v,xor())
  return v
 result=expr();assert i==len(tokens),(formula,tokens[i:]);return result

def evaluate(t,inputs):
 if isinstance(t,str):return int(t) if t in '01' else inputs[t]
 if t[0]=='NOT':return 1-evaluate(t[1],inputs)
 a,b=[evaluate(v,inputs) for v in t[1:]]
 return {'AND':a&b,'OR':a|b,'XOR':a^b}[t[0]]

def circuit_models(api,data):
 tx,line,svg,frame,model=api
 a,b=parse(data['reference']),parse(data['candidate']);frames=[]
 def depth(t):return 0 if isinstance(t,str) else 1+max(map(depth,t[1:]))
 def leaves(t):return 1 if isinstance(t,str) else sum(map(leaves,t[1:]))
 def draw(t,inputs,offset,label):
  d=depth(t);height=max(130,leaves(t)*58+50);cursor=offset+58;s=''
  def node(t):
   nonlocal cursor,s
   x=90+depth(t)*min(118,500/max(1,d))
   if isinstance(t,str):
    y=cursor;cursor+=58;s+=tx(x-14,y+6,f'{t} = {evaluate(t,inputs)}',18,anchor='end');return x,y
   children=[node(u) for u in t[1:]];y=sum(p[1] for p in children)/len(children);op=t[0];ports=[y] if len(children)==1 else [y-11,y+11]
   for j,((X,Y),py) in enumerate(zip(children,ports)):
    # Separate orthogonal input lanes attach to the actual gate boundary.
    entry=x+9*(1-(11/23)**2) if op in ['OR','XOR'] else x
    bend=x-22-j*8
    s+=f'<path d="M{X} {Y}H{bend}V{py}H{entry}" fill="none" stroke="#557e91" stroke-width="1.5"/>'
   if op=='AND':path=f'M{x} {y-23}H{x+23}A23 23 0 0 1 {x+23} {y+23}H{x}Z';out=x+46
   elif op in ['OR','XOR']:
    path=f'M{x} {y-23}Q{x+31} {y-23} {x+51} {y}Q{x+31} {y+23} {x} {y+23}Q{x+18} {y} {x} {y-23}Z';out=x+51
    if op=='XOR':s+=f'<path d="M{x-6} {y-23}Q{x+12} {y} {x-6} {y+23}" fill="none" stroke="#557e91" stroke-width="1.5"/>'
   else:path=f'M{x} {y-23}L{x+39} {y}L{x} {y+23}Z';out=x+49
   s+=f'<path d="{path}" fill="#eef6f8" stroke="#557e91" stroke-width="1.5"/>'
   if op=='NOT':s+=f'<circle cx="{x+44}" cy="{y}" r="5" fill="white" stroke="#557e91" stroke-width="1.5"/>'
   s+=line(out,y,out+25,y)+tx(out+15,y-13,evaluate(t,inputs),16)
   return out+25,y
  out,y=node(t);s+=line(out,y,707,y)+tx(730,y+6,evaluate(t,inputs),19)+tx(40,offset+24,label,20,anchor='start')
  return s,height
 for i,values in enumerate(data['values']):
  inputs=dict(zip('ABCD',map(int,format(i,'04b'))));actual=[evaluate(a,inputs),evaluate(b,inputs)];assert actual==values,(data['name'],i,actual,values)
  s,h=draw(a,inputs,38,'Reference F');s2,h2=draw(b,inputs,38+h,'Candidate G');s+=s2
  s+=tx(380,24,'Settled input ABCD = '+format(i,'04b'),20)+tx(380,38+h+h2+25,f'Miter F XOR G = {actual[0]^actual[1]}',21)
  frames.append(frame(svg(s,'Exact gate-level equivalence miter',38+h+h2+60),f'ABCD={i:04b}: F={actual[0]}, G={actual[1]}. '+('This row detects the proposed change.' if actual[0]!=actual[1] else 'Both circuits agree on this row; this alone does not prove equivalence.'),inputs=inputs,outputs=actual))
 assert [i for i,v in enumerate(data['values']) if v[0]!=v[1]]==data['diff']
 return model('gate-equivalence-miter',frames,'Follow each signal through the distinct AND, OR, XOR and inverter symbols. Both trees receive the same valuation; the miter tests their outputs.','Exact Boolean functions from this question. Repeated leaf labels denote the same input signal. This is settled logic, not a propagation-delay simulation or a minimal shared-gate implementation.')

def arrival_model(api,data):
 tx,line,svg,frame,model=api;n=data['n'];late=data['late'];leaves=list(range(n))
 def balanced(xs):
  if len(xs)==1:return xs[0]
  k=len(xs)//2;return (balanced(xs[:k]),balanced(xs[k:]))
 chain=0
 for i in range(1,n):chain=(chain,i)
 designs=[('Balanced complete tree; late input at the last listed leaf',balanced(leaves)),('Early chain followed by late input',chain),('Balanced early subtree followed by late input',(balanced(leaves[:-1]),n-1))]
 def depth(t):return 0 if isinstance(t,int) else 1+max(map(depth,t))
 def gates(t):return 0 if isinstance(t,int) else 1+sum(map(gates,t))
 def arrival(t):return (late if t==n-1 else 0) if isinstance(t,int) else 1+max(map(arrival,t))
 frames=[]
 for title,t in designs:
  cursor=80;body='';width=max(760,240+110*depth(t));height=130+52*n
  def draw(t):
   nonlocal cursor,body
   x=130+110*depth(t)
   if isinstance(t,int):
    y=cursor;cursor+=52;body+=tx(x-14,y+6,f'x{t+1} @ {late if t==n-1 else 0}',18,anchor='end');return x,y
   points=[draw(c) for c in t];y=(points[0][1]+points[1][1])/2
   for j,(X,Y) in enumerate(points):body+=f'<path d="M{X} {Y}H{x-24-j*8}V{y-11+22*j}H{x}" fill="none" stroke="#557e91" stroke-width="1.5"/>'
   body+=f'<path d="M{x} {y-23}H{x+23}A23 23 0 0 1 {x+23} {y+23}H{x}Z" fill="#edf5f8" stroke="#557e91" stroke-width="1.5"/>'+tx(x+22,y+6,arrival(t),18)
   body+=line(x+46,y,x+70,y);return x+70,y
  X,Y=draw(t);body+=line(X,Y,width-60,Y)+tx(width-34,Y+6,arrival(t),18)
  body+=tx(width/2,30,'Gate numbers are latest arrival bounds',20)+tx(width/2,height-30,f'{n-1} AND gates; depth {depth(t)}; final arrival {arrival(t)}',20)
  image=svg(body,title,height).replace(f'viewBox="0 0 760 {height}"',f'viewBox="0 0 {width} {height}"')
  assert gates(t)==data['gates']
  frames.append(frame(image,title+f'. Each gate adds one to the later input arrival; the output bound is {arrival(t)}.',arrival=arrival(t),depth=depth(t),gates=gates(t)))
 assert frames[0]['depth']==data['balancedDepth'];assert frames[1]['arrival']==data['lateLast']
 return model('arrival-sensitive-and-trees',frames,'Compare the three actual topologies. At each AND, the displayed number is one plus the larger input arrival; wires carry no added delay.','Exact n and late-input time from this problem. The fully balanced tree uses the explicitly shown late-leaf placement. Bounds assume sensitized transitions and unit gate delay, not an electrical loading model.')

def word_model(api,data):
 tx,line,svg,frame,model=api;w,x,y=data['w'],data['x'],data['y'];mask=(1<<w)-1
 signed=lambda z:z-(1<<w) if z&(1<<(w-1)) else z
 expected=dict(bitNot=(~x)&mask,logicalNot=int(x==0),unsignedLess=int(x<y),signedLess=int(signed(x)<signed(y)),modsum=(x+y)&mask,carry=(x+y)>>w)
 assert expected==data['results'];assert data['signed']==[signed(x),signed(y)]
 frames=[];carry=0;bits=[];step=600/w
 for active in range(w):
  a=(x>>active)&1;b=(y>>active)&1;cin=carry;bit=(a+b+carry)&1;carry=(a+b+carry)>>1;bits.append(bit)
  s=tx(380,32,f'{w}-bit ripple addition; least significant column first',20)
  for j in range(w):
   cx=670-j*step;yy=190
   s+=tx(cx,72,'bit '+str(j),17)+tx(cx,111,'X: '+str((x>>j)&1),18)+tx(cx,146,'Y: '+str((y>>j)&1),18)
   s+=f'<rect x="{cx-30}" y="{yy-24}" width="60" height="48" rx="4" fill="'+('#ffe7b9' if j==active else '#edf5f8')+'" stroke="#557e91"/>'+tx(cx,yy+6,'FA',18)
   s+=line(cx-12,153,cx-12,yy-24)+line(cx+12,153,cx+12,yy-24)+line(cx,yy+24,cx,250)
   s+=tx(cx,278,str(bits[j]) if j<=active else '?',21)
   if j<w-1:s+=line(cx-30,yy,cx-step+30,yy,arrow=True)
   else:s+=line(cx-30,yy,cx-54,yy,arrow=True)+tx(cx-54,yy-14,carry if active==w-1 else '?',17)
   if j==0:s+=line(cx+55,yy,cx+30,yy,arrow=True)+tx(cx+55,yy-14,'0',17)
  s+=tx(380,328,f'Column {active}: {a} + {b} + carry {cin} = {a+b+cin}; sum bit {bit}, carry out {carry}',18)
  s+=tx(380,365,f'Unsigned operands: {x}, {y}; signed operands: {signed(x)}, {signed(y)}',18)
  s+=tx(380,404,'Unsigned X < Y: '+str(expected['unsignedLess'])+'; signed X < Y: '+str(expected['signedLess']),18)
  frames.append(frame(svg(s,'Actual fixed-width addition',440),f'Full adder at bit {active} receives carry {cin}. Its sum output is {bit} and carry output is {carry}. Bitwise NOT X is {expected["bitNot"]}; logical NOT X is {expected["logicalNot"]}.',bit=active,carryIn=cin,carryOut=carry,sumBits=bits[:]))
 assert sum(v<<j for j,v in enumerate(bits))==expected['modsum'];assert carry==expected['carry']
 return model('ripple-carry-contract',frames,'Read carry propagation from the least significant column at the right toward the most significant column at the left. A full-adder block has two operand inputs and one carry input.','Actual question bit patterns. Carry is not signed overflow. The written solution separately handles extension and signedness.')
