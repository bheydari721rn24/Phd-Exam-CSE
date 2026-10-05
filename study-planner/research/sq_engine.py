"""Exact bounded teaching traces; each model has its own stated representation."""
from copy import deepcopy
from fractions import Fraction
from math import comb

def evaluate(mode,p):
 F=[]
 def frame(caption,rows=(),**kw):F.append(dict(caption=caption,rows=[dict(name=n,values=list(v),style=s) for n,v,s in rows],**deepcopy(kw)))
 if mode=='order':
  s=[];q=[];so=[];qo=[];frame('Initially empty; stack bottom-to-top, queue front-to-rear.',[('Stack',s,'stack'),('Queue',q,'row')])
  for op in p['ops']:
   if op.startswith('E:'):x=int(op[2:]);s.append(x);q.append(x)
   else:
    if not s:raise ValueError('Underflow')
    so.append(s.pop());qo.append(q.pop(0))
   frame(op+': each discipline removes its specified live end.',[('Stack',s,'stack'),('Queue',q,'row'),('Stack outputs',so,'row'),('Queue outputs',qo,'row')],n=len(s))
  return dict(mode=mode,frames=F,result=dict(stack=s,queue=q,stackOutput=so,queueOutput=qo))
 if mode=='ring':
  C=p['C'];f=p.get('f',0);v=list(p.get('values',[]));A=[None]*C;n=len(v)
  assert C>=1 and 0<=f<C and n<=C
  for j,x in enumerate(v):A[(f+j)%C]=x
  out=[]
  def add(c):frame(c,[('Logical FIFO order',v,'row'),('Removed values',out,'row')],storage=A,C=C,f=f,n=n,r=(f+n)%C)
  add('Physical slots wrap; count distinguishes empty from full.')
  for op in p['ops']:
   if op.startswith('E:'):
    if n==C:raise ValueError('Ring overflow: no state was changed.')
    x=int(op[2:]);A[(f+n)%C]=x;v.append(x);n+=1
   elif op=='D':
    if n==0:raise ValueError('Ring underflow: no state was changed.')
    out.append(A[f]);assert out[-1]==v.pop(0);A[f]=None;f=(f+1)%C;n-=1
   else:raise ValueError('Use E:value or D.')
   assert [A[(f+j)%C] for j in range(n)]==v
   add(op+': inspect both physical slots and logical order.')
  return dict(mode=mode,frames=F,result=dict(f=f,n=n,r=(f+n)%C,values=v,output=out,storage=A))
 if mode in ['two','two-bad']:
  I=[];O=[];removed=[];seen=[];e=d=t=0
  ops=p.get('ops',['E:1','E:2','D','E:3','BAD','D'])
  def add(c,transfer=False,logical=None):frame(c,[('Input: bottom to top',I,'stack'),('Output: bottom to top',O,'stack'),('Logical queue',logical if logical is not None else O[::-1]+I,'row'),('Removed',removed,'row')],transfer=transfer,e=e,d=d,t=t,cost=e+2*t+d,potential=2*len(I))
  add('Both stacks are empty; initial potential is zero.')
  for op in ops:
   if op.startswith('E:'):x=int(op[2:]);I.append(x);e+=1;seen.append(x);add(op+': append only to input.')
   elif op=='BAD':
    while I:O.append(I.pop());t+=1
    add('Counterexample: newer input moved above a still-pending older output.')
   else:
    if not I and not O:raise ValueError('Queue underflow')
    if not O:
     abstract=I[:]
     while I:
      O.append(I.pop());t+=1;add('Internal transfer checkpoint: public logical order remains fixed; complete transfer before front/removal.',True,abstract)
     add('Complete transfer restores reverse(output) concatenated with input.')
    if op=='D':removed.append(O.pop());d+=1;add('D returns the oldest available output-stack top.')
    elif op=='F':add('F observes '+str(O[-1])+' without removal.')
    else:raise ValueError('Use E:value, D or F.')
  return dict(mode=mode,frames=F,result=dict(I=I,O=O,output=removed,e=e,d=d,t=t,cost=e+2*t+d,queue=O[::-1]+I))
 if mode=='shared':
  C=p['C'];L=p.get('left',[])[:];R=p.get('right',[])[:]
  def add(c):frame(c,[],shared=dict(C=C,L=L,R=R),n=len(L)+len(R))
  add('Left grows rightward; right grows leftward.')
  for op in p['ops']:
   if op.startswith(('L:','R:')):
    if len(L)+len(R)==C:raise ValueError('Shared array overflow')
    (L if op[0]=='L' else R).append(int(op[2:]))
   else:(L if op=='DL' else R).pop()
   add(op+': free interval lies strictly between occupied tops.')
  return dict(mode=mode,frames=F,result=dict(left=L,right=R,free=C-len(L)-len(R)))
 if mode in ['linked','deque']:
  v=list(p.get('values',[]));out=[]
  def add(c):frame(c,[('Removed values',out,'row')],nodes=v,bidirectional=mode=='deque',n=len(v))
  add('Endpoint handles identify the live chain; empty and singleton states are explicit.')
  for op in p['ops']:
   if op.startswith(('E:','ER:')):v.append(int(op.split(':')[1]))
   elif op.startswith('EF:'):v.insert(0,int(op[3:]))
   elif op in ['D','DF']:out.append(v.pop(0))
   elif op=='DR':out.append(v.pop())
   add(op+': reconnect endpoint links and preserve surviving identity order.')
  return dict(mode=mode,frames=F,result=dict(values=v,output=out))
 if mode=='resize':
  C=p['C'];f=p['f'];v=p['values'];N=p['newC'];old=[None]*C;new=[None]*N
  for j,x in enumerate(v):old[(f+j)%C]=x
  frame('Old physical order is different from FIFO order.',[('Old physical slots',old,'indexed'),('New buffer',new,'indexed')],copies=0)
  for j,x in enumerate(v):
   new[j]=old[(f+j)%C];frame(f'Copy logical rank {j} from old slot {(f+j)%C} to new slot {j}.',[('Old physical slots',old,'indexed'),('New buffer',new,'indexed')],copies=j+1)
  frame('Publish new buffer, front zero, count preserved.',[('New physical slots',new,'indexed'),('Logical FIFO order',v,'row')],f=0,n=len(v),r=len(v)%N,copies=len(v))
  return dict(mode=mode,frames=F,result=dict(values=v,copies=len(v),f=0))
 if mode=='restore':
  S=p['values'][:];T=[];C=[];count=0
  def add(c):frame(c,[('Source S',S,'stack'),('Temporary T',T,'stack'),('Copy C',C,'stack')],cost=count)
  add('Source bottom-to-top order is part of the postcondition.')
  while S:T.append(S.pop());count+=2;add('Move one source top to temporary; first reversal.')
  if not p.get('reverseOnly'):
   while T:
    x=T.pop();S.append(x);count+=2
    if p.get('copy'):C.append(x);count+=1
    add('Restore one original identity; optional independent copy receives the same logical value.')
  return dict(mode=mode,frames=F,result=dict(S=S,T=T,C=C,cost=count))
 if mode=='qstack':
  Q=[];out=[];cost=0
  frame('Queue front is the simulated stack top.',[('Queue',Q,'row')],cost=0)
  for x in p['values']:
   old=len(Q);Q.append(x);cost+=1;frame('Append new item at rear.',[('Queue',Q,'row')],cost=cost)
   for _ in range(old):Q.append(Q.pop(0));cost+=2;frame('Rotate one older item behind the new top.',[('Queue',Q,'row')],cost=cost)
  for _ in range(p.get('pops',0)):out.append(Q.pop(0));cost+=1;frame('Remove front, which is newest simulated stack item.',[('Queue',Q,'row'),('Outputs',out,'row')],cost=cost)
  return dict(mode=mode,frames=F,result=dict(values=Q,output=out,cost=cost))
 if mode=='queue-restore':
  Q=p['values'][:];T=[];total=cost=0
  def add(c):frame(c,[('Source queue front to rear',Q,'row'),('Temporary front to rear',T,'row')],cost=cost,total=total)
  add('Drain while accumulating; temporary preserves FIFO orientation.')
  while Q:x=Q.pop(0);T.append(x);total+=x;cost+=2;add('Transfer one front value; partial sum '+str(total)+'.')
  while T:Q.append(T.pop(0));cost+=2;add('Restore one original front value.')
  return dict(mode=mode,frames=F,result=dict(Q=Q,sum=total,cost=cost))
 if mode=='sortedness':
  S=p['values'][:];C=S[:];last=None;weak=strict=True
  frame('A separate preserving container copy is scanned top-to-bottom.',[('Original S',S,'stack'),('Copy C',C,'stack')])
  while C:
   x=C.pop()
   if last is not None:weak=weak and last>=x;strict=strict and last>x
   frame('Pop '+str(x)+'; nondecreasing '+str(weak)+', strictly increasing '+str(strict)+'.',[('Original S',S,'stack'),('Remaining copy',C,'stack')]);last=x
  return dict(mode=mode,frames=F,result=dict(S=S,nondecreasing=weak,strictlyIncreasing=strict))
 if mode=='recursive':
  S=p['values'][:];calls=[];cost=0
  frame('Enter preserving size; every pending frame retains its own removed value.',[('Data stack',S,'stack'),('Pending saved values',calls,'stack')],cost=cost)
  while S:calls.append(S.pop());cost+=1;frame('Pop and create a distinct pending continuation.',[('Data stack',S,'stack'),('Pending saved values',calls,'stack')],cost=cost)
  frame('Empty base call returns zero; maximum call count is n+1.',[('Data stack',S,'stack'),('Pending saved values',calls,'stack')],cost=cost)
  count=0
  while calls:S.append(calls.pop());cost+=1;count+=1;frame('Restore saved value while returning count '+str(count)+'.',[('Data stack',S,'stack'),('Pending saved values',calls,'stack')],cost=cost)
  return dict(mode=mode,frames=F,result=dict(S=S,count=count,cost=cost))
 if mode=='aggregate':
  I=[];O=[]
  def add(c):frame(c,[('Input bottom-to-top',I,'stack'),('Output bottom-to-top',O,'stack'),('Output fold: top-to-bottom',[''.join(O[::-1]) or 'identity'],'row'),('Input fold: bottom-to-top',[''.join(I) or 'identity'],'row'),('Queue fold',[''.join(O[::-1]+I) or 'identity'],'row')])
  add('Concatenation is associative but not commutative.')
  for x in ['a','b']:I.append(x);add('Append '+x+' to the input fold on its right.')
  abstract=''.join(I)
  while I:
   O.append(I.pop());add('Internal transfer; output cache prepends its new top. Do not query a partial public queue.')
  for x in ['c','d']:I.append(x);add('Later arrival '+x+' appends to input; combine output fold before input fold.')
  return dict(mode=mode,frames=F,result=dict(fold=''.join(O[::-1]+I)))
 if mode=='sort':
  S=p['values'][:];T=[];moves=0
  def add(c):frame(c,[('Input S',S,'stack'),('Sorted temporary T',T,'stack')],cost=moves)
  add('Maintain T nondecreasing bottom-to-top; final move reverses its orientation.')
  while S:
   x=S.pop();moves+=1;add('Save removed value '+str(x)+' in a local temporary.')
   while T and T[-1]>x:S.append(T.pop());moves+=2;add('Move an excessive temporary top back to input.')
   T.append(x);moves+=1;add('Insert saved value '+str(x)+' at its sorted temporary position.')
  while T:S.append(T.pop());moves+=2;add('Transfer sorted temporary back; output is nonincreasing bottom-to-top.')
  return dict(mode=mode,frames=F,result=dict(S=S,cost=moves))
 if mode=='permutation':
  target=p['target'];n=len(target);assert sorted(target)==list(range(1,n+1));S=[];a=1;out=[];peak=0;ok=True
  def add(c):frame(c,[('Pending stack',S,'stack'),('Unused inputs',list(range(a,n+1)),'row'),('Outputs',out,'row'),('Target',target,'row')],peak=peak,valid=ok)
  add('Increasing inputs; desired output order is fixed.')
  for x in target:
   while (not S or S[-1]!=x) and a<=n:
    S.append(a);a+=1;peak=max(peak,len(S));add('Forced push before desired output '+str(x)+'.')
   if not S or S[-1]!=x:ok=False;add('Reject: the required value is covered by another top.');break
   out.append(S.pop());add('Pop desired value '+str(x)+'.')
  return dict(mode=mode,frames=F,result=dict(valid=ok,peak=peak,output=out))
 if mode=='catalan':
  n=p['n'];h=p['h'];D=[[0]*(n+1) for _ in range(n+1)];D[0][0]=1
  frame('Count only cells with 0 <= pushes - pops <= capacity.',[],grid=D,p=0,d=0,n=n,h=h)
  for total in range(2*n+1):
   for a in range(n+1):
    b=total-a
    if b<0 or b>a or b>n or a-b>h or not D[a][b]:continue
    if a<n and a-b<h:D[a+1][b]+=D[a][b]
    if b<a:D[a][b+1]+=D[a][b]
    frame(f'Propagate {D[a][b]} histories from pushes {a}, pops {b}; reject negative or excessive height.',[],grid=D,p=a,d=b,n=n,h=h)
  return dict(mode=mode,frames=F,result=dict(count=D[n][n]))
 if mode=='brackets':
  S=[];ok=True;error=None;tokens=p['tokens'];frame('Store unmatched opening types.',[('Openings',S,'stack'),('Tokens',tokens,'row')])
  for i,x in enumerate(tokens):
   if x in '([{':S.append(x)
   elif x in ')]}':
    if not S or S[-1]!='([{'[')]}'.index(x)]:ok=False;error=i;frame('Type mismatch or empty opening stack; stop.',[('Openings',S,'stack'),('Tokens',tokens,'row')],at=i,valid=False);break
    S.pop()
   else:raise ValueError('Only bracket tokens are supported.')
   frame('Token '+str(i+1)+': newest unmatched opener determines the only legal closer.',[('Openings',S,'stack'),('Tokens',tokens,'row')],at=i,valid=True)
  if S and ok:ok=False;error=len(tokens);frame('End rejects unclosed openings.',[('Openings',S,'stack')],valid=False)
  return dict(mode=mode,frames=F,result=dict(valid=ok,errorIndex=error))
 if mode=='postfix':
  S=[];tokens=p['tokens'];ok=True;err=None;frame('Operands are exact rational numbers; tokens are space-separated.',[('Values',S,'stack'),('Tokens',tokens,'row')])
  for i,x in enumerate(tokens):
   if x in ['+','-','*','/']:
    if len(S)<2:ok=False;err='Arity underflow';break
    b=S.pop();a=S.pop()
    if x=='/' and b==0:ok=False;err='Division by zero';break
    y={'+':lambda:a+b,'-':lambda:a-b,'*':lambda:a*b,'/':lambda:a/b}[x]();S.append(y);c=f'Apply {a} {x} {b}; right operand was popped first.'
   else:
    try:S.append(Fraction(x));c='Push operand '+x+'.'
    except (ValueError,ZeroDivisionError):ok=False;err='Unknown operand';break
   frame(c,[('Values',[str(z) for z in S],'stack'),('Tokens',tokens,'row')],at=i)
  if ok and len(S)!=1:ok=False;err='Exactly one final value is required'
  if not ok:frame('Reject: '+err+'.',[('Values',[str(z) for z in S],'stack')],valid=False)
  return dict(mode=mode,frames=F,result=dict(valid=ok,value=str(S[0]) if ok else None,error=err))
 if mode=='infix':
  S=[];O=[];tokens=p['tokens'];prec={'+':1,'-':1,'*':2,'/':2,'^':3};frame('Operator stack and postfix output have distinct roles.',[('Operators',S,'stack'),('Output',O,'row')])
  for x in tokens:
   if x=='(':S.append(x)
   elif x==')':
    while S and S[-1]!='(':O.append(S.pop())
    if not S:raise ValueError('Unmatched close')
    S.pop()
   elif x in prec:
    while S and S[-1]!='(' and (prec[S[-1]]>prec[x] or prec[S[-1]]==prec[x] and x!='^'):O.append(S.pop())
    S.append(x)
   else:O.append(x)
   frame('Read '+x+': respect precedence and incoming associativity.',[('Operators',S,'stack'),('Output',O,'row')])
  while S:
   if S[-1]=='(':raise ValueError('Unmatched open')
   O.append(S.pop());frame('Drain one completed operator.',[('Operators',S,'stack'),('Output',O,'row')])
  return dict(mode=mode,frames=F,result=dict(postfix=O))
 if mode=='extrema':
  S=[];M=[];frame('One prefix maximum is stored per live data item.',[('Values',S,'stack'),('Prefix maxima',M,'stack')])
  for x in p['values']:S.append(x);M.append(max(x,M[-1]) if M else x);frame('Push '+str(x)+' and its prefix maximum.',[('Values',S,'stack'),('Prefix maxima',M,'stack')])
  for _ in range(p.get('pops',0)):x=S.pop();M.pop();frame('Pop '+str(x)+'; surviving cached maximum is restored.',[('Values',S,'stack'),('Prefix maxima',M,'stack')])
  return dict(mode=mode,frames=F,result=dict(values=S,max=M[-1] if M else None))
 if mode in ['monostack','histogram','window','dominated']:
  A=p['values'];S=[];ans=[None]*len(A);outs=[];best=0;added=removed=0;k=p.get('k',1)
  if mode=='window' and not 1<=k<=len(A):raise ValueError('Window must fit the nonempty input.')
  def add(c,i=-1,rect=None):frame(c,[('Input values',A,'indexed'),('Candidate indices',S,'row'),('Candidate values',[A[j] for j in S],'row'),('Answers',ans if mode=='monostack' else outs,'row')],at=i,best=best,added=added,removed=removed,rect=rect,bars=A if mode=='histogram' else None)
  add('Candidate identities and values are distinct; indices preserve boundaries.')
  for i,x in enumerate(A+([0] if mode=='histogram' else [])):
   if mode=='window':
    while S and S[0]<=i-k:S.pop(0);removed+=1;add('Expire a candidate by index age.',i)
   def needs():
    if not S:return False
    if mode=='monostack':return x>=A[S[-1]] if p.get('equal') else x>A[S[-1]]
    if mode=='histogram':return x<A[S[-1]]
    if mode=='window':return A[S[-1]]<=x
    return A[S[-1]]>x
   while needs():
    j=S.pop();removed+=1
    if mode=='monostack':ans[j]=i;add(f'Resolve index {j}: first qualifying index is {i}.',i)
    elif mode=='histogram':
     left=S[-1] if S else -1;width=i-left-1;area=A[j]*width;best=max(best,area);add(f'Pop height {A[j]}: width {width}, area {area}; best {best}.',i,dict(left=left+1,right=i-1,height=A[j],area=area))
    else:add('Remove a rear candidate dominated by the new arrival.',i)
   if i<len(A):S.append(i);added+=1;add('Append current index to the maintained candidate sequence.',i)
   if mode=='window' and i>=k-1:outs.append(A[S[0]]);add('Front gives this completed window maximum.',i)
  if mode=='histogram':
   while S:S.pop();removed+=1;add('Flush remaining zero-height candidate; area stays zero.',len(A))
  return dict(mode=mode,frames=F,result=dict(answers=ans if mode=='monostack' else outs,candidates=S,best=best,added=added,removed=removed))
 if mode=='josephus':
  v=list(range(1,p['n']+1));out=[];frame('Front is next person counted as one.',[('Survivors',v,'row'),('Eliminated',out,'row')])
  while v:
   r=(p['k']-1)%len(v)
   for _ in range(r):v.append(v.pop(0));frame('Rotate one person; continue cyclic counting.',[('Survivors',v,'row'),('Eliminated',out,'row')])
   out.append(v.pop(0));frame('Remove the kth current person.',[('Survivors',v,'row'),('Eliminated',out,'row')])
  return dict(mode=mode,frames=F,result=dict(order=out,survivor=out[-1]))
 if mode=='worklist':
  frame('Same rooted tree; different pending-work disciplines.',[('FIFO frontier',['B','C'],'row'),('LIFO frontier',['C','B'],'stack'),('FIFO visited',['A'],'row'),('LIFO visited',['A'],'row')],tree=True)
  frame('FIFO exposes the earlier discovered sibling before the deeper child.',[('FIFO frontier',['C','D'],'row'),('LIFO frontier',['C','D'],'stack'),('FIFO visited',['A','B'],'row'),('LIFO visited',['A','B'],'row')],tree=True)
  frame('FIFO completes layers; LIFO finishes the left branch first.',[('FIFO visited',['A','B','C','D','E'],'row'),('LIFO visited',['A','B','D','C','E'],'row')],tree=True)
  return dict(mode=mode,frames=F,result=dict(fifo=['A','B','C','D','E'],lifo=['A','B','D','C','E']))
 raise ValueError('Unsupported model mode '+mode)
